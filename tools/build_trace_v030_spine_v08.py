#!/usr/bin/env python3
"""Build TRACE v0.3.0 spine candidate v0.8 deterministically from v0.7.

v0.8 repairs only the executable-pathway/occurrence binding regression found
in v0.7. No other semantic or schema change is permitted by this compiler.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
BASE_PATH = REPO_ROOT / "PROJECT" / "TRACE_v0_3_0_SPINE_CANDIDATE_v0_7.md"
OUTPUT_PATH = REPO_ROOT / "PROJECT" / "TRACE_v0_3_0_SPINE_CANDIDATE_v0_8.md"

OLD_HEADER = "# TRACE // v0.3.0 SPINE CANDIDATE v0.7"
NEW_HEADER = "# TRACE // v0.3.0 SPINE CANDIDATE v0.8"

OLD_PRECEDENCE = """where `V` contains load-bearing stages/events and `E_prec` required precedence. `E_prec` is a derived process/timing view, not a new canonical TRACE relation.\n\nEvery load-bearing derived precedence edge retains the canonical ordering-claim references that support it and, where not recoverable from those claims, the material mechanism and scope/time bindings. The edge does not upgrade the evidence or currentness of its sources.\n\nBefore critical-path arithmetic is used for a strong window claim, bind the relevant ordering edges to the same declared process/scope/time context and require the resulting precedence view to be acyclic. Material contradictory/cyclic ordering, or unresolved binding/acyclicity, blocks the **critical-path route** to a strong window status unless separate domain-supported timing evidence establishes the result without relying on that invalid/unresolved path.\n\n```text\nDERIVED_EDGE_PRESENT != ORDERING_TRUE\nPROVENANCE_PRESERVED != ORDERING_CONSISTENT\nSUPPORTED_EDGES != VALID_DAG\nCYCLIC_PRECEDENCE != COMPUTABLE_CRITICAL_PATH\nCYCLIC_REPRESENTED_ORDERING != WORLD_DEADLOCK_PROVEN\n```\n\nA precedence-only critical path may be an optimistic structural bound; it is not automatically a feasible completion time.\n\n```text\nNO_PRECEDENCE_EDGE != CONCURRENCY_AVAILABLE\nSTRUCTURAL_PARALLELISM != FEASIBLE_PARALLELISM\nPRECEDENCE_GRAPH_COMPLETE != EXECUTION_FEASIBILITY_COMPLETE\nACYCLIC_SUPPORTED != FEASIBLE_SCHEDULE_ESTABLISHED\n```\n\nIf assumed overlap materially changes the conclusion, require support that relevant execution constraints permit it. Otherwise use a domain-supported feasible completion bound or preserve `UNKNOWN`. Existing coupling/control/constraint/route/capability structure carries whatever shared worker, actuator, lock, channel, queue or other capacity is material; no resource ontology is added.\n"""

NEW_PRECEDENCE = """where `V` contains load-bearing event/stage occurrences and `E_prec` required precedence. `E_prec` is a derived timing view, not a canonical TRACE relation.\n\nEach load-bearing precedence edge retains its supporting canonical ordering claims plus material mechanism/binding refs not recoverable from them. Before critical-path use, build the view for one executable pathway hypothesis: bind process/pathway, scope, target, route/execution alternative, capability context, time/policy version and use where they can change the result. Unknown load-bearing route membership remains `UNKNOWN`; do not union mutually exclusive alternatives. When stage types recur, distinguish occurrences where collapse could create/erase a cycle or change timing. The resulting view must be acyclic.\n\n```text\nDERIVED_EDGE_PRESENT != ORDERING_TRUE\nSAME_PROCESS_SCOPE_TIME != SAME_ROUTE_BINDING\nALTERNATIVE_ROUTE_ORDERINGS != ONE_PROCESS_CYCLE\nSTAGE_TYPE_CYCLE != EVENT_INSTANCE_CYCLE\nPROVENANCE_PRESERVED != ORDERING_CONSISTENT\nSUPPORTED_EDGES != VALID_DAG\nCYCLIC_PRECEDENCE != COMPUTABLE_CRITICAL_PATH\nCYCLIC_REPRESENTED_ORDERING != WORLD_DEADLOCK_PROVEN\n```\n\nContradictory/cyclic ordering or unresolved binding/acyclicity blocks that **critical-path proof route** to a strong window status; it does not invalidate separate domain-supported timing evidence.\n\nA precedence critical path may be an optimistic structural bound, not feasible completion time.\n\n```text\nNO_PRECEDENCE_EDGE != CONCURRENCY_AVAILABLE\nSTRUCTURAL_PARALLELISM != FEASIBLE_PARALLELISM\nPRECEDENCE_GRAPH_COMPLETE != EXECUTION_FEASIBILITY_COMPLETE\nACYCLIC_SUPPORTED != FEASIBLE_SCHEDULE_ESTABLISHED\n```\n\nIf assumed overlap changes the conclusion, require support that execution constraints permit it; otherwise use a domain-supported feasible bound or preserve `UNKNOWN`. Existing coupling/control/constraint/route/capability structure carries material shared capacity; no resource ontology is added.\n"""

OLD_KERNEL = "Correction timing needs an explicit target boundary, comparable clocks and a supported process bound; derived precedence remains source-bound and acyclic for critical-path use, and apparent parallelism does not shorten the window unless it is feasible."
NEW_KERNEL = "Correction timing needs an explicit target boundary, comparable clocks and a supported process bound; critical-path precedence remains source-, pathway- and occurrence-bound, acyclic, and separately feasible."


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"{label}: expected exactly one anchor, observed {count}")
    return text.replace(old, new, 1)


def compile_spine(base: str) -> str:
    text = replace_once(base, OLD_HEADER, NEW_HEADER, "header")
    text = replace_once(text, OLD_PRECEDENCE, NEW_PRECEDENCE, "precedence block")
    text = replace_once(text, OLD_KERNEL, NEW_KERNEL, "survival-kernel timing sentence")
    return text


def normalize_candidate(candidate: str) -> str:
    text = replace_once(candidate, NEW_HEADER, OLD_HEADER, "normalized header")
    text = replace_once(text, NEW_PRECEDENCE, OLD_PRECEDENCE, "normalized precedence block")
    text = replace_once(text, NEW_KERNEL, OLD_KERNEL, "normalized survival-kernel sentence")
    return text


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def verify(base: str, candidate: str) -> dict[str, object]:
    normalized = normalize_candidate(candidate)
    errors: list[str] = []
    if normalized != base:
        errors.append("candidate differs from v0.7 outside the three declared replacement surfaces")

    required_tokens = (
        "SAME_PROCESS_SCOPE_TIME != SAME_ROUTE_BINDING",
        "ALTERNATIVE_ROUTE_ORDERINGS != ONE_PROCESS_CYCLE",
        "STAGE_TYPE_CYCLE != EVENT_INSTANCE_CYCLE",
        "PROVENANCE_PRESERVED != ORDERING_CONSISTENT",
        "ACYCLIC_SUPPORTED != FEASIBLE_SCHEDULE_ESTABLISHED",
        "source-, pathway- and occurrence-bound",
    )
    for token in required_tokens:
        if candidate.count(token) != 1:
            errors.append(f"required token count != 1: {token!r}")

    return {
        "status": "PASS" if not errors else "FAIL",
        "base_path": str(BASE_PATH.relative_to(REPO_ROOT)),
        "output_path": str(OUTPUT_PATH.relative_to(REPO_ROOT)),
        "base_sha256": sha256(base),
        "candidate_sha256": sha256(candidate),
        "base_bytes": len(base.encode("utf-8")),
        "candidate_bytes": len(candidate.encode("utf-8")),
        "normalized_candidate_equals_base": normalized == base,
        "declared_replacement_surfaces": 3,
        "errors": errors,
        "claim_boundary": "ROUTE_OCCURRENCE_BINDING_REPAIR_ONLY_NOT_VALIDATION_NOT_RELEASE_NOT_CANON",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args(argv)

    base = BASE_PATH.read_text(encoding="utf-8")
    candidate = compile_spine(base)
    report = verify(base, candidate)

    if args.write:
        OUTPUT_PATH.write_text(candidate, encoding="utf-8")

    if args.check:
        if not OUTPUT_PATH.exists():
            report["errors"].append("candidate output file missing")
        elif OUTPUT_PATH.read_text(encoding="utf-8") != candidate:
            report["errors"].append("committed v0.8 candidate differs from deterministic output")

    if report["errors"]:
        report["status"] = "FAIL"

    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.report:
        args.report.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
