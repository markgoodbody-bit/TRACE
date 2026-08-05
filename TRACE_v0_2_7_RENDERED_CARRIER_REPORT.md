# TRACE v0.2.7 rendered formal carrier report

**Carrier ID:** `TRACE-v0.2.7-RENDERED-FORMAL-CARRIER`  
**Status:** exact binary visually reviewed; independent exact-head review pending  

```text
NOT_CANON
NOT_VALIDATED
NOT_AUTHORITY
NOT_PERMISSION
NOT_CLEARANCE
```

## Purpose

Replace the stale mixed-format v0.5 `TRACE.pdf` with a current human-readable carrier of the released v0.2.7 formal seed while leaving the released Markdown object byte-unchanged.

The Markdown file remains the formal source. The PDF changes presentation, pagination, typography, and line wrapping only.

## Source binding

```text
released baseline main: 084a8c2ad0f5b54212b079e1a7edd7630932f6eb
formal source blob: 9238986ddc18c34709906b2fc4510d827c68d2b2
formal source SHA-256: de21182f42228a0104181fb24f245c652c3150853e14172c4174be4bb9ef03ab
wrapper SHA-256: add8d15f435b42a0d3115f0b45a52ec111152067abb3a667aa4941ee0329fcd2
```

Prior `TRACE.pdf` remains recoverable in Git history:

```text
prior blob: b3167d9859d25049b6ed11161bb62ff544baae19
prior SHA-256: 1ed0e170901d7df5a95fdec125d8c509ec5ec5df622439522d495a73e4ccc45f
prior pages: 77
prior page geometry: 48 US Letter + 29 A4
prior title: TRACE After-Fall Interface Layer v0.5 CARRIER CANDIDATE
```

## Candidate object

```text
path: TRACE.pdf
SHA-256: 8cf8233442f034d2495268fb33dfe741ad360260a61b84afab14301c675fbbc6
Git blob: c74d2dafe7870eab1b6a039cecb93d24d5c26ead
size: 313450 bytes
pages: 75
page geometry: all A4
```

## Presentation-only repairs

The generated wrapper differs from the released source in exactly two body locations:

1. the `CLOCKS` function cell in the core-glyph table is line-broken to prevent collision with the ASCII-alias column;
2. the long corresponding-path hardening equation is line-broken inside its existing aligned environment to prevent right-edge clipping.

No symbol, predicate, relation, claim, identifier, schema field, invariant, example, or prose proposition is added or removed by those repairs.

The carrier layout contains one table of contents after the title page. A duplicate Pandoc-generated pre-title table of contents exposed during exact-binary visual QA was removed before review.

## Hosted build and exact-object evidence

```text
initial materializer run: 30995111725
initial artifact: 8925848342
initial artifact ZIP SHA-256:
44326621786b2f2b980de1c2d2c9606248316974a8bda887a0799dcf6f568d81

corrected rematerializer run: 30995700552
corrected artifact: 8926082081
corrected artifact ZIP SHA-256:
75123015e125ba88b2e5247d03c8e2e88464800123afb48e6fee76328a448a1c
```

The first exact hosted binary exposed a duplicate automatically generated table of contents before the title page. It was rejected, rematerialized, and replaced by the corrected exact object above. The rejected binary was not approved for merge.

## Automated verification

```text
PDF openable: PASS
page count: 75
all pages A4: PASS
blank pages: 0
fonts embedded: PASS
minimum ink margins at 100 dpi:
  left: 70 px
  right: 16 px
  top: 32 px
  bottom: 28 px
source headings checked: 145
missing headings: 0
invariants I01-I60 checked: 60
missing invariants: 0
additional key tokens checked: 8
missing key tokens: 0
Unicode replacement characters: 0
normalized extracted-text SHA-256:
2135547767b1e14963ad9c286aeb647ad5cedc0762f9a6aa9513849aacd77442
```

## Exact-binary visual review

The corrected workflow artifact was downloaded and the exact PDF was rendered at 160 dpi. All 75 pages were inspected across 19 contact sheets, with focused inspection of the title/contents order, the core-glyph table, the long hardening equation, schema pages, worked transformations, invariants, survival kernel, and closing document-control pages.

```text
title page first: PASS
single contents sequence after title: PASS
page order and numbering: PASS
clipping: none observed
overlap: none observed
broken tables: none observed
broken equations: none observed
missing glyphs: none observed
blank pages: none
right-edge collision: none observed
```

Visual inspection is evidence about this rendered binary only. It is not evidence that the underlying framework is valid in the world.

## Claim boundary

This work does not establish TRACE's semantic adequacy, world validity, decision advantage, moral correctness, operational effectiveness, authority, permission, clearance, or canon.
