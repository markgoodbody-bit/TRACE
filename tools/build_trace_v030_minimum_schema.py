#!/usr/bin/env python3
"""Build the TRACE v0.3.0 minimum-schema candidate from released v0.2.7.

The current v0.3 working theory has earned semantic/use-rule changes but no
canonical vocabulary or minimum-schema shape change. This compiler therefore
changes only packet/schema version identity and fails if any other schema leaf
changes after normalization.

Green output means deterministic version-only schema carry-forward. It does
not mean semantic completeness, release, canon, validation, world validity,
authority, permission or clearance.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
DONOR_PATH = REPO_ROOT / "TRACE_FORMAL_SEED_v0_2_7.md"
OUTPUT_PATH = REPO_ROOT / "PROJECT" / "TRACE_v0_3_0_MINIMUM_SCHEMA_CANDIDATE_v0_1.json"

SECTION_MARKER = "## [14.4] Minimum validator contract"
JSON_FENCE = "```json"

DONOR_VERSION = "0.2.7"
DONOR_SCHEMA_ID = "TRACE-GRAPH-0.2.7"
DONOR_URN = "urn:trace:graph:0.2.7"
DONOR_TITLE = "TRACE-GRAPH-0.2.7 minimum validator"

CANDIDATE_VERSION = "0.3.0"
CANDIDATE_SCHEMA_ID = "TRACE-GRAPH-0.3.0"
CANDIDATE_URN = "urn:trace:graph:0.3.0"
CANDIDATE_TITLE = "TRACE-GRAPH-0.3.0 minimum validator"

EXPECTED_VERSION_DIFF_PATHS = {
    "$id",
    "title",
    "properties.trace_graph.properties.schema.const",
    "properties.trace_graph.properties.trace_version.const",
}


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")


def sha256(value: Any) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def extract_minimum_schema(seed_path: Path = DONOR_PATH) -> dict[str, Any]:
    text = seed_path.read_text(encoding="utf-8")
    section_start = text.index(SECTION_MARKER)
    fence_start = text.index(JSON_FENCE, section_start) + len(JSON_FENCE)
    fence_end = text.index("\n```", fence_start)
    payload = text[fence_start:fence_end].strip()
    schema = json.loads(payload)
    if not isinstance(schema, dict):
        raise ValueError("embedded minimum schema is not a JSON object")
    return schema


def graph_properties(schema: dict[str, Any]) -> dict[str, Any]:
    return schema["properties"]["trace_graph"]["properties"]


def assert_donor_identity(donor: dict[str, Any]) -> None:
    props = graph_properties(donor)
    observed = {
        "$id": donor.get("$id"),
        "title": donor.get("title"),
        "schema_const": props.get("schema", {}).get("const"),
        "trace_version_const": props.get("trace_version", {}).get("const"),
    }
    expected = {
        "$id": DONOR_URN,
        "title": DONOR_TITLE,
        "schema_const": DONOR_SCHEMA_ID,
        "trace_version_const": DONOR_VERSION,
    }
    if observed != expected:
        raise ValueError(f"unexpected donor schema identity: {observed!r}")


def build_candidate(donor: dict[str, Any]) -> dict[str, Any]:
    candidate = copy.deepcopy(donor)
    candidate["$id"] = CANDIDATE_URN
    candidate["title"] = CANDIDATE_TITLE
    props = graph_properties(candidate)
    props["schema"]["const"] = CANDIDATE_SCHEMA_ID
    props["trace_version"]["const"] = CANDIDATE_VERSION
    return candidate


def normalize_candidate(candidate: dict[str, Any]) -> dict[str, Any]:
    normalized = copy.deepcopy(candidate)
    normalized["$id"] = DONOR_URN
    normalized["title"] = DONOR_TITLE
    props = graph_properties(normalized)
    props["schema"]["const"] = DONOR_SCHEMA_ID
    props["trace_version"]["const"] = DONOR_VERSION
    return normalized


def diff_paths(left: Any, right: Any, prefix: str = "") -> set[str]:
    if type(left) is not type(right):
        return {prefix or "<root>"}
    if isinstance(left, dict):
        out: set[str] = set()
        keys = set(left) | set(right)
        for key in keys:
            path = f"{prefix}.{key}" if prefix else str(key)
            if key not in left or key not in right:
                out.add(path)
            else:
                out |= diff_paths(left[key], right[key], path)
        return out
    if isinstance(left, list):
        if len(left) != len(right):
            return {prefix or "<root>"}
        out: set[str] = set()
        for idx, (l_item, r_item) in enumerate(zip(left, right)):
            out |= diff_paths(l_item, r_item, f"{prefix}[{idx}]")
        return out
    return set() if left == right else {prefix or "<root>"}


def schema_vocab(schema: dict[str, Any], def_name: str, property_name: str = "type") -> tuple[str, ...]:
    return tuple(
        schema.get("$defs", {})
        .get(def_name, {})
        .get("properties", {})
        .get(property_name, {})
        .get("enum", [])
    )


def claim_enum(schema: dict[str, Any], property_name: str) -> tuple[str, ...]:
    return tuple(
        schema.get("$defs", {})
        .get("claim", {})
        .get("properties", {})
        .get(property_name, {})
        .get("enum", [])
    )


def verify(donor: dict[str, Any], candidate: dict[str, Any]) -> dict[str, Any]:
    assert_donor_identity(donor)

    version_diff_paths = diff_paths(donor, candidate)
    normalized = normalize_candidate(candidate)
    normalized_equal = normalized == donor

    vocab = {
        "node_types": {
            "donor": schema_vocab(donor, "node"),
            "candidate": schema_vocab(candidate, "node"),
        },
        "relation_types": {
            "donor": schema_vocab(donor, "edge"),
            "candidate": schema_vocab(candidate, "edge"),
        },
        "claim_kinds": {
            "donor": claim_enum(donor, "claim_kind"),
            "candidate": claim_enum(candidate, "claim_kind"),
        },
        "evidence_states": {
            "donor": claim_enum(donor, "evidence_state"),
            "candidate": claim_enum(candidate, "evidence_state"),
        },
        "access_states": {
            "donor": claim_enum(donor, "access_state"),
            "candidate": claim_enum(candidate, "access_state"),
        },
    }
    vocab_equal = all(row["donor"] == row["candidate"] for row in vocab.values())

    donor_graph = donor["properties"]["trace_graph"]
    candidate_graph = candidate["properties"]["trace_graph"]
    required_equal = donor_graph.get("required") == candidate_graph.get("required")
    ports_required_equal = (
        donor_graph["properties"]["ports"].get("required")
        == candidate_graph["properties"]["ports"].get("required")
    )
    discipline_required_equal = (
        donor_graph["properties"]["discipline"].get("required")
        == candidate_graph["properties"]["discipline"].get("required")
    )

    errors: list[str] = []
    if version_diff_paths != EXPECTED_VERSION_DIFF_PATHS:
        errors.append(
            "schema leaf diff is not exactly the four declared version-identity paths: "
            f"observed={sorted(version_diff_paths)!r}"
        )
    if not normalized_equal:
        errors.append("candidate does not equal donor after version-identity normalization")
    if not vocab_equal:
        errors.append("controlled vocabulary changed")
    if not required_equal:
        errors.append("trace_graph required properties changed")
    if not ports_required_equal:
        errors.append("required port roles changed")
    if not discipline_required_equal:
        errors.append("required discipline blocks changed")

    return {
        "status": "PASS" if not errors else "FAIL",
        "donor_path": str(DONOR_PATH.relative_to(REPO_ROOT)),
        "output_path": str(OUTPUT_PATH.relative_to(REPO_ROOT)),
        "donor_schema_sha256": sha256(donor),
        "candidate_schema_sha256": sha256(candidate),
        "normalized_candidate_sha256": sha256(normalized),
        "normalized_equal_to_donor": normalized_equal,
        "version_diff_paths": sorted(version_diff_paths),
        "expected_version_diff_paths": sorted(EXPECTED_VERSION_DIFF_PATHS),
        "vocabulary_equal": vocab_equal,
        "required_packet_properties_equal": required_equal,
        "required_port_roles_equal": ports_required_equal,
        "required_discipline_blocks_equal": discipline_required_equal,
        "vocabulary_counts": {
            name: len(row["candidate"]) for name, row in vocab.items()
        },
        "errors": errors,
        "claim_boundary": (
            "DETERMINISTIC_VERSION_ONLY_MINIMUM_SCHEMA_CARRY_FORWARD_"
            "NOT_SEMANTIC_COMPLETENESS_NOT_RELEASE_NOT_CANON_NOT_VALIDATION"
        ),
    }


def render_candidate(candidate: dict[str, Any]) -> str:
    return json.dumps(candidate, indent=2, ensure_ascii=False) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="write deterministic candidate JSON")
    parser.add_argument("--check", action="store_true", help="require committed candidate to match deterministic output")
    parser.add_argument("--report", type=Path, help="optional JSON report path")
    args = parser.parse_args(argv)

    donor = extract_minimum_schema()
    candidate = build_candidate(donor)
    report = verify(donor, candidate)

    expected_text = render_candidate(candidate)
    if args.write:
        OUTPUT_PATH.write_text(expected_text, encoding="utf-8")

    if args.check:
        if not OUTPUT_PATH.exists():
            report["errors"].append("candidate output file missing")
        elif OUTPUT_PATH.read_text(encoding="utf-8") != expected_text:
            report["errors"].append("committed candidate differs from deterministic compiler output")

    if report["errors"]:
        report["status"] = "FAIL"

    rendered_report = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.report:
        args.report.write_text(rendered_report, encoding="utf-8")
    print(rendered_report, end="")
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
