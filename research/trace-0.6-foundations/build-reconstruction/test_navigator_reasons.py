import unittest
from fractions import Fraction

from navigator_reasons import Offer, compare


class NavigatorReasonsTests(unittest.TestCase):
    def test_same_offers_reverse_rank_when_aim_changes(self):
        result = compare(Offer.CONFIRMED)
        self.assertIsNotNone(result.practice)
        self.assertEqual(result.practice.attendance - result.demonstration.attendance, Fraction(-1, 2))
        self.assertEqual(
            result.practice.independent_attempt - result.demonstration.independent_attempt,
            Fraction(1, 2),
        )

    def test_declined_and_unresolved_offers_remain_distinct(self):
        for status in (Offer.DECLINED, Offer.UNCONFIRMED):
            with self.subTest(status=status):
                result = compare(status)
                self.assertIs(result.facilitator_offer, status)
                self.assertIsNone(result.practice)
                self.assertEqual(result.demonstration.attendance, 1)

    def test_window_includes_the_completion_minute(self):
        result = compare(Offer.CONFIRMED, (19, 20, 39, 40))
        self.assertEqual(result.demonstration.attendance, Fraction(3, 4))
        self.assertIsNotNone(result.practice)
        self.assertEqual(result.practice.independent_attempt, Fraction(1, 4))

    def test_missing_windows_cannot_supply_probabilities(self):
        for windows in ((), (-1,)):
            with self.subTest(windows=windows):
                with self.assertRaises(ValueError):
                    compare(Offer.CONFIRMED, windows)
