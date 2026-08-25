# TRACE v0.3.0 — SOURCE COLLECTION MANIFEST v0.3 ATTACK v0.1

**Status:** PRE-FREEZE BOUNDED ATTACK — NOT VALIDATION  
**Target:** `PROJECT/TRACE_v0_3_0_SOURCE_COLLECTION_MANIFEST_v0_3.md`  
**Date:** 2026-08-25

## Purpose

Test only the new source-native ordering conflict repair. Do not reopen the already-frozen collection/domain/date/quota choices by momentum.

## Fixed cases

| # | Attack | Result |
|---|---|---|
| 1 | two official surfaces give identical exact date | RESISTED — one unambiguous value |
| 2 | month-only card + exact day inside same month | RESISTED after repair — compatible; use precise value |
| 3 | year-only value + exact day in same year | RESISTED — compatible if same ordering concept |
| 4 | two exact official dates in same year that change scan order | RESISTED — `ORDER_DATE_DISPUTED` |
| 5 | conflicting official dates straddle 2021/2022 | RESISTED — `TEMPORAL_ELIGIBILITY_DISPUTED` |
| 6 | one official surface omits date, another supplies one | RESISTED — absence is not a conflicting value; use sole unambiguous value |
| 7 | occurrence date differs from publication date | RESISTED — different clocks/concepts are not source conflict |
| 8 | operator believes one conflicting value is a migration typo | RESISTED — suspected cause does not authorise choosing it |
| 9 | disputed item would be especially valuable to TRACE | RESISTED — value cannot enter primary selector while order unresolved; object preserved separately |
| 10 | excluding disputed item makes quota harder to reach | RESISTED — continue deterministic scan; do not force inclusion |
| 11 | so many dates are disputed that candidate enumeration cannot be trusted | RESISTED — `COLLECTION_ENUMERATION_HOLD` |
| 12 | another source family later shows the same class of conflict | RESISTED — rule is symmetric across all six families |
| 13 | compatible coarse/precise values disagree only in formatting | RESISTED — semantic/interval compatibility, not textual equality |
| 14 | two conflicting values are both inside 2022 and happen not to affect the first five | RESISTED — still disputed; no outcome-dependent waiver |
| 15 | a later documented source-family rule establishes authoritative precedence | BOUNDED — may support a future profile/run; cannot retroactively rewrite this run |

## Finding during attack

Initial v0.3 draft would have classified compatible coarse/precise official dates as conflicts. That was over-firing and could have excluded clean items. The draft was repaired before freeze:

```text
COARSE_DATE + CONSISTENT_PRECISE_DATE != SOURCE_CONFLICT
```

The repaired target now distinguishes compatible precision refinement from incompatible official values.

## Verdict

```text
ATTACKS: 15
MATERIAL DEFECTS SURVIVING REPAIRED TARGET: 0
VERDICT: CLEAR_WITH_RESIDUAL_LIMITS
```

Residual limits:

- source semantics may remain undocumented;
- official source conflicts can make some primary cases unusable without making the underlying material worthless;
- fail-closed dispute handling may systematically expose source-quality bias in the primary sample;
- no rule here determines world truth from publication metadata.

```text
ORDER_RESOLVED != SOURCE_TRUE
SOURCE_METADATA_CLEAN != WORLD_COMPLETE
FAIL_CLOSED != UNBIASED_SAMPLE
```
