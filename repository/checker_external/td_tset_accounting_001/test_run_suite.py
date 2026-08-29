from __future__ import annotations

import json
import unittest
from pathlib import Path

from checker import FAIL_UNACCOUNTED
from integrity import FAIL_UNSUPPORTED
from run_suite import run_combined_envelope, run_regression_suites

HERE = Path(__file__).resolve().parent
ACCOUNTING_FIXTURES = HERE / "fixtures.json"
INTEGRITY_FIXTURES = HERE / "fixtures_hostile.json"


def load_fixture(path: Path, fixture_id: str) -> dict:
    bundle = json.loads(path.read_text(encoding="utf-8"))
    return next(item for item in bundle["fixtures"] if item["fixture_id"] == fixture_id)


class CheckerSuiteOrchestrationTests(unittest.TestCase):
    def test_a_both_passes_remain_separate(self) -> None:
        result = run_combined_envelope(load_fixture(ACCOUNTING_FIXTURES, "A_FULL_ACCOUNTING"))
        self.assertEqual("PASS", result["combined_status"])
        self.assertEqual("PASS", result["accounting_result"]["status"])
        self.assertEqual("PASS", result["integrity_result"]["status"])
        self.assertTrue(result["results_are_separate"])
        self.assertTrue(result["failure_codes_are_not_merged"])
        self.assertNotEqual(
            result["accounting_result"]["epistemic_limit"],
            result["integrity_result"]["epistemic_limit"],
        )

    def test_d_accounting_failure_does_not_become_integrity_failure(self) -> None:
        result = run_combined_envelope(load_fixture(ACCOUNTING_FIXTURES, "D_SILENT_OMISSION"))
        self.assertEqual("FAIL", result["combined_status"])
        self.assertEqual("FAIL", result["accounting_result"]["status"])
        self.assertEqual([FAIL_UNACCOUNTED], result["accounting_result"]["failure_codes"])
        self.assertEqual("PASS", result["integrity_result"]["status"])
        self.assertEqual([], result["integrity_result"]["failure_codes"])

    def test_i_integrity_failure_does_not_rewrite_accounting_result(self) -> None:
        result = run_combined_envelope(
            load_fixture(INTEGRITY_FIXTURES, "I_REPRESENTED_STATUS_CONTRADICTION")
        )
        self.assertEqual("FAIL", result["combined_status"])
        self.assertEqual("PASS", result["accounting_result"]["status"])
        self.assertEqual([], result["accounting_result"]["failure_codes"])
        self.assertEqual("FAIL", result["integrity_result"]["status"])
        self.assertEqual([FAIL_UNSUPPORTED], result["integrity_result"]["failure_codes"])

    def test_bounded_regression_bundles_match(self) -> None:
        result = run_regression_suites(ACCOUNTING_FIXTURES, INTEGRITY_FIXTURES)
        self.assertEqual("PASS", result["regression_status"])
        self.assertTrue(result["accounting_suite"]["all_match_expected"])
        self.assertTrue(result["integrity_suite"]["all_match_expected"])
        self.assertTrue(result["results_are_separate"])

    def test_missing_bundle_is_input_error_without_suppressing_other_pass(self) -> None:
        result = run_regression_suites(HERE / "missing.json", INTEGRITY_FIXTURES)
        self.assertEqual("INPUT_ERROR", result["regression_status"])
        self.assertEqual("INPUT_ERROR", result["accounting_suite"]["status"])
        self.assertEqual("PASS", result["integrity_suite"]["regression_status"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
