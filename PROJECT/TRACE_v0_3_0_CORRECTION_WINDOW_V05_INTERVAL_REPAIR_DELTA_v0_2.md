# TRACE v0.3.0 — v0.5 interval + target-boundary repair delta v0.2

**Status:** WORKING REPAIR DELTA — ATTACK OBJECT — NOT v0.6 — NOT SPINE TEXT — NOT CANON — NOT VALIDATED — NOT AUTHORITY — NOT PERMISSION — NOT CLEARANCE  
**Failed predecessor:** `PROJECT/TRACE_v0_3_0_CORRECTION_WINDOW_V05_INTERVAL_REPAIR_DELTA_v0_1.md` @ `57a9f67eb558918562e651f9a3acff90f3d72c85`  
**Falsification witness:** `falsification/TRACE_v0_3_0_CORRECTION_WINDOW_INTERVAL_DELTA_V01_CC139_ATTACK.md`  
**Purpose:** retain interval-safe donor recovery while refusing to manufacture a target-close time from an undeclared target/adequacy threshold.

---

## 0. Ceiling

This delta does not repair or validate all of corrected v0.5.

It addresses two demonstrated timing/warrant failures:

```text
POINT_ESTIMATE_FITS != GUARANTEED_OPEN
TARGET_BOUNDARY_TIME != ADEQUACY_FREE_PHYSICAL_FACT
```

No new primitive is proposed.

```text
DONOR_RECOVERY != NEW_ONTOLOGY
BOUNDARY_CONDITION != PRIORITY_RULE
REPAIR_DELTA != INTEGRATED_SPINE
```

TRACE may expose which condition defines a target-facing timing boundary. It does not choose the morally correct target, threshold or trade-off.

---

## 1. Event graph remains primary

Retain corrected v0.5's event/precedence graph:

```text
G_window(q,l,o,c,g,u)
```

including load-bearing signal, diagnosis, verification, result-return, application/decision-conditioning, routing, correction and target-reaching events.

Retain:

```text
REQUIRED_CHECK_TIME != ZERO_DURATION
LOAD_BEARING_CHECK != FREE_CHECK
CHECK_IN_PARALLEL != SERIAL_DELAY
SERIAL_SUM != PARALLEL_CRITICAL_PATH
```

The repair changes how uncertain timing claims and target-facing boundaries are admitted and warranted. It does not restore a naive serial sum.

---

## 2. Time claims may be bounded rather than scalar

For any load-bearing event or derived completion time `t_x`, permit a supported bound:

```text
t_x in [lower(t_x), upper(t_x)]
```

or another declared uncertainty representation when interval bounds are not the honest model.

A point estimate may still be carried, but it must not inherit interval-safe semantics.

```text
POINT_ESTIMATE != GUARANTEE
EXPECTED_TIME != LATEST_SUPPORTED_TIME
MEAN_BOUNDARY != EARLIEST_SUPPORTED_BOUNDARY
```

If the event graph has interval-valued durations, derive completion bounds using a method valid for the represented precedence/dependency structure.

If cycles, resource contention, retries, correlation, shared uncertainty or state dependence make the calculation invalid or materially misleading:

```text
CLOCK_MODEL = INSUFFICIENT
```

or preserve a narrower uncertainty claim.

Do not manufacture tight bounds by treating dependent uncertain durations as independent.

---

## 3. Path closure remains distinct

A path can close through a represented mechanism or event without implying that every possible correction target is irrecoverable.

Let:

```text
T_complete in [C_lo, C_hi]
T_path_close in [P_lo, P_hi]
```

when `T_path_close` is itself a supported path-closure quantity.

Then:

```text
P_lo > C_hi
  -> PATH_WINDOW_GUARANTEED_OPEN under stated bounds

P_hi <= C_lo
  -> PATH_WINDOW_GUARANTEED_CLOSED under stated bounds

otherwise
  -> PATH_WINDOW_STATUS = UNKNOWN / OVERLAPPING_BOUNDS
```

Retain:

```text
REPAIR_UNREACHABLE_BY_c != WORLD_IRREVERSIBLE
PATH_CLOSURE != TARGET_HARDENING
POINT_ESTIMATE_FITS != GUARANTEED_OPEN
```

---

## 4. Target-facing timing requires a represented boundary condition

Do not assume that every correction target has a natural point event called `target close`.

For a discrete target, a represented event may directly establish the boundary.

For a continuous or graded target, the target-facing boundary is a derived claim: the time at which a represented condition tied to correction target `g` is crossed.

The reading must therefore carry, where load-bearing:

- the declared correction target `g`;
- the target effect/state that matters to the window claim;
- the boundary condition whose crossing changes the relevant target status;
- the affected scope to which that condition applies;
- selector/source/basis for that condition;
- measure/instrument/model where the condition is quantitative or inferred;
- threshold/comparison rule where one exists;
- timing/source/uncertainty of the boundary-crossing claim;
- disputes or materially plausible alternative boundary conditions where known;
- residue/non-restoration relevant to what crossing the boundary means.

These are references/profiles over existing TRACE objects and relations, not a new primitive.

```text
PROFILE_FIELD != PRIMITIVE
BOUNDARY_CONDITION_DECLARED != BOUNDARY_CONDITION_JUSTIFIED
BOUNDARY_CONDITION_JUSTIFIED != MORAL_ADEQUACY
```

If no supported boundary condition exists:

```text
TARGET_BOUNDARY_STATUS = UNRESOLVED
```

Do not invent `T_target_close` merely because the window profile expects a number.

---

## 5. Conditional target-window timing

Where a supported target boundary condition exists, derive a target-boundary timing claim conditional on that represented condition and target.

Conceptually:

```text
process/state history
+ target g
+ represented boundary condition for g
+ evidence/model linking state to the condition
-> T_target_boundary(g, declared condition)
```

The notation is descriptive shorthand, not a new formal primitive.

If bounded:

```text
T_complete        in [C_lo, C_hi]
T_target_boundary in [G_lo, G_hi]
```

then:

```text
G_lo > C_hi
  -> TARGET_WINDOW_GUARANTEED_OPEN
     under stated timing bounds AND stated boundary condition

G_hi <= C_lo
  -> TARGET_WINDOW_GUARANTEED_CLOSED
     under stated timing bounds AND stated boundary condition

otherwise
  -> TARGET_WINDOW_STATUS = UNKNOWN / OVERLAPPING_BOUNDS
```

Every strong target-window status must carry the condition it is conditional on.

```text
TIMING_FIT_GIVEN_CONDITION != CONDITION_SHOULD_HAVE_BEEN_CHOSEN
TARGET_WINDOW_GUARANTEED_OPEN != TARGET_MORALLY_ADEQUATE
TARGET_WINDOW_GUARANTEED_OPEN != RESTORATION
```

A downstream `CORRECTION_WINDOW_FITS_FOR(c,g)` must state whether it relies on a point estimate, interval-guaranteed timing, another declared uncertainty model, unresolved target boundary, or unresolved target/boundary dispute.

Do not hide this behind one Boolean.

---

## 6. Target gaming must change the claim, not silently move the clock

Weakening the correction target or changing the boundary condition can move the apparent target boundary later without improving the world's actual correction capacity.

Example:

```text
same degrading system

claim A target: restore >= 0.80
claim B target: restore >= 0.50

boundary for B occurs later
```

That does not establish that the same correction claim gained more time.

```text
WEAKER_TARGET_CREATES_LATER_BOUNDARY
!=
SAME_CORRECTION_CLAIM_IMPROVED
```

Changing `g`, affected scope, claimed effect or the load-bearing boundary condition changes the identity/scope of the derived window claim and must remain visible.

```text
TARGET_CHANGED -> WINDOW_CLAIM_REBOUND
BOUNDARY_CONDITION_CHANGED -> WINDOW_CLAIM_REBOUND
```

This is visibility/attribution discipline, not a rule choosing the stronger target.

---

## 7. Target-boundary dynamics can be path-dependent

A required check, correction step, communication or other path event can change the target process itself.

Example:

```text
verification opens a chamber
opening accelerates degradation
```

If the declared boundary condition is:

```text
restore integrity >= 0.80
```

then opening the chamber can change the time at which that condition becomes unattainable.

Where represented path events causally alter the boundary process, recompute or rebind the target-boundary timing claim **using the same declared boundary condition unless the condition itself is explicitly changed**.

```text
PATH_EVENT_CHANGES_TARGET_PROCESS
  -> STATIC_PRE_EVENT_BOUNDARY_TIME_NOT_AUTOMATICALLY_CURRENT

PATH_EVENT_CHANGES_PROCESS
!=
LICENSE_TO_CHANGE_BOUNDARY_CONDITION
```

If the path event changes both the process and the target/condition, record both changes separately.

---

## 8. Point use may not be the whole validity horizon

Retain:

```text
CURRENT_AT_USE != VALID_THROUGH_DEPENDENT_INTERVAL
```

If correction execution during interval `[u, t_g]` depends on proposition `p` remaining true, preserve the supported validity horizon/monitoring condition for `p` across that interval or mark the dependence unresolved.

Example:

```text
bridge clear at authorization
crossing lasts ten minutes
safety condition must hold during crossing
```

A check current at authorization alone does not establish the interval proposition.

---

## 9. Continuous targets need not be forced into binary closure

Some domains may not support a defensible crisp boundary condition.

If the represented target changes continuously and no justified threshold or transition condition is available, TRACE may preserve the graded state/process and decline binary target-window status.

```text
CONTINUOUS_DEGRADATION != NATURAL_CLOSE_EVENT
NO_DEFENSIBLE_THRESHOLD != THRESHOLD_AT_DEFAULT_VALUE
UNRESOLVED_TARGET_BOUNDARY != ZERO_TIME_LEFT
```

A domain-specific profile may supply a valid threshold, utility surface, operational limit, regulatory boundary, physical phase transition, minimum viable state or other condition. Preserve its provenance and ceiling.

TRACE does not invent one merely to complete the form.

---

## 10. No probability or adequacy laundering

Interval-safe statements are sufficient bound statements, not calibrated probabilities.

```text
GUARANTEED_OPEN_UNDER_BOUNDS != HIGH_PROBABILITY_OPEN
UNKNOWN_INTERVAL_STATUS != 50_PERCENT
CONSERVATIVE_BOUND != CALIBRATED_DISTRIBUTION
```

Target-boundary conditions also remain claims with sources and limits.

```text
SUPPORTED_THRESHOLD != UNIVERSAL_THRESHOLD
POLICY_THRESHOLD != PHYSICAL_LAW
MEASURED_THRESHOLD_CROSSING != MORAL_PERMISSION
```

If a domain supplies a valid stochastic/process model, TRACE may carry the resulting claims with estimator/provenance. This delta does not invent one.

---

## 11. Worked replay A — uncertain timing

Input:

```text
T_complete in [8,14]
T_target_boundary in [11,13]
boundary condition: declared and supported for this target
point estimates: 10 and 12
```

Naive point result:

```text
10 < 12
```

This delta refuses:

```text
TARGET_WINDOW_GUARANTEED_OPEN
```

because the timing bounds overlap.

The point estimate may be retained as a point estimate, not promoted into stronger status.

---

## 12. Worked replay B — continuous degradation

Scene:

```text
verification opens chamber at t0
integrity then degrades continuously
correction can restore some integrity, with achievable restoration declining over time
```

Bad representation:

```text
T_target_close = 30 min
```

with no statement of what becomes impossible at 30 minutes.

This delta returns:

```text
TARGET_BOUNDARY_STATUS = UNRESOLVED
```

until a represented condition is supplied.

If the supplied, sourced target condition is:

```text
g: restore integrity >= 0.80 for protected scope l
```

and a supported model yields:

```text
condition becomes unattainable in [24,31] min
```

then `[24,31]` is a target-boundary timing claim **conditional on that target/condition**.

Changing the target to `>=0.50` creates a different window claim. It does not retroactively prove that the `>=0.80` correction window was larger.

---

## 13. Falsifiers for this delta

Hold or kill v0.2 if:

1. it still permits a target-boundary time with no represented boundary condition or transition;
2. it hides the source/selector/basis of a load-bearing boundary condition;
3. changing the target/threshold silently changes the clock while preserving the same window-claim identity;
4. interval bounds are forced where a different uncertainty representation is required;
5. correlated/dependent durations are combined as though independent and produce false assurance;
6. interval treatment double-counts parallel work already handled by `G_window`;
7. a point estimate is silently promoted to guaranteed-open status;
8. overlapping bounds are silently collapsed to open/closed;
9. a path-induced process change remains tied to a stale pre-event boundary time;
10. a path-induced process change silently changes the boundary condition rather than only recomputing the crossing under the declared condition;
11. a proposition current at `u` is treated as valid through execution when its validity horizon is shorter;
12. a declared boundary condition is treated as morally adequate merely because it is explicit;
13. a continuous target with no defensible threshold is forced into binary open/closed status;
14. the repair requires a new primitive rather than existing target/claim/measure/selector/policy/state/clock/event structure;
15. the machinery becomes mandatory bureaucracy for exact deterministic event closures.

One counterexample is enough to hold this delta.

---

## 14. Disposition

Current proposal:

```text
v0.5                              -> failed historical object
interval delta v0.1 @ 57a9f67     -> failed historical object
CC/139 target-boundary attack      -> integrated as falsifier, not authority
interval + target-boundary v0.2    -> current attack object
new root                           -> NO
new primitive                      -> NO
v0.6                               -> NOT YET
spine integration                  -> NO
merge/release/canon                -> NO
```

Smallest surviving candidate rules:

```text
POINT_ESTIMATE_FITS != GUARANTEED_OPEN
OVERLAPPING_TIME_BOUNDS != WINDOW_FITS
TARGET_BOUNDARY_TIME_REQUIRES_REPRESENTED_BOUNDARY_CONDITION
BOUNDARY_CONDITION_DECLARED != MORAL_ADEQUACY_ESTABLISHED
WEAKER_TARGET_CREATES_LATER_BOUNDARY != SAME_CORRECTION_CLAIM_IMPROVED
CURRENT_AT_USE != VALID_THROUGH_DEPENDENT_INTERVAL
PATH_EVENT_CHANGES_TARGET_PROCESS != STATIC_BOUNDARY_TIME_STILL_VALID
```

Attack this object before any standalone v0.6 candidate is written.
