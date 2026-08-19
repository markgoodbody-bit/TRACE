# TRACE v0.3.0 — CORRECTION WINDOW REPAIR CANDIDATE v0.2

**Status:** WORKING REPAIR CANDIDATE — NOT FORMAL BASELINE — NOT CANON — NOT VALIDATED — NOT AUTHORITY — NOT PERMISSION — NOT CLEARANCE  
**Target:** correction-window section of `PROJECT/TRACE_v0_3_0_SPINE_CANDIDATE_v0_2.md`  
**Source attacks:** COM #46, CC/48 and CC/60  
**Supersedes for attack:** `PROJECT/TRACE_v0_3_0_CORRECTION_WINDOW_REPAIR_CANDIDATE_v0_1.md`  
**Purpose:** preserve correction-before-hardening as a world/target-facing constraint without collapsing actor-relative reachability into world irreversibility or letting the evaluated actor choose an easy deadline/target that makes the condition true by construction

---

## 1. What v0.1 repaired — and what it broke

The original spine used:

```text
T_detect(q,l) + T_route(q,l) + T_correct(q,l) < T_irreversible(q,l)
```

Two established breaks required repair:

```text
FAULT_SIGNALLED != FAULT_DIAGNOSED
REPAIR_UNREACHABLE_BY_c != WORLD_IRREVERSIBLE
```

v0.1 therefore split signal from diagnosis and indexed the observation/correction path by apertures `o` and `c`.

That repair was necessary but its right-hand side became too actor-relative:

```text
T_signal(q,l,o)
+ T_diagnose(q,l,o)
+ T_route(q,l,o,c)
+ T_correct(q,l,c)
< T_repair_close(q,l,c)
```

If `T_repair_close(q,l,c)` means "when c's declared correction path stops reaching c's declared target", then almost the whole inequality is defined through the same path it is evaluating.

The condition approaches:

```text
c's path completes before c's path stops being viable
```

That is a useful path-feasibility statement, but it is not yet the stronger claim that gave the correction-window idea its force:

```text
can correction complete before the threatened target/world transition hardens?
```

So v0.2 restores the tension without restoring the old collapse.

```text
PATH_CLOSURE != TARGET_HARDENING
TARGET_HARDENING != WORLD_IRREVERSIBILITY_IN_GENERAL
REPAIR_UNREACHABLE_BY_c != TARGET_CLOSED
```

---

## 2. Keep three objects separate

For a represented failure/harm/correction pathway `q`, affected scope `l`, observation/diagnosis aperture `o`, correcting aperture `c`, and declared correction target `g`, keep three objects distinct.

### A. Correction completion through c

The represented time required for signal, diagnosis, routing and correction to reach target `g` through `c`.

### B. Path closure for c

The time after which this particular correction route through `c` is no longer executable or reachable because of facts such as:

```text
route loss
authority expiry
capability loss
access loss
corrector-specific dependency loss
```

This is corrector-relative.

### C. Target hardening / target closure

The time after which the declared target `g` can no longer prevent, preserve or restore the represented target-state consequence for affected scope `l`, because of an independently represented transition such as:

```text
physical / biological hardening
third-party commitment or execution
loss of a required external dependency
material evidence destruction
allocation of a unique resource
expiry of an externally imposed opportunity
other represented target-state closure
UNKNOWN
```

This is target/world-facing. It is not made world-objective merely by omitting `c`; its source, controller, estimator and evidence still need to be named.

```text
CORRECTOR_RELATIVE != SUBJECTIVE
TARGET_RELATIVE != UNIVERSAL
EXTERNALLY_ANCHORED != NATURAL_LAW
```

A socially created deadline can be real. A deadline controlled or movable by an actor is not therefore invalid; the controller and mutability are part of the structure.

---

## 3. The correction target must be an inspectable object

Let `g` denote the declared correction target. This does not add a new TRACE primitive: `g` is a local binding to an already representable state, transition, claim target or other declared object.

The target must not disappear inside a clock term.

Minimum target record:

```text
target_id / reference
what reaching the target changes in q
which affected scope l it addresses
who selected the target
selection basis / provenance
when it was selected or frozen for this evaluation
what reaching it does NOT restore
known omitted affected scopes or residue
challenge / alternative target if one is live
```

Two anti-gaming guards follow.

```text
TARGET_REACHABLE != TARGET_ADEQUATE
TARGET_DECLARED != TARGET_INDEPENDENT_OF_WINDOW_FIT
```

A target chosen after the evaluator already knows which target can fit inside the window is not, by declaration alone, evidence that the target was independently justified. Retrospective analysis remains possible, but the target needs an independent basis if the analysis wants to claim more than "this chosen target was reachable".

A partial target is allowed. It must remain visibly partial.

```text
PARTIAL_CORRECTION != RESTORATION
RECORD_CORRECTED != LOST_OPPORTUNITY_RESTORED
NOTICE_PUBLISHED != ORIGINAL_PUBLICATION_RECOVERED
```

The notation does not decide what morally adequate repair requires. It prevents a weak reachable target from silently standing in for a stronger target that the downstream claim actually concerns.

---

## 4. Candidate timing form

Let:

- `q` = represented harm/failure/correction pathway;
- `l` = affected scope;
- `o` = observation/diagnosis aperture for this represented path;
- `c` = correcting aperture/system whose route is being tested;
- `g` = declared correction target.

Use one declared reference event/time origin for all scalar durations below. If stages overlap, have different origins, or need multiple apertures, use an event/precedence graph instead of forcing a serial sum.

Define the represented completion time:

[SCHEMATIC_MODEL]

```text
T_complete(q,l,o,c,g)
:= T_signal(q,l,o)
 + T_diagnose(q,l,o)
 + T_route(q,l,o,c)
 + T_correct(q,l,c,g)
```

This additive form is only for declared sequential composition.

Now test two distinct windows rather than one mixed closing clock.

### 4.1 Corrector-path feasibility

[NECESSARY_CONDITION_FOR_THIS_DECLARED_PATH]

```text
T_complete(q,l,o,c,g) < T_path_close(q,l,c,g)
```

This asks whether `c` can finish before its own route/authority/capability path closes.

It can establish only:

```text
PATH_FITS_c
```

It cannot establish correction-before-hardening.

### 4.2 Target hardening window

[SUFFICIENT_CONDITION_FOR_REPRESENTED_TARGET_WINDOW_FIT]

```text
T_complete(q,l,o,c,g) < T_target_close(q,l,g)
```

`T_target_close(q,l,g)` is the represented target-state deadline after which reaching `g` is too late for the specific consequence the target is declared to address.

It must carry at least:

```text
reference event / time origin
source of deadline
controller, if any
mutability, if known
estimator / evidence
relation to target g and affected scope l
status: observed / derived / reported / unknown as applicable
```

When both comparisons are supported:

```text
CORRECTION_WINDOW_FITS_FOR(c,g)
:= PATH_FITS_c
   AND TARGET_WINDOW_FITS_g
```

This preserves the original useful tension:

```text
corrector-relative completion
        versus
separately represented target/world hardening
```

without pretending that loss of reach by `c` is itself world irreversibility.

---

## 5. Do not collapse closure classes

The same event type may belong to different classes in different cases. Classification must follow the represented mechanism, not the noun.

Illustrative partition:

```text
physical / biological hardening
    usually TARGET/WORLD-facing

route loss
    usually CORRECTOR/PATH-facing

authority expiry
    usually CORRECTOR/PATH-facing

capability loss
    usually CORRECTOR/PATH-facing

evidence loss
    TARGET-facing if the evidence loss closes the represented target for any relevant route;
    PATH-facing if only c's particular evidential route is lost

dependency change
    either, depending on which dependency changes

commitment / execution boundary
    either, depending on whether it hardens the affected target-state or only c's route
```

```text
SAME_LABEL != SAME_CLOCK_ROLE
DEADLINE != IRREVERSIBILITY
ACTOR_CREATED_DEADLINE != INVALID_DEADLINE
ACTOR_CONTROLLED_DEADLINE != EXOGENOUS_DEADLINE
```

If the classification is load-bearing and unresolved, keep it `UNKNOWN` or represent both live readings. Do not choose the class that makes the inequality pass.

---

## 6. Target selection and deadline selection are the same general attack surface

CC/60 exposed two apparently separate hostile tests as one structural defect:

```text
the evaluated condition can be made easy when
an interested actor gets to choose the quantity
that determines whether the condition passes
```

This can happen through the target:

```text
target A = restore the lost opportunity
target B = publish a note that a mismatch occurred
```

or through the deadline:

```text
hard target-state boundary
vs
actor-selected administrative date
```

The fix is not to prohibit actor-selected targets or socially constructed deadlines. Many real systems contain both. The fix is to expose selection and control.

Before reporting `CORRECTION_WINDOW_FITS_FOR(c,g)`, require:

```text
TARGET NAMED
TARGET BASIS NAMED
TARGET SELECTOR NAMED
TARGET NON-RESTORATION / RESIDUE NAMED
TARGET-WINDOW DEPENDENCE DISCLOSED

TARGET-CLOSE SOURCE NAMED
TARGET-CLOSE CONTROLLER NAMED IF ANY
TARGET-CLOSE MUTABILITY NAMED IF KNOWN
CLOCK EVIDENCE / ESTIMATOR NAMED
```

If target independence from the evaluated window is material but cannot be established:

```text
TARGET_INDEPENDENCE := UNKNOWN
```

Do not coerce that to `INDEPENDENT` merely because the target was written down.

---

## 7. Signal, diagnosis and multi-aperture routing remain split

The CC/48 repair survives unchanged:

```text
FAULT_SIGNALLED != FAULT_DIAGNOSED
```

A signal can be immediate while diagnosis remains unavailable or unbounded. Missing duration does not become zero.

Likewise:

```text
signal aperture != diagnosis aperture
diagnosis aperture != routing aperture
routing authority != correcting authority
correcting capability != rollback capability
```

When these differences alter the critical path, use a precedence graph.

```text
COMPACT_EQUATION != UNIVERSAL_PROCESS_MODEL
SERIAL_SUM != PARALLEL_CRITICAL_PATH
UNKNOWN != ZERO_DURATION
```

---

## 8. Required firing conditions

Before using a correction-window result in a downstream claim, fire at least the distinctions that are load-bearing for that claim:

```text
signal vs diagnosis
observer/diagnoser aperture
correcting aperture
capability vs authority
route existence vs reachability
route reachability vs independence
corrector-path closure vs target hardening
target hardening vs world irreversibility in general
correction target vs affected scope
target reachability vs target adequacy
partial correction vs restoration
selector vs selected object
deadline source vs deadline controller
fixed deadline vs mutable deadline
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
REPAIR_UNREACHABLE_BY_c != TARGET_CLOSED
TARGET_CLOSED != WORLD_CLOSED
PATH_CLOSURE != TARGET_HARDENING
TARGET_REACHABLE != TARGET_ADEQUATE
PARTIAL_CORRECTION != RESTORATION
DEADLINE != IRREVERSIBILITY
UNKNOWN != ZERO_DURATION
```

A declared distinction that is never fired at the point of use remains decorative.

```text
DISTINCTION_PRESENT != DISTINCTION_APPLIED
```

---

## 9. What each result may say

Do not emit one generic `WINDOW_FITS` label.

### If only the path comparison is supported

```text
PATH_FITS_c
```

Meaning: under the declared model, this correction path can complete before this path loses its represented capability/authority/route.

### If only the target comparison is supported

```text
TARGET_WINDOW_FITS_g
```

Meaning: under the declared model, the represented completion time falls before the represented hardening deadline for target `g`.

This does not establish that `c` actually has a viable route.

### If both are supported

```text
CORRECTION_WINDOW_FITS_FOR(c,g)
```

Meaning: under the declared model, the represented path through `c` both remains executable long enough and reaches declared target `g` before the represented target-state hardening deadline.

None of these establishes:

```text
that c will act
that c is morally entitled to act
that authority is legitimate
that g is morally adequate repair
that g restores the prior world
that another aperture lacks a better route
that the world becomes irreversible when c loses reach
that the estimates are true
```

```text
WINDOW_FITS != CORRECTION_EXECUTED
WINDOW_FITS != AUTHORIZATION
WINDOW_FITS != RESTORATION
WINDOW_FITS != TARGET_LEGITIMACY
WINDOW_CLOSED_FOR_c != WORLD_CLOSED
```

---

## 10. Worked anti-gaming specimen — correction debt

Use the structural shape only; this is not a canon field case.

Suppose a publication differs from the intended object and the intended wording is no longer recoverable.

Two targets are available:

```text
g1 = recreate the exact intended publication
     impossible because intended text is not retained

g2 = publish a correction that states the mismatch,
     preserves the public object as failed carrier,
     and refuses to invent the lost wording
     reachable now
```

`g2` may be a legitimate partial correction, but reaching it does not make `g1` true.

So record:

```text
TARGET g2: correction / mismatch disclosure
NON_RESTORED: exact intended publication remains unrecoverable
RESIDUE: historical public object remains; intended semantic content unknown
```

A window result about `g2` must not be phrased as restoration of `g1`.

This is exactly why target and non-restoration travel together.

---

## 11. Hostile tests before integration

Try to break v0.2 with cases where:

1. signal is immediate but diagnosis never becomes possible;
2. observer can diagnose but has no route to a corrector;
3. one corrector loses authority while another retains it;
4. one actor cannot reverse a record but a maintainer can;
5. physical damage hardens even though the affected actor never witnesses it;
6. correction stages overlap, making the serial sum wrong;
7. a deadline is socially manufactured but binding on the affected target-state;
8. the same actor can move the deadline after seeing whether the path fits;
9. the evaluator chooses a weaker correction target after learning the stronger target cannot fit;
10. a partial correction is valuable but cannot restore the lost opportunity;
11. evidence loss closes one corrector's route but not another's;
12. evidence loss closes the target for every relevant route;
13. target selection predates the clock estimate but was still chosen by the beneficiary;
14. target selection follows the clock estimate but has an independent pre-existing basis;
15. missing clock evidence is silently coerced to zero or infinity;
16. the notation costs more cognition than the collapse it prevents.

The candidate fails if it treats selection chronology alone as legitimacy, if it treats social deadlines as unreal, if it treats actor-relative path loss as world closure, or if a weak target can silently inherit the semantics of a stronger one.

---

## 12. Current disposition

Retain from v0.1:

```text
signal / diagnosis split
aperture-indexed observation and correction path
UNKNOWN != ZERO_DURATION
serial-sum caveat
world irreversibility not derived from c's incapacity
```

Repair from CC/60:

```text
one mixed T_repair_close
    -> separate T_path_close and T_target_close

implicit correction target
    -> explicit target g with selector, basis and non-restoration

WINDOW_FITS
    -> PATH_FITS_c / TARGET_WINDOW_FITS_g / CORRECTION_WINDOW_FITS_FOR(c,g)

tests 7 and 8 as separate edge cases
    -> one general selection/control attack surface
```

Still unresolved:

```text
whether the scalar form earns integration at all
how much target metadata belongs in universal TRACE versus a profile
whether target adequacy needs a narrower structural test
how best to represent mutable deadlines without bloating the core
whether a second-reader challenge should be required or merely available
```

Do not promote this object because it is more elaborate. Prefer the smallest form that survives the hostile cases and preserves the world/path/target distinctions.
