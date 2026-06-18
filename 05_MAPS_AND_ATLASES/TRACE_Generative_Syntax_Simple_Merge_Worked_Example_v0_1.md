# TRACE Generative Syntax Simple Merge Worked Example v0.1

Date: 2026-06-18
Status: first Generative Syntax worked example / toy schematic Merge probe / not validation / not proof / not linguistic theory / not grammar implementation / not operator promotion / not Kernel v0.3

## 0. Control header

This file follows:

- `TRACE_Generative_Syntax_Translation_Input_Packet_v0_1.md`
- `TRACE_Generic_Invariant_Profile_Translation_Template_v0_1.md`
- `TRACE_Profile_Morphism_Formal_Status_Patch_v0_1.md`

This is a toy/schematic worked example.

It is not a full Minimalist grammar.

It does not use source-backed syntactic judgments.

It does not implement a parser.

It does not claim a theory of English or any other language.

```trace
Generative_Syntax_Simple_Merge_Worked_Example_v0_1 :=
  toy_lexical_items
  + External_Merge_step
  + syntactic_object_profile
  + hierarchy_not_surface_string
  + back_translation_test
  + loss_register
  - validation
  - full_Minimalist_grammar
  - grammar_implementation
```

## 1. Native case

The toy case uses two lexical items and one External Merge operation.

```trace
native_case :=
  toy_syntax_scope
  + lexical_items := {D_the, N_cat}
  + operation := External_Merge(D_the, N_cat)
  + output := syntactic_object_SO1
```

Surface readout placeholder:

```trace
surface_readout_placeholder :=
  "the cat"
```

Boundary:

The surface readout is included only to test the distinction between a surface string and a syntactic object. It is not a full account of English determiner phrase syntax.

## 2. Native roles

```trace
native_roles :=
  lexical_item:
    D_the
    + N_cat
  operation:
    External_Merge
  syntactic_object:
    SO1 := {D_the, N_cat}
  hierarchy_profile:
    binary_branching_toy_structure
  interface_readout:
    surface_readout_placeholder
```

Plain version:

The important structure is not just the two-word string `the cat`. The toy syntactic object records selected items, operation, and hierarchy.

## 3. Operation profile

```trace
operation_sequence :=
  step_1:
    External_Merge(D_the, N_cat)
    -> SO1
```

Toy structural notation:

```trace
SO1 :=
  {
    head_or_label_status := unresolved_in_this_probe,
    daughters := [D_the, N_cat],
    operation := External_Merge,
    surface_readout := "the cat"
  }
```

Head/label status is deliberately unresolved. The probe tests translation of Merge and hierarchy, not a specific labelling theory.

## 4. Native profile assignment

```trace
Phi_Syntax:
  toy_Merge_case
  -> derivation_feature_dependency_profile
```

Profile value:

```trace
P_Syntax(toy_Merge_case) :=
  {
    lexical_items := [D_the, N_cat],
    operations := [External_Merge],
    syntactic_objects_built := [SO1],
    hierarchy_profile := binary_branching_toy_structure,
    surface_readout := "the cat",
    feature_dependencies := not_modelled,
    displacement_status := none_in_this_probe,
    label_status := unresolved
  }
```

This is a profile object for translation testing. It is not a full syntactic derivation.

## 5. TRACE-form mapping

```trace
TRACE_form(Generative_Syntax_Minimalist_Program) :=
  {S_Syntax, T_Syntax, C_Syntax, O_Syntax, K_Syntax, B_Syntax, I_Syntax}
```

Mapping:

```trace
S_Syntax := lexical_items_and_syntactic_object_context
T_Syntax := External_Merge_operation
C_Syntax := one_step_structure_building
O_Syntax := surface_readout_placeholder
K_Syntax := toy_scope_no_feature_calculus_no_judgment_data
B_Syntax := derivation_boundary_one_step_probe_and_interface_scope
I_Syntax := derivation_feature_dependency_profile
```

## 6. Profile-preserving morphism instance

Using cooled morphism language:

```trace
m_Syntax:
  structured_native_syntax_profile_record
  -> structured_TRACE_syntax_profile_record
```

Read as candidate translation-map shape only.

```trace
m_Syntax(toy_Merge_case)
  preserves:
    lexical_item_identity
    + External_Merge_operation
    + syntactic_object_SO1
    + hierarchy_profile
    + surface_readout_as_interface_placeholder
    + no_feature_dependency_claim
    + no_full_grammar_claim
    + loss_register
```

Loss register:

```trace
L_Syntax :=
  toy_one_step_Merge_only
  + no_formal_label_theory
  + no_feature_calculus
  + no_Agree_or_Internal_Merge
  + no_grammaticality_judgment_dataset
  + no_parser_or_generation_algorithm
  + no_cross_linguistic_claim
```

## 7. Back-translation test

A successful translation must reconstruct the native syntax case.

```trace
BT_Syntax(m_Syntax(toy_Merge_case))
  ~=
  toy_Merge_case_under_declared_loss
```

Required recovery:

```trace
back_translation_recovery :=
  toy_syntax_scope
  + lexical_items_D_the_and_N_cat
  + External_Merge_operation
  + syntactic_object_SO1
  + hierarchy_profile_binary_branching_toy_structure
  + surface_readout_placeholder_not_full_derivation
  + no_feature_dependency_claim
  + no_full_grammar_claim
  + loss_register
```

Fail condition:

```trace
back_translation_fails_if:
  translation_returns_only:
    words_the_and_cat_combined
  but_loses:
    Merge_operation
    + syntactic_object_SO1
    + hierarchy_profile
    + toy_scope
    + loss_register
```

## 8. Critical distinctions preserved or not

### 8.1 Merge vs generic combination

```trace
Merge_test :=
  External_Merge(D_the, N_cat)
  -> SO1
  not:
    generic_combination
    OR word_adjacency_only
```

Failure:

```trace
failure :=
  Merge_read_as_putting_two_words_next_to_each_other
```

### 8.2 Syntactic object vs surface string

```trace
syntactic_object_test :=
  SO1 := operation_built_object
  surface_readout := "the cat"
  distinction := SO1 != surface_string_only
```

Failure:

```trace
failure :=
  syntactic_object_reduced_to_surface_string
```

### 8.3 Hierarchy vs linear order

```trace
hierarchy_test :=
  hierarchy_profile := binary_branching_toy_structure
  not:
    mere_linear_order
```

Failure:

```trace
failure :=
  hierarchy_erased_into_sequence_the_then_cat
```

### 8.4 Feature dependency absent, not silently preserved

```trace
feature_dependency_status :=
  not_modelled_in_this_probe
  not:
    preserved
    OR solved
    OR checked
```

Failure:

```trace
failure :=
  feature_dependency_claim_added_without_native_structure
```

## 9. Flattening risks blocked

```trace
blocked_flattening :=
  Merge_as_generic_combination
  + syntax_as_word_order_only
  + syntactic_object_as_surface_string
  + hierarchy_as_tree_picture_only
  + feature_as_semantic_label
  + grammaticality_as_truth_or_style
```

Still not solved:

```trace
not_solved :=
  full_Minimalist_derivation
  + labelling_theory
  + feature_checking
  + Agree
  + Internal_Merge
  + phases
  + Spell_Out
  + PF_LF_mapping
  + grammaticality_judgments
  + parser_or_grammar_implementation
```

## 10. What this earns

```trace
earned_claim :=
  TRACE_can_preserve_one_toy_External_Merge_profile_internally
  + Merge_vs_generic_combination_is_translation_testable
  + syntactic_object_vs_surface_string_is_translation_testable
  + hierarchy_vs_linear_order_is_translation_testable
  + feature_dependency_absence_is_visible
  - full_Minimalist_grammar
  - grammar_implementation
  - validation
```

## 11. What remains untested

```trace
not_tested :=
  source_backed_Minimalist_formalism
  + labelling_algorithm
  + feature_checking_or_valuation
  + Agree
  + Internal_Merge_or_movement
  + copy_theory
  + phase_theory
  + Spell_Out
  + PF_LF_interface_mapping
  + native_speaker_judgment_data
  + cross_linguistic_variation
  + implemented_parser
  + specialist_review
```

## 12. Next step

```trace
recommended_next :=
  syntax_first_example_cooling_or_hostile_audit
  because:
    Merge_language_can_overclaim
    + surface_readout_can_be_misread_as_full_syntax
    + feature_dependencies_are_not_modelled
```

Alternative:

```trace
alternative_next :=
  syntax_two_example_contrast
  only_after:
    cooling_or_audit
```

## 13. Final compression

```trace
Generative_Syntax_Simple_Merge_Worked_Example_v0_1 :=
  case := External_Merge(D_the,N_cat)
  output := SO1
  profile := lexical_items + operation + syntactic_object + hierarchy + surface_readout_placeholder
  success := recover_Merge_operation_and_syntactic_object_not_surface_string
  failure := words_combined_only
  status := INTERNAL_PROFILE_CANDIDATE + NATIVE_REVIEW_REQUIRED + TOY_STATUS_REQUIRED
  next := cooling_or_hostile_audit
  - validation
  - full_Minimalist_grammar
  - grammar_implementation
```

End.
