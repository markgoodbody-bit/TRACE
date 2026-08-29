#!/usr/bin/env python3
"""Execute the bounded TRACE v0.3.0 Gemini/Kimi primary study through Campfire.

The runner is intentionally specific. It admits no Qwen route, no retry route,
no manual route, and no direct provider URL. Every paid call goes through the
loopback Campfire server's estimate -> round -> one-use call sequence.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import re
import sys
from urllib.error import HTTPError
from urllib.parse import quote, urlparse
from urllib.request import HTTPRedirectHandler, Request, build_opener


EXPECTED_SERVER_VERSION = "0.18.33"
EXPECTED_STUDY_ID = "TRACE-V0.3.0-PRIMARY-API-PREFLIGHT-CANDIDATE-V0.2-TWO-FAMILY"
EXPECTED_MANIFEST_SHA256 = "5b2ea0e916409d9283991bee4e55d2ca5be5af7bea99c5801562aa5889ae1eab"
EXPECTED_PREFLIGHT_SHA256 = "0b5dfd21d799c8268f3bb5ddea2a6dbdebc6de7eeabdcd1edd248c858afeada1"
AUTHORIZED_PROVIDERS = {"gemini": "gemini-3.6-flash", "kimi": "kimi-k3"}
EMPTY_SHA256 = hashlib.sha256(b"").hexdigest()
CONNECTION_PROMPT = "Return exactly: CAMPFIRE_CONNECTION_OK"
AUTHORIZATION_ID = "CODEX-THREAD-20260829-USD4-GEMINI-KIMI-001"


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):  # noqa: N802
        return None


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_json(value: object) -> str:
    return json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def local_base_url(value: str) -> str:
    parsed = urlparse(value)
    if parsed.scheme != "http" or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}:
        raise ValueError("Campfire base URL must be loopback HTTP")
    if parsed.path not in {"", "/"} or parsed.query or parsed.fragment:
        raise ValueError("Campfire base URL must not include a path, query or fragment")
    return value.rstrip("/")


def admitted_route(route: str, method: str) -> bool:
    static = {
        ("/api/health", "GET"),
        ("/api/models", "GET"),
        ("/api/estimate", "POST"),
        ("/api/connections/gemini", "POST"),
        ("/api/connections/gemini/test", "POST"),
        ("/api/connections/kimi/test", "POST"),
        ("/api/rounds", "POST"),
    }
    if (route, method) in static:
        return True
    return bool(
        method == "POST"
        and re.fullmatch(
            r"/api/sessions/[A-Za-z0-9_-]+/rounds/[A-Za-z0-9_-]+/call/(gemini|kimi)",
            route,
        )
    )


def request_json(base_url: str, route: str, method: str = "GET", body: object | None = None) -> tuple[int, dict[str, object]]:
    method = method.upper()
    if not admitted_route(route, method):
        raise ValueError(f"route not admitted: {method} {route}")
    data = None if body is None else json.dumps(body, ensure_ascii=False).encode("utf-8")
    request = Request(
        f"{base_url}{route}",
        data=data,
        method=method,
        headers={"Content-Type": "application/json; charset=utf-8"},
    )
    opener = build_opener(NoRedirect)
    try:
        response = opener.open(request, timeout=180)
    except HTTPError as error:
        raw = error.read()
        try:
            parsed = json.loads(raw.decode("utf-8"))
        except Exception:
            parsed = {"error": raw.decode("utf-8", errors="replace")[:1000]}
        return error.code, parsed
    with response:
        final = urlparse(response.geturl())
        if final.hostname not in {"127.0.0.1", "localhost", "::1"} or final.path != route:
            raise ValueError("Campfire request escaped the admitted loopback route")
        return response.status, json.loads(response.read().decode("utf-8"))


def append_event(ledger: Path, event: dict[str, object]) -> None:
    line = json.dumps(event, sort_keys=True, ensure_ascii=False, separators=(",", ":")) + "\n"
    with ledger.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(line)
        handle.flush()
        os.fsync(handle.fileno())


def exclusive_bytes(path: Path, data: bytes) -> None:
    with path.open("xb") as handle:
        handle.write(data)
        handle.flush()
        os.fsync(handle.fileno())


def exclusive_json(path: Path, value: object) -> None:
    exclusive_bytes(path, canonical_json(value).encode("utf-8"))


def exact_prompt(manifest_path: Path, job: dict[str, object]) -> tuple[bytes, str]:
    prompt_path = (manifest_path.parent / str(job["promptPath"])).resolve()
    data = prompt_path.read_bytes()
    if sha256(data) != job["promptSha256"] or len(data) != job["promptBytes"]:
        raise ValueError(f'{job["jobId"]}: prompt identity drift')
    text = data.decode("utf-8")
    if text != text.strip():
        raise ValueError(f'{job["jobId"]}: Campfire trim would change the prompt')
    return data, text


def round_draft(job: dict[str, object], prompt: str) -> dict[str, object]:
    return {
        "title": f'TRACE primary {job["jobId"]}',
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


def validate_estimate(job: dict[str, object], response: dict[str, object]) -> tuple[float, str]:
    estimates = response.get("estimates", [])
    if len(estimates) != 1:
        raise ValueError(f'{job["jobId"]}: server estimate cardinality')
    estimate = estimates[0]
    checks = {
        "provider": estimate.get("modelId") == job["providerId"],
        "preset": estimate.get("presetId") == job["presetId"],
        "api": estimate.get("transport") == "api",
        "fallback": not bool(estimate.get("fallbackReason")),
        "input": estimate.get("effectiveInputSha256") == job["promptSha256"],
        "context": estimate.get("contextSha256") == EMPTY_SHA256,
        "role": estimate.get("roleInstructionSha256") == EMPTY_SHA256,
        "identity": estimate.get("dispatchBasis", {}).get("identityRequired") is False,
        "visible": estimate.get("visibleAnswerTokens") == job["visibleAnswerTokens"],
        "transportTokens": estimate.get("transportMaxOutputTokens") == job["maxOutputTokens"],
        "billingTokens": estimate.get("billingOutputCeilingTokens") == job["maxOutputTokens"],
        "oneCall": response.get("budgetPreflight", {}).get("plannedCallCount") == 1,
    }
    failed = [name for name, passed in checks.items() if not passed]
    if failed:
        raise ValueError(f'{job["jobId"]}: estimate contract failed: {failed}')
    cost = estimate.get("estimate") or {}
    currency = str(cost.get("currency", ""))
    amount = cost.get("maximumEstimatedCost")
    if currency != "USD" or not isinstance(amount, (int, float)) or amount < 0:
        raise ValueError(f'{job["jobId"]}: non-USD or missing maximum estimate')
    fingerprint = str(response.get("budgetConfirmation", {}).get("fingerprint", ""))
    if not re.fullmatch(r"[a-f0-9]{64}", fingerprint):
        raise ValueError(f'{job["jobId"]}: missing exact budget fingerprint')
    return float(amount), fingerprint


def public_model(models_response: dict[str, object], provider_id: str) -> dict[str, object]:
    matches = [model for model in models_response.get("models", []) if model.get("id") == provider_id]
    if len(matches) != 1:
        raise ValueError(f"public model cardinality for {provider_id}")
    return matches[0]


def connection_ceiling(models_response: dict[str, object], provider_id: str) -> float:
    model = public_model(models_response, provider_id)
    preset_id = AUTHORIZED_PROVIDERS[provider_id]
    preset = next((item for item in model.get("setupPresets", []) if item.get("id") == preset_id), None)
    if not preset:
        raise ValueError(f"missing connection preset {provider_id}/{preset_id}")
    input_rate = float(preset.get("inputPricePerMillion", 0))
    output_rate = float(preset.get("outputPricePerMillion", 0))
    if input_rate <= 0 or output_rate <= 0 or str(preset.get("priceCurrency", "")) != "USD":
        raise ValueError(f"unknown/non-USD connection pricing for {provider_id}")
    input_tokens = max(1, math.ceil(len(CONNECTION_PROMPT) / 4))
    output_tokens = 768 if provider_id == "kimi" else 128
    return (input_tokens * input_rate + output_tokens * output_rate) / 1_000_000


def safe_call_record(response: dict[str, object]) -> dict[str, object]:
    keys = [
        "timestamp", "durationMs", "connectorResponseId", "connectorRequestId",
        "providerReportedModel", "providerFinishReason", "truncated", "usage", "actualCost",
        "billingOutputCeilingTokens", "costAccounting", "unconfirmedCostCeiling",
        "normalizedUsageV2", "postRunAccounting", "spendFeedback", "reserveOverrun",
    ]
    return {key: response.get(key) for key in keys if key in response}


def accounted_exposure(response: dict[str, object], estimate: float) -> float:
    actual = response.get("actualCost")
    if isinstance(actual, dict) and actual.get("currency") == "USD" and isinstance(actual.get("amount"), (int, float)):
        return max(0.0, float(actual["amount"]))
    ceiling = response.get("unconfirmedCostCeiling")
    if isinstance(ceiling, dict) and ceiling.get("currency") == "USD" and isinstance(ceiling.get("amount"), (int, float)):
        return max(0.0, float(ceiling["amount"]))
    return estimate


def write_summary(path: Path, *, status: str, cap: float, connection_reserve: float,
                  completed_exposure: float, jobs: list[dict[str, object]],
                  events: list[dict[str, object]], failure: object | None = None) -> None:
    pair_models: dict[str, list[str]] = {}
    for event in events:
        if event.get("type") != "primary.completed":
            continue
        pair_models.setdefault(str(event["pairId"]), []).append(str(event.get("providerReportedModel") or ""))
    runtime_drift_pairs = [
        pair_id for pair_id, models in pair_models.items()
        if len(models) == 2 and len(set(models)) != 1
    ]
    summary = {
        "schema": "trace-v030-two-family-api-run-summary-v1",
        "status": status,
        "authorizationId": AUTHORIZATION_ID,
        "authorizedCap": {"amount": cap, "currency": "USD"},
        "connectionReserveUsd": connection_reserve,
        "completedOrReservedExposureUsd": round(connection_reserve + completed_exposure, 12),
        "remainingAuthorizedUsd": round(cap - connection_reserve - completed_exposure, 12),
        "plannedPrimaryCalls": len(jobs),
        "completedPrimaryCalls": sum(event.get("type") == "primary.completed" for event in events),
        "failedPrimaryCalls": sum(event.get("type") == "primary.failed" for event in events),
        "runtimeDriftPairs": runtime_drift_pairs,
        "overWordLimitJobs": [event["jobId"] for event in events if event.get("type") == "primary.completed" and event.get("over1200Words")],
        "truncatedJobs": [event["jobId"] for event in events if event.get("type") == "primary.completed" and event.get("truncated")],
        "failure": failure,
        "claimBoundary": "EXECUTED_PROVIDER_EVIDENCE_NOT_ADJUDICATED_NOT_EFFICACY_RESULT_NOT_VALIDATION",
    }
    exclusive_json(path, summary)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--preflight-report", type=Path, required=True)
    parser.add_argument("--base-url", default="http://127.0.0.1:4317")
    parser.add_argument("--cap-usd", type=float, required=True)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args()

    if args.cap_usd <= 0 or args.cap_usd > 4.0:
        raise ValueError("cap must be positive and cannot exceed the authorized 4.00 USD")
    base_url = local_base_url(args.base_url)
    manifest_path = args.manifest.resolve()
    preflight_path = args.preflight_report.resolve()
    manifest_bytes = manifest_path.read_bytes()
    if sha256(manifest_bytes) != EXPECTED_MANIFEST_SHA256:
        raise ValueError("manifest SHA-256 differs from the authorized object")
    if sha256(preflight_path.read_bytes()) != EXPECTED_PREFLIGHT_SHA256:
        raise ValueError("server-preflight SHA-256 differs from the authorized object")
    manifest = json.loads(manifest_bytes.decode("utf-8"))
    jobs = sorted(manifest.get("jobs", []), key=lambda job: int(job["order"]))
    if manifest.get("studyId") != EXPECTED_STUDY_ID or len(jobs) != 32:
        raise ValueError("study identity/cardinality mismatch")
    if {job.get("providerId") for job in jobs} != set(AUTHORIZED_PROVIDERS):
        raise ValueError("receiver family set differs from authorization")
    if any(job.get("presetId") != AUTHORIZED_PROVIDERS[job["providerId"]] for job in jobs):
        raise ValueError("receiver preset differs from authorization")
    if [job["order"] for job in jobs] != list(range(1, 33)):
        raise ValueError("study order is not exact 1..32")

    health_status, health = request_json(base_url, "/api/health")
    if health_status != 200 or health.get("version") != EXPECTED_SERVER_VERSION:
        raise ValueError("Campfire runtime identity mismatch")
    models_status, models_response = request_json(base_url, "/api/models")
    if models_status != 200:
        raise ValueError("Campfire public model snapshot unavailable")

    planned_costs: dict[str, float] = {}
    for job in jobs:
        _, prompt = exact_prompt(manifest_path, job)
        status, response = request_json(base_url, "/api/estimate", "POST", round_draft(job, prompt))
        if status != 200:
            raise ValueError(f'{job["jobId"]}: initial estimate failed: {status}')
        planned_costs[job["jobId"]], _ = validate_estimate(job, response)

    connection_costs = {
        provider: connection_ceiling(models_response, provider)
        for provider in ("gemini", "kimi")
    }
    connection_reserve = sum(connection_costs.values())
    planned_total = connection_reserve + sum(planned_costs.values())
    plan = {
        "schema": "trace-v030-two-family-api-execution-plan-v1",
        "authorizationId": AUTHORIZATION_ID,
        "manifestSha256": EXPECTED_MANIFEST_SHA256,
        "preflightReportSha256": EXPECTED_PREFLIGHT_SHA256,
        "serverVersion": health.get("version"),
        "capUsd": args.cap_usd,
        "connectionCeilingsUsd": connection_costs,
        "connectionReserveUsd": connection_reserve,
        "primaryCeilingUsd": round(sum(planned_costs.values()), 12),
        "aggregateCeilingUsd": round(planned_total, 12),
        "remainingMarginUsd": round(args.cap_usd - planned_total, 12),
        "providers": AUTHORIZED_PROVIDERS,
        "primaryCalls": len(jobs),
        "qwenCalls": 0,
        "retries": 0,
        "manualFallbacks": 0,
    }
    if planned_total > args.cap_usd:
        raise ValueError(f"aggregate ceiling {planned_total:.12f} USD exceeds authorization")
    print(canonical_json({"phase": "PLAN", **plan}), end="", flush=True)
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
    exclusive_json(output_dir / "authorization-and-plan.json", plan)
    events: list[dict[str, object]] = []

    def record(event: dict[str, object]) -> None:
        events.append(event)
        append_event(ledger, event)
        print(canonical_json({"phase": "EVENT", **event}), end="", flush=True)

    # Align the configured Gemini connection diagnostic with the exact authorized candidate.
    before_gemini = public_model(models_response, "gemini")
    if before_gemini.get("model") != "gemini-3.6-flash":
        status, saved = request_json(
            base_url, "/api/connections/gemini", "POST", {"model": "gemini-3.6-flash"}
        )
        if status != 200 or saved.get("connection", {}).get("model") != "gemini-3.6-flash":
            raise RuntimeError("failed to align Gemini configured model to 3.6 Flash")
        record({
            "type": "configuration.aligned",
            "providerId": "gemini",
            "beforeModel": before_gemini.get("model"),
            "afterModel": "gemini-3.6-flash",
            "providerCalls": 0,
        })

    # Exactly two connection diagnostics; stop before primary calls on any failure.
    for provider in ("gemini", "kimi"):
        status, result = request_json(base_url, f"/api/connections/{provider}/test", "POST", {})
        safe = {
            key: result.get(key)
            for key in (
                "ok", "modelId", "provider", "configuredModel", "protocol", "durationMs",
                "expectedMarkerSeen", "visibleAnswerTokens", "transportMaxOutputTokens",
                "billingOutputCeilingTokens", "connectorResponseId", "connectorRequestId",
                "providerReportedModel", "providerFinishReason", "truncated", "code", "error",
            )
            if key in result
        }
        record({
            "type": "connection.completed" if status == 200 and result.get("ok") else "connection.failed",
            "providerId": provider,
            "httpStatus": status,
            "reservedCeilingUsd": connection_costs[provider],
            "result": safe,
        })
        if status != 200 or not result.get("ok"):
            write_summary(
                output_dir / "run-summary.json", status="STOPPED_CONNECTION_FAILURE",
                cap=args.cap_usd, connection_reserve=connection_reserve,
                completed_exposure=0.0, jobs=jobs, events=events, failure=safe,
            )
            return 2

    completed_exposure = 0.0
    remaining = dict(planned_costs)
    for job in jobs:
        prompt_bytes, prompt = exact_prompt(manifest_path, job)
        draft = round_draft(job, prompt)
        status, estimate_response = request_json(base_url, "/api/estimate", "POST", draft)
        if status != 200:
            raise RuntimeError(f'{job["jobId"]}: fresh estimate HTTP {status}')
        fresh_estimate, fingerprint = validate_estimate(job, estimate_response)
        remaining[job["jobId"]] = fresh_estimate
        projected = connection_reserve + completed_exposure + sum(remaining.values())
        if projected > args.cap_usd:
            raise RuntimeError(f'{job["jobId"]}: refreshed aggregate ceiling exceeds authorization')

        create_body = {
            **draft,
            "budgetConfirmation": {"confirmed": True, "fingerprint": fingerprint},
        }
        create_status, created = request_json(base_url, "/api/rounds", "POST", create_body)
        if create_status != 201:
            raise RuntimeError(f'{job["jobId"]}: round creation failed {create_status}: {created.get("code") or created.get("error")}')
        session_id = str(created.get("sessionId", ""))
        round_id = str(created.get("roundId", ""))
        if not re.fullmatch(r"[A-Za-z0-9_-]+", session_id) or not re.fullmatch(r"[A-Za-z0-9_-]+", round_id):
            raise RuntimeError(f'{job["jobId"]}: unsafe/missing round identity')
        record({
            "type": "primary.authorized",
            "jobId": job["jobId"], "pairId": job["pairId"], "arm": job["arm"],
            "order": job["order"], "providerId": job["providerId"], "presetId": job["presetId"],
            "promptSha256": job["promptSha256"], "promptBytes": len(prompt_bytes),
            "maximumEstimatedCostUsd": fresh_estimate, "budgetFingerprint": fingerprint,
            "sessionId": session_id, "roundId": round_id,
        })
        route = (
            f"/api/sessions/{quote(session_id, safe='')}/rounds/{quote(round_id, safe='')}"
            f"/call/{job['providerId']}"
        )
        call_status, call = request_json(base_url, route, "POST", {})
        raw = str(call.get("rawResponse", ""))
        safe_record = safe_call_record(call)
        exclusive_json(response_dir / f'{int(job["order"]):02d}_{job["jobId"]}.json', safe_record)
        if raw:
            raw_bytes = raw.encode("utf-8")
            exclusive_bytes(raw_dir / f'{int(job["order"]):02d}_{job["jobId"]}.txt', raw_bytes)
        else:
            raw_bytes = b""

        exposure = accounted_exposure(call, fresh_estimate)
        remaining.pop(job["jobId"], None)
        completed_exposure += exposure
        common = {
            "jobId": job["jobId"], "pairId": job["pairId"], "arm": job["arm"],
            "order": job["order"], "providerId": job["providerId"], "presetId": job["presetId"],
            "sessionId": session_id, "roundId": round_id, "httpStatus": call_status,
            "maximumEstimatedCostUsd": fresh_estimate, "accountedExposureUsd": exposure,
            "providerReportedModel": call.get("providerReportedModel"),
            "providerFinishReason": call.get("providerFinishReason"),
            "truncated": bool(call.get("truncated")),
            "rawResponseSha256": sha256(raw_bytes) if raw_bytes else None,
            "rawResponseBytes": len(raw_bytes),
            "outputWords": len(re.findall(r"\b\w+\b", raw)),
            "over1200Words": len(re.findall(r"\b\w+\b", raw)) > 1200,
        }
        if call_status == 200 and raw:
            record({"type": "primary.completed", **common})
        else:
            failure = {"code": call.get("code"), "error": call.get("error"), **common}
            record({"type": "primary.failed", **failure})
            write_summary(
                output_dir / "run-summary.json", status="STOPPED_PRIMARY_FAILURE",
                cap=args.cap_usd, connection_reserve=connection_reserve,
                completed_exposure=completed_exposure, jobs=jobs, events=events, failure=failure,
            )
            return 3

    write_summary(
        output_dir / "run-summary.json", status="COMPLETE_UNADJUDICATED",
        cap=args.cap_usd, connection_reserve=connection_reserve,
        completed_exposure=completed_exposure, jobs=jobs, events=events,
    )
    print(canonical_json({
        "phase": "COMPLETE",
        "status": "COMPLETE_UNADJUDICATED",
        "primaryCalls": len(jobs),
        "completedOrReservedExposureUsd": round(connection_reserve + completed_exposure, 12),
        "remainingAuthorizedUsd": round(args.cap_usd - connection_reserve - completed_exposure, 12),
    }), end="", flush=True)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(canonical_json({
            "phase": "FATAL",
            "status": "STOPPED_FAIL_CLOSED",
            "error": str(error),
            "providerRetryAttempted": False,
            "qwenContacted": False,
        }), end="", file=sys.stderr, flush=True)
        raise
