"""Regression checks for the authored exp.5 booking extract, not field outcomes."""

from html.parser import HTMLParser
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parent
CASE = "navigator-0.6.1-exp.5"
REASON_TERMS = ("day left", "afternoon", "evening", "rest of the day", "rest_of_day", "daylight")


class EncounterRecords(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = None
        self.records = []

    def handle_starttag(self, tag, attrs):
        if tag == "script" and dict(attrs).get("id") == "trace-encounter":
            self.parts = []

    def handle_data(self, data):
        if self.parts is not None:
            self.parts.append(data)

    def handle_endtag(self, tag):
        if tag == "script" and self.parts is not None:
            self.records.append("".join(self.parts))
            self.parts = None


class NavigatorBookingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = (ROOT / f"{CASE}.json").read_bytes()
        cls.record = json.loads(cls.raw)

    def test_standalone_record_matches_the_single_html_extract(self):
        parser = EncounterRecords()
        parser.feed((ROOT / f"{CASE}.html").read_text(encoding="utf-8"))
        self.assertEqual(len(parser.records), 1)
        self.assertEqual(parser.records[0].strip().encode("utf-8"), self.raw.strip())

    def test_booking_excludes_the_known_private_evening_leaks(self):
        # Guard known leaks and listed rewordings in this authored case.
        # A term list cannot establish general privacy.
        self.assertNotEqual(self.record["case"], "Some of the day left")
        self.assertNotIn('"rest_of_day"', json.dumps(self.record))
        text = json.dumps(self.record).lower()
        self.assertEqual([term for term in REASON_TERMS if term in text], [])
        self.assertEqual(
            self.record["departure_correction"]["forwarding_scope"],
            "departure time for booking",
        )

    def test_ordinary_return_distinguishes_unoffered_from_declined_or_unknown(self):
        ordinary = self.record["histories"]["ordinary-return"]
        self.assertIsNone(ordinary["learner_accepted_earlier_at"])
        self.assertEqual(ordinary.get("earlier_offer_status"), "not offered before booking locked")
        self.assertEqual(ordinary.get("check_status"), "not done; recorded as outstanding")
        self.assertEqual(self.record["event_sources"]["earlier_offer_status"], "duty organiser return")
        self.assertEqual(self.record["event_sources"]["check_status"], "duty organiser return")

    def test_timely_check_fits_agreement_booking_and_departure_limit(self):
        timely = self.record["histories"]["reach-organiser"]
        offer = self.record["facilitator_offer"]
        self.assertTrue(offer["requires_learner_agreement"])
        self.assertLessEqual(timely["organiser_received_at"], timely["learner_accepted_earlier_at"])
        self.assertLessEqual(timely["learner_accepted_earlier_at"], timely["booking_changed_at"])
        self.assertLess(timely["booking_changed_at"], self.record["booking"]["amend_before"])
        self.assertLessEqual(self.record["attempt_end"], timely["check_start"])
        self.assertIn(timely["check_start"], offer["start_times"])
        self.assertEqual(timely["check_completed_at"], timely["check_start"] + offer["duration"])
        self.assertLessEqual(
            timely["check_completed_at"],
            self.record["departure_correction"]["departure_no_later_than"],
        )

    def test_late_return_has_no_observed_check_completion(self):
        ordinary = self.record["histories"]["ordinary-return"]
        booking = self.record["booking"]
        self.assertGreaterEqual(ordinary["organiser_received_at"], booking["amend_before"])
        self.assertIsNone(ordinary["booking_changed_at"])
        self.assertIsNone(ordinary["check_start"])
        self.assertIsNone(ordinary["check_completed_at"])
        self.assertGreater(
            booking["scheduled_check_start"] + self.record["facilitator_offer"]["duration"],
            self.record["departure_correction"]["departure_no_later_than"],
        )

    def test_home_performance_and_support_remain_unresolved(self):
        for field in ("home_capability", "qualified_help_at_home"):
            with self.subTest(field=field):
                self.assertEqual(self.record["handoff"][field], "unresolved")


if __name__ == "__main__":
    unittest.main()
