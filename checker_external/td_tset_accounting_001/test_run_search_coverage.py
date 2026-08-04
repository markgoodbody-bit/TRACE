from __future__ import annotations

import unittest
from copy import deepcopy

from run_search_coverage import run_regressions, run_search_coverage_suite
from search_coverage import FAIL_UNSUPPORTED
from search_coverage_fixtures import SEARCH_COVERAGE_FIXTURES


class SearchCoverageOrchestrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixtures = {item["fixture_id"]: item for item in SEARCH_COVERAGE_FIXTURES}

    def test_o_both_passes_succeed_and_remain_separate(self) -> None:
        result = run_search_coverage_suite(
            self.fixtures["O_DECLARED_REACHABILITY_CHAIN"]
        )
        self.assertEqual("PASS", result["combined_status"])
        self.assertEqual("PASS", result["coverage_result"]["status"])
        self.assertEqual("PASS", result["integrity_result"]["status"])
        self.assertTrue(result["results_are_separate"])
        self.assertTrue(result["failure_codes_are_not_merged"])

    def test_p_base_contradiction_does_not_become_integrity_failure(self) -> None:
        result = run_search_coverage_suite(
            self.fixtures["P_RITUAL_TARGET_BLINDSPOT"]
        )
        self.assertEqual("FAIL", result["combined_status"])
        self.assertEqual("FAIL", result["coverage_result"]["status"])
        self.assertEqual("PASS", result["integrity_result"]["status"])

    def test_v_integrity_failure_catches_weak_base_pass(self) -> None:
        fixture = deepcopy(self.fixtures["O_DECLARED_REACHABILITY_CHAIN"])
        fixture["fixture_id"] = "V_NO_COMPARISON_BASIS"
        fixture["coverage_evidence"]["comparison_basis_claim_refs"] = []
        result = run_search_coverage_suite(fixture)
        self.assertEqual("FAIL", result["combined_status"])
        self.assertEqual("PASS", result["coverage_result"]["status"])
        self.assertEqual("FAIL", result["integrity_result"]["status"])
        self.assertEqual([FAIL_UNSUPPORTED], result["integrity_result"]["failure_codes"])

    def test_q_not_assessable_remains_pass_without_clearance(self) -> None:
        result = run_search_coverage_suite(self.fixtures["Q_NO_COVERAGE_COMPARISON"])
        self.assertEqual("PASS", result["combined_status"])
        self.assertEqual("NOT_ASSESSABLE", result["coverage_result"]["coverage_status"])
        self.assertIn(
            "does not establish actual search coverage",
            result["orchestrator_epistemic_limit"],
        )

    def test_bounded_regressions_match(self) -> None:
        result = run_regressions()
        self.assertEqual("PASS", result["regression_status"])
        self.assertTrue(result["all_match_expected"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
