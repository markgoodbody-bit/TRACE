# TRACE v0.3.0 — OUTWARD POOL INTAKE — SC-RAIB v0.1

**Status:** EXECUTED COLLECTION INTAKE — NOT CASE SELECTION — NOT VALIDATION  
**Date:** 2026-08-25  
**Manifest:** `PROJECT/TRACE_v0_3_0_SOURCE_COLLECTION_MANIFEST_v0_2.md` (frozen)  
**Collection:** `SC-RAIB` — UK Rail Accident Investigation Branch  
**Frozen start:** 2022-10-11  
**Order:** occurrence date ascending, then report identifier ascending  
**Filter:** completed investigation reports only

## Execution note

The 2022 RAIB annual-report investigation table was used as the canonical in-window ordering witness. It explicitly marks safety digests with `SD`; non-`SD` entries are full investigations. The scan begins after the frozen start day, runs forward to 31 December, then wraps to 1 January until five eligible full investigations are collected.

No item was included or excluded for expected TRACE usefulness.

## Considered items in exact scan order

| # | Occurrence date | Source-native identity | Type | Eligibility | Reason / source pointer |
|---|---|---|---|---|---|
| 1 | 2022-10-19 | Report 10/2023 — Petteril Bridge Junction | full investigation | ELIGIBLE | completed investigation report; public report page and PDF available |
| 2 | 2022-10-26 | Report 11/2023 — South Wingfield | full investigation | ELIGIBLE | completed investigation report; public report/press-release evidence available |
| 3 | 2022-11-15 | Safety digest 02/2023 — Bulkington | safety digest | INELIGIBLE | frozen collection filter is completed investigation reports only |
| 4 | 2022-01-14 | Safety digest 02/2022 — Uphill Junction | safety digest | INELIGIBLE | frozen collection filter is completed investigation reports only |
| 5 | 2022-01-14 | Safety digest 01/2022 — Wood Street | safety digest | INELIGIBLE | frozen collection filter is completed investigation reports only |
| 6 | 2022-01-30 | Report 07/2023 — Haddiscoe | full investigation | ELIGIBLE | completed investigation report; public report page and PDF available |
| 7 | 2022-02-01 | Report 02/2023 — West Worthing | full investigation | ELIGIBLE | completed investigation report; public report page and PDF available |
| 8 | 2022-04-15 | Report 05/2023 — Chalfont & Latimer | full investigation | ELIGIBLE | completed investigation report; public report page and PDF available |

Quota reached at item 8. Later 2022 items were not considered for this collection in this run.

## Five eligible pool entries

### RAIB-1 — Petteril Bridge Junction

```text
SOURCE_COLLECTION_ID: SC-RAIB
SOURCE_NATIVE_ID: Report 10/2023
CASE_ID: 7921a96b9ff7622ed84c5864aacb2202f432a29b7671b3bf642c7ff471f308f3
SOURCE_DATE: 2022-10-19
TYPE: full investigation
TITLE: Freight train derailment at Petteril Bridge Junction
CANONICAL_URL: https://www.gov.uk/raib-reports/report-10-slash-2023-freight-train-derailment-at-petteril-bridge-junction
RETRIEVED: 2026-08-25
```

Bounded source witness: five tank wagons derailed near Carlisle after a wheelset stopped rotating and slid for a long distance; the condition was not identified by signallers, the driver, or an engineered system before derailment. RAIB issued recommendations/learning points. Preserve source conclusions as RAIB findings, not world-complete truth.

### RAIB-2 — South Wingfield

```text
SOURCE_COLLECTION_ID: SC-RAIB
SOURCE_NATIVE_ID: Report 11/2023
CASE_ID: 72d91043b10df9fe6f6e9c2fb6ac4b9ab5064d008ecf4f4fbd455d51df045e31
SOURCE_DATE: 2022-10-26
TYPE: full investigation
TITLE: Two trains in the same signal section at South Wingfield
CANONICAL_URL: https://www.gov.uk/raib-reports/report-11-slash-2023-two-trains-in-the-same-signal-section-at-south-wingfield
RETRIEVED: 2026-08-25
```

Bounded source witness: a wrong-side signalling failure followed reconnection work; a train passed a red signal after the preceding signal had displayed green and a following train later entered the same signal section. RAIB investigated testing process, responsibilities, competence, workload/time pressure and management assurance.

### RAIB-3 — Haddiscoe

```text
SOURCE_COLLECTION_ID: SC-RAIB
SOURCE_NATIVE_ID: Report 07/2023
CASE_ID: eb267e8b3e88f07c8a2cbf476c770acb8e29bdb2d6bc3c582abce0f2f7e2c2a7
SOURCE_DATE: 2022-01-30
TYPE: full investigation
TITLE: Embankment washout under a passenger train at Haddiscoe
CANONICAL_URL: https://www.gov.uk/raib-reports/report-07-slash-2023-embankment-washout-under-a-passenger-train-at-haddiscoe
RETRIEVED: 2026-08-25
```

Bounded source witness: a passenger train entered a section whose supporting formation was being washed out during unusually high water; flood-warning/risk-management and third-party flood-defence interactions were material to RAIB's findings. Five passengers were evacuated and nobody was injured.

### RAIB-4 — West Worthing

```text
SOURCE_COLLECTION_ID: SC-RAIB
SOURCE_NATIVE_ID: Report 02/2023
CASE_ID: d53834bdc3f48daf0551a84de9fcc9508a7d9b7b67ccd90c4d85b39fcb9ba94b
SOURCE_DATE: 2022-02-01
TYPE: full investigation
TITLE: Train driver struck by a train near West Worthing Middle Siding
CANONICAL_URL: https://www.gov.uk/raib-reports/report-02-slash-2023-train-driver-struck-by-a-train-near-west-worthing-middle-siding
RETRIEVED: 2026-08-25
```

Bounded source witness: a train driver left a stationary train and was fatally struck by another train. RAIB could not establish why the driver left the cab and retained uncertainty about the immediate personal reason; recommendations/learning points covered toilets, CCTV, protection before leaving cabs, PPE and trackside hazards.

### RAIB-5 — Chalfont & Latimer

```text
SOURCE_COLLECTION_ID: SC-RAIB
SOURCE_NATIVE_ID: Report 05/2023
CASE_ID: e5bc8b58f95a9e2c585e6db9bfd3953abdaa786aed47f67aa6533169222d4089
SOURCE_DATE: 2022-04-15
TYPE: full investigation
TITLE: Track worker struck by train near Chalfont & Latimer station
CANONICAL_URL: https://www.gov.uk/raib-reports/report-05-slash-2023-track-worker-struck-by-train-near-chalfont-and-latimer-station
RETRIEVED: 2026-08-25
```

Bounded source witness: a lookout was struck and injured while working on a line open to traffic. RAIB found location/briefing issues and broader inadequacy in processes for managing track-worker risk; its report also records earlier identified risk-assessment/process defects that had not all been corrected by the time of the accident.

## Source-aperture limits

```text
RAIB_INVESTIGATION != WORLD
RAIB_SELECTED_EVENT != ALL_RAIL_EVENT
RAIB_CAUSAL_FINDING != COMPLETE_CAUSAL_HISTORY
PUBLIC_REPORT != COMPLETE_AFFECTED_PARTY_EXPERIENCE
```

This collection contributes five deterministic pool entries only. No TRACE reading or case ranking has yet been performed.
