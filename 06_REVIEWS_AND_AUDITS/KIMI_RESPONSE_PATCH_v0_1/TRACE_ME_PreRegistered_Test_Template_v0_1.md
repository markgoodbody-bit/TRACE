# TRACE / ME Pre-Registered Test Template v0.1

Date: 2026-06-16  
Trigger: Kimi external review of TRACE Relay Pack v0.1.  
Status: prospective test template; not validation; not proof.

## 0. Purpose

This template is for testing TRACE before the outcome is known.

```trace
goal :=
  move_TRACE
  from:
    post_hoc_interpretation
  toward:
    prospective_diagnostic_pressure
```

A test does not validate TRACE. It creates a chance for TRACE to be wrong in a way that changes the framework.

## 1. Case Selection

| Field | Entry |
|---|---|
| Case name |  |
| Domain |  |
| Date selected |  |
| Selected before outcome known? | yes / no / partial |
| Why this case matters |  |
| Why TRACE should have something to say |  |
| Why this case might break TRACE |  |

## 2. Outcome Window

| Field | Entry |
|---|---|
| Review date |  |
| Minimum review interval |  |
| What counts as relevant harm? |  |
| What counts as relevant near-miss? |  |
| What counts as no-harm / non-confirmation? |  |
| What evidence sources will be used? |  |

## 3. Branch Selection

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

## 4. K-Gate Pre-Scoring

Use only defined ratings: `PASS`, `PASS_LIMITED`, `PARTIAL`, `FAIL`, `UNKNOWN`.

| Gate | Rating | Threshold for rating | Evidence before outcome | What would change rating? |
|---|---|---|---|---|
| Witness |  |  |  |  |
| Record |  |  |  |  |
| Authority |  |  |  |  |
| Time |  |  |  |  |
| Enforcement |  |  |  |  |
| Repair |  |  |  |  |

## 5. Clock Definitions

```trace
live_correction :=
  tau_correct < tau_harden
```

| Clock | Definition in this case | Measurement source | Uncertainty |
|---|---|---|---|
| `tau_harden` |  |  | high / medium / low |
| `tau_correct` |  |  | high / medium / low |
| `tau_detect` |  |  | high / medium / low |
| `tau_review` |  |  | high / medium / low |

If the clocks cannot be defined prospectively, record that as a limitation. Do not invent false precision.

## 6. Predicted Failure Modes

List 3 to 7 specific predictions.

| ID | Predicted failure mode | TRACE basis | Confidence | What would falsify this prediction? |
|---|---|---|---|---|
| P1 |  |  | high / medium / low |  |
| P2 |  |  | high / medium / low |  |
| P3 |  |  | high / medium / low |  |

## 7. Predicted Success / Non-Failure Conditions

TRACE must also say what would count against it.

| ID | Non-failure or success condition | Why this would weaken TRACE's warning | Evidence needed |
|---|---|---|---|
| S1 |  |  |  |
| S2 |  |  |  |
| S3 |  |  |  |

## 8. Demotion Rule Before Outcome

Before observing the outcome, specify how TRACE will update.

| Result | Required update |
|---|---|
| TRACE predicts risk and relevant harm/near-miss occurs through predicted path | Retain or cautiously strengthen related claim |
| TRACE predicts risk but no relevant harm/near-miss occurs | Run cry-wolf check; tighten thresholds; demote if repeated |
| TRACE misses harm it should have caught | Demote related claim/operator; record false-negative |
| TRACE cannot score prospectively | Mark operator as interpretive, not diagnostic, in this domain |
| Existing framework predicts better than TRACE | Demote TRACE remainder claim in that domain |

## 9. Comparator Frameworks

Name at least two comparators.

| Comparator | What it predicts/checks | Where it may outperform TRACE |
|---|---|---|
|  |  |  |
|  |  |  |

Comparators are mandatory because TRACE must not claim novelty by renaming existing work.

## 10. Pre-Registration Hash

Before using the template, freeze the file and record:

```trace
preregistration_record :=
  date
  + author
  + case
  + document_hash
  + review_date
  + no_outcome_peeking_statement
```

## 11. Review After Outcome

At review date, complete:

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

## 12. Compression

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

End.
