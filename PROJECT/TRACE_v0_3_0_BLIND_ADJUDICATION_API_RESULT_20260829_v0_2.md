# TRACE v0.3.0 — BLIND ADJUDICATION API RESULT — 2026-08-29 v0.2

**Status:** STOPPED ON FIRST CALL — ADVERSE KIMI TRANSPORT RESULT PRESERVED — KEY STILL SEALED — NOT ADJUDICATION COMPLETION — NOT EFFICACY RESULT

## Earned result

The exact whole-study successor began under authorization
`CODEX-THREAD-20260829-USD0_95643875-BLIND-ADJUDICATION-002`.

```text
planned calls = 32
attempted calls = 1
completed calls = 0
failed calls = 1
unattempted calls = 31
retries = 0
manual fallbacks = 0
Qwen contacts = 0
arm key unsealed = NO
```

The first fail-fast call was Kimi K2.6 on neutral packet `PAIR-09F86168CA`. Campfire returned
HTTP 502 after the provider reported model `kimi-k2.6`, `finish_reason=length`, and a truncated
result with no extractable visible text. No raw provider response was available to preserve as a
model answer. The runner therefore failed closed before any Gemini call.

This is a transport result, not an adjudication result. It does not support a substantive reading
of the neutral packet.

## Accounting boundary

```text
actual recorded exposure = USD 0.02001755
maximum preflight estimate for attempted call = USD 0.02069395
unspent authorization = USD 0.93642120
```

The actual recorded amount, rather than the higher preflight estimate, is the accounted exposure
because Campfire supplied an actual cost for the failed call. Unspent authority is not carried into
another attempt automatically.

## Frozen stopped-run identity

Directory:
`C:/Users/markg/Downloads/TRACE-v0.3.0-blind-adjudication-run-20260829-v0.2-two-family`

```text
files = 4
bytes = 13,079
run-summary.json SHA-256 = 038a3aa2c6be0ad46cb2f40369d6e08eaa77728cb19547720b923a9f7852e8c3
failed-response record SHA-256 = b15d00b1ec01f7562a5b6e9d5691be7f8cb74f8da5f7136121c9f173a6dd4f05
```

Download archive:
`C:/Users/markg/Downloads/TRACE-v0.3.0-blind-adjudication-run-STOPPED-20260829-v0.2.zip`

```text
archive bytes = 5,197
archive SHA-256 = 5056a3d1b353a3188806aacb7d4965114bf4f7d069e45cc152bcbf0e2583a571
```

## What this does and does not establish

Established:

- the Kimi K2.6 `debate-judging` repair did not yield an adjudicator return for the first packet;
- the earlier Kimi K3 watchdog failure was not repaired by this smaller 4,000-token K2.6 profile;
- the exact successor run stopped before Gemini and without retry, fallback or key exposure;
- Kimi is not a usable adjudication aperture for this packet under either tested profile.

Not established:

- that no conceivable Kimi prompt could return;
- any substantive adjudicator judgment from Kimi;
- two-family confirmation of any candidate gain;
- aggregate baseline capture, reproduction, over-fire disposition or placement;
- any TRACE efficacy, validation, release or canon result.

## Narrow disposition

Do not try Kimi again in this evidence gate. Estimate-only checks show that the configured Campfire
routes for OpenAI, Anthropic, Grok and MiniMax are manual-only, while Qwen remains unavailable.
Consequently Campfire cannot currently supply the second independent adjudicator family.

A fresh successor may combine the already verified Gemini API route with a genuinely separate,
fresh web adjudicator, but only under a newly frozen route and attempt identity. A web return must
preserve packet identity, model/service identity, visible response text, session freshness limits,
and the fact that browser delivery is not the same transport condition as the API run. The arm key
must remain sealed until all returns for that successor are frozen.
