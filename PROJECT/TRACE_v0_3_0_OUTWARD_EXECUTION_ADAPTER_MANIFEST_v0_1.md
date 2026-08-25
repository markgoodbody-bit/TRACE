# TRACE v0.3.0 — OUTWARD EXECUTION ADAPTER MANIFEST v0.1

**Status:** PRE-FREEZE SUCCESSOR STUDY ADAPTER — NOT CASE SELECTION — NOT VALIDATION  
**Date:** 2026-08-25  
**Trigger:** `PROJECT/TRACE_v0_3_0_SOURCE_COLLECTION_EXECUTION_READINESS_FINDING_v0_1.md`

## 0. Purpose

Repair the outward study's execution-layer assumption without erasing the original six-source attempt.

The primary pool for the successor execution uses four broad official source families whose enumeration route is declared **before** case selection:

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
SC-NHTSA-SGO  c828ef2b -> day 308 -> 2022-11-04
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
**Official collection:** committee reports for Session 2022–23, with `publications.parliament.uk` report bodies and committee publication/index pages.  
**Ordering field:** report `Date Published` ascending  
**Tie-break:** numeric ordinary Report number ascending; Special Reports are separate type and do not displace ordinary Report ordering unless they independently satisfy the common eligibility rule and share a date.  
**Filter:** ordinary Committee of Public Accounts `Report` objects; exclude Government Responses, correspondence, oral/written evidence and Special Reports from this source family.  
**Current adapter:** static HTML report pages expose date, report number/session, inquiry and report body; reports themselves contain a stable numbered session list.  
**Source-native identity:** `SESSION|REPORT_NUMBER|HC_REFERENCE`  
**Transport:** direct public HTML read  
**HOLD:** session/report numbering conflict, missing publication date, or inability to establish complete-enough 2022 ordinary-report sequence.

Declared aperture: PAC reports are parliamentary oversight/review objects, not all public-administration decisions and not neutral samples of government activity.

## 5. SC-EPA-FOIA2 — OFFICIAL BULK FILE ADAPTER

**Domain:** ecological / environmental intervention  
**Organisation:** US Environmental Protection Agency, Superfund program  
**Official carrier:** SEMS Superfund Public User Database `FOIA-002 Records of Decision (RODs), ROD Amendments, and Explanation of Significant Differences (ESDs)` bulk report.  
**Ordering field:** `Actual Complete Date` ascending  
**Tie-break/source-native identity:** canonical composite
`EPA_ID|SITE_ID|ACT_SEQ|ACTION_NAME|OPERABLE_UNIT_NAME`; lexical ascending after normalization of surrounding whitespace only.  
**Filter:** action names ROD / ROD Amendment / ESD as represented by the official FOIA-002 carrier.  
**Transport:** exact official bulk carrier downloaded from EPA by bounded human transport when direct programmatic ingestion is unavailable; upload unchanged to study aperture; record source URL, retrieval date, original filename, byte count and SHA-256.  
**Evidence state:** human-reported direct official download + locally observed bytes/hash; no official cryptographic hash is assumed.  
**Source-content path:** after identities are selected, retrieve the associated official decision document/site material where available for bounded case packet construction.  
**HOLD:** bulk carrier provenance unknown, unreadable/corrupt carrier, ordering fields missing/ambiguous, or candidate identity collision.

The FOIA-002 carrier is an action ledger, not a complete ecological history or affected-party record.

## 6. SC-NHTSA-SGO — OFFICIAL BULK CSV ADAPTER

**Domain:** AI / software / automated decision or control  
**Organisation:** US National Highway Traffic Safety Administration  
**Official carriers:** archived SGO incident-report CSVs for ADS and Level-2 ADAS prior to 2025.  
**Ordering field:** 2022 occurrence month/date fields as actually present in the official rows; if the carrier exposes only month/year for a row, that is the available precision.  
**Tie-break/source-native identity:** official stable incident/report identifier; lexical ascending.  
**Filter:** ADS + Level-2 ADAS incident reports; preserve automation class.  
**Transport:** exact two official archive CSVs downloaded by bounded human transport when direct text/csv ingestion is unavailable; upload unchanged; record official URLs, retrieval date, filenames, byte counts and SHA-256.  
**Evidence state:** human-reported direct official download + locally observed bytes/hash; no official hash assumed.  
**HOLD:** carrier provenance unknown, schema cannot expose frozen ordering/identity fields, duplicate-report identity cannot be resolved without operator judgement, or row data are unreadable.

Hard ceiling inherited:

```text
IN_SGO_DATA != AUTOMATION_CAUSED_CRASH
REPORTED_CRASH_COUNT != NORMALIZED_RISK
NOT_REPORTED != DID_NOT_OCCUR
```

## 7. Source conflict rule

The frozen manifest-v0.3 source-native conflict discipline applies symmetrically:

```text
compatible coarse + precise values -> most precise compatible value
incompatible values for same ordering concept -> ORDER_VALUE_DISPUTED
window-straddling conflict -> TEMPORAL_ELIGIBILITY_DISPUTED
disputed item -> preserve outside primary selector
```

No operator plausibility override.

## 8. Known pre-freeze exposure

Framework inspected source interfaces and some PAC report identities while testing executability. Framework is already excluded as a cold efficacy receiver/adjudicator. The source-family decision was driven by execution-route viability, not by scoring candidate cases for expected TRACE benefit.

```text
FRAMEWORK_SOURCE_EXPOSURE != COLD_EFFICACY_EVIDENCE
```

## 9. Failure semantics

If one source adapter fails, preserve the failure and HOLD that family. Do not silently substitute search-engine results or a third-party mirror.

If the four-family pool cannot reach >=20 eligible entries or loses one mandatory domain, primary cold comparison does not execute under this adapter object. A successor adapter/source expansion may then be designed with ancestry preserved.

## 10. Pre-freeze attack

Before freezing this object, attack at least:

- source substitution after seeing cases;
- human transport as hidden item selector;
- carrier mutation/save-as risk;
- bulk snapshot freshness versus historical event date;
- duplicate identity handling;
- PAC oversight-selection bias;
- EPA action-ledger versus decision-document mismatch;
- NHTSA reporting/telemetry aperture;
- mixed date precision;
- case identity collisions;
- source-family HOLD reducing mandatory-domain coverage;
- temptation to use search-engine snippets as exhaustive enumeration.

Freeze only after any material execution defect is repaired.