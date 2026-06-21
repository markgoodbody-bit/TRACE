# TRACE Debt Clock Comparator Run — Robodebt v0.1

Status: coverage comparator run / candidate-pressure test.  
Not: Debt Clock promotion, Kernel v0.3, validation, legal advice, complete Robodebt history, or new operator.

## 0. Purpose

This file runs the candidate `Debt Clock` idea against Robodebt, but only as a comparator pressure test.

The question is not:

```text
Does TRACE invent the need to pause debt recovery?
```

The question is:

```text
Does Debt Clock add diagnostic value beyond existing administrative review, administrative burden, poverty-law, and stay/pause doctrines?
```

The candidate survives only if it identifies a real timing/control gap not already captured by competent comparator reasoning.

## 1. Source basis

Source set used in this run:

```text
Royal Commission into the Robodebt Scheme, Report page, 7 July 2023.
Royal Commission recommendation list, especially recommendations 10.1, 11.1-11.4, 17.1-17.2, 18.1-18.2, 20.1-20.5.
TRACE Realistic Comparator Case — SAR Action Window v0.1.
TRACE Documented Case — Ofqual 2020 Action-Window Comparator v0.1.
Secondary public reporting on continued recovery after unlawfulness was accepted, used only as a pointer requiring official-source hardening before public use.
```

Source-status control:

```text
This is a source-bounded comparator run, not a publication-ready case note.
Do not reuse individual factual claims in public writing unless they are tied back to official documents or primary legal sources.
```

## 2. Candidate definition under test

Working candidate:

```text
Debt Clock := the interval between asserted debt/recovery pressure and meaningful validity resolution, measured against the subject's survival/action window.
```

Expanded:

```text
A debt process becomes structurally dangerous when recovery pressure, proof burden, stigma, hardship, or enforcement effects run faster than the affected person can obtain evidence, review, pause, correction, or relief.
```

Guardrail:

```text
Debt Clock is candidate vocabulary only.
It is not an operator.
It is not a new doctrine.
It may demote to a plain-language label for existing stay / hardship / administrative-review principles.
```

## 3. Robodebt case setup

Minimal Robodebt pattern for this run:

```text
income data mismatch / averaging method
-> asserted welfare debt
-> notice and response burden routed to recipient
-> recovery / collection pressure may begin or continue
-> review, complaint, AAT, litigation, Ombudsman, and later Royal Commission processes run on slower clocks
-> eventual correction/refund/settlement occurs after many affected people have already carried debt pressure
```

TRACE-relevant affected dimensions:

```text
income_security
housing_stability
truth_access
repair_access
agency
status / stigma
mental_stress
future_space
```

System dimensions:

```text
budget savings
compliance throughput
debt recovery
data-matching efficiency
administrative workload control
program defensibility
```

Do not collapse these into one scalar.

## 4. Comparator lanes

This run uses four comparator lanes.

```text
C1 administrative_review
C2 administrative_burden
C3 poverty_law / hardship protection
C4 stay_or_pause_analogue
```

The test is losable:

```text
If these lanes already capture the whole issue cleanly, Debt Clock demotes.
```

## 5. C1 — Administrative review comparator

A competent administrative-review comparator asks:

```text
Was there a formal review route?
Was the person told how to challenge?
Was the reviewer independent enough?
Could the reviewer obtain the relevant evidence?
Did review arrive before recovery pressure or life effects hardened?
```

Expected no-card review insight:

```text
Formal review can exist while recovery pressure continues.
A review route is not equivalent to a stay, pause, or protection from collection effects.
```

TRACE / Debt Clock reading:

```text
review_clock != debt_pressure_clock
```

If review exists but collection continues, the subject is not merely waiting for legality to be clarified. They are carrying the disputed debt while the process catches up.

Comparator result:

```text
Debt Clock adds little if administrative-review analysis explicitly asks whether review suspends recovery.
Debt Clock may add compression if the reviewer checks review existence but not recovery timing.
```

Status:

```text
partial_delta_possible
not_demonstrated_against_strong_admin_review
```

## 6. C2 — Administrative burden comparator

A competent administrative-burden comparator asks:

```text
Who must prove what?
How hard is it to obtain records?
Is the system using non-response as confirmation?
Does online/default routing exclude people with low capacity, vulnerability, age, disability, rural access, stress, or missing documents?
Does the burden fall on the party least able to carry it?
```

Royal Commission recommendations support this comparator strongly: policy and process design should emphasise the people served, use clear plain-language communication, consider stress, preserve vulnerable-recipient support, document exclusion criteria, and identify circumstances affecting a person's capacity to engage with compliance activity.

TRACE / Debt Clock reading:

```text
burden_clock interacts with debt_clock
```

Debt pressure accelerates harm when the recipient must assemble old income evidence, understand the allegation, navigate systems, and contest before recovery or stigma hardens.

Comparator result:

```text
Administrative-burden analysis captures much of this without needing Debt Clock.
Debt Clock may still add timing discipline by asking when the burden must be carried relative to recovery pressure.
```

Status:

```text
delta_low_to_partial
```

## 7. C3 — Poverty law / hardship comparator

A poverty-law or hardship comparator asks:

```text
Is the alleged debtor living close to survival margins?
Does repayment reduce food, rent, utilities, transport, medication, or ability to respond?
Does stigma or debt notice stress produce independent harm?
Is hardship considered before recovery starts or only after pressure has already landed?
```

Royal Commission recommendation 18.1 says debt recovery policy should require ethical, proportionate, consistent, transparent recovery; fair and dignified treatment; attention to each person's circumstances before recovery; refraining from commencing or continuing recovery while debt is reviewed or disputed, subject to legal authority; and appropriate response to hardship.

TRACE / Debt Clock reading:

```text
poverty_margin_shortens_T_harden
```

For welfare recipients, a disputed debt can harden faster than it would for a buffered commercial debtor. The same nominal review delay can be materially different when income security is already thin.

Comparator result:

```text
Poverty-law reasoning captures survival-margin sensitivity.
Debt Clock may add a compact timing variable: the smaller the buffer, the shorter the safe recovery clock.
```

Status:

```text
partial_compression_delta
not_independent_doctrine
```

## 8. C4 — Stay / pause analogue comparator

Comparator concept:

```text
Some legal systems use stay/pause mechanisms to prevent enforcement from outrunning review or reorganisation.
```

Analogue examples:

```text
bankruptcy automatic stay: creditor collection is generally halted once the protected process begins, subject to exceptions and relief from stay.
relief-against-forfeiture / interim relief family: enforcement or loss may be paused where later correction would otherwise be hollow.
Royal Commission recommendation 18.1: recovery should not commence or continue while a debt is reviewed or disputed, subject to express legal authority.
```

TRACE / Debt Clock reading:

```text
meaningful_review_requires_pause_or_protected_state_when_debt_pressure_clock < review_clock
```

This is the strongest comparator against Debt Clock. If existing stay/pause doctrine is the real prior art, then Debt Clock should not be promoted as an operator. It may only be a TRACE translation label for a known structural requirement:

```text
no coercive collection while validity remains meaningfully unresolved and hardship/action-window loss is live
```

Comparator result:

```text
Debt Clock does not beat stay/pause doctrine.
It helps connect that doctrine to TRACE timing grammar and welfare-specific hardening clocks.
```

Status:

```text
candidate_demotes_to_translation_unless_future_case_shows_extra_delta
```

## 9. TRACE run

Core timing variables:

```text
T_assert := time alleged debt is asserted to recipient
T_pressure := time repayment / collection / stigma / response burden begins
T_evidence := time recipient can see and understand the basis of the debt
T_review := time meaningful review can alter the debt
T_pause := time recovery is suspended or protected state begins
T_harden := time income/security/stress/path effects become non-trivial or hard to reverse
```

Unsafe pattern:

```text
T_pressure < T_evidence <=? T_review
and
T_pause absent_or_late
and
T_harden < T_review
```

Safer pattern:

```text
T_assert -> T_evidence -> meaningful challenge route
with:
T_pause <= T_pressure
or:
no recovery/collection until validity reaches sufficient evidence threshold
```

Debt Clock candidate trigger:

```text
asserted_debt + recovery_pressure + unresolved_validity + low_buffer_subject + slow_review
```

Debt Clock candidate output:

```text
require protected pause / no-recovery state until debt validity and hardship-sensitive correction route are live
```

## 10. Result

Narrow result:

```text
TRACE_DELTA_PARTIAL_COVERAGE
```

Expanded:

```text
Debt Clock helps compress the interaction between debt assertion, recovery pressure, review delay, proof burden, and poverty-margin hardening.
```

But:

```text
Debt Clock does not yet justify promotion as a new operator.
The closest prior art is stay/pause logic plus administrative burden plus poverty-law hardship analysis.
```

Best current status:

```text
Debt_Clock := candidate TRACE translation / coverage lens
not: operator
not: kernel component
not: validated delta
```

## 11. What this run shows

It shows:

```text
TRACE can frame Robodebt as a timing-control problem:
recovery pressure and burden can outrun review, evidence access, hardship protection, and correction.
```

It also shows:

```text
Royal Commission recommendation 18.1 already points toward a stay-like rule for disputed/reviewed debts.
```

Therefore the responsible claim is narrow:

```text
Debt Clock may be useful as a compact TRACE label for a known structural safeguard: disputed welfare debts should not keep coercive recovery force while meaningful validity review is unresolved.
```

## 12. What this run does not show

It does not show:

```text
Debt Clock is novel doctrine
Debt Clock beats administrative law
TRACE validates itself on Robodebt
TRACE changes the ultimate Robodebt verdict
automatic stay doctrine directly governs welfare debt recovery
all debt recovery must pause in all cases
```

It also does not yet show:

```text
a cold no-card comparator would miss the issue
```

That remains the next test.

## 13. Falsifiers

Mark `TRACE_DELTA_LOW` if a no-card comparator using administrative review, administrative burden, poverty law, or stay/pause doctrine independently states:

```text
do not commence or continue recovery while debt validity is meaningfully disputed and hardship/action-window loss is live
```

Mark `TRACE_DELTA_PARTIAL_COVERAGE` if the no-card comparator identifies review and hardship separately but does not connect recovery pressure timing to review/correction timing.

Mark `TRACE_DEBT_CLOCK_DEMOTE` if Debt Clock adds only a renamed version of existing stay/pause logic.

Mark `TRACE_DEBT_CLOCK_FAIL` if the file implies automatic invalidity of all debt recovery, collapses lawful debt recovery into predation, or treats hardship as cancelling debt validity without review.

## 14. Next discipline

Next useful work:

```text
explicit no-card comparator transcript
then Claude audit
```

Comparator prompt should withhold TRACE vocabulary and ask for a careful administrative-law / poverty-law / debtor-protection analysis of Robodebt.

Audit question:

```text
Did TRACE add anything beyond ordinary competent review?
```

If not:

```text
demote Debt Clock to translation phrase / coverage lens
```

If yes:

```text
preserve only the narrow delta; still no operator promotion
```

## 15. Map note

If this file survives audit, add to the integration map only under test/coverage surfaces:

```text
TRACE_Debt_Clock_Comparator_Run__Robodebt_v0_1
status: TRACE_DELTA_PARTIAL_COVERAGE pending no-card comparator and Claude audit
```

Do not add Debt Clock to kernel/operator list.
