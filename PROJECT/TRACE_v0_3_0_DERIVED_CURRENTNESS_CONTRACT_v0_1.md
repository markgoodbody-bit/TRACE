# TRACE v0.3.0 — DERIVED CURRENTNESS CONTRACT v0.1

**Status:** NARROW EXECUTION REPAIR — WORKING CONTRACT — NOT UNIVERSAL TRACE PRIMITIVE  
**Date:** 2026-08-27  
**Trigger:** recurring derived-state currentness failures observed across PR prose, project front doors and cross-project continuity surfaces  
**Placement:** project/checker/orientation layer unless later evidence earns broader structure

## 0. Problem

A derived current-state surface can remain internally coherent after the world it describes has moved.

Observed failure forms include:

```text
1. stale derived value / projection
2. stale dependency topology / route
3. stale act validity while payload remains unchanged
```

The repair target is not historical records, frozen semantic objects, or every prose file. It is a surface whose job is to tell a successor or operator what is **current now**.

```text
RECORD_CORRECT_AT_T0 != RECORD_CURRENT_AT_T1
COHERENT_ORIENTATION != CURRENT_ORIENTATION
```

## 1. Minimum currentness block

Any static derived surface that carries mutable project-state claims should expose:

```text
CURRENTNESS_MODE: SNAPSHOT | STALE | UNKNOWN
DERIVED_AT_COMMIT: <commit SHA or NONE>
DEPENDS_ON:
  - <named immutable object/blob or mutable dependency + observed basis>
LAST_VERIFIED: <UTC date/time or commit-bounded verification marker>
REACQUIRE:
  - <route needed to re-measure each consequential mutable claim>
```

`LIVE` is deliberately excluded for ordinary committed prose. A static file does not stay live merely because it was true when written.

A genuinely transactionally evaluated surface may use `LIVE` only if its value is computed from its dependencies at read/execution time rather than carried forward as prose.

## 2. State rule

For a claim whose dependency can move:

```text
observed dependency == recorded basis -> SNAPSHOT remains historically supported
observed dependency != recorded basis -> STALE — QUERY LIVE SOURCE
current dependency cannot be reacquired -> UNKNOWN
```

A stale value may remain useful historical evidence. It must not silently continue as current authority.

```text
STALE != FALSE_AT_DERIVATION
STALE != DELETE
UNKNOWN != LAST_KNOWN
```

## 3. Route-over-conclusion rule for mutable state

A static successor surface should prefer carrying:

- durable purpose/constraints/authority boundaries;
- frozen object identities and immutable evidence pointers;
- correction debts and explicit holds;
- the **route/test** that can reacquire mutable state.

It should avoid carrying a mutable answer as if inheritance made it current.

```text
CONTINUITY_OF_ROUTE != CONTINUITY_OF_CONCLUSION
CARRY_ROUTE_TO_REMEASURE != ERASE_HISTORY
```

This is a project-currentness repair hypothesis, not a claim that every form of continuity should omit conclusions. Frozen decisions, commitments, debts and historical conclusions remain legitimate carried objects when their status is itself part of what must survive.

## 4. Self-invalidating branch-head trap

A file committed on a moving branch cannot safely present a branch-head SHA as enduring current state: committing the file itself moves the head.

Therefore project front doors should not carry `CURRENT_BRANCH_HEAD = ...` as a current claim. They should say how to reacquire it:

```text
REACQUIRE mutable PR / branch state -> live PR #38 / GitHub branch head
```

If a snapshot head is useful for provenance, label it `DERIVED_AT_COMMIT` or `LAST_VERIFIED_HEAD`, not `CURRENT_HEAD`.

## 5. Narrow application in this pass

Apply this contract now only to the two TRACE project front doors that were observed stale:

```text
PROJECT/PROJECT.md
PROJECT/MAP.md
```

Do not retrofit the whole repository.
Do not rewrite historical intake/falsification records.
Do not build a continuity subsystem merely because currentness matters.

The current 20-case pool itself is an immutable freeze object and does not become a mutable project-status dashboard.

## 6. Falsification / kill condition

This repair earns retention only if it reduces wrong-current orientation without imposing more reconstruction cost than it saves.

A hostile comparison should later ask whether a successor given:

A. a prose current-state summary, versus  
B. durable constraints + immutable pointers + explicit reacquisition routes

reaches the correct live execution boundary more reliably and with acceptable burden.

If route-first orientation repeatedly loses material state that a bounded summary preserves safely, narrow or redesign this contract.

```text
ROUTE_FIRST != PROVEN_BETTER
CURRENTNESS_REPAIR != NEW_TRACE_PRIMITIVE
```
