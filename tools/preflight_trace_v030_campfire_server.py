#!/usr/bin/env python3
"""Check a TRACE exact-input manifest against Campfire's local estimate route.

Only GET /api/health and POST /api/estimate are admitted. The script has no
round/dispatch path and never sends confirmation authority.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import HTTPRedirectHandler, Request, build_opener


EMPTY_SHA256 = hashlib.sha256(b"").hexdigest()
CLAIM_CEILING = (
    "LOCAL_SERVER_ESTIMATE_ONLY_NOT_CONNECTION_TEST_NOT_AUTHORIZATION_"
    "NOT_DISPATCH_NOT_PROVIDER_RETURN"
)


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


def request_json(base_url: str, route: str, body: object | None = None) -> dict[str, object]:
    if route not in {"/api/health", "/api/estimate"}:
        raise ValueError(f"route not admitted: {route}")
    data = None if body is None else json.dumps(body, ensure_ascii=False).encode("utf-8")
    request = Request(
        f"{base_url}{route}",
        data=data,
        method="GET" if body is None else "POST",
        headers={"Content-Type": "application/json; charset=utf-8"},
    )
    with build_opener(NoRedirect).open(request, timeout=30) as response:
        final = urlparse(response.geturl())
        if final.hostname not in {"127.0.0.1", "localhost", "::1"} or final.path != route:
            raise ValueError("Campfire request escaped the admitted loopback route")
        return json.loads(response.read().decode("utf-8"))


def build_report(manifest_path: Path, base_url: str) -> dict[str, object]:
    manifest_bytes = manifest_path.read_bytes()
    manifest = json.loads(manifest_bytes.decode("utf-8"))
    if manifest.get("schema") != "campfire-exact-input-study-v1":
        raise ValueError("unsupported study manifest schema")

    health = request_json(base_url, "/api/health")
    jobs = []
    reasons = []
    totals_by_currency: dict[str, float] = {}
    total_gbp = 0.0
    gbp_complete = True

    for declared in manifest.get("jobs", []):
        job_id = str(declared.get("jobId", ""))
        job_reasons = []
        prompt_path = (manifest_path.parent / str(declared["promptPath"])).resolve()
        prompt_bytes = prompt_path.read_bytes()
        prompt_text = prompt_bytes.decode("utf-8")
        observed_hash = sha256(prompt_bytes)
        if observed_hash != declared.get("promptSha256"):
            job_reasons.append("PROMPT_SHA256_MISMATCH")
        if len(prompt_bytes) != declared.get("promptBytes"):
            job_reasons.append("PROMPT_BYTES_MISMATCH")
        if prompt_text != prompt_text.strip():
            job_reasons.append("SERVER_TRIM_WOULD_CHANGE_PROMPT")

        request_body = {
            "prompt": prompt_text,
            "maxOutputTokens": declared["maxOutputTokens"],
            "executionProfile": "standard",
            "mode": declared.get("mode", "independent"),
            "identityRequired": declared["identityRequired"],
            "contextMode": declared["contextMode"],
            "targets": [
                {
                    "modelId": declared["providerId"],
                    "presetId": declared["presetId"],
                    "transport": "api",
                    "roleInstruction": declared["roleInstruction"],
                }
            ],
        }
        response = request_json(base_url, "/api/estimate", request_body)
        estimates = response.get("estimates", [])
        if len(estimates) != 1:
            job_reasons.append("SERVER_ESTIMATE_CARDINALITY")
            estimate = {}
        else:
            estimate = estimates[0]

        checks = {
            "providerId": estimate.get("modelId") == declared["providerId"],
            "presetId": estimate.get("presetId") == declared["presetId"],
            "apiTransport": estimate.get("transport") == "api",
            "noFallback": not bool(estimate.get("fallbackReason")),
            "promptSha256": estimate.get("effectiveInputSha256") == declared["promptSha256"],
            "emptyContext": estimate.get("contextSha256") == EMPTY_SHA256,
            "emptyRole": estimate.get("roleInstructionSha256") == EMPTY_SHA256,
            "visibleAnswerTokens": estimate.get("visibleAnswerTokens") == declared["visibleAnswerTokens"],
            "providerOutputTokens": estimate.get("transportMaxOutputTokens") == declared["maxOutputTokens"],
            "billingOutputTokens": estimate.get("billingOutputCeilingTokens") == declared["maxOutputTokens"],
            "identityDisabled": estimate.get("dispatchBasis", {}).get("identityRequired") is False,
            "onePlannedCall": response.get("budgetPreflight", {}).get("plannedCallCount") == 1,
            "fingerprintPresent": bool(response.get("budgetConfirmation", {}).get("fingerprint")),
        }
        job_reasons.extend(key for key, passed in checks.items() if not passed)

        cost = estimate.get("estimate") or {}
        currency = str(cost.get("currency", ""))
        amount = cost.get("maximumEstimatedCost")
        if currency and isinstance(amount, (int, float)):
            totals_by_currency[currency] = totals_by_currency.get(currency, 0.0) + float(amount)
        else:
            job_reasons.append("SERVER_COST_ESTIMATE_MISSING")
        gbp = estimate.get("gbpEstimate")
        if isinstance(gbp, (int, float)):
            total_gbp += float(gbp)
        else:
            gbp_complete = False

        reasons.extend({"jobId": job_id, "code": code} for code in job_reasons)
        jobs.append(
            {
                "jobId": job_id,
                "pairId": declared.get("pairId"),
                "arm": declared.get("arm"),
                "order": declared.get("order"),
                "promptSha256": observed_hash,
                "providerId": declared["providerId"],
                "presetId": declared["presetId"],
                "configuredModel": estimate.get("configuredModel"),
                "transport": estimate.get("transport"),
                "requestControlsHash": estimate.get("dispatchBasis", {}).get("requestControlsHash"),
                "maximumEstimatedCost": amount,
                "currency": currency or None,
                "gbpEstimate": gbp,
                "budgetRisk": response.get("budgetPreflight", {}).get("risk"),
                "confirmationRequired": response.get("budgetConfirmation", {}).get("required"),
                "budgetFingerprint": response.get("budgetConfirmation", {}).get("fingerprint"),
                "status": "HOLD" if job_reasons else "PASS_SERVER_ESTIMATE_ONLY",
                "reasons": job_reasons,
            }
        )

    return {
        "schema": "trace-v030-campfire-local-server-preflight-report-v1",
        "claimCeiling": CLAIM_CEILING,
        "status": "HOLD" if reasons else "PASS_SERVER_ESTIMATE_ONLY",
        "campfire": {"baseUrl": base_url, "version": health.get("version")},
        "study": {
            "studyId": manifest.get("studyId"),
            "manifestSha256": sha256(manifest_bytes),
            "declaredJobs": len(manifest.get("jobs", [])),
        },
        "summary": {
            "passedJobs": sum(job["status"] == "PASS_SERVER_ESTIMATE_ONLY" for job in jobs),
            "heldJobs": sum(job["status"] == "HOLD" for job in jobs),
            "totalsByCurrency": {
                currency: round(amount, 12)
                for currency, amount in sorted(totals_by_currency.items())
            },
            "totalGbp": round(total_gbp, 12) if gbp_complete else None,
            "gbpComplete": gbp_complete,
            "serverEstimateRequests": len(jobs),
            "connectionTestRequests": 0,
            "roundRequests": 0,
            "providerDispatchRequests": 0,
            "dispatchAuthorizationsCreated": 0,
        },
        "reasons": reasons,
        "jobs": jobs,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--base-url", default="http://127.0.0.1:4317")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = build_report(args.manifest.resolve(), local_base_url(args.base_url))
    output = args.output.resolve()
    with output.open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(canonical_json(report))
    print(
        canonical_json(
            {
                "claimCeiling": CLAIM_CEILING,
                "dispatchPerformed": False,
                "output": str(output),
                "sha256": sha256(output.read_bytes()),
                "status": report["status"],
                "summary": report["summary"],
            }
        ),
        end="",
    )
    return 0 if report["status"] == "PASS_SERVER_ESTIMATE_ONLY" else 2


if __name__ == "__main__":
    raise SystemExit(main())
