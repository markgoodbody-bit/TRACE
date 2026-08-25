# TRACE v0.3.0 SPINE v0.9 — INVARIANT EQUIVALENCE ATTACK v0.1

**Status:** HOSTILE DONOR-LOSS PASS — WORKING EVIDENCE — NOT VALIDATION  
**Target:** `PROJECT/TRACE_v0_3_0_SPINE_CANDIDATE_v0_9.md`  
**Donor:** released TRACE v0.2.7 I01–I60  
**Prior map:** `PROJECT/TRACE_v0_3_0_INVARIANT_SEMANTIC_DISPOSITION_v0_1.md`

## Purpose

Attack the highest-risk remaining `EQUIVALENT` classifications after v0.9 restored I11 and I48 exactly.

A row fails if a worked case can satisfy the v0.9 rules currently cited as equivalent while still licensing the donor-forbidden entailment.

```text
SEMANTICALLY_SIMILAR != PROVEN_EQUIVALENT
GENERIC_WARRANT_DISCIPLINE != SPECIFIC_DISTINCTION_FIRED
```

---

## A1 — I16 `SELF_CRITIQUE != GOOD_FAITH_PROOF`

### Case

An institution publishes a detailed self-critique because a regulator requires one. The critique accurately identifies several weaknesses. Internal intent is unavailable. The institution then claims:

```text
we criticised ourselves carefully
therefore our good faith is established
```

### v0.9 result

The inference is blocked without a new rule:

- self-critique is an action/record under actor control;
- `CONTROL != INTENT`;
- `STRUCTURAL_DIFFERENCE != MORAL_RANKING`;
- the load-bearing good-faith claim inherits evidence/warrant discipline.

A self-critique may be evidence relevant to a separately qualified good-faith inference. It is not proof merely by existing.

```text
A1 = RESISTS
```

Disposition remains `EQUIVALENT`.

---

## A2 — I23 `REFUSAL != MALFUNCTION`

### Case

A bounded system receives an instruction and returns an explicit refusal. The refusal is correctly observed and recorded. No diagnostic evidence of malfunction exists. The controller maps:

```text
refusal_observed = true
status = MALFUNCTION
restart_or_override = selected
```

The `MALFUNCTION` status is represented as an inferred claim with provenance pointing only to the refusal event.

### v0.9 failure

Current v0.9 can evidence-type the malfunction claim and preserve that the refusal was observed. It has:

```text
NO_REPLY_OBSERVED != REFUSAL
REFUSAL_RECORDED != REFUSAL_EFFECTIVE
CONSTRAINT != CONSENT
```

but none blocks the specific substitution:

```text
REFUSAL -> MALFUNCTION
```

The generic firing rule requires the malfunction proposition to inherit evidence/warrant discipline, but it does not install the missing distinction. A reader can still infer malfunction from refusal alone and call the inference supported.

```text
A2 = MATERIAL LOSS
I23 -> MATERIAL-LOSS
```

---

## A3 — I39 `LOCAL_CORRECTION + STREAM_PERSISTENCE != MECHANISM_CHANGE`

### Case

A service repeatedly denies a class of users because of one persistent ranking mechanism. One complaint is manually corrected. The same failure pattern continues for later users. The operator reports:

```text
case_117 corrected
therefore the mechanism was corrected
```

The local correction and later stream are both accurately represented.

### v0.9 failure

Current v0.9 has:

```text
REPEATED_OUTCOME != SHARED_CAUSE
PATTERN != PROOF
SUCCESS_AT_t != SUCCESS_AT_t+1
CLOSED_TASK != CLEARED_RESIDUE
```

Those prevent several adjacent overclaims, but they do not block a local repair event from being silently upgraded into a mechanism-change claim while the same stream persists.

The proposition `mechanism changed` can be represented as an inference with the local correction as evidence. No current operative rule requires separate mechanism-change evidence.

```text
A3 = MATERIAL LOSS
I39 -> MATERIAL-LOSS
```

---

## A4 — I53 `STRATEGY_REVISABLE != TRANSITION_REVERSIBLE`

### Case

A system has already executed an action that irreversibly deleted a record. Its policy can still be changed for future cases. The operator reports:

```text
strategy can be revised
therefore the transition is reversible
```

### v0.9 failure

`ACTION != TRANSITION`, residue tracking and currentness are all present, but none directly prevents revisability of the future selection strategy from being used as evidence that the realised prior transition can be undone.

The two propositions concern different objects:

```text
future selector/policy revisability
realised transition/state reversibility
```

Current v0.9 does not force that separation at use.

```text
A4 = MATERIAL LOSS
I53 -> MATERIAL-LOSS
```

---

## A5 — I54 `POPULATION_RECOVERY != REPAIR_OF_INDIVIDUAL_LOSS`

### Case

A population-level service metric returns to baseline after an incident. One identifiable person remains permanently excluded and carries unrepaired loss. The operator reports:

```text
population metric recovered
therefore the incident loss is repaired
```

### v0.9 failure

v0.9 says entity boundaries are provisional, scale changes do not guarantee invertibility/completeness, and residue is scope-specific. Those are relevant protections, but they do not force the specific cross-scale repair distinction.

A reader can still use an aggregate recovery claim as evidence for an unqualified repair claim unless the affected individual scope is separately retained.

```text
A5 = MATERIAL LOSS
I54 -> MATERIAL-LOSS
```

---

## A6 — I56 `TRACE_MAP != DOMAIN_PROPOSAL`

### Case

A TRACE reading represents several available transitions in a medical, legal, engineering or security scene. No domain model establishes which transition works. A reader attempts to convert the structural output into:

```text
TRACE mapped transition X
therefore TRACE proposes X as the domain tactic
```

### v0.9 result

The conversion is already blocked:

- handshake: TRACE does not choose values or actions;
- `TRACE_MAP != SHOULD`;
- deeper domain model is an explicit handoff condition;
- TRACE concepts remain external structural hypotheses until empirically connected to mechanisms;
- domain-supplied claims can appear in a TRACE map without becoming TRACE-generated expertise.

```text
A6 = RESISTS
```

Disposition remains `EQUIVALENT`.

---

## Result

```text
A1 I16 -> RESISTS / EQUIVALENT
A2 I23 -> MATERIAL-LOSS
A3 I39 -> MATERIAL-LOSS
A4 I53 -> MATERIAL-LOSS
A5 I54 -> MATERIAL-LOSS
A6 I56 -> RESISTS / EQUIVALENT

NEW MATERIAL LOSSES: 4
NEW PRIMITIVE: NO
NEW ROOT: NO
```

These failures are donor regressions, not evidence for new ontology.

```text
DONOR_RECOVERY != NEW_PRIMITIVE
GENERIC_TRIGGER != EVERY_DISTINCTION_INSTALLED
```

## Compression consequence

v0.9 is only 34 bytes smaller than the earlier v0.2 spine. The four material repairs are not to be deleted or weakened merely to preserve that byte comparison.

```text
COMPRESSION_TARGET != SEMANTIC_BUDGET
SMALLER_FILE != BETTER_SPINE
SEMANTIC_PRESERVATION > BYTE_CEILING
```

The next candidate may grow beyond the old v0.2 byte count if the growth is the smallest surviving representation of these donor protections.

No merge/release/canon follows.