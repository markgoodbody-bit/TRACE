import unittest
from itertools import combinations, permutations, product

from choice_history import BRAKES, OPTIONS, PUNCTURES, compare, possible_choices


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


if __name__ == "__main__":
    unittest.main()
