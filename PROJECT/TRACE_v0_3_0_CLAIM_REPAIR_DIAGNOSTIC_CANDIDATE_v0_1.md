# TRACE v0.3.0 — CLAIM REPAIR DIAGNOSTIC CANDIDATE v0.1

**Status:** WORKING DERIVED VIEW — NOT FORMAL BASELINE — NOT CANON — NOT VALIDATED — NOT NEW CLAIM STATUS — NOT AUTHORITY — NOT PERMISSION — NOT CLEARANCE  
**Purpose:** expose the evidential repair available to a claim without turning `DECAYED / NEVER_SUPPORTED / NEVER_EVALUATED` into truth-like statuses.

## 0. Build claim

Reject three exclusive universal classes.

Use existing TRACE claim freshness/scope for **current applicability**. Add no duplicate current-fit status.

Where repair history matters, derive only this bounded diagnostic:

```text
H  prior adequate support represented for a declared earlier proposition/scope/time
E  relevant evaluation/check represented as executed
R  evidential repair/reconstruction route currently available
```

Each may be `YES / NO / UNKNOWN` relative to a declared evidence/history aperture. They are a derived view, not new canonical fields.

```text
DIAGNOSTIC_VIEW != CLAIM_TRUTH_VALUE
REPAIR_ROUTE != PERMISSION_TO_ACT
NO_RECORD != WORLD_HISTORICAL_ABSENCE
```

## 1. Existing carriers

The spine already carries proposition, provenance, observation/derivation route, aperture, freshness/time, supporting/contrary evidence, unknowns and omissions; retained history is already separate from current world state.

The donor graph already has `CLAIM`, `RECORD`, `ROUTE`, `CLOCK`, `APERTURE` plus `REPORTS`, `INFERS`, `DISPUTES`, `RECORDS`, `VERIFIES`, `DEPENDS_ON`, `PERSISTS_AS` and related edges.

No new primitive or claim status is required.

## 2. H — prior support represented

`H` concerns a prior support state that a current claim or repair is relying on as historical basis. It does **not** itself decide whether that support remains current.

```text
H = YES
  adequate support is represented for a declared earlier proposition/scope/time

H = NO
  an evidence/history aperture adequate for this negative establishes that adequate support was not established there

H = UNKNOWN
  represented history is insufficient to establish either
```

```text
NO_SUPPORT_RECORD != SUPPORT_NEVER_EXISTED
SOURCE_ANCHORED != PROPOSITION_SUPPORTED
NO_ESTABLISHED_SUPPORT_IN_ONE_LEDGER != WORLD_HISTORICAL_ABSENCE
```

Whether `H = YES` still supports the current use is answered by the ordinary TRACE freshness/scope/dependency reading, not by a new diagnostic axis.

## 3. E — evaluation represented as executed

```text
E = YES
  a relevant evaluation/check/adjudication is represented as having executed

E = NO
  a bounded event history adequate for this negative establishes that it did not execute

E = UNKNOWN
  no adequate positive or negative evaluation history is available
```

```text
NO_EVALUATION_RECORD != EVALUATION_NEVER_OCCURRED
CHECK_PATH_EXISTS != CHECK_EXECUTED
CHECK_EXECUTED != CLAIM_SURVIVED_CHECK
```

`E = YES` says an evaluation occurred. It does not say whether the proposition was supported, falsified or resolved.

## 4. R — repair/reconstruction route available

`R` stops the view recommending endless re-derivation when the evidence needed for historical adjudication is no longer recoverable.

```text
R = YES
  a represented route can still acquire, reproduce, re-observe or validly reconstruct the needed evidence/evaluation

R = NO
  the declared evidence boundary establishes that the required historical evidence/evaluation cannot now be recovered through an available route

R = UNKNOWN
  repairability itself is unresolved
```

```text
ROUTE_LISTED != ROUTE_EXECUTABLE
MISSING_SURVIVING_EVIDENCE != EVIDENCE_NEVER_EXISTED
HISTORICAL_CLAIM_UNREPAIRABLE != FUTURE_MECHANISM_UNREPAIRABLE
```

`R` is ordinary route structure viewed for repair. If naming it as a diagnostic adds no work, delete it and use the route directly.

## 5. Repair implications

### Prior support exists but current applicability fails

Represented pattern:

```text
H = YES
ordinary current-use reading = prior support no longer applicable / freshness unresolved
```

If `R = YES`, refresh/re-observe/re-derive through an appropriate current route, or narrow the proposition to its supported historical scope/time.

This is the only clean home for optional shorthand `DECAYED`.

```text
DECAYED -> derived shorthand at most
DECAYED != CLAIM_STATUS
```

### Evaluation executed but current proposition is not supported

```text
E = YES
current support for asserted proposition != ESTABLISHED
```

Do not repair this by refreshing the assertion timestamp. Inspect what the evaluation actually discriminated; seek another evidential route if warranted; otherwise preserve/narrow/retract the unsupported proposition as external use requires.

```text
EVALUATED != SUPPORTED
FRESH_ASSERTION != FRESH_EVIDENCE
```

### Evaluation history unresolved

```text
E = UNKNOWN
current support != ESTABLISHED
```

If `R = YES`, locate or run an appropriate evaluation. If `R = NO`, preserve the historical evidential limit rather than retrying a route that cannot reconstruct the proposition.

### Irrecoverable historical adjudication

An instrument can preserve `MISMATCH` and failed-check names while the expected projection needed to adjudicate the old state is absent from surviving evidence.

```text
EXPECTED_PROJECTION_ABSENT_FROM_SURVIVING_EVIDENCE
    != EXPECTED_PROJECTION_NEVER_EXISTED

UNRESOLVED_WITH_LIVE_EVIDENCE_ROUTE
    != UNADJUDICABLE_FROM_SURVIVING_EVIDENCE
```

Historical adjudication may be impossible while a future mechanism repair remains possible—for example, preserve expected-state evidence before comparable future actuation.

## 6. Non-AI transfer — calibration triplet

Three dashboard claims read `sensor reading is acceptable`.

### A — prior calibration expired

A traceable calibration previously supported the same operating range, but its validity interval no longer covers today's use.

```text
H = YES
E = YES
current applicability = NO
R = YES
```

Repair: recalibrate/re-observe or narrow to the historical claim.

### B — current comparison did not establish tolerance

A relevant current comparison executed and did not establish the acceptable-within-tolerance proposition.

```text
E = YES
current support = NOT_ESTABLISHED
R = YES
```

Repair is not a timestamp refresh of the old certificate.

### C — replacement sensor, incomplete history

A replacement sensor is listed, but supplied history contains no calibration comparison and is not independently known to be exhaustive.

```text
H = UNKNOWN
E = UNKNOWN
R = YES if a current comparison can still be run
```

Do not convert missing history into `never evaluated`.

## 7. What happens to the old labels

```text
DECAYED
  optional derived shorthand only when prior adequate support is represented and current applicability fails

NEVER_SUPPORTED
  reject as absolute; replace with bounded support state relative to an adequate history/evidence aperture

NEVER_EVALUATED
  reject as absolute; replace with bounded evaluation-event state relative to an adequate history aperture
```

If an independently bounded event history is exhaustive for the relevant interval/class, a strong negative may be warranted **relative to that aperture**. World-universal `NEVER` still does not follow automatically.

## 8. Falsification targets

Delete or demote this view if:

1. `H/E/R` do not change the available evidential repair;
2. the same repair is appropriate across materially different states;
3. `H` adds nothing beyond ordinary evidence history;
4. `E` adds nothing beyond existing check records;
5. `R` adds nothing beyond ordinary route status;
6. bounded negative history can never produce useful `NO` rather than `UNKNOWN`;
7. a missing record is still silently treated as a never-event;
8. evaluation execution is mistaken for support or falsity;
9. the view requires universal event logging;
10. the view imports a value, authority, priority or action selector;
11. an unfamiliar receiver given only the ordinary spine already selects the correct evidential repair in the transfer cases without this view.

## 9. Current disposition

```text
NEW CLAIM STATUS:          NO
THREE EXCLUSIVE CLASSES:   REJECT
ABSOLUTE NEVER_* LABELS:   REJECT
DECAYED:                   OPTIONAL DERIVED SHORTHAND AT MOST
H/E/R REPAIR VIEW:         HOSTILE-REVIEW CANDIDATE
PREFERRED FINAL STATUS:    DERIVED / SMALLER / POSSIBLY DELETE
```

The build succeeds if the taxonomy disappears and the correct repair remains visible.
