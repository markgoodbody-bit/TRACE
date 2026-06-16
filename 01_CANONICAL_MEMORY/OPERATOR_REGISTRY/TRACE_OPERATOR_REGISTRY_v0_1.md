# TRACE Operator Registry v0.1

Status: canonical memory spine draft. Not validation. Not final theory.

## Purpose

Operators are the central memory unit.

```trace
operator :=
  name
  + compression
  + definition
  + source_case
  + activation_condition
  + deactivation_condition
  + comparator
  + distinct_remainder
  + falsifier
  + demoter
  + status
  + must_not_claim
```

Cases teach operators. Claims status operators. Tests pressure operators. Reviews attack operators. Operators remember.

## Status vocabulary

- `core_operator`: central, active, repeatedly used.
- `patterned_operator`: recurring across cases, not yet core.
- `known_guard`: anti-overclaim or safety guard.
- `boundary_claim`: protects a risky seam.
- `hypothesis_operator`: promising but not operationally earned.
- `candidate_branch`: possible future Kernel branch; not active Kernel.
- `alignment_relevant_hypothesis`: AI/alignment-relevant but not validated.
- `core_governance`: controls wrongability, demotion, preregistration.

## Operator table

| ID | Operator | Family | Status | Kernel | Compression | Source | Must-not-claim |
|---|---|---|---|---|---|---|---|
| OP-001 | Correction Before Hardening | Timing | core_operator | in Kernel | `tau_correct < tau_harden` | Apollo 13 / Temporal Power | Do not claim every delay is harm. |
| OP-002 | K-Gate | Correction | core_operator | in Kernel | `K := Witness * Record * Authority * Time * Enforcement * Repair` | Apollo 13 / Columbia | Do not turn K into a numeric score without measurement rules. |
| OP-003 | Safeguard Corrigibility | Correction | patterned_operator | not Kernel | `safeguard_real := bites_in_time + remains_corrigible` | Rosetta / Kimi | Do not claim all certification is meaningless. |
| OP-004 | Harm Clock | Timing | patterned_operator | support | `harm_clock := time_until_loss_hardens` | WRATT / Temporal Power | Do not treat speed itself as good or bad. |
| OP-005 | Memory Bridge | Memory | patterned_operator | not Kernel | `memory_bridge := record + continuity + contestability` | Memento | Do not equate record with truth automatically. |
| OP-006 | Record Trust | Memory | patterned_operator | support | `record_trust := preserved + contestable + non_captured` | Memento / Robodebt | Do not assume digital record means trustworthy record. |
| OP-007 | Method Floor | Method | known_guard | not Kernel | `outcome_success_does_not_clean_method` | Unthinkable | Do not claim method questions are already solved. |
| OP-008 | No-Clean-Branch | Method | known_guard | not Kernel | `all_options_dirty != method_erasure` | Unthinkable | Do not erase harm because the alternative was worse. |
| OP-009 | Method Laundering | Method | patterned_operator | support | `outcome_or_process_used_to_clean_harmful_method` | Unthinkable / PCFU | Do not treat procedure itself as suspect. |
| OP-010 | Predatory System Boundary | Exit | candidate_branch | not Kernel | `official_route_is_harm_carrier` | Harriet Tubman | Do not call every flawed institution predatory. |
| OP-011 | Exit Route | Exit | patterned_operator | candidate | `protected_path_out_before_capture` | Harriet Tubman | Do not turn exit into immunity from review. |
| OP-012 | Protective Secrecy | Exit | boundary_claim | not Kernel | `bounded_opacity_to_preserve_subject_escape` | Harriet Tubman | Protective secrecy is not opacity permission. |
| OP-013 | Care With Teeth | Care | patterned_operator | not Kernel | `option_space_restoration + enforceable_constraint` | Samwise / Tubman | Care must not become control. |
| OP-014 | Load-Bearing Care | Care | patterned_operator | not Kernel | `carry_burden_without_taking_corrupting_power` | Samwise | Do not glorify suffering. |
| OP-015 | Option-Space Restoration | Care / Repair | core_operator | support | `repair := restore_real_future_options` | Children of Men / Samwise | Do not count symbolic repair as enough. |
| OP-016 | Recursive Agency | Agency | hypothesis_operator | candidate only | `branch_selection + memory + feedback + self_update under_constraint` | Groundhog Day | Groundhog Day is not proof of free will. |
| OP-017 | Escape Condition | Agency | hypothesis_operator | candidate only | `what_counts_as_release_from_loop` | Groundhog Day | Do not assume every system has a clean escape. |
| OP-018 | Mandelbrot Boundary | Pattern | boundary_claim | not Kernel | `same_rule + iteration + boundary + small_delta -> path` | Groundhog / lattice work | Mandelbrot is not proof. |
| OP-019 | Creator Responsibility | Creation | candidate_branch | not Kernel v0.3 | `created_power -> continuing_answerability` | Frankenstein | Frankenstein is not proof of AI personhood. |
| OP-020 | Created Subject Boundary | Subject | boundary_claim | not Kernel | `created_origin != property_status` | Frankenstein | Created origin is not property status. |
| OP-021 | Recognition Failure | Subject | patterned_operator | not Kernel | `appearance_or_origin_used_to_cancel_subject_claim` | Frankenstein | Do not equate all rejection with recognition failure. |
| OP-022 | Repair Debt | Creation / Repair | patterned_operator | candidate | `causal_initiation + avoidable_harm_path + unmet_repair_duty` | Frankenstein | Repair debt is not total blame. |
| OP-023 | Lifecycle Answerability | Creation / Governance | alignment_relevant_hypothesis | candidate | `deploy + monitor + correct + repair + retire_ethically` | Frankenstein / AI | Do not call it solved by checklist. |
| OP-024 | Demotion Protocol | Governance | core_governance | control | `falsifier + demoter + removal_condition` | Kimi review | Do not protect TRACE from being wrong. |
| OP-025 | Pre-Registered Test | Governance | core_governance | control | `case_before_outcome + thresholds + predictions + review_date` | Kimi review | Do not call one prospective test validation. |
| OP-026 | Cry-Wolf Check | Governance | core_governance | control | `repeated_FAIL_without_relevant_harm -> threshold_review` | Kimi review | Do not only count hits. |
| OP-027 | False-Negative Check | Governance | core_governance | control | `PASS/PARTIAL + missed_harm -> demote` | Kimi review | Do not move goalposts. |
| OP-028 | Contested Legitimacy Candidate | Governance / Exit | candidate_branch | not Kernel | `official_system_not_predatory_but_legitimacy_fractured` | Kimi COVID breaker | Do not rush this branch. |

## Required detail for each operator

Every operator eventually needs a full row with:

```trace
operator_row :=
  id
  + name
  + compression
  + plain_definition
  + source_case
  + connected_cases
  + activation_condition
  + deactivation_condition
  + comparator
  + distinct_remainder
  + falsifier
  + demoter
  + status
  + kernel_status
  + must_not_claim
```

This registry is the memory spine, not the whole project. The full bootstraps and artifacts must remain preserved.
