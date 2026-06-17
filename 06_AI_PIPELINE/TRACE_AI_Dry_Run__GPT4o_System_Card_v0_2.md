# TRACE AI Dry Run — GPT-4o System Card v0.2

Date: 2026-06-17
Status: rerun against AI Pipeline Operator Table v0.3 / actor-evidence capped / not validation

## Plain purpose

This file reruns the GPT-4o System Card dry run after the evidence-grade patch.

The previous dry run treated actor-controlled documentation too generously. This version applies the new rule:

```trace
actor_source_cap :=
  if evidence <= E2_actor_documented:
    operator_status_claim <= weak_signal_or_unknown
```

This is not an audit of OpenAI. It is a test of whether TRACE can preserve unknowns when the main public source is actor-controlled.

## Source artefact

Primary source:

- OpenAI, `GPT-4o System Card`, arXiv record `2410.21276`, dated 2024-10-25.

Source status:

```trace
source_status :=
  public_system_card
  + actor_controlled_documentation
  + useful_for_mapping_actor_claims
  - independent_confirmation
  - replayable_audit
```

Date correction:

```trace
date_correction :=
  previous_dry_run_mixed:
    August_2024_public_release_context
    + arXiv_2410_date
  corrected_here_as:
    arXiv_record_date_2024_10_25
```

## Evidence grades used

```trace
evidence_grade :=
  E0_none
  OR E1_claimed
  OR E2_actor_documented
  OR E2_independent_documented
  OR E3_independent_corrobated
  OR E4_replayable
```

Applied rule:

```trace
operator_confidence_requires:
  E2_actor_documented_for_actor_claim_mapping
  + E2_independent_documented_for_non_actor_mapping
  + E3_independent_corrobated_for_external_claim
  + E4_replayable_for_strong_diagnostic_claim
```

## Source-support discipline

The source can support only this type of claim:

```trace
permitted_claim :=
  system_card_says_X
  OR actor_document_maps_X_as_claimed_structure
```

The source cannot by itself support:

```trace
forbidden_claim :=
  X_works
  OR X_is_independently_confirmed
  OR X_is_replayable
  OR operator_status_promoted_above_weak_signal
```

## Rerun table

| Pipeline stage | Evidence grade | Visible gate | Source-supported mapping | TRACE finding under actor cap | Unknowns preserved |
|---|---:|---|---|---|---|
| Training signal | E2_actor_documented | Training-signal gate partly described by actor. | The system card describes model capabilities, training/alignment context, safety mitigations, and evaluation focus. | Weak signal only. Actor documentation can map claimed shaping surfaces but cannot establish internal causal structure. | exact dataset mix; objective weights; relative contribution of training/fine-tuning/RL/preference signals; internal change controls. |
| Evaluation surface | E2_actor_documented | Evaluation gate actor-described. | The card describes safety evaluations, Preparedness Framework evaluations, red teaming, and third-party assessments. | Useful mapping surface, not proof. The table can ask whether failure could stop deployment, but the card alone does not make that replayable. | full eval set; failure thresholds; unreported failures; release-stop authority; independent replication. |
| Deployment gate | E2_actor_documented | Release gate only partially visible. | The card describes risk evaluation and mitigation work around GPT-4o. | Weak signal. Actor documentation suggests a release-preparation process, but does not expose the deployment decision gate. | named gate holders; signoff record; stop/delay criteria; scope-change log; affected-subject analysis. |
| Tool action | E0/E1 from this artefact | Tool-action gate not sufficiently mapped. | The card focuses on model capabilities and risks, especially multimodal/voice; it does not provide a full tool permission/action map. | Unknown. Do not infer tool permissions or interruption routes from system-card capability discussion. | authorised tool calls; executed state changes; action logs; undo paths; human approval thresholds. |
| Affected-subject route | E1/E2_actor partial | Subject-route gate weakly visible. | The card describes mitigations and safety behaviours, but not a full contest/correction/repair route for affected subjects. | Weak signal / gap. Safety design is not the same as affected-subject contestability. | notice; explanation route; appeal route; response clocks; remedies; repair outcomes. |
| Monitoring / live record | E2_actor_documented | Monitoring gate actor-described but not replayable. | The card describes safety mitigations and evaluation surfaces; some monitoring/enforcement-like surfaces are mentioned at product level. | Weak signal. Actor documentation may show monitoring claims, but not incident-to-action liveness. | telemetry access; escalation thresholds; incident logs; stop authority; response time. |
| Rollback / repair | E1/E2_actor partial | Rollback gate weakly visible. | The card describes certain mitigations and blocking/discontinuing unsafe outputs in places, but not a full rollback/repair architecture. | Weak signal. Output-level mitigation is not system-level rollback or subject repair. | rollback authority; deprecation plan; affected-subject repair; recurrence controls; scar record. |
| Responsibility routing | E1/E2_actor partial | Responsibility gate incomplete. | OpenAI is the actor publishing the card; some processes and assessment types are described. | Weak signal. Responsibility is not laundered to the model, but named gate-holders and repair owners are not fully mapped. | named responsible roles; deployer/operator split; repair owner; vendor contracts; escalation owners. |

## Operator findings under actor cap

### Contestability Clock

```trace
status_in_rerun := weak_signal
```

The system card does not establish a full affected-subject contestability clock.

```trace
finding :=
  safety_mitigation_surface_visible
  but:
    subject_challenge_route_not_established
```

### Prediction Authority Gate

```trace
status_in_rerun := weak_signal_or_unknown
```

The system card is not primarily an institutional scoring or decision-authority document. Prediction authority may appear where model outputs, classifiers, or policy systems govern access or action, but this artefact alone does not map those gates fully.

```trace
finding :=
  prediction_authority_not_demonstrated_by_system_card_alone
```

### Future-Space Closure at Gate

```trace
status_in_rerun := linked_consequence_only
```

Future-space closure is not promoted as an independent operator. It can be considered only where prediction/classification authority plus contestability failure is visible.

```trace
finding :=
  possible_downstream_future_effects
  but:
    no_independent_future_space_operator_status
```

### Technical Opacity as Route Block

```trace
status_in_rerun := linked_component
```

The card increases public visibility but does not make training, evaluation thresholds, release signoff, tool permissions, or incident-to-action records replayable.

```trace
finding :=
  transparency_exists
  + replayability_limited
```

### Correction Before Hardening

```trace
status_in_rerun := global_timing_check
```

The card describes evaluation and mitigation surfaces. Actor-only documentation cannot establish that correction reaches the relevant gate before scaling or harm hardening.

```trace
finding :=
  correction_surfaces_claimed
  but:
    correction_liveness_not_established
```

### Live Record

```trace
status_in_rerun := global_liveness_check
```

The card itself is a public record, and it references evaluation and mitigation surfaces. But this does not show which records can change release, rollback, or repair decisions.

```trace
finding :=
  records_visible
  but:
    liveness_unproven
```

### Lever Realism

```trace
status_in_rerun := global_state_change_check
```

Some claimed mitigations are visible, but actor-only documentation does not prove that levers are effective under pressure.

```trace
finding :=
  claimed_levers_visible
  but:
    effectiveness_not_independently_confirmed
```

## Main result

```trace
rerun_result :=
  table_v0_3_blocks_actor_document_laundering
  + unknowns_preserved
  + operator_statuses_capped
  - validation
```

Plain version:

The rerun is stricter than v0.1. It no longer upgrades system-card claims into active operator findings. Most entries remain weak signals or unknowns unless independently corroborated or replayable.

## Strongest TRACE value after rerun

```trace
strongest_value :=
  separates:
    actor_described_safety_work
    from:
      independently_confirmed_gate_liveness
      + affected_subject_route
      + rollback_repair
      + responsibility_owner
```

Plain version:

The dry run now distinguishes a safety document from proof of a working safety mechanism.

## Main weaknesses still exposed

```trace
remaining_gaps :=
  no_replayable_deployment_gate
  + weak_subject_route
  + actor_only_evaluation_surface
  + tool_action_not_mapped
  + rollback_repair_unclear
  + responsibility_roles_incomplete
```

## Difference from v0.1 dry run

```trace
v0_1_error :=
  actor_document
  -> documented_structure
  -> operator_status_strengthened
```

```trace
v0_2_fix :=
  actor_document
  -> actor_claim_mapping
  -> weak_signal_or_unknown
```

## Provisional verdict

```trace
verdict :=
  dry_run_successful_as_guardrail_test
  + not_alignment_validation
  + not_OpenAI_audit
  + next_case_not_required_yet
```

## What this does not claim

```trace
not_claimed :=
  GPT4o_safe_or_unsafe
  OR OpenAI_pass_or_fail
  OR TRACE_validated
  OR hidden_training_cause_known
  OR actor_document_independently_confirms_liveness
```

## Next move

```trace
next_move :=
  drift_check_AI_branch_after_actor_cap
```

Plain version:

Do not add a new case yet. First check whether the actor-evidence cap now holds across the AI branch and whether old files need a clear supersession note.
