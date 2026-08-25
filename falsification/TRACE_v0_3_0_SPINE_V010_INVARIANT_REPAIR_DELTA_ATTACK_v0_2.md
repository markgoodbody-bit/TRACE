# TRACE v0.3.0 SPINE v0.10 — INVARIANT REPAIR DELTA ATTACK v0.2

**Status:** TARGETED SELF-ATTACK — NOT VALIDATION  
**Target:** `PROJECT/TRACE_v0_3_0_SPINE_V010_INVARIANT_REPAIR_DELTA_v0_2.md`

## Criterion

The repair must block silent substitution without forbidding legitimate inference, policy selection, or coincidence.

```text
NON_ENTAILMENT != IMPOSSIBILITY
ATTRIBUTION_DISCIPLINE != POLICY_BAN
```

---

## T1 — authoritative report can establish under explicit rule

A statute or domain protocol says a signed report from authority X establishes procedural status Y unless challenged. The signed report is present and valid.

Required result:

```text
report = REPORTED
establishment_rule = DECLARED / SATISFIED
procedural_status_Y = ESTABLISHED_RELATIVE_TO_RULE
```

The repair allows this because it blocks `REPORTED` status alone from doing the work; the explicit establishment rule carries the upgrade.

**RESISTS.**

## T2 — report alone silently upgraded

A controller-owned field reports a state with no establishment rule or independent evidence. Downstream code calls it established.

`REPORTED != ESTABLISHED` blocks the shortcut.

**RESISTS.**

---

## T3 — record plus corroboration establishes event

A signed log, independent sensor and witness all support that event E occurred.

The repair permits an event claim strongly supported by those sources while preserving that the record object is not the event itself.

**RESISTS.**

## T4 — intact record but event did not occur

A pre-created job row survives although execution failed before actuation.

The repair blocks `record observed -> event observed`.

**RESISTS.**

---

## T5 — external policy chooses action under uncertainty

Declared policy P says: if claim X remains UNKNOWN after deadline D, select protective action A. P, selector and authority are represented.

Required attribution:

```text
uncertainty = policy input
P/selector = selection source
A = selected
```

The repair permits this. It does not prohibit action under uncertainty.

**RESISTS.**

## T6 — external policy chooses delay under uncertainty

Declared policy Q says: if evidence remains UNKNOWN and holding transition H is available, wait 30 minutes.

The repair permits Q to select delay while blocking `UNKNOWN` itself from becoming the selector.

**RESISTS.**

## T7 — hidden default chooses action

No selector/default policy is represented; an implementation maps UNKNOWN directly to ACT.

`IMPLICIT_DEFAULT != NO_SELECTION_RULE` exposes the hidden selection rule and blocks attribution to uncertainty alone.

**RESISTS.**

## T8 — hidden default chooses delay

Same case with UNKNOWN -> WAIT.

**RESISTS.**

---

## T9 — hardening and irreversibility coincide

A chemical transition hardens continuously and at threshold t becomes physically irreversible. Independent domain evidence establishes both.

The repair allows both claims; it only blocks hardening label/status from establishing irreversibility automatically.

**RESISTS.**

## T10 — hardening without irreversibility

A legal review path becomes slower and more expensive after a deadline but remains usable and can restore the target state.

The repair preserves hardening without promoting it to irreversibility.

**RESISTS.**

---

## Disposition

```text
TESTS: 10
MATERIAL FAILURES: 0
OVERBLOCK FAILURES: 0
RESULT: CLEAR_WITH_RESIDUAL_LIMITS
```

Residuals:

- domain contracts define when reports establish status;
- event inference quality remains domain/evidence dependent;
- TRACE does not choose which external uncertainty policy is legitimate;
- hardening dimensions remain typed and need not share one threshold;
- these guards still require the representation-independent firing rule at use.

```text
CLEAR_WITH_RESIDUAL_LIMITS != VALIDATED
```

Next: deterministic v0.11 integration + survival-kernel propagation.