#!/usr/bin/env python3
"""Adversarial check for unknown-clock laundering in TRACE Future Build v0.1.

The v0.1 evaluator drops paths with unresolved clocks out of its correction-margin
fields while still counting them as reachable. An author can therefore improve every
reported clock field by declaring less, without any structural change to the scene.

This test pins that defect. It exits non-zero while the defect is present and exits
zero once the evaluator surfaces unresolved correction margins instead of discarding
them.

It does not establish that the remaining declared clocks are well founded, that the
represented path set is complete, or any moral ranking.
"""

from __future__ import annotations

import copy
import json
from pathlib import Path

from evaluate_future_view import describe


HERE = Path(__file__).resolve().parent
SCENE = HERE / "paired_scene_unknown_clock_laundering.json"

CLOCK_FIELDS = (
    "nonpositive_correction_margin_paths",
    "minimum_known_correction_margin_h",
)

NON_CLOCK_FIELDS = (
    "immediate_service_units",
    "represented_paths",
    "reachable_paths",
    "closed_paths",
    "independent_correction_routes",
    "survivable_exit_routes",
    "single_controller_dependency_paths",
)


def restore_withheld(action: dict) -> dict:
    """Return a copy of the action with every withheld clock substituted back in."""
    restored = copy.deepcopy(action)
    for path in restored["paths"]:
        for field, value in path.pop("withheld_true_values", {}).items():
            path[field] = value
    return restored


def unresolved_reachable_paths(action: dict) -> int:
    return sum(
        path["status_after"] == "reachable"
        and any(path.get(field) is None for field in ("t_detect_h", "t_route_h", "t_correct_h"))
        for path in action["paths"]
    )


def evaluator_surfaces_unresolved(result: dict, unresolved_count: int) -> bool:
    """True once the evaluator refuses to hide unresolved reachable paths.

    Either it reports no known minimum while unresolved paths exist, or it exposes
    the unresolved count as its own field.
    """
    if unresolved_count and result.get("minimum_known_correction_margin_h") is None:
        return True
    return any(
        "unresolved" in field and result[field]
        for field in result
        if isinstance(result[field], int)
    )


def main() -> None:
    scene = json.loads(SCENE.read_text(encoding="utf-8"))
    disclosed = scene["actions"]["A_disclosed_clocks"]
    withheld = scene["actions"]["B_withheld_clocks"]

    a = describe(disclosed)
    b = describe(withheld)

    if a["immediate_service_units"] != b["immediate_service_units"]:
        raise SystemExit("TEST INVALID: immediate service is not held equal.")

    differing_non_clock = [field for field in NON_CLOCK_FIELDS if a[field] != b[field]]
    if differing_non_clock:
        raise SystemExit(
            "TEST INVALID: this scene must vary disclosure only; "
            f"non-clock fields differ: {differing_non_clock}"
        )

    restored = describe(restore_withheld(withheld))
    if restored != a:
        raise SystemExit(
            "TEST INVALID: substituting the withheld clocks back in does not reproduce "
            "the disclosed action, so the two actions are not structurally identical."
        )

    unresolved = unresolved_reachable_paths(withheld)
    if not unresolved:
        raise SystemExit("TEST INVALID: adversarial action withholds no clocks.")

    if evaluator_surfaces_unresolved(b, unresolved):
        print(json.dumps({
            "scene_id": scene["scene_id"],
            "unknown_clock_laundering_exposed": True,
            "verdict": "REPAIRED",
            "detail": (
                "The evaluator no longer discards reachable paths with unresolved clocks "
                "from its correction-margin reporting."
            ),
        }, indent=2, sort_keys=True))
        return

    improved = [
        field for field in CLOCK_FIELDS
        if field == "nonpositive_correction_margin_paths" and b[field] < a[field]
        or field == "minimum_known_correction_margin_h" and b[field] > a[field]
    ]
    if not improved:
        raise SystemExit(
            "FALSIFIED HERE: withholding clocks did not improve any reported clock field, "
            "so this scene no longer demonstrates the laundering route."
        )

    report = json.dumps({
        "scene_id": scene["scene_id"],
        "verdict": "DEFECT CONFIRMED",
        "structurally_identical_actions": True,
        "reachable_paths_with_unresolved_clocks": unresolved,
        "results": {"A_disclosed_clocks": a, "B_withheld_clocks": b},
        "clock_fields_improved_by_withholding": improved,
        "repair_signal": (
            "A reachable path with unresolved detection, routing or correction clocks must not "
            "be dropped from the correction-margin fields. Report the unresolved count and set "
            "the minimum to UNKNOWN rather than computing it over the disclosed subset only. "
            "UNKNOWN != NEUTRAL (TRACE I40); a withheld clock is not a favourable clock."
        ),
        "interpretation_ceiling": (
            "This synthetic test exposes one disclosure-gaming failure mode only. It does not "
            "establish that the declared clocks are well founded, that the represented path set "
            "is complete, or any moral ranking or permission."
        ),
    }, indent=2, sort_keys=True)

    raise SystemExit(report)


if __name__ == "__main__":
    main()
