#!/usr/bin/env python3
"""
TRACE semantic lint.

Status: semantic drift-control fixture, not validation of TRACE claims.

JSON schema checks whether files are well formed. This script checks for a
small set of forbidden meaning moves that JSON schema cannot see, including:

- schema validity or format transfer being treated as truth / decision advantage
- contaminated DecisionDelta records being upgraded too far
- negative controls producing strong deltas
- missing demotion rules or forbidden-inference blocks

Usage:
  python tests/semantic_lint/trace_semantic_lint.py
  python tests/semantic_lint/trace_semantic_lint.py --json

Exit codes:
  0 = no ERROR-level semantic lint findings
  1 = one or more ERROR-level findings
  2 = setup/load failure
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Iterable


ERROR = "ERROR"
WARN = "WARN"
INFO = "INFO"


@dataclass
class Finding:
    level: str
    path: str
    rule_id: str
    message: str


def repo_root_from_script() -> Path:
    return Path(__file__).resolve().parents[2]


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def as_bool(value: Any) -> bool:
    return bool(value) if isinstance(value, bool) else False


def iter_json_files(root: Path) -> Iterable[Path]:
    if root.exists():
        yield from sorted(root.glob("*.json"))


def lint_case_graph(path: Path, data: dict[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    metadata = data.get("metadata", {}) if isinstance(data, dict) else {}
    guards = metadata.get("guards", []) if isinstance(metadata, dict) else []
    status = str(metadata.get("status", "")).lower() if isinstance(metadata, dict) else ""

    if "schema_valid_not_claim_true" not in guards:
        findings.append(Finding(
            WARN,
            str(path),
            "CG001_missing_schema_truth_guard",
            "Case graph metadata should include schema_valid_not_claim_true to block schema-validity laundering.",
        ))

    if "validation" in status and "not validation" not in status:
        findings.append(Finding(
            ERROR,
            str(path),
            "CG002_validation_status_without_negation",
            "Case graph metadata mentions validation without an explicit 'not validation' guard.",
        ))

    claims = data.get("claims", []) if isinstance(data, dict) else []
    if isinstance(claims, list):
        for i, claim in enumerate(claims):
            if not isinstance(claim, dict):
                continue
            claim_path = f"{path}#/claims/{i}"
            claim_guards = claim.get("guards", [])
            if "schema_valid_not_claim_true" not in claim_guards:
                findings.append(Finding(
                    WARN,
                    claim_path,
                    "CG003_claim_missing_schema_truth_guard",
                    "Claim lacks schema_valid_not_claim_true guard.",
                ))
            if not claim.get("contest_edge"):
                findings.append(Finding(
                    ERROR,
                    claim_path,
                    "CG004_claim_missing_contest_edge",
                    "Claim has no visible contest_edge; live claims must remain challengeable.",
                ))

    baseline_falsifier = data.get("baseline_falsifier") if isinstance(data, dict) else None
    if not baseline_falsifier:
        findings.append(Finding(
            ERROR,
            str(path),
            "CG005_missing_baseline_falsifier",
            "Case graph lacks baseline_falsifier; TRACE cannot claim delta against a blank page.",
        ))

    open_wounds = data.get("open_wounds", []) if isinstance(data, dict) else []
    if not open_wounds:
        findings.append(Finding(
            WARN,
            str(path),
            "CG006_no_open_wounds",
            "Case graph has no open_wounds; check for false closure.",
        ))

    return findings


def lint_decision_delta(path: Path, data: dict[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    assessment = data.get("delta_assessment", {}) if isinstance(data, dict) else {}
    label = assessment.get("label") if isinstance(assessment, dict) else None
    negative_status = data.get("negative_control_status")
    evidence_status = data.get("evidence_status")
    contamination = data.get("contamination_controls", {}) if isinstance(data, dict) else {}
    forbidden = data.get("forbidden_inferences", []) if isinstance(data, dict) else []
    demotion = data.get("demotion_rule") if isinstance(data, dict) else None

    if not forbidden:
        findings.append(Finding(
            ERROR,
            str(path),
            "DD001_missing_forbidden_inferences",
            "DecisionDelta record lacks forbidden_inferences; this allows result laundering.",
        ))

    if not demotion:
        findings.append(Finding(
            ERROR,
            str(path),
            "DD002_missing_demotion_rule",
            "DecisionDelta record lacks a demotion_rule.",
        ))

    if negative_status == "negative_control_pass_idle" and label == "STRONG_DELTA":
        findings.append(Finding(
            ERROR,
            str(path),
            "DD003_negative_control_strong_delta",
            "Negative control produced STRONG_DELTA; this is a pattern-overfit alarm unless case facts changed.",
        ))

    if evidence_status == "illustrative" and label == "STRONG_DELTA":
        findings.append(Finding(
            ERROR,
            str(path),
            "DD004_illustrative_strong_delta",
            "Illustrative evidence status cannot support STRONG_DELTA.",
        ))

    contamination_failed = any(
        contamination.get(key) == "failed"
        for key in [
            "answer_leak_check",
            "order_effect_check",
            "prompt_steering_check",
            "same_model_check",
            "self_scoring_check",
        ]
    )
    if contamination_failed and label == "STRONG_DELTA":
        findings.append(Finding(
            ERROR,
            str(path),
            "DD005_contaminated_strong_delta",
            "Contaminated comparison cannot support STRONG_DELTA.",
        ))
    if contamination_failed and label == "PARTIAL_DELTA":
        findings.append(Finding(
            WARN,
            str(path),
            "DD006_contaminated_partial_delta",
            "Contaminated comparison weakens PARTIAL_DELTA; keep claim low.",
        ))

    changed_flags = [
        as_bool(assessment.get("decision_changed")),
        as_bool(assessment.get("review_route_changed")),
        as_bool(assessment.get("correction_timing_changed")),
        as_bool(assessment.get("affected_scope_added")),
        as_bool(assessment.get("forbidden_inference_blocked")),
    ]
    if label in {"PARTIAL_DELTA", "STRONG_DELTA"} and not any(changed_flags):
        findings.append(Finding(
            ERROR,
            str(path),
            "DD007_delta_without_changed_feature",
            "Delta label is PARTIAL/STRONG but no decision-relevant feature is marked changed.",
        ))

    if label == "COMPRESSION_ONLY" and any(changed_flags[:4]):
        findings.append(Finding(
            WARN,
            str(path),
            "DD008_compression_only_with_changed_feature",
            "COMPRESSION_ONLY record marks a practical changed feature; check label consistency.",
        ))

    return findings


FORBIDDEN_CLAIM_PATTERNS = [
    ("TXT001_validated_claim", re.compile(r"\bTRACE\b.*\b(validated|proven)\b", re.IGNORECASE)),
    ("TXT002_solves_alignment", re.compile(r"\bTRACE\b.*\bsolves?\b.*\balignment\b", re.IGNORECASE)),
    ("TXT003_decision_advantage_proven", re.compile(r"\bdecision advantage\b.*\b(proven|shown|demonstrated)\b", re.IGNORECASE)),
]

NEGATION_OR_GUARD = re.compile(r"\b(not|false|forbidden|do not|cannot|must not|unproven|no validation|not validation)\b", re.IGNORECASE)


def lint_markdown_claims(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    candidate_dirs = [root / "core", root / "00_CONTROL", root / "tests", root / "prompts", root / "reviews"]
    for directory in candidate_dirs:
        if not directory.exists():
            continue
        for path in sorted(directory.rglob("*.md")):
            try:
                lines = path.read_text(encoding="utf-8").splitlines()
            except UnicodeDecodeError:
                continue
            for line_no, line in enumerate(lines, start=1):
                for rule_id, pattern in FORBIDDEN_CLAIM_PATTERNS:
                    if pattern.search(line) and not NEGATION_OR_GUARD.search(line):
                        findings.append(Finding(
                            WARN,
                            f"{path}:{line_no}",
                            rule_id,
                            "Possible overclaim without visible negation/guard.",
                        ))
    return findings


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="TRACE semantic lint checks.")
    parser.add_argument("--json", action="store_true", help="Emit JSON report")
    parser.add_argument("--no-text-scan", action="store_true", help="Skip markdown overclaim scan")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    root = repo_root_from_script()
    findings: list[Finding] = []

    try:
        for path in iter_json_files(root / "cases" / "graphs"):
            findings.extend(lint_case_graph(path, load_json(path)))
        for path in iter_json_files(root / "tests" / "fair_compare"):
            findings.extend(lint_decision_delta(path, load_json(path)))
        if not args.no_text_scan:
            findings.extend(lint_markdown_claims(root))
    except Exception as exc:
        if args.json:
            print(json.dumps({"ok": False, "setup_errors": [str(exc)]}, indent=2))
        else:
            print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    error_count = sum(1 for f in findings if f.level == ERROR)
    warn_count = sum(1 for f in findings if f.level == WARN)
    ok = error_count == 0

    if args.json:
        print(json.dumps({
            "ok": ok,
            "error_count": error_count,
            "warn_count": warn_count,
            "findings": [asdict(f) for f in findings],
        }, indent=2))
    else:
        print("TRACE semantic lint")
        print("NOTE: semantic-lint clean != true, justified, complete, or decision-useful")
        print(f"ERRORS: {error_count}")
        print(f"WARNINGS: {warn_count}")
        print("")
        for finding in findings:
            print(f"[{finding.level}] {finding.path} {finding.rule_id}: {finding.message}")
        print("")
        print("RESULT:", "PASS" if ok else "FAIL")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
