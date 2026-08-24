# TRACE v0.3.0 — SPINE v0.6 ACYCLICITY REPAIR DELTA v0.1 IMMEDIATE ATTACK

**Target:** `PROJECT/TRACE_v0_3_0_SPINE_V06_ACYCLICITY_REPAIR_DELTA_v0_1.md`  
**Verdict:** `CLEAR_WITH_RESIDUAL_LIMITS` — NOT VALIDATION  
**Scope:** seven targeted cases only

---

## Case 1 — ordinary serial DAG

```text
A -> B -> C
```

All edges current, same process binding, provenance retained.

Result: `ACYCLIC_SUPPORTED`. Critical-path route remains available subject to the separate v0.6 timing/boundary/feasibility conditions.

**RESISTS.**

---

## Case 2 — parallel stages, no precedence edge

```text
A     B
 \   /
   C
```

A and B have no ordering edge. Derived precedence is acyclic.

The delta does not infer that A and B can actually execute concurrently. v0.6 still requires support for execution feasibility when overlap changes the conclusion.

```text
ACYCLIC_SUPPORTED != FEASIBLE_PARALLELISM
```

**RESISTS.**

---

## Case 3 — same-binding policy conflict

```text
c1 -> A before B
c2 -> B before A
same process / scope / time binding
```

Derived view contains a directed cycle.

Result: `CONFLICTING_OR_CYCLIC`; critical-path arithmetic cannot license a strong window result. The delta does not infer which policy is authoritative or whether the world process is deadlocked.

**RESISTS.**

---

## Case 4 — apparent cycle across different regimes

```text
morning policy: A -> B
evening policy: B -> A
```

A downstream claim concerns the morning process only.

The binding step prevents unioning the evening edge into the morning view. No false cycle is created.

If a later claim deliberately compares/joins both regimes, the join itself becomes load-bearing.

**RESISTS.**

---

## Case 5 — stale edge after policy change

Initial:

```text
policy P1 supports A -> B
```

Later P1 is superseded; partial B may begin before A completes.

Because the derived edge retains ordering claim/mechanism provenance and the ordering dependency changed, the view must rebind before reuse. A cached `A -> B` cannot remain current merely because the edge object still exists.

**RESISTS.**

---

## Case 6 — acyclic but shared capacity unresolved

```text
A and B have no precedence relation
both may require one shared analyst
capacity evidence unresolved
```

Graph is acyclic. The capacity guard still blocks a guaranteed-open result based only on structural parallelism.

```text
ACYCLIC_SUPPORTED != FEASIBLE_SCHEDULE_ESTABLISHED
```

**RESISTS.**

---

## Case 7 — cyclic precedence view, separate scheduler timing evidence

Canonical ordering claims conflict, so `E_prec` is cyclic. Separately, a domain scheduler/instrument supplies a supported feasible-completion interval without using the invalid precedence critical path.

The delta blocks only the critical-path route. It permits the separate domain-supported timing route to be evaluated under the ordinary evidence/currentness/boundary rules.

```text
INVALID_CRITICAL_PATH != ALL_TIMING_EVIDENCE_INVALID
```

**RESISTS.**

---

## Residual limits

Not established by this attack:

1. cycle detection in a future executable serializer/checker;
2. completeness of ordering-claim discovery;
3. correctness of domain scheduler bounds;
4. reconstruction by an unfamiliar receiver;
5. how nested/iterative domain processes should project into a bounded acyclic timing view;
6. whether a full candidate preserves the donor acyclicity rule through serialization and validation.

---

## Disposition

```text
MATERIAL FINDING IN IMMEDIATE ATTACK: NONE
DONOR ACYCLICITY REPAIR: SURVIVES TARGETED CASES
NEW NODE/RELATION: NONE EARNED
SPINE v0.6: STILL FAILED/PRESERVED
DELTA: MAY PROCEED TO INTEGRATION ONLY AFTER SCHEMA/VOCABULARY NO-LOSS CHECK
```

`CLEAR_WITH_RESIDUAL_LIMITS != VALIDATED`.