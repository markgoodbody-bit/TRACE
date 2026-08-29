# TRACE v0.3.0 — BLIND ADJUDICATION MIXED-ROUTE PREFLIGHT — 2026-08-29 v0.1

**Status:** EXACT SUCCESSOR ROUTE FROZEN — NO PACKET DISPATCHED — NO NEW SPEND — KEY STILL SEALED — NOT ADJUDICATION RESULT

## Why this successor exists

Both tested Kimi adjudication profiles failed on the first neutral packet. Estimate-only Campfire
checks also show that its configured OpenAI, Anthropic, Grok and MiniMax routes are manual-only and
Qwen is unavailable. Kimi must not be tried again for this gate.

The smallest available repair is a mixed-transport, two-provider-family successor:

1. a fresh signed-out Grok web chat for each frozen neutral packet; then
2. the verified Gemini API route for the same 16 packets.

This changes transport and weakens exact model identity on the Grok side. It does not rewrite either
stopped attempt and cannot inherit their partial returns as study observations.

## Frozen public input

```text
public packet-set ID SHA-256 = 9df5a362ca7a132ca2ceebcde12a53d0746e6a088f91b5f544613a5a6a4b4856
public packet count = 16
sealed arm-key SHA-256 = 4c2da969d4ebb006c48964e644172244718254fe9b9b253d49d70de148075b0c
arm key included = NO
delta/provenance notes included = NO
```

## Route A — Grok browser adjudicator

Directory:
`C:/Users/markg/Downloads/TRACE-v0.3.0-blind-adjudication-grok-web-manifest-20260829-v0.4`

```text
manifest = browser-grok-adjudication-manifest.json
manifest SHA-256 = e636b3c854348b55169afa2daf09e32a28ecb1f059b005d5c21e646ae385228c
jobs = 16
service = grok.com
account state = signed-out guest
visible mode = Fast
backend model identity = UNKNOWN_NOT_DISCLOSED_BY_UI
fresh chat required per packet = YES
retry count = 0
```

Each job transmits only the exact public neutral-packet prompt bound by its byte count and SHA-256.
The visible page export and session URL must be preserved before moving to the next packet. External
search is prohibited by the packet instructions, but the browser interface cannot technically prove
that the service did not use undisclosed retrieval. Any return therefore carries that limitation.

## Route B — Gemini API adjudicator

Directory:
`C:/Users/markg/Downloads/TRACE-v0.3.0-blind-adjudication-gemini-api-preflight-20260829-v0.4`

```text
manifest = campfire-adjudication-manifest.json
manifest SHA-256 = d22aab62ef3f48aa96d92d21a3dbfc5fe74a34248b2ef09b22d50cccdcdacf4e
preflight = campfire-local-server-preflight-report.json
preflight SHA-256 = f3258917caa180b6a13f91d5bcbe97c81e836f7d6b51a91b6791258d827a7e56
Campfire version = 0.18.34
provider = gemini
preset = gemini-3.6-flash
jobs = 16
maximum output tokens per job = 4,000
exact aggregate USD ceiling = 0.6149625
provider calls made by preflight = 0
```

## Fail-closed execution order

```text
1. Confirm the browser transmission and exact new paid cap at action time.
2. Run Grok first, one fresh signed-out guest chat per packet.
3. Stop on the first blocked, missing, materially truncated or unpreservable Grok return.
4. Only after all 16 Grok returns are frozen, run all 16 Gemini API jobs.
5. Stop the Gemini route on its first transport failure; do not retry or substitute.
6. Keep the arm key sealed until all 32 successor returns are frozen.
7. Unseal once, aggregate mechanically, and preserve null/adverse findings.
```

Proposed exact paid authorization object, not yet activated by this preflight:
`CODEX-THREAD-20260829-USD0_6149625-BLIND-ADJUDICATION-003`.

## Claim boundary

If complete, this route can provide two independent provider/service-family readings. It cannot
provide two exact-model-identity readings because the signed-out Grok interface exposes only the
mode label `Fast`, not its backend model. Browser and API delivery are also different transport
conditions. Any aggregate result must state both limitations and must not be promoted to validation,
efficacy, release, canon or universal-transfer status.
