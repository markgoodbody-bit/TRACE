import itertools
import json
import unittest
from fractions import Fraction
from pathlib import Path
import build_views
import simulator


def distribution():
    return [{"direct": d, "f1": a, "f2": b,
             "prob": str((Fraction(18, 25) if d else Fraction(7, 25)) / 4)}
            for d, a, b in itertools.product((False, True), repeat=3)]


def workshop_checks():
    scenario = json.loads(Path(__file__).with_name("scenario.example.json").read_text(encoding="utf-8"))
    return simulator.workshop_inquiry(scenario["worlds"])


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
        blocks = build_views.review_blocks(raw, units)
        self.assertEqual(blocks[0]["start_line"], 1)
        self.assertEqual(blocks[-1]["end_line"], len(lines))
        self.assertTrue(all(a["end_line"] + 1 == b["start_line"] for a, b in zip(blocks, blocks[1:])))
        self.assertEqual(b"".join("".join(lines[b["start_line"]-1:b["end_line"]]).encode("utf8") for b in blocks), raw)

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

    def test_report_copies_and_partial_checks(self):
        checks = workshop_checks()
        copy = checks["copy_of_the_listing"]
        self.assertEqual(list(copy["answers"]), ["positive"])
        self.assertEqual(copy["answers"]["positive"]["probability_direct_works"], "1/2")
        partial = checks["fresh_partial_check"]
        self.assertEqual(partial["answers"]["negative"]["probability_direct_works"], "1/3")
        self.assertEqual(partial["answers"]["positive"]["probability_direct_works"], "2/3")
        for check in (copy, partial):
            self.assertTrue(check["usable_before_lock"])
            self.assertEqual(check["gain_in_success_probability"], "0")
            self.assertTrue(all(a["best_routes_if_in_time"] == ["fallback"]
                                for a in check["answers"].values()))

    def test_full_check_needs_booking_time_and_authority(self):
        checks = workshop_checks()
        early = checks["fresh_full_check_before_lock"]
        late = checks["fresh_full_check_at_lock"]
        self.assertEqual(early["answers"], late["answers"])
        self.assertEqual(early["gain_in_success_probability"], "1/8")
        self.assertEqual(early["success_by_acting_on_available_evidence"], "7/8")
        self.assertEqual(late["booking_effect_time"], 10)
        self.assertFalse(late["usable_before_lock"])
        self.assertEqual(late["success_by_acting_on_available_evidence"], "3/4")
        limited = checks["full_check_with_only_direct_authority"]
        self.assertTrue(limited["usable_before_lock"])
        self.assertEqual(limited["baseline_routes"], ["direct"])
        self.assertEqual(limited["gain_in_success_probability"], "0")
        self.assertEqual(limited["success_by_acting_on_available_evidence"], "1/2")

    def test_inquiry_preserves_joint_dependence(self):
        same_dependency = [
            {"direct": True, "f1": True, "f2": True, "prob": "1/2"},
            {"direct": False, "f1": True, "f2": False, "prob": "1/2"},
        ]
        result = simulator.inquiry(same_dependency, positive_likelihoods=(0, 1),
                                   observation_time=7, booking_minutes=2, booking_lock=10)
        self.assertEqual(result["baseline_routes"], ["direct", "fallback"])
        self.assertEqual(result["success_by_acting_on_available_evidence"], "1/2")

    def test_no_joint_law_or_extra_field_is_not_guessed(self):
        with self.assertRaises(ValueError):
            simulator.simulate_scenario({"marginals": [0.9, 0.8]})

    def test_unknown_and_temporal_boundaries(self):
        self.assertFalse(simulator.before_hardening(5, 5))
        self.assertTrue(simulator.delivered_by_due(5, 5))
        self.assertEqual(simulator.unknown_conditions("yes", "unknown")["delivery"], "unknown")
        self.assertEqual(simulator.unknown_conditions("yes", "unknown")["authorization"], "UNASSESSED")

    def test_acknowledgement_does_not_establish_timely_effect(self):
        sample = dict(acknowledgement_time=3, delivery_time=8, backup_available=True,
                      backup_cancelled_before_delivery=True, backup_time=4, due_time=6, hardening_time=7)
        self.assertEqual(simulator.delivery_route(**sample)["status"], "NOT_SUPPORTED_IN_MODEL")
        sample["backup_cancelled_before_delivery"] = False
        self.assertEqual(simulator.delivery_route(**sample)["status"], "SUPPORTED_IN_MODEL")
        sample["backup_cancelled_before_delivery"] = True
        sample["delivery_time"] = None
        self.assertEqual(simulator.delivery_route(**sample)["status"], "UNKNOWN")
        sample["delivery_time"] = 7
        sample["due_time"] = 7
        self.assertEqual(simulator.delivery_route(**sample)["status"], "NOT_SUPPORTED_IN_MODEL")

    def test_legacy_ambiguous_cancellation_name_is_rejected(self):
        with self.assertRaises(TypeError):
            simulator.delivery_route(acknowledgement_time=1, delivery_time=8, backup_available=True,
                                     backup_cancelled=True, backup_time=4, due_time=6, hardening_time=7)

    def test_reject_incomplete_or_invalid_joint_law(self):
        with self.assertRaises(ValueError):
            simulator.support([], "early", 2)
        with self.assertRaises(ValueError):
            simulator.support([{"direct": True, "f1": True, "f2": True, "prob": "3/2"}], "early", 2)
        with self.assertRaises(ValueError):
            simulator.support(distribution(), "unspecified", 2)

    def test_spine_is_derived_and_flags_unknown(self):
        candidate = build_views.CANDIDATE.read_text(encoding="utf8")
        spine = build_views.render_spine(candidate)
        decision = candidate.split(build_views.DECISION_HEADING, 1)[1].split("\n## 1.", 1)[0]
        title, lead, _ = candidate.split("\n\n", 2)
        self.assertTrue(spine.startswith(f"{title} (short spine)\n\n{lead}\n"))
        self.assertIn(build_views.DECISION_HEADING + decision.rstrip(), spine)
        self.assertIn("UNRESOLVED", spine)
        self.assertIn("co-evolving social layer", spine)
        self.assertIn("## 3. Offers, duties and power", spine)
        self.assertIn("[Expand section 3](CANDIDATE.md#3-offers-duties-and-power)", spine)
        self.assertIn("[donor and case index](DONOR-AND-CASE-INDEX.md)", spine)


if __name__ == "__main__":
    unittest.main()
