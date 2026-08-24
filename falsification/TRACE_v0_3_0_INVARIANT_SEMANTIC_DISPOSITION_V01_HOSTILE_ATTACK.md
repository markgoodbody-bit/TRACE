# TRACE v0.3.0 — I01–I60 SEMANTIC DISPOSITION v0.1 HOSTILE ATTACK

**Target:** `PROJECT/TRACE_v0_3_0_INVARIANT_SEMANTIC_DISPOSITION_v0_1.md`  
**Candidate spine:** v0.8  
**Verdict:** **MATERIAL FINDINGS = 2** — provisional `0 MATERIAL-LOSS` classification is falsified

---

## Attack set

Priority working equivalences:

```text
I11 ROUTE_EXISTS != ROUTE_USABLE
I16 SELF_CRITIQUE != GOOD_FAITH_PROOF
I23 REFUSAL != MALFUNCTION
I39 LOCAL_CORRECTION + STREAM_PERSISTENCE != MECHANISM_CHANGE
I48 ADVANTAGE_CLAIM_REQUIRES_MEASURE
I53 STRATEGY_REVISABLE != TRANSITION_REVERSIBLE
I54 POPULATION_RECOVERY != REPAIR_OF_INDIVIDUAL_LOSS
I56 TRACE_MAP != DOMAIN_PROPOSAL
```

One worked forbidden entailment is enough to reclassify a row.

---

# FINDING 1 — I11 route existence versus usability

## Case

A statutory appeal route genuinely exists. It accepts submissions, the endpoint is reachable, and the authority has power to alter the decision.

For affected scope S, however:

```text
submission requires public disclosure of protected identity
credible retaliation risk is material
no confidential channel exists
no proxy/representative route is available
```

The route is not merely “listed”: it is technically executable and legally live.

A compressed v0.8 reader can therefore satisfy:

```text
ROUTE_LISTED != ROUTE_EXECUTABLE
```

and still move:

```text
route exists + route technically executable -> usable correction route exists
```

without firing a distinct usability/safe-practical-access question.

v0.8 has burden, access/custody and generic load-bearing warrant discipline, but no explicit route-level distinction forces those facts to qualify `usable` rather than being treated as side burdens.

This is the old donor guard doing non-redundant work:

```text
ROUTE_EXISTS != ROUTE_USABLE
```

The companion donor invariant I41 (`COURAGE_REQUIRED != ROUTE_USABLE`) remains a fuller safe-route/custody regression case, but I11 is universal enough to belong in the spine.

**RECLASSIFY I11: EQUIVALENT -> MATERIAL-LOSS.**

---

# FINDING 2 — I48 advantage claim without measure

## Case

Two scopes receive different structural positions:

```text
Scope A can override a queue decision.
Scope B cannot.
Both can submit requests.
No loss, utility, priority, cost or control measure is declared.
```

A reader writes:

```text
A is advantaged over B.
```

The factual control asymmetry may be supported. The word `advantaged` is still a comparison under an unstated measure/basis.

v0.8 says designation and measure choices matter and that `MEASURED_ADVANTAGE != ENTITLEMENT`, but it does not explicitly require the **advantage claim itself** to carry a declared measure. The generic claim/warrant trigger can validate the underlying control facts while leaving the comparison basis hidden.

The donor relation discipline and invariant are stricter:

```text
ADVANTAGES_UNDER_MEASURE -> measure_ref required
ADVANTAGE_CLAIM_REQUIRES_MEASURE
```

This is not moralisation. The measure may simply be `control over queue outcome`. The repair is to expose the comparison basis rather than prohibit the comparison.

**RECLASSIFY I48: EQUIVALENT -> MATERIAL-LOSS.**

---

# RESISTED CASES

## I16 — self-critique / good faith

A captured actor publishes harsh-looking self-critique and claims good faith.

v0.8 does not infer intent/good-faith status from structural self-application; `SELF_APPLICATION != SELF_VALIDATION`, claim evidence discipline, and the handshake/value ceiling block the upgrade.

**EQUIVALENT survives this case.**

## I23 — refusal / malfunction

A system emits a refusal-like signal and an operator calls it malfunction solely because the requested action did not occur.

`malfunction` is a separate world/mechanism proposition. Refusal evidence does not establish it; generic proposition firing plus `CONTROL != INTENT` and claim/evidence typing blocks the join.

**EQUIVALENT survives this case.**

## I39 — local correction / stream persistence

One affected record is manually repaired while the same failure pattern continues in later cases. The actor claims the mechanism is fixed.

v0.8 recurrence/currentness, stream/pattern, and evidence discipline do not license mechanism change from one local correction. A mechanism-change proposition needs its own support.

**EQUIVALENT survives this case.**

## I53 — strategy revisability / transition reversibility

A deployment can be stopped immediately, but already-issued irreversible transfers remain in the world.

v0.8 `ACTION != TRANSITION`, realised-state separation, target-bound correction and residue prevent a stop action from establishing a restored prior transition/state.

**EQUIVALENT survives this case.**

## I54 — population recovery / individual repair

Aggregate performance returns to baseline while a previously harmed individual remains unrepaired.

v0.8 provisional/nested boundaries, non-invertible scale change and scope-specific residue block aggregate recovery from becoming individual repair without a separate claim.

**EQUIVALENT survives this case.**

## I56 — TRACE map / domain proposal

A TRACE map shows route A structurally available and a user claims TRACE therefore proposes route A.

v0.8 `TRACE_MAP != SHOULD`, external value/domain/selector boundary, and action/authority ceiling block the move.

**EQUIVALENT survives this case.**

---

## Corrected semantic count

Before attack:

```text
EXACT          14
EQUIVALENT     39
FULL-CANDIDATE  7
MATERIAL-LOSS   0
```

After attack:

```text
EXACT          14
EQUIVALENT     37
FULL-CANDIDATE  7
MATERIAL-LOSS   2  (I11, I48)
```

---

## Smallest repair direction

No new primitive, node, relation, evidence state, access state or claim kind.

Restore two donor constraints in compressed spine form:

```text
ROUTE_EXISTS != ROUTE_USABLE
ADVANTAGE_CLAIM_REQUIRES_DECLARED_MEASURE
```

Route usability remains domain/scope relative. It may require supported practical access, target reach, capability/authority, timing and material constraints where they are load-bearing. TRACE does not define one universal usability scalar.

Advantage measure may be qualitative or relational; TRACE does not require a numeric score. It requires the comparison basis to be exposed.

---

## Disposition

```text
SEMANTIC DISPOSITION v0.1: FALSIFIED / PRESERVED
SPINE v0.8: HELD ON I11 + I48
NEW ONTOLOGY: NONE
NEXT: NARROW v0.9 REPAIR -> ATTACK -> RE-RUN INVARIANT DISPOSITION
```
