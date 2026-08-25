# TRACE v0.3.0 — EPA CASE-UNIT ADAPTER ATTACK v0.1

**Status:** PRE-FREEZE BOUNDED ATTACK — NOT VALIDATION  
**Target:** `PROJECT/TRACE_v0_3_0_OUTWARD_EXECUTION_ADAPTER_EPA_CASE_UNIT_v0_1.md`  
**Date:** 2026-08-25

| # | Attack | Result |
|---|---|---|
| 1 | same site + same date but two independent decision documents | RESISTED — no cluster without official shared-document evidence |
| 2 | same decision document emits two OU rows | RESISTED — cluster, preserve both rows |
| 3 | same action label but different dates | RESISTED — no inferred cluster |
| 4 | rows adjacent in FOIA report | RESISTED — adjacency is not relation evidence |
| 5 | official document clearly names all member OUs | RESISTED — stable cluster justified |
| 6 | duplicate relation plausible but source unavailable | RESISTED — `EPA_CASE_RELATION_UNKNOWN` |
| 7 | clustering reduces quota count | RESISTED — continue deterministic scan; do not refill by judgement |
| 8 | clustering hides a materially different OU history | RESISTED — member row identities remain preserved and packet may expose OU differences |
| 9 | one case cluster accidentally counted as reproduced evidence twice | RESISTED — primary unit is cluster, not row |
| 10 | human chooses a convenient cluster label that changes CASE_ID | RESISTED — cluster identity hashes sorted source-row identities |
| 11 | later evidence shows cluster relation was wrong | BOUNDED — preserve prior run and correction; do not rewrite ancestry |
| 12 | five database rows mistaken for five primary EPA cases | RESISTED — quota explicitly counts primary case units |

```text
ATTACKS: 12
MATERIAL DEFECTS SURVIVING: 0
VERDICT: CLEAR_WITH_RESIDUAL_LIMITS
```

Residual: official decision-document relations may themselves be incomplete or later corrected. Clustering protects against known database-row multiplication; it does not establish complete real-world event identity.
