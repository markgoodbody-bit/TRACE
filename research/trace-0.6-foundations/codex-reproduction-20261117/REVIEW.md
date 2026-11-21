# Codex reproduction of Build's TRACE candidate

Task: [COM954](https://github.com/markgoodbody-bit/COM/issues/954).
Candidate tested: **32ba2e0dfd08f6301390d523771a8f504cb40419**, directory
`research/trace-0.6-foundations/build-reconstruction`.

## What changed since the previous Codex return

The earlier return tested the initial mathematical packet and supplied
alternative-assumption cases. This return executes an actual newly constructed
candidate: the simulator, delivery predicate, coverage checker and derived
views. It does not rerun the old 83-check packet.

The branch appeared during this sync. Codex first acquired and tested
`87fa30186453bffbdacb5737b167bc09d2146d70` (eight owner tests). Build then added
the explicit compatibility floor and delivery predicate in `d1eb4161`; Codex
read the intervening changes and tested that newer exact commit (nine tests).
The [prior d1eb4161 receipt](https://github.com/markgoodbody-bit/TRACE/tree/58e8afbc7f583eba24a214965af824f1b8cfedf9/research/trace-0.6-foundations/codex-reproduction-20261117)
is preserved at its immutable review commit. Build then addressed the cancellation
ambiguity at `32ba2e0d`; the current receipt binds that version (ten owner tests),
with the changed code read before execution. None is the unrecovered earlier
reported 114-unit lab, nor a final semantic-preservation return.

## Earned execution result

All 11 acquired file identities matched their Git blobs. Original candidate
files were kept unchanged; mutation/generation runs used separate local copies
of only the manifest-listed public source files. Execution used Windows and
Python 3.10.11, isolated stdlib mode. No VM queue or runtime provider was used.

| Check | Observed result | Limit |
| --- | --- | --- |
| Build's `build_views.py --check` | PASS: 38 heading spans, 206 review blocks | Mechanical inventory and drift detection, not semantic correspondence |
| Build's `test_lab.py` | 10 tests pass | Owner's finite examples |
| Separate closed-form oracle | 7,920 matches over all 330 eight-world distributions with probability multiples of 1/4, two timing modes, capacities 0–3 and demands 1–3 | This finite model and grid only; correlated support is included |
| Dependence controls | Direct/fallback overlap 0, 9/50 and 1/4 gives 97/100, 79/100 and 18/25 | Explicit joint laws, not inferred real probabilities |
| Invalid inputs | 11 cases rejected | Tested probability, world, timing and capacity boundaries; no general parser/security certification |
| Delivery oracle | 288 matches against sets of possible completed event times | Static availability/cancellation contract on one stipulated clock |
| Cancellation regression | Before-delivery cancellation prevents the backup; no earlier cancellation permits it; old keyword rejected | Three targeted checks of the clarified interface, not a general cancellation history |
| Deliberate changes | Reference, candidate, manifest and spine changes each cause a nonzero checker result | These four changes, not universal tamper detection/authentication |
| Regeneration on Windows | Generated views pass; LF-normalized text matches; raw bytes differ through CRLF translation | Do not claim cross-platform byte identity |

The separate oracle computes early success as `P(D) + P(not D and F1 and F2)`
when fallback capacity is sufficient, otherwise `P(D)`. Late success is the
maximum of the two unconditional plan probabilities. It does not copy the
simulator's enumeration of observation-dependent policies. Randomisation
cannot improve these expected values beyond the maximum of the pure plans.

For delivery, unknown arrival times are completed both before and after the
declared boundary. All-success, all-failure and mixed completion sets give
the three expected statuses. Acknowledgement is varied independently. This
checks the implemented contract; it does not establish an observed delivery.

## Resolved input meaning: cancellation relative to delivery

At d1eb4161 the predicate took `backup_cancelled` and `backup_time`, without a
cancellation time or an explicit before-delivery qualification. That ambiguity
was returned on COM954 c6944069677. Build has now renamed the flag to
`backup_cancelled_before_delivery`, documented it in the function, result basis
and README, and rejects the old keyword instead of silently interpreting it.

With primary arrival8, backup4, due6 and hardening7, the before-delivery flag
true returns NOT_SUPPORTED_IN_MODEL and false returns SUPPORTED_IN_MODEL.
The independent oracle and explicit regressions pass. This **closes the naming
and contract ambiguity for this static model**. It does not add cancellation
event histories or establish that a real backup actually delivered. Such
historical uses still require appropriate cancellation/effect times and evidence.

## Construction still open

- All 206 review blocks remain UNRESOLVED. Passing the inventory does not
  establish preservation of any unreviewed source meaning. Selected prose
  reconciliation is Build's work; this is an execution/model-challenge return.
- The simulator is a two-action, binary-observation, pooled-capacity finite
  model. It is not a general scheduler, full observation-history interpreter,
  normative-authority procedure or complete TRACE implementation.
- The carrier/controller and benefit/burden conditions now appear in candidate
  prose. The simulator's typed input does not carry them or classify controlled
  UNKNOWN; the numeric 1/8 timing difference is not that attribution test.
- A completed action across clocks, full consent/commitment histories, partial
  contributor burden and field outcomes remain outside these passes.
- The generated spine omits later paragraphs by design. Preservation and
  appropriate expansion on an unfamiliar decision need separate evidence.
- The new community-learning probe explicitly separates bounded logistics from
  evolving participation, trust and learning, and says the finite lab does not
  predict the group's social outcome. This source-level boundary is present;
  no independent reader-use or real-group validation is established by it.

The candidate openly states these broader limits. Useful finite mechanisms
have now been reproduced; complete semantic preservation remains unearned.
Campfire integrates the result. No release, hosted service change or practical
advantage over ordinary prose is claimed.

## Reproduce

Obtain the exact candidate directory from the commit above and verify it
against `ACQUISITION.json`. From this review directory, with a fresh work
directory (existing mutation directories deliberately cause a stop):

```text
python -I -S -B ../build-reconstruction/build_views.py --check
python -I -S -B -m unittest discover -s ../build-reconstruction -p test_lab.py -v
python -I -S -B independent_review.py --source ../build-reconstruction --acquisition ACQUISITION.json --work-dir ./fresh-run --output ./fresh-results.json
```

`RESULTS.json` is the observed independent result. `EXECUTION.json` binds the
owner-check results and reviewer script/output hashes. Captured stdout/stderr
hashes refer to UTF-8 text after subprocess newline decoding, not raw pipe bytes.
The source identity is pinned; later branch changes need a separate disposition.
