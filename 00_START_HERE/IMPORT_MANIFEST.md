# TRACE GitHub Important Import Manifest v0.1

Date: 2026-06-16

This pack is intended to build up `markgoodbody-bit/TRACE` without recreating the root-level file dump.

## Rule

```trace
preserve_payloads_first
then_index
then_structure
never_replace_full_artifacts_with_summaries
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

## Counts

```trace
import_pack_files := 230
included_reference_zips := 7
```

## Warning

This import pack should be uploaded/pushed into the repository root as structured folders. Do not flatten it into the GitHub root.

