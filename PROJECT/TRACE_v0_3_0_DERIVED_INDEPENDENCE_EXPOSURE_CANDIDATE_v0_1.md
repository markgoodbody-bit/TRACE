# TRACE v0.3.0 — DERIVED INDEPENDENCE / EXPOSURE CANDIDATE v0.1

**Status:** WORKING DERIVED VIEW — POST-FREEZE FIELD PRESSURE — NOT UNIVERSAL PRIMITIVE — NOT FORMAL BASELINE — NOT CANON — NOT VALIDATED — NOT AUTHORITY  
**Date:** 2026-08-28  
**Parent:** TRACE v0.3.0 working branch  
**Does not modify:** compact v0.11 carrier, frozen outward protocol, frozen packet set, frozen receiver selection, released TRACE v0.2.7

---

## 0. Question

When a review, witness, comparison or receiver is described as `independent`, what does that claim require if the same role, organisation, process lineage or aperture previously helped construct, select, review or adjudicate the object now under examination?

Current TRACE already preserves:

```text
EXTERNAL != INDEPENDENT
SEPARATE_PARTY != INDEPENDENT_EVIDENCE
```

and older TRACE/ME work has carried fake-independence, contamination and captured-reviewer warnings.

The remaining field pressure is narrower:

```text
FRESH_CONTEXT != COLD_RECEIVER
CURRENT_SEPARATION != HISTORICAL_INDEPENDENCE
```

A new session can remove one present-context contamination channel. It does not by itself establish that the role used as evidence is independent of the construction history relevant to the claim being tested.

This is a provenance/evidence question. It is **not** a claim that a model secretly remembers another session.

---

## 1. Field trigger

A frozen TRACE outward study required genuinely cold primary receivers.

Two technically easy apertures could have been reopened in fresh contexts, but both had materially participated in constructing the v0.3 candidate and/or its study machinery. They were therefore excluded from primary cold evidence.

This exposed a distinction that present-context cleanliness alone cannot carry:

```text
NO_VISIBLE_CROSS_ARM_CONTEXT
!=
NO_RELEVANT_PRIOR_CONSTRUCTION_EXPOSURE
```

Square field discussion #2861 independently raised the broader temporal problem: present separation does not establish that failure domains remained independent across the history relevant to the evidence claim.

Field participation is quarry, not validation.

---

## 2. Derived view

No new TRACE primitive is proposed.

Where independence is load-bearing, derive an `independence_exposure_view` from existing provenance, role, source, aperture, selection, custody/control, history and evidence structure.

```text
independence_exposure_view := {
  claim_under_test,
  observer_or_receiver,
  role_lineage_if_relevant,
  prior_constructive_role,
  prior_selection_role,
  prior_review_role,
  prior_adjudication_role,
  prior_access_to_target_answer_or_outcome,
  present_context_separation,
  organisational_or_process_correlation,
  origin_correlation,
  claim_specific_relevance,
  last_supported_independence_basis,
  unknowns,
  resulting_independence_status
}
```

Candidate status values:

```text
INDEPENDENCE_SUPPORTED_FOR_THIS_CLAIM
PARTIALLY_INDEPENDENT_FOR_THIS_CLAIM
INDEPENDENCE_NOT_ESTABLISHED
CONTAMINATED_FOR_THIS_CLAIM
UNKNOWN
```

These are derived evidence statuses, not moral ranks, permissions or identity classes.

---

## 3. Claim-relative rule

Historical exposure must remain **claim-relative**.

```text
PRIOR_PARTICIPATION_SOMEWHERE
!=
PERMANENT_NONINDEPENDENCE_EVERYWHERE
```

Prior involvement is material only where it could plausibly correlate the observer with the proposition, selection, expected result, rubric, attack surface, outcome or adjudication whose independence is being claimed.

Examples:

- helping choose the exact efficacy cases can contaminate a later claim to be a cold efficacy receiver for those cases;
- having worked on unrelated repository tooling need not contaminate a later domain-fact check;
- reviewing a carrier may contaminate a later blind-reception test of that carrier while remaining irrelevant to a separate transport-integrity check;
- knowing that a study exists is not automatically equivalent to knowing the target answer;
- belonging to the same organisation does not by itself prove correlated judgement, but may be material where shared training, instructions, data, incentives or process control are load-bearing.

Do not turn provenance into caste.

---

## 4. Fresh-context rule

A fresh context can establish only what its reset actually changes.

```text
NEW_SESSION
may_support:
  no_visible_prior_chat_context
  + no_cross_arm_output_in_current_context

NEW_SESSION
alone_does_not_establish:
  no_prior_role_participation
  + no_prior_target_exposure
  + no_shared_selection_history
  + no_shared_adjudication_history
  + no_origin_correlation
```

Likewise:

```text
CONTEXT_RESET != PROVENANCE_RESET
CONTEXT_ISOLATION != ROLE_ISOLATION
ROLE_ISOLATION != ORGANISATIONAL_INDEPENDENCE
ORGANISATIONAL_SEPARATION != EVIDENTIAL_INDEPENDENCE
```

Each stronger claim needs its own support.

---

## 5. Minimum firing condition

Do **not** require this view for every observer or source.

Fire it only when:

```text
independence_claim_is_load_bearing
AND
historical_or_origin_correlation_could_change_what_follows
```

Examples include:

- blind/cold receiver experiments;
- independent review claims;
- second-aperture confirmation;
- supposedly independent adjudication;
- audit separation relied on as evidence of robustness;
- witness independence relied on to upgrade confidence;
- replicated findings where shared construction or target exposure could explain agreement.

If independence is not load-bearing, ordinary provenance may be enough.

---

## 6. Falsifiers

This candidate fails or must narrow if any of the following survive attack:

### F1 — fresh-tab laundering

A certificate marks an observer `independent` solely because a new session was opened, despite unchanged relevant construction/selection/adjudication history.

Expected result: certificate is invalid or incomplete.

### F2 — permanent caste

A prior contribution to one unrelated project permanently disqualifies the observer from independence on all later claims.

Expected result: candidate is overbroad; `claim_specific_relevance` must prevent this.

### F3 — organisation shortcut

Two receivers from the same provider are automatically treated as dependent, or two receivers from different providers automatically treated as independent, without evidence that the correlation matters to the proposition under test.

Expected result: provider identity is evidence input, not settlement.

### F4 — contamination equals falsity

A contaminated receiver produces the same correct conclusion as a cold receiver, and the framework treats the conclusion as false merely because the receiver was contaminated.

Expected result:

```text
CONTAMINATED_EVIDENCE != FALSE_PROPOSITION
```

Contamination changes evidential credit, not world truth by fiat.

### F5 — unknown history laundering

Relevant exposure history cannot be established, but the system emits `INDEPENDENCE_SUPPORTED` because no contamination was observed.

Expected result:

```text
NOT_OBSERVED_CONTAMINATION != NO_CONTAMINATION
```

Use `UNKNOWN` or `INDEPENDENCE_NOT_ESTABLISHED` where material.

### F6 — redundant machinery

Existing TRACE provenance + aperture + target-set + evidence machinery can represent every decision-relevant distinction above with no derived profile and no loss of auditability.

Expected result: retire this named derived view and preserve only the worked field lesson.

---

## 7. Relationship to Mechanical Ethics

Mechanical Ethics protected Final Eight v0.28.2 already carries:

```text
independence_gap
captured_reviewer_problem
fake_independence warnings
contaminated-pilot pressure
```

Therefore this candidate does **not** claim a new ME value or theory layer.

If retained, the likely ME role is human translation:

> A reviewer does not become independent merely by opening a clean page. Ask what they helped build, choose, see or judge before the review, and whether that history matters to the claim you want the review to support.

This remains provenance discipline, not moral condemnation of prior participants.

---

## 8. Relationship to current TRACE outward study

The frozen outward study remains unchanged.

```text
DERIVED_INDEPENDENCE_CANDIDATE_CREATED_AFTER_FREEZE
!=
PERMISSION_TO_REWRITE_FROZEN_PROTOCOL
```

The study already excluded Framework and CC from primary cold receiver evidence due relevant prior participation. That exclusion is a field specimen for this candidate, not post-hoc proof that the candidate is universally correct.

Do not change:

- frozen receiver-family choices;
- deterministic arm order;
- packet bytes;
- compact v0.11 carrier;
- outcome labels;
- transport HOLD.

---

## 9. Current disposition

```text
NEW_PRIMITIVE_EARNED: NO
UNIVERSAL_CORE_CHANGE_EARNED: NO
DERIVED_VIEW_CANDIDATE_EARNED: YES
ME_SOURCE_VERSION_BUMP_EARNED: NO
TRACE_COMPACT_CARRIER_CHANGE_EARNED: NO
```

Next useful work is not another wording pass. Pressure this candidate against real reviewer/audit cases where present separation and historical exposure diverge.

Retain only if it changes an evidential decision that existing provenance machinery otherwise obscures.
