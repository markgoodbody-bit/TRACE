import unittest

from choice_history import BRAKES, OPTIONS, PUNCTURES, compare


class ChoiceHistoryTests(unittest.TestCase):
    def test_same_observed_choice_warrants_different_accounts(self):
        open_menu = compare(OPTIONS, PUNCTURES, OPTIONS)
        restricted_menu = compare((PUNCTURES,), PUNCTURES, OPTIONS)
        self.assertEqual(open_menu["observed_choice"], restricted_menu["observed_choice"])
        self.assertEqual(open_menu["compatible_rankings"], [[PUNCTURES, BRAKES]])
        self.assertEqual(open_menu["possible_next_choices"], [PUNCTURES])
        self.assertEqual(len(restricted_menu["compatible_rankings"]), 2)
        self.assertCountEqual(restricted_menu["possible_next_choices"], OPTIONS)

    def test_display_without_support_leaves_the_usable_menu_restricted(self):
        result = compare((PUNCTURES,), PUNCTURES, (PUNCTURES,))
        self.assertEqual(len(result["compatible_rankings"]), 2)
        self.assertEqual(result["possible_next_choices"], [PUNCTURES])

    def test_unknown_options_and_impossible_observations_are_rejected(self):
        with self.assertRaises(ValueError):
            compare((PUNCTURES,), BRAKES, OPTIONS)
        with self.assertRaises(ValueError):
            compare(OPTIONS, PUNCTURES, ("unmodelled option",))


if __name__ == "__main__":
    unittest.main()
