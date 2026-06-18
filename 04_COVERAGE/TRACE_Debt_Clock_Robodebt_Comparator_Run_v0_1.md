# TRACE Debt Clock — Robodebt Comparator Run v0.1

Date: 2026-06-18
Status: source-scoped comparator mapping / demotion record / translation note / not validation / not proof / not operator promotion / not Kernel v0.3

## 0. Control header

This file records the first source-scoped comparator mapping proposed in `TRACE_Debt_Clock_Comparator_Queue_v0_1.md`.

It does not promote `debt_clock`.

It demotes `debt_clock` from pending candidate to translation note.

It does not validate TRACE.

It does not create Kernel v0.3.

It does not use AI agreement as evidence.

It does not treat the comparator queue as evidence.

It does not use actor documents as independent confirmation.

The prior version concluded `retain_as_candidate_narrowed`. Claude hostile audit identified that as too generous: the surviving remainder was only `correction_before_hardening` re-scoped to debt, and the file met its own relabel/demotion trigger. This revision accepts that hostile audit pressure as a correction, not as validation.

```trace
run_scope :=
  Robodebt
  against:
    administrative_review
    + administrative_burden
    + poverty_law
    + automatic_stay_or_relief_against_forfeiture_analogue

run_result :=
  demote_to_translation_note
  + merge_target := correction_before_hardening
  + legal_analogue_note := automatic_stay_or_stay_like_pause
  - promotion
  - validation
```

## 1. Candidate under test

Original candidate definition:

```trace
debt_clock :=
  obligation_or_claim_against_subject
  + time_pressure
  + compounding_burden_or_constraint
  + correction_route_slower_than_hardening
```

Plain version:

Debt Clock asked whether a debt or debt-like claim creates pressure that hardens faster than the affected person can realistically contest, correct, pause, or repair it.

The test was not whether Robodebt was bad. That is already established by stronger sources. The test was whether Debt Clock added anything beyond existing fields.

The result is demotion:

```trace
Debt_Clock_after_run :=
  correction_before_hardening(debt_scoped)
  + stay_like_pause_translation
  - standalone_candidate_operator
```

## 2. Source hierarchy and evidence rules

Preferred source classes for this run:

1. Royal Commission into the Robodebt Scheme, report page and recommendations.
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

Core source anchors used or discussed:

- Royal Commission report page and recommendations: https://robodebt.royalcommission.gov.au/publications/report
- Commonwealth Ombudsman 2017 report: https://www.ombudsman.gov.au/__data/assets/pdf_file/0022/43528/Report-Centrelinks-automated-debt-raising-and-recovery-system-April-2017.pdf
- 11 U.S.C. § 362 automatic stay: https://www.law.cornell.edu/uscode/text/11/362
- Secondary reporting on post-admission recovery continuation: https://www.theguardian.com/australia-news/2021/may/05/robodebt-victims-referred-to-debt-collectors-even-after-government-admitted-scheme-was-unlawful
- Secondary reporting on debt-collector / private-information concern; not an Amato pinpoint and should not be used for that claim without relabelling: https://www.theguardian.com/australia-news/2019/dec/13/robodebt-private-information-may-have-been-improperly-handed-to-debt-collectors

Evidence-grade note for this revision:

```trace
evidence_grades_used_here :=
  E4 := official_primary_or_inquiry_source_with_direct_text
  E3 := legal_or_official_source_outside_actor_control
  E2 := secondary_reporting_or_independent_analysis
  E1 := actor_statement_or_unsourced_internal_claim
  E0 := unsupported_or_not_yet_gathered
```

Applied grades:

```trace
source_grades :=
  Royal_Commission_recommendation_18_1 := E4
  Royal_Commission_AAT_recommendations := E4
  Ombudsman_2017_report_for_early_system_mechanics := E4_with_caveat
  USC_362_automatic_stay := E3_cross_jurisdiction_analogue
  Guardian_post_admission_recovery_reporting := E2_not_corroborated_here
  Guardian_private_information_debt_collector_reporting := E2_descriptor_corrected
```

Caveat on the Ombudsman 2017 report:

The Ombudsman report is useful for contemporaneous system mechanics, user-facing friction, and burden descriptions. It should not be treated as a clean final independent confirmation of legality or repair adequacy. Later Robodebt investigations put pressure on what the Ombudsman was told by departments.

## 3. Source-backed Robodebt baseline

The Royal Commission report was tabled on 7 July 2023 and records recommendations across effects on individuals, vulnerability, advocacy and legal services, automated decision-making, debt recovery, AAT/administrative review, and Ombudsman reform.

The Royal Commission's debt-recovery recommendation is the strongest in-context demoter for Debt Clock. Recommendation 18.1 says Services Australia should develop a comprehensive debt-recovery policy and, among other requirements, staff must:

- treat recipients fairly and with dignity before recovery;
- `refrain from commencing or continuing recovery action while a debt is being reviewed or disputed`;
- consider hardship proportionately; and
- give recipients appropriate opportunities to challenge, review, and seek guidance before referral for debt recovery.

That recommendation already expresses much of the timing/pause logic Debt Clock was trying to name.

The Ombudsman 2017 report gives useful early system mechanics. It describes the OCI process as matching Centrelink earnings records with ATO employer-reported income, shifting parts of the prior manual process into an automated process, and, if the customer did not engage or gaps remained, filling those gaps with fortnightly income derived from averaged ATO data.

The Ombudsman report also identifies burden surfaces relevant to this comparator mapping: unclear initial messaging, lack of crucial information such as a compliance phone number, customers not realising income would be averaged if they did not enter fortnightly income, problems gathering old employment evidence, service delivery problems, long wait times, unclear explanations, and need for more support for vulnerable customers.

The automatic-stay comparator is not Robodebt law. It is a cross-jurisdictional analogue from US bankruptcy law. Under 11 U.S.C. § 362, a bankruptcy petition generally operates as a stay of proceedings or acts to recover pre-petition claims, while allowing parties in interest to seek relief from stay for cause. This expresses a clean legal form of pause-before-hardening within bankruptcy. It is not an Australian welfare-debt doctrine.

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
- correction of administrative error;
- interim or pause-like relief where available.

The Royal Commission's AAT recommendations already address this field directly: systems for identifying significant AAT cases, training legal officers, identifying significant AAT decisions, publishing first-instance social security decisions with significant legal or policy implications, and reinstating an Administrative Review Council or equivalent.

```trace
administrative_review_already_sees :=
  formal_review_path
  + significant_case_escalation
  + tribunal_signal_visibility
  + model_litigant_pressure
  + published_decision_need
  + pause_or_interim_relief_question
```

### 4.2 Debt Clock delta after audit

Debt Clock added only a liveness question:

```trace
Debt_Clock_delta_admin_review :=
  review_exists
  but:
    recovery_pressure_may_continue
    + correction_may_arrive_after_debt_hardens
```

That is not a distinct operator. It is administrative review plus correction-before-hardening.

### 4.3 Lane result

```trace
lane_1_result := redundant

reason :=
  administrative_review
  + recovery_pause_during_dispute
  + correction_before_material_hardening
  already_cover_the_live_timing_problem
```

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

The Ombudsman report is a Robodebt example of burden, not a substitute for administrative-burden scholarship.

### 5.2 Debt Clock delta after audit

The prior version asserted that Debt Clock might force timer visibility:

```trace
Debt_Clock_delta_admin_burden :=
  administrative_burden
  + debt_recovery_timer
  + correction_delay
  -> burden_hardens_before_subject_can_correct
```

That remains plausible as a prompt but source-insufficient as a comparator verdict. The file did not cite administrative-burden scholarship strongly enough to adjudicate redundancy.

### 5.3 Lane result

```trace
lane_2_result := weak + source_insufficient

reason :=
  burden_field_not_directly_sourced
  + timer_visibility_remainder_thin
```

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

### 6.2 Debt Clock delta after audit

Debt Clock added a narrower phrase for timing in welfare-debt cases:

```trace
Debt_Clock_delta_poverty_law :=
  low_buffer_subject
  + asserted_debt
  + recovery_or_collection_pressure
  + slow_review
  -> subsistence_or_agency_window_closes
```

That is useful as translation, not as a candidate operator. Poverty law and welfare-rights practice already own the low-buffer/hardship/recovery-pressure problem, and Recommendation 18.1 owns the pause-during-dispute principle in this case.

### 6.3 Lane result

```trace
lane_3_result := redundant_as_operator + translation_note_only
```

## 7. Comparator lane 4 — Automatic stay / relief against forfeiture analogue

### 7.1 What the existing field already explains

Automatic stay and related relief doctrines already explain the strongest abstract version of the Debt Clock shape:

- stop or pause enforcement;
- prevent a race to collection;
- preserve estate/household position;
- allow contested enforcement later;
- provide supervised creditor relief where justified;
- prevent irreversible or disproportionate loss before adjudication.

Under 11 U.S.C. § 362, a bankruptcy petition generally operates as a stay of judicial, administrative, or other proceedings to recover pre-petition claims and of acts to collect, assess, or recover those claims. Section 362 also allows relief from stay after notice and hearing for cause, including lack of adequate protection.

This is cross-jurisdictional and analogical. It should not be over-ranked against the Royal Commission's in-context recovery-pause recommendation.

```trace
automatic_stay_analogue_sees :=
  pause_enforcement
  + preserve_position
  + creditor_relief_path
  + court_supervision
  + enforcement_after_threshold
```

### 7.2 Debt Clock delta after audit

The only surviving Debt Clock contribution would be translation into non-bankruptcy systems:

```trace
Debt_Clock_delta_stay :=
  automatic_stay_logic
  translated_to:
    administrative_debt
    + welfare_debt
    + algorithmic_debt
    + informal_debt_pressure
```

That is not operator-worthy. It is a useful note attached to correction-before-hardening and stay-like pause design.

### 7.3 Lane result

```trace
lane_4_result := redundant_as_operator

Debt_Clock_survives_only_as :=
  stay_like_pause_translation_note
  - legal_doctrine
  - operator
```

## 8. Cross-lane result after hostile audit

```trace
cross_lane_result :=
  administrative_review := redundant
  administrative_burden := weak + source_insufficient
  poverty_law := translation_note_only
  automatic_stay := redundant_as_operator + legal_analogue_note

Debt_Clock_result :=
  demote_to_translation_note
  + merge_target := correction_before_hardening
  + legal_analogue_note := automatic_stay_or_stay_like_pause
  - candidate_operator
  - promote
  - validate
```

Debt Clock does not earn operator status.

Debt Clock no longer remains a pending candidate.

The correct preserved form is:

```trace
Debt_Clock_translation_note :=
  in_debt_or_debt_like_processes:
    ask_whether_recovery_or_collection_hardens
    before_correction_or_pause_reaches_subject
```

Plain version:

Debt Clock is a debt-scoped way to remember correction-before-hardening and the need for stay-like pause in disputed, unlawful, hardship-active, or review-pending debt systems.

## 9. What remains useful

The useful remainder is not a new doctrine. It is a translation note:

```trace
useful_remainder :=
  debt_or_debt_like_claim
  + recovery_pressure
  + low_buffer_or_high_burden_subject
  + correction_slow
  + no_pause_mechanism
  -> apply_correction_before_hardening
     and_consider_stay_like_pause
```

This is a good reminder. It is not a standalone candidate operator.

## 10. Why the prior conclusion was wrong

The prior version said `retain_as_candidate_narrowed`.

That was too generous.

The file's own surviving remainder was:

```trace
does_recovery_or_collection_harden
before_correction_or_pause_reaches_subject?
```

That is simply `correction_before_hardening` re-scoped to debt. It meets the demotion trigger:

```trace
demote_or_merge_if :=
  Debt_Clock_only_relabels_correction_before_hardening
```

Therefore the corrected result is demotion, not narrow survival.

## 11. Missing evidence retained as open, not rescue

The following evidence would be needed for a worked historical delta test. Its absence does not keep Debt Clock alive as a candidate; it explains why no stronger claim can be made.

```trace
needed_for_worked_delta :=
  actual_recovery_timeline
  + review_or_dispute_timeline
  + pause_or_non_pause_during_dispute
  + hardship_or_low_buffer_evidence
  + correction_or_refund_timing
  + source_independence
  + administrative_burden_and_poverty_law_field_sources
  + concrete_definition_of_what_Debt_Clock_caught_that_others_missed
```

A future worked comparison may still be useful, but its default question is now:

```trace
worked_delta_question :=
  does_the_Debt_Clock_translation_note
  catch_any_timing_failure
  not_already_caught_by:
    administrative_review
    + administrative_burden
    + poverty_law
    + stay_like_pause
    + correction_before_hardening?
```

If not, the note can be removed entirely.

## 12. Spine wording drift note

This run does not invoke the Exit branch. It runs on correction-before-hardening / pause logic.

Do not harmonise the unresolved spine wording:

```trace
exit_when_correction_channel_is_harm_carrier
vs
exit_when_correction_channel_is_predatory
```

If Robodebt were later assessed under an Exit branch, the distinction would matter:

```trace
Robodebt_under_harm_carrier := likely_trigger
Robodebt_under_predatory := contestable
```

This comparator run does not resolve that drift.

## 13. Stop rules preserved

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

## 14. Final compression

```trace
Debt_Clock_v0_1_after_hostile_audit :=
  source_scoped_mapping
  + hostile_audit_applied
  + surviving_remainder == correction_before_hardening(debt_scoped)
  + legal_analogue_note := automatic_stay_or_stay_like_pause
  -> demote_to_translation_note
  - candidate_operator
  - promotion
  - validation
```

Plain conclusion:

Debt Clock is demoted. It remains only as a translation note: in debt-like systems, check whether recovery pressure hardens before correction or pause reaches the subject. The primary operator is correction-before-hardening. The closest legal analogue is a stay-like pause. Existing fields already explain most of the Robodebt failure.

End.
