# TRACE v0.3.0 — OUTWARD EXECUTION ADAPTER MANIFEST ATTACK v0.1

**Status:** PRE-FREEZE BOUNDED ATTACK — NOT VALIDATION  
**Target:** `PROJECT/TRACE_v0_3_0_OUTWARD_EXECUTION_ADAPTER_MANIFEST_v0_1.md`  
**Date:** 2026-08-25

## Purpose

Attack whether the successor study is actually executable and whether its adapters can silently steer case selection.

## Attacks

| # | Attack | Result |
|---|---|---|
| 1 | source family substituted after seeing a favourable case | RESISTED — family/adapter frozen before primary selection; ancestry/exposure preserved |
| 2 | human chooses which rows to upload | RESISTED — only exact predeclared whole official carriers allowed |
| 3 | browser opens/re-saves CSV/PDF and mutates bytes | RESISTED — direct download unchanged required; otherwise fail closed |
| 4 | uploaded file hash is mistaken for proof of official-server bytes | RESISTED — human provenance remains REPORTED, not cryptographic origin proof |
| 5 | EPA monthly/current refresh changes historic rows later | RESISTED — uploaded bytes become frozen study snapshot; later difference is new evidence |
| 6 | EPA FOIA-002 `Actual Complete Date` treated as Collection-25504 document publication date | RESISTED — new source-family ID and explicit non-equivalence |
| 7 | EPA action row lacks enough decision material for a bounded case | RESISTED — common eligibility fails that row; continue deterministic scan and preserve exclusion |
| 8 | PAC source accidentally covers only Session 2022-23 rather than calendar 2022 | REPAIRED BEFORE FREEZE — collection now covers all ordinary PAC reports published in calendar 2022 across sessions |
| 9 | PAC report numbering resets across session boundary | RESISTED — identity includes session + report number + HC reference |
| 10 | PAC oversight reports assumed representative of public administration | RESISTED — declared selected oversight aperture |
| 11 | NHTSA 2022-11-04 start cannot be compared to month-only rows | REPAIRED BEFORE FREEZE — start maps to November source-native bucket; report-ID tie-break inside month |
| 12 | NHTSA exact day/time silently reorders month-bucket rows | RESISTED — exact precision preserved for packets but does not alter primary order |
| 13 | ADS and L2 report IDs collide | REPAIRED BEFORE FREEZE — identity namespaced by automation class |
| 14 | multiple SGO reports for one crash count as multiple independent real-world cases | REPAIRED BEFORE FREEZE — report-record unit distinguished from real-world incident; mechanical clustering if official relation exists, otherwise duplicate relation stays UNKNOWN and cannot establish independent reproduction |
| 15 | NHTSA reported incidents treated as automation-caused or normalized risk sample | RESISTED — hard ceiling inherited |
| 16 | one of four source families fails and study quietly proceeds with only three mandatory domains | RESISTED — primary comparison cannot execute under this adapter if >=20/four-domain requirement fails |
| 17 | search-engine snippets used to fill gaps in official enumeration | RESISTED — snippets may discover pointers but cannot become exhaustive selector input |
| 18 | source conflict is resolved by operator plausibility | RESISTED — frozen v0.3 dispute rule applies |
| 19 | same source-native identity hashes differently after whitespace noise | BOUNDED — EPA composite normalizes surrounding whitespace only; other identities use source-native stable strings; collision/conflict -> HOLD |
| 20 | RAIB prior intake is grandfathered despite a later concrete ordering contradiction | RESISTED — standing only absent concrete occurrence-date conflict; conflict would reopen |

## Repairs earned during attack

Four material pre-freeze repairs were made to the adapter target:

1. PAC collection widened from Session 2022-23 to all ordinary PAC reports published in calendar 2022;
2. NHTSA start-day semantics mapped explicitly to its month-resolution selector;
3. NHTSA source-native identity namespaced by automation class;
4. NHTSA report-record identity separated from independent real-world crash identity / duplicate relation.

Human transport provenance and bulk-snapshot ceilings were also made explicit.

## Verdict

```text
ATTACKS: 20
MATERIAL DEFECTS SURVIVING REPAIRED TARGET: 0
VERDICT: CLEAR_WITH_RESIDUAL_LIMITS
```

Residual limits:

- human-reported official download is not cryptographic origin proof;
- current official bulk snapshots may contain later corrections to 2022 records;
- PAC/RAIB/EPA/NHTSA remain institutionally selected apertures;
- NHTSA duplicate relation may remain unresolved in some rows;
- executable collection selection is not representative world sampling;
- the four-domain design has no redundancy if a mandatory source adapter fails.

```text
EXECUTABLE != REPRESENTATIVE
FROZEN_BYTES != ORIGINAL_EVENT
OFFICIAL_SOURCE != COMPLETE_WORLD
ADAPTER_CLEAR != EVALUATION_VALIDATED
```
