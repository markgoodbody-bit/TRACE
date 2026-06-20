# TRACE Repo Cleanup Manifest v0.1

Status: cleanup manifest / deletion-control surface.  
Authority: working manifest for the TRACE mathematical rebuild.  
Parent files:
- `00_CORE/TRACE_MATH_KERNEL_v0_1.md`
- `00_CORE/TRACE_REBUILD_RULES_v0_1.md`

Not: complete inventory, deletion execution, validation, archive execution.

## 0. Current Constraint

The repo is not code-search indexed through the available connector.

Therefore, from this environment, full repo enumeration is not currently reliable.

No mass deletion may occur until a complete file inventory is supplied or generated.

Required local inventory command:

```bash
git ls-files > TRACE_FILE_INVENTORY_2026_06_20.txt
```

Optional stronger inventory:

```bash
git ls-tree -r --name-only HEAD > TRACE_FILE_INVENTORY_TREE_2026_06_20.txt
```

## 1. Cleanup Objective

Rebuild the repository around TRACE as a mathematical middle-out modelling language.

Root form:

```math
Entity -> State -> Observation -> Belief/Uncertainty -> Action-Space -> Reachability -> Transition -> Consequence -> Update
```

Mechanical Ethics becomes the human-language constraint layer derived from TRACE outputs.

## 2. Keep Immediately

These files are known current rebuild roots and must be kept:

```text
00_CORE/TRACE_MATH_KERNEL_v0_1.md
00_CORE/TRACE_REBUILD_RULES_v0_1.md
00_CORE/TRACE_REPO_CLEANUP_MANIFEST_v0_1.md
```

## 3. Keep Unless Explicitly Reviewed

Never delete blindly:

```text
source packs
external reviews
audit logs
sha manifests
repo manifests
control files
current kernel files
unique case evidence
unique user-authored source material
```

## 4. Likely Delete / Archive Classes

After inventory, files should be marked as one of:

```text
KEEP_CORE
KEEP_SOURCE
KEEP_AUDIT
MIGRATE_TO_MATH
ARCHIVE_PRESERVE
DELETE_SUPERSEDED
HOLD_UNKNOWN
```

Likely `DELETE_SUPERSEDED` candidates:

```text
old duplicate relay packs
obsolete generated bundles
old public prose superseded by math kernel
working drafts duplicated elsewhere
stale front-door drafts replaced by kernel-rooted versions
case-note variants with no unique source/evidence content
```

Likely `ARCHIVE_PRESERVE` candidates:

```text
historically important but non-current synthesis files
old glyph-heavy scaffolds
pre-kernel essays
old case experiments
superseded reader packs with unique lineage value
```

Likely `MIGRATE_TO_MATH` candidates:

```text
files containing reusable primitives
case studies with clear state/action/reachability structures
uncertainty/future-space/harm formulations
Bluey/positive-continuation notes
entity-to-entity modelling notes
```

## 5. Deletion Safety Rule

A file may be deleted only if all are true:

```text
1. It appears in the complete file inventory.
2. It is marked DELETE_SUPERSEDED.
3. It is not a source, review, audit, manifest, or control file.
4. It has no unique mathematical primitive not migrated elsewhere.
5. It has no unique evidentiary content.
6. Its path and blob SHA are known at deletion time.
```

## 6. Required Inventory Table

When the full inventory is supplied, fill this table:

| Path | Class | Action | Dependency | Reason | Status |
|---|---|---|---|---|---|
| `00_CORE/TRACE_MATH_KERNEL_v0_1.md` | KEEP_CORE | keep | root | rebuild kernel | done |
| `00_CORE/TRACE_REBUILD_RULES_v0_1.md` | KEEP_CORE | keep | root governance | rebuild control | done |
| `00_CORE/TRACE_REPO_CLEANUP_MANIFEST_v0_1.md` | KEEP_CORE | keep | cleanup governance | deletion manifest | done |

## 7. Cut Plan

After inventory is complete:

```text
Pass 1: classify all paths.
Pass 2: identify source/review/audit/manifest/control exemptions.
Pass 3: identify duplicate generated bundles.
Pass 4: identify superseded prose files.
Pass 5: migrate useful primitives into 00_CORE or 04_CASES_REBUILT.
Pass 6: delete only DELETE_SUPERSEDED files.
Pass 7: create post-cleanup manifest.
```

## 8. Target Repo Shape

Final rebuilt shape should be small:

```text
00_CORE/
01_ME_TRANSLATION/
02_METHOD/
03_TESTS/
04_CASES_REBUILT/
05_SOURCES/
06_REVIEWS_AND_AUDITS/
90_ARCHIVE/
```

## 9. Hard Rule

Do not let cleanup become theory expansion.

Cleanup task is:

```text
inventory -> classify -> migrate -> delete/archive -> verify
```

not:

```text
write more essays
```
