# TRACE v0.3.0 — v0.5 interval-safety repair delta v0.1

**Status:** WORKING REPAIR DELTA — ATTACK OBJECT — NOT v0.6 — NOT SPINE TEXT — NOT CANON — NOT VALIDATED — NOT AUTHORITY — NOT PERMISSION — NOT CLEARANCE  
**Failed target:** `PROJECT/TRACE_v0_3_0_CORRECTION_WINDOW_REPAIR_CANDIDATE_v0_5.md` @ `d862a021b0d1f614c44062e12fb7cb84badbdd71`  
**Falsifier:** `falsification/TRACE_v0_3_0_CORRECTION_WINDOW_V05_SEAM_ATTACK_v0_1.md`  
**Purpose:** restore interval-safe timing/warrant discipline already present in the v0.2.7 donor without reopening the rest of corrected v0.5.

---

## 0. Ceiling

This delta does not repair or validate all of v0.5.

It attacks one demonstrated regression:

```text
point-estimate timing comparison
!=
interval-safe correction-window status
```

No new primitive is proposed.

```text
DONOR_RECOVERY != NEW_ONTOLOGY
REPAIR_DELTA != INTEGRATED_SPINE
```

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

The interval repair changes how uncertain event times and derived closing comparisons are warranted. It does not restore a naive serial sum.

---

## 2. Time claims may be bounded rather than scalar

For any load-bearing event/derived completion time `t_x`, permit a supported bound:

```text
t_x in [lower(t_x), upper(t_x)]
```

or another declared uncertainty representation when interval bounds are not the honest model.

A point estimate may still be carried, but it must not inherit interval-safe semantics.

```text
POINT_ESTIMATE != GUARANTEE
EXPECTED_TIME != LATEST_SUPPORTED_TIME
MEAN_CLOSE != EARLIEST_SUPPORTED_CLOSE
```

If the event graph has interval-valued durations, derive completion bounds using a method valid for the represented precedence/dependency structure.

If cycles, resource contention, retries, correlation, shared uncertainty or state dependence make the bound calculation invalid or materially misleading:

```text
CLOCK_MODEL = INSUFFICIENT
```

or preserve a narrower uncertainty claim.

Do not manufacture tight bounds by treating dependent uncertain durations as independent.

---

## 3. Interval-safe path window

Let:

```text
T_complete in [C_lo, C_hi]
T_path_close in [P_lo, P_hi]
```

Then:

```text
P_lo > C_hi
  -> PATH_WINDOW_GUARANTEED_OPEN under stated bounds

P_hi <= C_lo
  -> PATH_WINDOW_GUARANTEED_CLOSED under stated bounds

otherwise
  -> PATH_WINDOW_STATUS = UNKNOWN / OVERLAPPING_BOUNDS
```

A point comparison such as:

```text
T_complete_est < T_path_close_est
```

may support only a labelled point-estimate statement under its declared estimator. It does not support `GUARANTEED_OPEN`.

---

## 4. Interval-safe target window

Let:

```text
T_complete in [C_lo, C_hi]
T_target_close in [G_lo, G_hi]
```

Then:

```text
G_lo > C_hi
  -> TARGET_WINDOW_GUARANTEED_OPEN under stated bounds

G_hi <= C_lo
  -> TARGET_WINDOW_GUARANTEED_CLOSED under stated bounds

otherwise
  -> TARGET_WINDOW_STATUS = UNKNOWN / OVERLAPPING_BOUNDS
```

Preserve:

```text
POINT_ESTIMATE_FITS != TARGET_WINDOW_GUARANTEED_OPEN
OVERLAPPING_TIME_BOUNDS != WINDOW_FITS
UNKNOWN_BOUND != ZERO_DURATION
```

A downstream `CORRECTION_WINDOW_FITS_FOR(c,g)` must state what timing status it actually relies on: point estimate, interval-guaranteed open, another declared uncertainty model, or unresolved.

Do not hide this behind one Boolean.

---

## 5. Target-close bounds can be path-dependent

A required check, correction step, communication, or other path event can itself change the target-hardening process.

Example:

```text
verification opens a chamber
opening accelerates degradation
therefore the pre-verification target-close bound no longer describes the post-verification path
```

Where represented path events causally alter the closing mechanism, target-close claims/bounds must be conditioned on the relevant path/state or recomputed after the transition.

```text
PATH_EVENT_CHANGES_TARGET_CLOSE
  -> STATIC_PRE_EVENT_CLOSE_BOUND_NOT_AUTOMATICALLY_CURRENT
```

This uses existing transition/coupling/control/evidence structure. It does not create a new clock primitive.

---

## 6. Point use may not be the whole validity horizon

Corrected v0.5 binds verification freshness to downstream use/commitment event `u` where material.

Retain that, but distinguish claims that need to remain valid through a later dependent interval.

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

## 7. No probability laundering

Interval-safe statements are sufficient bound statements, not calibrated probabilities.

```text
GUARANTEED_OPEN_UNDER_BOUNDS != HIGH_PROBABILITY_OPEN
UNKNOWN_INTERVAL_STATUS != 50_PERCENT
CONSERVATIVE_BOUND != CALIBRATED_DISTRIBUTION
```

If a domain supplies a valid stochastic/process model, TRACE may carry the resulting claims with their estimator/provenance. This delta does not invent one.

---

## 8. Worked falsifier replay

Input:

```text
T_complete in [8,14]
T_target_close in [11,13]
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

because:

```text
G_lo = 11
C_hi = 14
11 > 14  = false

G_hi = 13
C_lo = 8
13 <= 8  = false
```

So:

```text
TARGET_WINDOW_STATUS = UNKNOWN / OVERLAPPING_BOUNDS
```

The point estimate may be retained as a point estimate, not promoted into stronger status.

---

## 9. Falsifiers for this delta

Hold or kill the delta if:

1. interval bounds are forced where a different uncertainty representation is required;
2. correlated/dependent durations are combined as though independent and produce false assurance;
3. interval treatment double-counts parallel work already handled by `G_window`;
4. a point estimate is silently promoted to guaranteed-open status;
5. overlapping bounds are silently collapsed to open/closed;
6. dynamic/path-induced changes to target close remain tied to a stale pre-event bound;
7. a proposition current at `u` is treated as valid through execution when its validity horizon is shorter;
8. the repair requires a new primitive rather than ordinary clock/claim/event structure;
9. the interval machinery becomes mandatory bureaucracy for cases with exact deterministic timing;
10. the delta weakens the claim ceiling and lets timing fit imply authorization, adequacy or restoration.

One counterexample is enough to hold this delta.

---

## 10. Disposition

Current proposal:

```text
v0.5 remains failed historical attack object
interval repair remains a narrow delta
no v0.6 yet
no spine integration
no new primitive
```

The smallest recovered rules are:

```text
POINT_ESTIMATE_FITS != GUARANTEED_OPEN
OVERLAPPING_TIME_BOUNDS != WINDOW_FITS
CURRENT_AT_USE != VALID_THROUGH_DEPENDENT_INTERVAL
PATH_EVENT_CHANGES_TARGET_CLOSE != STATIC_CLOSE_BOUND_STILL_VALID
```

If this delta survives hostile contact, fold only the surviving rules into the next standalone candidate rather than carrying the scaffolding automatically.
