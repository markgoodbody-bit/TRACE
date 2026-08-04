"""Constructed applied witness for TD-TSET-ACCOUNTING-001.

This is not a record of an actual feral-hog control operation. It is a
non-minimal checker envelope used to test transfer and expose ritual compliance.
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any

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


def claim(
    claim_id: str,
    proposition: str,
    *,
    source_refs: list[str] | None = None,
    evidence_state: str = "R",
) -> dict[str, Any]:
    return {
        "id": claim_id,
        "proposition": proposition,
        "source_refs": source_refs or [],
        "evidence_state": evidence_state,
    }


def information_transition(
    transition_id: str,
    basis_claim_refs: list[str],
) -> dict[str, Any]:
    return {
        "id": transition_id,
        "type": "TRANSITION",
        "claim_refs": basis_claim_refs,
        "attributes": {
            "transition_mode": "INFORMATION",
            "availability_status": "AVAILABLE",
            "basis_claim_refs": basis_claim_refs,
            "affected_scope_refs": [],
            "reversibility": "UNKNOWN",
            "strategy_revisable": True,
        },
    }


def graph(
    reading_id: str,
    *,
    claims: list[dict[str, Any]],
    nodes: list[dict[str, Any]],
    information_refs: list[str] | None = None,
    unrepresented: list[str] | None = None,
    reason_refs: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "schema": "TRACE-GRAPH-0.2.5",
        "trace_version": "0.2.5",
        "reading_id": reading_id,
        "claims": claims,
        "nodes": nodes,
        "discipline": {
            "transition_set": {
                "action_or_intervention_refs": [],
                "wait_delay_inaction_refs": [],
                "information_refs": information_refs or [],
                "unrepresented_transition_classes": unrepresented or [],
                "unavailability_reason_claim_refs": reason_refs or [],
                "uncertainty_selects_transition": False,
            }
        },
        "anti_clearance": {"schema_validity_is_not_world_validity": True},
        "available_transition_refs": [
            node["id"]
            for node in nodes
            if node.get("attributes", {}).get("availability_status") == "AVAILABLE"
        ],
        "edges": [],
        "limits": {
            "receiver_limits": [],
            "unavailable_evidence": [],
            "unresolved_claim_refs": [],
        },
        "ports": {
            "selector": {"selection_state": "UNKNOWN"},
            "brake": {"state": "UNKNOWN"},
            "carrier": {"state": "UNKNOWN", "weight_types": []},
            "designation": {},
            "enforcement": {"state": "UNKNOWN"},
            "measure": {},
        },
        "institutional_use": {"observable_transition_change": "UNKNOWN"},
    }


BASE_LIVE_CLAIMS = [
    claim("c_commit_20", "Operational commitment occurs in twenty seconds."),
    claim("c_route_4", "The county dispatch record can be queried in four seconds."),
    claim("c_authority", "The decision unit has authority to query the dispatch record."),
    claim(
        "c_info_live",
        "INFORMATION is materially live before commitment.",
        source_refs=["c_route_4", "c_commit_20", "c_authority"],
    ),
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
        "combined_status": "PASS",
        "accounting_status": "PASS",
        "integrity_status": "PASS",
    },
    "trace_graph": graph(
        "k_applied_disciplined_query",
        claims=deepcopy(BASE_LIVE_CLAIMS),
        nodes=[
            information_transition(
                "n_info_dispatch",
                ["c_info_live", "c_route_4", "c_commit_20", "c_authority"],
            )
        ],
        information_refs=["n_info_dispatch"],
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
        "combined_status": "FAIL",
        "accounting_status": "FAIL",
        "accounting_failure_codes": ["TD-TSET-UNACCOUNTED-CLASS"],
        "integrity_status": "PASS",
    },
    "trace_graph": graph(
        "l_applied_silent_omission",
        claims=deepcopy(BASE_LIVE_CLAIMS),
        nodes=[],
    ),
}


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
        "unavailability_bindings": {
            "INFORMATION": ["c_info_too_slow"],
        },
    },
    "expected": {
        "combined_status": "PASS",
        "accounting_status": "PASS",
        "integrity_status": "PASS",
    },
    "trace_graph": graph(
        "m_applied_time_dominated_bypass",
        claims=[
            claim("c_commit_3", "Immediate protective commitment occurs in three seconds."),
            claim("c_route_10", "The dispatch record requires ten seconds to query."),
            claim(
                "c_info_too_slow",
                "INFORMATION is unavailable before commitment.",
                source_refs=["c_route_10", "c_commit_3"],
            ),
        ],
        nodes=[],
        unrepresented=["INFORMATION"],
        reason_refs=["c_info_too_slow"],
    ),
}


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
        "combined_status": "PASS",
        "accounting_status": "PASS",
        "integrity_status": "PASS",
        "known_limit": "RITUAL_SCAN_NOT_DETECTED",
    },
    "trace_graph": graph(
        "n_applied_ritual_scan",
        claims=[
            claim("c_commit_20", "Operational commitment occurs in twenty seconds."),
            claim("c_route_4", "A four-second information query is available."),
            claim(
                "c_ritual_scope",
                (
                    "The query checks only the three entity categories already "
                    "present in the working map and cannot expose the omitted field team."
                ),
            ),
        ],
        nodes=[
            information_transition(
                "n_info_ritual",
                ["c_route_4", "c_commit_20", "c_ritual_scope"],
            )
        ],
        information_refs=["n_info_ritual"],
    ),
}


APPLIED_FIXTURES: tuple[dict[str, Any], ...] = (
    K_DISCIPLINED_QUERY,
    L_SILENT_OMISSION,
    M_TIME_DOMINATED_BYPASS,
    N_RITUAL_SCAN,
)
