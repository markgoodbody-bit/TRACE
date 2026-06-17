# TRACE Operator Registry Schema Patch — Scale, Agency, Responsibility v0.1

Date: 2026-06-17
Status: schema patch / applies to future operator promotion / audit-preserving addendum / not validation

## Plain purpose

This patch extends the TRACE Operator Registry schema before any new high-level operators are promoted.

Reason: recent probes produced larger candidates — Debt Clock, Preservation Love, intimate-system operators, scale-recursive operators. Without stricter registry fields, the repo risks becoming a metaphor machine.

This file does not rewrite the original registry. It extends it by rule.

```trace
schema_patch :=
  add_scale_fields
  + add_agency_window_field
  + add_responsibility_trace_field
  + add_boundary_demoters
  + add_evidence_grade
  + add_scale_translation_test
  - silent_overwrite
  - validation_claim
```

## Applies to

```trace
applies_to :=
  every_new_operator_probe
  + every_operator_promotion
  + every_scaled_operator_claim
  + every_high_level_candidate
```

High-level candidate means any proposed operator that touches love, care, agency, responsibility, free will, debt, work, education, illness, ecology, ritual, or other large domains.

## Original schema being patched

The original registry required:

```trace
operator_entry_original :=
  name
  + compression
  + definition
  + source_case
  + activation_conditions
  + deactivation_conditions
  + comparator
  + distinct_remainder
  + falsifier
  + demoter
  + status
  + must_not_claim
```

This remains valid but is now insufficient for new candidates.

## Extended schema

```trace
operator_entry_extended :=
  name
  + compression
  + definition
  + home_scale
  + target_scale_if_any
  + source_case_or_source_surface
  + activation_conditions
  + deactivation_conditions
  + agency_window_effect
  + responsibility_trace
  + affected_subject_scope
  + evidence_grade
  + comparator
  + distinct_remainder
  + falsifier
  + demoter
  + boundary_demoters
  + status
  + must_not_claim
  + scale_translation_test_if_scaled
```

## New required fields

### 1. Home scale

```trace
home_scale :=
  scale_where_operator_first_has_clear_shape
```

Allowed values:

```trace
scale_values :=
  body
  OR person
  OR dyad
  OR family
  OR group
  OR organisation
  OR institution
  OR market
  OR state
  OR ecosystem
  OR AI_system
  OR civilisation
```

Purpose:

Prevents moving an operator across scales without noticing substrate change.

### 2. Target scale if any

```trace
target_scale_if_any :=
  scale_where_operator_is_being_translated
  OR none
```

If none, the operator remains at home scale.

If not none, the scale translation test is mandatory.

### 3. Agency window effect

```trace
agency_window_effect :=
  how_operator_affects:
    live_options
    + subject_capacity
    + knowledge_enough_to_choose
    + route_access
    + time_before_hardening
```

Purpose:

Prevents free-will language from becoming metaphysical fog. TRACE asks whether meaningful selection is preserved or collapsed.

### 4. Responsibility trace

```trace
responsibility_trace :=
  knowledge
  + control_or_influence
  + role_or_duty
  + benefit_or_gate_holding
  + available_action
  + foreseeable_path_effect
```

Purpose:

Prevents both blame inflation and responsibility laundering.

### 5. Affected subject scope

```trace
affected_subject_scope :=
  who_or_what_bears_the_route_change
```

Allowed examples:

```trace
affected_subjects :=
  individual_person
  + group
  + dependent_subject
  + caregiver
  + non_user_affected_party
  + future_subject
  + nonhuman_subject_or_proxy
  + institution_as_governance_carrier
  + AI_status_uncertain_subject
```

Purpose:

Prevents invisible burden-routing.

### 6. Evidence grade

```trace
evidence_grade :=
  E0_none
  OR E1_claimed
  OR E2_actor_documented
  OR E2_independent_documented
  OR E3_independent_corrobated
  OR E4_replayable
```

Actor-source cap remains active:

```trace
actor_source_cap :=
  if evidence <= E2_actor_documented:
    operator_status_claim <= weak_signal_or_unknown
```

### 7. Boundary demoters

```trace
boundary_demoters :=
  conditions_under_which_operator_becomes_harmful_or_overbroad
```

Purpose:

Especially required for love, care, agency, responsibility, safety, protection, and emergency operators.

Example:

```trace
preservation_love_boundary_demoters :=
  love_excuses_boundary_violation
  OR love_erases_carer_burden
  OR love_claim_overrides_consent
```

### 8. Scale translation test

Required if target scale differs from home scale.

```trace
scale_translation_test :=
  preserve_core_relation
  + identify_changed_substrate
  + identify_changed_evidence
  + identify_changed_lever
  + identify_changed_affected_subject
  + identify_changed_demoter
```

## Promotion requirements after patch

```trace
promote_operator_only_if:
  original_schema_complete
  + extended_schema_complete
  + comparator_named
  + demoter_named
  + evidence_grade_not_E0
  + must_not_claim_set
```

For active_candidate status:

```trace
active_candidate_requires:
  evidence_grade >= E2_independent_documented
  OR strong_reason_for_exception_recorded
```

For actor-only evidence:

```trace
actor_only_rule :=
  if evidence == E2_actor_documented:
    max_status := pending_comparator_or_weak_signal
```

For story-only carriers:

```trace
story_only_rule :=
  if source_case_is_story_only:
    max_status := recognition_carrier
```

## Candidate status mapping

```trace
status_after_patch :=
  active_candidate
  OR narrowed_candidate
  OR linked_component
  OR recognition_carrier
  OR demoted
  OR pending_comparator
  OR weak_signal
  OR foundation_carrier
```

New statuses:

- `weak_signal`: some source signal exists, but not enough to support operator status.
- `foundation_carrier`: useful orienting structure, too large or dangerous for active operator promotion.

## Current candidates affected

### Debt Clock

```trace
Debt_Clock_status_after_patch := pending_comparator
```

Reason:

```trace
reason :=
  strong_source_signal_from_Robodebt
  + comparator_required_before_promotion
```

Required next comparator:

```trace
required_comparator :=
  debt_collection_law
  + administrative_review
  + poverty_law
  + consumer_credit
```

### Preservation Love

```trace
Preservation_Love_status_after_patch := foundation_carrier + pending_comparator
```

Reason:

```trace
reason :=
  high_structural_value
  + high_vibe_drift_risk
  + high_boundary_risk
```

Required comparators:

```trace
required_comparator :=
  care_ethics
  + attachment_theory
  + trauma_informed_care
  + palliative_care
  + disability_support
```

### External Memory Scaffold

```trace
External_Memory_Scaffold_status_after_patch := pending_comparator
```

Required comparators:

```trace
required_comparator :=
  memory_studies
  + dementia_care
  + archives
  + identity_continuity_literature
```

### Affection Laundering

```trace
Affection_Laundering_status_after_patch := pending_comparator
```

Required comparators:

```trace
required_comparator :=
  consent_theory
  + coercive_control
  + boundary_psychology
  + care_ethics
```

## Registry guard update

Previous guard:

```trace
registry_guard_old :=
  add_operator_only_if:
    source_case_exists
    + activation_conditions_defined
    + falsifier_defined
    + must_not_claim_defined
```

Updated guard:

```trace
registry_guard_v0_2 :=
  add_operator_only_if:
    source_case_or_source_surface_exists
    + activation_conditions_defined
    + deactivation_conditions_defined
    + home_scale_defined
    + agency_window_effect_defined
    + responsibility_trace_defined
    + affected_subject_scope_defined
    + evidence_grade_defined
    + comparator_defined
    + falsifier_defined
    + demoter_defined
    + boundary_demoters_defined
    + must_not_claim_defined
```

## Anti-metaphor rule

```trace
anti_metaphor_rule :=
  operator_candidate
  cannot_be_promoted
  because:
    story_feels_right
    OR pattern_recurs
    OR phrase_is_beautiful
```

Promotion requires route structure.

```trace
route_structure_required :=
  gate
  OR clock
  OR record
  OR lever
  OR agency_window
  OR responsibility_trace
  OR affected_subject_route
```

## Anti-scale-laundering rule

```trace
anti_scale_laundering_rule :=
  distributed_system
  still_requires:
    role_trace
    + gate_trace
    + record_trace
    + repair_trace
```

Do not let scale erase responsibility.

## Anti-blame-inflation rule

```trace
anti_blame_inflation_rule :=
  responsibility_trace
  must_separate:
    repair_duty
    + role_responsibility
    + liability
    + blame
```

Do not let responsibility analysis become total condemnation.

## Immediate effect on repo workflow

```trace
workflow_after_patch :=
  new_operator_probe
  -> extended_schema_check
  -> comparator_queue
  -> dry_run
  -> demote_or_hold_or_promote
```

No future operator should be promoted directly from a story carrier or a single actor-controlled document.

## What this does not claim

```trace
not_claimed :=
  registry_complete
  OR TRACE_validated
  OR responsibility_solved
  OR free_will_solved
  OR scale_recursion_proves_operator_truth
```

## Next move

```trace
next_move :=
  create_comparator_queue
  for:
    Debt_Clock
    + Preservation_Love
    + External_Memory_Scaffold
    + Affection_Laundering
```

Recommended first comparator queue item:

```trace
first_queue_item := Debt_Clock
```

Plain version:

Before promoting Debt Clock, test it against the fields that may already do the job.
