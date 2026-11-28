# Mathematical review: honesty, regard, responsibility and supported hope

16 November 2026. Temporary session mathematical reviewer. Independent derivations against `BRIEF.md` and the corrected `prior/EVOLVED.md`. This is a research proposal and challenge, not a release, a new theorem of ethics, an empirical hope measure, or a claim about experience. All numerical cases below are stipulated finite models, not forecasts about real people or services. No private correspondence or personal case material is used.

## 1. Surviving architecture

The four concepts can share a mathematical setting without becoming four numbers. Honesty concerns the relation between reports, evidence and their stated limits. Regard concerns which affected subjects, goals, burdens and objections enter deliberation. Responsibility concerns undertakings, powers, support and answerability. Hope concerns valued possibilities and what can discover, make, maintain or restore routes toward them. These are proposed operational roles; mathematics does not establish their full meanings.

Use a finite horizon `t=0,...,T`, a finite history `h_t`, and a declared family of possible models `M(e)` consistent with the evidence account `e`. A model specifies transition and observation laws. A policy `pi(a_t|h_t)` may use information available at time `t`; it cannot read the true model index or a hidden state merely because the evaluator can. Joint policies must respect the actual information available to each participant. A central omniscient planner is an extra assumption, not a default.

Let `I` be an explicitly bounded affected-subject index. For each `i`, keep a goal event `G_i` on complete trajectories, a burden vector `B_i`, and a representation/objection record. Keeping a separate coordinate does not establish adequate representation or consent. Omitted subjects and unmodelled effects remain open questions.

Two policy classes are distinct:

\[
\mathcal F(e,c)=\{\pi:\text{physically implementable with the declared capacities, information and support }c\},
\]
\[
\mathcal N(e,n)=\{\pi:\text{meets the declared normative conditions }n\},\qquad
\mathcal A=\mathcal F\cap\mathcal N.
\]

The conditions in `N` are explicit normative inputs: authority, consent, floors, exceptions, and how conflicts are resolved. They are not deduced from reachability or high expected benefit. The set may be only partially known. A policy which has not been certified admissible is not thereby proved forbidden; an unknown condition is also not permission. Distinguish the actual set, the modelled set and the presently certified subset.

`F` must include shared budgets, joint availability, timing and uncertainty. A promised support is represented as uncertain future delivery unless already delivered or guaranteed under a specifically declared model. A stochastic policy can be physically implementable even when its desired outcome is not certain. Do not define implementability to require success.

## 2. Corrected hope calculations

Retain the prior correction:

\[
J_{i,m}(\pi)=\Pr_m^\pi(G_i\mid e),\qquad
D_{i,m}(\pi:\rho)=J_{i,m}(\pi)-J_{i,m}(\rho).
\]

The candidate and named alternative share the same target, horizon, evidence and model. Each is a fixed information-responsive policy evaluated across all `m`. Different continuations after observations are allowed; knowing the hidden model in advance is not.

With model ambiguity, report:

\[
\underline D_i=\inf_{m\in\mathcal M}D_{i,m},\qquad
\overline D_i=\sup_{m\in\mathcal M}D_{i,m}.
\]

These are ranges over stated models, not confidence intervals. Also show the absolute prospects of both plans and their burdens. Neither `D>0` nor an admissible policy entails that the target ought to be pursued.

### Counterexample: subtracting worst cases

| Model | Candidate `J(pi)` | Alternative `J(rho)` | Paired gain |
|---|---:|---:|---:|
| `m1` | 0.8 | 0.7 | 0.1 |
| `m2` | 0.5 | 0.1 | 0.4 |

The worst paired gain is 0.1. But `min J(pi)-min J(rho)=0.5-0.1=0.4`. Subtracting worst cases compares guaranteed levels; it does not establish a 0.4 improvement in every possible world. Exact rational evaluation confirms these values.

### Conditional proposition: optional capability

If, under the same model, target and horizon, `A_old` is a subset of `A_new`, then

\[
\sup_{\pi\in A_{new}}J_{i,m}(\pi)\geq\sup_{\pi\in A_{old}}J_{i,m}(\pi).
\]

Proof: every old candidate remains in the maximization. This is set inclusion, not evidence that creating capability is free or that another person's outcomes improve. If obtaining support consumes time, creates a new obligation, reduces another participant's capacity, or changes the target, the inclusion needs to be checked again. The complete construction policy belongs in the comparison.

### Conditional proposition: additional constraints

If regard leads the decision-makers to add restrictions while all else is fixed, the permitted policy set can shrink, so the maximized value of a single actor's target can decrease. That is compatible with worthwhile moral correction. Cooperation can separately enlarge physically feasible options. Neither effect guarantees a positive total or a Pareto improvement.

### Required prohibition: the old Bellman subtraction

For a value already maximized over learning, construction and support-seeking,

\[
V(h)=\max_a Q(h,a)\quad\Rightarrow\quad Q(h,a)-V(h)\leq0.
\]

Calling the left-hand difference positive hope-creation remains wrong. Compare named complete policies, or explicitly distinguish a restricted readiness class from unrestricted planning. A better posterior assessment is not automatically a better world.

## 3. Regard and honesty: what can be represented without pretending to measure them

A vector of effects keeps distribution visible:

\[
\mathbf D_m(\pi:\rho)=(D_{1,m},\ldots,D_{|I|,m}),\qquad
\mathbf B_m(\pi)=(B_{1,m},\ldots,B_{|I|,m}).
\]

A Pareto comparison can report that every represented subject's chosen probability coordinate weakly improves, with at least one strict improvement. It cannot establish consent, adequate goals, comprehensive regard, or absence of rights violations. Positive weights in a scalar objective do not solve those problems. An extremely small positive weight can make one person's losses negligible in a trade; even large weights cannot give someone a voice.

An implementable regard record therefore includes: who is represented; whose stated goals these are; uncertainty or disagreement in representation; effects/burdens; and an actual route to refuse or correct the account where applicable. The availability of that route is an empirical/procedural condition, not a conclusion from `J`.

One narrow honesty check can be formalized without claiming to detect moral honesty. Suppose a report presents a numerical interval `C(r)` for a quantity whose values over the declared model set are `Q(M(e))`. Internal uncertainty coverage requires:

\[
Q(\mathcal M(e))\subseteq C(r).
\]

A report narrower than its own declared model uncertainty fails that check. Satisfying the check does not establish that the model set is adequate, the underlying observations true, or the speaker's intention honest. A justified model refinement may narrow the interval. Preserve the changed evidence and assumptions rather than treating narrower rhetoric as learning.

Honesty can lower a displayed forecast while improving the ability to act. Report truthfulness is therefore not a monotone function of success probability or reassurance. A confidence statement must retain its goal, horizon, model and evidence identifiers.

## 4. Responsibility as joint undertakings and support requirements

Represent an undertaking `k` as a record:

\[
c_k=(\text{bearer},\text{beneficiaries},\text{content},\text{trigger/deadline},
\text{scope},\text{acceptance},\text{support},\text{correction/succession}).
\]

None of these fields individually implies control, capability, fulfilment, blame or a durable subjective identity. A successor needs an actual assignment/acceptance route; a name or copied record does not supply it. The existence of a record does not prove an undertaking was validly made.

Let `x_kt` be a scheduled task allocation, `b_jt` a carrier's available capacity and `a_jk` the amount of that capacity needed. Feasibility requires, for each shared resource/carrier `j` and time `t`,

\[
\sum_k a_{jk}x_{kt}\leq b_{jt}.
\]

Other constraints encode ordering, deadlines, willingness, permissions and uncertainty. Unknown future availability stays unknown or is supplied by an explicitly stated stochastic model. Do not treat another agent's policy as controllable without a real coordination arrangement.

### Counterexample: separately feasible promises

Two tasks are due in the same slot. Each needs one unit; only one unit is available. Each promise is individually feasible and could have success probability one if evaluated alone. Their joint fulfilment is impossible. Reporting `(1,1)` by combining the two independent optimizations invents capacity. A lottery choosing one produces marginal success `(1/2,1/2)`, while joint fulfilment remains zero.

An added unit can change the joint outcome, given acceptance and all other conditions. The support deficit is visible without converting it into a blame number. If no feasible policy meets all commitments, record the conflict, communicate it through actual routes and examine repair. Merely naming duties does not produce the missing resource.

### Counterexample: multiplying marginal reliability

For two support events with marginal probabilities `p` and `q`,

\[
\max(0,p+q-1)\leq\Pr(A\cap B)\leq\min(p,q).
\]

With `p=q=0.9`, joint delivery can range from 0.8 to 0.9. The independent product 0.81 is one possible model, not a deduction from the marginals. Shared carriers and infrastructure can create correlation. Three or more undertakings require the full relevant dependence structure or defensible bounds.

## 5. Promises change reliance before delivery

Let `z` be an announcement, `s` a supplied capability and `eta_z` the recipient's response policy. In a stipulated structural model, evaluate

\[
J(z,s)=\mathbb E[\mathbf1_G\mid do(Z=z),do(S=s)].
\]

The recipient's response mechanism is held fixed across interventions, while its input `z` changes. In field data, these intervention values are not identified merely by observing `P(G|Z=z,S=s)`. Announcements can depend on pre-existing capability, selection and hidden circumstances. Observational association is not itself the effect of promising.

Three quantities can be kept distinct:

\[
\Delta_{announce}=J(1,0)-J(0,0),
\]
\[
\Delta_{support}=J(1,1)-J(1,0),
\]
\[
\Delta_{interaction}=J(1,1)-J(1,0)-J(0,1)+J(0,0).
\]

These are finite differences within the same stipulated causal model. They do not by themselves determine ethical responsibility or establish a universal theory of promises.

### Worked countermodel

A recipient otherwise uses a remote route with success probability `3/5`. An announcement makes them choose a direct route. Without an upgrade, direct support succeeds with probability `1/2`; an actual capacity upgrade raises that to `9/10`. In this deliberately simple model, an unannounced upgrade is not used.

| Announcement `z` | Upgrade `s` | Recipient route | `J(z,s)` |
|---:|---:|---|---:|
| 0 | 0 | Remote | 3/5 |
| 1 | 0 | Direct | 1/2 |
| 0 | 1 | Remote | 3/5 |
| 1 | 1 | Direct | 9/10 |

Announcement alone changes success by `-1/10`. The supplied upgrade under the announcement changes it by `2/5`. The complete combination improves over the original route by `3/10`. The interaction is `2/5`. A statement can change reliance while adding no capability; a real capability may remain unused without communication. A model of only delivery or only confidence misses this coupling.

Correction timing belongs in the response policy. If withdrawing an inaccurate promise before a booking deadline preserves the remote option, the outcome differs from withdrawing after that option disappears. The same eventual truth statement can therefore have different consequences depending on when it arrives. Model the lost fallback explicitly rather than assigning a generic penalty to lateness.

## 6. Supported viability, with its quantifiers exposed

For a finite fully observed deterministic-with-disturbance system, let `x` contain all variables needed for continuation: resources, obligations, elapsed time and relevant history. Let `S_t` be an explicitly specified acceptable-state set, `A_t(x)` the available permitted actions, `W_t(x,a)` the declared disturbances, and `f_t` the transition. A finite robust viability recursion is:

\[
K_T=S_T,
\]
\[
K_t=\{x\in S_t:\exists a\in A_t(x)\;\forall w\in W_t(x,a),
f_t(x,a,w)\in K_{t+1}\}.
\]

With a required terminal goal, use `K_T=S_T intersect G_T`; a path-dependent goal must be encoded in the augmented state. This recursion states that one available action can keep every allowed next state inside the next viable set. The existential choice is before the universal disturbance. Reversing them gives the decision-maker knowledge of the disturbance and can certify an impossible policy.

The derivation is backward induction. At `T`, membership is exactly the terminal requirement. At each preceding time, an action with all successors in `K_(t+1)` has viable continuations by the induction hypothesis; if no such action exists, every current action has an allowed successor without one. This establishes the finite conditional claim under the specified observation/control and disturbance semantics.

### Crucial limitation: fixed model uncertainty is not arbitrary switching

If the uncertainty is one unknown but fixed model `m`, taking a fresh worst model at every stage can create a stronger adversary than the problem contains. A simple two-stage reward example has a fixed `theta` in `{0,1}` with rewards `theta` and `1-theta`. Every fixed model totals one. Independently minimizing the two stages gives `0+0=0`, describing a model switch that was forbidden.

Use whole-policy evaluation `inf_m J_m(pi)`, or an augmented information state and a valid dynamic model. A pointwise robust Bellman recursion requires appropriate rectangular disturbance uncertainty or another justification of dynamic consistency. The displayed viability recursion is valid for the explicitly stagewise disturbance model it states; it is not automatically the solution to arbitrary model ambiguity.

For partial observation, an action must be shared by all states/models still indistinguishable to the actor. Use histories or information states with correct updates. Applying the fully observed recursion to hidden physical state is an oracle-policy error.

### Chance constraints are different

For stochastic support, one may instead require

\[
\Pr_m^\pi(X_t\in S_t\text{ for every }0\leq t\leq T)\geq1-\epsilon.
\]

This is a horizon-level condition, not the deterministic robust kernel. It must specify whether it holds for one model, every stated model, or a justified mixture. A 0.99 success probability at each of 100 independent stages gives `0.99^100 = 0.3660323412732295` for all stages, not 0.99.

If unconditional failure probabilities are bounded by `epsilon_t`, the union bound gives total failure at most `sum epsilon_t`. Allocating `sum epsilon_t <= epsilon` is sufficient, sometimes conservative. If instead the bounds are conditional on survival to each stage, the chain rule gives survival at least `product(1-epsilon_t)`; independence is not additionally needed for those conditional bounds. State which kind of bound is available.

Being outside a certified kernel means no route was certified under that model and requirement. It is not a proof that no route exists in the world. Unknown support is neither proven absent nor guaranteed available.

## 7. Constructive connection: support can change the feasible region

The useful link among the concepts is inspectable:

1. An honest account names models, observations, forecasts and their limits.
2. Regard gives the affected subjects and their valued trajectories a place in the account, including disagreements and burdens.
3. Responsibility connects undertakings to actual permissions, capacities, carriers, timing and correction.
4. Hope-directed work compares ways to discover, enable, maintain or restore valued possibilities within that account.

An elementary support hypergraph exposes complementarity. Suppose a remote route gives success `1/2`, and a reliable direct route requires both transport `z1` and access `z2`:

\[
J(z_1,z_2)=\tfrac12+\tfrac12 z_1z_2,\quad z_1,z_2\in\{0,1\}.
\]

Transport has zero marginal effect without access and effect `1/2` with access. The cross difference is `1/2`. A policy that rejects each support because its isolated marginal effect is zero misses the jointly enabling package. Conversely, a package can fail on shared budgets, timing or willingness; an AND-node is not evidence those dependencies will be supplied.

The architecture supports a productive question: which missing jointly feasible support would change a valued trajectory, at what cost to whom, under whose choice, and before which opportunity closes? It does not require the beneficiary personally to perform the enabling act or continuously improve an internal score.

## 8. Required repairs and surviving claims

**Required in the root synthesis:**

- Keep the distinction between actual, modelled and certified admissibility/feasibility.
- Define goals as trajectory events and retain losses when revising them.
- Keep nonanticipation and decentralized information visible.
- Check joint capacity and dependence before combining individual commitments.
- Separate announcement, delivery and recipient response; do not infer causal effects from conditional probabilities without identification.
- State the full-observation/stagewise-disturbance assumptions for a viability recurrence.
- Distinguish horizon chance constraints from one-step probabilities.
- Compare paired plans inside each model before taking model ranges.
- Do not call measured confidence, feasible-route count, probability gain or constraint satisfaction a universal hope/regard/responsibility score.
- An empty certified set is an information/coordination result; it neither creates blame nor authorizes harm or coercive goal revision.

**Survives:** corrected policy comparison; optional-set monotonicity under explicit inclusion; distribution-aware vector accounting; joint-resource feasibility; support complementarity; announcement/reliance coupling under a stated causal model; finite robust viability under the stated assumptions; and uncertainty-sensitive comparisons with correction routes.

**Not established:** empirical forecast calibration, ethical legitimacy of selected constraints, complete affected-subject coverage, subjective hope, consciousness, actual consent, general efficacy, superiority to expert practice or any new mathematics beyond the stated synthesis.

## 9. Established CC contribution: preserve, then challenge its stronger inference

The root supplied the established Claude Code return in `prior/CC-HOPE-CHALLENGE.md`. This is a separate project aperture's source reading, not one of these temporary session reviews. The return explicitly reports no new execution of the old test suite. Its exact contribution and that limit should remain attributed.

### Target probability alone can reward ruin

CC's finite counterexample is decisive against using target probability as a complete outcome assessment:

| Plan | Target attained | Secure below target | Ruin |
|---|---:|---:|---:|
| `rho` | 1/10 | 9/10 | 0 |
| `pi` | 3/10 | 0 | 7/10 |

The target gain is `1/5` while ruin probability increases by `7/10`. Keep both the valued goal `G_i` and a protective trajectory predicate `S_i`, and report `P(G_i)` alongside `P(S_i)`, relevant burden distributions and joint events when material. If the declared floor requires `P(S_i)>=19/20`, `pi` fails and `rho` passes in this toy model. That threshold is an external normative input, not a theorem. Floors can be contested; adding one safety coordinate does not prove all harms represented.

The normal-distribution variance illustration in CC's report is not needed to establish the counterexample; the finite table is sufficient. For maintenance, the protective goal may improve even while the aspirational goal's attainment probability remains unchanged. A zero aspirational delta does not mean maintenance has zero value.

### The martingale identity is correct; observed drift is not a diagnosis

Fix a model `m`, an information filtration `F_t`, a complete information-adapted policy `pi`, and a bounded terminal indicator `Y=1_G`. Define

\[
J_t=\mathbb E_m^\pi[Y\mid\mathcal F_t].
\]

Then the tower property gives

\[
\mathbb E_m^\pi[J_{t+1}\mid\mathcal F_t]=J_t.
\]

This is a valuable internal consistency condition. A fixed adaptive policy can specify different later choices after different observations; those permitted adaptations do not break the identity. Nor does ordinary Bayesian conditioning inside the fixed model. A changed target, a genuinely replaced policy or a changed probability model requires a fresh comparison, unless that revision was already represented in the original complete policy/model.

The stronger statement that a systematic observed drift *indicates miscalibration* needs substantial qualification. The expectation is under the declared model. An observed sample mean involves a sampling process, and could reflect model error, updating errors, changing populations, dependent cases, informative dropout, outcome-conditioned selection, model/target changes, or ordinary sampling variability. Multiple testing matters. Calibration and conditional temporal coherence are related but distinct properties.

Simple selection counterexample: every case begins with a correct 1/2 success forecast. At the next observation, success cases resolve at one while unsuccessful cases remain in a review queue at zero. A dashboard that keeps only unresolved cases shows a fall from 1/2 to zero under a perfectly coherent model. It is selecting on the realised information. This is not a counterexample to the martingale identity; it is a counterexample to reading the selected dashboard trend as diagnostic proof of poor calibration.

For an exploratory monitor, predeclare the cohort, goal/policy/model identifiers, update opportunities, treatment of resolved and missing cases, dependencies, and a statistical criterion. A bounded stopping rule in a complete fixed cohort does not by itself invalidate the martingale expectation, but retrospective selection of the reported cases can. Treat a flagged pattern as a reason to inspect the model and data process, not as an automatic verdict. The present simulator can verify the exact identity in a finite stipulated model; it cannot validate a field calibration diagnostic without data and design.

CC also correctly calls for author/time/contestability of models and counterfactuals, absolute prospect ranges as well as paired deltas, a separate discovery entry, and distinguishing assertion counts from independent cases. Incorporate those points. Its remembered legal citation should not be republished as verified authority without checking the primary source; the mathematical fact that free information can be ignored does not itself establish permission to impose information on a person.

## 10. Formal bridge to the released v0.5 navigator

This reviewer directly read the current TRACE `README.md` and `TRACE-v0.5.md` lines 1–250 on 16 November 2026. This is a bounded reading, not a whole-specification or donor-source reread. The resulting bridge preserves the released navigator rather than replacing it with an optimizing controller.

| v0.5 distinction or port | Proposed mathematical binding | Boundary retained |
|---|---|---|
| World, aperture, map and history | Actual transition law; participant observation kernel; represented model family; information history | A represented state is not access to the world or another agent's hidden state |
| Actor-held aims and boundaries | Separately owned trajectory predicates `G_i`, protective predicates `S_i`, burdens and normative conditions | Selection of goals/floors remains attributed and contestable |
| Feasible, permitted, chosen, executed | `F`, `N`, selected adapted policy, actual action/event record | A calculated optimum is neither authority nor actuation |
| Noticed route, formed and usable capability | Model discovery, transition/resource change, and entity/time-specific implementability | Learning a route and building a route are different changes |
| Offer, agreement and usable exit | Distinct proposal/acceptance variables and exit policy with actual dependencies | Forecast benefit does not supply consent or a usable refusal |
| Source-relative claims and evidence | Evidence-scoped model assumptions with contrary claims and freshness | Neither probabilities nor syntax authenticate witnesses |
| Participant-specific consequences and return | Vector goal/protection outcomes, burden distributions, unresolved dependencies | One participant's success is not joint success |
| Goal revision and remaining loss | Versioned event predicates with author, applies-from and retained original comparison | Better odds for a substitute target do not meet the earlier aim |
| Maintenance and external obligation questions | Resource/undertaking records, support carriers, renewals and missing-assignment states | A volunteer's offer does not transfer an institutional duty |

The minimal formal core is therefore: typed participant/claim/goal/route/undertaking records; histories and actor information; feasibility and normative interfaces; complete candidate policies; and per-goal/protection/burden comparisons with provenance. The shared-fabrication narrative can bind these elements while preserving the two participants' independent aims, alternative neutral-object activity, session-specific authority and unresolved maintenance. It does not require one global reward function.

Exploratory extensions should remain separately selected: robust viability computation, causal identification of reliance, statistical forecast monitoring, abstraction/refinement contracts, and automated policy search. Each adds assumptions and implementation burdens. Failure or absence of an extension does not make the basic navigator unusable; a successful toy extension does not validate the full language.

## 11. Recursive decomposition and compression: a preservation contract, not a fractal theorem

Reusable structure across scales is a defensible design aim. Exact mathematical self-similarity, scale invariance, or a Mandelbrot-type dynamical system has not been shown and should not be claimed merely because the same questions recur.

Let the concrete state space be `X`, the compressed space `Xbar`, and `alpha:X->Xbar` a projection. Let `gamma(xbar)={x:alpha(x)=xbar}` denote its concretization. For a concrete protective set `S`, an abstract label can certify safety only if

\[
\gamma(\bar x)\subseteq S.
\]

The weaker condition `gamma(xbar) intersect S != empty` means some represented concrete state is safe. It cannot certify that the actual one is safe. If the aggregate records only total resources, two concrete states `(2,0)` and `(1,1)` have the same total. A floor requiring each of two participants to have at least one unit holds only in the second. An aggregate total of two conceals the child-level violation.

For action claims, an abstract action must admit a realizable lifting rule using the actual actor's information. A sufficient one-step preservation condition is

\[
\forall x\in\gamma(\bar x),\;\forall w\in W(x,\lambda(x,\bar a)),\quad
\alpha(f(x,\lambda(x,\bar a),w))\in\overline{Post}(\bar x,\bar a),
\]

with `lambda` feasible, permitted and information-adapted, and `Postbar` an over-approximation of concrete successors. If `lambda` uses hidden concrete distinctions unavailable to the controller, the claimed abstract action is not implementable. For a controller seeing only `xbar`, indistinguishable states require a common permitted implementation or an information-gathering step explicitly included in the policy.

If every reached abstract state's concretization is inside the concrete protective set and all implemented transitions are included in the abstract transition relation, a safe abstract policy induces a concrete policy satisfying that protective condition. This follows by induction over the trajectory. Under-approximated outcomes, omitted burdens or unliftable actions break the inference.

Independent child guarantees also do not automatically compose. Two children can each meet their specification assuming exclusive use of the same resource; their parent cannot grant both exclusivity assumptions. Contracts must expose shared resources, interfaces, timing and dependencies, then check joint compatibility. Recursive decomposition must propagate material child limits to the parent conclusion rather than average them away.

This gives the proposed v0.6-to-1.0 development a concrete mathematical question at each refinement: which distinctions can be compressed while preserving the particular claim being made, and which must remain exposed? There is no universal lossless compression guarantee for every possible future use.

## Verification performed

The review derived the finite propositions directly. A local Python check using exact fractions confirmed the paired-difference counterexample (`1/10` versus difference of minima `2/5`) and calculated the independent 100-stage survival value. This is a narrow arithmetic check, not execution of the full architecture or a field trial. No external messaging, repository write, provider experiment or human commitment was performed by this reviewer.
