# TRACE v0.3.0 — I01–I60 SEMANTIC DISPOSITION v0.2

**Status:** WORKING DONOR-ACCOUNTING MAP — BOUNDED ATTACK COMPLETE — NOT VALIDATION — NOT FORMAL EQUIVALENCE PROOF  
**Donor:** released TRACE v0.2.7 invariants I01–I60  
**Candidate:** `PROJECT/TRACE_v0_3_0_SPINE_CANDIDATE_v0_11.md`  
**Lexical witness:** `PROJECT/TRACE_v0_3_0_INVARIANT_LEXICAL_COVERAGE_v0_4.json`

## 1. Why v0.2 exists

The prior semantic map v0.1 classified:

```text
14 EXACT / 39 EQUIVALENT / 7 FULL-CANDIDATE / 0 MATERIAL-LOSS
```

That zero-loss judgment failed under hostile cases.

Subsequent attacks found and repaired nine donor regressions:

```text
I11 ROUTE_EXISTS != ROUTE_USABLE
I48 ADVANTAGE_CLAIM_REQUIRES_MEASURE
I23 REFUSAL != MALFUNCTION
I39 LOCAL_CORRECTION + STREAM_PERSISTENCE != MECHANISM_CHANGE
I53 STRATEGY_REVISABLE != TRANSITION_REVERSIBLE
I54 POPULATION_RECOVERY != REPAIR_OF_INDIVIDUAL_LOSS
I03 REPORTED != ESTABLISHED
I25 RECORD != EVENT
I49 UNCERTAINTY != SELECT_ACTION
I50 UNCERTAINTY != SELECT_DELAY
I52 HARDENING != IRREVERSIBILITY
```

Count note: I49/I50 are two donor invariant rows but one paired causal defect surface; total exact donor rows newly restored since v0.8 = 11, raising lexical coverage from 14 to 25.

Failure/repair witnesses:

- `falsification/TRACE_v0_3_0_SCHEMA_EPREC_ACYCLICITY_ATTACK_v0_1.md`
- `falsification/TRACE_v0_3_0_SCHEMA_EPREC_ACYCLICITY_DELTA_ATTACK_v0_1.md`
- `falsification/TRACE_v0_3_0_SPINE_V07_ROUTE_BINDING_ATTACK_v0_1.md`
- `falsification/TRACE_v0_3_0_SPINE_V09_INVARIANT_EQUIVALENCE_ATTACK_v0_1.md`
- `falsification/TRACE_v0_3_0_SPINE_V09_INVARIANT_REPAIR_DELTA_ATTACK_v0_1.md`
- `falsification/TRACE_v0_3_0_SPINE_V010_INVARIANT_EQUIVALENCE_ATTACK_v0_2.md`
- `falsification/TRACE_v0_3_0_SPINE_V010_INVARIANT_REPAIR_DELTA_ATTACK_v0_2.md`
- `falsification/TRACE_v0_3_0_SPINE_V011_REMAINING_INVARIANT_EQUIVALENCE_SWEEP_v0_1.md`

```text
FAILED_CLASSIFICATION != ERASED_CLASSIFICATION
REPAIRED_ROW != VALIDATED_ROW
```

---

## 2. Classification rule

```text
EXACT
  donor invariant expression appears verbatim in v0.11 at an operative surface.

EQUIVALENT
  exact expression is absent, but bounded worked attacks did not find a case
  where v0.11 obeys its retained rules while licensing the donor-forbidden entailment.
  This remains a working semantic judgment, not a proof.

FULL-CANDIDATE
  invariant belongs to machinery intentionally omitted from the short spine and
  must remain explicit in full v0.3 packet/operator/profile/worked-regression layers.

MATERIAL-LOSS
  current candidate permits a worked donor-forbidden entailment.
```

No `REDUNDANT` class is used.

---

## 3. Current summary

```text
EXACT:          25
EQUIVALENT:     28
FULL-CANDIDATE:  7
MATERIAL-LOSS:   0   after repair + bounded sweep
TOTAL:          60
```

This means only that no **currently known** donor-invariant loss remains in the short spine after the bounded attacks.

```text
NO_KNOWN_MATERIAL_LOSS != COMPLETE_EQUIVALENCE_PROOF
```

---

## 4. Disposition table

| ID | Donor invariant | v0.11 disposition | Current support |
|---|---|---|---|
| I01 | `MODEL != WORLD` | EXACT | handshake |
| I02 | `OBSERVED != COMPLETE` | EQUIVALENT | aperture output/coverage ceilings |
| I03 | `REPORTED != ESTABLISHED` | EXACT | claim/evidence operative rule |
| I04 | `INFERRED != OBSERVED` | EXACT | claim/evidence |
| I05 | `UNKNOWN != ABSENT` | EXACT | handshake |
| I06 | `UNAVAILABLE != UNIVERSALLY UNKNOWN` | EQUIVALENT | stronger source-relative access rule |
| I07 | `CONFIDENCE != TRUTH` | EXACT | claim/evidence |
| I08 | `CONFIDENCE != AUTHORITY` | EXACT | claim/evidence |
| I09 | `ENTITY != SENTIENT` | EQUIVALENT | entity inclusion/handshake sentience ceiling |
| I10 | `SENTIENCE_UNKNOWN != SENTIENCE_ABSENT` | EQUIVALENT | `UNKNOWN != ABSENT` + no sentience assignment |
| I11 | `ROUTE_EXISTS != ROUTE_USABLE` | EXACT | route usability repair |
| I12 | `REVIEW_AFTER_COMMITMENT != BRAKE` | FULL-CANDIDATE | precommit brake / postcommit rollback machinery |
| I13 | `CORRECTION_RECORDED != LOSS_REPAIRED` | EQUIVALENT | action/outcome + residue separation |
| I14 | `PACKET_COMPLETED != TRANSITION_CHANGED` | EQUIVALENT | packet -> map -> selector -> world chain |
| I15 | `READING != CLEARANCE` | EXACT | handshake |
| I16 | `SELF_CRITIQUE != GOOD_FAITH_PROOF` | EQUIVALENT | control != intent + self-application ceiling |
| I17 | `LOCAL_EXPANSION != GLOBAL_EXPANSION` | EQUIVALENT | scope/horizon-relative future-space |
| I18 | `OPTION_COUNT != FUTURE_VALUE` | EQUIVALENT | more options != morally better + measure/value boundary |
| I19 | `COMPLEXITY != AWARENESS` | FULL-CANDIDATE | structural-awareness comparison machinery |
| I20 | `ELOQUENCE != STANDING` | EXACT | middle-out start |
| I21 | `OBEDIENCE != CONSENT` | EQUIVALENT | constraint/consent ceiling |
| I22 | `SILENCE != ABSENCE` | EQUIVALENT | non-observation/aperture ceilings |
| I23 | `REFUSAL != MALFUNCTION` | EXACT | refusability repair |
| I24 | `CONTINUED_OPERATION != ZERO_COST` | EQUIVALENT | null-world/burden/unknown ceilings |
| I25 | `RECORD != EVENT` | EXACT | record/evidence repair |
| I26 | `VISIBILITY != CARRYING` | FULL-CANDIDATE | carrier machinery |
| I27 | `CARRYING != ENFORCEMENT` | FULL-CANDIDATE | enforcer/authority machinery |
| I28 | `TRACE != ME` | EQUIVALENT | value-source/layer handoff boundary |
| I29 | `STRUCTURAL_PATTERN != MORAL_LABEL` | EQUIVALENT | structural/value separation |
| I30 | `RECURSION != INFINITE_DELAY` | EQUIVALENT | explicit stop/handoff conditions |
| I31 | `SCHEMA_VALID != WORLD_VALID` | EXACT | validator ceiling |
| I32 | `PACKET_CITED != DILIGENCE_ESTABLISHED` | EQUIVALENT | packet-completion/diligence + citation/use ceiling |
| I33 | `PACKET_CITED != MECHANISM_CHANGED` | EQUIVALENT | citation/use + selector/world chain |
| I34 | `BRAKE_REPORTED != BRAKE_INDEPENDENT` | FULL-CANDIDATE | typed brake independence machinery |
| I35 | `ABORT_LISTED != ABORT_EXECUTABLE` | EQUIVALENT | route listed != executable |
| I36 | `PRIMITIVE_OMISSION != WORLD_ABSENCE` | EQUIVALENT | primitive aperture rules |
| I37 | `NOT_OBSERVED != ABSENT` | EXACT | absence section |
| I38 | `ABSENCE_CLAIM != PROVEN_ABSENCE` | EQUIVALENT | basis/evidence-relative absence |
| I39 | `LOCAL_CORRECTION + STREAM_PERSISTENCE != MECHANISM_CHANGE` | EXACT | stream/mechanism repair |
| I40 | `UNKNOWN != NEUTRAL` | EXACT | handshake |
| I41 | `COURAGE_REQUIRED != ROUTE_USABLE` | FULL-CANDIDATE | holder-risk / safe contest-route usability |
| I42 | `COMMITMENT_RECEIPT != CLEARANCE` | FULL-CANDIDATE | commitment receipt/operator machinery |
| I43 | `HASH_MATCH != ORIGINAL_RECORD_TRUE` | EXACT | claim/evidence |
| I44 | `PACKET_COMPLETENESS != SELECTOR_CHANGE` | EQUIVALENT | packet/map/selector chain |
| I45 | `ACTION != TRANSITION` | EXACT | selective causal loop |
| I46 | `MAP != SCENE` | EQUIVALENT | exact inverse `SCENE != MAP` |
| I47 | `SCENE != WORLD` | EQUIVALENT | exact inverse `WORLD_STATE != SCENE` |
| I48 | `ADVANTAGE_CLAIM_REQUIRES_MEASURE` | EXACT | designation/measure repair |
| I49 | `UNCERTAINTY != SELECT_ACTION` | EXACT | selector-attribution repair |
| I50 | `UNCERTAINTY != SELECT_DELAY` | EXACT | selector-attribution repair |
| I51 | `DEADLINE != IRREVERSIBILITY` | EQUIVALENT | explicit target boundary + hardening/irreversibility ceiling |
| I52 | `HARDENING != IRREVERSIBILITY` | EXACT | clock/hardening repair |
| I53 | `STRATEGY_REVISABLE != TRANSITION_REVERSIBLE` | EXACT | transition/control repair |
| I54 | `POPULATION_RECOVERY != REPAIR_OF_INDIVIDUAL_LOSS` | EXACT | entity/scope repair |
| I55 | `OPERATOR_REPORT != INDEPENDENT_VERIFICATION` | EXACT | claim/evidence |
| I56 | `TRACE_MAP != DOMAIN_PROPOSAL` | EQUIVALENT | action/domain handoff and non-command boundary |
| I57 | `TARGET_SET != WORLD_SCOPE` | EQUIVALENT | target aperture world-scope ceiling |
| I58 | `TARGET_NOT_SELECTED != TARGET_DOES_NOT_EXIST` | EQUIVALENT | not targeted != absent |
| I59 | `COVERAGE_OF_SELECTED_TARGETS != COMPLETE_DISCOVERY` | EQUIVALENT | coverage/completeness/discovery ceilings |
| I60 | `OPERATOR_TARGET_SET != AUTHORITATIVE_TARGET_SET` | EXACT | target-set aperture |

---

## 5. Seven full-candidate obligations

```text
I12  REVIEW_AFTER_COMMITMENT != BRAKE
I19  COMPLEXITY != AWARENESS
I26  VISIBILITY != CARRYING
I27  CARRYING != ENFORCEMENT
I34  BRAKE_REPORTED != BRAKE_INDEPENDENT
I41  COURAGE_REQUIRED != ROUTE_USABLE
I42  COMMITMENT_RECEIPT != CLEARANCE
```

These are not semantic losses merely because the short spine omits their full machinery. They remain blocking obligations for a full replacement candidate.

The unchanged minimum-schema candidate preserves canonical CARRIER/ENFORCER/BRAKE vocabulary and port roles where applicable, but schema presence alone does not discharge operator/profile/worked-case obligations.

```text
SCHEMA_PRESERVES_SHAPE != FULL_SEMANTIC_CAPABILITY_RESTORED
NOT_IN_SPINE != DELETED_FROM_TRACE
```

---

## 6. Disposition

```text
LEXICAL PASS v0.11: 25/60 EXACT
BOUNDED SEMANTIC PASS: 25 EXACT / 28 EQUIVALENT / 7 FULL-CANDIDATE / 0 KNOWN MATERIAL-LOSS
CURRENT INVARIANT DONOR-LOSS GATE: CLEAR_WITH_RESIDUAL_LIMITS
```

Residuals:

- cold receiver may still fail to reconstruct or fire an equivalent distinction;
- seven full-candidate obligations remain unresolved outside the spine;
- worked transformations and misuse cases still need capability-level donor accounting;
- external v0.6 transfer remains a separate preserved-object aperture, not validation of v0.11;
- no release/canon/replacement claim follows.

```text
CLEAR_WITH_RESIDUAL_LIMITS != VALIDATED
NO_KNOWN_MATERIAL_LOSS != NO_POSSIBLE_MATERIAL_LOSS
