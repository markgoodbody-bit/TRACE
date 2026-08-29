#!/usr/bin/env python3
"""Run the base and hostile-integrity search-coverage passes together."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Mapping

from search_coverage import (
    EPISTEMIC_LIMIT as COVERAGE_LIMIT,
    SearchCoverageInputError,
    check_search_coverage,
)
from search_coverage_integrity import (
    EPISTEMIC_LIMIT as INTEGRITY_LIMIT,
    check_search_coverage_integrity,
)

SUITE_ID = "TD-TSET-SEARCH-COVERAGE-ORCHESTRATOR-001"
ORCHESTRATOR_LIMIT = (
    "Running both passes detects only packet-relative contradiction and comparison-"
    "envelope integrity failures. It does not establish actual search coverage, "
    "complete target selection, good faith, source truth, route executability, or "
    "world completeness."
)


def _error_result(pass_name: str, error: Exception, limit: str) -> dict[str, Any]:
    return {
        "pass": pass_name,
        "status": "INPUT_ERROR",
        "error": str(error),
        "epistemic_limit": limit,
    }


def run_search_coverage_suite(envelope: Mapping[str, Any]) -> dict[str, Any]:
    input_error = False

    try:
        coverage_result = check_search_coverage(envelope).to_dict()
    except (SearchCoverageInputError, TypeError, ValueError) as exc:
        input_error = True
        coverage_result = _error_result("search_coverage", exc, COVERAGE_LIMIT)

    try:
        integrity_result = check_search_coverage_integrity(envelope).to_dict()
    except (SearchCoverageInputError, TypeError, ValueError) as exc:
        input_error = True
        integrity_result = _error_result("search_coverage_integrity", exc, INTEGRITY_LIMIT)

    if input_error:
        combined_status = "INPUT_ERROR"
    elif coverage_result.get("status") == "FAIL" or integrity_result.get("status") == "FAIL":
        combined_status = "FAIL"
    else:
        combined_status = "PASS"

    return {
        "suite_id": SUITE_ID,
        "combined_status": combined_status,
        "coverage_result": coverage_result,
        "integrity_result": integrity_result,
        "results_are_separate": True,
        "failure_codes_are_not_merged": True,
        "orchestrator_epistemic_limit": ORCHESTRATOR_LIMIT,
    }


def run_regressions() -> dict[str, Any]:
    from search_coverage_fixtures import SEARCH_COVERAGE_FIXTURES

    rows: list[dict[str, Any]] = []
    mismatch = False
    for fixture in SEARCH_COVERAGE_FIXTURES:
        result = run_search_coverage_suite(fixture)
        expected = fixture["coverage_expected"]
        expected_combined = "FAIL" if expected["status"] == "FAIL" else "PASS"
        matches = (
            result["combined_status"] == expected_combined
            and result["coverage_result"].get("status") == expected["status"]
            and result["coverage_result"].get("coverage_status")
            == expected["coverage_status"]
            and result["integrity_result"].get("status") == "PASS"
        )
        mismatch = mismatch or not matches
        rows.append(
            {
                "fixture_id": fixture["fixture_id"],
                "actual_combined_status": result["combined_status"],
                "actual_coverage_status": result["coverage_result"].get("coverage_status"),
                "actual_integrity_status": result["integrity_result"].get("status"),
                "expected_combined_status": expected_combined,
                "matches_expected": matches,
            }
        )

    return {
        "suite_id": SUITE_ID,
        "regression_status": "FAIL" if mismatch else "PASS",
        "all_match_expected": not mismatch,
        "results": rows,
        "orchestrator_epistemic_limit": ORCHESTRATOR_LIMIT,
    }


def _load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot load {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def _exit_code(status: str) -> int:
    if status == "PASS":
        return 0
    if status == "INPUT_ERROR":
        return 2
    return 1


def _main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Run both search-coverage passes without collapsing their results."
    )
    parser.add_argument("--compact", action="store_true", help="emit compact JSON")
    subparsers = parser.add_subparsers(dest="command", required=True)
    check_parser = subparsers.add_parser("check", help="check one JSON envelope")
    check_parser.add_argument("input", type=Path)
    subparsers.add_parser("regress", help="run bounded O-R regressions")
    args = parser.parse_args(argv)

    if args.command == "check":
        try:
            envelope = _load_json(args.input)
        except ValueError as exc:
            output = {
                "suite_id": SUITE_ID,
                "combined_status": "INPUT_ERROR",
                "error": str(exc),
                "orchestrator_epistemic_limit": ORCHESTRATOR_LIMIT,
            }
        else:
            output = run_search_coverage_suite(envelope)
        status = str(output.get("combined_status", "INPUT_ERROR"))
    else:
        output = run_regressions()
        status = str(output.get("regression_status", "INPUT_ERROR"))

    print(json.dumps(output, indent=None if args.compact else 2, sort_keys=True))
    return _exit_code(status)


if __name__ == "__main__":
    raise SystemExit(_main())
