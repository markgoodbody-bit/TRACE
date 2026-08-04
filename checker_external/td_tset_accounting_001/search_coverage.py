#!/usr/bin/env python3
"""Checker-external search-coverage contradiction candidate.

Candidate ID: TD-TSET-SEARCH-COVERAGE-001

This checker does not prove that a search genuinely widens an aperture. It can
only test a declared discovery target and a declared packet-internal
reachability path for explicit contradiction, missing support, or unusable
references.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, field
from typing import Any, Mapping

CANDIDATE_ID = "TD-TSET-SEARCH-COVERAGE-001"

FAIL_CONTRADICTION = "TD-TSET-SEARCH-COVERAGE-CONTRADICTION"
FAIL_UNSUPPORTED = "TD-TSET-SEARCH-COVERAGE-UNSUPPORTED-REACHABILITY"
FAIL_REFERENCE = "TD-TSET-SEARCH-COVERAGE-REFERENCE-MISMATCH"

ASSESSMENT_STATUSES = frozenset({"ASSESS", "UNAVAILABLE", "NOT_ASSESSABLE"})
ALLOWED_PATH_EDGE_TYPES = frozenset(
    {"OBSERVES", "REPORTS", "ROUTES_TO", "REPRESENTS", "CONTAINS"}
)

EPISTEMIC_LIMIT = (
    "This checker tests only a supplied discovery target, a declared INFORMATION "
    "transition, its bound aperture, and packet-internal reachability claims. A "
    "PASS does not establish actual search coverage, good faith, source truth, "
    "route executability, world completeness, or discovery of unseen entities. "
    "Targets omitted from the comparison envelope remain outside the check."
)


class SearchCoverageInputError(ValueError):
    """Raised when the checker envelope cannot be interpreted."""


@dataclass(slots=True)
class SearchCoverageResult:
    fixture_id: str
    status: str
    coverage_status: str
    information_transition_ref: str | None = None
    aperture_ref: str | None = None
    required_target_refs: list[str] = field(default_factory=list)
    comparison_basis_claim_refs: list[str] = field(default_factory=list)
    validated_target_refs: list[str] = field(default_factory=list)
    contradicted_target_refs: list[str] = field(default_factory=list)
    failure_codes: list[str] = field(default_factory=list)
    diagnostics: list[str] = field(default_factory=list)
    epistemic_limit: str = EPISTEMIC_LIMIT

    def to_dict(self) -> dict[str, Any]:
        return {
            "candidate_id": CANDIDATE_ID,
            "fixture_id": self.fixture_id,
            "status": self.status,
            "coverage_status": self.coverage_status,
            "information_transition_ref": self.information_transition_ref,
            "aperture_ref": self.aperture_ref,
            "required_target_refs": self.required_target_refs,
            "comparison_basis_claim_refs": self.comparison_basis_claim_refs,
            "validated_target_refs": self.validated_target_refs,
            "contradicted_target_refs": self.contradicted_target_refs,
            "failure_codes": self.failure_codes,
            "diagnostics": self.diagnostics,
            "epistemic_limit": self.epistemic_limit,
        }


def _as_dict(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise SearchCoverageInputError(f"{label} must be an object")
    return value


def _as_string_list(value: Any, label: str) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        raise SearchCoverageInputError(f"{label} must be an array of strings")
    return list(value)


def _result(
    fixture_id: str,
    *,
    status: str,
    coverage_status: str,
    transition_ref: str | None = None,
    aperture_ref: str | None = None,
    targets: list[str] | None = None,
    basis_refs: list[str] | None = None,
    validated_targets: list[str] | None = None,
    contradicted_targets: list[str] | None = None,
    failure_codes: list[str] | None = None,
    diagnostics: list[str] | None = None,
) -> SearchCoverageResult:
    return SearchCoverageResult(
        fixture_id=fixture_id,
        status=status,
        coverage_status=coverage_status,
        information_transition_ref=transition_ref,
        aperture_ref=aperture_ref,
        required_target_refs=targets or [],
        comparison_basis_claim_refs=basis_refs or [],
        validated_target_refs=validated_targets or [],
        contradicted_target_refs=contradicted_targets or [],
        failure_codes=failure_codes or [],
        diagnostics=diagnostics or [],
    )


def _validate_path(
    *,
    target_ref: str,
    edge_refs: list[str],
    edge_by_id: Mapping[str, Mapping[str, Any]],
    allowed_starts: set[str],
) -> tuple[str, list[str]]:
    """Return VALID, REFERENCE_ERROR, or UNSUPPORTED with diagnostics."""

    diagnostics: list[str] = []
    if not edge_refs:
        return "UNSUPPORTED", [f"no declared reachability path for {target_ref}"]

    edges: list[Mapping[str, Any]] = []
    missing = [ref for ref in edge_refs if ref not in edge_by_id]
    if missing:
        return "REFERENCE_ERROR", [
            "unresolvable coverage path edge refs for "
            f"{target_ref}: {', '.join(missing)}"
        ]

    edges = [edge_by_id[ref] for ref in edge_refs]
    first_from = edges[0].get("from")
    if first_from not in allowed_starts:
        diagnostics.append(
            f"coverage path for {target_ref} starts at {first_from!r}, not the "
            "declared INFORMATION transition or its aperture"
        )

    previous_to: Any = None
    for index, edge in enumerate(edges):
        edge_type = edge.get("type")
        if edge_type not in ALLOWED_PATH_EDGE_TYPES:
            diagnostics.append(
                f"coverage path edge {edge_refs[index]} uses non-reachability "
                f"type {edge_type!r}"
            )
        if index and edge.get("from") != previous_to:
            diagnostics.append(
                f"coverage path for {target_ref} is not contiguous at "
                f"{edge_refs[index]}"
            )
        previous_to = edge.get("to")

    if previous_to != target_ref:
        diagnostics.append(
            f"coverage path ends at {previous_to!r}, not required target {target_ref!r}"
        )

    return ("UNSUPPORTED", diagnostics) if diagnostics else ("VALID", [])


def check_search_coverage(envelope: Mapping[str, Any]) -> SearchCoverageResult:
    envelope_dict = _as_dict(dict(envelope), "envelope")
    fixture_id = str(envelope_dict.get("fixture_id", "UNNAMED"))
    graph = _as_dict(envelope_dict.get("trace_graph"), "trace_graph")

    raw_evidence = envelope_dict.get("coverage_evidence")
    if raw_evidence is None:
        return _result(
            fixture_id,
            status="PASS",
            coverage_status="NOT_ASSESSABLE",
            diagnostics=["no coverage comparison envelope supplied"],
        )

    evidence = _as_dict(raw_evidence, "coverage_evidence")
    assessment_status = evidence.get("assessment_status", "NOT_ASSESSABLE")
    if not isinstance(assessment_status, str):
        raise SearchCoverageInputError("coverage_evidence.assessment_status must be a string")
    assessment_status = assessment_status.upper()
    if assessment_status not in ASSESSMENT_STATUSES:
        raise SearchCoverageInputError(
            "coverage_evidence.assessment_status must be one of "
            + ", ".join(sorted(ASSESSMENT_STATUSES))
        )

    nodes = graph.get("nodes", [])
    edges = graph.get("edges", [])
    claims = graph.get("claims", [])
    if not isinstance(nodes, list) or any(not isinstance(item, dict) for item in nodes):
        raise SearchCoverageInputError("trace_graph.nodes must be an array of objects")
    if not isinstance(edges, list) or any(not isinstance(item, dict) for item in edges):
        raise SearchCoverageInputError("trace_graph.edges must be an array of objects")
    if not isinstance(claims, list) or any(not isinstance(item, dict) for item in claims):
        raise SearchCoverageInputError("trace_graph.claims must be an array of objects")

    node_by_id = {
        item["id"]: item for item in nodes if isinstance(item.get("id"), str)
    }
    edge_by_id = {
        item["id"]: item for item in edges if isinstance(item.get("id"), str)
    }
    claim_by_id = {
        item["id"]: item for item in claims if isinstance(item.get("id"), str)
    }

    basis_refs = _as_string_list(
        evidence.get("comparison_basis_claim_refs", []),
        "coverage_evidence.comparison_basis_claim_refs",
    )
    missing_basis = [ref for ref in basis_refs if ref not in claim_by_id]
    if missing_basis:
        return _result(
            fixture_id,
            status="FAIL",
            coverage_status="UNUSABLE_COMPARISON_BASIS",
            basis_refs=basis_refs,
            failure_codes=[FAIL_REFERENCE],
            diagnostics=[
                "unresolvable comparison basis claim refs: " + ", ".join(missing_basis)
            ],
        )

    if assessment_status == "NOT_ASSESSABLE":
        return _result(
            fixture_id,
            status="PASS",
            coverage_status="NOT_ASSESSABLE",
            basis_refs=basis_refs,
            diagnostics=["coverage comparison explicitly marked not assessable"],
        )

    if assessment_status == "UNAVAILABLE":
        reason_refs = _as_string_list(
            evidence.get("unavailability_reason_claim_refs", []),
            "coverage_evidence.unavailability_reason_claim_refs",
        )
        missing_reasons = [ref for ref in reason_refs if ref not in claim_by_id]
        if not reason_refs or missing_reasons:
            diagnostics = ["UNAVAILABLE coverage assessment requires resolvable reason claims"]
            if missing_reasons:
                diagnostics.append(
                    "unresolvable unavailability reason claim refs: "
                    + ", ".join(missing_reasons)
                )
            return _result(
                fixture_id,
                status="FAIL",
                coverage_status="UNUSABLE_UNAVAILABILITY_RECORD",
                basis_refs=basis_refs,
                failure_codes=[FAIL_REFERENCE],
                diagnostics=diagnostics,
            )
        return _result(
            fixture_id,
            status="PASS",
            coverage_status="NOT_APPLICABLE_INFORMATION_UNAVAILABLE",
            basis_refs=basis_refs,
            diagnostics=[
                "search coverage not assessed because INFORMATION is explicitly unavailable"
            ],
        )

    transition_ref = evidence.get("information_transition_ref")
    if not isinstance(transition_ref, str) or not transition_ref:
        return _result(
            fixture_id,
            status="FAIL",
            coverage_status="UNBOUND_INFORMATION_TRANSITION",
            basis_refs=basis_refs,
            failure_codes=[FAIL_REFERENCE],
            diagnostics=["ASSESS requires information_transition_ref"],
        )

    transition = node_by_id.get(transition_ref)
    transition_attributes = transition.get("attributes", {}) if transition else {}
    transition_mode = (
        transition_attributes.get("transition_mode")
        if isinstance(transition_attributes, dict)
        else None
    )
    if (
        not transition
        or transition.get("type") != "TRANSITION"
        or not isinstance(transition_mode, str)
        or transition_mode.upper() != "INFORMATION"
    ):
        return _result(
            fixture_id,
            status="FAIL",
            coverage_status="UNBOUND_INFORMATION_TRANSITION",
            transition_ref=transition_ref,
            basis_refs=basis_refs,
            failure_codes=[FAIL_REFERENCE],
            diagnostics=[
                "information_transition_ref does not resolve to an INFORMATION TRANSITION"
            ],
        )

    aperture_ref = transition_attributes.get("aperture_ref")
    aperture = node_by_id.get(aperture_ref) if isinstance(aperture_ref, str) else None
    if not aperture or aperture.get("type") != "APERTURE":
        return _result(
            fixture_id,
            status="FAIL",
            coverage_status="UNBOUND_APERTURE",
            transition_ref=transition_ref,
            aperture_ref=aperture_ref if isinstance(aperture_ref, str) else None,
            basis_refs=basis_refs,
            failure_codes=[FAIL_REFERENCE],
            diagnostics=["INFORMATION transition does not bind to a resolvable APERTURE"],
        )

    targets = _as_string_list(
        evidence.get("required_target_refs", []),
        "coverage_evidence.required_target_refs",
    )
    if not targets:
        return _result(
            fixture_id,
            status="PASS",
            coverage_status="NOT_ASSESSABLE",
            transition_ref=transition_ref,
            aperture_ref=aperture_ref,
            basis_refs=basis_refs,
            diagnostics=["no required discovery target was supplied"],
        )

    missing_targets = [ref for ref in targets if ref not in node_by_id]
    if missing_targets:
        return _result(
            fixture_id,
            status="FAIL",
            coverage_status="UNUSABLE_TARGET_SET",
            transition_ref=transition_ref,
            aperture_ref=aperture_ref,
            targets=targets,
            basis_refs=basis_refs,
            failure_codes=[FAIL_REFERENCE],
            diagnostics=["unresolvable required target refs: " + ", ".join(missing_targets)],
        )

    aperture_attributes = aperture.get("attributes", {})
    blindspots = set(
        _as_string_list(
            aperture_attributes.get("blindspots", [])
            if isinstance(aperture_attributes, dict)
            else [],
            f"APERTURE {aperture_ref}.attributes.blindspots",
        )
    )
    cannot_access_targets = {
        edge.get("to")
        for edge in edges
        if edge.get("type") == "CANNOT_ACCESS" and edge.get("from") == aperture_ref
    }
    contradicted = [
        target for target in targets if target in blindspots or target in cannot_access_targets
    ]
    if contradicted:
        return _result(
            fixture_id,
            status="FAIL",
            coverage_status="CONTRADICTED",
            transition_ref=transition_ref,
            aperture_ref=aperture_ref,
            targets=targets,
            basis_refs=basis_refs,
            contradicted_targets=contradicted,
            failure_codes=[FAIL_CONTRADICTION],
            diagnostics=[
                "required discovery target is explicitly outside the selected aperture: "
                + ", ".join(contradicted)
            ],
        )

    raw_paths = evidence.get("target_path_edge_refs", {})
    paths = _as_dict(raw_paths, "coverage_evidence.target_path_edge_refs")
    validated_targets: list[str] = []
    reference_errors: list[str] = []
    unsupported: list[str] = []

    for target in targets:
        edge_refs = _as_string_list(
            paths.get(target, []),
            f"coverage_evidence.target_path_edge_refs.{target}",
        )
        path_status, diagnostics = _validate_path(
            target_ref=target,
            edge_refs=edge_refs,
            edge_by_id=edge_by_id,
            allowed_starts={transition_ref, aperture_ref},
        )
        if path_status == "VALID":
            validated_targets.append(target)
        elif path_status == "REFERENCE_ERROR":
            reference_errors.extend(diagnostics)
        else:
            unsupported.extend(diagnostics)

    if reference_errors:
        return _result(
            fixture_id,
            status="FAIL",
            coverage_status="UNUSABLE_REACHABILITY_PATH",
            transition_ref=transition_ref,
            aperture_ref=aperture_ref,
            targets=targets,
            basis_refs=basis_refs,
            validated_targets=validated_targets,
            failure_codes=[FAIL_REFERENCE],
            diagnostics=reference_errors + unsupported,
        )

    if unsupported or len(validated_targets) != len(targets):
        return _result(
            fixture_id,
            status="FAIL",
            coverage_status="UNSUPPORTED_REACHABILITY",
            transition_ref=transition_ref,
            aperture_ref=aperture_ref,
            targets=targets,
            basis_refs=basis_refs,
            validated_targets=validated_targets,
            failure_codes=[FAIL_UNSUPPORTED],
            diagnostics=unsupported,
        )

    return _result(
        fixture_id,
        status="PASS",
        coverage_status="DECLARED_REACHABILITY_CHAIN",
        transition_ref=transition_ref,
        aperture_ref=aperture_ref,
        targets=targets,
        basis_refs=basis_refs,
        validated_targets=validated_targets,
        diagnostics=[
            "packet contains a contiguous declared path to each supplied target; "
            "actual reachability is not established"
        ],
    )


def _main(argv: list[str] | None = None) -> int:
    from search_coverage_fixtures import SEARCH_COVERAGE_FIXTURES

    parser = argparse.ArgumentParser(
        description="Run the bounded TRACE search-coverage contradiction fixtures."
    )
    parser.add_argument("--compact", action="store_true", help="emit compact JSON")
    args = parser.parse_args(argv)

    rows: list[dict[str, Any]] = []
    mismatch = False
    for fixture in SEARCH_COVERAGE_FIXTURES:
        result = check_search_coverage(fixture).to_dict()
        expected = fixture["coverage_expected"]
        matches = (
            result["status"] == expected["status"]
            and result["coverage_status"] == expected["coverage_status"]
            and result["failure_codes"] == expected.get("failure_codes", [])
        )
        mismatch = mismatch or not matches
        rows.append(
            {
                "fixture_id": fixture["fixture_id"],
                "actual_status": result["status"],
                "actual_coverage_status": result["coverage_status"],
                "actual_failure_codes": result["failure_codes"],
                "expected_status": expected["status"],
                "expected_coverage_status": expected["coverage_status"],
                "expected_failure_codes": expected.get("failure_codes", []),
                "matches_expected": matches,
            }
        )

    output = {
        "candidate_id": CANDIDATE_ID,
        "all_match_expected": not mismatch,
        "results": rows,
        "epistemic_limit": EPISTEMIC_LIMIT,
    }
    print(json.dumps(output, indent=None if args.compact else 2, sort_keys=True))
    return 1 if mismatch else 0


if __name__ == "__main__":
    raise SystemExit(_main())
