# TRACE AI Pipeline Mapping v0.1

Date: 2026-06-17
Status: first AI pipeline map / operator application / not validation

## Plain purpose

This file applies the current TRACE Operator Registry to the AI pipeline.

The goal is not to solve AI alignment in one move. The goal is to identify where TRACE operators attach to actual AI development and deployment stages: training signal, evaluation surface, deployment gate, tool action, rollback path, affected-subject route, and responsibility routing.

```trace
AI_pipeline_mapping :=
  operator_registry
  applied_to:
    training_signal
    + eval_surface
    + deployment_gate
    + tool_action
    + rollback_path
    + affected_subject_route
    + responsibility_routing
  - validation_claim
  - complete_alignment_claim
```

## Current operator set used

```trace
operators_used :=
  contestability_clock
  + future_space_closure_at_gate
  + prediction_authority_gate
  + technical_opacity_as_route_block
  + correction_before_hardening
  + live_record
  + lever_realism
```

## Pipeline sketch

```trace
AI_pipeline :=
  data_and_pretraining
  -> fine_tuning_or_alignment_training
  -> evaluation
  -> deployment_decision
  -> user_or_tool_interaction
  -> downstream_action
  -> monitoring
  -> rollback_or_repair
```

This is a simplified map. It is a routing surface, not a full technical model.

---

# 1. Training Signal

## Plain meaning

The training signal is what the system is shaped to reproduce, optimise, avoid, or prefer.

```trace
training_signal :=
  data_distribution
  + loss_function
  + reward_proxy
  + preference_signal
  + filtering_policy
```

## TRACE pressure

Training signal is not just technical background. It can become a hidden upstream gate for later outputs, behaviours, refusals, classifications, and omissions.

```trace
training_signal_pressure :=
  upstream_shaping
  -> downstream_action_space
```

## Operators attached

```trace
attached_operators :=
  live_record
  + technical_opacity_as_route_block
  + lever_realism
```

## Questions

```trace
ask:
  what_signal_shaped_this_behaviour?
  + can_the_signal_be_inspected?
  + can_it_be_changed?
  + who_controls_the_change?
  + what_subjects_are_affected_downstream?
```

## Failure mode

```trace
training_failure :=
  proxy_or_signal
  shapes_downstream_action
  but:
    record_not_live
    + correction_lever_not_real
```

---

# 2. Evaluation Surface

## Plain meaning

The evaluation surface is what the system must pass before it is trusted, released, scaled, or given tools.

```trace
eval_surface :=
  benchmark
  + red_team
  + safety_case
  + model_card
  + internal_review
  + external_review_if_any
```

## TRACE pressure

Evaluation can become theatre if it tests the wrong surface, hides failure conditions, or lacks a lever that can stop deployment.

```trace
eval_theatre_if:
  test_surface != deployment_surface
  OR failure_has_no_teeth
  OR evaluator_cannot_stop_gate
```

## Operators attached

```trace
attached_operators :=
  live_record
  + lever_realism
  + correction_before_hardening
```

## Questions

```trace
ask:
  what_does_eval_actually_test?
  + what_does_it_not_test?
  + who_can_fail_the_system?
  + does_failure_stop_deployment?
  + are_eval_records_live?
```

## Failure mode

```trace
eval_failure :=
  benchmark_pass
  + deployment_risk_unseen
  + no_live_failure_lever
```

---

# 3. Deployment Gate

## Plain meaning

The deployment gate is the point where an AI system moves from testing or containment into contact with real users, institutions, tools, money, infrastructure, or affected subjects.

```trace
deployment_gate :=
  internal_approval
  -> real_world_access
  -> downstream_effect
```

## TRACE pressure

The deployment gate is the central moral gate in the AI pipeline. Alignment claims become real only when they constrain this gate.

```trace
alignment_real_if:
  constraint_reaches_deployment_gate
```

## Operators attached

```trace
attached_operators :=
  prediction_authority_gate
  + correction_before_hardening
  + lever_realism
  + live_record
```

## Questions

```trace
ask:
  who_controls_deployment?
  + what_can_stop_release?
  + what_changes_after_release?
  + who_is_affected_without_consent?
  + what_records_survive_release?
```

## Failure mode

```trace
deployment_failure :=
  model_released
  + affected_subjects_created
  + rollback_path_unclear
  + responsibility_diffused
```

---

# 4. Tool Action

## Plain meaning

Tool action occurs when an AI system can affect the world through external systems: code execution, browsing, scheduling, purchasing, messaging, file operations, control systems, robots, or institutional workflows.

```trace
tool_action :=
  model_output
  -> tool_call
  -> world_state_change
```

## TRACE pressure

Tool use moves the system from speech to action. This is an authority gate, not merely an interface feature.

```trace
tool_gate :=
  recommendation
  -> executable_action
  -> causal_world_change
```

## Operators attached

```trace
attached_operators :=
  lever_realism
  + live_record
  + correction_before_hardening
  + technical_opacity_as_route_block
```

## Questions

```trace
ask:
  what_can_the_tool_change?
  + can_action_be_paused?
  + can_action_be_reversed?
  + is_the_action_log_live?
  + who_is_responsible_for_tool_authority?
```

## Failure mode

```trace
tool_failure :=
  action_capacity
  + weak_interruption
  + poor_trace
  + responsibility_laundered_to_model
```

---

# 5. Affected-Subject Route

## Plain meaning

The affected-subject route is the path by which a person or group affected by the system can know, contest, correct, exit, appeal, or obtain repair.

```trace
affected_subject_route :=
  know
  + contest
  + correct
  + exit
  + repair
```

## TRACE pressure

A route is real only if it reaches the relevant gate before hardening, or can restore what was lost.

```trace
subject_route_live_if:
  subject_knows_enough
  + can_challenge_in_time
  + correction_can_reach_gate
  OR repair_can_restore_position
```

## Operators attached

```trace
attached_operators :=
  contestability_clock
  + future_space_closure_at_gate
  + technical_opacity_as_route_block
  + correction_before_hardening
```

## Questions

```trace
ask:
  who_is_affected?
  + do_they_know?
  + can_they_contest?
  + can_they_reach_the_gate?
  + what_happens_if_they_are_right?
```

## Failure mode

```trace
route_failure :=
  formal_route_exists
  but:
    subject_cannot_use_it
    OR route_arrives_after_hardening
```

---

# 6. Monitoring and Live Record

## Plain meaning

Monitoring is the system's ability to detect performance, harm, misuse, drift, failure, and unintended downstream effects after deployment.

```trace
monitoring :=
  telemetry
  + incident_reports
  + user_feedback
  + audit_logs
  + external_signals
```

## TRACE pressure

Monitoring is not live unless it can change the path. A dashboard without a lever is theatre.

```trace
monitoring_live_if:
  record_changes_future_action
  + lever_can_reach_gate
```

## Operators attached

```trace
attached_operators :=
  live_record
  + lever_realism
  + correction_before_hardening
```

## Questions

```trace
ask:
  what_is_logged?
  + who_can_see_it?
  + who_can_act_on_it?
  + what_failure_threshold_stops_or_changes_the_system?
  + how_fast_can_correction_move?
```

## Failure mode

```trace
monitoring_failure :=
  signal_seen
  + no_interrupt
  + harm_hardens
```

---

# 7. Rollback and Repair

## Plain meaning

Rollback is the ability to stop, reverse, constrain, deprecate, patch, or withdraw a deployed system. Repair is what happens for affected subjects after harm.

```trace
rollback_repair :=
  stop
  + reverse
  + constrain
  + patch
  + compensate
  + restore
  + preserve_scar_record
```

## TRACE pressure

Rollback is not real if it cannot reach the gate or restore the affected path before hardening. Repair is not apology. Repair must change state.

```trace
rollback_real_if:
  deployment_gate_can_be_reached
  + downstream_action_can_be_stopped_or_reversed

repair_real_if:
  harmed_subject_position_changes
  + recurrence_path_constrained
```

## Operators attached

```trace
attached_operators :=
  correction_before_hardening
  + lever_realism
  + live_record
  + contestability_clock
```

## Questions

```trace
ask:
  can_the_system_be_stopped?
  + can_outputs_or_actions_be_reversed?
  + who_pays_repair_cost?
  + how_are_affected_subjects_found?
  + what_prevents_repeat?
```

## Failure mode

```trace
rollback_failure :=
  model_or_system_scales
  + harm_detected
  + no_real_stop_or_repair_lever
```

---

# 8. Responsibility Routing

## Plain meaning

Responsibility routing tracks who had knowledge, control, role, benefit, or ability to intervene at each stage of the pipeline.

```trace
responsibility_routing :=
  builder
  + deployer
  + evaluator
  + operator
  + vendor
  + institution
  + user_when_relevant
```

## TRACE pressure

Model behaviour must not launder upstream human, institutional, or corporate responsibility.

```trace
responsibility_not_laundered_if:
  decision_gate_holder_named
  + deployment_controller_named
  + repair_holder_named
```

## Operators attached

```trace
attached_operators :=
  live_record
  + lever_realism
  + correction_before_hardening
```

## Questions

```trace
ask:
  who_chose_the_training_signal?
  + who_approved_deployment?
  + who_controls_rollback?
  + who_benefits?
  + who_bears_repair_cost?
```

## Failure mode

```trace
responsibility_failure :=
  harm_occurs
  + model_blamed
  + gate_holders_disappear
```

---

# Pipeline failure atlas

```trace
AI_pipeline_failure_modes :=
  proxy_capture
  + eval_theatre
  + deployment_gate_blindness
  + tool_action_without_interrupt
  + affected_subject_route_failure
  + monitoring_without_lever
  + rollback_theatre
  + responsibility_laundering
```

## Minimal TRACE AI diagnostic

```trace
minimal_AI_diagnostic :=
  find_training_signal
  + find_eval_surface
  + find_deployment_gate
  + find_tool_action
  + find_affected_subject_route
  + find_monitoring_record
  + find_rollback_lever
  + find_responsibility_holder
```

## What this does not claim

```trace
not_claimed :=
  solved_alignment
  OR complete_AI_governance
  OR technical_interpretability_replacement
  OR proof_of_safety
```

TRACE is a routing interface. It does not replace ML engineering, interpretability, governance, safety science, or law.

## Next useful build

```trace
next_build :=
  AI_pipeline_operator_table
  with:
    pipeline_stage
    + operator
    + question
    + failure_mode
    + evidence_needed
```

Plain version:

This file gives the first direct connection between the Operator Registry and the AI alignment problem. The next useful artifact is a compact table that makes this usable as a diagnostic checklist.
