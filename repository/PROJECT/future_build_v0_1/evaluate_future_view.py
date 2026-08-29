#!/usr/bin/env python3
"""Minimal evaluator for TRACE Future Build v0.1 synthetic paired scene.

Descriptive only. It does not establish moral ranking, permission, authority,
completeness of the represented future envelope, or empirical validity.
"""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SCENE = HERE / "paired_scene_essential_infrastructure.json"


def correction_margin(path: dict) -> float | None:
    values = [path.get("t_detect_h"), path.get("t_route_h"), path.get("t_correct_h")]
    if any(value is None for value in values):
        return None
    return float(path["t_irreversible_h"]) - sum(float(value) for value in values)


def describe(action: dict) -> dict:
    paths = action["paths"]
    margins = [correction_margin(path) for path in paths if path["status_after"] == "reachable"]
    known_margins = [margin for margin in margins if margin is not None]

    return {
        "immediate_service_units": action["immediate_service_units"],
        "represented_paths": len(paths),
        "reachable_paths": sum(path["status_after"] == "reachable" for path in paths),
        "closed_paths": sum(path["status_after"] == "closed" for path in paths),
        "nonpositive_correction_margin_paths": sum(
            margin is not None and margin <= 0 for margin in margins
        ),
        "minimum_known_correction_margin_h": min(known_margins) if known_margins else None,
        "independent_correction_routes": sum(path["independent_correction_routes"] for path in paths),
        "survivable_exit_routes": sum(path["survivable_exit_routes"] for path in paths),
        "single_controller_dependency_paths": sum(path["single_controller_dependency"] for path in paths),
    }


def main() -> None:
    scene = json.loads(SCENE.read_text(encoding="utf-8"))
    results = {name: describe(action) for name, action in scene["actions"].items()}

    names = list(results)
    if len(names) != 2:
        raise SystemExit("This minimal test expects exactly two candidate actions.")

    left, right = (results[name] for name in names)
    if left["immediate_service_units"] != right["immediate_service_units"]:
        raise SystemExit("TEST INVALID: immediate service is not held equal.")

    structural_fields = [
        "reachable_paths",
        "closed_paths",
        "nonpositive_correction_margin_paths",
        "minimum_known_correction_margin_h",
        "independent_correction_routes",
        "survivable_exit_routes",
        "single_controller_dependency_paths",
    ]
    differing = [field for field in structural_fields if left[field] != right[field]]
    if not differing:
        raise SystemExit("FALSIFIED HERE: derived view exposed no structural difference.")

    print(json.dumps({
        "scene_id": scene["scene_id"],
        "immediate_outcome_matched": True,
        "results": results,
        "structural_fields_that_differ": differing,
        "interpretation_ceiling": (
            "The represented future structures differ despite matched immediate service. "
            "This is a synthetic structural distinction only; it is not a moral ranking, "
            "permission, empirical validation, or proof that the represented path set is complete."
        ),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
