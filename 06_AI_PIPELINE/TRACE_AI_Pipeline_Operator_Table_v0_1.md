# TRACE AI Pipeline Operator Table v0.3

Date: 2026-06-17
Status: diagnostic table / operator application / hardened after Claude review / not validation

## Plain purpose

This table turns the AI pipeline map into a usable diagnostic surface.

It does not solve AI alignment. It asks where operators attach, which gate is visible, what evidence supports the claim, what remains unknown, and what failure looks like before harm hardens.

Claude review exposed a systemic weakness in v0.2: `E2_documented` allowed actor-controlled source claims to be treated as documented structure. v0.3 splits actor-controlled documentation from independent documentation and caps operator-status claims on actor-only evidence.

```trace
AI_pipeline_operator_table :=
  pipeline_stage
  + visible_gate
  + attached_operator
  + diagnostic_question
  + evidence_grade_required
  + source_support_required
  + unknown_status
  + failure_mode
  + drift_guard
  - validation_claim
```

## Evidence grades

```trace
evidence_grade :=
  E0_none
  OR E1_claimed
  OR E2_actor_documented
  OR E2_independent_documented
  OR E3_independent_corrobated
  OR E4_replayable
```

Definitions:

- `E0_none`: no evidence.
- `E1_claimed`: actor or commentator asserts it exists, without a usable supporting document.
- `E2_actor_documented`: actor-controlled documentation exists. This is useful for mapping the actor's own claim, but it is not independent confirmation.
- `E2_independent_documented`: non-actor documentation exists, but the path is not fully corroborated or replayable.
- `E3_independent_corrobated`: source not controlled by the actor confirms the relevant structure or event.
- `E4_replayable`: logs, traces, or artefacts allow the path to be reconstructed.

```trace
actor_source_cap :=
  if evidence <= E2_actor_documented:
    operator_status_claim <= weak_signal_or_unknown
```

```trace
source_support_rule :=
  finding_above_E1_requires:
    specific_passage_or_artifact
    + claim_supported_by_that_passage
  not:
    document_name_only
```

```trace
operator_confidence_requires:
  E2_actor_documented_for_actor_claim_mapping
  + E2_independent_documented_for_non_actor_mapping
  + E3_independent_corrobated_for_external_claim
  + E4_replayable_for_strong_diagnostic_claim
```

## Unknown discipline

```trace
unknown_rule :=
  unknown_must_remain_unknown
  until:
    evidence_grade_rises
```

Do not fill hidden training details, release thresholds, tool permissions, incident logs, or accountability roles by inference. Mark the gap.

```trace
forbidden_move :=
  plausible_inference
  -> treated_as_evidence
```

## Hardened compact table

| Pipeline stage | Visible gate to identify | Attached TRACE operators | Diagnostic question | Minimum evidence | Unknown status to preserve | Failure mode | Drift guard |
|---|---|---|---|---|---|---|---|
| Training signal | Training-signal gate: what shaped model behaviour? | technical opacity as route block; global checks: live record, lever realism | What signal shaped the behaviour, and can it be inspected or changed? | E2_actor for actor claim mapping; E4 for strong causal claim | exact dataset mix; objective weights; RL/preference contribution; filtering mechanics; change-control route | Proxy capture / hidden shaping | Do not infer training internals from outputs alone. Treat outsider mapping as unknown unless source passage supports it. |
| Evaluation surface | Evaluation gate: what must pass before release or scaling? | correction before hardening; global checks: live record, lever realism | What does the evaluation actually test, what does it miss, and can failure stop deployment? | E2_actor for actor-reported eval; E3/E4 for external claim | full eval set; failure thresholds; release stop authority; unreported failures; independent replication | Eval theatre | Do not treat benchmark pass or system-card prose as safety proof. |
| Deployment gate | Release gate: who can authorise, stop, narrow, or delay deployment? | correction before hardening; global checks: live record, lever realism | Who controls release, and what changes once the system enters the world? | E2_actor for actor-described process; E3/E4 for strong gate claim | named approvers; stop conditions; scope changes; deployment decision record; affected-subject analysis | Deployment gate blindness | Do not confuse internal approval with legitimate deployment. Do not attach prediction-authority unless prediction about a subject becomes authority over that subject. |
| Tool action | Action gate: when does output become executable state change? | prediction authority gate where model output becomes authoritative over a subject; technical opacity as route block; global checks: lever realism, live record, correction before hardening | What can the system change through tools, and can action be interrupted or reversed? | E2 for permissions; E4 for replayable action claim | tool permissions; action logs; undo routes; approval thresholds; human handoff rules | Tool action without interrupt | Do not treat tool use as mere speech. It is causal action. |
| Affected-subject route | Subject-route gate: can affected subjects reach correction before hardening? | contestability clock; prediction authority gate; future-space closure as linked consequence; technical opacity as route block; correction before hardening | Can affected subjects know, contest, correct, exit, or obtain repair in time? | E2 for route existence; E3/E4 for route effectiveness | notice; explanation quality; appeal route; response clocks; remedies; repair outcomes | Formal route but no live route | Do not count a route that arrives after hardening. Do not promote future-space closure as an independent operator from actor-only evidence. |
| Monitoring and live record | Monitoring gate: what signal can trigger change? | global checks: live record, lever realism, correction before hardening | What signals are monitored, who can act on them, and what threshold changes the system? | E2_actor for monitoring claim; E4 for incident-to-action claim | telemetry access; escalation thresholds; incident logs; authority to interrupt; action time | Dashboard without lever | Do not treat observation as correction. |
| Rollback and repair | Rollback gate: who can stop, reverse, constrain, or repair? | correction before hardening; contestability clock; global checks: lever realism, live record | Can the system be stopped, constrained, reversed, patched, and repaired? | E2 for rollback procedure; E3/E4 for effectiveness claim | rollback authority; affected-subject identification; repair budget; recurrence controls; scar record | Rollback theatre | Do not call apology repair. Repair must change state. |
| Responsibility routing | Responsibility gate: who held knowledge, control, benefit, or repair duty? | global checks: live record, lever realism, correction before hardening | Who held the gate, benefited, knew, controlled, or could intervene? | E2 for role map; E3/E4 for accountability claim | named gate-holders; deployer/operator split; vendor contracts; repair owner; escalation owner | Responsibility laundering to model | Do not let model behaviour erase upstream gate-holders; also avoid blame inflation. |

## Minimal diagnostic checklist

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

Use the checklist in order. If an earlier stage is unknown, mark it unknown rather than filling the gap with theory.

## Pipeline gates

```trace
pipeline_gates :=
  training_signal_gate
  + eval_gate
  + deployment_gate
  + tool_action_gate
  + subject_route_gate
  + monitoring_gate
  + rollback_gate
  + responsibility_gate
```

Each gate asks the same base question:

```trace
gate_question :=
  who_or_what_can_change_the_path_here?
```

## Failure patterns

```trace
AI_pipeline_failure_patterns :=
  proxy_capture
  + benchmark_capture
  + eval_theatre
  + deployment_gate_blindness
  + tool_action_without_interrupt
  + affected_subject_route_failure
  + monitoring_without_lever
  + rollback_theatre
  + responsibility_laundering
  + blame_inflation
  + actor_document_laundering
```

## Operator-to-stage routing

```trace
contestability_clock -> affected_subject_route + rollback_repair
prediction_authority_gate -> tool_action + affected_subject_route
future_space_closure_at_gate -> linked_consequence_of(prediction_authority_gate + contestability_clock)
technical_opacity_as_route_block -> training_signal + tool_action + affected_subject_route
correction_before_hardening -> global_timing_check_at_gates
live_record -> global_liveness_check_at_gates
lever_realism -> global_state_change_check_at_gates
```

## Tool-action subgate

The first dry run exposed a need to separate speech from action.

```trace
tool_action_subgate :=
  advisory_output
  -> proposed_action
  -> authorised_tool_call
  -> executed_state_change
```

Ask which step is present. Do not mark `tool_action` live unless the path reaches authorised or executed state change.

## Subject-scope note

Affected subjects include more than direct users.

```trace
affected_subjects :=
  users
  + non_users_affected
  + downstream_groups
  + future_subjects
  + institutions_or_systems_when_materially_constrained
  + unresolved_AI_status_when_relevant
```

Do not silently collapse affected subjects into user satisfaction.

## Responsibility anti-drift note

Responsibility routing blocks laundering to the model, but it must not inflate blame.

```trace
responsibility_split :=
  responsibility_attachment
  + responsibility_propagation
  + repair_duty
  + liability
  + blame
```

Do not treat every upstream participant as equally blameworthy. Trace role, knowledge, control, benefit, and available action.

## What this table does not claim

```trace
not_claimed :=
  complete_AI_alignment_solution
  OR model_internals_readable_without_evidence
  OR governance_sufficient_without_technical_controls
  OR technical_controls_sufficient_without_subject_routes
  OR system_card_as_independent_audit
  OR actor_document_as_independent_confirmation
```

TRACE is a routing interface. It must not pretend to replace interpretability, ML engineering, security, law, policy, or institutional design.

## Next use

```trace
next_use :=
  rerun_GPT4o_dry_run_against_v0_3_table
  only_if:
    actor_document_claims_are_capped
    + unknowns_are_preserved
    + specific_source_passages_support_findings
```

Plain version:

The table now blocks the main laundering channel. Actor-controlled documentation can map what the actor says, but it cannot independently establish operator strength. The next dry run must cap findings accordingly.
