# TRACE v0.3.0 — OUTWARD POOL INTAKE — SC-NHTSA-SGO v0.1

**Status:** EXECUTED SOURCE-FAMILY INTAKE — WORKING EVIDENCE — NOT CASE ANALYSIS — NOT VALIDATION  
**Date:** 2026-08-27  
**Adapter:** `PROJECT/TRACE_v0_3_0_OUTWARD_EXECUTION_ADAPTER_MANIFEST_v0_1.md`  
**Protocol:** frozen `PROJECT/TRACE_v0_3_0_OUTWARD_EVALUATION_PROTOCOL_v0_5_EXPANSION.md`  
**Collection:** `SC-NHTSA-SGO` — NHTSA Standing General Order crash-reporting archive  
**Frozen start:** `c828ef2b -> day 308 -> 2022-11-04 -> November 2022 bucket`  
**Primary order:** occurrence month ascending; within month `AUTOMATION_CLASS|OFFICIAL_REPORT_ID` lexical ascending

## 0. Carrier identity gate

The study aperture received one upload bundle:

```text
UPLOAD_NHTSA_SGO_TO_CHAT.zip
bytes: 927669
sha256: a8f9b3152bc265f94aae1a1794fbfed2097392e5b40d2d3a66705cff235d6e89
```

The ZIP contained exactly the two predeclared official archive CSVs plus the transport receipt. Before CSV parsing, Framework independently hashed the extracted member bytes.

| automation class | filename | official URL | retrieved UTC in receipt | bytes | SHA-256 | identity |
|---|---|---|---|---:|---|---|
| ADS | `SGO-2021-01_Incident_Reports_ADS.csv` | https://static.nhtsa.gov/odi/ffdd/sgo-2021-01/Archive-2021-2025/SGO-2021-01_Incident_Reports_ADS.csv | `2026-08-25T22:54:41.3205463Z` | 3943732 | `cb2b38a21e2ce5c2337dfa0cffe8d6fce5e422cf93fe4c78942eec5cf72f41ba` | MATCH |
| LEVEL_2_ADAS | `SGO-2021-01_Incident_Reports_ADAS.csv` | https://static.nhtsa.gov/odi/ffdd/sgo-2021-01/Archive-2021-2025/SGO-2021-01_Incident_Reports_ADAS.csv | `2026-08-25T22:54:43.6884384Z` | 4092534 | `99579d4c9add8f2fd0adfcff9199210fee8aaf9cbaf64347fd7adbb4446b6f5e` | MATCH |

Receipt member:

```text
NHTSA_SGO_TRANSPORT_RECEIPT.json
bytes: 1730
sha256: 0302a1a41724aef28a997866fc7f5eb35016510551ab2a2ba03ae3e329193c21
shape: JSON array with one record per automation class
```

Each receipt record states:

```text
transport = direct official download by bounded human-triggered PowerShell carrier operation
content_inspected_before_hash = false
provenance_ceiling = reported official URL + locally observed bytes/hash; no official cryptographic hash assumed
```

The uploaded CSV byte counts and SHA-256 values exactly match their receipt records. Raw carrier bytes are frozen for this study aperture.

```text
HUMAN_REPORTED_HASH -> APERTURE_OBSERVED_HASH_MATCH
CARRIER_IDENTITY_MATCH != SOURCE_COMPLETENESS
CARRIER_IDENTITY_MATCH != CAUSAL_ATTRIBUTION
```

## 1. Parse/schema observation after identity freeze

Raw bytes were not rewritten or normalized.

```text
ADS decode used: utf-8-sig
LEVEL_2_ADAS decode used: Windows-1252 / cp1252
ADS logical data rows: 2295
LEVEL_2_ADAS logical data rows: 4027
columns in each carrier: 137
combined logical rows: 6322
distinct AUTOMATION_CLASS|Report ID identities: 4589
```

The Level-2 archive is not valid UTF-8 at the raw-byte level; decoding it as Windows-1252 is a parsing observation only. It does not alter the frozen carrier.

Fields used for identity/ordering only:

```text
occurrence month/year       = Incident Date (MON-YYYY)
occurrence-unknown guard    = Incident Date - Unknown
official report identity    = AUTOMATION_CLASS + Report ID
report revision             = Report Version
submission clock            = Report Submission Date
cross-report incident link  = Same Incident ID
cross-report vehicle link   = Same Vehicle ID
```

`Report Month` / `Report Year` are not the occurrence-order field.

Official NHTSA documentation states that:
- each submitted report receives a unique `Report ID`;
- updates retain that `Report ID` and receive a new `Report Version`;
- `Same Incident ID` is intended to show when multiple reports refer to the same incident;
- duplicate/relationship fields can themselves be incomplete or inaccurate.

For this intake, all versions are preserved. For one report identity, the highest numeric `Report Version` is the representative row used for selector fields. If the latest representative row lacks a usable stable incident relation, the case relation is `DUPLICATE_CASE_RELATION_UNKNOWN`; operator judgement does not manufacture independence.

## 2. Frozen selector execution

After report-version collapse, the November 2022 bucket contains **70 report identities**:

```text
ADS: 13
LEVEL_2_ADAS: 57
```

Because the frozen tie-break is lexical `AUTOMATION_CLASS|OFFICIAL_REPORT_ID`, `ADS` sorts before `LEVEL_2_ADAS`. Therefore the first five distinct incident clusters reached by the selector are all sourced from the ADS carrier. This is a selector consequence, not an importance, prevalence, safety, or risk judgement.

### Considered report identities in exact scan order

| # | report identity | latest version | Same Incident ID | disposition |
|---:|---|---:|---|---|
| 1 | `ADS|1306-4389` | 2 | `03ad388e6676c05` | SELECT — new incident cluster |
| 2 | `ADS|30270-4482` | 1 | `439627d9d2569d4` | SELECT — new incident cluster |
| 3 | `ADS|30270-4484` | 1 | `420fb566c542133` | SELECT — new incident cluster |
| 4 | `ADS|30270-4485` | 1 | `5628c7d47cd45e9` | SELECT — new incident cluster |
| 5 | `ADS|30413-4170` | 1 | `03ad388e6676c05` | CLUSTER — same incident as earlier selected cluster |
| 6 | `ADS|30531-4492` | 2 | `439627d9d2569d4` | CLUSTER — same incident as earlier selected cluster |
| 7 | `ADS|30531-4494` | 1 | `5628c7d47cd45e9` | CLUSTER — same incident as earlier selected cluster |
| 8 | `ADS|30571-4399` | 2 | `84d4fa517d86789` | SELECT — new incident cluster |

Quota reached at report identity 8.

Later November report identities were **not considered for new-case selection**. A full-carrier relationship-completion pass was then used only to attach any other report identity carrying one of the five already-selected `Same Incident ID` values. This found one later constituent, `ADS|855-4460`, for selected cluster `84d4fa517d86789`.

```text
QUOTA_REACHED != LATER_ROWS_ERASED
RELATIONSHIP_COMPLETION != NEW_CASE_SELECTION
```

## 3. Five frozen NHTSA pool entries

### NHTSA-01

```text
SOURCE_COLLECTION_ID: SC-NHTSA-SGO
SOURCE_NATIVE_ID: SAME_INCIDENT_ID|03ad388e6676c05
CASE_ID: c30fbf38dc1c4bb958c69d1aea5153d5d311732ddaa6d98373f44b34c93fa4b0
SOURCE_DATE: 2022-11
TYPE: SGO reported-incident cluster
AUTOMATION_CLASS_AT_SELECTOR: ADS
```

Official relationship key: `Same Incident ID = 03ad388e6676c05`.

Constituent report identities preserved from the frozen carriers:

- `ADS|1306-4389` — versions `1,2`; latest `2`; reporting entity `Toyota Motor Engineering & Manufacturing`; Incident Date `NOV-2022`.
- `ADS|30413-4170` — version `1`; latest `1`; reporting entity `May Mobility`; Incident Date `NOV-2022`.

Narrative fields are non-empty in the latest constituent rows, but **no narrative content was used or interpreted for selection**.

### NHTSA-02

```text
SOURCE_COLLECTION_ID: SC-NHTSA-SGO
SOURCE_NATIVE_ID: SAME_INCIDENT_ID|439627d9d2569d4
CASE_ID: d0a5b777dcd0c9594dcfd24673495b4fb18def3da7ab87cb14a36c2f8d26dba9
SOURCE_DATE: 2022-11
TYPE: SGO reported-incident cluster
AUTOMATION_CLASS_AT_SELECTOR: ADS
```

Official relationship key: `Same Incident ID = 439627d9d2569d4`.

Constituent report identities preserved from the frozen carriers:

- `ADS|30270-4482` — version `1`; latest `1`; reporting entity `Waymo LLC`; Incident Date `NOV-2022`.
- `ADS|30531-4492` — versions `1,2`; latest `2`; reporting entity `Transdev Alternative Services`; Incident Date `NOV-2022`.

Narrative fields are non-empty in the latest constituent rows, but **no narrative content was used or interpreted for selection**.

### NHTSA-03

```text
SOURCE_COLLECTION_ID: SC-NHTSA-SGO
SOURCE_NATIVE_ID: SAME_INCIDENT_ID|420fb566c542133
CASE_ID: 0d0b8ea4ae3cad32e15246ef5d33cc8715c5fcc8df24215e9c2cee4ab1230f64
SOURCE_DATE: 2022-11
TYPE: SGO reported-incident cluster
AUTOMATION_CLASS_AT_SELECTOR: ADS
```

Official relationship key: `Same Incident ID = 420fb566c542133`.

Constituent report identity preserved from the frozen carrier:

- `ADS|30270-4484` — version `1`; latest `1`; reporting entity `Waymo LLC`; Incident Date `NOV-2022`.

Narrative field is non-empty in the latest row, but **no narrative content was used or interpreted for selection**.

### NHTSA-04

```text
SOURCE_COLLECTION_ID: SC-NHTSA-SGO
SOURCE_NATIVE_ID: SAME_INCIDENT_ID|5628c7d47cd45e9
CASE_ID: 811f32e7904c2962f2ce4dd8e4bb39835b2eb5ad8b79b23c1afdf731adec3b2f
SOURCE_DATE: 2022-11
TYPE: SGO reported-incident cluster
AUTOMATION_CLASS_AT_SELECTOR: ADS
```

Official relationship key: `Same Incident ID = 5628c7d47cd45e9`.

Constituent report identities preserved from the frozen carriers:

- `ADS|30270-4485` — version `1`; latest `1`; reporting entity `Waymo LLC`; Incident Date `NOV-2022`.
- `ADS|30531-4494` — version `1`; latest `1`; reporting entity `Transdev Alternative Services`; Incident Date `NOV-2022`.

Narrative fields are non-empty in the latest constituent rows, but **no narrative content was used or interpreted for selection**.

### NHTSA-05

```text
SOURCE_COLLECTION_ID: SC-NHTSA-SGO
SOURCE_NATIVE_ID: SAME_INCIDENT_ID|84d4fa517d86789
CASE_ID: 98523b61c535cd054bd25b6f41fe063daa97556bc1271b0f8a8096091b055099
SOURCE_DATE: 2022-11
TYPE: SGO reported-incident cluster
AUTOMATION_CLASS_AT_SELECTOR: ADS
```

Official relationship key: `Same Incident ID = 84d4fa517d86789`.

Constituent report identities preserved from the frozen carriers:

- `ADS|30571-4399` — versions `1,2`; latest `2`; reporting entity `NVIDIA CORP`; Incident Date `NOV-2022`.
- `ADS|855-4460` — version `1`; latest `1`; reporting entity `Mercedes-Benz USA, LLC`; Incident Date `NOV-2022`.

Narrative fields are non-empty in the latest constituent rows, but **no narrative content was used or interpreted for selection**.

## 4. Case-identity rule

The pool-wide case-id convention used by the existing RAIB/PAC entries is:

```text
CASE_ID = SHA256(SOURCE_COLLECTION_ID + "\n" + SOURCE_NATIVE_ID)
```

For NHTSA, the real-world case unit is the mechanically clustered incident, so:

```text
SOURCE_NATIVE_ID = SAME_INCIDENT_ID|<official Same Incident ID>
```

Report IDs and versions remain preserved as constituent evidence and are not promoted back into independent cases.

## 5. Source-aperture limits

```text
IN_SGO_DATA != AUTOMATION_CAUSED_CRASH
REPORTED_CRASH_COUNT != NORMALIZED_RISK
NOT_REPORTED != DID_NOT_OCCUR
REPORT_RECORD != NECESSARILY_DISTINCT_REAL_WORLD_CRASH
SAME_INCIDENT_ID != INFALLIBLE_GROUND_TRUTH
ADS_SELECTED_FIRST != ADS_MORE_IMPORTANT
OFFICIAL_ARCHIVE != COMPLETE_AFFECTED_PARTY_EXPERIENCE
```

Some selected latest report rows state `Automation System Engaged? = Unknown, see Narrative`. That field was not used to reinterpret automation class or causal responsibility. The source family is the predeclared archived ADS / Level-2 SGO carrier, and this intake freezes reported incident identities only.

No TRACE-assisted reading of the substantive crash narratives has occurred in this intake.

## 6. Disposition

```text
SC-RAIB       5
SC-PAC        5
SC-EPA-FOIA2  5
SC-NHTSA-SGO  5
TOTAL        20 / 20
```

This completes source-family intake. It does not select the later efficacy cases and does not validate TRACE.
