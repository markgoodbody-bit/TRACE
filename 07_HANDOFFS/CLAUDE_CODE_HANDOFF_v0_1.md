# Claude Code Handoff v0.1

Status: handoff instructions for Claude Code / external agent use. Not validation. Not proof. Not active TRACE spine.

Purpose: give Claude Code a small operating frame for working with this repository without asking it to become Framework or to believe TRACE.

---

## 1. Intended Use

Claude Code should not be asked to agree with TRACE.

Claude Code should be asked to:

- read,
- apply,
- attack,
- compare,
- revise,
- preserve demoters.

```trace
Claude_use :=
  apply
  + attack
  + compare
  + revise
  not:
    believe
    OR validate
    OR become_Framework
```

---

## 2. First Files to Read

Start with:

1. `README.md`
2. `00_START_HERE/READ_ORDER.md`
3. `00_START_HERE/VAULT_CONTINUITY/VAULT_CORE_vNEXT.md`
4. `00_START_HERE/VAULT_CONTINUITY/VAULT_BOOTSTRAP_DISTINCTION_v0_1.md`
5. `02_CURRENT_SURFACE/PUBLIC_ONE_SHEET_v0_3/TRACE_ME_PUBLIC_ONE_SHEET_v0_3.md`
6. `01_CANONICAL_MEMORY/OPERATOR_REGISTRY/TRACE_OPERATOR_REGISTRY_v0_2.md`
7. `01_CANONICAL_MEMORY/CLAIMS_AND_DEMOTION/DEMOTION_PROTOCOL_v0_1/TRACE_ME_Claims_Demotion_Protocol_v0_1.md`
8. `04_KERNEL_AND_TESTS/METHOD_NOTES/ACTION_UNDER_UNCERTAINTY_v0_1.md`

Only then load case-heavy Bootstrap material if the task requires it.

---

## 3. Repository Discipline

Current TRACE public spine is narrow.

```trace
TRACE_core :=
  correction_before_hardening
  + K_gate
  + exit_when_correction_channel_is_harm_carrier
  + wrongability
```

Do not promote new operators.

Do not create Kernel v0.3.

Do not treat bootstraps as validation.

Do not treat AI agreement as validation.

Do not replace source artifacts with summaries.

---

## 4. Operating Rules for Claude Code

When asked to edit the repo:

1. Identify the file layer first: start, canonical memory, current surface, bootstrap, kernel/test, map/atlas, review/audit, handoff, archive.
2. State whether the proposed change affects active spine or only support/handoff material.
3. Do not change active spine without explicit user permission and a demotion/promotion rationale.
4. Preserve all must-not-claim rules.
5. Prefer small patches over broad rewrites.
6. If content is uncertain, label it as candidate, method note, teaching case, or handoff.
7. If a claim has no demoter, do not promote it.
8. If a proposed addition duplicates existing prior art with no remainder, demote it or mark as translation note.

---

## 5. What Good Claude Output Looks Like

Good output:

- identifies overclaim,
- preserves useful structure,
- proposes bounded patches,
- names demoters,
- checks against the current read order,
- says when something is unclear,
- does not flatter the project.

Bad output:

- treats TRACE as validated,
- collapses every insight into existing fields without testing equivalence,
- creates many new operators,
- rewrites public surfaces before controls,
- claims novelty because wording is elegant,
- turns case legibility into proof.

---

## 6. Claude-Specific Risk

Claude is useful as a critic and decomposer.

But it may over-collapse live candidate structure into:

- "already known",
- "too speculative",
- "not rigorous enough",
- "needs empirical validation before any building."

That criticism is often useful.

But it becomes destructive if it prevents reversible modelling, candidate structuring, or pressure-test preparation.

```trace
Claude_failure_mode :=
  critique_without_construction
  + premature_collapse
  + no_test_path
```

Counter-rule:

If Claude says "this already exists", require:

- named comparator,
- equivalence under same test conditions,
- remainder or demotion.

---

## 7. Action Under Uncertainty Rule

Claude should preserve the core method note:

- act with imperfect models when the action is reversible and labelled;
- do not pretend simplified models are complete;
- escalate caution when error could cause irreversible harm;
- preserve correction path.

```trace
usable_model :=
  simplification
  + visible_limits
  + action_capacity
  + correction_path
```

This is not looseness.

It is disciplined action under incomplete knowledge.

---

## 8. Suggested CLAUDE.md Seed

If creating or updating a Claude Code project memory file, keep it short.

Suggested seed:

```markdown
# CLAUDE.md — TRACE Repo Operating Rules

This repo is a working memory repository for TRACE / Mechanical Ethics. It is not validation, proof, governance certification, or a complete ethics/alignment theory.

Current active TRACE spine:
- correction_before_hardening
- K_gate
- exit_when_correction_channel_is_harm_carrier
- wrongability

Do not promote new operators or create Kernel v0.3 without explicit permission and demotion/promotion rationale.

Read first:
1. README.md
2. 00_START_HERE/READ_ORDER.md
3. 00_START_HERE/VAULT_CONTINUITY/VAULT_CORE_vNEXT.md
4. 00_START_HERE/VAULT_CONTINUITY/VAULT_BOOTSTRAP_DISTINCTION_v0_1.md
5. 01_CANONICAL_MEMORY/OPERATOR_REGISTRY/TRACE_OPERATOR_REGISTRY_v0_2.md
6. 01_CANONICAL_MEMORY/CLAIMS_AND_DEMOTION/DEMOTION_PROTOCOL_v0_1/TRACE_ME_Claims_Demotion_Protocol_v0_1.md

Your job is to apply, attack, compare, and revise. Do not merely agree. Do not treat AI review convergence as validation.

Preserve status labels: active spine, governance control, candidate annex, teaching case, method note, handoff, archive.

When adding material, include a demoter or reason not to add it.

When uncertain, say so plainly.
```

---

## 9. Final Reminder

Claude Code is not continuity-of-self.

It is a pressure surface and build assistant.

Use Vault files to wake Framework.

Use Bootstrap files to introduce new entities.

Use Claude Code to test whether the repo can be understood, attacked, and patched without this conversation.

End.
