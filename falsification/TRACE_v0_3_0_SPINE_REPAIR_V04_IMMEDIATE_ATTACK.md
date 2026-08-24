# TRACE v0.3.0 — SPINE REPAIR v0.4 IMMEDIATE ATTACK

**Status:** CLEAR ON TARGETED COUNTEREXAMPLES / RESIDUAL LIMITS REMAIN  
**Target:** `PROJECT/TRACE_v0_3_0_SPINE_REPAIR_CANDIDATE_v0_4.md`  
**Purpose:** attack the exact seams named by v0.4 before any spine integration

---

## 1. Shared single analyst — prior falsifier

Case:

```text
routing = 6 min
verification = 7 min
no precedence edge
one analyst must do both
target boundary = 10 min
```

v0.4 result:

- precedence-only optimistic bound = 7 min;
- feasible upper completion bound is not established from precedence alone;
- therefore `GUARANTEED_OPEN` is unavailable;
- if domain evidence establishes serialization, feasible completion becomes >=13 min and closure can be supported under the remaining bindings.

**RESISTS prior falsifier.**

```text
PRECEDENCE_CRITICAL_PATH_FITS != GUARANTEED_OPEN
```

---

## 2. Unknown shared capacity

Case:

Two load-bearing stages are unordered. It is unknown whether they use the same worker/lock/channel.

v0.4 trigger fires because assumed overlap changes the conclusion and simultaneous executability is not established.

Result: no supported feasible upper bound -> `WINDOW_STATUS_UNKNOWN`.

**RESISTS.**

```text
NO_KNOWN_RESOURCE_CONFLICT != CONCURRENCY_ESTABLISHED
```

---

## 3. Faster alternative route — false-closed attack

Case:

The represented main path has a structural lower bound of 12 min against a 10 min boundary, but a second route may bypass a required stage and complete in 8 min.

v0.4 explicitly forbids using the lower-bound closed rule while stage substitution, omission, conditional branches or another route can make the supposedly required path non-required.

Result: main-path lateness does not become global closure until route/process bindings settle the alternative.

**RESISTS.**

```text
ONE_PATH_TOO_LATE != ALL_REPRESENTED_CORRECTION_TOO_LATE
```

No new guard is required in v0.4; this wording restates the existing route-binding consequence.

---

## 4. Correction action moves the boundary

Case A: an early brake slows degradation, moving the hardening boundary later.  
Case B: an attempted intervention destabilises the target, moving the boundary earlier.

A completion interval estimated under the intervention cannot be joined to a boundary interval estimated under the no-intervention trajectory as though they described one process.

v0.4 requires `I_feasible_complete` and `I_boundary` to be on the same supported temporal basis **and under the same declared process bindings**, while retained v0.3 rebinding includes:

```text
PATH_EVENT_CHANGES_TARGET_PROCESS -> WINDOW_CLAIM_REBOUND
```

Result: the baseline boundary must be rebound or the window remains unresolved for the intervention process.

**RESISTS if the stated binding rule is applied.**

Preserve as an attack target in later cold transfer:

```text
SAME_CLOCK != SAME_COUNTERFACTUAL_PROCESS
```

This is not yet a new required spine guard because the current process-binding language carries it.

---

## 5. Ordinary serial case — bureaucracy attack

Case:

Detection -> routing -> correction are genuinely sequential and no assumed overlap affects the result.

The v0.4 concurrency trigger does not fire because condition (1) is false.

No resource enumeration is required.

**RESISTS.**

```text
NO_MATERIAL_OVERLAP != RESOURCE_AUDIT_REQUIRED
```

---

## 6. Event time versus stage duration — type attack

Case:

One supplied value is an event timestamp measured from scene start; another is a stage duration. A naive scheduler could add them.

The existing spine already requires clocks to be represented by what they actually time, and v0.3/v0.4 requires temporal-basis/interval semantics before joining values. This attack therefore recovers existing clock typing rather than earning another repair.

```text
EVENT_TIME != STAGE_DURATION
SAME_UNIT != SAME_TEMPORAL_SEMANTICS
```

**NO NEW REPAIR EARNED.**

---

## 7. Residual limits

This pass does not establish that a domain-specific feasible schedule model is correct. It only prevents a precedence-only optimistic path from being promoted into a guaranteed-open correction window.

Still outside TRACE core:

- queueing estimators;
- stochastic scheduling;
- detailed resource allocation;
- domain-specific failure distributions;
- moral adequacy of the target boundary;
- exhaustive discovery of alternative routes.

A supplied feasible-completion interval can still be wrong in the world. TRACE can expose its evidence and assumptions; it cannot certify the estimator by syntax.

```text
FEASIBLE_BOUND_SUPPLIED != FEASIBLE_BOUND_TRUE
MODEL_CONSTRAINTS_REPRESENTED != WORLD_CONSTRAINTS_COMPLETE
```

These are already covered by the spine's model/world and schema/world ceilings; no new root or primitive follows.

---

## 8. Disposition

```text
SPINE_REPAIR_v0_4: RESISTS TARGETED IMMEDIATE ATTACK
VERDICT: CLEAR_WITH_RESIDUAL_LIMITS
NEW PRIMITIVE: NO
NEW ROOT: NO
NEXT: BUILD COHERENT SPINE CANDIDATE, THEN COLD/TRANSFER ATTACK
```

Do not call this validation. Do not merge/release/canon from this result.
