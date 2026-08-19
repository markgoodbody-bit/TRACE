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

Requires a declared current-state source, check time, and explicit current reacquisition.

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

This is only a falsifier for an obvious omission.

```text
LEXICAL_HIT -> POSSIBLE_UNDECLARED_MODE
NO_LEXICAL_HIT != NO_UNDECLARED_MODE
MATCHER_PRESENT != MATCHER_ADEQUATE
```

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

## Run

From this directory:

```bash
python correction_preflight.py envelope.json
python correction_preflight.py envelope.json --json
python -m unittest -v test_correction_preflight.py
```

Exit codes:

```text
0  NOT_APPLICABLE or DECLARED_SUPPORT_FIELDS_PRESENT
1  MODE_DECLARATION_CHALLENGED or STRUCTURAL_GAP
2  INPUT_ERROR
```

Exit `0` is not clearance.

## First hostile fixtures

The test file freezes eight cases:

1. stale record used for a `CURRENT` claim;
2. selected denominator with a known omitted target for `COMPLETE`;
3. repeated execution through an instrument with a known blind spot for `VERIFIED`;
4. reachable rollback with unknown arrival-before-hardening for `CORRECTABLE`;
5. mundane `7 x 8` control — the checker must stay out of the way;
6. a bounded completeness claim with its declared comparison basis present;
7. undeclared `100%` language must return `MODE_DECLARATION_CHALLENGED`, never a green-looking success state;
8. capability evidence incorrectly substituted for `AUTHORIZED`.

All eight branches were exercised before the current review head. They are regression tests, not validation.

## Epistemic ceiling

This checker does **not** establish:

- truth of the claim;
- completeness of the target set in the world;
- adequacy of a caller-selected comparison basis;
- actual current-world correspondence;
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
