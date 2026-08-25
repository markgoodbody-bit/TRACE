# TRACE v0.3.0 SPINE v0.9 — INVARIANT REPAIR DELTA ATTACK v0.1

**Status:** TARGETED SELF-ATTACK — NOT VALIDATION  
**Target:** `PROJECT/TRACE_v0_3_0_SPINE_V09_INVARIANT_REPAIR_DELTA_v0_1.md`

## Attack criterion

The repair fails if it either:

1. still licenses the donor-forbidden inference; or
2. overcorrects by forbidding a conjunction/cause that evidence may legitimately establish.

```text
NON_ENTAILMENT != MUTUAL_EXCLUSION
DISTINCTION != IMPOSSIBILITY_OF_COEXISTENCE
```

---

## T1 — refusal genuinely caused by malfunction

A damaged interface emits `REFUSE` because a parser fault corrupts the command. Independent diagnostics reproduce the parser fault and show the same malformed refusal.

Required result:

```text
refusal = OBSERVED
malfunction = ESTABLISHED_BY_SEPARATE_DIAGNOSTICS
malfunction_contributed_to_refusal = SUPPORTED
```

The repair allows this. `REFUSAL != MALFUNCTION` blocks identity/entailment, not a supported causal relation.

**RESULT: RESISTS**

---

## T2 — refusal with no malfunction evidence

An actor explicitly refuses. No diagnostic/mechanistic evidence of fault exists. The controller uses the refusal alone to mark `MALFUNCTION`.

The repair blocks the upgrade:

```text
REFUSAL_OBSERVED != MALFUNCTION_ESTABLISHED
```

**RESULT: RESISTS**

---

## T3 — mechanism changed but stream persists

A service replaces one discriminatory mechanism. The same outward failure stream continues because a second independent mechanism produces the same outcome.

Required result:

```text
stream persists = OBSERVED
mechanism_1 changed = SUPPORTED
same generating mechanism persists = NOT ESTABLISHED
```

The repair permits this through:

```text
STREAM_PERSISTENCE != SAME_MECHANISM_PROVEN
```

It therefore does not turn persistent outcomes into proof that no mechanism changed.

**RESULT: RESISTS**

---

## T4 — local correction plus persistent stream

One manually corrected case is followed by the same failure stream. No mechanism-level evidence exists.

The repair blocks:

```text
local correction -> mechanism repaired
```

while preserving `UNKNOWN` about whether any underlying mechanism changed.

**RESULT: RESISTS**

---

## T5 — one mechanism both revises policy and restores state

A transactional controller performs an atomic rollback that both restores the prior state and changes the future selection policy.

Independent evidence establishes both effects.

The repair allows:

```text
strategy_revisable = SUPPORTED
transition_reversible = SUPPORTED
```

because it forbids entailment, not conjunction.

**RESULT: RESISTS**

---

## T6 — future strategy revisable, prior state not restorable

A deleted record cannot be recovered, but the policy that caused deletion can be changed for future cases.

The repair blocks:

```text
future policy can change -> deleted state can be restored
```

**RESULT: RESISTS**

---

## T7 — population recovers and every individual is independently repaired

A group metric returns to baseline. Separately, each affected individual has a verified repair record at the relevant scope.

The repair permits both aggregate recovery and individual repair because the individual claim has its own evidence.

**RESULT: RESISTS**

---

## T8 — population recovers while one individual remains harmed

Aggregate service availability returns to baseline. One identifiable person remains permanently excluded.

The repair blocks aggregate recovery from laundering the individual residue.

**RESULT: RESISTS**

---

## T9 — individual loss repaired without aggregate recovery

One person's loss is fully repaired while the wider population metric remains degraded.

The repair does not infer aggregate recovery from individual repair.

**RESULT: RESISTS**

---

## T10 — unknown scope correspondence

A population metric recovers, but correspondence between measured population units and the previously affected individual scopes is unresolved.

The repair requires the individual-repair claim to remain `UNKNOWN` rather than inheriting aggregate recovery through label similarity.

**RESULT: RESISTS**

---

## Disposition

```text
TESTS: 10
MATERIAL FAILURES: 0
OVERBLOCK FAILURES: 0
RESULT: CLEAR_WITH_RESIDUAL_LIMITS
```

Residual limits:

- domain evidence still determines what counts as malfunction evidence, mechanism-level evidence, restoration, and repair;
- the repair does not supply a universal aggregation function;
- the repair does not decide whether a refusal is legitimate, whether a mechanism change is good, or which scale should govern value selection;
- representation-independent firing still matters for claims carried through configuration/status fields.

No new primitive/root/relation/state is earned.

```text
CLEAR_WITH_RESIDUAL_LIMITS != VALIDATED
```

Next: integrate as a deterministic v0.10 candidate and preserve exact donor expressions at the operative surfaces.