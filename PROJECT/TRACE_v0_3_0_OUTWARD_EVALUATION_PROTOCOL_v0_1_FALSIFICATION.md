# TRACE v0.3.0 — OUTWARD EVALUATION PROTOCOL v0.1 FALSIFICATION

**Status:** FALSIFIED BEFORE CASE SELECTION — DO NOT EXECUTE v0.1  
**Date:** 2026-08-25  
**Target:** `PROJECT/TRACE_v0_3_0_OUTWARD_EVALUATION_PROTOCOL_v0_1.md`

## Verdict

```text
BREAK / PRE-FREEZE
CASES SELECTED: 0
RUNS EXECUTED: 0
SEMANTIC TRACE OBJECT CHANGED: NO
```

The protocol was attacked before case identities were selected, as required by the evaluation freeze. Several defects could bias the result while still looking pre-registered.

## Material findings

### P01 — comparator contamination through the common output contract

v0.1 says Arm A receives an ordinary-analysis prompt, but §7 then requires both arms to return categories including affected scopes, correction/review/rollback routes, hardening constraints and residue/limits.

If §7 is supplied to the receiver, the baseline is being taught a substantial part of the structure TRACE is supposed to earn.

If §7 is not supplied, the protocol is ambiguous about what the receiver actually sees.

```text
COMMON_ADJUDICATION_SCHEMA != COMMON_RECEIVER_PROMPT
COMPETENT_BASELINE != TRACE_VOCABULARY_INJECTION
```

Repair: v0.2 makes receiver prompts exact and complete. The common dimensions become post-hoc adjudication/extraction dimensions only.

### P02 — source-pool cherry-picking remains possible

“Create a pool of at least 20 public cases” still lets the project choose which source collections to inspect after anticipating where TRACE will perform well.

Mechanical hashing inside a hand-picked pool does not remove upstream selection bias.

```text
DETERMINISTIC_SELECTION != UNBIASED_POOL_CONSTRUCTION
HASHED_POOL != INDEPENDENT_POOL
```

Repair: source collections and native intake order must be frozen before individual case narratives are inspected for TRACE usefulness. Intake takes the first eligible items in native source order until the declared quota is reached.

### P03 — case-ID hash gaming

v0.1 hashes “stable case IDs” without specifying how IDs are formed. A pool constructor can rename IDs until desired cases sort first.

Repair: case IDs are derived mechanically from immutable source collection ID + source-native case identifier (or canonical source URL when no native ID exists), then hashed. Human-chosen aliases do not participate.

### P04 — domain/slot gaming

v0.1 requires at least four domains but does not freeze domain-slot order. Borderline domain labels or slot ordering could change which hashes win.

Repair: v0.2 freezes four mandatory domain slots before case selection and requires domain labels to be assigned from source context before hashes are inspected. Remaining slots are filled mechanically subject to the non-AI constraint.

### P05 — packet-construction framing bias

The same packet across A/T protects the comparison from differential facts, but project authors can still compress source material around facts they expect TRACE to exploit.

Repair: prefer full bounded source material where feasible; otherwise record an omission map and require an independent packet audit focused on whether omitted facts would change either arm. The case question must remain ordinary-language and non-TRACE-coded.

### P06 — arm blinding is too weak

TRACE-specific invariant names or framework recital can reveal Arm T to adjudicators even after headers are stripped.

Repair: Arm T main answer must use ordinary language and avoid invariant codes/framework labels. A separate `TRACE_DELTA_NOTE` may name framework distinctions and is removed before blind adjudication.

### P07 — receiver independence definition is too coarse

“Distinct providers/families” can double-count closely related or identically based systems. Conversely, requiring proof of no training exposure is impossible.

Repair: count distinct model organisations/training lineages where known; record uncertainty. Session/context coldness is required. Unknown pretraining exposure is disclosed but does not automatically disqualify a receiver absent evidence of project familiarity.

### P08 — verbosity can create apparent gain

A longer TRACE output gets more chances to mention something baseline omitted. D6 penalises irrelevant burden but v0.1 lacks a precision-style view.

Repair: adjudication records both supported material gains and unsupported/irrelevant asserted distinctions; duplicate granularity earns no extra credit. Cost/length remains visible beside gain.

### P09 — disposition rules can conflict

A run could meet the retention threshold through two crucial gains while also trigger the 80%-coverage/1.5x-cost shrink rule.

Repair: v0.2 specifies precedence and a `RETAIN_NARROW_WITH_COMPRESSION_PRESSURE` outcome when bounded material benefit exists but complexity remains excessive. Safety/contamination HOLD gates take precedence over efficacy scoring.

### P10 — packet/question construction can leak expected lessons

A neutral-looking “decision point” can still be phrased around correction, affected scope or irreversibility in ways that cue TRACE concepts.

Repair: case questions ask for ordinary review/decision analysis and are checked for TRACE-coded wording before dispatch.

## Non-findings / retained choices

- The ordinary baseline should remain strong; weakening it would be a false win.
- Framework and CC should not count as cold efficacy receivers.
- Six real cases + two controls is acceptable as a bounded first evaluation, provided conclusions remain narrow.
- Arm F cannot rescue a failed compact-transfer result without preserving the failure.
- Fixed thresholds are imperfect but preferable to post-result goalpost movement; v0.2 will require sensitivity reporting rather than silently changing them.

## Disposition

Do not execute v0.1.

Build v0.2 from these repairs, attack it again, and freeze only if no material protocol bias survives the bounded second pass.
