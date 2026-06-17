# TRACE Debt Clock Comparator Queue v0.1

Date: 2026-06-17
Status: comparator queue / candidate-pressure artifact / not validation / not proof / not operator promotion / not Kernel v0.3

## Plain purpose

This file creates the comparator queue required before `debt_clock` can be promoted, demoted, merged, or narrowed.

It does not promote `debt_clock`.

It does not claim novelty.

It exists to make the candidate vulnerable to better existing frameworks.

```trace
Debt_Clock_Comparator_Queue :=
  named_comparators
  + what_they_already_explain
  + possible_TRACE_delta
  + evidence_needed
  + demoters
  - promotion
  - validation
```

## Candidate definition under pressure

```trace
debt_clock :=
  obligation_or_claim_against_subject
  + time_pressure
  + compounding_burden_or_constraint
  + correction_route_slower_than_hardening
```

Plain version:

A debt clock may exist when an obligation or claim against a person creates time pressure and compounding burden, while the route for correcting error or hardship runs slower than the burden hardens.

This is a candidate only.

## Global guardrails

Do not treat all debt as harm.

Do not treat debt collection as inherently illegitimate.

Do not ignore lawful or necessary recovery.

Do not ignore notice, evidence, proportionality, hardship, agency, appeal, error correction, or repair.

Do not claim Robodebt validates Debt Clock.

Do not claim Debt Clock is novel until comparator lanes are checked.

```trace
must_not_claim :=
  all_debt_is_harm
  OR all_collection_is_illegitimate
  OR Robodebt_validates_Debt_Clock
  OR Debt_Clock_is_novel_before_comparator_run
  OR burden_equals_injustice_without_context
```

## Promotion block

```trace
debt_clock_promotion_blocked_until :=
  comparator_queue_exists
  + at_least_one_source_backed_comparator_run_completed
  + candidate_survives_or_demotes
```

This file satisfies only the first condition: `comparator_queue_exists`.

It does not satisfy the comparator-run condition.

## Comparator Lane 1 — Debt Collection Law

### What this comparator already explains

Debt collection law already addresses:

- lawful recovery of obligations;
- notice requirements;
- prohibited collection practices;
- enforcement limits;
- debtor rights;
- dispute procedures;
- limitation periods;
- court or tribunal process;
- remedies for improper collection.

### What TRACE / Debt Clock might add

TRACE may add a timing-focused diagnostic:

```trace
collection_burden_hardens_before_dispute_resolves
```

Possible remainder:

Debt collection law may ask whether the collection is lawful or procedurally proper. Debt Clock asks whether correction can arrive before the debt process hardens harm through penalty, default, credit damage, asset loss, stress, or service exclusion.

### What would show TRACE adds nothing

Demote if debt collection law already provides a clearer and equally usable timing test for:

- dispute-before-enforcement;
- pause-before-penalty;
- hardship-before-escalation;
- correction-before-credit-or-asset harm.

### Evidence needed for comparator run

- statutory or regulatory debt-collection rules;
- dispute timelines;
- enforcement escalation timelines;
- hardship pause rules;
- evidence of actual pause / correction capacity;
- subject-facing appeal cost and delay.

### Demoter / removal condition

```trace
demote_Debt_Clock_if :=
  debt_collection_law_covers_timing_hardening_with_less_distortion
```

## Comparator Lane 2 — Administrative Review

### What this comparator already explains

Administrative review already addresses:

- review rights;
- merits review;
- internal review;
- tribunal appeal;
- procedural fairness;
- correction of administrative error;
- remedy after unlawful or mistaken decisions.

### What TRACE / Debt Clock might add

TRACE may add focus on whether review is fast enough to stop burden hardening.

```trace
review_available_but_late :=
  formal_review_exists
  + debt_burden_hardens_before_review_effective
```

### What would show TRACE adds nothing

Demote if administrative review doctrine/practice already tracks the live burden clock, including interim relief, suspension of recovery, hardship routing, and real correction before debt consequences harden.

### Evidence needed for comparator run

- review pathway steps;
- expected time to review;
- whether recovery pauses automatically;
- whether interest/penalty/credit damage continues;
- availability and use of interim relief;
- repair after successful review.

### Demoter / removal condition

```trace
demote_Debt_Clock_if :=
  administrative_review_already_captures_live_debt_hardening
```

## Comparator Lane 3 — Poverty Law / Welfare Conditionality

### What this comparator already explains

Poverty law and welfare conditionality already address:

- benefit dependency;
- conditional payments;
- overpayment recovery;
- sanctions;
- hardship exemptions;
- vulnerability;
- administrative burden;
- subsistence risk;
- state-created scarcity.

### What TRACE / Debt Clock might add

TRACE may clarify when overpayment, sanction, or recovery processes create clocks that outrun realistic correction.

```trace
subsistence_clock :=
  recovery_or_sanction
  + low_buffer
  + correction_delay
  -> rapid_hardening
```

Possible remainder:

Debt Clock may help distinguish ordinary owed recovery from recovery that functions as an accelerating harm path because the subject lacks buffer and correction is slow.

### What would show TRACE adds nothing

Demote if poverty law and welfare conditionality literature already provide a better operational model of timing, hardship, and correction-before-subsistence harm.

### Evidence needed for comparator run

- recovery/sanction rules;
- benefit dependency evidence;
- hardship exemption process;
- average appeal/review timing;
- immediate subsistence impacts;
- evidence of pause or non-pause during dispute.

### Demoter / removal condition

```trace
demote_Debt_Clock_if :=
  poverty_law_framework_explains_subsistence_timing_better
```

## Comparator Lane 4 — Consumer Credit / Credit Reporting

### What this comparator already explains

Consumer credit and credit reporting already address:

- credit obligations;
- default;
- arrears;
- credit-file reporting;
- dispute mechanisms;
- correction of inaccurate records;
- affordability and responsible lending;
- long-term credit harm.

### What TRACE / Debt Clock might add

TRACE may add explicit attention to when the credit scar occurs before a dispute is resolved.

```trace
credit_scar_clock :=
  disputed_claim
  + reporting_or_default_marker
  + slow_correction
  -> future_option_loss
```

Note: `credit_scar` is not currently promoted. This lane pressures whether it should remain held, merge into Debt Clock, or demote.

### What would show TRACE adds nothing

Demote if credit reporting law and consumer-credit frameworks already supply a clearer liveness test for dispute-before-credit-harm and repair of inaccurate credit damage.

### Evidence needed for comparator run

- reporting thresholds;
- dispute timing;
- default marker consequences;
- correction/removal route;
- downstream option-space harms such as housing, employment, credit access;
- actual time to repair records.

### Demoter / removal condition

```trace
demote_or_merge_if :=
  credit_reporting_framework_covers_clock_better
```

## Comparator Lane 5 — Administrative Burden Literature

### What this comparator already explains

Administrative burden literature already addresses:

- learning costs;
- compliance costs;
- psychological costs;
- burden as policy design;
- rationing through friction;
- take-up failure;
- unequal impact;
- state-created obstacle courses.

### What TRACE / Debt Clock might add

TRACE may add a specific debt-time hardening frame:

```trace
burden_clock :=
  administrative_friction
  + debt_or_recovery_pressure
  + compounding_constraint
  -> correction_too_late
```

Possible remainder:

Administrative burden explains friction and access failure. Debt Clock may focus on how burden interacts with debt escalation timelines and correction delay.

### What would show TRACE adds nothing

Demote if administrative burden literature already covers debt escalation timing, compounding consequences, and live correction in a clearer framework.

### Evidence needed for comparator run

- burden types;
- required steps;
- time limits;
- failure consequences;
- subject capacity and resources;
- correction success rates;
- whether debt consequences pause during burden-heavy dispute.

### Demoter / removal condition

```trace
demote_Debt_Clock_if :=
  administrative_burden_framework_covers_debt_time_pressure_without_TRACE
```

## Comparator Lane 6 — Procedural Justice / Due Process

### What this comparator already explains

Procedural justice and due process already address:

- notice;
- hearing;
- reasons;
- evidence;
- impartial decision-maker;
- opportunity to contest;
- fairness before deprivation;
- legitimacy of process.

### What TRACE / Debt Clock might add

TRACE may add a stricter timing condition:

```trace
due_process_late :=
  hearing_or_review_exists
  + deprivation_or_burden_hardens_first
```

Possible remainder:

Due process may establish whether a contest route exists. Debt Clock asks whether the route operates before debt consequences harden.

### What would show TRACE adds nothing

Demote if procedural justice / due process already contains a live correction-before-hardening test adequate for debt-pressure systems.

### Evidence needed for comparator run

- notice timing;
- hearing timing;
- deprivation/recovery timing;
- pause/suspension availability;
- remedy timing;
- whether post-hoc correction restores the subject's lost options.

### Demoter / removal condition

```trace
demote_Debt_Clock_if :=
  due_process_live_relief_doctrine_covers_same_work_better
```

## Comparator Lane 7 — Financial Hardship / Scarcity Psychology

### What this comparator already explains

Financial hardship and scarcity psychology already address:

- scarcity bandwidth;
- stress and cognitive load;
- compounding disadvantage;
- short-term pressure;
- reduced agency under financial threat;
- limited buffer;
- debt stress and avoidance.

### What TRACE / Debt Clock might add

TRACE may add a correction-path frame:

```trace
scarcity_plus_slow_correction :=
  low_buffer
  + debt_pressure
  + slow_dispute_route
  -> agency_window_closes
```

Possible remainder:

Scarcity psychology explains subject-side pressure. Debt Clock may connect that pressure to institutional correction speed and hardening points.

### What would show TRACE adds nothing

Demote if scarcity psychology and financial hardship frameworks already model the interaction between debt pressure, correction delay, and agency-window collapse better than TRACE.

### Evidence needed for comparator run

- household buffer / income dependency;
- debt amount relative to resources;
- escalation timing;
- cognitive/administrative burden;
- hardship support route;
- actual correction / pause mechanism.

### Demoter / removal condition

```trace
demote_Debt_Clock_if :=
  scarcity_hardship_framework_explains_agency_window_closure_better
```

## First source-backed comparator run candidate

Recommended first run:

```trace
first_run_candidate :=
  Robodebt
  against:
    administrative_review
    + administrative_burden
    + poverty_law
```

Reason:

The repo already has a source-backed Robodebt dry run. That makes it efficient to test whether `debt_clock` adds anything beyond existing administrative review, administrative burden, and poverty-law frames.

Do not treat this as validation.

## Output of first comparator run should decide

A first comparator run should produce one of:

```trace
Debt_Clock_result :=
  retain_as_candidate
  OR narrow_definition
  OR merge_into_existing_operator
  OR demote_to_translation_note
  OR remove_from_pending_queue
```

Promotion is not available after a single run unless explicitly authorised and pressure-tested beyond this queue.

## Stop rule remains active

```trace
no_operator_promotion
until:
  comparator_queue_exists
  + first_comparator_run_completed
  + candidate_survives_or_demotes
```

This file only creates the queue.

It does not complete the run.

## Final compression

```trace
Debt_Clock_question :=
  does_debt_pressure_harden_faster_than_correction_can_reach_the_subject?
```

If existing fields already answer this better, demote TRACE.

End.
