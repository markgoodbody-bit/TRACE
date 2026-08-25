# TRACE v0.3.0 — SOURCE COLLECTION MANIFEST v0.1

**Status:** WORKING PRE-INTAKE MANIFEST — NOT YET FROZEN — NOT CASE SELECTION — NOT VALIDATION  
**Date:** 2026-08-25  
**Parent protocol:** `PROJECT/TRACE_v0_3_0_OUTWARD_EVALUATION_PROTOCOL_v0_5_EXPANSION.md`

## 0. Purpose

Freeze the broad source apertures, temporal window, intake quotas and ordering rules **before** item-level case selection.

This manifest is intended to reduce cherry-picking. It does not make the source collections neutral or representative of the world.

```text
SOURCE_COLLECTION_FROZEN != SOURCE_COLLECTION_NEUTRAL
BROAD_COLLECTION != REPRESENTATIVE_WORLD_SAMPLE
DETERMINISTIC_INTAKE != UNBIASED_WORLD_MODEL
```

## 1. Common temporal aperture

Primary intake window:

```text
2022-01-01 through 2022-12-31 inclusive
```

Reason for choosing 2022 before item-level intake:

- all six candidate source families have material covering this period or a predecessor/legacy collection carried into the same public front door;
- NHTSA Standing General Order crash reporting began in 2021, so 2022 is the earliest complete common calendar year after the latest-starting source family;
- the window is old enough that completed investigations/decisions are likely to exist while avoiding selection based on current headlines;
- the year was selected as a common temporal aperture, not because any known 2022 case is expected to favour TRACE.

Where a source family does not expose one equivalent date concept, use the source-native date declared below. Do not silently substitute occurrence date for decision/publication date after seeing which cases enter.

## 2. Intake quota

Take the first **5 eligible source-native items** from each collection under the frozen order rule, yielding a target pool of 30 eligible real-world cases before deterministic case selection.

If fewer than 5 eligible items exist in-window, preserve the shortfall and reason; do not widen the window or alter the order without preserving this manifest as failed ancestry.

Eligibility remains that of frozen outward-evaluation mechanics:

1. sufficient public facts for a bounded packet;
2. consequential decision/transition or retrospective decision review;
3. not project-authored/designed;
4. source can be frozen/cited;
5. not excluded for being too easy, too hard, favourable or unfavourable to TRACE.

Ineligible source-native items remain recorded with exact exclusion reason.

## 3. Source collections

### SC-RAIB — Rail Accident Investigation Branch reports

**Domain:** essential infrastructure / safety / engineering  
**Responsible organisation:** UK Rail Accident Investigation Branch  
**Canonical collection:** `https://www.gov.uk/raib-reports`  
**Why broad:** official public collection of RAIB reports across railway accident/incident investigations rather than a curated list of cases chosen for a known TRACE pattern.  
**Source-native date for window:** occurrence date.  
**Canonical order:** occurrence date ascending, then report identifier ascending as displayed by RAIB.  
**Intake filter:** investigation reports only; exclude safety digests, bulletins, interim and discontinuation reports for the primary pool because investigation reports provide the fullest completed causal/evidence record.  
**Quota:** first 5 eligible 2022 occurrences in canonical order.

### SC-LGSCO — Local Government and Social Care Ombudsman decisions

**Domain:** public administration / institutional decision  
**Responsible organisation:** Local Government and Social Care Ombudsman  
**Canonical collection:** `https://www.lgo.org.uk/decisions`  
**Why broad:** large public decision database spanning local-government and social-care complaint outcomes, not a thematic failure list.  
**Source-native date for window:** published decision date as exposed by the decision search.  
**Canonical order:** date ascending; within the same date, reference number lexicographically ascending.  
**Intake filter:** both statements and reports; upheld and not-upheld outcomes both eligible; no subject-area filtering.  
**Quota:** first 5 eligible 2022 published decisions in canonical order.

### SC-EPA-ROD — EPA Superfund decision documents

**Domain:** ecological / environmental intervention  
**Responsible organisation:** US Environmental Protection Agency  
**Canonical collection:** `https://www.epa.gov/superfund/search-superfund-decision-documents`  
**Why broad:** official collection of Superfund remedy decision documents including Records of Decision, ROD amendments and Explanations of Significant Differences; documents exist to record reasoning for cleanup choices/changes.  
**Source-native date for window:** document date.  
**Canonical order:** document date ascending; ties by Doc ID lexicographically ascending.  
**Intake filter:** ROD, ROD Amendment and ESD all eligible; associated non-decision memos/files excluded unless they are the primary decision document.  
**Quota:** first 5 eligible 2022 decision documents in canonical order.

### SC-NHTSA-SGO — NHTSA Standing General Order crash reporting

**Domain:** AI / software / automated decision or control  
**Responsible organisation:** US National Highway Traffic Safety Administration  
**Canonical collection:** `https://www.nhtsa.gov/laws-regulations/standing-general-order-crash-reporting`  
**Why broad:** regulator-mandated public reporting collection for crashes involving ADS and SAE Level 2 ADAS, including explicit published limitations about incomplete/unverified reporting, duplicate reports, telemetry asymmetry and non-normalized exposure.  
**Source-native date for window:** crash occurrence month/year in the public summary incident data.  
**Canonical order:** occurrence month ascending; within month use stable incident/report identifier lexicographically ascending. If the archived 2022 file exposes a more specific source-native incident date, do not use it to reorder unless the same field is available for all candidate 2022 rows.  
**Intake filter:** ADS and Level 2 ADAS eligible; preserve reporting-coverage limitations; do not infer system causation merely from inclusion in the SGO dataset.  
**Quota:** first 5 eligible 2022 incidents in canonical order.

### SC-FOS — Financial Ombudsman Service final decisions

**Domain:** finance / contract / organisational governance  
**Responsible organisation:** UK Financial Ombudsman Service  
**Canonical collection:** `https://www.financial-ombudsman.org.uk/businesses/resolving-complaint/ombudsman-decisions`  
**Why broad:** database containing published final ombudsman decisions across financial sectors since 1 April 2013, not a curated failure collection.  
**Source-native date for window:** final decision date.  
**Canonical order:** decision date ascending; ties by DRN/reference identifier lexicographically ascending.  
**Intake filter:** all sectors; upheld and not-upheld decisions eligible; no keyword or business-name filter.  
**Quota:** first 5 eligible 2022 decisions in canonical order.

### SC-HSSIB — HSSIB / legacy HSIB patient safety investigations

**Domain:** health-service operations / patient safety  
**Responsible organisation:** Health Services Safety Investigations Body (including legacy HSIB investigation material retained in its public collection)  
**Canonical collection:** `https://www.hssib.org.uk/patient-safety-investigations/`  
**Why broad:** official patient-safety investigation collection intended to identify systemic learning rather than individual blame; the public collection exposes investigations and published reports across healthcare safety themes.  
**Source-native date for window:** report publication date.  
**Canonical order:** report publication date ascending; ties by canonical investigation URL lexicographically ascending.  
**Intake filter:** completed published national patient-safety investigation reports; exclude launch-only pages without a completed report for the primary pool.  
**Quota:** first 5 eligible reports published in 2022 in canonical order.

## 4. Known pre-freeze exposure / contamination note

Framework has inspected collection front doors to verify collection identity, scope and ordering feasibility. Search results incidentally exposed a small number of individual item titles/summaries, including some RAIB and Financial Ombudsman entries and current HSSIB/NHTSA examples.

This exposure occurred **after the broad collection families had already been proposed** but before this manifest was frozen.

Disposition:

```text
COLLECTION_CHOICE_PRECEDED_ITEM_EXPOSURE = YES
FRAMEWORK_ITEM_COLDNESS = NO / PARTIALLY CONTAMINATED
DETERMINISTIC_SELECTION_RULE = STILL REQUIRED
FRAMEWORK_MUST_NOT_COUNT_AS COLD RECEIVER OR INDEPENDENT EFFICACY ADJUDICATOR
```

Do not remove these collections merely to create an appearance of purity. Preserve the exposure and mechanically prevent it from influencing intake/selection.

A previously considered Google Cloud incident-history source was excluded for this cycle because Framework opened its machine-readable history before collection freeze and encountered a detailed individual incident narrative while verifying the schema. The exclusion is preserved as contamination evidence, not treated as a defect in Google Cloud's source.

## 5. Alternative qualifying collection classes considered

Alternatives remain discoverable but are not active primary apertures for this run:

- aviation/marine accident investigation collections for infrastructure safety;
- Parliamentary and other ombudsman decision collections for public administration;
- environmental enforcement/court decisions instead of Superfund remedy decisions;
- autonomous-system incident databases curated outside regulators;
- FCA enforcement decisions or court judgments for finance;
- CQC enforcement/inspection material or other NHS safety collections for health services.

They were not selected because the six active sources together provide broad official collections, stable public provenance, cross-domain diversity and enough material for deterministic intake. This is a design choice, not proof of neutrality.

## 6. Manifest attack questions before freeze

Attack this manifest before item-level intake for at least:

1. 2022 chosen because it secretly favours known cases;
2. occurrence-date versus publication/decision-date mismatch causing selection distortion;
3. first-five intake systematically choosing a nonrepresentative edge of each collection;
4. source-native identifiers/order not actually stable enough to reproduce;
5. RAIB investigation-report-only filter introducing severity bias;
6. LGSCO inclusion of both upheld/not-upheld but chronological order creating seasonal/administrative bias;
7. EPA ROD/Amendment/ESD mixture combining unlike decision types;
8. NHTSA reporting coverage/telemetry asymmetry making incident inclusion itself a biased aperture;
9. FOS decision-publication process/retention changing what remains visible;
10. HSSIB investigation-selection process meaning the collection is already a selected subset of patient-safety reality;
11. UK-heavy domain mix creating institutional/cultural overconcentration;
12. official-source bias excluding affected-party accounts;
13. Framework pre-freeze item exposure contaminating collection choice or later adjudication;
14. six domains too close to TRACE's existing favourite failure surfaces;
15. deterministic selection being mistaken for representative sampling.

Material defects may repair the manifest before freeze. Once frozen, substantive collection/window/order/quota changes require preserving the original manifest and its consequences rather than silently moving the aperture.

## 7. Stop boundary

Do not inspect item-level cases for eligibility/intake until this manifest has survived the bounded attack and a freeze record identifies the exact Git object.
