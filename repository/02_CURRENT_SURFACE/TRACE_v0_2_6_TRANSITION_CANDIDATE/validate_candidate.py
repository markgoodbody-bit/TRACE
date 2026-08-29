#!/usr/bin/env python3
"""Check TRACE v0.2.6 transition-package integrity and declared contract.

This executable does not validate the truth, adequacy, or operational effect of
the candidate's formal argument. Its scope is intentionally limited to package
integrity, bounded manifest closure, source anchors, and release gates.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping

CANDIDATE_DIR = Path(__file__).resolve().parent
REPO_ROOT = CANDIDATE_DIR.parents[1]
DEFAULT_MANIFEST = CANDIDATE_DIR / "candidate_manifest.json"
DEFAULT_BASE_SEED = REPO_ROOT / "TRACE_FORMAL_SEED_v0_2_5.md"
DEFAULT_MATRIX = CANDIDATE_DIR / "01_DISPOSITION_MATRIX.md"
DEFAULT_PATCH = CANDIDATE_DIR / "02_NARROW_FORMAL_PATCH.md"
DEFAULT_REGRESSION = CANDIDATE_DIR / "03_REGRESSION_CONTRACT.md"
DEFAULT_README = CANDIDATE_DIR / "README.md"

CHECK_SCOPE = "PACKAGE_INTEGRITY_AND_DECLARED_CONTRACT_ONLY"
EXPECTED_FINDINGS = {f"F{number:02d}" for number in range(1, 13)}
EXPECTED_PRIMARY_CORE = {"F03", "F04"}
EXPECTED_REGRESSION_IDS = {
    *(f"R{number:02d}" for number in range(1, 13)),
    *(f"V26-{letter}" for letter in "ABCDEFGH"),
}
EXPECTED_PATCH_SECTIONS = list("ABCDEFG")
EXPECTED_VERSION_STRATEGY = "SYNCHRONIZED_IDENTIFIER_BUMP"
EXPECTED_PACKET_SCHEMA = "TRACE-GRAPH-0.2.6"
EXPECTED_DIGEST_ARTIFACTS = {
    "01_DISPOSITION_MATRIX.md",
    "02_NARROW_FORMAL_PATCH.md",
    "03_REGRESSION_CONTRACT.md",
}
EXPECTED_PATCH_PHRASES = {
    "TARGET_SET != WORLD_SCOPE",
    "INFORMATION_TRANSITION_REPRESENTED != OUTWARD_SEARCH_COVERAGE",
    "DIVERGENT_READINGS != AUTHORITY",
    "ROUTE_TO_BRAKE != CORRECTION_COMPLETED",
    "record_target_set_apertures_and_alternatives(R)",
    "Every material search-coverage claim references a target-set aperture",
    "TRACE-GRAPH-0.2.5 -> TRACE-GRAPH-0.2.6",
    "minimum_schema_shape_change: false",
}
EXPECTED_MATRIX_PHRASES = {
    "## Containment test for F03 and F04",
    "target_set_source_ref",
    "known_omitted_target_categories",
    "If a full-seed compilation cannot preserve that specialization using existing objects",
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
            "check_scope": CHECK_SCOPE,
            "status": self.status,
            "errors": self.errors,
            "warnings": self.warnings,
            "details": self.details,
        }


def normalize_text(value: str) -> str:
    """Collapse all Unicode whitespace for non-semantic integrity comparison."""
    return re.sub(r"\s+", " ", value).strip()


def normalized_sha256(value: str) -> str:
    return hashlib.sha256(normalize_text(value).encode("utf-8")).hexdigest()


def _contains_normalized(text: str, phrase: str) -> bool:
    return normalize_text(phrase) in normalize_text(text)


def _load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def _extract_regression_sections(text: str) -> dict[str, str]:
    lines = text.splitlines()
    starts: list[tuple[int, str]] = []
    pattern = re.compile(r"^###\s+(R\d{2}|V26-[A-H])\b")
    for index, line in enumerate(lines):
        match = pattern.match(line)
        if match:
            starts.append((index, match.group(1)))

    sections: dict[str, str] = {}
    for offset, (start, section_id) in enumerate(starts):
        end = starts[offset + 1][0] if offset + 1 < len(starts) else len(lines)
        sections[section_id] = "\n".join(lines[start + 1 : end]).strip()
    return sections


def _extract_patch_sections(text: str) -> list[str]:
    pattern = re.compile(r"^##\s+Patch\s+([A-G])\b")
    return [
        match.group(1)
        for line in text.splitlines()
        if (match := pattern.match(line)) is not None
    ]


def validate_manifest(
    manifest: Mapping[str, Any],
    *,
    base_seed_text: str,
    matrix_text: str,
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
    if manifest.get("check_scope") != CHECK_SCOPE:
        errors.append(f"check_scope must be {CHECK_SCOPE}")
    if manifest.get("target_formal_version") != "0.2.6":
        errors.append("target_formal_version must be 0.2.6")
    if manifest.get("target_packet_schema") != EXPECTED_PACKET_SCHEMA:
        errors.append(f"target_packet_schema must be {EXPECTED_PACKET_SCHEMA}")
    if manifest.get("version_strategy") != EXPECTED_VERSION_STRATEGY:
        errors.append(f"version_strategy must be {EXPECTED_VERSION_STRATEGY}")
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

    containment = manifest.get("containment_test")
    if not isinstance(containment, dict):
        errors.append("containment_test must be an object")
    else:
        if containment.get("finding_ids") != ["F03", "F04"]:
            errors.append("containment_test finding_ids must be exactly F03 and F04")
        for key in ("v025_general_rules", "nonduplicative_specialization"):
            values = containment.get(key)
            if not isinstance(values, list) or len(values) < 3 or not all(
                isinstance(item, str) and item.strip() for item in values
            ):
                errors.append(f"containment_test {key} must contain at least three strings")

    for phrase in EXPECTED_MATRIX_PHRASES:
        if not _contains_normalized(matrix_text, phrase):
            errors.append(f"disposition matrix is missing containment content: {phrase}")

    patch_sections = _extract_patch_sections(patch_text)
    if patch_sections != EXPECTED_PATCH_SECTIONS:
        errors.append(
            "patch section closure mismatch; "
            f"expected={EXPECTED_PATCH_SECTIONS}, observed={patch_sections}"
        )
    for phrase in EXPECTED_PATCH_PHRASES:
        if not _contains_normalized(patch_text, phrase):
            errors.append(f"narrow patch is missing normalized phrase: {phrase}")

    regression_sections = _extract_regression_sections(regression_text)
    observed_regression_ids = set(regression_sections)
    if observed_regression_ids != EXPECTED_REGRESSION_IDS:
        missing = sorted(EXPECTED_REGRESSION_IDS - observed_regression_ids)
        extra = sorted(observed_regression_ids - EXPECTED_REGRESSION_IDS)
        errors.append(f"regression section closure mismatch; missing={missing}, extra={extra}")
    for section_id, body in regression_sections.items():
        word_count = len(re.findall(r"\b[\w-]+\b", body))
        if word_count < 8:
            errors.append(f"{section_id} regression body is substantively empty")

    digest_map = manifest.get("normalized_artifact_sha256")
    if not isinstance(digest_map, dict) or set(digest_map) != EXPECTED_DIGEST_ARTIFACTS:
        errors.append(
            "normalized_artifact_sha256 must contain exactly: "
            + ", ".join(sorted(EXPECTED_DIGEST_ARTIFACTS))
        )
        digest_map = {}

    artifact_texts = {
        "01_DISPOSITION_MATRIX.md": matrix_text,
        "02_NARROW_FORMAL_PATCH.md": patch_text,
        "03_REGRESSION_CONTRACT.md": regression_text,
    }
    for name, text in artifact_texts.items():
        expected_digest = digest_map.get(name)
        observed_digest = normalized_sha256(text)
        if expected_digest != observed_digest:
            errors.append(
                f"normalized artifact digest mismatch for {name}; "
                f"expected={expected_digest}, observed={observed_digest}"
            )

    for forbidden in ("Status: **RELEASED**", "Status: **CANON**", "validated and ready"):
        if forbidden in readme_text:
            errors.append(f"README contains forbidden promotion: {forbidden}")

    for required_readme_phrase in (
        "formal seed: 0.2.6",
        "packet schema: TRACE-GRAPH-0.2.6",
        "minimum schema shape: unchanged from 0.2.5",
        "check scope: PACKAGE_INTEGRITY_AND_DECLARED_CONTRACT_ONLY",
        "green CI != semantic validity",
    ):
        if not _contains_normalized(readme_text, required_readme_phrase):
            errors.append(f"README is missing scope/version boundary: {required_readme_phrase}")

    release_gate = manifest.get("release_gate")
    if not isinstance(release_gate, dict) or not all(
        release_gate.get(key) is True
        for key in (
            "requires_full_seed_compilation",
            "requires_version_strategy_lock",
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
            "check_scope": manifest.get("check_scope"),
            "finding_count": len(findings),
            "primary_core_repairs": sorted(primary_core),
            "source_anchor_count": len(anchors),
            "target_packet_schema": manifest.get("target_packet_schema"),
            "version_strategy": manifest.get("version_strategy"),
            "minimum_schema_shape_change": manifest.get("minimum_schema_shape_change"),
            "compiled_seed_present": manifest.get("compiled_seed_present"),
            "artifact_digests_checked": sorted(artifact_texts),
            "regression_sections_checked": len(regression_sections),
        },
    )


def validate_paths(
    *,
    manifest_path: Path = DEFAULT_MANIFEST,
    base_seed_path: Path = DEFAULT_BASE_SEED,
    matrix_path: Path = DEFAULT_MATRIX,
    patch_path: Path = DEFAULT_PATCH,
    regression_path: Path = DEFAULT_REGRESSION,
    readme_path: Path = DEFAULT_README,
) -> ValidationResult:
    try:
        manifest = _load_json(manifest_path)
        base_seed_text = base_seed_path.read_text(encoding="utf-8")
        matrix_text = matrix_path.read_text(encoding="utf-8")
        patch_text = patch_path.read_text(encoding="utf-8")
        regression_text = regression_path.read_text(encoding="utf-8")
        readme_text = readme_path.read_text(encoding="utf-8")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        return ValidationResult(status="INPUT_ERROR", errors=[str(exc)])

    return validate_manifest(
        manifest,
        base_seed_text=base_seed_text,
        matrix_text=matrix_text,
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
