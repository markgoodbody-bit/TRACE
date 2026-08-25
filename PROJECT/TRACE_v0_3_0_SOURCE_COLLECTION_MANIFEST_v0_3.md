# TRACE v0.3.0 — SOURCE COLLECTION MANIFEST v0.3

**Status:** NARROW EXECUTION REPAIR CANDIDATE — NOT YET FROZEN — NOT CASE SELECTION — NOT VALIDATION  
**Date:** 2026-08-25  
**Parent:** frozen `PROJECT/TRACE_v0_3_0_SOURCE_COLLECTION_MANIFEST_v0_2.md`  
**Trigger:** `PROJECT/TRACE_v0_3_0_SOURCE_COLLECTION_EXECUTION_FINDING_HSSIB_DATE_CONFLICT_v0_1.md`

## 0. Inheritance

This object inherits the v0.2 manifest unchanged except for the conflict-resolution rules below.

The following remain frozen exactly as in v0.2:

- six source collection IDs and source families;
- calendar year 2022;
- source-native date semantics declared per collection;
- deterministic start-day formula and six computed start dates;
- five-eligible-item quota per collection;
- eligibility rules and collection-specific filters;
- NHTSA reported-incident ceiling;
- Framework coldness exclusion;
- official-source aperture and source-persistence requirements.

No source family, date window, quota or start position changes as a consequence of seeing HSSIB items.

## 1. Source-native ordering conflict rule

A declared source-native ordering field may be used only when the official source supplies a value that is sufficiently unambiguous for the selection operation.

Multiple official surfaces are first checked for semantic and interval compatibility.

A coarse value and a more precise value are compatible when they refer to the same frozen ordering concept and the precise value falls wholly inside the coarse interval. Example:

```text
March 2022
16 March 2022
```

Those values do not conflict merely because their precision differs. Use the most precise compatible official value available.

```text
COARSE_DATE + CONSISTENT_PRECISE_DATE != SOURCE_CONFLICT
MORE_PRECISE_COMPATIBLE_VALUE != POST_HOC_DATE_CHOICE
```

Where multiple official surfaces for the same item provide genuinely incompatible values for the frozen ordering field, preserve all values and apply the following fail-closed rule:

```text
ONE_UNAMBIGUOUS_OFFICIAL_ORDER_VALUE -> USE_DECLARED_VALUE
MULTIPLE_COMPATIBLE_OFFICIAL_VALUES -> USE_MOST_PRECISE_COMPATIBLE_VALUE
MULTIPLE_CONFLICTING_OFFICIAL_VALUES -> ORDER_VALUE_DISPUTED
```

Do not choose a value because it appears more plausible, yields a convenient case, or matches an expected chronology.

```text
OFFICIAL_FIELD_A != OFFICIAL_FIELD_B
SOURCE_CONFLICT != OPERATOR_PERMISSION_TO_CHOOSE
DETERMINISTIC_RULE + AMBIGUOUS_INPUT != DETERMINISTIC_SELECTION
```

Different source fields that measure different concepts do not become a conflict merely because their dates differ; only values claiming the frozen ordering concept are compared.

```text
OCCURRENCE_DATE != REPORT_PUBLICATION_DATE
DOCUMENT_DATE != INCIDENT_DATE
DIFFERENT_CLOCKS != CONFLICTING_VALUES_OF_ONE_CLOCK
```

## 2. Temporal eligibility

For a primary intake window `[2022-01-01, 2022-12-31]`:

- if every materially plausible official value places the item inside 2022 but incompatible values would change scan order, mark `ORDER_DATE_DISPUTED` and do not let the item determine primary pool order until resolved;
- if conflicting official values straddle the 2022 window boundary, mark `TEMPORAL_ELIGIBILITY_DISPUTED`;
- a disputed item does **not** count toward the five-item primary quota while the dispute remains;
- it is preserved in a separate source-conflict ledger with all official values/pointers and remains eligible for later expansion/source-quality analysis;
- disputed status is not `ABSENT`, not `IRRELEVANT`, and not evidence that the underlying event/report is invalid.

```text
DISPUTED_ORDER != INELIGIBLE_IN_WORLD
EXCLUDED_FROM_PRIMARY_SELECTOR != ERASED
TEMPORAL_ELIGIBILITY_UNKNOWN != OUT_OF_WINDOW
```

## 3. No post-hoc semantic precedence

This run does not introduce a HSSIB-specific rule such as `timeline beats report page` or `report page beats collection card` after seeing the conflict.

A future source-family profile may establish a stable precedence rule if independently supported by the source's documented publication semantics. That later profile cannot retroactively rewrite this frozen primary run.

## 4. Enumeration rule under dirty metadata

Collection enumeration may use collection pages/search indexes to discover candidate item identities, but primary ordering uses only the frozen source-native field after compatibility/conflict checking.

If the collection cannot expose a complete enough candidate identity set for the 2022 aperture without relying on the disputed values themselves, set `COLLECTION_ENUMERATION_HOLD` rather than silently omitting possible items.

```text
DISCOVERY_ORDER != PRIMARY_SELECTION_ORDER
INDEX_LABEL != ORDERING_FACT
ENUMERATION_AVAILABLE != ORDER_VALUE_RESOLVED
```

## 5. Symmetry

This conflict rule applies to all six collections, not only HSSIB.

If RAIB, LGSCO, EPA, NHTSA or FOS later expose conflicting official values for their frozen ordering fields, the same dispute/hold logic fires.

The already-recorded RAIB intake remains valid unless a concrete conflicting occurrence-date value is subsequently observed for one of its considered items; no such conflict is currently claimed.

## 6. Preservation

The frozen v0.2 manifest, its clean 15-attack replay, the later HSSIB execution failure, and every disputed HSSIB item remain visible ancestry.

This repair expands the source model by representing source-internal ordering uncertainty. It does not narrow the corpus.
