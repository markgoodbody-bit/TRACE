# TRACE Operator Registry — Claude AI Branch Patch v0.1

Date: 2026-06-17
Status: patch directive / applies to AI branch / not canon by itself

## Plain purpose

Claude's hostile review found that the AI branch was viable but over-ranked several operators and allowed actor-controlled documents to raise claim strength too easily.

This patch records the accepted operator-status corrections before the next dry run.

```trace
accepted_patch :=
  split_E2_actor_vs_independent
  + cap_actor_only_operator_status
  + demote_future_space_closure_to_linked_component
  + narrow_prediction_authority_gate_attachment
  + reclassify_broad_operators_as_global_checks
  + replace_alignment_truth_condition_with_safeguard_gate_condition
```

## Accepted critique summary

```trace
Claude_verdict :=
  viable_but_not_validated
  + evidence_scale_launders_actor_claims
  + some_operator_attachments_overbroad
  + future_space_closure_is_composite
  + prediction_authority_gate_misattached_to_deployment_gate
```

## Evidence patch

```trace
evidence_patch :=
  E2_documented
  split_into:
    E2_actor_documented
    E2_independent_documented
```

```trace
actor_source_cap :=
  if evidence <= E2_actor_documented:
    operator_status_claim <= weak_signal_or_unknown
```

Rationale:

Actor-controlled documents can map what the actor says. They cannot independently establish that the mapped safety, governance, training, rollback, or repair structure works.

## Operator status corrections

### Contestability Clock

```trace
contestability_clock :=
  keep_active_candidate
```

Reason:

It remains the strongest discriminating operator in the AI branch. It asks whether challenge reaches the relevant gate before hardening.

### Future-Space Closure at Gate

```trace
future_space_closure_at_gate :=
  demote_to_linked_component
```

Reason:

It is a composite consequence of prediction/classification authority plus contestability failure. It should not be treated as an independent primitive in the AI pipeline branch.

```trace
future_space_closure_at_gate :=
  linked_consequence_of:
    prediction_authority_gate
    + contestability_clock_failure
```

### Prediction Authority Gate

```trace
prediction_authority_gate :=
  keep_narrowed_candidate
  + remove_from_org_deployment_gate_attachment
```

Reason:

A model deployment decision is not itself a prediction-about-a-subject becoming authoritative over that subject. The operator applies when a forecast, score, classifier, or model output becomes authority over an affected subject.

```trace
valid_attachment :=
  tool_action
  + affected_subject_route
  + classifier_or_score_governing_access
```

```trace
invalid_attachment :=
  generic_release_approval_gate
```

### Technical Opacity as Route Block

```trace
technical_opacity_as_route_block :=
  keep_linked_component
```

Reason:

It remains useful but is already strongly covered by existing transparency, reviewability, and accountability fields.

### Correction Before Hardening

```trace
correction_before_hardening :=
  reclassify_as_global_timing_check
```

Reason:

It applies across many gates, which makes it important but not discriminating as a per-stage routing operator. It must not be counted as strong because it appears everywhere.

### Live Record

```trace
live_record :=
  reclassify_as_global_liveness_check
```

Reason:

It should test whether a record can change the path. It should not inflate every pipeline row as if it were a stage-specific operator.

### Lever Realism

```trace
lever_realism :=
  reclassify_as_global_state_change_check
```

Reason:

It tests whether a safeguard, remedy, or intervention changes state. It is broadly useful but not itself a narrow AI-stage operator.

## Alignment wording correction

Previous risky form:

```trace
alignment_real_if:
  constraint_reaches_deployment_gate
```

Corrected form:

```trace
safeguard_real_if:
  constraint_reaches_relevant_gate
```

Reason:

TRACE may say a safeguard is inert unless it reaches a relevant gate. It must not define alignment's truth condition.

## Updated AI-branch operator routing

```trace
routing_after_patch :=
  contestability_clock -> affected_subject_route + rollback_repair
  prediction_authority_gate -> tool_action + affected_subject_route + classifier_access_gate
  future_space_closure_at_gate -> linked_consequence
  technical_opacity_as_route_block -> linked_component_at_route_failure
  correction_before_hardening -> global_timing_check
  live_record -> global_liveness_check
  lever_realism -> global_state_change_check
```

## Must-not-claim update

```trace
must_not_claim :=
  actor_document_proves_structure
  OR system_card_is_independent_audit
  OR deployment_gate_equals_prediction_authority_gate
  OR future_space_closure_is_independent_primitive
  OR broad_operator_attachment_equals_strength
  OR TRACE_defines_alignment_truth_condition
```

## Next required dry-run correction

```trace
next_dry_run :=
  rerun_GPT4o_system_card
  using:
    E2_actor_documented
    + actor_source_cap
    + weak_signal_cap
    + no_status_promotion_from_actor_only_source
```

Plain version:

The registry correction is narrow: split the evidence grade, cap actor-only claims, demote the composite operator, and stop counting broad global checks as discriminating AI-pipeline operators.
