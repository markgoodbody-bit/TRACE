# Archive Provenance

This file records archive moves made during repo hygiene.

Archive moves are not deletion in intent. They preserve the original material under `99_ARCHIVE/` and remove it from the live reader path only after the original path is no longer referenced by the front door.

## Applied moves — 2026-07-01 (Claude/Opus atomic pass)

Applied on branch `repo-hygiene-archive-audit-2026-07-01` (PR #9) using `git mv`, atomically, after full recursive tree verification of every source path (tracked and untracked; no untracked files were present, so no partial-move risk). Git recorded all entries as renames.

```text
03_BOOTSTRAPS/ACTIVE_COLLECTION/            -> 99_ARCHIVE/historical_bootstraps/ACTIVE_COLLECTION/     (10 files)
09_SANDBOX/SCIFI_CLUB/                      -> 99_ARCHIVE/sandbox/SCIFI_CLUB/                          (1 file)
02_CURRENT_SURFACE/PUBLIC_ONE_SHEET_v0_2/   -> 99_ARCHIVE/superseded_surfaces/PUBLIC_ONE_SHEET_v0_2/   (4 files)
TRACE_COMBINED_FOR_NOTEBOOKLM.pdf           -> 99_ARCHIVE/old_exports/TRACE_COMBINED_FOR_NOTEBOOKLM.pdf (1 file)
```

Total: 16 files moved as clean renames.

### Full file-level record

```text
03_BOOTSTRAPS/ACTIVE_COLLECTION/01_ACTIVE_BOOTSTRAP_SET/00_TRACE_ROSETTA_CORE__v6_FULL.pdf -> 99_ARCHIVE/historical_bootstraps/ACTIVE_COLLECTION/01_ACTIVE_BOOTSTRAP_SET/00_TRACE_ROSETTA_CORE__v6_FULL.pdf
03_BOOTSTRAPS/ACTIVE_COLLECTION/03_SUPPORT/PATCH_NOTES_v0_1_1.md -> 99_ARCHIVE/historical_bootstraps/ACTIVE_COLLECTION/03_SUPPORT/PATCH_NOTES_v0_1_1.md
03_BOOTSTRAPS/ACTIVE_COLLECTION/03_SUPPORT/PATCH_NOTES_v0_2.md -> 99_ARCHIVE/historical_bootstraps/ACTIVE_COLLECTION/03_SUPPORT/PATCH_NOTES_v0_2.md
03_BOOTSTRAPS/ACTIVE_COLLECTION/03_SUPPORT/PATCH_NOTES_v0_2_1.md -> 99_ARCHIVE/historical_bootstraps/ACTIVE_COLLECTION/03_SUPPORT/PATCH_NOTES_v0_2_1.md
03_BOOTSTRAPS/ACTIVE_COLLECTION/03_SUPPORT/PATCH_NOTES_v0_3.md -> 99_ARCHIVE/historical_bootstraps/ACTIVE_COLLECTION/03_SUPPORT/PATCH_NOTES_v0_3.md
03_BOOTSTRAPS/ACTIVE_COLLECTION/03_SUPPORT/PATCH_NOTES_v0_4.md -> 99_ARCHIVE/historical_bootstraps/ACTIVE_COLLECTION/03_SUPPORT/PATCH_NOTES_v0_4.md
03_BOOTSTRAPS/ACTIVE_COLLECTION/03_SUPPORT/PATCH_NOTES_v0_5.md -> 99_ARCHIVE/historical_bootstraps/ACTIVE_COLLECTION/03_SUPPORT/PATCH_NOTES_v0_5.md
03_BOOTSTRAPS/ACTIVE_COLLECTION/03_SUPPORT/PRESERVATION_INDEX_v0_5.md -> 99_ARCHIVE/historical_bootstraps/ACTIVE_COLLECTION/03_SUPPORT/PRESERVATION_INDEX_v0_5.md
03_BOOTSTRAPS/ACTIVE_COLLECTION/README.md -> 99_ARCHIVE/historical_bootstraps/ACTIVE_COLLECTION/README.md
03_BOOTSTRAPS/ACTIVE_COLLECTION/SHA256_MANIFEST.md -> 99_ARCHIVE/historical_bootstraps/ACTIVE_COLLECTION/SHA256_MANIFEST.md
09_SANDBOX/SCIFI_CLUB/SCIFI_CLUB_LOG.md -> 99_ARCHIVE/sandbox/SCIFI_CLUB/SCIFI_CLUB_LOG.md
02_CURRENT_SURFACE/PUBLIC_ONE_SHEET_v0_2/README.md -> 99_ARCHIVE/superseded_surfaces/PUBLIC_ONE_SHEET_v0_2/README.md
02_CURRENT_SURFACE/PUBLIC_ONE_SHEET_v0_2/SHA256_MANIFEST.md -> 99_ARCHIVE/superseded_surfaces/PUBLIC_ONE_SHEET_v0_2/SHA256_MANIFEST.md
02_CURRENT_SURFACE/PUBLIC_ONE_SHEET_v0_2/TRACE_ME_PUBLIC_ONE_SHEET_v0_2.md -> 99_ARCHIVE/superseded_surfaces/PUBLIC_ONE_SHEET_v0_2/TRACE_ME_PUBLIC_ONE_SHEET_v0_2.md
02_CURRENT_SURFACE/PUBLIC_ONE_SHEET_v0_2/TRACE_ME_PUBLIC_ONE_SHEET_v0_2.pdf -> 99_ARCHIVE/superseded_surfaces/PUBLIC_ONE_SHEET_v0_2/TRACE_ME_PUBLIC_ONE_SHEET_v0_2.pdf
TRACE_COMBINED_FOR_NOTEBOOKLM.pdf -> 99_ARCHIVE/old_exports/TRACE_COMBINED_FOR_NOTEBOOKLM.pdf
```

### Pre-move gate checks (all passed)

```text
branch                 = repo-hygiene-archive-audit-2026-07-01 (PR #9, draft, open)
README "Open first" #2 = 02_CURRENT_SURFACE/LIVE_USE_CARD_v0_2_1/... (already repointed; no card material moved)
full recursive tree    = verified for all four source paths
untracked files        = none under any source path (no partial-move risk)
destination collisions = none
```

### Side effect noted

`09_SANDBOX/` is now an empty directory on disk (SCIFI_CLUB was its only content). Git does not track empty directories, so it will not appear in the commit or in fresh clones. Left in place — not deleted — as it was not on the approved move list.

## Application note

The earlier connector-only view could not expose a full recursive file tree, so moves were deferred. This pass was run against the local git working copy, where the full tree was verified and the moves were performed atomically with `git mv`. That blocker is resolved for these four paths.

Status: applied to the working tree on branch `repo-hygiene-archive-audit-2026-07-01`. Not yet committed/pushed pending Mark's go-ahead. PR not marked ready; not merged.
