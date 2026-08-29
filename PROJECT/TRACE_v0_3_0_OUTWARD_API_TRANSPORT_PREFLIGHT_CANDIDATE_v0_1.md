# TRACE v0.3.0 — OUTWARD API TRANSPORT PREFLIGHT CANDIDATE v0.1

**Status:** WORKING / NON-CANON / UNVALIDATED — NO PROVIDER CONTACT — NOT A FROZEN DISPATCH REVISION

**Date:** 2026-08-29

**Source prompt contract:** `PROJECT/TRACE_v0_3_0_OUTWARD_PRIMARY_PROMPT_ASSEMBLY_v0_1.md`

**Source dispatch plan:** `PROJECT/TRACE_v0_3_0_OUTWARD_PRIMARY_DISPATCH_PLAN_v0_1.md`

## 0. Earned result

The rejected 48-step human copy/paste route is no longer the only technically available shape.
Campfire Relay already has direct connector implementations for the three selected provider
families, and its local connector/identity tests pass without provider calls. A new isolated
preflight can verify exact prompt bytes, exact preset identity, request controls, price/cap state
and local API readiness without creating dispatch authority.

This does **not** clear the execution hold. No provider credentials are configured in the inspected
process, no numeric study budget has been authorized, and no primary receiver has been contacted.

## 1. Contradictions exposed in the frozen manual plan

The v0.1 plan froze model-name snapshots for a manual route. Those names are not a complete direct
API contract:

| family | v0.1 manual snapshot | API preflight problem | candidate exact preset |
|---|---|---|---|
| `GEMINI_GOOGLE` | `gemini-3.5-flash` | Campfire's 2026-08-03 catalogue now marks it `legacy`, replaced by 3.6 Flash | `gemini-3.6-flash` |
| `QWEN_ALIBABA` | `qwen3.7-plus` | model name does not choose the Singapore or US endpoint | `qwen3.7-plus-us` |
| `KIMI_MOONSHOT` | `kimi-k3` | exact preset exists, but K3 always-thinks and remains cost/latency sensitive | `kimi-k3` |

The Gemini substitution is a material runtime change. Because no primary output exists, it can be
considered before dispatch without discarding evidence, but it must not be described as the same
frozen model snapshot. The Qwen US endpoint is selected provisionally because it is the catalogue's
configured default route; that is an engineering choice, not an efficacy result.

## 2. Candidate exact-input request contract

For every candidate job:

```text
contextMode = none
identityRequired = false
roleInstruction = empty bytes
visibleAnswerTokens = 8000
providerOutputTokens = 8000
judgeCall = false
connectionProbe = false
```

The equal visible/provider token ceilings matter: Campfire otherwise adds a visible-answer system
line when the provider ceiling is larger. With identity disabled and the role empty, the connector
adds no receiver-visible system text. Provider-native non-text controls may still fire; notably Kimi
K3 uses its declared reasoning-effort control. Those controls must remain in the dispatch identity.

The 8000-token ceiling is inherited from Campfire's current ordinary default and sits beside the
frozen prompt instruction `Return no more than 1200 words.` It is a conservative transport allowance,
not an empirical claim that 8000 is optimal or that hidden reasoning will fit. A/T within a receiver
family must keep identical controls.

## 3. Reproducible non-dispatch build

1. Run `tools/build_trace_v030_primary_prompts.py --emit-dir <output>/prompts`.
2. Run `tools/build_trace_v030_campfire_study.py --prompt-dir <output>/prompts --output <output>/campfire-study-manifest.json`.
3. Run Campfire's `scripts/preflight-exact-input-study.mjs` against that manifest.

The adapter reconstructs all 48 jobs in the already-frozen family/pair/arm order and rechecks every
prompt's bytes and SHA-256 against the committed primary prompt manifest. It does not dispatch.

## 4. Claim ceiling and unresolved work

```text
PREFLIGHT_PASS != MONEY_GUARD_AUTHORIZATION
MONEY_GUARD_AUTHORIZATION != PROVIDER_RETURN
PROVIDER_RETURN != VALID_PAIR
CURRENT_MODEL_SUBSTITUTION != ORIGINAL_FROZEN_MODEL
API_AUTOMATION != COLDNESS_PROOF
```

Remaining before any external call:

1. externally challenge or explicitly adopt the candidate model/endpoint substitutions;
2. configure credentials locally without committing or exposing them;
3. set an explicit numeric total budget and per-currency treatment;
4. confirm that server dispatch uses the preflighted empty system-envelope contract;
5. preserve raw returns, runtime identity, usage, timing, errors and no-retry evidence append-only;
6. stop rather than silently downgrade to manual transport if an API target is unavailable.

This is a governance/transport repair. It is not evidence that TRACE improves analysis.
