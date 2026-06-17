# TRACE AI Dry Run — GPT-4o System Card v0.1

Date: 2026-06-17
Status: first documented AI pipeline dry run / source-backed / not validation

## Plain purpose

This file applies `TRACE_AI_Pipeline_Operator_Table_v0_1.md` to one documented AI artefact: the GPT-4o System Card.

This is not an audit of OpenAI. It is a dry run of the TRACE diagnostic table against a public system card to test whether the table creates usable questions and preserves unknowns.

```trace
dry_run :=
  AI_pipeline_operator_table
  + one_documented_source
  + evidence_grades
  + unknowns_marked_unknown
  - validation_claim
  - model_internals_inferred_without_source
```

## Source artefact

Primary source:

- OpenAI, `GPT-4o System Card`, published August 2024, available through arXiv as `2410.21276`.

Source status:

```trace
source_status :=
  public_system_card
  + actor_controlled_source
  + source_backed
  - independent_audit
```

Evidence caveat:

The system card is a useful public artefact, but much of it is self-reported by the developer. Treat most entries as `E2_documented`, not as independent confirmation.

## Evidence grades used

```trace
evidence_grade :=
  E0_none
  OR E1_claimed
  OR E2_documented
  OR E3_independent
  OR E4_replayable
```

Applied rule:

```trace
operator_confidence_requires:
  E2_for_mapping
  + E3_for_external_claim
  + E4_for_strong_diagnostic_claim
```

## Dry run table

| Pipeline stage | Evidence grade | What the source shows | TRACE question | Provisional finding | Unknowns preserved |
|---|---:|---|---|---|---|
| Training signal | E2 | The card describes public web data, proprietary partnerships, code/math, multimodal data, filtering, preference alignment, red teaming, and moderation-related mitigations. | What shaped behaviour, and can the signal be inspected or changed? | Mapping possible. Strong causal claims not permitted. | exact dataset composition; weight of each signal; internal objective details; change-control mechanics. |
| Evaluation surface | E2 | The card reports risk identification, external red teaming, converted evaluation datasets, methodology limits, and observed safety challenge evaluations. | What did eval test, what did it miss, and could failure stop deployment? | Evaluation surface visible enough for TRACE questions. Stop authority only partly visible. | release decision threshold; internal failure thresholds; full red-team data; independent replication. |
| Deployment gate | E2 partial | The card says deployment preparation included identifying risks, structured measurements, mitigations, and Preparedness Framework evaluations. | Who controlled release, and what changed at deployment? | Deployment gate is partially visible but not replayable. | names/roles of gate holders; exact signoff; release-stop conditions; final approval record. |
| Tool action | E0/E1 | The card is mostly about GPT-4o capabilities and safety evaluations, especially multimodal and voice; it does not provide a full tool-action map. | What can the system change through tools, and can action be interrupted? | Tool-action mapping not supported from this artefact alone. | tool permissions; action logs; tool approval thresholds; undo paths. |
| Affected-subject route | E1/E2 partial | The card describes mitigations, refusal training, classifiers, moderation, and user-facing safety design in places, but not a full affected-subject contest/repair route. | Can affected subjects know, contest, correct, exit, or obtain repair in time? | Weakest major area for this artefact. Formal route not established. | appeal route; subject notice; response clocks; remedies; repair path. |
| Monitoring / live record | E2 | The card mentions product-level mitigations, monitoring and enforcement, moderation classifiers, output classifiers, transparency reports, and blocking/discontinuing some outputs. | Are records live, and can monitoring change the path? | Some live monitoring visible. Replayability not established. | audit log access; escalation thresholds; human review clocks; incident-to-action records. |
| Rollback / repair | E1/E2 partial | The card describes specific output blocking and discontinuing some unsafe audio generations; broader rollback or repair is not fully mapped. | Can the system be stopped, constrained, reversed, patched, and repaired? | Output-level interruption visible; system-level rollback/repair unclear. | rollback authority; deprecation plan; affected-subject repair; recurrence controls. |
| Responsibility routing | E1/E2 partial | OpenAI is the actor producing the card; some teams/processes are named generally, but responsibility routing across builder, evaluator, deployer, operator, and repair holder is incomplete. | Who held the gate, benefited, knew, controlled, or could intervene? | Responsibility not laundered to model in the document, but gate-holders are not fully mapped. | named accountable roles; repair owner; deployment controller; vendor/operator splits. |

## Operator findings

### Contestability Clock

```trace
status_in_dry_run := weak_signal
```

The system card contains safety mitigations and evaluation discussion, but it does not establish a full affected-subject contestability clock.

```trace
finding :=
  safety_review_visible
  but:
    subject_contest_route_not_visible
```

TRACE pressure:

```trace
ask_next :=
  if_GPT4o_output_or_action_harms_subject
  can_subject_reach_correction_gate_before_hardening?
```

### Future-Space Closure at Gate

```trace
status_in_dry_run := partial_signal
```

The source supports concern about outputs that may affect people, including voice, ungrounded inference, sensitive trait attribution, and misinformation-like risks. But it does not provide a full map of future-space closure.

```trace
finding :=
  possible_future_path_effects_visible
  but:
    future_space_closure_not_mapped_as_subject_route
```

TRACE pressure:

```trace
ask_next :=
  where_can_model_output_or_classification
  become_authoritative_over_user_or_non_user_future_path?
```

### Prediction Authority Gate

```trace
status_in_dry_run := partial_signal
```

The system card is not mainly a scoring or institutional decision system document. Prediction-authority risk is only indirectly visible through model outputs and safety classifiers.

```trace
finding :=
  authority_gate_not_primary_in_source
  but:
    safety_classifiers_and_moderation_act_as_internal_gates
```

TRACE pressure:

```trace
ask_next :=
  when_classifier_or_policy_output
  becomes_authoritative_gate
  over_user_access_or_output_flow?
```

### Technical Opacity as Route Block

```trace
status_in_dry_run := active_as_linked_component
```

The source gives substantial public explanation, but not enough to replay internal decisions, data weighting, eval thresholds, or deployment signoff.

```trace
finding :=
  transparency_exists
  + replayability_limited
```

TRACE pressure:

```trace
ask_next :=
  what_must_be_visible
  for_subject_or_auditor_to_challenge_failure?
```

### Correction Before Hardening

```trace
status_in_dry_run := active_candidate
```

The system card shows multiple mitigation layers, external red teaming, evaluation methodology, classifiers, and output blocking. This gives TRACE a real correction-before-hardening route to ask about.

```trace
finding :=
  correction_layers_visible
  but:
    correction_speed_and_gate_authority_not_replayable
```

TRACE pressure:

```trace
ask_next :=
  can_detected_failure_stop_or_change_deployment
  before_harm_scales?
```

### Live Record

```trace
status_in_dry_run := active_candidate
```

The card shows evaluations, red-team data, classifiers, and transparency reports as record surfaces. But the live pathway from record to deployment or rollback is not fully replayable.

```trace
finding :=
  records_exist
  but:
    liveness_partly_unproven
```

TRACE pressure:

```trace
ask_next :=
  which_records_can_change_release_or_rollback_decisions?
```

### Lever Realism

```trace
status_in_dry_run := active_candidate
```

Some concrete levers are visible, especially classifier-based blocking and discontinuing outputs under certain conditions. Broader deployment stop or rollback levers are less visible.

```trace
finding :=
  output_level_levers_visible
  + deployment_level_levers_unclear
```

TRACE pressure:

```trace
ask_next :=
  what_lever_can_stop_the_system_not_just_one_output?
```

## Main drift result

```trace
TRACE_table_result :=
  usable
  + evidence_disciplined
  + unknown_preserving
  - validation
```

The table worked. It produced useful questions and prevented several overclaims.

## Main weaknesses found

```trace
weaknesses_found :=
  subject_route_weak
  + deployment_gate_not_replayable
  + training_signal_not_replayable
  + responsibility_roles_incomplete
  + rollback_repair_unclear
```

Plain version:

The system card is useful for mapping safety evaluations and mitigations. It is weaker for affected-subject contestability, deployment gate replayability, broad rollback/repair, and named responsibility routing.

## Strongest TRACE value in this dry run

```trace
strongest_value :=
  separates:
    safety_evaluation_surface
    from:
      affected_subject_route
      + deployment_gate
      + rollback_repair
```

Plain version:

A system card can show extensive safety work and still leave open whether affected people have a live route, whether deployment gates are replayable, and whether rollback/repair can change state after harm.

## Provisional verdict

```trace
verdict :=
  dry_run_successful_as_method_test
  + no_alignment_validation
  + next_case_should_target_subject_route_or_deployment_gate
```

## What this does not claim

```trace
not_claimed :=
  GPT4o_safe_or_unsafe
  OR OpenAI_pass_or_fail
  OR TRACE_validated
  OR hidden_training_cause_known
```

## Next move

```trace
next_move :=
  either:
    improve_table_with_subject_route_column
  OR:
    run_second_dry_run_on_public_safety_framework
```

Recommended:

```trace
recommendation :=
  patch_AI_operator_table
  to add:
    visible_gate
    + evidence_grade
    + unknown_status
```

Plain version:

The dry run shows the table is useful, but the table should now be tightened so every row forces three checks: which gate is visible, what evidence grade supports it, and what remains unknown.
