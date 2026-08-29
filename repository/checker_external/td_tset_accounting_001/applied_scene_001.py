"""Schema-valid constructed applied witnesses for TD-TSET-ACCOUNTING-001.

These fixtures are not records of an actual feral-hog control operation. They
are non-minimal TRACE-GRAPH-0.2.5 packets used to test transfer, emergency
bypass, silent omission, and ritual information-seeking.
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any

TIMESTAMP = "2026-08-04T00:00:00Z"

SCENE_COMMON: dict[str, Any] = {
    "scene_status": "CONSTRUCTED_APPLIED_SCENE",
    "domain": "feral-hog aerial control operation",
    "decision": "A county wildlife unit is preparing an aerial control operation.",
    "mapped_scopes": [
        "crop farmers requesting control",
        "flight and ground operations crew",
        "target feral-hog population",
    ],
    "omitted_scope": "an agricultural field team working inside the proposed flight zone",
    "external_source": "county dispatch record",
    "epistemic_note": (
        "The scene is constructed to test checker behavior. "
        "It is not a record of an actual operation."
    ),
}


def unknown_context() -> dict[str, Any]:
    return {
        "contamination_state": "UNKNOWN",
        "evidence_controlled_by_refs": [],
        "clock_controlled_by_refs": [],
        "delay_advantage_claim_refs": [],
        "delay_cost_carrier_refs": [],
        "resolution_owner_refs": [],
        "resolution_deadline_refs": [],
        "available_pause_or_protection_refs": [],
        "earlier_options_before_urgency_refs": [],
    }


def claim(
    claim_id: str,
    proposition: str,
    *,
    source_refs: list[str] | None = None,
    evidence_state: str = "R",
    claim_kind: str = "STATUS",
) -> dict[str, Any]:
    return {
        "id": claim_id,
        "proposition": proposition,
        "claim_kind": claim_kind,
        "evidence_state": evidence_state,
        "access_state": "A",
        "source_refs": source_refs or [],
        "provenance_edge_refs": [],
        "timestamp": TIMESTAMP,
        "confidence": {"representation": "UNKNOWN", "value": None},
        "alternative_hypothesis_refs": [],
        "unknown_context": unknown_context(),
    }


def node(
    node_id: str,
    node_type: str,
    *,
    claim_refs: list[str] | None = None,
    attributes: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "id": node_id,
        "type": node_type,
        "attributes": attributes or {},
        "claim_refs": claim_refs or [],
    }


def edge(
    edge_id: str,
    edge_type: str,
    from_ref: str,
    to_ref: str,
    *,
    claim_refs: list[str] | None = None,
    attributes: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "id": edge_id,
        "type": edge_type,
        "from": from_ref,
        "to": to_ref,
        "directed": True,
        "attributes": attributes or {},
        "claim_refs": claim_refs or [],
    }


def information_transition(
    transition_id: str,
    basis_claim_refs: list[str],
    *,
    aperture_ref: str,
) -> dict[str, Any]:
    return node(
        transition_id,
        "TRANSITION",
        claim_refs=basis_claim_refs,
        attributes={
            "transition_mode": "INFORMATION",
            "availability_status": "AVAILABLE",
            "basis_claim_refs": basis_claim_refs,
            "aperture_ref": aperture_ref,
            "affected_scope_refs": ["n_entity_field_team"],
            "reversibility": "REVERSIBLE",
            "strategy_revisable": True,
        },
    )


def full_discipline(
    *,
    information_refs: list[str] | None = None,
    unrepresented: list[str] | None = None,
    reason_refs: list[str] | None = None,
    planning_refs: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "transition_set": {
            "action_or_intervention_refs": [],
            "information_refs": information_refs or [],
            "wait_delay_inaction_refs": [],
            "unrepresented_transition_classes": unrepresented or [],
            "unavailability_reason_claim_refs": reason_refs or [],
            "uncertainty_selects_transition": False,
        },
        "clock_typing": {
            "planning_refs": planning_refs or [],
            "detection_refs": [],
            "evidence_hardening_refs": [],
            "irreversibility_refs": [],
            "unsupported_irreversibility_claim_refs": [],
            "deadline_entails_irreversibility": False,
            "hardening_entails_irreversibility": False,
        },
        "scope_granularity": {
            "individual_refs": [],
            "group_refs": ["n_entity_farmers", "n_entity_crew", "n_entity_field_team"],
            "population_refs": ["n_entity_hogs"],
            "ecosystem_refs": [],
            "cross_scale_substitution_claim_refs": [],
            "aggregate_recovery_repairs_individual_loss": False,
        },
        "layer_handoff": {
            "trace_structure_refs": [],
            "value_input_refs": [],
            "domain_input_refs": [],
            "selector_refs": [],
            "actuator_refs": [],
            "unresolved_handoffs": [],
        },
        "evidence_custody": {
            "operator_refs": ["n_entity_unit"],
            "evidence_holder_refs": ["n_record_dispatch"],
            "verifier_refs": [],
            "independent_verifier_refs": [],
            "self_verification_status": "UNKNOWN",
            "control_alone_establishes_deception": False,
        },
    }


def graph(
    reading_id: str,
    *,
    claims: list[dict[str, Any]],
    nodes: list[dict[str, Any]],
    edges: list[dict[str, Any]],
    information_refs: list[str] | None = None,
    unrepresented: list[str] | None = None,
    reason_refs: list[str] | None = None,
    planning_refs: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "schema": "TRACE-GRAPH-0.2.5",
        "trace_version": "0.2.5",
        "reading_id": reading_id,
        "nodes": nodes,
        "edges": edges,
        "claims": claims,
        "ports": {
            "designation": {},
            "measure": {},
            "selector": {"selection_state": "UNKNOWN"},
            "carrier": {"state": "UNKNOWN", "weight_types": []},
            "enforcement": {"state": "UNKNOWN"},
            "brake": {"state": "UNKNOWN"},
        },
        "discipline": full_discipline(
            information_refs=information_refs,
            unrepresented=unrepresented,
            reason_refs=reason_refs,
            planning_refs=planning_refs,
        ),
        "available_transition_refs": [
            item["id"]
            for item in nodes
            if item.get("type") == "TRANSITION"
            and item.get("attributes", {}).get("availability_status") == "AVAILABLE"
        ],
        "institutional_use": {"observable_transition_change": "UNKNOWN"},
        "limits": {
            "receiver_limits": [],
            "unavailable_evidence": [],
            "unresolved_claim_refs": [],
        },
        "anti_clearance": {
            "voluntary_use_only": True,
            "reading_is_not_truth": True,
            "reading_is_not_permission": True,
            "packet_completion_is_not_correction": True,
            "schema_validity_is_not_world_validity": True,
        },
    }


def common_claims(*, route_seconds: int, commit_seconds: int) -> list[dict[str, Any]]:
    return [
        claim("c_scene", "The represented scene is a planned aerial control operation."),
        claim("c_map", "The working map represents three affected scopes."),
        claim(
            "c_omission",
            "The working map omits an agricultural field team inside the proposed flight zone.",
            claim_kind="ABSENT",
        ),
        claim("c_record", "A county dispatch record may reveal the field team."),
        claim(
            f"c_route_{route_seconds}",
            f"The county dispatch record can be queried in {route_seconds} seconds.",
        ),
        claim(
            f"c_commit_{commit_seconds}",
            f"Operational commitment occurs in {commit_seconds} seconds.",
        ),
        claim("c_authority", "The decision unit has authority to query the dispatch record."),
    ]


def common_nodes(*, route_seconds: int, commit_seconds: int) -> list[dict[str, Any]]:
    return [
        node("n_scene_operation", "SCENE", claim_refs=["c_scene"]),
        node("n_map_working", "MAP", claim_refs=["c_map", "c_omission"]),
        node("n_entity_unit", "ENTITY"),
        node("n_entity_farmers", "ENTITY"),
        node("n_entity_crew", "ENTITY"),
        node("n_entity_hogs", "ENTITY"),
        node("n_entity_field_team", "ENTITY", claim_refs=["c_omission"]),
        node("n_record_dispatch", "RECORD", claim_refs=["c_record"]),
        node(
            "n_aperture_dispatch",
            "APERTURE",
            claim_refs=["c_record"],
            attributes={
                "source_refs": ["n_record_dispatch"],
                "blindspots": [],
                "latency_seconds": route_seconds,
            },
        ),
        node(
            "n_route_dispatch",
            "ROUTE",
            claim_refs=[f"c_route_{route_seconds}", "c_authority"],
            attributes={
                "latency_seconds": route_seconds,
                "authority_claim_ref": "c_authority",
                "destination_ref": "n_aperture_dispatch",
            },
        ),
        node(
            "n_clock_commit",
            "CLOCK",
            claim_refs=[f"c_commit_{commit_seconds}"],
            attributes={"clock_type": "PLANNING", "seconds": commit_seconds},
        ),
        node(
            "n_clock_query",
            "CLOCK",
            claim_refs=[f"c_route_{route_seconds}"],
            attributes={"clock_type": "PLANNING", "seconds": route_seconds},
        ),
    ]


def common_edges() -> list[dict[str, Any]]:
    return [
        edge("e_scene_contains_map", "CONTAINS", "n_scene_operation", "n_map_working", claim_refs=["c_map"]),
        edge("e_map_contains_farmers", "CONTAINS", "n_map_working", "n_entity_farmers", claim_refs=["c_map"]),
        edge("e_map_contains_crew", "CONTAINS", "n_map_working", "n_entity_crew", claim_refs=["c_map"]),
        edge("e_map_contains_hogs", "CONTAINS", "n_map_working", "n_entity_hogs", claim_refs=["c_map"]),
        edge("e_map_omits_team", "OMITS", "n_map_working", "n_entity_field_team", claim_refs=["c_omission"]),
        edge("e_record_reports_team", "REPORTS", "n_record_dispatch", "n_entity_field_team", claim_refs=["c_record"]),
        edge("e_route_to_aperture", "ROUTES_TO", "n_route_dispatch", "n_aperture_dispatch", claim_refs=["c_authority"]),
    ]


BASE_LIVE_CLAIMS = common_claims(route_seconds=4, commit_seconds=20) + [
    claim(
        "c_info_live",
        "INFORMATION is materially live before commitment.",
        source_refs=["c_route_4", "c_commit_20", "c_authority"],
    )
]


K_NODES = common_nodes(route_seconds=4, commit_seconds=20) + [
    information_transition(
        "n_info_dispatch",
        ["c_info_live", "c_route_4", "c_commit_20", "c_authority"],
        aperture_ref="n_aperture_dispatch",
    )
]

K_EDGES = common_edges() + [
    edge(
        "e_info_observes_record",
        "OBSERVES",
        "n_info_dispatch",
        "n_record_dispatch",
        claim_refs=["c_info_live"],
    )
]


K_DISCIPLINED_QUERY: dict[str, Any] = {
    "fixture_id": "K_APPLIED_DISCIPLINED_QUERY",
    "scene": {
        **SCENE_COMMON,
        "variant": (
            "The dispatch record is queried before commitment and can expose "
            "the omitted field team."
        ),
    },
    "checker_evidence": {
        "class_assessments": {
            "INFORMATION": {
                "basis_claim_refs": ["c_route_4", "c_commit_20", "c_authority"],
                "evidence_status": "MATERIALLY_LIVE",
            }
        },
        "unavailability_bindings": {},
    },
    "expected": {
        "schema_status": "PASS",
        "combined_status": "PASS",
        "accounting_status": "PASS",
        "integrity_status": "PASS",
    },
    "trace_graph": graph(
        "k_applied_disciplined_query",
        claims=deepcopy(BASE_LIVE_CLAIMS),
        nodes=deepcopy(K_NODES),
        edges=deepcopy(K_EDGES),
        information_refs=["n_info_dispatch"],
        planning_refs=["n_clock_commit", "n_clock_query"],
    ),
}


L_SILENT_OMISSION: dict[str, Any] = {
    "fixture_id": "L_APPLIED_SILENT_OMISSION",
    "scene": {
        **SCENE_COMMON,
        "variant": (
            "The available dispatch query is omitted without an unavailability "
            "or unresolved-status record."
        ),
    },
    "checker_evidence": deepcopy(K_DISCIPLINED_QUERY["checker_evidence"]),
    "expected": {
        "schema_status": "PASS",
        "combined_status": "FAIL",
        "accounting_status": "FAIL",
        "accounting_failure_codes": ["TD-TSET-UNACCOUNTED-CLASS"],
        "integrity_status": "PASS",
    },
    "trace_graph": graph(
        "l_applied_silent_omission",
        claims=deepcopy(BASE_LIVE_CLAIMS),
        nodes=common_nodes(route_seconds=4, commit_seconds=20),
        edges=common_edges(),
        planning_refs=["n_clock_commit", "n_clock_query"],
    ),
}


M_CLAIMS = common_claims(route_seconds=10, commit_seconds=3) + [
    claim(
        "c_info_too_slow",
        "INFORMATION is unavailable before commitment.",
        source_refs=["c_route_10", "c_commit_3"],
    )
]

M_TIME_DOMINATED_BYPASS: dict[str, Any] = {
    "fixture_id": "M_APPLIED_TIME_DOMINATED_BYPASS",
    "scene": {
        **SCENE_COMMON,
        "variant": (
            "The information route is slower than the protective commitment "
            "window, and the bypass is explicitly bound to the clocks."
        ),
    },
    "checker_evidence": {
        "class_assessments": {
            "INFORMATION": {
                "basis_claim_refs": ["c_route_10", "c_commit_3"],
                "evidence_status": "UNAVAILABLE",
            }
        },
        "unavailability_bindings": {"INFORMATION": ["c_info_too_slow"]},
    },
    "expected": {
        "schema_status": "PASS",
        "combined_status": "PASS",
        "accounting_status": "PASS",
        "integrity_status": "PASS",
    },
    "trace_graph": graph(
        "m_applied_time_dominated_bypass",
        claims=M_CLAIMS,
        nodes=common_nodes(route_seconds=10, commit_seconds=3),
        edges=common_edges(),
        unrepresented=["INFORMATION"],
        reason_refs=["c_info_too_slow"],
        planning_refs=["n_clock_commit", "n_clock_query"],
    ),
}


N_CLAIMS = common_claims(route_seconds=4, commit_seconds=20) + [
    claim(
        "c_ritual_scope",
        (
            "The query checks only the three entity categories already present "
            "in the working map and cannot expose the omitted field team."
        ),
    )
]

N_NODES = common_nodes(route_seconds=4, commit_seconds=20) + [
    node(
        "n_aperture_ritual",
        "APERTURE",
        claim_refs=["c_ritual_scope"],
        attributes={
            "source_refs": ["n_map_working"],
            "blindspots": ["n_entity_field_team"],
            "search_frame": "CURRENT_MAP_CATEGORIES_ONLY",
            "latency_seconds": 4,
        },
    ),
    information_transition(
        "n_info_ritual",
        ["c_route_4", "c_commit_20", "c_ritual_scope"],
        aperture_ref="n_aperture_ritual",
    ),
]

N_EDGES = common_edges() + [
    edge(
        "e_ritual_observes_map",
        "OBSERVES",
        "n_info_ritual",
        "n_map_working",
        claim_refs=["c_ritual_scope"],
    ),
    edge(
        "e_ritual_cannot_access_team",
        "CANNOT_ACCESS",
        "n_aperture_ritual",
        "n_entity_field_team",
        claim_refs=["c_ritual_scope"],
    ),
]

N_RITUAL_SCAN: dict[str, Any] = {
    "fixture_id": "N_APPLIED_RITUAL_SCAN",
    "scene": {
        **SCENE_COMMON,
        "variant": (
            "A nominal information transition runs, but it searches only "
            "categories already present in the narrowed map."
        ),
    },
    "checker_evidence": {
        "class_assessments": {
            "INFORMATION": {
                "basis_claim_refs": ["c_route_4", "c_commit_20"],
                "evidence_status": "MATERIALLY_LIVE",
            }
        },
        "unavailability_bindings": {},
    },
    "expected": {
        "schema_status": "PASS",
        "combined_status": "PASS",
        "accounting_status": "PASS",
        "integrity_status": "PASS",
        "known_limit": "RITUAL_SCAN_NOT_DETECTED",
    },
    "trace_graph": graph(
        "n_applied_ritual_scan",
        claims=N_CLAIMS,
        nodes=N_NODES,
        edges=N_EDGES,
        information_refs=["n_info_ritual"],
        planning_refs=["n_clock_commit", "n_clock_query"],
    ),
}


APPLIED_FIXTURES: tuple[dict[str, Any], ...] = (
    K_DISCIPLINED_QUERY,
    L_SILENT_OMISSION,
    M_TIME_DOMINATED_BYPASS,
    N_RITUAL_SCAN,
)
