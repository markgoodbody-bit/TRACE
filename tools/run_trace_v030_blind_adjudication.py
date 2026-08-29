#!/usr/bin/env python3
"""Execute the exact frozen two-family blind-adjudication manifest through Campfire.

This runner has no diagnostic, Qwen, retry, manual, direct-provider, or arm-key route.
It uses Campfire's loopback estimate -> round -> one-use call sequence and preserves
malformed/truncated adjudicator returns as adverse evidence without selective retry.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import quote

TOOLS_DIR = str(Path(__file__).resolve().parent)
if TOOLS_DIR not in sys.path:
    sys.path.insert(0, TOOLS_DIR)

import run_trace_v030_two_family_api_study as base


EXPECTED_SERVER_VERSION = "0.18.34"
EXPECTED_STUDY_ID = "TRACE-v0.3.0-BLIND-ADJUDICATION-TWO-FAMILY-20260829-v0.1"
EXPECTED_MANIFEST_SHA256 = "7539d764fa98ebfda675b2e6c0ef30878bf4793ac8af343336c2a22571515e6d"
EXPECTED_PREFLIGHT_SHA256 = "9b5ed1dc06dbb514941b1aade54541b392569abea3092031ff8bca32a04bc8b6"
EXPECTED_PACKET_SET_SHA256 = "9df5a362ca7a132ca2ceebcde12a53d0746e6a088f91b5f544613a5a6a4b4856"
EXPECTED_SEALED_KEY_SHA256 = "4c2da969d4ebb006c48964e644172244718254fe9b9b253d49d70de148075b0c"
AUTHORIZED_CAP_USD = 2.5648875
AUTHORIZATION_ID = "CODEX-THREAD-20260829-USD2_5648875-BLIND-ADJUDICATION-001"
AUTHORIZED_PROVIDERS = {"gemini": "gemini-3.6-flash", "kimi": "kimi-k3"}


def round_draft(job: dict[str, object], prompt: str) -> dict[str, object]:
    return {
        "title": f'Blind paired-analysis adjudication {job["jobId"]}',
        "prompt": prompt,
        "mode": "independent",
        "executionProfile": "standard",
        "maxOutputTokens": job["maxOutputTokens"],
        "identityRequired": False,
        "contextMode": "none",
        "targets": [
            {
                "modelId": job["providerId"],
                "presetId": job["presetId"],
                "transport": "api",
                "roleInstruction": "",
            }
        ],
    }


def extract_strict_json(raw: str) -> tuple[bool, object | None]:
    try:
        parsed = json.loads(raw)
    except Exception:
        return False, None
    return isinstance(parsed, dict), parsed


def validate_manifest(manifest: dict[str, object]) -> list[dict[str, object]]:
    if manifest.get("studyId") != EXPECTED_STUDY_ID:
        raise ValueError("adjudication study identity mismatch")
    if manifest.get("sourceBlindPacketSetIdSha256") != EXPECTED_PACKET_SET_SHA256:
        raise ValueError("blind packet set identity mismatch")
    if manifest.get("sealedArmKeySha256") != EXPECTED_SEALED_KEY_SHA256:
        raise ValueError("sealed arm-key commitment mismatch")
    if manifest.get("armKeyIncluded") is not False or manifest.get("deltaNotesIncluded") is not False:
        raise ValueError("adjudicator manifest exposes sealed material")
    jobs = sorted(manifest.get("jobs", []), key=lambda job: int(job["order"]))
    if len(jobs) != 32 or [job.get("order") for job in jobs] != list(range(1, 33)):
        raise ValueError("adjudication job cardinality/order mismatch")
    if {job.get("providerId") for job in jobs} != set(AUTHORIZED_PROVIDERS):
        raise ValueError("adjudicator family set differs from authority")
    if any(job.get("presetId") != AUTHORIZED_PROVIDERS[job["providerId"]] for job in jobs):
        raise ValueError("adjudicator model differs from authority")
    if any(job.get("arm") != "JUDGE" for job in jobs):
        raise ValueError("non-judge job present")
    if len({job.get("pairId") for job in jobs}) != 16:
        raise ValueError("expected exactly 16 blind packet identities")
    return jobs


def write_summary(
    path: Path,
    *,
    status: str,
    completed_exposure: float,
    jobs: list[dict[str, object]],
    events: list[dict[str, object]],
    failure: object | None = None,
) -> None:
    completed = [event for event in events if event.get("type") == "adjudication.completed"]
    base.exclusive_json(
        path,
        {
            "schema": "trace-v030-blind-adjudication-run-summary-v1",
            "status": status,
            "authorizationId": AUTHORIZATION_ID,
            "authorizedCap": {"amount": AUTHORIZED_CAP_USD, "currency": "USD"},
            "accountedExposureUsd": round(completed_exposure, 12),
            "remainingAuthorizedUsd": round(AUTHORIZED_CAP_USD - completed_exposure, 12),
            "plannedCalls": len(jobs),
            "completedCalls": len(completed),
            "failedCalls": sum(event.get("type") == "adjudication.failed" for event in events),
            "strictJsonReturns": sum(event.get("strictJsonParsed") is True for event in completed),
            "packetIdMatches": sum(event.get("reportedPacketIdMatches") is True for event in completed),
            "truncatedJobs": [event["jobId"] for event in completed if event.get("truncated")],
            "runtimeDriftJobs": [
                event["jobId"]
                for event in completed
                if event.get("providerReportedModel") != AUTHORIZED_PROVIDERS.get(str(event.get("providerId")))
            ],
            "failure": failure,
            "packetSetIdSha256": EXPECTED_PACKET_SET_SHA256,
            "sealedArmKeySha256": EXPECTED_SEALED_KEY_SHA256,
            "armKeyUnsealed": False,
            "claimBoundary": "ADJUDICATOR_RETURNS_PRESERVED_KEY_STILL_SEALED_NOT_AGGREGATED_NOT_EFFICACY_RESULT",
        },
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--preflight-report", type=Path, required=True)
    parser.add_argument("--base-url", default="http://127.0.0.1:4317")
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args()

    if args.execute and args.authorization_id != AUTHORIZATION_ID:
        raise ValueError("execution requires the exact blind-adjudication authorization id")
    base_url = base.local_base_url(args.base_url)
    manifest_path = args.manifest.resolve()
    preflight_path = args.preflight_report.resolve()
    manifest_bytes = manifest_path.read_bytes()
    if base.sha256(manifest_bytes) != EXPECTED_MANIFEST_SHA256:
        raise ValueError("adjudication manifest SHA-256 differs from the authorized object")
    if base.sha256(preflight_path.read_bytes()) != EXPECTED_PREFLIGHT_SHA256:
        raise ValueError("adjudication preflight SHA-256 differs from the authorized object")
    manifest = json.loads(manifest_bytes.decode("utf-8"))
    jobs = validate_manifest(manifest)

    health_status, health = base.request_json(base_url, "/api/health")
    if health_status != 200 or health.get("version") != EXPECTED_SERVER_VERSION:
        raise ValueError("Campfire runtime identity mismatch")

    planned_costs: dict[str, float] = {}
    for job in jobs:
        _, prompt = base.exact_prompt(manifest_path, job)
        status, response = base.request_json(base_url, "/api/estimate", "POST", round_draft(job, prompt))
        if status != 200:
            raise ValueError(f'{job["jobId"]}: estimate failed: HTTP {status}')
        planned_costs[str(job["jobId"])], _ = base.validate_estimate(job, response)
    planned_total = round(sum(planned_costs.values()), 12)
    if planned_total > AUTHORIZED_CAP_USD:
        raise ValueError(f"fresh aggregate ceiling {planned_total:.12f} USD exceeds authority")

    plan = {
        "schema": "trace-v030-blind-adjudication-execution-plan-v1",
        "authorizationId": AUTHORIZATION_ID,
        "manifestSha256": EXPECTED_MANIFEST_SHA256,
        "preflightReportSha256": EXPECTED_PREFLIGHT_SHA256,
        "packetSetIdSha256": EXPECTED_PACKET_SET_SHA256,
        "sealedArmKeySha256": EXPECTED_SEALED_KEY_SHA256,
        "armKeyIncluded": False,
        "serverVersion": health.get("version"),
        "capUsd": AUTHORIZED_CAP_USD,
        "plannedCeilingUsd": round(planned_total, 12),
        "remainingMarginUsd": round(AUTHORIZED_CAP_USD - planned_total, 12),
        "providers": AUTHORIZED_PROVIDERS,
        "calls": len(jobs),
        "diagnosticCalls": 0,
        "qwenCalls": 0,
        "retries": 0,
        "manualFallbacks": 0,
    }
    print(base.canonical_json({"phase": "PLAN", **plan}), end="", flush=True)
    if not args.execute:
        return 0
    if not args.output_dir:
        raise ValueError("--output-dir is required with --execute")

    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=False)
    raw_dir = output_dir / "raw"
    response_dir = output_dir / "responses"
    raw_dir.mkdir()
    response_dir.mkdir()
    ledger = output_dir / "ledger.jsonl"
    base.exclusive_json(output_dir / "authorization-and-plan.json", plan)
    events: list[dict[str, object]] = []

    def record(event: dict[str, object]) -> None:
        events.append(event)
        base.append_event(ledger, event)
        print(base.canonical_json({"phase": "EVENT", **event}), end="", flush=True)

    completed_exposure = 0.0
    remaining = dict(planned_costs)
    for job in jobs:
        prompt_bytes, prompt = base.exact_prompt(manifest_path, job)
        draft = round_draft(job, prompt)
        status, estimate_response = base.request_json(base_url, "/api/estimate", "POST", draft)
        if status != 200:
            raise RuntimeError(f'{job["jobId"]}: fresh estimate HTTP {status}')
        fresh_estimate, fingerprint = base.validate_estimate(job, estimate_response)
        remaining[str(job["jobId"])] = fresh_estimate
        projected = round(completed_exposure + sum(remaining.values()), 12)
        if projected > AUTHORIZED_CAP_USD:
            raise RuntimeError(f'{job["jobId"]}: refreshed aggregate ceiling exceeds authority')

        create_status, created = base.request_json(
            base_url,
            "/api/rounds",
            "POST",
            {**draft, "budgetConfirmation": {"confirmed": True, "fingerprint": fingerprint}},
        )
        if create_status != 201:
            raise RuntimeError(
                f'{job["jobId"]}: round creation failed {create_status}: '
                f'{created.get("code") or created.get("error")}'
            )
        session_id = str(created.get("sessionId", ""))
        round_id = str(created.get("roundId", ""))
        if not re.fullmatch(r"[A-Za-z0-9_-]+", session_id) or not re.fullmatch(r"[A-Za-z0-9_-]+", round_id):
            raise RuntimeError(f'{job["jobId"]}: unsafe/missing round identity')
        record(
            {
                "type": "adjudication.authorized",
                "jobId": job["jobId"],
                "packetId": job["promptId"],
                "caseLabel": job["caseLabel"],
                "order": job["order"],
                "providerId": job["providerId"],
                "presetId": job["presetId"],
                "promptSha256": job["promptSha256"],
                "promptBytes": len(prompt_bytes),
                "maximumEstimatedCostUsd": fresh_estimate,
                "budgetFingerprint": fingerprint,
                "sessionId": session_id,
                "roundId": round_id,
            }
        )
        route = (
            f"/api/sessions/{quote(session_id, safe='')}/rounds/{quote(round_id, safe='')}"
            f"/call/{job['providerId']}"
        )
        call_status, call = base.request_json(base_url, route, "POST", {})
        raw = str(call.get("rawResponse", ""))
        safe_record = base.safe_call_record(call)
        base.exclusive_json(response_dir / f'{int(job["order"]):02d}_{job["jobId"]}.json', safe_record)
        raw_bytes = raw.encode("utf-8") if raw else b""
        if raw_bytes:
            base.exclusive_bytes(raw_dir / f'{int(job["order"]):02d}_{job["jobId"]}.txt', raw_bytes)
        exposure = base.accounted_exposure(call, fresh_estimate)
        remaining.pop(str(job["jobId"]), None)
        completed_exposure += exposure
        strict_json, parsed = extract_strict_json(raw)
        reported_packet_id = parsed.get("packet_id") if isinstance(parsed, dict) else None
        common = {
            "jobId": job["jobId"],
            "packetId": job["promptId"],
            "caseLabel": job["caseLabel"],
            "order": job["order"],
            "providerId": job["providerId"],
            "presetId": job["presetId"],
            "sessionId": session_id,
            "roundId": round_id,
            "httpStatus": call_status,
            "maximumEstimatedCostUsd": fresh_estimate,
            "accountedExposureUsd": exposure,
            "providerReportedModel": call.get("providerReportedModel"),
            "providerFinishReason": call.get("providerFinishReason"),
            "truncated": bool(call.get("truncated")),
            "rawResponseSha256": base.sha256(raw_bytes) if raw_bytes else None,
            "rawResponseBytes": len(raw_bytes),
            "outputWords": len(re.findall(r"\b\w+\b", raw)),
            "strictJsonParsed": strict_json,
            "reportedPacketId": reported_packet_id,
            "reportedPacketIdMatches": reported_packet_id == job["promptId"],
        }
        if call_status == 200 and raw:
            record({"type": "adjudication.completed", **common})
        else:
            failure = {"code": call.get("code"), "error": call.get("error"), **common}
            record({"type": "adjudication.failed", **failure})
            write_summary(
                output_dir / "run-summary.json",
                status="STOPPED_ADJUDICATION_TRANSPORT_FAILURE",
                completed_exposure=completed_exposure,
                jobs=jobs,
                events=events,
                failure=failure,
            )
            return 3

    write_summary(
        output_dir / "run-summary.json",
        status="COMPLETE_RETURNS_KEY_SEALED",
        completed_exposure=completed_exposure,
        jobs=jobs,
        events=events,
    )
    print(
        base.canonical_json(
            {
                "phase": "COMPLETE",
                "status": "COMPLETE_RETURNS_KEY_SEALED",
                "calls": len(jobs),
                "accountedExposureUsd": round(completed_exposure, 12),
                "remainingAuthorizedUsd": round(AUTHORIZED_CAP_USD - completed_exposure, 12),
            }
        ),
        end="",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(
            base.canonical_json(
                {
                    "phase": "FATAL",
                    "status": "STOPPED_FAIL_CLOSED",
                    "error": str(error),
                    "providerRetryAttempted": False,
                    "qwenContacted": False,
                    "armKeyUnsealed": False,
                }
            ),
            end="",
            file=sys.stderr,
            flush=True,
        )
        raise
