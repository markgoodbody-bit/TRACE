# TRACE v0.3.0 — OUTWARD REAL-WORLD POOL FREEZE — 20 CASES v0.1

**Status:** FROZEN 20-CASE REAL-WORLD POOL — NOT EFFICACY SELECTION — NOT VALIDATION  
**Date:** 2026-08-27  
**Protocol:** frozen `PROJECT/TRACE_v0_3_0_OUTWARD_EVALUATION_PROTOCOL_v0_5_EXPANSION.md`  
**Execution adapter:** `PROJECT/TRACE_v0_3_0_OUTWARD_EXECUTION_ADAPTER_MANIFEST_v0_1.md`

## 0. Purpose

Freeze the completed successor-study real-world source pool before any later efficacy-case selection or Arm A/T comparison.

This object does not rewrite the historical source-family intake records. It composes them.

```text
SOURCE_FAMILY_INTAKE != EFFICACY_SELECTION
POOL_FREEZE != CASE_ANALYSIS
POOL_MEMBERSHIP != TRACE_SUCCESS
```

## 1. Intake ancestry

| family | count | intake object | blob SHA at freeze |
|---|---:|---|---|
| `SC-RAIB` | 5 | `PROJECT/TRACE_v0_3_0_OUTWARD_POOL_INTAKE_RAIB_v0_1.md` | `7f087dc74015721aab88769b47b8444f5c37a9f3` |
| `SC-PAC` | 5 | `PROJECT/TRACE_v0_3_0_OUTWARD_POOL_INTAKE_PAC_v0_1.md` | `17d98393f045441e3b4a6f24b2be6127a36e156a` |
| `SC-EPA-FOIA2` | 5 | `PROJECT/TRACE_v0_3_0_OUTWARD_POOL_INTAKE_EPA_v0_1.md` | `c0fcd56449ee40de79a58d9b0934813fd3b1e2ff` |
| `SC-NHTSA-SGO` | 5 | `PROJECT/TRACE_v0_3_0_OUTWARD_POOL_INTAKE_NHTSA_SGO_v0_1.md` | `a2128603faba36dcdbd7f6a56353e2d7536fffa2` |

Pool composition:

```text
SC-RAIB       5
SC-PAC        5
SC-EPA-FOIA2  5
SC-NHTSA-SGO  5
TOTAL        20 / 20
```

## 2. Frozen identities

Pool-wide deterministic case identity:

```text
CASE_ID = SHA256(SOURCE_COLLECTION_ID + "\n" + SOURCE_NATIVE_ID)
```

For already-clustered case units, `SOURCE_NATIVE_ID` is the frozen cluster identity recorded by the source-family intake rather than one constituent row/report.

| label | source collection | source-native case identity | CASE_ID |
|---|---|---|---|
| RAIB-1 | `SC-RAIB` | `Report 10/2023` | `7921a96b9ff7622ed84c5864aacb2202f432a29b7671b3bf642c7ff471f308f3` |
| RAIB-2 | `SC-RAIB` | `Report 11/2023` | `72d91043b10df9fe6f6e9c2fb6ac4b9ab5064d008ecf4f4fbd455d51df045e31` |
| RAIB-3 | `SC-RAIB` | `Report 07/2023` | `eb267e8b3e88f07c8a2cbf476c770acb8e29bdb2d6bc3c582abce0f2f7e2c2a7` |
| RAIB-4 | `SC-RAIB` | `Report 02/2023` | `d53834bdc3f48daf0551a84de9fcc9508a7d9b7b67ccd90c4d85b39fcb9ba94b` |
| RAIB-5 | `SC-RAIB` | `Report 05/2023` | `e5bc8b58f95a9e2c585e6db9bfd3953abdaa786aed47f67aa6533169222d4089` |
| PAC-1 | `SC-PAC` | `2022-23|7|HC259` | `6bd0b0cc9829fcdab2361ad9deb533b61446dbacaed7b9d9424f2773260fb731` |
| PAC-2 | `SC-PAC` | `2022-23|5|HC252` | `8a3509c6f9889fd5567b09e16b784c650f28453daa4b76000a47c68490ce5def` |
| PAC-3 | `SC-PAC` | `2022-23|6|HC253` | `d73d9500b0485a2f592c2a07d8e0bd525921e1838c2ded6d30b63c44251b0776` |
| PAC-4 | `SC-PAC` | `2022-23|8|HC257` | `173bb291d5cdf471946ba050f0915b630d552b1f84cbc7d7cf317bcf7d3d1733` |
| PAC-5 | `SC-PAC` | `2022-23|9|HC255` | `6bf2c8e67538aa04ac6aa985971f67a0e613d4655fd6c6eebab9caef29e4892c` |
| EPA-01 | `SC-EPA-FOIA2` | `OHSFN0507973|0507973|1|Record of Decision (ROD)|SEMS` | `f45111faa589c89c837ae4b44b7a34bc945c84ef68757d4895fd190412a8d66a` |
| EPA-02 | `SC-EPA-FOIA2` | `VAD003127578|0302526|1|Explanation Of Significant Differences (ESD)|DISPOSAL PONDS` | `7d22f8296a6b4aaa21a1b388bc7bd50dffd106f3b97b5480e2b60026060f96e3` |
| EPA-03 | `SC-EPA-FOIA2` | `NJ0570024018|0201162|4|Record of Decision (ROD)|BFSA & FIRE TRAINING AREA` | `0e66ad853ad9f5e71bae907fa8f0aa5177355963efbd9e50abe2ea644a67575c` |
| EPA-04 | `SC-EPA-FOIA2` | `MT0009083840|0801744|ESD|2022-05-03|OU4+OU7` | `ae373cd8dcafbd94242cbefc6a239ec3f555422f372782c68d90f8f25dcbad73` |
| EPA-05 | `SC-EPA-FOIA2` | `PAN000306939|0306939|1|Record of Decision (ROD)|OU 01 (OU SPECIFIC)` | `ed134be6d1ac7e4f2e957c4ca430bc1ed749fc5c00f07dd2ff3b54e0a6aa4839` |
| NHTSA-01 | `SC-NHTSA-SGO` | `SAME_INCIDENT_ID|03ad388e6676c05` | `c30fbf38dc1c4bb958c69d1aea5153d5d311732ddaa6d98373f44b34c93fa4b0` |
| NHTSA-02 | `SC-NHTSA-SGO` | `SAME_INCIDENT_ID|439627d9d2569d4` | `d0a5b777dcd0c9594dcfd24673495b4fb18def3da7ab87cb14a36c2f8d26dba9` |
| NHTSA-03 | `SC-NHTSA-SGO` | `SAME_INCIDENT_ID|420fb566c542133` | `0d0b8ea4ae3cad32e15246ef5d33cc8715c5fcc8df24215e9c2cee4ab1230f64` |
| NHTSA-04 | `SC-NHTSA-SGO` | `SAME_INCIDENT_ID|5628c7d47cd45e9` | `811f32e7904c2962f2ce4dd8e4bb39835b2eb5ad8b79b23c1afdf731adec3b2f` |
| NHTSA-05 | `SC-NHTSA-SGO` | `SAME_INCIDENT_ID|84d4fa517d86789` | `98523b61c535cd054bd25b6f41fe063daa97556bc1271b0f8a8096091b055099` |

## 3. NHTSA completion note

The final five entries were frozen from exact uploaded NHTSA archive carrier bytes after byte/SHA-256 verification.

The NHTSA case unit is an official `Same Incident ID` cluster. Constituent `Report ID` / `Report Version` rows remain preserved in the NHTSA intake and do not become independent cases merely because they are separate reports.

```text
REPORT_RECORD != NECESSARILY_DISTINCT_REAL_WORLD_CRASH
ADS_SELECTED_FIRST != ADS_MORE_IMPORTANT
```

No substantive NHTSA narrative analysis occurred before these identities were frozen.

## 4. Freeze consequence

No additional real-world case may be substituted into this 20-case pool because it appears more favorable, clearer, more dramatic, or more likely to expose a TRACE distinction.

A later source correction may be preserved and may force an explicit pool-integrity decision, but it must not silently rewrite this object.

```text
FROZEN_POOL != IMMUNE_TO_CORRECTION
CORRECTION != SILENT_SUBSTITUTION
LATER_DISCOVERY != POST_HOC_CASE_SHOPPING
```

## 5. Next execution boundary

The source-family intake phase is complete.

Before deterministic efficacy-case selection, perform only the already-earned narrow currentness repair so derived mutable-state surfaces expose whether their values are live, snapshot, stale, or unknown and provide the route needed to reacquire them.

Then:

```text
20/20 POOL FROZEN
-> narrow currentness repair
-> deterministic efficacy-case selection
-> frozen case packets
-> cold paired Arm A / Arm T comparison
-> blind adjudication
-> expansion / placement / redesign / containment map
```

No F11 is earned by completing the pool. No merge, release, canon, validation, authority, permission, or clearance follows from this freeze.
