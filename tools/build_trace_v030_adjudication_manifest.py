#!/usr/bin/env python3
"""Build a no-authority Campfire estimate manifest for frozen blind packets."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


PROVIDERS = (
    ("gemini", "gemini-3.6-flash", "GEMINI_GOOGLE"),
    ("kimi", "kimi-k3", "KIMI_MOONSHOT"),
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def exclusive_text(path: Path, text: str) -> None:
    with path.open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--public-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--max-output-tokens", type=int, default=6000)
    args = parser.parse_args()

    public_dir = args.public_dir.resolve()
    output_dir = args.output_dir.resolve()
    if output_dir.exists():
        raise FileExistsError(f"output directory exists: {output_dir}")
    if args.max_output_tokens < 1000 or args.max_output_tokens > 8000:
        raise ValueError("max output tokens must be between 1000 and 8000")

    public_manifest_path = public_dir / "public-manifest.json"
    public_manifest_bytes = public_manifest_path.read_bytes()
    public_manifest = read_json(public_manifest_path)
    if public_manifest.get("schema") != "trace-v030-blind-adjudication-public-manifest-v1":
        raise ValueError("unsupported blind-packet manifest")
    if public_manifest.get("armKeyIncluded") is not False:
        raise ValueError("public packet set claims to include an arm key")

    output_dir.mkdir(parents=True)
    prompts_dir = output_dir / "prompts"
    prompts_dir.mkdir()
    jobs: list[dict[str, Any]] = []
    order = 0
    for packet in sorted(public_manifest.get("packets", []), key=lambda item: item["packetId"]):
        packet_id = str(packet["packetId"])
        packet_path = public_dir / str(packet["file"])
        packet_bytes = packet_path.read_bytes()
        if sha256(packet_bytes) != packet.get("sha256") or len(packet_bytes) != packet.get("bytes"):
            raise ValueError(f"public packet identity mismatch: {packet_id}")
        prompt_text = packet_bytes.decode("utf-8").strip()
        if not prompt_text:
            raise ValueError(f"empty packet: {packet_id}")
        prompt_bytes = prompt_text.encode("utf-8")
        prompt_name = f"{packet_id}.txt"
        exclusive_text(prompts_dir / prompt_name, prompt_text)
        for provider_id, preset_id, family_id in PROVIDERS:
            order += 1
            jobs.append(
                {
                    "order": order,
                    "jobId": f"{packet_id}__ADJUDICATOR_{family_id}__ATTEMPT_1",
                    "pairId": f"{packet_id}__ADJUDICATION",
                    "arm": "JUDGE",
                    "caseLabel": packet["caseId"],
                    "pairAttempt": 1,
                    "promptId": packet_id,
                    "promptPath": f"prompts/{prompt_name}",
                    "promptBytes": len(prompt_bytes),
                    "promptSha256": sha256(prompt_bytes),
                    "providerId": provider_id,
                    "presetId": preset_id,
                    "receiverFamilyId": family_id,
                    "visibleAnswerTokens": args.max_output_tokens,
                    "maxOutputTokens": args.max_output_tokens,
                    "identityRequired": False,
                    "contextMode": "none",
                    "roleInstruction": "",
                }
            )

    manifest = {
        "schema": "campfire-exact-input-study-v1",
        "studyId": "TRACE-v0.3.0-BLIND-ADJUDICATION-TWO-FAMILY-20260829-v0.1",
        "canonicalText": "utf8-no-leading-or-trailing-whitespace",
        "claimBoundary": "ADJUDICATION_PREFLIGHT_CANDIDATE_NOT_AUTHORIZATION_NOT_DISPATCH_NOT_RESULT",
        "sourceBlindPacketManifestSha256": sha256(public_manifest_bytes),
        "sourceBlindPacketSetIdSha256": public_manifest["packetSetIdSha256"],
        "sealedArmKeySha256": public_manifest["sealedArmKeySha256"],
        "armKeyIncluded": False,
        "deltaNotesIncluded": False,
        "adjudicatorFamilies": [family for _, _, family in PROVIDERS],
        "jobs": jobs,
    }
    manifest_path = output_dir / "campfire-adjudication-manifest.json"
    exclusive_text(manifest_path, json.dumps(manifest, indent=2, ensure_ascii=False, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "manifest": str(manifest_path),
                "manifestSha256": sha256(manifest_path.read_bytes()),
                "jobs": len(jobs),
                "maxOutputTokens": args.max_output_tokens,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
