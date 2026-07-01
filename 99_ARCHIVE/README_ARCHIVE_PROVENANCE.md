# Archive Provenance

This file records archive moves made during repo hygiene.

Archive moves are not deletion in intent. They preserve the original material under `99_ARCHIVE/` and remove it from the live reader path only after the original path is no longer referenced by the front door.

## Pending low-risk moves from Claude/Fable audit — 2026-07-01

```text
03_BOOTSTRAPS/ACTIVE_COLLECTION/ -> 99_ARCHIVE/historical_bootstraps/ACTIVE_COLLECTION/
09_SANDBOX/SCIFI_CLUB/ -> 99_ARCHIVE/sandbox/SCIFI_CLUB/
02_CURRENT_SURFACE/PUBLIC_ONE_SHEET_v0_2/ -> 99_ARCHIVE/superseded_surfaces/PUBLIC_ONE_SHEET_v0_2/
TRACE_COMBINED_FOR_NOTEBOOKLM.pdf -> 99_ARCHIVE/old_exports/TRACE_COMBINED_FOR_NOTEBOOKLM.pdf
```

These were classified as low-risk archive candidates by the Claude/Fable hygiene audit and approved by Mark for the next pass.

## Applied moves

None yet.

## Application note

The current connector view has not exposed a full recursive file tree for these paths. Do not perform partial directory moves. Apply only when exact file list/tree entries are available, or when using local git so the move can be performed atomically with `git mv`.

## Apply prompt for Claude/Fable or local git

```text
Apply only the approved low-risk TRACE moves listed in this file.
Use git mv or an atomic equivalent.
Do not delete content.
Do not move uncertain paths.
Update this provenance file with every old_path -> new_path actually applied.
Then show git diff --stat and stop.
```

Status: ready for atomic move pass.
