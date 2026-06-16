# TRACE / ME Claims Demotion Protocol v0.1

Status: subtraction machinery. Triggered by Kimi review. Not validation. Not proof.

## Why this exists

Kimi's strongest criticism was that TRACE had many anti-overclaim guards but not enough machinery for subtraction.

```trace
missing_before :=
  claim_statuses
  without:
    hard_demotion_path
    removal_condition
    cry_wolf_check
    preregistered_wrongness_test
```

This protocol exists so TRACE can lose claims.

## Core rule

```trace
if_TRACE_cannot_lose_claims:
  TRACE_becomes_belief_system

if_TRACE_can_lose_claims:
  TRACE_remains_tool_under_pressure
```

## Status ladder

| Status | Meaning |
|---|---|
| `known_guard` | Boundary rule preventing overclaim or misuse. |
| `core_operator` | Central TRACE operator used across cases. |
| `patterned_operator` | Recurring pattern across multiple cases. |
| `boundary_claim` | Guard for a risky seam. |
| `hypothesis_operator` | Plausible operator needing tests. |
| `alignment_relevant_hypothesis` | AI/alignment-relevant but not validated. |
| `candidate_branch` | Possible future Kernel branch. |
| `deprecated` | No longer reliable as stated. |
| `removed` | Retired from active framework. |

## Demotion triggers

A claim or operator must be demoted, frozen, split, or removed if any of these apply:

| Trigger | Action |
|---|---|
| It only renames existing work and adds no operational remainder. | Downgrade to translation note or deprecated. |
| It cannot identify what would make it false. | Freeze or deprecated. |
| It explains every case equally well after the fact. | Demote for overfit. |
| It cannot discriminate before outcome knowledge. | Demote from diagnostic to interpretive. |
| It produces false positives repeatedly. | Add cry-wolf warning, then demote if repeated. |
| It produces false negatives on cases it should catch. | Demote or split. |
| It requires vague virtue language to function. | Demote to aspirational frame. |
| It becomes dangerous when applied literally. | Freeze pending safety note. |
| It duplicates an existing operator. | Merge, split, or remove. |
| It is being used as validation despite guardrails. | Freeze and revise public surface. |

## Removal condition

```trace
remove_if :=
  no_distinct_remainder
  OR unfalsifiable_after_revision
  OR repeatedly_misleads_use
  OR cannot_be_safely_bounded
  OR better_existing_framework_covers_it_with_less_confusion
```

Removal is successful correction, not project failure.

## Cry-wolf check

```trace
cry_wolf_check :=
  if TRACE_assigns_FAIL
  and no_relevant_harm_or_near_miss_materializes
  after_review_window:
    investigate_overprediction
    tighten_gate_thresholds
    demote_overbroad_claim_if_repeated
```

## False-negative check

```trace
false_negative_check :=
  if TRACE_assigns_PASS_or_PARTIAL
  and later_harm_occurs
  that TRACE_operators_should_have_detected:
    demote_related_claim
    update_gate_threshold
    record_failure
```

## Candidate branch gate

No candidate branch may enter the Diagnostic Kernel until it has:

```trace
candidate_branch_gate :=
  clear_activation_condition
  + clear_deactivation_condition
  + at_least_one_success_case
  + at_least_one_failure_case
  + one_breaker_case
  + demotion_rule
  + no_safer_existing_operator
```

Current held branches:

| Branch | Source | Status |
|---|---|---|
| Recursive agency / training-loop | Groundhog Day | candidate only |
| Creator responsibility | Frankenstein | candidate only |
| Contested legitimacy | Kimi COVID breaker suggestion | candidate only |

## K-gate tautology check

```trace
K_gate_earns_use :=
  if it discriminates:
    nominal_presence
    vs
    functional_linkage
  before_outcome_known
```

Demote K-gate use in a domain if it only says failure failed, all after-the-fact assignments fit, no thresholds exist, or existing frameworks discriminate better.

## Minimal demotion record

```trace
demotion_record :=
  claim_id
  + old_status
  + new_status
  + reason
  + evidence
  + affected_artifacts
  + date
  + whether_public_surface_changed
```
