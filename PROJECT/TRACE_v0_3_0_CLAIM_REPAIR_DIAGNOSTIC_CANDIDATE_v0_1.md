# TRACE v0.3.0 — CLAIM REPAIR DIAGNOSTIC CANDIDATE v0.1

**Status:** WORKING DERIVED VIEW — NOT FORMAL BASELINE — NOT CANON — NOT VALIDATED — NOT NEW CLAIM STATUS — NOT AUTHORITY — NOT PERMISSION — NOT CLEARANCE  
**Purpose:** choose the next evidential repair without turning `DECAYED / NEVER_SUPPORTED / NEVER_EVALUATED` into truth-like statuses.

## 0. Build claim

Reject three exclusive universal classes.

Instead derive a small repair vector from existing TRACE claim/evidence/history/route structure:

```text
H  prior support represented for the exact proposition/scope/time
E  relevant evaluation/check represented as executed
F  prior support/evidence fit for the current declared use
R  evidential repair/reconstruction route currently available
```

Each component may be `YES / NO / UNKNOWN` relative to a declared aperture/history. These are diagnostic views, not new canonical fields.

```text
DIAGNOSTIC_VIEW != CLAIM_TRUTH_VALUE
REPAIR_ROUTE != PERMISSION_TO_ACT
NO_RECORD != WORLD_HISTORICAL_ABSENCE
```

## 1. Existing carriers

The spine already asks a material claim to preserve, where needed:

```text
proposition
source / provenance
observation or derivation route
aperture / access boundary
freshness / observation time
supporting evidence pointer
contrary evidence / dispute
unknowns / omissions
```

It already separates retained history from current world state. The donor graph already contains `CLAIM`, `RECORD`, `ROUTE`, `CLOCK`, `APERTURE` and relations such as `REPORTS`, `INFERS`, `DISPUTES`, `RECORDS`, `VERIFIES`, `DEPENDS_ON`, and `PERSISTS_AS`.

No new primitive or claim status is required merely to derive the repair vector.

## 2. H — prior support represented

For the exact proposition, scope and time relevant to the current use:

```text
H = YES
  adequate prior support is represented

H = NO
  the declared represented history establishes that adequate support was not established

H = UNKNOWN
  the represented history is insufficient to establish either
```

A bare missing record does not justify `H = NO` unless the history aperture is adequate for that negative.

```text
NO_SUPPORT_RECORD != SUPPORT_NEVER_EXISTED
SOURCE_ANCHORED != PROPOSITION_SUPPORTED
NO_ESTABLISHED_SUPPORT_IN_ONE_LEDGER != WORLD_HISTORICAL_ABSENCE
```

## 3. E — evaluation represented as executed

```text
E = YES
  a relevant evaluation/check/adjudication is represented as having executed

E = NO
  a bounded history adequate for the event class establishes that it did not execute

E = UNKNOWN
  no adequate positive or negative event history is available
```

```text
NO_EVALUATION_RECORD != EVALUATION_NEVER_OCCURRED
CHECK_PATH_EXISTS != CHECK_EXECUTED
CHECK_EXECUTED != CLAIM_SURVIVED_CHECK
```

An executed evaluation may support, dispute, falsify, or fail to resolve the proposition. `E = YES` is not a result status.

## 4. F — fit for current declared use

`F` asks whether the represented support/evidence remains applicable to the current proposition, scope and time.

Possible causes of `F = NO` include:

```text
world change
evidence expiry
scope or target-set change
changed aperture
changed capability / authority / control
superseding evidence
changed dependency or route
```

```text
HISTORICALLY_SUPPORTED != CURRENTLY_SUPPORTED
OLD_EVIDENCE != CURRENT_STATE
RETAINED_RECORD != CURRENT_STATE
```

The old shorthand `DECAYED` is at most a derived label for a case such as `H = YES, F = NO`. It is not a new claim status and need not survive into the final spine.

## 5. R — repair/reconstruction route available

`R` prevents the diagnostic from recommending endless re-derivation when the load-bearing evidence needed for historical adjudication no longer exists or is unreachable.

```text
R = YES
  a represented route can still acquire, reproduce, re-observe, or validly reconstruct the needed evidence/evaluation

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

## 6. Repair implications

The vector does not select an action. It exposes why different evidential moves are available.

### Prior support no longer fits

```text
H = YES
F = NO
```

Possible evidential move when `R = YES`:

```text
refresh / re-observe / re-derive through an appropriate current route
or narrow the proposition to the supported historical scope/time
```

### Evaluation executed but support not established

Typical represented pattern:

```text
E = YES
H != YES for the proposition now asserted
```

Do not repair this merely by refreshing the assertion timestamp. Inspect what the evaluation actually discriminated; seek a different support route if warranted; or keep/narrow/retract the unsupported proposition as the external use requires.

```text
EVALUATED != SUPPORTED
FRESH_ASSERTION != FRESH_EVIDENCE
```

### Evaluation status unresolved

```text
E = UNKNOWN
H != YES
```

If `R = YES`, an evaluation may be constituted/run or located. If `R = NO`, preserve the historical evidential limit rather than retrying a route that cannot reconstruct the proposition.

### Irrecoverable historical adjudication

An instrument may preserve `MISMATCH` and named failed checks while the expected projection needed to adjudicate the historical state is absent from surviving evidence.

```text
EXPECTED_PROJECTION_ABSENT_FROM_SURVIVING_EVIDENCE
    != EXPECTED_PROJECTION_NEVER_EXISTED

UNRESOLVED_WITH_LIVE_EVIDENCE_ROUTE
    != UNADJUDICABLE_FROM_SURVIVING_EVIDENCE
```

Historical repair may be impossible while a future mechanism repair remains possible—for example, preserving expected-state evidence before comparable future actuation.

## 7. Non-AI transfer — calibration triplet

Three current dashboard claims read `sensor reading is acceptable`.

### A — prior calibration expired

A traceable calibration previously supported the same range, but its validity interval no longer covers today's use.

```text
H = YES
E = YES
F = NO
R = YES
```

Refresh/recalibrate or narrow to the historical claim.

### B — current calibration comparison failed tolerance

A relevant current comparison ran and did not establish the acceptable-within-tolerance proposition.

```text
E = YES
H != YES for the current acceptability proposition
F != YES
R = YES
```

The right evidential move is not to refresh the old certificate.

### C — replacement sensor, incomplete history

A replacement sensor is listed by serial number, but the supplied history contains no calibration comparison and is not independently known to be exhaustive.

```text
H = UNKNOWN
E = UNKNOWN
F = UNKNOWN
R = YES if a current comparison can still be run
```

Do not convert missing history into `never evaluated`.

## 8. Falsification targets

Delete or demote this view if hostile cases show:

1. `H/E/F/R` do not change the available evidential repair;
2. the same repair is appropriate across materially different vectors;
3. `H` and `F` cannot be separated without duplicating the proposition's ordinary scope/time fields;
4. `E` adds no information beyond existing check records;
5. `R` is just ordinary route status and therefore need not appear in a diagnostic view;
6. bounded negative history can never produce useful `NO` rather than `UNKNOWN`;
7. a missing record is still silently treated as a never-event;
8. evaluation execution is mistaken for support or falsity;
9. the view requires universal event logging;
10. the view imports a value, authority, priority or action selector;
11. an unfamiliar receiver given only the ordinary spine already chooses the correct repair in the transfer cases without this view.

## 9. Current disposition

```text
NEW CLAIM STATUS:             NO
THREE EXCLUSIVE CLASSES:      REJECT
ABSOLUTE NEVER_* LABELS:      REJECT
DECAYED:                      OPTIONAL DERIVED SHORTHAND AT MOST
H/E/F/R REPAIR VECTOR:        HOSTILE-REVIEW CANDIDATE
PREFERRED FINAL STATUS:       DERIVED / SMALLER / POSSIBLY DELETE
```

The build succeeds if the taxonomy disappears and the correct repair remains visible.
