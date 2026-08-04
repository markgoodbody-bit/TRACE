from __future__ import annotations

import unittest
from copy import deepcopy

from search_coverage import FAIL_REFERENCE, FAIL_UNSUPPORTED
from search_coverage_fixtures import SEARCH_COVERAGE_FIXTURES
from search_coverage_integrity import check_search_coverage_integrity


class SearchCoverageIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixtures = {item["fixture_id"]: item for item in SEARCH_COVERAGE_FIXTURES}

    def test_o_declared_path_has_bound_directed_evidence(self) -> None:
        result = check_search_coverage_integrity(
            self.fixtures["O_DECLARED_REACHABILITY_CHAIN"]
        )
        self.assertEqual("PASS", result.status)
        self.assertEqual([], result.failure_codes)

    def test_p_explicit_contradiction_is_not_an_integrity_failure(self) -> None:
        result = check_search_coverage_integrity(
            self.fixtures["P_RITUAL_TARGET_BLINDSPOT"]
        )
        self.assertEqual("PASS", result.status)
        self.assertEqual([], result.failure_codes)

    def test_r_unavailability_reason_binds_clock_basis(self) -> None:
        result = check_search_coverage_integrity(
            self.fixtures["R_INFORMATION_UNAVAILABLE"]
        )
        self.assertEqual("PASS", result.status)
        self.assertEqual([], result.failure_codes)

    def test_v_assess_without_comparison_basis_fails(self) -> None:
        fixture = deepcopy(self.fixtures["O_DECLARED_REACHABILITY_CHAIN"])
        fixture["fixture_id"] = "V_NO_COMPARISON_BASIS"
        fixture["coverage_evidence"]["comparison_basis_claim_refs"] = []
        result = check_search_coverage_integrity(fixture)
        self.assertEqual("FAIL", result.status)
        self.assertEqual([FAIL_UNSUPPORTED], result.failure_codes)

    def test_w_undirected_path_edge_fails(self) -> None:
        fixture = deepcopy(self.fixtures["O_DECLARED_REACHABILITY_CHAIN"])
        fixture["fixture_id"] = "W_UNDIRECTED_PATH_EDGE"
        edge = next(
            item
            for item in fixture["trace_graph"]["edges"]
            if item["id"] == "e_info_observes_record"
        )
        edge["directed"] = False
        result = check_search_coverage_integrity(fixture)
        self.assertEqual("FAIL", result.status)
        self.assertEqual([FAIL_UNSUPPORTED], result.failure_codes)

    def test_x_path_edge_with_missing_claim_ref_fails(self) -> None:
        fixture = deepcopy(self.fixtures["O_DECLARED_REACHABILITY_CHAIN"])
        fixture["fixture_id"] = "X_MISSING_EDGE_CLAIM"
        edge = next(
            item
            for item in fixture["trace_graph"]["edges"]
            if item["id"] == "e_info_observes_record"
        )
        edge["claim_refs"] = ["c_missing_claim"]
        result = check_search_coverage_integrity(fixture)
        self.assertEqual("FAIL", result.status)
        self.assertIn(FAIL_REFERENCE, result.failure_codes)

    def test_y_unavailability_reason_not_bound_to_basis_fails(self) -> None:
        fixture = deepcopy(self.fixtures["R_INFORMATION_UNAVAILABLE"])
        fixture["fixture_id"] = "Y_UNBOUND_UNAVAILABILITY_REASON"
        reason = next(
            item
            for item in fixture["trace_graph"]["claims"]
            if item["id"] == "c_info_too_slow"
        )
        reason["source_refs"] = []
        result = check_search_coverage_integrity(fixture)
        self.assertEqual("FAIL", result.status)
        self.assertEqual([FAIL_UNSUPPORTED], result.failure_codes)


if __name__ == "__main__":
    unittest.main(verbosity=2)
