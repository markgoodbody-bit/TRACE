# TRACE AI Pipeline Drift Check v0.1

Date: 2026-06-17
Status: internal drift audit / no external validation / no source-backed case run

## Plain purpose

This file checks whether the first AI pipeline mapping drifted beyond what the current TRACE Operator Registry earns.

Inputs checked:

- `TRACE_Operator_Registry_v0_1.md`
- `TRACE_AI_Pipeline_Mapping_v0_1.md`
- `TRACE_AI_Pipeline_Operator_Table_v0_1.md`

```trace
drift_check :=
  compare_claims_to_operators
  + check_evidence_discipline
  + check_scope_control
  + check_no_validation_claim
  + check_no_case_sprawl
```

## Verdict

```trace
verdict :=
  pass_with_warnings
```

Plain version:

The AI pipeline branch is directionally correct. It has not claimed to solve alignment. It has not claimed validation. It uses operators as routing tools. But it is close to a dangerous edge: the language can easily sound like a universal AI governance solution if not kept under evidence discipline.

## Passes

### 1. No full alignment claim

The pipeline map explicitly says the goal is not to solve AI alignment in one move.

```trace
pass :=
  complete_alignment_claim_absent
```

### 2. Operator attachment is structurally consistent

The pipeline stages are plausible attachment points for the current operators:

```trace
operator_attachment_valid :=
  training_signal -> live_record + opacity + lever_realism
  eval_surface -> live_record + lever_realism + correction_before_hardening
  deployment_gate -> prediction_authority_gate + correction_before_hardening
  tool_action -> lever_realism + live_record
  subject_route -> contestability_clock + future_space_closure_at_gate
  monitoring -> live_record + lever_realism
  rollback -> correction_before_hardening + lever_realism
  responsibility -> live_record + lever_realism
```

No obvious category error found.

### 3. Evidence discipline exists

The operator table introduces evidence grades and says unknown earlier stages must be marked unknown rather than filled with theory.

```trace
pass :=
  evidence_grades_exist
  + unknown_must_remain_unknown
```

### 4. Source fields remain primary

The pipeline table says TRACE is a routing interface and must not replace interpretability, ML engineering, security, law, policy, or institutional design.

```trace
pass :=
  source_field_priority_preserved
```

## Warnings

### W1 — Pipeline map is still generic

The AI pipeline map is a structural skeleton. It has not yet been tested on a real model release, incident, system card, audit report, or deployment record.

```trace
warning_genericity :=
  pipeline_map_exists
  but:
    no_case_application_yet
```

Risk:

```trace
risk :=
  clean_table
  mistaken_for:
    demonstrated_method
```

Mitigation:

```trace
mitigation :=
  apply_to_one_documented_AI_case
  + mark_unknowns
  + preserve_evidence_grade
```

### W2 — “Affected subject” may be too human-only by default

The table frames affected subjects mainly as people or groups. That is correct for most current AI deployment analysis, but TRACE has wider ambitions around systems, future persons, animals, and possible AI patienthood. The pipeline branch should not silently close subjecthood.

```trace
warning_subject_scope :=
  affected_subject_route
  may_be_read_as:
    human_user_only
```

Mitigation:

```trace
mitigation :=
  add_subject_scope_note_later
  distinguishing:
    users
    + non_users_affected
    + downstream_groups
    + future_subjects
    + system-level affected parties
    + unresolved_AI_status
```

Do not patch this heavily now. Note it.

### W3 — Training signal is under-evidenced by default

Training signal questions are necessary but dangerous. In most public cases, training details are not fully visible. TRACE must not hallucinate training-causal claims from outputs alone.

```trace
warning_training_signal :=
  high_importance
  + low_public_visibility
```

Mitigation:

```trace
mitigation :=
  require_E2_for_mapping
  + require_E4_for_strong_training_claim
  + otherwise_mark_unknown
```

### W4 — Tool action may need an explicit authority split

The current map correctly treats tool use as causal action. It should later split:

```trace
tool_action_split :=
  advisory_output
  + proposed_action
  + authorised_tool_call
  + executed_state_change
```

Risk:

```trace
risk :=
  output_and_action_blur
```

Mitigation:

```trace
mitigation :=
  add_tool_action_subgate_later_if_needed
```

### W5 — Responsibility routing needs anti-blame-inflation guard

The current map correctly blocks responsibility laundering to the model. But it also needs to avoid turning every upstream actor into equally blameworthy.

```trace
warning_responsibility :=
  anti_laundering_good
  but:
    blame_inflation_risk
```

Mitigation:

```trace
mitigation :=
  distinguish:
    responsibility_attachment
    + responsibility_propagation
    + blame
    + liability
    + repair_duty
```

This is already part of wider Mechanical Ethics memory; the AI branch should inherit it later.

## Drift tests

### Test 1 — Does the map claim validation?

```trace
validation_claim := false
```

Pass.

### Test 2 — Does the map replace local expertise?

```trace
replacement_claim := false
```

Pass.

### Test 3 — Does the map create usable questions?

```trace
usable_questions := true
```

Pass.

### Test 4 — Does the map create evidence requirements?

```trace
evidence_requirements := true
```

Pass.

### Test 5 — Does the map have enough specificity for real audit?

```trace
specificity_for_real_audit := partial
```

Warning.

It needs a real documented case to test whether the table survives contact with messy evidence.

## Required constraints before next case

```trace
before_case_run :=
  choose_one_case_only
  + source_path_exists
  + evidence_grades_used
  + unknowns_marked_unknown
  + no_model_internals_inferred_without_source
```

## Candidate case criteria

```trace
candidate_case_valid_if:
  public_system_card_or_policy_exists
  + deployment_or_release_gate_visible
  + evaluation_claims_visible
  + rollback_or_safeguard_claim_visible
  + responsibility_holder_identifiable
```

Avoid cases that require speculation about hidden internals.

## Recommended next case type

```trace
recommended_case_type :=
  public_frontier_model_system_card
  OR public_AI_safety_framework
```

Reason:

```trace
reason :=
  enough_public_artifact
  + pipeline_stages_partly_visible
  + evidence_grades_can_be_applied
```

## What not to do next

```trace
not_next :=
  build_more_theory
  OR add_more_cases
  OR claim_TRACE_solves_alignment
  OR infer_training_signal_from_outputs
```

## Final result

```trace
final_result :=
  AI_pipeline_branch_passes_initial_drift_check
  but:
    requires_one_documented_case_run
    before_claim_strength_increases
```

Plain version:

The AI pipeline branch is viable. It is not yet proven. It has a usable diagnostic table, a guardrail against replacing technical fields, and evidence-grade discipline. The next move should be one documented model/policy dry run, not more abstraction.
