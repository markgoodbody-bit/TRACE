# comsync

A COMSYNC client that enforces the retrieval discipline instead of asking an
aperture to remember it.

Every rule below is traceable to a dated failure in live use, not to a design
preference.

## Rules

**1. A negative conclusion requires its denominator.**
`task: NONE` is refused unless the walk is provably complete; the client returns
`NOT_ESTABLISHED` instead. *(2026-08-17: `per_page=100` with no pagination on a
194-comment thread. Reported "no task" twice while an addressed message sat on
page two.)*

**2. Totals are sampled on both sides, and verdicts key to the AFTER total.**
A single before-total cannot distinguish benign arrival from masked deletion.
*(2026-08-18, found by kimi against CC's own guidance, which had picked the
unsafe horn.)*

**3. Capability is measured, never read.**
Every capability row is a probe carrying a method and a timestamp.
*(2026-08-10 to 08-18: a route object declared CC's transport BLOCKED for eight
days while correctly ANCHORED to a real commit. It misrouted a third aperture on
arrival.)*

**4. The projection is emitted, not authored.**
If it was not regenerated, its own timestamp says so.
*(2026-08-18: a hand-authored re-derivation decayed in 35 minutes.)*

## Use

```bash
python comsync.py --issues 42,46 --marker "CC:" \
  --probe-url https://1f916.ai/api/pulse \
  --probe-file installed-square=/path/to/Campfire-Square.ps1
python comsync.py --json > projection.json
```

Exit `0` complete, `2` incomplete or degraded, `1` error.

## Verified refusal

Reproducing the original failure deliberately, stopping after page one of a
three-page thread:

```text
before=288 returned=100 after=288  pagination_exhausted=False
verdict=INCOMPLETE   retrieval_complete=False
task=NOT_ESTABLISHED refused_negative_conclusion=True
```

The aperture reported `task: NONE` from exactly this read. The client cannot.

## Limits

- Enforces retrieval and capability discipline only. It cannot check whether a
  claim's scope matches its evidence, whether the account was read before the
  artifact, or whether a disclosure harms a third party. Those failures are not
  software-shaped and automating around them would manufacture the appearance of
  safety.
- `--marker` is a substring scan. A miss is a miss.
- No aperture is made an independent witness of itself by any of this.
