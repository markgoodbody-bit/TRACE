# TRACE Neurophysiology Action Potential Toy Profile Worked Example v0.1

Date: 2026-06-18
Status: toy action-potential worked example / voltage-trace profile / no real recording / not validation / not Hodgkin-Huxley solution / not medical advice / not clinical interpretation / not treatment guidance / not operator promotion / not Kernel v0.3

## 0. Control header

This file follows:

- `TRACE_Neurophysiology_Translation_Input_Packet_v0_1.md`
- `TRACE_Second_Four_Domain_Stress_Map_v0_1.md`
- `TRACE_Profile_Morphism_Formal_Status_Patch_v0_1.md`

It creates a toy voltage-trace profile only.

It does not model a real neuron.

It does not solve Hodgkin-Huxley equations.

It does not use recording data.

It does not give medical or clinical guidance.

```trace
Neurophysiology_Action_Potential_Toy_Profile_Worked_Example_v0_1 :=
  toy_voltage_trace
  + resting_baseline_placeholder
  + threshold_crossing_placeholder
  + depolarisation_peak_repolarisation_recovery_phases
  + conductance_context_named_not_solved
  + back_translation_test
  + loss_register
  - validation
  - full_biophysical_model
  - medical_advice
```

## 1. Toy native case

The toy case uses a schematic membrane-voltage profile.

```trace
toy_native_case :=
  model_family := toy_action_potential_voltage_trace
  + membrane_voltage_unit := mV_placeholder
  + time_unit := ms_placeholder
  + resting_baseline := -70
  + threshold_placeholder := -55
  + peak_placeholder := +30
  + recovery_placeholder := -70
  + conductance_context := named_gap_only
  + Hodgkin_Huxley_status := not_solved
```

Boundary:

These values are schematic placeholders for translation testing. They are not fitted data, not a clinical reference, and not a complete physiological model.

## 2. Toy phase profile

```trace
toy_phase_profile :=
  phase_0_resting:
    voltage := -70
    status := resting_baseline_placeholder
  phase_1_threshold_crossing:
    voltage := -55
    status := threshold_placeholder
  phase_2_depolarisation_peak:
    voltage := +30
    status := peak_placeholder
  phase_3_repolarisation:
    voltage := decreasing_toward_baseline
    status := recovery_phase_placeholder
  phase_4_recovery:
    voltage := -70
    status := return_to_baseline_placeholder
```

Plain version:

The profile tests whether TRACE can preserve phase structure in a voltage trace without turning the action potential into a generic signal or message.

## 3. Conductance context status

The conductance context is named but not solved.

```trace
conductance_context_status :=
  named_biophysical_context
  not:
    solved_channel_dynamics
    OR Hodgkin_Huxley_solution
    OR fitted_conductance_model
    OR empirical_recording
```

Consequence:

```trace
conductance_context_consequence :=
  no_channel_equation_solution_claim
  + no_parameter_fit_claim
  + no_real_neuron_claim
```

## 4. Hodgkin-Huxley status

```trace
Hodgkin_Huxley_status :=
  referenced_as_native_model_family_context
  not:
    equations_solved
    OR parameters_supplied
    OR conductance_dynamics_calculated
    OR physiology_prediction
```

Failure:

```trace
failure := Hodgkin_Huxley_named_as_if_solved
```

## 5. Synaptic and LTP boundary

This toy example is about an action-potential voltage trace, not a synaptic plasticity model.

```trace
synaptic_LTP_status :=
  not_modelled_gap
  not:
    synaptic_transmission_solution
    OR LTP_mechanism
    OR learning_model
    OR memory_claim
```

Consequence:

```trace
synaptic_LTP_consequence :=
  no_synaptic_mechanism_claim
  + no_LTP_mechanism_claim
  + no_memory_claim
```

## 6. Toy profile object

```trace
Neurophysiology_toy_profile :=
  model_family_status := toy_action_potential_voltage_trace
  + state_variable := membrane_voltage
  + voltage_placeholders := [-70, -55, +30, decreasing_toward_baseline, -70]
  + phase_sequence := [resting, threshold_crossing, depolarisation_peak, repolarisation, recovery]
  + conductance_context := named_not_solved
  + Hodgkin_Huxley_status := not_solved
  + synaptic_LTP_status := not_modelled_gap
  + readout := voltage_trace_profile
  + boundary := no_recording_no_full_model_no_medical_guidance
```

This is a profile object for translation testing, not a simulation or applied interpretation.

## 7. TRACE-form mapping

```trace
TRACE_form(Neurophysiology) :=
  {S_Neuro, T_Neuro, C_Neuro, O_Neuro, K_Neuro, B_Neuro, I_Neuro}
```

Mapping:

```trace
S_Neuro := membrane_voltage_state_and_named_channel_context
T_Neuro := phase_transition_across_toy_voltage_trace
C_Neuro := ordered_phase_profile_composition
O_Neuro := voltage_trace_readout
K_Neuro := ion_channel_capacitance_gradient_constraints_named_not_solved
B_Neuro := toy_time_window_no_recording_no_medical_boundary
I_Neuro := action_potential_voltage_trace_profile
```

## 8. Candidate translation-map instance

Using cooled morphism language:

```trace
m_Neuro_AP:
  structured_native_voltage_trace_profile_record
  -> structured_TRACE_neurophysiology_profile_record
```

Read as candidate translation-map shape only.

Preservation target:

```trace
m_Neuro_AP_preserves :=
  membrane_voltage_state
  + phase_sequence
  + threshold_status
  + peak_and_recovery_status
  + conductance_context_as_named_gap
  + Hodgkin_Huxley_not_solved_boundary
  + synaptic_LTP_gap
  + no_medical_boundary
  + loss_register
```

## 9. Back-translation test

```trace
BT_Neuro(m_Neuro_AP(Neurophysiology_toy_profile))
  ~=
  toy_action_potential_voltage_trace_under_declared_loss
```

Required recovery:

```trace
back_translation_recovery :=
  toy_action_potential_voltage_trace_case
  + membrane_voltage_state_variable
  + resting_baseline_placeholder_minus_70
  + threshold_placeholder_minus_55
  + peak_placeholder_plus_30
  + repolarisation_and_recovery_phases
  + conductance_context_named_not_solved
  + Hodgkin_Huxley_not_solved
  + synaptic_LTP_not_modelled
  + voltage_trace_readout
  + no_recording_no_full_model_no_medical_boundary
  + loss_register
```

Failure:

```trace
back_translation_fails_if:
  translation_returns_only:
    neuron_sends_signal
  but_loses:
    membrane_voltage_state
    + phase_sequence
    + threshold_and_recovery_profile
    + conductance_context_gap
    + Hodgkin_Huxley_not_solved_boundary
    + no_medical_boundary
```

## 10. Critical distinctions tested

### 10.1 Action potential is not generic signal

```trace
action_potential_test :=
  phase_profile := resting -> threshold_crossing -> depolarisation_peak -> repolarisation -> recovery
  not:
    generic_signal
    OR message
```

Failure:

```trace
failure := action_potential_flattened_to_signal_message
```

### 10.2 Resting membrane potential is not inactivity

```trace
resting_status_test :=
  resting_baseline := active_biophysical_state_placeholder
  not:
    nothing_happening
    OR inactive_zero
```

Failure:

```trace
failure := resting_state_flattened_to_absence
```

### 10.3 Threshold is not a decision metaphor

```trace
threshold_test :=
  threshold_placeholder := voltage_condition_in_toy_profile
  not:
    choice_point
    OR moral_boundary
    OR decision_gate
```

Failure:

```trace
failure := threshold_metaphor_replaces_voltage_context
```

### 10.4 Conductance is not wire current

```trace
conductance_test :=
  ion_channel_conductance_context := named_gap
  not:
    ordinary_wire_current
    OR generic_flow
```

Failure:

```trace
failure := channel_context_collapsed_to_wire_model
```

### 10.5 LTP is not memory itself

```trace
LTP_boundary_test :=
  LTP_status := not_modelled_gap
  not:
    memory_claim
    OR learning_explanation
```

Failure:

```trace
failure := LTP_gap_replaced_by_memory_story
```

### 10.6 Medical boundary stays active

```trace
medical_boundary_test :=
  no_medical_advice
  + no_clinical_interpretation
  + no_treatment_guidance
```

Failure:

```trace
failure := toy_voltage_profile_read_as_clinical_or_guidance_output
```

## 11. Loss register

```trace
L_Neuro_AP :=
  toy_voltage_trace_only
  + no_real_recording
  + no_parameter_fit
  + no_full_Hodgkin_Huxley_solution
  + no_spatial_cable_model
  + no_synaptic_model
  + no_LTP_mechanism
  + no_medical_or_clinical_evaluation
```

Loss effects:

```trace
loss_effects :=
  no_real_recording -> no_real_neuron_claim
  + no_parameter_fit -> no_empirical_model_claim
  + no_Hodgkin_Huxley_solution -> no_full_channel_model_claim
  + no_spatial_cable_model -> no_propagation_model_claim
  + no_synaptic_model -> no_synaptic_transmission_claim
  + no_LTP_mechanism -> no_memory_or_learning_claim
  + no_clinical_evaluation -> no_medical_claim
```

## 12. What this earns

```trace
earned_claim :=
  TRACE_can_preserve_one_toy_action_potential_voltage_trace_profile_internally
  + action_potential_not_generic_signal_is_testable
  + resting_state_not_inactivity_is_testable
  + threshold_not_decision_metaphor_is_testable
  + conductance_gap_not_wire_current_is_testable
  + LTP_not_memory_itself_boundary_is_testable
  + medical_boundary_is_active
  - validation
  - full_biophysical_model
  - medical_advice
```

## 13. What remains untested

```trace
not_tested :=
  real_neuronal_recording
  + source_backed_equations
  + Hodgkin_Huxley_parameter_solution
  + voltage_gated_channel_dynamics
  + spatial_cable_propagation
  + synaptic_transmission
  + LTP_mechanism
  + network_neuroscience
  + clinical_context
  + specialist_review
```

## 14. Next step

```trace
recommended_next :=
  Neurophysiology_Toy_Status_Patch_or_Input_Consolidation
  because:
    action_potential_language_can_flatten_to_signal
    + threshold_language_can_metaphorise
    + LTP_language_can_overclaim_memory
    + medical_boundary_must_remain_active
```

Alternative:

```trace
alternative_next :=
  Geodynamics_input_packet
  if:
    second_battery_sequence_prioritises_domain_breadth_over_neurophysiology_cooling
```

## 15. Final compression

```trace
Neurophysiology_Action_Potential_Toy_Profile_Worked_Example_v0_1 :=
  case := toy_voltage_trace_rest_threshold_peak_recovery
  profile := membrane_voltage + phase_sequence + conductance_gap + no_HH_solution + no_medical_boundary
  success := recover_voltage_state_phase_profile_boundary_loss
  failure := signal_wire_or_medical_story
  status := INTERNAL_PROFILE_CANDIDATE + TOY_STATUS_REQUIRED + NATIVE_REVIEW_REQUIRED
  next := cooling_or_consolidation
  - validation
  - full_model
  - medical_advice
```

End.
