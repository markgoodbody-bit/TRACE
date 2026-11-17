# Changed spine generator: bounded Codex check

Source: **0941c4f6efc480cc125acffdca12f9e01ae76926**, Build's
`research/trace-0.6-foundations/build-reconstruction/`. Scope follows the
changed-generator return on COM954 c6945695652. No broad numerical or previously
closed review-parser baseline was rerun.

All 17 acquired file identities matched their Git blobs. The candidate and
spine delta was read. The generator change adds explicit expansion markers for
proposed/accepted room revision, supported/independent performance, old/new
aims, conditional offers/agreement and unresolved practical arrangements.

## Observed

- Supplied derived-view checker passes; review checker reports 15 partial
  reviews and 206 unresolved blocks.
- Clean regeneration preserves the review file byte-for-byte and reproduces
  the supplied spine text. All generated review blocks stay UNRESOLVED.
- A sentinel change to a selected first paragraph reaches the generated spine;
  a sentinel in the explicitly omitted later return does not. Missing and
  duplicate numbered candidate sections are rejected.
- Changing the later claim `The room opens.` to `The room does not open.` makes
  both derived-view and review-anchor checks fail. Regenerating the views makes
  their mechanical check pass again, **while review-anchor validation continues
  to reject the stale candidate digest**. The review ledger remains unchanged;
  regeneration does not reassess or repin it.
- All 17 original acquired files remain unchanged. Mutation and regeneration
  tests ran only on manifest-listed public source copies.

`RESULTS.json` contains the observed CLI exits and diagnostics. The script
retains each synthetic case under a fresh work directory; existing directories
stop a run rather than overwrite evidence.

## Limits

This checks the authored selection, source drift and review-ledger interaction.
The expansion markers are authored prose; the generator does not infer which
omitted premise matters to an unfamiliar decision. Passing these tests does not
establish faithful compression for every use, reader uptake, evidence-content
identity, semantic preservation or a justified review repin. The donor index
and new continuous case remain prose/source-review work; their historical
meaning equivalence was not independently audited here.

The supplied first-decision spine identifies its use class and omissions. It
does not purport to reproduce the whole later encounter. This check does not
promote the 15 partial reviews into completed dispositions: all 206 remain
unresolved in the mechanical inventory.

Run against an exact-byte copy of the pinned directory:

```text
python -X utf8 -E -S -B spine_checks.py --source <candidate-dir> --acquisition ACQUISITION.json --work-dir <fresh-case-dir> --output <results.json>
```

No candidate edit, merge, release, provider, Workshop queue or private-data use
occurred. Campfire integrates; a material changed stable generator or actual
downstream reader result is the next relevant invalidator.
