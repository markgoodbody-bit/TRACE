# TRACE v0.3.0 — SOURCE COLLECTION EXECUTION READINESS FINDING v0.1

**Status:** MATERIAL STUDY-INTERFACE FINDING — PRIMARY INTAKE PARTIALLY HOLD — NOT TRACE VALIDATION/FALSIFICATION  
**Date:** 2026-08-25  
**Parent:** frozen outward protocol + source manifest v0.2/v0.3

## Finding

The source manifest froze broad public collection identity, date semantics and deterministic ordering before item selection, but it did not require proof that the **current study aperture can actually execute the declared enumeration/order contract**.

That assumption failed across several source families in materially different ways.

```text
PUBLIC_COLLECTION != EXECUTABLE_COLLECTION_APERTURE
ORDER_DECLARED != ORDER_REPRODUCIBLE
FILTER_AVAILABLE_IN_UI != FILTER_INVOKABLE_BY_CURRENT_READER
PUBLIC_DOWNLOAD_LINK != CURRENT_READER_CAN_INGEST
SOURCE_METADATA_PRESENT != SOURCE_METADATA_COHERENT
```

## Current collection readiness

### SC-RAIB — EXECUTABLE / PASS

The official 2022 investigation corpus exposes enough stable occurrence-date/report identity information to reproduce the frozen forward/wrap scan. Five eligible entries were recorded with three filter exclusions preserved.

Evidence:
`PROJECT/TRACE_v0_3_0_OUTWARD_POOL_INTAKE_RAIB_v0_1.md`

### SC-HSSIB — HOLD / SOURCE-METADATA CONFLICT

Official legacy/current surfaces repeatedly disagree on the same frozen `final report publication date`, including conflicts across the 2022 boundary. No post-hoc field precedence is authorised.

Evidence:
- `PROJECT/TRACE_v0_3_0_SOURCE_COLLECTION_EXECUTION_FINDING_HSSIB_DATE_CONFLICT_v0_1.md`
- `PROJECT/TRACE_v0_3_0_OUTWARD_POOL_INTAKE_HSSIB_HOLD_v0_1.md`

### SC-NHTSA-SGO — HOLD / TRANSPORT-INGESTION BOUNDARY

NHTSA exposes official archived ADS and Level-2 ADAS incident CSVs and documents their limitations. The current web aperture can resolve the official CSV links but cannot ingest `text/csv` row content. The official 2022 summary carrier preserves aggregate limitations but not the individual stable report IDs required by the frozen selector.

Do not replace the official CSV with a third-party mirror merely for convenience.

```text
OFFICIAL_ARCHIVE_EXISTS != ARCHIVE_ROWS_AVAILABLE_TO_THIS_READER
AGGREGATE_SUMMARY != INCIDENT_ENUMERATION
```

A bounded human transport of the two unchanged official archive CSV files can discharge this aperture limitation without changing the source family or selector.

### SC-FOS — HOLD / FORM-ACTUATION BOUNDARY

The official Financial Ombudsman decision database exposes date-from/date-to, upheld/not-upheld and date-sort controls, and states that it contains all published final ombudsman decisions since April 2013. The current text/web aperture can read result pages and individual decisions but cannot reproducibly submit/freeze the exact all-sector 2022 date-filter/sort form state needed to enumerate from the frozen 2022-09-06 start without search-engine sampling or hidden UI state.

Search-engine snippets are not a substitute for exhaustive official enumeration.

### SC-LGSCO — HOLD / FORM-ACTUATION + PERSISTENCE BOUNDARY

The official LGSCO decision interface exposes date range, ascending/descending sort, decision type and reason filters. The current aperture can read the form description and some result pages but cannot reproducibly actuate/freeze the exact all-subject date-filtered ascending result set. In addition, ordinary decision statements are only kept for five years, creating a known persistence horizon.

Do not infer publication ordering from complaint-event dates or search snippets.

### SC-EPA-ROD — HOLD / CLIENT-RENDERED ENUMERATION BOUNDARY

EPA's official Superfund Decision Documents collection is explicitly column-sortable/searchable and identifies Collection 25504, but the current text aperture receives the table schema without the row data. Individual official 2022 documents can be found by search, but that would not reproduce the frozen all-collection date/Doc-ID ordering from 2022-08-19.

Do not manually assemble an apparently plausible five-item set from search results.

## Root of the study-design failure

The protocol tested **selection neutrality** before item reading but insufficiently tested **selector executability in the actual receiving aperture**.

A deterministic rule over inaccessible/ambiguous inputs is not operationally deterministic.

```text
RULE_DETERMINISTIC != EXECUTION_REPRODUCIBLE
COLLECTION_PUBLIC != COLLECTION_ENUMERABLE_HERE
SOURCE_IDENTITY_FROZEN != TRANSPORT_FROZEN
```

This is closely related to the newly preserved aperture-actuation seam:

```text
AVAILABLE_APERTURE != ACTIVATED_APERTURE
```

but no TRACE primitive/root is earned from this study failure.

## Disposition

Do not weaken the frozen selection rule or cherry-pick cases to keep the experiment moving.

```text
RAIB: KEEP 5 RECORDED POOL ENTRIES
HSSIB: PRESERVE HOLD / 0 PRIMARY ENTRIES
NHTSA: BOUNDED HUMAN-TRANSPORT PATH AVAILABLE
FOS/LGSCO/EPA: HOLD UNTIL REPRODUCIBLE OFFICIAL ENUMERATION PATH EXISTS
PRIMARY CASE SELECTION: NOT YET AUTHORISED
```

The original source manifest and its attack/freeze remain valid ancestry about collection-choice discipline. The new finding shows an additional layer that must be designed before a fully reproducible outward run.

## Evolution pressure

A successor outward-study design should freeze, **before item-level reading**:

1. collection identity;
2. ordering/date semantics;
3. **execution adapter / transport path** for enumeration;
4. evidence that the adapter exposes the complete enough candidate identity set needed by the selector;
5. fallback/HOLD behavior if the adapter fails;
6. source-content capture path after an item is selected.

```text
SOURCE MANIFEST
+ EXECUTION ADAPTER MANIFEST
+ SELECTION RULE
```

not source manifest alone.

## Preservation / expansion

No source family or failed execution path is erased. HSSIB metadata conflict and inaccessible-enumeration cases become part of the project's source/aperture evidence corpus.

A new cycle may use additional broad collections with machine-reproducible static/bulk interfaces, but adding them is **expansion**, not replacement-as-erasure. The current six remain preserved as attempted apertures and future profiles.
