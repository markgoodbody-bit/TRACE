# TRACE Pressure Comparator Test v0.1

Status: comparator pressure test / pattern challenge. Not canon. Not validation. Not a public historical evidence file. This file tests whether the *Pressure* case note pattern distinguishes good from bad pressure decisions, or whether it is too broad.

```trace
Pressure_Comparator_Test_v0_1 :=
  comparator_pressure_test
  + pattern_challenge
  + demotion_check
  + distinction_test
  - canon
  - validation
```

Source case note:

`04_COVERAGE/PRESSURE_CASE_NOTE_v0_1/TRACE_Pressure_Uncertainty_Under_Command_Case_Note_v0_1.md`

## Candidate pattern under test

```trace
candidate_pattern :=
  good_pressure_system
  = disciplined_conversion_of_uncertainty_into_action
```

Expanded:

```trace
Pressure_pattern :=
  uncertainty_high
  + action_window_closing
  + consequence_irreversible_or_high
  + authority_demands_closure
  -> requires:
      uncertainty_visible
      + competing_clocks_named
      + dissent_legible
      + decision_owner_named
      + downstream_subjects_visible
```

Question:

```trace
test_question :=
  does_this_pattern_distinguish_good_pressure_decisions
  from_bad_pressure_decisions?
```

If not, it is too general and should be demoted.

## Scoring frame

Each comparator is scored on five fields:

```trace
score_fields :=
  uncertainty_visibility
  + competing_clocks_named
  + dissent_or_warning_legible
  + decision_owner_named
  + downstream_subject_visibility
```

Each field gets:

```trace
field_score :=
  present
  OR partial
  OR weak
  OR absent
  OR unknown
```

Overall status:

```trace
overall_status :=
  distinguishes_pattern
  OR too_general
  OR needs_more_cases
```

## Comparator 1 — Pressure / D-Day weather decision

```trace
Pressure_case :=
  uncertainty_visibility := present
  competing_clocks_named := present
  dissent_or_warning_legible := present
  decision_owner_named := present
  downstream_subject_visibility := present
```

Read:

```trace
Pressure_good_pattern :=
  uncertainty_not_erased
  + clocks_compared
  + Stagg_truth_carrier_survives
  + Eisenhower_closure_owner
  + troops_as_consequence_bearers
```

Why it scores well:

- Uncertainty remains visible.
- Delay and action both carry cost.
- The truth carrier is not simply silenced.
- The commander owns selection.
- The cost is visibly borne by bodies.

Caution:

```trace
Pressure_caution :=
  success_after_action
  != process_validation
```

## Comparator 2 — Challenger launch decision

```trace
Challenger_case :=
  uncertainty_visibility := weak
  competing_clocks_named := partial
  dissent_or_warning_legible := weakened
  decision_owner_named := diffused
  downstream_subject_visibility := weak
```

Read:

```trace
Challenger_bad_pattern :=
  warning_signal_under_schedule_pressure
  + proof_burden_shifted_to_warners
  + launch_selected
  + crew_pays
```

Distinction from Pressure:

```trace
Pressure_vs_Challenger :=
  Pressure_preserves_unwelcome_uncertainty
  while_Challenger_weakens_warning_under_schedule_pressure
```

Why this matters:

A pressure system fails when the warning carrier is forced to provide impossible certainty before the action will pause.

Demoter check:

```trace
demoter_check_Challenger :=
  if_case_records_show_warning_was_fully_visible_and_owned
  then_this_read_weakens
```

## Comparator 3 — Cuban Missile Crisis / ExComm pressure chamber

```trace
Cuban_Missile_Crisis_case :=
  uncertainty_visibility := present
  competing_clocks_named := present
  dissent_or_warning_legible := present
  decision_owner_named := present
  downstream_subject_visibility := partial
```

Read:

```trace
Cuban_Missile_Crisis_good_pattern :=
  catastrophic_irreversibility
  + pressure_for_decisive_action
  + option_space_preserved
  + less_irreversible_pressure_selected_first
```

Distinction:

```trace
Cuban_Missile_Crisis_distinction :=
  good_pressure_system_can_delay_closure
  when_delay_preserves_option_space
```

This prevents the pattern from becoming blindly pro-decision or pro-delay.

## Comparator 4 — Chernobyl safety test disaster

```trace
Chernobyl_case :=
  uncertainty_visibility := weak
  competing_clocks_named := weak
  dissent_or_warning_legible := weak_or_absent
  decision_owner_named := diffused
  downstream_subject_visibility := absent_before_event
```

Read:

```trace
Chernobyl_bad_pattern :=
  test_pressure
  + hidden_design_and_operational_risk
  + weak_truth_culture
  + safety_test_becomes_harm_carrier
  + body_and_ecology_bill
```

Distinction:

```trace
Chernobyl_distinction :=
  if_test_requires_weakening_constraints
  then_test_itself_may_become_harm_carrier
```

This adds a special case to the pressure pattern: not all pressure decisions are explicit command decisions. Some are procedural tests whose risk is hidden inside routine.

## Comparator 5 — Therac-25 medical-machine harm

```trace
Therac_25_case :=
  uncertainty_visibility := weak
  competing_clocks_named := absent
  dissent_or_warning_legible := weak
  decision_owner_named := diffused
  downstream_subject_visibility := absent_until_patient_harm
```

Read:

```trace
Therac_25_bad_pattern :=
  software_confidence
  + interlock_loss
  + opaque_error_signal
  + operator_and_patient_signal_dismissed
  + patient_body_pays
```

Distinction:

```trace
Therac_25_distinction :=
  machine_confidence_can_suppress_uncertainty_visibility
```

This is directly relevant to AI/tool systems: a confident interface can make uncertainty socially invisible.

## Comparator 6 — Apollo 13 improvised repair

```trace
Apollo_13_case :=
  uncertainty_visibility := present
  competing_clocks_named := present
  dissent_or_warning_legible := present
  decision_owner_named := present
  downstream_subject_visibility := present
```

Read:

```trace
Apollo_13_good_pattern :=
  damage_visible
  + clock_visible
  + options_constrained
  + repair_carriers_identified
  + improvisation_under_truth
```

Distinction:

```trace
Apollo_13_distinction :=
  good_pressure_system_can_switch_from_plan_execution
  to_repair_carrier_search
```

This expands the pattern: disciplined conversion of uncertainty into action may mean abandoning the original objective and finding the smallest survivable repair path.

## Comparator 7 — Bay of Pigs planning / group pressure caution

```trace
Bay_of_Pigs_case :=
  uncertainty_visibility := weak
  competing_clocks_named := partial
  dissent_or_warning_legible := weak
  decision_owner_named := present_but_influenced
  downstream_subject_visibility := partial
```

Read:

```trace
Bay_of_Pigs_bad_pattern :=
  inherited_plan
  + prestige_pressure
  + weak_dissent_processing
  + optimistic_assumptions
  + failure_bill_on_invaders_and_civilians
```

Distinction:

```trace
Bay_of_Pigs_distinction :=
  decision_owner_named_is_not_enough
  if_option_space_and_dissent_are_captured
```

This challenges the pattern usefully. Naming a decision owner alone does not make closure honest.

## Cross-case result

```trace
cross_case_result :=
  pattern_distinguishes_some_good_from_bad_pressure_decisions
  + needs_careful_role_and_signal_analysis
  - sufficient_as_operator
  - sufficient_as_validation
```

The pattern is not empty. It distinguishes:

```trace
distinguishes :=
  Pressure_from_Challenger
  + Cuban_Missile_Crisis_from_Bay_of_Pigs
  + Apollo_13_from_Chernobyl_or_Therac_25
```

But it is still too broad to promote as an operator without source-pinned casework.

## What the test changed

### Strengthened

```trace
strengthened :=
  good_pressure_system_sentence
  + minimum_honest_closure
  + role_separation
  + hidden_bill_vector
```

The retained sentence remains strong:

> A good pressure system does not eliminate uncertainty; it disciplines the conversion of uncertainty into action.

### Weakened

```trace
weakened :=
  automatic_operator_candidate
  + broad_AI_alignment_bridge
  + any_claim_of_historical_validation
```

### Added distinction

```trace
added_distinctions :=
  decision_owner_named_is_not_enough
  + uncertainty_visibility_can_be_suppressed_by_interface_confidence
  + pressure_system_can_require_repair_path_switch
  + test_itself_can_become_harm_carrier
```

## Revised candidate pattern

```trace
revised_candidate_pattern :=
  Pressure_Discipline_Pattern

not :=
  Uncertainty_to_Action_Gate_operator
```

This is better as a pattern note than a gate/operator.

```trace
Pressure_Discipline_Pattern :=
  under_high_consequence_uncertainty:
    preserve_uncertainty_visibility
    + name_competing_clocks
    + keep_warning_signal_legible
    + identify_real_decision_owner
    + show_downstream_subjects
    + select_or_repair_before_window_closes
```

## Demoters after comparator test

```trace
demoters :=
  if_pattern_cannot_explain_when_delay_is_better_than_action
  OR if_pattern_cannot_explain_when_action_is_better_than_delay
  OR if_standard_decision_theory_fully_captures_subject_burden_and_repairability
  OR if_source_pinned_casework_contradicts_role_analysis
  OR if_AI_bridge_becomes_solution_claim
  then_demote_pattern
```

## Current status

```trace
current_status :=
  Pressure_Discipline_Pattern := support_candidate
  operator_status := rejected_for_now
  case_note_status := useful_internal
  public_status := source_pin_required
  validation_status := false
```

## Next action

Do not expand further.

```trace
next_action :=
  if_public_use_desired:
    source_pin_each_comparator
    + shorten_to_one_page
  else:
    stop_here
```

End.
