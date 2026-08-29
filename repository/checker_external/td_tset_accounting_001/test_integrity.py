from __future__ import annotations

import json
import unittest
from pathlib import Path

from integrity import FAIL_REFERENCE, FAIL_UNSUPPORTED, check_integrity, run_bundle

FIXTURE_FILE = Path(__file__).resolve().parent / "fixtures_hostile.json"


class HostileIntegrityRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        bundle = json.loads(FIXTURE_FILE.read_text(encoding="utf-8"))
        cls.fixtures = {item["fixture_id"]: item for item in bundle["fixtures"]}

    def check_expected(self, fixture_id: str):
        envelope = self.fixtures[fixture_id]
        result = check_integrity(envelope)
        self.assertEqual(envelope["expected"]["status"], result.status)
        self.assertEqual(envelope["expected"]["failure_codes"], result.failure_codes)
        return result

    def test_g_reference_mismatch(self) -> None:
        result = self.check_expected("G_REFERENCE_MISMATCH")
        self.assertEqual([FAIL_REFERENCE], result.failure_codes)
        diagnostics = " ".join(result.classes["INFORMATION"].diagnostics)
        self.assertIn("does not resolve", diagnostics)
        self.assertIn("non-TRANSITION", diagnostics)
        self.assertIn("wrong mode", diagnostics)

    def test_h_missing_assessment_basis(self) -> None:
        result = self.check_expected("H_UNRESOLVED_ASSESSMENT_BASIS")
        self.assertEqual([FAIL_REFERENCE], result.failure_codes)
        self.assertIn(
            "c_missing_basis", " ".join(result.classes["INFORMATION"].diagnostics)
        )

    def test_i_represented_status_contradiction(self) -> None:
        result = self.check_expected("I_REPRESENTED_STATUS_CONTRADICTION")
        self.assertEqual([FAIL_UNSUPPORTED], result.failure_codes)
        self.assertEqual(
            ["n_info"], result.classes["INFORMATION"].matching_transition_refs
        )

    def test_j_omitted_assessment_does_not_infer_liveness(self) -> None:
        result = self.check_expected("J_OMITTED_MANIFEST_ASSESSMENT")
        info = result.classes["INFORMATION"]
        self.assertFalse(info.assessment_present)
        self.assertEqual("NOT_ASSESSABLE", info.availability_status)
        self.assertEqual([], info.failure_codes)

    def test_bundle_matches_expected(self) -> None:
        rows, mismatch = run_bundle(FIXTURE_FILE)
        self.assertFalse(mismatch)
        self.assertEqual(4, len(rows))
        self.assertTrue(all(row["matches_expected"] for row in rows))


if __name__ == "__main__":
    unittest.main(verbosity=2)
