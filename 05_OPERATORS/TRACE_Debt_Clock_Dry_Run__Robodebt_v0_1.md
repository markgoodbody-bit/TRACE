# TRACE Debt Clock Dry Run — Robodebt v0.1

Date: 2026-06-17
Status: source-backed operator dry run / non-story case / not validation

## Plain purpose

This file applies `TRACE_Money_Debt_Extraction_Clocks_Operator_Probe_v0_1.md` to a non-story case: the Australian Robodebt scheme, using the Royal Commission report page and recommendations as the primary source surface.

This is not a full Robodebt case history. It is a narrow dry run of the `debt_clock`, `payment_gate`, `interest_as_hardening`, `repair_outbid_by_extraction`, and `credit_scar` candidate operators.

```trace
dry_run :=
  debt_clock_operator_probe
  + source_backed_non_story_case
  + evidence_grades
  + unknowns_preserved
  - full_case_history
  - validation_claim
```

## Primary source surface

Primary source:

- Royal Commission into the Robodebt Scheme, `Report`, publication page and recommendations, publication date 7 July 2023.

Source grade:

```trace
source_grade := E3_independent_corrobated
```

Reason:

The report is an official Royal Commission source, external to the delivery agency being assessed. It is stronger than actor self-description, but this dry run still does not treat the public report page as a complete replayable operational trace.

```trace
not_E4_because:
  public_recommendations
  are_not:
    complete_case_logs
    + individual_debt_records
    + full_collection_timeline
```

## Case frame

```trace
case_frame :=
  Robodebt
  as:
    contested_public_debt_recovery_system
  tested_for:
    financial_clock
    + contestability_pause
    + recovery_gate
    + vulnerability_route
    + record_scar
```

The report page records that the Royal Commission report was presented and tabled on 7 July 2023, and that the report contains 57 recommendations. It includes recommendations on people-centred service design, vulnerability, automation, debt recovery, review, and documentation.

## Evidence grade table

```trace
evidence_grade :=
  E0_none
  OR E1_claimed
  OR E2_actor_documented
  OR E2_independent_documented
  OR E3_independent_corrobated
  OR E4_replayable
```

| Dry-run component | Evidence grade | Basis |
|---|---:|---|
| Royal Commission report exists and was tabled | E3_independent_corrobated | Official Royal Commission publication page. |
| Recommendations on debt recovery during review/dispute | E3_independent_corrobated | Recommendation 18.1. |
| Recommendations on opportunities to challenge/review debts | E3_independent_corrobated | Recommendation 18.1. |
| Vulnerability/capacity-to-engage recommendations | E3_independent_corrobated | Recommendations 11.2–11.4. |
| Automated decision review and algorithm scrutiny recommendations | E3_independent_corrobated | Recommendations 17.1–17.2. |
| Individual debt timelines and account-level accrual/collection paths | E0/E1 in this file | Not reconstructed here. |
| Full credit-record effects for individual recipients | E0 in this file | Not established from the source surface used. |

## Operator 1 — Debt Clock

```trace
debt_clock :=
  obligation_or_claim
  increases_burden_over_time
  faster_than:
    subject_can_contest_or_repair
```

### Source-backed signal

Recommendation 18.1 says Services Australia should develop a comprehensive debt recovery policy, including debt recovery that is ethical, proportionate, consistent, transparent, fair, dignified, hardship-sensitive, and — subject to legal authority — should refrain from commencing or continuing recovery while a debt is reviewed or disputed.

### TRACE reading

```trace
Robodebt_debt_clock_signal :=
  debt_recovery_action
  + review_or_dispute_route
  + need_to_pause_recovery
```

The recommendation is strong evidence that the Commission saw debt recovery continuing during review/dispute as a live design problem.

```trace
finding :=
  debt_clock_operator_supported_as_mapping_question
  but:
    individual_clock_speed_not_reconstructed_here
```

### Status

```trace
status := strong_candidate_supported_for_further_testing
```

### Unknowns

```trace
unknowns :=
  individual_notice_dates
  + review_request_dates
  + collection_start_dates
  + repayment_schedule_dates
  + hardship_intervention_dates
  + recovery_pause_or_non_pause_records
```

## Operator 2 — Payment Gate

```trace
payment_gate :=
  access_or_continuity
  depends_on:
    timely_payment
  before:
    subject_route_can_correct_or_stabilise
```

### Source-backed signal

Recommendation 18.1 says recipients should be given ample and appropriate opportunities to challenge, review, and seek guidance on proposed debts before referral for debt recovery.

Recommendation 10.1 also directs service design to emphasise the people being served, including clear communication and avoiding exacerbating financial or other stress.

### TRACE reading

```trace
payment_gate_signal :=
  proposed_debt
  -> debt_recovery_referral
  before_or_without:
    adequate_challenge_guidance
```

The gate here is not simply payment. It is referral into recovery/enforcement before review and support have done their work.

```trace
finding :=
  payment_gate_supported_as_candidate
  but:
    precise_access_loss_not_mapped_here
```

### Status

```trace
status := promising_candidate
```

### Unknowns

```trace
unknowns :=
  whether_payment_deadline_closed_specific_access
  + whether_recovery_referral_changed_credit_or_service_access
  + whether_support_options_paused_gate
```

## Operator 3 — Interest as Hardening

```trace
interest_as_hardening :=
  time_price
  compounds_or_accumulates
  into:
    future_space_loss
```

### Source-backed signal

The report page recommendations on debt recovery support a general concern about recovery action during review/dispute. However, this source surface does not reconstruct interest, penalty, or fee accrual as the specific hardening mechanism.

### TRACE reading

```trace
interest_as_hardening_signal :=
  weak_or_unproven_in_this_dry_run
```

This operator should not be promoted from the Robodebt report page alone.

```trace
finding :=
  hold
```

### Status

```trace
status := not_supported_from_current_source_surface
```

### Unknowns

```trace
unknowns :=
  interest_or_fee_accrual
  + enforcement_costs
  + compounding_penalties
  + individual_financial_escalation_records
```

## Operator 4 — Repair Outbid by Extraction

```trace
repair_outbid_by_extraction :=
  available_surplus
  routed_to:
    debt_service
    + penalties
    + rent
    + compliance_cost
  before:
    repair_or_stabilisation
```

### Source-backed signal

Recommendation 10.1 refers to acting with sensitivity to financial and other stress and avoiding government interactions that exacerbate stress or introduce new stress. Recommendation 18.1 refers to hardship-sensitive debt recovery and pausing recovery while disputed or reviewed, subject to legal authority.

### TRACE reading

```trace
repair_outbid_signal :=
  financial_stress
  + recovery_action
  + hardship_route_needed
```

This supports the question but does not prove the operator in a full case-specific way.

```trace
finding :=
  supported_as_question
  + not_yet_demonstrated_as_full_operator
```

### Status

```trace
status := promising_candidate_needs_individual_or_cohort_trace
```

### Unknowns

```trace
unknowns :=
  household_budget_effects
  + repayment_vs_food_housing_medical_costs
  + repair_capacity_loss
  + support_availability
```

## Operator 5 — Credit Scar

```trace
credit_scar :=
  financial_event_or_record
  persists_after_event
  and_constrains:
    housing
    + employment
    + borrowing
    + insurance
    + social_participation
```

### Source-backed signal

The public report page supports concerns about records, debt recovery, review, automation, and legal process, but it does not by itself establish credit-record scarring for specific recipients.

### TRACE reading

```trace
credit_scar_signal :=
  possible_but_not_supported_here
```

### Status

```trace
status := hold_as_candidate
```

### Unknowns

```trace
unknowns :=
  credit_reporting_effects
  + debt_collector_record_effects
  + future_access_impact
  + correction_or_removal_of_records
```

## Supporting TRACE gates in Robodebt source surface

### Vulnerability / capacity route

The Royal Commission recommendations call for identifying circumstances affecting a recipient's capacity to engage with compliance activity, recording those circumstances, engaging before removing vulnerability indicators, and considering categories of vulnerable recipients affected by compliance programs.

```trace
vulnerability_route :=
  capacity_to_engage
  + compliance_activity
  + record_on_file
  + no_auto_expiry_without_confirmation
```

TRACE relevance:

```trace
operator_link :=
  affected_subject_route
  + contestability_clock
  + capacity_clock_candidate
```

### Automated decision / algorithm scrutiny route

The report recommendations say that where automated decision-making is implemented, affected people should have a clear review path, departmental websites should explain the use of automation in plain language, and business rules/algorithms should be available for independent expert scrutiny.

```trace
automation_route :=
  automated_decision
  + clear_review_path
  + plain_language_explanation
  + business_rules_and_algorithms_available_for_scrutiny
```

TRACE relevance:

```trace
operator_link :=
  technical_opacity_as_route_block
  + prediction_authority_gate
  + contestability_clock
```

### Debt recovery pause route

The report recommends refraining from commencing or continuing recovery action while a debt is reviewed or disputed, subject to legal authority.

```trace
debt_recovery_pause_route :=
  disputed_or_reviewed_debt
  -> pause_recovery_action
```

TRACE relevance:

```trace
operator_link :=
  debt_clock
  + correction_before_hardening
  + payment_gate
```

## Main dry-run findings

```trace
findings :=
  debt_clock := strong_candidate_supported
  payment_gate := promising_candidate
  repair_outbid_by_extraction := promising_question_needs_trace
  interest_as_hardening := not_supported_from_current_source_surface
  credit_scar := hold_as_candidate
```

## What TRACE adds here, if anything

```trace
TRACE_delta_candidate :=
  debt_recovery_pause
  framed_as:
    stopping_financial_clock_before_correction_hardens
```

Plain version:

The clearest TRACE contribution is to frame debt recovery during review/dispute as a clock problem: recovery must stop or slow while correction is still live, otherwise the money path hardens faster than the affected person can contest it.

## What existing fields already cover

```trace
existing_fields_cover:
  debt_collection_ethics
  + administrative_review
  + vulnerability_policy
  + automation_review
  + algorithmic transparency
  + legal advice/documentation
```

TRACE does not replace these fields. It links them through clock, gate, route, and hardening language.

## Demoters

```trace
demote_debt_clock_if:
  existing_debt_law_already_provides_equal_clock_route_test
  + less_vocabulary_burden
```

```trace
demote_payment_gate_if:
  no_material_access_or_future_path_change
```

```trace
demote_repair_outbid_if:
  no_measurable_repair_capacity_loss
```

## Verdict

```trace
verdict :=
  Robodebt_supports_debt_clock_as_strong_candidate
  + supports_payment_gate_as_promising_candidate
  + supports_repair_outbid_as_question
  + does_not_yet_support_interest_as_hardening_or_credit_scar
  - validation
```

## Next move

```trace
next_move :=
  either:
    add_debt_clock_to_operator_registry_as_pending_comparator
  OR:
    run_one_more_source_check_against_existing_debt_collection_law
```

Recommended:

```trace
recommended_next :=
  add_debt_clock_to_operator_registry_as_pending_comparator
  with:
    comparator_required
    + must_not_claim_all_debt_bad
```

Plain version:

Debt Clock has enough signal to enter the registry as `pending_comparator`, not as active. It must be tested against debt collection law, administrative review, and poverty-law comparators before promotion.
