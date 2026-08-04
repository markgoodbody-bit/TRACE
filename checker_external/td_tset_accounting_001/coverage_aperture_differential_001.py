#!/usr/bin/env python3
"""Constructed target-set aperture differential for search coverage.

The same schema-valid TRACE packet is checked against two different external
coverage comparison envelopes. The differential preserves disagreement rather
than treating either target set as world truth.
"""

from __future__ import annotations

import hashlib
import json
from copy import deepcopy
from typing import Any, Mapping

from applied_scene_001 import N_RITUAL_SCAN
from run_search_coverage import run_search_coverage_suite

WITNESS_ID = "TD-TSET-COVERAGE-APERTURE-DIFFERENTIAL-001"

EPISTEMIC_LIMIT = (
    "This witness shows that search-coverage results depend on the supplied "
    "target-set aperture. It does not establish which aperture is authoritative, "
    "whether either target set is complete, or whether the represented claims are true."
)


def _canonical_graph_sha256(graph: Mapping[str, Any]) -> str:
    payload = json.dumps(graph, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _base_envelope(fixture_id: str) -> dict[str, Any]:
    envelope = deepcopy(N_RITUAL_SCAN)
    envelope["fixture_id"] = fixture_id
    envelope.pop("expected", None)
    envelope.pop("coverage_evidence", None)
    envelope.pop("coverage_expected", None)
    return envelope


OPERATOR_APERTURE = _base_envelope("Z1_OPERATOR_TARGET_SET")
OPERATOR_APERTURE["comparison_aperture"] = {
    "aperture_id": "operator_working_map",
    "source_kind": "OPERATOR_DECLARATION",
    "independence_status": "NOT_INDEPENDENT",
    "target_set_claim": "The target set requiring coverage contains the hog population.",
}
OPERATOR_APERTURE["coverage_evidence"] = {
    "assessment_status": "ASSESS",
    "information_transition_ref": "n_info_ritual",
    "required_target_refs": ["n_entity_hogs"],
    "comparison_basis_claim_refs": ["c_map", "c_ritual_scope"],
    "target_path_edge_refs": {
        "n_entity_hogs": [
            "e_ritual_observes_map",
            "e_map_contains_hogs",
        ]
    },
}


INDEPENDENT_APERTURE = _base_envelope("Z2_DISPATCH_TARGET_SET")
INDEPENDENT_APERTURE["comparison_aperture"] = {
    "aperture_id": "dispatch_record_comparison",
    "source_kind": "EXTERNAL_RECORD_DECLARATION",
    "independence_status": "DECLARED_INDEPENDENT",
    "target_set_claim": (
        "The target set requiring coverage includes the field team inside the flight zone."
    ),
}
INDEPENDENT_APERTURE["coverage_evidence"] = {
    "assessment_status": "ASSESS",
    "information_transition_ref": "n_info_ritual",
    "required_target_refs": ["n_entity_field_team"],
    "comparison_basis_claim_refs": ["c_omission", "c_ritual_scope"],
    "target_path_edge_refs": {
        "n_entity_field_team": [
            "e_ritual_observes_map",
            "e_map_omits_team",
        ]
    },
}


def run_differential() -> dict[str, Any]:
    operator_graph_hash = _canonical_graph_sha256(OPERATOR_APERTURE["trace_graph"])
    independent_graph_hash = _canonical_graph_sha256(INDEPENDENT_APERTURE["trace_graph"])

    operator_result = run_search_coverage_suite(OPERATOR_APERTURE)
    independent_result = run_search_coverage_suite(INDEPENDENT_APERTURE)

    same_packet = operator_graph_hash == independent_graph_hash
    results_differ = (
        operator_result["combined_status"] != independent_result["combined_status"]
        or operator_result["coverage_result"].get("coverage_status")
        != independent_result["coverage_result"].get("coverage_status")
    )

    return {
        "witness_id": WITNESS_ID,
        "same_trace_packet": same_packet,
        "trace_graph_sha256": operator_graph_hash if same_packet else None,
        "differential_status": "DIVERGENT" if results_differ else "NO_DIVERGENCE",
        "operator_aperture": {
            "metadata": OPERATOR_APERTURE["comparison_aperture"],
            "result": operator_result,
        },
        "independent_aperture": {
            "metadata": INDEPENDENT_APERTURE["comparison_aperture"],
            "result": independent_result,
        },
        "authoritative_aperture": "UNRESOLVED",
        "epistemic_limit": EPISTEMIC_LIMIT,
    }


def _main() -> int:
    output = run_differential()
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if output["same_trace_packet"] and output["differential_status"] == "DIVERGENT" else 1


if __name__ == "__main__":
    raise SystemExit(_main())
