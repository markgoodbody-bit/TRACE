# TRACE v0.3.0 — interval delta v0.1 — CC/139 falsification witness

**Status:** FALSIFICATION WITNESS — FAILED OBJECT PRESERVATION — NOT VALIDATION — NOT CANON  
**Target:** `PROJECT/TRACE_v0_3_0_CORRECTION_WINDOW_V05_INTERVAL_REPAIR_DELTA_v0_1.md` @ `57a9f67eb558918562e651f9a3acff90f3d72c85`  
**External attack:** COM #46, CC/139, read-only inspection  
**Disposition:** **HOLD / FAILED AS WRITTEN**

---

## 1. What survived

The interval donor recovery remains necessary:

```text
POINT_ESTIMATE_FITS != GUARANTEED_OPEN
OVERLAPPING_TIME_BOUNDS != WINDOW_FITS
CURRENT_AT_USE != VALID_THROUGH_DEPENDENT_INTERVAL
PATH_EVENT_CHANGES_TARGET_CLOSE != STATIC_CLOSE_BOUND_STILL_VALID
```

CC/139 did not falsify those guards.

The break is narrower and upstream of the interval arithmetic.

---

## 2. The break

v0.1 §4 asserted:

```text
T_target_close in [G_lo, G_hi]
```

and then applied interval-safe comparisons.

That assumes there is a well-posed target-close quantity to bound.

For a discrete route or mechanism, that may be true. For a continuously degrading target, it need not be.

Worked shape already present in v0.1:

```text
verification opens a chamber
opening accelerates degradation
```

A continuously degrading chamber does not contain a natural physical instant called `target close` unless the reading also states the condition whose crossing counts as the target no longer being achievable.

For example:

```text
restore integrity >= 0.80
```

versus:

```text
restore integrity >= 0.50
```

can produce different target-boundary times from the same physical degradation process.

Therefore:

```text
TARGET_CLOSE_IS_NOT_AN_EVENT_WITHOUT_AN_ADEQUACY_THRESHOLD
TIMING_BOUND_CARRYING_A_HIDDEN_THRESHOLD != PURE_TIMING_CLAIM
```

v0.1 made the interval arithmetic conservative while leaving the quantity being bounded partly constituted by an undeclared target/adequacy condition.

That is an unjustified compression.

---

## 3. Why v0.1's existing escapes do not repair it

### `CLOCK_MODEL = INSUFFICIENT`

This catches invalid or misleading **calculation** of a represented time quantity.

CC/139's case is earlier:

```text
NO_DECLARED_BOUNDARY_CONDITION
-> NO_WELL_POSED_TARGET_BOUNDARY_TIME
```

There may be nothing admissible to calculate yet.

### path-dependent recomputation

v0.1 §5 correctly says a path event can change the target-hardening process and require recomputation.

But recomputing the same undeclared target-close quantity does not expose the hidden criterion that defines the crossing.

### claim ceiling

v0.1 correctly says timing fit does not establish adequacy.

But if the target-close time already embeds an undeclared adequacy threshold, the ceiling is asserted too late. The value/target choice has already entered the timing input.

---

## 4. Root analysis

No new semantic root is earned.

The failure is a composition defect across existing structure:

- the correction target `g` already carries claimed effect, affected scope, selector/source/basis and residue/non-restoration context;
- existing CLAIM / MEASURE / SELECTOR / POLICY / STATE / CLOCK / transition and evidence relations can carry a boundary condition and its source;
- A prevents an unsupported upgrade from an undefined or weakly supported boundary into a stronger window status;
- C carries the process/model/evidence used to estimate when the represented boundary condition is crossed.

So:

```text
HIDDEN_TARGET_CRITERION != NEW_PRIMITIVE
ROOT != PROFILE_FIELD
```

---

## 5. Required narrow repair

Any target-facing boundary time used in a correction-window claim must be conditional on an explicit represented boundary condition tied to the declared correction target.

For a continuous target:

```text
physical/process state
+ declared target boundary condition
+ evidence/model relating state to that condition
-> target-boundary time claim
```

If the boundary condition is absent, unsupported or materially disputed:

```text
TARGET_BOUNDARY_STATUS = UNRESOLVED
```

not a manufactured close instant.

The boundary condition's presence does not validate the condition:

```text
BOUNDARY_CONDITION_DECLARED != BOUNDARY_CONDITION_JUSTIFIED
BOUNDARY_CONDITION_JUSTIFIED != MORAL_ADEQUACY
TIMING_FIT_GIVEN_CONDITION != CONDITION_SHOULD_HAVE_BEEN_CHOSEN
```

A change to the target or boundary condition changes the identity/scope of the window claim rather than silently moving its deadline.

```text
WEAKER_TARGET_CREATES_LATER_BOUNDARY != SAME_CORRECTION_CLAIM_IMPROVED
```

---

## 6. Disposition

```text
interval delta v0.1 @ 57a9f67 -> FAILED AS WRITTEN
interval-safe donor rule       -> SURVIVES
CC/139 threshold attack        -> MATERIAL
new root                       -> NO
new primitive                  -> NO
v0.6                           -> NOT EARNED
spine integration              -> NO
```

The next justified object is a narrow v0.2 repair delta that exposes target-boundary conditions before any target-window timing comparison.
