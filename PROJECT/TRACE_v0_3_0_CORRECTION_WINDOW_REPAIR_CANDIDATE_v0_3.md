# TRACE v0.3.0 — CORRECTION WINDOW REPAIR CANDIDATE v0.3

**Status:** WORKING REPAIR CANDIDATE — NOT FORMAL BASELINE — NOT CANON — NOT VALIDATED — NOT AUTHORITY — NOT PERMISSION — NOT CLEARANCE  
**Target:** correction-window section of `PROJECT/TRACE_v0_3_0_SPINE_CANDIDATE_v0_2.md`  
**Source attacks:** COM #46 CC/48, CC/60, FW self-attack after v0.2  
**Supersedes for attack:** `PROJECT/TRACE_v0_3_0_CORRECTION_WINDOW_REPAIR_CANDIDATE_v0_2.md`  
**Purpose:** preserve correction-before-hardening without treating a target-facing deadline as independent merely because it is indexed to the target, and without allowing a predeclared but causally trivial correction target to inherit the semantics of the threatened loss.

---

## 1. Established repairs that survive

Retain:

```text
FAULT_SIGNALLED != FAULT_DIAGNOSED
REPAIR_UNREACHABLE_BY_c != WORLD_IRREVERSIBLE
PATH_CLOSURE != TARGET_HARDENING
TARGET_REACHABLE != TARGET_ADEQUATE
PARTIAL_CORRECTION != RESTORATION
UNKNOWN != ZERO_DURATION
SERIAL_SUM != PARALLEL_CRITICAL_PATH
```

Retain the explicit bindings:

- `q` — represented harm/failure/correction pathway;
- `l` — affected scope;
- `o` — observation/diagnosis aperture;
- `c` — correcting aperture/system;
- `g` — declared correction target.

Retain the split between:

```text
T_path_close(q,l,c,g)
```

and

```text
T_target_close(q,l,g)
```

The former is corrector/path-facing. The latter is target-state-facing.

That split remains necessary.

---

## 2. v0.2 remaining break: target-facing does not mean independent

Counterexample:

```text
q = wrongful administrative action
c = institution able to correct it
g = stop the action before an appeal/freeze deadline
T_target_close(q,l,g) = noon Friday
```

If the institution, a superior authority, or a coupled decision-maker can extend, waive, accelerate, suspend, selectively apply, or replace that deadline, then the target-facing clock is real but partly controlled.

```text
TARGET_FACING_DEADLINE != INDEPENDENT_HARDENING_BOUND
DEADLINE_LOCATION != DEADLINE_CONTROL
DECLARED_DEADLINE != EXOGENOUS_DEADLINE
SOCIAL_DEADLINE != UNREAL_DEADLINE
```

The repair is **not** to demand that every useful deadline be physical, natural, external, or immutable. Many consequential deadlines are institutional and movable.

The repair is to expose control when control can change the downstream claim.

---

## 3. A load-bearing closure clock carries a control envelope

A target-close clock used in a correction-window claim must carry, where material and knowable:

```text
clock / closure reference
reference event / time origin
source / basis
controller set
available control modes
movement direction / bounds if known
conditions / authority required to move it
observability / contestability of movement
estimator / evidence
status
```

`controller set` may contain:

```text
c
affected actor
third party
distributed authority
mechanical / environmental process
NONE ESTABLISHED
UNKNOWN
```

Control modes may include, without becoming a universal vocabulary:

```text
advance
delay
waive
suspend
replace
selectively apply
UNKNOWN
```

These are attributes of the represented mechanism, not new primitives.

```text
CONTROLLER_NAMED != CONTROL_COMPLETE
CONTROL_POSSIBLE != CONTROL_EXERCISED
CONTROL_ABSENT_FROM_RECORD != CONTROL_ABSENT
```

---

## 4. Do not force a controlled deadline into an independence binary

A controlled deadline can still constrain action.

Example:

```text
current deadline = Friday
controller can extend to Monday
controller cannot bring it earlier than Friday
```

If correction completes Thursday, the current Friday bound remains useful and conservative even though the deadline is movable.

Conversely:

```text
current deadline = Friday
controller can move execution to Wednesday
```

A Thursday completion no longer supports an unqualified target-window fit claim.

So distinguish at least:

```text
TARGET_WINDOW_FITS_AT_DECLARED_CLOSE
TARGET_WINDOW_CONTROL_SENSITIVE
TARGET_WINDOW_ROBUST_TO_REPRESENTED_CONTROL
TARGET_WINDOW_CONTROL_UNKNOWN
```

Do not require every reading to emit all four.

### 4.1 Declared-close fit

[SCHEMATIC_MODEL]

```text
T_complete(q,l,o,c,g) < T_target_close_declared(q,l,g)
```

may establish only:

```text
TARGET_WINDOW_FITS_AT_DECLARED_CLOSE
```

provided the underlying clock evidence is supported.

### 4.2 Control sensitivity

If at least one represented feasible clock movement would change whether the inequality holds:

```text
TARGET_WINDOW_CONTROL_SENSITIVE
```

This is not a failure verdict. It says the fit result depends on an actor/control path that remains part of the mechanism.

### 4.3 Robustness

Only if the represented feasible control set is itself bounded well enough to evaluate, and the fit result survives every materially supported clock state within that set, may the reading emit:

```text
TARGET_WINDOW_ROBUST_TO_REPRESENTED_CONTROL
```

```text
ROBUST_TO_REPRESENTED_CONTROL != IMMUTABLE
ROBUST_TO_REPRESENTED_CONTROL != WORLD_OBJECTIVE
BOUNDED_CONTROL_SET != COMPLETE_CONTROL_SET
```

If controller identity, movement direction, or feasible movement is load-bearing and unresolved:

```text
TARGET_WINDOW_CONTROL_UNKNOWN
```

Do not coerce unknown control to independence.

---

## 5. v0.2 second remaining break: a predeclared target can still be trivial

Predeclaring `g` before seeing the available window blocks one form of opportunistic target selection. It does not show that `g` actually bears on `q` for affected scope `l`.

A target can be honestly predeclared and still be causally irrelevant to the threatened transition.

```text
PREDECLARED_TARGET != LOAD_BEARING_TARGET
TARGET_NAMED != TARGET_LINK_ESTABLISHED
```

The correction target therefore needs an explicit, challengeable linkage to the represented pathway.

---

## 6. Target linkage is a claim, not a priority rule

For a target `g` to support a target-window claim about `q,l`, record a linkage claim sufficient to answer:

```text
what threatened state / transition / edge in q is being addressed?
what does reaching g change about it?
which affected scope l does that claimed change reach?
what evidence / mechanism supports the linkage?
what threatened loss or residue remains even if g is reached?
```

This does not require TRACE to decide whether `g` is morally adequate.

A useful representation may be as small as:

```text
TARGET g
THREATENED TRANSITION: <reference>
CLAIMED EFFECT OF g: <specific causal/mechanistic change>
AFFECTED SCOPE: l
BASIS / EVIDENCE: <reference or UNKNOWN>
NON-RESTORED / RESIDUE: <named remainder>
CHALLENGE / ALTERNATIVE LINK: <if live>
```

The linkage uses ordinary TRACE claims/edges/evidence/apertures. No new `TARGET_LINK` primitive is required.

```text
TARGET_LINK_REPORTED != TARGET_LINK_ESTABLISHED
TARGET_LINK_ESTABLISHED != MORAL_ADEQUACY
TARGET_LINK_ESTABLISHED != RESTORATION
```

A second aperture may dispute the linkage without needing to supply a universal priority rule.

---

## 7. Output discipline

Do not let one generic `WINDOW_FITS` hide which claim survived.

Possible derived statements include:

```text
PATH_FITS_c
TARGET_WINDOW_FITS_AT_DECLARED_CLOSE
TARGET_WINDOW_CONTROL_SENSITIVE
TARGET_WINDOW_ROBUST_TO_REPRESENTED_CONTROL
TARGET_WINDOW_CONTROL_UNKNOWN
CORRECTION_WINDOW_FITS_FOR(c,g)
```

`CORRECTION_WINDOW_FITS_FOR(c,g)` requires, at minimum:

```text
path feasibility supported
AND
target-close fit supported
AND
target linkage to q,l supported to the level required by the downstream claim
```

If deadline control is load-bearing, the control qualifier must travel with the result.

Example:

```text
CORRECTION_WINDOW_FITS_FOR(c,g)
CONTROL: SENSITIVE
```

is allowed.

A control-sensitive result is not silently upgraded to a robust result.

---

## 8. Worked transfer cases

### 8.1 Administrative deadline

```text
appeal freezes at Friday noon
correction path completes Thursday
superior authority may extend but not accelerate freeze
```

Possible reading:

```text
TARGET_WINDOW_FITS_AT_DECLARED_CLOSE
known control can only delay closure
TARGET_WINDOW_ROBUST_TO_REPRESENTED_CONTROL
```

subject to the stated control evidence.

If the authority can instead accelerate the freeze to Wednesday:

```text
TARGET_WINDOW_CONTROL_SENSITIVE
```

and Thursday cannot support an unqualified robust fit.

### 8.2 Public correction after lost intended wording

```text
q = publication mismatch / record-integrity failure
g = publish a correction naming the mismatch and refusing invented reconstruction
```

The target may be causally linked to the **record-integrity** pathway while not being linked to restoration of the lost intended publication.

So record:

```text
CLAIMED EFFECT: corrects public record about what is known
NON-RESTORED: intended wording remains unrecoverable
```

A window result about `g` cannot inherit restoration semantics.

### 8.3 Trivial but predeclared target

```text
q = flood threatens occupied homes
g = publish a notice that flooding may occur
```

If the downstream claim is about preventing inundation, the target linkage is unsupported unless the notice is connected through a represented mechanism that actually changes that threatened transition.

The fact that `g` was selected yesterday rather than today is irrelevant to that causal gap.

---

## 9. What this repair deliberately does not do

It does not:

```text
require every deadline to be independent
require every deadline to be physical
assign legitimacy to controllers
choose the morally correct target
rank affected scopes
assume the full controller set is known
assume control will be exercised
convert a causal linkage into permission
```

```text
STRUCTURAL_CONTROL_VISIBILITY != LEGITIMACY
CAUSAL_LINK != AUTHORIZATION
CAUSAL_LINK != MORAL_PRIORITY
CLOCK_CONTROL != CLOCK_INVALIDITY
```

---

## 10. Hostile tests before integration

Try to break v0.3 with:

1. a deadline the corrector can only extend;
2. a deadline the corrector can only accelerate;
3. a deadline two parties can move in opposite directions;
4. a distributed process where no single controller exists;
5. controller identity known but feasible movement unknown;
6. feasible movement bounded incorrectly by the evaluator;
7. a target selected before the clock was known but causally trivial;
8. a target selected after the clock was known but independently required by a pre-existing contract;
9. a target causally repairs one scope while leaving another affected scope untouched;
10. a partial correction that is valuable but cannot restore the lost state;
11. a physical deadline preceded by a socially controlled earlier cutoff;
12. a socially controlled deadline preceded by an immutable physical hardening boundary;
13. a case where control sensitivity adds no useful information and should be deleted;
14. a case where target linkage cannot be expressed using existing TRACE claims/edges without inventing a primitive;
15. a case where the control envelope costs more cognition than the collapse it prevents.

One counterexample is enough to keep this out of the spine.

---

## 11. Current disposition

Provisional repair:

```text
TARGET_FACING_DEADLINE
    -> target-close clock + explicit control envelope when load-bearing

INDEPENDENT / NOT INDEPENDENT
    -> declared-close fit + control sensitivity / represented-control robustness / unknown

PREDECLARED TARGET g
    -> explicit challengeable causal linkage from g to threatened q,l + named residue
```

Retain the smallest useful rule if hostile review survives:

> A correction-window claim must not hide control over its closing bound or the causal relation between its declared target and the threatened transition.

Everything else in this candidate is scaffolding until that sentence survives transfer.
