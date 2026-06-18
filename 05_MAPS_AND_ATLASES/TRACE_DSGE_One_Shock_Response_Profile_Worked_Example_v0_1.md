# TRACE DSGE One-Shock Response Profile Worked Example v0.1

Date: 2026-06-18
Status: first DSGE worked example / toy schematic internal translation probe / not validation / not proof / not macroeconomic theory / not forecast / not policy advice / not operator promotion / not Kernel v0.3

## 0. Control header

This file follows:

- `TRACE_DSGE_Translation_Input_Packet_v0_1.md`
- `TRACE_Generic_Invariant_Profile_Translation_Template_v0_1.md`
- `TRACE_Profile_Morphism_Formal_Status_Patch_v0_1.md`

This is a toy/schematic worked example. It is not a solved DSGE model.

It does not use real data.

It does not estimate parameters.

It does not make a forecast.

It does not give policy advice.

```trace
DSGE_One_Shock_Response_Profile_Worked_Example_v0_1 :=
  toy_model_case
  + one_named_shock
  + selected_variables
  + response_path_profile
  + endogenous_exogenous_distinction
  + back_translation_test
  + loss_register
  - validation
  - solved_DSGE
  - forecast
  - policy_advice
```

## 1. Native case

The worked case is schematic:

```trace
native_case :=
  toy_DSGE_style_model
  + one_exogenous_demand_shock
  + three_tracked_variables
  + four_period_response_profile
```

Tracked variables:

```trace
tracked_variables :=
  output_gap_y
  + inflation_pi
  + policy_rate_i
```

Shock:

```trace
shock :=
  positive_demand_shock
  + period_0_arrival
  + normalised_size_1
  + exogenous_for_this_toy_case
```

Boundary:

The values below are schematic profile values, not empirical estimates and not a solved model output.

## 2. Native roles

```trace
native_roles :=
  state_or_dynamic_condition:
    output_gap_y
    + inflation_pi
  control_or_policy_response:
    policy_rate_i
  exogenous_disturbance:
    positive_demand_shock
  reference_path:
    steady_state_zero_gap_zero_inflation_deviation_baseline
```

Plain version:

The shock is not simply an event. It is an exogenous disturbance inside the model case. The variables are not generic outcomes. They have model roles.

## 3. Toy response path profile

The response profile is deliberately simple.

| Period | Shock | Output gap `y` | Inflation `pi` | Policy rate `i` | Native reading |
|---|---:|---:|---:|---:|---|
| `t=0` | `+1.0` | `+0.8` | `+0.3` | `+0.2` | shock arrives; output and inflation move above reference |
| `t=1` | `0.0` | `+0.5` | `+0.4` | `+0.4` | inflation persistence and policy response visible |
| `t=2` | `0.0` | `+0.2` | `+0.2` | `+0.3` | response begins decaying toward reference |
| `t=3` | `0.0` | `0.0` | `+0.1` | `+0.1` | near return toward reference path |

Profile object:

```trace
DSGE_response_profile_object :=
  model_id := toy_DSGE_style_case_v0_1
  shock_type := positive_demand_shock
  shock_size := normalised_1
  variables_tracked := {y, pi, i}
  response_path := table_t0_to_t3
  horizon := 4_periods
  reference_path := steady_state_deviation_baseline
  policy_rule_context := schematic_policy_response
  constraint_context := not_formally_modelled
```

## 4. Native profile assignment

```trace
Phi_DSGE:
  toy_model_and_positive_demand_shock
  -> impulse_response_profile
```

```trace
P_DSGE(toy_case) :=
  {
    y_path := [0.8, 0.5, 0.2, 0.0],
    pi_path := [0.3, 0.4, 0.2, 0.1],
    i_path := [0.2, 0.4, 0.3, 0.1]
  }
```

This is a profile object for translation testing. It is not a claim that these are real macro responses.

## 5. TRACE-form mapping

```trace
TRACE_form(Dynamic_Macroeconomics_DSGE) :=
  {S_Macro, T_Macro, C_Macro, O_Macro, K_Macro, B_Macro, I_Macro}
```

Mapping:

```trace
S_Macro := toy_model_state_and_variable_context
T_Macro := schematic_transition_response_over_t0_to_t3
C_Macro := not_primary_in_this_probe
O_Macro := impulse_response_readout_table
K_Macro := schematic_constraints_and_policy_response_context
B_Macro := toy_scope_horizon_reference_path_and_model_boundary
I_Macro := response_path_profile
```

## 6. Profile-preserving morphism instance

Using the cooled morphism language:

```trace
m_DSGE:
  structured_native_macro_profile_record
  -> structured_TRACE_macro_profile_record
```

Read as candidate translation-map shape only.

```trace
m_DSGE(toy_case)
  preserves:
    model_case_identity
    + shock_type_and_size
    + variable_roles
    + response_path_values
    + horizon
    + reference_path
    + toy_scope_and_loss_register
```

Loss register:

```trace
L_DSGE :=
  toy_schematic_values_only
  + no_model_equations
  + no_estimation
  + no_solution_method
  + no_expectations_specification
  + no_welfare_analysis
  + no_policy_advice
```

## 7. Back-translation test

A successful translation must reconstruct the native macro case.

```trace
BT_DSGE(m_DSGE(toy_case))
  ~=
  toy_case_under_declared_loss
```

Required recovery:

```trace
back_translation_recovery :=
  toy_DSGE_style_case
  + positive_demand_shock
  + shock_exogenous_in_this_case
  + variables_tracked_y_pi_i
  + response_path_t0_to_t3
  + policy_rate_as_response_variable_not_shock
  + model_solution_path_not_real_world_prediction
  + toy_scope_and_loss_register
```

Fail condition:

```trace
back_translation_fails_if:
  translation_returns_only:
    demand_shock_caused_output_and_inflation_to_rise
  but_loses:
    variable_roles
    + response_path_values
    + model_conditioning
    + toy_scope
    + no_forecast_boundary
```

## 8. Critical distinctions preserved or not

### 8.1 Exogenous shock vs endogenous response

```trace
exogenous_endogenous_test :=
  shock := exogenous_disturbance_for_toy_case
  y_pi_i := response_variables_in_profile
```

Failure:

```trace
failure :=
  policy_rate_i_treated_as_same_kind_as_shock
  OR output_path_treated_as_free_event_sequence
```

### 8.2 Impulse response vs prediction

```trace
IRF_prediction_test :=
  impulse_response_profile := model_conditioned_path_after_specified_shock
  not:
    real_world_forecast
```

Failure:

```trace
failure :=
  table_read_as_prediction_of_actual_economy
```

### 8.3 Policy rule vs intention

```trace
policy_rule_test :=
  policy_rate_i := schematic_policy_response_variable
  not:
    central_bank_intention_claim
```

Failure:

```trace
failure :=
  policy_response_interpreted_as_human_intent_or_normative_advice
```

### 8.4 Model output vs reality

```trace
model_reality_test :=
  response_path := toy_model_output_for_translation_probe
  not:
    empirical_reality
    OR policy_evidence
```

Failure:

```trace
failure :=
  toy_path_treated_as_real_macro_data
```

## 9. Flattening risks blocked

```trace
blocked_flattening :=
  shock_as_generic_event
  + impulse_response_as_prediction
  + expectations_as_feelings
  + policy_rule_as_intention
  + model_output_as_reality
  + calibration_as_truth
```

Still not solved:

```trace
not_solved :=
  formal_DSGE_equations
  + rational_expectations_solution
  + equilibrium_determinacy
  + empirical_estimation
  + welfare_analysis
  + policy_choice
```

## 10. What this earns

```trace
earned_claim :=
  TRACE_can_preserve_one_toy_DSGE_impulse_response_profile_internally
  + macro_flattening_errors_are_named
  + model_conditioned_path_not_generic_causation_story_is_testable
  + morphism_template_can_host_macro_profile_under_loss
  - solved_DSGE_claim
  - forecast_claim
  - policy_advice
  - validation
```

## 11. What remains untested

```trace
not_tested :=
  source_backed_model_equations
  + microfoundations
  + representative_agent_or_heterogeneous_agent_structure
  + rational_expectations_solution
  + stochastic_process_specification
  + calibration_or_estimation
  + likelihood_or_fit
  + equilibrium_existence
  + uniqueness_or_determinacy
  + welfare_loss
  + real_policy_counterfactual
```

## 12. Next step

```trace
recommended_next :=
  DSGE_first_example_cooling_or_hostile_audit
  because:
    macro_terms_can_overclaim
    + toy_values_can_be_misread_as_prediction
    + policy_interpretation_risk_is_high
```

Alternative:

```trace
alternative_next :=
  DSGE_two_profile_contrast_example
  only_after:
    cooling_or_audit
```

## 13. Final compression

```trace
DSGE_One_Shock_Response_Profile_Worked_Example_v0_1 :=
  case := toy_positive_demand_shock
  variables := y + pi + i
  profile := response_path_t0_to_t3
  success := recover_model_conditioned_shock_response_profile
  failure := generic_causation_story_or_forecast_or_policy_advice
  status := INTERNAL_PROFILE_CANDIDATE + NATIVE_REVIEW_REQUIRED
  next := cooling_or_hostile_audit
  - validation
  - solved_DSGE
  - forecast
  - policy_advice
```

End.
