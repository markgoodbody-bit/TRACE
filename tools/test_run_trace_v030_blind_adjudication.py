import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("run_trace_v030_blind_adjudication.py")
SPEC = importlib.util.spec_from_file_location("adjudication_runner", MODULE_PATH)
assert SPEC and SPEC.loader
runner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(runner)


class BlindAdjudicationRunnerTests(unittest.TestCase):
    def test_extract_strict_json(self):
        ok, value = runner.extract_strict_json('{"packet_id":"PAIR-X"}')
        self.assertTrue(ok)
        self.assertEqual(value["packet_id"], "PAIR-X")

    def test_markdown_fence_is_not_strict_json(self):
        ok, value = runner.extract_strict_json('```json\n{"packet_id":"PAIR-X"}\n```')
        self.assertFalse(ok)
        self.assertIsNone(value)

    def test_manifest_rejects_sealed_material(self):
        manifest = {
            "studyId": runner.EXPECTED_STUDY_ID,
            "sourceBlindPacketSetIdSha256": runner.EXPECTED_PACKET_SET_SHA256,
            "sealedArmKeySha256": runner.EXPECTED_SEALED_KEY_SHA256,
            "armKeyIncluded": True,
            "deltaNotesIncluded": False,
            "jobs": [],
        }
        with self.assertRaises(ValueError):
            runner.validate_manifest(manifest)


if __name__ == "__main__":
    unittest.main()
