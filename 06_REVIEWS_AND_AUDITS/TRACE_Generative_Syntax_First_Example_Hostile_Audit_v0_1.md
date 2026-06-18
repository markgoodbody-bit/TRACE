# TRACE Generative Syntax First Example Hostile Audit v0.1

Date: 2026-06-18
Status: hostile audit / simple Merge toy-profile pressure / not validation / not proof / not linguistic theory / not full Minimalist grammar / not grammar implementation / not operator promotion / not Kernel v0.3

## 0. Audit identity and limits

```text
Reviewer identity: Framework hostile self-audit
Scope: Generative Syntax simple Merge toy profile only
Files audited:
  - TRACE_Generative_Syntax_Translation_Input_Packet_v0_1.md
  - TRACE_Generative_Syntax_Simple_Merge_Worked_Example_v0_1.md
External sources used: none in this audit
Specialist linguistic review: absent
Confidence: limited
```

This audit attacks whether the simple Merge example has accidentally created the appearance of a formal Minimalist derivation, grammar, parser, or syntactic theory.

```trace
audit_question :=
  does_simple_Merge_example_preserve_native_syntax_roles
  OR merely_make_two_words_sound_formal?
```

## 1. Verdict

VERDICT: `retain_but_patch_before_second_syntax_example`

```trace
verdict :=
  retain_simple_Merge_example
  because:
    it_blocks_Merge_as_generic_combination
    + it_names_syntactic_object_vs_surface_string
    + it_preserves_hierarchy_vs_linear_order
    + it_keeps_feature_dependency_absence_visible
  but:
    Merge_language_can_sound_formally_handled
    + label_status_is_unresolved
    + no_feature_system_exists
    + no_grammaticality_judgments_exist
    + surface_readout_can_be_misread_as_full_syntax
```

Plain verdict:

Keep it. It is a useful syntax translation probe. But before a second syntax example, add a toy-status/term-status patch that prevents this from reading like a formal Minimalist derivation or grammar fragment.

## 2. Main risk: Merge as fully formalised

The worked example uses `External_Merge(D_the, N_cat) -> SO1`. That is useful, but it can sound like the operation has been formally defined and theoretically grounded.

```trace
Merge_overclaim_risk :=
  External_Merge_notation
  + syntactic_object_output
  -> apparent_formal_derivation
```

Patch required:

```trace
patch_Merge_status :=
  External_Merge := toy_operation_label_for_translation_probe
  not:
    fully_formalised_Minimalist_operation
    OR source_backed_definition
    OR grammar_rule
    OR implemented_derivation_step
```

## 3. Surface readout risk

The example uses the surface readout placeholder `"the cat"`. Readers may treat this as the actual object of analysis, collapsing the syntactic object into a string.

```trace
surface_readout_risk :=
  surface_string_present
  -> syntactic_object_collapses_to_words_in_order
```

Patch required:

```trace
patch_surface_status :=
  surface_readout := interface_placeholder
  not:
    syntactic_object_itself
    OR full_derivation
    OR grammaticality_claim
    OR English_DP_analysis
```

## 4. Label/head status unresolved

The worked example explicitly leaves head/label status unresolved. This is good, but it must remain status-affecting.

```trace
label_gap :=
  head_or_label_status := unresolved_in_this_probe
```

Consequence:

```trace
label_gap_consequence :=
  no_labelling_theory_claim
  + no_phrase_category_claim
  + no_complete_syntactic_object_theory
```

Patch required:

```trace
patch_label_status :=
  label_status_unresolved
  must_demote:
    phrase_category_claim
    + head_projection_claim
    + full_derivation_claim
```

## 5. Feature dependency gap

The example marks `feature_dependencies := not_modelled`. This is essential. But a syntax example with lexical items and Merge can easily invite an implicit feature story.

```trace
feature_dependency_risk :=
  D_the
  + N_cat
  + Merge
  may_invite:
    hidden_feature_checking_story
```

Patch required:

```trace
patch_feature_dependency_status :=
  feature_dependencies := not_modelled_gap
  not:
    checked
    OR valued
    OR preserved
    OR solved
```

## 6. Grammaticality and acceptability absent

The example does not use native-speaker judgments or grammaticality data. It cannot claim the string is grammatical, acceptable, or representative of English grammar.

```trace
grammaticality_gap :=
  no_judgment_dataset
  + no_acceptability_claim
  + no_language_specific_source
```

Patch required:

```trace
patch_grammaticality_status :=
  no_grammaticality_claim
  + no_acceptability_claim
  + no_English_grammar_claim
```

## 7. Hierarchy distinction works, but is fragile

Strength:

```trace
strength :=
  SO1_not_surface_string
  + binary_branching_toy_structure_named
```

Weakness:

The hierarchy is only named, not formally represented by a full tree, labelling algorithm, or derivational system.

```trace
hierarchy_gap :=
  hierarchy_profile_named
  but:
    formal_tree_theory_absent
    + labelling_absent
    + feature_relations_absent
```

Patch required:

```trace
patch_hierarchy_status :=
  hierarchy_profile := toy_binary_branching_placeholder
  not:
    full_phrase_structure_theory
    OR labelled_tree_claim
```

## 8. Back-translation is strongest feature

The back-translation target is the strongest part of the example because it requires recovery of:

```trace
strongest_feature :=
  toy_scope
  + lexical_items
  + External_Merge_operation
  + SO1
  + hierarchy_profile
  + surface_readout_as_placeholder
  + no_feature_dependency_claim
  + loss_register
```

Retain this. It prevents the example collapsing into “the words were combined.”

## 9. Loss register pass, but must affect claims

The loss register names missing labelling theory, feature calculus, Agree/Internal Merge, judgments, parser, and cross-linguistic claims.

Strength:

```trace
loss_register_strength :=
  missing_native_syntax_structure_visible
```

Patch required:

```trace
loss_register_required_effect :=
  no_label_theory -> no_phrase_category_claim
  + no_feature_calculus -> no_feature_dependency_claim
  + no_judgment_data -> no_grammaticality_claim
  + no_parser -> no_implementation_claim
  + no_cross_linguistic_data -> no_general_language_claim
```

## 10. Required patch before second syntax example

```trace
required_patch_before_second_syntax_example :=
  Merge_status_patch
  + surface_readout_status_patch
  + label_gap_patch
  + feature_dependency_gap_patch
  + grammaticality_status_patch
  + hierarchy_status_patch
  + loss_register_claim_effects
```

Minimal acceptable patch file:

```trace
Syntax_First_Example_Toy_Status_Patch_v0_1 :=
  Merge_not_fully_formalised
  + surface_readout_not_syntactic_object
  + label_status_unresolved
  + feature_dependency_gap_visible
  + no_grammaticality_or_English_grammar_claim
```

## 11. Audit result

```trace
audit_result :=
  retain_simple_Merge_example
  + patch_toy_status_before_second_syntax_example
  + do_not_delete
  + do_not_promote
  + do_not_add_second_syntax_example_until_patch
  - validation
  - full_Minimalist_grammar
  - grammar_implementation
  - English_grammar_claim
```

Plain result:

The first syntax worked example is useful because it tests Merge vs generic combination and syntactic object vs surface string. But it needs a toy-status patch before expansion because the notation can sound like formal syntax has been solved.

## 12. Final compression

```trace
Syntax_First_Example_Hostile_Audit_v0_1 :=
  verdict := retain_but_patch_before_second_syntax_example
  strengths := Merge_test + SO1_not_string + hierarchy_named + back_translation
  weaknesses := Merge_too_hot + label_unresolved + no_features + no_judgments + surface_string_leak
  required_patch := Syntax_First_Example_Toy_Status_Patch_v0_1
  next := toy_status_patch_before_second_syntax_example
  - validation
  - full_Minimalist_grammar
  - grammar_implementation
```

End.
