# Codex preliminary execution and dependency challenge

Task: [COM 954](https://github.com/markgoodbody-bit/COM/issues/954),
`TRACE-06-FOUNDATIONS-20261116`, execution/model-challenge lane.

## Earned result

The initial immutable packet at
`09c07a4b20134c6fccec2b6eb26fa4daf612bc5e` was acquired with all eight Git
blob identities checked. Its unmodified `countermodels.py` completed on
Windows/Python 3.10.11: 18 groups, 83 passing checks. The parsed output equals
the committed `RESULTS.json`; this is semantic JSON equality, not identical
output-file bytes. The examples' declared arithmetic reproduces.

`dependency_attacks.py` adds 29 passing exact-arithmetic checks under explicitly
changed synthetic assumptions. It enumerates policies constant on observable
information cells and checks dependence, capacity and delivery boundaries.
These checks exercise the alternative models below. They do not execute a
final simulator: its pin was still absent when this return was prepared.

## What changes when an assumption changes

The initial workshop example has direct joint success `D = 0.9 * 0.8 = 0.72`,
independent fallbacks with joint success `F = 0.25`, and timely observation
before choosing a feasible fallback. Its joint outcome is
`P(D or F) = 0.72 + 0.28 * 0.25 = 0.79`.

| Changed assumption | Result in this declared variation | Consequence for the final simulator |
| --- | --- | --- |
| Direct versus fallback must be selected exclusively before the cutoff; D is learned too late | Best common precommitted policy is `max(0.72, 0.25) = 0.72` | Do not let a policy read the hidden state or use an unavailable contingent action. Early observation restores 0.79. |
| Fallbacks require two simultaneous units but only one is available | Joint success is 0.72 | Resource checks must compose across participants. A second available unit restores 0.79 in this variation. |
| Van/room marginals remain 0.9 and 0.8; dependence is unspecified | Direct success can range from 0.70 to 0.80; with the independent fallback pair, total ranges from 0.775 to 0.85 | A product requires a declared independence assumption. |
| Each fallback marginal remains 0.5; their dependence varies, independently of D | Their joint success ranges from 0 to 0.5; total ranges from 0.72 to 0.86 | Separate fallbacks need not be independent fallbacks. |
| D and the fallback-pair marginals remain 0.72 and 0.25; their dependence varies | Their union ranges from 0.72 to 0.97 | Marginals alone cannot identify 0.79. |
| Acknowledgement arrives early; actual delivery arrives after the due time | Timely-delivery goal fails if the backup was cancelled; a retained timely backup succeeds | A promise/receipt must not be counted as the delivered effect. |

The ranges follow directly from nonnegative four-cell joint distributions:
`max(0,p+q-1) <= P(A and B) <= min(p,q)`. They are model-sensitivity bounds,
not confidence intervals. The script checks attainable endpoints and the
independent interior case.

Two controls retain constructive outcomes: restored fallback capacity recovers
the cooperative route; actually delivered recurring support enables a
maintenance plan that otherwise runs out of resources. A corrected model
should retain these opportunities as well as reject infeasible combinations.

## Preservation and numerical provenance checks to apply to the final pin

- The released v0.5 source remains the reference. Its F07 and correction section
  require compatible clocks, feasible completion bounds and shared-resource
  scheduling. `T_protective_effect < T_hardening` is strict; a separately declared
  ordinary delivery-*by*-due contract may be inclusive. A numerical equality
  boundary must carry its contract and event ordering.
- F09 requires an affected scope, horizon, baseline and measure. A prospect
  comparison must not silently change those when changing its joint law.
- Tests with constant `2 <= 1`, an empty admissible set, or equal capacities
  assigned by construction demonstrate their encoding, not a scheduler,
  normative decision procedure or causal promise model. This limits the 83
  passing checks' coverage; it does not falsify their stated arithmetic.
- The forthcoming parameterised simulator should reject impossible probability
  laws or return an explicit unknown. The initial CLI accepts no model input;
  this is a test requirement, not a discovered user-input vulnerability.
- A preservation span/checksum pass is distinct from retaining meaning. This
  lane will execute its mechanical check when pinned; Build owns the substantive
  full-source preservation/architecture audit.

Selected v0.5 source passages were read for these execution requirements, not
the entire release as a fresh preservation audit. The frozen release Git blob
is `39d943b26dd355781f2d01986b229b4f1da6c793` at
`d688c149afc15c90ab51afaf08fe303771e9de20`.

## Review exposure and unresolved work

Codex read the initial README, synthesis and countermodel code before writing
the independent dependency cases. CC's return `6932365622` arrived after the
first 29-check execution and was then read; its observation-timing challenge
overlaps this one. That is a distinct return, not independent empirical
validation or a blinded experiment. A literal constant check in this local
draft was then replaced by an actual delivery/backup transition calculation.

The final simulator, preservation manifest and integrated source map are
pending. This packet establishes neither their correctness nor preservation
of all TRACE meanings. No release, field efficacy, model-worker execution or
provider operation occurred. These files contain synthetic/public-source
material only.

Run from this directory:

```text
python -I -S -B dependency_attacks.py --output DEPENDENCY-RESULTS.json
```

`REPRODUCTION.json` binds the acquired initial sources and executed local
artifacts by SHA-256. It is an execution receipt, not an authenticated account
of world conditions.
