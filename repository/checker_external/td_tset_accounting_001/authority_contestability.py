#!/usr/bin/env python3
"""Checker-external contestability candidate for declared authority handoffs.

Candidate ID: TD-AUTHORITY-CONTESTABILITY-001

This checker does not determine whether an authority is legitimate or whether a
challenge should prevail. It tests whether a supplied conflicting aperture
result has a declared route to a bound brake before a declared contest deadline,
while preserving capture and clock uncertainty.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, field
from typing import Any, Mapping

CANDIDATE_ID = "TD-AUTHORITY-CONTESTABILITY-001"

FAIL_REFERENCE = "TD-AUTHORITY-CONTEST-REFERENCE-MISMATCH"
FAIL_NO_ROUTE = "TD-AUTHORITY-CONTEST-NO-ROUTE"
FAIL_TOO_SLOW = "TD-AUTHORITY-CONTEST-ROUTE-TOO-SLOW"
FAIL_CAPTURED = "TD-AUTHORITY-CONTEST-ROUTE-CAPTURED"
FAIL_UNBOUND_BRAKE = "TD-AUTHORITY-CONTEST-UNBOUND-BRAKE"
FAIL_UNSUPPORTED = "TD-AUTHORITY-CONTEST-UNSUPPORTED-STATUS"

ASSESSMENT_STATUSES = frozenset({"ASSESS", "NOT_ASSESSABLE"})
CONFLICT_STATUSES = frozenset({"DIVERGENT", "NO_DIVERGENCE", "UNKNOWN"})
CAPTURE_STATUSES = frozenset({"UNCAPTURED", "CAPTURED", "UNKNOWN"})

EPISTEMIC_LIMIT = (
    "This checker tests a declared challenge route, bound brake, capture status, "
    "and route/deadline clocks relative to supplied packet evidence. PASS does not "
    "establish legitimate authority, actual route executability, brake independence, "
    "correct challenge, complete affected-scope discovery, or world truth."
)


class AuthorityContestabilityInputError(ValueError):
    """Raised when the comparison envelope is structurally unusable."""


@dataclass(slots=True)
class AuthorityContestabilityResult:
    fixture_id: str
    status: str
    contestability_status: str
    conflict_status: str
    selected_transition_ref: str | None = None
    challenging_result_refs: list[str] = field(default_factory=list)
    contest_route_ref: str | None = None
    brake_ref: str | None = None
    route_seconds: float | int | None = None
    deadline_seconds: float | int | None = None
    margin_seconds: float | int | None = None
    failure_codes: list[str] = field(default_factory=list)
    diagnostics: list[str] = field(default_factory=list)
    epistemic_limit: str = EPISTEMIC_LIMIT

    def to_dict(self) -> dict[str, Any]:
        return {
            "candidate_id": CANDIDATE_ID,
            "fixture_id": self.fixture_id,
            "status": self.status,
            "contestability_status": self.contestability_status,
            "conflict_status": self.conflict_status,
            "selected_transition_ref": self.selected_transition_ref,
            "challenging_result_refs": self.challenging_result_refs,
            "contest_route_ref": self.contest_route_ref,
            "brake_ref": self.brake_ref,
            "route_seconds": self.route_seconds,
            "deadline_seconds": self.deadline_seconds,
            "margin_seconds": self.margin_seconds,
            "failure_codes": self.failure_codes,
            "diagnostics": self.diagnostics,
            "epistemic_limit": self.epistemic_limit,
        }


def _as_dict(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise AuthorityContestabilityInputError(f"{label} must be an object")
    return value


def _as_string_list(value: Any, label: str) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        raise AuthorityContestabilityInputError(f"{label} must be an array of strings")
    return list(value)


def _number_or_none(value: Any, label: str) -> float | int | None:
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise AuthorityContestabilityInputError(f"{label} must be a non-negative number or null")
    if value < 0:
        raise AuthorityContestabilityInputError(f"{label} must be non-negative")
    return value


def _result(
    fixture_id: str,
    *,
    status: str,
    contestability_status: str,
    conflict_status: str,
    selected_transition_ref: str | None = None,
    challenging_result_refs: list[str] | None = None,
    contest_route_ref: str | None = None,
    brake_ref: str | None = None,
    route_seconds: float | int | None = None,
    deadline_seconds: float | int | None = None,
    margin_seconds: float | int | None = None,
    failure_codes: list[str] | None = None,
    diagnostics: list[str] | None = None,
) -> AuthorityContestabilityResult:
    return AuthorityContestabilityResult(
        fixture_id=fixture_id,
        status=status,
        contestability_status=contestability_status,
        conflict_status=conflict_status,
        selected_transition_ref=selected_transition_ref,
        challenging_result_refs=challenging_result_refs or [],
        contest_route_ref=contest_route_ref,
        brake_ref=brake_ref,
        route_seconds=route_seconds,
        deadline_seconds=deadline_seconds,
        margin_seconds=margin_seconds,
        failure_codes=failure_codes or [],
        diagnostics=diagnostics or [],
    )


def _matching_edges(
    edges: list[Mapping[str, Any]],
    edge_type: str,
    *,
    from_ref: str | None = None,
    to_ref: str | None = None,
) -> list[Mapping[str, Any]]:
    matches: list[Mapping[str, Any]] = []
    for edge in edges:
        if edge.get("type") != edge_type:
            continue
        if from_ref is not None and edge.get("from") != from_ref:
            continue
        if to_ref is not None and edge.get("to") != to_ref:
            continue
        matches.append(edge)
    return matches


def check_authority_contestability(
    envelope: Mapping[str, Any],
) -> AuthorityContestabilityResult:
    envelope_dict = _as_dict(dict(envelope), "envelope")
    fixture_id = str(envelope_dict.get("fixture_id", "UNNAMED"))
    graph = _as_dict(envelope_dict.get("trace_graph"), "trace_graph")

    raw_evidence = envelope_dict.get("authority_contestability_evidence")
    if raw_evidence is None:
        return _result(
            fixture_id,
            status="PASS",
            contestability_status="NOT_ASSESSABLE",
            conflict_status="UNKNOWN",
            diagnostics=["no authority-contestability comparison envelope supplied"],
        )
    evidence = _as_dict(raw_evidence, "authority_contestability_evidence")

    assessment_status = evidence.get("assessment_status", "NOT_ASSESSABLE")
    if not isinstance(assessment_status, str):
        raise AuthorityContestabilityInputError("assessment_status must be a string")
    assessment_status = assessment_status.upper()
    if assessment_status not in ASSESSMENT_STATUSES:
        raise AuthorityContestabilityInputError(
            "assessment_status must be one of " + ", ".join(sorted(ASSESSMENT_STATUSES))
        )

    conflict_status = evidence.get("conflict_status", "UNKNOWN")
    if not isinstance(conflict_status, str):
        raise AuthorityContestabilityInputError("conflict_status must be a string")
    conflict_status = conflict_status.upper()
    if conflict_status not in CONFLICT_STATUSES:
        raise AuthorityContestabilityInputError(
            "conflict_status must be one of " + ", ".join(sorted(CONFLICT_STATUSES))
        )

    if assessment_status == "NOT_ASSESSABLE":
        return _result(
            fixture_id,
            status="PASS",
            contestability_status="NOT_ASSESSABLE",
            conflict_status=conflict_status,
            diagnostics=["contestability comparison explicitly marked not assessable"],
        )
    if conflict_status == "NO_DIVERGENCE":
        return _result(
            fixture_id,
            status="PASS",
            contestability_status="NOT_APPLICABLE_NO_DIVERGENCE",
            conflict_status=conflict_status,
        )
    if conflict_status == "UNKNOWN":
        return _result(
            fixture_id,
            status="PASS",
            contestability_status="CONFLICT_STATUS_UNKNOWN",
            conflict_status=conflict_status,
            diagnostics=["aperture divergence remains UNKNOWN"],
        )

    nodes = graph.get("nodes", [])
    edges = graph.get("edges", [])
    claims = graph.get("claims", [])
    if not isinstance(nodes, list) or any(not isinstance(item, dict) for item in nodes):
        raise AuthorityContestabilityInputError("trace_graph.nodes must be an array of objects")
    if not isinstance(edges, list) or any(not isinstance(item, dict) for item in edges):
        raise AuthorityContestabilityInputError("trace_graph.edges must be an array of objects")
    if not isinstance(claims, list) or any(not isinstance(item, dict) for item in claims):
        raise AuthorityContestabilityInputError("trace_graph.claims must be an array of objects")

    node_by_id = {
        item["id"]: item for item in nodes if isinstance(item.get("id"), str)
    }
    claim_by_id = {
        item["id"]: item for item in claims if isinstance(item.get("id"), str)
    }

    selected_transition_ref = evidence.get("selected_transition_ref")
    selected_transition_ref = (
        selected_transition_ref
        if isinstance(selected_transition_ref, str) and selected_transition_ref
        else None
    )
    challenging_result_refs = _as_string_list(
        evidence.get("challenging_aperture_result_refs", []),
        "authority_contestability_evidence.challenging_aperture_result_refs",
    )
    contest_route_ref = evidence.get("contest_route_ref")
    contest_route_ref = (
        contest_route_ref if isinstance(contest_route_ref, str) and contest_route_ref else None
    )
    brake_ref = evidence.get("brake_ref")
    brake_ref = brake_ref if isinstance(brake_ref, str) and brake_ref else None
    route_clock_ref = evidence.get("route_clock_ref")
    route_clock_ref = (
        route_clock_ref if isinstance(route_clock_ref, str) and route_clock_ref else None
    )
    deadline_clock_ref = evidence.get("contest_deadline_clock_ref")
    deadline_clock_ref = (
        deadline_clock_ref
        if isinstance(deadline_clock_ref, str) and deadline_clock_ref
        else None
    )
    conflict_claim_refs = _as_string_list(
        evidence.get("conflict_claim_refs", []),
        "authority_contestability_evidence.conflict_claim_refs",
    )
    authority_claim_refs = _as_string_list(
        evidence.get("contest_authority_claim_refs", []),
        "authority_contestability_evidence.contest_authority_claim_refs",
    )

    reference_diagnostics: list[str] = []
    if selected_transition_ref not in node_by_id:
        reference_diagnostics.append("selected transition ref does not resolve")
    elif node_by_id[selected_transition_ref].get("type") != "TRANSITION":
        reference_diagnostics.append("selected transition ref does not resolve to TRANSITION")
    for ref in challenging_result_refs:
        node = node_by_id.get(ref)
        if node is None:
            reference_diagnostics.append(f"challenging aperture result ref does not resolve: {ref}")
        elif node.get("type") not in {"RECORD", "CLAIM"}:
            reference_diagnostics.append(
                f"challenging aperture result must resolve to RECORD or CLAIM: {ref}"
            )
    if contest_route_ref is not None:
        node = node_by_id.get(contest_route_ref)
        if node is None:
            reference_diagnostics.append("contest route ref does not resolve")
        elif node.get("type") != "ROUTE":
            reference_diagnostics.append("contest route ref does not resolve to ROUTE")
    if brake_ref is not None:
        node = node_by_id.get(brake_ref)
        if node is None:
            reference_diagnostics.append("brake ref does not resolve")
        elif node.get("type") != "BRAKE":
            reference_diagnostics.append("brake ref does not resolve to BRAKE")
    for label, ref in (
        ("route clock", route_clock_ref),
        ("contest deadline clock", deadline_clock_ref),
    ):
        if ref is None:
            continue
        node = node_by_id.get(ref)
        if node is None:
            reference_diagnostics.append(f"{label} ref does not resolve")
        elif node.get("type") != "CLOCK":
            reference_diagnostics.append(f"{label} ref does not resolve to CLOCK")
    missing_claims = [
        ref
        for ref in conflict_claim_refs + authority_claim_refs
        if ref not in claim_by_id
    ]
    if missing_claims:
        reference_diagnostics.append(
            "unresolvable conflict or contest-authority claim refs: "
            + ", ".join(missing_claims)
        )

    if reference_diagnostics:
        return _result(
            fixture_id,
            status="FAIL",
            contestability_status="UNUSABLE_CONTESTABILITY_RECORD",
            conflict_status=conflict_status,
            selected_transition_ref=selected_transition_ref,
            challenging_result_refs=challenging_result_refs,
            contest_route_ref=contest_route_ref,
            brake_ref=brake_ref,
            failure_codes=[FAIL_REFERENCE],
            diagnostics=reference_diagnostics,
        )

    if not challenging_result_refs:
        return _result(
            fixture_id,
            status="FAIL",
            contestability_status="NO_CHALLENGING_APERTURE_RESULT",
            conflict_status=conflict_status,
            selected_transition_ref=selected_transition_ref,
            failure_codes=[FAIL_UNSUPPORTED],
            diagnostics=["DIVERGENT contestability assessment requires a challenging result"],
        )

    if contest_route_ref is None:
        return _result(
            fixture_id,
            status="FAIL",
            contestability_status="NO_CONTEST_ROUTE",
            conflict_status=conflict_status,
            selected_transition_ref=selected_transition_ref,
            challenging_result_refs=challenging_result_refs,
            brake_ref=brake_ref,
            failure_codes=[FAIL_NO_ROUTE],
            diagnostics=["no route from the challenging aperture result to a brake is declared"],
        )

    if brake_ref is None:
        return _result(
            fixture_id,
            status="FAIL",
            contestability_status="UNBOUND_CONTEST_BRAKE",
            conflict_status=conflict_status,
            selected_transition_ref=selected_transition_ref,
            challenging_result_refs=challenging_result_refs,
            contest_route_ref=contest_route_ref,
            failure_codes=[FAIL_UNBOUND_BRAKE],
            diagnostics=["contest route has no declared brake target"],
        )

    route_node = node_by_id[contest_route_ref]
    route_attributes = _as_dict(route_node.get("attributes", {}), "contest route attributes")
    capture_status = route_attributes.get("capture_status", "UNKNOWN")
    if not isinstance(capture_status, str):
        raise AuthorityContestabilityInputError("contest route capture_status must be a string")
    capture_status = capture_status.upper()
    if capture_status not in CAPTURE_STATUSES:
        raise AuthorityContestabilityInputError(
            "contest route capture_status must be one of "
            + ", ".join(sorted(CAPTURE_STATUSES))
        )

    brake_port = _as_dict(graph.get("ports", {}).get("brake", {}), "ports.brake")
    brake_state = brake_port.get("state", "UNKNOWN")
    if brake_state in {"ABSENT", "PRESENT_CAPTURED"}:
        return _result(
            fixture_id,
            status="FAIL",
            contestability_status="UNBOUND_CONTEST_BRAKE",
            conflict_status=conflict_status,
            selected_transition_ref=selected_transition_ref,
            challenging_result_refs=challenging_result_refs,
            contest_route_ref=contest_route_ref,
            brake_ref=brake_ref,
            failure_codes=[FAIL_UNBOUND_BRAKE],
            diagnostics=[f"brake port state is {brake_state}"],
        )

    challenge_to_route = [
        edge
        for challenge_ref in challenging_result_refs
        for edge in _matching_edges(
            edges, "ROUTES_TO", from_ref=challenge_ref, to_ref=contest_route_ref
        )
    ]
    route_to_brake = _matching_edges(
        edges, "ROUTES_TO", from_ref=contest_route_ref, to_ref=brake_ref
    )
    brake_to_transition = _matching_edges(
        edges, "BRAKES", from_ref=brake_ref, to_ref=selected_transition_ref
    )

    route_diagnostics: list[str] = []
    if not challenge_to_route:
        route_diagnostics.append("challenging aperture result does not ROUTES_TO contest route")
    if not route_to_brake:
        route_diagnostics.append("contest route does not ROUTES_TO brake")
    if not brake_to_transition:
        route_diagnostics.append("brake does not BRAKES selected transition")
    if not authority_claim_refs:
        route_diagnostics.append("contest route has no external authority claim")

    edge_claim_refs = {
        ref
        for edge in challenge_to_route + route_to_brake + brake_to_transition
        for ref in edge.get("claim_refs", [])
        if isinstance(ref, str)
    }
    if authority_claim_refs and not edge_claim_refs.intersection(authority_claim_refs):
        route_diagnostics.append("contest authority claims are not bound to route/brake edges")
    if conflict_claim_refs and not edge_claim_refs.intersection(conflict_claim_refs):
        route_diagnostics.append("conflict claims are not bound to the contest route")

    if route_diagnostics:
        return _result(
            fixture_id,
            status="FAIL",
            contestability_status="UNSUPPORTED_CONTEST_ROUTE",
            conflict_status=conflict_status,
            selected_transition_ref=selected_transition_ref,
            challenging_result_refs=challenging_result_refs,
            contest_route_ref=contest_route_ref,
            brake_ref=brake_ref,
            failure_codes=[FAIL_UNSUPPORTED],
            diagnostics=route_diagnostics,
        )

    if capture_status == "CAPTURED":
        return _result(
            fixture_id,
            status="FAIL",
            contestability_status="CONTEST_ROUTE_CAPTURED",
            conflict_status=conflict_status,
            selected_transition_ref=selected_transition_ref,
            challenging_result_refs=challenging_result_refs,
            contest_route_ref=contest_route_ref,
            brake_ref=brake_ref,
            failure_codes=[FAIL_CAPTURED],
            diagnostics=["contest route is explicitly marked CAPTURED"],
        )

    if route_clock_ref is None or deadline_clock_ref is None:
        return _result(
            fixture_id,
            status="PASS",
            contestability_status="CONTESTABILITY_CLOCK_UNKNOWN",
            conflict_status=conflict_status,
            selected_transition_ref=selected_transition_ref,
            challenging_result_refs=challenging_result_refs,
            contest_route_ref=contest_route_ref,
            brake_ref=brake_ref,
            diagnostics=["route or contest-deadline clock is not supplied"],
        )

    route_clock = node_by_id[route_clock_ref]
    deadline_clock = node_by_id[deadline_clock_ref]
    route_seconds = _number_or_none(
        _as_dict(route_clock.get("attributes", {}), "route clock attributes").get("seconds"),
        "route clock seconds",
    )
    deadline_seconds = _number_or_none(
        _as_dict(deadline_clock.get("attributes", {}), "deadline clock attributes").get("seconds"),
        "deadline clock seconds",
    )

    if capture_status == "UNKNOWN" or route_seconds is None or deadline_seconds is None:
        reasons: list[str] = []
        if capture_status == "UNKNOWN":
            reasons.append("contest route capture status is UNKNOWN")
        if route_seconds is None:
            reasons.append("contest route clock is UNKNOWN")
        if deadline_seconds is None:
            reasons.append("contest deadline clock is UNKNOWN")
        return _result(
            fixture_id,
            status="PASS",
            contestability_status="CONTESTABILITY_UNKNOWN",
            conflict_status=conflict_status,
            selected_transition_ref=selected_transition_ref,
            challenging_result_refs=challenging_result_refs,
            contest_route_ref=contest_route_ref,
            brake_ref=brake_ref,
            route_seconds=route_seconds,
            deadline_seconds=deadline_seconds,
            diagnostics=reasons,
        )

    margin = deadline_seconds - route_seconds
    if route_seconds >= deadline_seconds:
        return _result(
            fixture_id,
            status="FAIL",
            contestability_status="CONTEST_ROUTE_TOO_SLOW",
            conflict_status=conflict_status,
            selected_transition_ref=selected_transition_ref,
            challenging_result_refs=challenging_result_refs,
            contest_route_ref=contest_route_ref,
            brake_ref=brake_ref,
            route_seconds=route_seconds,
            deadline_seconds=deadline_seconds,
            margin_seconds=margin,
            failure_codes=[FAIL_TOO_SLOW],
            diagnostics=[
                "declared contest route does not reach the brake before the declared deadline"
            ],
        )

    return _result(
        fixture_id,
        status="PASS",
        contestability_status="DECLARED_ROUTE_REACHES_BRAKE_BEFORE_DEADLINE",
        conflict_status=conflict_status,
        selected_transition_ref=selected_transition_ref,
        challenging_result_refs=challenging_result_refs,
        contest_route_ref=contest_route_ref,
        brake_ref=brake_ref,
        route_seconds=route_seconds,
        deadline_seconds=deadline_seconds,
        margin_seconds=margin,
        diagnostics=[
            "declared route reaches the declared brake before the declared deadline; actual contestability is not established"
        ],
    )


def _main(argv: list[str] | None = None) -> int:
    from authority_contestability_fixtures import AUTHORITY_CONTESTABILITY_FIXTURES

    parser = argparse.ArgumentParser(
        description="Run bounded authority-contestability fixtures."
    )
    parser.add_argument("--compact", action="store_true", help="emit compact JSON")
    args = parser.parse_args(argv)

    rows: list[dict[str, Any]] = []
    mismatch = False
    for fixture in AUTHORITY_CONTESTABILITY_FIXTURES:
        result = check_authority_contestability(fixture).to_dict()
        expected = fixture["contestability_expected"]
        matches = (
            result["status"] == expected["status"]
            and result["contestability_status"] == expected["contestability_status"]
            and result["failure_codes"] == expected.get("failure_codes", [])
        )
        mismatch = mismatch or not matches
        rows.append(
            {
                "fixture_id": fixture["fixture_id"],
                "actual_status": result["status"],
                "actual_contestability_status": result["contestability_status"],
                "actual_failure_codes": result["failure_codes"],
                "expected_status": expected["status"],
                "expected_contestability_status": expected["contestability_status"],
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
