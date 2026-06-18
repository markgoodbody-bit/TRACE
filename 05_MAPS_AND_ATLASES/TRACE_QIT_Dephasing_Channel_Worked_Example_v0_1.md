# TRACE QIT Dephasing Channel Worked Example v0.1

Date: 2026-06-18
Status: worked mathematical translation example / QIT boundary and decoherence test / not validation / not proof / not QIT theory / not operator promotion / not Kernel v0.3

## 0. Control header

This file follows `TRACE_QIT_Measurement_Record_Worked_Example_v0_1.md`.

The previous example tested observation and record. This example tests boundary and decoherence using a simple dephasing channel.

It does not claim TRACE unifies QIT.

It does not replace QIT, quantum mechanics, or specialist mathematics.

```trace
dephasing_channel_example :=
  coherent_input_state
  -> dephasing_channel
  -> diagonal_output_state
  + test:
      coherence_loss_preserved?
      + boundary_role_preserved?
      + no_outcome_record_required?
      + back_translation_possible?
  - validation
  - completed_unification
```

## 1. Native object

Use the one-qubit plus state:

```text
|+> = (|0> + |1>) / sqrt(2)
```

Density matrix:

```text
rho_plus = |+><+| = 1/2 [[1, 1], [1, 1]]
```

A complete dephasing channel in the computational basis maps:

```text
Delta(rho) = P0 rho P0 + P1 rho P1
P0 = |0><0|
P1 = |1><1|
```

For `rho_plus`:

```text
Delta(rho_plus) = 1/2 [[1, 0], [0, 1]]
```

Boundary:

This is a simple dephasing example. It is not a full theory of decoherence.

## 2. TRACE-form target

```trace
TRACE_form(QIT) :=
  {S_Q, T_Q, C_Q, O_Q, K_Q, B_Q, I_Q}
```

For this example:

```trace
S_Q := density_operator
T_Q := dephasing_channel
C_Q := not_primary_in_single_qubit_case
O_Q := optional_readout_not_required_for_channel
K_Q := positivity_trace_and_channel_constraints
B_Q := basis_and_environment_or_channel_boundary
I_Q := coherence_off_diagonal_terms
```

## 3. TRACE translation

Native transition:

```text
rho_plus -> Delta(rho_plus)
```

TRACE translation:

```trace
dephasing_translation :=
  pre_state := rho_plus
  transformation := Delta
  basis := computational_basis
  off_diagonal_terms_before := nonzero
  off_diagonal_terms_after := zero
  diagonal_terms_preserved := true
  specific_outcome_record_required := false
```

Plain version:

The channel removes coherence in the chosen basis. It does not require a specific observed outcome record like `0` or `1`.

## 4. Critical distinction

Dephasing is not ordinary forgetting.

```trace
critical_distinction :=
  forgetting:
    missing_information_about_record_or_state
  dephasing:
    channel_maps_state_by_suppressing_off_diagonal_terms_in_basis
```

This matters because the output state may resemble a classical mixture in the measurement basis, but the translation must preserve the process by which coherence was removed.

## 5. What must be preserved

```trace
dephasing_preserve :=
  pre_state_has_coherence
  + channel_suppresses_off_diagonal_terms
  + basis_context_matters
  + output_state_is_density_operator
  + no_single_outcome_record_required
```

Failure conditions:

```trace
dephasing_translation_fails_if:
  dephasing_is_treated_as_ordinary_forgetting
  OR off_diagonal_terms_are_not_tracked
  OR basis_context_is_lost
  OR output_is_treated_as_specific_measurement_record
  OR channel_role_is_erased
```

## 6. Boundary role

The boundary role in this example is not a moral or institutional boundary. It is a QIT boundary: what state-space, basis, and channel are being used.

```trace
QIT_boundary_role :=
  chosen_basis
  + channel_context
  + possible_system_environment_interaction_model
```

Plain version:

TRACE must not translate `decoherence` as generic loss. It must preserve the native structure: basis-sensitive suppression of coherence through a channel or interaction model.

## 7. Back-translation checklist

A successful TRACE translation must recover:

```trace
back_translation_checklist :=
  input_state_rho_plus
  + off_diagonal_terms_before_dephasing
  + dephasing_channel_Delta
  + output_state_diagonalised_in_basis
  + no_specific_measurement_record_required
  + distinction_between_dephasing_and_observed_measurement_outcome
```

If this cannot be recovered, the translation is metaphor rather than structure.

## 8. Minimal table

| Object | Matrix / map | TRACE role |
|---|---|---|
| `rho_plus` | `1/2 [[1, 1], [1, 1]]` | pre-state with coherence |
| `Delta` | `P0 rho P0 + P1 rho P1` | dephasing transformation |
| `Delta(rho_plus)` | `1/2 [[1, 0], [0, 1]]` | output state with off-diagonal terms suppressed |
| no observed outcome | not `0` or `1` | record not required by this channel example |

## 9. What this tests in TRACE

```trace
TRACE_pressure_tests :=
  loss_is_not_always_forgetting
  + boundary_context_matters
  + transformation_can_remove_structure_without_generating_specific_record
  + state_record_distinction_still_holds
```

This is a useful pressure point for TRACE’s universal language: the same word `loss` cannot be allowed to flatten mathematically distinct processes.

## 10. What this earns

```trace
earned_claim :=
  TRACE_can_preserve_one_QIT_boundary_loss_distinction
  + dephasing_vs_forgetting_failure_is_visible
  + channel_role_is_preserved
  + back_translation_test_is_nontrivial
  - QIT_unified
  - general_decoherence_theory
```

## 11. Next step

The next step should consolidate the three QIT examples.

```trace
next :=
  QIT_three_example_consolidation
  with:
    composition_example
    + measurement_record_example
    + dephasing_channel_example
    + success_failure_matrix
```

Reason:

```trace
reason :=
  QIT_path_now_has:
    composition_test
    + observation_record_test
    + boundary_loss_test
```

## 12. Final compression

```trace
QIT_Dephasing_Channel_Worked_Example_v0_1 :=
  input := rho_plus
  transformation := Delta
  output := Delta(rho_plus)
  preserved := diagonal_terms
  suppressed := off_diagonal_terms
  record_required := false
  success := recover_channel + basis + coherence_loss + no_specific_record
  failure := dephasing_as_forgetting_or_record
  next := QIT_three_example_consolidation
  - validation
  - completed_unification
```

End.
