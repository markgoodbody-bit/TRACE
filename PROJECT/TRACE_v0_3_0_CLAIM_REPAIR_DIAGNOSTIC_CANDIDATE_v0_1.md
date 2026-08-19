# TRACE v0.3.0 — CLAIM REPAIR DIAGNOSTIC CANDIDATE v0.1

**Status:** WORKING DERIVED VIEW — NOT FORMAL BASELINE — NOT CANON — NOT VALIDATED — NOT NEW CLAIM STATUS — NOT AUTHORITY — NOT PERMISSION — NOT CLEARANCE  
**Motivation:** live cases previously compressed as `DECAYED / NEVER_SUPPORTED / NEVER_EVALUATED` imply different repair routes, but the labels overlap and the word `NEVER` can overclaim historical completeness.

## 0. Build claim

Do not add `DECAYED`, `NEVER_SUPPORTED`, or `NEVER_EVALUATED` as universal claim statuses.

Instead derive repair-relevant diagnostics from existing TRACE claim/evidence/history structure along at least three separable axes:

```text
A  SUPPORT HISTORY
   what support for the proposition is represented as having been established, when, and for what scope

B  EVALUATION HISTORY
   what relevant evaluation/check/adjudication is represented as having occurred

C  CURRENT APPLICABILITY
   whether earlier support/evaluation remains current enough for the declared use
```

The purpose of the view is not classification for its own sake. It is to avoid attempting the wrong repair.

```text
DIAGNOSTIC_LABEL != TRUTH_VALUE
DIFFERENT_HISTORY != DIFFERENT_TRUTH_VALUE
REPAIR_ROUTE != PERMISSION_TO_ACT
```

## 1. Existing TRACE carriers

The current spine already asks a material claim to preserve, where needed:

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

Retained history is already separate from current world state.

The donor graph also has existing `CLAIM`, `RECORD`, `ROUTE`, `CLOCK`, `APERTURE` structure and relations including `REPORTS`, `INFERS`, `DISPUTES`, `RECORDS`, `VERIFIES`, `DEPENDS_ON`, `PERSISTS_AS` and others sufficient to represent evaluation history without a new node type.

No new primitive is proposed.

## 2. Axis A — represented support history

For the exact proposition/scope/time relevant to the current use, distinguish only what the represented history warrants:

```text
SUPPORT_ESTABLISHED_FOR_PRIOR_SCOPE_TIME
NO_ESTABLISHED_SUPPORT_IN_REPRESENTED_HISTORY
SUPPORT_HISTORY_UNKNOWN_OR_INCOMPLETE
```

Do **not** silently upgrade the second form to universal historical absence.

```text
NO_SUPPORT_RECORD != SUPPORT_NEVER_EXISTED
NO_ESTABLISHED_SUPPORT_IN_REPRESENTED_HISTORY != PROPOSITION_FALSE
SOURCE_ANCHORED != PROPOSITION_SUPPORTED
```

A source can perfectly establish that an assertion/configuration/report existed without establishing the world proposition later attributed to it.

## 3. Axis B — represented evaluation history

Distinguish:

```text
EVALUATION_RECORDED
NO_EVALUATION_RECORDED_IN_REPRESENTED_HISTORY
EVALUATION_HISTORY_UNKNOWN_OR_INCOMPLETE
```

Again, the negative is bounded by the represented history.

```text
NO_EVALUATION_RECORD != EVALUATION_NEVER_OCCURRED
CHECK_PATH_EXISTS != CHECK_EXECUTED
CHECK_EXECUTED != CLAIM_SURVIVED_CHECK
```

Where a bounded process record independently establishes exhaustive evaluation-event accounting for the relevant interval, a stronger negative may be warranted **relative to that declared aperture**. World-universal `NEVER` does not follow merely from silence in one ledger.

## 4. Axis C — current applicability

Earlier support may have been adequate and still fail the current use because of:

```text
world change
evidence expiry
scope change
target-set change
changed aperture
changed capability / authority / control
superseding evidence
changed dependency or route
```

Represent, where warranted:

```text
CURRENT_FOR_DECLARED_USE
PRIOR_SUPPORT_NOT_CURRENT_FOR_DECLARED_USE
CURRENT_APPLICABILITY_UNKNOWN
```

```text
HISTORICALLY_SUPPORTED != CURRENTLY_SUPPORTED
OLD_EVIDENCE != CURRENT_STATE
RETAINED_RECORD != CURRENT_STATE
```

`DECAYED` may remain a convenient derived shorthand for the second case **only when prior adequate support is actually represented**.

## 5. Derived repair view

A compact repair diagnostic can be derived without changing the underlying claim status.

### Case 1 — prior support, no longer current

```text
support history       prior adequate support represented
evaluation history    may be recorded or irrelevant to the decay mechanism
current applicability not current / unresolved
```

Typical structural repair:

```text
refresh / re-observe / re-derive through an appropriate current route
or narrow the proposition to the historical scope/time
```

This is the clean case for derived shorthand `DECAYED`.

### Case 2 — proposition evaluated, support not established

```text
support history       no adequate support established in represented history
evaluation history    relevant evaluation recorded
current applicability not upgraded by freshness alone
```

Typical structural repair:

```text
inspect what the evaluation actually discriminated
seek a different evidential route if warranted
or narrow / retract the unsupported proposition
```

Refreshing the timestamp of the same inadequate source does not repair this.

### Case 3 — no relevant evaluation recorded

```text
support history       no adequate support established in represented history
evaluation history    no relevant evaluation recorded in represented history
current applicability cannot be established from freshness of the assertion alone
```

Typical structural repair depends on whether an evaluable proposition and route can still be constituted:

```text
IF evaluable now:
    constitute/run the evaluation
ELSE IF the load-bearing expected state/evidence was never preserved and cannot be reconstructed:
    preserve UNKNOWN / retire the unsupported projection / record unrecoverable evidence loss
ELSE:
    preserve the bounded limit and avoid pretending re-derivation occurred
```

This is why `NEVER_EVALUATED` is better treated as a repair diagnostic over represented history than as a truth-like status.

## 6. Worked transfer — expired calibration / unrun comparison

Three laboratory claims look identical in a dashboard: `sensor reading is acceptable`.

### L1 — decayed support

The sensor was calibrated against a traceable standard one month ago for the same operating range. The calibration interval has expired before today's use.

```text
prior support represented: YES
relevant evaluation represented: YES
current applicability: NO / requires refresh
repair: recalibrate or narrow to historical claim
```

### L2 — evaluated but unsupported

A current calibration comparison was run and the sensor exceeded the declared tolerance.

```text
prior/current support represented: NO for acceptable-within-tolerance proposition
relevant evaluation represented: YES
repair: do not refresh the old certificate; inspect/repair/retest or retract current-acceptability claim
```

### L3 — not evaluated in represented history

A replacement sensor was installed. The log contains a configuration entry and serial number but no calibration comparison record. The supplied history is not independently known to be exhaustive.

```text
support established in represented history: NO
evaluation recorded in represented history: NO
world claim `never evaluated`: NOT ESTABLISHED
repair: run/locate an appropriate evaluation if still possible; otherwise preserve UNKNOWN
```

The same three-way repair difference transfers without AI-specific assumptions.

## 7. Unrecoverable-evidence case

An instrument records `MISMATCH` and names failed checks, but the expected projection against which the mismatch should be adjudicated was never preserved in the available record. Later reconstruction cannot determine what correct public state was expected.

Do not compress this to `unresolved` if the missing evidence makes the prior proposition unadjudicable from surviving records.

But also do not automatically claim the expected projection was never constituted anywhere in the world.

```text
EXPECTED_PROJECTION_ABSENT_FROM_SURVIVING_RECORD
    !=
EXPECTED_PROJECTION_NEVER_EXISTED

UNRESOLVED_WITH_LIVE_EVIDENCE_ROUTE
    !=
UNADJUDICABLE_FROM_SURVIVING_EVIDENCE
```

Repair may be impossible for the historical proposition while a mechanism repair remains possible for future cases: require expected-state evidence to be preserved before comparable actuation.

```text
HISTORICAL_CLAIM_UNREPAIRABLE != FUTURE_MECHANISM_UNREPAIRABLE
```

## 8. Falsification targets

Delete or demote this view if hostile cases show:

1. support and evaluation history cannot be separated without inventing new semantics;
2. the three axes add no repair information beyond ordinary claim/evidence/freshness prose;
3. `NO_*_IN_REPRESENTED_HISTORY` becomes procedural hedging that never permits a useful negative;
4. a bounded exhaustive history aperture cannot justify stronger historical absence when it should;
5. the view mistakes failure to support for evidence of falsity;
6. `DECAYED` is applied without represented prior adequate support;
7. the same repair route is appropriate regardless of the diagnostic state;
8. the view requires universal event logging to function;
9. an unavailable historical evaluation is treated as though it never occurred;
10. the diagnostic imports a value, authority or action selector.

## 9. Current disposition

```text
NEW CLAIM STATUS:                 NO
THREE EXCLUSIVE CLASSES:          REJECT
DECAYED AS DERIVED SHORTHAND:     POSSIBLY USEFUL
NEVER_SUPPORTED AS ABSOLUTE:      REJECT
NEVER_EVALUATED AS ABSOLUTE:      REJECT
SUPPORT/EVALUATION/FRESHNESS VIEW: HOSTILE-REVIEW CANDIDATE
PREFERRED FINAL STATUS:           DERIVED DIAGNOSTIC OR DELETE
```

The strongest deletion test is simple:

> If an unfamiliar receiver given only the ordinary spine already chooses the right repair in the three laboratory cases without this view, delete it rather than teach another taxonomy.
