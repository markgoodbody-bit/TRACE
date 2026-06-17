# TRACE AI Pipeline Operator Table v0.2

Date: 2026-06-17
Status: diagnostic table / operator application / hardened after first dry run / not validation

## Plain purpose

This table turns the first AI pipeline map into a usable diagnostic surface.

It does not solve AI alignment. It asks where operators attach, which gate is visible, what evidence is needed, what remains unknown, and what failure looks like before harm hardens.

```trace
AI_pipeline_operator_table :=
  pipeline_stage
  + visible_gate
  + attached_operator
  + diagnostic_question
  + evidence_grade_required
  + unknown_status
  + failure_mode
  + drift_guard
  - validation_claim
```

## Hardened compact table

| Pipeline stage | Visible gate to identify | Attached TRACE operators | Diagnostic question | Minimum evidence | Unknown status to preserve | Failure mode | Drift guard |
|---|---|---|---|---|---|---|---|
| Training signal | Training-signal gate: what shaped model behaviour? | live record; technical opacity as route block; lever realism | What signal shaped the behaviour, and can it be inspected or changed? | E2 for mapping; E4 for strong causal claim | exact dataset mix; objective weights; RL/preference contribution; filtering mechanics; change-control route | Proxy capture / hidden shaping | Do not infer training internals from outputs alone. |
| Evaluation surface | Evaluation gate: what must pass before release or scaling? | live record; lever realism; correction before hardening | What does the evaluation actually test, what does it miss, and can failure stop deployment? | E2 for mapping; E3/E4 for strong external claim | full eval set; failure thresholds; release stop authority; unreported failures; independent replication | Eval theatre | Do not treat benchmark pass or system-card prose as safety proof. |
| Deployment gate | Release gate: who can authorise, stop, narrow, or delay deployment? | prediction authority gate; correction before hardening; lever realism; live record | Who controls release, and what changes once the system enters the world? | E2 for mapping; E3 for external claim | named approvers; stop conditions; scope changes; deployment decision record; affected-subject analysis | Deployment gate blindness | Do not confuse internal approval with legitimate deployment. |
| Tool action | Action gate: when does output become executable state change? | lever realism; live record; correction before hardening; technical opacity as route block | What can the system change through tools, and can action be interrupted or reversed? | E2 for permissions; E4 for replayable action claim | tool permissions; action logs; undo routes; approval thresholds; human handoff rules | Tool action without interrupt | Do not treat tool use as mere speech. It is causal action. |
| Affected-subject route | Subject-route gate: can affected subjects reach correction before hardening? | contestability clock; future-space closure at gate; technical opacity as route block; correction before hardening | Can affected subjects know, contest, correct, exit, or obtain repair in time? | E2 for route existence; E3/E4 for route effectiveness | notice; explanation quality; appeal route; response clocks; remedies; repair outcomes | Formal route but no live route | Do not count a route that arrives after hardening. |
| Monitoring and live record | Monitoring gate: what signal can trigger change? | live record; lever realism; correction before hardening | What signals are monitored, who can act on them, and what threshold changes the system? | E2 for monitoring claim; E4 for incident-to-action claim | telemetry access; escalation thresholds; incident logs; authority to interrupt; action time | Dashboard without lever | Do not treat observation as correction. |
| Rollback and repair | Rollback gate: who can stop, reverse, constrain, or repair? | correction before hardening; lever realism; live record; contestability clock | Can the system be stopped, constrained, reversed, patched, and repaired? | E2 for rollback procedure; E3/E4 for effectiveness claim | rollback authority; affected-subject identification; repair budget; recurrence controls; scar record | Rollback theatre | Do not call apology repair. Repair must change state. |
| Responsibility routing | Responsibility gate: who held knowledge, control, benefit, or repair duty? | live record; lever realism; correction before hardening | Who held the gate, benefited, knew, controlled, or could intervene? | E2 for role map; E3/E4 for accountability claim | named gate-holders; deployer/operator split; vendor contracts; repair owner; escalation owner | Responsibility laundering to model | Do not let model behaviour erase upstream gate-holders; also avoid blame inflation. |

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

## Evidence grades

```trace
evidence_grade :=
  E0_none
  OR E1_claimed
  OR E2_documented
  OR E3_independent
  OR E4_replayable
```

Definitions:

- `E0_none`: no evidence.
- `E1_claimed`: actor says it exists.
- `E2_documented`: internal or public document exists.
- `E3_independent`: source not controlled by the actor confirms it.
- `E4_replayable`: logs, traces, or artefacts allow the path to be reconstructed.

```trace
operator_confidence_requires:
  at_least_E2_for_mapping
  + at_least_E3_for_external_claim
  + E4_for_strong_diagnostic_claim
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
```

## Operator-to-stage routing

```trace
contestability_clock -> affected_subject_route + rollback_repair
future_space_closure_at_gate -> deployment_gate + affected_subject_route
prediction_authority_gate -> deployment_gate + tool_action + affected_subject_route
technical_opacity_as_route_block -> training_signal + tool_action + affected_subject_route
correction_before_hardening -> evaluation + deployment_gate + monitoring + rollback
live_record -> training_signal + evaluation + monitoring + responsibility_routing
lever_realism -> evaluation + deployment_gate + tool_action + rollback
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
```

TRACE is a routing interface. It must not pretend to replace interpretability, ML engineering, security, law, policy, or institutional design.

## Next use

```trace
next_use :=
  rerun_GPT4o_dry_run_against_v0_2_table
  OR:
    run_second_documented_case
  only_if:
    evidence_path_exists
    + unknowns_are_preserved
```

Plain version:

The table is now harder to misuse. It forces visible gate, evidence grade, and unknown status. The next step can be either a small patch to the GPT-4o dry run using this v0.2 table, or a second documented case.
