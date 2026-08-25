# TRACE v0.3.0 — OUTWARD POOL INTAKE — EPA FOIA-002 v0.1

**Status:** EXECUTED SOURCE-FAMILY INTAKE — WORKING EVIDENCE — NOT CASE ANALYSIS — NOT VALIDATION  
**Date:** 2026-08-25  
**Source family:** `SC-EPA-FOIA2`  
**Parent adapter:** `PROJECT/TRACE_v0_3_0_OUTWARD_EXECUTION_ADAPTER_MANIFEST_v0_1.md` plus frozen case-clustering repair  

## 0. Purpose

Record the deterministic EPA source-family intake after the frozen 2022 start point without selecting for expected TRACE value.

Frozen start:

```text
SC-EPA-FOIA2
start day 109
2022-04-19
quota: 5 distinct eligible decision cases
```

Primary source is EPA's SEMS Superfund Public User Database FOIA-002 carrier. Site/decision pages are secondary official pointers used only to confirm that each mechanically encountered ledger entry corresponds to a bounded public decision object.

```text
FOIA_ROW != WORLD_CASE
DATABASE_ROW != DECISION_DOCUMENT
ROW_CLUSTERING != ROW_ERASURE
```

## 1. Scan result

The first five distinct eligible decision cases at/after the frozen start are:

### EPA-01 — Milford Contaminated Aquifer

```text
date: 2022-04-20
site: MILFORD CONTAMINATED AQUIFER
site_id: 0507973
epa_id: OHSFN0507973
action: Record of Decision (ROD)
operable_unit: SEMS
act_seq: 1
status: Final
```

Official site material states the remedy was selected 20 April 2022 and describes groundwater treatment, monitoring, water-supply protections and institutional controls.

Primary identity:
`OHSFN0507973|0507973|1|Record of Decision (ROD)|SEMS`

### EPA-02 — Saltville Waste Disposal Ponds

```text
date: 2022-04-26
site: SALTVILLE WASTE DISPOSAL PONDS
site_id: 0302526
epa_id: VAD003127578
action: Explanation Of Significant Differences (ESD)
operable_unit: DISPOSAL PONDS
act_seq: 1
status: Final
```

Official EPA material states the April 2022 ESD modified the Pond 5 remedy, including cap extension, environmental covenant, operations/maintenance and long-term monitoring.

Primary identity:
`VAD003127578|0302526|1|Explanation Of Significant Differences (ESD)|DISPOSAL PONDS`

### EPA-03 — McGuire Air Force Base #1

```text
date: 2022-04-29
site: MCGUIRE AIR FORCE BASE #1
site_id: 0201162
epa_id: NJ0570024018
action: Record of Decision (ROD)
operable_unit: BFSA & FIRE TRAINING AREA
act_seq: 4
status: Final
```

Official EPA material states the OU4 ROD was signed 29 April 2022 and selected a remedy including natural source-zone depletion, LNAPL skimming/mass-removal optimization, monitoring and institutional/engineering controls.

Primary identity:
`NJ0570024018|0201162|4|Record of Decision (ROD)|BFSA & FIRE TRAINING AREA`

### EPA-04 — Libby Asbestos Site — OUs 4 and 7 decision cluster

FOIA-002 exposes two rows on the same date:

```text
row A:
  date: 2022-05-03
  site_id: 0801744
  epa_id: MT0009083840
  action: Explanation Of Significant Differences (ESD)
  operable_unit: REMEDIAL SITEWIDE
  act_seq: 4

row B:
  date: 2022-05-03
  site_id: 0801744
  epa_id: MT0009083840
  action: Explanation Of Significant Differences (ESD)
  operable_unit: TROY
  act_seq: 5
```

EPA's actual ESD is one decision document specific to OUs 4 and 7, covering Libby and Troy residential/commercial properties, parks and schools. Therefore the two ledger rows form **one primary case cluster**, not two independent cases.

Cluster identity:
`MT0009083840|0801744|ESD|2022-05-03|OU4+OU7`

Preserve both source rows as constituents.

### EPA-05 — Baghurst Drive

```text
date: 2022-05-18
site: BAGHURST DRIVE
site_id: 0306939
epa_id: PAN000306939
action: Record of Decision (ROD)
operable_unit: OU 01 (OU SPECIFIC)
act_seq: 1
status: Final
```

Official EPA material states the final remedy was selected 18 May 2022 for a VOC-contaminated groundwater plume and includes in-situ thermal remediation, chemical oxidation, groundwater/vapor monitoring and institutional controls.

Primary identity:
`PAN000306939|0306939|1|Record of Decision (ROD)|OU 01 (OU SPECIFIC)`

## 2. Selection discipline

No item above was retained or excluded because it appeared likely to help or hurt TRACE.

The Libby duplicate-row event triggered the previously preserved execution finding and case-clustering repair before the five-case quota was finalized.

```text
TWO_ROWS_SAME_DECISION != TWO_CASES
CLUSTERED_CASE != DATA_ROW_DELETED
```

## 3. Pool contribution

```text
EPA DISTINCT ELIGIBLE CASES: 5
RAIB DISTINCT ELIGIBLE CASES: 5
PAC DISTINCT ELIGIBLE CASES: 5
CURRENT REAL-WORLD POOL TOTAL: 15 / 20
```

NHTSA SGO remains the final mandatory source family. Its official ADS and Level-2 archive CSV bytes must be transported unchanged into the study aperture before deterministic incident intake can execute.

## 4. Limits carried forward

- EPA FOIA-002 is an official action/decision ledger, not the whole environmental history of a site.
- official source completeness does not establish affected-party completeness;
- one decision document can map to multiple database rows;
- `Actual Complete Date` is the frozen source-family ordering field, not a universal event clock;
- later source updates may change live site pages; the case identity and 2022 ordering evidence above remain the run's preserved intake record.

No TRACE-assisted analysis has yet been performed on these five cases.
