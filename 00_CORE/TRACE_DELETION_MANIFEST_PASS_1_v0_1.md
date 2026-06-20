# TRACE Deletion Manifest Pass 1 v0.1

Status: deletion manifest for branch `cleanup/math-kernel-prune-pass-1`.
Parent inventory:
- `TRACE_FILE_INVENTORY_FULL.tsv`
- `TRACE_CLEANUP_CANDIDATE_GROUPS.md`
- `TRACE_INVENTORY_REPORT.md`

Base HEAD from inventory:

```text
06eda32ff01d1707d1d5a8483f34fe717485171f
```

## Purpose

First cut of non-core generated bundles and relay/archive artifacts after creation of:

```text
00_CORE/TRACE_MATH_KERNEL_v0_1.md
00_CORE/TRACE_REBUILD_RULES_v0_1.md
00_CORE/TRACE_REPO_CLEANUP_MANIFEST_v0_1.md
```

This pass removes only files previously classified as `ARCHIVE_PRESERVE` by the inventory and now selected for deletion from the GitHub repo because the user has confirmed a local backup exists.

This pass does **not** delete:

```text
source notes
audit/review files
manifests/control files
math-kernel files
case files with unique source/evidence content
MIGRATE_TO_MATH candidates
HOLD_UNKNOWN files
```

## Summary

```text
files_selected_for_deletion: 27
total_bytes_selected_for_deletion: 5080487
```

## Selected deletion list

| Path | Size bytes | Blob SHA |
|---|---:|---|
| `02_CURRENT_SURFACE/FRONT_DOOR_v0_3/TRACE_BOOTSTRAP_ROSETTA_CURRENT_FRONT_DOOR_v0_3.pdf` | 70299 | `4b7b8e1ce674aeb297f50bc4be999817a2c463af` |
| `02_CURRENT_SURFACE/PUBLIC_ONE_SHEET_v0_2/TRACE_ME_PUBLIC_ONE_SHEET_v0_2.pdf` | 65079 | `cba83ef6afdf1e4ed3bef47086927bcf788013a7` |
| `03_BOOTSTRAPS/ACTIVE_COLLECTION/01_ACTIVE_BOOTSTRAP_SET/00_TRACE_ROSETTA_CORE__v6_FULL.pdf` | 72607 | `31158bdaa75601acd64c14c9bb7f046bbccbbb1d` |
| `06_REVIEWS_AND_AUDITS/KIMI_RESPONSE_PATCH_v0_1/TRACE_ME_Claims_Demotion_Protocol_v0_1_2026_06_16.zip` | 4910 | `81f6f3011389a9299059f9e88c2a3ddc453f8825` |
| `06_REVIEWS_AND_AUDITS/KIMI_RESPONSE_PATCH_v0_1/TRACE_ME_PreRegistered_Test_Template_v0_1_2026_06_16.zip` | 3815 | `57f016d43d274a484fb1508355db9417f09d4172` |
| `07_HANDOFFS/NOTEBOOKLM_SINGLE_PDF_BUILD_SPEC_v0_1/TRACE_NotebookLM_Single_PDF_Build_Spec_v0_1.md` | 6704 | `e9978c84fe7aedcf1ceee41d3987be83c869a4c8` |
| `07_HANDOFFS/RELAY_PACK_v0_1/00_READ_ME_FIRST.md` | 3599 | `2544a76df69c118f1989017ba9ab733869289b68` |
| `07_HANDOFFS/RELAY_PACK_v0_1/01_TRACE_ME_PUBLIC_ONE_SHEET_v0_2.pdf` | 65079 | `cba83ef6afdf1e4ed3bef47086927bcf788013a7` |
| `07_HANDOFFS/RELAY_PACK_v0_1/02_TRACE_BOOTSTRAP_ROSETTA_CURRENT_FRONT_DOOR_v0_3.md` | 23638 | `cd9389316fda0e0f48633be6cbfd77970b77c8f3` |
| `07_HANDOFFS/RELAY_PACK_v0_1/03_TRACE_ME_TOP_20_CLAIMS_VIEW_v0_1.md` | 9378 | `9a290fcd2fa3916edf86b55dff05cf6e63166c15` |
| `07_HANDOFFS/RELAY_PACK_v0_1/04_TRACE_ME_Diagnostic_Kernel_v0_2.md` | 19403 | `6d05996ff5cc36b00e63b6ed24901266f738ecf6` |
| `07_HANDOFFS/RELAY_PACK_v0_1/05_TRACE_ME_Concordance_v0_6.md` | 39024 | `db1a5d75dfa68a54483c660c8ffbf66ae94d2c24` |
| `07_HANDOFFS/RELAY_PACK_v0_1/06_TRACE_ME_Case_Atlas_v0_4.md` | 28628 | `44d2c0c14cb363329404e4831f2d689ee3d2ad3a` |
| `07_HANDOFFS/RELAY_PACK_v0_1/07_TRACE_ME_TOP_20_CLAIMS_VIEW_v0_1.csv` | 4326 | `657cd57fab27e4718ef577c63ac92e15564fce91` |
| `07_HANDOFFS/RELAY_PACK_v0_1/08_PROMPT_FOR_EXTERNAL_AI_REVIEW.md` | 5388 | `d9ec23a9ee18a53b7ea380cb67b00eab7f9e6600` |
| `07_HANDOFFS/RELAY_PACK_v0_1/09_SHA256_MANIFEST.md` | 579 | `0f7545651f90a90cf586c3ed86227c6f2719d47c` |
| `08_ORCHESTRATION/AI_RELAY_WORKFLOW/README.md` | 4767 | `50c88500f44712624ef14050ab9bff60c7285123` |
| `08_ORCHESTRATION/AI_RELAY_WORKFLOW/TRACE_AI_Relay_Orchestration_Notes_v0_1.md` | 5729 | `d1abbff07d00b9e3d37e5499027ad7f52d5a0231` |
| `08_ORCHESTRATION/AI_RELAY_WORKFLOW/TRACE_Retrieval_Guard_Protocol_v0_1.md` | 3164 | `6f33feec0af16ba2d5fb6afbe5c3c17f0f362cbe` |
| `90_ORIGINAL_ZIPS/TRACE_Bootstrap_Collection_v0_4_2026_06_16(3).zip` | 596963 | `017d56d355bc66b57086842e9d41d6b2273a08a5` |
| `90_ORIGINAL_ZIPS/TRACE_Bootstrap_Collection_v0_5_2026_06_16.zip` | 669539 | `5a85102b844377f2381f42f99254ae9e305c0e92` |
| `90_ORIGINAL_ZIPS/TRACE_ME_CURRENT_STACK_HANDOFF_2026_06_16(2).zip` | 1193400 | `148d9fd9d7861d420ab9bf4cf434a0e220ae51a9` |
| `90_ORIGINAL_ZIPS/TRACE_ME_CURRENT_STACK_HANDOFF_v0_3_2026_06_16.zip` | 1663687 | `7f4ddaf2d0e86a711ab5e70dc63a9ed55aebfbe6` |
| `90_ORIGINAL_ZIPS/TRACE_ME_KIMI_RESPONSE_PATCH_PACK_v0_1_2026_06_16.zip` | 16468 | `862f4d4eb6061156b38d22114e4373b954707097` |
| `90_ORIGINAL_ZIPS/TRACE_ME_RELAY_PACK_v0_1_2026_06_16.zip` | 82491 | `c5647e54ea9e4c9fcb0432ae3854cc0bbd45230b` |
| `90_ORIGINAL_ZIPS/TRACE_MEMORY_PRESERVATION_PACK_v0_1_2026_06_16.zip` | 30571 | `9644653bf1f8dd3d05d5a6da4e09e81806d1b1f5` |
| `TRACE_COMBINED_FOR_NOTEBOOKLM.pdf` | 467328 | `298ac0a671f0f3f332d251c5f404182065639c8a` |

## Verification rule

Each deletion must use the listed blob SHA at deletion time.

If a file SHA has changed, stop and re-inventory that path.

## Post-pass required checks

After deletion pass:

```text
1. Confirm branch exists.
2. Confirm core files remain.
3. Confirm selected generated/archive artifacts are absent.
4. Do not merge without review.
```
