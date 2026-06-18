# TRACE DSGE Demand vs Supply Shock Profile Contrast v0.1

Date: 2026-06-18
Status: second DSGE worked example / toy schematic contrast profile / no forecast / no policy advice / not validation / not proof / not solved DSGE / not macroeconomic theory / not operator promotion / not Kernel v0.3

## 0. Control header

This file follows:

- `TRACE_DSGE_Translation_Input_Packet_v0_1.md`
- `TRACE_DSGE_One_Shock_Response_Profile_Worked_Example_v0_1.md`
- `TRACE_DSGE_First_Example_Toy_Status_Patch_v0_1.md`

It adds a second macro profile only under the active toy-status gate.

It does not use real data.

It does not solve a DSGE model.

It does not estimate parameters.

It does not make a forecast.

It does not offer policy advice.

```trace
DSGE_Demand_vs_Supply_Shock_Profile_Contrast_v0_1 :=
  toy_demand_shock_profile
  vs
  toy_supply_shock_profile
  + same_inflation_direction_different_macro_structure
  + response_path_profile_contrast
  + back_translation_test
  + loss_register
  - validation
  - solved_DSGE
  - forecast
  - policy_advice
```

## 1. Native contrast case

```trace
native_contrast_case :=
  toy_DSGE_style_model_family_placeholder
  + two_exogenous_shock_types
  + same_tracked_variables
  + four_period_response_profiles
```

Tracked variables remain:

```trace
tracked_variables :=
  output_gap_y
  + inflation_pi
  + policy_rate_i
```

Shock profiles:

```trace
shock_profiles :=
  demand_shock:
    positive_demand_shock
    + period_0_arrival
    + normalised_size_1
    + exogenous_for_this_toy_case
  supply_shock:
    negative_supply_shock_or_cost_push_shock
    + period_0_arrival
    + normalised_size_1
    + exogenous_for_this_toy_case
```

Boundary:

The values below are schematic placeholder profile values. They are not solved model output, empirical estimates, forecasts, calibration results, or policy counterfactuals.

## 2. Native profile family

```trace
native_profile_family :=
  impulse_response_profile_contrast
```

Profile assignment:

```trace
Phi_DSGE:
  {toy_demand_shock_case, toy_supply_shock_case}
  -> impulse_response_profile_contrast
```

Core distinction:

```trace
core_native_distinction :=
  demand_shock:
    output_gap_up
    + inflation_up
    + policy_rate_response_up_in_toy_profile
  supply_shock:
    output_gap_down
    + inflation_up
    + policy_rate_response_up_in_toy_profile
```

Plain version:

Both toy shocks raise inflation in the schematic profiles, but they differ in output-gap direction. That is the translation test: TRACE must not flatten both into “inflation rises, policy responds.”

## 3. Demand-shock toy profile

| Period | Demand shock | Output gap `y` | Inflation `pi` | Policy rate `i` | Native reading |
|---|---:|---:|---:|---:|---|
| `t=0` | `+1.0` | `+0.8` | `+0.3` | `+0.2` | demand disturbance; output and inflation above reference |
| `t=1` | `0.0` | `+0.5` | `+0.4` | `+0.4` | persistence and schematic policy response visible |
| `t=2` | `0.0` | `+0.2` | `+0.2` | `+0.3` | decay toward reference |
| `t=3` | `0.0` | `0.0` | `+0.1` | `+0.1` | near return toward reference |

```trace
demand_profile :=
  shock_type := positive_demand_shock
  y_path := [0.8, 0.5, 0.2, 0.0]
  pi_path := [0.3, 0.4, 0.2, 0.1]
  i_path := [0.2, 0.4, 0.3, 0.1]
  status := schematic_placeholder_profile_values
```

## 4. Supply-shock toy profile

| Period | Supply shock | Output gap `y` | Inflation `pi` | Policy rate `i` | Native reading |
|---|---:|---:|---:|---:|---|
| `t=0` | `+1.0` | `-0.5` | `+0.6` | `+0.2` | cost-push disturbance; inflation up while output gap falls |
| `t=1` | `0.0` | `-0.4` | `+0.5` | `+0.3` | inflation remains elevated; output remains below reference |
| `t=2` | `0.0` | `-0.2` | `+0.3` | `+0.2` | gradual decay toward reference |
| `t=3` | `0.0` | `0.0` | `+0.1` | `+0.1` | near return toward reference |

```trace
supply_profile :=
  shock_type := negative_supply_or_cost_push_shock
  y_path := [-0.5, -0.4, -0.2, 0.0]
  pi_path := [0.6, 0.5, 0.3, 0.1]
  i_path := [0.2, 0.3, 0.2, 0.1]
  status := schematic_placeholder_profile_values
```

## 5. Contrast profile object

```trace
DSGE_contrast_profile_object :=
  model_family_status := toy_placeholder
  tracked_variables := {y, pi, i}
  horizon := 4_periods
  reference_path := steady_state_deviation_baseline
  shock_pair := {positive_demand_shock, negative_supply_or_cost_push_shock}
  demand_profile := demand_profile
  supply_profile := supply_profile
  contrast := output_gap_direction_differs_while_inflation_rises_in_both
  loss_register := L_DSGE_contrast
```

This is a contrast profile for translation testing, not a policy or empirical claim.

## 6. TRACE-form mapping

```trace
TRACE_form(Dynamic_Macroeconomics_DSGE) :=
  {S_Macro, T_Macro, C_Macro, O_Macro, K_Macro, B_Macro, I_Macro}
```

Mapping:

```trace
S_Macro := toy_model_family_and_variable_role_context
T_Macro := two_schematic_transition_response_paths
C_Macro := contrast_composition_of_two_toy_profiles
O_Macro := impulse_response_contrast_readout
K_Macro := schematic_constraints_policy_response_and_toy_scope
B_Macro := horizon_reference_path_and_no_forecast_boundary
I_Macro := demand_vs_supply_response_profile_contrast
```

## 7. Profile-preserving morphism instance

Using cooled morphism language:

```trace
m_DSGE_contrast:
  structured_native_macro_contrast_record
  -> structured_TRACE_macro_contrast_record
```

Read as candidate translation-map shape only.

Preservation target:

```trace
m_DSGE_contrast_preserves :=
  demand_shock_identity
  + supply_shock_identity
  + both_exogenous_for_toy_case
  + tracked_variable_roles
  + demand_response_path_values
  + supply_response_path_values
  + output_gap_direction_contrast
  + inflation_rises_in_both_profiles
  + no_forecast_no_policy_advice_boundaries
  + loss_register
```

## 8. Back-translation test

```trace
BT_DSGE(m_DSGE_contrast(toy_pair))
  ~=
  demand_vs_supply_toy_contrast_under_declared_loss
```

Required recovery:

```trace
back_translation_recovery :=
  two_toy_shock_profiles
  + positive_demand_shock_case
  + negative_supply_or_cost_push_shock_case
  + output_gap_up_for_demand_profile
  + output_gap_down_for_supply_profile
  + inflation_up_in_both_profiles
  + policy_rate_as_schematic_response_variable
  + no_forecast_boundary
  + no_policy_advice_boundary
  + toy_status_and_loss_register
```

Failure:

```trace
back_translation_fails_if:
  translation_returns_only:
    inflation_rises_and_policy_responds
  but_loses:
    shock_type_distinction
    + output_gap_direction_contrast
    + toy_status
    + no_forecast_boundary
```

## 9. Critical distinctions tested

### 9.1 Same inflation direction does not imply same macro profile

```trace
same_inflation_different_profile_test :=
  demand_profile.pi_path > reference
  + supply_profile.pi_path > reference
  but:
    demand_profile.y_path_above_reference
    + supply_profile.y_path_below_reference
```

Failure:

```trace
failure :=
  both_profiles_flattened_to_inflation_up
```

### 9.2 Shock type matters

```trace
shock_type_test :=
  demand_shock != supply_or_cost_push_shock
```

Failure:

```trace
failure :=
  shock_as_generic_event
```

### 9.3 Policy-rate path is not policy advice

```trace
policy_rate_test :=
  i_path := schematic_response_variable
  not:
    recommendation
    OR welfare_result
    OR central_bank_intention
```

Failure:

```trace
failure :=
  toy_policy_rate_path_read_as_recommended_response
```

### 9.4 Contrast profile is not real forecast

```trace
forecast_boundary_test :=
  demand_profile_and_supply_profile := toy_translation_profiles
  not:
    empirical_prediction
    OR policy_counterfactual
```

Failure:

```trace
failure :=
  toy_contrast_read_as_macro_prediction
```

## 10. Loss register

```trace
L_DSGE_contrast :=
  toy_schematic_values_only
  + no_model_equations
  + no_microfoundations
  + no_estimation
  + no_solution_method
  + no_expectations_specification
  + no_policy_rule_derivation
  + no_welfare_analysis
  + no_empirical_claim
  + no_policy_advice
```

Loss effects:

```trace
loss_effects :=
  no_equations -> no_solved_model_claim
  + no_estimation -> no_empirical_claim
  + no_solution_method -> no_solution_claim
  + no_expectations -> no_expectations_preserved_claim
  + no_welfare -> no_policy_advice
  + toy_values -> no_forecast_claim
```

## 11. What this earns

```trace
earned_claim :=
  TRACE_can_preserve_one_toy_DSGE_two_profile_contrast_internally
  + shock_type_distinction_is_translation_testable
  + same_inflation_direction_can_coexist_with_different_output_gap_profiles
  + macro_flattening_beyond_generic_causation_is_blocked
  + profile_morphism_template_can_host_contrast_profiles_under_loss
  - solved_DSGE_claim
  - forecast_claim
  - policy_advice
  - validation
```

## 12. What remains untested

```trace
not_tested :=
  actual_DSGE_equations
  + structural_shock_identification
  + expectations_solution
  + equilibrium_determinacy
  + calibration_or_estimation
  + empirical_IRFs
  + welfare_loss
  + optimal_policy
  + representative_agent_or_HANK_structure
  + source_review
```

## 13. Next step

```trace
recommended_next :=
  DSGE_two_profile_consolidation_or_hostile_audit
  because:
    branch_now_has_two_macro_profiles
    + contrast_matrix_can_be_defined
    + toy_status_must_remain_active
```

Alternative:

```trace
alternative_next :=
  move_to_syntax_input_packet
  only_after:
    DSGE_consolidation
```

## 14. Final compression

```trace
DSGE_Demand_vs_Supply_Shock_Profile_Contrast_v0_1 :=
  profiles := demand_shock_profile + supply_shock_profile
  distinction := same_inflation_direction_different_output_gap_direction
  success := recover_shock_type_and_response_path_contrast
  failure := generic_inflation_story_or_forecast_or_policy_advice
  status := INTERNAL_PROFILE_CANDIDATE + NATIVE_REVIEW_REQUIRED + TOY_STATUS_COOLED
  next := DSGE_two_profile_consolidation_or_hostile_audit
  - validation
  - solved_DSGE
  - forecast
  - policy_advice
```

End.
