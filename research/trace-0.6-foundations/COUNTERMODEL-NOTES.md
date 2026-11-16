# Exact finite countermodels: compass, commitment and hope

16 November 2026. Temporary session reviewer; research evidence, not a new TRACE/ME release.

## Reproduce

```sh
python3 countermodels.py --output RESULTS.json
```

Python standard library only. `fractions.Fraction` retains exact probabilities and arithmetic. `RESULTS.json` is produced from the computations and contains an assertion log. No Monte Carlo sampling, real-world probability fitting, live system operation, or human experiment occurs.

**Result: 18 finite countermodel groups, with 83 passing assertions.** The assertions include bookkeeping and consequences of other checks; they are not 83 independent findings. The groups are also related. The correct headline is the set of exposed assumptions and counterexamples, not a test-count claim of validation.

## Computed versus stipulated

Every probability, resource quantity, policy response, goal event, consent assumption and transition in these examples is stipulated. Event probabilities, differences, feasible menus, viability kernels and programme outcomes are then computed from those stipulations. The output's `meaning`, `scope`, `source`, `analytic_argument`, `analytic_upper_bound` and `important_assumptions` fields are explanatory text, not measurements or algorithmic discoveries. Exact decimals are display conveniences derived from exact fractions.

The finite enumerations illustrate conditional mathematical arguments. They do not establish stakeholder standing, legitimate consent, appropriate ethical floors, emotional hope, intrinsic agency, empirical effectiveness, novelty, or calibrated real-world odds.

## Countermodels and required changes

| Group | Computed result | Implication |
|---|---|---|
| Bellman trap | Optimal inspection has old delta 0, but gains 1/2 over a blind named plan. | Preserve paired-policy comparison; do not reintroduce positive gain over an optimum already containing the action. |
| Filtering and construction | Removing a harmful shortcut lowers the selected goal optimum from 9/10 to 3/5. A costly new route can lower available success from 4/5 to 3/5. | Ethical admissibility need not improve the chosen goal. Only truly nested cost-free menus guarantee a nondecreasing optimum. |
| Regard and weights | Positive weights for both toy subjects still select the policy imposing burden on one. | A nonzero optimisation weight is not adequate regard, consent, or protection. Declared floors require independent justification. |
| Assurance and reliance | Keeping a fallback gives 13/16 success; a false certainty announcement inducing its cancellation gives 1/4, a loss of 9/16. | The receiver's response and action menu mediate the effect. An announcement can cause harm before delivery, but deception does not have a universal sign independent of context. |
| Commitment/capacity | Delivery remains 2/5 when a recorded promise is added while resources and policy are held fixed. | A record is not delivered capacity or a guarantee. A richer model may include actual promise-induced effort. |
| Announcement confounding | Observed success given an announcement is 1; intervening to make the announcement yields 1/2, with zero causal effect. | `P(Y|Z)` does not in general establish `P(Y|do(Z))`; state causal assumptions or stay descriptive. |
| Complementarity | One support has zero standalone gain and gain 1 when its complement is present. | Marginal value depends on the other dependencies. Zero standalone contribution does not establish uselessness. |
| Joint resource budget | Two one-unit commitments each fit a one-unit budget, but their conjunction does not. | Evaluate joint allocation and time windows; individual feasibility is insufficient. |
| Correlated support | Two devices sharing one supply each have availability 4/5; either device available is also 4/5, not 24/25. | Common-cause dependence can erase apparent redundancy. Multiplication of marginals requires justification. |
| Attainment versus sustaining | Attainment is 1; sustained success is 1/2. A two-period mandatory service kernel is empty without replenishment and `{1,2}` with it. | State trajectory goals and resource replenishment explicitly; first attainment is not sustained viability. |
| Per-step versus horizon risk | Each of two independent steps is safe with probability 9/10; both are safe with probability 81/100. | Local chance constraints cannot be called the same horizon guarantee. A union-bound lower bound is 4/5 here. |
| Common policy versus clairvoyance | Robust value is 0 for common deterministic policies, 1/2 with common randomisation, and 1 for falsely model-specific choices. | Fix the information available to the policy. Do not swap minimisation and maximisation or let a policy know the hidden model. |
| Paired model differences | Both paired differences are +1/10. Subtracting unpaired extrema gives the unnecessarily wide interval [-2/5, 3/5]. | Compare plans within each common model, and report absolute prospects as well. |
| Target and protection | Candidate target success improves by 1/5 while protection worsens by 7/10. | Incorporate the established CC challenge: report protective targets and failure severity, not merely success at the aspiration target. |
| Model boundary | Two completions agree on all recorded failures and disagree about an unexamined candidate. | No known route does not establish impossibility outside the model. It also supplies no evidence that an outside route exists, or any probability for it. |
| Recursion budget | Positive geometric costs sum to less than 1 at every finite step count; a uniform cost floor of 1/10 permits at most 10 paid steps. | Positive cost plus finite budget alone does not guarantee termination. Use a finite step cap or a justified uniform positive lower bound. |
| Aggregation loss | Burden vectors (1,1) and (2,0) both total 2, but differ on the declared individual floor for A. | A compressed representation must preserve distinctions required for person-specific protection. |
| Workshop programme | Baseline joint success 1/4; rescheduled direct success 18/25; with preserved observable fallback 79/100. | Joint capacity, consent, dependencies, timing, fallback and correlated outcomes can be represented in one inspectable case. |

## Worked example: two workshop groups

Two groups seek one workshop session each within the same programme window. One facilitator can serve one group per slot. Both groups may voluntarily accept different slots; the model does not infer their consent from a computed benefit.

The van is available for the whole programme with probability 9/10 and the room with probability 4/5. These two availability variables are independent of each other but **shared across both sessions**. Direct programme success requires both, so it is 18/25. Each group also has a remote fallback with probability 1/2; the fallback outcomes are independent of each other and of van/room availability. The support state is observable before the fallback deadline. Preserving those reservations does not consume conflicting resources in this example.

The declared comparison uses the same target, horizon, underlying distribution and initial opportunities:

| Plan | Both groups receive their agreed session | Each group's marginal success |
|---|---:|---:|
| Existing remote reservations | 1/4 | 1/2 |
| Promise simultaneous sessions and cancel both fallbacks | 0 | Depends on allocation; no priority is inferred or endorsed |
| Accept different slots, direct route only | 18/25 | 18/25 |
| Accept different slots; use direct support if available, otherwise preserved fallbacks | 79/100 | 43/50 |

The last policy is nonanticipative: its later choice uses a support observation actually available before the cutoff. It does not secretly know an unobservable model or future fallback outcome.

The computations are:

\[
p_D=(9/10)(4/5)=18/25,
\]
\[
J_{AB}=p_D+(1-p_D)(1/2)(1/2)=79/100,
\]
\[
J_A=J_B=p_D+(1-p_D)(1/2)=43/50.
\]

The joint gain over the named baseline is 27/50. Preserving fallbacks contributes 7/100 over the direct-only plan. The product of individual marginals is **not** the joint probability because the direct support is common. These numbers do not price the burden of facilitating or establish whether the programme should be undertaken; burden, consent and protective targets remain separate.

This case is suitable as an independent exact oracle for a parametric simulator, provided the simulator uses the same contract. Alternative reservation costs, observation cutoffs, cross-slot correlation and shared fallback resources are changes to the scenario, not arithmetic errors in this baseline.

## Analytic limits behind selected finite cases

For the hidden-model policy example, any common randomised policy chooses left with probability q. Its two success probabilities are q and 1-q. Thus `min(q,1-q) <= 1/2` for all q, with equality at q=1/2; the 101-point grid is an illustration, while this inequality establishes the bound.

For the recursion example, the finite geometric-sum identity `sum(k=0..n-1, 2^(-(k+1))) = 1 - 2^(-n)` proves that a budget of 1 is never exhausted at a finite n under that cost schedule. Testing n=100 is only an instance. This is a challenge to an implementation inference, not an allegation that a released text already asserted a termination theorem.

The deterministic viability kernel uses a fully specified capacity state, mandatory one-unit service, support before service, capacity capped at two, and a safety requirement of capacity at least one at every time. It does not prove a partially observed or stochastic viability result. The separate chance-constraint and hidden-model cases expose why those stronger claims need additional assumptions.

## Attribution and scope

- Temporary session countermodel agent authored and ran this new suite.
- The target/protection case comes from the actual established CC challenge recovered by the coordinator; the suite recomputes its finite example. It does not claim CC ran this suite.
- The recursion and aggregation attacks were suggested by the current temporary foundations reviewer and made executable here.
- The root coordinator must independently rerun the suite before claiming an independent rerun.
- The session simulator agent may reuse the worked contract; sharing this contract does not make its checks an independent empirical replication.

No clinical, family or private correspondence example is included. No established team aperture was awakened by running this local suite.
