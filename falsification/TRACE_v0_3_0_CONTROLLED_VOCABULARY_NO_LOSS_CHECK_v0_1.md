# TRACE v0.3.0 — CONTROLLED VOCABULARY NO-LOSS CHECK v0.1

**Status:** DETERMINISTIC CONTROLLED-VOCABULARY PASS — FULL SCHEMA NO-LOSS NOT YET CHECKABLE  
**Donor:** released TRACE v0.2.7 `TRACE_FORMAL_SEED_v0_2_7.md`  
**Candidate declaration:** `PROJECT/TRACE_v0_3_0_SCHEMA_DELTA_CANDIDATE_v0_1.md`  
**Scope:** node types, relation types, evidence states, access states, claim kinds; port/full-packet shape checked only for whether a candidate comparison object exists

---

## 1. Method

For each controlled vocabulary explicitly reproduced by the schema-delta candidate:

1. read the ordered donor token list from released v0.2.7;
2. read the ordered candidate carry-forward token list;
3. compare count;
4. compare exact ordered sequence;
5. compare set difference in both directions;
6. check duplicate tokens;
7. compute SHA-256 over the UTF-8 normalized representation `TOKEN\nTOKEN\n...`.

This is a vocabulary comparison only. It does not establish semantic equivalence, serializer equivalence or world validity.

---

## 2. Results

| Vocabulary | Donor count | Candidate count | Ordered equality | Missing | Added | Duplicates | Normalized SHA-256 |
|---|---:|---:|---|---|---|---|---|
| NODE_TYPE | 27 | 27 | YES | none | none | none | `380ab1fb808db15864db4bfdbff052dddee0c8c6e70eb258f7810ef046e6f20a` |
| RELATION_TYPE | 46 | 46 | YES | none | none | none | `74f9bd5797ec903abfad390da32a3d71abab15d7fcee3dcee6430023417dfb65` |
| EVIDENCE_STATE | 5 | 5 | YES | none | none | none | `9900c4411fda620eef81dcae5465f9eb1ce26d667e986c8c13ce08c3f41c29d4` |
| ACCESS_STATE | 4 | 4 | YES | none | none | none | `93d3bca9d70e3905ae07c4849bead4458b2deb0ad5c29af3a2161187406b3253` |
| CLAIM_KIND | 7 | 7 | YES | none | none | none | `395bcdf073cb26592fce6ac5f877b0598fe7d359588d0f345c641712fe60bc74` |

Exact donor/candidate controlled lists therefore match for this scope.

```text
CONTROLLED_VOCABULARY_MISSING = 0
CONTROLLED_VOCABULARY_ADDED = 0
CONTROLLED_VOCABULARY_REORDERED = 0
CONTROLLED_VOCABULARY_DUPLICATES = 0
```

---

## 3. What this does establish

Within the five compared controlled vocabularies, the current v0.3 schema-delta proposal is literally a zero-vocabulary-change proposal relative to released v0.2.7.

No current semantic repair has yet forced a new universal:

```text
node type
relation type
evidence state
access state
claim kind
```

This supports—but does not prove—the current disposition that v0.3 semantic changes can be carried as tightened use rules, claim bindings, derived views and profiles over the donor schema.

---

## 4. What this does NOT establish

There is not yet an assembled v0.3 canonical serialization/schema object to compare field-for-field with the donor.

Released v0.2.7 canonical graph includes top-level structure such as:

```text
schema
trace_version
reading_id
nodes
edges
claims
ports
limits
available_transition_refs
institutional_use
anti_clearance
```

and exposes six port roles:

```text
designation
measure
selector
carrier
enforcement
brake
```

The schema-delta candidate says `NEW PORT: NONE`, but it does not itself instantiate a replacement `PORTS`/`LIMITS`/packet schema. Therefore:

```text
NO_NEW_PORT != ALL_DONOR_PORTS_MECHANICALLY_PRESERVED
VOCABULARY_EQUAL != SERIALIZATION_EQUAL
CONTROLLED_LISTS_EQUAL != FULL_SCHEMA_EQUAL
```

Full-schema zero-loss remains **UNRESOLVED / NOT YET CHECKABLE** until a candidate serialization object exists.

---

## 5. Additional donor boundaries still requiring explicit comparison

Before any full replacement claim, mechanically compare at least:

```text
canonical top-level packet fields
NODE and EDGE required fields
CLAIM required fields
PORTS structure
LIMITS structure
institutional use state
claim ceiling / anti-clearance fields
existing-object target-set serialization profile
validator-enforced references and enums
```

This is separate from semantic donor-capability accounting such as nested boundaries, recursive zoom, worked transfers and misuse coverage.

---

## 6. Precedence delta consequence

The acyclicity/provenance repairs do not alter the controlled vocabulary result.

Derived `E_prec` remains outside canonical relation vocabulary and must preserve canonical supporting claim/mechanism references. Donor acyclicity is restored as a derived process rule, not a new relation.

```text
DERIVED_VIEW_FIELD != CANONICAL_RELATION_TYPE
```

---

## 7. Disposition

```text
CONTROLLED VOCABULARY NO-LOSS: PASS
FULL SCHEMA NO-LOSS: NOT YET CHECKABLE
NEW NODE/RELATION/EVIDENCE/ACCESS/CLAIM-KIND TERM EARNED: NO
NEXT: BUILD A MINIMAL FULL-CANDIDATE SERIALIZATION BOUNDARY FROM v0.2.7, THEN DIFF IT MECHANICALLY
```

`PASS_WITHIN_DECLARED_COMPARISON != FULL_SCHEMA_EQUIVALENCE`.
