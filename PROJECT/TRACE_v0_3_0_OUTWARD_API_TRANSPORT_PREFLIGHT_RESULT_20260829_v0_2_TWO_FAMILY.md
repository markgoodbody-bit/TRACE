# TRACE v0.3.0 — OUTWARD API TRANSPORT PREFLIGHT RESULT — 2026-08-29 v0.2 — TWO FAMILY

**Status:** PASS SERVER ESTIMATE ONLY — NOT CONNECTION TEST — NOT AUTHORIZATION — NOT DISPATCH — NOT RECEIVER EVIDENCE

**Candidate contract:** `PROJECT/TRACE_v0_3_0_OUTWARD_API_TRANSPORT_PREFLIGHT_CANDIDATE_v0_2_TWO_FAMILY.md`

**Campfire runtime:** locally running v0.18.33 at loopback

## 0. Result

The human-scoped Gemini/Kimi candidate passed Campfire's actual local `/api/estimate` path for all
32 ordered jobs.

```text
declared jobs = 32
passed server estimates = 32
held jobs = 0
local server estimate requests = 32
connection-test requests = 0
round requests = 0
provider dispatch requests = 0
dispatch authorizations created = 0
```

For every job the server returned:

- the requested exact preset;
- API transport, with no manual fallback;
- effective input SHA-256 equal to the frozen prompt SHA-256;
- empty context and role SHA-256;
- `identityRequired=false`;
- 8000 visible, transport and billing output tokens;
- one server-owned planned call and a call-specific budget fingerprint.

This establishes local routing/estimation coherence only. It does not prove that either provider
accepts the credential, preserves the requested runtime, or returns a usable answer.

## 1. Artifact identity

```text
two-family study manifest SHA-256:
5b2ea0e916409d9283991bee4e55d2ca5be5af7bea99c5801562aa5889ae1eab

local server preflight report SHA-256:
0b5dfd21d799c8268f3bb5ddea2a6dbdebc6de7eeabdcd1edd248c858afeada1

claim ceiling:
LOCAL_SERVER_ESTIMATE_ONLY_NOT_CONNECTION_TEST_NOT_AUTHORIZATION_NOT_DISPATCH_NOT_PROVIDER_RETURN
```

The extended manifest builder was also checked against the original three-family output. Its default
reproduction retained the exact prior manifest SHA-256
`75d6188ddeaab7a12d202622c655997819ccca501d45286c434b9f43187858e1`.

## 2. Current server estimate

```text
native paid-equivalent ceiling = 3.2027535 USD
server-derived GBP view        = 2.357392536435 GBP
GBP completeness               = true
```

The GBP figure is a derived current-FX view from the local server. It is neither a provider charge
nor settlement evidence. The native USD ceiling remains the primary pre-dispatch money object.

## 3. Qwen disposition

```text
QWEN JOBS = 0
QWEN PROVIDER CALLS = 0
QWEN RESULT = NOT EVALUATED / HUMAN-SCOPED EXCLUSION
```

The running Campfire process reports Qwen configuration fields present, but Mark reported that Qwen
would not work and instructed that it be left for now. No connection test was used to override that
instruction or manufacture a more specific failure claim.

## 4. Remaining limitation

Campfire's ordinary estimate route binds one prompt/call plan at a time. The 32 call-specific budget
fingerprints do not compose themselves into one study-wide authorization. The report's 3.2027535 USD
total is a deterministic aggregation of server estimates, not a server-created aggregate spending
right.

Before provider contact:

1. Mark must state an explicit numeric cap and whether it includes two preliminary connection tests;
2. a runner must preserve a study-wide remaining-cap ledger above the call-specific Money Guard;
3. each call must still receive fresh server preflight/authorization immediately before dispatch;
4. connection failure must stop the affected family without manual fallback or selective retry;
5. primary outputs must preserve order, raw bytes, runtime identity, usage, time and failure evidence
   append-only.

No further TRACE wording change is earned by this preflight.
