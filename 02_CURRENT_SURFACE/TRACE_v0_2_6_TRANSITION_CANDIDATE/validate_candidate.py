#!/usr/bin/env python3
"""Validate the bounded TRACE v0.2.6 transition candidate."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping

CANDIDATE_DIR = Path(__file__).resolve().parent
REPO_ROOT = CANDIDATE_DIR.parents[1]
DEFAULT_MANIFEST = CANDIDATE_DIR / "candidate_manifest.json"
DEFAULT_BASE_SEED = REPO_ROOT / "TRACE_FORMAL_SEED_v0_2_5.md"
DEFAULT_PATCH = CANDIDATE_DIR / "02_NARROW_FORMAL_PATCH.md"
DEFAULT_REGRESSION = CANDIDATE_DIR / "03_REGRESSION_CONTRACT.md"
DEFAULT_README = CANDIDATE_DIR / "README.md"

EXPECTED_FINDINGS = {f"F{number:02d}" for number in range(1, 13)}
EXPECTED_PRIMARY_CORE = {"F03", "F04"}
EXPECTED_PATCH_TOKENS = {
    "TARGET_SET != WORLD_SCOPE",
    "INFORMATION_TRANSITION_REPRESENTED",
    "DIVERGENT_READINGS != AUTHORITY",
    "ROUTE_TO_BRAKE != CORRECTION_COMPLETED",
    "record_target_set_apertures_and_alternatives(R)",
    "Every material search-coverage claim references a target-set aperture",
}
EXPECTED_REGRESSION_IDS = {
    *(f"R{number:02d}" for number in range(1, 13)),
    *(f"V26-{letter}" for letter in "ABCDEFGH"),
}


@dataclass(slots=True)
class ValidationResult:
    status: str
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    details: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "candidate_id": "TRACE-V0.2.6-TRANSITION-CANDIDATE-001",
            "status": self.status,
            "errors": self.errors,
            "warnings": self.warnings,
            "details": self.details,
        }


def _load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def validate_manifest(
    manifest: Mapping[str, Any],
    *,
    base_seed_text: str,
    patch_text: str,
    regression_text: str,
    readme_text: str,
) -> ValidationResult:
    errors: list[str] = []
    warnings: list[str] = []

    if manifest.get("candidate_id") != "TRACE-V0.2.6-TRANSITION-CANDIDATE-001":
        errors.append("candidate_id mismatch")
    if manifest.get("status") != "WORKING_CANDIDATE":
        errors.append("status must remain WORKING_CANDIDATE")
    if manifest.get("target_formal_version") != "0.2.6":
        errors.append("target_formal_version must be 0.2.6")
    if manifest.get("compiled_seed_present") is not False:
        errors.append("transition candidate must not claim a compiled seed is present")
    if manifest.get("minimum_schema_shape_change") is not False:
        errors.append("minimum schema shape change is unsupported by this candidate")

    for key in (
        "new_node_types",
        "new_edge_types",
        "new_ports",
        "new_required_packet_fields",
    ):
        if manifest.get(key) != []:
            errors.append(f"{key} must remain empty")

    allowed = manifest.get("allowed_destinations")
    if not isinstance(allowed, list) or not all(isinstance(item, str) for item in allowed):
        errors.append("allowed_destinations must be an array of strings")
        allowed_set: set[str] = set()
    else:
        allowed_set = set(allowed)

    findings = manifest.get("findings")
    if not isinstance(findings, list):
        errors.append("findings must be an array")
        findings = []

    finding_ids: list[str] = []
    primary_core: set[str] = set()
    for index, item in enumerate(findings):
        if not isinstance(item, dict):
            errors.append(f"finding {index} must be an object")
            continue
        finding_id = item.get("id")
        if not isinstance(finding_id, str):
            errors.append(f"finding {index} has no string id")
            continue
        finding_ids.append(finding_id)
        primary = item.get("primary")
        secondary = item.get("secondary")
        if primary not in allowed_set:
            errors.append(f"{finding_id} primary destination is not allowed")
        if primary == "CORE_REPAIR":
            primary_core.add(finding_id)
        if not isinstance(secondary, list) or any(
            destination not in allowed_set for destination in secondary
        ):
            errors.append(f"{finding_id} secondary destinations are invalid")

    if set(finding_ids) != EXPECTED_FINDINGS:
        missing = sorted(EXPECTED_FINDINGS - set(finding_ids))
        extra = sorted(set(finding_ids) - EXPECTED_FINDINGS)
        errors.append(f"finding closure mismatch; missing={missing}, extra={extra}")
    if len(finding_ids) != len(set(finding_ids)):
        errors.append("finding ids must be unique")
    if primary_core != EXPECTED_PRIMARY_CORE:
        errors.append(
            "primary CORE_REPAIR findings must be exactly F03 and F04; "
            f"observed={sorted(primary_core)}"
        )

    anchors = manifest.get("source_anchors")
    if not isinstance(anchors, list) or not all(isinstance(item, str) for item in anchors):
        errors.append("source_anchors must be an array of strings")
        anchors = []
    missing_anchors = [anchor for anchor in anchors if anchor not in base_seed_text]
    if missing_anchors:
        errors.append("base seed is missing source anchors: " + ", ".join(missing_anchors))

    missing_patch_tokens = sorted(
        token for token in EXPECTED_PATCH_TOKENS if token not in patch_text
    )
    if missing_patch_tokens:
        errors.append("narrow patch is missing required tokens: " + ", ".join(missing_patch_tokens))

    missing_regression_ids = sorted(
        token for token in EXPECTED_REGRESSION_IDS if token not in regression_text
    )
    if missing_regression_ids:
        errors.append(
            "regression contract is missing ids: " + ", ".join(missing_regression_ids)
        )

    for forbidden in ("Status: **RELEASED**", "Status: **CANON**", "validated and ready"):
        if forbidden in readme_text:
            errors.append(f"README contains forbidden promotion: {forbidden}")

    release_gate = manifest.get("release_gate")
    if not isinstance(release_gate, dict) or not all(
        release_gate.get(key) is True
        for key in (
            "requires_full_seed_compilation",
            "requires_version_strategy_decision",
            "requires_regression_pass",
            "requires_human_release_authority",
        )
    ):
        errors.append("release_gate must retain all four explicit gates")

    if not errors and "minimum schema shape remains identical" not in patch_text:
        warnings.append("patch should continue to state that schema shape remains identical")

    return ValidationResult(
        status="FAIL" if errors else "PASS",
        errors=errors,
        warnings=warnings,
        details={
            "finding_count": len(findings),
            "primary_core_repairs": sorted(primary_core),
            "source_anchor_count": len(anchors),
            "minimum_schema_shape_change": manifest.get("minimum_schema_shape_change"),
            "compiled_seed_present": manifest.get("compiled_seed_present"),
        },
    )


def validate_paths(
    *,
    manifest_path: Path = DEFAULT_MANIFEST,
    base_seed_path: Path = DEFAULT_BASE_SEED,
    patch_path: Path = DEFAULT_PATCH,
    regression_path: Path = DEFAULT_REGRESSION,
    readme_path: Path = DEFAULT_README,
) -> ValidationResult:
    try:
        manifest = _load_json(manifest_path)
        base_seed_text = base_seed_path.read_text(encoding="utf-8")
        patch_text = patch_path.read_text(encoding="utf-8")
        regression_text = regression_path.read_text(encoding="utf-8")
        readme_text = readme_path.read_text(encoding="utf-8")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        return ValidationResult(status="INPUT_ERROR", errors=[str(exc)])

    return validate_manifest(
        manifest,
        base_seed_text=base_seed_text,
        patch_text=patch_text,
        regression_text=regression_text,
        readme_text=readme_text,
    )


def _main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args(argv)

    result = validate_paths()
    print(json.dumps(result.to_dict(), indent=None if args.compact else 2, sort_keys=True))
    if result.status == "PASS":
        return 0
    if result.status == "INPUT_ERROR":
        return 2
    return 1


if __name__ == "__main__":
    raise SystemExit(_main())
