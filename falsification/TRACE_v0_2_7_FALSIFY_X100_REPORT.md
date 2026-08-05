# TRACE v0.2.7 — falsify x100 regression and drift closure

**Audit ID:** `TRACE-V027-FALSIFY-X100`  
**Candidate:** `TRACE_FORMAL_SEED_v0_2_7.md`  
**Candidate build base:** released v0.2.6 at `d166a97d0a3d4e4e5bf0f6cd2395f15bd5f16869`  
**Exact audited head:** `53318b50d8faa1f3ea0915c9043824d5ad30ddce`  
**Hosted run:** `30963692069` / run #2  
**Artifact:** `8913881593`  
**Artifact ZIP digest:** `sha256:27e529f78c02333fb82b6dde7f19c51a24bade3bc3f67642644b9012e33dbf0a`  
**v0.2.7 JSON digest:** `sha256:dac7678604314cb677c819a7e67c721bf5527c9750cec020caf08fd46865b5f6`  
**v0.2.6 comparison JSON digest:** `sha256:8c550315538d0c8937aadcaf3d9aa2d60cfa2efccf9d407b2a06d5c99de7b278`  

## Verdict

```text
CLEAR_WITH_RESIDUAL_LIMITS
```

```text
probe_count:                       100
resisted_count:                    100
finding_count:                       0
mutation_probe_count:               20
mutation_detector_failure_count:     0
```

The candidate resisted the declared v0.2.7 regression and drift-closure suite. This means the bounded repair is present at the tested surfaces, deterministic compilation is preserved, the minimum-schema shape and vocabulary remain unchanged, the hostile mutations were detected, and the repository front-door correction is represented.

It does not establish validation, world correspondence, decision advantage, complete target discovery, legitimate authority, operational effectiveness, permission, or clearance.

## Deterministic build result

At the audited head:

```text
base lines:                         5,591
compiled lines:                     5,759
base SHA-256:     5a26462f613d9051d8f165dc7b4bb8778dd79ac4c4836144ac94622802f1ddaa
compiled SHA-256: de21182f42228a0104181fb24f245c652c3150853e14172c4174be4bb9ef03ab
schema shape identical:             true
node vocabulary unchanged:          true
edge vocabulary unchanged:          true
required packet properties unchanged:true
stale v0.2.6 machine identifiers:   0
compiler status:                    PASS
```

The committed `TRACE_FORMAL_SEED_v0_2_7.md` was byte-identical to deterministic compiler output.

## Probe families

```text
identity, determinism and schema containment     20
propagation and documentary drift closure        20
existing-object serialization profile            15
constructed worked transfer                      10
authority, value and claim ceilings               15
hostile mutation resistance                       20
```

## Drift closures that resisted

### Partial ingestion

The target-set repair now survives:

- the middle-out seed;
- numbered invariants `I57`–`I60`;
- the survival kernel;
- the revision declaration;
- the unresolved register.

### Serialization

The candidate includes one canonical, non-required target-set-aperture profile using existing graph objects and edge vocabulary. The audit confirmed that no `TARGET_SET` node type, required packet field, primitive, selector, or value rule was introduced.

The following ceilings remain explicit:

```text
TARGET_SET_PROFILE_PRESENT != TARGET_SET_COMPLETE
PROFILE_CONFORMANCE != TARGET_DISCOVERY
ALTERNATIVE_TARGET_SET_RECORDED != ALTERNATIVE_TARGET_SET_AUTHORITATIVE
```

### Worked transfer

One constructed service-migration scene preserves two divergent target-set apertures, relative coverage claims, unknown world completeness, and the prohibition on silent union or inferred authority.

The scene is a construction test, not empirical validation.

### Front door

The repository README now places the active released v0.2.6 formal baseline before `TRACE.pdf` and labels the PDF as the older v0.5 human-facing carrier candidate. The PDF itself was not rebuilt or silently overwritten.

## Hostile mutation closure

All 20 mutations were detected, including:

- removal of the v0.2.7 identity;
- removal of middle-out, invariant, survival, revision, unresolved, serialization, and worked-transfer repairs;
- reintroduction of stale v0.2.6 machine identity;
- node-vocabulary or required-property growth;
- conversion of profile visibility into completeness;
- README front-door reversal;
- removal of the stale-PDF warning;
- removal of the `NOT_VALIDATED` boundary.

The first audit execution exposed four instrument defects: one brittle value-layer token and three ineffective mutation detectors. Those defects were repaired and the full suite was rerun at a new exact head. They were not counted as candidate failures.

## Preserved v0.2.6 comparison

The workflow reran the existing v0.2.6 audit unchanged. It remained `NARROW`, with 87 resisted probes and 13 findings after the README correction. This is expected: the old suite continues to inspect the released v0.2.6 object, while v0.2.7 is a distinct successor candidate carrying the repair.

The v0.2.6 formal object remains byte-preserved. No errata rewrite or silent relabelling occurred.

## Residual limits

```text
AUDIT_EXECUTION_NOT_VALIDATION
MINIMUM_VALIDATOR_REMAINS_SHAPE_AND_VOCABULARY_ONLY
TARGET_DISCOVERY_AND_AUTHORITY_REMAIN_CHECKER_EXTERNAL
TRACE_PDF_REMAINS_OLDER_CARRIER_BUT_IS_NOW_LABELLED
CONSTRUCTED_TRANSFER_NOT_WORLD_EVIDENCE
```

## Disposition

```text
candidate rollback:                 NO
new primitive or schema growth:     NO
additional documentary repair:      NOT SUPPORTED BY THIS SUITE
exact-head hostile review:          REQUIRED BEFORE INTEGRATION
release decision:                   NOT YET
v0.2.6 active baseline:             PRESERVED
```

## Claim boundary

```text
100/100 RESISTED != WORLD VALIDITY
GREEN WORKFLOW != RELEASE
GREEN WORKFLOW != CANON
GREEN WORKFLOW != AUTHORITY
GREEN WORKFLOW != PERMISSION
GREEN WORKFLOW != CLEARANCE
CLEAR_WITH_RESIDUAL_LIMITS != VALIDATED
```
