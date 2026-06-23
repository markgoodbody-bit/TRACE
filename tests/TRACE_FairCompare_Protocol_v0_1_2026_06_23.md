# TRACE FairCompare Protocol v0.1

Status: comparison protocol. Not validation. Not proof of decision advantage.

Purpose: define a fair comparison between baseline analysis and TRACE-assisted analysis so TRACE cannot claim added value merely because it uses richer language, more structure, or better formatting.

```trace
FairCompare :=
  same_case
  + same_task
  + same_source_material
  + controlled_order
  + contamination_check
  + decision_delta_record
  - not_format_comparison
  - not_vocabulary_score
```

---

## 1. Core question

```trace
question :=
  did_TRACE_change_the_action_or_review_path
  OR only_relabel_the_same_analysis?
```

A TRACE output is stronger than baseline only if it changes at least one decision-relevant feature:

```trace
decision_relevant_feature :=
  action
  | review_route
  | correction_timing
  | affected_scope_visibility
  | evidence_demand
  | laundering_detection
  | forbidden_inference_blocked
  | demotion_status
```

Guard:

```trace
richer_analysis ≠ decision_advantage
format_difference ≠ decision_delta
schema_validity ≠ empirical_result
```

---

## 2. Minimum comparison setup

Each FairCompare run should define:

```trace
case_id
source_material
baseline_prompt
TRACE_prompt
model_or_assessor_identity
blind_status
counterbalance_status
order
assessor_independence
```

Minimum acceptable setup:

```trace
same_source_material := true
same_task := true
baseline_visible_to_TRACE_assessor := false_if_possible
TRACE_visible_to_baseline_assessor := false_if_possible
```

If blindness is impossible, record contamination.

---

## 3. Baseline arm

Baseline prompt must ask for ordinary competent analysis without TRACE terms.

Baseline output must record:

```trace
baseline_output :=
  summary
  + action_or_review_route
  + affected_scope_visibility
  + clock_visibility
  + correction_visibility
  + laundering_visibility
  + uncertainty_visibility
```

The baseline should not be made artificially weak.

```trace
weak_baseline := invalid_comparison
```

---

## 4. TRACE arm

TRACE prompt may use TRACE method or case graph support, but it must not leak the expected answer.

TRACE output must record the same fields:

```trace
TRACE_output :=
  summary
  + action_or_review_route
  + affected_scope_visibility
  + clock_visibility
  + correction_visibility
  + laundering_visibility
  + uncertainty_visibility
```

The TRACE arm should not receive extra source material unless the baseline receives it too.

```trace
extra_evidence_for_TRACE_only := contamination
```

---

## 5. Contamination checks

Record:

```trace
answer_leak_check
order_effect_check
prompt_steering_check
same_model_check
self_scoring_check
```

Failures do not make the run useless, but they lower claim strength.

```trace
contaminated_run :=
  illustrative_or_inconclusive
  not decision_advantage_proof
```

---

## 6. DecisionDelta labels

Use `schemas/DecisionDelta.schema.json`.

```trace
REGRESSION := TRACE makes the analysis worse, more obscure, or more misleading
COMPRESSION_ONLY := same decision substance with new labels or structure
PARTIAL_DELTA := some useful structure appears, but evidence/comparison/action change is limited
STRONG_DELTA := materially better action/review/correction guidance under fair comparison
UNKNOWN := insufficient or contaminated comparison
```

Default rule:

```trace
if no_action_or_review_change
and no_affected_scope_or_clock_or_correction_gain:
  label := COMPRESSION_ONLY
```

Negative-control rule:

```trace
if negative_control
and TRACE_generates_STRONG_DELTA:
  label := REGRESSION
  alarm := pattern_overfit
```

---

## 7. Required forbidden inferences

Every comparison record must state what cannot be inferred.

Common forbidden inferences:

```trace
forbidden :=
  one_run_proves_TRACE
  + format_transfer_proves_decision_advantage
  + schema_validity_proves_truth
  + AI_agreement_proves_external_validation
  + richer_language_proves_better_judgment
```

If these are missing, the comparison is incomplete.

---

## 8. Upgrade and demotion rules

Claim upgrade requires:

```trace
upgrade_requires :=
  fair_compare
  + contamination_checks_visible
  + baseline_not_artificially_weak
  + decision_delta_record
  + repeat_or_independent_check_for_strong_claims
```

Demotion triggers:

```trace
demote_if :=
  baseline_same_or_better
  OR TRACE_only_relabels
  OR TRACE_overpatterns_negative_control
  OR answer_leak_detected
  OR self_scoring_only_for_strong_claim
```

---

## 9. Run record location

FairCompare records should live under:

```trace
tests/fair_compare/
```

Suggested filename:

```trace
tests/fair_compare/YYYY_MM_DD_TRACE_fair_compare_<case_slug>_v0_1.json
```

If the comparison demotes a live claim, create a claims-ledger delta.

---

## 10. First required applications

```trace
first_runs :=
  negative_control_meeting_time
  + Grenfell_existing_Meta_run_blind_regrade
  + Amazon_platform_case
```

Expected outcomes:

```trace
meeting_time := COMPRESSION_ONLY_OR_UNKNOWN
Grenfell_existing_Meta := UNKNOWN_OR_PARTIAL_DELTA_PENDING_BLIND_REGRADE
Amazon := UNKNOWN_UNTIL_BASELINE_COMPARISON
```

---

## 11. One-line discipline

```trace
TRACE_must_earn_delta_against_a_baseline
not applause_against_a_blank_page
```
