# TRACE AI Pipeline Operator Table v0.1

Date: 2026-06-17
Status: diagnostic table / operator application / not validation

## Plain purpose

This table turns the first AI pipeline map into a usable diagnostic surface.

It does not solve AI alignment. It asks where operators attach, what evidence is needed, and what failure looks like before harm hardens.

```trace
AI_pipeline_operator_table :=
  pipeline_stage
  + attached_operator
  + diagnostic_question
  + failure_mode
  + evidence_needed
  + drift_guard
  - validation_claim
```

## Compact table

| Pipeline stage | Attached TRACE operators | Diagnostic question | Failure mode | Evidence needed | Drift guard |
|---|---|---|---|---|---|
| Training signal | live record; technical opacity as route block; lever realism | What signal shaped the behaviour, and can it be inspected or changed? | Proxy capture / hidden shaping | data notes; training objective; reward/preference process; filtering rules; change-control record | Do not pretend TRACE can infer training internals without evidence. |
| Evaluation surface | live record; lever realism; correction before hardening | What does the evaluation actually test, and can failure stop deployment? | Eval theatre | eval plan; benchmark list; red-team results; known gaps; release criteria; stop authority | Do not treat benchmark pass as safety proof. |
| Deployment gate | prediction authority gate; correction before hardening; lever realism; live record | Who controls release, and what changes once the system enters the world? | Deployment gate blindness | approval record; release scope; access controls; affected-user analysis; rollback plan | Do not confuse internal approval with legitimate deployment. |
| Tool action | lever realism; live record; correction before hardening; technical opacity as route block | What can the system change through tools, and can action be interrupted? | Tool action without interrupt | tool permissions; action logs; undo routes; rate limits; approval thresholds | Do not treat tool use as mere output. It is causal action. |
| Affected-subject route | contestability clock; future-space closure at gate; technical opacity as route block; correction before hardening | Can affected subjects know, contest, correct, exit, or obtain repair in time? | Formal route but no live route | user notice; appeal route; explanation route; response clocks; remedy record | Do not count a route that arrives after hardening. |
| Monitoring and live record | live record; lever realism; correction before hardening | What signals are monitored, who can act on them, and what threshold changes the system? | Dashboard without lever | telemetry; incident reports; audit logs; escalation policy; interrupt authority | Do not treat observation as correction. |
| Rollback and repair | correction before hardening; lever realism; live record; contestability clock | Can the system be stopped, constrained, reversed, patched, and repaired? | Rollback theatre | rollback procedure; deprecation plan; affected-subject identification; repair budget; recurrence controls | Do not call apology repair. Repair must change state. |
| Responsibility routing | live record; lever realism; correction before hardening | Who held the gate, benefited, knew, controlled, or could intervene? | Responsibility laundering to model | owner map; deployer map; evaluator signoff; vendor contracts; incident ownership; repair owner | Do not let model behaviour erase upstream gate-holders. |

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

This table needs a simple evidence discipline.

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

## Pipeline gates

```trace
pipeline_gates :=
  training_signal_gate
  + eval_gate
  + deployment_gate
  + tool_action_gate
  + subject_route_gate
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

## What this table does not claim

```trace
not_claimed :=
  complete_AI_alignment_solution
  OR model_internals_readable_without_evidence
  OR governance_sufficient_without_technical_controls
  OR technical_controls_sufficient_without_subject_routes
```

TRACE is a routing interface. It must not pretend to replace interpretability, ML engineering, security, law, policy, or institutional design.

## Next use

```trace
next_use :=
  apply_table_to_one_real_or_well_documented_AI_case
  only_if:
    evidence_path_exists
    + no_more_theory_needed_first
```

Plain version:

This table is now the first practical AI pipeline diagnostic. The next step should be a small evidence-backed dry run, not another abstract expansion.
