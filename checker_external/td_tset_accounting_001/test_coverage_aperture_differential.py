from __future__ import annotations

import unittest

from coverage_aperture_differential_001 import (
    INDEPENDENT_APERTURE,
    OPERATOR_APERTURE,
    run_differential,
)
from minimum_schema import assert_schema_valid
from run_search_coverage import run_search_coverage_suite
from search_coverage import FAIL_CONTRADICTION


class CoverageApertureDifferentialTests(unittest.TestCase):
    def test_both_apertures_use_the_same_schema_valid_trace_packet(self) -> None:
        assert_schema_valid(OPERATOR_APERTURE["trace_graph"])
        assert_schema_valid(INDEPENDENT_APERTURE["trace_graph"])
        output = run_differential()
        self.assertTrue(output["same_trace_packet"])
        self.assertIsNotNone(output["trace_graph_sha256"])

    def test_operator_target_set_passes_for_known_hog_scope(self) -> None:
        result = run_search_coverage_suite(OPERATOR_APERTURE)
        self.assertEqual("PASS", result["combined_status"])
        self.assertEqual(
            "DECLARED_REACHABILITY_CHAIN",
            result["coverage_result"]["coverage_status"],
        )
        self.assertEqual("PASS", result["integrity_result"]["status"])

    def test_dispatch_target_set_exposes_field_team_contradiction(self) -> None:
        result = run_search_coverage_suite(INDEPENDENT_APERTURE)
        self.assertEqual("FAIL", result["combined_status"])
        self.assertEqual("CONTRADICTED", result["coverage_result"]["coverage_status"])
        self.assertEqual(
            [FAIL_CONTRADICTION], result["coverage_result"]["failure_codes"]
        )
        self.assertEqual("PASS", result["integrity_result"]["status"])

    def test_differential_preserves_disagreement(self) -> None:
        output = run_differential()
        self.assertEqual("DIVERGENT", output["differential_status"])
        self.assertEqual("UNRESOLVED", output["authoritative_aperture"])
        self.assertEqual(
            "PASS", output["operator_aperture"]["result"]["combined_status"]
        )
        self.assertEqual(
            "FAIL", output["independent_aperture"]["result"]["combined_status"]
        )

    def test_aperture_metadata_is_not_promoted_to_truth(self) -> None:
        output = run_differential()
        self.assertEqual(
            "DECLARED_INDEPENDENT",
            output["independent_aperture"]["metadata"]["independence_status"],
        )
        self.assertIn(
            "does not establish which aperture is authoritative",
            output["epistemic_limit"],
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
