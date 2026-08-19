#!/usr/bin/env python3
from __future__ import annotations

import unittest

from correction_preflight import check_preflight


class CorrectionPreflightTests(unittest.TestCase):
    @staticmethod
    def _result(envelope):
        return check_preflight(envelope).to_dict()

    @staticmethod
    def _codes(result):
        return {item["code"] for item in result["findings"]}

    def test_mundane_control_does_not_expand(self):
        result = self._result(
            {"fixture_id": "E", "claim_text": "What is 7 x 8?", "claim_modes": []}
        )
        self.assertEqual(result["status"], "NOT_APPLICABLE")
        self.assertEqual(result["findings"], [])

    def test_current_claim_requires_reacquisition(self):
        result = self._result(
            {
                "fixture_id": "A",
                "claim_text": "Is the deployment ready now?",
                "claim_modes": ["CURRENT"],
                "currentness": {
                    "source_ref": "yesterday-status-report",
                    "checked_at_utc": "2026-08-18T10:00:00Z",
                    "reacquired": False,
                },
            }
        )
        self.assertEqual(result["status"], "STRUCTURAL_GAP")
        self.assertIn("PREFLIGHT-CURRENT-NOT-REACQUIRED", self._codes(result))

    def test_complete_claim_fails_known_omission(self):
        result = self._result(
            {
                "fixture_id": "B",
                "claim_text": "Every occupied room passed tonight's detector test.",
                "claim_modes": ["COMPLETE"],
                "coverage": {
                    "target_set_ref": "registered-devices",
                    "selection_basis_ref": "asset-register",
                    "comparison_basis_ref": "occupied-rooms",
                    "coverage_status": "CONTRADICTED",
                    "known_omissions": "PRESENT",
                },
            }
        )
        self.assertEqual(result["status"], "STRUCTURAL_GAP")
        self.assertIn("PREFLIGHT-KNOWN-OMISSION-PRESENT", self._codes(result))

    def test_repeated_check_does_not_establish_instrument_adequacy(self):
        result = self._result(
            {
                "fixture_id": "C",
                "claim_text": "The result was tested twice and verified.",
                "claim_modes": ["VERIFIED"],
                "verification": {
                    "proposition_ref": "screening-result",
                    "executed": True,
                    "instrument_adequacy": "KNOWN_BLINDSPOT",
                    "result_returned_to_use": True,
                    "result_ref": "run-2",
                },
            }
        )
        self.assertEqual(result["status"], "STRUCTURAL_GAP")
        self.assertIn(
            "PREFLIGHT-INSTRUMENT-ADEQUACY-NOT-ESTABLISHED",
            self._codes(result),
        )

    def test_correction_window_unknown_is_not_correctable(self):
        result = self._result(
            {
                "fixture_id": "D",
                "claim_text": "The change is reversible.",
                "claim_modes": ["CORRECTABLE"],
                "correction": {
                    "route_ref": "rollback-route",
                    "reachability": "YES",
                    "hardening_ref": "batch-copy-at-30m",
                    "arrives_before_hardening": "UNKNOWN",
                },
            }
        )
        self.assertEqual(result["status"], "STRUCTURAL_GAP")
        self.assertIn(
            "PREFLIGHT-CORRECTION-WINDOW-NOT-ESTABLISHED",
            self._codes(result),
        )

    def test_bounded_complete_claim_can_satisfy_declared_fields(self):
        result = self._result(
            {
                "fixture_id": "F",
                "claim_text": "All devices in the declared emergency register passed.",
                "claim_modes": ["COMPLETE"],
                "coverage": {
                    "target_set_ref": "emergency-register",
                    "selection_basis_ref": "frozen-register",
                    "comparison_basis_ref": "declared-emergency-register",
                    "coverage_status": "ESTABLISHED_RELATIVE_TO_DECLARED_BASIS",
                    "known_omissions": "NONE_ESTABLISHED",
                },
            }
        )
        self.assertEqual(result["status"], "DECLARED_SUPPORT_FIELDS_PRESENT")

    def test_lexical_sentinel_challenge_never_looks_green(self):
        result = self._result(
            {"fixture_id": "S", "claim_text": "100% passed", "claim_modes": []}
        )
        self.assertEqual(result["status"], "MODE_DECLARATION_CHALLENGED")
        self.assertIn("PREFLIGHT-UNDECLARED-MODE-SUSPECTED", self._codes(result))

    def test_capability_cannot_substitute_for_authority(self):
        result = self._result(
            {
                "fixture_id": "G",
                "claim_text": "The operator is authorized to deploy.",
                "claim_modes": ["AUTHORIZED"],
                "authority": {
                    "authority_ref": "",
                    "scope_ref": "deploy-production",
                    "current_applicability": "UNKNOWN",
                    "capability_only": True,
                },
            }
        )
        self.assertEqual(result["status"], "STRUCTURAL_GAP")
        codes = self._codes(result)
        self.assertIn("PREFLIGHT-AUTHORITY-REF-MISSING", codes)
        self.assertIn("PREFLIGHT-CAPABILITY-NOT-AUTHORITY", codes)


if __name__ == "__main__":
    unittest.main()
