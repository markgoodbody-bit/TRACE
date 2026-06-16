# TRACE / ME Case Atlas v0.4

Status: exploratory case-comparison atlas. Not validation. Not proof.

## Purpose

The Case Atlas keeps bootstraps and cases from becoming free-floating stories. Each case must point back to operators.

```trace
case_atlas :=
  case
  + operator_family
  + branch
  + K_pattern
  + failure_point
  + repair_or_exit_route
  + must_not_claim
```

## Case summary

| ID | Case | Class | Branch | Core pattern |
|---|---|---|---|---|
| C01 | Apollo 13 | positive correction case | internal_correction | Truth, authority, time, enforcement, and repair stay functionally linked before failure hardens. |
| C02 | Columbia | failed correction case | internal_correction_failure | K-factors are nominally present but not linked; warning fails to become binding correction. |
| C03 | Harriet Tubman | exit under predatory law | exit_route_candidate | When official system is harm carrier, correction may require protected exit rather than internal review. |
| C04 | Memento | memory / identity case | memory_bridge | Agency becomes manipulable when memory/record continuity is corrupted. |
| C05 | Groundhog Day | recursive agency case | recursive_training_loop | Same conditions plus memory and feedback allow self-update and possible escape condition. |
| C06 | Frankenstein | creator responsibility case | creator_responsibility_candidate | Creation without stewardship, recognition, correction, and repair creates repair debt and destructive drift risk. |

## Current additions

Groundhog Day adds recursive agency but does not prove free will.

Frankenstein adds creator responsibility but does not prove AI personhood.

## Case-use rule

```trace
bootstrap_case :=
  teaching_surface
  not:
    proof
    validation
    canon_by_itself
```

## Next Atlas work

The next Atlas task is not another attractive case. It is a breaker case that tests whether TRACE can fail prospectively.

Kimi proposed COVID-19 vaccine deployment as a breaker because it attacks the binary between corrigible systems and predatory systems. That likely requires a held candidate branch:

```trace
contested_legitimacy :=
  official_system_not_uniformly_predatory
  but legitimacy_fractured_under_polarization
```

This branch is not Kernel v0.3.
