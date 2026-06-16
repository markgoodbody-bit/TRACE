# Root Cleanup Plan

Status: cleanup control note.

The repository received a manual root-level file upload dump. The current root should be kept lean:

- `README.md`
- organized directories only

Root-level uploaded artifacts should be removed from the current tree once confirmed unnecessary in root. They remain in Git history and/or the local repo seed/payload archive.

```trace
root_cleanup :=
  remove_upload_dump_from_current_tree
  + keep_history
  + keep_payload_upload_issue_open
```
