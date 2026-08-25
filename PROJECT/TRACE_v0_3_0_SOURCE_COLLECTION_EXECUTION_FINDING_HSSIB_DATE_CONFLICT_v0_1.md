# TRACE v0.3.0 — SOURCE COLLECTION EXECUTION FINDING — HSSIB PUBLICATION-DATE CONFLICT v0.1

**Status:** MATERIAL EXECUTION FINDING — MANIFEST REOPEN REQUIRED — NO HSSIB CASES SELECTED  
**Date:** 2026-08-25  
**Frozen parent:** `PROJECT/TRACE_v0_3_0_SOURCE_COLLECTION_MANIFEST_v0_2.md` + freeze record

## Finding

The frozen HSSIB profile specifies:

```text
Date: report publication date
Order: publication date ascending, then canonical investigation URL ascending
```

During first deterministic intake, HSSIB's current public legacy corpus exposed internally conflicting official publication metadata for the same investigation object.

Concrete specimen:

```text
investigation: Weight-based medication errors in children
investigation overview timeline: Final report published — 3 February 2022
migrated investigation-report page: Date Published — 13/04/2021
```

The current manifest does not define which official field wins when the source itself supplies conflicting values for the ordering variable.

Other HSSIB collection cards also expose month labels that do not reliably match exact dates on investigation/report pages. This means the issue is not safely reducible to one obvious typo without a declared source-resolution rule.

## Why material

The HSSIB frozen start is 2022-12-19 and the scan wraps to 1 January. The first five eligible cases therefore depend directly on exact publication ordering.

Choosing whichever official date seems more plausible after seeing an item would make the operator part of the selector:

```text
OFFICIAL_FIELD_A != OFFICIAL_FIELD_B
SOURCE_CONFLICT != OPERATOR_PERMISSION_TO_CHOOSE
ORDER_DECLARED != ORDER_REPRODUCIBLE
DETERMINISTIC_RULE + AMBIGUOUS_INPUT != DETERMINISTIC_SELECTION
```

This is an execution defect in the manifest contract, not evidence against HSSIB as a source family and not a TRACE case result.

## Immediate disposition

```text
SC-HSSIB INTAKE: HOLD
HSSIB ELIGIBLE CASE COUNT: 0 frozen/accepted so far
CASE SELECTION: NOT STARTED
MANIFEST v0.2: PRESERVE FROZEN ANCESTRY
MANIFEST REOPEN: YES / NARROW
```

Do not silently reinterpret the old freeze.

## Smallest repair to attack

Add a collection-agnostic conflict rule before HSSIB intake resumes:

1. if the frozen source-native ordering field has one unambiguous official value, use it;
2. if multiple official values conflict, apply a predeclared field-precedence rule grounded in what each field semantically claims, not which date yields a desirable case;
3. if semantic precedence cannot be established without item-specific judgement, mark the item `ORDER_DATE_DISPUTED` and do not let it silently determine pool order;
4. preserve every conflicting value and source pointer;
5. the same rule must apply symmetrically to all six collections if analogous source-native conflicts appear.

Potential HSSIB-specific evidence for the repair may distinguish an explicit event labelled `Final report published` from generic migrated-page metadata, but that precedence must be justified and frozen before continuing the scan.

## Ceiling

```text
SOURCE_METADATA_CONFLICT != WORLD_EVENT_CONFLICT
MIGRATION_ANOMALY_POSSIBLE != MIGRATION_CAUSE_ESTABLISHED
ONE_CONFLICT != WHOLE_COLLECTION_UNUSABLE
REPAIRING_ORDER_RULE != CHOOSING_CASE
```
