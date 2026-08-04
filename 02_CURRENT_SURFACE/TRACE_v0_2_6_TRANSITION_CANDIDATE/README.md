# TRACE v0.2.6 transition candidate

Status: **MERGED TRANSITION PACKAGE / COMPILED WORKING SEED CANDIDATE**

Base: `TRACE_FORMAL_SEED_v0_2_5.md`

Transition-package merge commit: `e310b9e0314213524183d1ffe83e14f2d4f0745c`

Compiled output: `TRACE_FORMAL_SEED_v0_2_6.md`

Release status: **NOT RELEASED**

Canon status: **NOT CANON**

Validation status: **NOT VALIDATED**

## Purpose

This package converts the completed v0.2.5 checker-external evidence sequence into a bounded disposition and compilation contract for TRACE v0.2.6.

It answers two separate questions:

1. Which findings expose a defect or missing distinction in the formal seed?
2. Which findings must remain checker-external, implementation-level, human-facing, or explicitly unresolved?

The package does not copy every checker result into TRACE. It admits the smallest formal-semantic repair supported by the evidence.

## Current disposition

One repair family crosses the formal-seed boundary:

> **Selection of the target set used for search, comparison, or coverage assessment is itself aperture-bearing, and any accounting or coverage result is relative to that declared aperture.**

TRACE v0.2.5 already represents apertures, blindspots, transition-set symmetry, layer handoff, routes, brakes, commitment receipts and anti-clearance limits. The repair is not justified merely by repeating that general principle. `01_DISPOSITION_MATRIX.md` carries the explicit containment test: v0.2.5 does not require an inspectable target-set source, selected targets, known omitted categories, alternatives, control/custody, uncertainty, or distinct target-set provenance for a material coverage claim.

The v0.2.6 compilation therefore adds:

- one explicit target-set-aperture rule using the existing `APERTURE`, `CLAIM`, `RECORD`, `ROUTE`, `TRANSITION`, and edge vocabulary;
- explicit anti-compression statements joining existing v0.2.5 distinctions;
- checker-external binding rules for transition accounting, target-relative coverage, authority handoff and contestability;
- no new node type;
- no new edge type;
- no new port;
- no new packet field;
- no new selector or moral authority;
- no automatic brake-effectiveness checker.

## Package

- `01_DISPOSITION_MATRIX.md` — destination of each finding and the F03/F04 containment warrant.
- `02_NARROW_FORMAL_PATCH.md` — semantic and identifier patch compiled into the full v0.2.6 candidate.
- `03_REGRESSION_CONTRACT.md` — invariants and adversarial cases the compiled seed must preserve.
- `candidate_manifest.json` — machine-readable package state, scope, gates and normalized artefact digests.
- `validate_candidate.py` — compatibility filename for the transition-package integrity checker.
- `test_validate_candidate.py` — positive, negative and hostile package-integrity tests.
- `/tools/compile_trace_v026.py` — deterministic full-seed compiler and verifier.
- `/.github/workflows/trace-v026-full-seed.yml` — compilation and exact-output CI.
- `/TRACE_FORMAL_SEED_v0_2_6.md` — compiled single-file working candidate.

## Integrity-check scope

The executable transition-package check is deliberately narrower than semantic validation:

```text
check scope: PACKAGE_INTEGRITY_AND_DECLARED_CONTRACT_ONLY
green CI != semantic validity
green CI != adequacy of the formal argument
green CI != TRACE validation
```

It verifies:

- manifest closure and bounded destinations;
- source anchors in v0.2.5;
- synchronized version posture;
- normalized integrity digests for the patch, regression contract and disposition matrix;
- expected patch sections and R01-R12 / V26-A-H section closure;
- release gates and non-promotion boundaries.

The full-seed compiler separately verifies deterministic output, synchronized identifiers, required semantic insertions and exact embedded-schema shape equality after version normalization. Its hostile tests reject a gutted target-set repair, mixed identifiers and minimum-schema growth while permitting line-ending-only reflow.

These checks establish that CI is checking the reviewed package and deterministic compilation. They do not establish that the argument is true, sufficient in the world, operationally effective or validated.

## Version posture

The compiled working candidate uses:

```text
formal seed: 0.2.6
packet schema: TRACE-GRAPH-0.2.6
minimum schema shape: unchanged from 0.2.5
```

The full seed updates the title/version, canonical graph constants, embedded schema `$id` and title, pseudocode initialiser and validator target. It adds no required property or controlled vocabulary.

A v0.2.5 packet is not silently relabelled as v0.2.6. Compatibility is structural, but version identity remains explicit.

Checker-external rules remain outside the embedded minimum validator.

A version-label change is not evidence that the system is validated or operationally effective.

## Review provenance

Claude's hostile review of the transition package returned `NARROW`. The validator-vacuity finding and the missing F03/F04 containment warrant were accepted and repaired before the transition package merged.

A requested additional review of the repaired transition-package head was not received before Mark explicitly instructed Framework to proceed. That is recorded as a human-authority override of the additional wait, not as Claude clearance or agreement.

The compiled full seed still requires exact-head inspection before any release or canon decision.

## Strongest candidate claim

> TRACE v0.2.6 makes target selection visible as part of the aperture and states more explicitly that transition accounting, search coverage, authority handoff and contestability remain relative to supplied evidence and declared comparison envelopes.

It does not pretend to discover the unseen world, legitimate authority, select values, or prove correction.

## Stop condition

Do not expand this candidate with another formal object merely because another limitation can be named.

Expansion requires one of:

- a scene that cannot represent a materially required distinction with existing objects;
- a concrete false-complete result inside the candidate's claimed boundary;
- repeated applied evidence that the target-set-aperture rule is insufficient;
- or a minimum-schema defect that cannot be repaired checker-externally.
