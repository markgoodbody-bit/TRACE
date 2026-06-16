# TRACE / ME Claims Demotion Protocol v0.1

Date: 2026-06-16  
Trigger: Kimi external review of TRACE Relay Pack v0.1.  
Status: subtraction / demotion machinery; not validation; not proof.

## 0. Why This Exists

Kimi's strongest criticism was that TRACE has many anti-overclaim guards but not enough formal machinery for subtraction.

```trace
missing_before :=
  claim_statuses
  without:
    hard_demotion_path
    removal_condition
    cry_wolf_check
    preregistered_wrongness_test
```

This protocol makes TRACE more attackable.

The purpose is not to make TRACE look safer. The purpose is to create a mechanism by which TRACE can lose claims.

## 1. Core Rule

```trace
if_TRACE_cannot_lose_claims:
  TRACE_becomes_belief_system

if_TRACE_can_lose_claims:
  TRACE_remains_tool_under_pressure
```

A claim must be able to move downward, freeze, split, or be removed.

## 2. Claim Status Ladder

The Claims Ledger should use a directional status ladder.

| Status | Meaning | Use condition |
|---|---|---|
| `known_guard` | Boundary rule preventing overclaim or misuse | Strongly retained unless it blocks truth or creates harm |
| `core_operator` | Central TRACE operator used across cases | Retained only while it discriminates better than generic language |
| `patterned_operator` | Recurring pattern across multiple cases | Requires non-trivial remainder and counterexample discipline |
| `boundary_claim` | Guards a risky seam | Requires clear activation and deactivation conditions |
| `hypothesis_operator` | Plausible operator needing tests | Must have falsifier and test route |
| `alignment_relevant_hypothesis` | AI/alignment-relevant hypothesis | Must not pretend deployment validity |
| `candidate_branch` | Possible future Kernel branch | Not operational until pressure-tested |
| `deprecated` | No longer reliable as stated | Kept for audit trail, not active use |
| `removed` | Retired from active framework | Kept only in archive with reason |

## 3. Allowed Transitions

```trace
allowed_transitions :=
  known_guard -> revised_guard OR deprecated
  core_operator -> patterned_operator OR hypothesis_operator OR deprecated
  patterned_operator -> hypothesis_operator OR deprecated
  boundary_claim -> revised_boundary_claim OR deprecated
  hypothesis_operator -> candidate_branch OR deprecated OR removed
  candidate_branch -> Kernel_candidate_after_test OR deprecated
  deprecated -> removed
```

Promotion requires pressure. Demotion requires evidence of failure, overbreadth, redundancy, danger, or non-discrimination.

## 4. Demotion Triggers

A claim must be demoted if any of these apply.

| Trigger | Demotion direction |
|---|---|
| It only renames existing work and adds no operational remainder | downgrade to `translation_note` or `deprecated` |
| It cannot identify what would make it false | downgrade to `rhetorical_claim` / `deprecated` |
| It explains every case equally well after the fact | downgrade for overfit |
| It cannot discriminate before outcome knowledge | downgrade from diagnostic to interpretive |
| It produces false positives repeatedly | add `cry_wolf_risk`, demote if repeated |
| It produces false negatives on cases it should catch | demote or split |
| It requires vague virtue language to function | demote to `aspirational_frame` |
| It becomes dangerous when applied literally | freeze pending safety note |
| It duplicates an existing operator | merge, split, or remove |
| It is being used as validation despite guardrails | freeze and revise public surface |

## 5. Removal Conditions

A claim should be removed from the active layer if:

```trace
remove_if :=
  no_distinct_remainder
  OR unfalsifiable_after_revision
  OR repeatedly_misleads_use
  OR cannot_be_safely_bounded
  OR better_existing_framework_covers_it_with_less_confusion
```

Removal is not failure of the project. It is successful correction.

## 6. Cry-Wolf Check

TRACE must not only catch failures. It must also avoid predicting failure everywhere.

```trace
cry_wolf_check :=
  if TRACE_assigns_FAIL
  and no_relevant_harm_or_near_miss_materializes
  after_review_window:
    investigate_overprediction
    tighten_gate_thresholds
    demote_overbroad_claim_if_repeated
```

One non-harm outcome does not falsify TRACE by itself. Repeated overprediction does.

## 7. False-Negative Check

```trace
false_negative_check :=
  if TRACE_assigns_PASS_or_PARTIAL
  and later_harm_occurs
  that TRACE_operators_should_have_detected:
    demote_related_claim
    update_gate_threshold
    record_failure
```

The test is not whether harm happened at all. The test is whether TRACE missed a harm path it claimed to diagnose.

## 8. Candidate Branch Rule

No new branch may enter the Diagnostic Kernel until it passes this gate:

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

| Candidate | Source | Reason held |
|---|---|---|
| Training-loop / recursive-agency branch | Groundhog Day | Promising but may duplicate learning theory / RL analysis |
| Creator-responsibility branch | Frankenstein | Powerful but currently vulnerable to vague moralizing |
| Contested-legitimacy branch | Kimi COVID breaker suggestion | Needed, but high-risk and not yet scoped |

## 9. K-Gate Tautology Check

The K-gate must not remain true only by definition.

```trace
K_gate_earns_use :=
  if it discriminates:
    nominal_presence
    vs
    functional_linkage
  before_outcome_known
```

Demote K-gate use in a domain if:

```trace
demote_K_if :=
  it_only_says_failure_failed
  OR all_after_the_fact_assignments_fit
  OR no_thresholds_exist
  OR existing_frameworks_discriminate_better
```

## 10. Frankenstein Specific Guard

```trace
Frankenstein_branch_freeze_if :=
  creator_responsibility == vague_moralizing
  OR AI_personhood_shortcut
  OR total_control_forever
  OR anti_technology_rhetoric
```

The branch may be developed only if creator duties can be specified as roles, thresholds, remedies, limits, transfer conditions, and decommissioning ethics.

## 11. Groundhog Specific Guard

```trace
Groundhog_branch_freeze_if :=
  recursion == moral_progress
  OR free_will == metaphysical_proof
  OR training_loop == alignment
  OR subject == training_object
```

The branch may be developed only if it adds a distinct diagnostic question beyond ordinary learning theory.

## 12. Ledger Patch Rule

Every Claims Ledger row should eventually include:

```trace
claim_row :=
  claim
  + status
  + source_or_comparator
  + distinct_remainder
  + falsifier_or_demoter
  + demotion_trigger
  + removal_condition
  + must_not_claim
```

Until this is implemented, the current Claims Ledger is incomplete but repairable.

## 13. Minimal Demotion Record

When demoting a claim, record:

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

## 14. Compression

```trace
TRACE_must_be_wrongable :=
  every_active_claim
  needs:
    falsifier
    demoter
    removal_condition
    cry_wolf_check
    false_negative_check
```

End.
