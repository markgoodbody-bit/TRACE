# TRACE Operator Registry v0.1

Date: 2026-06-17
Status: working operator registry / not canon / not validation

## Plain purpose

This registry is the memory spine for TRACE operators.

Cases teach operators. Comparators pressure operators. Claims are demoted or narrowed through operators. Operators are the reusable unit; examples are carriers, not the memory system itself.

```trace
operator_registry :=
  preserve_reusable_structure
  + prevent_case_sprawl
  + record_status
  + preserve_demoters
  + route_future_tests
  - validation_claim
  - canon_claim
```

## Entry schema

Every operator entry should use this minimum shape.

```trace
operator_entry :=
  name
  + compression
  + definition
  + source_case
  + activation_conditions
  + deactivation_conditions
  + comparator
  + distinct_remainder
  + falsifier
  + demoter
  + status
  + must_not_claim
```

## Status key

```trace
status :=
  active_candidate
  OR narrowed_candidate
  OR linked_component
  OR recognition_carrier
  OR demoted
  OR pending_comparator
```

- `active_candidate`: live operator worth further testing.
- `narrowed_candidate`: survived only after being narrowed.
- `linked_component`: useful inside a route, but not an independent TRACE delta.
- `recognition_carrier`: useful teaching/training carrier, not demonstrated delta.
- `demoted`: should not currently be used as a TRACE contribution.
- `pending_comparator`: cannot be judged until a named comparator is run.

---

# OP-001 — Contestability Clock

## Name

Contestability Clock

## Status

```trace
status := active_candidate
```

## Compression

```trace
contestability_clock :=
  challenge_window
  before:
    path_hardening
```

## Definition

Contestability is real only if the affected subject can challenge, correct, or interrupt the relevant decision path before the resulting classification, restriction, burden, harm, or future-space closure hardens.

## Source case

Prediction Authority / Minority Report worked-delta case.

## Activation conditions

```trace
activate_if:
  subject_affecting_decision
  + claimed_review_or_challenge_route
  + time_sensitive_hardening_possible
```

## Deactivation conditions

```trace
deactivate_if:
  no_subject_affecting_decision
  OR no_hardening_window
  OR post_hoc_review_fully_restores_position
```

## Comparator

- contestability literature;
- reviewability literature;
- administrative law;
- process-centric explanations;
- algorithmic accountability.

## Distinct remainder

```trace
distinct_remainder :=
  challenge_must_reach_gate_before_hardening
```

## Falsifier

```trace
falsifier :=
  comparator_fields_already_provide:
    equal_timing_gate_navigation
    + equal_cross_domain_transfer
    + less_vocabulary_burden
```

## Demoter

```trace
demote_if:
  used_as_generic_fast_review_slogan
  without:
    gate_identification
    + hardening_window
    + subject_route_test
```

## Must-not-claim

Do not claim TRACE invented contestability.

Do not claim all delayed appeal is theatre.

Do not claim every decision requires pre-action contestation.

---

# OP-002 — Future-Space Closure at Gate

## Name

Future-Space Closure at Gate

## Status

```trace
status := narrowed_candidate
```

## Compression

```trace
future_space_closure_at_gate :=
  prediction_or_classification
  gains_authority
  before:
    subject_can_know_contest_or_alter_path
  -> future_paths_shrink
```

## Definition

A system closes future-space at a gate when a prediction, classification, risk score, eligibility marker, or identity label becomes causally authoritative before the affected subject can know, contest, or alter the path, shrinking the person's available future options.

## Source case

Prediction Authority / Minority Report worked-delta case; Open-Future Comparator Run.

## Activation conditions

```trace
activate_if:
  prediction_or_classification_exists
  + authority_gate_engaged
  + affected_subject_route_missing_or_late
  + available_future_paths_shrink
```

## Deactivation conditions

```trace
deactivate_if:
  classification_does_not_affect_future_path
  OR subject_can_contest_before_hardening
  OR correction_restores_lost_future_space
```

## Comparator

- right-to-an-open-future family;
- anticipatory ethics;
- due process;
- algorithmic accountability;
- scored-society / risk-scoring analysis.

## Distinct remainder

```trace
distinct_remainder :=
  open_future_harm
  located_at:
    authority_gate
  and_tested_by:
    contestability_clock
```

## Falsifier

```trace
falsifier :=
  open_future_or_anticipatory_harm_literature
  already_provides:
    gate_identification
    + contestability_clock
    + affected_subject_route_test
    + cross_domain_transfer
  with_less_vocabulary_burden
```

## Demoter

```trace
demote_if:
  used_as_generic_future_harm_language
  without:
    gate
    + clock
    + route
```

## Must-not-claim

Do not claim TRACE invented open-future harm.

Do not use broad future-space language without gate, clock, and route.

Do not equate every prediction with illegitimate closure.

---

# OP-003 — Prediction Authority Gate

## Name

Prediction Authority Gate

## Status

```trace
status := narrowed_candidate
```

## Compression

```trace
prediction_authority_gate :=
  forecast_or_score
  -> authorised_intervention
  -> present_constraint
```

## Definition

A prediction authority gate occurs when a forecast, score, risk assessment, or model output becomes a basis for institutional action that materially constrains an affected subject.

## Source case

Prediction Authority / Minority Report worked-delta case.

## Activation conditions

```trace
activate_if:
  forecast_or_score_exists
  + institution_acts_on_it
  + affected_subject_path_changes
```

## Deactivation conditions

```trace
deactivate_if:
  prediction_only_informs
  and:
    no_authority_gate
    + no_material_constraint
```

## Comparator

- automated decision-making reviewability;
- administrative law;
- algorithmic accountability;
- risk-assessment governance.

## Distinct remainder

```trace
distinct_remainder :=
  forecast_becomes_gate
```

## Falsifier

```trace
falsifier :=
  comparator_fields_provide_equal_gate_test
  + equal_transfer_across_domains
  + less_vocabulary_burden
```

## Demoter

```trace
demote_if:
  used_to_treat_all_predictions_as_coercion
```

## Must-not-claim

Do not claim prediction is inherently illegitimate.

Do not claim all risk assessment is pre-crime.

Do not ignore preventive-action boundaries where imminent serious harm exists.

---

# OP-004 — Technical Opacity as Route Block

## Name

Technical Opacity as Route Block

## Status

```trace
status := linked_component
```

## Compression

```trace
technical_opacity_as_route_block :=
  subject_cannot_replay_basis
  + decision_changes_life_path
```

## Definition

Technical opacity blocks a route when the affected subject cannot understand or reconstruct enough of the decision basis to challenge, correct, or interrupt the path.

## Source case

Prediction Authority comparator run.

## Activation conditions

```trace
activate_if:
  technical_or_process_opacity
  + affected_subject
  + challenge_route_depends_on_basis_visibility
```

## Deactivation conditions

```trace
deactivate_if:
  basis_visible_enough_for_challenge
  OR opacity_not_route_relevant
```

## Comparator

- reviewability;
- process-centric explanation;
- transparency;
- algorithmic accountability.

## Distinct remainder

```trace
distinct_remainder :=
  route_block_linkage
  not:
    opacity_discovery
```

## Falsifier

Already substantially met as an independent delta.

## Demoter

```trace
demote_if:
  claimed_as_TRACE_invention
```

## Must-not-claim

Do not claim TRACE invented opacity concerns.

Do not treat opacity as always fatal; the question is whether it blocks a subject-relevant route.

---

# OP-005 — Correction Before Hardening

## Name

Correction Before Hardening

## Status

```trace
status := active_candidate
```

## Compression

```trace
correction_before_hardening :=
  correction_reaches_gate
  before:
    harm_path_hardens
```

## Definition

Correction is real only if it can reach the causal path before the relevant harm, burden, classification, dependency, or loss becomes practically irreversible or too costly to restore.

## Source case

Apollo 13 as recognition carrier; PCFU / WRATT timing work; broader TRACE timing spine.

## Activation conditions

```trace
activate_if:
  harm_path_visible_or_partly_visible
  + correction_route_claimed
  + hardening_possible
```

## Deactivation conditions

```trace
deactivate_if:
  no_causal_path_to_correct
  OR harm_already_fully_hardened_without_repair_path
  OR correction_is_symbolic_only
```

## Comparator

- crisis management;
- high-reliability organisation theory;
- administrative law;
- procedural fairness;
- repair and redress literature.

## Distinct remainder

```trace
distinct_remainder :=
  correction_timing_as_moral_condition
```

## Falsifier

```trace
falsifier :=
  comparator_fields_already_provide:
    equal_cross_domain_correction_timing_test
    + equal_subject_route_test
    + less_vocabulary_burden
```

## Demoter

```trace
demote_if:
  used_as_generic_act_fast_language
  without:
    gate
    + hardening_condition
    + repair_route
```

## Must-not-claim

Do not claim all correction must occur before action.

Do not ignore cases where delay itself prevents serious harm.

Do not use success cases as validation.

---

# OP-006 — Live Record

## Name

Live Record

## Status

```trace
status := active_candidate
```

## Compression

```trace
live_record :=
  record_changes_future_action
```

## Definition

A record is live when it can alter decision, contestability, correction, responsibility, or future action. A stored record that cannot affect the path in time is archive, not live record.

## Source case

Apollo 13; memory/identity cluster; provenance and reviewability work.

## Activation conditions

```trace
activate_if:
  evidence_or_log_exists
  + future_decision_or_correction_depends_on_it
```

## Deactivation conditions

```trace
deactivate_if:
  record_unavailable_to_decision
  OR record_cannot_change_path
  OR record_arrives_after_hardening_without_repair
```

## Comparator

- auditability;
- reviewability;
- evidence law;
- incident investigation;
- software/system logging;
- provenance literature.

## Distinct remainder

```trace
distinct_remainder :=
  record_liveness_test
```

## Falsifier

```trace
falsifier :=
  existing_auditability_or_reviewability_tools
  already_provide_equal_liveness_test
  + equal_cross_domain_transfer
```

## Demoter

```trace
demote_if:
  live_record
  becomes:
    store_more_data
```

## Must-not-claim

Do not claim all records should be public.

Do not claim record existence equals accountability.

Do not ignore privacy, vulnerability, or evidence-integrity constraints.

---

# OP-007 — Lever Realism

## Name

Lever Realism

## Status

```trace
status := active_candidate
```

## Compression

```trace
lever_real_if:
  changes_state
  + reaches_gate
  + works_under_constraint
```

## Definition

A safeguard, remedy, protest, review, or intervention is real only if it can materially change the relevant state through a route that reaches the causal gate under actual constraints.

## Source case

Apollo 13; enforcement-carrier work; safeguard-with-teeth work.

## Activation conditions

```trace
activate_if:
  safeguard_or_remedy_claimed
  + causal_change_needed
```

## Deactivation conditions

```trace
deactivate_if:
  no_material_state_change_possible
  OR lever_cannot_reach_gate
  OR lever_arrives_after_hardening_without_repair
```

## Comparator

- control theory;
- institutional design;
- legal remedies;
- safety engineering;
- governance enforcement.

## Distinct remainder

```trace
distinct_remainder :=
  symbolic_action_vs_state_change
```

## Falsifier

```trace
falsifier :=
  existing_control_or_remedy_frameworks
  already_provide_equal_lever_test
  + equal_transfer_across_domains
```

## Demoter

```trace
demote_if:
  used_to_dismiss_soft_actions
  that_actually_change_state_indirectly
```

## Must-not-claim

Do not claim only hard technical controls matter.

Do not ignore social, legal, financial, reputational, and procedural levers where they materially change the gate.

---

# Registry summary

```trace
active_candidates :=
  contestability_clock
  + correction_before_hardening
  + live_record
  + lever_realism

narrowed_candidates :=
  future_space_closure_at_gate
  + prediction_authority_gate

linked_components :=
  technical_opacity_as_route_block
```

## Current guardrail

```trace
registry_guard :=
  add_operator_only_if:
    source_case_exists
    + activation_conditions_defined
    + falsifier_defined
    + must_not_claim_defined
```

## Next move

```trace
next_move :=
  AI_pipeline_mapping
  using:
    operator_registry
  not:
    fresh_case_collection
```

Plain version:

The registry is now seeded. The next useful build is to map the AI pipeline using these operators: training signal, evaluation surface, deployment gate, tool action, rollback path, affected-subject route, and responsibility routing.
