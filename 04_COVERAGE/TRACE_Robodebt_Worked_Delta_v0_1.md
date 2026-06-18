# TRACE Robodebt Worked Delta v0.1

Date: 2026-06-18
Status: first worked delta / public-administration case / not validation / not proof / not operator promotion / not Kernel v0.3

## 0. Control header

This file runs the first worked delta requested after hostile audit.

It does not validate TRACE.

It does not promote an operator.

It does not create Kernel v0.3.

It does not use Robodebt as proof of TRACE.

It does not treat AI review as evidence.

It asks whether a TRACE read catches anything materially earlier, clearer, or more navigable than an ordinary careful public-law / administrative-review read.

```trace
worked_delta_scope :=
  Robodebt
  + public_administration
  + administrative_review_comparator
  + TRACE_read
  + explicit_delta_or_demote

stop_rules :=
  no_TRACE_validation
  + no_operator_promotion
  + no_Kernel_v0_3
  + no_story_as_evidence
  + no_actor_document_as_independent_confirmation
```

## 1. Source base

This worked delta uses the already source-scoped Robodebt comparator run:

- `04_COVERAGE/TRACE_Debt_Clock_Robodebt_Comparator_Run_v0_1.md`

The comparator run identified the following source hierarchy:

```trace
source_hierarchy :=
  Royal_Commission_report_and_recommendations
  + Commonwealth_Ombudsman_2017_report
  + court_or_legal_material_where_available
  + non_actor_journalism_only_as_secondary
  + actor_documents_only_for_actor_claim_process_chronology
```

This worked delta does not add new external source claims. It tests navigation using the existing source-scoped material.

## 2. Test question

```trace
worked_delta_question :=
  does_TRACE_catch_a_live_failure
  that_an_ordinary_careful_public_law_read_misses
  or_catches_less_clearly?
```

Possible outcomes:

```trace
worked_delta_outcomes :=
  Delta_A := TRACE_catches_material_failure_ordinary_read_misses
  Delta_B := TRACE_compresses_or_orders_failure_better_but_no_new_detection
  Delta_C := ordinary_read_catches_same_failure_equally_well
  Delta_D := ordinary_read_catches_failure_better
```

Demotion rule:

```trace
demote_if :=
  Delta_C
  OR Delta_D
```

If the result is `Delta_B`, TRACE earns only a navigation/compression note, not validation.

## 3. Ordinary careful public-law / administrative-review read

A careful ordinary read sees the main Robodebt failure surface without needing TRACE.

From the source-scoped comparator run, administrative review already explains:

```trace
ordinary_admin_read_sees :=
  formal_review_path
  + internal_review
  + tribunal_or_AAT_review
  + procedural_fairness
  + model_litigant_obligations
  + significant_case_escalation
  + publication_or_visibility_of_significant_review_decisions
  + correction_of_administrative_error
  + interim_or_pause_like_relief_where_available
```

The Royal Commission's recommendations already address many of these directly, including systems for identifying significant AAT cases, training legal officers, identifying significant AAT decisions, publishing significant first-instance social security decisions, and reinstating an Administrative Review Council or equivalent.

Ordinary public-law read also sees the debt-recovery pause issue. The source-scoped comparator run records Recommendation 18.1 as requiring debt-recovery policy that includes treating recipients fairly and with dignity, refraining from commencing or continuing recovery while debt is reviewed or disputed, considering hardship, and giving recipients opportunities to challenge/review/guidance before debt recovery.

```trace
ordinary_admin_read_core_failure :=
  review_and_legal_signal_existed_or_should_have_existed
  + recovery_or_system_continuation_could_harden_position
  + escalation_publication_and_pause_mechanisms_failed_or_were_insufficient
```

Plain result:

Administrative law already has strong tools for this case: procedural fairness, legality, reasons/evidence, review, tribunal signal escalation, model-litigant behaviour, publication of significant decisions, and pause/interim-relief logic.

## 4. Administrative burden / poverty law read

A careful ordinary social-policy read also sees burdens without TRACE.

The source-scoped comparator run says administrative burden explains:

```trace
administrative_burden_read_sees :=
  learning_costs
  + compliance_costs
  + psychological_costs
  + burden_shifting
  + friction_as_policy_design
  + unequal_impact
  + access_failure
  + state_created_obstacle_courses
```

The same run says poverty law and welfare-rights practice already explain:

```trace
poverty_law_read_sees :=
  benefit_dependency
  + low_financial_buffer
  + welfare_conditionality
  + overpayment_recovery
  + hardship
  + vulnerability
  + legal_aid_and_community_legal_centre_importance
  + dignity_and_stigma
  + formal_rights_vs_usable_rights
```

Plain result:

TRACE does not own the burdens here. Existing fields already see the difference between formal process and usable process.

## 5. TRACE read

TRACE reads the same case through a narrower timing/correction grammar.

```trace
TRACE_read :=
  correction_before_hardening
  + K_gate
  + harm_clock
  + subject_future_space
  + record_and_witness_integrity
  + enforcement_carrier
  + repair_before_closure
```

TRACE asks:

```trace
TRACE_questions :=
  did_correction_reach_subject_before_position_hardened?
  + did_review_exist_only_formally_or_as_live_pause?
  + did_record_and_witness_channels_escalate_legal_signal?
  + did_recovery_continue_while_legality_or_amount_was_contested?
  + did_repair_restore_future_space_or merely close institutional exposure?
```

TRACE's clearest compression is:

```trace
TRACE_compression :=
  formal_review_not_enough
  unless:
    correction_reaches_subject
    before:
      recovery_or_burden_hardens_position
```

Plain result:

TRACE does not discover the public-law problem from scratch. It compresses the live timing requirement: review must interrupt hardening, not merely exist.

## 6. Delta comparison

### 6.1 Did TRACE catch something ordinary administrative review missed?

```trace
Delta_A_material_new_detection := false
```

Reason:

The ordinary public-law / administrative-review read already catches the major legal and procedural failure surfaces. It also catches the pause/interim-relief question through Recommendation 18.1 and administrative review logic.

### 6.2 Did TRACE order the failure differently?

```trace
Delta_B_navigation_or_compression := true_but_limited
```

TRACE makes one pressure more explicit:

```trace
TRACE_delta_limited :=
  review_clock
  must_be_compared_to:
    hardening_clock
```

This is useful because it forces the question:

```trace
liveness_question :=
  did_the_correction_channel_change_the_subject_position
  before_recovery_burden_or_irreversibility_hardened?
```

But this is not unique enough to promote a new operator. It strengthens and demonstrates `correction_before_hardening`, which was already active.

### 6.3 Did ordinary read catch the same failure equally well?

```trace
Delta_C_same_failure_equally_well := mostly_true
```

Administrative law, poverty law, administrative burden, and stay-like pause comparators already explain most of the case.

### 6.4 Did ordinary read catch anything better?

```trace
Delta_D_ordinary_better := partly_true_for_legal_specificity
```

Ordinary public law is better for legal detail: duties, decision-maker obligations, tribunal decisions, model-litigant obligations, statutory review routes, and precise remedial authority.

TRACE is not a substitute for that.

## 7. Worked result

```trace
worked_delta_result :=
  Delta_B_limited_navigation_compression
  + Delta_C_most_failure_already_caught
  + Delta_D_legal_specificity_belongs_to_public_law
  - Delta_A_material_new_detection
```

Plain result:

TRACE did not beat the ordinary public-law read as a detector. It did provide a useful compression: compare the review/correction clock to the hardening clock. But that is not validation and not a new operator. It is a demonstration of how `correction_before_hardening` can order the case.

## 8. Consequence for TRACE architecture

This result does not validate TRACE.

It does not promote any new operator.

It does not justify more scaffolding by itself.

It gives a modest result:

```trace
architecture_consequence :=
  keep_scope_map_as_orientation
  + keep_primitive_registry_as_support
  + keep_domain_translation_registry_as_T1_mapping
  + require_more_worked_deltas_before_expansion
  - validation
  - universality_claim
  - operator_promotion
```

The worked delta pressures the architecture in the right direction:

```trace
architecture_pressure :=
  TRACE_useful_when_it_orders_clocks_and_carriers
  but:
    existing_fields_often_own_the_domain_specific_content
```

## 9. Demotions / holds caused by this test

```trace
demotions_or_holds :=
  no_new_operator
  + no_design_pattern_library_yet
  + no_domain_status_above_T1
  + no_claim_TRACE_beats_public_law
  + no_claim_Robodebt_validates_TRACE
```

The Domain Translation Registry's cap remains correct:

```trace
law_admin_governance_status := T1
finance_debt_status := T1_or_T0
```

## 10. What this worked delta actually earns

```trace
earned_claim :=
  TRACE_can_usefully_compress_Robodebt_as:
    correction_before_hardening
    + review_clock_vs_hardening_clock
    + pause_or_stay_like_carrier_question
```

Must-not-claim:

```trace
must_not_claim :=
  TRACE_detected_Robodebt_better_than_public_law
  OR TRACE_validated
  OR Robodebt_proves_TRACE
  OR legal_specificity_can_be_replaced_by_TRACE
```

## 11. Next test suggested

This Robodebt delta is modest and partly redundant by design. That is useful but not enough.

The next worked delta should target a domain where ordinary expert tools are less obviously sufficient.

Candidate next tests:

```trace
next_worked_delta_candidates :=
  AI_deployment_failure
  OR mechanistic_interpretability_case
  OR policing_preemption_case
```

Selection rule:

```trace
select_next_if :=
  case_has_clear_ordinary_comparator
  + case_has_source_record
  + TRACE_prediction_or_navigation_can_fail
```

## 12. Final compression

```trace
Robodebt_Worked_Delta_v0_1 :=
  first_worked_delta
  + ordinary_public_law_read_strong
  + TRACE_read_useful_as_clock_compression
  + result := Delta_B_limited + Delta_C_mostly
  - material_new_detection
  - validation
  - operator_promotion
  - Kernel_v0_3

next :=
  one_more_worked_delta_in_less_law-owned_domain
  before:
    design_pattern_library
    OR failure_mode_atlas
    OR formal_MI_bridge
```

Plain conclusion:

TRACE did not beat ordinary public law on Robodebt. It did clarify one reusable timing structure: correction only matters if it reaches the subject before burden, recovery, or irreversibility hardens the position. That is useful, but modest. The architecture survives only as orientation and compression, not validation.

End.
