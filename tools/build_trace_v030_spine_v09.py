#!/usr/bin/env python3
"""Build TRACE v0.3.0 spine candidate v0.9 deterministically from v0.8.

v0.9 restores only donor invariants I11 and I48 after the semantic-disposition
hostile attack: route existence != route usability, and advantage claims require
a measure. No other semantic or schema change is permitted by this compiler.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
BASE_PATH = REPO_ROOT / "PROJECT" / "TRACE_v0_3_0_SPINE_CANDIDATE_v0_8.md"
OUTPUT_PATH = REPO_ROOT / "PROJECT" / "TRACE_v0_3_0_SPINE_CANDIDATE_v0_9.md"

OLD_HEADER = "# TRACE // v0.3.0 SPINE CANDIDATE v0.8"
NEW_HEADER = "# TRACE // v0.3.0 SPINE CANDIDATE v0.9"

OLD_ROUTE_BLOCK = """```text
CAUSES != CORRELATES
CONTROL != INTENT
CONSTRAINT != CONSENT
NO_DIRECT_EDGE != NO_INDIRECT_PATH
ROUTE_LISTED != ROUTE_EXECUTABLE
REFUSAL_RECORDED != REFUSAL_EFFECTIVE
```
"""

NEW_ROUTE_BLOCK = """```text
CAUSES != CORRELATES
CONTROL != INTENT
CONSTRAINT != CONSENT
NO_DIRECT_EDGE != NO_INDIRECT_PATH
ROUTE_LISTED != ROUTE_EXECUTABLE
ROUTE_EXISTS != ROUTE_USABLE
BURDEN_PRESENT != ROUTE_UNUSABLE
REFUSAL_RECORDED != REFUSAL_EFFECTIVE
```

Route usability is scope/target-relative; access, target reach, authority, timing and burden/constraints fire only when they can change that claim.
"""

OLD_VALUE_BLOCK = """```text
STRUCTURAL_VISIBILITY != VALUE_SELECTION
DESIGNATED != MORALLY_CORRECT
MEASURED_ADVANTAGE != ENTITLEMENT
TRACE_MAP != SHOULD
DESCRIPTION != PERMISSION
```
"""

NEW_VALUE_BLOCK = """```text
STRUCTURAL_VISIBILITY != VALUE_SELECTION
DESIGNATED != MORALLY_CORRECT
ADVANTAGE_CLAIM_REQUIRES_MEASURE
MEASURED_ADVANTAGE != ENTITLEMENT
TRACE_MAP != SHOULD
DESCRIPTION != PERMISSION
```
"""

OLD_KERNEL = "Expose coupling, routes, burden, residue, future-path changes, designation and measure at the resolution evidence supports."
NEW_KERNEL = "Expose route usability, coupling, burden, residue, future-path changes, designation and comparison measure at the resolution evidence supports."


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"{label}: expected exactly one anchor, observed {count}")
    return text.replace(old, new, 1)


def compile_spine(base: str) -> str:
    text = replace_once(base, OLD_HEADER, NEW_HEADER, "header")
    text = replace_once(text, OLD_ROUTE_BLOCK, NEW_ROUTE_BLOCK, "route block")
    text = replace_once(text, OLD_VALUE_BLOCK, NEW_VALUE_BLOCK, "value block")
    text = replace_once(text, OLD_KERNEL, NEW_KERNEL, "survival-kernel exposure sentence")
    return text


def normalize_candidate(candidate: str) -> str:
    text = replace_once(candidate, NEW_HEADER, OLD_HEADER, "normalized header")
    text = replace_once(text, NEW_ROUTE_BLOCK, OLD_ROUTE_BLOCK, "normalized route block")
    text = replace_once(text, NEW_VALUE_BLOCK, OLD_VALUE_BLOCK, "normalized value block")
    text = replace_once(text, NEW_KERNEL, OLD_KERNEL, "normalized survival-kernel sentence")
    return text


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def verify(base: str, candidate: str) -> dict[str, object]:
    normalized = normalize_candidate(candidate)
    errors: list[str] = []
    if normalized != base:
        errors.append("candidate differs from v0.8 outside the four declared replacement surfaces")

    required_tokens = (
        "ROUTE_EXISTS != ROUTE_USABLE",
        "BURDEN_PRESENT != ROUTE_UNUSABLE",
        "ADVANTAGE_CLAIM_REQUIRES_MEASURE",
        "Route usability is scope/target-relative",
        "comparison measure",
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
        "declared_replacement_surfaces": 4,
        "errors": errors,
        "claim_boundary": "I11_I48_DONOR_REPAIR_ONLY_NOT_VALIDATION_NOT_RELEASE_NOT_CANON",
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
            report["errors"].append("committed v0.9 candidate differs from deterministic output")

    if report["errors"]:
        report["status"] = "FAIL"

    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.report:
        args.report.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
