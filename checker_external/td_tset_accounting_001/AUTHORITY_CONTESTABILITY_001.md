# TD-AUTHORITY-CONTESTABILITY-001

Status: **checker-external working candidate**

TRACE change: **none**

Minimum-schema change: **none**

Authority-handoff change: **none**

## Source-grounded boundary

TRACE v0.2.5 distinguishes a visible route from an effective one. A route may need to be reachable, authority-effective, fast enough, and exposed for capture and independence. It also distinguishes commitment from later correction and does not let a declared brake imply actual interruption.

This candidate tests only a narrow continuation of the authority-handoff work:

> After an authority handoff is represented, can a conflicting aperture result reach a declared brake before a declared contest deadline?

## Core distinction

> Visible authority is not contestable authority.

A selector, owner, policy and route may all be declared while the opposing aperture has no usable path to interrupt or delay the selected transition.

## External comparison envelope

```json
{
  "authority_contestability_evidence": {
    "assessment_status": "ASSESS",
    "conflict_status": "DIVERGENT",
    "selected_transition_ref": "n_transition_launch",
    "challenging_aperture_result_refs": [
      "n_record_dispatch_result"
    ],
    "contest_route_ref": "n_route_dispatch_contest",
    "brake_ref": "n_brake_safety",
    "route_clock_ref": "n_clock_contest_route",
    "contest_deadline_clock_ref": "n_clock_contest_deadline",
    "conflict_claim_refs": ["c_aperture_conflict"],
    "contest_authority_claim_refs": ["c_brake_authority"]
  }
}
```

The comparison envelope remains checker-external. The deadline may represent commitment, irreversibility or another declared contest boundary; the checker does not invent its meaning.

## What the checker requires

For a divergent, assessable case:

- a represented selected transition;
- at least one challenging aperture-result record;
- a `ROUTE` from that result toward a represented `BRAKE`;
- `ROUTES_TO` edges from result to route and route to brake;
- a `BRAKES` edge from brake to selected transition;
- resolvable conflict and contest-authority claims bound to the route;
- capture status kept explicit;
- route and contest-deadline clocks when available.

The strict timing comparison is:

```text
route_seconds < contest_deadline_seconds
```

Equality is not “before.”

## Outcomes

### `DECLARED_ROUTE_REACHES_BRAKE_BEFORE_DEADLINE`

The packet contains a declared, uncaptured route to a bound brake and its route clock is strictly below the supplied contest deadline.

This is not proof that the route or brake works.

### `CONTEST_ROUTE_TOO_SLOW`

The declared route reaches the brake at or after the declared deadline.

### `NO_CONTEST_ROUTE`

No route from the challenging aperture result to a brake is supplied.

### `CONTEST_ROUTE_CAPTURED`

The route is explicitly marked captured.

### `CONTESTABILITY_UNKNOWN`

Capture status, route latency or deadline remains `UNKNOWN`. This is preserved without converting uncertainty into failure or permission.

### `UNSUPPORTED_CONTEST_ROUTE`

The route lacks the required topology or an external contest-authority claim.

## Fixtures AG–AL

| Fixture | Expected result |
|---|---|
| AG — challenge reaches brake in 4 s before 20 s deadline | PASS / `DECLARED_ROUTE_REACHES_BRAKE_BEFORE_DEADLINE` |
| AH — challenge route requires 25 s against 20 s deadline | FAIL / `TD-AUTHORITY-CONTEST-ROUTE-TOO-SLOW` |
| AI — no challenge route | FAIL / `TD-AUTHORITY-CONTEST-NO-ROUTE` |
| AJ — route explicitly captured | FAIL / `TD-AUTHORITY-CONTEST-ROUTE-CAPTURED` |
| AK — capture and route clock unresolved | PASS / `CONTESTABILITY_UNKNOWN` |
| AL — route lacks external contest authority | FAIL / `TD-AUTHORITY-CONTEST-UNSUPPORTED-STATUS` |

Hostile regressions additionally test equal route/deadline clocks, unresolved challenge-result references, no comparison envelope and absence of divergence.

## Finding

The authority-handoff checker can show who selected and under what declared basis. This candidate asks whether a contrary aperture can still alter the trajectory in time.

```text
DECLARED_AUTHORITY_HANDOFF
!=
CONTESTABLE_AUTHORITY_HANDOFF
```

## Epistemic ceiling

PASS does not establish:

- legitimate authority;
- actual route executability;
- brake independence or effectiveness;
- correct challenge;
- complete target selection;
- lawful procedure;
- permission to proceed;
- world truth.
