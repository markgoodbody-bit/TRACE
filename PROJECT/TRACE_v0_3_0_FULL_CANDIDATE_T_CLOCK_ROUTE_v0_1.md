# TRACE v0.3.0 FULL CANDIDATE — T_CLOCK_ROUTE v0.1

**Status:** EXACT-TRANSFORM SPEC — ATTACK BEFORE COMPILER — NOT FULL CANDIDATE — NOT VALIDATION  
**Donor target:** released v0.2.7 `[8] CLOCKS / ROUTES / HARDENING`  
**Overlay source:** v0.11 `[9] CLOCKS / ROUTES / HARDENING`

## Objective

Tighten the donor timing section only where later attacks found material defects, while preserving donor capabilities that the short spine intentionally omitted.

```text
DONOR_TIMING != OBSOLETE_TIMING
V0_11_REPAIR != REPLACE_ALL_DONOR_DETAIL
```

The transform must preserve:

```text
clock typing
donor event-time notation
donor interval-safe bounds
donor clock authorship
donor route object and usability dimensions
donor multidimensional hardening
action load / correction backlog
precommit brake vs postcommit rollback
strategy revisability vs transition reversibility
```

and add/tighten:

```text
target-boundary condition
verification time
precedence provenance/binding
route-alternative separation
event-occurrence identity
acyclicity before critical path
execution-feasibility ceiling
strong OPEN/CLOSED warrant rules
window rebinding
hardening != irreversibility
```

No new schema object/relation is introduced.

---

# Transform C1 — qualify `[8.1] Event times and correction margin`

Retain donor event-time definitions including `t_irreversible`.

Insert after the donor event-time list:

```text
v0.3 boundary qualification:

A strong correction-window claim is indexed by:
  pathway q
  affected scope l
  target effect/state o
  correction capability/route context c
  target-boundary condition g
  use u

The target boundary need not be world/practical irreversibility.
`t_irreversible` is one admissible boundary only when its donor bindings
(loss state, affected scope, measure, mechanism/basis, reference event,
uncertainty) establish the condition actually used by the downstream claim.

TARGET_BOUNDARY_TIME_REQUIRES_REPRESENTED_BOUNDARY_CONDITION
BOUNDARY_CONDITION_DECLARED != BOUNDARY_CONDITION_JUSTIFIED
BOUNDARY_CONDITION_JUSTIFIED != MORAL_ADEQUACY
THRESHOLD_SELECTED_AFTER_RESULT != PREDECLARED_BOUNDARY
UNREACHABLE_BY_DECLARED_ROUTE_SET != WORLD_IRREVERSIBLE
NO_KNOWN_ALTERNATIVE_ROUTE != WORLD_IRREVERSIBLE
```

Retain donor `kappa` as the **practical-irreversibility special case**, not the universal v0.3 window object.

Before donor serial shorthand, insert:

```text
The serial decomposition is a bounded derived special case. Required
verification/check work that is load-bearing is part of the represented
process; it is not zero-duration merely because the shorthand names only
`detect`, `route`, and `correct`.

REQUIRED_CHECK_TIME != ZERO_DURATION
LOAD_BEARING_CHECK != FREE_CHECK
```

Do not add a universal `T_verify` term if verification is already represented inside a stage/process. The requirement is causal/time completeness, not a fixed four-term sum.

---

# Transform C2 — replace the operational centre of `[8.2] Parallel and overlapping correction work`

Retain the donor fact that overlapping correction work is represented as a DAG and retain duration intervals/distributions.

Replace the claim that critical-path completion is automatically `t_correct_done` with a two-layer reading:

```text
G_window(q,l,o,c,g,u) = (V, E_prec)

V contains load-bearing event/stage occurrences.
E_prec is a derived process/timing ordering view over supported canonical
claims. It is not a canonical PRECEDES relation.
```

For every load-bearing derived edge preserve:

```text
supporting canonical claim refs
material ordering mechanism when not recoverable from the claims
process/pathway binding
scope/target binding
route/execution-alternative binding
capability context
time/policy version
use where it can change the conclusion
```

Before critical-path arithmetic:

```text
1. construct one executable pathway hypothesis;
2. do not union mutually exclusive route/execution alternatives;
3. if stage types recur, distinguish event occurrences where collapse can
   create/erase a cycle or change timing;
4. require the resulting precedence view to be acyclic;
5. preserve UNKNOWN when load-bearing membership/binding/ordering is unresolved.
```

Ceilings:

```text
DERIVED_EDGE_PRESENT != ORDERING_TRUE
SAME_PROCESS_SCOPE_TIME != SAME_ROUTE_BINDING
ALTERNATIVE_ROUTE_ORDERINGS != ONE_PROCESS_CYCLE
STAGE_TYPE_CYCLE != EVENT_INSTANCE_CYCLE
PROVENANCE_PRESERVED != ORDERING_CONSISTENT
SUPPORTED_EDGES != VALID_DAG
CYCLIC_PRECEDENCE != COMPUTABLE_CRITICAL_PATH
CYCLIC_REPRESENTED_ORDERING != WORLD_DEADLOCK_PROVEN
```

Let `L_prec(G_window)` be the precedence critical-path bound under represented stage durations.

Do **not** label it feasible completion automatically:

```text
PRECEDENCE_CRITICAL_PATH = optimistic structural completion bound
```

unless the represented execution model also supports the relevant shared-worker, actuator, lock, channel, queue, batching, retry, scheduling or other capacity constraints.

```text
NO_PRECEDENCE_EDGE != CONCURRENCY_AVAILABLE
STRUCTURAL_PARALLELISM != FEASIBLE_PARALLELISM
PRECEDENCE_GRAPH_COMPLETE != EXECUTION_FEASIBILITY_COMPLETE
ACYCLIC_SUPPORTED != FEASIBLE_SCHEDULE_ESTABLISHED
```

Where a supported execution model yields a feasible-completion interval/bound, record it separately.

If cycles invalidate the precedence view, block only the critical-path proof route unless separate domain-supported timing evidence establishes the result.

This preserves donor `CLOCK_MODEL = INSUFFICIENT` for cases requiring a richer process model, while making the insufficiency trigger explicit before a false strong window claim is emitted.

No `RESOURCE`, `QUEUE`, `LOCK`, `CAPACITY`, `SCHEDULER`, or `PROCESS` primitive is added.

---

# Transform C3 — tighten `[8.3] Interval-safe reading`

Retain the donor interval algebra.

Generalise its strong statuses from only `t_irreversible` / `t_correct_done` to the represented target boundary and supported feasible completion:

```text
lower(target_boundary) > upper(feasible_completion)
  -> GUARANTEED_OPEN_FOR_REPRESENTED_BINDINGS
```

For closure:

```text
upper(target_boundary) <= lower(required_feasible_completion)
  -> GUARANTEED_CLOSED_FOR_REPRESENTED_BINDINGS
```

The closure rule is allowed only when the represented correction path/work is actually required; if a live alternative/substitution can avoid that required path, preserve `UNKNOWN` until the alternative is resolved or separately bounded.

Preserve donor interval uncertainty and correlation caveat.

Add:

```text
POINT_ESTIMATE_FITS != GUARANTEED_OPEN
OPTIMISTIC_COMPLETION_FITS != GUARANTEED_OPEN
OVERLAPPING_TIME_BOUNDS != WINDOW_FITS
MULTIPLE_LOAD_BEARING_BOUNDARIES != ONE_UNQUALIFIED_CLOSE
```

The donor irreversibility formulas remain a valid special case when:

```text
target_boundary = represented practical irreversibility condition
feasible_completion = supported correction-completion bound
```

Do not silently relabel an old packet's v0.2.7 `GUARANTEED_OPEN/CLOSED` result as the v0.3 qualified status without checking these bindings.

---

# Transform C4 — preserve `[8.4] Clock authorship` and extend rebinding

Retain all donor authorship fields.

Add that a strong window claim is rebound/recomputed when any load-bearing element changes:

```text
target
boundary condition
capability/route scope
temporal origin/conversion
precedence/process binding
execution constraint
target process
policy/time version
```

```text
PAST_WINDOW_FIT != CURRENT_WINDOW_FIT
CURRENT_AT_USE != VALID_THROUGH_DEPENDENT_INTERVAL
```

---

# Transform C5 — tighten `[8.5] Route`

Retain the complete donor route tuple and usability dimensions.

Add exact donor/spine guard at operative surface:

```text
ROUTE_EXISTS != ROUTE_USABLE
BURDEN_PRESENT != ROUTE_UNUSABLE
```

Usability is scope/target/time/context-relative.

The donor's safe-use/custody detail in `[9.3]` remains part of full-object route usability; do not reduce usability to technical reachability or latency.

---

# Transform C6 — tighten `[8.6] Hardening state`

Retain multidimensional hardening and no cross-dimension sum without measure.

Add:

```text
HARDENING != IRREVERSIBILITY
HARDER_TO_CORRECT != IMPOSSIBLE_TO_CORRECT
HARDENING_BOUNDARY != IRREVERSIBILITY_BOUNDARY_BY_DEFAULT
```

A hardening dimension can contribute to a separately evidenced target/irreversibility boundary. Its label alone does not establish one.

---

# Transform C7 — preserve `[8.7]`, `[8.8]`, `[8.8.1]`

`[8.7] Action load and correction backlog`: `EXACT_CARRY` unless a later worked attack finds a conflict.

`[8.8] Pre-commit brake and post-commit rollback`: retain and add the exact invariant wording if not already present:

```text
REVIEW_AFTER_COMMITMENT != BRAKE
```

while preserving donor `REVIEW_AFTER_COMMITMENT != PRECOMMIT_BRAKE`.

`[8.8.1]`: retain exact donor strategy/transition distinction.

```text
STRATEGY_REVISABLE != TRANSITION_REVERSIBLE
```

No v0.3 timing repair turns rollback availability into restoration proof.

---

# Mechanical transformation contract

The future compiler must implement C1–C7 with exact donor anchors.

Required post-transform assertions:

```text
A1 donor [8.4] authorship field list survives
A2 donor [8.5] route tuple survives
A3 donor [8.6] hardening vector survives
A4 donor [8.7] backlog equation survives
A5 donor [8.8] brake/rollback phase distinction survives
A6 donor [8.8.1] strategy/transition distinction survives
A7 PRECEDES absent from canonical relation vocabulary
A8 no new resource/process primitive appears in node vocabulary
A9 donor interval uncertainty/correlation caveat survives
A10 strong v0.3 OPEN requires feasible-completion upper bound
A11 strong v0.3 CLOSED uses required-feasible lower bound and live-alternative guard
A12 target-boundary condition is explicit for strong status
A13 precedence route/execution binding prevents union of mutually exclusive alternatives
A14 occurrence distinction prevents fake stage-type cycles
```

---

# Known failure ancestry preserved by this transform

This class exists because earlier objects failed on:

```text
verification time treated as free
point estimate accepted despite overlapping intervals
hidden/post-hoc target threshold
capability-relative boundary laundered into world irreversibility
precedence-only parallelism treated as feasible concurrency
provenance-preserving but cyclic/contradictory derived ordering
mutually exclusive route orderings unioned into one false cycle
stage-type recurrence confused with event-occurrence cycle
hardening promoted to irreversibility
```

No one repair should erase the evidence of the previous failure.

---

# Disposition

```text
T_CLOCK_ROUTE v0.1: READY FOR HOSTILE TRANSFORM ATTACK
SCHEMA CHANGE: NO
NEW PRIMITIVE: NO
NEW RELATION: NO
FULL CANDIDATE: NOT YET BUILT
```

Next: attack C1–C7 for contradiction with retained donor machinery, false OPEN/CLOSED, overblocking of valid domain timing, and accidental weakening of I12/I41.