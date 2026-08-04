from __future__ import annotations

import unittest
from copy import deepcopy

from minimum_schema import assert_schema_valid
from search_coverage import (
    FAIL_CONTRADICTION,
    FAIL_REFERENCE,
    FAIL_UNSUPPORTED,
    check_search_coverage,
)
from search_coverage_fixtures import SEARCH_COVERAGE_FIXTURES


class SearchCoverageRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixtures = {item["fixture_id"]: item for item in SEARCH_COVERAGE_FIXTURES}

    def run_fixture(self, fixture_id: str):
        fixture = self.fixtures[fixture_id]
        assert_schema_valid(fixture["trace_graph"])
        return fixture, check_search_coverage(fixture)

    def test_o_declared_reachability_chain(self) -> None:
        _, result = self.run_fixture("O_DECLARED_REACHABILITY_CHAIN")
        self.assertEqual("PASS", result.status)
        self.assertEqual("DECLARED_REACHABILITY_CHAIN", result.coverage_status)
        self.assertEqual(["n_entity_field_team"], result.validated_target_refs)
        self.assertEqual([], result.failure_codes)

    def test_p_ritual_target_blindspot_is_explicit_contradiction(self) -> None:
        _, result = self.run_fixture("P_RITUAL_TARGET_BLINDSPOT")
        self.assertEqual("FAIL", result.status)
        self.assertEqual("CONTRADICTED", result.coverage_status)
        self.assertEqual(["n_entity_field_team"], result.contradicted_target_refs)
        self.assertEqual([FAIL_CONTRADICTION], result.failure_codes)

    def test_q_no_comparison_basis_is_not_assessable(self) -> None:
        _, result = self.run_fixture("Q_NO_COVERAGE_COMPARISON")
        self.assertEqual("PASS", result.status)
        self.assertEqual("NOT_ASSESSABLE", result.coverage_status)
        self.assertEqual([], result.failure_codes)

    def test_r_information_unavailable_is_not_a_coverage_failure(self) -> None:
        _, result = self.run_fixture("R_INFORMATION_UNAVAILABLE")
        self.assertEqual("PASS", result.status)
        self.assertEqual("NOT_APPLICABLE_INFORMATION_UNAVAILABLE", result.coverage_status)
        self.assertEqual([], result.failure_codes)

    def test_assess_without_declared_path_is_unsupported(self) -> None:
        fixture = deepcopy(self.fixtures["O_DECLARED_REACHABILITY_CHAIN"])
        fixture["fixture_id"] = "S_MISSING_DECLARED_PATH"
        fixture["coverage_evidence"]["target_path_edge_refs"] = {}
        result = check_search_coverage(fixture)
        self.assertEqual("FAIL", result.status)
        self.assertEqual("UNSUPPORTED_REACHABILITY", result.coverage_status)
        self.assertEqual([FAIL_UNSUPPORTED], result.failure_codes)

    def test_missing_target_ref_is_reference_failure(self) -> None:
        fixture = deepcopy(self.fixtures["O_DECLARED_REACHABILITY_CHAIN"])
        fixture["fixture_id"] = "T_MISSING_TARGET_REF"
        fixture["coverage_evidence"]["required_target_refs"] = ["n_missing_target"]
        fixture["coverage_evidence"]["target_path_edge_refs"] = {
            "n_missing_target": ["e_info_observes_record", "e_record_reports_team"]
        }
        result = check_search_coverage(fixture)
        self.assertEqual("FAIL", result.status)
        self.assertEqual("UNUSABLE_TARGET_SET", result.coverage_status)
        self.assertEqual([FAIL_REFERENCE], result.failure_codes)

    def test_non_contiguous_path_is_unsupported(self) -> None:
        fixture = deepcopy(self.fixtures["O_DECLARED_REACHABILITY_CHAIN"])
        fixture["fixture_id"] = "U_NON_CONTIGUOUS_PATH"
        fixture["coverage_evidence"]["target_path_edge_refs"] = {
            "n_entity_field_team": ["e_record_reports_team"]
        }
        result = check_search_coverage(fixture)
        self.assertEqual("FAIL", result.status)
        self.assertEqual("UNSUPPORTED_REACHABILITY", result.coverage_status)
        self.assertEqual([FAIL_UNSUPPORTED], result.failure_codes)

    def test_declared_path_does_not_claim_actual_coverage(self) -> None:
        _, result = self.run_fixture("O_DECLARED_REACHABILITY_CHAIN")
        self.assertIn("actual reachability is not established", result.diagnostics[0])
        self.assertIn("does not establish actual search coverage", result.epistemic_limit)


if __name__ == "__main__":
    unittest.main(verbosity=2)
