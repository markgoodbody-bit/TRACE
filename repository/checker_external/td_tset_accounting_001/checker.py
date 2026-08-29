#!/usr/bin/env python3
"""Checker-external transition-class accounting candidate for TRACE v0.2.5.

Candidate ID: TD-TSET-ACCOUNTING-001

This module checks packet-internal transition-class accounting relative to a
supplied evidence envelope. It does not validate world completeness, truth,
good faith, or actual executability.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Mapping

TRANSITION_CLASSES: tuple[str, ...] = (
    "ACT",
    "WAIT",
    "DELAY",
    "INACTION",
    "INFORMATION",
)

BUCKET_BY_CLASS: Mapping[str, str] = {
    "ACT": "action_or_intervention_refs",
    "WAIT": "wait_delay_inaction_refs",
    "DELAY": "wait_delay_inaction_refs",
    "INACTION": "wait_delay_inaction_refs",
    "INFORMATION": "information_refs",
}

EVIDENCE_STATES: frozenset[str] = frozenset(
    {"MATERIALLY_LIVE", "UNAVAILABLE", "UNRESOLVED", "NOT_ASSESSABLE"}
)

FAIL_UNACCOUNTED = "TD-TSET-UNACCOUNTED-CLASS"
FAIL_UNSUPPORTED = "TD-TSET-UNSUPPORTED-STATUS"
FAIL_REFERENCE = "TD-TSET-REFERENCE-MISMATCH"

EPISTEMIC_LIMIT = (
    "This checker tests transition-class accounting and internal consistency "
    "relative to supplied packet evidence and declared apertures. It does not "
    "establish world completeness, claim truth, good faith, route executability, "
    "or the absence of unseen entities or alternatives."
)


class CheckerInputError(ValueError):
    """Raised when the checker envelope is not structurally usable."""


@dataclass(slots=True)
class ClassResult:
    transition_class: str
    accounting_status: str
    availability_status: str
    evidence_status: str
    represented_transition_refs: list[str] = field(default_factory=list)
    declared_unrepresented: bool = False
    reason_claim_refs: list[str] = field(default_factory=list)
    resolved_reason_claim_refs: list[str] = field(default_factory=list)
    basis_claim_refs: list[str] = field(default_factory=list)
    failure_codes: list[str] = field(default_factory=list)
    diagnostics: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "transition_class": self.transition_class,
            "accounting_status": self.accounting_status,
            "availability_status": self.availability_status,
            "evidence_status": self.evidence_status,
            "represented_transition_refs": self.represented_transition_refs,
            "declared_unrepresented": self.declared_unrepresented,
            "reason_claim_refs": self.reason_claim_refs,
            "resolved_reason_claim_refs": self.resolved_reason_claim_refs,
            "basis_claim_refs": self.basis_claim_refs,
            "failure_codes": self.failure_codes,
            "diagnostics": self.diagnostics,
        }


@dataclass(slots=True)
class CheckerResult:
    fixture_id: str
    status: str
    classes: dict[str, ClassResult]
    failure_codes: list[str]
    epistemic_limit: str = EPISTEMIC_LIMIT

    def to_dict(self) -> dict[str, Any]:
        return {
            "candidate_id": "TD-TSET-ACCOUNTING-001",
            "fixture_id": self.fixture_id,
            "status": self.status,
            "failure_codes": self.failure_codes,
            "classes": {name: result.to_dict() for name, result in self.classes.items()},
            "epistemic_limit": self.epistemic_limit,
        }


def _as_dict(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise CheckerInputError(f"{label} must be an object")
    return value


def _as_string_list(value: Any, label: str) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        raise CheckerInputError(f"{label} must be an array of strings")
    return list(value)


def _upper_set(values: Iterable[str]) -> set[str]:
    return {value.upper() for value in values}


def _claim_dependency_refs(claim: Mapping[str, Any]) -> set[str]:
    refs: set[str] = set()
    for key in ("source_refs", "provenance_edge_refs", "alternative_hypothesis_refs"):
        value = claim.get(key, [])
        if isinstance(value, list):
            refs.update(item for item in value if isinstance(item, str))

    unknown_context = claim.get("unknown_context")
    if isinstance(unknown_context, dict):
        for value in unknown_context.values():
            if isinstance(value, list):
                refs.update(item for item in value if isinstance(item, str))
    return refs


def _matching_transition_refs(
    transition_class: str,
    transition_set: Mapping[str, Any],
    node_by_id: Mapping[str, Mapping[str, Any]],
) -> tuple[list[str], list[str]]:
    bucket = BUCKET_BY_CLASS[transition_class]
    refs = _as_string_list(transition_set.get(bucket, []), f"transition_set.{bucket}")
    matching: list[str] = []
    mismatched: list[str] = []

    aggregate_modes = (
        {"WAIT", "DELAY", "INACTION"}
        if bucket == "wait_delay_inaction_refs"
        else {transition_class}
    )

    for ref in refs:
        node = node_by_id.get(ref)
        if not node or node.get("type") != "TRANSITION":
            mismatched.append(ref)
            continue
        attributes = node.get("attributes")
        mode = attributes.get("transition_mode") if isinstance(attributes, dict) else None
        normalized_mode = mode.upper() if isinstance(mode, str) else None
        if normalized_mode == transition_class:
            matching.append(ref)
        elif normalized_mode not in aggregate_modes:
            mismatched.append(ref)
        # A valid WAIT/DELAY/INACTION node in the shared aggregate bucket is
        # relevant to its own class, not a mismatch for the other two classes.
    return matching, mismatched


def _assessment_for(
    transition_class: str,
    checker_evidence: Mapping[str, Any],
) -> tuple[str, list[str], bool]:
    assessments = checker_evidence.get("class_assessments", {})
    if assessments is None:
        assessments = {}
    assessments = _as_dict(assessments, "checker_evidence.class_assessments")
    raw = assessments.get(transition_class)
    if raw is None:
        return "NOT_ASSESSABLE", [], False
    raw = _as_dict(raw, f"checker_evidence.class_assessments.{transition_class}")
    status = raw.get("evidence_status", "NOT_ASSESSABLE")
    if not isinstance(status, str) or status.upper() not in EVIDENCE_STATES:
        raise CheckerInputError(
            f"checker_evidence.class_assessments.{transition_class}.evidence_status "
            f"must be one of {sorted(EVIDENCE_STATES)}"
        )
    basis = _as_string_list(
        raw.get("basis_claim_refs", []),
        f"checker_evidence.class_assessments.{transition_class}.basis_claim_refs",
    )
    return status.upper(), basis, True


def _reason_bindings_for(
    transition_class: str,
    checker_evidence: Mapping[str, Any],
) -> list[str]:
    bindings = checker_evidence.get("unavailability_bindings", {})
    if bindings is None:
        bindings = {}
    bindings = _as_dict(bindings, "checker_evidence.unavailability_bindings")
    return _as_string_list(
        bindings.get(transition_class, []),
        f"checker_evidence.unavailability_bindings.{transition_class}",
    )


def _reasons_are_supported(
    reason_refs: list[str],
    basis_refs: list[str],
    claim_by_id: Mapping[str, Mapping[str, Any]],
    global_reason_refs: set[str],
) -> tuple[bool, list[str], list[str]]:
    diagnostics: list[str] = []
    resolved = [ref for ref in reason_refs if ref in claim_by_id]
    missing = [ref for ref in reason_refs if ref not in claim_by_id]

    if missing:
        diagnostics.append(f"unresolvable reason claim refs: {', '.join(missing)}")
    if not reason_refs:
        diagnostics.append("no class-specific reason claim refs supplied")
        return False, resolved, diagnostics
    if any(ref not in global_reason_refs for ref in reason_refs):
        omitted = [ref for ref in reason_refs if ref not in global_reason_refs]
        diagnostics.append(
            "class-specific reason refs absent from "
            f"transition_set.unavailability_reason_claim_refs: {', '.join(omitted)}"
        )
    if missing or any(ref not in global_reason_refs for ref in reason_refs):
        return False, resolved, diagnostics

    if not basis_refs:
        return True, resolved, diagnostics

    supported_basis: set[str] = set(resolved)
    for ref in resolved:
        supported_basis.update(_claim_dependency_refs(claim_by_id[ref]))

    missing_basis = [ref for ref in basis_refs if ref not in supported_basis]
    if missing_basis:
        diagnostics.append(
            "reason claims do not bind required supplied-evidence refs: "
            + ", ".join(missing_basis)
        )
        return False, resolved, diagnostics
    return True, resolved, diagnostics


def check_envelope(envelope: Mapping[str, Any]) -> CheckerResult:
    """Check one external-checker envelope.

    The envelope contains a TRACE graph plus a checker-only evidence manifest:

    - ``trace_graph``: the packet under test.
    - ``checker_evidence.class_assessments``: source-relative assessment of
      each transition class, with claim refs already present in the packet.
    - ``checker_evidence.unavailability_bindings``: per-class mapping to the
      packet's global ``unavailability_reason_claim_refs`` array.

    The evidence manifest is not a TRACE field and makes no world-truth claim.
    """

    envelope_dict = _as_dict(dict(envelope), "envelope")
    fixture_id = str(envelope_dict.get("fixture_id", "UNNAMED"))
    graph = _as_dict(envelope_dict.get("trace_graph"), "trace_graph")
    checker_evidence = _as_dict(
        envelope_dict.get("checker_evidence", {}), "checker_evidence"
    )

    nodes = graph.get("nodes", [])
    claims = graph.get("claims", [])
    if not isinstance(nodes, list) or any(not isinstance(node, dict) for node in nodes):
        raise CheckerInputError("trace_graph.nodes must be an array of objects")
    if not isinstance(claims, list) or any(not isinstance(claim, dict) for claim in claims):
        raise CheckerInputError("trace_graph.claims must be an array of objects")

    node_by_id = {
        str(node["id"]): node
        for node in nodes
        if isinstance(node.get("id"), str) and node.get("id")
    }
    claim_by_id = {
        str(claim["id"]): claim
        for claim in claims
        if isinstance(claim.get("id"), str) and claim.get("id")
    }

    discipline = _as_dict(graph.get("discipline"), "trace_graph.discipline")
    transition_set = _as_dict(
        discipline.get("transition_set"), "trace_graph.discipline.transition_set"
    )
    unrepresented = _upper_set(
        _as_string_list(
            transition_set.get("unrepresented_transition_classes", []),
            "transition_set.unrepresented_transition_classes",
        )
    )
    global_reason_refs = set(
        _as_string_list(
            transition_set.get("unavailability_reason_claim_refs", []),
            "transition_set.unavailability_reason_claim_refs",
        )
    )

    class_results: dict[str, ClassResult] = {}
    all_failures: list[str] = []

    for transition_class in TRANSITION_CLASSES:
        evidence_status, basis_refs, explicitly_assessed = _assessment_for(
            transition_class, checker_evidence
        )
        matching_refs, mismatched_refs = _matching_transition_refs(
            transition_class, transition_set, node_by_id
        )
        declared_unrepresented = transition_class in unrepresented
        reason_refs = _reason_bindings_for(transition_class, checker_evidence)
        if declared_unrepresented or reason_refs:
            reasons_supported, resolved_reasons, reason_diagnostics = _reasons_are_supported(
                reason_refs, basis_refs, claim_by_id, global_reason_refs
            )
        else:
            reasons_supported, resolved_reasons, reason_diagnostics = False, [], []

        failures: list[str] = []
        diagnostics = list(reason_diagnostics)
        if mismatched_refs:
            failures.append(FAIL_REFERENCE)
            diagnostics.append(
                "bucket contains missing, non-TRANSITION, or wrong-mode refs: "
                + ", ".join(mismatched_refs)
            )

        represented = bool(matching_refs)

        if represented:
            accounting_status = "ACCOUNTED"
            availability_status = "REPRESENTED"
        elif evidence_status == "MATERIALLY_LIVE":
            if declared_unrepresented or reason_refs:
                accounting_status = "UNSUPPORTED_STATUS"
                availability_status = "MATERIALLY_LIVE_UNREPRESENTED"
                failures.append(FAIL_UNSUPPORTED)
                diagnostics.append(
                    "supplied evidence marks the class materially live, but the packet "
                    "classifies or excuses it as unrepresented"
                )
            else:
                accounting_status = "UNACCOUNTED"
                availability_status = "MATERIALLY_LIVE_UNREPRESENTED"
                failures.append(FAIL_UNACCOUNTED)
                diagnostics.append(
                    "supplied evidence marks the class materially live, but no matching "
                    "transition or supported status record exists"
                )
        elif declared_unrepresented:
            if reasons_supported:
                accounting_status = "ACCOUNTED"
                availability_status = evidence_status
            else:
                accounting_status = "UNSUPPORTED_STATUS"
                availability_status = evidence_status
                failures.append(FAIL_UNSUPPORTED)
        elif explicitly_assessed and evidence_status in {
            "UNAVAILABLE",
            "UNRESOLVED",
            "NOT_ASSESSABLE",
        }:
            accounting_status = "UNACCOUNTED"
            availability_status = evidence_status
            failures.append(FAIL_UNACCOUNTED)
            diagnostics.append(
                "the supplied evidence envelope assesses the class, but the packet "
                "contains no represented transition and no explicit status record"
            )
        else:
            accounting_status = "NO_CHECKER_FAILURE"
            availability_status = "NOT_ASSESSABLE"
            diagnostics.append(
                "no supplied evidence makes this class assessable; no world-completeness "
                "inference is permitted"
            )

        unique_failures = list(dict.fromkeys(failures))
        all_failures.extend(unique_failures)
        class_results[transition_class] = ClassResult(
            transition_class=transition_class,
            accounting_status=accounting_status,
            availability_status=availability_status,
            evidence_status=evidence_status,
            represented_transition_refs=matching_refs,
            declared_unrepresented=declared_unrepresented,
            reason_claim_refs=reason_refs,
            resolved_reason_claim_refs=resolved_reasons,
            basis_claim_refs=basis_refs,
            failure_codes=unique_failures,
            diagnostics=diagnostics,
        )

    unique_all_failures = list(dict.fromkeys(all_failures))
    return CheckerResult(
        fixture_id=fixture_id,
        status="FAIL" if unique_all_failures else "PASS",
        classes=class_results,
        failure_codes=unique_all_failures,
    )


def load_json(path: Path) -> dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as handle:
            value = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        raise CheckerInputError(f"cannot load {path}: {exc}") from exc
    return _as_dict(value, str(path))


def run_path(path: Path) -> CheckerResult:
    return check_envelope(load_json(path))


def run_bundle(path: Path) -> tuple[list[dict[str, Any]], bool]:
    bundle = load_json(path)
    fixtures = bundle.get("fixtures")
    if not isinstance(fixtures, list) or any(not isinstance(item, dict) for item in fixtures):
        raise CheckerInputError("bundle.fixtures must be an array of checker envelopes")

    rows: list[dict[str, Any]] = []
    mismatch = False
    for envelope in fixtures:
        result = check_envelope(envelope)
        expected = envelope.get("expected", {})
        if not isinstance(expected, dict):
            expected = {}
        matches_expected = (
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
                "matches_expected": matches_expected,
                "classes": {
                    name: {
                        "accounting_status": item.accounting_status,
                        "availability_status": item.availability_status,
                        "failure_codes": item.failure_codes,
                    }
                    for name, item in result.classes.items()
                },
            }
        )
        mismatch = mismatch or not matches_expected
    return rows, mismatch


def _main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Run TRACE TD-TSET-ACCOUNTING-001 against JSON checker input."
    )
    parser.add_argument("input", type=Path, help="JSON checker envelope or fixture bundle")
    parser.add_argument(
        "--all",
        action="store_true",
        help="treat input as a fixture bundle and compare every result with expected output",
    )
    parser.add_argument(
        "--compact", action="store_true", help="emit compact JSON rather than indented JSON"
    )
    args = parser.parse_args(argv)

    try:
        if args.all:
            rows, mismatch = run_bundle(args.input)
            output: dict[str, Any] = {
                "candidate_id": "TD-TSET-ACCOUNTING-001",
                "results": rows,
                "all_match_expected": not mismatch,
                "epistemic_limit": EPISTEMIC_LIMIT,
            }
            exit_code = 1 if mismatch else 0
        else:
            result = run_path(args.input)
            output = result.to_dict()
            exit_code = 1 if result.status == "FAIL" else 0
    except CheckerInputError as exc:
        print(json.dumps({"status": "INPUT_ERROR", "error": str(exc)}), file=sys.stderr)
        return 2

    print(json.dumps(output, indent=None if args.compact else 2, sort_keys=True))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(_main())
