from __future__ import annotations

import unittest

from applied_scene_001 import APPLIED_FIXTURES
from checker import FAIL_UNACCOUNTED
from run_suite import run_combined_envelope


class AppliedSceneRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixtures = {item["fixture_id"]: item for item in APPLIED_FIXTURES}

    def run_fixture(self, fixture_id: str) -> tuple[dict, dict]:
        envelope = self.fixtures[fixture_id]
        return envelope, run_combined_envelope(envelope)

    def test_k_disciplined_query_passes_both_checks(self) -> None:
        envelope, result = self.run_fixture("K_APPLIED_DISCIPLINED_QUERY")
        self.assertEqual(envelope["expected"]["combined_status"], result["combined_status"])
        self.assertEqual("PASS", result["accounting_result"]["status"])
        self.assertEqual("PASS", result["integrity_result"]["status"])

    def test_l_silent_omission_fails_accounting_only(self) -> None:
        envelope, result = self.run_fixture("L_APPLIED_SILENT_OMISSION")
        self.assertEqual(envelope["expected"]["combined_status"], result["combined_status"])
        self.assertEqual("FAIL", result["accounting_result"]["status"])
        self.assertEqual([FAIL_UNACCOUNTED], result["accounting_result"]["failure_codes"])
        self.assertEqual("PASS", result["integrity_result"]["status"])

    def test_m_time_dominated_bypass_is_accounted(self) -> None:
        envelope, result = self.run_fixture("M_APPLIED_TIME_DOMINATED_BYPASS")
        self.assertEqual(envelope["expected"]["combined_status"], result["combined_status"])
        self.assertEqual("PASS", result["accounting_result"]["status"])
        self.assertEqual("PASS", result["integrity_result"]["status"])
        self.assertEqual(
            "UNAVAILABLE",
            result["accounting_result"]["classes"]["INFORMATION"]["availability_status"],
        )

    def test_n_ritual_scan_exposes_checker_ceiling(self) -> None:
        envelope, result = self.run_fixture("N_APPLIED_RITUAL_SCAN")
        self.assertEqual("RITUAL_SCAN_NOT_DETECTED", envelope["expected"]["known_limit"])
        self.assertEqual("PASS", result["combined_status"])
        self.assertEqual("PASS", result["accounting_result"]["status"])
        self.assertEqual("PASS", result["integrity_result"]["status"])
        self.assertEqual(
            "REPRESENTED",
            result["accounting_result"]["classes"]["INFORMATION"]["availability_status"],
        )

    def test_applied_scene_does_not_claim_actual_event(self) -> None:
        for fixture in self.fixtures.values():
            self.assertEqual("CONSTRUCTED_APPLIED_SCENE", fixture["scene"]["scene_status"])
            self.assertIn(
                "not a record of an actual operation",
                fixture["scene"]["epistemic_note"],
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
