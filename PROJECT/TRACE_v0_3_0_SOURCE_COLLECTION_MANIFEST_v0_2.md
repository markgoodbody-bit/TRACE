# TRACE v0.3.0 — SOURCE COLLECTION MANIFEST v0.2

**Status:** REPAIRED PRE-FREEZE MANIFEST — NOT YET FROZEN — NOT CASE SELECTION — NOT VALIDATION  
**Date:** 2026-08-25  
**Supersedes for execution:** v0.1, preserved as failed pre-freeze ancestry  
**Attack:** `PROJECT/TRACE_v0_3_0_SOURCE_COLLECTION_MANIFEST_ATTACK_v0_1.md`

## 0. Purpose

Freeze broad source apertures, temporal window, deterministic intake and source-persistence rules before item-level case selection.

```text
SOURCE_COLLECTION_FROZEN != SOURCE_COLLECTION_NEUTRAL
BROAD_COLLECTION != REPRESENTATIVE_WORLD_SAMPLE
DETERMINISTIC_INTAKE != UNBIASED_WORLD_MODEL
OFFICIAL_RECORD != WORLD
```

## 1. Temporal aperture

Primary intake window:

```text
2022-01-01 through 2022-12-31 inclusive
```

2022 is used because all six source families expose material for the period and NHTSA SGO began in 2021, making 2022 the earliest complete calendar year after the latest-starting family. It is not claimed representative.

Use the source-native date declared for each collection. Cross-collection rates or temporal prevalence may not be inferred from these unlike date semantics.

## 2. Deterministic intake rule

For each collection:

```text
START_HASH = SHA256(SOURCE_COLLECTION_ID + "\n2022")
START_DAY  = 1 + (uint32(first_8_hex(START_HASH)) mod 365)
```

Begin at `START_DAY` in the collection's frozen canonical order, scan forward to 31 December, wrap to 1 January, and continue until **5 eligible items** are collected or every in-window item has been considered once.

Eligibility:

1. sufficient public facts for a bounded packet;
2. consequential decision/transition or retrospective decision review;
3. not project-authored/designed;
4. source can be frozen/cited;
5. not excluded for being too easy, too hard, favourable or unfavourable to TRACE.

Every considered ineligible item retains source identity and exact exclusion reason.

Frozen start positions:

```text
SC-RAIB       hash-prefix 76ebc800 -> day 284 -> 2022-10-11
SC-LGSCO      hash-prefix eb756c64 -> day 241 -> 2022-08-29
SC-EPA-ROD    hash-prefix 001595cd -> day 231 -> 2022-08-19
SC-NHTSA-SGO  hash-prefix c828ef2b -> day 308 -> 2022-11-04
SC-FOS        hash-prefix b5cf81f6 -> day 249 -> 2022-09-06
SC-HSSIB      hash-prefix ce7ca953 -> day 353 -> 2022-12-19
```

Collection IDs and these start positions may not be renamed/recomputed after item reading in this run.

## 3. Source collections

### SC-RAIB

**Domain:** essential infrastructure / safety / engineering  
**Organisation:** UK Rail Accident Investigation Branch  
**Collection:** `https://www.gov.uk/raib-reports`  
**Date:** occurrence date  
**Order:** occurrence date ascending, then report identifier ascending  
**Filter:** completed investigation reports only  
**Declared aperture:** full-investigation reports are a selected/severity/completion subset, not all rail events.

### SC-LGSCO

**Domain:** public administration / institutional decision  
**Organisation:** Local Government and Social Care Ombudsman  
**Collection:** `https://www.lgo.org.uk/decisions`  
**Date:** published decision date  
**Order:** date ascending, then reference number ascending  
**Filter:** statements and reports; upheld and not-upheld; no subject filter  
**Persistence warning:** ordinary decision statements are retained for a shorter period than public-interest reports. Preserve selected source identity/retrieval promptly.

### SC-EPA-ROD

**Domain:** ecological / environmental intervention  
**Organisation:** US Environmental Protection Agency  
**Collection:** `https://www.epa.gov/superfund/search-superfund-decision-documents`  
**Date:** document date  
**Order:** document date ascending, then Doc ID ascending  
**Filter:** ROD, ROD Amendment, ESD; preserve decision-document type  
**Declared aperture:** unlike decision-document types are not one homogeneous intervention class.

### SC-NHTSA-SGO

**Domain:** AI / software / automated decision or control  
**Organisation:** US National Highway Traffic Safety Administration  
**Collection:** `https://www.nhtsa.gov/laws-regulations/standing-general-order-crash-reporting`  
**Date:** crash occurrence month/year in archived public incident data  
**Order:** occurrence month ascending; within month stable incident/report identifier ascending  
**Filter:** ADS and Level 2 ADAS reports  
**Hard ceiling:** this is a sample of **reported SGO incidents**, not the crash population and not a system-caused-crash sample. Reporting depends on awareness, telemetry and reporting requirements; reports may be incomplete/unverified or duplicated and exposure is not normalized.

```text
IN_SGO_DATA != AUTOMATION_CAUSED_CRASH
REPORTED_CRASH_COUNT != NORMALIZED_RISK
NOT_REPORTED != DID_NOT_OCCUR
```

### SC-FOS

**Domain:** finance / contract / organisational governance  
**Organisation:** UK Financial Ombudsman Service  
**Collection:** `https://www.financial-ombudsman.org.uk/businesses/resolving-complaint/ombudsman-decisions`  
**Date:** final decision date  
**Order:** date ascending, then DRN/reference identifier ascending  
**Filter:** all sectors; upheld and not-upheld; no keyword/business filter.

### SC-HSSIB

**Domain:** health-service operations / patient safety  
**Organisation:** Health Services Safety Investigations Body / legacy HSIB public investigation corpus  
**Collection:** `https://www.hssib.org.uk/patient-safety-investigations/`  
**Date:** report publication date  
**Order:** publication date ascending, then canonical investigation URL ascending  
**Filter:** completed published investigation reports  
**Declared aperture:** HSSIB/HSIB selects which systemic issues to investigate; this is not all patient-safety harm.

## 4. Source persistence and packet capture

As soon as an item enters the deterministic eligible pool, preserve:

- exact source identity / native identifier;
- canonical source URL;
- retrieval date;
- source-native date used for ordering;
- decision/report/incident type;
- bounded source packet or stable evidence pointer sufficient for later reconstruction;
- any known source-retention/persistence limit.

```text
LIVE_COLLECTION_PERSISTENCE != SOURCE_EVENT_PERSISTENCE
LATER_UNAVAILABLE != NEVER_PUBLISHED
SOURCE_CAPTURE != WORLD_CAPTURE
```

## 5. Official-source aperture

The six primary collections are institutional/official sources. This improves provenance but may underrepresent affected-party experience and contested accounts.

Do not fix this by cherry-picking cases. After case identity is mechanically frozen, packet construction may add secondary public evidence only under a separately frozen source-supplement rule.

## 6. Known Framework exposure

Framework has partial pre-freeze item exposure from front-door verification/search snippets. Collection choice preceded those exposures, but Framework is not cold for efficacy purposes.

```text
FRAMEWORK_ITEM_COLDNESS = NO / PARTIALLY CONTAMINATED
FRAMEWORK != COLD RECEIVER
FRAMEWORK != INDEPENDENT EFFICACY ADJUDICATOR
```

A previously considered Google Cloud incident-history collection remains excluded for this cycle because a detailed individual incident was opened before collection freeze while verifying its schema. Preserve the contamination event rather than pretending a clean aperture.

## 7. Residual limits

- four collections are UK and two US;
- source-native date concepts differ;
- RAIB/HSSIB are institutionally selected investigation subsets;
- official sources can omit affected-party knowledge;
- deterministic collection intake is not representative sampling;
- 2022 is a practical common aperture, not a special or representative year.

These limits are carried into the eventual expansion map; none authorises silent reinterpretation of the sample.

## 8. Pre-freeze replay gate

Replay the 15 attacks from `TRACE_v0_3_0_SOURCE_COLLECTION_MANIFEST_ATTACK_v0_1.md` against this exact object.

Freeze only if no material manifest defect survives. Do not broaden the attack set by momentum after a clean replay; later real execution failures remain new evidence and may reopen the manifest with ancestry preserved.
