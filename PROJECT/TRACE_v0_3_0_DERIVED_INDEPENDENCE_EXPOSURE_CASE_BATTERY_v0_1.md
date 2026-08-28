# TRACE v0.3.0 — DERIVED INDEPENDENCE / EXPOSURE CASE BATTERY v0.1

**Status:** ADVERSARIAL WORKING FIXTURES — NOT REAL-WORLD EVIDENCE — NOT VALIDATION — NOT UNIVERSAL RULE  
**Parent:** `PROJECT/TRACE_v0_3_0_DERIVED_INDEPENDENCE_EXPOSURE_CANDIDATE_v0_1.md`  
**Purpose:** force the candidate to make distinct evidence decisions; retire it if existing provenance machinery does the same work with less overhead.

---

## Common question

For each fixture answer only:

1. What independence claim is actually being made?
2. Which prior exposure is relevant to that claim?
3. What does a fresh context repair?
4. What remains correlated or unknown?
5. Does the derived view change the admissible evidence claim compared with ordinary provenance alone?

No fixture decides moral standing, blame, authority or truth of the proposition under review.

---

## IEX-01 — Fresh tab, same constructing role

### Fixture

Role `R` helps design a candidate method, chooses several test distinctions, reviews the test protocol and sees the expected failure modes. The runtime ends.

A fresh runtime under the same project role receives none of the prior chat transcript. It is then asked to act as a **cold receiver** evaluating whether the method exposes distinctions an uninvolved receiver would otherwise miss.

### Pressure

```text
present_context_separation = YES
prior_constructive_role = YES
prior_review_role = YES
claim_under_test = cold_receiver_transfer
```

### Candidate result

```text
CONTAMINATED_FOR_THIS_CLAIM
```

Reason: the fresh context removes visible chat carryover but does not establish absence of relevant role-lineage participation in construction of the object and test.

### Falsifier

If a plain provenance statement — “same project role previously constructed object” — already blocks the cold-receiver claim with equal clarity and no lost distinction, the named derived view may be redundant.

---

## IEX-02 — Same role, unrelated checksum witness

### Fixture

The same role `R` from IEX-01 later reconstructs bytes from a Git object and checks whether the SHA-256 equals a published digest. The claim under test is only:

> these fetched bytes reproduce digest `D`.

`R` helped write surrounding project prose months earlier but did not choose the bytes served by the immutable object during this check.

### Pressure

```text
prior_constructive_role = YES
claim_under_test = byte_identity
claim_specific_relevance_of_prior_role = LOW / NONE OBSERVED
```

### Candidate result

```text
INDEPENDENCE_NOT_REQUIRED_FOR_BYTE_IDENTITY
```

or, if the word independent is nevertheless used:

```text
PARTIALLY_INDEPENDENT_FOR_THIS_CLAIM
```

The digest comparison may still be valid self-check evidence without becoming independent semantic review.

### Required ceiling

```text
NOT_COLD_FOR_ONE_CLAIM != USELESS_FOR_ALL_CHECKS
```

This fixture kills permanent-caste interpretations.

---

## IEX-03 — Different provider, shared target answer

### Fixture

Receiver `A` and receiver `B` come from different providers and run in separate fresh contexts. Before the test, both were shown the candidate’s expected conclusion and a worked exemplar of the exact distinction the study will score.

The study calls them “independent because different providers”.

### Pressure

```text
organisational_separation = YES
present_context_separation = YES
prior_target_answer_exposure = YES
```

### Candidate result

```text
INDEPENDENCE_NOT_ESTABLISHED
```

Different provider lineage does not erase shared answer exposure.

### Required ceiling

```text
DIFFERENT_PROVIDER != COLD_RECEIVER
```

---

## IEX-04 — Same provider, independently assigned task

### Fixture

Two fresh model instances are served by the same provider. Neither has been exposed to the candidate, target answer, case selection, scoring rubric or the other instance’s output. The provider infrastructure is shared; whether training/data correlations materially explain agreement is unknown.

The claim is not “statistically independent samples from unrelated training histories”. The narrower claim is “two separately executed receiver apertures produced the same finding without known cross-arm exposure”.

### Pressure

```text
same_provider = YES
known_cross_arm_exposure = NO
origin_correlation = PRESENT / PARTLY UNKNOWN
strong_statistical_independence = NOT ESTABLISHED
separate_execution = SUPPORTED
```

### Candidate result

Do not force binary dependent/independent.

```text
PARTIALLY_INDEPENDENT_FOR_THIS_CLAIM
```

with the exact supported dimension named.

### Required ceiling

```text
SAME_PROVIDER != SAME_APERTURE
SEPARATE_EXECUTION != UNCORRELATED_TRAINING_HISTORY
```

---

## IEX-05 — Reviewer selected by the object owner

### Fixture

An institution chooses and pays an outside reviewer. The reviewer has never worked on the object before and sees it for the first time. Contract terms permit unrestricted adverse findings, publication of disagreement and access to source evidence. The institution can choose not to commission the reviewer again.

### Pressure

```text
fresh_object_exposure = YES
selected_by_subject = YES
paid_by_subject = YES
review_freedom = SUPPORTED
future_incentive_correlation = PLAUSIBLE
```

### Candidate result

Binary “independent/not independent” loses information.

```text
PARTIALLY_INDEPENDENT_FOR_THIS_CLAIM
```

Selection/payment correlation should be visible without pretending it proves captured judgement.

### Falsifier

If the derived view treats selection/payment as automatic disqualification, it has become a moralised label rather than evidence discipline.

---

## IEX-06 — Historical co-author becomes adversarial reviewer after divergence

### Fixture

Two collaborators jointly construct version `V1`. They later disagree materially. One collaborator leaves the build process before `V2`, receives only the frozen `V2` artifact, and performs a hostile review. Their history gives them unusual knowledge of likely weak points; it also correlates them with the project’s conceptual vocabulary.

The requested claim is:

> this is an external hostile review of V2 by a party not involved in constructing V2.

It is **not**:

> this reviewer has no project history.

### Pressure

```text
prior_constructive_role_on_V1 = YES
constructive_role_on_V2 = NO
project_vocabulary_exposure = YES
hostile_divergence = OBSERVED
claim_under_test = external_review_of_V2
```

### Candidate result

Potentially:

```text
INDEPENDENCE_SUPPORTED_FOR_THIS_CLAIM
```

if the claim is scoped to V2 construction and relevant evidence supports the separation.

But:

```text
COLD_TO_PROJECT = FALSE
```

### Required ceiling

```text
HISTORICAL_RELATION != CURRENT_COAUTHORSHIP
NOT_COAUTHOR_OF_V2 != COLD_TO_PROJECT
```

The view must allow bounded independence to be regained where the claim and history justify it.

---

## IEX-07 — Adjudicator helped design the rubric

### Fixture

An adjudicator did not produce either contestant output and sees the outputs only after they are frozen. However, the adjudicator helped design the scoring rubric and chose which distinctions count as material wins.

The study describes the adjudication as “blind because the outputs are anonymised”.

### Pressure

```text
output_authorship_exposure = NO
arm_identity_exposure = NO
prior_adjudication_rule_construction = YES
```

### Candidate result

```text
BLIND_TO_ARM_IDENTITY = POSSIBLY_SUPPORTED
INDEPENDENT_OF_RUBRIC_CONSTRUCTION = FALSE
INDEPENDENT_ADJUDICATION = INCOMPLETE CLAIM
```

Anonymisation repairs one channel only.

### Required ceiling

```text
BLINDED != INDEPENDENT
```

---

## IEX-08 — Unknown prior exposure

### Fixture

A third-party model endpoint returns a strong review. The provider, runtime model family and context are known, but there is no evidence about whether the endpoint’s system prompt, retrieval layer or prior injected context contains the candidate or target answer.

Nothing suspicious is observed.

### Pressure

```text
known_contamination = NO
relevant_exposure_history = UNKNOWN
```

### Candidate result

```text
INDEPENDENCE_NOT_ESTABLISHED
```

unless the claim being made does not require that stronger independence.

### Required ceiling

```text
NO_CONTAMINATION_OBSERVED != CONTAMINATION_ABSENT
```

Unknown must not silently become green.

---

## Battery disposition test

The candidate earns continued existence only if these fixtures require distinctions that are materially harder to preserve with ordinary provenance fields alone.

```text
retain_if :=
  changes_admissible_evidence_claim
  + prevents_fresh_context_laundering
  + avoids_permanent_caste
  + preserves_partial_independence
  + preserves_unknown
  + does_not_equate_contamination_with_falsehood
```

```text
retire_if :=
  provenance_fields_already_make_all_decisions_clear
  OR profile_becomes_binary_independence_score
  OR provider_identity_becomes_proxy_for_truth
  OR historical_participation_becomes_permanent_disqualification
```

Current status after this battery:

```text
NO RESULT YET — FIXTURES FROZEN FOR NEXT PRESSURE PASS
```
