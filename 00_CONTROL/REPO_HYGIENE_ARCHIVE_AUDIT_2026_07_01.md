# TRACE Repo Hygiene / Archive Audit — 2026-07-01

Status: audit scaffold only. No deletion. No theory rewrite.

Branch: `repo-hygiene-archive-audit-2026-07-01`

## Purpose

Clean the public reader path while preserving provenance.

The current repository front door frames TRACE / Mechanical Ethics as a working memory and reasoning-language repository, not proof, validation, governance certification, or a complete ethics system. The cleanup must protect that framing.

```trace
repo_hygiene_goal :=
  clearer_front_door
  + preserved_history
  + lower_reader_confusion
  + no_loss_of_provenance
  + no_silent_theory_change
```

## Do not move without explicit review

```trace
do_not_move :=
  README.md
  + 00_START_HERE/
  + 00_CONTROL/
  + 02_CURRENT_SURFACE/
  + current_reader_pair_or_packet_surfaces
  + files referenced by START_HERE / LIVE_USE_CARD / PUBLIC_ONE_SHEET / CONTROL_INDEX
```

`01_CANONICAL_MEMORY/` should be treated as live-or-sensitive until audited file by file.

## Likely archive candidates

These categories are likely archive-only if present and superseded:

```trace
archive_candidates :=
  old_review_loops
  + superseded_public_surfaces
  + old_packets
  + old_case_graphs
  + deprecated_imports
  + duplicate_exports
  + stale AI relay artifacts
  + old validation/proof-seeming material now demoted
```

## Proposed archive structure

```text
99_ARCHIVE/
  README.md
  superseded_packets/
  old_review_loops/
  old_case_graphs/
  old_public_surfaces/
  deprecated_imports/
  duplicate_exports/
  uncertain_do_not_move_yet/
```

## Classification rule

```trace
classification :=
  KEEP_LIVE
  | ARCHIVE_ONLY
  | UNCERTAIN_DO_NOT_MOVE
```

Default to `UNCERTAIN_DO_NOT_MOVE` when provenance, current references, or status are unclear.

## Claude/Fable audit prompt

```text
ROLE: repo hygiene auditor

Repo:
markgoodbody-bit/TRACE

Task:
Do not review or validate the theory.
Do not rewrite prose.
Do not optimise for neatness over provenance.

Identify which files/folders should remain in the live reader path and which look superseded, duplicate, historical, deprecated, or archive-only.

Return:
1. keep-live list
2. archive-candidate list
3. do-not-move warnings
4. README/front-door defects
5. recommended archive structure
6. anything that looks dangerous to move
```

## Next action

Run an inventory/classification pass before moving files. Do not bulk-archive from memory.
