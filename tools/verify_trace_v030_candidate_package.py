#!/usr/bin/env python3
"""Verify the bounded TRACE v0.3.0 candidate package.

This checks exact artifact identities, JSON readability, public-archive naming,
and a small set of status ceilings. It does not validate TRACE or reproduce the
full historical build quarry.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from io import BytesIO
from pathlib import Path
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]

EXPECTED = {
    "work/v0_3_0/candidate/TRACE_v0_3_0_SPINE_CANDIDATE_v0_11.md": (25355, "de35637f1a6db1648f725db0e533c4b4f8e2eb1f40c817ed24de9039e1525084"),
    "work/v0_3_0/candidate/TRACE_FORMAL_SEED_v0_3_0_FULL_WORKING_CANDIDATE_v0_1.md": (179731, "32409ee8d91e9c4bc67ecbb2359cc7d1c68249cab457511a50e586733ee7598a"),
    "work/v0_3_0/candidate/TRACE_v0_3_0_MINIMUM_SCHEMA_CANDIDATE_v0_1.json": (22774, "d50ad1e82bc5935d99c9994bdc9a3ac7c22d5f5c5ddcd1e2efc813fd8ce9a24b"),
    "work/v0_3_0/candidate/TRACE_v0_3_0_BUILD_BRIEF.md": (8927, "17e89c7ac3ee79d9fb6417eb8c4ae7ef2cb0170b710f27c2d67bb54b422f4e98"),
    "work/v0_3_0/evidence/TRACE_v0_3_0_READINESS_AUDIT_20260829_v0_1.md": (3525, "51a70ac5b9ec27a8cfaf3285a236113c63b4b9c155a9ab7aa06ed32d23086bca"),
    "work/v0_3_0/evidence/TRACE_v0_3_0_FPF_NEAREST_NEIGHBOUR_DISPOSITION_20260828_v0_1.md": (5091, "c8a1fc08049a77ed58466533d27143878a9a00a481de83630aec9a9a3b674def"),
    "work/v0_3_0/evidence/TRACE_v0_3_0_FPF_NEAREST_NEIGHBOUR_CROSSWALK_v0_1.md": (28783, "6513dd47cd304e718672cff82fca1a6ec27e58c2026346d2fe7b3a0262346ffc"),
    "work/v0_3_0/evidence/TRACE_v0_3_0_OUTWARD_API_EXECUTION_RESULT_20260829_v0_2.md": (6372, "38f6005a4f224abea7a285d602cd9ab75b21d7d4586118085db58bcc8c2c8e6a"),
    "work/v0_3_0/evidence/TRACE_v0_3_0_BLIND_ADJUDICATION_API_RESULT_20260829_v0_4.md": (2139, "2ff542803216c6e03aac99e4cb2f87b96ad36e3554c979c25e533b27c868874d"),
    "work/v0_3_0/evidence/TRACE_v0_2_8_TO_v0_3_0_LINEAGE_RECONCILIATION_20260829_v0_1.md": (4769, "1a9c9ca673b29a9ae7f5a94b160fafc18fa11f969fe2124c80a43735d20fbe1a"),
    "work/v0_3_0/evidence/TRACE_v0_2_7_TO_v0_3_0_DONOR_MAP_v0_1.md": (12781, "735d77c2081f2697917b20622a0724e438bc319bfe9c47a70fadd693d3e0eede"),
    "work/v0_3_0/evidence/TRACE_v0_3_0_FULL_CANDIDATE_BUILD_REPORT_v0_1.json": (18277, "b966cd3da115315565c952ddaf184e531359921b4db381b48a18a069499a400a"),
    "work/v0_3_0/evidence/TRACE_v0_3_0_FULL_CANDIDATE_TRANSFORMATION_MANIFEST_v0_2.md": (6141, "b15557bed9857968eb2274c6d5843328ba7c34c6a15c5aac772d55e57f0481e9"),
    "work/v0_3_0/evidence/TRACE_v0_3_0_MINIMUM_SCHEMA_BUILD_REPORT_v0_1.json": (1281, "3c960e6903f44ccada0289d5de1d476d62c835b526b79344f55b5ca5401b27a2"),
    "work/v0_3_0/evidence/TRACE_v0_3_0_INVARIANT_LEXICAL_COVERAGE_v0_4.json": (14314, "6d49e8499c5ec55af99ad48e61c1f7280fd16081b6034848e39ca95b564e5bf5"),
    "work/v0_3_0/evidence/TRACE_v0_3_0_INVARIANT_SEMANTIC_DISPOSITION_v0_2.md": (9701, "a697f552bced6cf046a23c0a6a368f891f5b5fa61dd235941435a0eca67e0c4b"),
    "work/v0_3_0/artifacts/TRACE-v0.3.0-blind-adjudication-public-20260829-v0.1.zip": (141979, "6813717cc10bf321741c978ddb45c91ef5579ad2017c44a8cd9f0f56560948c5"),
}

REQUIRED_TEXT = {
    "work/v0_3_0/candidate/TRACE_v0_3_0_SPINE_CANDIDATE_v0_11.md": ("WORKING SPINE", "NOT VALIDATED"),
    "work/v0_3_0/candidate/TRACE_FORMAL_SEED_v0_3_0_FULL_WORKING_CANDIDATE_v0_1.md": ("FULL WORKING CANDIDATE v0.1",),
    "work/v0_3_0/evidence/TRACE_v0_3_0_READINESS_AUDIT_20260829_v0_1.md": ("NOT EFFICACY RESULT", "No efficacy disposition exists."),
    "work/v0_3_0/evidence/TRACE_v0_3_0_FPF_NEAREST_NEIGHBOUR_DISPOSITION_20260828_v0_1.md": ("ESTABLISHED TRACE-UNIQUE SEMANTIC PRIMITIVES IN THIS PASS: 0",),
    "work/v0_3_0/evidence/TRACE_v0_3_0_OUTWARD_API_EXECUTION_RESULT_20260829_v0_2.md": ("is not an efficacy disposition",),
    "work/v0_3_0/evidence/TRACE_v0_3_0_BLIND_ADJUDICATION_API_RESULT_20260829_v0_4.md": ("arm key unsealed = NO",),
    "work/v0_3_0/QUARRY_POINTER.md": ("8635438c7d5cd600dd2c8d50322353e59d27b70e", "ARTIFACT_IDENTITY_CHECK != FULL_REBUILD"),
    "work/v0_3_0/evidence/TRACE_v0_3_0_REPOSITORY_IDENTITY_CORRECTION_20260829_v0_1.md": ("REPOSITORY_OBJECT_IDENTITY", "WORKING_TREE_SNAPSHOT_IDENTITY"),
}


def repository_bytes(relative: str) -> bytes:
    """Read the indexed Git blob, falling back only outside an indexed checkout.

    Exact package identities refer to repository objects. Reading the working
    file directly would make text identities depend on checkout line endings.
    """
    try:
        return subprocess.check_output(
            ["git", "show", f":{relative}"],
            cwd=ROOT,
            stderr=subprocess.DEVNULL,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return (ROOT / relative).read_bytes()


def main() -> int:
    errors: list[str] = []

    for relative, (expected_bytes, expected_sha) in EXPECTED.items():
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"missing: {relative}")
            continue
        data = repository_bytes(relative)
        actual_bytes = len(data)
        actual_sha = hashlib.sha256(data).hexdigest()
        if actual_bytes != expected_bytes:
            errors.append(f"byte mismatch: {relative}: {actual_bytes} != {expected_bytes}")
        if actual_sha != expected_sha:
            errors.append(f"sha256 mismatch: {relative}: {actual_sha} != {expected_sha}")
        if path.suffix == ".json":
            try:
                json.loads(data.decode("utf-8"))
            except (UnicodeDecodeError, json.JSONDecodeError) as exc:
                errors.append(f"invalid JSON: {relative}: {exc}")

    for relative, markers in REQUIRED_TEXT.items():
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"missing marker surface: {relative}")
            continue
        text = repository_bytes(relative).decode("utf-8")
        for marker in markers:
            if marker not in text:
                errors.append(f"missing marker in {relative}: {marker}")

    archive = ROOT / "work/v0_3_0/artifacts/TRACE-v0.3.0-blind-adjudication-public-20260829-v0.1.zip"
    if archive.is_file():
        archive_data = repository_bytes("work/v0_3_0/artifacts/TRACE-v0.3.0-blind-adjudication-public-20260829-v0.1.zip")
        with ZipFile(BytesIO(archive_data)) as handle:
            lowered = [name.lower() for name in handle.namelist()]
        for forbidden in ("arm_key", "expected_result", "expected-result"):
            if any(forbidden in name for name in lowered):
                errors.append(f"public archive exposes forbidden filename marker: {forbidden}")

    if errors:
        print("TRACE v0.3.0 candidate package verification: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("TRACE v0.3.0 candidate package verification: PASS")
    print(f"- exact indexed repository objects: {len(EXPECTED)}")
    print("- selected JSON objects: readable")
    print("- status and claim ceilings: present")
    print("- public archive filename boundary: present")
    print("This verifies package identity and declared boundaries only; it does not validate TRACE or establish efficacy.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
