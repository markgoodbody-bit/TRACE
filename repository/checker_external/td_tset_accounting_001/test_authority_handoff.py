from __future__ import annotations

import unittest
from copy import deepcopy

from authority_handoff import (
    FAIL_MISSING_RECEIPT,
    FAIL_RECEIPT_MISMATCH,
    FAIL_REFERENCE,
    FAIL_SILENT_INHERITANCE,
    FAIL_UNBOUND_BRAKE,
    check_authority_handoff,
)
from authority_handoff_fixtures import AUTHORITY_HANDOFF_FIXTURES
from minimum_schema import assert_schema_valid


class AuthorityHandoffRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixtures = {item["fixture_id"]: item for item in AUTHORITY_HANDOFF_FIXTURES}

    def run_fixture(self, fixture_id: str):
        fixture = self.fixtures[fixture_id]
        assert_schema_valid(fixture["trace_graph"])
        return fixture, check_authority_handoff(fixture)

    def test_all_packets_pass_embedded_minimum_schema(self) -> None:
        for fixture in self.fixtures.values():
            with self.subTest(fixture_id=fixture["fixture_id"]):
                assert_schema_valid(fixture["trace_graph"])

    def test_aa_unresolved_authority_is_preserved_without_failure(self) -> None:
        _, result = self.run_fixture("AA_UNRESOLVED_AUTHORITY")
        self.assertEqual("PASS", result.status)
        self.assertEqual("UNRESOLVED_AUTHORITY", result.handoff_status)
        self.assertEqual([], result.failure_codes)

    def test_ab_silent_operator_inheritance_fails(self) -> None:
        _, result = self.run_fixture("AB_SILENT_OPERATOR_INHERITANCE")
        self.assertEqual("FAIL", result.status)
        self.assertEqual("SILENT_AUTHORITY_INHERITANCE", result.handoff_status)
        self.assertEqual([FAIL_SILENT_INHERITANCE], result.failure_codes)

    def test_ac_declared_hold_handoff_passes_without_endorsement(self) -> None:
        _, result = self.run_fixture("AC_DECLARED_HOLD_HANDOFF")
        self.assertEqual("PASS", result.status)
        self.assertEqual("DECLARED_AUTHORITY_HANDOFF", result.handoff_status)
        self.assertEqual("n_selector_incident", result.selector_ref)
        self.assertEqual("n_brake_safety", result.brake_ref)
        self.assertIn("legitimacy is not established", result.diagnostics[0])

    def test_ad_commitment_without_receipt_fails(self) -> None:
        _, result = self.run_fixture("AD_COMMITTED_WITHOUT_RECEIPT")
        self.assertEqual("FAIL", result.status)
        self.assertEqual("MISSING_COMMITMENT_RECEIPT", result.handoff_status)
        self.assertEqual([FAIL_MISSING_RECEIPT], result.failure_codes)

    def test_ae_commitment_receipt_preserves_unresolved_conflict(self) -> None:
        _, result = self.run_fixture("AE_COMMITTED_WITH_RECEIPT")
        self.assertEqual("PASS", result.status)
        self.assertEqual(
            "COMMITMENT_RECORDED_UNDER_UNRESOLVED_CONFLICT",
            result.handoff_status,
        )
        self.assertEqual([], result.failure_codes)
        self.assertIn("not clearance", result.diagnostics[0])

    def test_af_unbound_brake_fails(self) -> None:
        _, result = self.run_fixture("AF_UNBOUND_BRAKE")
        self.assertEqual("FAIL", result.status)
        self.assertEqual("UNBOUND_BRAKE_AUTHORITY", result.handoff_status)
        self.assertEqual([FAIL_UNBOUND_BRAKE], result.failure_codes)

    def test_selected_result_outside_conflict_set_fails_reference(self) -> None:
        fixture = deepcopy(self.fixtures["AC_DECLARED_HOLD_HANDOFF"])
        fixture["fixture_id"] = "AG_SELECTED_RESULT_OUTSIDE_SET"
        fixture["authority_handoff_evidence"]["selected_aperture_result_ref"] = (
            "n_record_dispatch"
        )
        result = check_authority_handoff(fixture)
        self.assertEqual("FAIL", result.status)
        self.assertEqual("SELECTED_RESULT_OUTSIDE_CONFLICT_SET", result.handoff_status)
        self.assertEqual([FAIL_REFERENCE], result.failure_codes)

    def test_commitment_receipt_mismatch_fails(self) -> None:
        fixture = deepcopy(self.fixtures["AE_COMMITTED_WITH_RECEIPT"])
        fixture["fixture_id"] = "AH_RECEIPT_MISMATCH"
        fixture["trace_graph"]["commitment_receipts"][0]["selected_transition_ref"] = (
            "n_transition_hold"
        )
        result = check_authority_handoff(fixture)
        self.assertEqual("FAIL", result.status)
        self.assertEqual("COMMITMENT_RECEIPT_MISMATCH", result.handoff_status)
        self.assertEqual([FAIL_RECEIPT_MISMATCH], result.failure_codes)

    def test_no_comparison_envelope_remains_not_assessable(self) -> None:
        fixture = deepcopy(self.fixtures["AA_UNRESOLVED_AUTHORITY"])
        fixture["fixture_id"] = "AI_NO_AUTHORITY_ENVELOPE"
        fixture.pop("authority_handoff_evidence")
        result = check_authority_handoff(fixture)
        self.assertEqual("PASS", result.status)
        self.assertEqual("NOT_ASSESSABLE", result.handoff_status)
        self.assertIn("does not establish legitimate authority", result.epistemic_limit)


if __name__ == "__main__":
    unittest.main(verbosity=2)
