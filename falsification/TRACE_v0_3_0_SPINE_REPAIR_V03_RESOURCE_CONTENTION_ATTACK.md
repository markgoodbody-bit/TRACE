# TRACE v0.3.0 — SPINE REPAIR v0.3 RESOURCE-CONTENTION ATTACK

**Status:** MATERIAL FINDING — HOLD v0.3 AS WRITTEN  
**Target:** `PROJECT/TRACE_v0_3_0_SPINE_REPAIR_CANDIDATE_v0_3.md`  
**Purpose:** test whether the proposed event/precedence correction-window model can still produce a false timing claim after common-clock and interval repairs  

---

## 1. Counterexample

Declared correction process:

- target boundary: 10 minutes after a shared reference event;
- routing stage: duration 6 minutes;
- required verification stage: duration 7 minutes;
- routing and verification have no logical precedence relation;
- both stages require the same single analyst and therefore cannot execute concurrently;
- correction after both stages is negligible for this constructed case.

A precedence-only graph contains two parallel branches:

```text
start -> routing(6) ------\
                         -> complete
start -> verification(7) -/
```

The precedence critical path is 7 minutes.

If `T_complete = critical_path_completion(G_window)` is treated as the completion time, the represented window appears open against a 10-minute boundary.

But no feasible execution can complete both stages in 7 minutes because the single analyst cannot perform both at once. The earliest feasible completion is 13 minutes.

The real represented-use conclusion is therefore closed (or at minimum not established open), while the v0.3 precedence-only calculation can report open.

---

## 2. Failure

```text
NO_PRECEDENCE_EDGE != CAN_EXECUTE_CONCURRENTLY
PARALLEL_BY_PRECEDENCE != PARALLEL_IN_CAPACITY
PRECEDENCE_GRAPH_COMPLETE != EXECUTION_FEASIBILITY_COMPLETE
CRITICAL_PATH_OF_PRECEDENCE_ONLY != FEASIBLE_COMPLETION_TIME
```

A precedence graph answers which stages must come before which other stages. It does not by itself answer whether stages that are unordered can actually execute at the same time.

Shared constraints may include, where material:

```text
one human reviewer / analyst
one machine or actuator
one credential / lock / lease
one communication channel
one scarce route
one budget or rate limit
one mutually exclusive state
other domain-specific capacity
```

The issue is causal/timing structure, not scheduling aesthetics. If a supposedly parallel stage is actually serialized by shared capacity, the completion window changes.

---

## 3. Why current v0.3 text does not already close it

v0.3 binds `G_window(q,l,o,c,g,u)` to a capability/route context `c`, but the defined process object is:

```text
G_window = (V, E_prec)
```

and then states:

```text
T_complete = critical_path_completion(G_window)
```

Nothing in that calculation requires unordered stages to have simultaneously available execution capacity. A reader can therefore faithfully instantiate every stated precedence edge and still compute an infeasible completion time.

The later rebinding rules do not cure this. No process event has changed. The original process was represented incompletely for the timing claim.

```text
CAPABILITY_CONTEXT_NAMED != CAPACITY_CONSTRAINT_BOUND_IN_COMPLETION
```

---

## 4. Classification

This does **not** earn a new primitive, semantic root, scheduler, queueing theory, or universal resource ontology.

Existing TRACE structure can carry the needed evidence:

- `COUPLING` / `DEPENDS_ON` for shared dependencies;
- `CONTROLS` / `CONSTRAINS` for execution limits;
- `ROUTE` / capability claims for reachable execution;
- `CLAIM` / evidence for whether concurrency is actually available.

The repair belongs in the completion-warrant rule.

```text
DONOR/EXISTING-STRUCTURE RECOVERY
NEW PRIMITIVE: NO
NEW ROOT: NO
```

---

## 5. Smallest repair direction

Do not define precedence critical path as the general feasible completion time.

Instead:

1. derive a precedence-only critical path as a structural/optimistic bound;
2. before using an unordered pair as parallel for a load-bearing completion bound, require adequate support that relevant execution constraints permit that concurrency;
3. where shared capacity, mutual exclusion, queueing or other feasibility constraints are load-bearing, use a domain-appropriate feasible schedule/process bound or preserve `UNKNOWN`;
4. require a supported **upper bound on feasible completion** for a guaranteed-open result;
5. permit an adequately supported optimistic lower bound to contribute to a guaranteed-closed result when even the optimistic completion is too late.

```text
CRITICAL_PATH_LOWER_BOUND != FEASIBLE_COMPLETION_UPPER_BOUND
OPEN_REQUIRES_SUPPORTED_FEASIBLE_COMPLETION_UPPER_BOUND
NO_CONCURRENCY_EVIDENCE != CONCURRENCY_AVAILABLE
```

Do not require exhaustive resource modelling in ordinary sequential cases. Fire this distinction only when assumed overlap materially changes the correction-window conclusion.

---

## 6. Other immediate hostile probes

### 6.1 Common units / different origins

v0.3 survives the prior defect: it now requires a shared temporal basis or supported conversion before interval comparison.

### 6.2 Unrelated source mutation

v0.3 survives the prior false-staleness defect: it does not invalidate a derivation merely because an unrelated source component changed.

### 6.3 Measurement reactivity

No new failure found in this pass. v0.3 explicitly preserves both directions:

```text
MEASUREMENT != PASSIVE_OBSERVATION
MEASUREMENT_OCCURRED != MEASUREMENT_CAUSED_CHANGE
```

### 6.4 Missing heartbeat

No new causal overclaim found in this pass. The text permits the current verification interval to close without naming tampering, refusal, process death or another unobserved cause.

### 6.5 No observed invalidator

Potential pressure remains around how a positive `CURRENT` claim is warranted when no invalidation-monitoring aperture exists. Existing spine guards (`RETAINED_RECORD != CURRENT_STATE`, `OLD_EVIDENCE != CURRENT_STATE`) plus v0.3's `INVALIDATOR_NOT_IDENTIFIED != NO_INVALIDATOR_EXISTS` already block the obvious upgrade. No additional repair is earned by this pass unless a concrete receiver actually licenses `CURRENT` from non-observation alone.

---

## 7. Disposition

```text
SPINE_REPAIR_v0_3: FAILED AS GENERAL TIMING REPAIR / PRESERVED
MATERIAL FINDING: SHARED-CAPACITY / EXECUTION-FEASIBILITY GAP
NEXT: NARROW v0.4 REPAIR ONLY
```

Do not integrate v0.3 into the spine as written.
