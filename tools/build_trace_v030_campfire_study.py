#!/usr/bin/env python3
"""Build the non-dispatch Campfire exact-input manifest for TRACE v0.3.0.

This adapter consumes the already-frozen primary prompt manifest and an emitted
prompt directory. It does not contact a provider, authorize spend, or dispatch.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_MANIFEST = REPO_ROOT / "PROJECT" / "TRACE_v0_3_0_OUTWARD_PRIMARY_PROMPT_MANIFEST_v0_1.json"

RECEIVERS = {
    "GEMINI_GOOGLE": {"providerId": "gemini", "presetId": "gemini-3.6-flash"},
    "QWEN_ALIBABA": {"providerId": "qwen", "presetId": "qwen3.7-plus-us"},
    "KIMI_MOONSHOT": {"providerId": "kimi", "presetId": "kimi-k3"},
}

MAX_OUTPUT_TOKENS = 8000


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_json(value: object) -> str:
    return json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def build(prompt_dir: Path, output_path: Path) -> dict[str, object]:
    source_bytes = SOURCE_MANIFEST.read_bytes()
    source = json.loads(source_bytes.decode("utf-8"))
    prompt_rows = {row["prompt_id"]: row for row in source["prompts"]}
    jobs = []
    ordinal = 0

    for pair in source["pairs"]:
        receiver = RECEIVERS[pair["receiver_family_id"]]
        arm_order = ("A", "T") if pair["order"] == "A_FIRST" else ("T", "A")
        for arm in arm_order:
            ordinal += 1
            prompt_id = pair[f"{arm.lower()}_prompt_id"]
            prompt_row = prompt_rows[prompt_id]
            prompt_path = (prompt_dir / f"{prompt_id}.txt").resolve()
            prompt_bytes = prompt_path.read_bytes()
            if len(prompt_bytes) != prompt_row["bytes"]:
                raise ValueError(f"{prompt_id}: byte count drift")
            if sha256(prompt_bytes) != prompt_row["sha256"]:
                raise ValueError(f"{prompt_id}: SHA-256 drift")
            try:
                prompt_bytes.decode("utf-8")
            except UnicodeDecodeError as error:
                raise ValueError(f"{prompt_id}: not UTF-8") from error
            if prompt_bytes.startswith(b"\xef\xbb\xbf") or b"\r" in prompt_bytes:
                raise ValueError(f"{prompt_id}: canonical text drift")

            jobs.append(
                {
                    "arm": arm,
                    "caseLabel": pair["case_label"],
                    "contextMode": "none",
                    "identityRequired": False,
                    "jobId": f'{pair["case_label"]}__{pair["receiver_family_id"]}__{arm}__ATTEMPT_{pair["pair_attempt"]}',
                    "maxOutputTokens": MAX_OUTPUT_TOKENS,
                    "order": ordinal,
                    "pairAttempt": pair["pair_attempt"],
                    "pairId": f'{pair["case_label"]}__{pair["receiver_family_id"]}__ATTEMPT_{pair["pair_attempt"]}',
                    "presetId": receiver["presetId"],
                    "promptBytes": prompt_row["bytes"],
                    "promptId": prompt_id,
                    "promptPath": prompt_path.relative_to(output_path.parent.resolve()).as_posix(),
                    "promptSha256": prompt_row["sha256"],
                    "providerId": receiver["providerId"],
                    "receiverFamilyId": pair["receiver_family_id"],
                    "roleInstruction": "",
                    "visibleAnswerTokens": MAX_OUTPUT_TOKENS,
                }
            )

    return {
        "schema": "campfire-exact-input-study-v1",
        "studyId": "TRACE-V0.3.0-PRIMARY-API-PREFLIGHT-CANDIDATE-V0.1",
        "canonicalText": "utf8-lf-no-bom",
        "claimBoundary": "CANDIDATE_TRANSPORT_PREFLIGHT_NOT_PROTOCOL_ADOPTION_NOT_AUTHORIZATION_NOT_DISPATCH_NOT_RECEIVER_EVIDENCE",
        "maxOutputTokens": MAX_OUTPUT_TOKENS,
        "sourcePromptManifest": {
            "path": SOURCE_MANIFEST.relative_to(REPO_ROOT).as_posix(),
            "sha256": sha256(source_bytes),
        },
        "receiverCandidate": RECEIVERS,
        "jobs": jobs,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    manifest = build(args.prompt_dir.resolve(), output)
    output.write_text(canonical_json(manifest), encoding="utf-8", newline="\n")
    print(
        canonical_json(
            {
                "dispatch_performed": False,
                "jobs": len(manifest["jobs"]),
                "output": str(output),
                "sha256": sha256(output.read_bytes()),
                "status": "PASS_BUILD_ONLY",
            }
        ),
        end="",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
