#!/usr/bin/env python3
"""Build TRACE v0.3.0 spine candidate v0.10 from v0.9.

The only admitted changes are donor restorations for I23, I39, I53 and I54,
plus survival-kernel propagation. No schema or ontology change is made.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
BASE_PATH = REPO_ROOT / "PROJECT" / "TRACE_v0_3_0_SPINE_CANDIDATE_v0_9.md"
OUTPUT_PATH = REPO_ROOT / "PROJECT" / "TRACE_v0_3_0_SPINE_CANDIDATE_v0_10.md"
REPORT_PATH = REPO_ROOT / "PROJECT" / "TRACE_v0_3_0_SPINE_V010_BUILD_REPORT_v0_1.json"

REPLACEMENTS = (
    (
        "# TRACE // v0.3.0 SPINE CANDIDATE v0.9",
        "# TRACE // v0.3.0 SPINE CANDIDATE v0.10",
        "version header",
    ),
    (
        "BOUNDARY_CHOICE != NATURAL_KIND_PROOF\n```",
        "BOUNDARY_CHOICE != NATURAL_KIND_PROOF\nPOPULATION_RECOVERY != REPAIR_OF_INDIVIDUAL_LOSS\nGROUP_METRIC_RESTORED != EVERY_AFFECTED_SCOPE_REPAIRED\n```\n\nAggregate/group recovery does not establish repair of a particular lower-level scope; individual repair needs evidence at that scope or a justified correspondence rule that actually entails it.",
        "population/individual scope repair",
    ),
    (
        "BURDEN_PRESENT != ROUTE_UNUSABLE\nREFUSAL_RECORDED != REFUSAL_EFFECTIVE\n```\n\nRoute usability is scope/target-relative; access, target reach, authority, timing and burden/constraints fire only when they can change that claim.",
        "BURDEN_PRESENT != ROUTE_UNUSABLE\nREFUSAL_RECORDED != REFUSAL_EFFECTIVE\nREFUSAL != MALFUNCTION\nSTRATEGY_REVISABLE != TRANSITION_REVERSIBLE\nFUTURE_POLICY_CAN_CHANGE != PRIOR_STATE_CAN_BE_RESTORED\n```\n\nRoute usability is scope/target-relative; access, target reach, authority, timing and burden/constraints fire only when they can change that claim. Refusal and malfunction require separately supported propositions where that distinction is load-bearing. Future strategy/policy revisability does not establish restoration or reversal of a realised transition; if one mechanism genuinely establishes both, support both separately.",
        "refusal and strategy/transition separation",
    ),
    (
        "REPEATED_OUTCOME != SHARED_CAUSE\nPATTERN != PROOF\n```",
        "REPEATED_OUTCOME != SHARED_CAUSE\nPATTERN != PROOF\nLOCAL_CORRECTION + STREAM_PERSISTENCE != MECHANISM_CHANGE\nLOCAL_CASE_REPAIRED != GENERATING_MECHANISM_REPAIRED\nSTREAM_PERSISTENCE != SAME_MECHANISM_PROVEN\n```\n\nA load-bearing mechanism-change claim needs evidence about the relevant mechanism/process/coupling at the resolution used downstream; neither one repaired case nor persistence of the outward stream settles that claim alone.",
        "local correction / mechanism change",
    ),
    (
        "Expose route usability, coupling, burden, residue, future-path changes, designation and comparison measure at the resolution evidence supports.",
        "Expose route usability, coupling, burden, residue, future-path changes, designation and comparison measure at the resolution evidence supports. Keep refusal distinct from malfunction, local correction distinct from mechanism change, future-strategy revisability distinct from realised-transition reversibility, and aggregate recovery distinct from individual repair.",
        "survival-kernel donor propagation",
    ),
)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"{label}: expected exactly one anchor; observed {count}")
    return text.replace(old, new, 1)


def build(base: str) -> str:
    text = base
    for old, new, label in REPLACEMENTS:
        text = replace_once(text, old, new, label)
    return text


def normalize(candidate: str) -> str:
    text = candidate
    for old, new, label in reversed(REPLACEMENTS):
        text = replace_once(text, new, old, f"reverse {label}")
    return text


def report(base: str, candidate: str) -> dict[str, object]:
    errors: list[str] = []
    try:
        normalized_equal = normalize(candidate) == base
    except Exception as exc:  # pragma: no cover - report exact failure
        normalized_equal = False
        errors.append(str(exc))

    required = (
        "REFUSAL != MALFUNCTION",
        "STRATEGY_REVISABLE != TRANSITION_REVERSIBLE",
        "POPULATION_RECOVERY != REPAIR_OF_INDIVIDUAL_LOSS",
        "LOCAL_CORRECTION + STREAM_PERSISTENCE != MECHANISM_CHANGE",
    )
    for token in required:
        if candidate.count(token) != 1:
            errors.append(f"required donor invariant count != 1: {token}")

    if not normalized_equal:
        errors.append("candidate does not normalize exactly to v0.9")

    return {
        "status": "PASS" if not errors else "FAIL",
        "base_path": str(BASE_PATH.relative_to(REPO_ROOT)),
        "output_path": str(OUTPUT_PATH.relative_to(REPO_ROOT)),
        "base_sha256": sha256_text(base),
        "candidate_sha256": sha256_text(candidate),
        "base_bytes": len(base.encode("utf-8")),
        "candidate_bytes": len(candidate.encode("utf-8")),
        "declared_replacement_surfaces": len(REPLACEMENTS),
        "normalized_candidate_equals_base": normalized_equal,
        "restored_invariants": ["I23", "I39", "I53", "I54"],
        "errors": errors,
        "claim_boundary": "I23_I39_I53_I54_DONOR_REPAIR_ONLY_NOT_VALIDATION_NOT_RELEASE_NOT_CANON",
    }


def render(obj: dict[str, object]) -> str:
    return json.dumps(obj, indent=2, sort_keys=True) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args(argv)

    base = BASE_PATH.read_text(encoding="utf-8")
    candidate = build(base)
    rep = report(base, candidate)
    expected = candidate

    if args.write:
        OUTPUT_PATH.write_text(expected, encoding="utf-8")
        REPORT_PATH.write_text(render(rep), encoding="utf-8")

    if args.check:
        if not OUTPUT_PATH.exists() or OUTPUT_PATH.read_text(encoding="utf-8") != expected:
            rep["status"] = "FAIL"
            rep.setdefault("errors", []).append("committed v0.10 differs from deterministic output")
        if not REPORT_PATH.exists() or REPORT_PATH.read_text(encoding="utf-8") != render(report(base, candidate)):
            rep["status"] = "FAIL"
            rep.setdefault("errors", []).append("committed v0.10 build report differs from deterministic output")

    if args.report:
        args.report.write_text(render(rep), encoding="utf-8")
    print(render(rep), end="")
    return 0 if rep["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
