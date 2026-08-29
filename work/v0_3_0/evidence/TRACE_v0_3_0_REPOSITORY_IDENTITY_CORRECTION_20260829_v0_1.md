# TRACE v0.3.0 repository identity correction — 2026-08-29 — v0.1

**Status:** EARNED CORRECTION / NO SOURCE OR SEMANTIC CHANGE / NOT VALIDATION

## Correction

Four JSON identities in the first bounded-package commit were calculated from
a Windows working-tree snapshot with CRLF line endings. They were then
incorrectly presented as exact package identities. Git stores the corresponding
text blobs with LF line endings, so those recorded byte counts and SHA-256
values did not identify the repository objects served by GitHub.

The package verifier now hashes indexed Git blob bytes. This makes the check
independent of checkout line-ending policy.

| Object | Superseded working-tree snapshot identity | Correct repository-object identity |
|---|---|---|
| minimum schema candidate v0.1 | 23,654 bytes / `2263dcac8306c3d47539da458756426351a74a2fc550ad833b6d120d090f21c3` | 22,774 bytes / `d50ad1e82bc5935d99c9994bdc9a3ac7c22d5f5c5ddcd1e2efc813fd8ce9a24b` |
| full candidate build report v0.1 | 18,673 bytes / `ca5461b5080d776ca4b682b9ea40c63e6b44836e8edbf57e703e50b30520e2ba` | 18,277 bytes / `b966cd3da115315565c952ddaf184e531359921b4db381b48a18a069499a400a` |
| minimum schema build report v0.1 | 1,315 bytes / `6fc056e33149997a554be5a8358b49253d7225573464e64b4f4aaffb1bd6bc7a` | 1,281 bytes / `3c960e6903f44ccada0289d5de1d476d62c835b526b79344f55b5ca5401b27a2` |
| invariant lexical coverage v0.4 | 14,812 bytes / `59258015bf2c9b89145d70dead2a5a63e7ad2ce02dcf53422aac0746d1050123` | 14,314 bytes / `6d49e8499c5ec55af99ad48e61c1f7280fd16081b6034848e39ca95b564e5bf5` |

## What did not change

- The four package blobs have the same Git blob SHA-1 identities as their
  source objects at quarry commit
  `8635438c7d5cd600dd2c8d50322353e59d27b70e`.
- No source text, JSON value, schema meaning, build result or evidence result
  changed.
- The compact spine and full working candidate byte identities were unaffected.
- This correction does not reproduce the build, establish semantic correctness
  or validate TRACE.

## Governance result

`REPOSITORY_OBJECT_IDENTITY != WORKING_TREE_SNAPSHOT_IDENTITY` when checkout
normalization can change bytes.

Future exact identity records must state the representation being hashed. For
version-controlled candidate packages, the default is the indexed Git blob;
a working-tree hash is admissible only when it is explicitly labelled with its
line-ending or other transformation conditions.
