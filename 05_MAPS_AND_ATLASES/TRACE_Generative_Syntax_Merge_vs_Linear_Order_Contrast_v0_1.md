# TRACE Generative Syntax Merge vs Linear Order Contrast v0.1

Date: 2026-06-18
Status: second Generative Syntax worked example / toy schematic contrast profile / no formal derivation claim / no language-specific grammar claim / not validation / not proof / not grammar implementation / not operator promotion / not Kernel v0.3

## 0. Control header

This file follows:

- `TRACE_Generative_Syntax_Translation_Input_Packet_v0_1.md`
- `TRACE_Generative_Syntax_Simple_Merge_Worked_Example_v0_1.md`
- `TRACE_Generative_Syntax_First_Example_Toy_Status_Patch_v0_1.md`

It adds a second syntax profile only under the active toy-status gate.

It does not claim a formal derivation.

It does not claim a language-specific grammar.

It does not use judgment data.

It does not implement a parser.

```trace
Generative_Syntax_Merge_vs_Linear_Order_Contrast_v0_1 :=
  toy_Merge_profile
  vs
  toy_linear_order_profile
  + same_surface_sequence_different_structural_status
  + syntactic_object_vs_word_sequence_contrast
  + back_translation_test
  + loss_register
  - validation
  - full_grammar
  - grammar_implementation
```

## 1. Native contrast case

The toy contrast compares two records that can share a similar surface readout while differing in structural status.

```trace
native_contrast_case :=
  toy_syntax_scope
  + Merge_record:
      External_Merge(D_the, N_cat) -> SO1
  + Linear_record:
      linear_sequence([D_the, N_cat]) -> string_placeholder
```

Surface placeholder:

```trace
surface_placeholder := "the cat"
```

Boundary:

The surface placeholder is not the syntactic object. It is only used to test whether TRACE can preserve the distinction between hierarchical syntactic construction and linear sequence.

## 2. Native profile family

```trace
native_profile_family :=
  derivation_vs_linear_order_contrast_profile
```

Profile assignment:

```trace
Phi_Syntax:
  {toy_Merge_record, toy_linear_record}
  -> derivation_vs_linear_order_contrast_profile
```

Core distinction:

```trace
core_native_distinction :=
  Merge_record:
    lexical_items := [D_the, N_cat]
    + operation := External_Merge
    + output := SO1
    + hierarchy_profile := binary_branching_toy_structure
  Linear_record:
    lexical_items := [D_the, N_cat]
    + operation := linear_ordering_placeholder
    + output := surface_string_placeholder
    + hierarchy_profile := absent
```

Plain version:

The test is not whether the words look the same. The test is whether TRACE keeps the structural difference between a toy syntactic object and a linear word sequence.

## 3. Merge-side toy profile

```trace
Merge_profile :=
  lexical_items := [D_the, N_cat]
  operation_sequence := [External_Merge]
  syntactic_objects_built := [SO1]
  hierarchy_profile := binary_branching_toy_structure
  surface_readout := "the cat"
  label_status := unresolved
  feature_dependencies := not_modelled
  status := toy_operation_profile
```

## 4. Linear-order toy profile

```trace
Linear_profile :=
  lexical_items := [D_the, N_cat]
  operation_sequence := [linear_ordering_placeholder]
  syntactic_objects_built := none_claimed
  hierarchy_profile := absent
  surface_readout := "the cat"
  label_status := not_applicable
  feature_dependencies := not_modelled
  status := toy_linear_sequence_profile
```

This is not a claim that linear order is irrelevant to syntax. It only creates a contrast object for testing whether TRACE collapses hierarchy into sequence.

## 5. Contrast profile object

```trace
Syntax_contrast_profile_object :=
  toy_scope := true
  lexical_items_shared := [D_the, N_cat]
  surface_placeholder_shared := "the cat"
  Merge_profile := Merge_profile
  Linear_profile := Linear_profile
  contrast := hierarchy_present_vs_absent
  loss_register := L_Syntax_contrast
```

This is a contrast profile for translation testing, not a language-specific grammar claim.

## 6. TRACE-form mapping

```trace
TRACE_form(Generative_Syntax_Minimalist_Program) :=
  {S_Syntax, T_Syntax, C_Syntax, O_Syntax, K_Syntax, B_Syntax, I_Syntax}
```

Mapping:

```trace
S_Syntax := lexical_items_and_record_context
T_Syntax := External_Merge_vs_linear_ordering_placeholder
C_Syntax := structure_building_vs_sequence_recording
O_Syntax := shared_surface_readout_placeholder
K_Syntax := toy_scope_no_feature_calculus_no_judgment_data
B_Syntax := derivation_boundary_and_surface_readout_scope
I_Syntax := hierarchy_vs_linear_order_contrast_profile
```

## 7. Profile-preserving morphism instance

Using cooled morphism language:

```trace
m_Syntax_contrast:
  structured_native_syntax_contrast_record
  -> structured_TRACE_syntax_contrast_record
```

Read as candidate translation-map shape only.

Preservation target:

```trace
m_Syntax_contrast_preserves :=
  shared_lexical_items
  + shared_surface_placeholder
  + Merge_record_has_External_Merge_operation
  + Merge_record_has_SO1_syntactic_object
  + Merge_record_has_hierarchy_profile
  + Linear_record_has_no_syntactic_object_claim
  + Linear_record_has_no_hierarchy_profile
  + label_gap_visible
  + feature_gap_visible
  + no_judgment_or_language_specific_claim
  + loss_register
```

## 8. Back-translation test

```trace
BT_Syntax(m_Syntax_contrast(toy_pair))
  ~=
  Merge_vs_linear_order_toy_contrast_under_declared_loss
```

Required recovery:

```trace
back_translation_recovery :=
  two_toy_records
  + shared_lexical_items_D_the_and_N_cat
  + shared_surface_placeholder
  + Merge_record_as_operation_built_SO1
  + Linear_record_as_sequence_without_syntactic_object_claim
  + hierarchy_present_in_Merge_record
  + hierarchy_absent_in_Linear_record
  + label_status_unresolved
  + feature_dependency_not_modelled
  + no_judgment_claim
  + loss_register
```

Failure:

```trace
back_translation_fails_if:
  translation_returns_only:
    the_words_are_the_same
  but_loses:
    operation_type_distinction
    + syntactic_object_status
    + hierarchy_contrast
    + toy_status
    + loss_register
```

## 9. Critical distinctions tested

### 9.1 Same surface placeholder does not imply same syntactic profile

```trace
same_surface_different_profile_test :=
  Merge_profile.surface_readout == Linear_profile.surface_readout
  but:
    Merge_profile.hierarchy_profile := present
    + Linear_profile.hierarchy_profile := absent
```

Failure:

```trace
failure :=
  both_profiles_flattened_to_surface_string
```

### 9.2 Merge operation matters

```trace
Merge_operation_test :=
  External_Merge != linear_ordering_placeholder
```

Failure:

```trace
failure :=
  Merge_as_generic_combination_or_ordering
```

### 9.3 Syntactic object status matters

```trace
syntactic_object_status_test :=
  Merge_record.output := SO1
  Linear_record.output := surface_string_placeholder
  distinction := syntactic_object_status_differs
```

Failure:

```trace
failure :=
  SO1_reduced_to_surface_string
```

### 9.4 Toy boundary remains active

```trace
toy_boundary_test :=
  both_profiles := toy_translation_profiles
  not:
    language_specific_grammar
    OR judgment_claim
    OR parser_output
```

Failure:

```trace
failure :=
  toy_contrast_read_as_grammar_or_parser_claim
```

## 10. Loss register

```trace
L_Syntax_contrast :=
  toy_two_record_contrast_only
  + no_formal_Merge_definition
  + no_label_theory
  + no_feature_calculus
  + no_Agree_or_Internal_Merge
  + no_judgment_dataset
  + no_parser_or_generation_algorithm
  + no_language_specific_claim
  + no_cross_linguistic_claim
```

Loss effects:

```trace
loss_effects :=
  no_formal_Merge_definition -> no_formal_derivation_claim
  + no_label_theory -> no_phrase_category_claim
  + no_feature_calculus -> no_feature_dependency_claim
  + no_judgment_data -> no_grammaticality_claim
  + no_parser -> no_implementation_claim
  + toy_records -> no_language_specific_grammar_claim
```

## 11. What this earns

```trace
earned_claim :=
  TRACE_can_preserve_one_toy_syntax_contrast_internally
  + same_surface_placeholder_can_coexist_with_different_structural_profiles
  + Merge_vs_linear_order_is_translation_testable
  + syntactic_object_status_is_translation_testable
  + hierarchy_flattening_is_blocked
  - full_grammar
  - formal_derivation_claim
  - parser_claim
  - validation
```

## 12. What remains untested

```trace
not_tested :=
  source_backed_Minimalist_formalism
  + labelled_tree_analysis
  + feature_checking_or_valuation
  + Agree
  + Internal_Merge_or_movement
  + copy_theory
  + phase_theory
  + interface_mapping
  + judgment_data
  + parser_or_grammar_implementation
  + specialist_review
```

## 13. Next step

```trace
recommended_next :=
  syntax_two_example_consolidation
  because:
    branch_now_has_two_syntax_profiles
    + contrast_matrix_can_be_defined
    + four_domain_matrix_waits_on_syntax_consolidation
```

Alternative:

```trace
alternative_next :=
  syntax_second_example_hostile_audit
  if:
    surface_placeholder_risk_or_Merge_language_risk_needs_more_cooling
```

## 14. Final compression

```trace
Generative_Syntax_Merge_vs_Linear_Order_Contrast_v0_1 :=
  profiles := Merge_profile + Linear_profile
  distinction := same_surface_placeholder_different_structural_status
  success := recover_operation_type + syntactic_object_status + hierarchy_contrast
  failure := surface_string_only_or_generic_combination
  status := INTERNAL_PROFILE_CANDIDATE + NATIVE_REVIEW_REQUIRED + TOY_STATUS_COOLED
  next := syntax_two_example_consolidation
  - validation
  - full_grammar
  - parser_claim
```

End.
