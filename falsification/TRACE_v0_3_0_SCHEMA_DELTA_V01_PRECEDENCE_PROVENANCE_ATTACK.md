# TRACE v0.3.0 — SCHEMA DELTA v0.1 PRECEDENCE-PROVENANCE ATTACK

**Status:** MATERIAL FINDING — HOLD DERIVED `E_prec` CONTRACT AS WRITTEN  
**Target:** `PROJECT/TRACE_v0_3_0_SCHEMA_DELTA_CANDIDATE_v0_1.md`  
**Schema conclusion under test:** no new canonical relation type is required for correction-process precedence.

---

## 1. Counterexample

Canonical scene:

```text
stage A = evidence collection
stage B = review decision
policy P says B may not begin until A is complete
```

Canonical representation can preserve:

```text
POLICY P
P CONSTRAINS B
RELATIONAL claim c1:
  proposition = "B cannot begin before A completes under policy P"
  source/provenance = P
  time/scope = current procedure
```

A derived correction-process view normalizes this to:

```text
A -> B
```

in `E_prec`.

Now policy P changes so that partial review may begin before A completes.

If the derived `E_prec` edge stores only `(A,B)` and does not retain the canonical claim/mechanism references that established the ordering, the process view can continue carrying `A -> B` after its source ordering has changed.

A critical-path/window calculation can therefore use a stale ordering premise even though the canonical graph contains the policy change.

---

## 2. Failure

```text
DERIVED_ORDERING != PROVENANCE_FREE_ORDERING
NORMALIZED_EDGE != SOURCE_MECHANISM_ERASED
ORDERING_EDGE_CURRENT != ORDERING_SOURCE_CURRENT
DERIVED_VIEW_RECOMPUTABLE != DERIVED_VIEW_CURRENT
```

The failure is not that TRACE lacks a `PRECEDES` relation. The failure is that the derived normalization contract was underspecified.

---

## 3. Smallest repair

Keep canonical vocabulary unchanged.

Every load-bearing derived precedence edge should retain enough reference back to canonical evidence to audit and rebind the ordering:

```text
DERIVED_PRECEDENCE_EDGE := {
  from_stage_ref,
  to_stage_ref,
  ordering_claim_refs,
  mechanism_ref(s) where material,
  temporal/scope binding where not already recoverable from claims
}
```

`ordering_claim_refs` must identify canonical claims supporting the ordering. `mechanism_ref(s)` may identify the policy, route, state, dependency, control or constraint that gives the ordering its meaning when that distinction matters.

The derived edge does not upgrade those claims.

```text
DERIVED_EDGE_PRESENT != ORDERING_TRUE
CLAIM_REF_PRESENT != CLAIM_CURRENT
```

The generic currentness/firing rules remain responsible for checking load-bearing source changes before use.

---

## 4. Why not add `PRECEDES`

A canonical `PRECEDES` relation would still require evidence, provenance, scope and currentness. Adding the relation name does not solve the stale-derived-view failure.

Different mechanisms can generate the same derived ordering:

```text
physical dependency
policy constraint
route reachability
state transition structure
explicit procedural rule
```

Keeping those mechanisms canonical and deriving the common timing view preserves more causal information than replacing them with one universal relation.

```text
COMMON_DERIVED_VIEW != COMMON_CANONICAL_MECHANISM
```

No new relation is earned by this case.

---

## 5. Disposition

```text
SCHEMA VOCABULARY CHANGE: STILL NONE EARNED
SCHEMA DELTA v0.1 E_prec CONTRACT: FAILED / REPAIR REQUIRED
NEXT: PROVENANCE-PRESERVING DERIVED PRECEDENCE PROFILE + REPRESENTABILITY ATTACK
```

Do not treat zero-vocabulary-change as proven until the repaired derived view survives worked cases.
