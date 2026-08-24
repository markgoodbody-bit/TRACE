# TRACE v0.3.0 — interval + target-boundary delta v0.2 — immediate self-attack

**Status:** SELF-ATTACK WITNESS — NARROW MATERIAL FINDINGS — NOT VALIDATION — NOT CANON  
**Initial target:** `PROJECT/TRACE_v0_3_0_CORRECTION_WINDOW_V05_INTERVAL_REPAIR_DELTA_v0_2.md` @ `10a4aa4b937c92e2d4c4ccc1bc2820612dca7251`  
**Disposition:** **HOLD INITIAL v0.2 / NARROW REPAIR REQUIRED**

---

## 1. Why attack immediately

CC/139 showed that exposing a target boundary condition is necessary because a continuously degrading target has no adequacy-free natural close instant.

The first v0.2 draft exposed the condition, but three ways of laundering a convenient deadline remained possible.

No new root or primitive is indicated by any of them.

---

## 2. Finding A — post-hoc boundary selection

Scene:

```text
degradation history already observed
candidate thresholds: 0.80, 0.65, 0.50
after seeing which threshold produces a fitting window,
selector declares that threshold as the target boundary
```

The initial v0.2 carried selector/source/basis but did not explicitly require selection/freeze time where timing makes that history load-bearing.

A threshold can therefore be fully declared yet still be post-hoc.

Preserve:

```text
BOUNDARY_CONDITION_DECLARED != BOUNDARY_CONDITION_PREDECLARED
THRESHOLD_SELECTED_AFTER_RESULT != PREDECLARED_BOUNDARY
SELECTION_TIME_UNKNOWN != SELECTION_BEFORE_OUTCOME
```

Repair: carry selection/freeze time where material, and preserve later revisions as new claim state rather than rewriting the earlier boundary.

---

## 3. Finding B — capability-relative target boundary without route scope

Scene:

```text
target g: restore integrity >= 0.80
corrector c1 can still achieve g until minute 10
corrector c2 can still achieve g until minute 30
physical degradation process is identical
```

A boundary condition stated only as:

```text
g becomes unattainable
```

is still under-specified.

Unattainable by what corrector, represented route set, capability horizon or physical mechanism?

If one analyst sees only c1 and another sees c1+c2, they can produce different `T_target_boundary` values from the same target and state history.

Preserve:

```text
UNREACHABLE_BY_c != WORLD_IRREVERSIBLE
UNREACHABLE_BY_DECLARED_ROUTE_SET != WORLD_IRREVERSIBLE
TARGET_BOUNDARY_REQUIRES_CAPABILITY_SCOPE_WHEN_CAPABILITY_RELATIVE
```

Repair: where the boundary proposition depends on achievability/restorability, bind it to the represented corrector/route set or to an independently supported physical hardening proposition. Unknown alternative routes remain visible as aperture limits.

---

## 4. Finding C — multiple load-bearing boundaries compressed to one deadline

Scene:

```text
target g has two required effects:
  g1: maintain hospital access
  g2: prevent water contamination

different affected scopes and different boundary times
```

A single unqualified `T_target_boundary` can hide which effect/scope supplied the deadline.

Depending on target logic, the aggregate may require both effects, either effect, or a declared priority/alternative structure. TRACE must not invent that composition.

Preserve:

```text
MULTIPLE_LOAD_BEARING_BOUNDARIES != ONE_UNQUALIFIED_CLOSE
EARLIEST_BOUNDARY != UNIVERSAL_AGGREGATE_RULE
LATEST_BOUNDARY != UNIVERSAL_AGGREGATE_RULE
```

Repair: bind each boundary to its target effect/scope and preserve the declared composition rule if a higher-level window status aggregates them. If composition is unresolved, aggregate target-window status remains unresolved.

---

## 5. Root / ontology check

All three findings are representable with existing structure:

- CLAIM timestamps / records for selection history;
- SELECTOR / POLICY / MEASURE / evidence refs for threshold basis;
- ROUTE / CAN_CORRECT / DEPENDS_ON / CONTROLS for capability-relative boundary claims;
- target effects and affected scopes for multiple boundary conditions;
- aperture/unknown structure for unobserved alternative routes.

Therefore:

```text
THRESHOLD_HISTORY != NEW_ROOT
CAPABILITY_SCOPE != NEW_ROOT
MULTIPLE_BOUNDARIES != NEW_ROOT
PROFILE_REPAIR != NEW_PRIMITIVE
```

---

## 6. Disposition

```text
initial v0.2 @ 10a4aa4 -> HOLD
finding A -> MATERIAL NARROW
finding B -> MATERIAL NARROW
finding C -> MATERIAL NARROW
new root -> NO
new primitive -> NO
v0.6 -> NOT EARNED
spine integration -> NO
```

Correct v0.2 in place only if the repair remains purely representational: selection/freeze history, capability scope, and explicit multi-boundary composition. Preserve this witness and the initial commit rather than rewriting the failure away.
