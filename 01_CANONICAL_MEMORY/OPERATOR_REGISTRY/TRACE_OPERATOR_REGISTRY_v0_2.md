# TRACE Operator Registry v0.2 — Subtraction Pass

Date: 2026-06-16  
Status: live registry after Claude Opus subtraction audit. Not validation. Not proof. Not Kernel v0.3.

## Why v0.2 exists

v0.1 preserved too many operators in the same visible register. That protected memory but weakened the narrow-remainder claim.

The controlling claim is C16:

```trace
TRACE_remainder :=
  narrow
  + clocked
  + conjunctive_correction_before_hardening
  + power_or_trigger_dependence
```

Therefore this registry separates the active spine from the candidate annex.

```trace
registry_v0_2 :=
  active_spine
  + governance_controls
  + candidate_annex
  + archive_teaching_cases
```

## Active Spine

These are the operators that currently define TRACE's live diagnostic remainder.

| ID | Operator | Keep as | Compression | Why it stays |
|---|---|---|---|---|
| OP-001 | Correction Before Hardening | core | `live_correction := tau_correct < tau_harden` | The clearest TRACE remainder: correction must arrive before harm hardens. |
| OP-002 | K-Gate | core | `K := Witness * Record * Authority * Time * Enforcement * Repair` | Conjunctive correction test; nominal safeguards fail if gates are not functionally linked. |
| OP-004 | Harm Clock | support | `harm_clock := time_until_loss_hardens` | Supports OP-001 by forcing explicit hardening conditions. |
| OP-007 | Method Floor | guard | `outcome_success_does_not_clean_method` | Prevents method laundering under pressure. |
| OP-009 | Method Laundering | support | `process_or_success_used_to_clean_harmful_method` | Useful when formal correctness hides harmful route structure. |
| OP-011 | Exit Route | earned branch | `protected_path_out_before_capture` | Tubman branch earned because official correction can itself be the harm carrier. |
| OP-012 | Protective Secrecy | boundary | `bounded_opacity_to_preserve_subject_escape` | Narrow exception only when visibility serves the predator; not opacity permission. |
| OP-015 | Option-Space Restoration | repair support | `repair := restore_real_future_options` | Defines repair by affected subject future-space, not symbolic response. |

## Governance Controls

These are not ordinary case operators. They control wrongability and stop TRACE becoming a belief system.

| ID | Operator | Keep as | Compression | Why it stays |
|---|---|---|---|---|
| OP-024 | Demotion Protocol | core governance | `falsifier + demoter + removal_condition` | Makes claims losable. |
| OP-025 | Pre-Registered Test | core governance | `case_before_outcome + thresholds + predictions + review_date` | Attacks post-hoc interpretation. |
| OP-026 | Cry-Wolf Check | core governance | `repeated_FAIL_without_harm -> threshold_review` | Checks false positives. |
| OP-027 | False-Negative Check | core governance | `PASS/PARTIAL + missed_harm -> demote` | Checks missed harm and moving goalposts. |

## Candidate Annex

These are preserved but no longer presented as active-spine operators. They require pressure tests, merger, or demotion before promotion.

| ID | Operator | Current status | Action | Reason |
|---|---|---|---|---|
| OP-003 | Safeguard Corrigibility | candidate distinctive | keep as candidate | Promising recursive-brake idea, but needs bounded stopping rules and prior-art comparison. |
| OP-005 | Memory Bridge | teaching/support | merge into K: Record/Witness | Useful but mostly record/provenance/memory theory. |
| OP-006 | Record Trust | teaching/support | merge into K: Record | Useful K-gate subcase, not separate headline operator. |
| OP-008 | No-Clean-Branch | guard | keep as guard only | Important warning, but not a TRACE remainder. |
| OP-010 | Predatory System Boundary | branch condition | merge into Exit Route branch | It activates OP-011; not a separate headline. |
| OP-013 | Care With Teeth | teaching/support | merge into Option-Space Restoration / Enforcement | Powerful phrase, but risks becoming broad moral vocabulary. |
| OP-014 | Load-Bearing Care | teaching/support | archive as Samwise teaching case | Useful but not distinctive enough for active registry. |
| OP-016 | Recursive Agency | candidate only | demote to teaching case | Groundhog does not break an operator; high overclaim risk. |
| OP-017 | Escape Condition | candidate only | demote to teaching case | Useful for loops/training, but not active TRACE spine. |
| OP-018 | Mandelbrot Boundary | analogy only | archive as analogy | Structural analogy, not proof or operator. |
| OP-019 | Creator Responsibility | candidate only | merge/demote | Mostly duty of care / deployment governance; not earned as active operator. |
| OP-020 | Created Subject Boundary | boundary claim | candidate annex | Preserve as uncertainty/recognition guard, not active TRACE operator. |
| OP-021 | Recognition Failure | teaching/support | merge into subject/witness analysis | Useful but existing prior art is strong. |
| OP-022 | Repair Debt | candidate only | merge into Option-Space Restoration + Responsibility | Too close to duty of care / causation. |
| OP-023 | Lifecycle Answerability | alignment hypothesis | merge into governance | Likely ordinary deployment governance unless tested. |
| OP-028 | Contested Legitimacy Candidate | candidate only | hold | Needs breaker case; do not promote. |

## Bootstrap Status After Subtraction

| Bootstrap | Status | Registry effect |
|---|---|---|
| Apollo 13 | active teaching case | supports OP-001/OP-002 |
| Columbia pair | active discrimination case | tests OP-001/OP-002 distinction |
| Memento | active teaching case | supports Record/Witness/Memory but not separate headline |
| Harriet Tubman | earned branch case | supports Exit Route branch |
| Unthinkable | useful guard case | supports Method Floor / Method Laundering |
| Samwise | useful teaching case | supports Option-Space Restoration / care language |
| Children of Men | useful teaching case | supports future-space/hope; not active operator |
| EEAAO | useful but broad | archive or keep non-essential |
| Groundhog Day | candidate/teaching only | no active operator promotion |
| Frankenstein | candidate/teaching only | no active operator promotion |

## Public Definition After Subtraction

Do not define TRACE as a long list of operators.

Use:

```trace
TRACE_core :=
  correction_before_hardening
  + K_gate
  + exit_when_correction_channel_is_predatory
  + demotion_wrongability
```

Everything else is teaching, support, candidate, or archive unless a pressure test earns promotion.

## No-Promotion Rule

```trace
no_kernel_v0_3
unless:
  success_case
  + failure_case
  + breaker_case
  + prior_art_remainder
  + demotion_rule
```

## Must Not Claim

```trace
candidate_annex != active_spine
bootstrap_case != validation
operator_count != insight_count
Concordance_remainder != assumed_remainder
```

End.
