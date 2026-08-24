# TRACE v0.3.0 — SCHEMA DELTA v0.1 PRECEDENCE REPAIR v0.1

**Status:** WORKING REPAIR — ZERO CANONICAL VOCABULARY CHANGE STILL PROPOSED  
**Parent:** `PROJECT/TRACE_v0_3_0_SCHEMA_DELTA_CANDIDATE_v0_1.md`  
**Failure witness:** `falsification/TRACE_v0_3_0_SCHEMA_DELTA_V01_PRECEDENCE_PROVENANCE_ATTACK.md`

---

## 1. Repair

`E_prec` remains a **derived timing/process view**, not a canonical TRACE relation.

A load-bearing derived precedence edge must preserve reference to the canonical evidence that establishes its ordering:

```text
DERIVED_PRECEDENCE_EDGE := {
  from_stage_ref,
  to_stage_ref,
  ordering_claim_refs,
  mechanism_refs,
  scope_time_refs
}
```

Minimum requirement:

```text
ordering_claim_refs != []
```

`mechanism_refs` and `scope_time_refs` may be empty only when the canonical ordering claims themselves fully carry that information.

The derived edge inherits the evidence/currentness ceiling of its referenced claims and mechanisms.

```text
DERIVED_EDGE_PRESENT != ORDERING_TRUE
DERIVED_EDGE_CACHED != ORDERING_CURRENT
CLAIM_REF_PRESENT != CLAIM_CURRENT
```

If a load-bearing source policy, route, state, dependency, control/constraint or timing basis changes, the process view must be recomputed/rebound before a strong window status is reused.

---

## 2. Canonical mechanisms remain heterogeneous

The same derived ordering may arise from different retained structures:

```text
B DEPENDS_ON A
POLICY P CONSTRAINS B until A
ROUTE R makes B unreachable before A
STATE/TRANSITION structure permits B only after A
RELATIONAL claim with evidence states procedural order
```

Do not overwrite those mechanisms with the derived view.

```text
DERIVED_PRECEDENCE != CAUSES
DERIVED_PRECEDENCE != DEPENDS_ON
DERIVED_PRECEDENCE != CONSTRAINS
```

The view states only the ordering needed by the bounded process/timing calculation under its declared bindings.

---

## 3. No schema promotion

Do not add:

```text
PRECEDES relation
PROCESS node
STAGE node
SCHEDULE node
```

unless a later worked case demonstrates material information cannot be preserved/audited through the canonical claim/mechanism references above.

A convenient serialization name is not enough to earn universal vocabulary.

---

## 4. Firing / currentness interaction

The v0.6 representation-independent firing rule applies to the propositions that support ordering.

If the timing result depends on derived edge `A -> B`, the supporting ordering proposition is load-bearing even though the edge itself belongs only to a derived process view.

Dependency-relative freshness applies to the edge's source claims/mechanisms. A policy or route mutation unrelated to the ordering does not automatically stale the edge; a load-bearing ordering change does.

```text
SOURCE_MUTATED != ORDERING_CHANGED
ORDERING_DEPENDENCY_CHANGED -> DERIVED_PROCESS_REBOUND
```

---

## 5. Full-candidate contract

A full v0.3 packet or derived-view carrier that emits a correction-window process graph must make it possible to trace every load-bearing derived precedence edge back to its canonical claim evidence.

A viewer may hide those references in ordinary prose/UI, but the canonical/derived data contract must retain them.

```text
HUMAN_VIEW_COMPACT != PROVENANCE_DROPPED
```

---

## 6. Disposition

```text
CANONICAL VOCABULARY DELTA: ZERO
DERIVED VIEW CONTRACT: REPAIRED / ATTACK NEXT
NEW PRIMITIVE: NO
NEW RELATION: NO
```
