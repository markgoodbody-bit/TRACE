# Mathematical synthesis: a compass for supported possibilities

Research candidate · 16 November 2026 · foundation work toward TRACE 0.6, with 1.0 a destination.

**Purpose:** make change, harm, formation, worthwhile possibilities, correction and answerability usable across contexts. This construction integrates known mathematical tools. It does not derive ethics from probability, define felt hope, establish artificial experience or claim new mathematical theorems.

## 1. Start with distinctions, not a single score

The proposed local account is
\[
\mathcal L_t=(E_t,V_t,C_t,F_t,N_t,P_t).
\]
This is a typed interface proposal:
- \(E_t\): evidence, claims, sources, time, disagreements and correction history.
- \(V_t\): affected subjects, attributed goals, burdens, representation and usable objection/refusal.
- \(C_t\): self-undertakings, social promises, offers and externally grounded obligations, with their different grounds.
- \(F_t\): physical implementability, information, carriers, resources and support dependencies.
- \(N_t\): stated normative requirements and permission questions, including disputes.
- \(P_t\): conditional prospects and comparisons between named complete plans.

Honesty constrains what the whole account may claim. Regard determines whose lives, possibilities and burdens enter it and who can challenge its framing. Responsibility connects undertakings to capacity, consequences and response. Hope concerns valued futures and the means that may be discovered, created, sustained or restored. These roles interact; multiplying four scores would hide their different meanings.

The model never infers consent from benefit, duty from cooperation, delivery from a promise, impossible from unknown, or moral standing from complexity. These are normative and epistemic boundaries supplied by ME/TRACE, not consequences of an optimizer.

## 2. A common mathematical setting

Use a finite horizon \(t=0,\dots,T\), history \(h_t\), an explicitly bounded participant set \(I\), and declared models \(m\in\mathcal M(E_t)\). A model supplies transition and observation laws. Each actor's policy uses only their available information; an evaluator's knowledge is not automatically the actor's knowledge.

Let \(G_i\) be an attributed goal event over a complete trajectory, \(S_i\) a protective trajectory event, and \(B_i\) a typed burden vector. An instantaneous achievement and sustained provision are different events. Preserve the original goal, losses and authorship when a goal changes.

For one complete feasible plan \(\pi\) and a credible predeclared alternative \(\rho\),
\[
J_{i,m}(\pi)=\Pr_m^\pi(G_i\mid E_t),\qquad
Q_{i,m}(\pi)=\Pr_m^\pi(S_i\mid E_t),
\]
\[
D_{i,m}(\pi:\rho)=J_{i,m}(\pi)-J_{i,m}(\rho).
\]
Report the absolute \(J,Q,B\) coordinates of both plans, plus paired differences. Use distributions or bounds for burdens where available; an expected burden alone can conceal extreme losses. Different units are not summed without a declared justified conversion.

For uncertain models, calculate each pair *inside the same model*, then report
\[
[\inf_m D_{i,m},\sup_m D_{i,m}],
\quad [\inf_m J_{i,m}(\pi),\sup_m J_{i,m}(\pi)]
\]
and corresponding baseline/protection ranges. They are model sensitivity ranges, not confidence intervals. The same information-responsive policy must be evaluated throughout. It cannot know which model is true before an actual observation distinguishes them.

A positive aspiration gain need not be desirable. In CC's counterexample, changing a plan from 0.1 attainment with otherwise secure failure to 0.3 attainment with otherwise ruin improves \(J\) by 0.2 while worsening protection by 0.7. These are stipulated figures, not real-world forecasts. Separate protective outcomes expose the trade; they do not decide its legitimacy.

## 3. Where regard enters

Regard is not \(w_i>0\) in a weighted sum. A tiny positive weight can still permit almost unlimited sacrifice of that participant. Goals, standing and burden-bearing remain contestable inputs.

The affected-subject record includes:
- the source of each goal and material boundary;
- benefits, losses and responsibilities of helpers as well as beneficiaries;
- representation gaps and disagreement;
- actual means to challenge the goal, model or proposed action;
- privacy, refusal, withdrawal and relevant externally grounded duties.

A comparison which improves by silently deleting a participant or replacing their goal is a different comparison. A source-preserving audit can detect some such changes; it cannot certify complete regard.

Constraints may narrow one actor's permitted opportunities while cooperation expands what people can do together. Neither effect has a universally positive probability delta. An opportunity count is not a moral value measure.

## 4. Responsibility connects commitment, capacity and response

Represent an undertaking as
\[
c=(kind,bearer,beneficiary,content,trigger,due,grounds,scope,
acceptance,support,review,succession).
\]
The source, validity, capacity and performance of this record are separate axes. A self-undertaking need not create a recipient's reliance. An externally grounded obligation need not originate in a voluntary promise. A loss of capacity does not automatically erase an obligation or establish blame.

For resources \(r\), slots \(t\), task allocations \(x_{kt}\), capacities \(b_{rt}\) and demands \(a_{rk}\),
\[
\sum_k a_{rk}x_{kt}\le b_{rt}.
\]
Two separately feasible undertakings may violate this joint constraint. Unknown future support stays unresolved or belongs to a declared stochastic model. A helper's own needs and other undertakings stay in the account.

Separate:
\[
\mathcal A=\mathcal F\cap\mathcal N,
\]
physical implementability and normative acceptability. Also separate actual world sets, model-relative sets and demonstrated subsets. No demonstrated acceptable plan is not proof that no plan exists. If the original commitments cannot jointly be fulfilled, notification, support-seeking, authorised revision, substitution and repair are separate possible actions with their own authority and feasibility. Impossibility does not silently rewrite the original obligation.

## 5. A promise can change another person's options before delivery

An announcement \(z\) may change a recipient's policy \(\eta_z\). Delivered support \(s\) can change actual capability. In a stipulated causal model,
\[
J(z,s)=\mathbb E[\mathbf1_G\mid do(Z=z),do(S=s)].
\]
Compare announcement, support and interaction separately:
\[
\Delta_z=J(1,0)-J(0,0),\quad
\Delta_s=J(1,1)-J(1,0),
\]
\[
\Delta_{zs}=J(1,1)-J(1,0)-J(0,1)+J(0,0).
\]
This is ordinary causal finite-difference accounting under explicit assumptions. Observational conditional probabilities do not identify these effects automatically.

An assurance can cause someone to release a backup, producing a change before anything is delivered. Correcting the assurance after the backup deadline may fix the record while leaving the lost option unrepaired. The simulator must expose that timing rather than treat a correction flag as repair.

## 6. Hope includes creating, maintaining and recovering support

A useful support package can require several contributions jointly. In one simple model,
\[
J(z_1,z_2)=\tfrac12+\tfrac12 z_1z_2.
\]
Either contribution has zero marginal effect alone; together they create a reliable route. This can expose useful cooperation that one-at-a-time ranking misses.

The repaired hope account compares complete plans. It does not subtract a value that already includes the contemplated action:
\[
V(h)=\max_a Q(h,a)\Rightarrow Q(h,a)-V(h)\le0.
\]
Learning, construction and asking for help can already belong to the initial optimum. Explicit comparison with an actual alternative restores the meaningful question.

No equation here requires constant progress, self-sufficiency or personal control. Waiting, rest, companionship and maintenance may matter without increasing the selected success probability. An unknown route has no justified probability merely because it is conceivable; an incomplete search does not establish hopelessness.

Information and world change remain distinct. For a fixed model, target and complete adaptive policy, the conditional forecast of the terminal event is a martingale. The tower property proves that identity under the model. A downward trend in selected unresolved cases does not diagnose miscalibration: removing resolved successes alone can create that trend. Statistical use needs a declared cohort, observation/selection process and test, beyond this prototype.

## 7. Recursive refinement: make compression answerable

Let \(\alpha:X\to\bar X\) compress detailed states and \(\gamma(\bar x)=\{x:\alpha(x)=\bar x\}\). A compressed state can certify a protective condition \(S\) only when
\[
\gamma(\bar x)\subseteq S.
\]
Having *some* safe detail state is insufficient. Total resources of two can represent \((1,1)\) or \((2,0)\); only the former meets a one-unit-per-person floor.

Abstract actions also need executable implementations using the actor's actual information, with all relevant concrete successors represented. Child guarantees must have compatible shared-resource, clock, consent and authority assumptions. Otherwise individually sound children can form an unsound parent.

This is the precise research interpretation of the fractal intuition: repeat a bounded pattern of inquiry while preserving the distinctions needed for the current claim. It is not a claim of exact self-similarity of people, institutions and minds.

A finite budget with merely positive costs does not ensure recursive termination: \(1/2+1/4+\dots\) remains within one. Use a finite step/depth cap, a supported positive minimum cost, or another well-founded decreasing measure. When expansion stops early, unresolved limits propagate upward.

## 8. One edition, complete and spine reading profiles

The complete specification carries definitions, assumptions, examples, objections and evidence limits. A spine is a version-pinned selective view with expansion anchors. It is not a second independently drifting authority.

A spine preservation contract should name its use class and material distinctions. A compressed packet may return UNKNOWN or request expansion when those distinctions are missing. It cannot strengthen evidence, turn a proposal into consent, collapse participant outcomes, omit a decisive clock, or upgrade a toy result to field efficacy. No fixed short spine can be lossless for every possible future use.

The next test should include both seeded loss cases and useful positive construction, compare the spine with the full source and ordinary prose, and measure retained distinctions, actual decision changes, reading burden and false confidence. A cold receiver must use a correction in a downstream decision; retrieval alone is not uptake.

## 9. Integration decisions and evidence ceiling

Retained: the corrected hope comparison, all released v0.5 meanings as preservation requirements, separate participants and aims, negative space, evidence/currentness, clocks, consent, external standing, formation, refusal, repair and self-application.

Strengthened in this proposal: protective outcomes beside aspirations; joint support capacity; promise-induced reliance; explicit uncertainty over feasible versus certified routes; conservative abstraction and recursion termination; preservation evidence for complete/spine views.

Open: justified normative constraints, calibrated real-world models, discovering genuinely omitted routes, lower-burden encoding, cross-model receiver use, suitable protected-versus-valued outcomes, and field usefulness. These remain research tasks. They do not turn the whole purpose into an expert-outperformance contest.

The temporary reviewers supplied algebraic and conceptual challenges and 18 finite countermodel groups. Campfire independently reran those groups. The real CC hope return was separately read and integrated; its no-execution limit remains. Established Build/Codex/CC reviews of this new foundations packet require actual returns. Source coverage checks are not proof of semantic coverage, and local simulator tests are not validation of the full language.

