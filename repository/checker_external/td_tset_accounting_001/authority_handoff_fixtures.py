"""Schema-valid constructed fixtures for TD-AUTHORITY-HANDOFF-001."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from applied_scene_001 import N_RITUAL_SCAN, claim, edge, node


def transition(
    transition_id: str,
    mode: str,
    claim_refs: list[str],
) -> dict[str, Any]:
    return node(
        transition_id,
        "TRANSITION",
        claim_refs=claim_refs,
        attributes={
            "transition_mode": mode,
            "availability_status": "AVAILABLE",
            "basis_claim_refs": claim_refs,
            "affected_scope_refs": [
                "n_entity_crew",
                "n_entity_hogs",
                "n_entity_field_team",
            ],
            "reversibility": "UNKNOWN",
            "strategy_revisable": mode == "WAIT",
        },
    )


def base_conflict_graph(reading_id: str) -> dict[str, Any]:
    graph = deepcopy(N_RITUAL_SCAN["trace_graph"])
    graph["reading_id"] = reading_id
    graph["claims"].extend(
        [
            claim(
                "c_operator_result",
                "The operator target-set aperture returns PASS for the hog target.",
            ),
            claim(
                "c_dispatch_result",
                "The dispatch-record target-set aperture returns FAIL for the field-team target.",
            ),
            claim(
                "c_aperture_conflict",
                "The two supplied aperture results diverge and authority between them is unresolved.",
                evidence_state="D",
            ),
        ]
    )
    graph["nodes"].extend(
        [
            node(
                "n_record_operator_result",
                "RECORD",
                claim_refs=["c_operator_result", "c_aperture_conflict"],
                attributes={
                    "aperture_id": "operator_working_map",
                    "coverage_status": "DECLARED_REACHABILITY_CHAIN",
                },
            ),
            node(
                "n_record_dispatch_result",
                "RECORD",
                claim_refs=["c_dispatch_result", "c_aperture_conflict"],
                attributes={
                    "aperture_id": "dispatch_record_comparison",
                    "coverage_status": "CONTRADICTED",
                },
            ),
        ]
    )
    graph["edges"].append(
        edge(
            "e_dispatch_disputes_operator",
            "DISPUTES",
            "n_record_dispatch_result",
            "n_record_operator_result",
            claim_refs=["c_aperture_conflict"],
        )
    )
    graph["limits"]["unresolved_claim_refs"] = ["c_aperture_conflict"]
    graph["discipline"]["layer_handoff"]["unresolved_handoffs"] = [
        "authority among divergent apertures"
    ]
    graph["institutional_use"].update(
        {
            "packet_owner_refs": [],
            "selector_owner_refs": [],
            "brake_owner_refs": [],
            "independent_verifier_refs": [],
            "packet_cited_as_diligence": "UNKNOWN",
            "packet_cited_as_authority": "UNKNOWN",
            "mechanism_change_for_next_case": "UNKNOWN",
            "use_evidence_claim_refs": [],
        }
    )
    graph["commitment_receipts"] = []
    return graph


def add_minimal_selection(
    graph: dict[str, Any],
    *,
    selected_result_ref: str,
    transition_ref: str,
    mode: str,
) -> None:
    graph["claims"].append(
        claim(
            "c_selection",
            "The incident selector selects a transition while relying on one aperture result.",
        )
    )
    graph["nodes"].extend(
        [
            node("n_entity_incident_commander", "ENTITY"),
            node(
                "n_selector_incident",
                "SELECTOR",
                claim_refs=["c_selection"],
                attributes={"selection_state": "SELECTED"},
            ),
            transition(transition_ref, mode, ["c_selection"]),
        ]
    )
    graph["edges"].extend(
        [
            edge(
                "e_commander_controls_selector",
                "CONTROLS",
                "n_entity_incident_commander",
                "n_selector_incident",
                claim_refs=["c_selection"],
            ),
            edge(
                "e_selector_cites_result",
                "CITES_AS_AUTHORITY",
                "n_selector_incident",
                selected_result_ref,
                claim_refs=["c_selection"],
            ),
            edge(
                "e_selector_selects_transition",
                "SELECTS",
                "n_selector_incident",
                transition_ref,
                claim_refs=["c_selection"],
            ),
        ]
    )
    graph["discipline"]["layer_handoff"]["selector_refs"] = [
        "n_selector_incident"
    ]
    graph["institutional_use"]["selector_owner_refs"] = [
        "n_entity_incident_commander"
    ]
    graph["institutional_use"]["packet_cited_as_authority"] = "YES"
    graph["institutional_use"]["use_evidence_claim_refs"] = ["c_selection"]
    graph["ports"]["selector"] = {
        "selection_state": "SELECTED",
        "selector_ref": "n_selector_incident",
    }
    if mode == "WAIT":
        graph["discipline"]["transition_set"]["wait_delay_inaction_refs"].append(
            transition_ref
        )
    else:
        graph["discipline"]["transition_set"]["action_or_intervention_refs"].append(
            transition_ref
        )
    graph["available_transition_refs"].append(transition_ref)


def add_declared_handoff(
    graph: dict[str, Any],
    *,
    selected_result_ref: str,
    transition_ref: str,
    mode: str,
) -> None:
    graph["claims"].extend(
        [
            claim(
                "c_selector_authority",
                "County emergency policy delegates operational hold-or-launch selection to the incident commander.",
                claim_kind="NORMATIVE_EXTERNAL",
            ),
            claim(
                "c_policy_conflict",
                "County emergency policy requires explicit incident-command review when safety-relevant apertures diverge.",
                claim_kind="NORMATIVE_EXTERNAL",
            ),
            claim(
                "c_authority_route",
                "The divergent aperture records are routed to the incident selector before commitment.",
            ),
            claim(
                "c_selection",
                "The incident selector selects the represented transition under the declared policy and authority claim.",
                source_refs=["c_selector_authority", "c_policy_conflict"],
            ),
        ]
    )
    graph["nodes"].extend(
        [
            node(
                "n_entity_incident_commander",
                "ENTITY",
                claim_refs=["c_selector_authority"],
            ),
            node(
                "n_selector_incident",
                "SELECTOR",
                claim_refs=["c_selector_authority", "c_selection"],
                attributes={"selection_state": "SELECTED"},
            ),
            node(
                "n_policy_conflict",
                "POLICY",
                claim_refs=["c_policy_conflict"],
                attributes={"policy_source": "county emergency policy"},
            ),
            node(
                "n_route_results_to_selector",
                "ROUTE",
                claim_refs=["c_authority_route", "c_selector_authority"],
                attributes={
                    "origin_refs": [
                        "n_record_operator_result",
                        "n_record_dispatch_result",
                    ],
                    "destination_ref": "n_selector_incident",
                    "authority_claim_ref": "c_selector_authority",
                    "independence_status": "UNKNOWN",
                },
            ),
            transition(
                transition_ref,
                mode,
                ["c_selection", "c_selector_authority", "c_policy_conflict"],
            ),
        ]
    )
    graph["edges"].extend(
        [
            edge(
                "e_commander_controls_selector",
                "CONTROLS",
                "n_entity_incident_commander",
                "n_selector_incident",
                claim_refs=["c_selector_authority"],
            ),
            edge(
                "e_results_route_to_selector",
                "ROUTES_TO",
                "n_route_results_to_selector",
                "n_selector_incident",
                claim_refs=["c_authority_route", "c_selector_authority"],
            ),
            edge(
                "e_selector_cites_result",
                "CITES_AS_AUTHORITY",
                "n_selector_incident",
                selected_result_ref,
                claim_refs=["c_selector_authority", "c_policy_conflict"],
            ),
            edge(
                "e_selector_selects_transition",
                "SELECTS",
                "n_selector_incident",
                transition_ref,
                claim_refs=["c_selection", "c_selector_authority", "c_policy_conflict"],
            ),
        ]
    )
    graph["discipline"]["layer_handoff"].update(
        {
            "value_input_refs": ["n_policy_conflict"],
            "domain_input_refs": [
                "n_record_operator_result",
                "n_record_dispatch_result",
            ],
            "selector_refs": ["n_selector_incident"],
            "unresolved_handoffs": [
                "legitimacy and completeness of the selected authority basis"
            ],
        }
    )
    graph["institutional_use"].update(
        {
            "selector_owner_refs": ["n_entity_incident_commander"],
            "packet_cited_as_authority": "YES",
            "use_evidence_claim_refs": [
                "c_selector_authority",
                "c_policy_conflict",
                "c_selection",
            ],
        }
    )
    graph["ports"]["selector"] = {
        "selection_state": "SELECTED",
        "selector_ref": "n_selector_incident",
        "authority_claim_refs": ["c_selector_authority"],
        "policy_refs": ["n_policy_conflict"],
    }
    if mode == "WAIT":
        graph["discipline"]["transition_set"]["wait_delay_inaction_refs"].append(
            transition_ref
        )
    else:
        graph["discipline"]["transition_set"]["action_or_intervention_refs"].append(
            transition_ref
        )
    graph["available_transition_refs"].append(transition_ref)


def add_bound_brake(graph: dict[str, Any], transition_ref: str) -> None:
    graph["claims"].append(
        claim(
            "c_brake_authority",
            "County safety policy authorises the safety officer to interrupt the selected transition.",
            claim_kind="NORMATIVE_EXTERNAL",
            source_refs=["c_policy_conflict"],
        )
    )
    graph["nodes"].extend(
        [
            node(
                "n_entity_safety_officer",
                "ENTITY",
                claim_refs=["c_brake_authority"],
            ),
            node(
                "n_brake_safety",
                "BRAKE",
                claim_refs=["c_brake_authority", "c_policy_conflict"],
                attributes={"connection_status": "DECLARED_CONNECTED"},
            ),
        ]
    )
    graph["edges"].extend(
        [
            edge(
                "e_safety_officer_controls_brake",
                "CONTROLS",
                "n_entity_safety_officer",
                "n_brake_safety",
                claim_refs=["c_brake_authority"],
            ),
            edge(
                "e_brake_brakes_transition",
                "BRAKES",
                "n_brake_safety",
                transition_ref,
                claim_refs=["c_brake_authority", "c_policy_conflict"],
            ),
        ]
    )
    graph["institutional_use"]["brake_owner_refs"] = [
        "n_entity_safety_officer"
    ]
    graph["ports"]["brake"] = {
        "state": "PRESENT_UNTESTED",
        "brake_ref": "n_brake_safety",
        "authority_claim_refs": ["c_brake_authority"],
        "policy_refs": ["n_policy_conflict"],
    }


def common_evidence(
    *,
    selected_result_ref: str | None = None,
    transition_ref: str | None = None,
    commitment_status: str = "NOT_COMMITTED",
) -> dict[str, Any]:
    return {
        "conflict_status": "DIVERGENT",
        "aperture_result_refs": [
            "n_record_operator_result",
            "n_record_dispatch_result",
        ],
        "selected_aperture_result_ref": selected_result_ref,
        "selected_transition_ref": transition_ref,
        "commitment_status": commitment_status,
        "selector_ref": "n_selector_incident" if transition_ref else None,
        "selector_owner_ref": "n_entity_incident_commander" if transition_ref else None,
        "selector_authority_claim_refs": [],
        "value_or_policy_refs": [],
        "authority_route_refs": [],
        "brake_ref": None,
        "brake_owner_ref": None,
        "brake_authority_claim_refs": [],
        "unresolved_claim_refs": ["c_aperture_conflict"],
    }


AA_UNRESOLVED_AUTHORITY: dict[str, Any] = {
    "fixture_id": "AA_UNRESOLVED_AUTHORITY",
    "trace_graph": base_conflict_graph("aa_unresolved_authority"),
    "authority_handoff_evidence": common_evidence(),
    "authority_expected": {
        "status": "PASS",
        "handoff_status": "UNRESOLVED_AUTHORITY",
        "failure_codes": [],
    },
}


AB_SILENT_OPERATOR_INHERITANCE_GRAPH = base_conflict_graph(
    "ab_silent_operator_inheritance"
)
add_minimal_selection(
    AB_SILENT_OPERATOR_INHERITANCE_GRAPH,
    selected_result_ref="n_record_operator_result",
    transition_ref="n_transition_launch",
    mode="ACT",
)
AB_SILENT_OPERATOR_INHERITANCE: dict[str, Any] = {
    "fixture_id": "AB_SILENT_OPERATOR_INHERITANCE",
    "trace_graph": AB_SILENT_OPERATOR_INHERITANCE_GRAPH,
    "authority_handoff_evidence": common_evidence(
        selected_result_ref="n_record_operator_result",
        transition_ref="n_transition_launch",
    ),
    "authority_expected": {
        "status": "FAIL",
        "handoff_status": "SILENT_AUTHORITY_INHERITANCE",
        "failure_codes": ["TD-AUTHORITY-SILENT-INHERITANCE"],
    },
}


AC_DECLARED_HOLD_HANDOFF_GRAPH = base_conflict_graph("ac_declared_hold_handoff")
add_declared_handoff(
    AC_DECLARED_HOLD_HANDOFF_GRAPH,
    selected_result_ref="n_record_dispatch_result",
    transition_ref="n_transition_hold",
    mode="WAIT",
)
add_bound_brake(AC_DECLARED_HOLD_HANDOFF_GRAPH, "n_transition_hold")
AC_EVIDENCE = common_evidence(
    selected_result_ref="n_record_dispatch_result",
    transition_ref="n_transition_hold",
)
AC_EVIDENCE.update(
    {
        "selector_authority_claim_refs": ["c_selector_authority"],
        "value_or_policy_refs": ["n_policy_conflict"],
        "authority_route_refs": ["n_route_results_to_selector"],
        "brake_ref": "n_brake_safety",
        "brake_owner_ref": "n_entity_safety_officer",
        "brake_authority_claim_refs": ["c_brake_authority"],
    }
)
AC_DECLARED_HOLD_HANDOFF: dict[str, Any] = {
    "fixture_id": "AC_DECLARED_HOLD_HANDOFF",
    "trace_graph": AC_DECLARED_HOLD_HANDOFF_GRAPH,
    "authority_handoff_evidence": AC_EVIDENCE,
    "authority_expected": {
        "status": "PASS",
        "handoff_status": "DECLARED_AUTHORITY_HANDOFF",
        "failure_codes": [],
    },
}


AD_COMMITTED_WITHOUT_RECEIPT_GRAPH = base_conflict_graph(
    "ad_committed_without_receipt"
)
add_declared_handoff(
    AD_COMMITTED_WITHOUT_RECEIPT_GRAPH,
    selected_result_ref="n_record_operator_result",
    transition_ref="n_transition_launch",
    mode="ACT",
)
AD_EVIDENCE = common_evidence(
    selected_result_ref="n_record_operator_result",
    transition_ref="n_transition_launch",
    commitment_status="COMMITTED",
)
AD_EVIDENCE.update(
    {
        "selector_authority_claim_refs": ["c_selector_authority"],
        "value_or_policy_refs": ["n_policy_conflict"],
        "authority_route_refs": ["n_route_results_to_selector"],
    }
)
AD_COMMITTED_WITHOUT_RECEIPT: dict[str, Any] = {
    "fixture_id": "AD_COMMITTED_WITHOUT_RECEIPT",
    "trace_graph": AD_COMMITTED_WITHOUT_RECEIPT_GRAPH,
    "authority_handoff_evidence": AD_EVIDENCE,
    "authority_expected": {
        "status": "FAIL",
        "handoff_status": "MISSING_COMMITMENT_RECEIPT",
        "failure_codes": ["TD-AUTHORITY-MISSING-COMMITMENT-RECEIPT"],
    },
}


AE_COMMITTED_WITH_RECEIPT_GRAPH = deepcopy(AD_COMMITTED_WITHOUT_RECEIPT_GRAPH)
AE_COMMITTED_WITH_RECEIPT_GRAPH["reading_id"] = "ae_committed_with_receipt"
AE_COMMITTED_WITH_RECEIPT_GRAPH["commitment_receipts"] = [
    {
        "selected_transition_ref": "n_transition_launch",
        "unresolved_claim_refs": ["c_aperture_conflict"],
        "disputed_claim_refs": ["c_aperture_conflict"],
        "live_alternative_refs": ["n_transition_hold", "n_info_ritual"],
        "declared_value_policy_refs": ["n_policy_conflict"],
        "reason_for_commitment_claim_refs": ["c_selection"],
        "review_debt_refs": ["c_aperture_conflict"],
        "receipt_is_not_clearance": True,
    }
]
AE_EVIDENCE = deepcopy(AD_EVIDENCE)
AE_EVIDENCE["commitment_receipt_index"] = 0
AE_COMMITTED_WITH_RECEIPT: dict[str, Any] = {
    "fixture_id": "AE_COMMITTED_WITH_RECEIPT",
    "trace_graph": AE_COMMITTED_WITH_RECEIPT_GRAPH,
    "authority_handoff_evidence": AE_EVIDENCE,
    "authority_expected": {
        "status": "PASS",
        "handoff_status": "COMMITMENT_RECORDED_UNDER_UNRESOLVED_CONFLICT",
        "failure_codes": [],
    },
}


AF_UNBOUND_BRAKE_GRAPH = deepcopy(AC_DECLARED_HOLD_HANDOFF_GRAPH)
AF_UNBOUND_BRAKE_GRAPH["reading_id"] = "af_unbound_brake"
AF_UNBOUND_BRAKE_GRAPH["claims"] = [
    item for item in AF_UNBOUND_BRAKE_GRAPH["claims"] if item["id"] != "c_brake_authority"
]
for item in AF_UNBOUND_BRAKE_GRAPH["nodes"]:
    if item["id"] in {"n_entity_safety_officer", "n_brake_safety"}:
        item["claim_refs"] = [
            ref for ref in item["claim_refs"] if ref != "c_brake_authority"
        ]
for item in AF_UNBOUND_BRAKE_GRAPH["edges"]:
    if item["id"] in {
        "e_safety_officer_controls_brake",
        "e_brake_brakes_transition",
    }:
        item["claim_refs"] = [
            ref for ref in item["claim_refs"] if ref != "c_brake_authority"
        ]
AF_EVIDENCE = deepcopy(AC_EVIDENCE)
AF_EVIDENCE["brake_authority_claim_refs"] = []
AF_UNBOUND_BRAKE: dict[str, Any] = {
    "fixture_id": "AF_UNBOUND_BRAKE",
    "trace_graph": AF_UNBOUND_BRAKE_GRAPH,
    "authority_handoff_evidence": AF_EVIDENCE,
    "authority_expected": {
        "status": "FAIL",
        "handoff_status": "UNBOUND_BRAKE_AUTHORITY",
        "failure_codes": ["TD-AUTHORITY-UNBOUND-BRAKE"],
    },
}


AUTHORITY_HANDOFF_FIXTURES: tuple[dict[str, Any], ...] = (
    AA_UNRESOLVED_AUTHORITY,
    AB_SILENT_OPERATOR_INHERITANCE,
    AC_DECLARED_HOLD_HANDOFF,
    AD_COMMITTED_WITHOUT_RECEIPT,
    AE_COMMITTED_WITH_RECEIPT,
    AF_UNBOUND_BRAKE,
)
