# TRACE Epidemiology SIR Toy Profile Worked Example v0.1

Date: 2026-06-18
Status: toy SIR worked example / compartment-flow profile / no real-world model / not validation / not forecasting / not guidance / not parameter estimation / not operator promotion / not Kernel v0.3

## 0. Control header

This file follows:

- `TRACE_Epidemiology_Translation_Input_Packet_v0_1.md`
- `TRACE_Second_Four_Domain_Stress_Map_v0_1.md`
- `TRACE_Profile_Morphism_Formal_Status_Patch_v0_1.md`

It creates a toy SIR profile only.

It does not model a real event.

It does not forecast.

It does not estimate parameters.

It does not give real-world guidance.

```trace
Epidemiology_SIR_Toy_Profile_Worked_Example_v0_1 :=
  toy_population_compartments
  + S_I_R_initial_state
  + beta_gamma_transition_context
  + R0_status
  + compartment_flow_profile
  + back_translation_test
  + loss_register
  - validation
  - forecasting
  - real_world_guidance
```

## 1. Toy native case

The toy case uses a closed population of size 1000.

```trace
toy_native_case :=
  model_family := toy_SIR
  + population_size_N := 1000
  + initial_state:
      S0 := 990
      I0 := 10
      R0_compartment := 0
  + beta_parameter := 0.30
  + gamma_parameter := 0.10
  + time_horizon := schematic_short_horizon
```

Important notation warning:

```trace
notation_warning :=
  R0_compartment != R0_reproduction_measure
```

This file uses `R0_compartment` for the initial recovered/removed compartment and `R0_measure` for the reproduction measure.

## 2. Toy flow rules

The toy SIR flow rules are represented schematically:

```trace
flow_rules :=
  S_to_I_flow := beta_parameter * S * I / N
  I_to_R_flow := gamma_parameter * I
```

Equivalent compartment-change sketch:

```trace
compartment_change_sketch :=
  dS_dt := - beta_parameter * S * I / N
  dI_dt := beta_parameter * S * I / N - gamma_parameter * I
  dR_dt := gamma_parameter * I
```

Boundary:

These equations are included only as toy structural notation. They are not fitted to data and are not a forecast.

## 3. Reproduction-measure status

For this toy case:

```trace
R0_measure_status :=
  R0_measure := beta_parameter / gamma_parameter
  -> 3.0
```

Under simple SIR assumptions, this value is a reproduction-measure placeholder for the toy model.

It is not an observed case count.

It is not a real-world claim.

It is not a danger score.

```trace
R0_measure_not :=
  observed_case_count
  OR empirical_estimate
  OR forecast
  OR guidance_metric
```

## 4. Incidence / prevalence distinction

The toy example keeps incidence and prevalence distinct.

```trace
prevalence_like_readout_at_t :=
  I_t
```

```trace
incidence_like_readout_over_interval :=
  new_S_to_I_flow_over_interval
```

Plain version:

`I_t` is a current compartment level. New transitions from S to I over a time interval are a flow/readout over time. These are not the same object.

## 5. Toy profile object

```trace
SIR_toy_profile :=
  model_family_status := toy_SIR
  + compartments := [S, I, R]
  + initial_state := [990, 10, 0]
  + transition_parameters := [beta_parameter := 0.30, gamma_parameter := 0.10]
  + transition_rules := [S_to_I_flow, I_to_R_flow]
  + reproduction_measure_status := R0_measure_placeholder_3_0
  + readout_distinctions := [incidence_like_flow, prevalence_like_level]
  + time_horizon := schematic_short_horizon
  + boundary := no_forecast_no_real_world_claim
```

This is a profile object for translation testing, not an applied model.

## 6. TRACE-form mapping

```trace
TRACE_form(Epidemiology) :=
  {S_Epi, T_Epi, C_Epi, O_Epi, K_Epi, B_Epi, I_Epi}
```

Mapping:

```trace
S_Epi := SIR_compartment_state_vector
T_Epi := S_to_I_and_I_to_R_transition_dynamics
C_Epi := coupled_population_flow_between_compartments
O_Epi := incidence_like_and_prevalence_like_readout
K_Epi := closed_population_toy_rates_and_no_estimation_constraints
B_Epi := time_horizon_population_boundary_and_no_forecast_scope
I_Epi := compartment_flow_curve_profile_and_R0_measure_status
```

## 7. Candidate translation-map instance

Using cooled morphism language:

```trace
m_Epi_SIR:
  structured_native_SIR_profile_record
  -> structured_TRACE_epidemiology_profile_record
```

Read as candidate translation-map shape only.

Preservation target:

```trace
m_Epi_SIR_preserves :=
  compartment_names
  + initial_compartment_state
  + transition_parameters
  + transition_flow_direction
  + reproduction_measure_status
  + incidence_prevalence_distinction
  + toy_boundary
  + loss_register
```

## 8. Back-translation test

```trace
BT_Epi(m_Epi_SIR(SIR_toy_profile))
  ~=
  toy_SIR_case_under_declared_loss
```

Required recovery:

```trace
back_translation_recovery :=
  toy_SIR_model_family
  + population_size_1000
  + compartments_S_I_R
  + initial_state_990_10_0
  + beta_parameter_0_30
  + gamma_parameter_0_10
  + S_to_I_flow
  + I_to_R_flow
  + R0_measure_status_3_0_as_toy_placeholder
  + incidence_like_flow_vs_prevalence_like_level
  + no_forecast_no_real_world_claim_boundary
  + loss_register
```

Failure:

```trace
back_translation_fails_if:
  translation_returns_only:
    generic_population_spread
  but_loses:
    S_I_R_compartments
    + beta_gamma_transition_context
    + flow_direction
    + R0_measure_not_case_count
    + incidence_prevalence_distinction
    + no_forecast_boundary
```

## 9. Critical distinctions tested

### 9.1 Compartments are not generic labels

```trace
compartment_test :=
  S_state + I_state + R_state
  not:
    arbitrary_labels
    OR vague_phases
```

Failure:

```trace
failure := compartments_flattened_to_generic_states
```

### 9.2 Flow is not generic spread

```trace
flow_test :=
  S_to_I_flow
  + I_to_R_flow
  not:
    generic_spread_story
```

Failure:

```trace
failure := transition_dynamics_lost
```

### 9.3 R0 measure is not observed case count

```trace
R0_test :=
  R0_measure := beta_parameter / gamma_parameter
  not:
    observed_case_count
    OR empirical_estimate
    OR danger_score
```

Failure:

```trace
failure := R0_reduced_to_case_count_or_vague_risk
```

### 9.4 Incidence is not prevalence

```trace
readout_test :=
  incidence_like_flow != prevalence_like_level
```

Failure:

```trace
failure := new_transitions_and_current_level_collapsed
```

### 9.5 Toy model is not forecast

```trace
forecast_boundary_test :=
  toy_profile != forecast
```

Failure:

```trace
failure := toy_curve_read_as_real_world_prediction
```

## 10. Loss register

```trace
L_Epi_SIR :=
  toy_compartment_model_only
  + no_real_data
  + no_case_definition
  + no_parameter_estimation
  + no_stochastic_contact_events
  + no_network_topology
  + no_intervention_effects
  + no_mechanism_specific_biology
  + no_real_world_guidance
```

Loss effects:

```trace
loss_effects :=
  no_real_data -> no_real_world_claim
  + no_parameter_estimation -> no_empirical_parameter_claim
  + no_network_topology -> no_contact_network_claim
  + no_stochastic_model -> no_individual_event_claim
  + no_intervention_effects -> no_guidance_claim
  + toy_profile_only -> no_forecast_claim
```

## 11. What this earns

```trace
earned_claim :=
  TRACE_can_preserve_one_toy_SIR_compartment_flow_profile_internally
  + compartments_vs_generic_states_is_testable
  + transition_flow_vs_generic_spread_is_testable
  + R0_not_case_count_is_testable
  + incidence_prevalence_distinction_is_testable
  + toy_model_not_forecast_boundary_is_testable
  - validation
  - forecast
  - real_world_guidance
```

## 12. What remains untested

```trace
not_tested :=
  real_data
  + parameter_estimation
  + stochastic_transmission
  + contact_network_structure
  + intervention_effects
  + reporting_bias
  + model_fit
  + uncertainty_quantification
  + mechanism_specific_biology
  + specialist_review
```

## 13. Next step

```trace
recommended_next :=
  Epidemiology_first_example_toy_status_patch_or_consolidation
  because:
    R0_language_can_overclaim
    + toy_curve_can_be_misread_as_forecast
    + incidence_prevalence_distinction_must_remain_active
```

Alternative:

```trace
alternative_next :=
  Organic_Synthesis_input_packet
  if:
    second_battery_sequence_prioritises_domain_breadth_over_epidemiology_cooling
```

## 14. Final compression

```trace
Epidemiology_SIR_Toy_Profile_Worked_Example_v0_1 :=
  case := toy_SIR_N1000_initial_990_10_0
  parameters := beta_0_30_gamma_0_10
  profile := compartments + transition_flows + R0_measure_status + incidence_prevalence_distinction
  success := recover_compartments_flow_readout_boundary_loss
  failure := generic_spread_or_forecast_story
  status := INTERNAL_PROFILE_CANDIDATE + TOY_STATUS_REQUIRED + NATIVE_REVIEW_REQUIRED
  next := cooling_or_consolidation
  - validation
  - forecast
  - guidance
```

End.
