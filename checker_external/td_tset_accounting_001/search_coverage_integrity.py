"""Hostile integrity pass for TD-TSET-SEARCH-COVERAGE-001.

This pass keeps stronger comparison-envelope assumptions separate from the base
coverage checker. It verifies that basis claims and declared path edges are
usable without claiming that their propositions are true.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping

from search_coverage import (
    FAIL_REFERENCE,
    FAIL_UNSUPPORTED,
    SearchCoverageInputError,
)

CANDIDATE_ID = "TD-TSET-SEARCH-COVERAGE-002-HOSTILE-INTEGRITY"

EPISTEMIC_LIMIT = (
    "This integrity pass checks only whether the checker comparison envelope is "
    "bound to resolvable packet claims and directed, claim-bearing path edges. "
    "It does not establish that the claims are true, that the route executes, or "
    "that the supplied target set is complete."
)


@dataclass(slots=True)
class SearchCoverageIntegrityResult:
    fixture_id: str
    status: str
    failure_codes: list[str] = field(default_factory=list)
    diagnostics: list[str] = field(default_factory=list)
    epistemic_limit: str = EPISTEMIC_LIMIT

    def to_dict(self) -> dict[str, Any]:
        return {
            "candidate_id": CANDIDATE_ID,
            "fixture_id": self.fixture_id,
            "status": self.status,
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


def _claim_dependency_refs(claim: Mapping[str, Any]) -> set[str]:
    refs: set[str] = set()
    for key in ("source_refs", "provenance_edge_refs", "alternative_hypothesis_refs"):
        value = claim.get(key, [])
        if isinstance(value, list):
            refs.update(item for item in value if isinstance(item, str))
    return refs


def check_search_coverage_integrity(
    envelope: Mapping[str, Any],
) -> SearchCoverageIntegrityResult:
    envelope_dict = _as_dict(dict(envelope), "envelope")
    fixture_id = str(envelope_dict.get("fixture_id", "UNNAMED"))
    graph = _as_dict(envelope_dict.get("trace_graph"), "trace_graph")
    raw_evidence = envelope_dict.get("coverage_evidence")

    if raw_evidence is None:
        return SearchCoverageIntegrityResult(fixture_id=fixture_id, status="PASS")

    evidence = _as_dict(raw_evidence, "coverage_evidence")
    assessment_status = evidence.get("assessment_status", "NOT_ASSESSABLE")
    if not isinstance(assessment_status, str):
        raise SearchCoverageInputError("coverage_evidence.assessment_status must be a string")
    assessment_status = assessment_status.upper()
    if assessment_status == "NOT_ASSESSABLE":
        return SearchCoverageIntegrityResult(fixture_id=fixture_id, status="PASS")

    claims = graph.get("claims", [])
    edges = graph.get("edges", [])
    if not isinstance(claims, list) or any(not isinstance(item, dict) for item in claims):
        raise SearchCoverageInputError("trace_graph.claims must be an array of objects")
    if not isinstance(edges, list) or any(not isinstance(item, dict) for item in edges):
        raise SearchCoverageInputError("trace_graph.edges must be an array of objects")

    claim_by_id = {
        item["id"]: item for item in claims if isinstance(item.get("id"), str)
    }
    edge_by_id = {
        item["id"]: item for item in edges if isinstance(item.get("id"), str)
    }

    basis_refs = _as_string_list(
        evidence.get("comparison_basis_claim_refs", []),
        "coverage_evidence.comparison_basis_claim_refs",
    )
    diagnostics: list[str] = []
    failure_codes: list[str] = []

    if not basis_refs:
        diagnostics.append(
            f"{assessment_status} coverage assessment has no comparison basis claims"
        )
        failure_codes.append(FAIL_UNSUPPORTED)
    missing_basis = [ref for ref in basis_refs if ref not in claim_by_id]
    if missing_basis:
        diagnostics.append(
            "unresolvable comparison basis claim refs: " + ", ".join(missing_basis)
        )
        failure_codes.append(FAIL_REFERENCE)

    if assessment_status == "UNAVAILABLE":
        reason_refs = _as_string_list(
            evidence.get("unavailability_reason_claim_refs", []),
            "coverage_evidence.unavailability_reason_claim_refs",
        )
        missing_reasons = [ref for ref in reason_refs if ref not in claim_by_id]
        if not reason_refs:
            diagnostics.append("UNAVAILABLE assessment has no reason claims")
            failure_codes.append(FAIL_UNSUPPORTED)
        if missing_reasons:
            diagnostics.append(
                "unresolvable unavailability reason claim refs: "
                + ", ".join(missing_reasons)
            )
            failure_codes.append(FAIL_REFERENCE)

        supported: set[str] = set()
        for ref in reason_refs:
            claim = claim_by_id.get(ref)
            if claim:
                supported.add(ref)
                supported.update(_claim_dependency_refs(claim))
        unbound_basis = [ref for ref in basis_refs if ref not in supported]
        if basis_refs and unbound_basis:
            diagnostics.append(
                "unavailability reasons do not bind comparison basis claims: "
                + ", ".join(unbound_basis)
            )
            failure_codes.append(FAIL_UNSUPPORTED)

    elif assessment_status == "ASSESS":
        targets = _as_string_list(
            evidence.get("required_target_refs", []),
            "coverage_evidence.required_target_refs",
        )
        paths = _as_dict(
            evidence.get("target_path_edge_refs", {}),
            "coverage_evidence.target_path_edge_refs",
        )

        for target in targets:
            path_refs = _as_string_list(
                paths.get(target, []),
                f"coverage_evidence.target_path_edge_refs.{target}",
            )
            path_claim_refs: set[str] = set()
            for edge_ref in path_refs:
                edge = edge_by_id.get(edge_ref)
                if not edge:
                    diagnostics.append(f"unresolvable path edge ref: {edge_ref}")
                    failure_codes.append(FAIL_REFERENCE)
                    continue
                if edge.get("directed") is not True:
                    diagnostics.append(f"path edge {edge_ref} is not directed")
                    failure_codes.append(FAIL_UNSUPPORTED)
                claim_refs = _as_string_list(
                    edge.get("claim_refs", []), f"edge {edge_ref}.claim_refs"
                )
                if not claim_refs:
                    diagnostics.append(f"path edge {edge_ref} has no supporting claim refs")
                    failure_codes.append(FAIL_UNSUPPORTED)
                missing_edge_claims = [ref for ref in claim_refs if ref not in claim_by_id]
                if missing_edge_claims:
                    diagnostics.append(
                        f"path edge {edge_ref} has unresolvable claim refs: "
                        + ", ".join(missing_edge_claims)
                    )
                    failure_codes.append(FAIL_REFERENCE)
                path_claim_refs.update(ref for ref in claim_refs if ref in claim_by_id)

            if path_refs and basis_refs and not path_claim_refs.intersection(basis_refs):
                diagnostics.append(
                    f"declared path to {target} has no claim shared with the comparison basis"
                )
                failure_codes.append(FAIL_UNSUPPORTED)

    unique_codes: list[str] = []
    for code in failure_codes:
        if code not in unique_codes:
            unique_codes.append(code)

    return SearchCoverageIntegrityResult(
        fixture_id=fixture_id,
        status="FAIL" if unique_codes else "PASS",
        failure_codes=unique_codes,
        diagnostics=diagnostics,
    )
