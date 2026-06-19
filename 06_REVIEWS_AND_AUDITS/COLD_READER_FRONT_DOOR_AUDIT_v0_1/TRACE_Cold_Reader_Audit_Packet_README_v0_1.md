# TRACE Cold Reader Audit Packet README v0.1

Status: handoff note. Not an audit result. Not validation. This is the exact packet instruction for a true cold reader or fresh AI context.

```trace
Cold_Reader_Audit_Packet_README_v0_1 :=
  packet_manifest
  + handoff_instruction
  + contamination_guard
  + return_format
  - audit_result
  - validation
```

## Purpose

This packet tests whether the TRACE cold-reader front door works without project background.

```trace
purpose :=
  test_entry_cost
  + test_basic_comprehension
  + test_first_use
  + test_claim_boundaries
```

## Give the reviewer only these five files

Four reader files:

1. `00_START_HERE/TRACE_FOR_NEW_READERS_v0_1.md`
2. `00_START_HERE/USE_TRACE_ON_ONE_PROBLEM_v0_1.md`
3. `00_START_HERE/TRACE_WORKED_EXAMPLE_WALL_E_v0_1.md`
4. `00_START_HERE/WHAT_TRACE_IS_NOT_v0_1.md`

One audit prompt:

5. `06_REVIEWS_AND_AUDITS/COLD_READER_FRONT_DOOR_AUDIT_v0_1/TRACE_Cold_Reader_Front_Door_Audit_Prompt_v0_1.md`

```trace
packet :=
  four_reader_files
  + one_audit_prompt
  - full_repo
  - project_history
```

## Contamination guard

Do not tell the reviewer:

```trace
do_not_provide :=
  Mark_history
  + Framework_history
  + Mechanical_Ethics_history
  + repo_summary
  + prior_reviews
  + intended_answer
```

If using another AI, start a fresh chat if possible.

If the reviewer already knows TRACE / Mechanical Ethics, mark the result as contaminated.

```trace
if_prior_context := contaminated_result
```

## Reviewer instruction

Use the audit prompt exactly.

Do not ask for praise.

Do not ask whether TRACE is ultimately true.

Do not ask whether it solves AI alignment.

Ask only whether the four-file front door works for a new reader.

```trace
review_scope :=
  front_door_only
  + comprehension
  + useability
  + claim_boundaries
  + worked_example
  + patch_recommendations
```

## Required returned fields

The reviewer should return:

```trace
required_return :=
  basic_comprehension_score
  + useability_score
  + claim_boundary_score
  + worked_example_score
  + top_friction_points
  + overclaim_risks
  + five_patch_recommendations
  + verdict
```

Verdict options:

```trace
verdict :=
  pass
  OR pass_with_patches
  OR unclear_rework_needed
  OR fail
```

## Minimum pass condition

```trace
minimum_pass :=
  basic_comprehension_score >= 4
  + useability_score >= 4
  + claim_boundary_score >= 4
  + worked_example_score >= 4
  + verdict in {pass, pass_with_patches}
```

## How to record the result

If a true cold reader result comes back, create:

`06_REVIEWS_AND_AUDITS/COLD_READER_FRONT_DOOR_AUDIT_v0_1/TRACE_True_Cold_Reader_Audit_Result_[reviewer]_[date]_v0_1.md`

Required status line:

```trace
status :=
  true_cold_reader_result
  OR contaminated_result
  - validation
```

## Patch rule after result

If the result fails or returns `unclear_rework_needed`, patch only the four front-door files.

Do not add new atlases, operators, kernels, or broad theory.

```trace
if_fail :=
  patch_front_door_only
  + do_not_expand_repo
```

If the result passes, the next legitimate moves are:

```trace
if_pass :=
  public_summary_draft
  OR NotebookLM_single_PDF_build_later
```

## Current packet status

```trace
current_packet_status :=
  ready_for_true_cold_reader
  + patched_after_proxy_audit
  - validated
```

End.
