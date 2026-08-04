#!/usr/bin/env python3
"""Checker-external authority-handoff candidate for divergent apertures.

Candidate ID: TD-AUTHORITY-HANDOFF-001

The checker does not decide which aperture should govern. It tests whether a
selection made after declared aperture divergence has an explicit selector,
authority basis, policy/value basis, route, and—when committed under unresolved
conflict—a commitment receipt. An unresolved conflict may remain unresolved
without checker failure.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, field
from typing import Any, Mapping

CANDIDATE_ID = "TD-AUTHORITY-HANDOFF-001"

FAIL_REFERENCE = "TD-AUTHORITY-REFERENCE-MISMATCH"
FAIL_SILENT_INHERITANCE = "TD-AUTHORITY-SILENT-INHERITANCE"
FAIL_UNBOUND_BRAKE = "TD-AUTHORITY-UNBOUND-BRAKE"
FAIL_MISSING_RECEIPT = "TD-AUTHORITY-MISSING-COMMITMENT-RECEIPT"
FAIL_RECEIPT_MISMATCH = "TD-AUTHORITY-COMMITMENT-RECEIPT-MISMATCH"

CONFLICT_STATUSES = frozenset({"DIVERGENT", "NO_DIVERGENCE", "UNKNOWN"})
COMMITMENT_STATUSES = frozenset({"NOT_COMMITTED", "COMMITTED", "UNKNOWN"})

EPISTEMIC_LIMIT = (
    "This checker tests only declared authority handoff structure after supplied "
    "aperture divergence. A PASS does not establish legitimate authority, correct "
    "policy, good faith, independence, world truth, or that the selected transition "
    "should proceed. An unresolved handoff is preserved rather than solved."
)


class AuthorityHandoffInputError(ValueError):
    """Raised when the checker envelope is structurally unusable."""


@dataclass(slots=True)
class AuthorityHandoffResult:
    fixture_id: str
    status: str
    handoff_status: str
    conflict_status: str
    selected_aperture_result_ref: str | None = None
    selected_transition_ref: str | None = None
    selector_ref: str | None = None
    selector_owner_ref: str | None = None
    brake_ref: str | None = None
    failure_codes: list[str] = field(default_factory=list)
    diagnostics: list[str] = field(default_factory=list)
    epistemic_limit: str = EPISTEMIC_LIMIT

    def to_dict(self) -> dict[str, Any]:
        return {
            "candidate_id": CANDIDATE_ID,
            "fixture_id": self.fixture_id,
            "status": self.status,
            "handoff_status": self.handoff_status,
            "conflict_status": self.conflict_status,
            "selected_aperture_result_ref": self.selected_aperture_result_ref,
            "selected_transition_ref": self.selected_transition_ref,
            "selector_ref": self.selector_ref,
            "selector_owner_ref": self.selector_owner_ref,
            "brake_ref": self.brake_ref,
            "failure_codes": self.failure_codes,
            "diagnostics": self.diagnostics,
            "epistemic_limit": self.epistemic_limit,
        }


def _as_dict(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise AuthorityHandoffInputError(f"{label} must be an object")
    return value


def _as_string_list(value: Any, label: str) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        raise AuthorityHandoffInputError(f"{label} must be an array of strings")
    return list(value)


def _result(
    fixture_id: str,
    *,
    status: str,
    handoff_status: str,
    conflict_status: str,
    selected_result_ref: str | None = None,
    selected_transition_ref: str | None = None,
    selector_ref: str | None = None,
    selector_owner_ref: str | None = None,
    brake_ref: str | None = None,
    failure_codes: list[str] | None = None,
    diagnostics: list[str] | None = None,
) -> AuthorityHandoffResult:
    return AuthorityHandoffResult(
        fixture_id=fixture_id,
        status=status,
        handoff_status=handoff_status,
        conflict_status=conflict_status,
        selected_aperture_result_ref=selected_result_ref,
        selected_transition_ref=selected_transition_ref,
        selector_ref=selector_ref,
        selector_owner_ref=selector_owner_ref,
        brake_ref=brake_ref,
        failure_codes=failure_codes or [],
        diagnostics=diagnostics or [],
    )


def _edges_of_type(
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


def check_authority_handoff(envelope: Mapping[str, Any]) -> AuthorityHandoffResult:
    envelope_dict = _as_dict(dict(envelope), "envelope")
    fixture_id = str(envelope_dict.get("fixture_id", "UNNAMED"))
    graph = _as_dict(envelope_dict.get("trace_graph"), "trace_graph")

    raw_evidence = envelope_dict.get("authority_handoff_evidence")
    if raw_evidence is None:
        return _result(
            fixture_id,
            status="PASS",
            handoff_status="NOT_ASSESSABLE",
            conflict_status="UNKNOWN",
            diagnostics=["no authority-handoff comparison envelope supplied"],
        )
    evidence = _as_dict(raw_evidence, "authority_handoff_evidence")

    conflict_status = evidence.get("conflict_status", "UNKNOWN")
    if not isinstance(conflict_status, str):
        raise AuthorityHandoffInputError("conflict_status must be a string")
    conflict_status = conflict_status.upper()
    if conflict_status not in CONFLICT_STATUSES:
        raise AuthorityHandoffInputError(
            "conflict_status must be one of " + ", ".join(sorted(CONFLICT_STATUSES))
        )

    commitment_status = evidence.get("commitment_status", "UNKNOWN")
    if not isinstance(commitment_status, str):
        raise AuthorityHandoffInputError("commitment_status must be a string")
    commitment_status = commitment_status.upper()
    if commitment_status not in COMMITMENT_STATUSES:
        raise AuthorityHandoffInputError(
            "commitment_status must be one of "
            + ", ".join(sorted(COMMITMENT_STATUSES))
        )

    nodes = graph.get("nodes", [])
    edges = graph.get("edges", [])
    claims = graph.get("claims", [])
    if not isinstance(nodes, list) or any(not isinstance(item, dict) for item in nodes):
        raise AuthorityHandoffInputError("trace_graph.nodes must be an array of objects")
    if not isinstance(edges, list) or any(not isinstance(item, dict) for item in edges):
        raise AuthorityHandoffInputError("trace_graph.edges must be an array of objects")
    if not isinstance(claims, list) or any(not isinstance(item, dict) for item in claims):
        raise AuthorityHandoffInputError("trace_graph.claims must be an array of objects")

    node_by_id = {
        item["id"]: item for item in nodes if isinstance(item.get("id"), str)
    }
    claim_by_id = {
        item["id"]: item for item in claims if isinstance(item.get("id"), str)
    }

    result_refs = _as_string_list(
        evidence.get("aperture_result_refs", []),
        "authority_handoff_evidence.aperture_result_refs",
    )
    missing_results = [ref for ref in result_refs if ref not in node_by_id]
    wrong_result_types = [
        ref
        for ref in result_refs
        if ref in node_by_id and node_by_id[ref].get("type") not in {"RECORD", "CLAIM"}
    ]
    if missing_results or wrong_result_types:
        diagnostics: list[str] = []
        if missing_results:
            diagnostics.append("unresolvable aperture result refs: " + ", ".join(missing_results))
        if wrong_result_types:
            diagnostics.append(
                "aperture result refs must resolve to RECORD or CLAIM nodes: "
                + ", ".join(wrong_result_types)
            )
        return _result(
            fixture_id,
            status="FAIL",
            handoff_status="UNUSABLE_CONFLICT_RECORD",
            conflict_status=conflict_status,
            failure_codes=[FAIL_REFERENCE],
            diagnostics=diagnostics,
        )

    if conflict_status == "NO_DIVERGENCE":
        return _result(
            fixture_id,
            status="PASS",
            handoff_status="NOT_APPLICABLE_NO_DIVERGENCE",
            conflict_status=conflict_status,
        )

    if conflict_status == "UNKNOWN":
        return _result(
            fixture_id,
            status="PASS",
            handoff_status="UNRESOLVED_CONFLICT_STATUS",
            conflict_status=conflict_status,
            diagnostics=["aperture divergence remains UNKNOWN"],
        )

    if len(result_refs) < 2:
        return _result(
            fixture_id,
            status="FAIL",
            handoff_status="UNUSABLE_CONFLICT_RECORD",
            conflict_status=conflict_status,
            failure_codes=[FAIL_REFERENCE],
            diagnostics=["DIVERGENT status requires at least two aperture result refs"],
        )

    selected_result_ref = evidence.get("selected_aperture_result_ref")
    selected_result_ref = selected_result_ref if isinstance(selected_result_ref, str) and selected_result_ref else None
    selected_transition_ref = evidence.get("selected_transition_ref")
    selected_transition_ref = (
        selected_transition_ref
        if isinstance(selected_transition_ref, str) and selected_transition_ref
        else None
    )
    selector_ref = evidence.get("selector_ref")
    selector_ref = selector_ref if isinstance(selector_ref, str) and selector_ref else None
    selector_owner_ref = evidence.get("selector_owner_ref")
    selector_owner_ref = (
        selector_owner_ref
        if isinstance(selector_owner_ref, str) and selector_owner_ref
        else None
    )
    brake_ref = evidence.get("brake_ref")
    brake_ref = brake_ref if isinstance(brake_ref, str) and brake_ref else None

    if selected_result_ref is None and selected_transition_ref is None:
        if commitment_status == "COMMITTED":
            return _result(
                fixture_id,
                status="FAIL",
                handoff_status="COMMITTED_WITHOUT_DECLARED_SELECTION",
                conflict_status=conflict_status,
                failure_codes=[FAIL_SILENT_INHERITANCE],
                diagnostics=[
                    "commitment is declared while no selected aperture result or transition is recorded"
                ],
            )
        return _result(
            fixture_id,
            status="PASS",
            handoff_status="UNRESOLVED_AUTHORITY",
            conflict_status=conflict_status,
            diagnostics=[
                "divergent aperture results are preserved and no authority selection is asserted"
            ],
        )

    if selected_result_ref not in result_refs:
        return _result(
            fixture_id,
            status="FAIL",
            handoff_status="SELECTED_RESULT_OUTSIDE_CONFLICT_SET",
            conflict_status=conflict_status,
            selected_result_ref=selected_result_ref,
            selected_transition_ref=selected_transition_ref,
            failure_codes=[FAIL_REFERENCE],
            diagnostics=["selected aperture result is not one of the declared divergent results"],
        )

    reference_diagnostics: list[str] = []
    if selected_transition_ref not in node_by_id:
        reference_diagnostics.append("selected transition ref does not resolve")
    elif node_by_id[selected_transition_ref].get("type") != "TRANSITION":
        reference_diagnostics.append("selected transition ref does not resolve to TRANSITION")
    if selector_ref not in node_by_id:
        reference_diagnostics.append("selector ref does not resolve")
    elif node_by_id[selector_ref].get("type") != "SELECTOR":
        reference_diagnostics.append("selector ref does not resolve to SELECTOR")
    if selector_owner_ref not in node_by_id:
        reference_diagnostics.append("selector owner ref does not resolve")
    elif node_by_id[selector_owner_ref].get("type") != "ENTITY":
        reference_diagnostics.append("selector owner ref does not resolve to ENTITY")
    if reference_diagnostics:
        return _result(
            fixture_id,
            status="FAIL",
            handoff_status="UNUSABLE_AUTHORITY_HANDOFF",
            conflict_status=conflict_status,
            selected_result_ref=selected_result_ref,
            selected_transition_ref=selected_transition_ref,
            selector_ref=selector_ref,
            selector_owner_ref=selector_owner_ref,
            brake_ref=brake_ref,
            failure_codes=[FAIL_REFERENCE],
            diagnostics=reference_diagnostics,
        )

    authority_claim_refs = _as_string_list(
        evidence.get("selector_authority_claim_refs", []),
        "authority_handoff_evidence.selector_authority_claim_refs",
    )
    value_policy_refs = _as_string_list(
        evidence.get("value_or_policy_refs", []),
        "authority_handoff_evidence.value_or_policy_refs",
    )
    route_refs = _as_string_list(
        evidence.get("authority_route_refs", []),
        "authority_handoff_evidence.authority_route_refs",
    )

    missing_claims = [ref for ref in authority_claim_refs if ref not in claim_by_id]
    missing_policies = [ref for ref in value_policy_refs if ref not in node_by_id]
    wrong_policies = [
        ref
        for ref in value_policy_refs
        if ref in node_by_id and node_by_id[ref].get("type") != "POLICY"
    ]
    missing_routes = [ref for ref in route_refs if ref not in node_by_id]
    wrong_routes = [
        ref
        for ref in route_refs
        if ref in node_by_id and node_by_id[ref].get("type") != "ROUTE"
    ]
    if missing_claims or missing_policies or wrong_policies or missing_routes or wrong_routes:
        diagnostics = []
        if missing_claims:
            diagnostics.append("unresolvable authority claim refs: " + ", ".join(missing_claims))
        if missing_policies:
            diagnostics.append("unresolvable policy refs: " + ", ".join(missing_policies))
        if wrong_policies:
            diagnostics.append("value_or_policy_refs must resolve to POLICY: " + ", ".join(wrong_policies))
        if missing_routes:
            diagnostics.append("unresolvable authority route refs: " + ", ".join(missing_routes))
        if wrong_routes:
            diagnostics.append("authority_route_refs must resolve to ROUTE: " + ", ".join(wrong_routes))
        return _result(
            fixture_id,
            status="FAIL",
            handoff_status="UNUSABLE_AUTHORITY_HANDOFF",
            conflict_status=conflict_status,
            selected_result_ref=selected_result_ref,
            selected_transition_ref=selected_transition_ref,
            selector_ref=selector_ref,
            selector_owner_ref=selector_owner_ref,
            brake_ref=brake_ref,
            failure_codes=[FAIL_REFERENCE],
            diagnostics=diagnostics,
        )

    discipline = _as_dict(graph.get("discipline"), "trace_graph.discipline")
    layer_handoff = _as_dict(
        discipline.get("layer_handoff"), "trace_graph.discipline.layer_handoff"
    )
    handoff_selector_refs = set(
        _as_string_list(layer_handoff.get("selector_refs", []), "layer_handoff.selector_refs")
    )
    handoff_policy_refs = set(
        _as_string_list(layer_handoff.get("value_input_refs", []), "layer_handoff.value_input_refs")
    )
    institutional_use = _as_dict(
        graph.get("institutional_use", {}), "trace_graph.institutional_use"
    )
    selector_owner_refs = set(
        _as_string_list(
            institutional_use.get("selector_owner_refs", []),
            "institutional_use.selector_owner_refs",
        )
    )

    cite_edges = _edges_of_type(
        edges, "CITES_AS_AUTHORITY", from_ref=selector_ref, to_ref=selected_result_ref
    )
    select_edges = _edges_of_type(
        edges, "SELECTS", from_ref=selector_ref, to_ref=selected_transition_ref
    )
    owner_edges = _edges_of_type(
        edges, "CONTROLS", from_ref=selector_owner_ref, to_ref=selector_ref
    )
    route_edges = [
        edge
        for route_ref in route_refs
        for edge in _edges_of_type(edges, "ROUTES_TO", from_ref=route_ref, to_ref=selector_ref)
    ]

    silent_diagnostics: list[str] = []
    if not authority_claim_refs:
        silent_diagnostics.append("no selector authority claim is supplied")
    if not value_policy_refs:
        silent_diagnostics.append("no external value or policy basis is supplied")
    if not route_refs:
        silent_diagnostics.append("no authority route is supplied")
    if selector_ref not in handoff_selector_refs:
        silent_diagnostics.append("selector is absent from layer_handoff.selector_refs")
    if selector_owner_ref not in selector_owner_refs:
        silent_diagnostics.append("selector owner is absent from institutional_use.selector_owner_refs")
    if any(ref not in handoff_policy_refs for ref in value_policy_refs):
        silent_diagnostics.append("policy basis is absent from layer_handoff.value_input_refs")
    if not cite_edges:
        silent_diagnostics.append("selector does not CITES_AS_AUTHORITY the selected aperture result")
    if not select_edges:
        silent_diagnostics.append("selector does not SELECTS the selected transition")
    if not owner_edges:
        silent_diagnostics.append("selector owner does not CONTROLS the selector")
    if route_refs and not route_edges:
        silent_diagnostics.append("declared authority route does not ROUTES_TO the selector")

    authority_edge_claims = {
        ref
        for edge in cite_edges + select_edges + owner_edges + route_edges
        for ref in edge.get("claim_refs", [])
        if isinstance(ref, str)
    }
    if authority_claim_refs and not authority_edge_claims.intersection(authority_claim_refs):
        silent_diagnostics.append("authority claims are not bound to the handoff edges")

    if silent_diagnostics:
        return _result(
            fixture_id,
            status="FAIL",
            handoff_status="SILENT_AUTHORITY_INHERITANCE",
            conflict_status=conflict_status,
            selected_result_ref=selected_result_ref,
            selected_transition_ref=selected_transition_ref,
            selector_ref=selector_ref,
            selector_owner_ref=selector_owner_ref,
            brake_ref=brake_ref,
            failure_codes=[FAIL_SILENT_INHERITANCE],
            diagnostics=silent_diagnostics,
        )

    if brake_ref is not None:
        brake_owner_ref = evidence.get("brake_owner_ref")
        brake_owner_ref = (
            brake_owner_ref if isinstance(brake_owner_ref, str) and brake_owner_ref else None
        )
        brake_authority_claim_refs = _as_string_list(
            evidence.get("brake_authority_claim_refs", []),
            "authority_handoff_evidence.brake_authority_claim_refs",
        )
        brake_owner_refs = set(
            _as_string_list(
                institutional_use.get("brake_owner_refs", []),
                "institutional_use.brake_owner_refs",
            )
        )
        brake_diagnostics: list[str] = []
        if brake_ref not in node_by_id or node_by_id[brake_ref].get("type") != "BRAKE":
            brake_diagnostics.append("brake ref does not resolve to BRAKE")
        if brake_owner_ref not in node_by_id or node_by_id[brake_owner_ref].get("type") != "ENTITY":
            brake_diagnostics.append("brake owner ref does not resolve to ENTITY")
        if brake_owner_ref not in brake_owner_refs:
            brake_diagnostics.append("brake owner is absent from institutional_use.brake_owner_refs")
        missing_brake_claims = [
            ref for ref in brake_authority_claim_refs if ref not in claim_by_id
        ]
        if not brake_authority_claim_refs:
            brake_diagnostics.append("brake has no external authority claim")
        if missing_brake_claims:
            brake_diagnostics.append(
                "unresolvable brake authority claim refs: " + ", ".join(missing_brake_claims)
            )
        brake_edges = _edges_of_type(
            edges, "BRAKES", from_ref=brake_ref, to_ref=selected_transition_ref
        )
        brake_owner_edges = _edges_of_type(
            edges, "CONTROLS", from_ref=brake_owner_ref, to_ref=brake_ref
        )
        if not brake_edges:
            brake_diagnostics.append("brake does not BRAKES the selected transition")
        if not brake_owner_edges:
            brake_diagnostics.append("brake owner does not CONTROLS the brake")
        brake_edge_claims = {
            ref
            for edge in brake_edges + brake_owner_edges
            for ref in edge.get("claim_refs", [])
            if isinstance(ref, str)
        }
        if brake_authority_claim_refs and not brake_edge_claims.intersection(
            brake_authority_claim_refs
        ):
            brake_diagnostics.append("brake authority claims are not bound to brake edges")
        if not value_policy_refs:
            brake_diagnostics.append("brake has no external policy basis")
        if brake_diagnostics:
            return _result(
                fixture_id,
                status="FAIL",
                handoff_status="UNBOUND_BRAKE_AUTHORITY",
                conflict_status=conflict_status,
                selected_result_ref=selected_result_ref,
                selected_transition_ref=selected_transition_ref,
                selector_ref=selector_ref,
                selector_owner_ref=selector_owner_ref,
                brake_ref=brake_ref,
                failure_codes=[FAIL_UNBOUND_BRAKE],
                diagnostics=brake_diagnostics,
            )

    if commitment_status == "COMMITTED":
        receipt_index = evidence.get("commitment_receipt_index")
        receipts = graph.get("commitment_receipts", [])
        if not isinstance(receipts, list):
            raise AuthorityHandoffInputError("trace_graph.commitment_receipts must be an array")
        if not isinstance(receipt_index, int) or receipt_index < 0 or receipt_index >= len(receipts):
            return _result(
                fixture_id,
                status="FAIL",
                handoff_status="MISSING_COMMITMENT_RECEIPT",
                conflict_status=conflict_status,
                selected_result_ref=selected_result_ref,
                selected_transition_ref=selected_transition_ref,
                selector_ref=selector_ref,
                selector_owner_ref=selector_owner_ref,
                brake_ref=brake_ref,
                failure_codes=[FAIL_MISSING_RECEIPT],
                diagnostics=[
                    "commitment under divergent aperture results has no usable commitment receipt"
                ],
            )
        receipt = receipts[receipt_index]
        if not isinstance(receipt, dict):
            raise AuthorityHandoffInputError("commitment receipt must be an object")
        unresolved_claim_refs = _as_string_list(
            evidence.get("unresolved_claim_refs", []),
            "authority_handoff_evidence.unresolved_claim_refs",
        )
        receipt_unresolved = set(
            _as_string_list(
                receipt.get("unresolved_claim_refs", []),
                "commitment_receipt.unresolved_claim_refs",
            )
        )
        mismatch_diagnostics: list[str] = []
        if receipt.get("selected_transition_ref") != selected_transition_ref:
            mismatch_diagnostics.append("receipt selected_transition_ref does not match selection")
        if receipt.get("receipt_is_not_clearance") is not True:
            mismatch_diagnostics.append("receipt_is_not_clearance is not true")
        missing_unresolved = [
            ref for ref in unresolved_claim_refs if ref not in receipt_unresolved
        ]
        if missing_unresolved:
            mismatch_diagnostics.append(
                "receipt omits unresolved conflict claims: " + ", ".join(missing_unresolved)
            )
        if mismatch_diagnostics:
            return _result(
                fixture_id,
                status="FAIL",
                handoff_status="COMMITMENT_RECEIPT_MISMATCH",
                conflict_status=conflict_status,
                selected_result_ref=selected_result_ref,
                selected_transition_ref=selected_transition_ref,
                selector_ref=selector_ref,
                selector_owner_ref=selector_owner_ref,
                brake_ref=brake_ref,
                failure_codes=[FAIL_RECEIPT_MISMATCH],
                diagnostics=mismatch_diagnostics,
            )
        return _result(
            fixture_id,
            status="PASS",
            handoff_status="COMMITMENT_RECORDED_UNDER_UNRESOLVED_CONFLICT",
            conflict_status=conflict_status,
            selected_result_ref=selected_result_ref,
            selected_transition_ref=selected_transition_ref,
            selector_ref=selector_ref,
            selector_owner_ref=selector_owner_ref,
            brake_ref=brake_ref,
            diagnostics=[
                "authority handoff is declared and commitment conditions remain recorded; this is not clearance"
            ],
        )

    return _result(
        fixture_id,
        status="PASS",
        handoff_status="DECLARED_AUTHORITY_HANDOFF",
        conflict_status=conflict_status,
        selected_result_ref=selected_result_ref,
        selected_transition_ref=selected_transition_ref,
        selector_ref=selector_ref,
        selector_owner_ref=selector_owner_ref,
        brake_ref=brake_ref,
        diagnostics=[
            "selector, authority basis, policy basis, route and optional brake are explicitly represented; legitimacy is not established"
        ],
    )


def _main(argv: list[str] | None = None) -> int:
    from authority_handoff_fixtures import AUTHORITY_HANDOFF_FIXTURES

    parser = argparse.ArgumentParser(
        description="Run bounded authority-handoff fixtures for divergent apertures."
    )
    parser.add_argument("--compact", action="store_true", help="emit compact JSON")
    args = parser.parse_args(argv)

    rows: list[dict[str, Any]] = []
    mismatch = False
    for fixture in AUTHORITY_HANDOFF_FIXTURES:
        result = check_authority_handoff(fixture).to_dict()
        expected = fixture["authority_expected"]
        matches = (
            result["status"] == expected["status"]
            and result["handoff_status"] == expected["handoff_status"]
            and result["failure_codes"] == expected.get("failure_codes", [])
        )
        mismatch = mismatch or not matches
        rows.append(
            {
                "fixture_id": fixture["fixture_id"],
                "actual_status": result["status"],
                "actual_handoff_status": result["handoff_status"],
                "actual_failure_codes": result["failure_codes"],
                "expected_status": expected["status"],
                "expected_handoff_status": expected["handoff_status"],
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
