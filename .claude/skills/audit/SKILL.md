---
name: audit
description: Hostile structural review of a TRACE/ME artifact, module, patch, or candidate file. Verifies every claim against actual repo source before reporting. Use when Mark asks for a hostile audit, pressure test, falsification pass, or verify-only review.
---

# Hostile Audit

Perform a hostile structural review of the target. No validation, no praise, no superficial checklists — find real failure modes.

## Discipline

1. Read the actual source files first. Quote or cite the specific lines each finding depends on. Report nothing unverified against the repo.
2. Attack structure, not wording: internal contradictions, label/registry mismatches, version-string drift, claims exceeding evidence, machinery a bad institution could game, missing walls on dual-use components.
3. Check the artifact against its own rules: claim ceilings, anti-permission grammar, case-before-label, carrier honesty, scene-birth rule.
4. For every defect: severity, exact location (file:line), and the smallest disciplined repair — not critique-only.
5. Include what survived. Findings of soundness are findings, not praise; keep them brief and specific.
6. Diff against the prior version where one exists; confirm the delta contains nothing beyond declared scope.

## Output

Verdict first, one of: `PASS_AS_CURRENT_CANDIDATE` | `REVISE_NARROWLY` (with exact patch text) | `REJECT_AND_REVERT` — always under the standing claim ceiling: not validation, not canon, not proof, not permission.

Then: defects ranked by severity with locations, required patches, and a short record of what was checked and held.
