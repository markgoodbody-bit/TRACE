# TRACE Operator Registry — Coverage Extract v0.1

Date: 2026-06-17
Status: registry extract / coverage branch / not canon / not validation

## Plain purpose

This file extracts the actual operator candidates produced by the `04_COVERAGE` work.

It prevents the coverage branch from remaining a loose set of examples, audits, and comparator notes. Operators are the memory unit.

```trace
operator_registry_extract :=
  preserve_operators
  + record_status
  + name_demoters
  + prevent_case_sprawl
  - canon_claim
  - validation_claim
```

## Registry status key

```trace
operator_status :=
  active_candidate
  OR narrowed_candidate
  OR linked_component
  OR recognition_carrier
  OR demoted
  OR pending_comparator
```

Definitions:

- `active_candidate`: live operator worth further testing.
- `narrowed_candidate`: survived only after being narrowed.
- `linked_component`: useful inside a route, but not an independent TRACE delta.
- `recognition_carrier`: useful teaching/training carrier, not demonstrated delta.
- `demoted`: should not currently be used as a TRACE contribution.
- `pending_comparator`: cannot be judged until a named comparator is run.

---

# 1. Contestability Clock

## Status

```trace
status := active_candidate
```

## Compression

```trace
contestability_clock :=
  time_available_for_challenge
  before:
    decision_path_hardens
```

## Definition

Contestability is real only if an affected subject can challenge, correct, or interrupt the relevant decision path before the resulting harm, classification, restriction, or future-space closure hardens.

```trace
contestability_real_if:
  challenge_reaches_gate
  before:
    future_space_closes
```

## Source case

Prediction Authority / Minority Report worked-delta case.

## Comparator result

Existing contestability and administrative-law work capture challenge rights and procedural safeguards, but TRACE appears to add cross-domain timing compression: challenge must reach the gate before hardening.

## Activation conditions

```trace
activate_if:
  decision_affects_future_path
  + challenge_route_exists_or_is_claimed
  + timing_may_make_route_theatrical
```

## Deactivation conditions

```trace
deactivate_if:
  no_subject_affecting_decision
  OR no_time_sensitive_hardening
  OR challenge_afterward_is_fully_restorative
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
  contestability_clock
  becomes:
    slogan_for_fast_review
  without:
    actual_gate_identification
```

## Must-not-claim

Do not claim TRACE invented contestability.

Do not claim all delayed appeal is theatre.

Do not claim every decision needs pre-action contestation; emergency and prevention cases require their own boundary.

---

# 2. Future-Space Closure at Gate

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
    affected_subject_can_know_contest_or_alter_path
  causing:
    available_future_paths_to_shrink
```

## Definition

A system closes future-space at a gate when a prediction, classification, risk score, eligibility marker, or identity label becomes causally authoritative before the affected subject can know, contest, or alter the path, shrinking the person's available future options.

## Source case

Prediction Authority / Minority Report worked-delta case; Open-Future Comparator Run.

## Comparator result

Open-future and anticipatory-harm language already capture much of the broad future-space idea. TRACE's surviving contribution is the gate-clock-route interface, not broad originality over future-facing harm.

## Activation conditions

```trace
activate_if:
  prediction_or_classification_exists
  + gains_authority
  + affected_subject_route_missing_or_late
  + future_options_shrink
```

## Deactivation conditions

```trace
deactivate_if:
  classification_does_not_affect_future_path
  OR subject_can_meaningfully_contest_before_hardening
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
  future_closure
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
  operator_used_as:
    generic_future_harm_language
  without:
    gate
    + clock
    + subject_route
```

## Must-not-claim

Do not claim TRACE invented open-future harm.

Do not use broad future-space language without gate, clock, and route.

Do not equate every prediction with illegitimate closure.

---

# 3. Prediction Authority Gate

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

## Comparator result

Existing algorithmic-accountability, reviewability, and due-process work already recognise automated outputs becoming consequential. TRACE's value is compact gate-language that transfers beyond any one field.

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
  prediction_informs_only
  and:
    no_authority_gate
    + no_material_constraint
```

## Comparator

- automated decision-making reviewability;
- administrative law;
- algorithmic accountability;
- risk assessment governance.

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

# 4. Technical Opacity as Route Block

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

## Comparator result

This is strongly captured by existing reviewability, process-explanation, transparency, and algorithmic-accountability work. It should not be claimed as an independent TRACE contribution.

## Activation conditions

```trace
activate_if:
  technical_or_process_opacity
  + subject_affected
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

# 5. Apollo Correction-Before-Hardening Carrier

## Status

```trace
status := recognition_carrier
```

## Compression

```trace
Apollo_correction_carrier :=
  live_record
  + hardening_clock
  + material_lever
  + repair_carrier
  + responsibility_routing
```

## Definition

Apollo 13 is useful as a clean carrier for correction-before-hardening, but it is not currently a demonstrated TRACE delta because the actual actors already corrected the path successfully.

## Source case

Apollo 13 worked-delta case.

## Comparator result

Engineering crisis analysis, safety engineering, and high-reliability analysis are mature local comparators. Apollo is under demotion pressure as a worked-delta case.

## Activation conditions

```trace
activate_if:
  teaching_or_training_needs_clean_success_case
  + correction_before_hardening_pattern_needed
```

## Deactivation conditions

```trace
deactivate_if:
  used_as_validation
  OR used_to_claim_TRACE_outperforms_engineering_expertise
```

## Comparator

- engineering crisis analysis;
- safety engineering;
- high-reliability organisation analysis.

## Distinct remainder

```trace
distinct_remainder :=
  clean_training_compression
  not:
    expert_domain_superiority
```

## Falsifier

The falsifier is likely partly met if HRO/safety-engineering provides equal transfer with less vocabulary.

## Demoter

```trace
demote_if:
  treated_as_demonstrated_delta
```

## Must-not-claim

Do not claim Apollo 13 validates TRACE.

Do not claim TRACE would have improved Apollo 13.

Do not claim successful rescue equals theoretical proof.

---

# Registry summary

```trace
active_or_narrowed :=
  contestability_clock
  + future_space_closure_at_gate
  + prediction_authority_gate

linked_only :=
  technical_opacity_as_route_block

recognition_only :=
  Apollo_correction_carrier
```

## Next registry move

```trace
next_registry_move :=
  pause_04_COVERAGE
  + use_these_operator_entries
  when:
    building_formal_TRACE_operator_registry
    OR AI_pipeline_mapping
```

Plain version:

Coverage work has produced three live/narrowed operators, one linked component, and one recognition carrier. The branch should now stop expanding and route this extract into the wider TRACE operator memory system.
