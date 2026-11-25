import json
import subprocess
import sys
import unittest
from itertools import combinations, permutations, product
from pathlib import Path

import choice_history


def row(chosen, *others):
    return {"chosen": chosen, "usable": [chosen, *others]}


def brute_force(history, menu, first, last, orders):
    """Try each split and all whole rankings on each side, independently of the solver."""
    def fits(order, segment):
        return all(min(item["usable"], key=order.index) == item["chosen"] for item in segment)

    winners = {}
    for split in range(first, last + 1):
        if not any(fits(order, history[:split]) for order in orders):
            continue
        current_orders = [order for order in orders if fits(order, history[split:])]
        if current_orders:
            winners[split] = {min(menu, key=order.index) for order in current_orders} if menu else set()
    return winners


class ChangeWindowTests(unittest.TestCase):
    def run_window(self, history, menu, first, last, **kwargs):
        return choice_history.choices_across_change(
            history, menu, {"earliest": first, "latest": last}, **kwargs)

    def test_later_aim_reopens_the_guide_and_keeps_declining_available(self):
        history = [row("repair", "teach"), row("teach", "guide")]
        menu = ["teach", "guide", "decline"]
        result = self.run_window(history, menu, 1, 2, explain="guide")
        self.assertEqual(result["compatible_boundaries"], {"earliest": 1, "latest": 2})
        self.assertEqual(result["possible_at_some_boundary"], menu)
        self.assertEqual(result["possible_at_every_boundary"], ["teach", "decline"])
        early = result["witnesses"]["earliest"]
        self.assertEqual(early["steps"], [{"history_index": 1, "chosen": "teach", "over": "guide"}])
        late = result["witnesses"]["latest"]
        self.assertEqual(next(x for x in late["example_ranking"] if x in menu), "guide")
        self.assertEqual(choice_history.possible_choices(history, menu)["possible_next_choices"],
                         ["teach", "decline"])

    def test_only_one_split_survives_when_both_sides_are_checked(self):
        history = [row("a", "b"), row("b", "a")]
        result = self.run_window(history, ["a", "b"], 0, 2)
        self.assertEqual(result["compatible_boundaries"], {"earliest": 1, "latest": 1})
        self.assertEqual(result["possible_at_some_boundary"], ["b"])
        self.assertEqual(result["possible_at_every_boundary"], ["b"])
        # Discarding all old choices at the last boundary would hide a contradiction.
        self.assertEqual(self.run_window(history, ["c"], 2, 2)["status"], "inconsistent")

    def test_no_split_yields_source_rows_covering_every_allowed_boundary(self):
        history = [row("a", "b"), row("b", "a"), row("a", "b"), row("b", "a")]
        result = self.run_window(history, ["z"], 0, 4)
        self.assertEqual(result["status"], "inconsistent")
        self.assertEqual({(c["segment"], c["boundary"]) for c in result["conflicts"]},
                         {("before", 2), ("after", 2)})
        for conflict in result["conflicts"]:
            steps = conflict["steps"]
            self.assertEqual([s["over"] for s in steps],
                             [s["chosen"] for s in steps[1:] + steps[:1]])
            for s in steps:
                idx = s["history_index"]
                self.assertEqual(idx < conflict["boundary"], conflict["segment"] == "before")
                self.assertEqual(history[idx]["chosen"], s["chosen"])
                self.assertIn(s["over"], history[idx]["usable"])
        self.assertNotIn("possible_at_some_boundary", result)

    def test_empty_endpoints_and_original_witness_positions(self):
        for menu in ([], ["x", "x", "w"]):
            result = self.run_window([], menu, 0, 0)
            self.assertEqual(result["possible_at_some_boundary"], list(dict.fromkeys(menu)))
        history = [row("b", "c"), row("a", "b"), row("b", "c")]
        result = self.run_window(history, ["a", "c"], 1, 1, explain="c")
        self.assertEqual([s["history_index"] for s in result["witnesses"]["earliest"]["steps"]],
                         [1, 2])
        self.assertEqual(result["witnesses"]["latest"], result["witnesses"]["earliest"])
        self.assertEqual(self.run_window(history, ["a", "c"], 3, 3)["possible_at_every_boundary"],
                         ["a", "c"])

    def test_invalid_windows_rows_and_queries_fail_even_outside_the_active_segment(self):
        for window in (None, [], {}, {"earliest": False, "latest": 0},
                       {"earliest": 0, "latest": 1.0}, {"earliest": -1, "latest": 0},
                       {"earliest": 1, "latest": 0}, {"earliest": 0, "latest": 2},
                       {"earliest": 0, "latest": 1, "guess": True}):
            with self.subTest(window=window), self.assertRaises(ValueError):
                choice_history.choices_across_change([row("a")], ["a"], window)
        with self.assertRaises(ValueError):
            self.run_window([{"chosen": "x", "usable": ["b"]}], ["a"], 1, 1)
        with self.assertRaises(ValueError):
            self.run_window([row("a")], ["a"], 0, 1, explain="b")
        with self.assertRaises(ValueError):
            self.run_window(None, [], 0, 0)

    def test_exhaustive_small_histories_against_independent_orders(self):
        options = ("a", "b", "c")
        observations = [row(a, b) for a, b in permutations(options, 2)]
        orders = list(permutations(options))
        menus = [list(m) for k in range(4) for m in combinations(options, k)]
        for history in product(observations, repeat=2):
            for first in range(3):
                for last in range(first, 3):
                    for menu in menus:
                        expected = brute_force(history, menu, first, last, orders)
                        result = self.run_window(history, menu, first, last)
                        with self.subTest(history=history, menu=menu, first=first, last=last):
                            if not expected:
                                self.assertEqual(result["status"], "inconsistent")
                                continue
                            self.assertEqual(result["compatible_boundaries"],
                                             {"earliest": min(expected), "latest": max(expected)})
                            self.assertEqual(set(expected), set(range(min(expected), max(expected) + 1)))
                            self.assertEqual(result["possible_at_some_boundary"],
                                             [x for x in menu if any(x in s for s in expected.values())])
                            self.assertEqual(result["possible_at_every_boundary"],
                                             [x for x in menu if all(x in s for s in expected.values())])

    def test_documented_request_through_the_cli_and_mixed_queries(self):
        script = Path(choice_history.__file__)
        request = {"history": [row("repair", "teach"), row("teach", "guide")],
                   "usable_next": ["teach", "guide", "decline"],
                   "change_window": {"earliest": 1, "latest": 2}, "explain": "guide"}
        def invoke(data):
            return subprocess.run([sys.executable, str(script), "--stdin"], input=json.dumps(data),
                                  capture_output=True, text=True)
        completed = invoke(request)
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertEqual(json.loads(completed.stdout), self.run_window(
            request["history"], request["usable_next"], 1, 2, explain="guide"))
        request["check_availability"] = {"history_index": 1, "options": ["guide"]}
        mixed = invoke(request)
        self.assertNotEqual(mixed.returncode, 0)
        self.assertIn("complete historical menus", mixed.stderr)
