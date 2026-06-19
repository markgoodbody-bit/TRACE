# TRACE Real Use Capture — Energy Switch 2026-06-19 v0.1

Status: real-use capture / ordinary-life decision record / not validation / not proof / not source authority.

```trace
real_use_case :=
  household_energy_switch
  + estimated_usage_problem
  + daylight_meter_read_constraint
  + tariff_choice
  - validation
```

## 1. Situation

```trace
situation :=
  date := 2026-06-19
  domain := household_energy_supplier_switch
  affected_subjects := Mark + household_budget + future_energy_flexibility
  decision_window := comparison_offer_window + meter_read_update_window
  hardening_risk := fixed_contract_choice + exit_fee + wrong_estimate
```

Plain description:

Mark was comparing household energy tariffs. The main visible decision was whether to switch supplier and which fixed tariff to choose. The hidden issue was that the current gas usage appeared to be based on an estimated reading, so comparison accuracy depended on obtaining and using an actual gas meter reading.

## 2. No-TRACE baseline

```trace
baseline :=
  likely_action_without_TRACE := choose_cheapest_visible_comparison_result
  likely_blind_spot := estimated_gas_usage + exit_fee_lock_in
  likely_overreaction_or_underreaction := switch_too_fast_or_overweight_headline_saving
```

Plain baseline:

Ordinary comparison behaviour might have selected the lowest monthly quote without first checking whether the input data was real or estimated. It might also have ignored the difference between a 12-month and 24-month lock where the annual saving looked identical.

## 3. TRACE read

```trace
TRACE_read :=
  visible_symptom := cheaper_tariff_available
  possible_source := comparison_accuracy_depends_on_actual_meter_read
  anomalies := estimated_gas_read + tariff_lock_length + exit_fee_difference
  knowledge_carriers := EDF_bill + comparison_site + actual_meter + Mark_daylight_access
  local_records := meter_read + supplier_account + tariff_terms
  last_touch := latest_actual_meter_read_missing_or_unconfirmed
  local_fix_or_workaround := obtain_actual_read_before_final_switch
  carrier_fit := comparison_site_useful_only_if_inputs_are_real
  timed_gate := wait_until_meter_read_available_then_compare
```

The live-use value was not that TRACE found a clever answer. It forced the decision to route through actual input quality before accepting the comparison output.

## 4. Next action chosen

```trace
next_action :=
  action := obtain_actual_gas_meter_read_then_compare_tariffs
  recommended_tariff := EON_Next_Fixed_12m_Exclusive_v2_if_terms_hold
  what_was_not_done := immediate_switch_on_estimated_data + 24_month_lock
  why_not := estimate_risk + avoid_unnecessary_longer_lock_and_exit_fee
```

The working recommendation became: choose the 12-month E.ON fixed tariff rather than the 24-month version, assuming unit rates, standing charges, exit fee structure, smart-meter/payment conditions, and final actual-usage comparison were acceptable.

## 5. Outcome

```trace
outcome :=
  immediate_result := decision_clarified
  later_result := switch_completion_not_recorded_here
  harm_avoided_or_reduced := avoided_decision_on_estimated_gas_data
  cost_created := delayed_decision_until_meter_read_possible
  unresolved_residue := final_supplier_terms_and_completed_switch_not_logged
```

Plain outcome:

The process improved the decision quality before final action. It did not prove that the selected tariff was best long-term. It also did not record whether the switch was completed.

## 6. Demoter / falsifier

```trace
demoter :=
  no_added_value_if := ordinary_comparison_process_would_have_forced_actual_meter_read_anyway
  made_worse_if := TRACE_delayed_switch_until_offer_lost_without_material_data_gain
  expert_gap := full_tariff_terms + unit_rates + payment_conditions + exit_fee_total_or_per_fuel
```

This case would be demoted if the supplier or comparison site already required the actual meter reading before action, or if the delay caused a better offer to be lost without improving accuracy.

## 7. Classification

```trace
classification := useful_with_outcome_pending
```

Definitions note: the case appears useful because it changed the action sequence and guarded against estimated-input error. Final outcome remains pending because completion and actual bill impact are not recorded.

## 8. Scar / memory note

```trace
scar_note :=
  keep := input_quality_before_headline_saving
  do_not_generalise := TRACE_did_not_find_best_energy_tariff_generally
  future_patch_candidate := real_use_capture_needs_completed_outcome_followup
```

End.
