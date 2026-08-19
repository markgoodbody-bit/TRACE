# TRACE v0.3.0 — CORRECTION WINDOW REPAIR CANDIDATE v0.4

**Status:** WORKING REPAIR CANDIDATE — NOT FORMAL BASELINE — NOT CANON — NOT VALIDATED — NOT AUTHORITY — NOT PERMISSION — NOT CLEARANCE  
**Target:** correction-window section of `PROJECT/TRACE_v0_3_0_SPINE_CANDIDATE_v0_2.md`  
**Source attacks:** COM #46 CC/48, CC/60, FW self-attack after v0.2, CC/63  
**Supersedes for attack:** `PROJECT/TRACE_v0_3_0_CORRECTION_WINDOW_REPAIR_CANDIDATE_v0_3.md`  
**Purpose:** preserve the v0.3 control-envelope and target-linkage repair while making explicit when a declaration actually moves a selector problem rather than merely relocating it.

---

## 1. v0.3 survives, with one missing epistemic boundary

Retain v0.3:

```text
FAULT_SIGNALLED != FAULT_DIAGNOSED
REPAIR_UNREACHABLE_BY_c != WORLD_IRREVERSIBLE
PATH_CLOSURE != TARGET_HARDENING
TARGET_REACHABLE != TARGET_ADEQUATE
TARGET_FACING_DEADLINE != INDEPENDENT_HARDENING_BOUND
PREDECLARED_TARGET != LOAD_BEARING_TARGET
PARTIAL_CORRECTION != RESTORATION
UNKNOWN != ZERO_DURATION
SERIAL_SUM != PARALLEL_CRITICAL_PATH
```

Retain:

- target-close clocks with explicit control envelopes when control is load-bearing;
- declared-close fit distinct from control sensitivity and represented-control robustness;
- explicit causal linkage from correction target `g` to threatened pathway `q` and affected scope `l`;
- named non-restored residue;
- no new primitive for controller, control mode, or target linkage.

CC/63 adds a sharper test:

> Adding a declaration repairs a selector problem only if the new declaration is falsifiable by someone who is not the declarer.

That attack lands against one phrase in v0.3: `challengeable` is too weak if the same selector can supply the declaration, the evidence, and the interpretation that makes the declaration pass.

But the universal form is too strong. Some real evidence is initially available only to one aperture or custodian. TRACE should not turn `NOT INDEPENDENTLY CHECKABLE` into `FALSE`.

So distinguish:

```text
DECLARATION != WORLD FACT
CLAIM != INDEPENDENTLY CHECKABLE CLAIM
CHALLENGEABLE_IN_PRINCIPLE != CHECKABLE_BY_NONDECLARER
SOLE-CUSTODY_EVIDENCE != FALSE EVIDENCE
INDEPENDENCE_NOT_ESTABLISHED != CLAIM_REFUTED
```

---

## 2. Selector repair must expose its check path

When a load-bearing correction-window claim depends on a controller fact, feasible clock movement, or `q,l -> g` causal linkage, record enough to answer:

```text
who declared this?
what evidence supports it?
who controls / holds that evidence?
can an aperture other than the declarer check or falsify it?
if yes, by what route?
if no, is the dependence on the declarer still visible downstream?
```

This can be represented with ordinary TRACE claims, evidence, apertures, custody, routes, and status. No new primitive is required.

A compact representation may include:

```text
DECLARED_BY: <aperture / actor>
EVIDENCE: <reference / UNKNOWN>
EVIDENCE_CUSTODY: <actor / distributed / UNKNOWN>
NONDECLARER_CHECK_ROUTE: <route / NONE ESTABLISHED / UNKNOWN>
STATUS: <supported / reported / disputed / unknown>
```

The exact vocabulary remains profile-level unless the spine earns it.

---

## 3. The terminating rule

[SUFFICIENT_CONDITION CANDIDATE]

A new declaration may count as a repair of selector gaming only to the extent that either:

```text
A. its load-bearing content is falsifiable through a route not controlled solely by the selector/declarer;
```

or:

```text
B. no such route is established, and the downstream result remains explicitly dependent on that selector/declarer rather than being upgraded to an independent or robust claim.
```

Compression:

```text
SELECTOR_PROBLEM_REPAIRED
    only if
EXTERNAL_CHECK_PATH_SUPPORTED
    OR
SELECTOR_DEPENDENCE_REMAINS_EXPLICIT
```

Do not infer:

```text
DECLARER_EXTERNAL != EVIDENCE_INDEPENDENT
THIRD_PARTY_LABEL != THIRD_PARTY_CHECK
MULTIPLE_APERTURES != INDEPENDENT_EVIDENCE
NO_EXTERNAL_CHECK != FALSE
NO_EXTERNAL_CHECK != CLEARANCE
```

The point is not to require an outside witness for every fact. The point is to prevent a selector from laundering its own choice into a world constraint merely by adding fields around it.

---

## 4. Apply the rule to v0.3

### 4.1 Controller claims

```text
controller = external regulator
alterability = fixed
```

These are claims about the represented world, not choices merely because they are written in the packet.

They can support a stronger correction-window result if their basis can be checked outside the party whose window claim benefits from them.

If the only evidence is the correcting institution's own unsupported statement, retain that provenance and do not silently emit represented-control robustness.

### 4.2 Feasible clock movement

```text
current deadline = Friday
controller may extend to Monday but not accelerate
```

`may extend` and `may not accelerate` are load-bearing if they determine whether Thursday completion is robust.

If an independent statute, contract, public rule, mechanical limit, or separately controlled record supports the bounds, the claim may be externally checkable.

If the same institution can both describe and silently alter the bounds, the result remains control-sensitive or selector-dependent.

### 4.3 Target linkage

```text
g = publish a correction
q = public record falsely implies intended wording was preserved
l = affected readers / named subject
```

The claim that `g` changes `q` must expose its mechanism/evidence. A second aperture may falsify it by showing, for example, that the correction is not visible on the surface where the false implication persists.

If only the author can assert that the hidden backend is corrected, the public-record repair claim remains dependent on author-controlled evidence.

---

## 5. Cases where no independent check path exists

The absence of a nondeclarer check route does not make a claim meaningless.

Examples:

```text
- a patient's first-person report of pain before any external measurement exists;
- a sole witness reporting an event before corroborating evidence appears;
- a hardware device exposing an internal fault bit through only one vendor-controlled interface;
- an organisation reporting an undocumented internal discretionary power that outsiders cannot yet inspect.
```

TRACE may preserve these as reported or otherwise supported claims according to the available evidence.

But if such a claim is load-bearing for a correction-window sufficiency result, the dependence must travel:

```text
WINDOW_FIT: SUPPORTED_AT_DECLARED_CLOSE
CONTROL_BOUNDS: DECLARER_DEPENDENT
INDEPENDENT_CHECK: NOT ESTABLISHED
```

This is not a moral verdict. It is an epistemic boundary on what the representation currently establishes.

---

## 6. Worked hostile transfer

### 6.1 Deadline chosen by the same institution

```text
institution says appeal closes Friday
institution says it cannot accelerate the deadline
correction completes Thursday
no public rule or independent record establishes the non-acceleration claim
```

Do not emit unqualified:

```text
TARGET_WINDOW_ROBUST_TO_REPRESENTED_CONTROL
```

Possible output:

```text
TARGET_WINDOW_FITS_AT_DECLARED_CLOSE
CONTROL_BOUNDS: DECLARER_DEPENDENT
NONDECLARER_CHECK_ROUTE: NONE ESTABLISHED
```

The deadline may in fact be fixed. TRACE has not established that through an external check path.

### 6.2 Physical deadline observed through one instrument

```text
sensor operator says vessel failure becomes physically irreversible at 14:00
no second sensor exists
instrument calibration is documented but held by the same operator
```

Do not coerce the deadline to `UNKNOWN` merely because there is one custody path.

Preserve:

```text
physical deadline claim: REPORTED / SUPPORTED TO STATED EVIDENCE
independence: NOT ESTABLISHED
```

A decision may still be forced by the action clock. The representation must not manufacture certainty, but it must also not manufacture ignorance.

---

## 7. Interaction with trigger discipline

CC/47 and CC/63 expose a broader sequence:

```text
DISTINCTION_PRESENT != DISTINCTION_APPLIED
TRIGGER_PRESENT != TRIGGER_FIRED
DECLARATION_PRESENT != DECLARATION_EXTERNALLY_CHECKED
```

This candidate does not claim that prose alone will fire the check.

Where a machine-checkable route exists, profiles/validators should prefer executable checks. Where the check depends on aperture discipline, say so.

```text
FORMAL DISTINCTION != INSTALLED ENFORCEMENT
APERTURE DISCIPLINE != MACHINE CHECK
```

The correction-window spine should expose the dependency. A later implementation may enforce portions of it without turning TRACE itself into a clearance mechanism.

---

## 8. Hostile tests before integration

Try to break v0.4 with:

1. a true controller claim only the controller can presently evidence;
2. an external verifier captured by the declarer;
3. two nominally separate apertures using the same source record;
4. a public rule whose interpretation remains privately controlled;
5. a physical deadline measured by one instrument;
6. a first-person report that is load-bearing but inherently not third-party falsifiable at the time of action;
7. a target linkage supported by a public surface but not by the affected scope's actual access path;
8. an independent checker who can inspect evidence but cannot inspect omitted evidence;
9. a declarer-controlled claim later corroborated independently;
10. a case where requiring the external-check metadata costs more cognition than the selector ambiguity it prevents.

One counterexample is enough to keep this out of the spine.

---

## 9. Current disposition

Provisional repair:

```text
v0.3 control envelope
+ v0.3 target linkage
+ explicit declaration / evidence / custody / nondeclarer-check boundary
```

Retain the smallest useful rule if hostile review survives:

> A correction-window claim must not hide control over its closing bound, the causal relation between its declared target and the threatened transition, or whether the load-bearing claims that support those relations can be checked outside the selector that benefits from them.

Everything else in this candidate is scaffolding until that sentence survives transfer.
