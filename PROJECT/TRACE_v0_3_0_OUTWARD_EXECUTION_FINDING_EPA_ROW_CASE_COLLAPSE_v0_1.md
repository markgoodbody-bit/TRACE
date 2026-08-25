# TRACE v0.3.0 — OUTWARD EXECUTION FINDING — EPA ROW != CASE v0.1

**Status:** MATERIAL EXECUTION FINDING — NARROW ADAPTER REPAIR REQUIRED — NO EPA POOL ENTRY ACCEPTED FROM DUPLICATE ROWS  
**Date:** 2026-08-25

## Finding

During SC-EPA-FOIA2 deterministic intake, the official bulk action ledger exposed two 2022-05-03 rows at the Libby Asbestos Site:

```text
EPA ID: MT0009083840
Site ID: 0801744
Action: Explanation Of Significant Differences (ESD)
Row A: REMEDIAL SITEWIDE | ACT Seq 4 | 05/03/22
Row B: TROY              | ACT Seq 5 | 05/03/22
```

EPA's official ESD document is one decision document covering Libby and Troy Residential and Commercial Properties, Operable Units 4 and 7, approved May 3, 2022.

Therefore:

```text
BULK_ACTION_ROW != NECESSARILY_DISTINCT_DECISION
DISTINCT_ACT_SEQ != DISTINCT_REAL_WORLD_CASE
TWO_OU_ROWS != TWO_INDEPENDENT_DECISIONS
```

Counting both rows as independent primary real-world cases would allow database normalization to manufacture case multiplicity.

## Disposition

The two rows are preserved separately as source records but must form one primary case cluster for this run because official decision-document evidence establishes that they belong to the same ESD decision object.

No general claim is made that same-site/same-date rows always share one document.

```text
SAME_SITE + SAME_DATE != SAME_DECISION_ESTABLISHED
OFFICIAL_SHARED_DECISION_DOCUMENT -> CLUSTER_FOR_PRIMARY_CASE_UNIT
ROW_PRESERVED + CASE_CLUSTERED != ROW_ERASED
```

## Repair pressure

SC-EPA-FOIA2 needs the same distinction already earned for NHTSA:

```text
REPORT/ROW RECORD != NECESSARILY_DISTINCT REAL-WORLD CASE
```

Primary case-unit formation must be fail-closed where a stable official relation is absent. Operator intuition is not a duplicate resolver.

## Ceiling

This is a study-adapter finding, not a new TRACE primitive/root and not evidence for or against TRACE efficacy.
