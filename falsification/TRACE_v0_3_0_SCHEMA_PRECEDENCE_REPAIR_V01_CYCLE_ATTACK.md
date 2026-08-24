# TRACE v0.3.0 — PRECEDENCE REPAIR v0.1 CYCLE ATTACK

**Status:** MATERIAL DONOR REGRESSION — HOLD STRONG WINDOW USE OF REPAIRED `E_prec` UNTIL ACYCLICITY/CONFLICT GUARD IS RESTORED  
**Target:** `PROJECT/TRACE_v0_3_0_SCHEMA_DELTA_V01_PRECEDENCE_REPAIR_v0_1.md` + spine v0.6 correction-window use  
**Donor:** TRACE v0.2.7 [8.2], which explicitly represents precedence with a directed acyclic event graph

---

## 1. Counterexample

Two current, provenance-preserved procedural claims under the same process binding say:

```text
c1: stage B cannot begin until stage A completes
c2: stage A cannot begin until stage B completes
```

Both may be perfectly sourced and current, for example because two independently issued policies conflict.

The repaired derived view can faithfully emit:

```text
A -> B   ordering_claim_refs=[c1]
B -> A   ordering_claim_refs=[c2]
```

No provenance has been lost.

But the resulting `E_prec` is cyclic.

A critical-path calculation over this object is not a valid DAG critical-path calculation. The process may instead be deadlocked, the policies may be inconsistent, one claim may need supersession resolution, or the represented process may be infeasible. TRACE does not get to choose among those causes without evidence.

---

## 2. Failure

```text
PROVENANCE_PRESERVED != ORDERING_CONSISTENT
SUPPORTED_EDGES != VALID_DAG
CYCLIC_PRECEDENCE != COMPUTABLE_CRITICAL_PATH
CONFLICTING_ORDERING_CLAIMS != RESOLVED_PROCESS_ORDER
```

The v0.1 provenance repair blocks stale anonymous ordering but does not itself block a cyclic or contradictory derived precedence graph from entering a strong window calculation.

This is a donor regression: v0.2.7 [8.2] explicitly requires a **directed acyclic event graph** for overlapping correction work.

---

## 3. Smallest repair

No canonical vocabulary change.

For any correction-window calculation that uses a critical path over derived precedence:

```text
1. each load-bearing derived precedence edge retains its canonical claim/mechanism provenance;
2. all edges are evaluated under the same declared process/scope/time bindings;
3. the resulting load-bearing precedence graph must be acyclic;
4. material contradictory ordering claims remain visible;
5. if acyclicity/order consistency is unresolved, do not emit a strong open/closed result from critical-path arithmetic.
```

A bounded outcome may be:

```text
PRECEDENCE_STATUS = ACYCLIC_SUPPORTED
PRECEDENCE_STATUS = CONFLICTING_OR_CYCLIC
PRECEDENCE_STATUS = UNKNOWN
```

These are derived statuses, not new schema vocabulary.

For `CONFLICTING_OR_CYCLIC` or unresolved acyclicity:

```text
WINDOW_STATUS = UNKNOWN
```

unless a separate domain-supported feasible-completion bound establishes the required timing conclusion without relying on the invalid precedence critical path.

---

## 4. Important ceiling

A cycle does **not** by itself prove world deadlock, impossibility, deception, or irreversibility.

```text
CYCLIC_REPRESENTED_ORDERING != WORLD_DEADLOCK_PROVEN
POLICY_CONFLICT != PHYSICAL_IMPOSSIBILITY
INVALID_CRITICAL_PATH != NO_CORRECTION_ROUTE
```

The failure is narrower: this derived ordering object cannot license that critical-path timing claim as written.

---

## 5. Disposition

```text
NEW NODE: NO
NEW RELATION: NO
PRECEDENCE PROVENANCE REPAIR: RETAIN
ACYCLICITY / CONFLICT GUARD: RESTORE FROM DONOR
SPINE v0.6: HELD ON THIS SEAM
EXTERNAL v0.6 PASS: DO NOT REDIRECT AGAIN; RETURN REMAINS EVIDENCE ABOUT THE FAILED OBJECT
```

Next: integrate the donor acyclicity guard minimally, attack it, then perform the exact controlled-vocabulary no-loss comparison.