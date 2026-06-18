# TRACE Epidemiology Translation Input Packet v0.1

Date: 2026-06-18
Status: second-battery domain input packet / epidemiology and compartmental modelling / toy model-structure only / not validation / not forecasting / not real-world guidance / not native-domain unification / not operator promotion / not Kernel v0.3

## 0. Control header

This file opens the first domain input packet in the second four-domain stress battery.

It follows:

- `TRACE_Second_Four_Domain_Stress_Map_v0_1.md`
- `TRACE_Four_Domain_Success_Failure_Matrix_v0_1.md`
- `TRACE_Translation_Success_Protocol_v0_1.md`
- `TRACE_Profile_Morphism_Formal_Status_Patch_v0_1.md`

It begins with native epidemiological model structure.

It does not model a real event.

It does not forecast.

It does not give real-world guidance.

It does not replace domain expertise.

```trace
Epidemiology_Translation_Input_Packet_v0_1 :=
  native_epidemiology_entry
  + compartment_state_space
  + transition_dynamics
  + reproduction_measure_status
  + incidence_prevalence_distinction
  + loss_register_required
  + back_translation_target
  - validation
  - forecasting
  - real_world_guidance
```

## 1. Domain name

```trace
domain_name := Epidemiology_Compartmental_Modelling
```

Plain version:

This domain studies population-state change over time by tracking how members of a population move between defined model states.

## 2. Native object space

The native object space is a population-state structure.

```trace
native_epidemiology_object_space :=
  compartments
  + population_counts_or_proportions
  + transition_rates
  + contact_or_mixing_assumption
  + time_index_or_continuous_time
  + observation_readout_surface
  + model_boundary
```

Candidate native object for first probe:

```trace
native_object_or_case :=
  toy_SIR_compartment_profile
  under:
    simplified_internal_translation_probe
```

Boundary:

This is not a real-world model. It is an input packet for testing whether TRACE can preserve compartment-flow structure without turning it into generic spread language.

## 3. Native mathematical substrate

```trace
native_math_substrate :=
  ordinary_differential_equations
  + stochastic_processes_when_individual_events_are_modelled
  + network_theory_when_contacts_are_explicit
  + time_series_when_observation_readout_is_used
```

The first probe will use a toy compartmental framing only.

## 4. Native terms

```trace
native_terms :=
  susceptible_state
  + infected_state
  + recovered_or_removed_state
  + SIR_model
  + transition_rate
  + beta_parameter
  + gamma_parameter
  + R0
  + Rt
  + incidence
  + prevalence
  + attack_rate
  + model_curve
  + equilibrium_state
  + contact_network
```

Working definitions for this packet only:

```trace
working_definitions :=
  susceptible_state := population_state_available_for_transition_into_infected_state
  infected_state := population_state_currently_in_infected_model_compartment
  recovered_or_removed_state := population_state_no_longer_in_susceptible_or_infected_compartment_under_model_scope
  beta_parameter := transition_parameter_for_susceptible_to_infected_flow_in_simple_SIR_context
  gamma_parameter := transition_parameter_for_infected_to_recovered_or_removed_flow_in_simple_SIR_context
  R0 := reproduction_measure_under_fully_susceptible_model_assumptions
  Rt := reproduction_measure_under_current_model_conditions
  incidence := new_transitions_or_new_cases_over_time_interval
  prevalence := current_level_in_infected_or_case_state_at_time
```

These definitions are schematic and model-context dependent.

## 5. Native structures to preserve

```trace
native_structure :=
  compartment_state_vector
  + transition_dynamics_between_compartments
  + beta_gamma_parameter_context
  + population_boundary
  + observation_readout_context
  + time_horizon
```

Plain version:

The core structure is not simply that something spreads. The core structure is that a population is partitioned into states and transitions between them under explicit model assumptions.

## 6. Candidate native profile family

```trace
native_profile_family :=
  compartment_flow_curve_profile
```

Candidate profile object:

```trace
Epidemiology_profile_object :=
  model_family_status
  + compartment_names
  + initial_compartment_values
  + transition_parameters
  + transition_equations_or_flow_rules
  + time_horizon
  + modelled_readout
  + reproduction_measure_status
  + loss_register
```

Profile assignment:

```trace
Phi_Epi:
  SIR_case
  -> compartment_flow_curve_profile
```

Profile value:

```trace
P_Epi(SIR_case) :=
  structured_profile_of_compartment_states_transitions_and_readout
```

## 7. Intended TRACE form

```trace
TRACE_form(Epidemiology) :=
  {S_Epi, T_Epi, C_Epi, O_Epi, K_Epi, B_Epi, I_Epi}
```

Candidate mapping:

```trace
S_Epi := compartment_state_or_contact_network_state
T_Epi := transmission_recovery_or_removal_transition_dynamics
C_Epi := population_flow_or_contact_network_coupling
O_Epi := incidence_prevalence_Rt_or_curve_readout
K_Epi := population_conservation_rate_mixing_reporting_and_scope_constraints
B_Epi := population_boundary_time_horizon_and_model_scope
I_Epi := R0_Rt_attack_rate_peak_equilibrium_or_curve_profile
```

## 8. Critical distinctions

```trace
critical_distinctions :=
  SIR_compartments_not_generic_states
  + R0_not_observed_case_count
  + Rt_not_fixed_R0
  + incidence_not_prevalence
  + deterministic_flow_not_individual_contact_event
  + model_curve_not_real_world_forecast_without_conditions
  + equilibrium_state_not_process_absence
```

A TRACE translation fails if it turns SIR into a generic spread story without preserving compartments, transition rates, readout type, and model boundary.

## 9. Known flattening risks

```trace
flattening_risks :=
  process_as_generic_spread
  + R0_as_simple_danger_score
  + compartments_as_labels_only
  + incidence_prevalence_confusion
  + model_curve_as_forecast
  + deterministic_flow_same_as_contact_event
  + model_boundary_hidden
```

Hard guard:

```trace
hard_guard :=
  no_epidemiology_translation_claim
  unless:
    compartment_structure_preserved
    + transition_dynamics_preserved
    + readout_type_preserved
    + model_boundary_preserved
    + loss_register_written
    + back_translation_possible
```

## 10. Initial loss register

### 10.1 Toy model only

```trace
loss_entry_1 :=
  source_feature := real_world_epidemiological_model_or_event_analysis
  -> TRACE_translation := toy_SIR_input_packet
  -> loss_or_distortion := no_real_data_no_case_definition_no_calibration
  -> consequence_for_back_translation := no_real_world_claim
```

### 10.2 No parameter estimation

```trace
loss_entry_2 :=
  source_feature := estimated_beta_gamma_or_Rt_from_data
  -> TRACE_translation := not_tested
  -> loss_or_distortion := parameters_not_estimated
  -> consequence_for_back_translation := no_empirical_parameter_claim
```

### 10.3 No stochastic or network model yet

```trace
loss_entry_3 :=
  source_feature := stochastic_transmission_or_contact_network_structure
  -> TRACE_translation := named_gap_only
  -> loss_or_distortion := individual_contact_events_not_modelled
  -> consequence_for_back_translation := no_network_or_stochastic_claim
```

### 10.4 No intervention analysis

```trace
loss_entry_4 :=
  source_feature := intervention_effect_analysis
  -> TRACE_translation := boundary_context_only
  -> loss_or_distortion := no_effect_modelled
  -> consequence_for_back_translation := no_real_world_guidance
```

### 10.5 No mechanism-specific biology

```trace
loss_entry_5 :=
  source_feature := mechanism_specific_biology_or_transmission_mode
  -> TRACE_translation := abstract_transition_context
  -> loss_or_distortion := mechanism_not_modelled
  -> consequence_for_back_translation := no_mechanism_specific_claim
```

## 11. Back-translation target

A successful first epidemiology translation should recover:

```trace
back_translation_target :=
  toy_SIR_case
  + S_I_R_compartment_names
  + initial_compartment_values_if_supplied
  + beta_gamma_transition_context
  + compartment_flow_direction
  + R0_or_Rt_status_if_supplied
  + incidence_prevalence_readout_distinction
  + model_time_horizon
  + no_forecast_boundary
  + loss_register
```

Failure:

```trace
translation_fails_if:
  TRACE_form_returns_only:
    generic_population_spread
  but:
    cannot_recover_SIR_compartments
    + cannot_recover_transition_rates
    + cannot_recover_flow_direction
    + cannot_recover_readout_type
    + cannot_recover_no_forecast_boundary
```

## 12. Candidate first worked example

Recommended next file:

```trace
next_worked_example :=
  TRACE_Epidemiology_SIR_Toy_Profile_Worked_Example_v0_1
  with:
    toy_population_size
    + S_I_R_initial_state
    + beta_gamma_placeholder_values
    + R0_status
    + compartment_flow_profile
    + no_forecast_boundary
```

Boundary:

The worked example must stay toy/schematic unless source-backed data, parameter estimation, and model assumptions are added.

## 13. Status after input packet

```trace
Epidemiology_status :=
  NOT_STARTED_TRANSLATION
  + input_packet_exists
  + native_object_space_named
  + native_transition_family_named
  + native_profile_family_named
  + source_gap_named
  + loss_register_started
  - worked_example_complete
  - validation
  - real_world_claim
  - real_world_guidance
```

## 14. Final compression

```trace
Epidemiology_Translation_Input_Packet_v0_1 :=
  domain := Epidemiology_Compartmental_Modelling
  native_object_space := compartments + population_values + transition_rates + time + reporting_boundary
  first_profile_family := compartment_flow_curve_profile
  critical_distinction := SIR_not_generic_spread + R0_not_case_count + incidence_not_prevalence
  TRACE_form := {S_Epi,T_Epi,C_Epi,O_Epi,K_Epi,B_Epi,I_Epi}
  success := recover_compartments_transition_dynamics_readout_boundary_loss
  failure := generic_spread_story_only
  next := SIR_toy_profile_worked_example
  - validation
  - forecasting
  - real_world_guidance
```

End.
