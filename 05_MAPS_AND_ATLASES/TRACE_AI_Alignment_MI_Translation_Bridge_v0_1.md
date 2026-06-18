# TRACE AI Alignment / Mechanistic Interpretability Translation Bridge v0.1

Date: 2026-06-18
Status: cross-domain translation bridge / not active operator / not validation / not proof / not Kernel v0.3

## 0. Control header

This file records the relationship between AI alignment and mechanistic interpretability inside TRACE.

It does not solve AI alignment.

It does not solve mechanistic interpretability.

It does not claim model interpretation equals control.

It does not claim evaluation equals correction.

It does not promote a new operator.

It does not validate TRACE.

```trace
bridge_scope :=
  AI_alignment
  + mechanistic_interpretability
  + deployment_hardening
  + internal_evidence_channel
  + correction_carrier
  + affected_subject_contestability
  - operator_promotion
  - validation
  - Kernel_v0_3
```

## 1. Plain compression

AI alignment is about whether model behaviour remains acceptably constrained under deployment, power, incentives, uncertainty, and adversarial pressure.

Mechanistic interpretability is about whether internal model mechanisms can be made legible enough to support causal understanding, prediction, intervention, or control.

TRACE does not replace either field.

TRACE provides an interlingua between them:

```trace
TRACE_bridge_question :=
  does_internal_evidence
  change_deployment_correction
  before_harm_hardens?
```

Plain version:

Interpretability matters to alignment only when it changes what can be prevented, paused, rolled back, corrected, or contested before deployment hardens harm.

## 2. Separation rule

AI alignment and mechanistic interpretability should not be collapsed.

```trace
AI_alignment_focus :=
  deployment_governance
  + model_action_under_power
  + rollback_or_pause_carrier
  + affected_subject_contestability
  + corrigibility_under_pressure

MI_focus :=
  internal_evidence_channel
  + feature_or_circuit
  + causal_role
  + intervention_point
  + uncertainty_reduction
  + mechanism_boundary
```

Separation rule:

```trace
MI != alignment
alignment != MI
interpretability != accountability
explanation != control
control != repair
```

## 3. Bridge rule

The bridge exists only if mechanistic insight changes the correction structure.

```trace
AI_MI_bridge_exists_if :=
  internal_mechanistic_evidence
  changes:
    detection
    OR prevention
    OR deployment_gate
    OR rollback
    OR monitoring
    OR contestability
    OR repair
  before:
    deployment_hardening
```

Demoter:

```trace
demote_AI_MI_bridge_if :=
  MI_explanation_does_not_change_intervention_or_correction_window
  OR alignment_process_does_not_use_MI_evidence
  OR interpretation_is_only_post_hoc_story
  OR evidence_channel_cannot_be_replayed_or_contested
```

## 4. Clock / carrier translation

AI alignment speaks in terms of deployment risk, evals, monitoring, rollback, oversight, refusal, control, and safety cases.

Mechanistic interpretability speaks in terms of features, circuits, activations, ablations, causal roles, probes, and interventions.

TRACE translates both into clock/carrier structure.

```trace
AI_alignment_clock_carrier :=
  hardening_clock:
    deployment_release
    + user_exposure
    + automation_dependency
    + scaling
    + institutional_reliance
  correction_clock:
    detection
    + shutdown
    + rollback
    + model_update
    + user_notice
    + repair
  carrier:
    deployment_gate
    + monitoring
    + incident_response
    + rollback_authority
    + audit_log
    + affected_user_contest_route
```

```trace
MI_clock_carrier :=
  hardening_clock:
    model_capability_deployment
    + opaque_behavior_normalisation
    + automated_action_chain
    + monitoring_gap
  correction_clock:
    mechanistic_detection
    + causal_intervention
    + feature_suppression_or_steering
    + eval_update
    + deployment_policy_update
  carrier:
    reproducible_probe
    + causal_ablation
    + intervention_hook
    + safety_case_linkage
    + deployment_gate_authority
```

Bridge compression:

```trace
AI_MI_translation :=
  MI_evidence
  must_attach_to:
    AI_alignment_carrier
  before:
    deployment_hardening_clock_closes
```

## 5. Model-internal evidence channel

Mechanistic interpretability can function as a witness channel only under constraints.

```trace
MI_as_witness_channel :=
  internal_signal
  + reproducible_method
  + causal_test
  + intervention_link
  + record_surface
  + uncertainty_statement
```

But:

```trace
MI_witness_failure :=
  cherry_picked_feature
  OR noncausal_probe
  OR unreproducible_attribution
  OR explanation_without_intervention
  OR internal_story_used_to_launder_deployment
```

Plain version:

A feature name is not a safety argument. A mechanistic story becomes relevant only when it survives causal pressure and connects to a real intervention or gate.

## 6. Alignment carrier layer

AI alignment needs carriers: actual mechanisms that make safety constraints real in deployment.

```trace
alignment_carriers :=
  eval_gate
  + deployment_pause
  + staged_rollout
  + monitoring
  + incident_response
  + rollback_authority
  + external_audit
  + affected_subject_contest_route
  + refusal_boundary
  + model_update_or_retraining_path
```

Carrier failure:

```trace
alignment_carrier_failure :=
  eval_passes_but_no_deployment_gate
  OR monitoring_detects_but_no_pause_power
  OR rollback_exists_but_after_harm_hardens
  OR audit_finds_issue_but_no_enforcement
  OR user_reports_harm_but_no_repair_path
```

## 7. Affected subject / user surface

AI alignment can become model-centric and forget the harmed subject.

TRACE keeps this surface visible.

```trace
affected_surface :=
  user
  + non_user_subject
  + downstream_affected_party
  + institution_relying_on_model
  + public_record_or_environment
```

Key question:

```trace
subject_question :=
  who_can_be_harmed
  + who_can_notice
  + who_can_contest
  + who_can_trigger_pause_or_repair
```

Must-not-claim:

```trace
must_not_claim :=
  model_alignment_metric_equals_subject_safety
  OR user_satisfaction_equals_harm_absence
  OR eval_success_equals_real_world_correction
```

## 8. Translation ladder

```trace
AI_MI_translation_ladder :=
  L0_shared_terms:
    risk
    + evidence
    + intervention
    + deployment
  L1_TRACE_translation:
    hardening_clock
    + correction_clock
    + carrier
    + subject_surface
  L2_worked_case:
    ordinary_AI_or_MI_read
    + TRACE_read
    + explicit_delta_or_demote
  L3_formal_check:
    t_c < t_h
    + carrier_real
    + intervention_link
  L4_possible_support_check:
    only_if_multiple_cases_repeat_useful_navigation_delta
```

No jump from concept to operator.

## 9. Candidate worked delta types

Good candidate tests:

```trace
AI_MI_worked_delta_candidates :=
  mechanistic_interpretability_case_with_real_intervention_point
  + deployment_failure_where_internal_monitor_or_eval_could_have_changed_gate
  + model_behavior_case_where_MI_claim_failed_to_change_safety_decision
  + red_team_finding_with_or_without_mechanistic_explanation
```

Selection rule:

```trace
select_case_if :=
  public_source_record
  + clear_ordinary_AI_or_MI_comparator
  + explicit_intervention_or_gate_question
  + TRACE_can_fail
```

Avoid:

```trace
avoid_case_if :=
  hype_only
  OR no_public_source_record
  OR no_intervention_point
  OR MI_claim_only_illustrative
  OR alignment_claim_only_marketing
```

## 10. What TRACE may add

Possible TRACE addition:

```trace
TRACE_possible_addition :=
  connect_internal_mechanism
  to:
    deployment_gate
    + rollback_carrier
    + affected_subject_contestability
    + hardening_clock
```

But:

```trace
TRACE_does_not_add :=
  better_MI_method
  OR better_alignment_metric
  OR proof_of_model_safety
  OR personhood_solution
```

## 11. Demoters

```trace
demote_bridge_if :=
  AI_safety_framework_already_links_evidence_to_deployment_gate_better
  OR MI_field_already_links_mechanism_to_intervention_better
  OR TRACE_only_renames_existing_assurance_case_language
  OR no_worked_delta_shows_navigation_gain
```

Hard stop:

```trace
hard_stop :=
  using_TRACE_to_skip_AI_safety_detail
  OR using_TRACE_to_skip_MI_causal_detail
  OR claiming_interpretability_equals_alignment
  OR claiming_alignment_solved_by_clock_carrier_note
```

## 12. Final compression

```trace
AI_MI_Translation_Bridge_v0_1 :=
  AI_alignment_as_deployment_correction_problem
  + MI_as_internal_evidence_intervention_problem
  + TRACE_as_interlingua_between_them:
      internal_evidence
      -> carrier
      -> correction_before_deployment_hardening
      -> affected_subject_contestability
  - operator
  - validation
  - alignment_solution
  - MI_solution
```

Plain conclusion:

AI alignment and mechanistic interpretability meet when internal evidence changes real deployment correction. TRACE’s role is to keep the bridge honest: what is the mechanism, what intervention does it support, what carrier makes that intervention real, and does it happen before harm hardens?

End.
