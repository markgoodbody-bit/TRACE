import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("build_trace_v030_blind_adjudication_packets.py")
SPEC = importlib.util.spec_from_file_location("blind_builder", MODULE_PATH)
assert SPEC and SPEC.loader
builder = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(builder)


class BlindPacketBuilderTests(unittest.TestCase):
    def test_split_delta_heading(self):
        main, delta = builder.split_delta("Main answer.\n\n### TRACE_DELTA_NOTE\nReason.\n", True)
        self.assertEqual(main, "Main answer.")
        self.assertEqual(delta, "### TRACE_DELTA_NOTE\nReason.")

    def test_split_delta_inline(self):
        main, delta = builder.split_delta("Main answer.\nTRACE_DELTA_NOTE: Reason.\n", True)
        self.assertEqual(main, "Main answer.")
        self.assertEqual(delta, "TRACE_DELTA_NOTE: Reason.")

    def test_arm_a_rejects_delta(self):
        with self.assertRaises(ValueError):
            builder.split_delta("Main.\nTRACE_DELTA_NOTE: no\n", False)

    def test_creditable_prefix_exact_word_boundary(self):
        text = " ".join(f"w{i}" for i in range(1202))
        prefix, tail = builder.split_creditable_prefix(text)
        self.assertEqual(builder.word_count(prefix), 1200)
        self.assertEqual(builder.word_count(tail), 2)
        self.assertEqual(prefix + tail, text)

    def test_short_answer_has_no_tail(self):
        prefix, tail = builder.split_creditable_prefix("one two three")
        self.assertEqual(prefix, "one two three")
        self.assertEqual(tail, "")


if __name__ == "__main__":
    unittest.main()
