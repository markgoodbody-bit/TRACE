# TRACE correction preflight 001

Status: **checker-external working candidate**  
Candidate ID: `TRACE-CORRECTION-PREFLIGHT-001`

TRACE change: **none**  
Minimum-schema change: **none**  
Authority / permission change: **none**

## Purpose

Turn a small set of repeatedly observed false-closure failures into executable refusal conditions before a bounded claim is relied on.

The checker is deliberately narrower than TRACE. It does not build a full packet and does not decide whether a claim is true, safe, good, legitimate or permitted.

It checks only five **declared claim modes**:

```text
CURRENT
COMPLETE
VERIFIED
CORRECTABLE
AUTHORIZED
```

The question is:

> If a caller uses one of these strong words, is the minimum declared support structure needed for that word present?

## Why this is not another universal checker

The existing checker-external integration already warns against automatic checker proliferation. This candidate is justified only by concrete recurrent failure shapes:

```text
OLD_RECORD != CURRENT_STATE
ALL_SELECTED_TARGETS_PASS != ALL_RELEVANT_TARGETS_PASS
CHECK_EXISTS != CHECK_EXECUTED
TEST_RAN != RELEVANT_ALTERNATIVE_DETECTABLE
ROUTE_EXISTS != ROUTE_REACHABLE
CAPABILITY != AUTHORITY
```

It is an application-layer experiment, not a new TRACE primitive or formal status system.

## Input envelope

A minimal JSON object contains:

```json
{
  "fixture_id": "example",
  "claim_text": "All registered devices passed tonight.",
  "claim_modes": ["COMPLETE"],
  "coverage": {
    "target_set_ref": "registered-devices",
    "selection_basis_ref": "asset-register",
    "comparison_basis_ref": "all-relevant-devices",
    "coverage_status": "UNKNOWN",
    "known_omissions": "UNKNOWN"
  }
}
```

Only sections required by the declared modes are inspected.

### CURRENT

Requires:

```text
source_ref
checked_at_utc
reference_time_utc
max_age_seconds
reacquired = true
```

`checked_at_utc` and `reference_time_utc` must be parseable timezone-aware timestamps. `max_age_seconds` must be positive. The checker computes the observation age relative to the **declared** reference time and refuses a future-dated observation or one older than the **declared** maximum age.

This is deliberately not a world clock:

```text
PARSEABLE_TIME != TRUE_TIME
DECLARED_REFERENCE_TIME != TRUSTED_NOW
DECLARED_MAX_AGE != ADEQUATE_FRESHNESS_POLICY
REACQUIRED != CURRENT
```

The clock check prevents the old failure where an arbitrary non-empty timestamp such as `yesterday-ish`, or a seven-year-old timestamp paired with `reacquired:true`, could look structurally current. It still depends on externally justified time/freshness inputs if the result is to become load-bearing.

### COMPLETE

Requires a declared target/denominator set, selection basis, comparison basis, and coverage status relative to that basis.

`NONE_ESTABLISHED` for known omissions is **not** upgraded to world completeness.

### VERIFIED

Requires the exact proposition, represented execution, instrument adequacy for that proposition, a result reference, and a represented route back to the current use.

### CORRECTABLE

Requires a correction route, represented current reachability, a hardening/closure boundary, and support that correction arrives before that boundary.

### AUTHORIZED

Requires an authority/grant reference, action/scope reference, and current applicability. Capability alone is explicitly insufficient.

## Lexical sentinel

The checker also contains a deliberately weak one-way lexical sentinel for obvious words such as:

```text
all / every / 100%
current / now / tonight
verified / checked / tested
reversible / rollback
authorized / permitted
```

A lexical hit can produce:

```text
PREFLIGHT-UNDECLARED-MODE-SUSPECTED
```

if the caller did not declare the matching claim mode.

This is only a noisy falsifier for an obvious omission.

```text
LEXICAL_HIT -> POSSIBLE_UNDECLARED_MODE
NO_LEXICAL_HIT != NO_UNDECLARED_MODE
MATCHER_PRESENT != MATCHER_ADEQUATE
LEXICAL_MATCH != POLARITY_UNDERSTOOD
```

The sentinel intentionally does **not** attempt semantic or polarity parsing. A true negative such as `not verified` can still trigger the `VERIFIED` notice. That false positive is accepted as a limitation of a cheap one-way challenge; it must not be promoted into a truth parser or relied on as a clearing mechanism.

A sentinel challenge is therefore not allowed to return the same top-level state as a clean declared envelope.

## Output statuses

```text
NOT_APPLICABLE
  no declared mode and no sentinel challenge

MODE_DECLARATION_CHALLENGED
  lexical sentinel suggests an undeclared strong claim mode;
  inspect the trigger rather than treating omission as absence

DECLARED_SUPPORT_FIELDS_PRESENT
  no declared structural gap found for the modes the caller actually declared

STRUCTURAL_GAP
  at least one required declared support relation is missing, unknown,
  contradicted or inadequate for the claimed mode

INPUT_ERROR
  envelope cannot be interpreted
```

`DECLARED_SUPPORT_FIELDS_PRESENT` is deliberately weaker than `PASS`, `SAFE`, `VALID`, `TRUE`, `AUTHORIZED`, or `CLEAR`.

```text
DECLARED_SUPPORT_FIELDS_PRESENT != CLAIM_TRUE
DECLARED_SUPPORT_FIELDS_PRESENT != SUPPORT_FIELDS_WORLD_VALID
MODE_DECLARATION_UNCHALLENGED != MODES_COMPLETE
```

## Machine-consumption boundary

`NOT_APPLICABLE` is now deliberately machine-distinct from substantive structural green.

Exit codes:

```text
0  DECLARED_SUPPORT_FIELDS_PRESENT
1  MODE_DECLARATION_CHALLENGED or STRUCTURAL_GAP
2  INPUT_ERROR
3  NOT_APPLICABLE
```

A caller must not interpret `3` as a failed substantive check or `0` as clearance. The separation exists only to prevent `nothing was declared / nothing was examined` from being machine-indistinguishable from the checker finding no structural gap in declared modes.

## Run

From this directory:

```bash
python correction_preflight.py envelope.json
python correction_preflight.py envelope.json --json
python -m unittest -v test_correction_preflight.py
```

## Hostile-run repair

A hostile run against the prior head exposed three material limits:

1. `CURRENT` accepted arbitrary/stale timestamp strings because it checked non-empty presence only.
2. `NOT_APPLICABLE` shared exit `0` with substantive structural green.
3. the lexical sentinel is polarity-blind.

This repair:

- adds a declared, parseable temporal comparison for `CURRENT`;
- gives `NOT_APPLICABLE` its own machine exit code;
- keeps the sentinel explicitly noisy/polarity-blind instead of growing an NLP subsystem;
- moves the self-declaration/external-resolution ceiling into the normal output text.

This is a repair/reprice of the application checker, not evidence for a TRACE-core change.

## Regression fixtures

The test file now freezes thirteen cases, including:

- stale/reacquired `CURRENT`;
- unparseable `CURRENT` time;
- a bounded currentness declaration whose clock shape is internally coherent;
- selected denominator with a known omitted target for `COMPLETE`;
- repeated execution through an instrument with a known blind spot for `VERIFIED`;
- reachable rollback with unknown arrival-before-hardening for `CORRECTABLE`;
- mundane `7 x 8` control;
- bounded completeness relative to a declared comparison basis;
- undeclared `100%` sentinel challenge;
- explicit polarity-blind sentinel behavior;
- capability substituted for `AUTHORIZED`;
- machine distinction between `NOT_APPLICABLE` and substantive structural green.

They are regression tests, not validation.

## Epistemic / consumption ceiling

Every field in the envelope is supplied by the claimant/caller. This checker does not resolve `source_ref`, `result_ref`, `authority_ref`, or other references against an independent source.

Therefore:

```text
FIELD_PRESENT != EVIDENCE_VALID
SELF_DECLARED_REFERENCE != EXTERNAL_WITNESS
DECLARED_SUPPORT_FIELDS_PRESENT != INDEPENDENT_SUPPORT
CHECKER_GREEN != CLAIM_TRUE
```

A green result can become load-bearing only through evidence that resolves **outside** the envelope/checker — for example a hash/pointer that a separate route actually resolves, or an independent aperture that verifies the relevant external object.

This checker does **not** establish:

- truth of the claim;
- completeness of the target set in the world;
- adequacy of a caller-selected comparison basis;
- actual current-world correspondence;
- trustworthiness of the caller-declared reference time or freshness policy;
- genuine instrument adequacy beyond the supplied declaration;
- actual route reachability or correction;
- legitimate authority;
- moral adequacy;
- safety;
- permission to act;
- that no undeclared claim mode exists.

It can still be gamed by dishonest or defective inputs. It is useful only where making the support boundary explicit is cheaper than repeatedly allowing strong words to inherit unsupported meaning.

## Kill / shrink conditions

Delete or shrink this candidate if:

1. existing checker-external machinery already supplies the same pre-use refusal without this wrapper;
2. callers satisfy it ritualistically without improving the underlying evidence path;
3. the lexical sentinel creates false confidence or noisy expansion;
4. the five modes become a hidden universal taxonomy;
5. callers evade it simply by avoiding the strong words while making the same inference;
6. a smaller rule produces the same useful refusals;
7. it starts being treated as clearance.

Preferred final status:

```text
SMALL APPLICATION CHECK
or
DELETE
```

The build succeeds only if it makes a few recurring false closures harder without making TRACE itself larger.
