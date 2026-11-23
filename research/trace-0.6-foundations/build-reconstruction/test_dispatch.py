import unittest
from dataclasses import replace

from dispatch import DispatchTimeline, evaluate


class DispatchTests(unittest.TestCase):
    def test_same_acknowledgement_supports_different_actions(self):
        pending = DispatchTimeline()
        confirmed = replace(pending, hold_effective_at=17, dispatch_confirmed_at=18)
        pending_view = evaluate(pending, 18)
        confirmed_view = evaluate(confirmed, 18)
        self.assertEqual(pending_view["planning_acknowledged_at"],
                         confirmed_view["planning_acknowledged_at"])
        self.assertEqual(pending_view["hold"], "UNKNOWN")
        self.assertIn("call the duty line", pending_view["next_action"])
        self.assertEqual(confirmed_view["hold"], "CONFIRMED_BEFORE_RELEASE")
        self.assertIn("plan a usable North option", confirmed_view["next_action"])
        self.assertEqual(pending_view["south_hall"], confirmed_view["south_hall"])

    def test_call_deadline_and_release_boundary_have_separate_jobs(self):
        pending = DispatchTimeline()
        self.assertTrue(evaluate(pending, 22)["duty_line_available"])
        self.assertFalse(evaluate(pending, 23)["duty_line_available"])
        timely = replace(pending, duty_line_called_at=22,
                         hold_effective_at=29, dispatch_confirmed_at=31)
        equal = replace(timely, hold_effective_at=30)
        self.assertEqual(evaluate(timely, 31)["hold"], "CONFIRMED_BEFORE_RELEASE")
        late_view = evaluate(equal, 31)
        self.assertEqual(late_view["hold"], "CONFIRMED_AT_OR_AFTER_RELEASE")
        self.assertIn("North Hall households", late_view["burden_to_check"])

    def test_effect_can_precede_confirmation(self):
        called = DispatchTimeline(duty_line_called_at=22, hold_effective_at=27,
                                  dispatch_confirmed_at=29)
        waiting = evaluate(called, 28)
        self.assertIsNone(waiting["confirmed_effect_at"])
        self.assertEqual(waiting["hold"], "UNKNOWN")
        self.assertIn("seek dispatch confirmation", waiting["next_action"])
        earlier = replace(called, dispatch_confirmed_at=28)
        self.assertEqual(evaluate(earlier, 28)["hold"], "CONFIRMED_BEFORE_RELEASE")
        known = evaluate(called, 29)
        self.assertEqual(known["confirmed_effect_at"], 27)
        self.assertEqual(known["dispatch_confirmed_at"], 29)

    def test_late_authority_and_delayed_warning_change_the_next_action(self):
        ready = DispatchTimeline(planning_request_at=None, planning_acknowledged_at=None)
        self.assertIn("call the duty line", evaluate(ready, 18)["next_action"])
        no_authority = replace(ready, hold_authority_at=32)
        early = evaluate(no_authority, 18)
        self.assertEqual(early["venue_warning_received_at"], 14)
        self.assertIsNone(early["hold_authority_at"])
        self.assertIn("hand off to the duty holder", early["next_action"])
        delayed = replace(DispatchTimeline(), warning_received_at=19)
        self.assertIsNone(evaluate(delayed, 18)["venue_warning_recorded_at"])
        self.assertIn("check the venue's own record", evaluate(delayed, 18)["next_action"])

    def test_missing_readback_after_release_keeps_effect_unknown(self):
        view = evaluate(DispatchTimeline(), 32)
        self.assertEqual(view["hold"], "UNKNOWN")
        self.assertFalse(view["duty_line_available"])
        self.assertIn("check the dispatch outcome", view["next_action"])
        self.assertEqual(view["south_hall"], "continue")

    def test_reject_out_of_order_or_unsupported_events(self):
        for events in (
            {"warning_received_at": 11},
            {"hold_authority_at": 32},
            {"planning_acknowledged_at": 15},
            {"hold_effective_at": 15},
            {"hold_effective_at": 20, "dispatch_confirmed_at": 19},
            {"dispatch_confirmed_at": 18},
            {"duty_line_called_at": True},
        ):
            with self.subTest(events=events), self.assertRaises(ValueError):
                DispatchTimeline(**events)


if __name__ == "__main__":
    unittest.main()
