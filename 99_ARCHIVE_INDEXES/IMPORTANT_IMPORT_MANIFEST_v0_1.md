# TRACE GitHub Important Import Manifest v0.1

Date: 2026-06-16

A clean structured import pack has been built locally for `markgoodbody-bit/TRACE`.

```text
TRACE_GITHUB_IMPORT_IMPORTANT_v0_1_2026_06_16.zip
```

## Purpose

Build the repository up without recreating a root-level upload dump.

```trace
preserve_payloads_first
then_index
then_structure
never_replace_full_artifacts_with_summaries
```

## Build result

```trace
import_pack_files := 232
included_reference_zips := 7
missing_source_zips := 0
zip_integrity_OK := true
```

## Included layers

- Canonical memory: operator registry, memory architecture, loss-prevention, version lineage.
- Claims and demotion: Claims Ledger v0.5, Demotion Protocol v0.1.
- Current surface: Public One-Sheet v0.2 and Rosetta Current Front Door v0.3.
- Bootstraps: active v0.5 collection, including PDFs and source Markdown for Rosetta, Memento, EEAAO, Children of Men, Unthinkable, Samwise, Apollo 13, Harriet Tubman, Groundhog Day, Frankenstein.
- Kernel and tests: Diagnostic Kernel v0.2 and Pre-Registered Test Template v0.1.
- Maps and atlases: Concordance v0.6 and Case Atlas v0.4.
- Reviews and audits: AI Review Digest, Falsification & Drift Audit, Groundhog delta audit, Frankenstein delta audit, Kimi response patch.
- Handoffs: Relay Pack v0.1 and Current Stack Handoff v0.3.
- Original ZIPs: selected current and uploaded reference ZIPs.

## Upload rule

Upload/push the contents of the import pack into the repository root **as structured folders**. Do not flatten into root.

## Guard

```trace
operator_registry != source_replacement
front_door != payload_archive
summary != preservation
```
