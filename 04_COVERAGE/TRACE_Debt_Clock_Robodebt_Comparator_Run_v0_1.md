# TRACE Debt Clock — Robodebt Comparator Run v0.1

Date: 2026-06-18
Status: source-backed comparator run / candidate-pressure artifact / not validation / not proof / not operator promotion / not Kernel v0.3

## 0. Control header

This file completes the first source-backed comparator run proposed in `TRACE_Debt_Clock_Comparator_Queue_v0_1.md`.

It does not promote `debt_clock`.

It does not validate TRACE.

It does not create Kernel v0.3.

It does not use AI agreement as evidence.

It does not treat the comparator queue as evidence.

It does not use actor documents as independent confirmation.

```trace
run_scope :=
  Robodebt
  against:
    administrative_review
    + administrative_burden
    + poverty_law
    + automatic_stay_or_relief_against_forfeiture_analogue

run_result :=
  retain_as_candidate_narrowed
  + high_demoter_pressure
  - promotion
  - validation
```

## 1. Candidate under test

```trace
debt_clock :=
  obligation_or_claim_against_subject
  + time_pressure
  + compounding_burden_or_constraint
  + correction_route_slower_than_hardening
```

Plain version:

Debt Clock asks whether a debt or debt-like claim creates pressure that hardens faster than the affected person can realistically contest, correct, pause, or repair it.

The current test is not whether Robodebt was bad. That is already established by stronger sources. The test is whether Debt Clock adds anything beyond existing fields.

## 2. Source hierarchy and evidence rules

Preferred sources for this run:

1. Royal Commission into the Robodebt Scheme, Report page and recommendations.
2. Commonwealth Ombudsman, `Centrelink's automated debt raising and recovery system` report, April 2017.
3. Court / legal material where available.
4. Non-actor journalism or advocacy only where official/legal material is unavailable or used to locate a claim.
5. Actor documents only for actor position, system mechanics, or chronology — not for independent confirmation.

```trace
actor_document_rule :=
  actor_document_may_show:
    actor_claim
    + actor_process
    + actor_chronology
  but_not:
    independent_confirmation_of_legality
    + independent_confirmation_of_harm_absence
    + independent_confirmation_of_repair_adequacy
```

Core source anchors used:

- Royal Commission report page: https://robodebt.royalcommission.gov.au/publications/report
- Commonwealth Ombudsman 2017 report: https://www.ombudsman.gov.au/__data/assets/pdf_file/0022/43528/Report-Centrelinks-automated-debt-raising-and-recovery-system-April-2017.pdf
- 11 U.S.C. § 362 automatic stay: https://www.law.cornell.edu/uscode/text/11/362
- Secondary reporting on post-admission recovery continuation: https://www.theguardian.com/australia-news/2021/may/05/robodebt-victims-referred-to-debt-collectors-even-after-government-admitted-scheme-was-unlawful
- Secondary reporting on the Amato concession / income averaging issue: https://www.theguardian.com/australia-news/2019/dec/13/robodebt-private-information-may-have-been-improperly-handed-to-debt-collectors

## 3. Source-backed Robodebt baseline

The Royal Commission report was tabled on 7 July 2023 and records recommendations across effects on individuals, vulnerability, advocacy and legal services, automated decision-making, debt recovery, AAT/administrative review, and Ombudsman reform.

The Royal Commission's debt-recovery recommendation is the closest Robodebt-side source for Debt Clock. Recommendation 18.1 says Services Australia should develop comprehensive debt-recovery policy, treat recipients fairly and with dignity, consider each person's circumstances, and — subject to express legal authority — refrain from commencing or continuing recovery while a debt is being reviewed or disputed.

The Ombudsman 2017 report gives the early system mechanics. It says the OCI matched Centrelink earnings records with ATO employer-reported income, shifted parts of the prior manual process into an automated process, and, if the customer did not engage or gaps remained, filled those gaps with fortnightly income derived from averaged ATO data.

The Ombudsman also identified burdens relevant to this comparator run: unclear initial messaging, lack of crucial information such as a compliance phone number, people not realising income would be averaged if they did not enter fortnightly income, problems gathering old employment evidence, poor service delivery, long wait times, unclear explanations, and the need for more support for vulnerable customers.

The automatic-stay comparator is not Robodebt law. It is an analogue. Under 11 U.S.C. § 362, a bankruptcy petition generally operates as a stay of actions to recover pre-petition claims and acts to collect, assess, or recover those claims, while also allowing parties in interest to seek relief from stay for cause, including lack of adequate protection. This gives a clean legal comparator for "pause first, contested enforcement later under supervision."

## 4. Comparator lane 1 — Administrative review

### 4.1 What administrative review already explains

Administrative review already explains most of the public-law failure surface:

- review rights;
- internal review;
- tribunal / AAT review;
- procedural fairness;
- model-litigant obligations;
- escalation of significant legal issues;
- publication or visibility of significant review decisions;
- correction of administrative error.

The Royal Commission's AAT recommendations already address this field directly: systems for identifying significant AAT cases, training legal officers, identifying significant AAT decisions, publishing first-instance social security decisions with significant legal or policy implications, and reinstating an Administrative Review Council or equivalent.

```trace
administrative_review_already_sees :=
  formal_review_path
  + significant_case_escalation
  + tribunal_signal_visibility
  + model_litigant_pressure
  + published_decision_need
```

### 4.2 What Debt Clock might add

Debt Clock adds, at most, a liveness question:

```trace
Debt_Clock_delta_admin_review :=
  review_exists
  but:
    recovery_pressure_may_continue
    + correction_may_arrive_after_debt_hardens
```

Plain version:

Administrative review can tell us that a review route exists or should have worked. Debt Clock asks whether debt recovery, repayment, referral, hardship, stress, or evidentiary loss advances faster than that review route.

### 4.3 What would make Debt Clock redundant

Debt Clock is redundant in this lane if administrative review doctrine/practice already requires the live timing test:

```trace
admin_review_redundancy_condition :=
  review_available
  + recovery_paused_during_dispute
  + hardship_considered_before_recovery
  + significant_legal_issue_escalated
  + correction_before_material_hardening
```

Royal Commission recommendation 18.1 already gets very close to this by prescribing non-commencement or non-continuation of recovery during review/dispute, subject to legal authority. That is a strong demoter.

### 4.4 Lane result

```trace
lane_1_result :=
  Debt_Clock_adds_clear_question
  but:
    administrative_review_plus_debt_recovery_pause
    already_covers_much_of_the_work

lane_1_status := high_demoter_pressure
```

Administrative review does not fully erase Debt Clock, but it narrows it. The candidate cannot claim novelty here. It survives only as a compact timing check: review must be live before recovery hardens harm.

## 5. Comparator lane 2 — Administrative burden

### 5.1 What administrative burden already explains

Administrative burden already explains:

- learning costs;
- compliance costs;
- psychological costs;
- burden-shifting;
- friction as policy design;
- unequal impact;
- access failure;
- state-created obstacle courses.

The Ombudsman report is a strong Robodebt example of administrative burden. It identified unclear messaging, poor system usability, difficulty obtaining older employment-income evidence, inadequate communication, long wait times, and the need for extra support for vulnerable people.

```trace
administrative_burden_already_sees :=
  learning_cost
  + compliance_cost
  + psychological_cost
  + evidence_gathering_burden
  + service_access_failure
  + vulnerability_interaction
```

### 5.2 What Debt Clock might add

Debt Clock may add a temporal coupling:

```trace
Debt_Clock_delta_admin_burden :=
  administrative_burden
  + debt_recovery_timer
  + correction_delay
  -> burden_hardens_before_subject_can_correct
```

Plain version:

Administrative burden explains why the person struggles to contest. Debt Clock asks what happens when that burden operates under a running recovery clock.

### 5.3 What would make Debt Clock redundant

Debt Clock is redundant if administrative burden analysis already captures:

```trace
burden_redundancy_condition :=
  required_steps
  + burden_intensity
  + time_limit
  + recovery_escalation
  + correction_delay
  + hardship_consequence
  + pause_or_non_pause_during_dispute
```

If the burden field is applied with explicit time and recovery consequences, Debt Clock becomes a relabel.

### 5.4 Lane result

```trace
lane_2_result :=
  narrow_survival
  because:
    burden_field_explains_friction
    but_debt_clock_may_force_timer_visibility

lane_2_status := retain_as_candidate_only
```

Debt Clock survives here only as a clocking discipline attached to administrative burden. It does not beat the administrative-burden field; it may make one failure dimension harder to miss.

## 6. Comparator lane 3 — Poverty law

### 6.1 What poverty law already explains

Poverty law and welfare-rights practice already explain:

- benefit dependency;
- low financial buffer;
- welfare conditionality;
- overpayment recovery;
- hardship;
- vulnerability;
- legal-aid and community legal-centre importance;
- dignity and stigma;
- the difference between formal rights and usable rights.

The Royal Commission recommendations on design for the people served, vulnerability identification, advocacy access, legal-aid/community legal-centre funding, and debt recovery with dignity all sit naturally inside this field.

```trace
poverty_law_already_sees :=
  low_buffer
  + welfare_dependency
  + hardship
  + stigma
  + legal_access_gap
  + vulnerability
  + recovery_as_subsistence_pressure
```

### 6.2 What Debt Clock might add

Debt Clock may add a narrower phrase for timing in welfare-debt cases:

```trace
Debt_Clock_delta_poverty_law :=
  low_buffer_subject
  + asserted_debt
  + recovery_or_collection_pressure
  + slow_review
  -> subsistence_or_agency_window_closes
```

Plain version:

Poverty law explains why debt recovery can be harsher for people without buffer. Debt Clock asks whether recovery moves faster than the person can realistically prove, contest, pause, or repair the debt.

### 6.3 What would make Debt Clock redundant

Debt Clock is redundant if poverty-law / welfare-rights analysis already supplies an operational rule such as:

```trace
poverty_law_redundancy_condition :=
  disputed_welfare_debt_recovery_must_pause
  + hardship_must_be_assessed_before_recovery
  + legal_support_must_be_accessible
  + correction_must_precede_subsistence_harm
```

Royal Commission recommendation 18.1 again creates demoter pressure because it provides the pause-during-review/dispute principle directly.

### 6.4 Lane result

```trace
lane_3_result :=
  Debt_Clock_not_novel_as_poverty_law
  but:
    useful_as_welfare_debt_timing_prompt

lane_3_status := candidate_translation_note
```

In this lane, Debt Clock should be treated as a translation note unless it later outperforms existing poverty-law analysis in a worked case.

## 7. Comparator lane 4 — Automatic stay / relief against forfeiture analogue

### 7.1 What the existing field already explains

Automatic stay and related relief doctrines already explain the strongest version of the Debt Clock shape:

- stop or pause enforcement;
- prevent a race to collection;
- preserve estate/household position;
- allow contested enforcement later;
- provide supervised creditor relief where justified;
- prevent irreversible or disproportionate loss before adjudication.

Under 11 U.S.C. § 362, a bankruptcy petition generally operates as a stay of judicial, administrative, or other proceedings to recover pre-petition claims and of acts to collect, assess, or recover those claims. Section 362 also allows relief from stay after notice and hearing for cause, including lack of adequate protection.

```trace
automatic_stay_already_sees :=
  pause_enforcement
  + preserve_position
  + creditor_relief_path
  + court_supervision
  + enforcement_after_threshold
```

### 7.2 What Debt Clock might add

Debt Clock may add cross-domain translation where automatic stay does not legally apply:

```trace
Debt_Clock_delta_stay :=
  automatic_stay_logic
  translated_to:
    administrative_debt
    + welfare_debt
    + algorithmic_debt
    + informal_debt_pressure
```

Plain version:

Debt Clock is useful only if it helps ask whether a non-bankruptcy debt system needs a stay-like pause before recovery hardens harm.

### 7.3 What would make Debt Clock redundant

This lane is the strongest demoter. Debt Clock becomes redundant if the right answer is simply:

```trace
demote_to_stay_analogue :=
  install_or_require_automatic_stay_like_pause
  when:
    debt_is_disputed
    OR legality_uncertain
    OR hardship_active
    OR review_pending
```

If automatic-stay / relief-against-forfeiture analogies already provide the cleaner legal architecture, Debt Clock should not become an operator.

### 7.4 Lane result

```trace
lane_4_result := strongest_demoter

Debt_Clock_survives_only_as :=
  cross_domain_prompt_for_stay_like_pause
  - legal_doctrine
  - operator
```

This lane sharply narrows Debt Clock. The automatic stay analogue already expresses the deepest legal structure: stop enforcement before correction loses meaning, but preserve a supervised route for legitimate enforcement.

## 8. Cross-lane result

```trace
cross_lane_result :=
  administrative_review := high_demoter_pressure
  administrative_burden := partial_survival_as_timer_visibility
  poverty_law := translation_note_pressure
  automatic_stay := strongest_demoter

Debt_Clock_result :=
  retain_as_candidate_narrowed
  + demote_pressure_high
  - promote
  - validate
```

Debt Clock does not currently earn operator status.

It does earn a narrowed candidate role:

```trace
Debt_Clock_narrowed :=
  portable_timing_question_for_debt_like_pressure:
    does_recovery_or_collection_harden
    before_correction_or_pause_reaches_subject?
```

This is useful because it forces a specific timing question across administrative, welfare, algorithmic, and debt-recovery settings. It is not yet distinctive enough to promote. It may later demote to an automatic-stay analogue note or merge into correction-before-hardening.

## 9. What Debt Clock might add, if anything

Debt Clock's best surviving remainder is not a new doctrine. It is a portable diagnostic question:

```trace
surviving_remainder :=
  debt_or_debt_like_claim
  + recovery_pressure
  + subject_low_buffer_or_high_burden
  + correction_slow
  + no_pause_mechanism
  -> hardening_before_review
```

Plain version:

The candidate may help readers ask whether a debt process has a live pause before review becomes merely post-hoc repair.

That is a useful question. It is not enough for operator promotion.

## 10. Demotion triggers after this run

Demote or merge Debt Clock if any of the following occurs in the next pressure test:

```trace
demote_or_merge_if :=
  administrative_review_with_interim_relief_covers_it
  OR administrative_burden_with_timing_covers_it
  OR poverty_law_with_hardship_pause_covers_it
  OR automatic_stay_analogue_covers_it
  OR Debt_Clock_only_relabels_correction_before_hardening
  OR no_case_shows_better_navigation_than_existing_fields
```

## 11. Required next test

The next test should not be more theory.

It should be one worked comparison:

```trace
next_test :=
  one_Robodebt_sequence
  + ordinary_admin_review_read
  + administrative_burden_read
  + poverty_law_read
  + automatic_stay_analogue_read
  + Debt_Clock_read
  + explicit_delta_or_demotion
```

The key question:

```trace
worked_delta_question :=
  did_Debt_Clock_catch_any_live_timing_failure
  that_the_existing_fields_missed
  with_source_backing?
```

If not, demote.

## 12. Stop rules preserved

```trace
stop_rules :=
  no_TRACE_validation
  + no_Debt_Clock_promotion
  + no_Kernel_v0_3
  + no_AI_agreement_as_evidence
  + no_actor_document_as_independent_confirmation
  + no_story_as_evidence
  + no_queue_as_evidence
```

## 13. Final compression

```trace
Debt_Clock_v0_1_run :=
  completed_source_backed_comparator_run
  + Robodebt_as_case
  + four_lane_pressure
  + narrow_candidate_survival
  + strongest_demoter := automatic_stay_analogue
  + next_required := worked_navigation_delta
  - operator_promotion
  - TRACE_validation
```

Plain conclusion:

Debt Clock survives this run only as a narrow candidate diagnostic: a portable question about whether debt-like pressure hardens faster than correction or pause can reach the subject. Existing fields already explain most of the Robodebt failure. Automatic-stay / relief-against-forfeiture logic is the strongest comparator and may ultimately demote Debt Clock into a legal-analogue note rather than an operator.

End.
