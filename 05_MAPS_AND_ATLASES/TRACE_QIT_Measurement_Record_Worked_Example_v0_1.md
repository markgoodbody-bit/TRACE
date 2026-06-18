# TRACE QIT Measurement and Record Worked Example v0.1

Date: 2026-06-18
Status: worked mathematical translation example / QIT observation test / not validation / not proof / not QIT theory / not operator promotion / not Kernel v0.3

## 0. Control header

This file follows `TRACE_QIT_Two_Qubit_Product_vs_Entangled_Worked_Example_v0_1.md`.

The previous example tested composition and separability. This example tests observation, outcome probability, record, and post-measurement state in the computational basis.

It does not claim TRACE unifies QIT.

It does not replace QIT, quantum mechanics, or specialist mathematics.

```trace
measurement_record_example :=
  product_state_measurement
  vs
  entangled_state_measurement
  -> test:
      outcome_probabilities_preserved?
      + record_vs_state_distinction_preserved?
      + post_measurement_state_preserved?
      + back_translation_possible?
  - validation
  - completed_unification
```

## 1. Native objects

Product state:

```text
|psi_product> = |00>
```

Entangled Bell state:

```text
|Phi_plus> = (|00> + |11>) / sqrt(2)
```

Measurement basis:

```text
{|00>, |01>, |10>, |11>}
```

Boundary:

This file uses an ideal computational-basis projective measurement. It is not a general measurement theory.

## 2. TRACE-form target

```trace
TRACE_form(QIT) :=
  {S_Q, T_Q, C_Q, O_Q, K_Q, B_Q, I_Q}
```

For this worked example:

```trace
S_Q := pre_measurement_two_qubit_state
T_Q := measurement_update_if_measurement_occurs
C_Q := tensor_product_space
O_Q := computational_basis_measurement
K_Q := normalisation_and_projective_measurement_constraints
B_Q := pre_measurement_vs_post_measurement_boundary
I_Q := outcome_distribution_and_record_state_distinction
```

## 3. Product-state measurement

Native state:

```text
|psi_product> = |00>
```

Computational-basis outcome probabilities:

```text
P(00) = 1
P(01) = 0
P(10) = 0
P(11) = 0
```

Post-measurement state after outcome `00`:

```text
|00>
```

TRACE translation:

```trace
product_measurement_translation :=
  pre_state := |00>
  measurement_context := computational_basis
  outcome_distribution := {00:1, 01:0, 10:0, 11:0}
  record := 00
  post_state := |00>
```

Back-translation test:

```trace
product_measurement_back_translation :=
  TRACE_measurement_form
  -> recover:
      deterministic_00_outcome
      + product_state_preserved_under_this_measurement
      + record_matches_post_state_for_this_case
```

Failure if flattened:

```trace
product_measurement_translation_fails_if:
  record_00_is_treated_as_generic_label_without_probability
  OR measurement_context_is_lost
  OR post_state_is_not_distinguished_from_pre_state
```

## 4. Entangled-state measurement

Native state:

```text
|Phi_plus> = (|00> + |11>) / sqrt(2)
```

Computational-basis outcome probabilities:

```text
P(00) = 1/2
P(11) = 1/2
P(01) = 0
P(10) = 0
```

Post-measurement state:

```text
if record = 00, post_state = |00>
if record = 11, post_state = |11>
```

TRACE translation:

```trace
entangled_measurement_translation :=
  pre_state := |Phi_plus>
  measurement_context := computational_basis
  outcome_distribution := {00:1/2, 11:1/2, 01:0, 10:0}
  record := one_of {00,11}
  post_state := |00> OR |11> depending_on_record
  pre_state_not_recoverable_from_single_record := true
```

Back-translation test:

```trace
entangled_measurement_back_translation :=
  TRACE_measurement_form
  -> recover:
      pre_state_superposition
      + two_possible_records_00_or_11
      + perfect_joint_correlation_in_this_basis
      + post_state_depends_on_record
      + single_record_does_not_equal_full_pre_state
```

Failure if flattened:

```trace
entangled_measurement_translation_fails_if:
  Bell_state_is_treated_as_classical_mixture_only
  OR record_00_is_confused_with_original_pre_state
  OR measurement_context_is_lost
  OR correlation_is_described_without_joint_distribution
```

## 5. Critical distinction: record is not state

For the product case, the record `00` matches the deterministic state under this measurement context.

For the Bell case, the record `00` or `11` is an outcome of the measurement. It is not the full pre-measurement state.

```trace
record_state_distinction :=
  product_case:
    record_00_consistent_with_pre_and_post_state
  entangled_case:
    record_00_or_11_is_not_equivalent_to_pre_state
```

Plain version:

A record is an observed outcome under a context. It is not automatically the whole prior state.

## 6. What this tests in TRACE

```trace
TRACE_pressure_tests :=
  observation_is_not_passive_labeling
  + record_is_not_full_state
  + measurement_context_controls_outcome_space
  + post_state_boundary_matters
  + joint_distribution_matters
```

This matters for TRACE translation generally because many systems confuse evidence, record, state, and reality. QIT forces the distinction formally.

Boundary:

This does not mean institutional records are quantum measurements. It means TRACE must preserve the difference between state, observation operation, record, and post-observation state when translating domains.

## 7. Back-translation checklist

A successful TRACE translation must recover:

```trace
back_translation_checklist :=
  measurement_basis
  + pre_measurement_state
  + outcome_distribution
  + record
  + post_measurement_state
  + difference_between_record_and_pre_state
```

If the translation cannot recover these, it is only metaphor.

## 8. Minimal probability table

| State | P(00) | P(01) | P(10) | P(11) | Post-measurement state |
|---|---:|---:|---:|---:|---|
| `|00>` | 1 | 0 | 0 | 0 | `|00>` |
| `(|00> + |11>) / sqrt(2)` | 1/2 | 0 | 0 | 1/2 | `|00>` if record 00; `|11>` if record 11 |

TRACE use:

```trace
measurement_table_use :=
  preserve_probability_distribution
  + preserve_record
  + preserve_post_state_boundary
  + block_record_equals_pre_state_flattening
```

## 9. What this earns

```trace
earned_claim :=
  TRACE_can_preserve_one_QIT_observation_distinction
  + record_vs_state_failure_is_visible
  + measurement_context_must_be_explicit
  + back_translation_test_is_nontrivial
  - QIT_unified
  - general_measurement_theory
```

## 10. Next step

The next QIT step should test decoherence as a channel.

```trace
next :=
  simple_dephasing_channel_example
  because:
    tests_boundary
    + tests_system_environment_loss
    + tests_loss_of_interference_without_treating_it_as_ordinary_forgetting
```

Reason:

```trace
reason :=
  current_example_tests_observation_and_record
  next_example_should_test_boundary_and_decoherence
```

## 11. Final compression

```trace
QIT_Measurement_Record_Worked_Example_v0_1 :=
  product_state := |00>
  entangled_state := (|00> + |11>) / sqrt(2)
  measurement_context := computational_basis
  record := observed_outcome
  post_state := state_after_measurement_conditioned_on_record
  success := recover_basis + probabilities + record + post_state + pre_state_distinction
  failure := record_equals_full_state_or_measurement_as_passive_label
  next := dephasing_channel_example
  - validation
  - completed_unification
```

End.
