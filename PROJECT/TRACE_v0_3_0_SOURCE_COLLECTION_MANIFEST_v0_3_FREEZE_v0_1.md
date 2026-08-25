# TRACE v0.3.0 — SOURCE COLLECTION MANIFEST v0.3 FREEZE v0.1

**Status:** FROZEN NARROW SUCCESSOR FOR THIS OUTWARD-EVALUATION CYCLE — NOT VALIDATION — NOT CASE SELECTION  
**Date:** 2026-08-25

## Frozen composite

Execution now uses:

```text
base manifest: PROJECT/TRACE_v0_3_0_SOURCE_COLLECTION_MANIFEST_v0_2.md
base blob: 1aa136cbe0cb40fe78c3b853a9726c1056b53128
narrow successor: PROJECT/TRACE_v0_3_0_SOURCE_COLLECTION_MANIFEST_v0_3.md
successor blob: 26b87b10baf2e02490149205606497b423bf2a75
```

v0.3 changes only source-native ordering conflict handling. All collection IDs, source families, 2022 window, start positions, quotas, filters and prior ceilings remain inherited from frozen v0.2.

## Execution ancestry

HSSIB first intake exposed an internally conflicting official publication date. Intake stopped before HSSIB cases were accepted.

Finding:
`PROJECT/TRACE_v0_3_0_SOURCE_COLLECTION_EXECUTION_FINDING_HSSIB_DATE_CONFLICT_v0_1.md`

Attack:
`PROJECT/TRACE_v0_3_0_SOURCE_COLLECTION_MANIFEST_v0_3_ATTACK_v0_1.md`

```text
attacks: 15
pre-freeze finding: compatible coarse/precise dates were initially over-classified as conflict
repair: added semantic/interval compatibility rule
material defects surviving repaired target: 0
verdict: CLEAR_WITH_RESIDUAL_LIMITS
```

## Frozen rule

```text
compatible coarse + precise official values -> use most precise compatible value
incompatible values for same frozen ordering field -> ORDER_VALUE_DISPUTED
conflict across intake window boundary -> TEMPORAL_ELIGIBILITY_DISPUTED
disputed item -> preserve outside primary selector until resolved
collection enumeration not reproducible -> COLLECTION_ENUMERATION_HOLD
```

No operator may choose a conflicting value because it appears more plausible or produces a desirable case.

## Next boundary

Resume collection intake under the composite v0.2 + v0.3 contract.

RAIB intake already completed remains standing absent a concrete occurrence-date conflict.

HSSIB intake must restart from its frozen start/wrap path; internally incompatible publication metadata is carried as disputed rather than silently resolved.
