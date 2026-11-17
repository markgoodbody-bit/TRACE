# Codex check of the durable review layer

Assignment: [COM954 c6944634482](https://github.com/markgoodbody-bit/COM/issues/954#issuecomment-6944634482).
Exact Build source: **cb9f9b2c0c1b5b024c493d9205892f7aff26e375**,
`research/trace-0.6-foundations/build-reconstruction/`.

**Integration outcome:** Build subsequently incorporated the byte-identical
repair at **aa6fdb4934685f0737e0624d8747b804b2c817f5**. Codex acquired that
package and reproduced its five review tests, mechanical/review checks and the
same 35-case CLI matrix with zero malformed-input acceptances. The 15 partial
reviews and 206 unresolved blocks remain. See `INTEGRATED-ACQUISITION.json`,
`INTEGRATED-RESULTS.json` and `INTEGRATED-EXECUTION.json`. The original audit
and proposed-patch results below remain pinned to cb9f9b2c.

This is a distinct review-layer check. It does not rerun the completed
cancellation or broad finite-law baseline. All 16 fetched files matched Git
blob identities and remain unchanged. The patch was tested only in public-source
copies before submission; Build then integrated it. Codex did not edit or merge
Build's branch.

## Earned baseline

The mechanical checker passes (38 spans, 206 unresolved blocks). The review
checker reports **15 partial reviews anchored; 206 source blocks remain
unresolved overall**. All three `test_reviews.py` tests pass. This confirms
mechanical assertions under the supplied records, not interpretation or
semantic preservation. The reviews are explicitly same-author and partial.

An initial direct invocation with `-I` hid the sibling `build_views` module.
The documented CLI, using `-E -S -B` to retain the trusted script directory,
passes. That invocation error is not a source defect.

## Five confirmed malformed-input acceptances

`review_layer_attacks.py` supplies exact mutations of the pinned review JSON
and runs the real checker CLI. `ORIGINAL-RESULTS.json` and
`PATCHED-RESULTS.json` contain the observed exit codes, stdout and final
diagnostics for the same 35 cases. The source and candidate hashes stay valid
in these input-shape cases; this is not a stale-anchor bypass claim.

| Exact mutation | Original result | Proposed repair |
| --- | --- | --- |
| Set `schema` to JSON `true` | Exit 0, 15 partial reviews | Require integer schema 1, rejecting the boolean alias |
| Remove `reviews` | Exit 0, 0 partial reviews | Require the explicit array field |
| Set `reviews` to `{}` | Exit 0, 0 partial reviews | Reject the wrong container type |
| Set `reviews` to `""` | Exit 0, 0 partial reviews | Reject the wrong container type |
| Append a second top-level `"reviews": []` to the existing JSON object | Exit 0, 0 partial reviews; Python JSON parsing keeps the last value | Reject duplicate JSON field names at parse time |

The original CLI prints zero, so it does not falsely print fifteen. The defect
is that malformed or ambiguous data is accepted as a valid zero-review ledger.
A pipeline relying on successful exit would not distinguish that from an
intentional empty list.

`INPUT-VALIDATION.patch` adds explicit object/array/schema checks, per-review
object checks, duplicate-field rejection and explicit UTF-8 decoding. It adds
no schema, review status or semantic verdict. The patch applies to the exact
checker; with per-command `core.autocrlf=false`, its result is byte-identical
to the tested proposed file, SHA-256
`be5abda11320db357b3b4ba2a84c156f13674a197fecf484f94941a9ec392b4c`.
No Git configuration was changed persistently.

In the proposed version **all five malformed cases fail**. The valid 15-row
ledger and the existing three owner review tests still pass. An explicitly
empty `reviews: []` remains valid and reports zero partial reviews with all
206 source blocks unresolved; there is no imposed minimum review count.

## Other challenge results

- Stale source/candidate anchors, changed source/candidate bytes, a wrong block
  digest, unknown/duplicate blocks, promoted status, missing/blank findings,
  gaps, reviewers or evidence, missing evidence files and parent-path evidence
  references are rejected by both versions in the tested cases.
- On a clean copy, generation leaves `review-decisions.json` byte-for-byte
  unchanged, with 15 reviews still anchored. The generated crosswalk keeps all
  206 blocks UNRESOLVED. Regeneration therefore did not erase or promote the
  partial reviews in this test.
- Changing crosswalk/spine bytes is detected by `build_views.py --check`.
  `check_reviews.py` alone still accepts the independently valid review records.
  These guards are complementary; the review checker is not a replacement for
  the derived-view check.
- Replacing the cited `SEMANTIC-REVIEW.md` contents while keeping that filename
  passes both versions. This is a known boundary: the callback tests file
  existence, not evidence-content identity or whether it supports the finding.
  If evidence freshness is required, pin its digest/blob and reassess when it
  changes; semantic support still needs actual reading.
- Deliberately removing one otherwise valid review gives a valid 14-row ledger
  in both versions. The checker has no authenticated prior-count or withdrawal
  policy. Git/source comparison must expose that change; do not claim this
  patch prevents every deletion of a review.

## Reproduce on an exact-byte candidate copy

Pass the exact cb9f9b2c directory to the harness; it validates all source hashes.
Use fresh work directories: existing case directories cause a stop rather than
overwriting earlier receipts. The 35 generated input files and each CLI result
are retained under the chosen work directory.

```text
python -E -S -B review_layer_attacks.py --source <cb9-candidate-dir> --acquisition ACQUISITION.json --work-dir <fresh-original-dir> --output <original-results.json>
```

Apply the supplied patch in a separate copy with the repository-relative
directory layout, using `git -c core.autocrlf=false apply INPUT-VALIDATION.patch`.
The per-command setting avoids changing the tested file bytes on Windows.
Then run the same matrix with `--checker-sha256` set to the digest above and
`--expect-clean`. That override permits exactly the proposed checker difference;
the other 15 files must still match the acquired pin.

No conclusion here closes the 206 v0.5 meanings or the newly expanded v0.3/v0.4
historical reconciliation. No release, merge, provider, VM queue, private
correspondence or field test occurred.
