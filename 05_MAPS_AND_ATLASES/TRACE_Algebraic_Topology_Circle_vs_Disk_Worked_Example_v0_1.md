# TRACE Algebraic Topology Circle vs Disk Worked Example v0.1

Date: 2026-06-18
Status: worked mathematical translation example / Algebraic Topology first probe / not validation / not proof / not topology theory / not operator promotion / not Kernel v0.3

## 0. Control header

This file follows `TRACE_Algebraic_Topology_Translation_Input_Packet_v0_1.md`.

It tests whether TRACE can preserve the distinction between a circle and a disk under a simple homology-style translation.

It does not claim TRACE unifies Algebraic Topology.

It does not replace Algebraic Topology or specialist mathematics.

```trace
circle_vs_disk_worked_example :=
  S1
  vs
  D2
  -> test:
      cycle_boundary_distinction_preserved?
      + Betti_1_contrast_preserved?
      + invariant_not_visual_metaphor?
      + back_translation_possible?
  - validation
  - completed_unification
```

## 1. Native objects

First object:

```text
S1 := circle
```

Second object:

```text
D2 := disk
```

Working contrast:

```trace
native_contrast :=
  S1:
    closed_loop
    + one_independent_1_cycle
    + not_filled_inside_S1
  D2:
    filled_disk
    + boundary_circle_exists
    + loop_bounds_2_dimensional_region_inside_D2
```

Boundary:

This is a simple internal probe. It is not a full homology calculation account and uses simplified notation.

## 2. TRACE-form target

```trace
TRACE_form(Algebraic_Topology) :=
  {S_Top, T_Top, C_Top, O_Top, K_Top, B_Top, I_Top}
```

For this example:

```trace
S_Top := S1_or_D2_as_topological_space
T_Top := allowed_continuous_deformation_or_boundary_operator_context
C_Top := not_primary_except_space_construction_context
O_Top := homology_style_invariant_assignment
K_Top := continuity_and_homology_equivalence_constraints
B_Top := boundary_operator_cycle_boundary_distinction
I_Top := first_Betti_number_or_H1_contrast
```

## 3. Circle translation

Native object:

```text
S1
```

Simplified homology-style claim:

```text
H1(S1) ≅ Z
β1(S1) = 1
```

TRACE translation:

```trace
circle_translation :=
  space := S1
  cycle_status := one_independent_1_cycle
  boundary_status := not_boundary_of_2_chain_inside_S1
  invariant := beta_1_equals_1
  hole_language_status := formal_invariant_not_visual_metaphor
```

Back-translation test:

```trace
circle_back_translation_test :=
  TRACE_topology_form
  -> recover:
      S1
      + one_independent_1_dimensional_cycle
      + H1_like_nontriviality
      + beta_1_equals_1
```

Failure if flattened:

```trace
circle_translation_fails_if:
  circle_hole_is_only_visual_metaphor
  OR cycle_boundary_distinction_is_lost
  OR beta_1_contrast_is_not_recoverable
```

## 4. Disk translation

Native object:

```text
D2
```

Simplified homology-style claim:

```text
H1(D2) = 0
β1(D2) = 0
```

TRACE translation:

```trace
disk_translation :=
  space := D2
  boundary_circle_exists := true
  one_dimensional_hole_status := absent
  reason := boundary_loop_bounds_filled_2_dimensional_region
  invariant := beta_1_equals_0
```

Back-translation test:

```trace
disk_back_translation_test :=
  TRACE_topology_form
  -> recover:
      D2
      + filled_disk
      + no_independent_1_dimensional_hole
      + H1_like_triviality
      + beta_1_equals_0
```

Failure if flattened:

```trace
disk_translation_fails_if:
  disk_is_treated_as_circle_plus_colour_fill_only
  OR filled_region_role_is_lost
  OR boundary_vs_hole_distinction_is_lost
```

## 5. Critical distinction

The circle and disk are visually related, but the relevant distinction is formal.

```trace
critical_distinction :=
  S1:
    closed_1_cycle_not_filled_within_space
    -> beta_1 = 1
  D2:
    loop_bounds_filled_region_within_space
    -> beta_1 = 0
```

Plain version:

The important TRACE lesson is not “one has a hole and one does not” as a picture. The important distinction is whether the apparent loop is a non-boundary cycle or a boundary of a filled region in the space.

## 6. What this tests in TRACE

```trace
TRACE_pressure_tests :=
  invariant_is_not_visual_similarity
  + boundary_is_not_generic_edge
  + hole_is_not_metaphor_only
  + local_visual_relation_does_not_set_global_algebraic_structure
```

This does not mean social or ethical cases are topological spaces. It means TRACE must preserve the formal distinction between visual metaphor and invariant structure when translating topology.

## 7. Back-translation checklist

A successful TRACE translation must recover:

```trace
back_translation_checklist :=
  S1_as_circle_space
  + D2_as_filled_disk_space
  + cycle_vs_boundary_distinction
  + beta_1_S1_equals_1
  + beta_1_D2_equals_0
  + formal_invariant_not_visual_metaphor
```

If the translation cannot recover these, it is only metaphor.

## 8. Minimal contrast table

| Object | Simplified native contrast | TRACE role | Failure if flattened |
|---|---|---|---|
| `S1` | `H1(S1) ≅ Z`, `β1 = 1` | nontrivial 1-cycle / invariant survives | hole as picture only |
| `D2` | `H1(D2) = 0`, `β1 = 0` | filled region removes independent 1-hole | fill treated as cosmetic |
| contrast | cycle not boundary vs boundary of filled region | cycle/boundary distinction | boundary as generic edge |

## 9. What this earns

```trace
earned_claim :=
  TRACE_can_preserve_one_topology_invariant_distinction
  + hole_as_metaphor_failure_is_visible
  + cycle_boundary_distinction_is_translation_testable
  + back_translation_test_is_nontrivial
  - topology_unified
  - formal_homology_calculation_capacity
```

## 10. What remains untested

```trace
not_tested :=
  formal_chain_complex_calculation
  + higher_homology_groups
  + cohomology
  + exact_sequences
  + homotopy_groups
  + homeomorphism_vs_homotopy_vs_homology_equivalence
  + category_functor_formalism
```

Boundary:

Do not infer general Algebraic Topology success from this example.

## 11. Next step

The next topology step should test a second shape with a different invariant profile, or consolidate first.

Safer next:

```trace
next :=
  Topology_first_example_cooling_or_consolidation
  because:
    source_gap_exists
    + specialist_review_absent
    + formal_chain_details_simplified
```

Possible later worked example:

```trace
later_example :=
  sphere_vs_torus_invariant_contrast
  only_after:
    source_or_cooling_pass
```

## 12. Final compression

```trace
Circle_vs_Disk_Worked_Example_v0_1 :=
  S1 := beta_1_equals_1
  D2 := beta_1_equals_0
  distinction := nonboundary_cycle_vs_boundary_of_filled_region
  success := recover_cycle_boundary_invariant_structure
  failure := hole_as_metaphor_only
  next := topology_cooling_or_consolidation
  - validation
  - topology_unification
```

End.
