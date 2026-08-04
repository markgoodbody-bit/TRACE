from __future__ import annotations

import unittest
from copy import deepcopy

from applied_scene_001 import APPLIED_FIXTURES
from checker import FAIL_UNACCOUNTED
from minimum_schema import (
    MinimumSchemaError,
    assert_schema_valid,
    extract_minimum_schema,
    validation_errors,
)
from run_suite import run_combined_envelope


class AppliedSceneRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixtures = {item["fixture_id"]: item for item in APPLIED_FIXTURES}

    def run_fixture(self, fixture_id: str) -> tuple[dict, dict]:
        envelope = self.fixtures[fixture_id]
        return envelope, run_combined_envelope(envelope)

    def test_embedded_schema_extracts_expected_contract(self) -> None:
        schema = extract_minimum_schema()
        self.assertEqual("urn:trace:graph:0.2.5", schema["$id"])
        self.assertEqual("TRACE-GRAPH-0.2.5 minimum validator", schema["title"])

    def test_all_applied_packets_pass_embedded_minimum_schema(self) -> None:
        for fixture in self.fixtures.values():
            with self.subTest(fixture_id=fixture["fixture_id"]):
                self.assertEqual("PASS", fixture["expected"]["schema_status"])
                self.assertEqual([], validation_errors(fixture["trace_graph"]))
                assert_schema_valid(fixture["trace_graph"])

    def test_schema_validator_is_active(self) -> None:
        malformed = deepcopy(self.fixtures["K_APPLIED_DISCIPLINED_QUERY"]["trace_graph"])
        del malformed["anti_clearance"]["reading_is_not_truth"]
        errors = validation_errors(malformed)
        self.assertTrue(any("reading_is_not_truth" in error for error in errors))
        with self.assertRaises(MinimumSchemaError):
            assert_schema_valid(malformed)

    def test_k_disciplined_query_passes_both_checks(self) -> None:
        envelope, result = self.run_fixture("K_APPLIED_DISCIPLINED_QUERY")
        assert_schema_valid(envelope["trace_graph"])
        self.assertEqual(envelope["expected"]["combined_status"], result["combined_status"])
        self.assertEqual("PASS", result["accounting_result"]["status"])
        self.assertEqual("PASS", result["integrity_result"]["status"])

    def test_l_silent_omission_fails_accounting_only(self) -> None:
        envelope, result = self.run_fixture("L_APPLIED_SILENT_OMISSION")
        assert_schema_valid(envelope["trace_graph"])
        self.assertEqual(envelope["expected"]["combined_status"], result["combined_status"])
        self.assertEqual("FAIL", result["accounting_result"]["status"])
        self.assertEqual([FAIL_UNACCOUNTED], result["accounting_result"]["failure_codes"])
        self.assertEqual("PASS", result["integrity_result"]["status"])

    def test_m_time_dominated_bypass_is_accounted(self) -> None:
        envelope, result = self.run_fixture("M_APPLIED_TIME_DOMINATED_BYPASS")
        assert_schema_valid(envelope["trace_graph"])
        self.assertEqual(envelope["expected"]["combined_status"], result["combined_status"])
        self.assertEqual("PASS", result["accounting_result"]["status"])
        self.assertEqual("PASS", result["integrity_result"]["status"])
        self.assertEqual(
            "UNAVAILABLE",
            result["accounting_result"]["classes"]["INFORMATION"]["availability_status"],
        )

    def test_n_schema_valid_ritual_scan_still_exposes_checker_ceiling(self) -> None:
        envelope, result = self.run_fixture("N_APPLIED_RITUAL_SCAN")
        assert_schema_valid(envelope["trace_graph"])
        self.assertEqual("RITUAL_SCAN_NOT_DETECTED", envelope["expected"]["known_limit"])
        self.assertEqual("PASS", result["combined_status"])
        self.assertEqual("PASS", result["accounting_result"]["status"])
        self.assertEqual("PASS", result["integrity_result"]["status"])
        self.assertEqual(
            "REPRESENTED",
            result["accounting_result"]["classes"]["INFORMATION"]["availability_status"],
        )
        ritual_aperture = next(
            item
            for item in envelope["trace_graph"]["nodes"]
            if item["id"] == "n_aperture_ritual"
        )
        self.assertEqual(
            ["n_entity_field_team"], ritual_aperture["attributes"]["blindspots"]
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
