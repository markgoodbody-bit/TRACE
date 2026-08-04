#!/usr/bin/env python3
"""Hostile integrity checks for TRACE TD-TSET-ACCOUNTING-001.

This checker is deliberately source-relative. It validates the comparison
envelope and contradictions between that envelope and represented transition
nodes. It does not infer material liveness from the world or from packet data
that the comparison envelope has not designated for assessment.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping

TRANSITION_CLASSES = ("ACT", "WAIT", "DELAY", "INACTION", "INFORMATION")
BUCKET_BY_CLASS = {
    "ACT": "action_or_intervention_refs",
    "WAIT": "wait_delay_inaction_refs",
    "DELAY": "wait_delay_inaction_refs",
    "INACTION": "wait_delay_inaction_refs",
    "INFORMATION": "information_refs",
}
AGGREGATE_MODES = {"WAIT", "DELAY", "INACTION"}
EVIDENCE_STATES = {"MATERIALLY_LIVE", "UNAVAILABLE", "UNRESOLVED", "NOT_ASSESSABLE"}

FAIL_REFERENCE = "TD-TSET-REFERENCE-MISMATCH"
FAIL_UNSUPPORTED = "TD-TSET-UNSUPPORTED-STATUS"

EPISTEMIC_LIMIT = (
    "This integrity pass checks only declared comparison-envelope references and "
    "packet-internal contradictions. Omitted class assessments remain NOT_ASSESSABLE; "
    "the checker does not independently discover material liveness or world completeness."
)


class IntegrityInputError(ValueError):
    """Raised when the hostile-check envelope is unusable."""


@dataclass(slots=True)
class ClassIntegrityResult:
    transition_class: str
    assessment_present: bool
    evidence_status: str
    availability_status: str
    matching_transition_refs: list[str] = field(default_factory=list)
    failure_codes: list[str] = field(default_factory=list)
    diagnostics: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "transition_class": self.transition_class,
            "assessment_present": self.assessment_present,
            "evidence_status": self.evidence_status,
            "availability_status": self.availability_status,
            "matching_transition_refs": self.matching_transition_refs,
            "failure_codes": self.failure_codes,
            "diagnostics": self.diagnostics,
        }


@dataclass(slots=True)
class IntegrityResult:
    fixture_id: str
    status: str
    failure_codes: list[str]
    classes: dict[str, ClassIntegrityResult]
    epistemic_limit: str = EPISTEMIC_LIMIT

    def to_dict(self) -> dict[str, Any]:
        return {
            "candidate_id": "TD-TSET-ACCOUNTING-002-HOSTILE-INTEGRITY",
            "fixture_id": self.fixture_id,
            "status": self.status,
            "failure_codes": self.failure_codes,
            "classes": {name: result.to_dict() for name, result in self.classes.items()},
            "epistemic_limit": self.epistemic_limit,
        }


def _object(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise IntegrityInputError(f"{label} must be an object")
    return value


def _string_list(value: Any, label: str) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        raise IntegrityInputError(f"{label} must be an array of strings")
    return list(value)


def _assessment(
    transition_class: str, checker_evidence: Mapping[str, Any]
) -> tuple[bool, str, list[str]]:
    assessments = _object(
        checker_evidence.get("class_assessments", {}),
        "checker_evidence.class_assessments",
    )
    raw = assessments.get(transition_class)
    if raw is None:
        return False, "NOT_ASSESSABLE", []
    raw = _object(raw, f"checker_evidence.class_assessments.{transition_class}")
    evidence_status = raw.get("evidence_status", "NOT_ASSESSABLE")
    if not isinstance(evidence_status, str) or evidence_status.upper() not in EVIDENCE_STATES:
        raise IntegrityInputError(
            f"checker_evidence.class_assessments.{transition_class}.evidence_status "
            f"must be one of {sorted(EVIDENCE_STATES)}"
        )
    basis_refs = _string_list(
        raw.get("basis_claim_refs", []),
        f"checker_evidence.class_assessments.{transition_class}.basis_claim_refs",
    )
    return True, evidence_status.upper(), basis_refs


def _bucket_refs(
    transition_class: str, transition_set: Mapping[str, Any]
) -> list[str]:
    bucket = BUCKET_BY_CLASS[transition_class]
    return _string_list(transition_set.get(bucket, []), f"transition_set.{bucket}")


def check_integrity(envelope: Mapping[str, Any]) -> IntegrityResult:
    envelope = _object(dict(envelope), "envelope")
    fixture_id = str(envelope.get("fixture_id", "UNNAMED"))
    graph = _object(envelope.get("trace_graph"), "trace_graph")
    checker_evidence = _object(envelope.get("checker_evidence", {}), "checker_evidence")

    nodes = graph.get("nodes", [])
    claims = graph.get("claims", [])
    if not isinstance(nodes, list) or any(not isinstance(node, dict) for node in nodes):
        raise IntegrityInputError("trace_graph.nodes must be an array of objects")
    if not isinstance(claims, list) or any(not isinstance(claim, dict) for claim in claims):
        raise IntegrityInputError("trace_graph.claims must be an array of objects")

    node_by_id = {
        node["id"]: node
        for node in nodes
        if isinstance(node.get("id"), str) and node.get("id")
    }
    claim_ids = {
        claim["id"]
        for claim in claims
        if isinstance(claim.get("id"), str) and claim.get("id")
    }

    discipline = _object(graph.get("discipline"), "trace_graph.discipline")
    transition_set = _object(
        discipline.get("transition_set"), "trace_graph.discipline.transition_set"
    )

    class_results: dict[str, ClassIntegrityResult] = {}
    all_failures: list[str] = []

    for transition_class in TRANSITION_CLASSES:
        present, evidence_status, basis_refs = _assessment(
            transition_class, checker_evidence
        )
        failures: list[str] = []
        diagnostics: list[str] = []
        matching_refs: list[str] = []
        represented_availability: list[str] = []

        missing_basis = [ref for ref in basis_refs if ref not in claim_ids]
        if missing_basis:
            failures.append(FAIL_REFERENCE)
            diagnostics.append(
                "assessment basis claim refs do not resolve: " + ", ".join(missing_basis)
            )

        for ref in _bucket_refs(transition_class, transition_set):
            node = node_by_id.get(ref)
            if node is None:
                failures.append(FAIL_REFERENCE)
                diagnostics.append(f"transition ref does not resolve: {ref}")
                continue
            if node.get("type") != "TRANSITION":
                failures.append(FAIL_REFERENCE)
                diagnostics.append(f"transition ref points to non-TRANSITION node: {ref}")
                continue
            attributes = node.get("attributes")
            if not isinstance(attributes, dict):
                failures.append(FAIL_REFERENCE)
                diagnostics.append(f"TRANSITION node has no attributes object: {ref}")
                continue
            mode = attributes.get("transition_mode")
            normalized_mode = mode.upper() if isinstance(mode, str) else ""
            valid_modes = AGGREGATE_MODES if transition_class in AGGREGATE_MODES else {transition_class}
            if normalized_mode not in valid_modes:
                failures.append(FAIL_REFERENCE)
                diagnostics.append(
                    f"transition ref has wrong mode for {BUCKET_BY_CLASS[transition_class]}: "
                    f"{ref}={normalized_mode or 'MISSING'}"
                )
                continue
            if normalized_mode == transition_class:
                matching_refs.append(ref)
                availability = attributes.get("availability_status", "UNKNOWN")
                represented_availability.append(
                    availability.upper() if isinstance(availability, str) else "UNKNOWN"
                )

        if present and matching_refs:
            if evidence_status in {"UNAVAILABLE", "UNRESOLVED", "NOT_ASSESSABLE"} and any(
                status == "AVAILABLE" for status in represented_availability
            ):
                failures.append(FAIL_UNSUPPORTED)
                diagnostics.append(
                    "represented transition declares AVAILABLE while the supplied "
                    f"assessment is {evidence_status}"
                )
            if evidence_status == "MATERIALLY_LIVE" and represented_availability and all(
                status == "UNAVAILABLE" for status in represented_availability
            ):
                failures.append(FAIL_UNSUPPORTED)
                diagnostics.append(
                    "represented transition declares UNAVAILABLE while the supplied "
                    "assessment is MATERIALLY_LIVE"
                )

        if not present:
            availability_status = "NOT_ASSESSABLE"
            diagnostics.append(
                "no class assessment was supplied; this integrity pass does not infer "
                "material liveness from packet or world evidence"
            )
        elif matching_refs:
            availability_status = "REPRESENTED"
        else:
            availability_status = evidence_status

        unique_failures = list(dict.fromkeys(failures))
        all_failures.extend(unique_failures)
        class_results[transition_class] = ClassIntegrityResult(
            transition_class=transition_class,
            assessment_present=present,
            evidence_status=evidence_status,
            availability_status=availability_status,
            matching_transition_refs=matching_refs,
            failure_codes=unique_failures,
            diagnostics=diagnostics,
        )

    unique_all_failures = list(dict.fromkeys(all_failures))
    return IntegrityResult(
        fixture_id=fixture_id,
        status="FAIL" if unique_all_failures else "PASS",
        failure_codes=unique_all_failures,
        classes=class_results,
    )


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise IntegrityInputError(f"cannot load {path}: {exc}") from exc
    return _object(value, str(path))


def run_bundle(path: Path) -> tuple[list[dict[str, Any]], bool]:
    bundle = load_json(path)
    fixtures = bundle.get("fixtures")
    if not isinstance(fixtures, list) or any(not isinstance(item, dict) for item in fixtures):
        raise IntegrityInputError("bundle.fixtures must be an array of objects")
    rows: list[dict[str, Any]] = []
    mismatch = False
    for envelope in fixtures:
        result = check_integrity(envelope)
        expected = envelope.get("expected", {})
        if not isinstance(expected, dict):
            expected = {}
        matches = (
            result.status == expected.get("status")
            and result.failure_codes == expected.get("failure_codes", [])
        )
        rows.append(
            {
                "fixture_id": result.fixture_id,
                "actual_status": result.status,
                "actual_failure_codes": result.failure_codes,
                "expected_status": expected.get("status"),
                "expected_failure_codes": expected.get("failure_codes", []),
                "matches_expected": matches,
            }
        )
        mismatch = mismatch or not matches
    return rows, mismatch


def _main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run TD-TSET hostile integrity fixtures")
    parser.add_argument("input", type=Path)
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args(argv)
    try:
        if args.all:
            rows, mismatch = run_bundle(args.input)
            output = {
                "candidate_id": "TD-TSET-ACCOUNTING-002-HOSTILE-INTEGRITY",
                "results": rows,
                "all_match_expected": not mismatch,
                "epistemic_limit": EPISTEMIC_LIMIT,
            }
            code = 1 if mismatch else 0
        else:
            result = check_integrity(load_json(args.input))
            output = result.to_dict()
            code = 1 if result.status == "FAIL" else 0
    except IntegrityInputError as exc:
        print(json.dumps({"status": "INPUT_ERROR", "error": str(exc)}), file=sys.stderr)
        return 2
    print(json.dumps(output, indent=2, sort_keys=True))
    return code


if __name__ == "__main__":
    raise SystemExit(_main())
