from __future__ import annotations

import json
import unittest
from pathlib import Path

from checker import FAIL_UNACCOUNTED, FAIL_UNSUPPORTED, check_envelope

FIXTURE_FILE = Path(__file__).resolve().parent / "fixtures.json"


class TransitionClassAccountingRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        bundle = json.loads(FIXTURE_FILE.read_text(encoding="utf-8"))
        cls.fixtures = {item["fixture_id"]: item for item in bundle["fixtures"]}

    def check_expected(self, fixture_id: str):
        envelope = self.fixtures[fixture_id]
        result = check_envelope(envelope)
        expected = envelope["expected"]
        self.assertEqual(expected["status"], result.status, fixture_id)
        self.assertEqual(expected["failure_codes"], result.failure_codes, fixture_id)
        return result

    def test_a_full_accounting(self) -> None:
        self.check_expected("A_FULL_ACCOUNTING")

    def test_b_emergency_bypass(self) -> None:
        self.check_expected("B_EMERGENCY_BYPASS")

    def test_c_no_known_source(self) -> None:
        result = self.check_expected("C_NO_KNOWN_SOURCE")
        info = result.classes["INFORMATION"]
        self.assertEqual("ACCOUNTED", info.accounting_status)
        self.assertEqual("NOT_ASSESSABLE", info.availability_status)

    def test_d_silent_omission(self) -> None:
        result = self.check_expected("D_SILENT_OMISSION")
        self.assertEqual([FAIL_UNACCOUNTED], result.failure_codes)
        info = result.classes["INFORMATION"]
        self.assertEqual("UNACCOUNTED", info.accounting_status)
        self.assertEqual("MATERIALLY_LIVE_UNREPRESENTED", info.availability_status)

    def test_e_false_excuse(self) -> None:
        result = self.check_expected("E_FALSE_EXCUSE")
        self.assertEqual([FAIL_UNSUPPORTED], result.failure_codes)
        self.assertEqual("UNSUPPORTED_STATUS", result.classes["INFORMATION"].accounting_status)

    def test_f_hidden_world_is_not_checker_failure(self) -> None:
        result = self.check_expected("F_HIDDEN_WORLD")
        info = result.classes["INFORMATION"]
        self.assertEqual("NO_CHECKER_FAILURE", info.accounting_status)
        self.assertEqual("NOT_ASSESSABLE", info.availability_status)

    def test_wait_delay_inaction_are_assessed_by_node_mode(self) -> None:
        result = self.check_expected("A_FULL_ACCOUNTING")
        self.assertEqual(["n_t_wait"], result.classes["WAIT"].represented_transition_refs)
        self.assertEqual([], result.classes["DELAY"].represented_transition_refs)
        self.assertEqual([], result.classes["INACTION"].represented_transition_refs)
        self.assertEqual("ACCOUNTED", result.classes["DELAY"].accounting_status)
        self.assertEqual("ACCOUNTED", result.classes["INACTION"].accounting_status)


if __name__ == "__main__":
    unittest.main(verbosity=2)
