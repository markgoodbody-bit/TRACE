# TRACE v0.3.0 — correction-window v0.5 hostile seam attack v0.1

**Status:** FALSIFICATION / V0.5 HOLD — NOT VALIDATION — NOT REPAIR TEXT — NOT SPINE TEXT — NOT CANON  
**Frozen semantic target:** `d862a021b0d1f614c44062e12fb7cb84badbdd71`  
**Target file:** `PROJECT/TRACE_v0_3_0_CORRECTION_WINDOW_REPAIR_CANDIDATE_v0_5.md`  
**Purpose:** attack corrected v0.5 as a frozen object rather than continuing construction by default.

---

## 0. Verdict

```text
FALSIFIED / HOLD v0.5
NO NEW SEMANTIC ROOT FOUND
NARROW TIMING / WARRANT REGRESSION FOUND
```

The decisive break is **interval-safety regression**.

v0.5 correctly repairs the earlier omission of required verification time by making an event/precedence graph primary. But its derived window outputs return to point comparisons:

```text
T_complete < T_path_close
T_complete < T_target_close_declared
```

without restoring the released v0.2.7 interval-safe rule.

That can falsely upgrade an uncertain overlapping window to a represented fit.

```text
POINT_ESTIMATE_FITS != GUARANTEED_OPEN
OVERLAPPING_TIME_BOUNDS != WINDOW_FITS
```

This is a donor regression, not a new primitive/root requirement.

---

## 1. Decisive counterexample — overlapping timing bounds

Suppose the best supported timing claims are:

```text
T_complete in [8,14] minutes
T_path_close in [15,18] minutes
T_target_close in [11,13] minutes
```

A point estimator may emit:

```text
T_complete_est = 10
T_target_close_est = 12
10 < 12
```

and therefore tempt:

```text
TARGET_WINDOW_FITS_AT_DECLARED_CLOSE
```

But the honest bounds overlap:

```text
latest supported completion = 14
earliest supported target close = 11
```

So the represented evidence does not guarantee the correction completes before target hardening.

The released v0.2.7 donor already carried the interval-safe rule:

```text
lower(close) > upper(complete)
  -> GUARANTEED_OPEN under stated bounds

upper(close) <= lower(complete)
  -> GUARANTEED_CLOSED under stated bounds

otherwise
  -> WINDOW_STATUS = UNKNOWN
```

v0.5 did not carry that rule into its qualified outputs.

### Disposition

```text
FINDING — MATERIAL
class: ROOT C timing representation + ROOT A status/warrant
new primitive: NO
```

C must preserve the supported time bounds/uncertainty model. A must refuse a stronger window status than those bounds license.

---

## 2. Ten hostile seams

### S1 — critical-path circularity / verification changes the closing boundary

Worked shape:

```text
required verification consumes a scarce resource or changes physical state
that side effect advances target hardening
```

v0.5 already records verification side effects/capacity and requires load-bearing distinctions to condition timing. A correct instantiation can therefore rebind the target-close claim after the side effect.

However the candidate should not leave this implicit when scalar shorthand is used.

```text
PATH_EVENT_CHANGES_TARGET_CLOSE
  -> PRE_ACTION_CLOSE_BOUND_NOT_AUTOMATICALLY_CURRENT
```

**Result:** BOUNDED NARROWING, not new root.

### S2 — practical commitment before formal application

If a decision is practically committed before a later formal execution event, bind `u` to the actual load-bearing commitment/use boundary rather than the convenient later event.

v0.5 already allows `u = downstream use / decision / binding event`.

**Result:** RESISTED if `u` is instantiated honestly.

### S3 — conflicting checks over different scopes/times/objects

v0.5 carries exact proposition, object/version/state identity, observation time and competing checks, and refuses `LAST_CHECK_WINS`.

Apparent conflict that dissolves after proposition/time/scope separation is not a warrant conflict. Genuine unresolved conflict remains disputed.

**Result:** RESISTED.

### S4 — target/window co-selection

An interested actor can choose a reachable `g` after seeing the window.

v0.5 does not treat target chronology as legitimacy. It carries target selector/basis, explicit `g -> q,l` linkage and non-restored residue, and scopes the result to `FOR(c,g)`.

A weak reachable target therefore cannot honestly inherit restoration semantics merely because it fits.

**Result:** RESISTED under the narrow output ceiling.

### S5 — adaptive path compensation

Removing one claim can activate another route and preserve the endpoint while changing dependence/burden/control.

v0.5 explicitly preserves:

```text
SAME_ENDPOINT != SAME_CAUSAL_DEPENDENCE
COMPENSATED_COUNTERFACTUAL != NON_LOAD_BEARING
```

**Result:** RESISTED.

### S6 — verification-created evidence / verification requires partial correction

A check may be inseparable from an intervention that itself begins the correction or changes the world.

The event graph can represent action-before-evidence. A post-action observation cannot be silently upgraded into a pre-action warrant.

**Result:** RESISTED by event ordering + A/C distinction, provided the event graph is honest.

### S7 — distributed correction with no single corrector

v0.5 explicitly permits multiple `c` values and makes event/precedence structure primary.

Joint completion can therefore be represented without pretending one actor owns the whole transition.

**Result:** RESISTED.

### S8 — late discovery of an affected scope

A prior claim may remain correct for represented scope `l1` while later discovery of `l2` reveals an earlier hardening bound.

v0.5 carries aperture/selection basis and refuses selected scope -> complete scope. The later discovery changes the represented claim set; it does not rewrite the earlier scoped claim into universal truth.

**Result:** RESISTED.

### S9 — syntactic application with zero causal influence

A result may be logged, copied or marked `applied` without conditioning the selector/decision.

v0.5 already states:

```text
RESULT_RETURNED != RESULT_APPLIED
```

and requires actual conditioning where observable; otherwise application remains unestablished.

**Result:** RESISTED.

### S10 — cost of knowing destroys correction capacity

Verification can consume time, a one-shot brake, access, capacity or other future possibility.

v0.5 carries check time on the critical path and verification side effects/capacity consumption. TRACE need not choose the morally preferred check; it must expose the tradeoff.

**Result:** RESISTED, subject to S1's explicit target-close rebinding guard.

---

## 3. Additional interval consequence — current at one instant may be insufficient

A load-bearing proposition can be current at authorization/use `u` but need to remain true through a later execution interval.

Example:

```text
check: bridge is clear at t=0
use/authorization at t=1
crossing occupies t=1..10
safety proposition must remain true through crossing, not merely at t=1
```

v0.5 already permits a `validity interval / freshness condition`, so this does not require a new root. But the repair should make the consequence explicit:

```text
CURRENT_AT_USE != VALID_THROUGH_DEPENDENT_INTERVAL
```

Where a proposition must remain true across an execution interval, bind its validity horizon to that interval rather than only to a point event `u`.

**Result:** NARROW ROOT C/A sharpening.

---

## 4. What survives

The seam attack did **not** break the current compression:

```text
A  distinct epistemic-transition / warrant failure surface
B  derived claim/use-scoped dependency diagnostic
C  distinct verification-process root
X  cross-cutting activation/firing discipline
ADMISSION  failure location, not root
E  carrier/orientation root
```

No new semantic root was found.

The break is narrower:

```text
C must carry timing uncertainty/bounds faithfully
A must not upgrade a point-estimate fit into an interval-safe fit
```

Preserve:

```text
ROOT != PRIMITIVE
POINT_ESTIMATE_FITS != GUARANTEED_OPEN
OVERLAPPING_TIME_BOUNDS != WINDOW_FITS
CURRENT_AT_USE != VALID_THROUGH_DEPENDENT_INTERVAL
PATH_EVENT_CHANGES_TARGET_CLOSE != STATIC_CLOSE_BOUND_STILL_VALID
```

---

## 5. Disposition

```text
v0.5 semantic target d862a021... = FAILED ATTACK OBJECT
DO NOT REWRITE IT AWAY
DO NOT INTEGRATE
DO NOT MERGE BECAUSE OF THIS WORK
```

A narrow repair may reuse the released donor's interval-safe rule rather than inventing new ontology.

The next repair should remain an attack delta until it survives contact.

```text
FAILED_OBJECT != ERASED_OBJECT
DONOR_RECOVERY != NEW_PRIMITIVE
REPAIR_DELTA != INTEGRATED_SPINE
```
