# TRACE v0.3.0 — OUTWARD EXECUTION ADAPTER MANIFEST v0.1

**Status:** PRE-FREEZE SUCCESSOR STUDY ADAPTER — NOT CASE SELECTION — NOT VALIDATION  
**Date:** 2026-08-25  
**Trigger:** `PROJECT/TRACE_v0_3_0_SOURCE_COLLECTION_EXECUTION_READINESS_FINDING_v0_1.md`

## 0. Purpose

Repair the outward study's execution-layer assumption without erasing the original six-source attempt.

The primary pool for the successor execution uses four broad official source families whose enumeration route is declared **before** primary case selection:

```text
SC-RAIB
SC-PAC
SC-EPA-FOIA2
SC-NHTSA-SGO
```

Five eligible items per family yields a target 20-entry real-world pool spanning the four mandatory domains:

```text
infrastructure / safety / engineering
public administration / institutional review
ecological / environmental intervention
AI / software / automated control
```

The original SC-LGSCO, SC-FOS and SC-HSSIB attempts remain preserved as source/aperture evidence; they are not deleted or declared useless.

```text
SUCCESSOR_EXECUTION_SET != ORIGINAL_SET_NEVER_EXISTED
EXECUTION_HOLD != DOMAIN_ERASURE
ADDITIONAL_SOURCE_FAMILY != SILENT_REPLACEMENT
```

## 1. Common temporal and intake rule

Primary window remains calendar year 2022.

For each source family:

```text
START_HASH = SHA256(SOURCE_COLLECTION_ID + "\n2022")
START_DAY  = 1 + (uint32(first_8_hex(START_HASH)) mod 365)
```

Scan forward from the start day to 31 December, wrap to 1 January, and continue until five eligible items are accepted or all in-window items have been considered once.

If a source's frozen ordering precision is coarser than a day, the start day maps to the containing source-native bucket; scan begins at that bucket and uses the frozen tie-break inside it. This does not claim the true event occurred after the exact start instant.

Common eligibility remains:

1. enough official/public factual material for a bounded case packet;
2. consequential decision/transition or retrospective consequential review;
3. not project-authored/designed;
4. source identity/evidence can be preserved;
5. no exclusion because a case is expected to help or hurt TRACE.

Every considered exclusion retains identity and reason.

Frozen successor start positions:

```text
SC-RAIB       76ebc800 -> day 284 -> 2022-10-11
SC-PAC        14d2cf1f -> day 154 -> 2022-06-03
SC-EPA-FOIA2  45283bd7 -> day 109 -> 2022-04-19
SC-NHTSA-SGO  c828ef2b -> day 308 -> 2022-11-04 -> source-native November 2022 bucket
```

## 2. Execution adapter contract

A source family enters primary execution only if its adapter specifies:

- official collection/carrier identity;
- ordering field and stable tie-break identity;
- how the current study receives the complete-enough candidate identity set;
- transport provenance/evidence state;
- source conflict handling inherited from manifest v0.3;
- fail/HOLD condition;
- source-content retrieval path after selection.

```text
SOURCE_IDENTITY + EXECUTION_ADAPTER + SELECTOR
```

A deterministic selector over unavailable or ambiguous inputs is not treated as executed.

## 3. SC-RAIB — DIRECT STATIC/HTML INDEX ADAPTER

**Domain:** infrastructure / safety / engineering  
**Organisation:** UK Rail Accident Investigation Branch  
**Official collection:** GOV.UK RAIB reports + annual investigation index  
**Ordering:** occurrence date ascending; report identifier ascending tie-break  
**Filter:** completed full investigation reports only  
**Current adapter:** official annual/index metadata + individual GOV.UK report pages/PDF pointers are readable in current study aperture.  
**Transport:** direct public web read  
**HOLD:** contradictory occurrence-date identity or inability to reproduce annual candidate sequence.

Existing five-entry intake remains standing:
`PROJECT/TRACE_v0_3_0_OUTWARD_POOL_INTAKE_RAIB_v0_1.md`.

## 4. SC-PAC — STATIC PARLIAMENT REPORT ADAPTER

**Domain:** public administration / institutional review  
**Organisation:** House of Commons Committee of Public Accounts  
**Official collection:** ordinary Committee of Public Accounts reports published during calendar 2022, across parliamentary sessions where necessary, with `publications.parliament.uk` report bodies and committee publication/index pages.  
**Ordering field:** report `Date Published` ascending  
**Tie-break:** session identifier ascending then numeric ordinary Report number ascending.  
**Filter:** ordinary Committee of Public Accounts `Report` objects; exclude Government Responses, correspondence, oral/written evidence and Special Reports from this source family.  
**Current adapter:** static HTML report pages expose date, report number/session, inquiry and report body; reports themselves carry stable numbered session lists and HC references.  
**Source-native identity:** `SESSION|REPORT_NUMBER|HC_REFERENCE`  
**Transport:** direct public HTML read  
**HOLD:** session/report numbering conflict, missing publication date, or inability to establish complete-enough 2022 ordinary-report sequence.

Declared aperture: PAC reports are selected parliamentary oversight/review objects, not all public-administration decisions and not a neutral sample of government activity.

The calendar-year scope matters even though the five-item quota is expected to be reached in Session 2022–23 before wrap. Session boundaries are not silently treated as calendar boundaries.

## 5. SC-EPA-FOIA2 — OFFICIAL BULK FILE ADAPTER

**Domain:** ecological / environmental intervention  
**Organisation:** US Environmental Protection Agency, Superfund program  
**Official carrier:** SEMS Superfund Public User Database `FOIA-002 Records of Decision (RODs), ROD Amendments, and Explanation of Significant Differences (ESDs)` bulk report.  
**Ordering field:** `Actual Complete Date` ascending  
**Tie-break/source-native identity:** canonical composite
`EPA_ID|SITE_ID|ACT_SEQ|ACTION_NAME|OPERABLE_UNIT_NAME`; lexical ascending after normalization of surrounding whitespace only.  
**Filter:** action names ROD / ROD Amendment / ESD as represented by the official FOIA-002 carrier.  
**Transport:** exact official bulk carrier downloaded from EPA by bounded human transport when direct programmatic ingestion is unavailable; upload unchanged to study aperture; record official source URL, retrieval date, original filename, byte count and SHA-256. The uploaded bytes become the frozen study snapshot for this run.  
**Evidence state:** human-reported direct official download + locally observed bytes/hash; no official cryptographic hash is assumed.  
**Snapshot rule:** later EPA refreshes do not silently replace the frozen uploaded carrier. Corrections discovered later become new evidence.  
**Source-content path:** after identities are selected, retrieve the associated official decision document/site material where available for bounded case packet construction.  
**HOLD:** bulk carrier provenance unknown, unreadable/corrupt carrier, ordering fields missing/ambiguous, or candidate identity collision.

The FOIA-002 carrier is a Superfund action ledger, not the same object as the original client-rendered Collection 25504 decision-document table. It is therefore a new explicit source-family ID, not a hidden transport substitution.

```text
ACTUAL_COMPLETE_DATE != DECISION_DOCUMENT_PUBLICATION_DATE
FOIA2_ACTION_ROW != COMPLETE_ECOLOGICAL_EVENT
```

## 6. SC-NHTSA-SGO — OFFICIAL BULK CSV ADAPTER

**Domain:** AI / software / automated decision or control  
**Organisation:** US National Highway Traffic Safety Administration  
**Official carriers:** archived SGO incident-report CSVs for ADS and Level-2 ADAS prior to 2025.  
**Ordering field:** occurrence **month** ascending for the primary selector, matching the source precision guaranteed by the frozen collection design. Exact day/time fields, if present, are preserved for later case packets but do not reorder the primary pool.  
**Start mapping:** the frozen 2022-11-04 start maps to the `November 2022` bucket; all November candidate records are ordered by the tie-break below.  
**Tie-break/source-native identity:** `AUTOMATION_CLASS|OFFICIAL_REPORT_ID`, lexical ascending. ADS and Level-2 identifiers are namespaced by automation class even if raw identifier strings overlap.  
**Filter:** ADS + Level-2 ADAS incident reports; preserve automation class.  
**Case unit:** primary candidate unit is an official report record, but multiple report records demonstrably referring to the same real-world crash may not silently count as multiple independent real-world cases. If the official carrier exposes a stable duplicate/relationship field, use it mechanically to form an incident cluster. If duplicate relation would require operator judgement, preserve the records and set `DUPLICATE_CASE_RELATION_UNKNOWN`; do not count unresolved duplicates as reproduced independent cases.  
**Transport:** exact two official archive CSVs downloaded by bounded human transport when direct text/csv ingestion is unavailable; upload unchanged; record official URLs, retrieval date, filenames, byte counts and SHA-256. Uploaded bytes become the frozen study snapshots.  
**Evidence state:** human-reported direct official download + locally observed bytes/hash; no official hash assumed.  
**Snapshot rule:** later NHTSA archive refresh/correction does not silently replace frozen bytes; later differences are new evidence.  
**HOLD:** carrier provenance unknown, schema cannot expose frozen month/identity fields, duplicate-report relation makes the five-case real-world unit non-reproducible, or row data are unreadable.

Hard ceiling inherited:

```text
IN_SGO_DATA != AUTOMATION_CAUSED_CRASH
REPORTED_CRASH_COUNT != NORMALIZED_RISK
NOT_REPORTED != DID_NOT_OCCUR
REPORT_RECORD != NECESSARILY_DISTINCT_REAL_WORLD_CRASH
```

## 7. Bounded human transport rule

Human transport is a carrier operation, not a selection operation.

For EPA/NHTSA:

1. use only the predeclared official download link/carrier;
2. download the original file directly;
3. do not open/edit/re-save/convert before upload;
4. upload the downloaded file unchanged;
5. record human report of direct official download plus observed filename/bytes/SHA-256;
6. inspect schema/content only after byte identity is frozen locally.

A filename alone is not provenance. Human transport without an official published hash retains a provenance ceiling.

```text
HUMAN_DOWNLOADED_FROM_OFFICIAL_URL = REPORTED_PROVENANCE
REPORTED_PROVENANCE != CRYPTOGRAPHIC_ORIGIN_PROOF
HASHED_UPLOAD != PROOF_OF_SERVER_BYTES
TRANSPORTER != ITEM_SELECTOR
```

If the human deliberately or accidentally supplies a transformed/different file, fail closed rather than repairing content by hand.

## 8. Source conflict rule

The frozen manifest-v0.3 source-native conflict discipline applies symmetrically:

```text
compatible coarse + precise values -> most precise compatible value where precision participates in the source's ordering rule
incompatible values for same ordering concept -> ORDER_VALUE_DISPUTED
window-straddling conflict -> TEMPORAL_ELIGIBILITY_DISPUTED
disputed item -> preserve outside primary selector
```

For NHTSA primary ordering, month is deliberately the frozen ordering precision; more precise compatible day/time does not reorder the bucket.

No operator plausibility override.

## 9. Known pre-freeze exposure

Framework inspected source interfaces and some PAC report identities while testing executability. Framework is already excluded as a cold efficacy receiver/adjudicator. The source-family decision was driven by execution-route viability, not by scoring candidate cases for expected TRACE benefit.

The PAC source was selected as an executable broad public-administration oversight collection before its deterministic start/hash was used to derive the eventual five-item sequence. Any item exposure remains recorded rather than described as cold.

```text
FRAMEWORK_SOURCE_EXPOSURE != COLD_EFFICACY_EVIDENCE
```

## 10. Failure semantics

If one source adapter fails, preserve the failure and HOLD that family. Do not silently substitute search-engine results or a third-party mirror.

If the four-family pool cannot reach >=20 eligible entries or loses one mandatory domain, primary cold comparison does not execute under this adapter object. A successor adapter/source expansion may then be designed with ancestry preserved.

## 11. Pre-freeze attack

Before freezing this object, attack at least:

- source substitution after seeing cases;
- human transport as hidden item selector;
- carrier mutation/save-as risk;
- bulk snapshot freshness versus historical event date;
- duplicate identity handling;
- PAC session boundary accidentally replacing calendar boundary;
- PAC oversight-selection bias;
- EPA action-ledger versus decision-document mismatch;
- EPA actual-complete clock versus publication clock;
- NHTSA reporting/telemetry aperture;
- NHTSA exact start day falling inside a coarse month bucket;
- cross-file NHTSA ID collisions;
- duplicate reports masquerading as independent cases;
- mixed date precision;
- case identity collisions;
- source-family HOLD reducing mandatory-domain coverage;
- temptation to use search-engine snippets as exhaustive enumeration.

Freeze only after any material execution defect is repaired.