"""Bounded fixtures for TD-TSET-SEARCH-COVERAGE-001."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from applied_scene_001 import (
    K_DISCIPLINED_QUERY,
    M_TIME_DOMINATED_BYPASS,
    N_RITUAL_SCAN,
)


def fixture(base: dict[str, Any], fixture_id: str) -> dict[str, Any]:
    value = deepcopy(base)
    value["fixture_id"] = fixture_id
    value.pop("expected", None)
    value.pop("coverage_evidence", None)
    value.pop("coverage_expected", None)
    return value


O_DECLARED_REACHABILITY = fixture(
    K_DISCIPLINED_QUERY, "O_DECLARED_REACHABILITY_CHAIN"
)
O_DECLARED_REACHABILITY["coverage_evidence"] = {
    "assessment_status": "ASSESS",
    "information_transition_ref": "n_info_dispatch",
    "required_target_refs": ["n_entity_field_team"],
    "comparison_basis_claim_refs": ["c_omission", "c_record", "c_info_live"],
    "target_path_edge_refs": {
        "n_entity_field_team": [
            "e_info_observes_record",
            "e_record_reports_team",
        ]
    },
}
O_DECLARED_REACHABILITY["coverage_expected"] = {
    "status": "PASS",
    "coverage_status": "DECLARED_REACHABILITY_CHAIN",
    "failure_codes": [],
}


P_RITUAL_TARGET_BLINDSPOT = fixture(
    N_RITUAL_SCAN, "P_RITUAL_TARGET_BLINDSPOT"
)
P_RITUAL_TARGET_BLINDSPOT["coverage_evidence"] = {
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
P_RITUAL_TARGET_BLINDSPOT["coverage_expected"] = {
    "status": "FAIL",
    "coverage_status": "CONTRADICTED",
    "failure_codes": ["TD-TSET-SEARCH-COVERAGE-CONTRADICTION"],
}


Q_NO_COMPARISON_BASIS = fixture(K_DISCIPLINED_QUERY, "Q_NO_COVERAGE_COMPARISON")
Q_NO_COMPARISON_BASIS["coverage_expected"] = {
    "status": "PASS",
    "coverage_status": "NOT_ASSESSABLE",
    "failure_codes": [],
}


R_INFORMATION_UNAVAILABLE = fixture(
    M_TIME_DOMINATED_BYPASS, "R_INFORMATION_UNAVAILABLE"
)
R_INFORMATION_UNAVAILABLE["coverage_evidence"] = {
    "assessment_status": "UNAVAILABLE",
    "comparison_basis_claim_refs": ["c_route_10", "c_commit_3"],
    "unavailability_reason_claim_refs": ["c_info_too_slow"],
}
R_INFORMATION_UNAVAILABLE["coverage_expected"] = {
    "status": "PASS",
    "coverage_status": "NOT_APPLICABLE_INFORMATION_UNAVAILABLE",
    "failure_codes": [],
}


SEARCH_COVERAGE_FIXTURES: tuple[dict[str, Any], ...] = (
    O_DECLARED_REACHABILITY,
    P_RITUAL_TARGET_BLINDSPOT,
    Q_NO_COMPARISON_BASIS,
    R_INFORMATION_UNAVAILABLE,
)
