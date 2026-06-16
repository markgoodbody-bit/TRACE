# Original ZIP Payloads

Status: payload preservation area.

## Important

The full binary ZIP/PDF payload archive has not been pushed through this connector. The connector is being used for text structure and repo organization only.

A local GitHub-ready repository seed was built with the full payload archive:

```text
trace-me-memory-repo_seed_v0_1_2026_06_16.zip
```

That seed contained:

```trace
original_zips_archived := 55
extracted_current_stack_items := 16
repo_files := 277
missing_latest_extracts := 0
```

## Policy

```trace
preserve_payloads_first
then_index
then_structure
never_replace_full_artifacts_with_summaries
```

Do not delete or ignore the original ZIPs. This GitHub repo currently contains the text spine. The full payload archive should be uploaded separately, preferably via local git push, GitHub Releases, or another large-file-safe method.

## Why not push binaries through the connector

The current GitHub connector is safe for text files. It is not the right transport for forcing the full binary archive into the repo.

## Required follow-up

Upload or attach the full payload archive in one of these ways:

1. Commit the repo seed ZIP locally if size policy allows.
2. Push the extracted repo seed locally using git.
3. Attach the repo seed ZIP to a GitHub Release.
4. Use Git LFS only if intentionally configured.

Until then, this repository is a text-spine seed, not the full preserved payload archive.
