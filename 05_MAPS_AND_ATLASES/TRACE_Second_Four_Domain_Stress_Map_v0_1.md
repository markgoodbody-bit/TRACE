# TRACE Second Four-Domain Stress Map v0.1

Date: 2026-06-18
Status: second four-domain stress map / new physical-process domain battery / not validation / not proof / not universal theory / not native-domain unification / not operator promotion / not Kernel v0.3

## 0. Control header

This file opens a second four-domain stress battery proposed by Qwen and supplied by Mark.

Domains:

1. Epidemiology and Compartmental Modeling
2. Plate Tectonics and Geodynamics
3. Organic Synthesis and Retrosynthetic Analysis
4. Neurophysiology and Computational Neuroscience

This file does not attempt direct native-theory unification.

It does not claim that the Arrhenius equation, Hodgkin-Huxley equations, Euler poles, and SIR dynamics are the same mathematics.

It tests whether the TRACE translation scaffold can preserve native process structure across four new physical-process domains.

```trace
Second_Four_Domain_Stress_Map_v0_1 :=
  Epidemiology
  + Geodynamics
  + Organic_Synthesis
  + Neurophysiology
  -> test:
      can_TRACE_preserve_native_process_structure?
      + can_TRACE_preserve_units_scale_constraints?
      + can_TRACE_make_loss_explicit?
      + can_TRACE_back_translate_without_flattening?
  - validation
  - proof
  - native_theory_unification
```

## 1. Why this second battery matters

The first four-domain stress path tested translation across abstract and formal domains:

```trace
first_battery :=
  QIT
  + Algebraic_Topology
  + DSGE
  + Generative_Syntax
```

The second battery shifts pressure toward physical-process domains:

```trace
second_battery :=
  Epidemiology:
    population_flow_and_contact_networks
  Geodynamics:
    planetary_material_motion_over_geologic_time
  Organic_Synthesis:
    molecular_graph_transformation_and_route_design
  Neurophysiology:
    excitable_membrane_and_signal_dynamics
```

This is a harder physical-substrate test because units, conservation, scale, geometry, material constraints, and intervention boundaries are harder to ignore.

```trace
new_pressure :=
  physical_units_matter
  + conservation_or_balance_conditions_matter
  + time_scales_diverge_massively
  + spatial_scales_diverge_massively
  + material_constraints_are_domain_specific
  + intervention_boundaries_are_not_interchangeable
```

## 2. Shared second-battery entry discipline

Every new domain must enter through the same discipline:

```trace
second_battery_entry_rule :=
  name_native_object_space
  + name_native_transformations_or_flows
  + name_native_composition_or_coupling
  + name_native_observation_or_readout
  + name_native_constraints
  + name_boundary_scope
  + name_profile_or_invariant
  + write_loss_register
  + write_back_translation_target
```

Failure:

```trace
second_battery_failure_if:
  TRACE_returns_generic_process_language
  OR erases_units
  OR erases_scale
  OR erases_native_constraints
  OR hides_loss
  OR cannot_back_translate_to_native_domain
```

## 3. Domain 1: Epidemiology and Compartmental Modeling

### 3.1 Native focus

Epidemiology models disease, behaviour, or information spread through populations over time by tracking flows between states or contacts between individuals.

```trace
Epidemiology_focus :=
  population_state_flow
  + transmission_process
  + intervention_and_boundary_context
```

### 3.2 Native mathematical substrate

```trace
Epidemiology_math_substrate :=
  ordinary_differential_equations
  + stochastic_processes
  + contact_networks
  + incidence_prevalence_time_series
```

### 3.3 TRACE-form sketch

```trace
TRACE_form(Epidemiology) :=
  {S_Epi, T_Epi, C_Epi, O_Epi, K_Epi, B_Epi, I_Epi}
```

```trace
S_Epi := compartment_state_or_network_state
T_Epi := transmission_recovery_transition_dynamics
C_Epi := population_flow_or_contact_network_coupling
O_Epi := incidence_prevalence_Rt_or_epidemic_curve_readout
K_Epi := population_conservation_rate_contact_reporting_and_intervention_constraints
B_Epi := population_boundary_time_horizon_spillover_and_intervention_scope
I_Epi := R0_Rt_attack_rate_peak_endemic_equilibrium_or_epidemic_curve_profile
```

### 3.4 Native distinctions to preserve

```trace
Epidemiology_critical_distinctions :=
  susceptible_infected_recovered_compartments_not_generic_states
  + R0_not_observed_case_count
  + incidence_not_prevalence
  + deterministic_flow_not_individual_contact_event
  + endemic_equilibrium_not_disease_gone
  + zoonotic_spillover_not_same_as_within_population_transmission
  + fomite_pathway_not_generic_environment
```

### 3.5 Flattening risks

```trace
Epidemiology_flattening_risks :=
  epidemic_as_generic_spread
  + R0_as_danger_score
  + compartments_as_labels_only
  + model_curve_as_forecast_without_conditions
  + intervention_as_moral_choice_not_parameter_or_boundary_shift
```

### 3.6 First candidate worked example

```trace
Epidemiology_first_probe :=
  toy_SIR_compartment_profile
  with:
    S_I_R_compartments
    + transition_rates_beta_gamma
    + R0_status
    + epidemic_curve_profile
    + no_real_forecast_boundary
```

## 4. Domain 2: Plate Tectonics and Geodynamics

### 4.1 Native focus

Geodynamics models the mechanical, thermal, and chemical processes that drive lithosphere and mantle behaviour over geological time.

```trace
Geodynamics_focus :=
  plate_motion
  + mantle_deformation
  + thermal_mechanical_coupling
  + spherical_reference_frame
```

### 4.2 Native mathematical substrate

```trace
Geodynamics_math_substrate :=
  continuum_mechanics
  + fluid_dynamics
  + spherical_kinematics
  + heat_transport
  + rheology
```

### 4.3 TRACE-form sketch

```trace
TRACE_form(Geodynamics) :=
  {S_Geo, T_Geo, C_Geo, O_Geo, K_Geo, B_Geo, I_Geo}
```

```trace
S_Geo := plate_mantle_thermal_mechanical_state
T_Geo := plate_motion_subduction_convection_rotation_or_deformation
C_Geo := plate_boundary_interaction_and_spherical_motion_composition
O_Geo := seismic_paleomagnetic_GPS_topographic_or_geological_readout
K_Geo := rheology_gravity_heat_mass_conservation_and_spherical_geometry_constraints
B_Geo := plate_boundary_depth_time_scale_reference_frame_and_model_domain
I_Geo := Euler_pole_velocity_field_subduction_geometry_isostatic_or_seismicity_profile
```

### 4.4 Native distinctions to preserve

```trace
Geodynamics_critical_distinctions :=
  lithosphere_not_asthenosphere
  + subduction_not_surface_sliding
  + mantle_flow_not_short_timescale_liquid_flow
  + Euler_pole_not_map_pin
  + paleomagnetism_not_ordinary_memory
  + isostasy_not_simple_floating_metaphor
  + Wadati_Benioff_zone_not_random_earthquake_line
```

### 4.5 Flattening risks

```trace
Geodynamics_flattening_risks :=
  plates_as_rigid_tiles_only
  + mantle_as_ocean_fluid
  + geological_time_erased
  + spherical_geometry_flattened_to_map
  + subduction_as_simple_downward_motion
```

### 4.6 First candidate worked example

```trace
Geodynamics_first_probe :=
  toy_plate_rotation_Euler_pole_profile
  with:
    plate_on_sphere
    + angular_velocity
    + surface_velocity_field
    + reference_frame_boundary
    + no_real_geophysical_model_claim
```

## 5. Domain 3: Organic Synthesis and Retrosynthetic Analysis

### 5.1 Native focus

Organic synthesis constructs complex carbon-based molecules through planned reaction sequences and retrosynthetic disconnections.

```trace
Organic_Synthesis_focus :=
  molecular_graph_transformation
  + stereochemical_control
  + route_planning
  + reaction_feasibility_constraints
```

### 5.2 Native mathematical substrate

```trace
Organic_Synthesis_math_substrate :=
  molecular_graph_theory
  + stereochemical_geometry
  + thermodynamics
  + kinetics
  + symmetry_and_chirality_analysis
```

### 5.3 TRACE-form sketch

```trace
TRACE_form(Organic_Synthesis) :=
  {S_Chem, T_Chem, C_Chem, O_Chem, K_Chem, B_Chem, I_Chem}
```

```trace
S_Chem := molecular_graph_stereochemical_and_functional_group_state
T_Chem := reaction_transformation_or_retrosynthetic_disconnection
C_Chem := reaction_sequence_or_route_composition
O_Chem := product_identity_yield_selectivity_spectral_or_structural_readout
K_Chem := valence_stereochemistry_thermodynamics_kinetics_reagent_and_solvent_constraints
B_Chem := functional_group_reactivity_scope_protecting_group_and_step_boundary
I_Chem := route_profile_atom_economy_yield_selectivity_chirality_or_disconnection_profile
```

### 5.4 Native distinctions to preserve

```trace
Organic_Synthesis_critical_distinctions :=
  molecular_graph_not_recipe_item
  + retrosynthesis_not_forward_reaction_sequence
  + enantiomer_not_same_molecule_with_label
  + nucleophile_electrophile_not_good_bad_reactive_pair
  + protecting_group_not_arbitrary_blocker
  + atom_economy_not_yield
  + thermodynamic_feasibility_not_kinetic_rate
```

### 5.5 Flattening risks

```trace
Organic_Synthesis_flattening_risks :=
  synthesis_as_recipe_steps
  + molecule_as_name_only
  + stereochemistry_erased
  + reaction_feasibility_as_common_sense_possibility
  + protecting_group_as_generic_delay
```

### 5.6 First candidate worked example

```trace
Organic_Synthesis_first_probe :=
  toy_retrosynthetic_disconnection_profile
  with:
    target_molecular_graph
    + bond_disconnection
    + precursor_graphs
    + functional_group_reactivity_boundary
    + no_real_lab_protocol_claim
```

## 6. Domain 4: Neurophysiology and Computational Neuroscience

### 6.1 Native focus

Neurophysiology models how neurons generate, propagate, and transmit electrical and chemical signals.

```trace
Neurophysiology_focus :=
  excitable_cell_state
  + membrane_voltage_dynamics
  + ion_channel_conductance
  + synaptic_transmission_and_plasticity
```

### 6.2 Native mathematical substrate

```trace
Neurophysiology_math_substrate :=
  cable_theory
  + nonlinear_dynamical_systems
  + equivalent_circuit_models
  + conductance_based_ODEs
  + synaptic_plasticity_models
```

### 6.3 TRACE-form sketch

```trace
TRACE_form(Neurophysiology) :=
  {S_Neuro, T_Neuro, C_Neuro, O_Neuro, K_Neuro, B_Neuro, I_Neuro}
```

```trace
S_Neuro := membrane_voltage_ion_channel_synaptic_and_cell_compartment_state
T_Neuro := conductance_change_spike_generation_spike_propagation_or_synaptic_transmission
C_Neuro := circuit_cellular_or_synaptic_signal_pathway_composition
O_Neuro := voltage_trace_firing_rate_synaptic_response_or_plasticity_readout
K_Neuro := ion_gradients_membrane_capacitance_channel_kinetics_cable_and_synaptic_constraints
B_Neuro := membrane_compartment_synapse_cell_time_window_and_recording_boundary
I_Neuro := action_potential_profile_LTP_profile_signal_propagation_or_conductance_profile
```

### 6.4 Native distinctions to preserve

```trace
Neurophysiology_critical_distinctions :=
  action_potential_not_generic_signal
  + resting_membrane_potential_not_inactivity
  + synaptic_cleft_not_empty_gap
  + myelin_not_simple_insulation_metaphor
  + LTP_not_memory_itself
  + ion_channel_conductance_not_wire_current
  + Hodgkin_Huxley_profile_not_generic_circuit
```

### 6.5 Flattening risks

```trace
Neurophysiology_flattening_risks :=
  neuron_as_wire
  + spike_as_message
  + synapse_as_switch
  + LTP_as_memory_claim
  + membrane_voltage_as_simple_battery
```

### 6.6 First candidate worked example

```trace
Neurophysiology_first_probe :=
  toy_action_potential_voltage_trace_profile
  with:
    membrane_voltage_state
    + threshold_crossing
    + spike_profile
    + recovery_phase
    + no_Hodgkin_Huxley_solution_claim
```

## 7. Cross-domain second-battery comparison

| Domain | Native object space | Native transformation | Profile/invariant candidate | Main flattening risk |
|---|---|---|---|---|
| Epidemiology | compartments or contact network state | transmission/recovery transitions | epidemic curve, R0/Rt, attack rate, equilibrium profile | generic spread story |
| Geodynamics | plate/mantle thermal-mechanical state | rotation, subduction, convection, deformation | Euler pole, velocity field, seismicity/subduction profile | moving tiles on flat map |
| Organic Synthesis | molecular graph and stereochemical state | reaction or retrosynthetic disconnection | route, atom economy, selectivity, chirality profile | recipe steps |
| Neurophysiology | membrane voltage/channel/synaptic state | conductance/spike/synaptic transitions | voltage trace, action potential, LTP profile | neuron as wire |

## 8. Shared success condition for the second battery

```trace
second_battery_success_condition :=
  for_domain_D:
    native_object_space_recoverable
    + native_transformation_recoverable
    + native_constraints_recoverable
    + native_units_or_scale_not_erased
    + profile_or_invariant_recoverable
    + loss_register_recoverable
    + back_translation_possible
```

## 9. Shared failure condition for the second battery

```trace
second_battery_failure_condition :=
  for_domain_D:
    TRACE_translation_returns:
      generic_flow
      OR generic_motion
      OR generic_transformation
      OR generic_signal
  while:
    native_process_structure_lost
    OR units_lost
    OR constraints_lost
    OR boundary_lost
```

## 10. Expected fracture lines

```trace
expected_fracture_lines :=
  Epidemiology:
    model_curve_vs_real_outbreak_forecast
    + deterministic_flow_vs_stochastic_contact_event
  Geodynamics:
    timescale_reference_frame_and_spherical_geometry
    + solid_vs_viscous_fluid_language
  Organic_Synthesis:
    graph_connectivity_vs_3D_stereochemistry
    + thermodynamics_vs_kinetics
  Neurophysiology:
    circuit_metaphor_vs_biophysical_channel_dynamics
    + spike_profile_vs_information_or_memory_claim
```

These are likely places where TRACE will fail if it over-compresses.

## 11. Recommended build sequence

```trace
recommended_build_sequence :=
  1_Epidemiology_input_packet
  -> 2_Epidemiology_SIR_worked_example
  -> 3_Organic_Synthesis_input_packet
  -> 4_Organic_Synthesis_retrosynthesis_worked_example
  -> 5_Neurophysiology_input_packet
  -> 6_Neurophysiology_action_potential_worked_example
  -> 7_Geodynamics_input_packet
  -> 8_Geodynamics_Euler_pole_worked_example
  -> 9_second_battery_consolidation
```

Reason:

```trace
sequence_reason :=
  start_with_clean_compartment_flow
  + then_discrete_graph_transformation
  + then_excitable_dynamic_profile
  + then_hardest_scale_reference_frame_domain
```

## 12. Current status

```trace
Second_Four_Domain_Stress_Map_status :=
  STRESS_MAP_CREATED
  + four_native_domains_named
  + TRACE_form_sketches_written
  + flattening_risks_named
  + first_probe_candidates_written
  - input_packets_complete
  - worked_examples_complete
  - validation
  - proof
```

## 13. Final compression

```trace
Second_Four_Domain_Stress_Map_v0_1 :=
  domains := Epidemiology + Geodynamics + Organic_Synthesis + Neurophysiology
  shared_test := preserve_native_process_structure_under_loss
  pressure := units + scale + constraints + material_boundary + back_translation
  first_next := Epidemiology_input_packet
  sequence := Epidemiology -> Organic_Synthesis -> Neurophysiology -> Geodynamics
  - validation
  - proof
  - native_theory_unification
```

End.
