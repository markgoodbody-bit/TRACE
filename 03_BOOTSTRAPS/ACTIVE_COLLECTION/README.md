# TRACE Bootstrap Collection — Deprecated Active Surface

Date: 2026-06-16
Status: deprecated from live bootstrap surface / preserved in git history / replaced by Bootstrap V2

## Plain status

This folder is no longer the active bootstrap surface.

Bootstrap V2 now serves as the live relay-facing bootstrap layer:

`03_BOOTSTRAPS/BOOTSTRAP_V2/`

The previous per-case bootstrap collection was useful for building the material, but keeping it live beside Bootstrap V2 creates duplicate surface area and contradicts the subtraction discipline.

## Governance rule

```trace
old_active_bootstrap_collection :=
  preserved_in_history
  + deprecated_from_live_surface
  + not_current_relay_pack

current_bootstrap_surface :=
  03_BOOTSTRAPS/BOOTSTRAP_V2
```

## Reason

Bootstrap V2 consolidates the earlier case set into thematic middle-out clusters. If both layers remain live, the repo grows by addition while claiming consolidation. This folder is therefore deprecated from the live surface.

## Do not use this folder as

- current bootstrap canon;
- current external relay pack;
- validation evidence;
- active operator promotion surface.

## If old per-case files are needed

Use git history or archived local bundles. Do not re-promote the old per-case files without a specific reviewed reason.
