# TRACE v0.4 beta3 — worked parse

Status: **BETA ILLUSTRATION / NOT EVIDENCE / NOT VALIDATION / NOT A MORAL VERDICT**.

This example uses the Mechanical Ethics composite finance-appeal scene. The scene is invented for teaching; this file tests whether TRACE can carry the relevant structure without requiring the reader to complete the full schema.

## Scene

Amina needs a car for a new work rota. A finance application is refused after an automated assessment and human approval. She finds an old address attached to the wrong account, sends correcting evidence, and enters a review route expected to take up to twenty working days. The dealer cannot hold the car that long. She hires a car, borrows a deposit and later accepts worse finance elsewhere. The review eventually corrects the joined records and invites her to apply again.

## 1. Scene / aperture / map

```text
WORLD / LIVED SCENE
  transport need + work rota + available car + finance decision + time passing

INSTITUTIONAL APERTURE
  application fields + joined records + automated assessment + reviewer file

AMINA APERTURE
  refusal + credit report + own tenancy / identity evidence + dealer deadline

INSTITUTIONAL MAP != COMPLETE LIVED SCENE
AMINA MAP != COMPLETE FINANCE SYSTEM
```

Nothing in the parse establishes which hidden model feature caused the initial refusal until evidence supports that claim.

## 2. Load-bearing claims

| Claim | Initial state | What would strengthen / change it? |
|---|---|---|
| Two records were incorrectly joined | reported / later institutionally confirmed in the scene | review result, underlying record comparison |
| Review route exists | observed from refusal notice | route terms/current policy |
| Review can protect the first-car opportunity | not established prospectively; this review did not preserve it in the narrated outcome | dealer hold duration + supported review completion evidence |
| Correcting the joined record may protect later applications | projected | later applications/outcomes |

Representation type does not change the evidence duty. A status field saying `review_available=true` would not establish that the route can reach the threatened opportunity.

## 3. Route usability and clocks

The review route is findable and usable enough for Amina to submit evidence. That still does not make it timely for the first decision.

Load-bearing timing:
- target: the ability to obtain the identified car on terms available that Friday;
- review route: evidence submission -> review -> correction / reconsideration;
- competing clock: dealer's ability/willingness to hold the car;
- work/transport clock: new rota begins before the stated review period ends.

```text
ROUTE_EXISTS = supported
ROUTE_USED = supported
ROUTE_TIMELY_FOR_FIRST_CAR = not supported
CORRECTION_ROUTE_USEFUL_FOR_LATER_RECORD = supported by scene
```

A strong timing proof would require actual compatible bounds. The stated response period does not guarantee protection before the dealer deadline. The later narrated sale and correction establish that this instance did not preserve the first-car opportunity. They do not establish that every feasible execution of the review route would have been too late.

## 4. Action / transition / hardening

```text
INITIAL REFUSAL
-> review submitted
-> car remains unheld
-> first car sold / route closes
-> hire cost + borrowed deposit
-> alternative higher-cost finance accepted
-> review later corrects record
```

The sale of the first car is a realised closure of that identified opportunity. It does not prove every future transport or finance route is closed.

## 5. Burden / residue

The correction changes the record. It does not by itself establish repair of:
- hire cost;
- debt to the sister;
- the worse finance agreement;
- time or stress incurred;
- any downstream employment consequence.

Some of those may later be repaired. TRACE keeps the questions separate rather than declaring them permanent.

```text
RECORD_CORRECTED != FIRST_CAR_RESTORED
LATER_APPLICATION_POSSIBLE != EARLIER_RESIDUE_CLEARED
PAST_LOSS_IN_RECORD != CURRENT_IMPAIRMENT
```

## 6. Future-space baseline

At least three comparisons answer different questions:

1. **Before refusal vs after refusal** — the preferred finance/car route narrows.
2. **After refusal with review vs after refusal without review** — the review preserves a route to record correction and possibly better later applications.
3. **Review route vs faster interim hold / reconsideration** — a different policy might preserve the first-car route, but the scene does not establish that such a policy was available or justified.

Do not collapse those comparisons into one claim that 'the future got better' or 'the appeal failed'.

## 7. What TRACE adds — and what it does not

TRACE adds value here only if the distinctions above prevent a consequential collapse such as:
- `appeal exists -> protection existed`;
- `record corrected -> harm repaired`;
- `same person -> same opportunity set`;
- `review completed -> review reached the live decision`.

It does **not** decide:
- whether the lender should have approved the application;
- who should bear compensation;
- which transport/credit interest has moral priority;
- whether the institution had lawful authority;
- whether the review period was reasonable in its wider domain.

Those require external law, ethics, policy, evidence or domain expertise.

## 8. Practical falsifier

If an ordinary careful analysis or a stronger specialist method identifies every consequential distinction above with less burden, TRACE should shrink or hand off rather than claim advantage.
