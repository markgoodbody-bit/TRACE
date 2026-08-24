# TRACE v0.3.0 — SPINE CANDIDATE v0.7 ROUTE-BINDING ATTACK

**Status:** MATERIAL INTEGRATION REGRESSION — HOLD v0.7  
**Target:** `PROJECT/TRACE_v0_3_0_SPINE_CANDIDATE_v0_7.md`  
**Build witness:** `PROJECT/TRACE_v0_3_0_SPINE_V07_BUILD_REPORT_v0_1.json` proves deterministic integration only; it does not establish semantic adequacy  
**Donor/repair source:** v0.6 acyclicity repair delta required process/pathway, scope, target, route/capability, time and use bindings where material

---

## 1. Counterexample — mutually exclusive correction routes

One affected scope and one correction process at the same time has two live but mutually exclusive route choices:

```text
R1:
  A = isolate service
  B = restore clean snapshot
  ordering = A -> B

R2:
  B = restore clean snapshot into parallel environment
  A = cut traffic over only after restore
  ordering = B -> A
```

Both orderings are current and supported.

Both routes address the same target effect in the same scope and time regime.

But they are **alternative executable pathways**, not stages that must coexist in one execution.

v0.7 says, before critical-path arithmetic, to bind relevant ordering edges to the same declared `process/scope/time` context and require the resulting precedence view to be acyclic.

If an implementation or unfamiliar reader collects both current edges because process/scope/time match, it obtains:

```text
A -> B
B -> A
```

and therefore `CONFLICTING_OR_CYCLIC`.

That conclusion is false for either actual route. The cycle exists only in the union of mutually exclusive alternatives.

---

## 2. Failure

```text
ALTERNATIVE_ROUTE_ORDERINGS != ONE_PROCESS_CYCLE
UNION_OF_MUTUALLY_EXCLUSIVE_PATHS != EXECUTABLE_PRECEDENCE_GRAPH
SAME_PROCESS_SCOPE_TIME != SAME_ROUTE_BINDING
CURRENT_EDGE_IN_SOME_ROUTE != EDGE_REQUIRED_IN_THIS_ROUTE
```

The error is narrower than the earlier cycle finding. Acyclicity remains required for a critical-path view; v0.7 has not bound the view tightly enough before applying that guard.

The fuller repair delta already named the missing qualifier:

```text
route/capability context where material
```

The compression into v0.7 dropped it.

---

## 3. Why this matters

The result is not merely conservative formatting. A false cycle can turn a supported correction route into `WINDOW_STATUS_UNKNOWN`, obscuring real correction capacity at exactly the point TRACE is meant to preserve it.

```text
FALSE_UNCERTAINTY != HARMLESS_UNCERTAINTY
CONSERVATIVE_STATUS != SEMANTICALLY_CORRECT_STATUS
```

TRACE should preserve uncertainty where evidence is unresolved, not manufacture uncertainty by joining incompatible alternatives.

---

## 4. Smallest repair

No new node, relation, route ontology or scheduler.

A critical-path precedence view must be bound to the **same executable pathway hypothesis** before edges are unioned.

Where load-bearing, binding includes:

```text
process / pathway
scope
target effect/state
route-set member or execution alternative
capability context
time / policy version
use
```

If route membership itself is unresolved, preserve that uncertainty rather than unioning all alternatives into one precedence graph.

```text
ROUTE_MEMBERSHIP_UNKNOWN != ALL_ROUTE_EDGES_COEXECUTE
```

Each alternative may receive its own bounded precedence view and window status. Composition across alternatives requires an explicit selection/comparison rule; TRACE must not silently merge them.

---

## 5. Adjacent recurrence warning

A similar false-cycle risk exists when recurring **stage types** are collapsed across occurrences:

```text
A1 -> B1 -> A2
```

is an acyclic event-instance path even though the stage-type projection looks like:

```text
A -> B -> A
```

Therefore critical-path vertices/edges must be occurrence-specific enough to distinguish load-bearing event instances when recurrence matters.

```text
STAGE_TYPE_CYCLE != EVENT_INSTANCE_CYCLE
```

This adjacent case should be included in the repair attack; it does not by itself earn a new primitive.

---

## 6. Disposition

```text
v0.7: FAILED / PRESERVED
ACYCLICITY RULE: RETAIN
PROVENANCE RULE: RETAIN
MISSING BINDING: ROUTE/EXECUTION-ALTERNATIVE + OCCURRENCE WHERE MATERIAL
NEW SCHEMA VOCABULARY: NONE EARNED
```

Do not redirect the already-final external v0.6 pass. Next: narrow v0.8 binding repair, immediate route/recurrence attack, then I01–I60 coverage accounting.