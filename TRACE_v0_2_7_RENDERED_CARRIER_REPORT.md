# TRACE v0.2.7 rendered formal carrier report

**Carrier ID:** `TRACE-v0.2.7-RENDERED-FORMAL-CARRIER`  
**Status:** exact binary candidate; post-commit visual review pending  

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
SHA-256: 95df4b1fbca840f7738117ea49e1be1c00f8e4a87c5ac954a856d9e4029f7e75
Git blob: 7f6e2f8492b5df83da7fe9e50d7d19cf0d378fdf
size: 313754 bytes
pages: 76
page geometry: all A4
```

## Presentation-only repairs

The generated wrapper differs from the released source in exactly two body locations:

1. the `CLOCKS` function cell in the core-glyph table is line-broken to prevent collision with the ASCII-alias column;
2. the long corresponding-path hardening equation is line-broken inside its existing aligned environment to prevent right-edge clipping.

No symbol, predicate, relation, claim, identifier, schema field, invariant, example, or prose proposition is added or removed by those repairs.

## Automated verification

```text
PDF openable: PASS
page count: 76
all pages A4: PASS
blank pages: 0
fonts embedded: PASS
source headings checked: 145
missing headings: 0
invariants I01-I60 checked: 60
missing invariants: 0
additional key tokens checked: 8
missing key tokens: 0
Unicode replacement characters: 0
normalized extracted-text SHA-256:
9345c6d8e73df9b71a3d0c2ee666f96f0f4a6ab5a3aec9489dd3492f66c35a33
```

The exact committed binary must still be downloaded, rendered, and visually inspected before replacement approval. Until that check is integrated, this remains a carrier candidate.

## Claim boundary

This work does not establish TRACE's semantic adequacy, world validity, decision advantage, moral correctness, operational effectiveness, authority, permission, clearance, or canon.
