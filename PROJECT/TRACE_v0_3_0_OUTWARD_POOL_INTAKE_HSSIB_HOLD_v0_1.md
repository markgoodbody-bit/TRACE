# TRACE v0.3.0 — OUTWARD POOL INTAKE — SC-HSSIB HOLD v0.1

**Status:** COLLECTION EXECUTION HOLD — PRIMARY POOL COUNT 0 — SOURCE FAMILY PRESERVED  
**Date:** 2026-08-25  
**Manifest:** frozen v0.2 + v0.3 conflict-handling successor  
**Collection:** `SC-HSSIB`

## Why intake is held

The HSSIB/legacy-HSIB public corpus repeatedly supplies incompatible official values for the frozen ordering concept `final report publication date`.

Observed examples include:

```text
Administering a wrong site nerve block
  investigation overview timeline: Final report published — 13 September 2018
  migrated report page: Date Published — 30/01/2022

Recognition of the acutely ill infant
  investigation overview timeline: Final report published — 9 December 2021
  migrated report page: Date Published — 16/03/2022

Weight-based medication errors in children
  investigation overview timeline: Final report published — 3 February 2022
  migrated report page: Date Published — 13/04/2021

Local integrated investigation pilot 2
  investigation overview timeline: Final report published — 20 January 2022
  migrated report page: Date Published — 22/03/2022
```

The conflicts move in both directions across the 2022 boundary and can change both temporal eligibility and scan order.

A repeated pattern suggests migration/content-history effects may exist, but the cause is not established and the frozen run does not authorise Framework to declare one official surface authoritative after seeing the cases.

```text
REPEATED_METADATA_CONFLICT != MIGRATION_CAUSE_ESTABLISHED
TIMELINE_LOOKS_BETTER != TIMELINE_AUTHORITY_ESTABLISHED_FOR_THIS_RUN
REPORT_PAGE_LOOKS_WRONG != OPERATOR_PERMISSION_TO_IGNORE
```

## Execution consequence

Under manifest v0.3:

```text
SC-HSSIB PRIMARY INTAKE: COLLECTION_ENUMERATION_HOLD
PRIMARY ELIGIBLE CASES ACCEPTED: 0
HSSIB MATERIAL ERASED: 0
```

No HSSIB item is allowed to enter the primary deterministic pool through operator judgement about which publication date is 'really' correct.

The source family remains part of the expansion corpus. Its publication-metadata conflict is itself valuable source-quality evidence and may justify a separately designed HSSIB/legacy-HSIB source profile later.

## Primary evaluation viability

The other five frozen source families can still produce a target of 25 eligible real-world pool entries, exceeding the protocol minimum of 20. HSSIB is therefore not replaced ad hoc merely to preserve the planned count.

```text
ONE_COLLECTION_HOLD != WHOLE_EVALUATION_HOLD
POOL_TARGET_REACHABLE != HSSIB_PROBLEM_SOLVED
NO_REPLACEMENT != NO_HEALTH_DOMAIN_EVER
```

The primary real-case selection proceeds only from source families whose frozen ordering contracts can be reproduced.

## Future source-family work

A future HSSIB source-family profile may test whether the overview `Timeline -> Final report published` field is consistently the authoritative original publication event across legacy migrations. That work must be independently specified and cannot retroactively rewrite which items entered this primary run.

Preserve all conflicting objects and values.
