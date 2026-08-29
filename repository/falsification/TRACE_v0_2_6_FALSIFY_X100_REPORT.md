# TRACE v0.2.6 — falsify x100 and drift audit

**Audit ID:** `TRACE-V026-FALSIFY-X100`  
**Target:** released `TRACE_FORMAL_SEED_v0_2_6.md`  
**Released main:** `fb50464c219eb6b8cc8b6ea9a0790f183238c0eb`  
**Released object blob:** `5e50886f20bceef63be90456cae7f7f895bcd6`  
**Predecessor blob:** `6ebc97274eb07c27979491820793989ba918a102`  
**Exact audit head:** `a21b277944b2fac2a623e0d2be4cebdce3112c3d`  
**Hosted run:** `30960448135` / run #5  
**Artifact:** `8912715016`  
**Artifact ZIP digest:** `sha256:992e2b2df72c71ceb847dada23b9d9ec5d4fbaedb9ec8e11604ec2dcec921f9e`  
**Extracted JSON SHA-256:** `80f27f4ca8c6c73f57d3f162a2ad98a57583867dba3c2707979b739403c9ab0d`  

## Verdict

```text
NARROW
```

The released v0.2.6 object resisted falsification of its version identity, deterministic compilation boundary, minimum-schema shape claim, target-set-aperture core distinction, and authority/value ceilings.

It did not resist the audit as a complete single-file, partial-ingestion-tolerant release. The admitted repair is present in the main body but is not propagated through several declared compression, document-control, serialization, example, and front-door surfaces.

This is not a core collapse and does not justify reverting to v0.2.5. It is a bounded errata requirement.

## Executed probe set

```text
probe_count:                       100
resisted_count:                     85
finding_count:                      15
material_finding_count:             13
already_bounded_limitation_count:    1
transfer_gap_count:                  1
mutation_probe_count:               20
mutation_detector_failure_count:     0
verdict:                         NARROW
```

Probe families:

```text
release identity and front door                 10
version, schema, and compilation containment    20
target-set and coverage semantics               20
authority and value-layer ceilings              15
partial ingestion and document control          15
hostile mutation resistance                     20
```

A green workflow means the 100 probes executed, the report closed, and all 20 hostile mutation detectors worked. It does not mean TRACE passed every probe or is validated.

## What resisted falsification

### Release and object identity

The release declaration exists, names the active formal baseline, binds the compiled source commit and exact object blob, and preserves v0.2.5 as the predecessor. The computed Git blob matched the declared blob.

### Version and schema containment

The v0.2.6 header, graph identifier, trace version, schema `$id`, schema title, pseudocode initializer, and validator target are synchronized. No stale `TRACE-GRAPH-0.2.5` identifier remains.

After version normalization, the embedded minimum-schema shape is identical to v0.2.5. Node vocabulary, edge vocabulary, and required top-level properties did not expand.

### Deterministic scope

An independent invocation of `tools/compile_trace_v026.py` reproduced the released object. An independently implemented reverse transform removed the six admitted insertion families and reconstructed normalized v0.2.5. This found no unexplained semantic drift outside the declared compilation patch.

### Target-set repair

The target-set aperture records:

```text
source
targets
selection basis
known omitted categories
alternatives
control
uncertainty
```

The following ceilings are present and survived hostile removal tests:

```text
TARGET_SET != WORLD_SCOPE
TARGET_NOT_SELECTED != TARGET_DOES_NOT_EXIST
COVERAGE_OF_SELECTED_TARGETS != COMPLETE_DISCOVERY
OPERATOR_TARGET_SET != AUTHORITATIVE_TARGET_SET
DIVERGENT_READINGS != AUTHORITY
```

Coverage is explicitly relative to a declared target-set aperture and comparison basis. Completeness beyond that aperture remains `UNKNOWN`.

### Authority and value boundary

The admitted patch did not create a selector, permission rule, value rule, moral authority, or affirmative instruction to proceed. Normative claims remain external. Release still withholds canon, validation, authority, permission, and clearance.

## Material findings

### F1 — partial-ingestion drift

**Probe IDs:** `P02`, `P03`, `P04`, `P05`, `P11`, `P15`  
**Classification:** `DOCUMENTARY_DRIFT`  
**Affected sections:** `[1]`, `[19]`, `[20]`  

The v0.2.6 repair is introduced at `[5.3.1]`, `[6.1.1]`, `[10.4]`, `[13.2]`, and `[14]`, but it does not survive the document's own compression surfaces:

- the middle-out seed does not state that target selection is aperture-bearing;
- the numbered invariant list omits the target-set/world-scope and target-set/coverage non-entailments;
- the survival kernel identifies itself as v0.2.6 but omits target-set aperture and aperture-relative coverage.

This matters because the file claims partial-ingestion tolerance. A receiver given the survival kernel or early seed can reconstruct a v0.2.6-labelled object without the distinction that justified v0.2.6.

**Smallest justified repair:** propagate the admitted repair into the middle-out seed, numbered invariants, and survival kernel without adding a primitive, schema field, selector, or value rule.

### F2 — stale revision declaration

**Probe IDs:** `P06`, `P07`  
**Classification:** `DOCUMENTARY_DRIFT`  
**Affected section:** `[21.1] Revision declaration`  

`[21.1]` describes the earlier transition-discipline pass, including the bounded `discipline` object and its pilot history. It does not describe the target-set-aperture repair that distinguishes v0.2.6 from v0.2.5.

This is direct version-documentation drift inside the released formal object.

**Smallest justified repair:** rewrite `[21.1]` as a succession declaration: preserve the v0.2.5 transition-discipline change, then state the v0.2.6 target-set-aperture and aperture-relative accounting/coverage repair, with unchanged schema shape and checker-external enforcement.

### F3 — unresolved register omission

**Probe ID:** `P08`  
**Classification:** `DOCUMENTARY_DRIFT`  
**Affected section:** `[21.4] Unresolved`  

The unresolved register says that a symmetric transition set can omit a material option, but it does not state the corresponding v0.2.6 limitation: a selected target set can omit materially affected scopes while coverage remains complete only relative to that selected aperture.

**Smallest justified repair:** add the target-set incompleteness and target-selection authority limitations to `[21.4]`.

### F4 — serialization under-specification

**Probe ID:** `T19`  
**Classification:** `SERIALIZATION_DRIFT`  
**Affected sections:** `[5.3.1]`, `[14]`  

The prose defines a target-set aperture and lists recordable references, but the canonical packet provides no standard target-set-aperture block or named serialization profile. Existing objects can represent the distinction, but two implementations may invent incompatible local conventions while both claim v0.2.6 conformance.

This is not evidence that a new primitive or required minimum-schema field is necessary. It is evidence that the existing-object representation needs one canonical profile or example.

**Smallest justified repair:** add a non-required canonical serialization profile using existing `APERTURE`, `CLAIM`, `RECORD`, `ENTITY`, `ROUTE`, `TRANSITION`, and edge vocabulary. Preserve minimum-schema shape.

### F5 — minimum validator does not enforce the repair

**Probe ID:** `T20`  
**Classification:** `ALREADY_BOUNDED_LIMITATION`  

The minimum schema contains no target-set references and cannot enforce the v0.2.6 semantic repair.

This is already stated honestly in `[14.1]` and `[14.4]`. It is not a newly discovered contradiction and does not justify schema growth by itself.

**Disposition:** no minimum-schema change. Keep the enforcement checker-external unless applied evidence demonstrates that a non-required serialization profile is insufficient.

### F6 — worked-transfer gap

**Probe ID:** `P09`  
**Classification:** `TRANSFER_GAP`  
**Affected section:** `[15] Worked transformations`  

No worked transformation demonstrates two materially different target-set apertures over the same scene or shows how the existing graph objects serialize their disagreement.

**Smallest justified repair:** add one compact constructed example. Do not treat it as validation or world evidence.

### F7 — front-door drift

**Probe IDs:** `R10`, `P13`, `P14`  
**Classification:** `FRONT_DOOR_DRIFT`  
**Affected objects:** `README.md`, `TRACE.pdf`  

The repository `Start here` list places `TRACE.pdf` before the released formal seed. `TRACE.pdf` was last updated as a July v0.5 carrier candidate and does not identify the released v0.2.6 baseline. The README does not label it as older.

A new reader can therefore enter through a stale carrier before reaching the active formal baseline.

**Smallest justified repair:** put `TRACE_FORMAL_SEED_v0_2_6.md` first and explicitly label `TRACE.pdf` as the older v0.5 human-facing carrier candidate until a deliberately rebuilt PDF exists. Do not silently overwrite the PDF without a separate rendered review.

## Consolidated disposition

```text
core rollback:                         NO
release withdrawal:                    NO
new primitive:                         NO
minimum-schema growth:                 NO
new selector or value rule:            NO
narrow formal-document errata:        YES
canonical existing-object profile:    YES
constructed worked example:           YES
README front-door correction:         YES
new PDF required immediately:          NO
independent CC review:             PENDING
```

The released v0.2.6 baseline should remain active while carrying an open narrow errata state. The repair must be version-honest: either an explicit v0.2.6 errata object with unchanged formal identity, or a successor version if any machine contract changes. The audit does not pre-decide that release-form question.

## Tool and evidence record

- GitHub repository and exact-blob inspection;
- deterministic compiler invocation in hosted CI;
- independent reverse transform against v0.2.5;
- minimum-schema structural comparison;
- 20 hostile mutation probes;
- GitHub Actions exact-head execution;
- preserved workflow artifact and digests;
- independent Claude/CC hostile-review dispatch through COM issue #26;
- attempted second local container execution, which was blocked by the container's lack of network access and therefore was not counted as evidence.

## Claim boundary

```text
AUDIT_EXECUTION != VALIDATION
85 RESISTED PROBES != WORLD VALIDITY
15 FINDINGS != CORE COLLAPSE
GREEN WORKFLOW != CLEARANCE
NARROW != RELEASE FAILURE
```
