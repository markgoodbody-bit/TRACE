# TRACE v0.3.0 — OUTWARD API TRANSPORT PREFLIGHT CANDIDATE v0.2 — TWO FAMILY

**Status:** WORKING / NON-CANON / UNVALIDATED — HUMAN-SCOPED QWEN EXCLUSION — NO PROVIDER CONTACT

**Date:** 2026-08-29

**Supersedes as the active API candidate:** `PROJECT/TRACE_v0_3_0_OUTWARD_API_TRANSPORT_PREFLIGHT_CANDIDATE_v0_1.md`

## 0. Human decision and scope

Mark reported that Gemini and Kimi configuration had been repaired but Qwen would not work for now
and should be left out. Qwen is therefore excluded from the active candidate rather than probed,
retried, replaced or counted as a model failure.

```text
QWEN_UNAVAILABLE_TO_THIS_RUN != QWEN_MODEL_FAILURE
EXCLUDED_BEFORE_DISPATCH != MISSING_RETURN
TWO_FAMILY_MINIMUM != THREE_FAMILY_BREADTH
```

The frozen outward protocol permits a minimum of two genuinely cold receiver families, although
three remains preferable. Gemini plus Kimi therefore preserves the minimum breadth needed for a
possible later disposition. It reduces redundancy and makes any family-specific effect harder to
separate from a TRACE effect.

## 1. Active candidate shape

```text
8 packets x 2 receiver families x 2 arms = 32 calls
16 A/T pairs
```

| family | exact candidate preset | calls | status before provider test |
|---|---|---:|---|
| `GEMINI_GOOGLE` | `gemini-3.6-flash` | 16 | API-configured locally; connection not provider-witnessed in this step |
| `KIMI_MOONSHOT` | `kimi-k3` | 16 | API-configured locally; connection not provider-witnessed in this step |
| `QWEN_ALIBABA` | none in active candidate | 0 | excluded by human instruction |

The v0.1 exact-input controls remain unchanged: no context, no identity envelope, empty role,
8000 visible/provider output tokens, no judge mode and no connection-probe mode. Prompt bytes,
packet selection, A/T construction and within-family order are unchanged.

## 2. Evidence boundary

Campfire's public local status reports `apiReady=true` and `apiKeyPresent=true` for Gemini and Kimi.
That means the running v0.18.33 process has the required configuration fields. It does not establish
that either provider accepts the credential or returns the requested model.

No connection-test endpoint or provider endpoint was called to produce this candidate.

## 3. Remaining authority gate

The prior static ceiling for these two families was:

```text
Gemini maximum: 1.0675845 USD
Kimi maximum:   2.1351690 USD
combined:       3.2027535 USD
```

The local server must recompute that estimate under its own current pricing/FX/settings. Neither the
static figure nor a server estimate authorizes spend. Mark must still give an explicit numeric cap
for this exact 32-call candidate before any provider connection test or primary dispatch.
