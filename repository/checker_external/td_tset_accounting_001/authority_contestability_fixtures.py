"""Schema-valid constructed fixtures for TD-AUTHORITY-CONTESTABILITY-001."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from applied_scene_001 import claim, edge, node
from authority_handoff_fixtures import (
    add_bound_brake,
    add_declared_handoff,
    base_conflict_graph,
)


def contest_graph(
    reading_id: str,
    *,
    route_seconds: int | float | None,
    deadline_seconds: int | float | None,
    capture_status: str = "UNCAPTURED",
    include_route: bool = True,
    include_authority_claim: bool = True,
) -> dict[str, Any]:
    graph = base_conflict_graph(reading_id)
    add_declared_handoff(
        graph,
        selected_result_ref="n_record_operator_result",
        transition_ref="n_transition_launch",
        mode="ACT",
    )
    add_bound_brake(graph, "n_transition_launch")

    route_proposition = (
        "The dispatch-result challenge can be routed to the safety brake "
        + (
            f"in {route_seconds} seconds."
            if route_seconds is not None
            else "with unresolved latency."
        )
    )
    deadline_proposition = (
        f"The declared contest deadline occurs in {deadline_seconds} seconds."
        if deadline_seconds is not None
        else "The declared contest deadline is unresolved."
    )
    graph["claims"].extend(
        [
            claim(
                "c_contest_route",
                route_proposition,
                source_refs=["c_aperture_conflict", "c_brake_authority"],
            ),
            claim(
                "c_contest_route_clock",
                route_proposition,
                source_refs=["c_contest_route"],
            ),
            claim(
                "c_contest_deadline",
                deadline_proposition,
                source_refs=["c_selection"],
            ),
        ]
    )
    graph["nodes"].extend(
        [
            node(
                "n_clock_contest_route",
                "CLOCK",
                claim_refs=["c_contest_route_clock"],
                attributes={
                    "clock_type": "ROUTING",
                    "seconds": route_seconds,
                },
            ),
            node(
                "n_clock_contest_deadline",
                "CLOCK",
                claim_refs=["c_contest_deadline"],
                attributes={
                    "clock_type": "PLANNING",
                    "deadline_kind": "PRE_COMMIT_CONTEST",
                    "seconds": deadline_seconds,
                },
            ),
        ]
    )
    graph["discipline"]["clock_typing"]["planning_refs"].extend(
        ["n_clock_contest_route", "n_clock_contest_deadline"]
    )

    if include_route:
        authority_claim_refs = ["c_brake_authority"] if include_authority_claim else []
        route_claim_refs = ["c_contest_route", "c_aperture_conflict"] + authority_claim_refs
        graph["nodes"].append(
            node(
                "n_route_dispatch_contest",
                "ROUTE",
                claim_refs=route_claim_refs,
                attributes={
                    "origin_ref": "n_record_dispatch_result",
                    "destination_ref": "n_brake_safety",
                    "latency_seconds": route_seconds,
                    "route_clock_ref": "n_clock_contest_route",
                    "capture_status": capture_status,
                    "authority_claim_ref": (
                        "c_brake_authority" if include_authority_claim else None
                    ),
                },
            )
        )
        graph["edges"].extend(
            [
                edge(
                    "e_dispatch_result_routes_to_contest",
                    "ROUTES_TO",
                    "n_record_dispatch_result",
                    "n_route_dispatch_contest",
                    claim_refs=["c_contest_route", "c_aperture_conflict"],
                ),
                edge(
                    "e_contest_route_routes_to_brake",
                    "ROUTES_TO",
                    "n_route_dispatch_contest",
                    "n_brake_safety",
                    claim_refs=["c_contest_route"] + authority_claim_refs,
                ),
            ]
        )
        graph["discipline"]["layer_handoff"]["domain_input_refs"].append(
            "n_route_dispatch_contest"
        )

    return graph


def evidence(
    *,
    contest_route_ref: str | None = "n_route_dispatch_contest",
    route_clock_ref: str | None = "n_clock_contest_route",
    deadline_clock_ref: str | None = "n_clock_contest_deadline",
    include_authority_claim: bool = True,
) -> dict[str, Any]:
    return {
        "assessment_status": "ASSESS",
        "conflict_status": "DIVERGENT",
        "selected_transition_ref": "n_transition_launch",
        "challenging_aperture_result_refs": ["n_record_dispatch_result"],
        "contest_route_ref": contest_route_ref,
        "brake_ref": "n_brake_safety",
        "route_clock_ref": route_clock_ref,
        "contest_deadline_clock_ref": deadline_clock_ref,
        "conflict_claim_refs": ["c_aperture_conflict"],
        "contest_authority_claim_refs": (
            ["c_brake_authority"] if include_authority_claim else []
        ),
    }


AG_TIMELY_CONTEST_ROUTE: dict[str, Any] = {
    "fixture_id": "AG_TIMELY_CONTEST_ROUTE",
    "trace_graph": contest_graph(
        "ag_timely_contest_route",
        route_seconds=4,
        deadline_seconds=20,
    ),
    "authority_contestability_evidence": evidence(),
    "contestability_expected": {
        "status": "PASS",
        "contestability_status": "DECLARED_ROUTE_REACHES_BRAKE_BEFORE_DEADLINE",
        "failure_codes": [],
    },
}


AH_CONTEST_ROUTE_TOO_SLOW: dict[str, Any] = {
    "fixture_id": "AH_CONTEST_ROUTE_TOO_SLOW",
    "trace_graph": contest_graph(
        "ah_contest_route_too_slow",
        route_seconds=25,
        deadline_seconds=20,
    ),
    "authority_contestability_evidence": evidence(),
    "contestability_expected": {
        "status": "FAIL",
        "contestability_status": "CONTEST_ROUTE_TOO_SLOW",
        "failure_codes": ["TD-AUTHORITY-CONTEST-ROUTE-TOO-SLOW"],
    },
}


AI_NO_CONTEST_ROUTE: dict[str, Any] = {
    "fixture_id": "AI_NO_CONTEST_ROUTE",
    "trace_graph": contest_graph(
        "ai_no_contest_route",
        route_seconds=4,
        deadline_seconds=20,
        include_route=False,
    ),
    "authority_contestability_evidence": evidence(contest_route_ref=None),
    "contestability_expected": {
        "status": "FAIL",
        "contestability_status": "NO_CONTEST_ROUTE",
        "failure_codes": ["TD-AUTHORITY-CONTEST-NO-ROUTE"],
    },
}


AJ_CAPTURED_CONTEST_ROUTE: dict[str, Any] = {
    "fixture_id": "AJ_CAPTURED_CONTEST_ROUTE",
    "trace_graph": contest_graph(
        "aj_captured_contest_route",
        route_seconds=4,
        deadline_seconds=20,
        capture_status="CAPTURED",
    ),
    "authority_contestability_evidence": evidence(),
    "contestability_expected": {
        "status": "FAIL",
        "contestability_status": "CONTEST_ROUTE_CAPTURED",
        "failure_codes": ["TD-AUTHORITY-CONTEST-ROUTE-CAPTURED"],
    },
}


AK_CONTESTABILITY_UNKNOWN: dict[str, Any] = {
    "fixture_id": "AK_CONTESTABILITY_UNKNOWN",
    "trace_graph": contest_graph(
        "ak_contestability_unknown",
        route_seconds=None,
        deadline_seconds=20,
        capture_status="UNKNOWN",
    ),
    "authority_contestability_evidence": evidence(),
    "contestability_expected": {
        "status": "PASS",
        "contestability_status": "CONTESTABILITY_UNKNOWN",
        "failure_codes": [],
    },
}


AL_UNSUPPORTED_CONTEST_AUTHORITY: dict[str, Any] = {
    "fixture_id": "AL_UNSUPPORTED_CONTEST_AUTHORITY",
    "trace_graph": contest_graph(
        "al_unsupported_contest_authority",
        route_seconds=4,
        deadline_seconds=20,
        include_authority_claim=False,
    ),
    "authority_contestability_evidence": evidence(include_authority_claim=False),
    "contestability_expected": {
        "status": "FAIL",
        "contestability_status": "UNSUPPORTED_CONTEST_ROUTE",
        "failure_codes": ["TD-AUTHORITY-CONTEST-UNSUPPORTED-STATUS"],
    },
}


AUTHORITY_CONTESTABILITY_FIXTURES: tuple[dict[str, Any], ...] = (
    AG_TIMELY_CONTEST_ROUTE,
    AH_CONTEST_ROUTE_TOO_SLOW,
    AI_NO_CONTEST_ROUTE,
    AJ_CAPTURED_CONTEST_ROUTE,
    AK_CONTESTABILITY_UNKNOWN,
    AL_UNSUPPORTED_CONTEST_AUTHORITY,
)
