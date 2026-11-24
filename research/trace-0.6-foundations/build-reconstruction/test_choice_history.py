import json
import subprocess
import sys
import unittest
from itertools import combinations, permutations, product
from pathlib import Path

from choice_history import BRAKES, OPTIONS, PUNCTURES, compare, compare_availability, possible_choices


class ChoiceHistoryTests(unittest.TestCase):
    def test_same_observed_choice_warrants_different_accounts(self):
        open_menu = compare(OPTIONS, PUNCTURES, OPTIONS)
        restricted_menu = compare((PUNCTURES,), PUNCTURES, OPTIONS)
        self.assertEqual(open_menu["observed_choice"], restricted_menu["observed_choice"])
        self.assertEqual(open_menu["compatible_rankings"], [[PUNCTURES, BRAKES]])
        self.assertEqual(open_menu["possible_next_choices"], [PUNCTURES])
        self.assertEqual(len(restricted_menu["compatible_rankings"]), 2)
        self.assertCountEqual(restricted_menu["possible_next_choices"], OPTIONS)

    def test_display_without_support_leaves_the_usable_menu_restricted(self):
        result = compare((PUNCTURES,), PUNCTURES, (PUNCTURES,))
        self.assertEqual(len(result["compatible_rankings"]), 2)
        self.assertEqual(result["possible_next_choices"], [PUNCTURES])

    def test_unknown_options_and_impossible_observations_are_rejected(self):
        with self.assertRaises(ValueError):
            compare((PUNCTURES,), BRAKES, OPTIONS)
        with self.assertRaises(ValueError):
            compare(OPTIONS, PUNCTURES, ("unmodelled option",))


class PossibleChoiceTests(unittest.TestCase):
    def test_paths_through_unavailable_options_and_an_uncompared_offer(self):
        history = [{"usable": ["a", "b"], "chosen": "a"},
                   {"usable": ["b", "c"], "chosen": "b"}]
        self.assertEqual(possible_choices(history, ["d", "c", "a", "d"]),
                         {"status": "compatible", "possible_next_choices": ["d", "a"]})

    def test_a_withdrawn_option_remains_possible_when_it_returns(self):
        for original_menu in ([PUNCTURES], list(OPTIONS)):
            observed = [{"usable": original_menu, "chosen": PUNCTURES}]
            result = possible_choices(observed, list(OPTIONS))
            baseline = compare(original_menu, PUNCTURES, OPTIONS)
            self.assertCountEqual(result["possible_next_choices"], baseline["possible_next_choices"])

    def test_a_cycle_is_reported_even_outside_the_next_menu(self):
        history = [{"usable": [winner, loser], "chosen": winner}
                   for winner, loser in [("a", "b"), ("b", "c"), ("c", "a")]]
        result = possible_choices(history, ["d"])
        self.assertEqual(result["status"], "inconsistent")
        cycle = result["cycle"]
        self.assertEqual(cycle[0], cycle[-1])
        self.assertEqual(set(zip(cycle, cycle[1:])), {("a", "b"), ("b", "c"), ("c", "a")})

    def test_empty_and_unsupplied_menus_differ(self):
        self.assertEqual(possible_choices([], []), {"status": "compatible", "possible_next_choices": []})
        self.assertEqual(possible_choices([], ["b", "a"])["possible_next_choices"], ["b", "a"])
        for history, future in (([], None), ([], "abc"), (None, []),
                                ([{"chosen": "a"}], []), ([{"usable": [], "chosen": "a"}], []),
                                ([{"usable": ["a", None], "chosen": "a"}], [])):
            with self.subTest(history=history, future=future), self.assertRaises(ValueError):
                possible_choices(history, future)

    def test_matches_all_total_orders_on_three_options(self):
        options = ("a", "b", "c")
        menus = [menu for size in range(4) for menu in combinations(options, size)]
        observations = [{"usable": menu, "chosen": chosen} for menu in menus for chosen in menu]
        orders = list(permutations(options))
        for length in range(4):
            for history in product(observations, repeat=length):
                compatible = [order for order in orders if all(
                    min(row["usable"], key=order.index) == row["chosen"] for row in history)]
                for future in menus:
                    result = possible_choices(history, future)
                    if compatible:
                        winners = {min(future, key=order.index) for order in compatible} if future else set()
                        expected = [option for option in future if option in winners]
                        self.assertEqual(result, {"status": "compatible", "possible_next_choices": expected},
                                         (history, future))
                    else:
                        self.assertEqual(result["status"], "inconsistent", (history, future))


class ChoiceWitnessTests(unittest.TestCase):
    def assert_recorded_path(self, witness, history):
        steps = witness["steps"]
        self.assertTrue(steps)
        path = [steps[0]["chosen"]]
        for step in steps:
            self.assertGreaterEqual(step["history_index"], 0)
            row = history[step["history_index"]]
            self.assertEqual(path[-1], step["chosen"])
            self.assertEqual(row["chosen"], step["chosen"])
            self.assertIn(step["over"], row["usable"])
            self.assertNotEqual(step["over"], step["chosen"])
            path.append(step["over"])
        return path

    def test_exclusion_uses_the_shortest_chain_and_first_supporting_record(self):
        edges = [("r", "x"), ("x", "y"), ("y", "brakes"),
                 ("wheel", "brakes"), ("puncture", "wheel"), ("puncture", "wheel")]
        history = [{"chosen": winner, "usable": [winner, other]} for winner, other in edges]
        result = possible_choices(history, ["r", "puncture", "brakes"], explain="brakes")
        self.assertEqual(result["witness"], {
            "kind": "excluded", "option": "brakes", "steps": [
                {"history_index": 4, "chosen": "puncture", "over": "wheel"},
                {"history_index": 3, "chosen": "wheel", "over": "brakes"},
            ]})
        history[3]["usable"] = ["wheel"]
        remaining = possible_choices(history, ["r", "puncture", "brakes"], explain="brakes")
        self.assertEqual([step["history_index"] for step in remaining["witness"]["steps"]],
                         [0, 1, 2])

    def test_corrected_menu_reopens_a_choice_without_erasing_the_recorded_choice(self):
        history = [{"usable": ["puncture", "wheel"], "chosen": "puncture"},
                   {"usable": ["wheel", "brakes"], "chosen": "wheel"}]
        future = ["puncture", "brakes", "decline"]
        before = possible_choices(history, future, explain="brakes")
        self.assertEqual(before["possible_next_choices"], ["puncture", "decline"])
        history[1] = {"usable": ["wheel"], "chosen": "wheel"}
        after = possible_choices(history, future, explain="brakes")
        self.assertEqual(after["possible_next_choices"], future)
        witness = after["witness"]
        self.assertEqual((witness["kind"], witness["option"]), ("possible", "brakes"))
        ranking = witness["example_ranking"]
        self.assertCountEqual(ranking, ["puncture", "brakes", "decline", "wheel"])
        self.assertEqual(min(future, key=ranking.index), "brakes")
        for row in history:
            self.assertEqual(min(row["usable"], key=ranking.index), row["chosen"])

    def test_ranking_places_past_prerequisites_first_and_keeps_their_other_descendants(self):
        history = [{"usable": ["old", "mid", "other"], "chosen": "old"},
                   {"usable": ["mid", "target", "other"], "chosen": "mid"}]
        future = ["other", "target", "new"]
        ranking = possible_choices(history, future, explain="target")["witness"]["example_ranking"]
        self.assertCountEqual(ranking, ["old", "mid", "other", "target", "new"])
        self.assertEqual(min(future, key=ranking.index), "target")
        for row in history:
            self.assertEqual(min(row["usable"], key=ranking.index), row["chosen"])

    def test_contradiction_outside_menu_links_each_edge_to_an_observation(self):
        edges = [("u", "v"), ("v", "w"), ("w", "u")]
        history = [{"chosen": winner, "usable": [winner, other]} for winner, other in edges]
        result = possible_choices(history, ["new"], explain="new")
        self.assertEqual(result["status"], "inconsistent")
        self.assertEqual(result["witness"]["kind"], "inconsistent_history")
        steps = result["witness"]["steps"]
        self.assertCountEqual([s["history_index"] for s in steps], [0, 1, 2])
        self.assertEqual([(s["chosen"], s["over"]) for s in steps],
                         list(zip(result["cycle"], result["cycle"][1:])))
        for step in steps:
            self.assertEqual(edges[step["history_index"]], (step["chosen"], step["over"]))

    def test_explanation_names_a_member_of_the_next_usable_menu(self):
        for target in ("unavailable", "", ["a"]):
            with self.subTest(target=target), self.assertRaises(ValueError):
                possible_choices([], ["a"], explain=target)

    def test_json_entry_point_returns_a_witness_on_request(self):
        request = {"history": [], "usable_next": ["a", "b"], "explain": "b"}
        completed = subprocess.run(
            [sys.executable, str(Path(__file__).with_name("choice_history.py")), "--stdin"],
            input=json.dumps(request), text=True, capture_output=True, check=True)
        result = json.loads(completed.stdout)
        self.assertEqual(result["possible_next_choices"], ["a", "b"])
        self.assertEqual(result["witness"]["example_ranking"], ["b", "a"])

    def test_witnesses_against_all_four_option_comparison_graphs(self):
        options = ("a", "b", "c", "d")
        edges = list(permutations(options, 2))
        orders = list(permutations(options))
        menus = [menu for size in range(1, 5) for menu in combinations(options, size)]
        paths = [path for size in range(2, 5) for path in permutations(options, size)]
        for mask in range(1 << len(edges)):
            observed = [edge for bit, edge in enumerate(edges) if mask & (1 << bit)]
            history = [{"chosen": x, "usable": [x, y]} for x, y in observed]
            compatible = [order for order in orders
                          if all(order.index(x) < order.index(y) for x, y in observed)]
            if not compatible:
                result = possible_choices(history, ["new"], explain="new")
                self.assertEqual(result["status"], "inconsistent")
                cycle = self.assert_recorded_path(result["witness"], history)
                self.assertEqual(cycle, result["cycle"])
                self.assertEqual(cycle[0], cycle[-1])
                continue

            supported_paths = [path for path in paths
                               if all(edge in observed for edge in zip(path, path[1:]))]
            seen = {option for edge in observed for option in edge}
            for menu in menus:
                winners = {min(menu, key=order.index) for order in compatible}
                for target in menu:
                    result = possible_choices(history, menu, explain=target)
                    self.assertEqual(set(result["possible_next_choices"]), winners)
                    witness = result["witness"]
                    if target in winners:
                        self.assertEqual(witness["kind"], "possible")
                        rank = witness["example_ranking"]
                        self.assertCountEqual(rank, seen.union(menu))
                        self.assertEqual(min(menu, key=rank.index), target)
                        self.assertTrue(all(rank.index(x) < rank.index(y) for x, y in observed))
                    else:
                        self.assertEqual(witness["kind"], "excluded")
                        path = self.assert_recorded_path(witness, history)
                        rivals = [p for p in supported_paths if p[0] in menu and p[-1] == target]
                        self.assertIn(tuple(path), rivals)
                        self.assertEqual(len(path), min(map(len, rivals)))


class DisputedAvailabilityTests(unittest.TestCase):
    def test_one_entry_can_change_the_possible_choices_without_editing_the_input(self):
        history = [{"usable": ["puncture", "wheel"], "chosen": "puncture"},
                   {"usable": ["wheel", "brakes"], "chosen": "wheel"}]
        original = json.loads(json.dumps(history))
        future = ["puncture", "brakes", "decline"]
        disputed = {"history_index": 1, "option": "brakes"}
        result = compare_availability(history, future, disputed, explain="brakes")
        self.assertEqual(history, original)
        self.assertEqual(result["check_availability"], disputed)
        self.assertEqual(result["if_usable"]["possible_next_choices"], ["puncture", "decline"])
        self.assertEqual(result["if_usable"]["witness"]["kind"], "excluded")
        self.assertEqual(result["if_unusable"]["possible_next_choices"], future)
        self.assertEqual(result["if_unusable"]["witness"]["kind"], "possible")

    def test_another_observation_can_still_support_the_same_comparison(self):
        history = [{"usable": ["puncture", "brakes"], "chosen": "puncture"}] * 2
        result = compare_availability(history, ["puncture", "brakes"],
                                      {"history_index": 0, "option": "brakes"}, explain="brakes")
        for branch, row in (("if_usable", 0), ("if_unusable", 1)):
            self.assertEqual(result[branch]["possible_next_choices"], ["puncture"])
            self.assertEqual(result[branch]["witness"]["steps"][0]["history_index"], row)

    def test_removing_one_entry_can_restore_consistency(self):
        history = [{"usable": ["a", "b"], "chosen": "a"},
                   {"usable": ["a", "b"], "chosen": "b"}]
        result = compare_availability(history, ["a", "b"],
                                      {"history_index": 1, "option": "a"}, explain="b")
        self.assertEqual(result["if_usable"]["status"], "inconsistent")
        self.assertCountEqual([s["history_index"] for s in result["if_usable"]["witness"]["steps"]],
                         [0, 1])
        self.assertEqual(result["if_unusable"]["possible_next_choices"], ["a"])

    def test_check_requires_a_real_row_and_an_unchosen_recorded_option(self):
        history = [{"usable": ["a", "b"], "chosen": "a"}]
        for disputed in (None, {"option": "b"}, {"history_index": True, "option": "b"},
                         {"history_index": -1, "option": "b"}, {"history_index": 1, "option": "b"},
                         {"history_index": 0, "option": "a"}, {"history_index": 0, "option": "c"}):
            with self.subTest(disputed=disputed), self.assertRaises(ValueError):
                compare_availability(history, ["a", "b"], disputed)

    def test_json_entry_point_returns_both_conditions(self):
        request = {
            "history": [{"usable": ["a", "b"], "chosen": "a"}],
            "usable_next": ["a", "b"],
            "check_availability": {"history_index": 0, "option": "b"},
        }
        completed = subprocess.run(
            [sys.executable, str(Path(__file__).with_name("choice_history.py")), "--stdin"],
            input=json.dumps(request), text=True, capture_output=True, check=True)
        self.assertEqual(json.loads(completed.stdout), {
            "check_availability": request["check_availability"],
            "if_usable": {"status": "compatible", "possible_next_choices": ["a"]},
            "if_unusable": {"status": "compatible", "possible_next_choices": ["a", "b"]},
        })


if __name__ == "__main__":
    unittest.main()
