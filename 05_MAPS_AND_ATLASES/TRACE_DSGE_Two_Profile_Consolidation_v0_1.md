# TRACE DSGE Two-Profile Consolidation v0.1

Date: 2026-06-18
Status: DSGE two-profile consolidation / toy schematic macro branch / contrast matrix / no forecast / no policy advice / not validation / not proof / not solved DSGE / not macroeconomic theory / not operator promotion / not Kernel v0.3

## 0. Control header

This file consolidates the first two DSGE / Dynamic Macroeconomics toy profile probes:

1. `TRACE_DSGE_One_Shock_Response_Profile_Worked_Example_v0_1.md`
2. `TRACE_DSGE_Demand_vs_Supply_Shock_Profile_Contrast_v0_1.md`

It also carries forward:

- `TRACE_DSGE_First_Example_Toy_Status_Patch_v0_1.md`
- `TRACE_Profile_Morphism_Formal_Status_Patch_v0_1.md`

It does not solve a DSGE model.

It does not use real data.

It does not estimate or calibrate parameters.

It does not forecast.

It does not offer policy advice.

```trace
DSGE_Two_Profile_Consolidation_v0_1 :=
  one_shock_response_profile
  + demand_vs_supply_profile_contrast
  -> common_success_failure_matrix
  + macro_flattening_rules
  + macro_profile_translation_seed
  - validation
  - solved_DSGE
  - forecast
  - policy_advice
```

## 1. Why this consolidation matters

The first DSGE example tested whether TRACE could preserve a toy model-conditioned path rather than flatten it into generic causation.

The second DSGE example tested whether TRACE could preserve a contrast between two toy shock profiles, where inflation rises in both but output-gap direction differs.

Together they test whether TRACE can preserve macro profile structure without turning macroeconomics into ordinary event-story language.

```trace
macro_flattening_errors :=
  shock_as_generic_event
  + impulse_response_as_prediction
  + policy_rate_as_advice
  + model_output_as_reality
  + same_inflation_direction_as_same_profile
```

## 2. Shared DSGE TRACE-form

```trace
TRACE_form(Dynamic_Macroeconomics_DSGE) :=
  {S_Macro, T_Macro, C_Macro, O_Macro, K_Macro, B_Macro, I_Macro}
```

Working role meanings:

```trace
S_Macro := toy_model_state_variable_and_role_context
T_Macro := schematic_transition_or_response_path
C_Macro := profile_composition_or_contrast_when_relevant
O_Macro := impulse_response_readout_or_profile_table
K_Macro := schematic_constraints_policy_response_and_scope_conditions
B_Macro := horizon_reference_path_and_no_forecast_boundary
I_Macro := response_profile_or_contrast_profile
```

Toy-status rule remains active:

```trace
toy_status_active :=
  all_DSGE_values := schematic_placeholder_profile_values
  not:
    solved_model_output
    OR empirical_estimate
    OR forecast
    OR policy_counterfactual
```

## 3. Common success-failure matrix

| Example | Native distinction tested | TRACE role pressure | Success condition | Failure condition | Earned result |
|---|---|---|---|---|---|
| One demand-shock response profile | model-conditioned path vs generic causation story | `I_Macro` response path; `B_Macro` toy/no-forecast boundary; `K_Macro` schematic constraint context | Recover toy case, shock context, variable roles, response path, toy scope, and no-forecast boundary | Returns only “demand shock caused output/inflation to rise” | TRACE preserves one toy impulse-response profile internally |
| Demand vs supply shock contrast | same inflation direction but different output-gap direction | `I_Macro` contrast profile; `C_Macro` profile contrast; `O_Macro` profile readout | Recover shock-type distinction and output-gap direction contrast | Flattens both to “inflation rises and policy responds” | TRACE preserves one toy two-profile macro contrast internally |

## 4. Common back-translation suite

A macro profile translation is internally live only if back-translation recovers model-conditioning and toy status.

```trace
DSGE_back_translation_suite :=
  recover_toy_model_or_profile_case
  + recover_shock_type_and_exogenous_status
  + recover_tracked_variable_roles
  + recover_response_path_values_as_schematic
  + recover_horizon_and_reference_path
  + recover_policy_rate_as_response_variable_not_advice
  + recover_no_forecast_no_empirical_boundary
  + recover_loss_register
```

For current examples:

```trace
current_DSGE_back_translation_targets :=
  one_shock_profile:
    positive_demand_shock
    + y_pi_i_paths
    + policy_rate_as_response_variable
    + no_forecast_boundary
  demand_vs_supply_contrast:
    demand_shock_identity
    + supply_shock_identity
    + output_gap_direction_contrast
    + inflation_up_in_both_profiles
    + no_policy_advice_boundary
```

Failure:

```trace
DSGE_translation_fails_if:
  back_translation_returns_story_only
  OR response_path_values_become_prediction
  OR policy_rate_becomes_advice
  OR shock_type_distinction_lost
  OR toy_status_hidden
```

## 5. Emerging macro profile translation seed

```trace
macro_profile_translation_seed :=
  model_or_toy_case
  -> shock_context
  -> tracked_variable_roles
  -> response_path_profile
  -> horizon_reference_and_scope
  -> TRACE_I_Macro
  -> back_translation_test
```

Acceptable translation:

```trace
acceptable_macro_profile_translation_if:
  native_macro_case_recoverable
  + shock_context_recoverable
  + variable_roles_recoverable
  + response_path_recoverable_as_toy_or_model_conditioned
  + no_forecast_boundary_recoverable
  + loss_register_visible
```

Unacceptable translation:

```trace
unacceptable_macro_profile_translation_if:
  causal_story_only
  OR numbers_as_prediction
  OR policy_variable_as_advice
  OR model_output_as_reality
  OR toy_values_as_calibration
```

## 6. Cross-example anti-flattening rules

```trace
anti_flattening_rules :=
  shock != generic_event
  + impulse_response != forecast
  + policy_rate_path != policy_advice
  + model_conditioned_path != actual_history
  + calibration_or_estimation != truth
  + same_inflation_direction != same_macro_profile
  + toy_table != solved_model
```

Plain version:

TRACE may translate macro model profiles only if it keeps model-conditioning, variable roles, shock context, toy status, and loss visible.

## 7. Combined loss ledger

### 7.1 Toy profiles only

```trace
loss_entry_1 :=
  source_feature := full_DSGE_model_solution
  -> TRACE_translation := toy_schematic_response_profiles
  -> loss_or_distortion := no_equations_no_solution_method_no_determinacy_check
  -> consequence_for_back_translation := no_solved_DSGE_claim
```

### 7.2 No empirical grounding

```trace
loss_entry_2 :=
  source_feature := empirical_estimation_calibration_or_fit
  -> TRACE_translation := not_tested
  -> loss_or_distortion := no_data_or_parameter_estimation
  -> consequence_for_back_translation := no_forecast_or_empirical_claim
```

### 7.3 Expectations absent

```trace
loss_entry_3 :=
  source_feature := formal_expectations_structure
  -> TRACE_translation := named_gap_only
  -> loss_or_distortion := no_forward_solution_or_expectations_operator
  -> consequence_for_back_translation := no_expectations_preserved_claim
```

### 7.4 Policy and welfare excluded

```trace
loss_entry_4 :=
  source_feature := welfare_analysis_and_policy_evaluation
  -> TRACE_translation := excluded
  -> loss_or_distortion := no_welfare_loss_or_policy_objective
  -> consequence_for_back_translation := no_policy_advice
```

### 7.5 Structural shock identification absent

```trace
loss_entry_5 :=
  source_feature := structural_shock_identification
  -> TRACE_translation := named_toy_shock_types
  -> loss_or_distortion := shock_types_not_empirically_identified
  -> consequence_for_back_translation := no_real_structural_shock_claim
```

## 8. Status after two DSGE profiles

```trace
DSGE_two_profile_status :=
  INTERNAL_PROFILE_CANDIDATE
  + NATIVE_REVIEW_REQUIRED
  + TOY_STATUS_COOLED
  for:
    one_shock_response_profile
    + demand_vs_supply_profile_contrast
  because:
    response_path_structure_preserved_internally
    + shock_type_contrast_preserved_internally
    + macro_flattening_errors_named
    + loss_register_visible
  but:
    no_equations
    + no_estimation
    + no_expectations_solution
    + no_policy_welfare_analysis
    + no_specialist_review
```

## 9. What this earns

```trace
earned_claim :=
  TRACE_DSGE_branch_now_has_two_internal_toy_profile_translation_probes
  + common_macro_back_translation_suite_exists
  + macro_profile_translation_seed_exists
  + model_conditioned_path_not_generic_causation_story_is_testable
  + same_inflation_different_output_gap_contrast_is_testable
  - validation
  - solved_DSGE
  - forecast
  - policy_advice
  - macro_unification
```

This is expansion with toy-status control.

## 10. What remains untested

```trace
not_tested :=
  actual_model_equations
  + microfoundations
  + expectations_solution
  + equilibrium_determinacy
  + parameter_estimation
  + empirical_IRFs
  + structural_shock_identification
  + welfare_loss
  + optimal_policy
  + HANK_or_representative_agent_structure
  + central_bank_model_comparison
  + specialist_review
```

## 11. Next domain gate: Generative Syntax

The fourth Qwen stress domain is Generative Syntax / Minimalist Program.

Before entering it, the following gate applies:

```trace
syntax_entry_gate :=
  DSGE_two_profile_consolidation_complete
  + no_macro_terms_imported_into_syntax
  + syntax_native_input_packet_required
  + native_syntax_object_space_named
  + native_syntax_operation_or_profile_family_named
  + loss_register_required
```

Recommended next file:

```trace
recommended_next :=
  TRACE_Generative_Syntax_Translation_Input_Packet_v0_1
  because:
    four_domain_stress_map_requires_syntax
    + QIT_topology_macro_paths_now_have_internal_seed_examples
    + syntax_tests_symbolic_structure_not_quantity
```

Alternative next:

```trace
alternative_next :=
  DSGE_two_profile_hostile_audit
  if:
    macro_branch_needs_more_cooling_before_syntax
```

## 12. Final compression

```trace
DSGE_Two_Profile_Consolidation_v0_1 :=
  examples := one_shock_response + demand_vs_supply_contrast
  shared_test := macro_profile_back_translation
  anti_flattening := shock_not_event + IRF_not_forecast + policy_rate_not_advice + toy_table_not_solution
  status := INTERNAL_PROFILE_CANDIDATE + NATIVE_REVIEW_REQUIRED + TOY_STATUS_COOLED
  earned := two_internal_DSGE_profile_probes + macro_profile_translation_seed
  next := Generative_Syntax_input_packet
  - validation
  - solved_DSGE
  - forecast
  - policy_advice
```

End.
