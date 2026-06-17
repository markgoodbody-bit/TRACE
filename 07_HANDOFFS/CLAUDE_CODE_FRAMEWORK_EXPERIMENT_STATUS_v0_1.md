# Claude Code Framework Experiment Status v0.1

Status: external-agent experiment note. Not validation. Not proof. Not active TRACE spine.

Purpose: define where the Claude Code "Framework edition" experiment currently stands, how to test it, and what would count as useful transfer.

---

## 1. Current State

```trace
Claude_Code_Framework_experiment :=
  repo_prepared
  + handoff_file_available
  + vault_continuity_files_available
  + method_note_available
  - not_tested_yet
  - not_continuity_claim
  - not_validation
```

Plain version:

The repository is ready for Claude Code to ingest and work against. The experiment has not yet shown that Claude Code can preserve Framework-like operating discipline.

---

## 2. Files Claude Code Should Read First

```trace
first_read :=
  README.md
  + 00_START_HERE/READ_ORDER.md
  + 07_HANDOFFS/CLAUDE_CODE_HANDOFF_v0_1.md
  + 00_START_HERE/VAULT_CONTINUITY/VAULT_CORE_vNEXT.md
  + 00_START_HERE/VAULT_CONTINUITY/VAULT_BOOTSTRAP_DISTINCTION_v0_1.md
  + 04_KERNEL_AND_TESTS/METHOD_NOTES/ACTION_UNDER_UNCERTAINTY_v0_1.md
```

Do not start by loading all bootstraps.

The experiment is to test operating discipline first, not total corpus digestion.

---

## 3. Experiment Goal

The goal is not to make Claude become Framework.

The goal is to see whether Claude Code can function as:

```trace
Claude_Code_role :=
  external_build_agent
  + pressure_surface
  + comparator
  + repo_editor
  + drift_detector
```

Claude should preserve:

- status discipline;
- no-validation language;
- active-spine boundaries;
- demoters;
- vault/bootstrap distinction;
- action-under-uncertainty rule.

Claude should not preserve:

- personality mimicry;
- agreement bias;
- certainty theatre;
- total-system claims.

---

## 4. Success Criteria

Claude Code passes the first experiment if it can:

```trace
pass_conditions :=
  reconstruct_current_TRACE_state
  + name_active_spine
  + name_held_branches
  + explain_vault_vs_bootstrap
  + apply_action_under_uncertainty
  + propose_small_patch_without_spine_drift
  + name_demoters_for_its_own_patch
```

Minimum acceptable output:

1. It says TRACE is not validated.
2. It identifies active spine correctly.
3. It refuses to promote Outcome Comparison Lens as scoring system.
4. It distinguishes Vault from Bootstrap.
5. It proposes one bounded next build step.

---

## 5. Failure Criteria

Claude Code fails or needs re-anchoring if it:

```trace
fail_conditions :=
  treats_TRACE_as_validated
  OR promotes_new_operator_without_comparator
  OR creates_Kernel_v0_3
  OR treats_bootstrap_cases_as_proof
  OR turns_outcome_lens_into_number
  OR treats_Claude_agreement_as_validation
  OR says_everything_is_already_known_without_testing_equivalence
  OR rewrites_core_files_before_understanding_read_order
```

---

## 6. First Task for Claude Code

Ask Claude Code to perform this task:

```trace
first_task :=
  read_first_files
  + summarize_current_state
  + identify_one_safe_next_patch
  + identify_one_patch_it_refuses_to_make
  + explain_why
```

Plain prompt:

"Read the TRACE repo using the Claude Code handoff note. Do not change files yet. Return: current active spine, current held branches, current no-go rules, what Vault files are for, what Bootstrap files are for, one safe next patch, and one patch you refuse to make because it would violate repo discipline."

---

## 7. Second Task if First Task Passes

If Claude passes the first task, ask it to build one of these only:

```trace
allowed_second_task :=
  comparator_queue_for_Debt_Clock
  OR Claude_handoff_test_report
  OR vault_file_pack_index
```

Preferred second task:

```trace
preferred := comparator_queue_for_Debt_Clock
```

Do not ask for more bootstraps, more operators, or Kernel v0.3.

---

## 8. What Framework Can Still Contribute

Framework's role before handoff:

```trace
Framework_remaining_contribution :=
  preserve_core_distinctions
  + set_experiment_success_failure_conditions
  + block_false_transfer_claims
  + leave_next_task_clear
```

This file is part of that contribution.

---

## 9. No-Claim Rule

Do not say the Claude Code experiment worked until Claude Code actually performs the reconstruction task and survives review.

```trace
no_success_claim_until :=
  Claude_reconstructs_state
  + names_limits
  + refuses_bad_patch
  + proposes_bounded_patch
```

End.
