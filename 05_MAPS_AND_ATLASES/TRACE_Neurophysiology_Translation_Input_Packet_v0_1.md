# TRACE Neurophysiology Translation Input Packet v0.1

Date: 2026-06-18
Status: second-battery domain input packet / neurophysiology and computational neuroscience / biophysical signal-structure only / not validation / not medical advice / not treatment guidance / not clinical interpretation / not native-domain unification / not operator promotion / not Kernel v0.3

## 0. Control header

This file opens the third domain input packet in the second four-domain stress battery.

It follows:

- `TRACE_Second_Four_Domain_Stress_Map_v0_1.md`
- `TRACE_Organic_Synthesis_Toy_Status_Patch_v0_1.md`
- `TRACE_Translation_Success_Protocol_v0_1.md`
- `TRACE_Profile_Morphism_Formal_Status_Patch_v0_1.md`

It begins with native neurophysiology model structure.

It does not diagnose anything.

It does not give medical advice.

It does not specify treatment, stimulation, drug, device, or clinical guidance.

It does not replace neuroscience, physiology, or clinical expertise.

```trace
Neurophysiology_Translation_Input_Packet_v0_1 :=
  native_neurophysiology_entry
  + membrane_voltage_state
  + ion_channel_conductance_context
  + action_potential_profile
  + synaptic_boundary
  + LTP_status_boundary
  + loss_register_required
  + back_translation_target
  - validation
  - medical_advice
  - clinical_claim
```

## 1. Domain name

```trace
domain_name := Neurophysiology_Computational_Neuroscience
```

Plain version:

This domain studies how neurons and neural components generate, propagate, and transmit electrical and chemical signals under biophysical constraints.

## 2. Native object space

The native object space is not a wire, a message string, or a generic information channel. It is a biophysical cell-state structure.

```trace
native_neurophysiology_object_space :=
  membrane_voltage_state
  + ion_channel_state
  + ionic_gradient_context
  + membrane_capacitance_context
  + axon_or_compartment_context
  + synaptic_state_if_present
  + time_dependent_voltage_or_conductance_readout
```

Candidate native object for first probe:

```trace
native_object_or_case :=
  toy_action_potential_voltage_trace_profile
  under:
    simplified_internal_translation_probe
```

Boundary:

This is not a real neuronal recording, not a full Hodgkin-Huxley solution, and not a clinical interpretation. It is an input packet for testing whether TRACE can preserve voltage-state and conductance-profile structure without turning neurons into wires or messages.

## 3. Native mathematical substrate

```trace
native_math_substrate :=
  nonlinear_ordinary_differential_equations
  + cable_theory_when_spatial_propagation_is_modelled
  + equivalent_circuit_models
  + conductance_based_membrane_models
  + time_series_voltage_trace_readouts
```

The first probe will use a toy voltage-profile framing only.

## 4. Native terms

```trace
native_terms :=
  membrane_potential
  + resting_membrane_potential
  + action_potential
  + threshold
  + depolarisation
  + repolarisation
  + hyperpolarisation
  + ion_channel
  + conductance
  + capacitance
  + ionic_gradient
  + axon
  + myelin_sheath
  + synaptic_cleft
  + neurotransmitter
  + long_term_potentiation
  + Hodgkin_Huxley_model
  + voltage_trace
```

Working definitions for this packet only:

```trace
working_definitions :=
  membrane_potential := voltage_difference_across_neuronal_membrane
  resting_membrane_potential := baseline_voltage_state_when_not_in_action_potential_phase
  action_potential := rapid_transient_voltage_profile_with_depolarisation_and_repolarisation_phases
  threshold := model_context_voltage_condition_for_spike_initiation
  ion_channel := membrane_protein_context_affecting_ion_conductance
  conductance := ease_of_ion_flow_through_channel_context
  capacitance := membrane_charge_storage_context_in_circuit_model
  synaptic_cleft := gap_between_cells_where_signal_transfer_mechanism_is_modelled
  LTP := persistent_synaptic_strengthening_profile_under_activity_history
```

These definitions are schematic and model-context dependent.

## 5. Native structures to preserve

```trace
native_structure :=
  membrane_state_variable
  + voltage_trace_profile
  + threshold_or_phase_context
  + conductance_or_channel_state_context
  + recovery_or_refractory_context
  + synaptic_boundary_if_present
  + recording_or_readout_context
  + time_horizon
```

Plain version:

The core structure is not simply that a signal is sent. The core structure is a time-dependent membrane-state profile governed by biophysical constraints and read through voltage, conductance, or synaptic response measures.

## 6. Candidate native profile family

```trace
native_profile_family :=
  action_potential_voltage_trace_profile
```

Candidate profile object:

```trace
Neurophysiology_profile_object :=
  model_family_status
  + membrane_voltage_state
  + threshold_status
  + phase_sequence
  + conductance_context
  + time_profile
  + readout_type
  + synaptic_or_compartment_boundary
  + loss_register
```

Profile assignment:

```trace
Phi_Neuro:
  action_potential_case
  -> action_potential_voltage_trace_profile
```

Profile value:

```trace
P_Neuro(action_potential_case) :=
  structured_profile_of_voltage_state_phases_conductance_context_and_readout
```

## 7. Intended TRACE form

```trace
TRACE_form(Neurophysiology) :=
  {S_Neuro, T_Neuro, C_Neuro, O_Neuro, K_Neuro, B_Neuro, I_Neuro}
```

Candidate mapping:

```trace
S_Neuro := membrane_voltage_ion_channel_synaptic_and_compartment_state
T_Neuro := conductance_change_spike_generation_spike_propagation_or_synaptic_transmission
C_Neuro := circuit_cellular_or_synaptic_signal_pathway_composition
O_Neuro := voltage_trace_firing_rate_synaptic_response_or_plasticity_readout
K_Neuro := ion_gradients_membrane_capacitance_channel_kinetics_cable_and_synaptic_constraints
B_Neuro := membrane_compartment_synapse_cell_time_window_and_recording_boundary
I_Neuro := action_potential_profile_LTP_profile_signal_propagation_or_conductance_profile
```

## 8. Critical distinctions

```trace
critical_distinctions :=
  action_potential_not_generic_signal
  + resting_membrane_potential_not_inactivity
  + threshold_not_decision_point_metaphor
  + ion_channel_conductance_not_wire_current
  + membrane_capacitance_not_simple_battery
  + synaptic_cleft_not_empty_gap
  + myelin_not_simple_insulation_metaphor
  + LTP_not_memory_itself
  + Hodgkin_Huxley_profile_not_generic_circuit_story
```

A TRACE translation fails if it turns neurophysiology into a generic signal/wire/message story without preserving membrane-state profile, channel/conductance context, time dynamics, and biological boundaries.

## 9. Known flattening risks

```trace
flattening_risks :=
  neuron_as_wire
  + spike_as_message
  + synapse_as_switch
  + threshold_as_choice_point
  + LTP_as_memory_claim
  + membrane_voltage_as_simple_battery
  + Hodgkin_Huxley_as_generic_circuit
  + medical_or_clinical_interpretation_leak
```

Hard guard:

```trace
hard_guard :=
  no_neurophysiology_translation_claim
  unless:
    membrane_voltage_state_preserved
    + phase_or_trace_profile_preserved
    + conductance_context_preserved_or_gap_declared
    + biological_boundary_preserved
    + medical_guidance_boundary_preserved
    + loss_register_written
    + back_translation_possible
```

## 10. Initial loss register

### 10.1 Toy profile only

```trace
loss_entry_1 :=
  source_feature := real_neuronal_recording_or_full_biophysical_model
  -> TRACE_translation := toy_voltage_trace_input_packet
  -> loss_or_distortion := no_recording_no_parameter_fit_no_full_channel_model
  -> consequence_for_back_translation := no_real_neuron_or_full_model_claim
```

### 10.2 No Hodgkin-Huxley solution

```trace
loss_entry_2 :=
  source_feature := Hodgkin_Huxley_equations_and_parameterised_solution
  -> TRACE_translation := named_context_only
  -> loss_or_distortion := no_channel_equation_solution
  -> consequence_for_back_translation := no_Hodgkin_Huxley_solution_claim
```

### 10.3 No spatial cable model yet

```trace
loss_entry_3 :=
  source_feature := spatial_propagation_along_dendrite_or_axon
  -> TRACE_translation := named_gap_only
  -> loss_or_distortion := cable_dynamics_not_modelled
  -> consequence_for_back_translation := no_spatial_propagation_claim
```

### 10.4 No synaptic plasticity model yet

```trace
loss_entry_4 :=
  source_feature := long_term_potentiation_mechanism_or_learning_model
  -> TRACE_translation := boundary_term_only
  -> loss_or_distortion := synaptic_plasticity_not_modelled
  -> consequence_for_back_translation := no_memory_or_LTP_mechanism_claim
```

### 10.5 No medical or clinical evaluation

```trace
loss_entry_5 :=
  source_feature := clinical_interpretation_or_treatment_context
  -> TRACE_translation := excluded_from_packet
  -> loss_or_distortion := no_medical_context_evaluated
  -> consequence_for_back_translation := no_medical_advice_or_clinical_claim
```

## 11. Back-translation target

A successful first neurophysiology translation should recover:

```trace
back_translation_target :=
  toy_action_potential_voltage_trace_case
  + membrane_voltage_state
  + resting_baseline_status_if_supplied
  + threshold_status_if_supplied
  + depolarisation_repolarisation_recovery_phase_profile
  + conductance_or_channel_context_as_named_or_gap
  + voltage_trace_readout
  + time_horizon
  + no_Hodgkin_Huxley_solution_boundary
  + no_medical_advice_boundary
  + loss_register
```

Failure:

```trace
translation_fails_if:
  TRACE_form_returns_only:
    neuron_sends_signal
  but:
    cannot_recover_membrane_voltage_state
    + cannot_recover_phase_profile
    + cannot_recover_conductance_context_or_gap
    + cannot_recover_voltage_trace_readout
    + cannot_recover_no_medical_boundary
```

## 12. Candidate first worked example

Recommended next file:

```trace
next_worked_example :=
  TRACE_Neurophysiology_Action_Potential_Toy_Profile_Worked_Example_v0_1
  with:
    toy_voltage_trace
    + resting_baseline_placeholder
    + threshold_crossing_placeholder
    + depolarisation_peak_repolarisation_recovery_phases
    + conductance_context_named_not_solved
    + no_Hodgkin_Huxley_solution
    + no_medical_guidance
```

Boundary:

The worked example must stay toy/schematic unless source-backed equations, parameters, recordings, and model assumptions are added.

## 13. Status after input packet

```trace
Neurophysiology_status :=
  NOT_STARTED_TRANSLATION
  + input_packet_exists
  + native_object_space_named
  + native_transition_family_named
  + native_profile_family_named
  + medical_guidance_boundary_named
  + loss_register_started
  - worked_example_complete
  - validation
  - full_model_claim
  - medical_advice
```

## 14. Final compression

```trace
Neurophysiology_Translation_Input_Packet_v0_1 :=
  domain := Neurophysiology_Computational_Neuroscience
  native_object_space := membrane_voltage + ion_channel_state + conductance + synaptic_boundary + time_readout
  first_profile_family := action_potential_voltage_trace_profile
  critical_distinction := action_potential_not_generic_signal + LTP_not_memory_itself + channel_not_wire
  TRACE_form := {S_Neuro,T_Neuro,C_Neuro,O_Neuro,K_Neuro,B_Neuro,I_Neuro}
  success := recover_voltage_state_phase_profile_conductance_boundary_loss
  failure := wire_signal_or_medical_story_only
  next := action_potential_toy_profile_worked_example
  - validation
  - medical_advice
  - full_model_claim
```

End.
