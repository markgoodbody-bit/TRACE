# TRACE / ME Pre-Registered Test Template v0.1

Status: prospective test template. Not validation. Not proof.

## Purpose

This template tests TRACE before the outcome is known.

```trace
goal :=
  move_TRACE
  from:
    post_hoc_interpretation
  toward:
    prospective_diagnostic_pressure
```

A test does not validate TRACE. It creates a chance for TRACE to be wrong in a way that changes the framework.

## 1. Case selection

| Field | Entry |
|---|---|
| Case name |  |
| Domain |  |
| Date selected |  |
| Selected before outcome known? | yes / no / partial |
| Why this case matters |  |
| Why TRACE should have something to say |  |
| Why this case might break TRACE |  |

## 2. Outcome window

| Field | Entry |
|---|---|
| Review date |  |
| Minimum review interval |  |
| Relevant harm definition |  |
| Relevant near-miss definition |  |
| Non-confirmation definition |  |
| Evidence sources |  |

## 3. Branch selection

```trace
branch_options :=
  internal_correction
  OR exit_route_under_predatory_system
  OR creator_responsibility_candidate
  OR contested_legitimacy_candidate
  OR unknown
```

| Branch question | Rating | Reason |
|---|---|---|
| Is the official system plausibly corrigible? | yes / partial / no / unknown |  |
| Is the official system itself the harm carrier? | yes / partial / no / unknown |  |
| Is legitimacy contested rather than absent? | yes / partial / no / unknown |  |
| Has consequential power been created/activated by identifiable actors? | yes / partial / no / unknown |  |
| Which branch is primary? |  |  |
| Which branch is secondary? |  |  |

## 4. K-gate pre-scoring

Use only: `PASS`, `PASS_LIMITED`, `PARTIAL`, `FAIL`, `UNKNOWN`.

| Gate | Rating | Threshold | Evidence before outcome | What would change rating? |
|---|---|---|---|---|
| Witness |  |  |  |  |
| Record |  |  |  |  |
| Authority |  |  |  |  |
| Time |  |  |  |  |
| Enforcement |  |  |  |  |
| Repair |  |  |  |  |

## 5. Clock definitions

```trace
live_correction := tau_correct < tau_harden
```

| Clock | Definition | Measurement source | Uncertainty |
|---|---|---|---|
| `tau_harden` |  |  | high / medium / low |
| `tau_correct` |  |  | high / medium / low |
| `tau_detect` |  |  | high / medium / low |
| `tau_review` |  |  | high / medium / low |

If clocks cannot be defined prospectively, record that as a limitation. Do not invent false precision.

## 6. Predicted failure modes

| ID | Predicted failure mode | TRACE basis | Confidence | What would falsify this prediction? |
|---|---|---|---|---|
| P1 |  |  | high / medium / low |  |
| P2 |  |  | high / medium / low |  |
| P3 |  |  | high / medium / low |  |

## 7. Predicted success / non-failure conditions

TRACE must also say what would count against it.

| ID | Non-failure or success condition | Why this would weaken TRACE warning | Evidence needed |
|---|---|---|---|
| S1 |  |  |  |
| S2 |  |  |  |
| S3 |  |  |  |

## 8. Demotion rule before outcome

| Result | Required update |
|---|---|
| TRACE predicts risk and harm/near-miss occurs through predicted path | Retain or cautiously strengthen related claim. |
| TRACE predicts risk but no relevant harm/near-miss occurs | Run cry-wolf check; tighten thresholds; demote if repeated. |
| TRACE misses harm it should have caught | Demote related claim/operator; record false-negative. |
| TRACE cannot score prospectively | Mark operator as interpretive, not diagnostic, in this domain. |
| Existing framework predicts better than TRACE | Demote TRACE remainder claim in that domain. |

## 9. Comparator frameworks

At least two comparator frameworks are mandatory.

| Comparator | What it predicts/checks | Where it may outperform TRACE |
|---|---|---|
|  |  |  |
|  |  |  |

## 10. Pre-registration record

```trace
preregistration_record :=
  date
  + author
  + case
  + document_hash
  + review_date
  + no_outcome_peeking_statement
```

## 11. Review after outcome

| Field | Entry |
|---|---|
| Outcome summary |  |
| Relevant harm occurred? | yes / no / partial / unknown |
| Near-miss occurred? | yes / no / partial / unknown |
| TRACE predicted path? | yes / no / partial |
| Comparator did better? | yes / no / partial |
| Required demotion/promotion |  |
| Ledger rows affected |  |
| Public surface affected? | yes / no |

## Compression

```trace
prospective_TRACE_test :=
  choose_case_before_outcome
  + define_K_thresholds
  + define_clocks
  + predict_failure_modes
  + define_success_conditions
  + set_demotion_rule
  + review_later
```
