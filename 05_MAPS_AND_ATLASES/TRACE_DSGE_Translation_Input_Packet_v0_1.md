# TRACE DSGE Translation Input Packet v0.1

Date: 2026-06-18
Status: new-domain input packet / Dynamic Macroeconomics and DSGE stress domain / not validation / not proof / not macroeconomic theory / not policy advice / not operator promotion / not Kernel v0.3

## 0. Control header

This file opens the Dynamic Macroeconomics / DSGE path under:

- `TRACE_Translation_Success_Protocol_v0_1.md`
- `TRACE_Generic_Invariant_Profile_Translation_Template_v0_1.md`
- `TRACE_Profile_Morphism_Formal_Status_Patch_v0_1.md`

It begins with native macroeconomic structure.

It does not import topology terms.

It does not import QIT terms.

It does not claim TRACE unifies macroeconomics.

It does not replace macroeconomics, econometrics, central-bank modelling, or specialist judgment.

```trace
DSGE_input_packet :=
  native_macro_entry
  + dynamic_state_structure
  + shocks_expectations_constraints
  + profile_family_required
  + loss_register_required
  - validation
  - macro_unification
  - policy_advice
```

## 1. Domain name

```trace
domain_name := Dynamic_Macroeconomics_DSGE
```

Plain version:

This domain studies macroeconomic systems through dynamic models with state variables, expectations, shocks, policy rules, constraints, and equilibrium conditions.

## 2. Native object space

The native object space is not a topological or QIT object space. It is a macroeconomic model-and-path object space.

```trace
native_macro_object_space :=
  model_specification
  + state_variables
  + control_variables
  + shock_processes
  + expectation_structure
  + equilibrium_conditions
  + policy_or_closure_rules
  + simulated_or_solved_paths
```

Candidate native object for first probe:

```trace
native_object_or_case :=
  one_shock_DSGE_impulse_response_profile
  under:
    simplified_internal_translation_probe
```

Boundary:

This is not a full DSGE model. It is an input packet for testing whether TRACE can preserve the native shape of a DSGE-style shock-response profile without turning it into generic cause-and-effect language.

## 3. Native structure to preserve

```trace
native_structure :=
  dynamic_state_evolution
  + intertemporal_constraints
  + expectations
  + stochastic_shocks
  + equilibrium_or_solution_conditions
  + policy_or_closure_rule
  + impulse_response_or_path_profile
```

Plain version:

The important macro structure is not simply that an event causes outcomes. The important structure is a model-defined economy moving through time under constraints, expectations, shocks, and equilibrium/solution rules.

## 4. Native terms

```trace
native_terms :=
  state_variable
  + control_variable
  + shock
  + expectation
  + transition_equation
  + equilibrium_condition
  + policy_rule
  + constraint
  + calibration_or_estimation
  + impulse_response_function
  + steady_state
  + stability_or_determinacy_condition
  + welfare_or_loss_measure
```

Working definitions for this packet only:

```trace
working_definitions :=
  state_variable := variable_carrying_dynamic_condition_between_periods
  control_variable := choice_or_response_variable_in_model_solution
  shock := stochastic_disturbance_specified_by_model
  expectation := forward_looking_term_or_belief_condition_inside_model
  impulse_response := model_path_response_to_specified_shock
  steady_state := reference_condition_around_which_dynamics_may_be_expressed
```

These are working definitions only and require source/specialist review before public use.

## 5. Candidate native profile family

The first native profile family is an impulse-response profile.

```trace
native_profile_family :=
  impulse_response_profile
```

Candidate profile object:

```trace
DSGE_profile_object :=
  model_id
  + shock_type
  + shock_size_or_normalisation
  + variables_tracked
  + response_path_over_time
  + horizon
  + steady_state_or_reference_path
  + policy_rule_or_closure_context
  + constraint_context
```

Profile assignment:

```trace
Phi_DSGE:
  model_and_shock_case
  -> impulse_response_profile
```

Profile value:

```trace
P_DSGE(case) :=
  path_profile_of_selected_variables_after_specified_shock
```

## 6. Critical distinctions

The translation must preserve these distinctions:

```trace
critical_distinctions :=
  endogenous_vs_exogenous_variable
  + shock_vs_policy_rule
  + state_variable_vs_control_variable
  + expectation_term_vs_observed_outcome
  + model_solution_path_vs_real_world_prediction
  + calibration_or_estimation_vs_truth
  + steady_state_reference_vs_actual_history
  + impulse_response_profile_vs_story_about_causation
```

Plain version:

A DSGE translation fails if it turns a model-conditioned path into an ordinary causal narrative.

## 7. Intended TRACE form

```trace
TRACE_form(Dynamic_Macroeconomics_DSGE) :=
  {S_Macro, T_Macro, C_Macro, O_Macro, K_Macro, B_Macro, I_Macro}
```

Candidate mapping:

```trace
S_Macro := model_state_space_and_state_variables
T_Macro := transition_solution_or_policy_response_mapping
C_Macro := aggregation_or_model_closure_composition_when_relevant
O_Macro := model_output_measurement_or_impulse_response_readout
K_Macro := budget_resource_equilibrium_expectation_and_policy_constraints
B_Macro := model_boundary_closure_and_horizon_scope
I_Macro := impulse_response_profile_or_welfare_loss_stability_measure
```

## 8. Known flattening risks

```trace
flattening_risks :=
  shock_as_generic_event
  + impulse_response_as_prediction
  + equilibrium_as_moral_balance
  + expectations_as_feelings
  + policy_rule_as_human_intention
  + model_output_as_reality
  + calibration_as_truth
  + endogenous_exogenous_boundary_erased
```

Hard guard:

```trace
hard_guard :=
  no_macro_claim
  unless:
    native_model_structure_preserved
    + shock_context_preserved
    + expectation_constraint_context_preserved
    + loss_register_written
    + back_translation_possible
```

## 9. Initial loss register

### 9.1 Model family not specified yet

```trace
loss_entry_1 :=
  source_feature := full_DSGE_model_family
  -> TRACE_translation := generic_one_shock_impulse_response_input_packet
  -> loss_or_distortion := no_specific_model_equations_or_solution_method
  -> consequence_for_back_translation := cannot_recover_specific_model_dynamics_yet
```

### 9.2 No empirical estimation

```trace
loss_entry_2 :=
  source_feature := calibration_estimation_and_empirical_fit
  -> TRACE_translation := not_tested
  -> loss_or_distortion := no_data_no_estimation_no_fit_assessment
  -> consequence_for_back_translation := no_real_world_forecast_or_policy_claim
```

### 9.3 Expectations simplified

```trace
loss_entry_3 :=
  source_feature := formal_expectations_structure
  -> TRACE_translation := expectation_context_placeholder
  -> loss_or_distortion := rational_adaptive_or_other_expectation_form_not_specified
  -> consequence_for_back_translation := no_expectation_solution_claim
```

### 9.4 Equilibrium and determinacy not solved

```trace
loss_entry_4 :=
  source_feature := equilibrium_solution_and_determinacy_conditions
  -> TRACE_translation := solution_condition_placeholder
  -> loss_or_distortion := no_existence_uniqueness_stability_determinacy_check
  -> consequence_for_back_translation := no_solved_DSGE_claim
```

### 9.5 Policy interpretation excluded

```trace
loss_entry_5 :=
  source_feature := policy_evaluation_and_welfare_analysis
  -> TRACE_translation := not_tested
  -> loss_or_distortion := no_policy_recommendation_or_welfare_result
  -> consequence_for_back_translation := no_policy_advice_authorised
```

## 10. Back-translation target

A successful first DSGE translation should recover:

```trace
back_translation_target :=
  model_and_shock_case
  + state_control_variable_distinction
  + shock_type_and_size_context
  + expectation_or_forward_looking_context_if_present
  + policy_or_closure_rule_context
  + response_path_over_time
  + horizon_and_reference_path
  + explicit_model_scope_limits
```

Failure:

```trace
translation_fails_if:
  TRACE_form_returns_only:
    shock_causes_output_change
  but:
    cannot_recover_model_conditioning
    + cannot_recover_variable_roles
    + cannot_recover_response_path
    + cannot_recover_scope_conditions
```

## 11. Candidate first worked example

Recommended next file:

```trace
next_worked_example :=
  TRACE_DSGE_One_Shock_Response_Profile_Worked_Example_v0_1
  with:
    toy_model_scope
    + one_named_shock
    + selected_variables
    + response_path_profile
    + endogenous_exogenous_distinction
    + back_translation_test
```

Boundary:

The worked example must stay toy/schematic unless source-backed model equations are added.

## 12. Status after input packet

```trace
DSGE_status :=
  NOT_STARTED_TRANSLATION
  + input_packet_exists
  + native_macro_object_space_named
  + native_profile_family_named
  + source_gap_named
  + loss_register_started
  - worked_example_complete
  - validation
  - macro_unification
  - policy_advice
```

## 13. Final compression

```trace
DSGE_Translation_Input_Packet_v0_1 :=
  domain := Dynamic_Macroeconomics_DSGE
  native_object_space := model_specification + state_variables + shocks + expectations + equilibrium_conditions + paths
  first_profile_family := impulse_response_profile
  critical_distinction := model_conditioned_path_not_generic_causation_story
  TRACE_form := {S_Macro,T_Macro,C_Macro,O_Macro,K_Macro,B_Macro,I_Macro}
  success := recover_model_shock_variable_path_scope_structure
  failure := shock_as_generic_event_or_prediction
  next := one_shock_response_profile_worked_example
  - validation
  - macro_unification
  - policy_advice
```

End.
