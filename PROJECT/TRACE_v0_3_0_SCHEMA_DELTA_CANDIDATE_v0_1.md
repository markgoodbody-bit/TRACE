# TRACE v0.3.0 — SCHEMA DELTA CANDIDATE v0.1

**Status:** WORKING FULL-CANDIDATE BOUNDARY — NO SCHEMA CHANGE EARNED YET — NOT FORMAL BASELINE — NOT CANON — NOT VALIDATED  
**Donor schema:** released TRACE v0.2.7  
**Current semantic spine:** `PROJECT/TRACE_v0_3_0_SPINE_CANDIDATE_v0_6.md`  
**Purpose:** determine whether v0.3 semantic repairs require any controlled node/relation/claim/access vocabulary change before full-candidate assembly

---

## 1. Current decision

```text
NODE TYPE ADDITIONS:     NONE
RELATION TYPE ADDITIONS: NONE
CLAIM KIND ADDITIONS:    NONE
EVIDENCE STATE CHANGE:   NONE
ACCESS STATE CHANGE:     NONE
NEW PORT:                NONE
```

This is a candidate conclusion, not a permanent freeze. A new schema term requires a worked case that cannot be represented without material loss using retained donor structure.

```text
NEW SEMANTIC RULE != NEW SCHEMA OBJECT
USEFUL NAME != EARNED PRIMITIVE
```

---

## 2. Frozen donor node vocabulary

Carry forward unchanged unless separately falsified:

```text
SCENE
MAP
ENTITY
STATE
SIGNAL
CLAIM
APERTURE
ACTION
TRANSITION
COUPLING
CLOCK
FUTURE_PATH
ROUTE
BURDEN
RESIDUE
RECORD
ABSENCE
STREAM
PATTERN
DESIGNATION
MEASURE
SELECTOR
POLICY
CARRIER
ENFORCER
BRAKE
LIMIT
```

No v0.3 field finding currently requires `PROCESS`, `WITNESS`, `LIVENESS`, `RESOURCE`, `QUEUE`, `SCHEDULER`, `TARGET_BOUNDARY`, `TRIGGER`, or `FRESHNESS` as a new universal node.

---

## 3. Frozen donor relation vocabulary

Carry forward unchanged unless separately falsified:

```text
REPRESENTS
OBSERVES
REPORTS
INFERS
DISPUTES
CANNOT_ACCESS
OMITS
BOUNDS
CONTAINS
PERSISTS_AS
INSTANCE_OF
AGGREGATES
RECURS_AS
TRANSITIONS_TO
CAUSES
CONTRIBUTES_TO
COUPLES
DEPENDS_ON
CONTROLS
CONSTRAINS
ADVANTAGES_UNDER_MEASURE
BURDENS
OPENS
PRESERVES
CLOSES
HARDENS
FORECLOSES
ROUTES_TO
CAN_CORRECT
LEAVES_RESIDUE
RECORDS
ALTERS_RECORD
DESIGNATES
MEASURES
SELECTS
CARRIES
ENFORCES
BRAKES
INTERRUPTS
EXCLUDES
INHERITS
CITES_AS_AUTHORITY
CITES_AS_DILIGENCE
VERIFIES
ACTIVATES
FAILS_TO_ACTIVATE
```

No `PRECEDES`, `INVALIDATES`, `AUTHORIZES`, `WITNESSES`, `SCHEDULES`, or `CORRESPONDS_TO` relation is currently earned.

---

## 4. Frozen claim/evidence/access vocabulary

Retain donor canonical separation:

```text
EVIDENCE_STATE := O | R | I | D | U
ACCESS_STATE   := A | X | P | N

CLAIM_KIND :=
  PRESENT
  ABSENT
  RELATIONAL
  COUNTERFACTUAL
  STATUS
  FORECAST
  NORMATIVE_EXTERNAL
```

v0.6's compressed access/custody rule is a semantic use rule over this donor algebra, not a replacement for it.

---

## 5. Mapping v0.6 repairs onto retained schema

### 5.1 Representation-independent firing

No schema change.

A load-bearing proposition that arrives as configuration/metadata/status/default/cached output must be represented or referenced as a claim when its evidence/currentness/scope/warrant matters to a downstream use.

Existing donor rule already requires material edges to reference claims and allows a `CLAIM` node when the claim must participate in graph relations.

```text
CONFIGURATION_FIELD != WARRANT_FREE_FACT
MATERIAL_PROPOSITION -> CLAIM DISCIPLINE
```

The firing rule decides **when** existing claim machinery becomes load-bearing; it does not add a representation type.

### 5.2 Dependency-relative freshness

No `FRESHNESS` or `INVALIDATES` relation required.

Where a currentness claim depends on a source/version/route/capability, represent the load-bearing dependency through existing claim provenance and, when graph participation is needed, reify the canonical claim and connect relevant objects with `DEPENDS_ON`, `REPORTS`, `OBSERVES`, `INHERITS`, `ALTERS_RECORD`, or other accurate retained relations.

A later mutation/event is represented as its actual transition/record/capability change plus a claim about whether that change reaches the derivation.

```text
SOURCE_MUTATED != LOAD_BEARING_DEPENDENCY_CHANGED
```

No generic `INVALIDATES` edge is allowed to smuggle the conclusion into the relation label.

### 5.3 Measurement / publication reactivity

No measurement-intervention primitive.

A measurement remains a `MEASURE`/claim/evidence object. If the act of measuring, publishing, notifying or querying enters the causal path, represent the relevant `ACTION` and later `TRANSITION`, joined only by supported `CAUSES` or `CONTRIBUTES_TO` claims.

```text
MEASUREMENT_OCCURRED != MEASUREMENT_CAUSED_CHANGE
```

### 5.4 Verification discrimination

No `PROCESS` or `INSTRUMENT_ADEQUACY` node.

Use retained `VERIFIES`, `ACTIVATES`, `FAILS_TO_ACTIVATE`, claims, records, apertures, measures, actions/transitions and clocks as the domain evidence supports.

A `VERIFIES` relation still carries a verification target and limit; its label does not establish universal adequacy.

### 5.5 Liveness / witness

No `WITNESS` or `LIVENESS` node.

Represent the actual observer/entity/aperture/record/route and the observed heartbeat/status/non-observation claims. Loss of current witness can be a claim about the bounded verification interval without inventing a cause.

```text
SILENCE != TAMPERING
```

### 5.6 Evidence state / access / custody

No schema change: donor already separates `evidence_state` and `access_state` in canonical claims.

Richer custody risk remains representable with `RECORD`, control/custody claims and retained relations; full donor custody detail remains a full-candidate obligation.

### 5.7 Target boundary

No `TARGET_BOUNDARY` node.

Represent the target effect as `STATE`/`FUTURE_PATH`/claim as appropriate; the boundary observation/model through `CLOCK`, `MEASURE`, `CLAIM`, `DESIGNATION`, `BOUNDS` and provenance; capability/route context through retained route/control/dependency structure.

A target boundary is a qualified comparison condition, not an ontological thing that must exist in every scene.

### 5.8 Execution feasibility / shared capacity

No `RESOURCE`, `QUEUE`, `LOCK`, `CAPACITY` or `SCHEDULER` primitive.

When shared execution constraints matter, represent the actual domain object if already in the scene (`ENTITY`, `ROUTE`, `POLICY`, `CARRIER`, etc.) and use `DEPENDS_ON`, `COUPLES`, `CONTROLS`, `CONSTRAINS` plus evidence claims.

A domain scheduler/queue model may supply timing evidence without becoming TRACE vocabulary.

### 5.9 Future-path correspondence

No `CORRESPONDS_TO` relation.

Use retained `PERSISTS_AS` only when a supported claim establishes correspondence at the resolution relevant to the downstream preserved/lost/opened/closed claim.

```text
PERSISTS_AS edge label != correspondence evidence
SAME_PATH_LABEL != SAME_TRAJECTORY
```

If correspondence is unresolved, do not emit `PERSISTS_AS` merely because identifiers match.

---

## 6. The `E_prec` seam — precedence without a new relation

The semantic spine uses a process abstraction:

```text
G_window(q,l,o,c,g,u) = (V, E_prec)
```

`E_prec` is **not** proposed as a canonical TRACE relation type.

It is a derived timing/process view over supported claims that one represented stage/event cannot satisfy the relevant process timing before another stage/event or condition.

Canonical graph evidence may establish such ordering through different retained mechanisms:

```text
B DEPENDS_ON A
POLICY CONSTRAINS B until A
STATE/TRANSITION structure makes B reachable only after A
ROUTE/CONTROL condition prevents B before A
explicit RELATIONAL claim supplies the ordering with provenance/time/scope
```

The derived process view may normalize those heterogeneous mechanisms into an ordering edge for critical-path/process analysis **without writing `PRECEDES` back into the canonical schema**.

```text
DERIVED_PRECEDENCE != NEW_CANONICAL_RELATION
ORDERING_VIEW != CAUSAL_DEPENDENCY
```

This distinction matters because two events can be ordered for procedural or physical reasons without asserting that one causes the other.

If a worked case later shows that the ordering cannot be reconstructed/audited from retained claims without material ambiguity, revisit whether a canonical relation or profile field is earned. Do not add it pre-emptively.

---

## 7. Immediate schema attack targets

Hold this no-schema-change decision if any one lands:

1. a v0.6 semantic distinction cannot be serialized/audited without inventing an overloaded retained relation;
2. derived `E_prec` destroys the mechanism/source of ordering so thoroughly that a false timing conclusion becomes licensed;
3. `PERSISTS_AS` cannot carry path correspondence without conflating identity with materially comparable continuation;
4. currentness dependencies cannot be represented without making every claim a graph node or hiding dependencies in prose;
5. access/custody repair requires a new state beyond the donor `A/X/P/N` space for a load-bearing case rather than richer record/custody claims;
6. firing semantics require schema mutation rather than operator/checker behavior.

Preferred repair remains profile/derived/operator logic before universal vocabulary expansion.

---

## 8. Full-candidate assembly consequence

The next full TRACE candidate should begin from the **released v0.2.7 canonical schema**, not from the compressed spine text as if it were a replacement schema.

Then integrate v0.6 semantics as use rules / qualified derived views / tightened claim ceilings over retained objects.

```text
SPINE != SCHEMA
SEMANTIC_REPAIR != VOCABULARY_REVISION
NO_SCHEMA_CHANGE != NO_VERSION_CHANGE
```

Before any replacement claim, mechanically compare exact donor and candidate node/relation/evidence/access/claim-kind vocabularies and preserve a zero-loss report.

---

## 9. Disposition

```text
SCHEMA DELTA v0.1: ZERO-VOCABULARY-CHANGE CANDIDATE
NEW PRIMITIVE: NO
NEW RELATION: NO
NEXT: IMMEDIATE REPRESENTABILITY ATTACK + MECHANICAL VOCABULARY NO-LOSS CHECK
```

No merge/release/canon follows from this object.