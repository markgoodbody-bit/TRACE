# TRACE v0.3.0 — I01–I60 SEMANTIC DISPOSITION v0.1

**Status:** WORKING DONOR-ACCOUNTING MAP — NOT VALIDATION — NOT EQUIVALENCE PROOF  
**Donor:** released TRACE v0.2.7 invariants I01–I60  
**Candidate:** `PROJECT/TRACE_v0_3_0_SPINE_CANDIDATE_v0_8.md`  
**Lexical witness:** `PROJECT/TRACE_v0_3_0_INVARIANT_LEXICAL_COVERAGE_v0_1.json`

---

## 1. Classification rule

```text
EXACT
  donor invariant expression appears verbatim in v0.8.

EQUIVALENT
  exact expression is absent, but a narrower/broader or distributed v0.8 rule blocks the same tested false entailment.
  This is a working semantic judgment, not a formal proof.

FULL-CANDIDATE
  the invariant belongs to machinery intentionally omitted from the short spine and must remain explicit in the full v0.3 candidate/schema/operator/profile/worked-regression layer.
  Omission from the spine is not permission to delete it.

MATERIAL-LOSS
  v0.8 currently permits a downstream false entailment that the donor invariant blocked and no retained spine rule stops it.
```

No `REDUNDANT` classification is used here. A donor guard is not deleted merely because another sentence sounds similar.

---

## 2. Summary

```text
EXACT:          14
EQUIVALENT:     39
FULL-CANDIDATE:  7
MATERIAL-LOSS:   0   (PROVISIONAL — MUST BE ATTACKED)
TOTAL:          60
```

Lexical coverage alone was only 14/60. The remaining classifications below are semantic and therefore falsifiable.

---

## 3. Disposition table

| ID | Donor invariant | Disposition | v0.8 protection / reason |
|---|---|---|---|
| I01 | `MODEL != WORLD` | EXACT | handshake |
| I02 | `OBSERVED != COMPLETE` | EQUIVALENT | `APERTURE_OUTPUT != COMPLETE_SCENE`; `COVERAGE != COMPLETENESS`; visible scope ceiling |
| I03 | `REPORTED != ESTABLISHED` | EQUIVALENT | `REPORTED != OBSERVED`; generic warrant firing; reported capability does not establish capability |
| I04 | `INFERRED != OBSERVED` | EXACT | claim/evidence section |
| I05 | `UNKNOWN != ABSENT` | EXACT | handshake |
| I06 | `UNAVAILABLE != UNIVERSALLY UNKNOWN` | EQUIVALENT | refined `UNAVAILABLE_TO_THIS_READER != UNIVERSALLY_UNKNOWN` plus evidence/access separation |
| I07 | `CONFIDENCE != TRUTH` | EXACT | claim/evidence section |
| I08 | `CONFIDENCE != AUTHORITY` | EXACT | claim/evidence section |
| I09 | `ENTITY != SENTIENT` | EQUIVALENT | entity inclusion explicitly does not establish sentience; handshake does not assign/deny consciousness/experience |
| I10 | `SENTIENCE_UNKNOWN != SENTIENCE_ABSENT` | EQUIVALENT | `UNKNOWN != ABSENT` applies while entity/handshake forbids sentience inference from inclusion/omission |
| I11 | `ROUTE_EXISTS != ROUTE_USABLE` | EQUIVALENT | `ROUTE_LISTED != ROUTE_EXECUTABLE`; capability/material constraints and route binding must fire when downstream use depends on them |
| I12 | `REVIEW_AFTER_COMMITMENT != BRAKE` | FULL-CANDIDATE | precommit brake versus postcommit rollback/review machinery is intentionally outside the short spine; canonical BRAKE remains in donor schema |
| I13 | `CORRECTION_RECORDED != LOSS_REPAIRED` | EQUIVALENT | `RECORDED_LOSS != REPAIRED_LOSS`; residue/closure ceilings |
| I14 | `PACKET_COMPLETED != TRANSITION_CHANGED` | EQUIVALENT | packet/theatre ceiling plus `TRACE_OUTPUT != RECEIVER_MAP_UPDATE`, `MAP_UPDATE != SELECTOR_CHANGE`, `SELECTOR_CHANGE != WORLD_CHANGE` |
| I15 | `READING != CLEARANCE` | EXACT | handshake |
| I16 | `SELF_CRITIQUE != GOOD_FAITH_PROOF` | EQUIVALENT | self-application does not self-validate; TRACE does not infer intent/good-faith status from the structural act |
| I17 | `LOCAL_EXPANSION != GLOBAL_EXPANSION` | EQUIVALENT | future-space is scope/horizon relative; entity scale changes do not guarantee invertibility/completeness |
| I18 | `OPTION_COUNT != FUTURE_VALUE` | EQUIVALENT | `MORE_OPTIONS != MORALLY_BETTER`; future-space remains measure/designation relative rather than a scalar value score |
| I19 | `COMPLEXITY != AWARENESS` | FULL-CANDIDATE | structural-awareness comparison object is omitted from short spine; no v0.8 awareness scalar is emitted; full candidate must preserve donor ceiling |
| I20 | `ELOQUENCE != STANDING` | EXACT | middle-out start |
| I21 | `OBEDIENCE != CONSENT` | EQUIVALENT | handshake does not assign consent; `CONSTRAINT != CONSENT`; behaviour does not create authority/consent status |
| I22 | `SILENCE != ABSENCE` | EQUIVALENT | `NO_REPLY_OBSERVED != REFUSAL`; `NOT_OBSERVED != ABSENT`; liveness-loss cause remains unknown |
| I23 | `REFUSAL != MALFUNCTION` | EQUIVALENT | refusal and malfunction are distinct propositions requiring their own evidence; generic firing plus intent/causal ceilings blocks silent conversion |
| I24 | `CONTINUED_OPERATION != ZERO_COST` | EQUIVALENT | burden/residue remain live; null/continued operation is not a static world and unknown burden is not neutral/zero |
| I25 | `RECORD != EVENT` | EQUIVALENT | retained record/current world distinction; record completeness does not establish world/event completeness |
| I26 | `VISIBILITY != CARRYING` | FULL-CANDIDATE | carrier mechanics intentionally outside spine; canonical CARRIER and packet-use machinery remain full-candidate obligations |
| I27 | `CARRYING != ENFORCEMENT` | FULL-CANDIDATE | ENFORCER/authority machinery intentionally outside spine; no spine claim equates persistence with enforcement |
| I28 | `TRACE != ME` | EQUIVALENT | value terms may be supplied by Mechanical Ethics or other declared sources; `TRACE_MAP != SHOULD`; structural visibility != value selection |
| I29 | `STRUCTURAL_PATTERN != MORAL_LABEL` | EQUIVALENT | designation/measure/value-port boundary explicitly blocks moral ranking from structural pattern alone |
| I30 | `RECURSION != INFINITE_DELAY` | EQUIVALENT | stop/handoff rule bounds further differentiation; recurrence/self-application does not require endless recursion |
| I31 | `SCHEMA_VALID != WORLD_VALID` | EXACT | handshake/validator ceiling |
| I32 | `PACKET_CITED != DILIGENCE_ESTABLISHED` | EQUIVALENT | `PACKET_COMPLETED != DILIGENCE_ESTABLISHED`; `TRACE_CITED != TRACE_USED` |
| I33 | `PACKET_CITED != MECHANISM_CHANGED` | EQUIVALENT | `TRACE_CITED != TRACE_USED`; map/selector/world-change chain blocks citation from becoming mechanism change |
| I34 | `BRAKE_REPORTED != BRAKE_INDEPENDENT` | FULL-CANDIDATE | typed brake independence/test state remains canonical/full-candidate machinery; short spine does not issue brake-independence verdicts |
| I35 | `ABORT_LISTED != ABORT_EXECUTABLE` | EQUIVALENT | generalized `ROUTE_LISTED != ROUTE_EXECUTABLE` plus capability/authority firing |
| I36 | `PRIMITIVE_OMISSION != WORLD_ABSENCE` | EQUIVALENT | `OMITTED_PRIMITIVE != ABSENT_MECHANISM`; primitive aperture/self-application |
| I37 | `NOT_OBSERVED != ABSENT` | EXACT | absence/stream/pattern section |
| I38 | `ABSENCE_CLAIM != PROVEN_ABSENCE` | EQUIVALENT | absence remains aperture/comparison relative; generic evidence/warrant discipline and `ABSENT_FROM_APERTURE != ABSENT_FROM_WORLD` |
| I39 | `LOCAL_CORRECTION + STREAM_PERSISTENCE != MECHANISM_CHANGE` | EQUIVALENT | recurrence/currentness and stream/pattern ceilings; a local success does not establish future/common-mechanism change |
| I40 | `UNKNOWN != NEUTRAL` | EXACT | handshake |
| I41 | `COURAGE_REQUIRED != ROUTE_USABLE` | FULL-CANDIDATE | safe evidential/contest route usability and holder-risk machinery are fuller access/custody/route obligations; short spine keeps only compressed access/capability distinctions |
| I42 | `COMMITMENT_RECEIPT != CLEARANCE` | FULL-CANDIDATE | commitment receipt is canonical packet/operator machinery omitted from spine; handshake anti-clearance still applies but full candidate must retain receipt-specific guard |
| I43 | `HASH_MATCH != ORIGINAL_RECORD_TRUE` | EXACT | claim/evidence section |
| I44 | `PACKET_COMPLETENESS != SELECTOR_CHANGE` | EQUIVALENT | packet/theatre ceiling; `TRACE_OUTPUT != RECEIVER_MAP_UPDATE`; `MAP_UPDATE != SELECTOR_CHANGE` |
| I45 | `ACTION != TRANSITION` | EXACT | selective causal loop |
| I46 | `MAP != SCENE` | EQUIVALENT | same non-equivalence appears as `SCENE != MAP`; relation is symmetric |
| I47 | `SCENE != WORLD` | EQUIVALENT | `WORLD_STATE != SCENE`; scene is explicitly a representation, not actual surrounding state |
| I48 | `ADVANTAGE_CLAIM_REQUIRES_MEASURE` | EQUIVALENT | designation/measure section says future/loss comparison depends on declared measure; measured advantage does not create entitlement |
| I49 | `UNCERTAINTY != SELECT_ACTION` | EQUIVALENT | `UNCERTAINTY != PERMISSION_TO_ACT`; TRACE output/map update does not itself change selector; TRACE does not select action |
| I50 | `UNCERTAINTY != SELECT_DELAY` | EQUIVALENT | `UNCERTAINTY != PERMISSION_TO_DELAY`; delay/null input remains a represented transition choice rather than default moral selection |
| I51 | `DEADLINE != IRREVERSIBILITY` | EQUIVALENT | `URGENCY != IRREVERSIBILITY`; target boundary and route-relative irreversibility must be represented separately |
| I52 | `HARDENING != IRREVERSIBILITY` | EQUIVALENT | target/hardening boundary is condition/scope/capability relative; route-set unattainability is explicitly not world irreversibility |
| I53 | `STRATEGY_REVISABLE != TRANSITION_REVERSIBLE` | EQUIVALENT | action/transition separation, world-state/result distinction and residue prevent stopping/changing later action from undoing completed transition; retained as regression case |
| I54 | `POPULATION_RECOVERY != REPAIR_OF_INDIVIDUAL_LOSS` | EQUIVALENT | nested/provisional boundaries; scale changes do not guarantee invertibility/completeness; residue remains scope-specific |
| I55 | `OPERATOR_REPORT != INDEPENDENT_VERIFICATION` | EXACT | claim/evidence section |
| I56 | `TRACE_MAP != DOMAIN_PROPOSAL` | EQUIVALENT | TRACE concepts remain external structural hypotheses; value/domain/selection/actuation belong outside TRACE; build ceiling calls for deeper domain model when needed |
| I57 | `TARGET_SET != WORLD_SCOPE` | EQUIVALENT | target-set aperture; visible/selected scope is not complete affected/world scope |
| I58 | `TARGET_NOT_SELECTED != TARGET_DOES_NOT_EXIST` | EQUIVALENT | `NOT_TARGETED != ABSENT`; `UNKNOWN != ABSENT` |
| I59 | `COVERAGE_OF_SELECTED_TARGETS != COMPLETE_DISCOVERY` | EQUIVALENT | `ACCOUNTED_FOR != DISCOVERED_COMPLETE_SET`; `COVERAGE != COMPLETENESS` |
| I60 | `OPERATOR_TARGET_SET != AUTHORITATIVE_TARGET_SET` | EXACT | target-set aperture |

---

## 4. Full-candidate obligations exposed by this pass

The seven `FULL-CANDIDATE` rows are not rejected invariants:

```text
I12  REVIEW_AFTER_COMMITMENT != BRAKE
I19  COMPLEXITY != AWARENESS
I26  VISIBILITY != CARRYING
I27  CARRYING != ENFORCEMENT
I34  BRAKE_REPORTED != BRAKE_INDEPENDENT
I41  COURAGE_REQUIRED != ROUTE_USABLE
I42  COMMITMENT_RECEIPT != CLEARANCE
```

Their supporting donor machinery remains visible in the unchanged v0.3 minimum-schema candidate where applicable, or in the donor operator/profile/worked/misuse layer. Before a full v0.3 replacement claim, each must be mapped to an explicit retained location and regression case.

```text
NOT_IN_SPINE != DELETED_FROM_TRACE
SPINE_OMISSION != FULL_CANDIDATE_PERMISSION_TO_OMIT
```

---

## 5. Highest-risk working equivalences

The following `EQUIVALENT` judgments are most likely to fail under a worked counterexample and should be attacked first:

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

One worked case where v0.8 licenses the forbidden entailment converts that row to `MATERIAL-LOSS` and holds the current semantic spine until repaired or explicitly demoted to a full-candidate boundary with proof that the spine makes no such claim.

---

## 6. Disposition

```text
LEXICAL PASS: 14/60 EXACT
SEMANTIC PASS v0.1: 14 EXACT / 39 EQUIVALENT / 7 FULL-CANDIDATE / 0 MATERIAL-LOSS
ZERO MATERIAL LOSS: PROVISIONAL, NOT ACCEPTED UNTIL HOSTILE CASE PASS
```

`SEMANTICALLY_SIMILAR != PROVEN_EQUIVALENT`.
