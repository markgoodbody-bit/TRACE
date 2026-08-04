from __future__ import annotations

import json
import unittest
from copy import deepcopy

from validate_candidate import (
    DEFAULT_BASE_SEED,
    DEFAULT_MANIFEST,
    DEFAULT_PATCH,
    DEFAULT_README,
    DEFAULT_REGRESSION,
    validate_manifest,
    validate_paths,
)


class TraceV026TransitionCandidateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(DEFAULT_MANIFEST.read_text(encoding="utf-8"))
        cls.base_seed_text = DEFAULT_BASE_SEED.read_text(encoding="utf-8")
        cls.patch_text = DEFAULT_PATCH.read_text(encoding="utf-8")
        cls.regression_text = DEFAULT_REGRESSION.read_text(encoding="utf-8")
        cls.readme_text = DEFAULT_README.read_text(encoding="utf-8")

    def validate(self, manifest: dict):
        return validate_manifest(
            manifest,
            base_seed_text=self.base_seed_text,
            patch_text=self.patch_text,
            regression_text=self.regression_text,
            readme_text=self.readme_text,
        )

    def test_candidate_package_passes(self) -> None:
        result = validate_paths()
        self.assertEqual("PASS", result.status)
        self.assertEqual([], result.errors)
        self.assertEqual(["F03", "F04"], result.details["primary_core_repairs"])
        self.assertEqual("TRACE-GRAPH-0.2.6", result.details["target_packet_schema"])
        self.assertEqual(
            "SYNCHRONIZED_IDENTIFIER_BUMP", result.details["version_strategy"]
        )

    def test_missing_source_anchor_fails(self) -> None:
        manifest = deepcopy(self.manifest)
        manifest["source_anchors"].append("## [99.9] Invented anchor")
        result = self.validate(manifest)
        self.assertEqual("FAIL", result.status)
        self.assertTrue(any("missing source anchors" in error for error in result.errors))

    def test_duplicate_finding_fails(self) -> None:
        manifest = deepcopy(self.manifest)
        manifest["findings"].append(deepcopy(manifest["findings"][0]))
        result = self.validate(manifest)
        self.assertEqual("FAIL", result.status)
        self.assertIn("finding ids must be unique", result.errors)

    def test_schema_shape_growth_fails(self) -> None:
        manifest = deepcopy(self.manifest)
        manifest["minimum_schema_shape_change"] = True
        result = self.validate(manifest)
        self.assertEqual("FAIL", result.status)
        self.assertTrue(any("schema shape change" in error for error in result.errors))

    def test_new_required_packet_field_fails(self) -> None:
        manifest = deepcopy(self.manifest)
        manifest["new_required_packet_fields"] = ["target_set_aperture"]
        result = self.validate(manifest)
        self.assertEqual("FAIL", result.status)
        self.assertIn("new_required_packet_fields must remain empty", result.errors)

    def test_unbounded_core_promotion_fails(self) -> None:
        manifest = deepcopy(self.manifest)
        finding = next(item for item in manifest["findings"] if item["id"] == "F08")
        finding["primary"] = "CORE_REPAIR"
        result = self.validate(manifest)
        self.assertEqual("FAIL", result.status)
        self.assertTrue(any("F03 and F04" in error for error in result.errors))

    def test_unsynchronised_version_strategy_fails(self) -> None:
        manifest = deepcopy(self.manifest)
        manifest["version_strategy"] = "FORMAL_ONLY"
        result = self.validate(manifest)
        self.assertEqual("FAIL", result.status)
        self.assertTrue(any("SYNCHRONIZED_IDENTIFIER_BUMP" in error for error in result.errors))

    def test_wrong_packet_schema_target_fails(self) -> None:
        manifest = deepcopy(self.manifest)
        manifest["target_packet_schema"] = "TRACE-GRAPH-0.2.5"
        result = self.validate(manifest)
        self.assertEqual("FAIL", result.status)
        self.assertIn("target_packet_schema must be TRACE-GRAPH-0.2.6", result.errors)

    def test_release_gate_cannot_be_dropped(self) -> None:
        manifest = deepcopy(self.manifest)
        manifest["release_gate"]["requires_human_release_authority"] = False
        result = self.validate(manifest)
        self.assertEqual("FAIL", result.status)
        self.assertIn("release_gate must retain all four explicit gates", result.errors)


if __name__ == "__main__":
    unittest.main(verbosity=2)
