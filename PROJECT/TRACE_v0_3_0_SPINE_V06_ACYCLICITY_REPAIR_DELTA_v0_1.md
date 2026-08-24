# TRACE v0.3.0 — SPINE v0.6 ACYCLICITY REPAIR DELTA v0.1

**Status:** WORKING REPAIR DELTA — NOT INTEGRATED SPINE — NOT FORMAL BASELINE — NOT CANON — NOT VALIDATED  
**Parent:** `PROJECT/TRACE_v0_3_0_SPINE_CANDIDATE_v0_6.md`  
**Failure witness:** `falsification/TRACE_v0_3_0_SCHEMA_PRECEDENCE_REPAIR_V01_CYCLE_ATTACK.md`  
**Donor recovery:** TRACE v0.2.7 [8.2] directed acyclic event graph requirement

---

## 1. Repair surface

Retain the v0.6 correction-window object and the provenance-preserving derived `E_prec` contract, but qualify any critical-path use as follows.

A load-bearing derived precedence view used for correction timing must be built from ordering claims under a **common declared process/scope/time binding** and must be acyclic before critical-path arithmetic can license a strong window status.

```text
DERIVED_PRECEDENCE_EDGE := {
  from_stage_ref,
  to_stage_ref,
  ordering_claim_refs,
  mechanism_refs,
  scope_time_refs
}
```

```text
PROVENANCE_PRESERVED != ORDERING_CONSISTENT
SUPPORTED_EDGES != VALID_DAG
CYCLIC_PRECEDENCE != COMPUTABLE_CRITICAL_PATH
```

No `PRECEDES` relation, `PROCESS` node or scheduler ontology is added.

---

## 2. Binding before cycle test

Do not union every ordering edge merely because the stage labels match.

Before acyclicity testing, bind the derived view to the same declared:

```text
process / pathway
scope
target effect or state
route/capability context where material
time / interval / policy version
use
```

An edge valid only in morning procedure and an opposite edge valid only in evening procedure do not form one process cycle unless a downstream claim actually joins those regimes.

```text
SAME_STAGE_LABEL != SAME_PROCESS_BINDING
EDGE_A_AT_t1 + EDGE_B_AT_t2 != CYCLE_AT_ONE_BINDING
```

If a strong downstream claim intentionally joins regimes, the join itself becomes load-bearing and must be warranted.

---

## 3. Derived precedence status

For the bounded process view, use derived status only:

```text
ACYCLIC_SUPPORTED
CONFLICTING_OR_CYCLIC
UNKNOWN
```

`ACYCLIC_SUPPORTED` requires:

```text
all load-bearing ordering edges have supporting claim refs
relevant edge bindings are mutually comparable for this process view
no represented load-bearing ordering conflict produces a directed cycle
```

`CONFLICTING_OR_CYCLIC` means the represented ordering support under the same binding contains a material contradiction/cycle.

`UNKNOWN` covers missing ordering evidence, unresolved binding, or incomplete cycle/conflict resolution.

These are derived process statuses, not canonical TRACE schema terms.

---

## 4. Window consequence

Critical-path arithmetic may support a strong correction-window result only when the precedence view used by that arithmetic is `ACYCLIC_SUPPORTED` and the separate v0.6 feasibility/time/boundary requirements are also satisfied.

For `CONFLICTING_OR_CYCLIC` or `UNKNOWN`:

```text
PRECEDENCE_CRITICAL_PATH_CANNOT_LICENSE_STRONG_WINDOW_STATUS
```

Return `WINDOW_STATUS_UNKNOWN` **from that route of proof** unless a separate domain-supported feasible-completion bound establishes the timing conclusion without relying on the invalid/unresolved precedence view.

This matters because a cycle in the representation does not prove the world process cannot complete.

```text
CYCLIC_REPRESENTED_ORDERING != WORLD_DEADLOCK_PROVEN
INVALID_CRITICAL_PATH != NO_CORRECTION_ROUTE
```

---

## 5. Interaction with feasibility

Acyclicity is necessary for the derived critical-path route but not sufficient for feasible timing.

The v0.6 capacity guard remains:

```text
NO_PRECEDENCE_EDGE != CONCURRENCY_AVAILABLE
STRUCTURAL_PARALLELISM != FEASIBLE_PARALLELISM
PRECEDENCE_GRAPH_COMPLETE != EXECUTION_FEASIBILITY_COMPLETE
```

Therefore:

```text
ACYCLIC_SUPPORTED != FEASIBLE_SCHEDULE_ESTABLISHED
```

Guaranteed-open still requires a supported feasible-completion upper bound. A DAG alone cannot supply one when shared capacity or other execution constraints remain unresolved.

---

## 6. Rebinding

Recompute/rebind the derived precedence view when a load-bearing ordering claim, mechanism, process/scope/time binding, route/capability context or target process changes.

```text
PAST_ACYCLIC != CURRENT_ACYCLIC
POLICY_CHANGED != ORDERING_CHANGED
ORDERING_DEPENDENCY_CHANGED -> DERIVED_PROCESS_REBOUND
```

Unrelated mutations do not automatically stale the view.

---

## 7. Immediate attack set

The repair survives only if it handles:

1. ordinary serial DAG;
2. parallel independent stages with no precedence edge;
3. same-binding `A->B` and `B->A` policy conflict;
4. apparent opposite edges from different non-joined time regimes;
5. cycle caused by a stale edge whose provenance changed;
6. acyclic graph with unresolved shared capacity;
7. cyclic derived graph where an independent domain scheduler provides a valid feasible-completion bound without using the critical path.

One false strong open/closed claim is enough to hold the delta.

---

## 8. Disposition

```text
DONOR ACYCLICITY GUARD: RESTORED AS DERIVED PROCESS RULE
CANONICAL VOCABULARY CHANGE: NONE
SPINE v0.6: REMAINS FAILED / PRESERVED
THIS DELTA: ATTACK OBJECT
```

Do not redirect the already-bounded external v0.6 pass again. Its return remains evidence about v0.6.