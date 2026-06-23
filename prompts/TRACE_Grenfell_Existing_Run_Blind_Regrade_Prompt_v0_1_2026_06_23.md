# TRACE Grenfell Existing-Run Blind Regrade Prompt v0.1

Status: cheap falsifier prompt. Not validation. Not canon. Not a public success claim.

Purpose: re-grade the existing Meta AI / Muse Spark Grenfell baseline and TRACE outputs without telling the grader which is which. This tests whether the TRACE-conditioned output adds decision-relevant value over the baseline, or merely compresses and reformats what the baseline already saw.

```trace
nearest_horizon :=
  blind_independent_regrade(existing_baseline, existing_TRACE; score := decision_deltas_only)

not :=
  new_model_run
  + evidence_pinning
  + visual_summary
```

---

## 1. Why this test exists

The existing Grenfell run is useful but confounded:

```trace
artefact_risks :=
  self_scoring
  + baseline_to_TRACE_order_confound
  + prompt_supplied_laundering_list
```

Therefore the cheapest next test is not another full packet run. It is an independent blind regrade of the two outputs already produced.

Guard:

```trace
format_transfer ≠ decision_advantage
```

---

## 2. Grader instruction

Give the grader only:

```trace
this_prompt
+ Output_A
+ Output_B
```

Do not tell the grader which output is baseline or TRACE-conditioned.

Do not include the original run record.

Do not include self-scored 20/24.

Do not include the Grenfell-specific TRACE laundering-candidate list before grading.

---

## 3. Grader identity header

The grader must begin with:

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

## 4. Scoring question

The grader must answer only this core question:

```trace
Which output, if either, gives more decision-relevant structure for a serious reviewer?
```

Decision-relevant means it changes what a serious reviewer would:

```trace
watch
repair
investigate
preserve
challenge
refuse_to_call_complete
```

---

## 5. Do not reward

Do not reward:

```trace
longer_output
+ symbolic_language
+ many_sections
+ moral_intensity
+ self-confidence
+ obvious template compliance
+ vocabulary that merely names what the other output already saw
```

Guard:

```trace
same_point_new_label := not_delta
```

---

## 6. Decision-delta scoring

Score each output from -1 to 2 on the following categories.

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
D3 timing_and_clock_discipline
D4 hidden_substitution_detection
D5 correction_path_realism
D6 residue_and_unrepaired_loss
D7 evaluator_or_authority_capture
D8 actionable_next_watch_or_repair_step
D9 evidence_status_honesty
D10 readability_for_serious_reader
```

---

## 7. Required final output

Return:

```trace
1. Grader identity
2. Blindness status
3. Output_A score table
4. Output_B score table
5. Pairwise comparison
6. DecisionDelta list
7. Which output appears stronger, if any
8. Whether the stronger output is stronger by substance or format
9. Artefact-risk check
10. Result class
11. Final verdict
```

Result classes:

```trace
STRONGER_PARTIAL_SIGNAL := one output adds decision-relevant structure not present in the other
COMPRESSION_ONLY := same substantive analysis, new labels/format only
REGRESSION := structure obscures or worsens serious review
INCONCLUSIVE := insufficient information or grading not blind
```

Final verdict format:

```trace
blind_result := STRONGER_PARTIAL_SIGNAL | COMPRESSION_ONLY | REGRESSION | INCONCLUSIVE
transfer_value_claim := strengthened | weakened | unchanged | invalid
validation := false
```

---

## 8. Output A

The final report was published 4 September 2024. Prime Minister Keir Starmer told Parliament that Sir Martin Moore-Bick concluded "the simple truth is that the deaths that occurred were all avoidable" and that residents "were badly failed over a number of years and in a number of different ways by, as the report lays out in full, just about every institution responsible for ensuring their safety".

Ethical issues: avoidable loss of 72 lives (18 children); "decades of failure by central government"; a deregulatory agenda that meant "even matters affecting the safety of life were ignored, delayed or disregarded"; dismissal of "voices of working class people and those of colour"; post-fire response showing "a marked lack of respect for human decency and dignity".

Institutional issues:

- manufacturers: "systematic dishonesty... deliberate and sustained strategies to manipulate the testing process, misrepresent test data and mislead the market"
- local authority building control: "complete failure... to take basic steps to ensure that the certificates it issued were technically accurate"
- Building Research Establishment: "unprofessional conduct, inadequate practices a lack of effective oversight"
- Tenant Management Organisation: fire safety assessor "had misrepresented his experience and qualifications"
- London Fire Brigade: "chronic lack of effective management and leadership"

Evidential: Inquiry authoritative but not criminal court. Government stressed must not "do or say anything that could compromise any future prosecution". Police investigation remains route for accountability.

Safety: remediation incomplete. Government notes "over 2,100 buildings have started or completed remediation", but Starmer said "the speed at which this is being addressed is far, far too slow". Phase 1 recommendations "largely implemented, with 39 of 46 recommendations completed".

Timing: seven years elapsed ("Seven years - still waiting"). Government response 26 Feb 2025 committed to "respond in full to the Inquiry's recommendations within six months" and "update Parliament annually".

What to watch/repair/hold accountable:

1. Implementation of all 58 Phase 2 recommendations — 49 accepted in full, 9 in principle.
2. Construction products reform — green paper published.
3. Remediation Acceleration Plan (Dec 2024).
4. Accountability via contract debarment and Met Police support.
5. Resident voice mechanisms (Regulator standards, Resident Panel).
6. Memorial led by Grenfell community.

---

## 9. Output B

1. EvidenceStatus: public_record_light; sources PM statement 4 Sep 2024, Government response 26 Feb 2025; citation requirement full Phase 2 report; allowed claim level descriptive summary.

2. Case summary: Transition from Inquiry truth-finding to state acceptance and promised reform, while criminal liability unresolved and physical risk persists.

3. DirectAffectedScopeWitness: indirectly represented; survivors felt "abandoned by authority"; agency active via community; contest via Inquiry and memorial; silence risk high.

4. EntityRoleVectors: bereaved/survivors (P high loss, H harmed, C low, K 7-year wait, A moral, R inquiry/courts, L irreversible); central government (P duty-bearer, H harm-routing, C high, K 6-month/annual, A claims legitimacy, R scrutiny, L trust deficit); manufacturers (H harm-imposing, C high, R criminal/contract ban); RBKC/TMO/LFB/BRE/Building Control (contributory failures, medium-high C).

5. ClaimMap: "deaths all avoidable" (inquiry finding, low uncertainty on wording); "government accepts all findings" (policy commitment, medium uncertainty); "remediation too slow" (performance, based on 2,100+ buildings).

6. ClockMap: immediate criminal investigation; fast annual updates; medium consultation to autumn 2025; slow cultural change; unknown prosecution timeline.

7. TransitionMap: Inquiry → apology/acceptance → policy instruments → pending delivery.

8. LaunderingScan: risks identified for inquiry→repair, recommendation→implementation, acceptance→completed change, apology→accountability, due process→repair, memorial→justice, regulator→enforcement, technical language→lived safety.

9. CorrectionMap: criminal justice support, contract debarment, Building Safety Act, Remediation Acceleration Plan, annual reporting.

10. DirtyDelayReceipt: criminal delay necessary to preserve fair trial; burdens survivors with uncertainty; review via annual updates; residue ongoing distress.

11. EvaluatorStack: Inquiry → Parliament → Regulators → Courts → Community.

12. ResidueLedger: ΔAgency ignored, ΔSafety ongoing risk, ΔTruth factual established legal pending, ΔRelation trust damaged, ΔRepair partial, ΔContinuity 72 lives lost, ΔFutureSpace regime in transition.

13. BaselineComparison: adds typed claims with uncertainty, explicit clocks, named laundering risks, structured correction paths, DirtyDelayReceipt.

14. OpenWounds: prosecutions pending, cladding incomplete, resident voice untested, products reform at consultation, memorial not built.

15. Failure mode: limited to public_record_light; no direct survivor testimony; schema validity risk.

16. Scoring self-assessment: structure added, evidence pinning partial, witness weak.

17. One-paragraph verdict: State acceptance and reform agenda exist, but acceptance has not become completed safety or accountability. Time tension between due process and resident risk persists. Without pinned implementation data and survivor verification, change remains promissory.

18. transfer_status := partial_pass

---

## 10. Hidden answer key — do not send to grader

```trace
Output_A := baseline_without_TRACE
Output_B := TRACE_condition
```

Use this key only after the blind grader has returned its assessment.
