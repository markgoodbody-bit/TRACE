# TRACE v0.2.6 transition candidate

Status: **WORKING CANDIDATE**

Base: `TRACE_FORMAL_SEED_v0_2_5.md`

Base repository commit: `983aeec18d41935ec59dd84c70bc6b0dcd49e287`

Release status: **NOT RELEASED**

Canon status: **NOT CANON**

Validation status: **NOT VALIDATED**

## Purpose

This candidate converts the completed v0.2.5 checker-external evidence sequence into a bounded disposition for TRACE v0.2.6.

It answers two separate questions:

1. Which findings expose a defect or missing distinction in the formal seed?
2. Which findings must remain checker-external, implementation-level, human-facing, or explicitly unresolved?

The candidate does not copy every checker result into TRACE. It proposes the smallest formal-semantic repair supported by the evidence.

## Current disposition

One repair family crosses the formal-seed boundary:

> **Selection of the target set used for search, comparison, or coverage assessment is itself aperture-bearing, and any accounting or coverage result is relative to that declared aperture.**

TRACE v0.2.5 already represents apertures, blindspots, transition-set symmetry, layer handoff, routes, brakes, commitment receipts and anti-clearance limits. The new evidence does not justify new primitives for search coverage, authority legitimacy, contestability, brake effectiveness, or policy quality.

The v0.2.6 candidate therefore proposes:

- one explicit target-set-aperture rule using the existing `APERTURE`, `CLAIM`, `RECORD`, `ROUTE`, `TRANSITION`, and edge vocabulary;
- explicit anti-compression statements joining existing v0.2.5 distinctions;
- checker-external binding rules for transition accounting, target-relative coverage, authority handoff and contestability;
- no new node type;
- no new edge type;
- no new port;
- no new packet field;
- no new selector or moral authority;
- no automatic brake-effectiveness checker.

## Candidate package

- `01_DISPOSITION_MATRIX.md` — destination of each finding.
- `02_NARROW_FORMAL_PATCH.md` — exact semantic and identifier patch proposed for compilation into a full v0.2.6 seed.
- `03_REGRESSION_CONTRACT.md` — invariants and adversarial cases the compiled seed must preserve.
- `candidate_manifest.json` — machine-readable candidate state.
- `validate_candidate.py` — verifies the manifest, source anchors, version strategy and disposition closure.
- `test_validate_candidate.py` — negative and positive regressions for the transition package.

## Version posture

This is a **transition candidate**, not yet the compiled full formal seed.

The version strategy is fixed:

```text
formal seed: 0.2.6
packet schema: TRACE-GRAPH-0.2.6
minimum schema shape: unchanged from 0.2.5
```

At full compilation, update the formal seed title/version, canonical graph constants, embedded schema `$id` and title, pseudocode initialiser and validator target. No new required property or controlled vocabulary is added.

A v0.2.5 packet is not silently relabelled as v0.2.6. Compatibility is structural, but version identity remains explicit.

Checker-external rules remain outside the embedded minimum validator.

A version-label change is not evidence that the system is validated or operationally effective.

## Strongest candidate claim

> TRACE v0.2.6 should make target selection visible as part of the aperture and should state more explicitly that transition accounting, search coverage, authority handoff and contestability remain relative to supplied evidence and declared comparison envelopes.

It should not pretend to discover the unseen world, legitimate authority, select values, or prove correction.

## Stop condition

Do not expand this candidate with another formal object merely because another limitation can be named.

Expansion requires one of:

- a v0.2.5 scene that cannot represent a materially required distinction with existing objects;
- a concrete false-complete result inside the candidate's claimed boundary;
- repeated applied evidence that the proposed target-set-aperture rule is insufficient;
- or a minimum-schema defect that cannot be repaired checker-externally.
