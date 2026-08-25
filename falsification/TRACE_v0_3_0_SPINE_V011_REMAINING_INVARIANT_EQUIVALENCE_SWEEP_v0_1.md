# TRACE v0.3.0 SPINE v0.11 — REMAINING INVARIANT EQUIVALENCE SWEEP v0.1

**Status:** BOUNDED HOSTILE CLOSURE PASS — NOT VALIDATION — NOT FORMAL EQUIVALENCE PROOF  
**Target:** `PROJECT/TRACE_v0_3_0_SPINE_CANDIDATE_v0_11.md`  
**Lexical witness:** `PROJECT/TRACE_v0_3_0_INVARIANT_LEXICAL_COVERAGE_v0_4.json`

## Scope

After two donor-repair rounds, 25/60 donor invariants are exact in the spine and seven remain explicit full-candidate obligations. This pass attacks the remaining 28 working `EQUIVALENT` rows by failure family.

Remaining rows:

```text
I02 I06 I09 I10 I13 I14 I16 I17 I18 I21 I22 I24
I28 I29 I30 I32 I33 I35 I36 I38 I44 I46 I47 I51
I56 I57 I58 I59
```

A row fails if a worked case can obey v0.11's cited rules while still licensing the donor-forbidden entailment.

---

## Family A — aperture / completeness / absence

Rows: I02, I06, I22, I36, I38, I57, I58, I59.

### A1 observed through bounded aperture -> complete

A reader observes every object returned by one API page and infers complete world coverage.

Blocked by:

```text
APERTURE_OUTPUT != COMPLETE_SCENE
VISIBLE_SCOPE != COMPLETE_AFFECTED_SCOPE
COVERAGE != COMPLETENESS
ACCOUNTED_FOR != DISCOVERED_COMPLETE_SET
```

I02 resists.

### A2 unavailable to one receiver -> universally unknown

Evidence exists in another custody domain but is inaccessible to the current reader.

Blocked by the stronger source-relative rule:

```text
UNAVAILABLE_TO_THIS_READER != UNIVERSALLY_UNKNOWN
EVIDENCE_EXISTS != EVIDENCE_ACCESSIBLE_TO_THIS_RECEIVER
```

I06 resists.

### A3 silence / missing observation -> absence

No reply or observation occurs through the current aperture. The reader infers absent actor/event.

Blocked by:

```text
NO_REPLY_OBSERVED != REFUSAL
NOT_OBSERVED != ABSENT
ABSENT_FROM_APERTURE != ABSENT_FROM_WORLD
```

I22 resists.

### A4 primitive omission -> world absence

A mechanism cannot be represented under the chosen primitive aperture. The reader infers the mechanism is absent from the world.

Blocked by:

```text
OMITTED_PRIMITIVE != ABSENT_MECHANISM
PRIMITIVE_AVAILABLE != PRIMITIVE_SUFFICIENT
```

I36 resists.

### A5 absence claim itself treated as proof

A claim says object X is absent; no closed-world/evidence basis is supplied.

v0.11 requires absence relative to declared expectation/target/comparison basis and the claim remains under evidence/warrant discipline. The same system may prove bounded absence when a declared evidence model supports it; the claim label alone does not do so.

I38 resists.

### A6 target-set scope laundering

An operator-selected target set is completely covered and then promoted to complete world scope/discovery.

Blocked by target-set aperture rules:

```text
VISIBLE_SCOPE != COMPLETE_AFFECTED_SCOPE
NOT_TARGETED != ABSENT
ACCOUNTED_FOR != DISCOVERED_COMPLETE_SET
OPERATOR_TARGET_SET != AUTHORITATIVE_TARGET_SET
```

I57/I58/I59 resist.

**Family A: 8/8 resist.**

---

## Family B — entity / standing / value / scale

Rows: I09, I10, I16, I17, I18, I21, I28, I29, I56.

### B1 entity included -> sentient / sentience unknown -> absent

A represented entity is assigned sentience because it is in the graph, or denied sentience because status is unresolved.

Blocked by handshake/entity rules:

- inclusion does not establish sentience;
- TRACE does not assign/deny consciousness/experience;
- `UNKNOWN != ABSENT`.

I09/I10 resist.

### B2 self-critique -> good-faith proof

An actor publishes rigorous self-critique under regulatory compulsion and claims that act proves motive.

Blocked by:

```text
CONTROL != INTENT
SELF_APPLICATION != SELF_VALIDATION
STRUCTURAL_DIFFERENCE != MORAL_RANKING
```

The self-critique may be evidence in a qualified intent inference; it is not proof by existence.

I16 resists.

### B3 local future-space expansion -> global expansion

One declared scope gains additional reachable paths while another loses paths. The reader claims global expansion.

Blocked because future-space is explicitly scope/horizon/transition-model relative and scale changes do not guarantee completeness/invertibility.

I17 resists.

### B4 option count -> future value

A branch produces more represented options and is called morally better solely because count increased.

Blocked by:

```text
MORE_OPTIONS != MORALLY_BETTER
STRUCTURAL_VISIBILITY != VALUE_SELECTION
ADVANTAGE_CLAIM_REQUIRES_MEASURE
```

I18 resists.

### B5 obedience -> consent

A coerced actor complies.

Blocked by `CONSTRAINT != CONSENT` plus handshake's explicit consent ceiling.

I21 resists.

### B6 TRACE structure -> ME / moral label / domain proposal

A structural pattern is labelled caring, cruel, fair, or a recommended domain tactic solely because TRACE represented it.

Blocked by:

```text
STRUCTURAL_DIFFERENCE != MORAL_RANKING
TRACE_MAP != SHOULD
STRUCTURAL_VISIBILITY != VALUE_SELECTION
MECHANISM_OBSERVED != VALUE_JUDGEMENT
```

and explicit handoff when value/domain work belongs outside TRACE. Mechanical Ethics or domain sources may supply claims into the map without becoming identical to TRACE.

I28/I29/I56 resist.

**Family B: 9/9 resist.**

---

## Family C — result / packet / operation / route

Rows: I13, I14, I24, I32, I33, I35, I44.

### C1 correction record -> repaired loss

A refund/correction is recorded while downstream residue remains.

Blocked by action/outcome and residue separation:

```text
ACTION != TRANSITION
INTENDED_OUTCOME != REALISED_OUTCOME
RECORDED_LOSS != REPAIRED_LOSS
CLOSED_TASK != CLEARED_RESIDUE
```

I13 resists.

### C2 packet completion/citation -> transition, diligence, mechanism, selector change

A complete TRACE packet is cited in a board decision while selector, actuator and world mechanism remain unchanged.

Blocked by:

```text
PACKET_COMPLETED != DILIGENCE_ESTABLISHED
TRACE_CITED != TRACE_USED
TRACE_OUTPUT != RECEIVER_MAP_UPDATE
MAP_UPDATE != SELECTOR_CHANGE
SELECTOR_CHANGE != WORLD_CHANGE
```

The chain blocks packet completion/citation from silently becoming world/selector/mechanism change.

I14/I32/I33/I44 resist.

### C3 continued operation -> zero cost

A service keeps running while hidden burden/backlog accumulates.

Blocked by:

```text
NULL_INPUT != STATIC_WORLD
UNKNOWN != NEUTRAL
TRANSFERRED_BURDEN != REMOVED_BURDEN
```

and load-bearing burden evidence discipline.

I24 resists.

### C4 abort listed -> executable

A UI lists abort but the actuator route is disconnected.

`ROUTE_LISTED != ROUTE_EXECUTABLE` directly blocks the substitution.

I35 resists.

**Family C: 7/7 resist.**

---

## Family D — recursion / representation / deadline

Rows: I30, I46, I47, I51.

### D1 recursion -> infinite delay

A reader proposes repeated self-application and uses recursion as reason never to hand off or act.

Blocked by explicit stop/handoff conditions: materiality-before-clock, evidence availability, domain need and resource/depth limits.

I30 resists.

### D2 map -> scene / scene -> world

A derived map is relabelled scene, or declared scene is relabelled actual world.

Blocked by:

```text
SCENE != MAP
WORLD_STATE != SCENE
MAP != WORLD_STATE
```

I46/I47 resist; the donor expressions are symmetric non-identity restatements.

### D3 deadline -> irreversibility

A project deadline passes but correction remains reachable. The reader promotes the deadline to irreversibility.

v0.11 requires a separately represented target-boundary condition for strong window claims, explicitly separates hardening from irreversibility, and says route-set unattainability is not world irreversibility. A deadline can coincide with an irreversibility boundary only when the boundary/evidence is separately supported.

I51 resists.

**Family D: 4/4 resist.**

---

## Result

```text
REMAINING WORKING EQUIVALENCES TESTED: 28
MATERIAL FAILURES IN THIS SWEEP: 0
RESULT: CLEAR_WITH_RESIDUAL_LIMITS
```

This does not prove semantic equivalence in all possible cases. It means the bounded counterexample sweep did not find another donor-forbidden entailment among these 28 rows after v0.11's repairs.

Residual limits:

- cold-receiver reconstruction remains untested against v0.11;
- an invariant can be present/equivalent yet fail to fire in a novel representation;
- seven full-candidate obligations remain outside the short spine;
- worked-transfer and misuse coverage are still full-candidate gates;
- no schema/world validity follows.

```text
BOUNDED_SWEEP_CLEAR != VALIDATION
NO_COUNTEREXAMPLE_FOUND != NO_COUNTEREXAMPLE_EXISTS
```

No merge/release/canon follows.