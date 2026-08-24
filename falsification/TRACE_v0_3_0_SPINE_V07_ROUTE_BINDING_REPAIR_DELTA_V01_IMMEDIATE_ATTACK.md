# TRACE v0.3.0 — SPINE v0.7 ROUTE-BINDING REPAIR DELTA v0.1 IMMEDIATE ATTACK

**Target:** `PROJECT/TRACE_v0_3_0_SPINE_V07_ROUTE_BINDING_REPAIR_DELTA_v0_1.md`  
**Verdict:** `CLEAR_WITH_RESIDUAL_LIMITS` — NOT VALIDATION  
**Scope:** nine targeted route/occurrence cases only

---

## 1. Mutually exclusive routes with opposite orderings

```text
R1: A -> B
R2: B -> A
```

Same scope/time/target, but different executable pathway hypotheses.

Repair derives `E_prec_R1` and `E_prec_R2` separately. No false cycle is formed by union.

**RESISTS.**

---

## 2. True same-route cycle

```text
R1:
  A -> B
  B -> A
```

Both ordering claims apply to the same executable pathway binding.

Result remains `CONFLICTING_OR_CYCLIC`; critical-path proof route is blocked without claiming world deadlock.

**RESISTS.**

---

## 3. Opposite policy versions

```text
policy v1 at t1: A -> B
policy v2 at t2: B -> A
```

A current t2 route view does not union the stale v1 edge merely because stage labels match. If a downstream historical comparison joins both regimes, that join must be explicit and does not become one execution DAG by default.

**RESISTS.**

---

## 4. Same route label, changed capability context

`R_restore` persists as a label, but a parallel environment becomes unavailable. The old ordering/parallelism assumptions no longer support the same route execution.

Capability context is load-bearing; route/pathway view must rebind rather than treating label persistence as process persistence.

```text
SAME_ROUTE_LABEL != SAME_EXECUTION_BINDING
```

**RESISTS.**

---

## 5. Recurring stage types, acyclic occurrences

```text
A1 -> B1 -> A2 -> B2
```

Type-level projection revisits A and B. Occurrence-specific event references preserve the acyclic bounded execution.

```text
STAGE_TYPE_CYCLE != EVENT_INSTANCE_CYCLE
```

**RESISTS.**

---

## 6. Distinct occurrence IDs, true event-instance cycle

```text
A1 -> B1
B1 -> C1
C1 -> A1
```

Distinct IDs do not launder the actual directed cycle. Acyclicity test remains on the event-instance graph.

```text
DISTINCT_EVENT_IDS != INDEPENDENT_EVENTS
```

**RESISTS.**

---

## 7. Unknown route membership

Ordering edge `A -> B` is supported, but it is unresolved whether it applies to route R1 or only R2. R1's strong window conclusion would change depending on membership.

Repair keeps membership unresolved; it neither includes nor excludes the edge as settled. Strong R1 critical-path timing remains unavailable from that unresolved view.

**RESISTS.**

---

## 8. One route fits, but selection/authority is absent

R1 has a supported open correction window. No selector has chosen R1 and no current authority for its actuation is established.

Repair permits:

```text
WINDOW(R1) = open under represented bindings
```

but blocks:

```text
R1 WILL BE USED
R1 IS AUTHORISED
CORRECTION WILL OCCUR
```

**RESISTS.**

---

## 9. Silent best-window aggregation

```text
R1: GUARANTEED_OPEN, margin large
R2: UNKNOWN
R3: GUARANTEED_CLOSED
```

Repair preserves route-specific statuses. It does not silently output the maximum margin, label the whole process open, or select R1 because it looks best.

An existential claim such as “at least one represented executable route is open” requires the R1 route existence/executability and its window claim to be supported; it still does not imply selection or permission.

**RESISTS.**

---

## Residual limits

Not established here:

1. reliable route-membership discovery by an unfamiliar receiver;
2. executable event-instance unrolling for large recurrent processes;
3. branch explosion / computational cost;
4. completeness of the represented route set;
5. domain correctness of capability and feasibility claims;
6. whether a future serializer/checker preserves pathway bindings;
7. whether route-specific window comparison is reconstructed consistently across models.

---

## Disposition

```text
MATERIAL FINDING IN NINE-CASE ATTACK: NONE
ROUTE-BINDING DELTA: SURVIVES TARGETED CASES
NEW NODE/RELATION: NONE EARNED
NEXT: DETERMINISTIC v0.8 INTEGRATION + BUILD REPORT + DONOR INVARIANT COVERAGE
```

`CLEAR_WITH_RESIDUAL_LIMITS != VALIDATED`.
