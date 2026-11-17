import itertools
import unittest
from fractions import Fraction
import build_views
import simulator


def distribution():
    return [{"direct": d, "f1": a, "f2": b,
             "prob": str((Fraction(18, 25) if d else Fraction(7, 25)) / 4)}
            for d, a, b in itertools.product((False, True), repeat=3)]


class LaboratoryTests(unittest.TestCase):
    def test_partition_is_byte_complete_and_adjacent(self):
        raw = build_views.SOURCE.read_bytes()
        units = build_views.partition(raw)
        lines = raw.decode("utf8").splitlines(keepends=True)
        self.assertEqual(units[0]["start_line"], 1)
        self.assertEqual(units[-1]["end_line"], len(lines))
        self.assertTrue(all(a["end_line"] + 1 == b["start_line"] for a, b in zip(units, units[1:])))
        self.assertTrue(all(x["status"] == "UNRESOLVED" and x["proposed_candidate_sections"] for x in units))
        self.assertEqual(build_views.digest(raw), build_views.SOURCE_SHA256)

    def test_early_late_and_capacity(self):
        rows = distribution()
        self.assertEqual(simulator.support(rows, "early", 2)["success"], "79/100")
        self.assertEqual(simulator.support(rows, "late", 2)["success"], "18/25")
        self.assertEqual(simulator.support(rows, "early", 1)["success"], "18/25")

    def test_positive_cooperation_requires_both(self):
        world = [{"direct": False, "f1": True, "f2": True, "prob": "1"}]
        self.assertEqual(simulator.support(world, "early", 2)["success"], "1")
        self.assertEqual(simulator.support(world, "early", 1)["success"], "0")

    def test_controlled_observation_and_fallback(self):
        rows = [{"direct": d, "f1": True, "f2": b,
                 "prob": str(Fraction(1, 2) * (Fraction(3, 4) if b else Fraction(1, 4)))}
                for d, b in itertools.product((False, True), repeat=2)]
        scenario = {"worlds": rows, "observation_time": 4, "action_deadline": 5,
                    "capacity": 2, "fallback_units": 2}
        self.assertEqual(simulator.simulate_scenario(scenario)["result"]["success"], "7/8")
        scenario["observation_time"] = 6
        self.assertEqual(simulator.simulate_scenario(scenario)["result"]["success"], "3/4")
        scenario["observation_time"] = 5
        self.assertEqual(simulator.simulate_scenario(scenario)["result"]["success"], "7/8")

    def test_no_joint_law_or_extra_field_is_not_guessed(self):
        with self.assertRaises(ValueError):
            simulator.simulate_scenario({"marginals": [0.9, 0.8]})

    def test_unknown_and_temporal_boundaries(self):
        self.assertFalse(simulator.before_hardening(5, 5))
        self.assertTrue(simulator.delivered_by_due(5, 5))
        self.assertEqual(simulator.unknown_conditions("yes", "unknown")["delivery"], "unknown")
        self.assertEqual(simulator.unknown_conditions("yes", "unknown")["authorization"], "UNASSESSED")

    def test_reject_incomplete_or_invalid_joint_law(self):
        with self.assertRaises(ValueError):
            simulator.support([], "early", 2)
        with self.assertRaises(ValueError):
            simulator.support([{"direct": True, "f1": True, "f2": True, "prob": "3/2"}], "early", 2)
        with self.assertRaises(ValueError):
            simulator.support(distribution(), "unspecified", 2)

    def test_spine_is_derived_and_flags_unknown(self):
        spine = build_views.render_spine(build_views.CANDIDATE.read_text(encoding="utf8"))
        self.assertIn("UNRESOLVED", spine)
        self.assertIn("co-evolving worked case", spine)
        self.assertIn("## 3. Offers, duties and power", spine)


if __name__ == "__main__":
    unittest.main()
