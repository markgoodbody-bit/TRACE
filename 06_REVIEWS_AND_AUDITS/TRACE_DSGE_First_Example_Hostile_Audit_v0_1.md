# TRACE DSGE First Example Hostile Audit v0.1

Date: 2026-06-18
Status: hostile audit / DSGE toy-profile pressure / not validation / not proof / not macroeconomic theory / not forecast / not policy advice / not operator promotion / not Kernel v0.3

## 0. Audit identity and limits

```text
Reviewer identity: Framework hostile self-audit
Scope: DSGE one-shock toy response profile only
Files audited:
  - TRACE_DSGE_Translation_Input_Packet_v0_1.md
  - TRACE_DSGE_One_Shock_Response_Profile_Worked_Example_v0_1.md
External sources used: none in this audit
Specialist macroeconomic review: absent
Confidence: limited
```

This audit attacks whether the DSGE toy example has accidentally created the appearance of a macroeconomic model, forecast, or policy result.

```trace
audit_question :=
  does_DSGE_toy_profile_preserve_native_macro_roles
  OR merely_turn_macro_terms_into_plausible_story_table?
```

## 1. Verdict

VERDICT: `retain_but_patch_before_second_macro_profile`

```trace
verdict :=
  retain_DSGE_toy_example
  because:
    it_blocks_generic_causation_story
    + it_names_exogenous_endogenous_distinction
    + it_preserves_response_path_profile
    + it_blocks_forecast_and_policy_claims
  but:
    toy_values_can_look_like_model_output
    + no_equations_exist
    + no_expectations_structure_exists
    + no_solution_method_exists
    + policy_rate_language_can_leak_policy_interpretation
```

Plain verdict:

Keep it. It is a useful translation stress test. But before any second macro example, add a cooling/term-status patch that makes the toy table impossible to read as a solved DSGE output.

## 2. Main risk: toy table as fake model output

The table gives numerical paths for `y`, `pi`, and `i`. Even with warnings, numerical paths can look like a model solution.

```trace
toy_table_risk :=
  numerical_values
  + macro_variable_names
  + time_path
  -> apparent_model_output
```

Patch required:

```trace
patch_toy_values :=
  toy_values := schematic_placeholder_profile_values
  not:
    solved_model_output
    OR empirical_estimate
    OR forecast
    OR calibration_result
```

## 3. Native macro structure gap

The example has no model equations, no objective function, no household/firm structure, no expectations operator, no equilibrium definition, and no solution method.

```trace
native_structure_gap :=
  no_model_equations
  + no_microfoundations
  + no_expectations_operator
  + no_equilibrium_definition
  + no_solution_method
  + no_determinacy_check
```

Consequence:

```trace
consequence :=
  translation_probe_only
  + no_solved_DSGE_claim
  + no_macro_theory_claim
```

## 4. Policy-rate interpretation risk

The worked example includes `policy_rate_i`. That is dangerous because readers may infer central bank intention, policy recommendation, or welfare judgment.

```trace
policy_rate_risk :=
  policy_rate_i
  may_be_read_as:
    central_bank_intention
    OR recommended_policy
    OR welfare_optimal_response
```

Patch required:

```trace
patch_policy_rate_status :=
  policy_rate_i := schematic_response_variable_in_toy_profile
  not:
    policy_recommendation
    OR institution_intention_claim
    OR welfare_result
```

## 5. Exogenous/endogenous distinction partially works

Strength:

```trace
strength :=
  positive_demand_shock_marked_as_exogenous_for_toy_case
  + y_pi_i_marked_as_response_variables
```

Weakness:

The example does not specify why those variables respond as they do. There is no structural equation or decision rule.

```trace
weakness :=
  variable_roles_named
  but:
    response_mechanism_not_modelled
```

Patch required:

```trace
patch_response_mechanism_status :=
  response_path_values := illustrative_translation_profile
  not:
    derived_from_structural_model
```

## 6. Expectation structure missing

The input packet names expectations as important, but the worked example does not include a formal expectation term.

```trace
expectation_gap :=
  expectations_named_in_packet
  but:
    not_present_in_toy_profile
    + no_forward_solution_condition
```

Consequence:

```trace
expectation_gap_consequence :=
  cannot_claim_DSGE_expectations_preserved
  + can_only_claim_expectation_gap_visible
```

Patch required:

```trace
patch_expectations_status :=
  expectations := named_as_unmodelled_gap
  not:
    preserved_in_first_worked_example
```

## 7. Impulse response vs prediction pass, but fragile

Strength:

The file repeatedly says the path is not a forecast.

Attack:

The phrase `response path` plus time-indexed table can still be read as prediction unless every later use preserves the toy/schematic label.

```trace
IRF_prediction_fragility :=
  not_forecast_label_present
  but:
    time_path_table_invites_prediction_reading
```

Patch required:

```trace
patch_IRF_label :=
  every_DSGE_path_profile
  must_carry:
    toy_or_model_conditioned_status
    + no_forecast_status
    + no_empirical_status
```

## 8. Back-translation pass condition is useful

The back-translation target is the strongest part of the file.

```trace
strongest_feature :=
  back_translation_requires:
    toy_case
    + shock_context
    + variable_roles
    + path_values
    + no_forecast_boundary
```

Retain this. It prevents the table collapsing into generic causation.

## 9. Loss register pass, but must affect status

The loss register names missing equations, estimation, solution method, expectations, welfare, and policy advice.

Strength:

```trace
loss_register_strength :=
  missing_native_macro_structure_visible
```

Weakness:

Loss must change allowed claims. The file mostly does this, but the next patch should make it explicit.

```trace
loss_register_required_effect :=
  no_equations -> no_solved_model_claim
  + no_estimation -> no_empirical_claim
  + no_expectations -> no_expectations_preserved_claim
  + no_welfare -> no_policy_advice
```

## 10. Required patch before second macro profile

```trace
required_patch_before_second_macro_profile :=
  toy_values_status_patch
  + policy_rate_status_patch
  + expectations_gap_patch
  + response_mechanism_status_patch
  + IRF_not_forecast_label
  + loss_register_claim_effects
```

Minimal acceptable patch file:

```trace
DSGE_First_Example_Toy_Status_Patch_v0_1 :=
  toy_table_not_model_solution
  + policy_rate_not_policy_advice
  + expectations_gap_visible
  + response_values_not_derived
  + no_forecast_no_empirical_claim
```

## 11. Audit result

```trace
audit_result :=
  retain_DSGE_first_example
  + patch_toy_status_before_second_macro_profile
  + do_not_delete
  + do_not_promote
  + do_not_add_second_macro_profile_until_patch
  - validation
  - solved_DSGE
  - forecast
  - policy_advice
```

Plain result:

The example is worth keeping. It is a real stress test of whether TRACE can preserve a model-conditioned path rather than generic causation. But the table and policy-rate variable create enough risk that a toy-status patch is required before continuing macro expansion.

## 12. Final compression

```trace
DSGE_First_Example_Hostile_Audit_v0_1 :=
  verdict := retain_but_patch_before_second_macro_profile
  strengths := exogenous_shock + variable_roles + response_path + back_translation
  weaknesses := toy_values_look_like_output + no_equations + no_expectations + no_solution + policy_rate_leak
  required_patch := DSGE_First_Example_Toy_Status_Patch_v0_1
  next := toy_status_patch_before_second_macro_profile
  - validation
  - solved_DSGE
  - forecast
  - policy_advice
```

End.
