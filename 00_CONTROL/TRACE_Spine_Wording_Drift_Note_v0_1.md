# TRACE Spine Wording Drift Note v0.1

Date: 2026-06-17

Status:

```trace
status :=
  control_note
  + drift_flag
  + not_validation
  + not_active_spine
  + not_kernel_v0_3
```

## Plain purpose

This note flags a live wording inconsistency in how the third element of the active TRACE spine is stated across the repo. It does not resolve the inconsistency and does not change the spine. It exists so that no one silently harmonises the wording or lets the difference change branch activation without a deliberate decision.

## 1. The conflict

The active spine's exit element is stated two different ways.

Surfaces using `exit_when_correction_channel_is_harm_carrier`:

- `README.md:24`
- `02_CURRENT_SURFACE/PUBLIC_ONE_SHEET_v0_3/TRACE_ME_PUBLIC_ONE_SHEET_v0_3.md:14`
- `00_START_HERE/VAULT_CONTINUITY/VAULT_CORE_vNEXT.md:210`
- `07_HANDOFFS/CLAUDE_CODE_HANDOFF_v0_1.md:61` and `:245`
- `99_ARCHIVE_INDEXES/SUBTRACTION_PATCH_v0_1_2026_06_16.md:53`

Surface using `exit_when_correction_channel_is_predatory`:

- `01_CANONICAL_MEMORY/OPERATOR_REGISTRY/TRACE_OPERATOR_REGISTRY_v0_2.md:104` (the "Public Definition After Subtraction" block)

Note: the disagreement is asymmetric. The majority of surfaces (status, public one-sheet, vault, handoff, archive) use `harm_carrier`, while the single canonical operator-memory file uses `predatory`. The minority wording sits in the most authoritative file. The related operator `OP-011 Exit Route` and `OP-010 Predatory System Boundary` in that same registry use "before_capture" / "predatory" language at the operator layer; this note concerns the spine-level restatement only.

## 2. Why it matters

```trace
harm_carrier := correction_channel_itself_carries_harm
predatory     := correction_channel_intends_or_structurally_exploits
```

- `harm_carrier` is broader. A correction channel can carry harm through negligence, capture, design failure, or delay, with no intent.
- `predatory` is narrower and implies intention-like or structurally exploitative framing.
- A channel can be a harm carrier without being predatory. Therefore the two wordings do not pick out the same set of cases.
- Using both silently could change when the exit branch activates: a `predatory` reading would withhold exit in negligent-but-non-predatory harm cases that a `harm_carrier` reading would catch. This is an activation-threshold difference, not a cosmetic one.

## 3. Temporary rule (until Framework/Mark decides)

```trace
temporary_rule :=
  do_not_harmonise_until_explicit_decision
  + quote_the_source_wording_in_use
  + if branch_activation_depends_on_distinction: mark_uncertainty
```

- Do not harmonise the wording until Framework/Mark explicitly chooses.
- When applying TRACE, quote the exact source wording being used and cite the file.
- If a case's exit-branch activation turns on the harm_carrier-vs-predatory distinction, do not decide it silently. Mark the uncertainty and route it to the decision.

## 4. Candidate resolution options (no choice made here)

- **Option A — harmonise to `harm_carrier`.** Update the registry line to match the majority surfaces. Broadest exit coverage; loses the narrower "predatory" signal unless preserved elsewhere.
- **Option B — keep `predatory` as a subset of a `harm_carrier` branch.** Treat `harm_carrier` as the branch and `predatory` as a high-severity sub-case within it.
- **Option C — split into `harm_carrier` and `predatory_system` with different activation thresholds.** Two distinct activation conditions; more discriminating but adds structure and must pass the normal candidate gate (this would not be done casually and is not a spine change made by this note).

No option is endorsed. Listing is not selection.

## 5. Demoters / removal

```trace
remove_if := wording_harmonised + all_affected_files_updated
demote_if := conflict_already_deliberately_scoped_elsewhere
keep_if   := ambiguity_remains_live
```

- **Remove** this note once the wording is harmonised and every file in Section 1 is updated to the chosen wording.
- **Demote** if it turns out the two wordings are already deliberately scoped (e.g. spine surface vs operator surface) and documented somewhere this note missed; then this note is redundant.
- **Keep** while the ambiguity remains live and undecided.

## Must-not-claim

```trace
this_note != active_spine
this_note != validation
flagging_drift != resolving_drift
AI_agreement != validation
```

This note records a problem. It does not settle it, and it does not validate TRACE.

End.
