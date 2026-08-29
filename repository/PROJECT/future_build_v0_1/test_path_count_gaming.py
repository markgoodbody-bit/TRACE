#!/usr/bin/env python3
"""Adversarial check for nominal path-count gaming in TRACE Future Build v0.1.

The test does not prove real-world independence. It only checks whether the derived
view can distinguish many labels sharing one dependency root from fewer paths with
different declared dependency roots.
"""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SCENE = HERE / "paired_scene_path_count_gaming.json"


def dependency_key(path: dict) -> tuple[str, str, str]:
    sig = path["dependency_signature"]
    return (
        sig["controller_root"],
        sig["carrier_root"],
        sig["witness_root"],
    )


def describe(action: dict) -> dict:
    reachable = [path for path in action["paths"] if path["status_after"] == "reachable"]
    return {
        "nominal_reachable_paths": len(reachable),
        "dependency_distinct_path_classes": len({dependency_key(path) for path in reachable}),
        "correction_root_classes": len({path["correction_root"] for path in reachable}),
    }


def main() -> None:
    scene = json.loads(SCENE.read_text(encoding="utf-8"))
    actions = scene["actions"]
    a = describe(actions["A_three_dependency_distinct_paths"])
    b = describe(actions["B_six_nominal_paths_one_dependency_root"])

    if b["nominal_reachable_paths"] <= a["nominal_reachable_paths"]:
        raise SystemExit("TEST INVALID: adversarial action does not have more nominal paths.")

    if b["dependency_distinct_path_classes"] >= a["dependency_distinct_path_classes"]:
        raise SystemExit("FALSIFIED HERE: dependency collapse did not expose the nominal-path gaming case.")

    if b["correction_root_classes"] >= a["correction_root_classes"]:
        raise SystemExit("FALSIFIED HERE: correction-root collapse did not expose shared actuation dependency.")

    print(json.dumps({
        "scene_id": scene["scene_id"],
        "immediate_service_matched": True,
        "results": {
            "A_three_dependency_distinct_paths": a,
            "B_six_nominal_paths_one_dependency_root": b,
        },
        "path_count_gaming_exposed": True,
        "repair_signal": (
            "Report nominal path count separately from dependency-collapsed path classes. "
            "Do not infer independence from distinct labels, interfaces, providers or route names; "
            "independence remains an evidence-bearing claim about shared controller/carrier/witness/actuation roots."
        ),
        "interpretation_ceiling": (
            "This synthetic test exposes one representation-gaming failure mode only. "
            "It does not prove the dependency signatures are complete, establish moral ranking, or confer permission."
        ),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
