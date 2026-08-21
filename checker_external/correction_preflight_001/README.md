# TRACE correction preflight 001

Status: **checker-external working candidate**  
Candidate ID: `TRACE-CORRECTION-PREFLIGHT-001`

TRACE change: **none**  
Minimum-schema change: **none**  
Authority / permission change: **none**

## Purpose

Turn a small set of repeatedly observed false-closure failures into executable refusal conditions before a bounded claim is relied on.

The checker is deliberately narrower than TRACE. It does not build a full packet and does not decide whether a claim is true, safe, good, legitimate or permitted.

It checks only five declared claim modes:

```text
CURRENT
COMPLETE
VERIFIED
CORRECTABLE
AUTHORIZED
```

The question is: if a caller uses one of these strong modes, is the minimum declared support structure needed for that mode present?

## Why this is not another universal checker

The candidate is justified only by recurrent failure shapes:

```text
OLD_RECORD != CURRENT_STATE
ALL_SELECTED_TARGETS_PASS != ALL_RELEVANT_TARGETS_PASS
CHECK_EXISTS != CHECK_EXECUTED
TEST_RAN != RELEVANT_ALTERNATIVE_DETECTABLE
ROUTE_EXISTS != ROUTE_REACHABLE
ROUTE_REACHABLE != CLOSURE_PREDICATE_SATISFIABLE
CAPABILITY != AUTHORITY
```

It is an application-layer experiment, not a new TRACE primitive or formal status system.

## CURRENT

Requires:

```text
source_ref
checked_at_utc
reference_time_utc
max_age_seconds
reacquired = true
```

`checked_at_utc` and `reference_time_utc` must be parseable timezone-aware timestamps and `max_age_seconds` must be positive.

The checker now uses two different temporal relations:

1. observation age is computed from declared `reference_time_utc - checked_at_utc` and must fit the declared maximum age;
2. the declared `reference_time_utc` must be within 300 seconds of the runner's UTC execution clock.

The second relation is deliberately not supplied by the claimant envelope. It exists because hostile rerun KI-COM-012 demonstrated that a claimant could otherwise make a 2019 observation formally CURRENT by choosing a 2019 reference clock, or choose a far-future clock and a large age window.

```text
PARSEABLE_TIME != TRUE_TIME
DECLARED_REFERENCE_TIME != RUNNER_NOW
RUNNER_CLOCK != TRUE_TIME
DECLARED_MAX_AGE != ADEQUATE_FRESHNESS_POLICY
REACQUIRED != CURRENT
```

Moving the reference anchor to execution context prevents the claimant from choosing "now" for the checker. It does **not** establish that the machine clock is correct, that the source is valid, or that the chosen freshness policy is adequate.

## COMPLETE

Requires a declared target/denominator set, selection basis, comparison basis, and coverage status relative to that basis.

`NONE_ESTABLISHED` for known omissions is not upgraded to world completeness.

## VERIFIED

Requires the exact proposition, represented execution, instrument adequacy for that proposition, a result reference, and a represented route back to the current use.

## CORRECTABLE

Requires:

```text
route_ref
reachability = YES
closure_predicate_ref
closure_predicate_status = ESTABLISHED_FOR_REPRESENTED_TRANSITION
hardening_ref
arrives_before_hardening = YES
```

The closure predicate is the exact proposition/condition the route must be capable of satisfying. This field was added after the CC/125 field specimen showed a reachable witness-investigation route whose resolver compared public reads against the wrong digest. The route could execute, but its closure predicate could not become true under the represented server normalisation.

```text
ROUTE_PRESENT != ROUTE_EXECUTABLE
ROUTE_REACHABLE != CLOSURE_PREDICATE_SATISFIABLE
CHECK_EXISTS != CHECKS_THE_RIGHT_PROPOSITION
EXAMINATION_COMPLETED != CLOSURE_ROUTE_EXECUTABLE
```

`closure_predicate_status` is still claimant-supplied declaration structure. `ESTABLISHED_FOR_REPRESENTED_TRANSITION` does not prove that the predicate is satisfiable in the world; the supporting reference must still resolve outside this checker before a green result becomes load-bearing.

## AUTHORIZED

Requires an authority/grant reference, action/scope reference, and current applicability. Capability alone is explicitly insufficient.

## Lexical sentinel

A deliberately weak one-way lexical sentinel flags obvious strong words when the matching mode is undeclared.

```text
LEXICAL_HIT -> POSSIBLE_UNDECLARED_MODE
NO_LEXICAL_HIT != NO_UNDECLARED_MODE
MATCHER_PRESENT != MATCHER_ADEQUATE
LEXICAL_MATCH != POLARITY_UNDERSTOOD
```

It intentionally does not parse polarity. A true negative such as `not verified` can trigger the `VERIFIED` notice. This must not be promoted into semantic clearance machinery.

## Output statuses and exits

```text
0  DECLARED_SUPPORT_FIELDS_PRESENT
1  MODE_DECLARATION_CHALLENGED or STRUCTURAL_GAP
2  INPUT_ERROR
3  NOT_APPLICABLE
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

The CLI obtains the CURRENT execution anchor from the runner clock. Unit tests inject a fixed timezone-aware runner time so clock cases remain deterministic.

## Hostile-run history

The first hostile run found:

- arbitrary/stale timestamp strings could satisfy CURRENT;
- `NOT_APPLICABLE` shared exit `0` with substantive structural green;
- the lexical sentinel was polarity-blind.

Those were repaired/repriced without enlarging TRACE core.

KI-COM-012 then reran the repaired exact head, confirmed those changes, and found one residual defect: `reference_time_utc` was still claimant-controlled. Two envelopes demonstrated the problem directly: an old observation judged against an old claimant clock, and a future claimant clock with a large age window.

The runner-clock repair moved only that temporal anchor one step outside the envelope. KI-COM-014 then reran K1-K5 plus boundary probes and reported that the prior temporal attacks were repaired or honestly bounded by `RUNNER_CLOCK != TRUE_TIME`.

A later live Campfire witness-investigation specimen exposed a different CORRECTABLE gap. The server normalised a submitted body, public reads matched the recorded public-projection digest, but the resolver compared those reads against the pre-normalisation sent-body digest. The correction route existed and could execute, yet its closure predicate was unsatisfiable under the represented transition. This head therefore requires the closure proposition/predicate and a declared satisfiability status rather than allowing route reachability alone to stand in for correctability.

No TRACE-core primitive, semantic parser or authority rule is added.

## Regression fixtures

The test file now contains seventeen cases, including:

- stale/reacquired CURRENT;
- unparseable CURRENT time;
- bounded CURRENT with a runner-aligned reference clock;
- claimant-selected old reference clock refusal;
- claimant-selected future reference clock refusal;
- selected denominator with a known omitted target for COMPLETE;
- repeated execution through an instrument with a known blind spot for VERIFIED;
- reachable rollback with unknown arrival-before-hardening for CORRECTABLE;
- reachable correction route with a contradicted closure predicate for CORRECTABLE;
- a bounded CORRECTABLE declaration shape with an established represented closure predicate;
- mundane `7 x 8` control;
- bounded completeness relative to a declared comparison basis;
- undeclared `100%` sentinel challenge;
- explicit polarity-blind sentinel behavior;
- capability substituted for AUTHORIZED;
- machine distinction between NOT_APPLICABLE and substantive structural green.

They are authored regression tests, not validation or hosted-CI evidence.

## Epistemic / consumption ceiling

Most evidential fields remain supplied by the claimant/caller. This checker does not resolve `source_ref`, `result_ref`, `authority_ref`, `closure_predicate_ref`, or other references against an independent source. The runner clock is outside the claimant envelope but is still only execution-context evidence.

Therefore:

```text
FIELD_PRESENT != EVIDENCE_VALID
SELF_DECLARED_REFERENCE != EXTERNAL_WITNESS
DECLARED_CLOSURE_STATUS != WORLD_SATISFIABILITY
RUNNER_CLOCK != TRUE_TIME
DECLARED_SUPPORT_FIELDS_PRESENT != INDEPENDENT_SUPPORT
CHECKER_GREEN != CLAIM_TRUE
```

A green result can become load-bearing only through evidence that resolves outside the envelope/checker.

This checker does not establish truth, world completeness, comparison-basis adequacy, source validity, true time, freshness-policy adequacy, genuine instrument adequacy, actual correction, actual closure-predicate satisfiability, legitimate authority, moral adequacy, safety, permission to act, or completeness of declared claim modes.

## Kill / shrink conditions

Delete or shrink this candidate if existing checker-external machinery supplies the same useful refusals, callers satisfy it ritualistically, the sentinel creates false confidence, the five modes become a hidden universal taxonomy, callers evade it by changing wording, a smaller rule produces the same useful refusals, or it starts being treated as clearance.

Preferred final status:

```text
SMALL APPLICATION CHECK
or
DELETE
```

The build succeeds only if it makes a few recurring false closures harder without making TRACE itself larger.
