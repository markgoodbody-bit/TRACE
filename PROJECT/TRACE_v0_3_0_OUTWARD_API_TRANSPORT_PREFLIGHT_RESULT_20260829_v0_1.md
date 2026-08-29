# TRACE v0.3.0 — OUTWARD API TRANSPORT PREFLIGHT RESULT — 2026-08-29 v0.1

**Status:** HOLD — LOCAL NON-DISPATCH EVIDENCE — NOT PROTOCOL ADOPTION — NOT RECEIVER EVIDENCE — NOT VALIDATION  
**Candidate contract:** `PROJECT/TRACE_v0_3_0_OUTWARD_API_TRANSPORT_PREFLIGHT_CANDIDATE_v0_1.md`  
**Campfire branch under test:** `framework/exact-input-study-preflight`

## 0. Result

The complete 48-job candidate study was reconstructed from the frozen prompt manifest and passed
every checked prompt-identity, exact-preset, lifecycle, request-envelope, known-price and per-call-cap
condition. It remains on `HOLD` because none of the three provider connectors was API-ready in the
inspected process.

```text
declared jobs = 48
identity-valid jobs = 48
ready jobs = 0
held jobs = 48
hold reason = API_NOT_READY (48/48)
provider calls = 0
dispatch authorizations created = 0
```

This is an operational preflight result. It says nothing about TRACE efficacy.

## 1. Artifact identity

```text
study manifest SHA-256:
75d6188ddeaab7a12d202622c655997819ccca501d45286c434b9f43187858e1

preflight report SHA-256:
ab400f3d27f53f4fc5f9687d1e2e268c639d4339680f5af1b3e5c55539319096

Campfire claim ceiling:
PREFLIGHT_NOT_AUTHORIZATION_NOT_DISPATCH_NOT_PROVIDER_CONTACT
```

The generated local bundle contains 16 unique prompt files, the Campfire study manifest and the
full report. The adapter expands the prompts to 48 ordered jobs without duplicating or rewriting
the prompt bytes.

## 2. Preliminary native-currency ceiling

These figures use Campfire's approximate four-characters-per-token input estimate and assume the
full 8000-token provider output ceiling on every call. They are ceilings under the inspected
catalogue, not observed charges or invoice evidence.

| provider candidate | calls | native maximum estimate | largest call | configured per-call cap |
|---|---:|---:|---:|---:|
| Gemini 3.6 Flash | 16 | 1.0675845 USD | 0.0718065 USD | 0.25 USD |
| Kimi K3 | 16 | 2.135169 USD | 0.143613 USD | 0.25 USD |
| Qwen 3.7 Plus — US | 16 | 3.502338 CNY | 0.239226 CNY | 0.25 CNY |

```text
USD subtotal = 3.2027535 USD
CNY subtotal = 3.502338 CNY
CURRENCIES_COMBINED = false
```

The Qwen maximum sits close to its per-call cap. Prompt or output-ceiling drift can therefore block
that job. No cap should be raised silently.

## 3. What this corrects

Before:

- the only prepared execution path made the human operator service 48 browser interactions;
- the frozen manual snapshot did not define an exact Qwen API endpoint;
- the frozen Gemini model had become a legacy catalogue entry;
- exact prompt hashes did not by themselves prove an empty connector system envelope.

After this bounded repair:

- all 48 exact inputs can be reconstructed and checked automatically;
- the candidate API presets and request controls are explicit;
- the preflight proves that identity, pricing and per-call caps are internally coherent under the
  inspected catalogue;
- the only observed local hold is missing API readiness.

This is a governance/process improvement, not an earned efficacy result. The candidate Gemini/Qwen
choices remain provisional until adopted or externally challenged.

## 4. Remaining gate

Do not dispatch until all of the following are true:

1. the candidate receiver substitutions are explicitly adopted for a new dispatch-plan revision;
2. credentials are configured locally without entering repository history or reports;
3. Mark authorizes an explicit numeric study budget with USD and CNY treated separately or through
   an explicitly witnessed conversion basis;
4. the server's own Money Guard recomputes and binds each exact call;
5. the runner preserves deterministic order, append-only attempts and complete raw return metadata;
6. unavailable API transport fails closed rather than becoming a manual fallback.

The 2026-08-28 transport hold is narrowed but not cleared.
