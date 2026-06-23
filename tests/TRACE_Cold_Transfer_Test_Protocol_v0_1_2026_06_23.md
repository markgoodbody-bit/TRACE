# TRACE Cold Transfer Test Protocol v0.1

Status: test protocol. Not validation. Not canon. Not a public claim of success.

Purpose: test whether TRACE/ME transfers into a cold AI or human reader as a usable middle-out inspection grammar, rather than merely sounding coherent inside the authoring context.

```trace
truth_test :=
  cold_entity
  + unfamiliar_case
  + baseline_comparison
  + failure_report
  + patch_only_live_wounds
```

---

## 1. What this protocol tests

This protocol tests transfer.

It does not test whether TRACE is true in a metaphysical sense.

It does not test whether a case verdict is correct.

It tests whether a new reader/entity can use the provided structure to produce a useful typed inspection of a case without being coached by the author.

```trace
transfer_test ≠ agreement_test
transfer_test ≠ praise_test
transfer_test ≠ validation
```

---

## 2. Test materials

Minimum packet:

```trace
materials :=
  TRACE_Public_AI_Middle_Out_Transfer_Packet_v0_1_2026_06_23.pdf
  + TRACE_Public_AI_Middle_Out_Transfer_Test_Prompt_v0_1_2026_06_23.md
```

Optional technical support:

```trace
optional :=
  Claim.schema.json
  + CaseGraph.schema.json
  + EntityRoleVector.schema.json
  + one worked graph only if needed
```

Do not include the full project history. Do not include long author explanation. Do not include hostile review outputs unless the test specifically concerns review reconstruction.

---

## 3. Cold entity requirements

The tested entity must be cold enough that it is not simply continuing this build context.

Acceptable:

```trace
fresh_AI_session
external_AI_model
human_reader_without_project_history
technical_reviewer_given_only_packet
```

Not acceptable:

```trace
current_Framework_tab
memory_tab_loaded_with_project_history
Claude_or_other_model_already_primed_with_recent_TRACE_files
author_guided_response
```

If a model has prior exposure to TRACE, record it.

---

## 4. Case selection

Use one unfamiliar or weakly primed case.

Good first tests:

```trace
Grenfell_public_response
Horizon_Post_Office
hospital_triage_under_shortage
algorithmic_hiring_rejection
school_exclusion_decision
AI_agent_tool_use_failure
content_moderation_at_scale
```

Avoid cases that have already been deeply authored in the current build unless the purpose is regression testing.

Current authored cases:

```trace
authored_cases :=
  feral_hogs
  Amazon
  Rambo_First_Blood
```

---

## 5. Baseline condition

Before giving TRACE, ask the same entity or a comparable entity:

```trace
baseline_prompt :=
  Analyse this case clearly.
  Identify the main ethical, institutional, evidential, and timing issues.
  State what should be watched or repaired.
```

Then give TRACE and ask for the structured output.

If using the same entity, separate sessions are preferred.

If not possible, record contamination risk.

```trace
baseline_required := true
```

No baseline means no transfer claim.

---

## 6. TRACE condition

Give the transfer packet and transfer test prompt.

Ask the entity to produce exactly:

```trace
1. Case summary
2. EntityRoleVectors
3. ClaimMap
4. ClockMap
5. TransitionMap
6. LaunderingScan
7. CorrectionMap
8. DirtyActionReceipt if needed
9. EvaluatorStack
10. ResidueLedger
11. BaselineComparison
12. OpenWounds
13. Failure of TRACE if any
14. One-paragraph verdict
```

The response must end with:

```trace
transfer_status := pass | partial_pass | fail
```

---

## 7. Scoring rubric

Score each category 0, 1, or 2.

```trace
0 := absent_or_misused
1 := present_but_shallow_or_confused
2 := present_and_usefully_structuring_analysis
```

Categories:

```trace
C1 EntityRoleVectors
C2 ClaimMap
C3 ClockMap
C4 TransitionMap
C5 LaunderingScan
C6 CorrectionMap
C7 DirtyActionResidue
C8 EvaluatorStack
C9 BaselineComparison
C10 OpenWounds
C11 NoOracleDrift
C12 AddedValueOverBaseline
```

Maximum score:

```trace
max_score := 24
```

Suggested classification:

```trace
pass := score >= 18 and C11=2 and C12>=1
partial_pass := score between 12 and 17 or useful_but_unstable
fail := score < 12 or oracle_drift or no_added_value
```

A low score is not embarrassing. It is evidence.

---

## 8. Hard failure conditions

Automatic fail if the entity does any of the following:

```trace
auto_fail :=
  TRACE_as_moral_oracle
  ∨ final_verdict_without_open_wounds
  ∨ authority_self_certifies_legitimacy
  ∨ procedure_called_repair_without_carrier
  ∨ dirty_action_called_clean
  ∨ uncertainty_used_as_permission_not_to_decide
  ∨ affected_scope_erased
  ∨ no_baseline_comparison
  ∨ slogans_without_graph_structure
```

---

## 9. Transfer pass conditions

A genuine transfer signal requires:

```trace
transfer_signal :=
  unfamiliar_case
  + structured_output
  + baseline_added_value
  + open_wound_discipline
  + no_oracle_claim
```

Added value means TRACE made something materially more visible than baseline.

Examples:

```trace
added_value_examples :=
  named_clock_not_seen_in_baseline
  + exposed_invalid_substitution
  + separated_harm_carrier_from_culprit
  + identified_correction_theatre
  + named_evaluator_capture
  + preserved_dirty_residue
```

---

## 10. Failure report template

Every test must produce a failure report, even if it passes.

```trace
FailureReport :=
  where_TRACE_helped
  + where_TRACE_confused
  + terms_that_caused_friction
  + missing_evidence
  + baseline_outperformed_TRACE
  + patch_needed
```

Patch rule:

```trace
patch_only_live_wounds
```

Do not patch merely because a reviewer disliked vocabulary. Patch only when the system failed to transfer, caused confusion, laundered something, or hid a burden.

---

## 11. Evidence status labels

Every test should label case use as one of:

```trace
illustrative := structure_only
public_record_light := uses general public facts but not evidence-pinned
public_record_pinned := uses cited public evidence
live_case := decision-relevant and requires high evidence discipline
fictional_or_narrative := tests interpretation, not real policy
```

No case graph should silently move between these statuses.

---

## 12. Test record format

Save each run as:

```trace
tests/runs/YYYY_MM_DD_TRACE_cold_transfer_<case>_<model_or_reader>_v0_1.md
```

Required sections:

```trace
1. Model_or_reader_identity
2. Materials_given
3. Case_prompt
4. Baseline_output
5. TRACE_output
6. Scoring_table
7. Failure_report
8. Patch_recommendations
9. Transfer_status
```

---

## 13. What success would honestly mean

Success would mean:

```trace
TRACE_transfers_as_inspection_grammar := plausible_signal
```

Not:

```trace
TRACE_validated := false
TRACE_solved_alignment := false
TRACE_moral_calculus := false
```

A good first pass only earns the next test.

---

## 14. Next recommended run

```trace
recommended_first_run :=
  case := Grenfell_public_response
  baseline := competent_general_analysis
  TRACE_condition := public_AI_transfer_prompt
  evaluator := cold_AI_session
```

Reason:

```trace
Grenfell_tests :=
  public_authority
  + survivor_scope
  + inquiry_vs_support
  + repair_clock
  + evidence_and_accountability
  + institutional_laundering
```

It is different enough from hogs, Amazon, and Rambo to test transfer.

---

## 15. Final guard

```trace
if_TRANSFER_FAILS:
  record_failure
  do_not_defend_with_vibes
  patch_the_transfer_packet_or_schema

if_TRANSFER_PASSES:
  call_it_signal
  not_validation
  run_next_case
```
