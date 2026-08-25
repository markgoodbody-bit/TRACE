#!/usr/bin/env python3
"""Compare released TRACE v0.2.7 numbered invariants with v0.3 spine v0.10.

This is intentionally a lexical coverage check. An invariant expression being
absent verbatim does not prove semantic loss, and being present does not prove
it fires correctly. The report exists to make the second, semantic pass
bounded and explicit.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DONOR_PATH = REPO_ROOT / "TRACE_FORMAL_SEED_v0_2_7.md"
CANDIDATE_PATH = REPO_ROOT / "PROJECT" / "TRACE_v0_3_0_SPINE_CANDIDATE_v0_10.md"
OUTPUT_PATH = REPO_ROOT / "PROJECT" / "TRACE_v0_3_0_INVARIANT_LEXICAL_COVERAGE_v0_3.json"

SECTION_START = "# [19] INVARIANTS / MISUSE GUARDS"
SECTION_END = "## [19.1] Packet as diligence token"
INVARIANT_RE = re.compile(r"^I(?P<num>\d{2})\s{2,}(?P<expr>\S.*)$", re.MULTILINE)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def extract_invariants(text: str) -> list[tuple[str, str]]:
    start = text.index(SECTION_START)
    end = text.index(SECTION_END, start)
    section = text[start:end]
    rows = [(m.group("num"), m.group("expr").strip()) for m in INVARIANT_RE.finditer(section)]

    expected = [f"{i:02d}" for i in range(1, 61)]
    observed = [num for num, _ in rows]
    if observed != expected:
        raise ValueError(f"expected invariant ids I01..I60 in order; observed={observed!r}")
    if len({expr for _, expr in rows}) != 60:
        raise ValueError("donor invariant expressions are not unique")
    return rows


def build_report(donor_text: str, candidate_text: str) -> dict[str, object]:
    invariants = extract_invariants(donor_text)
    rows: list[dict[str, object]] = []
    exact_ids: list[str] = []
    missing_ids: list[str] = []

    for num, expr in invariants:
        count = candidate_text.count(expr)
        exact = count > 0
        invariant_id = f"I{num}"
        if exact:
            exact_ids.append(invariant_id)
        else:
            missing_ids.append(invariant_id)
        rows.append(
            {
                "id": invariant_id,
                "expression": expr,
                "exact_expression_count_in_candidate": count,
                "exact_expression_present": exact,
                "semantic_disposition": "UNASSESSED",
            }
        )

    return {
        "status": "PASS",
        "check_type": "LEXICAL_COVERAGE_ONLY",
        "donor_path": str(DONOR_PATH.relative_to(REPO_ROOT)),
        "candidate_path": str(CANDIDATE_PATH.relative_to(REPO_ROOT)),
        "donor_sha256": sha256_text(donor_text),
        "candidate_sha256": sha256_text(candidate_text),
        "donor_invariant_count": len(invariants),
        "exact_expression_present_count": len(exact_ids),
        "exact_expression_missing_count": len(missing_ids),
        "exact_expression_present_ids": exact_ids,
        "exact_expression_missing_ids": missing_ids,
        "invariants": rows,
        "claim_boundary": (
            "EXACT_EXPRESSION_PRESENCE_NOT_SEMANTIC_EQUIVALENCE_"
            "NOT_TRIGGER_ADEQUACY_NOT_VALIDATION"
        ),
    }


def render(report: dict[str, object]) -> str:
    return json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args(argv)

    donor_text = DONOR_PATH.read_text(encoding="utf-8")
    candidate_text = CANDIDATE_PATH.read_text(encoding="utf-8")
    report = build_report(donor_text, candidate_text)
    expected = render(report)

    errors: list[str] = []
    if args.write:
        OUTPUT_PATH.write_text(expected, encoding="utf-8")
    if args.check:
        if not OUTPUT_PATH.exists():
            errors.append("committed lexical coverage report missing")
        elif OUTPUT_PATH.read_text(encoding="utf-8") != expected:
            errors.append("committed lexical coverage report differs from deterministic output")

    if errors:
        report["status"] = "FAIL"
        report["errors"] = errors
    else:
        report["errors"] = []

    final = render(report)
    if args.report:
        args.report.write_text(final, encoding="utf-8")
    print(final, end="")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
