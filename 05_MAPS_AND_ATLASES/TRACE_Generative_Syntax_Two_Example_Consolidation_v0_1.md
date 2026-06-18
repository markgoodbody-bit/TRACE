# TRACE Generative Syntax Two-Example Consolidation v0.1

Date: 2026-06-18
Status: Generative Syntax two-example consolidation / toy schematic syntax branch / contrast matrix / not validation / not proof / not full grammar / not formal derivation claim / not grammar implementation / not operator promotion / not Kernel v0.3

## 0. Control header

This file consolidates the first two Generative Syntax toy profile probes:

1. `TRACE_Generative_Syntax_Simple_Merge_Worked_Example_v0_1.md`
2. `TRACE_Generative_Syntax_Merge_vs_Linear_Order_Contrast_v0_1.md`

It also carries forward:

- `TRACE_Generative_Syntax_First_Example_Toy_Status_Patch_v0_1.md`
- `TRACE_Profile_Morphism_Formal_Status_Patch_v0_1.md`

It does not claim a formal derivation.

It does not claim a full grammar.

It does not use judgment data.

It does not implement a parser.

```trace
Generative_Syntax_Two_Example_Consolidation_v0_1 :=
  simple_External_Merge_profile
  + Merge_vs_linear_order_contrast
  -> common_success_failure_matrix
  + syntax_back_translation_suite
  + syntax_profile_translation_seed
  - validation
  - full_grammar
  - parser_claim
```

## 1. Why this consolidation matters

The first syntax example tested whether TRACE could preserve a toy External Merge profile rather than flatten it into generic word combination.

The second syntax example tested whether TRACE could preserve a contrast between hierarchical construction and linear sequence, even when the surface placeholder is the same.

Together they test whether TRACE can preserve syntax profile structure without turning syntax into ordinary word order.

```trace
syntax_flattening_errors :=
  Merge_as_generic_combination
  + syntactic_object_as_surface_string
  + hierarchy_as_linear_order
  + surface_readout_as_full_derivation
  + feature_gap_hidden
```

## 2. Shared syntax TRACE-form

```trace
TRACE_form(Generative_Syntax_Minimalist_Program) :=
  {S_Syntax, T_Syntax, C_Syntax, O_Syntax, K_Syntax, B_Syntax, I_Syntax}
```

Working role meanings:

```trace
S_Syntax := lexical_items_features_and_syntactic_object_context
T_Syntax := Merge_or_other_derivational_operation_label_under_toy_status
C_Syntax := operation_composition_or_structure_building_contrast
O_Syntax := interface_or_surface_readout_placeholder
K_Syntax := toy_scope_label_gap_feature_gap_and_no_judgment_conditions
B_Syntax := derivation_boundary_surface_scope_and_no_full_grammar_boundary
I_Syntax := derivation_feature_dependency_or_hierarchy_contrast_profile
```

Toy-status rule remains active:

```trace
toy_status_active :=
  all_syntax_profiles := toy_translation_profiles
  not:
    formal_derivation
    OR full_grammar
    OR judgment_data
    OR parser_output
    OR language_specific_claim
```

## 3. Common success-failure matrix

| Example | Native distinction tested | TRACE role pressure | Success condition | Failure condition | Earned result |
|---|---|---|---|---|---|
| Simple External Merge profile | Merge operation and syntactic object vs words combined | `T_Syntax` operation; `I_Syntax` derivation profile; `B_Syntax` toy boundary | Recover lexical items, External Merge, SO1, hierarchy, surface placeholder as interface, and loss register | Returns only “the words were combined” | TRACE preserves one toy External Merge profile internally |
| Merge vs linear order contrast | same surface placeholder but different structural status | `T_Syntax` operation contrast; `I_Syntax` hierarchy contrast; `O_Syntax` surface placeholder | Recover operation type, syntactic-object status, hierarchy present vs absent, and toy boundary | Flattens both records to same surface string | TRACE preserves one toy syntax contrast internally |

## 4. Common back-translation suite

A syntax profile translation is internally live only if back-translation recovers operation, structure, and toy status.

```trace
Syntax_back_translation_suite :=
  recover_toy_syntax_case_or_contrast
  + recover_lexical_items
  + recover_operation_type
  + recover_syntactic_object_status
  + recover_hierarchy_profile
  + recover_surface_readout_as_placeholder
  + recover_label_gap
  + recover_feature_dependency_gap
  + recover_no_judgment_no_grammar_boundary
  + recover_loss_register
```

For current examples:

```trace
current_Syntax_back_translation_targets :=
  simple_Merge_profile:
    lexical_items_D_the_N_cat
    + External_Merge_operation
    + SO1_syntactic_object
    + binary_branching_toy_structure
    + surface_readout_placeholder
  Merge_vs_linear_order_contrast:
    Merge_record_has_SO1_and_hierarchy
    + Linear_record_has_sequence_without_syntactic_object_claim
    + shared_surface_placeholder
    + hierarchy_present_vs_absent
```

Failure:

```trace
Syntax_translation_fails_if:
  back_translation_returns_words_only
  OR surface_placeholder_replaces_syntactic_object
  OR Merge_becomes_generic_combination
  OR hierarchy_contrast_lost
  OR feature_gap_hidden
  OR toy_status_hidden
```

## 5. Emerging syntax profile translation seed

```trace
syntax_profile_translation_seed :=
  toy_syntax_case
  -> selected_lexical_items
  -> operation_sequence
  -> syntactic_object_or_sequence_status
  -> hierarchy_profile
  -> surface_or_interface_readout_scope
  -> label_feature_and_judgment_gaps
  -> TRACE_I_Syntax
  -> back_translation_test
```

Acceptable translation:

```trace
acceptable_syntax_profile_translation_if:
  native_syntax_case_recoverable
  + lexical_items_recoverable
  + operation_type_recoverable
  + syntactic_object_status_recoverable
  + hierarchy_or_no_hierarchy_recoverable
  + surface_placeholder_status_recoverable
  + loss_register_visible
```

Unacceptable translation:

```trace
unacceptable_syntax_profile_translation_if:
  word_order_only
  OR generic_combination_only
  OR surface_string_as_full_structure
  OR label_gap_hidden
  OR feature_gap_hidden
  OR judgment_claim_added
```

## 6. Cross-example anti-flattening rules

```trace
anti_flattening_rules :=
  Merge != generic_combination
  + syntactic_object != surface_string
  + hierarchy != linear_order
  + surface_readout != full_derivation
  + toy_operation_label != formal_definition
  + no_judgment_data != grammaticality_claim
  + missing_feature_calculus != preserved_features
```

Plain version:

TRACE may translate syntax toy profiles only if it keeps operation type, syntactic-object status, hierarchy, surface placeholder status, and missing native syntax machinery visible.

## 7. Combined loss ledger

### 7.1 Toy operation labels only

```trace
loss_entry_1 :=
  source_feature := formal_Merge_definition_and_derivation_theory
  -> TRACE_translation := toy_operation_labels
  -> loss_or_distortion := no_source_backed_formal_definition
  -> consequence_for_back_translation := no_formal_derivation_claim
```

### 7.2 No label theory

```trace
loss_entry_2 :=
  source_feature := labelling_or_head_projection_theory
  -> TRACE_translation := unresolved_gap
  -> loss_or_distortion := phrase_category_and_head_status_not_defined
  -> consequence_for_back_translation := no_phrase_category_claim
```

### 7.3 No feature calculus

```trace
loss_entry_3 :=
  source_feature := feature_checking_or_valuation_system
  -> TRACE_translation := not_modelled_gap
  -> loss_or_distortion := feature_dependencies_not_solved
  -> consequence_for_back_translation := no_feature_dependency_claim
```

### 7.4 No judgment data

```trace
loss_entry_4 :=
  source_feature := grammaticality_or_acceptability_judgments
  -> TRACE_translation := not_tested
  -> loss_or_distortion := no_judgment_dataset
  -> consequence_for_back_translation := no_grammaticality_claim
```

### 7.5 No implementation

```trace
loss_entry_5 :=
  source_feature := parser_or_derivation_engine
  -> TRACE_translation := not_tested
  -> loss_or_distortion := no_algorithmic_generation_or_parsing
  -> consequence_for_back_translation := no_implementation_claim
```

## 8. Status after two syntax profiles

```trace
Syntax_two_profile_status :=
  INTERNAL_PROFILE_CANDIDATE
  + NATIVE_REVIEW_REQUIRED
  + TOY_STATUS_COOLED
  for:
    simple_External_Merge_profile
    + Merge_vs_linear_order_contrast
  because:
    operation_type_preserved_internally
    + syntactic_object_status_preserved_internally
    + hierarchy_contrast_preserved_internally
    + syntax_flattening_errors_named
    + loss_register_visible
  but:
    no_formal_source_backing
    + no_label_theory
    + no_feature_calculus
    + no_judgment_data
    + no_parser
    + no_specialist_review
```

## 9. What this earns

```trace
earned_claim :=
  TRACE_Syntax_branch_now_has_two_internal_toy_profile_translation_probes
  + common_syntax_back_translation_suite_exists
  + syntax_profile_translation_seed_exists
  + Merge_not_generic_combination_is_testable
  + same_surface_different_structure_contrast_is_testable
  - validation
  - full_grammar
  - formal_derivation_claim
  - parser_claim
  - syntax_unification
```

This is expansion with toy-status control.

## 10. What remains untested

```trace
not_tested :=
  source_backed_Minimalist_formalism
  + labelling_algorithm
  + feature_checking_or_valuation
  + Agree
  + Internal_Merge_or_movement
  + copy_theory
  + phase_theory
  + interface_mapping
  + judgment_data
  + language_specific_analysis
  + cross_linguistic_variation
  + parser_or_grammar_implementation
  + specialist_review
```

## 11. Four-domain matrix gate

The four-domain matrix may now proceed because all four stress domains have at least one internal profile path, and syntax now has two toy profile probes.

```trace
four_domain_matrix_gate :=
  QIT_three_example_consolidation_exists
  + topology_two_example_consolidation_exists
  + DSGE_two_profile_consolidation_exists
  + syntax_two_profile_consolidation_exists
  + no_native_theory_unification_claim
  + no_validation_claim
  + loss_register_discipline_active
  + back_translation_discipline_active
```

Recommended next file:

```trace
recommended_next :=
  TRACE_Four_Domain_Success_Failure_Matrix_v0_1
  because:
    four_domain_paths_now_have_internal_consolidations
    + translation_scaffold_can_be_audited_cross_domain
    + unification_claim_needs_success_failure_table
```

Alternative:

```trace
alternative_next :=
  syntax_two_example_hostile_audit
  if:
    syntax_branch_needs_more_cooling_before_matrix
```

## 12. Final compression

```trace
Generative_Syntax_Two_Example_Consolidation_v0_1 :=
  examples := simple_External_Merge + Merge_vs_linear_order_contrast
  shared_test := syntax_profile_back_translation
  anti_flattening := Merge_not_generic_combination + syntactic_object_not_surface + hierarchy_not_linear_order
  status := INTERNAL_PROFILE_CANDIDATE + NATIVE_REVIEW_REQUIRED + TOY_STATUS_COOLED
  earned := two_internal_syntax_profile_probes + syntax_profile_translation_seed
  next := Four_Domain_Success_Failure_Matrix
  - validation
  - full_grammar
  - parser_claim
```

End.
