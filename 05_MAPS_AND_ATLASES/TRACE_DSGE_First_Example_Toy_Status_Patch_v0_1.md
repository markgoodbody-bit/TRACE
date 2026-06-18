# TRACE DSGE First Example Toy Status Patch v0.1

Date: 2026-06-18
Status: toy-status patch / DSGE first worked example / forecast-block / policy-advice-block / not validation / not proof / not macroeconomic theory / not solved model / not operator promotion / not Kernel v0.3

## 0. Control header

This file responds to `TRACE_DSGE_First_Example_Hostile_Audit_v0_1.md`.

It patches the formal status of `TRACE_DSGE_One_Shock_Response_Profile_Worked_Example_v0_1.md` before any second macro profile.

It does not add a second DSGE example.

It does not claim a solved model.

It does not make a forecast.

It does not offer policy advice.

```trace
DSGE_First_Example_Toy_Status_Patch_v0_1 :=
  toy_table_not_model_solution
  + policy_rate_not_policy_advice
  + expectations_gap_visible
  + response_values_not_derived
  + no_forecast_no_empirical_claim
  + loss_register_claim_effects
  -> first_DSGE_probe_terms_cooled
  - validation
  - solved_DSGE
  - macro_theory_claim
  - policy_advice
```

## 1. Patch target

```trace
patch_target :=
  TRACE_DSGE_One_Shock_Response_Profile_Worked_Example_v0_1
```

This patch does not delete or replace the worked example. It controls how the worked example must now be read.

## 2. Toy table status

The numerical response path table must be read as schematic placeholder profile values.

```trace
toy_table_status :=
  schematic_placeholder_profile_values
  not:
    solved_model_output
    OR empirical_estimate
    OR forecast
    OR calibration_result
    OR policy_counterfactual
```

Allowed reading:

```trace
allowed_toy_table_reading :=
  internal_translation_test
  for:
    model_conditioned_path_shape
    + variable_role_preservation
    + back_translation_recovery
```

Not allowed:

```trace
not_allowed_toy_table_reading :=
  prediction_of_actual_economy
  OR result_of_DSGE_solution
  OR evidence_about_policy_effects
  OR macroeconomic_truth_claim
```

## 3. Policy-rate status

The policy-rate variable `i` must be read as a schematic response variable in the toy profile.

```trace
policy_rate_status :=
  schematic_response_variable_in_toy_profile
  not:
    policy_recommendation
    OR central_bank_intention_claim
    OR welfare_optimal_response
    OR institutional_judgment
```

Allowed reading:

```trace
allowed_policy_rate_reading :=
  profile_variable_used_to_test_role_preservation
```

Failure if misread:

```trace
policy_rate_misread_failure :=
  profile_variable_becomes_policy_advice
  OR model_role_becomes_human_intention
```

## 4. Expectations gap status

Expectations are a native macro feature named in the input packet, but they are not modelled in the first worked example.

```trace
expectations_status :=
  named_as_unmodelled_gap
  not:
    preserved_in_first_worked_example
    OR solved_expectations_structure
    OR forward_solution_condition
```

Consequence:

```trace
expectations_consequence :=
  no_DSGE_expectations_preserved_claim
  + no_rational_expectations_solution_claim
  + expectation_gap_must_remain_visible
```

## 5. Response-values status

The response values are illustrative translation-profile values, not derived values.

```trace
response_values_status :=
  illustrative_translation_profile
  not:
    derived_from_structural_model
    OR solved_from_equations
    OR generated_by_estimation
    OR calibrated_from_data
```

Consequence:

```trace
response_values_consequence :=
  can_test_translation_of_path_profile
  but:
    cannot_claim_response_mechanism
    + cannot_claim_model_solution
```

## 6. IRF not forecast label

Every later use of this DSGE path profile must carry its status label.

```trace
IRF_status_label_required :=
  toy_or_model_conditioned_status
  + no_forecast_status
  + no_empirical_status
  + no_policy_advice_status
```

Failure:

```trace
IRF_label_failure :=
  table_read_as_real_economy_prediction
  OR table_read_as_policy_evidence
```

## 7. Loss register claim effects

The loss register must change allowed claims.

```trace
loss_register_claim_effects :=
  no_equations -> no_solved_model_claim
  + no_estimation -> no_empirical_claim
  + no_solution_method -> no_solution_claim
  + no_expectations -> no_expectations_preserved_claim
  + no_welfare -> no_policy_advice
  + no_source_review -> native_review_required
```

No consequence means audit theatre.

```trace
no_consequence_loss :=
  invalid_loss_register_entry
```

## 8. Updated back-translation requirement

The back-translation target remains valid only under toy status.

```trace
BT_DSGE_required_recovery_after_patch :=
  toy_DSGE_style_case
  + positive_demand_shock_as_exogenous_for_toy_case
  + y_pi_i_as_tracked_response_variables
  + response_path_values_as_schematic_profile
  + policy_rate_as_toy_response_variable
  + no_forecast_boundary
  + no_policy_advice_boundary
  + missing_equations_and_expectations_as_declared_losses
```

Failure:

```trace
BT_DSGE_fails_if:
  returns:
    real_forecast
    OR solved_model_result
    OR policy_recommendation
    OR generic_causation_story
```

## 9. Updated status

```trace
DSGE_first_example_status_after_patch :=
  INTERNAL_PROFILE_CANDIDATE
  + NATIVE_REVIEW_REQUIRED
  + TOY_STATUS_COOLED
  for:
    one_shock_schematic_response_profile_only
```

Meaning:

```trace
status_means :=
  useful_internal_translation_probe
  + macro_role_preservation_test
  + model_conditioned_path_shape_test
  + not_solved_model
  + not_forecast
  + not_policy_advice
```

## 10. Gate before second macro profile

A second macro profile may proceed only if it preserves this patch.

```trace
second_macro_profile_gate :=
  toy_status_patch_complete
  + no_forecast_boundary_active
  + no_policy_advice_boundary_active
  + native_macro_profile_family_named
  + source_gap_visible
  + loss_register_required
  + back_translation_target_written
```

Possible next macro example:

```trace
possible_next_macro_example :=
  compare_two_shock_profiles
  such_as:
    demand_shock_profile
    vs
    supply_shock_profile
  only_as:
    toy_schematic_translation_probe
```

Alternative:

```trace
alternative_next :=
  DSGE_first_example_consolidation
```

## 11. Updated must-not-claim

```trace
must_not_claim_after_patch :=
  solved_DSGE_model
  OR empirical_macro_result
  OR forecast
  OR policy_advice
  OR welfare_result
  OR expectations_preserved
  OR calibrated_model_output
  OR central_bank_intention
```

## 12. Updated allowed claim

```trace
allowed_claim_after_patch :=
  TRACE_has_internal_toy_DSGE_response_profile_probe
  + toy_table_status_is_cool
  + policy_rate_policy_advice_leak_is_blocked
  + expectations_gap_is_visible
  + response_values_are_not_derived
  + no_forecast_no_empirical_boundary_is_active
  + second_macro_profile_may_proceed_only_under_gate
  - validation
  - solved_model
  - policy_advice
```

## 13. Final compression

```trace
DSGE_First_Example_Toy_Status_Patch_v0_1 :=
  table := schematic_placeholder_profile_values
  policy_rate := schematic_response_variable_not_policy_advice
  expectations := unmodelled_gap
  response_values := illustrative_not_derived
  loss := allowed_claim_affecting
  status := INTERNAL_PROFILE_CANDIDATE + NATIVE_REVIEW_REQUIRED + TOY_STATUS_COOLED
  next := second_macro_profile_or_consolidation_under_gate
  - validation
  - solved_DSGE
  - forecast
  - policy_advice
```

End.
