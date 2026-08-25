# TRACE v0.3.0 — FULL-CANDIDATE TRANSFORMATION MANIFEST v0.2

**Status:** COMPILER-READY WORKING MANIFEST — NOT GENERATED FULL CANDIDATE — NOT VALIDATION — NOT RELEASE/CANON  
**Supersedes for current assembly:** `TRACE_v0_3_0_FULL_CANDIDATE_TRANSFORMATION_MANIFEST_v0_1.md`  
**Preserves:** v0.1 as historical compiler blueprint and evidence of the pre-ingress omission.

## Current inputs

```text
released donor:
  TRACE_FORMAL_SEED_v0_2_7.md
  source SHA-256 de21182f42228a0104181fb24f245c652c3150853e14172c4174be4bb9ef03ab

semantic overlay:
  PROJECT/TRACE_v0_3_0_SPINE_CANDIDATE_v0_11.md
  semantic commit 41fafe81a681cdc6514efc13524bae6ea6d6af8d
  blob 1ae5e8b8640b9506db585599a6cae5192087d870

minimum schema:
  PROJECT/TRACE_v0_3_0_MINIMUM_SCHEMA_CANDIDATE_v0_1.json
  version identity only; normalized shape equals donor

section address map:
  PROJECT/TRACE_v0_2_7_SECTION_MANIFEST_v0_1.json
  status PASS
  headings 145 = 22 level-1 + 88 level-2 + 35 level-3
```

```text
BRANCH_HEAD != SEMANTIC_OBJECT
SPINE != FULL_CANDIDATE
DONOR_RECOVERY != NEW_PRIMITIVE
```

---

# Transform-class disposition

The v0.1 transform classes remain in force except where this file tightens them.

Separately specified and attacked:

```text
T_CLOCK_ROUTE       CLEAR_WITH_RESIDUAL_LIMITS
T_CLAIM_EVIDENCE    CLEAR_WITH_RESIDUAL_LIMITS
```

Remaining class contract:

`PROJECT/TRACE_v0_3_0_REMAINING_TRANSFORM_CLASSES_v0_1.md`

Bounded grouped attack:

`falsification/TRACE_v0_3_0_REMAINING_TRANSFORM_CLASSES_ATTACK_v0_1.md`

Current grouped disposition:

```text
T_SELECTION_ATTRIBUTION   CLEAR_WITH_RESIDUAL_LIMITS
T_ROUTE_REFUSABILITY      CLEAR_WITH_RESIDUAL_LIMITS
T_SCOPE_AGGREGATION       CLEAR_WITH_RESIDUAL_LIMITS
T_FUTURE_CORRESPONDENCE   CLEAR_WITH_RESIDUAL_LIMITS
T_RECORD_RESIDUE          CLEAR_WITH_RESIDUAL_LIMITS
T_MEASURE_ADVANTAGE       CLEAR_WITH_RESIDUAL_LIMITS
T_OPERATOR_CHECKER        CLEAR_WITH_RESIDUAL_LIMITS
T_PACKET_BINDING          CLEAR_WITH_RESIDUAL_LIMITS
T_WORKED_CASES            CLEAR_WITH_RESIDUAL_LIMITS
T_RECEIVER_PROFILE        CLEAR_WITH_RESIDUAL_LIMITS
T_CONNECTED_BRAKE         CLEAR_WITH_RESIDUAL_LIMITS
T_INVARIANT_MISUSE        CLEAR_WITH_RESIDUAL_LIMITS
T_SURVIVAL_KERNEL         CLEAR_WITH_RESIDUAL_LIMITS at contract level
T_DOCUMENT_CONTROL        CLEAR_WITH_RESIDUAL_LIMITS at contract level
```

No class is validated by this label.

---

# NEW REQUIRED CLASS — T_INGRESS_ADMISSION

v0.1 omitted a failure location upstream of formed-map firing.

Repair object:

`PROJECT/TRACE_v0_3_0_FULL_CANDIDATE_INGRESS_ADMISSION_REPAIR_v0_1.md`

Disposition:

```text
ADMISSION / REPRESENTATION-CONSTITUTION PHENOMENON: REAL
NEW ROOT: NO
NEW PRIMITIVE: NO
NEW RELATION: NO
TRANSFORM CLASS REQUIRED: YES
STATUS: CLEAR_WITH_RESIDUAL_LIMITS in immediate C1-C8 attack
```

The compiler must preserve the distinction between:

```text
NEVER_ADMITTED
ADMITTED_ALTERED
```

as failure locations, not canonical statuses.

Required non-entailments include:

```text
TRIGGER_SUCCESS != REPRESENTATION_COMPLETE
CHECK_OVER_DECLARED_DEPENDENCIES != CHECK_FOR_UNDECLARED_DEPENDENCIES
MAP_FORMATION != REASONING_OVER_THE_MAP
VALID_WITHIN_REPRESENTATION != REPRESENTATION_ADEQUATE_FOR_USE
REPRESENTED_USE != OPERATIVE_USE
SOURCE_POINTER_PRESENT != REPRESENTATION_FIDELITY_ESTABLISHED
VERBATIM_TEXT != SPEECH_ACT_PRESERVED
SIGNAL_RECEIVED != MAP_ADOPTED
SUPPLIED_PREMISE != OBSERVED_WORLD
RETAINED_PREMISE != CURRENT_MEASUREMENT
PROVENANCE != AUTHORITY_TO_ADOPT
```

The class uses existing WORLD / SCENE / MAP / APERTURE / TARGET-SET / CLAIM / provenance / receiver-integration machinery. It must not add `ADMISSION`, `SPEECH_ACT`, `WITNESS`, `PROCESS`, or `PRECEDES` to canonical vocabulary.

Required propagation surfaces:

```text
[5] aperture / target-set representation formation
[13] operator ordering / map-formation challenge
[14.1] checker-external binding/use rules
[15.2.1] target-set worked transfer or another existing donor case
[19] v0.3 supplemental misuse/invariant block
[20] survival-kernel propagation
```

---

# Exact compiler discipline

Every mutating transform is bound at runtime to the released donor section manifest.

For each source heading touched:

```text
1. locate exact heading in donor section manifest
2. recompute section span SHA-256 from donor bytes
3. require equality with manifest SHA-256
4. require exact anchor count
5. apply named mutation only
6. record changed source heading + mutation id in build report
```

Fail closed:

```text
DONOR_SOURCE_SHA_MISMATCH -> FAIL
DONOR_SECTION_SHA_MISMATCH -> FAIL
ANCHOR_COUNT != EXPECTED -> FAIL
UNDECLARED_MUTATION -> FAIL
I01_I60_DONOR_ORDER_LOST -> FAIL
MINIMUM_SCHEMA_SHAPE_DRIFT -> FAIL
MISSING_REQUIRED_PROPAGATION -> FAIL
STALE_RELEASE_WORDING_IN_WORKING_CANDIDATE -> FAIL
```

No fuzzy matching.

---

# Current compiler readiness

```text
DONOR IDENTITY:               FROZEN
SECTION ADDRESS MANIFEST:     PASS
MINIMUM SCHEMA:               PASS / VERSION-ONLY
SEMANTIC SPINE:               v0.11 / ATTACK OBJECT
INVARIANT DONOR-LOSS GATE:    CLEAR_WITH_RESIDUAL_LIMITS
WORKED-CASE INVENTORY:        READY
T_CLOCK_ROUTE:                ATTACKED
T_CLAIM_EVIDENCE:             ATTACKED
T_INGRESS_ADMISSION:          ATTACKED IMMEDIATE C1-C8
REMAINING TRANSFORM CLASSES:  ATTACKED GROUPED
FULL COMPILER:                NEXT
FULL GENERATED CANDIDATE:     NOT YET
```

The next legitimate object is the deterministic full compiler. A compiler run proves only that the declared transformations were applied reproducibly; it does not validate the resulting theory.
