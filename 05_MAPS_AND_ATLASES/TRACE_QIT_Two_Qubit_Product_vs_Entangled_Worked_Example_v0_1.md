# TRACE QIT Two-Qubit Product vs Entangled Worked Example v0.1

Date: 2026-06-18
Status: worked mathematical translation example / QIT deep path / not validation / not proof / not QIT theory / not operator promotion / not Kernel v0.3

## 0. Control header

This file follows `TRACE_QIT_Form_Skeleton_v0_1.md`.

It tests whether TRACE can preserve tensor composition and nonseparability in a simple two-qubit example.

It does not claim TRACE unifies QIT.

It does not replace QIT, quantum mechanics, or specialist mathematics.

```trace
worked_example :=
  two_qubit_product_state
  vs
  two_qubit_entangled_state
  -> test:
      tensor_composition_preserved?
      + separability_distinction_preserved?
      + back_translation_possible?
  - validation
  - completed_unification
```

## 1. Native QIT objects

Let the one-qubit computational basis be:

```text
|0>, |1>
```

Two-qubit Hilbert space:

```text
H_AB = H_A tensor H_B
```

A product state example:

```text
|psi_product> = |0>_A tensor |0>_B = |00>
```

A Bell-state entangled example:

```text
|Phi_plus> = (|00> + |11>) / sqrt(2)
```

Boundary:

These are simple finite-dimensional examples. They are used to test translation structure, not to present a full QIT account.

## 2. TRACE-form mapping

From the QIT skeleton:

```trace
TRACE_form(QIT) :=
  {S_Q, T_Q, C_Q, O_Q, K_Q, B_Q, I_Q}
```

For this example:

```trace
S_Q := two_qubit_state
T_Q := identity_or_measurement_context_for_this_example
C_Q := tensor_product
O_Q := computational_basis_measurement_if_measured
K_Q := Hilbert_space_and_normalisation_constraints
B_Q := subsystem_split_A_B
I_Q := separability_or_entanglement_status
```

## 3. Product-state translation

Native form:

```text
|psi_product> = |0>_A tensor |0>_B
```

TRACE translation:

```trace
product_state_translation :=
  state := |00>
  composition := tensor_product_of_subsystem_states
  separability := true
  subsystem_description_possible := true
```

Back-translation test:

```trace
product_back_translation_test :=
  TRACE_state
  -> recover:
      |psi_product> = |0>_A tensor |0>_B
      + independent_subsystem_description
```

Failure if flattened:

```trace
product_translation_fails_if:
  tensor_product_is_treated_as_plain_pairing_only
  OR subsystem_structure_is_lost
```

## 4. Entangled-state translation

Native form:

```text
|Phi_plus> = (|00> + |11>) / sqrt(2)
```

TRACE translation:

```trace
entangled_state_translation :=
  state := |Phi_plus>
  composition := state_in_tensor_product_space
  separability := false
  subsystem_description_as_independent_pure_states := false
  correlation_structure := nonseparable_joint_state
```

Back-translation test:

```trace
entangled_back_translation_test :=
  TRACE_state
  -> recover:
      |Phi_plus> = (|00> + |11>) / sqrt(2)
      + cannot_factor_as |a>_A tensor |b>_B
```

Failure if flattened:

```trace
entangled_translation_fails_if:
  entanglement_is_translated_as_strong_correlation_only
  OR joint_state_is_treated_as_sum_of_two_independent_states
  OR tensor_product_space_is_lost
```

## 5. Critical distinction

Both states live in the same composite space.

```trace
same_space :=
  |00>
  and
  |Phi_plus>
  live_in:
    H_A tensor H_B
```

But they differ in separability.

```trace
critical_distinction :=
  product_state:
    factorable_as_subsystem_states
  entangled_state:
    not_factorable_as_independent_subsystem_states
```

Plain version:

The important TRACE lesson is not “things are connected”. That is too weak. The important distinction is whether the joint state can be decomposed into independent subsystem states.

## 6. What this tests in TRACE

This example pressures three TRACE assumptions.

```trace
TRACE_pressure_tests :=
  composition_is_not_always_aggregation
  + whole_state_may_not_reduce_to_parts
  + subsystem_boundary_does_not_guarantee_independent_state
```

This does not mean human subjects or institutions are quantum systems. It means TRACE must preserve the formal distinction between aggregation and nonseparable composition when translating domains.

## 7. Back-translation checklist

A successful TRACE translation must recover:

```trace
back_translation_checklist :=
  Hilbert_space_composite
  + tensor_product_composition
  + product_state_factorability
  + entangled_state_nonfactorability
  + distinction_between_joint_state_and_subsystem_description
```

If the translation cannot recover these, it is only metaphor.

## 8. Minimal formal discriminator

For a pure two-qubit state:

```text
|psi> = a|00> + b|01> + c|10> + d|11>
```

A separability condition can be expressed by:

```text
ad - bc = 0
```

For `|00>`:

```text
a = 1, b = 0, c = 0, d = 0
ad - bc = 0
```

For `|Phi_plus>`:

```text
a = 1/sqrt(2), b = 0, c = 0, d = 1/sqrt(2)
ad - bc = 1/2
```

TRACE use:

```trace
separability_discriminator :=
  product_if ad_minus_bc = 0
  entangled_if ad_minus_bc != 0
  for_pure_two_qubit_state
```

Boundary:

This is a simple pure-state two-qubit discriminator, not a general entanglement theory.

## 9. What this earns

```trace
earned_claim :=
  TRACE_can_preserve_one_QIT_composition_distinction
  + tensor_composition_vs_aggregation_failure_is_visible
  + back_translation_test_is_nontrivial
  - QIT_unified
  - general_entanglement_theory
```

## 10. Next step

The next QIT step should test observation.

```trace
next :=
  measure_product_vs_entangled_state_in_computational_basis
  and_track:
    outcome_probabilities
    + record
    + post_measurement_state_boundary
```

Reason:

```trace
reason :=
  current_example_tests_composition
  next_example_should_test_observation_and_record
```

## 11. Final compression

```trace
Two_Qubit_Product_vs_Entangled_v0_1 :=
  product_state := |00>
  entangled_state := (|00> + |11>) / sqrt(2)
  shared_space := H_A tensor H_B
  distinction := factorable_vs_nonfactorable
  discriminator := ad_minus_bc
  success := recover_tensor_product_and_separability_distinction
  failure := entanglement_as_metaphor_or_correlation_only
  next := measurement_and_record_example
  - validation
  - completed_unification
```

End.
