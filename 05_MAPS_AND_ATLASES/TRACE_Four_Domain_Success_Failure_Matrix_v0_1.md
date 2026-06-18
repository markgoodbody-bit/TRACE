# TRACE Four-Domain Success / Failure Matrix v0.1

Date: 2026-06-18
Status: four-domain success/failure matrix / translation-scaffold audit / not validation / not proof / not universal theory / not native-domain unification / not operator promotion / not Kernel v0.3

## 0. Control header

This file follows:

- `TRACE_Four_Domain_Unification_Status_Synthesis_v0_1.md`
- `TRACE_QIT_Three_Example_Consolidation_v0_1.md`
- `TRACE_Algebraic_Topology_Two_Example_Consolidation_v0_1.md`
- `TRACE_DSGE_Two_Profile_Consolidation_v0_1.md`
- `TRACE_Generative_Syntax_Two_Example_Consolidation_v0_1.md`

It tests the shared TRACE translation scaffold across four domains by asking, for each domain:

1. What must be preserved?
2. What is allowed to be lost only if declared?
3. What must back-translation recover?
4. What causes demotion?
5. What is the current status?

It does not claim validation.

It does not claim proof.

It does not claim the native theories are unified.

```trace
Four_Domain_Success_Failure_Matrix_v0_1 :=
  QIT
  + Topology
  + DSGE
  + Syntax
  -> compare:
      preserve_requirements
      + loss_requirements
      + back_translation_requirements
      + demotion_conditions
      + current_status
  - validation
  - proof
  - universal_completion
```

## 1. Matrix principle

The matrix tests whether TRACE is functioning as a translation grammar rather than a metaphor generator.

```trace
translation_success_if :=
  native_distinctions_preserved
  + declared_loss_visible
  + back_translation_recovers_native_case
  + status_demotes_when_loss_or_flattening_occurs
```

Failure:

```trace
translation_failure_if :=
  native_terms_relabelled_only
  OR native_structure_flattened
  OR loss_hidden
  OR back_translation_returns_generic_story
  OR status_not_demoted_after_loss
```

## 2. Core cross-domain matrix

| Domain | Example set | Must preserve | Must not flatten into | Current status |
|---|---|---|---|---|
| QIT | product/entangled, measurement record, dephasing | tensor/state distinction, record-state distinction, coherence/dephasing distinction | aggregation, record as full state, ordinary forgetting | internal candidate + native review required |
| Algebraic Topology | S1 vs D2, S2 vs T2 | cycle/boundary distinction, Betti-style profile contrast, invariant discipline | visual hole, shape vibe, generic boundary | internal candidate + native review required |
| DSGE / Macro | one demand shock, demand vs supply shock | model-conditioned profile, shock type, variable roles, no-forecast boundary | generic event story, prediction, policy advice | internal toy profile candidate + native review required |
| Generative Syntax | simple Merge, Merge vs linear order | operation type, syntactic object status, hierarchy, toy boundary | word order only, generic combination, surface string | internal toy profile candidate + native review required |

## 3. Preserve matrix

```trace
preserve_matrix :=
  QIT:
    tensor_composition_status
    + state_vs_record_distinction
    + dephasing_as_channel_not_forgetting
  Topology:
    cycle_boundary_distinction
    + Betti_or_invariant_profile
    + boundary_term_scope
  DSGE:
    shock_type_and_exogenous_status
    + tracked_variable_roles
    + response_path_as_toy_or_model_conditioned_profile
    + no_forecast_no_policy_advice_boundary
  Syntax:
    operation_type
    + syntactic_object_status
    + hierarchy_profile
    + surface_placeholder_status
    + label_and_feature_gaps
```

A TRACE translation succeeds only if the relevant domain entry can be recovered after translation.

## 4. Loss matrix

```trace
loss_matrix :=
  QIT:
    no_general_QIT_translation
    + no_foundations_claim
    + no_experimental_claim
    + no_specialist_review
  Topology:
    no_formal_homology_calculation_capacity
    + no_coefficient_scope_generalisation
    + no_functor_theory_claim
    + no_specialist_review
  DSGE:
    no_actual_model_equations
    + no_estimation_or_calibration
    + no_expectations_solution
    + no_welfare_or_policy_analysis
    + no_specialist_review
  Syntax:
    no_formal_derivation
    + no_label_theory
    + no_feature_calculus
    + no_judgment_data
    + no_parser
    + no_specialist_review
```

Loss rule:

```trace
loss_rule :=
  every_loss_entry
  must_affect:
    allowed_claim
    OR status
    OR back_translation_target
    OR next_gate
```

No-consequence loss is audit theatre.

## 5. Back-translation matrix

```trace
back_translation_matrix :=
  QIT:
    recover_product_vs_entangled_or_record_or_dephasing_case
    + recover_basis_or_channel_context_where_relevant
    + recover_not_ordinary_aggregation_or_forgetting
  Topology:
    recover_native_space_pair
    + recover_invariant_profile
    + recover_cycle_boundary_or_surface_contrast
    + recover_coefficient_scope_limits
  DSGE:
    recover_toy_model_or_profile_case
    + recover_shock_type
    + recover_variable_roles
    + recover_response_path_as_schematic
    + recover_no_forecast_no_policy_boundary
  Syntax:
    recover_toy_syntax_case_or_contrast
    + recover_lexical_items
    + recover_operation_type
    + recover_syntactic_object_status
    + recover_hierarchy_or_no_hierarchy
    + recover_no_judgment_no_grammar_boundary
```

Failure form:

```trace
back_translation_failure_common :=
  returns_only:
    metaphor
    OR generic_story
    OR surface_output
    OR decorative_TRACE_labels
```

## 6. Demotion matrix

| Domain | Demote if… | Demoted status |
|---|---|---|
| QIT | tensor/state/channel distinctions are lost or ordinary metaphors replace native structure | failed flattening or partial translation only |
| Topology | invariant profile becomes visual shape language or boundary meanings collapse | failed flattening or partial translation only |
| DSGE | response path becomes forecast, policy advice, or generic causal story | failed flattening or toy profile only |
| Syntax | Merge becomes generic combination, SO becomes string, hierarchy becomes word order | failed flattening or toy profile only |

Trace version:

```trace
demotion_matrix :=
  QIT:
    if tensor_or_record_or_dephasing_distinction_lost
    -> FAILED_FLATTENING_OR_PARTIAL_TRANSLATION
  Topology:
    if invariant_or_cycle_boundary_distinction_lost
    -> FAILED_FLATTENING_OR_PARTIAL_TRANSLATION
  DSGE:
    if IRF_as_forecast_or_policy_advice
    -> FAILED_FLATTENING_OR_TOY_ONLY
  Syntax:
    if Merge_as_generic_combination_or_SO_as_surface_string
    -> FAILED_FLATTENING_OR_TOY_ONLY
```

## 7. Common success condition

```trace
common_success_condition :=
  for_domain_D:
    native_case_recoverable
    + key_distinction_recoverable
    + profile_or_invariant_recoverable
    + boundary_scope_recoverable
    + loss_register_recoverable
    + no_forbidden_claim_added
```

If this condition holds, TRACE earns only an internal translation-candidate claim.

It does not earn native-domain truth.

## 8. Common failure condition

```trace
common_failure_condition :=
  for_domain_D:
    output_reads_like_TRACE_but_back_translation_cannot_recover_native_structure
```

Examples:

```trace
failure_examples :=
  QIT:
    entanglement_described_as_connectedness_only
  Topology:
    torus_described_as_having_more_hole_vibe_only
  DSGE:
    shock_profile_described_as_prediction_only
  Syntax:
    Merge_described_as_words_put_together_only
```

## 9. Fracture-line test

The scaffold fractures if a domain cannot be represented without importing alien structure.

```trace
fracture_line_test :=
  for_domain_D:
    if TRACE_form(D)
    requires:
      erasing_native_truth_conditions
      OR importing_terms_from_other_domain
      OR hiding_loss
      OR changing_native_object_of_analysis
    then:
      TRACE_translation_fails_for_D
```

Current fracture status:

```trace
current_fracture_status :=
  no_complete_fracture_detected_in_internal_toy_examples
  but:
    source_gap_large
    + specialist_review_absent
    + formal_math_unproven
    + toy_examples_may_be_too_friendly
```

## 10. What the matrix says worked

```trace
worked_so_far :=
  shared_record_shape_survived
  + profile_or_invariant_role_survived
  + explicit_loss_survived
  + back_translation_target_survived
  + demotion_rule_survived
  + anti_flattening_rules_survived
```

Plain version:

Across four domains, TRACE has remained usable as a disciplined translation record without immediately collapsing everything into the same metaphor.

## 11. What the matrix says did not work yet

```trace
not_worked_yet :=
  formal_universal_math
  + native_domain_theory_unification
  + external_validation
  + specialist_review
  + real_source_backed_formalisms_for_all_examples
  + cold_reviewer_back_translation
  + demonstrated_gain_over_existing_frameworks
```

Plain version:

The scaffold is coherent internally. It is not yet validated externally.

## 12. Strongest safe claim

```trace
strongest_safe_claim :=
  TRACE_currently_functions_as_an_internal_four_domain_translation_scaffold
  that:
    preserves_selected_native_distinctions
    + records_loss
    + requires_back_translation
    + demotes_overclaim
  across:
    QIT
    + Algebraic_Topology
    + DSGE
    + Generative_Syntax
```

## 13. Claims still forbidden

```trace
forbidden_claims :=
  TRACE_proves_universal_structure_of_all_domains
  OR TRACE_replaces_QIT_topology_macro_or_syntax
  OR TRACE_validated_by_four_domain_examples
  OR TRACE_has_formal_category_theory_account
  OR TRACE_solves_alignment_from_these_examples
  OR TRACE_can_skip_native_experts
```

## 14. Next build options

Option A: hostile audit this matrix.

```trace
option_A :=
  TRACE_Four_Domain_Success_Failure_Matrix_Hostile_Audit_v0_1
```

Option B: formalise the shared scaffold.

```trace
option_B :=
  TRACE_Formalisation_Workplan_From_Four_Domain_Matrix_v0_1
```

Option C: cold-review packet.

```trace
option_C :=
  TRACE_Four_Domain_Back_Translation_Cold_Review_Packet_v0_1
```

Recommended next:

```trace
recommended_next :=
  option_A
  because:
    matrix_language_can_overclaim
    + four_domain_synthesis_is_high_heat
    + hostile_audit_should_precede_formalisation_workplan
```

## 15. Final compression

```trace
Four_Domain_Success_Failure_Matrix_v0_1 :=
  domains := QIT + Topology + DSGE + Syntax
  success := native_distinction + profile + loss + back_translation + demotion
  failure := metaphor + hidden_loss + generic_story + surface_output
  current_result := internal_translation_scaffold_survived_four_domain_toy_tests
  current_limit := no_validation_no_native_theory_unification_no_formal_proof
  next := hostile_audit_before_formalisation
  - validation
  - proof
  - universal_completion
```

End.
