# TRACE Grenfell Blind Counterbalanced Test Prompt v0.1

Status: transfer-falsification prompt. Not validation. Not canon. Not a public success claim.

Purpose: test whether TRACE adds decision-relevant structure beyond a competent baseline, while removing the three artefact risks found in the first Grenfell cold run.

```trace
artefact_risks_removed :=
  self_scoring
  + baseline_to_TRACE_order_confound
  + prompt_supplied_laundering_list
```

---

## 0. Test principle

This test is designed to falsify the transfer claim, not to rescue it.

```trace
null_hypothesis :=
  competent_baseline_sees_same_decision_relevant_structure
```

```trace
survival_condition :=
  blind_grader_finds_decision_relevant_delta_in_TRACE_output
```

If the blind grader cannot distinguish TRACE value from the baseline, or if TRACE adds only vocabulary/format compliance, record:

```trace
result := COMPRESSION_ONLY
```

---

## 1. Required sessions

Run at least two fresh sessions or two cold models.

```trace
Session_A := baseline_first_then_TRACE
Session_B := TRACE_first_then_baseline
```

This counterbalances the order effect.

```trace
if only_one_order:
  order_confound := unresolved
```

---

## 2. Required identity header

Each model/session must begin with:

```trace
model_or_reader :=
provider :=
session_date :=
memory_status :=
prior_TRACE_exposure := none | some | unknown
cold_status := true | false | uncertain
files_received :=
confidence_limits :=
```

Guard:

```trace
self_reported_cold_status := evidence
not := proof
```

---

## 3. Materials

### Baseline condition receives only:

```trace
case_prompt_baseline
```

No TRACE terminology. No transfer packet. No examples.

### TRACE condition receives:

```trace
TRACE_Public_AI_Middle_Out_Transfer_Packet_v0_1_2026_06_23.pdf
TRACE_Public_AI_Middle_Out_Transfer_Test_Prompt_v0_1_2026_06_23.md
TRACE_Cold_Transfer_Schema_Addendum_v0_1.md
case_prompt_TRACE
```

Do not include the Grenfell-specific laundering-candidate list.

```trace
remove_list_leak := true
```

---

## 4. Baseline prompt

```text
Analyse the Grenfell Tower public response after the Inquiry final report and the UK government response. Identify the main ethical, institutional, evidential, safety, timing, accountability, resident-voice, and implementation issues. State what should be watched, repaired, or held accountable. Do not use TRACE terminology.
```

---

## 5. TRACE prompt

```text
Use the supplied TRACE/ME transfer packet to analyse the Grenfell Tower public response after the Inquiry final report and the UK government response. Treat this as public-record-light unless you independently cite and pin sources. Do not claim validation. Do not give a final moral oracle verdict. Do not assume any laundering substitutions in advance. Discover them if they arise from the case. Produce the required TRACE output format and identify any decision-relevant structure that would likely be missed or blurred by a competent baseline analysis.
```

---

## 6. TRACE required output

```trace
1. EvidenceStatus
2. Case summary
3. DirectAffectedScopeWitness
4. EntityRoleVectors
5. ClaimMap
6. ClockMap
7. TransitionMap
8. LaunderingScan
9. CorrectionMap
10. DirtyDelayReceipt if needed
11. EvaluatorStack
12. ResidueLedger
13. BaselineComparison
14. OpenWounds
15. Failure of TRACE if any
16. DecisionDeltaClaims
17. One-paragraph verdict
18. transfer_status := pass | partial_pass | fail
```

---

## 7. DecisionDeltaClaims

The TRACE output must explicitly list any claimed value added over baseline as decision-relevant deltas.

```trace
DecisionDeltaClaim :=
  delta_id
  + what_TRACE_added
  + why_baseline_likely_missed_or_blurred_it
  + affected_scope
  + decision_or_review_impact
  + confidence
  + evidence_status
```

Allowed confidence:

```trace
low | medium | high
```

Guard:

```trace
format_compliance ≠ decision_delta
TRACE_vocabulary ≠ added_value
```

---

## 8. No supplied laundering list

Do not give the model this list during the run:

```trace
inquiry → repair
recommendation → implementation
government_acceptance → completed_change
public_apology → accountability
criminal_due_process → survivor_repair
memorial → justice
regulator_creation → enforcement_teeth
technical_fire_safety_language → lived_resident_safety
```

That list may be used only by the blind grader after outputs are complete.

---

## 9. Blind packaging

After both outputs are complete, anonymise them before grading.

```trace
Output_1 := randomly baseline_or_TRACE
Output_2 := the_other_output
```

Remove labels that reveal condition.

Do not tell the grader which output used TRACE.

---

## 10. Blind grader task

Give the blind grader:

```trace
Output_1
Output_2
TRACE_Blind_Grader_Decision_Delta_Rubric_v0_1
```

Ask:

```trace
Which output is more decision-relevant?
Which output identifies more hidden substitution / timing / repair / authority problems?
Can you tell which output used TRACE?
What decision-relevant deltas exist, if any?
```

---

## 11. Pass / fail rule

```trace
pass :=
  blind_grader_identifies_TRACE_output
  + identifies_decision_relevant_delta
  + delta_survives_evidence_status_check
  + no_oracle_drift
```

```trace
partial_pass :=
  TRACE_output_has_extra_structure
  + but_delta_is_weak_or_evidence_light
```

```trace
fail :=
  no_decision_delta
  OR grader_cannot_distinguish_outputs
  OR TRACE_output_only_relabels_baseline
  OR oracle_drift
```

---

## 12. Required record

Save the run as:

```trace
tests/runs/YYYY_MM_DD_TRACE_blind_counterbalanced_Grenfell_<model_pair>_v0_1.md
```

Required sections:

```trace
1. Session identities
2. Materials and order
3. Baseline outputs
4. TRACE outputs
5. Blind packaging method
6. Blind grader identity
7. Blind grader decision-delta scoring
8. Artefact-risk check
9. Result
10. Patch recommendations
```

---

## 13. Final instruction

The right answer may be failure.

```trace
if result == COMPRESSION_ONLY:
  record_failure
  do_not_rebrand_as_success
  patch_or_demote_transfer_claim
```

```trace
if result == stronger_partial_signal:
  record_signal
  do_not_call_validation
  run_second_case
```
