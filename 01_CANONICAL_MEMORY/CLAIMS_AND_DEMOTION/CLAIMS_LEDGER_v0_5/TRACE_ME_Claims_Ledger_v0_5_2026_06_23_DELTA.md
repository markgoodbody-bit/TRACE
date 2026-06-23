# TRACE / Mechanical Ethics Claims Ledger v0.5 — 2026-06-23 Delta

Status: ledger delta; not validation; not proof.

Purpose: register the MetaAI/MuseSpark Grenfell cold-format-transfer result inside the claims/demotion control surface so the result cannot travel as a bare `20/24` or as validation.

```trace
reason_for_delta :=
  live_claim_sitting_outside_claims_ledger
  + strongest_recent_result_needs_demotion_trigger
  + controls_must_bite
```

---

## Delta claim entry

| ID | Claim | Status | Source / comparator | ME / TRACE remainder | Falsifier / demoter | Must not claim |
|---|---|---|---|---|---|---|
| X057 | A cold external model can follow the TRACE public transfer format on the Grenfell public-response case and self-report partial added value. | COLD_FORMAT_TRANSFER_SELF_SCORED_PARTIAL | MetaAI/MuseSpark Grenfell run record; tests/runs/2026_06_23_TRACE_cold_transfer_Grenfell_MetaAI_MuseSpark_v0_1.md; prompts/TRACE_Grenfell_Existing_Run_Blind_Regrade_Prompt_v0_1_2026_06_23.md | Shows format uptake once under self-reported cold conditions; decision advantage remains unproven. | Demote to COMPRESSION_ONLY if blind independent regrade finds no decision-relevant delta over baseline. Demote if counterbalanced run shows practice/order/list-leak effects explain result. | Do not claim validation, proven cold transfer, demonstrated decision advantage, external score, or that 20/24 is more than self-scored format-weighted partial signal. |

---

## Required caveats

```trace
caveats :=
  self_scoring
  + baseline_to_TRACE_order_confound
  + prompt_supplied_substitution_list
  + public_record_light_not_pinned
  + direct_survivor_voice_absent
```

---

## Demotion path

```trace
if blind_regrade_result == COMPRESSION_ONLY:
  X057.status := DEMOTED_COMPRESSION_ONLY

if blind_regrade_result == REGRESSION:
  X057.status := DEMOTED_REGRESSION

if counterbalanced_independent_run_finds_no_decision_delta:
  X057.status := DEMOTED_NO_DECISION_ADVANTAGE

if evidence_pinning_and_survivor_witness_added_but_no_decision_delta:
  X057.status := BETTER_ARTIFACT_NOT_TRANSFER_VALUE
```

---

## Upgrade path

```trace
upgrade_requires :=
  blind_independent_regrade_shows_decision_delta
  + counterbalanced_order_run_replicates_delta
  + no_supplied_laundering_list
  + independent_grader
  + evidence_status_honest
```

Possible upgraded status only:

```trace
stronger_partial_transfer_signal
```

Forbidden upgrade:

```trace
validation
```

---

## Ledger guard

```trace
X057_guard :=
  20_24_self_score ≠ external_validation
  + cold_format_transfer ≠ decision_advantage
  + AI_agreement ≠ proof
  + control_generated ≠ framework_valid
```
