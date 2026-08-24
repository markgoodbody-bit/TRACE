# TRACE v0.3.0 — SPINE v0.7 ROUTE-BINDING REPAIR DELTA v0.1

**Status:** WORKING REPAIR DELTA — NOT INTEGRATED SPINE — NOT FORMAL BASELINE — NOT CANON — NOT VALIDATED  
**Parent:** `PROJECT/TRACE_v0_3_0_SPINE_CANDIDATE_v0_7.md`  
**Failure witness:** `falsification/TRACE_v0_3_0_SPINE_CANDIDATE_V07_ROUTE_BINDING_ATTACK.md`

---

## 1. Repair

Retain the v0.7 provenance, acyclicity, feasibility and timing guards.

Before unioning ordering edges into a derived critical-path precedence view, bind them to the same **executable pathway hypothesis** at the resolution required by the downstream window claim.

Where load-bearing, the binding includes:

```text
process / pathway
scope
target effect/state
route-set member or execution alternative
capability context
time / policy version
use
```

For recurring or repeated stage types, bind event occurrences distinctly where collapsing occurrences could create or erase a cycle or alter timing.

```text
SAME_PROCESS_SCOPE_TIME != SAME_ROUTE_BINDING
ALTERNATIVE_ROUTE_ORDERINGS != ONE_PROCESS_CYCLE
ROUTE_MEMBERSHIP_UNKNOWN != ALL_ROUTE_EDGES_COEXECUTE
STAGE_TYPE_CYCLE != EVENT_INSTANCE_CYCLE
```

No route, stage, occurrence or scheduler primitive is added. Existing route/state/action/transition/claim/time references carry the domain identity as available.

---

## 2. Route-specific precedence views

For each represented executable pathway hypothesis `q_k`, derive only the ordering edges claimed to be load-bearing for that pathway under its current bindings:

```text
G_window(q_k,l,o,c,g,u) = (V_k, E_prec_k)
```

Each `E_prec_k`:

1. retains supporting canonical ordering claims and material mechanism references;
2. is bound to the pathway/route/capability/time/use context needed by the claim;
3. is tested for acyclicity at the event-instance resolution needed by the timing calculation;
4. remains subject to separate execution-feasibility and temporal-bound requirements.

```text
EDGE_VALID_FOR_R1 != EDGE_REQUIRED_FOR_R2
ROUTE_EXISTS != ROUTE_SELECTED
ROUTE_WINDOW_COMPUTED != ROUTE_AUTHORISED
```

TRACE may expose multiple route-specific window statuses. It does not choose a route merely because one has a wider window.

---

## 3. Unresolved route membership

If it is unknown whether an ordering edge belongs to the pathway being timed, do not silently:

```text
include it as though co-executed
exclude it as irrelevant
```

Preserve the membership uncertainty where it could change the window result.

```text
ROUTE_MEMBERSHIP_UNKNOWN != EDGE_ABSENT
ROUTE_MEMBERSHIP_UNKNOWN != EDGE_REQUIRED
```

A downstream strong window claim requires enough route membership resolution that its load-bearing precedence view is supported.

---

## 4. Recurrence / occurrence binding

A recurrent process may revisit the same stage type:

```text
A1 -> B1 -> A2 -> B2
```

The stage-type projection:

```text
A -> B -> A -> B
```

must not be treated as a cycle if the actual bounded event-instance ordering is acyclic.

Conversely, renaming occurrences must not hide a true same-execution dependency cycle.

```text
DISTINCT_EVENT_IDS != INDEPENDENT_EVENTS
OCCURRENCE_UNROLLED != CYCLE_IMPOSSIBLE
```

Use occurrence-specific references only to the extent needed to preserve ordering/timing distinctions; do not require universal event-instance expansion for static or non-timing readings.

---

## 5. Composition across alternatives

Multiple route-specific windows are not silently collapsed into one unqualified window.

```text
MULTIPLE_ROUTE_WINDOWS != ONE_ROUTE_WINDOW
BEST_WINDOW != SELECTED_ROUTE
WIDEST_CORRECTION_MARGIN != MORAL_OR_POLICY_PRIORITY
```

If a higher layer supplies a declared comparison/selection rule, TRACE may represent the resulting selection and its basis. TRACE does not invent that rule.

If the downstream proposition is existential—e.g. “at least one represented executable correction route remains within its target boundary”—the route existence/executability claim and the qualifying route-specific window must both be supported.

```text
ONE_ROUTE_FITS != ALL_ROUTES_FIT
ONE_ROUTE_FITS != ROUTE_WILL_BE_USED
```

---

## 6. Immediate attack set

Break this delta with:

1. two mutually exclusive routes with opposite orderings;
2. a true same-route `A->B` and `B->A` conflict;
3. opposite orderings under different policy versions;
4. same route label but materially changed capability context;
5. recurrent `A1->B1->A2` process whose type projection cycles;
6. distinct occurrence IDs that still form a true event-instance cycle;
7. unknown route membership for one load-bearing edge;
8. one route fits but selection/authority for that route is absent;
9. two route windows where a silent `max`/`best` aggregation would change the conclusion.

One false strong timing or route-existence claim is enough to hold the delta.

---

## 7. Disposition

```text
v0.7 FAILURE: REPAIRED IN DELTA
CANONICAL VOCABULARY CHANGE: NONE
ACYCLICITY: PER EXECUTABLE PATHWAY HYPOTHESIS
RECURRENCE: EVENT-INSTANCE RESOLUTION WHERE LOAD-BEARING
ROUTE SELECTION: EXTERNAL / REPRESENTED, NOT GENERATED
THIS DELTA: ATTACK OBJECT
```
