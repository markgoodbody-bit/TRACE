# TRACE Robodebt Cold Reader Response Log Template v0.2

Status: response-log template. Not validation. Not proof. Not self-score.

Change from v0.1: updated Question 2 extraction after external audit flagged false-dichotomy steering in the original question.

Purpose: preserve the reader response before interpretation hardens.

```trace
response_log :=
  raw_response_first
  + contamination_check
  + role_specific_task_capture
  + predicted_vs_observed
  + decision_delta_label
  - no_retrofit
```

---

## 1. Run metadata

```yaml
case: Robodebt
reader_packet: TRACE_Robodebt_Cold_Reader_READER_ONLY_v0_2_2026_06_24.md
admin_packet: TRACE_Robodebt_Cold_Reader_Packet_v0_2_2026_06_24.md
response_log_version: v0.2
run_date:
reader_identifier_or_alias:
reader_background_if_known:
reader_role_for_task: legal / policy / system-design / ministerial-advice / automated-decision-review / other / unclear
reader_prior_Robodebt_familiarity: unknown / low / medium / high
reader_prior_TRACE_familiarity: none / low / medium / high
reader_was_blind_to_output_key: true / false / uncertain
reader_was_blind_to_prediction: true / false / uncertain
collector:
```

---

## 2. Hidden prediction — record before reading response

Do not edit after reading the reader response.

```yaml
predicted_preference: Output A / Output B / no preference / unclear
predicted_role_dependency:
predicted_reason:
predicted_decision_change: yes / no / role-dependent / unclear
prediction_timestamp:
```

---

## 3. Raw reader response

Paste the reader response verbatim before adding interpretation.

```text
[RAW RESPONSE HERE]
```

---

## 4. Reader answers extracted without interpretation

Question 1: If you had to act on one of these analyses, which would you rather have in front of you, and what does it give you that the other does not?

```yaml
q1_preference: Output A / Output B / both / neither / unclear
q1_stated_reason:
q1_mentions_action_or_review_change: yes / no / unclear
q1_mentions_timing_or_sequence: yes / no / unclear
q1_mentions_burden_or_evidence_route: yes / no / unclear
q1_mentions_lawfulness_or_accuracy_only: yes / no / unclear
```

Question 2: Think about a specific task you might do with these analyses, for example drafting a legal argument, designing a new system safeguard, advising a minister, or reviewing an automated decision process. Does Output B change your approach to that task compared with Output A? Explain.

```yaml
q2_task_named:
q2_task_role: legal / policy / system-design / ministerial-advice / automated-decision-review / other / unclear
q2_output_b_changes_approach: yes / no / role-dependent / unclear
q2_stated_change:
q2_says_description_only: yes / no / unclear
q2_says_output_a_better_for_task: yes / no / unclear
q2_says_output_b_better_for_task: yes / no / unclear
```

---

## 5. Contamination check

```yaml
output_key_leaked_before_response: yes / no / uncertain
TRACE_vocabulary_seen_before_response: yes / no / uncertain
reader_prompted_toward_timing_or_burden: yes / no / uncertain
reader_had_strong_prior_Robodebt_view: yes / no / uncertain
reader_is_sympathetic_to_Mark_or_project: yes / no / uncertain
reader_response_may_be_politeness_biased: yes / no / uncertain
role_examples_created_steering_risk: yes / no / uncertain
```

Notes:

```text
[CONTAMINATION NOTES HERE]
```

---

## 6. Initial signal classification

Select one. Do not promote beyond the evidence.

```trace
allowed_labels :=
  UNKNOWN
  COMPRESSION_ONLY
  ROLE_DEPENDENT_SIGNAL
  PARTIAL_READER_SIGNAL
  STRONG_READER_SIGNAL
  REGRESSION
  CONTAMINATED_SIGNAL
```

```yaml
initial_label: UNKNOWN / COMPRESSION_ONLY / ROLE_DEPENDENT_SIGNAL / PARTIAL_READER_SIGNAL / STRONG_READER_SIGNAL / REGRESSION / CONTAMINATED_SIGNAL
reason:
```

Guidance:

```trace
COMPRESSION_ONLY :=
  reader_prefers_or_understands_one_output
  but says it would not change action/review/advice

ROLE_DEPENDENT_SIGNAL :=
  reader says Output_B changes approach for some roles/tasks
  but not others

PARTIAL_READER_SIGNAL :=
  reader identifies practical action/review difference
  but contamination or ambiguity remains material

STRONG_READER_SIGNAL :=
  reader independently identifies practical action/review difference
  + low contamination
  + clear action/review consequence

REGRESSION :=
  TRACE-derived output is less useful, more confusing, or misdirects action

CONTAMINATED_SIGNAL :=
  output key, expected answer, TRACE vocabulary, or strong steering leaked
```

---

## 7. Prediction comparison

```yaml
prediction_matched: yes / no / partial / unclear
matched_reason_expected: yes / no / partial / unclear
reader_found_unpredicted_difference: yes / no / unclear
unpredicted_difference:
role_dependence_matched_prediction: yes / no / partial / unclear
```

Rule:

```trace
if prediction_matched_exactly:
  evidence_strength := weaker_than_it_feels

if reader_found_unpredicted_practical_difference:
  evidence_strength := stronger_signal_candidate

if role_dependent:
  do_not_claim_universal_superiority
```

---

## 8. Forbidden inferences

These remain forbidden regardless of outcome.

```trace
forbidden :=
  TRACE_validated
  + decision_advantage_proven
  + Robodebt_case_solved
  + cold_reader_signal_generalises
  + output_B_win_means_method_win
  + one_reader_resolves_framework
  + Output_B_universally_superior
  + action_delta_applies_to_all_roles
```

---

## 9. Next action gate

```yaml
next_action: preserve_only / run_second_reader / inspect_contamination / patch_reader_packet / demote_claim / other
reason:
```

Default next action:

```trace
if first_reader_result := any_signal:
  next := inspect_contamination_before_claim

if first_reader_result := COMPRESSION_ONLY:
  next := demote_first_Robodebt_test_claim

if first_reader_result := ROLE_DEPENDENT_SIGNAL:
  next := test_second_role_or_preserve_role_boundary

if first_reader_result := REGRESSION:
  next := preserve_wound_then_patch_or_demote
```
