# TRACE v0.3.0 full candidate v0.1 — coherence attack v0.1

**Date:** 2026-08-25  
**Target:** `PROJECT/TRACE_FORMAL_SEED_v0_3_0_FULL_WORKING_CANDIDATE_v0_1.md`  
**Target SHA-256:** `0da980f51c16508c3420ed05eec7b9f767d73856516cab46b65b4bb6a7719b17`  
**Status:** MATERIAL NARROW FINDING / REPAIR REQUIRED  
**Claim ceiling:** self-attack evidence only; not validation, release, canon, authority, permission or clearance.

## Finding F01 — stale local validator ancestry prose

The deterministic full compiler correctly emitted a v0.3.0 embedded minimum validator, while the explanatory prose immediately above that validator remained donor-local v0.2.7 text:

```text
The v0.2.7 identifier records a narrow documentary, serialization-profile,
and worked-transfer repair while the embedded minimum-schema shape remains
identical to v0.2.6 after version normalization.

A v0.2.6 packet is not silently relabelled as v0.2.7.
```

That prose was correct in the released v0.2.7 donor. It is stale when carried unchanged into a v0.3.0 full working candidate whose local schema block is now identified as `TRACE-GRAPH-0.3.0` / `trace_version: 0.3.0`.

The rebuilt [21] document-control section already states the correct ancestry:

```text
v0.3.0 full working candidate
  generated from released v0.2.7
minimum schema changes version identity only
released v0.2.7 remains the released baseline
```

Therefore this is a propagation/coherence omission, not a new semantic root or schema change.

## Required repair

At the local [14.4] minimum-validator boundary, state the current relation explicitly:

```text
v0.3.0 candidate identifier -> generated full working candidate from released v0.2.7
minimum-schema normalized structure -> identical to released v0.2.7 donor
v0.2.7 packet != silently relabelled v0.3.0 packet
```

Retain the validator ceiling: version identity and schema compatibility do not establish semantic binding, world correctness, authority, permission, clearance, target discovery, route execution, brake effectiveness or correction.

## Preserve

```text
DETERMINISTIC_BUILD_PASS != COHERENCE_ESTABLISHED
CURRENT_SCHEMA_ID != CURRENT_SURROUNDING_PROSE
VERSION_NORMALIZED_EQUALITY != PACKET_IDENTITY
STRUCTURAL_COMPATIBILITY != SEMANTIC_IDENTITY
DONOR_TEXT_VALID_IN_DONOR != DONOR_TEXT_VALID_AT_NEW_USE_SITE
```

## Disposition

Narrow compiler repair required. Do not erase the v0.1 generated candidate or rewrite this finding as if the first full build had been semantically clean.
