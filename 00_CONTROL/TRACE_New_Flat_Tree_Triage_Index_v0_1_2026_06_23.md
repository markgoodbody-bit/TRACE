# TRACE New Flat-Tree Triage Index v0.1

Status: additive control index. Not canon promotion. Not validation. Not deletion authority.

Purpose: wire the 2026-06-23 flat-tree work into a visible control surface so recent artifacts do not become de facto canon by accumulation.

```trace
triage_index :=
  visibility_control
  + authority_status_map
  + drift_alarm_surface
  - not_canon_promotion
  - not_migration
  - not_deletion
```

---

## 0. Current repo drift being controlled

```trace
repo_drift :=
  numbered_canon_tree
  + newer_flat_tree
  + claims_ledger_delta
  + tests/prompts/schemas/cases
  + unmerged_live_outputs
```

Risk:

```trace
if flat_tree_work_not_indexed:
  new_files_gain_de_facto_authority_without_claim_demotion_gate
```

This index does not resolve final authority shape. It makes the fork visible.

---

## 1. Authority statuses used here

```trace
SOURCE_AUTHORITY := approved source/canon authority
CONTROL := governs claim/status/test/drift handling
LIVE_WORKING := active build artifact, not canon
TEST_FIXTURE := executable or prompt-based test control
RUN_RECORD := record of a specific run, not proof
REVIEW_INPUT := external/internal critique, not validation
DELTA_TO_MERGE := additive delta needing canonical merge/reference decision
ARCHIVE := retained history, not active
DEMOTE := active demotion candidate
DELETE_CANDIDATE := delete/archive only after reference check + Mark approval
```

---

## 2. Recent flat-tree artifacts

| Path | Current status | Proposed handling | Notes |
|---|---|---|---|
| `core/TRACE_Scale_With_Teeth_Program_v0_1_2026_06_23.md` | LIVE_WORKING | CONTROL-CANDIDATE / strategic build program | Preserves large-build-with-controls frame; not proof. |
| `tests/falsification/TRACE_Falsify_x100_Drift_Audit_v0_1_2026_06_23.md` | CONTROL | Keep findable from `00_CONTROL` | Current drift status: AMBER. |
| `tests/validate_case_graphs.py` | TEST_FIXTURE | Use as runnable schema drift check | Repo source returns non-zero on failed validation; see note below. |
| `prompts/TRACE_Grenfell_Existing_Run_Blind_Regrade_Prompt_v0_1_2026_06_23.md` | TEST_FIXTURE | Use for nearest cheap falsifier | Tests decision-delta, not format compliance. |
| `prompts/TRACE_Grenfell_Blind_Counterbalanced_Test_Prompt_v0_1_2026_06_23.md` | TEST_FIXTURE | Use after blind regrade | Removes order/list-leak confounds. |
| `prompts/TRACE_Blind_Grader_Decision_Delta_Rubric_v0_1_2026_06_23.md` | TEST_FIXTURE | Pair with blind outputs | Scores deltas, not TRACE vocabulary. |
| `01_CANONICAL_MEMORY/META_HYPOTHESES/TRACE_Meta_Hypotheses_2026_06_23.md` | LIVE_WORKING continuity memory | Keep but mark not-canon in local README | Location creates authority-risk. |
| `01_CANONICAL_MEMORY/CLAIMS_AND_DEMOTION/CLAIMS_LEDGER_v0_5/TRACE_ME_Claims_Ledger_v0_5_2026_06_23_DELTA.md` | DELTA_TO_MERGE | Reference from main ledger or control index; do not treat as merged yet | Registers X057 Meta/Grenfell claim with demoters. |
| `01_CANONICAL_MEMORY/CLAIMS_AND_DEMOTION/CLAIMS_LEDGER_v0_5/TRACE_ME_Claims_Ledger_v0_5_2026_06_23_DELTA.csv` | DELTA_TO_MERGE | CSV companion to X057 delta | Same status as MD delta. |

---

## 3. Validator status

Current reported validator result from Claude read-only run:

```trace
validator_result := FAIL
passes := [amazon, feral_hogs_v0_1_1]
fails := [feral_hogs_v0_1, rambo_first_blood]
```

Reported failures:

```trace
feral_hogs_v0_1 :=
  band enum
  + authority_status enum
  + extra metadata properties

rambo_first_blood :=
  guard values not in Claim.schema enum
```

Repository source check:

```trace
validator_exit_source :=
  tests/validate_case_graphs.py returns 0 if ok else 1
```

Therefore if a local run exits `0` while reporting `FAIL`, check the invocation wrapper or runtime, not only the source file.

Guard:

```trace
schema_valid ≠ true
schema_invalid ≠ bad_artifact_automatically
schema_failure := drift_to_triage
```

---

## 4. Case graph triage

| Path | Status | Proposed action | Requires Mark decision |
|---|---|---|---|
| `cases/graphs/TRACE_amazon_case_graph_v0_1_2026_06_23.json` | LIVE_WORKING / schema-pass reported | Keep; include in corpus. | false |
| `cases/graphs/TRACE_feral_hogs_case_graph_v0_1_1_2026_06_23.json` | LIVE_WORKING / schema-pass reported | Keep as active feral hog graph. | false |
| `cases/graphs/TRACE_feral_hogs_case_graph_v0_1_2026_06_23.json` | DELETE_CANDIDATE or ARCHIVE | Broken + superseded; verify references first. | true |
| `cases/graphs/TRACE_rambo_first_blood_case_graph_v0_1_2026_06_23.json` | LIVE_WORKING / schema-fail reported | Resolve schema-vs-instance guard enum authority. | true |

---

## 5. Live authority questions

```trace
needs_Mark_decision :=
  canonical_target_shape
  + rambo_guard_enum_resolution
  + feral_hogs_v0_1_delete_or_archive_after_ref_check
  + legacy_carryover_deletions_archives
```

### Decision 1: canonical target shape

```trace
options :=
  numbered_canon_tree
  | flat_tree
  | cleanup_manifest_math_kernel_target
  | hybrid
```

Current default until Mark decides:

```trace
current_default := hybrid_visible_not_merged
```

Meaning: flat-tree work remains live and visible, but not promoted into source canon by location or activity volume.

### Decision 2: Rambo guard enum

```trace
options :=
  expand_Claim_schema_guards
  OR rename_Rambo_graph_guards_to_existing_canonical_set
```

Do not auto-resolve. This changes schema vocabulary authority.

---

## 6. Immediate safe next actions

```trace
safe_next :=
  create_META_HYPOTHESES_README_not_canon
  + create_validation_status_record
  + create_negative_control_case
  + create_external_challenge_surface
```

Do not delete or migrate until Mark decides authority shape and deletion policy.

---

## 7. Control guard

```trace
this_index_must_not_be_used_as :=
  canon_promotion
  + validation
  + deletion_authority
  + migration_complete_claim
```

Allowed use:

```trace
allowed_use :=
  cold_reader_navigation
  + drift_visibility
  + cleanup_queue
  + authority_question_surface
```
