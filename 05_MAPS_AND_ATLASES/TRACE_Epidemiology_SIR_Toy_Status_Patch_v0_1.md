# TRACE Epidemiology SIR Toy Status Patch v0.1

Date: 2026-06-18
Status: toy-status patch / epidemiology SIR worked example cooling / not validation / not forecasting / not real-world guidance / not empirical model / not operator promotion / not Kernel v0.3

## 0. Control header

This file patches the status of `TRACE_Epidemiology_SIR_Toy_Profile_Worked_Example_v0_1.md` before the second-battery work moves onward.

It does not add a new epidemiology example.

It does not model a real event.

It does not forecast.

It does not estimate parameters.

It does not give real-world guidance.

```trace
Epidemiology_SIR_Toy_Status_Patch_v0_1 :=
  R0_measure_not_case_count
  + toy_curve_not_forecast
  + beta_gamma_not_estimated
  + incidence_not_prevalence
  + no_real_world_guidance
  + loss_register_claim_effects
  -> first_epidemiology_probe_terms_cooled
  - validation
  - forecasting
  - empirical_model_claim
```

## 1. Patch target

```trace
patch_target :=
  TRACE_Epidemiology_SIR_Toy_Profile_Worked_Example_v0_1
```

This patch does not delete or replace the worked example. It controls how the worked example must now be read.

## 2. Toy model status

The SIR example is a toy profile for translation testing.

```trace
toy_model_status :=
  schematic_compartment_flow_profile
  not:
    real_world_model
    OR fitted_model
    OR calibrated_model
    OR forecast
    OR guidance
```

Allowed reading:

```trace
allowed_model_reading :=
  internal_test_of_compartment_flow_translation
```

Not allowed:

```trace
not_allowed_model_reading :=
  real_event_analysis
  OR public_health_interpretation
  OR empirical_prediction
  OR policy_or_behavioural_guidance
```

## 3. R0 status patch

The worked example uses `R0_measure := beta / gamma -> 3.0` only as toy structure.

```trace
R0_measure_status :=
  toy_reproduction_measure_placeholder
  not:
    observed_case_count
    OR empirical_estimate
    OR forecast
    OR danger_score
    OR guidance_metric
```

Claim effects:

```trace
R0_claim_effects :=
  no_empirical_estimation
  + no_real_world_transmission_claim
  + no_risk_score_claim
  + no_guidance_claim
```

## 4. Beta / gamma status patch

The beta and gamma values in the worked example are placeholders.

```trace
beta_gamma_status :=
  toy_placeholder_parameters
  not:
    estimated_parameters
    OR calibrated_parameters
    OR pathogen_specific_parameters
    OR behaviour_specific_parameters
```

Claim effects:

```trace
beta_gamma_claim_effects :=
  no_empirical_parameter_claim
  + no_model_fit_claim
  + no_mechanism_specific_claim
```

## 5. Model curve status patch

Any curve or profile implied by the toy SIR example is not a forecast.

```trace
model_curve_status :=
  schematic_profile_shape_for_translation_testing
  not:
    forecast
    OR projected_outbreak_curve
    OR empirical_time_series
    OR decision_support_output
```

Claim effects:

```trace
model_curve_claim_effects :=
  no_forecast_claim
  + no_real_time_prediction_claim
  + no_decision_support_claim
```

## 6. Incidence / prevalence status patch

The incidence/prevalence distinction remains active and must not be collapsed.

```trace
readout_status :=
  incidence_like_flow_vs_prevalence_like_level
```

Claim effects:

```trace
readout_claim_effects :=
  incidence_like_flow := new_transition_over_interval
  + prevalence_like_level := current_compartment_level_at_time
  + these_are_not_interchangeable
```

Failure:

```trace
readout_failure :=
  current_level_and_new_transition_collapsed
```

## 7. Deterministic flow / stochastic event status patch

The worked example uses a deterministic toy compartment-flow sketch.

```trace
process_status :=
  deterministic_compartment_flow_placeholder
  not:
    stochastic_contact_model
    OR individual_event_simulation
    OR contact_network_model
```

Claim effects:

```trace
process_claim_effects :=
  no_individual_transmission_event_claim
  + no_network_topology_claim
  + no_stochastic_dynamics_claim
```

## 8. Boundary status patch

The boundary of the toy profile must remain visible.

```trace
boundary_status :=
  closed_population_toy_boundary
  + schematic_short_horizon
  + no_forecast_boundary
  + no_real_world_guidance_boundary
```

Failure:

```trace
boundary_failure :=
  toy_profile_read_as_open_real_world_process
```

## 9. Loss register claim effects

```trace
loss_register_claim_effects :=
  toy_profile_only -> no_real_world_model_claim
  + no_real_data -> no_empirical_claim
  + no_parameter_estimation -> no_beta_gamma_or_Rt_estimate_claim
  + no_stochastic_model -> no_individual_event_claim
  + no_contact_network -> no_network_claim
  + no_intervention_analysis -> no_guidance_claim
  + no_model_fit -> no_forecast_claim
```

No consequence means audit theatre.

```trace
no_consequence_loss :=
  invalid_loss_register_entry
```

## 10. Updated back-translation requirement

```trace
BT_Epi_required_recovery_after_patch :=
  toy_SIR_model_family
  + closed_population_N1000
  + compartments_S_I_R
  + initial_state_990_10_0
  + beta_gamma_as_toy_parameters
  + S_to_I_flow
  + I_to_R_flow
  + R0_measure_as_toy_placeholder_not_case_count
  + incidence_like_flow_not_prevalence_like_level
  + deterministic_flow_not_stochastic_contact_event
  + no_forecast_no_guidance_boundary
  + loss_register_claim_effects
```

Failure:

```trace
BT_Epi_fails_if:
  returns:
    generic_population_spread
    OR real_world_prediction
    OR risk_score
    OR guidance
  OR loses:
    compartments
    + transition_parameters
    + readout_distinction
    + toy_boundary
```

## 11. Status after patch

```trace
Epidemiology_first_example_status_after_patch :=
  INTERNAL_PROFILE_CANDIDATE
  + NATIVE_REVIEW_REQUIRED
  + TOY_STATUS_COOLED
  for:
    toy_SIR_compartment_flow_profile_only
```

Meaning:

```trace
status_means :=
  useful_internal_translation_probe
  + SIR_compartment_flow_test
  + R0_not_case_count_test
  + incidence_not_prevalence_test
  + toy_not_forecast_boundary
  + not_real_model
  + not_guidance
```

## 12. Gate before moving to organic synthesis

Organic synthesis may proceed if this patch remains active.

```trace
organic_synthesis_entry_gate :=
  epidemiology_input_packet_complete
  + SIR_toy_example_complete
  + SIR_toy_status_patch_complete
  + no_forecast_boundary_active
  + no_guidance_boundary_active
  + loss_register_claim_effects_active
  + second_battery_entry_rule_active
```

## 13. Updated must-not-claim

```trace
must_not_claim_after_patch :=
  real_world_model
  OR forecast
  OR empirical_R0_or_Rt_estimate
  OR fitted_beta_gamma_parameters
  OR public_health_guidance
  OR stochastic_contact_model
  OR contact_network_model
  OR intervention_effect_claim
```

## 14. Updated allowed claim

```trace
allowed_claim_after_patch :=
  TRACE_has_internal_toy_SIR_compartment_flow_translation_probe
  + R0_language_has_been_cooled
  + toy_curve_forecast_leak_is_blocked
  + incidence_prevalence_distinction_is_active
  + loss_register_claim_effects_are_active
  + organic_synthesis_input_packet_may_proceed_under_gate
  - validation
  - forecasting
  - real_world_guidance
```

## 15. Final compression

```trace
Epidemiology_SIR_Toy_Status_Patch_v0_1 :=
  model := toy_not_real
  R0 := reproduction_measure_placeholder_not_case_count
  beta_gamma := toy_parameters_not_estimates
  curve := schematic_profile_not_forecast
  readout := incidence_not_prevalence
  boundary := no_forecast_no_guidance
  loss := allowed_claim_affecting
  status := INTERNAL_PROFILE_CANDIDATE + NATIVE_REVIEW_REQUIRED + TOY_STATUS_COOLED
  next := Organic_Synthesis_input_packet
  - validation
  - forecasting
  - guidance
```

End.
