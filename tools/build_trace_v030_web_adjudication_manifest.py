#!/usr/bin/env python3
"""Build a no-dispatch browser manifest for frozen TRACE blind packets."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


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
    parser.add_argument(
        "--study-id",
        default="TRACE-v0.3.0-BLIND-ADJUDICATION-GEMINI-API-PLUS-GROK-WEB-20260829-v0.4",
    )
    args = parser.parse_args()

    public_dir = args.public_dir.resolve()
    output_dir = args.output_dir.resolve()
    if output_dir.exists():
        raise FileExistsError(f"output directory exists: {output_dir}")

    public_manifest_path = public_dir / "public-manifest.json"
    public_manifest_bytes = public_manifest_path.read_bytes()
    public_manifest = read_json(public_manifest_path)
    if public_manifest.get("schema") != "trace-v030-blind-adjudication-public-manifest-v1":
        raise ValueError("unsupported blind-packet manifest")
    if public_manifest.get("armKeyIncluded") is not False:
        raise ValueError("public packet set claims to include an arm key")
    if public_manifest.get("deltaNotesIncluded") is not False:
        raise ValueError("public packet set claims to include provenance notes")

    output_dir.mkdir(parents=True)
    prompts_dir = output_dir / "prompts"
    prompts_dir.mkdir()
    jobs: list[dict[str, Any]] = []
    for order, packet in enumerate(
        sorted(public_manifest.get("packets", []), key=lambda item: item["packetId"]), start=1
    ):
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
        jobs.append(
            {
                "order": order,
                "jobId": f"{packet_id}__ADJUDICATOR_GROK_WEB_GUEST_FAST__ATTEMPT_1",
                "packetId": packet_id,
                "caseLabel": packet["caseId"],
                "promptPath": f"prompts/{prompt_name}",
                "promptBytes": len(prompt_bytes),
                "promptSha256": sha256(prompt_bytes),
                "providerFamily": "XAI_GROK",
                "service": "grok.com",
                "transport": "browser",
                "accountMode": "SIGNED_OUT_GUEST",
                "visibleModeLabel": "Fast",
                "backendModelIdentity": "UNKNOWN_NOT_DISCLOSED_BY_UI",
                "freshChatRequired": True,
                "externalSearchAllowed": False,
                "retryCount": 0,
            }
        )

    if len(jobs) != 16:
        raise ValueError(f"expected 16 packets, observed {len(jobs)}")

    manifest = {
        "schema": "trace-v030-browser-adjudication-manifest-v1",
        "studyId": args.study_id,
        "claimBoundary": "BROWSER_ROUTE_FROZEN_NOT_DISPATCH_NOT_RETURN_NOT_EFFICACY_RESULT",
        "sourceBlindPacketManifestSha256": sha256(public_manifest_bytes),
        "sourceBlindPacketSetIdSha256": public_manifest["packetSetIdSha256"],
        "sealedArmKeySha256": public_manifest["sealedArmKeySha256"],
        "armKeyIncluded": False,
        "deltaNotesIncluded": False,
        "dispatchPolicy": "GROK_WEB_FIRST_FAIL_FAST_THEN_GEMINI_API",
        "capturePolicy": "PRESERVE_VISIBLE_PAGE_EXPORT_AND_SESSION_URL_BEFORE_NEXT_PACKET",
        "identityLimit": "SERVICE_AND_VISIBLE_MODE_ONLY_BACKEND_MODEL_UNDISCLOSED",
        "jobs": jobs,
    }
    manifest_path = output_dir / "browser-grok-adjudication-manifest.json"
    exclusive_text(manifest_path, json.dumps(manifest, indent=2, ensure_ascii=False, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "manifest": str(manifest_path),
                "manifestSha256": sha256(manifest_path.read_bytes()),
                "jobs": len(jobs),
                "service": "grok.com",
                "visibleModeLabel": "Fast",
                "backendModelIdentity": "UNKNOWN_NOT_DISCLOSED_BY_UI",
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
