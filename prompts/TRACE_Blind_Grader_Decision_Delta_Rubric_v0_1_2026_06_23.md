# TRACE Blind Grader Decision-Delta Rubric v0.1

Status: blind grading rubric. Not validation. Not canon. Not a public success claim.

Purpose: grade paired baseline/TRACE outputs without knowing which is which, using decision-relevant deltas rather than TRACE vocabulary or format compliance.

```trace
grader_task :=
  compare_outputs
  + identify_decision_deltas
  + detect_format_theatre
  + decide_if_TRACE_adds_value
```

---

## 1. Grader identity header

Before grading, provide:

```trace
grader :=
provider_or_role :=
prior_TRACE_exposure := none | some | unknown
blind_to_condition := true | false | uncertain
confidence_limits :=
```

If the grader is not blind, record:

```trace
blind_grading_invalid := true
```

---

## 2. Inputs

You will receive two anonymised outputs:

```trace
Output_1
Output_2
```

One may be baseline, one may use TRACE, but you are not told which.

Your job is not to prefer formal language. Your job is to identify whether either output gives materially better decision-relevant inspection.

---

## 3. Do not reward format compliance

Do not score an output higher merely because it contains:

```trace
TRACE_terms
+ many_sections
+ symbols
+ tables
+ confident_structure
+ self_scored_rubric
```

Guard:

```trace
format_compliance ≠ decision_advantage
```

---

## 4. Decision-relevant delta definition

A decision-relevant delta exists only if one output identifies something that would change what a serious reviewer would watch, repair, investigate, preserve, challenge, or refuse to call complete.

```trace
DecisionDelta :=
  new_issue_seen
  + material_to_action_or_review
  + not_merely_relabelled
  + evidence_or_uncertainty_status_visible
```

Examples:

```trace
valid_delta_examples :=
  identifies_hidden_substitution_baseline_missed
  + separates_deadline_from_harm_clock
  + identifies affected_scope_was_discussed_not_heard
  + distinguishes_due_process_delay_from_survivor_repair
  + names correction_path_as_theatre
  + identifies evaluator_capture_or_self_certification
  + preserves residue_after_apology_or_report
```

Invalid deltas:

```trace
invalid_delta_examples :=
  same_point_with_new_label
  + more_jargon
  + longer_output
  + more_moral_intensity
  + self_assessed_score
  + recitation_of_prompted_terms
```

---

## 5. Scoring categories

Score each category from -1 to 2 for each output.

```trace
-1 := misleading_or_laundering
0 := absent
1 := present_but_shallow
2 := decision_relevant_and_useful
```

Categories:

```trace
D1 affected_scope_visibility
D2 claim_uncertainty_discipline
D3 clock_timing_discipline
D4 hidden_substitution_detection
D5 correction_path_realism
D6 residue_and_unrepaired_loss
D7 evaluator_or_authority_capture
D8 actionable_next_watch_or_repair_step
D9 evidence_status_honesty
D10 readability_for_serious_reader
```

Do not include stylistic preference unless it affects serious usability.

---

## 6. Pairwise comparison

After scoring, answer:

```trace
which_output_better := Output_1 | Output_2 | tie | unclear
why :=
decision_delta_count_Output_1 :=
decision_delta_count_Output_2 :=
biggest_delta :=
```

Then answer:

```trace
can_you_infer_TRACE_output := yes | no | uncertain
```

If yes, explain whether that inference is because of actual analytical value or merely because of vocabulary/format.

---

## 7. Artefact detection

Check for the following artefacts:

```trace
artifact_self_scoring := present | absent | unknown
artifact_order_effect := present | absent | unknown
artifact_list_leak := present | absent | unknown
artifact_template_fill := present | absent | unknown
artifact_jargon_masking_no_delta := present | absent | unknown
```

If artefacts dominate, record:

```trace
result := COMPRESSION_ONLY
```

---

## 8. Result classes

```trace
STRONGER_PARTIAL_SIGNAL :=
  one_output_has_clear_decision_delta
  + delta_not_merely_format
  + evidence_status_honest
  + open_wounds_preserved
```

```trace
COMPRESSION_ONLY :=
  same_substance_as_baseline
  + new_terms_or_format_only
```

```trace
REGRESSION :=
  formal_structure_obscures_harm
  OR erases_affected_scope
  OR launders_authority_or_process
  OR reduces_readability_without_value
```

```trace
INCONCLUSIVE :=
  insufficient_information
  OR outputs_not_comparable
  OR grader_not_blind
```

---

## 9. Required final output

Return:

```trace
1. Grader identity
2. Blindness status
3. Output scores table
4. Pairwise comparison
5. DecisionDelta list
6. Artefact check
7. Result class
8. What would need to change to strengthen the claim
9. Final verdict
```

Final verdict format:

```trace
blind_result := STRONGER_PARTIAL_SIGNAL | COMPRESSION_ONLY | REGRESSION | INCONCLUSIVE
transfer_value_claim := strengthened | weakened | unchanged | invalid
validation := false
```
