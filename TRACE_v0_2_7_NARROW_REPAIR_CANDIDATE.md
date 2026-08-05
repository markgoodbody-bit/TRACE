# TRACE v0.2.7 narrow repair candidate

**Candidate ID:** `TRACE-V027-NARROW-REPAIR-001`  
**Base:** released TRACE v0.2.6 at `d166a97d0a3d4e4e5bf0f6cd2395f15bd5f16869`  
**Source audit:** `TRACE-V026-FALSIFY-X100`  
**Status:** compiled working candidate  

```text
NOT_RELEASED
NOT_CANON
NOT_VALIDATED
NOT_AUTHORITY
NOT_PERMISSION
NOT_CLEARANCE
```

## Repair scope

The v0.2.6 x100 audit returned `NARROW`: 85 of 100 probes resisted, 15 findings remained, 13 were material narrow findings, one was an already-bounded minimum-validator limitation, and one was a worked-transfer gap.

v0.2.7 is limited to the evidenced drift:

1. propagate target-set aperture and aperture-relative coverage into the middle-out seed;
2. add the corresponding numbered invariants;
3. repair the survival kernel;
4. replace the stale revision declaration with an explicit v0.2.6 → v0.2.7 succession declaration;
5. add target-set incompleteness and target-selection authority limits to the unresolved register;
6. add one non-required canonical serialization profile using existing graph objects;
7. add one constructed divergent-target-aperture worked transfer;
8. repair README front-door ordering and label `TRACE.pdf` as the older v0.5 carrier candidate.

## Locked non-growth boundary

```text
new primitive:                    NO
new node type:                    NO
new edge type:                    NO
new port:                         NO
new required packet property:     NO
minimum-schema shape change:      NO
new selector:                     NO
new value rule:                   NO
new authority rule:               NO
PDF replacement in this change:   NO
```

The canonical serialization profile is guidance over existing `APERTURE`, `CLAIM`, `RECORD`, `ENTITY`, `ROUTE`, `TRANSITION`, and existing edge vocabulary. It does not establish target discovery, completeness, governing authority, diligence, permission, or world correspondence.

## Build contract

`tools/compile_trace_v027.py` deterministically compiles `TRACE_FORMAL_SEED_v0_2_7.md` from the released v0.2.6 seed and verifies:

- synchronized v0.2.7 machine identifiers;
- unchanged minimum-schema shape after version normalization;
- unchanged node and edge vocabularies;
- unchanged required packet properties;
- exact presence of the bounded repair surfaces;
- absence of stale v0.2.6 machine identifiers.

The committed v0.2.7 seed must remain byte-identical to compiler output.

## Review boundary

The independent Claude/CC review of the v0.2.6 x100 audit was still pending when Mark instructed Framework to keep going. Audit evidence was merged under that explicit human override; no CC clearance or agreement is inferred.

v0.2.7 requires exact-head regression and hostile review before any release decision.
