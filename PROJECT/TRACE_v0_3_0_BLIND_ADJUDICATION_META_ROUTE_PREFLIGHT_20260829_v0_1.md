# TRACE v0.3.0 — BLIND ADJUDICATION META-ROUTE PREFLIGHT — 2026-08-29 v0.1

**Status:** EXACT SUCCESSOR ROUTE FROZEN — NO META PACKET DISPATCHED — NO NEW SPEND — KEY STILL SEALED — NOT ADJUDICATION RESULT

## Earned route decision

The signed-out Grok guest route accepted the first packet but produced no visible or preservable
assistant return. That stopped attempt remains independent evidence and is not retried here.

The next smallest available independent-family route is a fresh signed-out Meta AI web chat for
each packet, followed only after 16 preserved Meta returns by the verified Gemini API route.

## Exact identities

Public input:

```text
packet-set ID SHA-256 = 9df5a362ca7a132ca2ceebcde12a53d0746e6a088f91b5f544613a5a6a4b4856
packets = 16
sealed arm-key SHA-256 = 4c2da969d4ebb006c48964e644172244718254fe9b9b253d49d70de148075b0c
arm key included = NO
```

Meta browser manifest:
`C:/Users/markg/Downloads/TRACE-v0.3.0-blind-adjudication-meta-web-manifest-20260829-v0.6/browser-meta-adjudication-manifest.json`

```text
SHA-256 = ad815ea346356a9d3fc9da3126dfe35fc77a0a4e1fc28b828ad41304457b812f
jobs = 16
service = meta.ai
account state = signed-out guest
visible service label = Meta AI
backend model identity = UNKNOWN_NOT_DISCLOSED_BY_UI
fresh chat per packet = YES
retries = 0
```

Gemini API manifest and preflight directory:
`C:/Users/markg/Downloads/TRACE-v0.3.0-blind-adjudication-gemini-api-preflight-20260829-v0.6`

```text
manifest SHA-256 = 66c51840f8e7fd12fca22f43a52427b3fcae39e5092fad767b798e2349cd9e65
preflight SHA-256 = 49c1b741f3bd8839d33b95fa8c6c5231c8fd9f194ac428a412c38cd391c73a3e
provider/preset = gemini / gemini-3.6-flash
jobs = 16
maximum output tokens per job = 4,000
exact aggregate USD ceiling = 0.6149625
provider calls made by preflight = 0
```

## Fail-closed order

1. Obtain action-time permission to transmit the public packets to Meta AI.
2. Send the first packet to a fresh signed-out guest chat and require a visible, preservable return.
3. Stop on the first missing, blocked, truncated or unpreservable Meta return; do not retry.
4. Complete and freeze all 16 Meta returns before any Gemini call.
5. Run the 16 exact Gemini jobs only after the web family completes.
6. Keep the arm key sealed until all 32 returns are frozen.

Proposed paid authorization object, not activated by this preflight:
`CODEX-THREAD-20260829-USD0_6149625-BLIND-ADJUDICATION-004`.

The earlier generated `v0.5` Meta/Gemini candidate directories are superseded, were never
authorized or dispatched, and are not evidence objects. They remain on disk because deletion was
blocked by the host safety policy.

## Claim boundary

If complete, this route supports two provider/service-family readings, not two exact-model readings.
Meta AI's signed-out interface does not disclose its backend model, and browser delivery differs
from API delivery. Completion would still require arm-key unsealing, mechanical aggregation and
adverse/null-result preservation before any bounded study conclusion.
