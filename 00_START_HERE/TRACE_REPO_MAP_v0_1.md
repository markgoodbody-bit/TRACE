# TRACE Repo Map / Current Work Surface v0.1

Status: navigation and repo-hygiene control note. Not canon. Not validation. Not proof. Not a new operator.

Purpose: make the repository shape legible after the first archive pass, especially recent work that is visible at root but not yet fully folded into `README.md` / `READ_ORDER.md`.

```trace
repo_map_v0_1 :=
  front_door_clarity
  + current_work_visibility
  + archive_boundary
  + no_silent_promotion
  + no_blind_archiving
```

## Reader path

For ordinary use, start with:

```text
README.md
00_START_HERE/START_HERE_NOW_v0_1.md
00_START_HERE/READ_ORDER.md
02_CURRENT_SURFACE/LIVE_USE_CARD_v0_2_1/
02_CURRENT_SURFACE/PUBLIC_ONE_SHEET_v0_3/
00_CONTROL/TRACE_Current_Control_Index_v0_1.md
```

These are the public-facing orientation and use surfaces. They do not make the whole repository current.

## Numbered working spine

The numbered folders remain the main structured navigation layer:

```text
00_START_HERE/          orientation and reader path
00_CONTROL/             anti-self-deception, control, drift notes
01_CANONICAL_MEMORY/    registries, claims/demotion, primitive/domain memory
02_CURRENT_SURFACE/     live-use and public-facing current surfaces
03_BOOTSTRAPS/          Bootstrap V2 and preserved history
03_TESTS/               comparator / test material not yet fully consolidated
04_COVERAGE/            comparator queues, worked deltas, support notes
04_KERNEL_AND_TESTS/    diagnostic kernel and preregistered test template
05_MAPS_AND_ATLASES/    concordance, scope maps, atlases, case atlas
05_OPERATORS/           operator-support material and schema patches
06_AI_PIPELINE/         AI pipeline notes and branch index material
06_REVIEWS_AND_AUDITS/  reviews, audits, falsification/drift material
07_HANDOFFS/            handoff and relay-pack material
08_ORCHESTRATION/       AI relay workflow / orchestration support
90_ORIGINAL_ZIPS/       provenance source ZIPs and handoff ZIPs
99_ARCHIVE/             preserved superseded material moved out of live path
99_ARCHIVE_INDEXES/     archive indexes and manifests
```

## Recent flat technical work

The following root-level folders are recent technical work. They are not automatically archive-only just because they sit outside the numbered spine:

```text
core/
schemas/
cases/
tests/
prompts/
reviews/
```

Current rule:

```trace
unindexed_recent_work != archive_only
```

Treat these as `CURRENT_UNINDEXED` until reviewed. They should be indexed, folded into a numbered current-work layer, or deliberately archived only after a specific map/decision.

File-level index:

```text
00_START_HERE/TRACE_CURRENT_TECHNICAL_WORK_INDEX_v0_1.md
```

## TRACE_MASTER_PACKET_v0_6

`02_CURRENT_SURFACE/TRACE_MASTER_PACKET_v0_6/` is recent current-state packet work. It is not archive material by default.

Current rule:

```trace
TRACE_MASTER_PACKET_v0_6 := current_state_packet_candidate
  + needs_front_door_decision
  - validation
  - canon_promotion
```

## Archive rule

Archive means preserved, not erased:

```trace
archive :=
  preserve_provenance
  + remove_from_live_reader_path
  + do_not_delete
  + do_not_treat_as_current
```

Do not archive material merely because it is messy, recent, flat, duplicated, or hard to explain. Archive only when it is superseded, duplicate, stale, historical, or explicitly demoted.

## Next repo-hygiene decision

The next real cleanup step is not more blind movement. It is deciding what to do with current unindexed work:

```trace
next_repo_decision :=
  index_current_unindexed_work
  | fold_current_unindexed_work_into_numbered_spine
  | archive_specific_superseded_items_after_review
```

Default until then:

```trace
default := UNCERTAIN_DO_NOT_MOVE
```

End.
