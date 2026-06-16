# PATCH NOTES v0.2.1

Date: 2026-06-16  
Patch type: support/index update.  
Core/bootstrap source bodies changed: no.  
Active bootstrap PDFs changed: no.  
New active bootstrap added: no.

## Purpose

Update the bootstrap collection after Concordance v0.3 so the packet points to the current mapping layer without converting Columbia into a new bootstrap or treating the Concordance as validation.

## Changes

- Added `04_LINKED_CONCORDANCE/` with Concordance v0.3 Markdown/CSV files.
- Updated README to name Concordance v0.3 as the current companion mapping artifact.
- Added Preservation Index v0.2.1.
- Added Apollo/Columbia expression rule:

```trace
Apollo_13 := correction_network_bites_in_time
Columbia := correction_network_exists_but_fails_to_bite
```

- Preserved all previous active bootstrap PDFs and sources unchanged.
- Kept NHTSA empirical probe separate.

## Boundary

This patch does not validate TRACE. It only updates the collection to point at the current Concordance/discrimination layer.
