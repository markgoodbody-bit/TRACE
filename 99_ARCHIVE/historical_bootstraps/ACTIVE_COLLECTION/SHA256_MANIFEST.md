# Deprecated Active Collection Manifest

Date: 2026-06-16
Status: deprecated from live bootstrap surface / preserved in git history

This manifest formerly described `TRACE_Bootstrap_Collection_v0_7`.

That per-case collection is no longer the live bootstrap surface. The current live relay-facing bootstrap layer is:

`03_BOOTSTRAPS/BOOTSTRAP_V2/`

```trace
manifest_status :=
  historical_pointer
  + not_current_inventory

current_bootstrap_surface :=
  BOOTSTRAP_V2
```

Do not use this manifest as the current file inventory. Use the Bootstrap V2 README and Read Me First files instead.
