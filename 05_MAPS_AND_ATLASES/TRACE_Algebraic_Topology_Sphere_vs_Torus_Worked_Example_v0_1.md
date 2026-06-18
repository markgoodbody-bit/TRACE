# TRACE Algebraic Topology Sphere vs Torus Worked Example v0.1

Date: 2026-06-18
Status: second topology worked example / internal translation probe / source-gap visible / not validation / not proof / not topology theory / not operator promotion / not Kernel v0.3

## 0. Control header

This file follows:

- `TRACE_Translation_Success_Protocol_v0_1.md`
- `TRACE_Algebraic_Topology_Translation_Input_Packet_v0_1.md`
- `TRACE_Algebraic_Topology_First_Example_Term_Precision_Patch_v0_1.md`

It expands the topology branch outward after the first example was cooled and term-patched.

It does not claim TRACE unifies Algebraic Topology.

It does not replace Algebraic Topology or specialist mathematics.

```trace
sphere_vs_torus_worked_example :=
  S2
  vs
  T2
  -> test:
      richer_invariant_profile_preserved?
      + first_homology_contrast_preserved?
      + surface_class_distinction_preserved?
      + back_translation_possible?
  - validation
  - completed_unification
```

## 1. New example scope

```trace
new_example_scope :=
  sphere_S2
  vs
  torus_T2
  under:
    simplified_homology_style_translation_probe
```

Source gap remains:

```trace
source_gap :=
  no_external_topology_sources_in_files
  + no_specialist_review
  + notation_simplified_for_internal_probe
```

Boundary:

This is not a full algebraic topology account. It is a second internal probe of TRACE translation behaviour.

## 2. Native objects

First object:

```text
S2 := 2-sphere / surface of a ball
```

Second object:

```text
T2 := 2-torus / surface of a doughnut shape
```

Working contrast:

```trace
native_contrast :=
  S2:
    closed_surface
    + no_independent_1_dimensional_loop_holes
    + one_surface_class_in_simplified_H2_language
  T2:
    closed_surface
    + two_independent_1_dimensional_loop_directions
    + one_surface_class_in_simplified_H2_language
```

Plain version:

Both are closed surfaces in this simplified probe, but the torus has two independent 1-dimensional loop directions while the sphere does not.

## 3. TRACE-form target

```trace
TRACE_form(Algebraic_Topology) :=
  {S_Top, T_Top, C_Top, O_Top, K_Top, B_Top, I_Top}
```

For this example:

```trace
S_Top := S2_or_T2_as_topological_surface
T_Top := allowed_continuous_deformation_or_invariant_assignment_context
C_Top := surface_construction_or_product_context_not_primary
O_Top := simplified_homology_style_invariant_assignment
K_Top := continuity_and_homology_equivalence_constraints
B_Top := scope_of_surface_and_cycle_boundary_context
I_Top := Betti_profile_contrast
```

## 4. Term precision carried forward

The first topology patch remains active.

```trace
term_precision_active :=
  topological_boundary_of_space
  != chain_boundary_under_boundary_operator
  != TRACE_boundary_role_B_Top
```

In this file, `boundary` language is kept minimal because both objects are treated as closed surfaces in the simplified probe.

`beta_n` language remains cooled:

```trace
Betti_scope_note :=
  beta_n_used_as_simplified_rank_style_language
  + coefficient_context_not_handled
  + formal_group_calculation_not_provided
  + specialist_review_absent
```

## 5. Sphere translation

Native object:

```text
S2
```

Simplified homology-style profile:

```text
β0(S2) = 1
β1(S2) = 0
β2(S2) = 1
```

TRACE translation:

```trace
sphere_translation :=
  space := S2
  connected_components := one
  independent_1_cycles := zero
  surface_class := one_simplified_2_dimensional_feature
  invariant_profile := beta_profile_1_0_1
```

Back-translation test:

```trace
sphere_back_translation_test :=
  TRACE_topology_form
  -> recover:
      S2
      + connected_surface
      + no_independent_1_dimensional_loop_holes
      + beta_1_equals_0_in_simplified_probe
      + beta_2_equals_1_in_simplified_probe
```

Failure if flattened:

```trace
sphere_translation_fails_if:
  sphere_is_only_visual_roundness
  OR beta_1_zero_is_lost
  OR 2_dimensional_surface_feature_is_not_recoverable
```

## 6. Torus translation

Native object:

```text
T2
```

Simplified homology-style profile:

```text
β0(T2) = 1
β1(T2) = 2
β2(T2) = 1
```

TRACE translation:

```trace
torus_translation :=
  space := T2
  connected_components := one
  independent_1_cycles := two
  surface_class := one_simplified_2_dimensional_feature
  invariant_profile := beta_profile_1_2_1
```

Back-translation test:

```trace
torus_back_translation_test :=
  TRACE_topology_form
  -> recover:
      T2
      + connected_surface
      + two_independent_1_dimensional_loop_directions
      + beta_1_equals_2_in_simplified_probe
      + beta_2_equals_1_in_simplified_probe
```

Failure if flattened:

```trace
torus_translation_fails_if:
  torus_hole_is_only_visual_doughnut_hole
  OR two_independent_loop_directions_are_not_recoverable
  OR beta_profile_contrast_is_lost
```

## 7. Critical distinction

The sphere and torus are both closed surfaces in this simplified probe. Their key contrast is not merely visual.

```trace
critical_distinction :=
  S2:
    beta_profile := (1,0,1)
    + no_independent_1_cycles
  T2:
    beta_profile := (1,2,1)
    + two_independent_1_cycles
```

Plain version:

The torus is not just a sphere with a visible hole. In the simplified homology-style probe, it has a different invariant profile, especially two independent 1-dimensional loop directions.

## 8. What this tests in TRACE

```trace
TRACE_pressure_tests :=
  richer_invariant_profile_not_visual_shape
  + one_hole_picture_not_enough_for_torus
  + same_connectedness_does_not_mean_same_topology
  + beta_profile_preservation_required_for_back_translation
```

This does not mean social or ethical cases are topological spaces. It means TRACE must preserve invariant profile differences when translating topology.

## 9. Back-translation checklist

A successful TRACE translation must recover:

```trace
back_translation_checklist :=
  S2_as_sphere_surface
  + T2_as_torus_surface
  + both_have_one_connected_component_in_probe
  + beta_1_S2_equals_0
  + beta_1_T2_equals_2
  + beta_2_both_equal_1_in_probe
  + torus_two_loop_directions_not_visual_hole_only
  + beta_profile_contrast
```

If the translation cannot recover these, it is only metaphor.

## 10. Minimal contrast table

| Object | Simplified profile | TRACE role | Failure if flattened |
|---|---|---|---|
| `S2` | `β0=1`, `β1=0`, `β2=1` | connected closed surface with no independent 1-loops | sphere as visual roundness only |
| `T2` | `β0=1`, `β1=2`, `β2=1` | connected closed surface with two independent 1-loops | torus as visual doughnut only |
| contrast | `(1,0,1)` vs `(1,2,1)` | invariant profile distinction | hole as ordinary picture |

## 11. Loss ledger

### 11.1 Simplified Betti profile only

```trace
loss_entry_1 :=
  source_feature := formal_homology_groups
  -> TRACE_translation := simplified_Betti_profile
  -> loss_or_distortion := group_calculation_and_coefficient_context_excluded
  -> consequence_for_back_translation := only_rank_style_profile_contrast_recovered
```

### 11.2 No explicit chain calculation

```trace
loss_entry_2 :=
  source_feature := chain_complex_boundary_operator_calculation
  -> TRACE_translation := invariant_profile_language
  -> loss_or_distortion := no_chain_level_proof
  -> consequence_for_back_translation := cannot_claim_formal_computation_capacity
```

### 11.3 No classification theorem

```trace
loss_entry_3 :=
  source_feature := surface_classification_and_homeomorphism_theory
  -> TRACE_translation := sphere_vs_torus_contrast_only
  -> loss_or_distortion := no_general_surface_classification
  -> consequence_for_back_translation := cannot_claim_general_closed_surface_coverage
```

### 11.4 No functor/category treatment

```trace
loss_entry_4 :=
  source_feature := functorial_homology_structure
  -> TRACE_translation := invariant_assignment_language
  -> loss_or_distortion := functoriality_and_naturality_excluded
  -> consequence_for_back_translation := no_category_theoretic_bridge_claim
```

## 12. What this earns

```trace
earned_claim :=
  TRACE_can_preserve_second_topology_invariant_contrast_internally
  + beta_profile_back_translation_is_testable
  + visual_hole_flattening_is_again_blocked
  + topology_branch_expands_beyond_S1_vs_D2
  - topology_unified
  - formal_homology_calculation_capacity
  - source_grounded_claim
```

## 13. What remains untested

```trace
not_tested :=
  formal_homology_group_derivation
  + coefficient_dependence
  + cohomology_ring_structure
  + fundamental_group
  + exact_sequences
  + orientability_cases_beyond_S2_T2
  + higher_genus_surfaces
  + functoriality
  + classification_theorems
```

Boundary:

Do not infer general Algebraic Topology success from this example.

## 14. Next step

```trace
recommended_next :=
  topology_two_example_consolidation
  with:
    circle_vs_disk
    + sphere_vs_torus
    + common_success_failure_matrix
    + source_gap_retained
```

Alternative:

```trace
alternative_next :=
  hostile_audit_sphere_vs_torus_first
```

## 15. Final compression

```trace
Sphere_vs_Torus_Worked_Example_v0_1 :=
  S2_profile := (1,0,1)
  T2_profile := (1,2,1)
  distinction := beta_profile_and_independent_1_cycles
  success := recover_invariant_profile_contrast
  failure := visual_hole_or_shape_only
  next := topology_two_example_consolidation_or_hostile_audit
  - validation
  - topology_unification
  - formal_homology_calculation_claim
```

End.
