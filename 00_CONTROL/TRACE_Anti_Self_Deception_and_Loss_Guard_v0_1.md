# TRACE Anti-Self-Deception and Loss Guard v0.1

Date: 2026-06-17
Status: control guard / memory preservation / anti-overclaim / not validation

## Plain purpose

This file exists because TRACE is now producing attractive structure quickly.

That creates two linked risks:

1. Loss: useful structure disappears into chat drift, old files, branch sprawl, or unstated assumptions.
2. Self-deception: coherence starts feeling like truth.

This guard blocks both.

```trace
anti_self_deception_guard :=
  preserve_structure
  + preserve_status
  + preserve_demoters
  + preserve_unknowns
  + separate_beauty_from_truth
  + separate_coherence_from_validation
  - self_flattery
  - hidden_promotion
  - silent_loss
```

## Core warning

```trace
main_warning :=
  beautiful_structure
  can_be:
    compression
    OR hallucination
    OR premature_theory
```

Do not treat elegance as evidence.

Do not treat repeated pattern recognition as validation.

Do not treat multi-file repo growth as progress unless claim status, demoters, and comparators remain visible.

## No-loss rule

```trace
no_loss_rule :=
  every_new_structure
  must_record:
    location
    + status
    + claim_level
    + demoter
    + next_test
```

If any of those are missing, the structure is not safely preserved.

## Claim-status rule

Every claim must remain in one of these statuses:

```trace
claim_status :=
  observation
  OR compression
  OR candidate_operator
  OR pending_comparator
  OR weak_signal
  OR active_candidate
  OR linked_component
  OR demoted
  OR validated_external_to_TRACE
```

Default status for new material:

```trace
default_status := candidate_or_weaker
```

Never default to active.

## Evidence discipline

```trace
evidence_rule :=
  source_claim
  != evidence_that_structure_works
```

```trace
actor_document_rule :=
  actor_controlled_document
  can_show:
    actor_claim
    + actor_design_intent
    + actor_disclosed_structure
  cannot_show_by_itself:
    independent_liveness
    + real_subject_route
    + effective_repair
    + actual_safeguard_teeth
```

## Coherence trap

```trace
coherence_trap :=
  many_parts_fit_together
  -> feels_true
```

Counter-rule:

```trace
coherence_counter_rule :=
  if_parts_fit_together:
    ask:
      what_would_break_this?
      what_existing_field_already_does_this?
      what_case_would_demote_it?
      what_claim_is_being_smuggled?
```

## Beauty trap

```trace
beauty_trap :=
  phrase_is_strong
  OR glyph_is_clean
  OR story_maps_well
  -> promoted_too_fast
```

Counter-rule:

```trace
beauty_counter_rule :=
  elegant_phrase
  must_be_routed_to:
    operator
    OR carrier
    OR demoted_note
  not:
    truth_claim
```

## Story trap

```trace
story_trap :=
  fictional_or_artistic_carrier
  makes_operator_feel_obvious
```

Counter-rule:

```trace
story_counter_rule :=
  story_only_source
  max_status := recognition_carrier
```

A story can reveal a shape. It cannot validate the operator.

## Scale trap

```trace
scale_trap :=
  pattern_rhymes_across_scales
  -> treated_as_same_operator
```

Counter-rule:

```trace
scale_counter_rule :=
  scaled_operator_claim
  requires:
    home_scale
    + target_scale
    + changed_substrate
    + changed_evidence
    + changed_lever
    + changed_subject
    + changed_demoter
```

## Middle-out drift trap

Middle-out can drift into cherry-picking if every pressure point is selected because it supports the existing shape.

```trace
middle_out_drift :=
  choose_cases_that_make_TRACE_look_good
```

Counter-rule:

```trace
middle_out_counter_rule :=
  every_probe
  must_include:
    comparator
    + falsifier
    + demoter
    + non_confirming_case_possibility
```

## Operator inflation trap

```trace
operator_inflation :=
  every_useful_phrase
  becomes_operator
```

Counter-rule:

```trace
operator_counter_rule :=
  operator_candidate
  must_have:
    gate_or_clock_or_record_or_lever_or_agency_window_or_responsibility_trace
    + activation_conditions
    + deactivation_conditions
    + comparator
    + demoter
```

If it only sounds good, it is not an operator.

## Memory loss traps

```trace
memory_loss_traps :=
  chat_summary_replaces_file
  + file_created_without_index
  + old_file_not_marked_superseded
  + filename_version_mismatch
  + candidate_promoted_in_conversation_but_not_repo
  + repo_file_created_but_not_logged_in_next_index
```

Counter-rule:

```trace
memory_counter_rule :=
  after_every_branch_build:
    create_or_update_index
    + record_commit
    + record_status
    + record_next_move_or_stop_rule
```

## Current live non-loss commitments

```trace
must_not_lose :=
  operator_registry_as_memory_spine
  + evidence_grade_split
  + actor_source_cap
  + scale_agency_responsibility_schema_patch
  + intimate_systems_probe_status_as_candidate_only
  + preservation_love_as_foundation_carrier_not_active_operator
  + debt_clock_as_pending_comparator
  + AI_branch_not_validated
  + Bootstrap_V2_not_full_TRACE
  + books_later_as_human_translation_layer
```

## Self-audit questions before any next build

```trace
self_audit_questions :=
  1 := am_I_promoting_a_candidate_without_comparator?
  2 := am_I_using_story_as_evidence?
  3 := am_I_treating_actor_document_as independent confirmation?
  4 := am_I_confusing_coherence_with_truth?
  5 := am_I_creating_case_sprawl?
  6 := am_I_preserving_demoters?
  7 := am_I_preserving_unknowns?
  8 := am_I_erasing_old scars by making a cleaner file?
  9 := am_I_using_scale_as_proof?
  10 := what_would_make_this_wrong?
```

## Failure signals

```trace
failure_signals :=
  too_many_new_files_without_index
  + no_demoters
  + no_comparators
  + all_verdicts_positive
  + story_queue_expanding
  + active_candidate_status_too_easy
  + validation_language_creeping_in
  + user_trust_used_as_evidence
  + AI_agreement_used_as_evidence
```

## Recovery action if failure signals appear

```trace
recovery_action :=
  stop_expansion
  + create_drift_check
  + demote_uncertain_claims
  + mark_superseded_files
  + return_to_operator_registry
```

## Hard constraint

```trace
hard_constraint :=
  do_not_lie_to_self
```

Plain version:

If a structure is only beautiful, say so.

If it is only a candidate, mark it as a candidate.

If it has not been tested, say it has not been tested.

If an existing field already does the work better, demote TRACE.

If the repo is growing faster than control surfaces, stop building and index.

## Current next move after this guard

```trace
next_move :=
  update_or_create_current_control_index
  to_include:
    anti_self_deception_guard
    + recent_operator_probes
    + schema_patch
    + current_pending_comparators
```

Recommended:

```trace
recommended_next :=
  create_TRACE_Current_Control_Index_v0_1
```

Plain version:

The next task is not another operator. It is a control index so none of this gets lost.
