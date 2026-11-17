import copy
import json
import unittest
import build_views
import check_reviews


class ReviewAnchorTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((check_reviews.ROOT / 'review-decisions.json').read_text())
        self.source = build_views.SOURCE.read_bytes()
        self.candidate = build_views.CANDIDATE.read_bytes()
        self.exists = lambda name: (check_reviews.ROOT / name).is_file()

    def test_current_reviews_are_anchored_and_only_partial(self):
        reviewed, total = check_reviews.validate(self.data, self.source, self.candidate, self.exists)
        self.assertGreater(reviewed, 0)
        self.assertGreater(total, reviewed)

    def test_changed_source_or_candidate_invalidates_reviews(self):
        for source, candidate in ((self.source + b'change', self.candidate),
                                  (self.source, self.candidate + b'change')):
            with self.subTest(source_changed=source != self.source):
                with self.assertRaises(ValueError):
                    check_reviews.validate(self.data, source, candidate, self.exists)

    def test_invalid_ledger_shapes_fail_but_explicit_empty_is_valid(self):
        invalid = []
        for name, value in [('schema', True), ('reviews', {}), ('reviews', ''), ('reviews', None)]:
            data = copy.deepcopy(self.data)
            data[name] = value
            invalid.append(data)
        missing = copy.deepcopy(self.data)
        del missing['reviews']
        invalid.append(missing)
        for data in invalid:
            with self.subTest(data=data):
                with self.assertRaises(ValueError):
                    check_reviews.validate(data, self.source, self.candidate, self.exists)
        data = copy.deepcopy(self.data)
        data['reviews'] = []
        self.assertEqual(check_reviews.validate(data, self.source, self.candidate, self.exists), (0, 206))

    def test_duplicate_json_fields_are_rejected(self):
        with self.assertRaises(ValueError):
            json.loads('{"reviews": [1], "reviews": []}', object_pairs_hook=check_reviews.unique_object)

    def test_duplicate_block_missing_gap_and_wrong_hash_are_rejected(self):
        for corruption in ('duplicate', 'gap', 'hash', 'evidence'):
            data = copy.deepcopy(self.data)
            if corruption == 'duplicate': data['reviews'].append(copy.deepcopy(data['reviews'][0]))
            if corruption == 'gap': data['reviews'][0]['remaining'] = ''
            if corruption == 'hash': data['reviews'][0]['block_sha256'] = 'incorrect'
            if corruption == 'evidence': data['reviews'][0]['evidence'] = '../SEMANTIC-REVIEW.md'
            with self.subTest(corruption=corruption):
                with self.assertRaises(ValueError):
                    check_reviews.validate(data, self.source, self.candidate, self.exists)
