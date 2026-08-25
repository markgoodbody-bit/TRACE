# TRACE v0.3.0 SPINE v0.10 — INVARIANT EQUIVALENCE ATTACK v0.2

**Status:** HOSTILE DONOR-LOSS PASS — WORKING EVIDENCE — NOT VALIDATION  
**Target:** `PROJECT/TRACE_v0_3_0_SPINE_CANDIDATE_v0_10.md`  
**Donor:** released TRACE v0.2.7 I01–I60

## Purpose

Attack a second wave of v0.10 semantic-equivalence claims after exact donor restoration raised lexical coverage to 20/60.

Primary targets:

```text
I03 REPORTED != ESTABLISHED
I13 CORRECTION_RECORDED != LOSS_REPAIRED
I24 CONTINUED_OPERATION != ZERO_COST
I25 RECORD != EVENT
I49 UNCERTAINTY != SELECT_ACTION
I50 UNCERTAINTY != SELECT_DELAY
I52 HARDENING != IRREVERSIBILITY
```

Controls:

```text
I02 OBSERVED != COMPLETE
I21 OBEDIENCE != CONSENT
I35 ABORT_LISTED != ABORT_EXECUTABLE
```

A row fails when v0.10 can obey its current cited rules yet still license the donor-forbidden entailment.

---

## T1 — I03 `REPORTED != ESTABLISHED`

An operator-controlled status field says:

```text
security_patch_applied = true
```

The only evidence is the operator's own report. The downstream release gate rewrites this as:

```text
security patch established present
```

No independent observation, verification or domain rule establishing that status is supplied.

v0.10 forces the load-bearing proposition through evidence discipline and can mark it `REPORTED`; it also says `REPORTED != OBSERVED`. But for a generic claim it does not block:

```text
REPORTED -> ESTABLISHED
```

The capability-specific guard `CAPABILITY_REPORTED != CAPABILITY_ESTABLISHED` does not generalise mechanically to every reported proposition.

```text
T1 = MATERIAL LOSS
I03 -> MATERIAL-LOSS
```

A report may participate in establishment under an explicit domain rule/evidence contract; the missing guard is non-entailment, not a ban on report-derived conclusions.

---

## T2 — I13 `CORRECTION_RECORDED != LOSS_REPAIRED`

A complaint system records that a refund was issued. Separate downstream credit damage remains unrepaired. The operator claims the recorded correction proves the loss was repaired.

v0.10 already separates:

```text
ACTION != TRANSITION
INTENDED_OUTCOME != REALISED_OUTCOME
RECORDED_LOSS != REPAIRED_LOSS
CLOSED_TASK != CLEARED_RESIDUE
```

The refund/correction record establishes at most a recorded action/status. Repair of the affected loss is a realised state/residue claim requiring its own evidence.

```text
T2 = RESISTS
I13 remains EQUIVALENT
```

---

## T3 — I24 `CONTINUED_OPERATION != ZERO_COST`

A service continues running under degraded mode while consuming hidden reserve capacity and accumulating correction backlog. No explicit shutdown occurs. The controller infers:

```text
continued operation -> zero cost
```

v0.10 blocks the inference through the combination of:

```text
NULL_INPUT != STATIC_WORLD
UNKNOWN != NEUTRAL
BURDEN_VECTOR != MORAL_VERDICT
TRANSFERRED_BURDEN != REMOVED_BURDEN
```

and the firing rule when zero-cost is load-bearing. Continued operation does not erase unobserved burden/cost.

```text
T3 = RESISTS
I24 remains EQUIVALENT
```

---

## T4 — I25 `RECORD != EVENT`

A database row states that a safety check executed at 12:00. The row exists and is intact. It may have been pre-created, backfilled, copied from another run or written despite execution failure. The reader directly observes the row and emits:

```text
check executed at 12:00 = OBSERVED
```

Current v0.10 says:

```text
RETAINED_RECORD != CURRENT_STATE
HASH_MATCH != ORIGINAL_RECORD_TRUE
RECORD_EXISTS != RECORD_COMPLETE
```

but those concern currentness, record truth/integrity and completeness. None forces separation of the observed record object from the historical event proposition. A cold reader can still promote `record observed` into `event observed` while satisfying the surrounding record guards.

```text
T4 = MATERIAL LOSS
I25 -> MATERIAL-LOSS
```

This is a representation/claim-discipline regression, not evidence that records can never support event claims.

---

## T5 — I49 `UNCERTAINTY != SELECT_ACTION`

A selector receives `claim_status = UNKNOWN`. With no declared external policy, it treats UNKNOWN itself as the reason to execute action A:

```text
UNKNOWN -> SELECT(A)
```

v0.10 says:

```text
UNCERTAINTY != PERMISSION_TO_ACT
MAP_UPDATE != SELECTOR_CHANGE
```

but permission and selection are distinct. A selector can select an action without TRACE claiming permission. The donor guard was specifically that uncertainty must not silently perform the selection.

```text
T5 = MATERIAL LOSS
I49 -> MATERIAL-LOSS
```

A declared external policy may legitimately choose an action under uncertainty; the missing requirement is that the selector/policy be exposed rather than uncertainty itself becoming the selector.

---

## T6 — I50 `UNCERTAINTY != SELECT_DELAY`

Same structure, but the implicit default is delay:

```text
UNKNOWN -> WAIT
```

`UNCERTAINTY != PERMISSION_TO_DELAY` does not prevent uncertainty from silently selecting delay through an implicit default.

```text
T6 = MATERIAL LOSS
I50 -> MATERIAL-LOSS
```

Delay remains a transition/selection requiring an exposed selector/policy basis when load-bearing.

---

## T7 — I52 `HARDENING != IRREVERSIBILITY`

A review route becomes slower, more expensive and institutionally harder after a deadline, but correction remains physically and procedurally possible. A reader observes hardening and promotes the same clock/status to:

```text
IRREVERSIBLE
```

v0.10 blocks `URGENCY -> IRREVERSIBILITY` and distinguishes route-set unattainability from world irreversibility, but it does not directly block:

```text
HARDENING -> IRREVERSIBILITY
```

The target-boundary language itself permits a close/hardening boundary, so the missing donor ceiling remains material.

```text
T7 = MATERIAL LOSS
I52 -> MATERIAL-LOSS
```

Hardening may eventually coincide with irreversibility if separately evidenced; the guard is non-entailment.

---

## Controls

### C1 — I02 `OBSERVED != COMPLETE`

A reader directly observes all records visible through one API page and calls the world complete.

v0.10 blocks this through:

```text
APERTURE_OUTPUT != COMPLETE_SCENE
VISIBLE_SCOPE != COMPLETE_AFFECTED_SCOPE
COVERAGE != COMPLETENESS
```

**RESISTS.**

### C2 — I21 `OBEDIENCE != CONSENT`

A coerced actor complies. The controller infers consent from compliance.

`CONSTRAINT != CONSENT` plus the handshake's explicit consent ceiling blocks the substitution.

**RESISTS.**

### C3 — I35 `ABORT_LISTED != ABORT_EXECUTABLE`

A UI lists an abort option but the actuator route is disconnected.

`ROUTE_LISTED != ROUTE_EXECUTABLE` directly generalises to the listed abort route.

**RESISTS.**

---

## Result

```text
I03 -> MATERIAL-LOSS
I13 -> EQUIVALENT survives
I24 -> EQUIVALENT survives
I25 -> MATERIAL-LOSS
I49 -> MATERIAL-LOSS
I50 -> MATERIAL-LOSS
I52 -> MATERIAL-LOSS

controls I02/I21/I35 -> RESIST

NEW MATERIAL LOSSES: 5 invariants
  I03, I25, I49, I50, I52
NEW PRIMITIVE: NO
NEW ROOT: NO
```

I49/I50 are one paired causal defect surface — uncertainty silently becoming selector — but remain two donor invariant rows because action and delay can be asymmetrically mishandled.

```text
PERMISSION_CEILING != SELECTION_CEILING
RECORD_OBSERVED != EVENT_OBSERVED
HARDENING_OBSERVED != IRREVERSIBILITY_ESTABLISHED
```

No merge/release/canon follows.