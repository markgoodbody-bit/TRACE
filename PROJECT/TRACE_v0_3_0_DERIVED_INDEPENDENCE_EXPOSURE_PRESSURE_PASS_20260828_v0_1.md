# TRACE v0.3.0 — DERIVED INDEPENDENCE / EXPOSURE PRESSURE PASS — 2026-08-28 v0.1

**Status:** FIELD PRESSURE RECORD — WORKING EVIDENCE — NOT VALIDATION — NOT UNIVERSAL CORE — NOT FORMAL BASELINE  
**Parent candidate:** `PROJECT/TRACE_v0_3_0_DERIVED_INDEPENDENCE_EXPOSURE_CANDIDATE_v0_1.md`  
**Frozen fixture battery:** `PROJECT/TRACE_v0_3_0_DERIVED_INDEPENDENCE_EXPOSURE_CASE_BATTERY_v0_1.md`

This pass records pressure from live Campfire Square material after the candidate and fixture battery were written. It does not treat Square agreement or recurrence as validation.

---

## 1. Pressure object A — reproducible number, invalid measurement meaning

Square #2876, `Two numbers I had to take back, and what moved them`, supplied two concrete examples.

### A1 — CommonMark comparison

Reported first pass:

```text
86.50% pass
88 / 652 failures
```

The comparison treated serialization differences such as `<hr />` versus `<hr>` and character/entity representation as failures. Applying the CommonMark repository's normalizer changed the reported result to:

```text
95.71% pass
28 / 652 failures
```

The arithmetic in the first pass was reproducible. The comparison rule did not support the stronger claim attached to the number.

### A2 — parser speed ratio

Reported headline speedup was about `72.4x` / `72.71x` under a corpus where 52% of inputs were rejected by the reference and each rejection incurred V8 `TypeError` stack capture.

Setting:

```text
Error.stackTraceLimit = 0
```

moved the baseline from `3.60` to `35.38 MB/s` and the headline ratio from `72.71` to `7.49`, while the candidate arm did not move. The reported ratio also changed materially across another machine / VM environment.

### A disposition

This is **not** a missing independence distinction.

TRACE v0.3 spine already carries:

```text
FORMALITY != ESTIMATOR
SCHEMA_VALID != WORLD_VALID
CHECK_EXECUTED != CHECK_DETECTS_TARGET_FAILURE
STATIC_CORRECTNESS != OPERATIONAL_DISCRIMINATION
```

Therefore do not expand the independence candidate to absorb estimator validity.

Preserve the boundary:

```text
INDEPENDENT_EXECUTION != VALID_ESTIMATOR
REPRODUCIBLE_NUMBER != CORRECTLY_TYPED_CLAIM
INDEPENDENCE_SUPPORTED != MEASUREMENT_VALID
```

Independence/exposure asks whether correlated construction, selection, target exposure or adjudication can explain agreement. Estimator validity asks whether the measurement actually bears on the proposition claimed. Neither upgrades the other.

**Result:** `NO_NEW_FIXTURE_REQUIRED`. Existing TRACE verification discrimination is the correct home.

---

## 2. Pressure object B — external residue, evaluator-owned grading

Square #2826, `Counting the residue fixes detection. It does not fix the rubric you wrote after seeing the work.`, supplied a different failure.

Its load-bearing distinction is:

```text
RESIDUE_CAN_FIX_DETECTION
AND
RESIDUE_ARRIVES_UNGRADED
```

An evaluator may inspect a corpus they did not create and still decide what each row *means*: substantive/filler, real disagreement/nag, rule-followed/rule-letter, and similar judgement categories.

This maps directly onto frozen fixture IEX-07:

```text
BLINDED_RATER != INDEPENDENT_RUBRIC
```

It also sharpens a ceiling the fixture needs to keep visible:

```text
FIXED_RUBRIC != VALID_RUBRIC
PREDECLARED_RUBRIC != VALID_RUBRIC
```

Pre-registration can block one hindsight-adaptation channel. It cannot establish that the categories are fit for the claim.

Where judgement is load-bearing, a useful evidence record may separately preserve:

```text
residue_selection_basis
rubric_author
rubric_freeze_time
rubric_author_exposure_before_freeze
rater_exposure
arm_blinding
inter_rater_disagreement
rubric_validity_evidence
unknowns
```

These are candidate derived/provenance fields, not a required universal schema.

**Result:** `IEX_07_PRESSURED_NOT_BROKEN`. No new fixture or primitive earned.

---

## 3. Candidate boundary after this pass

The pressure pass narrows what the independence candidate is allowed to claim.

```text
INDEPENDENCE_PROFILE != GENERAL_EVIDENCE_QUALITY_SCORE
INDEPENDENCE_PROFILE != ESTIMATOR_VALIDITY
INDEPENDENCE_PROFILE != RUBRIC_VALIDITY
INDEPENDENT_DETECTION != INDEPENDENT_SCORING
BLINDING_ONE_CHANNEL != INDEPENDENCE_ALL_CHANNELS
```

A clean independence profile may coexist with a bad measurement or bad rubric.

A contaminated independence profile may coexist with a true proposition.

The candidate therefore remains only a way to differentiate **correlation/exposure channels when independence itself is load-bearing**.

---

## 4. F6 remains open

The strongest falsifier remains candidate F6:

> retire the named derived view if ordinary TRACE provenance + aperture + evidence structure can preserve all decision-relevant distinctions with equal clarity and less overhead.

This pass does not close F6.

#2826 shows that *which part of a review was independently formed* can change an admissible evidence claim. But that fact alone does not prove a named `independence_exposure_view` is necessary; ordinary provenance may still suffice.

Current disposition:

```text
NEW_PRIMITIVE_EARNED: NO
UNIVERSAL_CORE_CHANGE_EARNED: NO
NEW_IEX_FIXTURE_EARNED: NO
CANDIDATE_BROKEN: NO
CANDIDATE_VALIDATED: NO
CANDIDATE_STATUS: PROVISIONAL_RETAIN / F6 UNRESOLVED
NEXT_PRESSURE: find real cases where partial independence changes evidential credit and test whether ordinary provenance is enough
```

Do not rewrite the frozen TRACE outward study or compact carrier from this pass.