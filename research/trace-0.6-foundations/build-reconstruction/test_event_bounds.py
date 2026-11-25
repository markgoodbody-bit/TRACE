import json
import subprocess
import sys
import unittest
from itertools import product
from pathlib import Path

from event_bounds import event_bounds


def guide_booking():
    return {
        "clock": "minutes after 17:00", "events": ["answer", "desk", "booking", "kit"],
        "links": [["answer", "desk", 4], ["desk", "booking", 2], ["booking", "kit", 10]],
        "deadlines": [["booking", 20, "before"], ["kit", 30, "by"]],
        "check": {"event": "answer", "at": 14},
    }


class EventBoundsTests(unittest.TestCase):
    def test_tied_cutoffs_differ_at_equality_and_give_the_source_path(self):
        plan = guide_booking()
        result = event_bounds(plan)
        self.assertEqual(result["bounds"]["answer"], {"at": 14, "relation": "before"})
        self.assertEqual(result["check"],
                         {"event": "answer", "at": 14, "within_bound": False,
                          "link_indices": [0, 1], "deadline_index": 0})
        plan["check"]["at"] = 13
        self.assertTrue(event_bounds(plan)["check"]["within_bound"])
        plan["deadlines"].pop(0)
        plan["check"]["at"] = 14
        by = event_bounds(plan)
        self.assertTrue(by["check"]["within_bound"])
        self.assertEqual(by["check"]["link_indices"], [0, 1, 2])
        self.assertEqual(by["bounds"]["answer"], {"at": 14, "relation": "by"})

    def test_missing_deadline_repeated_link_and_unconnected_events(self):
        plan = guide_booking()
        plan["events"].append("another activity")
        plan["links"].append(["answer", "desk", 24])
        result = event_bounds(plan)
        self.assertEqual(result["bounds"]["answer"], {"at": -6, "relation": "before"})
        self.assertEqual(result["check"]["link_indices"], [3, 1])
        plan["check"] = {"event": "another activity", "at": 999}
        check = event_bounds(plan)["check"]
        self.assertIsNone(check["within_bound"])
        self.assertIsNone(check["deadline_index"])
        self.assertEqual(check["link_indices"], [])

    def test_bounds_match_every_path_to_every_deadline(self):
        events = ["a", "b", "c"]
        candidates = [("a", "b"), ("a", "c"), ("b", "c")]
        for lags in product((None, 0, 2), repeat=3):
            links = [[s, t, lag] for (s, t), lag in zip(candidates, lags) if lag is not None]
            for relations in product((None, "before", "by"), repeat=3):
                deadlines = [[e, 5 + i, rel] for i, (e, rel) in enumerate(zip(events, relations)) if rel]
                plan = {"clock": "synthetic ticks", "events": events, "links": links, "deadlines": deadlines}
                result = event_bounds(plan)
                for start in events:
                    paths = [(start, 0)]
                    limits = []
                    while paths:
                        node, lag = paths.pop()
                        limits.extend((at - lag, rel == "by") for e, at, rel in deadlines if node == e)
                        paths.extend((t, lag + extra) for s, t, extra in links if node == s)
                    expected = None
                    if limits:
                        bound, inclusive = min(limits)
                        expected = {"at": bound, "relation": "by" if inclusive else "before"}
                    self.assertEqual(result["bounds"][start], expected, (plan, start))

    def test_bad_references_cycles_and_unsupported_clock_inputs(self):
        invalid = [
            ("events", ["answer", "desk", "answer"]), ("clock", ""), ("links", None),
            ("links", [["x", "kit", 3]]), ("links", [["kit", "kit", 0]]),
            ("links", [["kit", "answer", -1]]), ("links", [["kit", "answer", True]]),
            ("deadlines", [["kit", 30, "maybe"]]), ("deadlines", [["kit", False, "by"]]),
            ("deadlines", [["x", 30, "before"]]), ("check", {"event": "missing", "at": 0}),
            ("check", {"event": "answer", "at": 0, "clock": "elsewhere"}),
        ]
        for key, value in invalid:
            plan = guide_booking()
            plan[key] = value
            with self.subTest(key=key, value=value), self.assertRaises(ValueError):
                event_bounds(plan)

    def test_simulator_stdin_uses_the_same_calculation(self):
        run = subprocess.run([sys.executable, str(Path(__file__).with_name("simulator.py")),
                              "--deadlines", "-"], text=True, input=json.dumps(guide_booking()),
                             capture_output=True)
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertEqual(json.loads(run.stdout), event_bounds(guide_booking()))
