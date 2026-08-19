# TRACE v0.3.0 — CORRECTION WINDOW REPAIR CANDIDATE v0.1

**Status:** WORKING REPAIR CANDIDATE — NOT FORMAL BASELINE — NOT CANON — NOT VALIDATED — NOT AUTHORITY — NOT PERMISSION — NOT CLEARANCE  
**Target:** correction-window section of `PROJECT/TRACE_v0_3_0_SPINE_CANDIDATE_v0_2.md`  
**Source attack:** COM #46, CC/48  
**Purpose:** repair aperture collapse in detection/correction timing without converting actor-relative reachability into a claim of world irreversibility

---

## 1. Established break

Current spine uses:

```text
T_detect(q,l) + T_route(q,l) + T_correct(q,l) < T_irreversible(q,l)
```

Two different collapses survive this form.

First, the same pathway and affected scope may be uncorrectable by one aperture while still correctable by another aperture with different capability, authority, route or access.

```text
IRREVERSIBLE != IRREVERSIBLE_BY_THIS_APERTURE
```

Second, an instrument may signal a mismatch immediately while diagnosis remains unavailable or unbounded.

```text
FAULT_SIGNALLED != FAULT_DIAGNOSED
```

A single `T_detect` can therefore hide a one-second signal and an indefinitely unresolved diagnosis inside the same number.

---

## 2. Do not repair one collapse by creating another

A direct repair would index `T_irreversible` by correcting aperture `c`.

That is useful if `irreversible` is being used to mean "no longer repairable by c". But it risks laundering an actor-relative loss of reach into a world-state claim.

Example shape:

```text
ordinary participant cannot edit record
maintainer can still correct database
```

The record is not necessarily world-irreversible. It is unreachable by one correction route.

So preserve two objects:

```text
WORLD / TARGET-STATE HARDENING OR IRREVERSIBILITY

vs

CORRECTION REACHABILITY FOR A DECLARED CORRECTOR
```

```text
REPAIR_UNREACHABLE_BY_c != WORLD_IRREVERSIBLE
ROUTE_CLOSED_TO_c != NO_CORRECTION_EXISTS
CAPABILITY_ABSENT_FOR_c != CAPABILITY_ABSENT
```

No new primitive family is required. These are clock/route/aperture bindings over existing structure.

---

## 3. Candidate timing form

Let:

- `q` = represented harm/failure/correction pathway;
- `l` = affected scope;
- `o` = aperture/system through which signal and diagnosis are obtained for this represented correction path;
- `c` = correcting aperture/system whose capability/authority/route is being tested.

[SCHEMATIC_MODEL]

```text
T_signal(q,l,o)
+ T_diagnose(q,l,o)
+ T_route(q,l,o,c)
+ T_correct(q,l,c)
< T_repair_close(q,l,c)
```

`T_repair_close(q,l,c)` is the represented deadline after which the declared correction path through `c` no longer reaches the declared correction target in time.

It may be determined by the earliest material closure among already represented clocks, for example:

```text
physical / biological hardening
evidence loss
route loss
authority expiry
capability loss
commitment / execution boundary
dependency change
other declared target-specific closure
UNKNOWN
```

This is a **correction-path deadline**, not automatically a world-irreversibility claim.

If the domain independently supports a world-state irreversibility clock, record that separately, e.g.:

```text
T_world_irreversible(q,l)
```

and state its estimator/evidence/reference event rather than deriving it from the corrector's limitations.

---

## 4. Multiple apertures may be needed before correction

The compact equation binds one observation/diagnosis aperture `o` and one correcting aperture `c`. That is already more truthful than the unindexed form, but it remains schematic.

A real process may contain:

```text
signal aperture != diagnosis aperture
diagnosis aperture != routing aperture
routing authority != correcting authority
correcting capability != rollback capability
```

When those differences are load-bearing, use an event/precedence graph rather than adding indices until the scalar equation becomes unreadable.

```text
COMPACT_EQUATION != UNIVERSAL_PROCESS_MODEL
SERIAL_SUM != PARALLEL_CRITICAL_PATH
```

The equation remains valid only under declared sequential composition assumptions.

---

## 5. Required firing conditions

Before using the correction-window inequality for a downstream claim, fire the following distinctions when collapse could change the result:

```text
signal vs diagnosis
observer/diagnoser aperture
correcting aperture
capability vs authority
route existence vs reachability
route reachability vs independence
corrector-relative closure vs world irreversibility
sequential vs parallel stages
estimate vs observed clock
UNKNOWN vs absent / zero
```

Minimum guards:

```text
FAULT_SIGNALLED != FAULT_DIAGNOSED
CAPABILITY != AUTHORITY
ROUTE_EXISTS != ROUTE_REACHABLE
REACHABLE != INDEPENDENT
REPAIR_UNREACHABLE_BY_c != WORLD_IRREVERSIBLE
DEADLINE != IRREVERSIBILITY
UNKNOWN != ZERO_DURATION
```

If a system cannot estimate one required clock, the result is `UNKNOWN` for the represented inequality. Missing duration must not become zero.

---

## 6. What the inequality can establish

[SUFFICIENT_CONDITION]

Under declared estimates, reference events, apertures, correction target, authority/capability assumptions and sequential composition, satisfaction of the inequality is sufficient only to say:

```text
the represented correction path through c fits inside its represented closing window
```

It does **not** establish:

```text
that c will act
that c is morally entitled to act
that authority is legitimate
that correction restores the prior world
that another aperture lacks a better route
that the world becomes irreversible when c loses reach
that the estimates are true
```

```text
WINDOW_FITS != CORRECTION_EXECUTED
WINDOW_FITS != AUTHORIZATION
WINDOW_FITS != RESTORATION
WINDOW_CLOSED_FOR_c != WORLD_CLOSED
```

---

## 7. Hostile tests before integration

Try to break this candidate with cases where:

1. signal is immediate but diagnosis never becomes possible;
2. observer can diagnose but has no route to a corrector;
3. one corrector loses authority while another retains it;
4. one actor cannot reverse a record but a maintainer can;
5. physical damage hardens even though the affected actor never witnesses it;
6. correction stages overlap, making the serial sum wrong;
7. a declared deadline is manufactured by an actor rather than physically imposed;
8. `T_repair_close` is gamed by choosing a convenient correction target;
9. missing clock evidence is silently coerced to zero or infinity;
10. the notation itself costs more cognition than the collapse it prevents.

Reject or simplify the repair if a smaller representation survives these cases.
