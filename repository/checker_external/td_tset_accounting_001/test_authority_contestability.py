from __future__ import annotations

import unittest
from copy import deepcopy

from authority_contestability import (
    FAIL_REFERENCE,
    FAIL_TOO_SLOW,
    check_authority_contestability,
)
from authority_contestability_fixtures import AUTHORITY_CONTESTABILITY_FIXTURES
from minimum_schema import assert_schema_valid


class AuthorityContestabilityRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixtures = {item["fixture_id"]: item for item in AUTHORITY_CONTESTABILITY_FIXTURES}

    def run_fixture(self, fixture_id: str):
        fixture = self.fixtures[fixture_id]
        assert_schema_valid(fixture["trace_graph"])
        return fixture, check_authority_contestability(fixture)

    def test_all_packets_pass_embedded_minimum_schema(self) -> None:
        for fixture in self.fixtures.values():
            with self.subTest(fixture_id=fixture["fixture_id"]):
                assert_schema_valid(fixture["trace_graph"])

    def test_ag_timely_route_reaches_brake_before_deadline(self) -> None:
        _, result = self.run_fixture("AG_TIMELY_CONTEST_ROUTE")
        self.assertEqual("PASS", result.status)
        self.assertEqual(
            "DECLARED_ROUTE_REACHES_BRAKE_BEFORE_DEADLINE",
            result.contestability_status,
        )
        self.assertEqual(4, result.route_seconds)
        self.assertEqual(20, result.deadline_seconds)
        self.assertEqual(16, result.margin_seconds)
        self.assertIn("actual contestability is not established", result.diagnostics[0])

    def test_ah_slow_route_fails(self) -> None:
        _, result = self.run_fixture("AH_CONTEST_ROUTE_TOO_SLOW")
        self.assertEqual("FAIL", result.status)
        self.assertEqual("CONTEST_ROUTE_TOO_SLOW", result.contestability_status)
        self.assertEqual([FAIL_TOO_SLOW], result.failure_codes)
        self.assertEqual(-5, result.margin_seconds)

    def test_ai_missing_route_fails(self) -> None:
        _, result = self.run_fixture("AI_NO_CONTEST_ROUTE")
        self.assertEqual("FAIL", result.status)
        self.assertEqual("NO_CONTEST_ROUTE", result.contestability_status)
        self.assertEqual(["TD-AUTHORITY-CONTEST-NO-ROUTE"], result.failure_codes)

    def test_aj_captured_route_fails(self) -> None:
        _, result = self.run_fixture("AJ_CAPTURED_CONTEST_ROUTE")
        self.assertEqual("FAIL", result.status)
        self.assertEqual("CONTEST_ROUTE_CAPTURED", result.contestability_status)
        self.assertEqual(
            ["TD-AUTHORITY-CONTEST-ROUTE-CAPTURED"], result.failure_codes
        )

    def test_ak_unknown_route_state_remains_unknown(self) -> None:
        _, result = self.run_fixture("AK_CONTESTABILITY_UNKNOWN")
        self.assertEqual("PASS", result.status)
        self.assertEqual("CONTESTABILITY_UNKNOWN", result.contestability_status)
        self.assertEqual([], result.failure_codes)

    def test_al_missing_external_contest_authority_fails(self) -> None:
        _, result = self.run_fixture("AL_UNSUPPORTED_CONTEST_AUTHORITY")
        self.assertEqual("FAIL", result.status)
        self.assertEqual("UNSUPPORTED_CONTEST_ROUTE", result.contestability_status)
        self.assertEqual(
            ["TD-AUTHORITY-CONTEST-UNSUPPORTED-STATUS"], result.failure_codes
        )

    def test_equal_route_and_deadline_is_not_before(self) -> None:
        fixture = deepcopy(self.fixtures["AG_TIMELY_CONTEST_ROUTE"])
        fixture["fixture_id"] = "AM_EQUAL_ROUTE_AND_DEADLINE"
        route_clock = next(
            item
            for item in fixture["trace_graph"]["nodes"]
            if item["id"] == "n_clock_contest_route"
        )
        route_clock["attributes"]["seconds"] = 20
        result = check_authority_contestability(fixture)
        self.assertEqual("FAIL", result.status)
        self.assertEqual("CONTEST_ROUTE_TOO_SLOW", result.contestability_status)
        self.assertEqual([FAIL_TOO_SLOW], result.failure_codes)
        self.assertEqual(0, result.margin_seconds)

    def test_missing_challenge_result_reference_fails(self) -> None:
        fixture = deepcopy(self.fixtures["AG_TIMELY_CONTEST_ROUTE"])
        fixture["fixture_id"] = "AN_MISSING_CHALLENGE_RESULT"
        fixture["authority_contestability_evidence"][
            "challenging_aperture_result_refs"
        ] = ["n_missing_result"]
        result = check_authority_contestability(fixture)
        self.assertEqual("FAIL", result.status)
        self.assertEqual("UNUSABLE_CONTESTABILITY_RECORD", result.contestability_status)
        self.assertEqual([FAIL_REFERENCE], result.failure_codes)

    def test_no_comparison_envelope_remains_not_assessable(self) -> None:
        fixture = deepcopy(self.fixtures["AG_TIMELY_CONTEST_ROUTE"])
        fixture["fixture_id"] = "AO_NO_CONTESTABILITY_ENVELOPE"
        fixture.pop("authority_contestability_evidence")
        result = check_authority_contestability(fixture)
        self.assertEqual("PASS", result.status)
        self.assertEqual("NOT_ASSESSABLE", result.contestability_status)
        self.assertIn("does not establish legitimate authority", result.epistemic_limit)

    def test_no_divergence_is_not_applicable(self) -> None:
        fixture = deepcopy(self.fixtures["AG_TIMELY_CONTEST_ROUTE"])
        fixture["fixture_id"] = "AP_NO_DIVERGENCE"
        fixture["authority_contestability_evidence"]["conflict_status"] = (
            "NO_DIVERGENCE"
        )
        result = check_authority_contestability(fixture)
        self.assertEqual("PASS", result.status)
        self.assertEqual(
            "NOT_APPLICABLE_NO_DIVERGENCE", result.contestability_status
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
