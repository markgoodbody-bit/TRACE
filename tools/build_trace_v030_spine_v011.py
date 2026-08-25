#!/usr/bin/env python3
"""Build TRACE v0.3.0 spine candidate v0.11 from v0.10.

Admitted changes restore donor invariants I03, I25, I49, I50 and I52 plus
survival-kernel propagation. No schema or ontology change is made.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
BASE_PATH = REPO_ROOT / "PROJECT" / "TRACE_v0_3_0_SPINE_CANDIDATE_v0_10.md"
OUTPUT_PATH = REPO_ROOT / "PROJECT" / "TRACE_v0_3_0_SPINE_CANDIDATE_v0_11.md"
REPORT_PATH = REPO_ROOT / "PROJECT" / "TRACE_v0_3_0_SPINE_V011_BUILD_REPORT_v0_1.json"

REPLACEMENTS = (
    (
        "# TRACE // v0.3.0 SPINE CANDIDATE v0.10",
        "# TRACE // v0.3.0 SPINE CANDIDATE v0.11",
        "version header",
    ),
    (
        "ACTOR_REPORT != WORLD_STATE\nNULL_INPUT != STATIC_WORLD\n```",
        "ACTOR_REPORT != WORLD_STATE\nNULL_INPUT != STATIC_WORLD\nUNCERTAINTY != SELECT_ACTION\nUNCERTAINTY != SELECT_DELAY\n```\n\nUncertainty may be an input to an external selector/policy, including a policy that chooses action or delay. Attribute the resulting selection to that selector/policy/default rule; uncertainty itself is not the selector.",
        "uncertainty selection attribution",
    ),
    (
        "OPERATOR_REPORT != INDEPENDENT_VERIFICATION\n```",
        "OPERATOR_REPORT != INDEPENDENT_VERIFICATION\nREPORTED != ESTABLISHED\nREPORT_PRESENT != ESTABLISHMENT_RULE_SATISFIED\n```\n\nA report may establish a status under a declared domain evidence/authority contract, but `REPORTED` status alone does not perform that upgrade.",
        "reported / established separation",
    ),
    (
        "EVENT_TIME != STAGE_DURATION\nURGENCY != IRREVERSIBILITY\n```",
        "EVENT_TIME != STAGE_DURATION\nURGENCY != IRREVERSIBILITY\nHARDENING != IRREVERSIBILITY\nHARDER_TO_CORRECT != IMPOSSIBLE_TO_CORRECT\n```\n\nHardening may contribute to a separately supported irreversibility claim, but a hardening clock/status does not become an irreversibility boundary by label alone.",
        "hardening / irreversibility separation",
    ),
    (
        "TRANSFERRED_BURDEN != REMOVED_BURDEN\nRECORD_EXISTS != RECORD_COMPLETE\n```",
        "TRANSFERRED_BURDEN != REMOVED_BURDEN\nRECORD_EXISTS != RECORD_COMPLETE\nRECORD != EVENT\nRECORD_OBSERVED != EVENT_OBSERVED\n```\n\nA record may support an event claim under an evidential contract; observing the record does not make the historical/world event itself directly observed.",
        "record / event separation",
    ),
    (
        "Keep evidence status distinct from who can access, control or disclose the evidence.",
        "Keep evidence status distinct from who can access, control or disclose the evidence; a report is not established merely by being reported, and a record is not the event it records.",
        "survival-kernel evidence propagation",
    ),
    (
        "Correction timing needs an explicit target boundary, comparable clocks and a supported process bound; critical-path precedence remains source-, pathway- and occurrence-bound, acyclic, and separately feasible.",
        "Correction timing needs an explicit target boundary, comparable clocks and a supported process bound; critical-path precedence remains source-, pathway- and occurrence-bound, acyclic, and separately feasible. Keep hardening distinct from irreversibility, and uncertainty distinct from the selector/policy that chooses action or delay.",
        "survival-kernel timing/selection propagation",
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


def make_report(base: str, candidate: str) -> dict[str, object]:
    errors: list[str] = []
    try:
        normalized_equal = normalize(candidate) == base
    except Exception as exc:
        normalized_equal = False
        errors.append(str(exc))

    required = (
        "REPORTED != ESTABLISHED",
        "RECORD != EVENT",
        "UNCERTAINTY != SELECT_ACTION",
        "UNCERTAINTY != SELECT_DELAY",
        "HARDENING != IRREVERSIBILITY",
    )
    for token in required:
        if candidate.count(token) != 1:
            errors.append(f"required donor invariant count != 1: {token}")

    if not normalized_equal:
        errors.append("candidate does not normalize exactly to v0.10")

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
        "restored_invariants": ["I03", "I25", "I49", "I50", "I52"],
        "errors": errors,
        "claim_boundary": "I03_I25_I49_I50_I52_DONOR_REPAIR_ONLY_NOT_VALIDATION_NOT_RELEASE_NOT_CANON",
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
    rep = make_report(base, candidate)

    if args.write:
        OUTPUT_PATH.write_text(candidate, encoding="utf-8")
        REPORT_PATH.write_text(render(rep), encoding="utf-8")

    if args.check:
        if not OUTPUT_PATH.exists() or OUTPUT_PATH.read_text(encoding="utf-8") != candidate:
            rep["status"] = "FAIL"
            rep.setdefault("errors", []).append("committed v0.11 differs from deterministic output")
        expected_report = render(make_report(base, candidate))
        if not REPORT_PATH.exists() or REPORT_PATH.read_text(encoding="utf-8") != expected_report:
            rep["status"] = "FAIL"
            rep.setdefault("errors", []).append("committed v0.11 build report differs from deterministic output")

    if args.report:
        args.report.write_text(render(rep), encoding="utf-8")
    print(render(rep), end="")
    return 0 if rep["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
