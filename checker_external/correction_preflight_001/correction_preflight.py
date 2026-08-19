#!/usr/bin/env python3
"""Bounded TRACE correction-preflight checker.

Candidate ID: TRACE-CORRECTION-PREFLIGHT-001

This checker examines only declared support structure for a bounded claim/use.
It does not establish truth, world completeness, safety, legitimacy, permission,
moral adequacy, or that an omitted claim mode is absent.
"""
from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, field
from typing import Any, Mapping

CANDIDATE_ID = "TRACE-CORRECTION-PREFLIGHT-001"

MODE_CURRENT = "CURRENT"
MODE_COMPLETE = "COMPLETE"
MODE_VERIFIED = "VERIFIED"
MODE_CORRECTABLE = "CORRECTABLE"
MODE_AUTHORIZED = "AUTHORIZED"
ALLOWED_MODES = frozenset(
    {MODE_CURRENT, MODE_COMPLETE, MODE_VERIFIED, MODE_CORRECTABLE, MODE_AUTHORIZED}
)

LEXICAL_SENTINELS = {
    MODE_COMPLETE: (
        r"\ball\b", r"\bevery\b", r"\bnone\b", r"\bcomplete\b",
        r"\bexhaustive\b", r"\b100\s*%", r"\bno counterexample\b",
        r"\bno alternative\b",
    ),
    MODE_CURRENT: (
        r"\bcurrent\b", r"\bcurrently\b", r"\bnow\b", r"\btoday\b",
        r"\btonight\b", r"\blive\b",
    ),
    MODE_VERIFIED: (r"\bverified\b", r"\bchecked\b", r"\bvalidated\b", r"\btested\b"),
    MODE_CORRECTABLE: (r"\bcorrectable\b", r"\breversible\b", r"\brollback\b", r"\bcan be repaired\b"),
    MODE_AUTHORIZED: (r"\bauthorized\b", r"\bauthorised\b", r"\bpermitted\b", r"\bpermission\b"),
}

EPISTEMIC_LIMIT = (
    "This preflight checks only declared support structure for declared claim "
    "modes. DECLARED_SUPPORT_FIELDS_PRESENT does not establish truth, completeness, "
    "safety, permission, legitimate authority, moral adequacy, actual route "
    "execution, or world effect. The lexical sentinel can suggest an undeclared "
    "mode but cannot establish that no other mode is present."
)


class PreflightInputError(ValueError):
    pass


@dataclass(slots=True)
class Finding:
    code: str
    mode: str
    message: str
    severity: str = "GAP"

    def to_dict(self) -> dict[str, str]:
        return {
            "code": self.code,
            "mode": self.mode,
            "severity": self.severity,
            "message": self.message,
        }


@dataclass(slots=True)
class PreflightResult:
    fixture_id: str
    status: str
    declared_modes: list[str] = field(default_factory=list)
    sentinel_modes: list[str] = field(default_factory=list)
    findings: list[Finding] = field(default_factory=list)
    epistemic_limit: str = EPISTEMIC_LIMIT

    def to_dict(self) -> dict[str, Any]:
        return {
            "candidate_id": CANDIDATE_ID,
            "fixture_id": self.fixture_id,
            "status": self.status,
            "declared_modes": self.declared_modes,
            "sentinel_modes": self.sentinel_modes,
            "findings": [item.to_dict() for item in self.findings],
            "epistemic_limit": self.epistemic_limit,
        }


def _as_dict(value: Any, label: str) -> dict[str, Any]:
    if value is None:
        return {}
    if not isinstance(value, dict):
        raise PreflightInputError(f"{label} must be an object")
    return dict(value)


def _as_modes(value: Any) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        raise PreflightInputError("claim_modes must be an array of strings")
    modes = [item.strip().upper() for item in value]
    unknown = sorted(set(modes) - ALLOWED_MODES)
    if unknown:
        raise PreflightInputError("unknown claim_modes: " + ", ".join(unknown))
    return sorted(set(modes))


def _sentinel_modes(text: str) -> list[str]:
    lower = text.lower()
    return sorted(
        mode
        for mode, patterns in LEXICAL_SENTINELS.items()
        if any(re.search(pattern, lower) for pattern in patterns)
    )


def _nonempty_str(mapping: Mapping[str, Any], key: str) -> bool:
    value = mapping.get(key)
    return isinstance(value, str) and bool(value.strip())


def _status(mapping: Mapping[str, Any], key: str) -> str:
    value = mapping.get(key, "UNKNOWN")
    return value.upper() if isinstance(value, str) else "UNKNOWN"


def check_preflight(envelope: Mapping[str, Any]) -> PreflightResult:
    if not isinstance(envelope, Mapping):
        raise PreflightInputError("envelope must be an object")

    env = dict(envelope)
    fixture_id = str(env.get("fixture_id", "UNNAMED"))
    claim_text = env.get("claim_text", "")
    if not isinstance(claim_text, str):
        raise PreflightInputError("claim_text must be a string")

    modes = _as_modes(env.get("claim_modes", []))
    sentinels = _sentinel_modes(claim_text)
    findings: list[Finding] = []

    # One-way falsifier only: a lexical hit can challenge an omission. No hit
    # cannot prove that a mode is absent.
    for mode in sorted(set(sentinels) - set(modes)):
        findings.append(
            Finding(
                "PREFLIGHT-UNDECLARED-MODE-SUSPECTED",
                mode,
                f"claim language suggests {mode} but claim_modes does not declare it; "
                "inspect rather than treating the omission as absence",
                "NOTICE",
            )
        )

    if MODE_CURRENT in modes:
        current = _as_dict(env.get("currentness"), "currentness")
        if not _nonempty_str(current, "source_ref"):
            findings.append(Finding("PREFLIGHT-CURRENT-SOURCE-MISSING", MODE_CURRENT, "CURRENT claim requires a declared current-state source/reference"))
        if not _nonempty_str(current, "checked_at_utc"):
            findings.append(Finding("PREFLIGHT-CURRENT-CHECK-TIME-MISSING", MODE_CURRENT, "CURRENT claim requires a declared current-state check time"))
        if current.get("reacquired") is not True:
            findings.append(Finding("PREFLIGHT-CURRENT-NOT-REACQUIRED", MODE_CURRENT, "CURRENT claim is not supported by an explicit current reacquisition"))

    if MODE_COMPLETE in modes:
        coverage = _as_dict(env.get("coverage"), "coverage")
        requirements = (
            ("target_set_ref", "PREFLIGHT-COVERAGE-TARGET-SET-MISSING", "COMPLETE claim requires a declared target/denominator set"),
            ("selection_basis_ref", "PREFLIGHT-COVERAGE-SELECTION-BASIS-MISSING", "COMPLETE claim requires a declared target-set selection basis"),
            ("comparison_basis_ref", "PREFLIGHT-COVERAGE-COMPARISON-BASIS-MISSING", "COMPLETE claim requires a declared comparison basis"),
        )
        for key, code, message in requirements:
            if not _nonempty_str(coverage, key):
                findings.append(Finding(code, MODE_COMPLETE, message))

        coverage_status = _status(coverage, "coverage_status")
        allowed_coverage = {"ESTABLISHED_RELATIVE_TO_DECLARED_BASIS", "CONTRADICTED", "UNKNOWN"}
        if coverage_status not in allowed_coverage:
            findings.append(Finding("PREFLIGHT-COVERAGE-STATUS-INVALID", MODE_COMPLETE, "coverage_status must be ESTABLISHED_RELATIVE_TO_DECLARED_BASIS, CONTRADICTED, or UNKNOWN"))
        elif coverage_status != "ESTABLISHED_RELATIVE_TO_DECLARED_BASIS":
            findings.append(Finding("PREFLIGHT-COVERAGE-NOT-ESTABLISHED", MODE_COMPLETE, f"coverage is {coverage_status}; selected-target success cannot support an unqualified COMPLETE claim"))

        omissions = _status(coverage, "known_omissions")
        if omissions == "PRESENT":
            findings.append(Finding("PREFLIGHT-KNOWN-OMISSION-PRESENT", MODE_COMPLETE, "known omitted targets/categories contradict an unqualified COMPLETE claim"))
        elif omissions not in {"NONE_ESTABLISHED", "PRESENT", "UNKNOWN"}:
            findings.append(Finding("PREFLIGHT-OMISSION-STATUS-INVALID", MODE_COMPLETE, "known_omissions must be NONE_ESTABLISHED, PRESENT, or UNKNOWN"))
        # NONE_ESTABLISHED is deliberately not treated as world completeness.

    if MODE_VERIFIED in modes:
        verification = _as_dict(env.get("verification"), "verification")
        if not _nonempty_str(verification, "proposition_ref"):
            findings.append(Finding("PREFLIGHT-VERIFICATION-PROPOSITION-MISSING", MODE_VERIFIED, "VERIFIED claim requires the exact proposition/check target"))
        if verification.get("executed") is not True:
            findings.append(Finding("PREFLIGHT-CHECK-NOT-EXECUTED", MODE_VERIFIED, "a check path or procedure is not evidence that the check executed"))
        adequacy = _status(verification, "instrument_adequacy")
        if adequacy != "ESTABLISHED_FOR_PROPOSITION":
            findings.append(Finding("PREFLIGHT-INSTRUMENT-ADEQUACY-NOT-ESTABLISHED", MODE_VERIFIED, f"instrument adequacy is {adequacy}; TEST_RAN != RELEVANT_ALTERNATIVE_DETECTABLE"))
        if verification.get("result_returned_to_use") is not True:
            findings.append(Finding("PREFLIGHT-CHECK-RESULT-NOT-RETURNED", MODE_VERIFIED, "check result is not represented as having reached the current use"))
        if not _nonempty_str(verification, "result_ref"):
            findings.append(Finding("PREFLIGHT-CHECK-RESULT-MISSING", MODE_VERIFIED, "VERIFIED claim requires a declared result/evidence reference"))

    if MODE_CORRECTABLE in modes:
        correction = _as_dict(env.get("correction"), "correction")
        if not _nonempty_str(correction, "route_ref"):
            findings.append(Finding("PREFLIGHT-CORRECTION-ROUTE-MISSING", MODE_CORRECTABLE, "CORRECTABLE claim requires a declared correction route"))
        if _status(correction, "reachability") != "YES":
            findings.append(Finding("PREFLIGHT-CORRECTION-ROUTE-NOT-REACHABLE", MODE_CORRECTABLE, f"correction route reachability is {_status(correction, 'reachability')}"))
        if not _nonempty_str(correction, "hardening_ref"):
            findings.append(Finding("PREFLIGHT-HARDENING-BOUNDARY-MISSING", MODE_CORRECTABLE, "CORRECTABLE claim requires a declared hardening/closure boundary"))
        if _status(correction, "arrives_before_hardening") != "YES":
            findings.append(Finding("PREFLIGHT-CORRECTION-WINDOW-NOT-ESTABLISHED", MODE_CORRECTABLE, f"arrival before hardening is {_status(correction, 'arrives_before_hardening')}"))

    if MODE_AUTHORIZED in modes:
        authority = _as_dict(env.get("authority"), "authority")
        if not _nonempty_str(authority, "authority_ref"):
            findings.append(Finding("PREFLIGHT-AUTHORITY-REF-MISSING", MODE_AUTHORIZED, "AUTHORIZED claim requires a declared authority/grant reference"))
        if not _nonempty_str(authority, "scope_ref"):
            findings.append(Finding("PREFLIGHT-AUTHORITY-SCOPE-MISSING", MODE_AUTHORIZED, "AUTHORIZED claim requires a declared scope/action-class reference"))
        if _status(authority, "current_applicability") != "YES":
            findings.append(Finding("PREFLIGHT-AUTHORITY-NOT-CURRENT", MODE_AUTHORIZED, f"authority current applicability is {_status(authority, 'current_applicability')}"))
        if authority.get("capability_only") is True:
            findings.append(Finding("PREFLIGHT-CAPABILITY-NOT-AUTHORITY", MODE_AUTHORIZED, "capability evidence cannot substitute for an authority/grant basis"))

    gaps = [item for item in findings if item.severity == "GAP"]
    notices = [item for item in findings if item.severity == "NOTICE"]
    if gaps:
        status = "STRUCTURAL_GAP"
    elif notices:
        status = "MODE_DECLARATION_CHALLENGED"
    elif not modes:
        status = "NOT_APPLICABLE"
    else:
        status = "DECLARED_SUPPORT_FIELDS_PRESENT"

    return PreflightResult(fixture_id, status, modes, sentinels, findings)


def main() -> int:
    parser = argparse.ArgumentParser(description=CANDIDATE_ID)
    parser.add_argument("path", help="JSON preflight envelope")
    parser.add_argument("--json", action="store_true", help="emit JSON")
    args = parser.parse_args()

    try:
        with open(args.path, encoding="utf-8") as handle:
            envelope = json.load(handle)
        result = check_preflight(envelope).to_dict()
    except (OSError, json.JSONDecodeError, PreflightInputError) as exc:
        payload = {
            "candidate_id": CANDIDATE_ID,
            "status": "INPUT_ERROR",
            "error": str(exc),
            "epistemic_limit": EPISTEMIC_LIMIT,
        }
        print(json.dumps(payload, indent=2) if args.json else f"INPUT_ERROR: {exc}")
        return 2

    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(f"{result['fixture_id']}: {result['status']}")
        for finding in result["findings"]:
            print(f"  {finding['severity']} {finding['code']}: {finding['message']}")
        print("  limit: " + result["epistemic_limit"])

    return 1 if result["status"] in {"STRUCTURAL_GAP", "MODE_DECLARATION_CHALLENGED"} else 0


if __name__ == "__main__":
    raise SystemExit(main())
