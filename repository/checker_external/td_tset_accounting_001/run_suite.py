#!/usr/bin/env python3
"""Orchestrate the TRACE transition-accounting and hostile-integrity passes.

The two passes remain separate. This module does not merge their failure codes,
epistemic ceilings, or meanings into a single semantic verdict.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Mapping

from checker import (
    CheckerInputError,
    EPISTEMIC_LIMIT as ACCOUNTING_EPISTEMIC_LIMIT,
    check_envelope,
    run_bundle as run_accounting_bundle,
)
from integrity import (
    EPISTEMIC_LIMIT as INTEGRITY_EPISTEMIC_LIMIT,
    IntegrityInputError,
    check_integrity,
    run_bundle as run_integrity_bundle,
)

SUITE_ID = "TD-TSET-ACCOUNTING-ORCHESTRATOR-001"
ORCHESTRATOR_LIMIT = (
    "Running both passes does not establish world completeness, claim truth, good "
    "faith, route executability, or the absence of unseen entities or alternatives. "
    "Accounting and integrity results remain separately attributable."
)


def _load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot load {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def _error_result(pass_name: str, error: Exception, epistemic_limit: str) -> dict[str, Any]:
    return {
        "pass": pass_name,
        "status": "INPUT_ERROR",
        "error": str(error),
        "epistemic_limit": epistemic_limit,
    }


def run_combined_envelope(envelope: Mapping[str, Any]) -> dict[str, Any]:
    """Run both passes against one envelope without merging their semantics."""

    input_error = False

    try:
        accounting_result: dict[str, Any] = check_envelope(envelope).to_dict()
    except (CheckerInputError, TypeError, ValueError) as exc:
        input_error = True
        accounting_result = _error_result(
            "transition_class_accounting", exc, ACCOUNTING_EPISTEMIC_LIMIT
        )

    try:
        integrity_result: dict[str, Any] = check_integrity(envelope).to_dict()
    except (IntegrityInputError, TypeError, ValueError) as exc:
        input_error = True
        integrity_result = _error_result(
            "hostile_integrity", exc, INTEGRITY_EPISTEMIC_LIMIT
        )

    if input_error:
        combined_status = "INPUT_ERROR"
    elif accounting_result.get("status") == "FAIL" or integrity_result.get("status") == "FAIL":
        combined_status = "FAIL"
    else:
        combined_status = "PASS"

    return {
        "suite_id": SUITE_ID,
        "mode": "single_envelope",
        "combined_status": combined_status,
        "accounting_result": accounting_result,
        "integrity_result": integrity_result,
        "results_are_separate": True,
        "failure_codes_are_not_merged": True,
        "orchestrator_epistemic_limit": ORCHESTRATOR_LIMIT,
    }


def _run_regression_pass(
    pass_name: str,
    path: Path,
    runner: Any,
    epistemic_limit: str,
    accepted_errors: tuple[type[Exception], ...],
) -> dict[str, Any]:
    try:
        rows, mismatch = runner(path)
    except accepted_errors as exc:
        return _error_result(pass_name, exc, epistemic_limit)
    return {
        "pass": pass_name,
        "regression_status": "FAIL" if mismatch else "PASS",
        "fixture_file": str(path),
        "results": rows,
        "all_match_expected": not mismatch,
        "epistemic_limit": epistemic_limit,
    }


def run_regression_suites(accounting_path: Path, integrity_path: Path) -> dict[str, Any]:
    """Run the A-F and G-J bundles while preserving pass separation."""

    accounting = _run_regression_pass(
        "transition_class_accounting",
        accounting_path,
        run_accounting_bundle,
        ACCOUNTING_EPISTEMIC_LIMIT,
        (CheckerInputError, OSError, ValueError),
    )
    integrity = _run_regression_pass(
        "hostile_integrity",
        integrity_path,
        run_integrity_bundle,
        INTEGRITY_EPISTEMIC_LIMIT,
        (IntegrityInputError, OSError, ValueError),
    )

    statuses = {
        accounting.get("regression_status", accounting.get("status")),
        integrity.get("regression_status", integrity.get("status")),
    }
    if "INPUT_ERROR" in statuses:
        regression_status = "INPUT_ERROR"
    elif "FAIL" in statuses:
        regression_status = "FAIL"
    else:
        regression_status = "PASS"

    return {
        "suite_id": SUITE_ID,
        "mode": "regression_bundles",
        "regression_status": regression_status,
        "accounting_suite": accounting,
        "integrity_suite": integrity,
        "results_are_separate": True,
        "failure_codes_are_not_merged": True,
        "orchestrator_epistemic_limit": ORCHESTRATOR_LIMIT,
    }


def _exit_code(status: str) -> int:
    if status == "PASS":
        return 0
    if status == "INPUT_ERROR":
        return 2
    return 1


def _main(argv: list[str] | None = None) -> int:
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(
        description="Run both TD-TSET checker passes without collapsing their results."
    )
    parser.add_argument("--compact", action="store_true", help="emit compact JSON")
    subparsers = parser.add_subparsers(dest="command", required=True)

    check_parser = subparsers.add_parser("check", help="run both passes on one envelope")
    check_parser.add_argument("input", type=Path)

    regress_parser = subparsers.add_parser(
        "regress", help="run the bounded A-F and G-J regression bundles"
    )
    regress_parser.add_argument(
        "--accounting",
        type=Path,
        default=here / "fixtures.json",
        help="A-F accounting fixture bundle",
    )
    regress_parser.add_argument(
        "--integrity",
        type=Path,
        default=here / "fixtures_hostile.json",
        help="G-J hostile-integrity fixture bundle",
    )

    args = parser.parse_args(argv)

    if args.command == "check":
        try:
            envelope = _load_json(args.input)
        except ValueError as exc:
            output = {
                "suite_id": SUITE_ID,
                "mode": "single_envelope",
                "combined_status": "INPUT_ERROR",
                "error": str(exc),
                "orchestrator_epistemic_limit": ORCHESTRATOR_LIMIT,
            }
        else:
            output = run_combined_envelope(envelope)
        status = str(output.get("combined_status", "INPUT_ERROR"))
    else:
        output = run_regression_suites(args.accounting, args.integrity)
        status = str(output.get("regression_status", "INPUT_ERROR"))

    print(json.dumps(output, indent=None if args.compact else 2, sort_keys=True))
    return _exit_code(status)


if __name__ == "__main__":
    raise SystemExit(_main())
