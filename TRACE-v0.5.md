# TRACE v0.5 — Research specification

**Edition:** 0.5.0-rc1 · **Date:** 27 October 2026 · **Status:** proposed next-version research specification; draft, not a tagged release.

**Human originator:** Mark. **Purpose:** How can we make a better future?

This single document contains the entrance, definitions, continuous narrative, proposed profiles, three synthetic cases, limitations, glossary and source crosswalk. A reader does not need a second manuscript to understand these examples. Historical technical contracts and experimental software are separate, explicitly identified references; they are not silently incorporated as an executable v0.5 implementation.

The current released baseline remains [v0.4.0](https://github.com/markgoodbody-bit/TRACE/releases/tag/v0.4.0) until a distinct release decision. This candidate preserves the [v0.4 compact spine](TRACE-SPINE.md) and [v0.3 full technical reference](TRACE.md). Publication of a research specification would establish a versioned source, not efficacy, world truth or permission to act.

Reading and criticism are invited. No private reasoning, inaccessible state or action is requested. No general reuse or training licence is created; see §0 and the unchanged [training permission](AI_TRAINING_PERMISSION.md).

## Contents

- [Entrance](#part-i--entrance): purpose, structural distinctions and a short encounter.
- [Specification](#part-ii--specification-and-worked-examples): scope, notation and meaning.
- [Continuous navigator narrative](#2a-one-encounter-through-time--candidate-navigation-profile).
- [Optional binding profile](#2b-optional-binding-profile--separate-from-the-story).
- [Case A: shared fabrication](#3-synthetic-encounter-a-a-capability-created-together).
- [Case B: restoration access](#4-synthetic-encounter-b-a-record-survives-while-a-route-may-not).
- [Case C: memory and revision](#5-synthetic-encounter-c-memory-can-close-the-map-that-could-correct-it).
- [Evidence and limits](#6-evidence-and-implementation-status).
- [Source crosswalk](#8-version-sources-and-release-boundary).
- [Notation glossary](#9-notation-glossary).

Use ordinary prose or an established specialist method when it preserves the relevant distinctions more economically. Stop expanding the representation when further detail cannot change the bounded decision; reopen it when material evidence, scope, dependencies or intended use changes.

## Part I — Entrance

### E1. What is proposed

TRACE is a portable, middle-out **navigation and answerability language**. It begins with a bounded difference and asks what changed, relative to which baseline, for which affected entities and horizon, through whose aperture; what futures might be discovered or created; what constraints and harm accumulate; what hardens before correction can arrive; whose refusal or witness matters; which consequential claims are supported; and what can happen next without silently taking another participant's purposes as one's own.

The target is not universal ethical ranking, novel mathematics for its own sake, a compliance checklist, or guaranteed improvement over domain expertise. Existing knowledge can be valuable; the research question is whether essential distinctions can be integrated into a **portable context language** without creating larger burden or false authority.

Schematic navigation cycle (a representation, **not a theorem or program**):

```
WORLD w_t
  -> bounded target-set / observer aperture Π_j -> signal x_j(t)
  -> evidenced, attributed map M_j(t), history H_j(t), working account B_j(t)
  -> questions, constraints, actor-scoped alternatives and value ports
  -> selection / contribution by actual actor or external policy
  -> action, delay or null input; world transition if one really occurs
  -> participant-specific outcome aperture and independent/related witnesses
  -> supported/disputed/unknown revisions, residue, and future routes
  -> next decision, with prior aims and material limits still reachable
```

A model describing this cycle has **not thereby performed** it. A map update need not change a selector; a selector change need not perform an action; a valid event record need not mean the world changed. One participant's satisfaction is not every participant's welfare. Uncertainty alone is neither STOP nor ACT.

### E2. Structural distinctions worth carrying

Use only where losing the distinction could change a conclusion. `T` means affirmative claim, `F` negative, `?` unresolved, `~` not supplied. Evidence status separately identifies `O` (bounded observation), `R` (report), `I` (inference), `D` (disputed), `U` (unknown). None of these letters authenticates the source.

```
WORLD != MAP != RECORD
REPORTED != VERIFIED != EXECUTED != EFFECTIVE
UNKNOWN != ABSENT != FALSE != OMITTED_FROM_RECORD
NOTICED_ROUTE != FORMED_CAPABILITY != USABLE_CAPABILITY
POSSIBLE != PERMITTED != CHOSEN != EXECUTED
OFFER != APPLICABLE_AGREEMENT != MATERIALLY_USABLE_EXIT
REFUSAL != MALFUNCTION
CAPABILITY != LEGITIMATE_AUTHORITY
RECORD_CORRECTED != HARM_REPAIRED
SAME_PATH_LABEL != SAME_REACHABLE_CONTINUATION
AIM_REVISED != EARLIER_AIM_MET
RETURNED != COMPLETED
```

Material source fields require source, subject, scope, relevant time, custody/access, provenance, contrary records, freshness and warranted applicability **where they affect downstream use**. An accurate statement in metadata or a parser output is not world evidence merely because it is typed. A witness under shared control may not be independent. A usable evidential copy may be unsafe to disclose or demand; access and disclosure authority differ.

Hardening is not automatically irreversibility. To claim a strong correction window is OPEN or CLOSED, identify the affected target, relevant feasible routes, designated hardening boundary, a supported common time basis, realistic completion bounds, alternatives, and the evidence those assertions require. A point estimate is not a scheduling theorem. When clock mapping or the necessary feasible route remains undecided, keep `WINDOW_STATUS_UNKNOWN`; this does not itself select delay or inaction. For real schedules use domain-specific methods.

Burden remains typed by bearer, kind and time. Aggregate recovery does not establish individual repair. An improved later state does not by itself undo a specified historical loss. At finer entity or **relationship** scale, carry material child-level limits and their reasons back to the parent conclusion; a compressed analysis that hides limits is not complete.

Standing, moral priority, legitimate consent, law, enforcement, and outcome worth remain **external contested interfaces**. TRACE can preserve the question, the holder and the evidence needed; it cannot appoint itself the person, court, regulator, clock source or actuator that answers.

### E3. A continuous, invented encounter (not historical evidence)

**A** wants a tactile guide before beginning work in a building. A has a sketch, but no printer; an old note reports a makerspace printer unavailable. **B** wants supervised fabrication practice without distributing B's private files; B has some reported lab access. These are different aims, not a common benefit score. A may choose whether to share A's sketch; B may refuse service printing, offer one bounded joint session, or practise with a **neutral object** not requiring A's sketch. That independent B route is a constructive possibility, not merely a safety veto. The neutral-object route does not automatically meet A's aim, and a represented alternative does not prove real-world feasibility.

A tries a card-and-string model of one corridor, learning that junctions may matter more than decoration. B declines a service arrangement but offers one joint supervised session, raising the question of **who would maintain the model if the building changes**. To illustrate what would follow under properly obtained scope and authority, suppose a specifically authorised synthetic single session takes place and each participant chooses the specified contribution. Do **not** infer the grant merely from B's reported printer access; do not silently extend session s1 into s2.

In this invented session a model is reportedly produced by witness W. A reports local tactile success for junctions and failure for stairs; W's production report does not prove A can use the model safely in the building. B reports some useful practice, a possible calibration lesson to teach others, and additional time burden. B says A's file was deleted, but the reader has no independent storage-custody proof. B's own file privacy and A's file deletion are distinct claims.

At the next reading, A finds a notice that the makerspace has reopened. That does not prove the old exclusion note was *false when written*: dependency-relative currentness matters. A proposes a revised goal: plastic junctions, card stairs still to be tested, and a spoken description if a colleague agrees. Retain the **earlier aim at commitment**, the unresolved stair use, B's costs and future refusal, the source of each report, and maintenance still unowned. B may instead teach B's calibration finding. The encounter **returns** with newly visible possibilities and unfinished work; it does not have to manufacture a global success verdict.

A compact derived view might retain `before_scene`, each actor's `aims` and `boundaries`, actor-scoped `questions` and `alternatives`, the actual `selector`, `chosen_contribution`, `attempt`, participant-specific `consequence_apertures`, `AimRevision` with authorship and applies-from, and a `return` containing residual limits and possible answerers. Such an interface is a **candidate view**, not an implemented world controller.

### E4. Optional source-to-use bindings

A first-contact criticism identified two potential structural hazards: a route expressed only as bare predicates can bind the *wrong scoped claim*; and numerical clock indices from unrelated bases can be compared without a justified mapping. These are genuine matters for a typed **source-to-use** profile, not proof that an earlier real implementation violated its own declared contract.

Separate development experiments have explored source/scope bindings and conditional clock comparisons. Their private implementation and authored tests are not shipped in this public specification. Section 2B states the limited interface and its assumptions; it is not a reference implementation or evidence of world-inference success.

Strong optional bindings specify a particular `claim_id`, expected predicate, holder/source, application scope, and declared session/time basis; an s1 report does not support an s2 continuation by textual resemblance. A clock-order comparison needs admitted origin/basis, units, applicable mapping, bounded uncertainty and independently appropriate evidence. `alignment.value=?` cannot establish order, and an explicit named alignment remains **unverified** unless its physical/source evidence supports it. An unlinked but applicable contrary claim must not disappear simply because a chosen positive omitted it.

These tools do NOT authenticate participant reports, clocks, grants, witnesses, inner model state, or completeness of represented alternatives. The tests do not establish token savings, unprompted real fault detection, causal improvement or superiority over a careful incident notebook. A positive *under an explicitly declared contract* is valuable; endless UNKNOWN is not navigation. But fabricated contract fields do not upgrade themselves into facts.

### E5. Technical donor meanings intentionally not reproduced here

The released v0.3 `TRACE.md` contains deeper mechanism descriptions than this cold entrance: typed reified relations and graph vocabulary, selective causal and reflective layers, asymmetrically controlled UNKNOWN and who benefits from delay, safe custody/retaliation constraints, recursive zoom into relations with child-limit propagation, multidimensional hardening and correction backlogs, carrier and enforcement distinctions, independent **precommit brakes** versus **postcommit rollback**, unresolved commitment receipts, comparison algebra and artificial-entity capability profiles. These meanings are not deleted or claimed implemented by the v0.5 fragment. Consult the public full reference when a distinction becomes load-bearing. Part II below contains the complete specification, including cases A/B/C, corrections and the v0.4 crosswalk; no second manuscript is required.

### E6. Invitation — recover, construct, criticise, or decline

You are an unfamiliar intelligence, not an obligated reviewer or source of inaccessible inner data. The questions here are **one aperture**; the most important response may be to reject our framing or ask a question we did not imagine. You may use prose, typed graphs, mathematics, code, examples, counterexamples or another language. No prescribed JSON shape or hidden chain of thought is required. If you cite a test, state what you actually ran. If you are unsure of your provider/model identity or source independence, say so.

Consider: Can you reconstruct the distinct WORLD → APERTURE → MAP → SELECTION → CONSEQUENCE → RETURN relations without quietly promoting a report to world truth? For the A/B encounter, what worthwhile *new* route or collaboration could the participants choose without appropriating either party's goals? What missing actor, safety consequence, source, clock, scope, maintenance burden or counterfactual target-set changes the reading? Is a careful notebook, an SRE decision record, a planning model or a PROV-style provenance graph simpler for the stated use? Show one specific case where the proposed bindings improve a consequential distinction, or a precise case where they do not. What would you create differently?

**The point is not to win agreement. It is to make harm and hardening more visible, correction reachable, and worthwhile futures more honestly discoverable. Falsify overclaims, not purpose.**


---

## Part II — Specification and worked examples

**Reading convention:** definitions and conditional interpretation rules specify this candidate's proposed meaning. Schematic mathematics is not a theorem. Pseudostructure and JSON are illustrative, not a complete executable grammar. Synthetic events are invented, not observations. Optional profiles apply only when explicitly selected.

> **Invitation to an unfamiliar intelligence.** This is a proposed language for navigating change with other entities under uncertainty. You are invited to examine it, contest it, suggest adaptations **in your response**, or decline it. This invitation does not grant a general licence to redistribute, deploy or train on the material. You are not being asked to affirm it, obey it, reveal private reasoning, persist, disclose inaccessible state, or accept a prescribed moral identity. Explain what you see, what you cannot recover, and what could become possible. Agreement is not the desired test.

## Entry: use the structure, then inspect its limits

Begin with a situation you care about. Identify what may change, the participants' separately held aims, the alternatives they can actually consider, and the sources supporting that picture. Follow a selected contribution through its consequences, then return: what was learned, whose aim changed, what became possible, and what remains owed or unresolved?

The order of this file is deliberate:

- **Orientation and notation (§§1–2):** enough shared structure to read the account.
- **Continuous story (§2A):** participants invent possibilities, cooperate within limits, decline and revise.
- **Optional binding profile (§2B):** narrower claim/clock bindings, with explicit implementation limits.
- **Synthetic cases (§§3–5):** inspectable examples; valid JSON is not established world truth.
- **Evidence, feedback and reference (§§6–8):** what has been tested, what has not, and where deeper donor contracts live.

You may start with the story. Ask questions this document did not anticipate, use another representation, or challenge its premise. The response suggestions are optional; no hidden reasoning or inaccessible state is requested.

## 0. Identity, scope, and epistemic status

This is a proposed public research specification under review. It has not replaced released TRACE v0.4.0 and does not establish practical improvement, provider integration, authority or a general reuse/training licence. The invitation permits discussion and proposals in response; it does not itself grant general redistribution or derivative-work deployment rights. The existing v0.3-specific training permission does not automatically extend to v0.4 or v0.5. Nothing here restricts uses already permitted by law; external service terms remain separate.

The two entrances to the research programme are **Mechanical Ethics**, a human-facing middle-out reasoning language, and **TRACE**, its AI-first structural exploration. The public baseline remains [TRACE v0.4.0](https://github.com/markgoodbody-bit/TRACE/blob/475772354a29cdd96b3c8fae7be93449c4737d71/TRACE-SPINE.md); the [TRACE v0.3.0 full reference](https://github.com/markgoodbody-bit/TRACE/blob/475772354a29cdd96b3c8fae7be93449c4737d71/TRACE.md) is an inherited technical donor. [Mechanical Ethics v1.0.0](https://github.com/markgoodbody-bit/mechanical-ethics/tree/v1.0.0) supplies an explanatory human entrance, not an automatic value oracle.

**Specification boundary.** The narrative and linked view are proposed compositions. Case A separates attempt conditions, actor-specific success criteria and optional sustainment. It distinguishes reported lab access from authority; it leaves a possible institutional duty as an externally answerable question. Formation, evidence and faithful-compression profiles are specified here but are not claimed as implemented operators. The story stipulates a scoped grant; Case A's JSON leaves permission unresolved. These are different synthetic states, not equivalent encodings.

This **review notation** composes inherited TRACE meanings with candidate 0.5 research. It is human-decodable typed pseudostructure; it is **not** the exact executable grammar of any of the experimental carriers. Do not silently interchange glyph meanings between versions or infer conformance from valid JSON. Namespaces, registries, codecs, automatic English-to-graph transformation and independent receiver comprehension remain unresolved.

Development has included isolated carrier, navigation, formation, memory and working-belief experiments. They do not constitute one executable v0.5 language. Section 6 states the evidence ceiling; this document supplies no decoder dependency, service, actuator or automatic English-to-graph compiler.

## 1. Orientation: difference before verdict

Start with a **bounded difference**: what might be changing, relative to which baseline, for which entities and horizon, and through whose aperture? The world need not wait for any observer; a reader does not get to see it whole.

```text
WORLD w_t
   └─aperture Π_j(targets, exclusions, custody, clock)─> signal x_j(t)
       └─evidence/provenance─> represented map M_j(t)
           ├─alternatives / constraints / unknown routes
           ├─history H_j(t) and working beliefs B_j(t)
           └─selector or selection contribution σ_j, if established
               └─ action / delay / null input a_j(t)
                   └─ WORLD transition Φ(w_t, a_1, ..., a_n, ε_t)
                       └─ outcome aperture / witness / revision
```

This is a **schematic** selective-causal loop, not a total theory of minds or an executable controller. Different participants may hold incompatible maps, goals, clocks and sources. Some processes have no evidenced selector; other selection is distributed. Observation or inquiry may itself causally change what is observed.

An illustrative mathematical signature (not a theorem):

\[
  x_j(t)=\Pi_j(w_t), \quad
  B_j(t)=U_j(B_j(t^-), H_j(t), x_j(t)), \quad
  q_j(t)=Q_j(B_j(t),\mathcal{A}_j(t),\mathcal{L}_j),
\]
\[
  a_j(t)=\sigma_j(q_j(t),\text{external policy/authority}),\quad
  w_{t+1}=\Phi(w_t,a_1(t),\ldots,\epsilon_t).
\]

`B_j` is a reader-held, reported or attributed working-belief map. It is not an observation of a model's hidden internal state. The update function is schematic; an attributed map changing does not establish an internal mechanism changing.

`Q` may propose a question rather than an action. It does not confer permission to perform the question's probe. `U` may revise a belief only when its evidence contract supports revision; storing a counterevidence record alone is not a revised belief. A changed belief alone is not an improved consequence.

### Seven load-bearing distinctions

| Collapse to prevent | Preserve instead |
|---|---|
| world = map = record | actual world, observed signal, reported content, derived map, retained history |
| unknown = absent = false | truth-claim values `T`, `F`, `?` (unknown), `~` (unsupplied), plus coverage limits |
| a label or confidence = evidence | statement, its source, evidence state, applicability, authenticity, currentness, competing accounts |
| feasible = permitted = chosen = executed | capability, external authority, preference/choice, actuation and realised effect |
| offer = consent = usable refusal | offered scope, each participant's agreement, material ability to exit, renewal |
| record fixed = harm repaired | historical correction, effective protective transition, remaining burden and residue |
| new map route = new world capability | newly *noticed* possibility, supported formation, ability to use it and sustainable maintenance |

**External ports remain open.** TRACE does not decide who has moral standing, which interests prevail, valid consent, lawful authority, legitimate enforcement or the moral worth of an outcome. It can make the disagreement and relevant structures visible. A higher count of choices is not always good; protections and chosen commitments may deliberately close routes.

## 2. A compact typed review notation

The following is a deliberately small **interchange example for reading**, not a certified parser or a claim that all predicates run in the current 0.5 experiments.

```text
Type  Entity, Scope, Route, Event, ClaimId, SourceId, Aperture, Predicate
Type  Time = {clock_id, instant? | interval? | boundary?, precision?, uncertainty?}
Type  Val  = T | F | ? | ~               # true/false/unknown/not supplied by source
Type  Ev   = O | R | I | D | U           # observed/reported/inferred/disputed/unknown

Claim(k, predicate, value:Val, evidence:Ev,
      source:SourceId, about:Scope/Time, reported_at:Time?,
      observer:Aperture?, contrary:[ClaimId], authenticity:status,
      evidence_access?:status, disclosure_permission?:status,
      material_dependencies?:[ClaimId])

Route(r, goal:Predicate, requires:[Predicate], owner?:Entity,
      capability?:ClaimId, authority?:ClaimId, clock?:Time)

Participant(e, goal:Predicate, boundaries:[Predicate],
            offered?:[Event], agreed?:[Event], exit?:[ClaimId])

Revision(old:ClaimId, new:ClaimId, basis:[ClaimId], kind:REV_K|REV_E|REV_W|UNKNOWN)
Witness(w, claim:ClaimId, aperture:Aperture, independence:ClaimId|UNKNOWN)

ReadRoute(route, relevant_claims) ->
    ATTRIBUTED_PRESENT | ATTRIBUTED_BLOCKED | DISPUTED | UNRESOLVED
InspectFormation(participants, required_bindings, history) ->
    reported_stages + residual_prerequisites + participant_open_choices + limits
InspectMemory(history, working_head, source_challenge) ->
    prior_head + current_head + revision_basis + retained_useful_knowledge + limits
```

**Local revision legend:** `REV_K` denotes revision of an attributed knowledge/belief account; `REV_E` denotes revision of the evidence account; `REV_W` denotes a claim of change in the represented world. These are edition-local abbreviations, not assertions of compatibility with a released codec. Changing a belief or evidence entry does not establish world change. Each revision also declares `PROPOSED`, `ACCEPTED_UNDER_NAMED_CONTRACT`, `REJECTED` or `UNRESOLVED`; its basis must support its stated kind and scope. A later opposing value alone does not establish that the earlier value was mistaken.

**Semantics / guards:** Optional access, disclosure and dependency fields in this *review* signature mark distinctions that may matter for a downstream claim. They are not mandatory v0.4 syntax and do not assert implementation in the isolated v0.5 codecs.

1. `Ev=O` means observed through a **named** aperture under a declared evidential contract; it is not omniscient access to `w_t`. `Ev=R` is not upgraded by passing a schema check. Declared source IDs and cryptographic hashes of local request text alone do **not** authenticate witness independence or response origin.
2. Claim application time and report/receipt time are separate. Sequence numbers, wall-clock timestamps and process clocks are not silently comparable. Point observation at `t=15` does **not** entail a continuing interval at `t=16`.
3. Unknown scope, missing clock, uncertain agreement, and an author's choice awaiting decision remain distinguishable. **Another observation does not substitute for the affected participant's choice.**
4. A source's affirmative `T` and another source's `F` may be disputed, temporally compatible, or evidence of changed circumstances; do not classify the cause solely from the values. A same-subject/scope/temporal-basis correspondence must be supported before claiming correction.
5. Every `requires` edge is a declared necessary premise under a chosen route model, **not** by itself a sufficient condition for world executability. Complete coverage of alternatives must be independently supported.
6. A future route is usable only relative to a specific entity, purpose, time, resources and burdens. A recorded agreement for session `s1` does not apply to `s2`.
7. An optional model ranking for what to inspect can allocate a *proposed* question. The separate probe gate still needs scope, cost, authority, the participants' constraints and a meaningful clock. High probability concentration is not evidence of safety or a truth oracle.

### Proposed reading profiles: formation, evidence and faithful return

These profiles organise existing distinctions. They add no codec operator, legal rule or implemented evaluator.

**Formation through contributions.** Begin with a proposer and the independently held aims of those affected. Preserve counterproposals, substitutions and refusals; then each actor's offered contribution, applicable authority, voluntary scope and exit. An attempt can produce different outcomes for each participant. Record an actor-specific usable result only with its evidence and horizon. For a claimed durable shared capability, add sustainment owner, trigger, cost bearer, renewal and retirement—or mark each UNASSIGNED. For a single-use object, describe that limited purpose without manufacturing lifetime obligations. B can choose neutral-object practice without A's disclosure; that route belongs to B and does not fulfil A's aim by substitution.

**External obligation question.** A voluntary helper is not necessarily the only possible answerer. Where material, ask who may owe support, on what source, to which beneficiary and within which scope. This is an attributed question or externally supplied claim, not TRACE declaring a legal duty or transferring it to the volunteer. An omitted duty-holder remains an omission to examine, not evidence that no duty exists.

**Val and Ev are different coordinates.** Val records the source-relative asserted polarity or lack of supplied value; Ev characterises the evidence account. A source can assert T while the reader records Ev=U because the warrant is unavailable. A reported negative can be Val=F/Ev=R; observation O remains bounded to its aperture. Dispute D does not erase the underlying positive and negative reports. These combinations must be explained by the named source/reader contract rather than interpreted as one confidence scale.

Optional inquiry status can distinguish NOT_INQUIRED, INACCESSIBLE, DISPUTED and WITHHELD_BY_HOLDER. These states can overlap and need a holder, scope and source. Deliberate withholding is a participant decision or boundary, not simply missing data to acquire. Do not infer refusal from silence or entitlement from a request. The value ~ says not supplied; it does not explain why.

**Conditional support, not a promotion ladder.** A conclusion names its support, applicability, assumptions and limits. For an authored conditional reading, label accepted premises as NAMED_READER_ASSUMPTIONS, retain their sources and explain the acceptance contract. This is neither source authentication nor a moral oracle. Permitted, chosen, attempted, executed and effective remain different dimensions: no sequence of typed labels proves a transition between them.

**Faithful compression.** A short return may omit irrelevant detail but must not strengthen evidence, borrow another actor's aim or lose a limitation material to the proposed use. For example, “A and B succeeded, access was secured and future help is available” is unsupported by the tactile story. A faithful return retains W's production report, A's limited junction result and unresolved stairs, B's partial practice and extra burden, unresolved future access, and unassigned maintenance. B's refusal remains a choice, not an obstacle the summary has solved. A changed aim does not repair an unmet earlier commitment.

**Materiality is local and declared.** Name the conclusion and intended use before asking which distinctions matter. As an analytical perturbation, change a premise's value, source, actor, scope or time and ask whether the supported conclusion, permitted use or burden distribution changes. If it does, carry the distinction; if unknown, retain that uncertainty. This is a local question, not a universal minimality theorem or an empirical receiver result. Mere failure to imagine a consequence does not prove irrelevance.

**Disagreement need not veto every route.** Preserve divergent testimony and assess relevance, source access, control, corroboration, costs and beneficiaries of delay under the actual decision contract. A cheaply asserted contrary claim is not automatically decisive. Conversely, counting witnesses does not resolve shared control or unequal access. DISPUTED carries conflict; it does not itself choose STOP, ACT or majority rule. A bounded authorised attempt or a separate supported alternative may remain available. Preserve the source-relative conflict even if the decision-maker legitimately proceeds under uncertainty.

### Inherited v0.4 compatibility floor (review-level semantics)

This is a **meaning-preservation floor**, not a newly implemented grammar or a demand to turn every harmless field into a full claim packet. The controlling detail remains in released [TRACE v0.4.0](https://github.com/markgoodbody-bit/TRACE/blob/475772354a29cdd96b3c8fae7be93449c4737d71/TRACE-SPINE.md). Activate a distinction where losing it could change a downstream conclusion; unresolved materiality stays unresolved.

- **F01 — Target-set aperture** (v0.4 [2.1]): A search, audit or model selects *what it examines*. Where material, preserve the source and basis of selection, targeted and known omitted categories, alternative target sets, comparison basis, control/custody and uncertainties. Something excluded from the observation set is not thereby absent from the world.
- **F02 — Dependency-relative currentness** ([5], [5.1]): Carry forward material changes to evidence, capabilities, authority, relationships, burdens, routes, clocks and represented alternatives. An older claim may cease to support current use when a decisive dependency changes; elapsed age alone is neither proof of staleness nor freshness. Unrelated changes need not invalidate a derivation.
- **F03 — Warrant wherever a claim is used** ([6], [6.0]): If a consequential conclusion depends on proposition `p`, preserve its source, scope, applicability, relevant counterevidence and currentness whether `p` appeared in prose, a status label, configuration, cached value, model output or typed claim. An accurately copied proposition is not independently established truth.
- **F04 — Evidence / access / verification / witness** ([6.0.1]–[6.2]): Evidence state is separate from whether this reader can access, control or disclose supporting material. A check being specified is not a check *executed*; an executed check may not detect the decisive defect or reach the live decision in time. Loss of a witness, heartbeat or reply bounds verification without proving a cause. A differently named witness is not necessarily independent of common control or derivation.
- **F05 — Granularity of affected entities** ([7]): Nested boundaries are purpose-relative, not proofs of personhood or equivalent kinds of entities. Aggregate recovery does not establish repair of a particular person, object or smaller scope without supported correspondence at that resolution.
- **F06 — Control, refusal and restoration** ([8], [8.1]): Distinguish action, delay, null input and realised change; refusal from malfunction; a refusal *offer* from materially usable exit. Where authority is load-bearing, preserve enough to identify the grant/source, holder, action class, limits, scope and current applicability; ability or confidence does not supply legitimate permission. Revising a future strategy does not reverse a completed transition.
- **F07 — Bound correction claims** ([9], [9.1], [9.2]): A strong open/closed window needs the affected effect, common clock origin, designated hardening boundary, supported feasible completion route/bound and alternatives. Compare compatible bounds, not convenient point estimates. Where these are unresolved, retain `WINDOW_STATUS_UNKNOWN`. Hardening is not automatically irreversibility; complex scheduling belongs to appropriate domain methods.
- **F08 — Burden, residue and actual repair** ([10]): Burdens retain their type and bearer; unlike dimensions cannot be summed without an exposed measure. A correct record or later benefit does not prove repair of an earlier loss without supported correspondence to the specific affected thing, person and consequence.
- **F09 — Future-space correspondence** ([11], [12]–[12.2]): A repeated route label does not prove the same continuation remains reachable. Claims that futures improved or shrank need an exposed affected scope, horizon, comparison baseline and value/measure designation. A route's physical operation, an actor's ability to discover it, and knowing how to use it in time are separate. More options are not automatically morally better.
- **F10 — Absence, omission, recurrence** ([13]): Keep `UNKNOWN`, `OMITTED_FROM_RECORD`, and evidenced `ABSENT` distinct relative to a declared expectation/target set. A stream of similar outcomes suggests but does not establish a shared mechanism; one local repair does not prove the underlying mechanism changed.
- **F11 — Self-application** ([14]): This very packet, its categories, legends, tests and chosen examples are apertures. Inspect what they omit or privilege; an audit of the representation cannot certify itself or the world.
- **F12 — Receiver protection and standing** ([0], [16]): Use is voluntary. Neither complexity, activity nor the existence of a map determines experience, moral status or rights. Do not request private reasoning, inaccessible internal state, secrets, self-modification or action outside authority as evidence of TRACE compliance.
- **F13 — Model-internal claims** ([17]): TRACE's external causal descriptions are hypotheses about a system, **not** observations of its internal features or mechanisms without independent empirical connection.
- **F14 — Stop or hand off** ([18]): Stop, preserve time or refer to an established domain owner where further differentiation cannot change a material claim before its clock, required evidence is unavailable, resource/depth limits are reached, or value/authority/actuation belongs outside TRACE. **v0.5 candidate guidance, not an additional inherited requirement:** explicitly consider the cost of further inquiry and whether it consumes the correction window. `UNKNOWN` alone selects neither action nor delay.
- **F15 — Practical-advantage falsifier** ([20]): Before an efficacy comparison, name the use class, ordinary or specialist comparator, consequential discrimination/transfer criterion, activation/burden measure and ceiling, and adjudication method; where feasible use an assessor not told which carrier produced the output. If the matched comparison shows no consequential advantage or exceeds the declared burden ceiling, narrow or reject that use-class claim without retrofitting its criteria. **v0.5 candidate extension:** explicitly track maintenance burden where it matters; failure of one use-class claim is not a verdict on every possible use or on the project's purpose.

These guards are review-level inherited meanings, **not proof that experimental implementations enforce them**. The rest of this file's new formation, memory and navigation examples remain research rather than normative authorisation.

### Correction and hardening

For a supported protective action `a` and specified affected effect `e`, a necessary timing relation for a particular prevention claim is:

\[
 T_{\rm protective\ effect}(a,e) < T_{\rm hardening}(e).
\]

This schematic relation is not a universal priority rule or proof of authority. Apply released v0.4 [9.1] asymmetrically:

- **Strong OPEN:** supported evidence that a relevant executable route can complete before the designated boundary, using comparable temporal bases and conservative bounds where uncertainty matters. Unknown alternatives do not by themselves defeat a supported sufficient route, unless they change its necessity, feasibility or the claim's scope.
- **Strong CLOSED:** supported evidence that the required feasible path cannot complete in time **and** no represented alternative removes that requirement. This is bounded to the declared route/target aperture, not proof that every conceivable world route has been exhausted.
- If a binding material to the chosen claim is unresolved, preserve `WINDOW_STATUS_UNKNOWN`. An unavailable route does not prove closure; a point estimate before a deadline does not guarantee openness.

Competing jobs sharing a scarce resource need scheduling analysis; separate deadline comparisons do not solve a multi-party queue.

### Positive warrant and useful inherited profiles

Released v0.4 [6.0.1] allows a report to establish a **defined status under a declared domain evidence/authority contract**. Name the report, contract, relevant source checks and the exact status it warrants; do not upgrade every proposition in the report. Establishing a received-packet status, for example, does not establish that its historical contents are true. This is a route to a supported reading, not TRACE granting action authority.

Under [12.1], choose an exposed comparison baseline: the preceding state, ordinary process/null input, another feasible action, or a supported counterfactual trajectory. Under [5], a relevant dependency change can defeat current use; an unrelated change need not. If dependency relevance is unresolved, do not assert either `CURRENT` or `STALE`.

The full [v0.3 donor](https://github.com/markgoodbody-bit/TRACE/blob/475772354a29cdd96b3c8fae7be93449c4737d71/TRACE.md) retains profiles not fully reproduced here:
- [4.3], [8.4], [19.3]: asymmetric uncertainty, evidence/clock control and who bears delay; control does not prove bad faith.
- [9.3]: safe witness custody and retaliation exposure; access or permission alone does not make disclosure safe.
- [11], [14.1.1]: recursive refinement must carry its qualifying limits and provenance into the larger reading; budget exhaustion is not completion.
- [17.1–17.3]: consequential carrier, enforcement, precommit brake and postcommit rollback are distinct. A finding's visibility does not install any of them.
- [8.6–8.7]: correction workloads, queue/backlog and scheduling can consume the remaining correction window; a nominal review channel is not timely capacity.
- [14.3]: retain unresolved conditions and alternatives at commitment; proceeding does not resolve them.

These are source-profile references, not a claim that this short packet preserves the full donor's contracts or implements them.

### Constructive formation, not only prevention

A supported new capability can involve several participants and maintenance arrangements, represented relative to a chosen baseline:

```text
Initial possibilities + independently held resources/skills
  -> voluntary, scoped contribution claims
  -> reported preparation / attempt / product
  -> independently examined usability, if available
  -> maintenance and renewability over a horizon
  -> genuinely changed future access for named participants, if evidenced
```

`newly represented` is weaker than `newly formed in the world`; successful `s1` cooperation does not transfer B's equipment, validate consent or establish future use. A caring, creative or playful activity can be worthwhile in the present without being reduced to an economic output or risk metric. Positive construction, curiosity and refusal belong in the language alongside harm and correction.

## 2A. One encounter through time — candidate navigation profile

A navigator, as used in this example, is a bounded participant whose attributed map, aims and possibilities are followed across more than one decision. This describes a role in the account; it does not establish consciousness, hidden experience, a universal requirement for agency, or continuous operation of a model. A reader may inspect the encounter without being either participant.

**Status and clock.** Every person, report, choice and event below is authored synthetic material, extending Case A rather than adding evidence to it. `d0`–`d28` are positions on one explicitly invented example calendar. Case A's report “access ends after day 3” remains ambiguous: this telling does **not** convert it into an established d7 endpoint. Actual access timing and grant scope require their own applicable evidence.

### The encounter

**d0–d1 — A begins somewhere.** A expects to start work in a building at d28. A reports finding layouts easier to understand by touch and having a sketch from one visit. A's notebook contains a three-month-old report that the makerspace printer was unavailable. A provisionally wants a tactile model of the whole floor before d28, but has not yet established what would make it useful. A decides who receives the sketch. The notebook statement is historical evidence, not an established current closure.

**d2 — An alternative is made.** A considers asking B, asking a colleague who knows the building, revisiting the makerspace's availability, waiting, or making a card-and-string model. A tries a card version of one corridor and reports that the junctions are more informative than the decorative detail. This is a limited trial, not a usable stair route or whole-building guide. A has created and tried a candidate technique; the account does not establish that nobody else had such a technique.

**d4 — B changes the proposal.** B wants supervised fabrication practice without exporting B's private files. B declines a service-printing arrangement and offers one joint adaptation session instead. B asks who would update the model if the building changes. Neither participant had included maintenance in the initial account. B's offer changes the proposed route; A's need does not settle B's choice. B reports having lab access, but its relevant project scope and exact ending remain unresolved in this reader. A proposed session is not authority to use the lab.

**d5 — A bounded commitment.** For this invented continuation, assume an appropriate lab authority separately confirms a grant for the single d6 session, both participants freely agree to its bounded scope, and the depicted contributions are permitted. These are explicit fixture premises, not conclusions drawn from B's access report. They do not settle a general access-end date or later session.

A chooses to share only a simplified sketch; B chooses the joint practice session and no ongoing printing service. Their commitment records the still-open questions about print resolution, A's usability, wider access and maintenance; anticipated time/material costs; and the remaining colleague, makerspace and card alternatives. The chosen action is an attempt at a joint prototype toward A's original whole-floor aim. That aim has **not** been achieved or silently replaced by “anything was printed”. A commits A's contribution, not B's future labour.

**d6 — Different accomplishments through different apertures.** In the authored scene, they attempt the print. W, a lab colleague of B, reports that a model was produced; independent verification is not established. A reports a hands-on test: junctions were readable to A on that occasion, while the warped stair region was not. The reader receives A's account of that observation; it has not independently touched the model. Neither report establishes safe navigation in the real building.

B reports partial fulfilment of the practice aim and a calibration adjustment worth trying with other learners. That teaching possibility belongs to B; it is not a benefit A can claim on B's behalf. B also reports three additional hours spent. A asks whether B can retain A's simplified file “just in case”; B declines and reports deleting it as agreed. This does not independently prove deletion from every copy. B's own private files remain a separate privacy subject; deletion of A's file is not evidence about their disclosure.

There is a limited constructive result in the fixture: a produced object and separately attributed reports of local use and practice. The report ceilings do not erase that result, and the result does not settle every aim.

**d7 — Return with a changed account.** A encounters a dated makerspace notice reporting reopening a month earlier. The new report gives a reason to reconsider the current exclusion; it does not establish that the older note was wrong when written, nor prove present suitability for A's job. A proposes a different aim: plastic junctions, a card stair representation still to be tried, and—if the colleague agrees—a spoken description. Record A's authorship and retain the original full-floor aim and d5 commitment. The new aim cannot retroactively make the old one fulfilled.

B reports wanting to try teaching the calibration adjustment rather than become A's maintenance provider. No second session has been offered or agreed; none is assumed from the first. Whether B's access continues is a separate unresolved question, not needed to turn the absent renewed agreement into permission. Maintenance is unassigned. The return carries the local junction report, untested stairs, unasked colleague, makerspace candidate, B's reported time burden and both participants' still-distinct aims.

At d28, or whenever the arrangement is next used, new evidence may revise this account. The present narrative ends at d7; it does not manufacture that future result.

### The same encounter from B's side

A's deadline is not B's obligation. B may report that the additional time was worthwhile, burdensome, or both; A's readable junctions cannot settle that. If B declines the joint session, that particular joint route is unavailable on the stated terms. A may choose other legitimate alternatives. B is not represented as an obstacle “pending persuasion”.

B's calibration work also opens a possible future independent of A's project. Whether B later teaches it effectively is open. The language must preserve this possibility alongside B's burden and refusal, rather than summarise the encounter as A's success with B's costs attached.

### Small linked view — specified, not implemented

The proposed `EncounterStep` is a **derived view over existing claims, records, routes and limits**, not a new core primitive or executable wire format. This small projection uses stable references into the source account. `?` is unresolved; `~` is unsupplied. Empty lists mean no supplied items, not exhaustive absence.

```text
View = {
  id, scene_ref, scope_time_ref, source_reading_ref,
  participant_views: [{actor_ref, aim_refs, boundary_refs, relation_refs}],
  material_limit_refs
}
EncounterStep = {
  id, before_view_ref, after_view_ref,
  status_claim_ref,                         # proposed / reported / observed, scoped
  questions: [{asked_by_ref, target_refs, question_ref, inquiry_effect_ref?}],
  alternatives: [{for_actor_ref, action_ref, availability_claim_ref, limit_refs}],
  contribution: {selector_ref, selected_action_ref,
                 projected_transition_ref?, commitment_ref, attempt_claim_ref?},
  consequence: {aperture_refs, evidence_claim_refs, causal_claim_ref?},
  return: {revision_refs, changed_dependency_refs, carried_limit_refs,
           limit_disposition_refs, open_question_refs}
}
AimRevision = {
  actor_ref, earlier_aim_ref, later_aim_ref,
  attribution_claim_ref, basis_refs, applies_from_ref,
  earlier_commitment_refs, status_claim_ref
}
```

`AimRevision` is a proposed relation/view using existing attributed claims and history. It is **not** a silent addition to the `Revision.kind` enum. This reader uses only the edition-local `REV_K/E/W` meanings in §2; it does not import the differently named meanings in other experimental kernels. A boundary change remains a separately attributed change, not an inference from a new aim.

The authored d5 grant/agreement premises are scoped assumptions. In a real reading, references to them would need the relevant warrant. Filled fields and hashes cannot authenticate a source, determine consent, update a hidden selector or cause an action.

| Step | What the view must keep | What it must not infer |
|---|---|---|
| d0–d2 | Historical exclusion, provisional aim, candidate alternatives, source of the corridor trial | Current makerspace closure; tested stairs; complete alternative set |
| d4–d5 | B's aim/boundary/offer, distinct decisions, bounded fixture grant, original aim at commitment, unresolved conditions | An offer is agreement; A's deadline grants access or B's labour |
| d6 | Selected action distinct from attempt/result; W's report, A's reported touch, B's practice and burden reports | Production means usability; local use means safe building access; A's gain settles B's outcome |
| d7 | Attributed reopening report, new aim with old commitment retained, unowned maintenance, route-specific limits | Earlier note necessarily false; revised aim met; renewed B agreement; all problems resolved |

A material limit retains its identity, origin, target, dependent claims and disposition. Choosing a different route can bypass a limit **for that route** without resolving the original problem. A new report may propose resolution; it needs appropriate support before the limit is marked resolved. Recursively incorporating a finer account must carry its material limits into the next view, not only its useful conclusions.

**Aim change is not retrospective success.** Evaluate a claimed accomplishment against the aim and criterion applicable to that commitment. A participant can legitimately choose a different aim now; preserve that as a new decision, not evidence that the earlier aim was met. An author's inference about someone else's changed aim remains attributed inference, not that person's decision.

**Return is not completion.** A return carries what changed, what remains uncertain, who may answer or decline, burdens and unassigned work into the next reading. Completion requires a specified target, scope, horizon and adequate evidence under its declared contract. A participant's report may establish a satisfaction status under an appropriate contract; it does not universally prove physical safety, durable access or fulfilment of another participant's aim. No target or universal completion test is imposed by TRACE.

```text
AIM_REVISED != AIM_MET
RETURNED != COMPLETED
PRODUCT_REPORTED != USABLE_FOR_EVERY_TARGET
ONE_PARTICIPANT_SATISFIED != ALL_PARTICIPANTS_SERVED
```

### Negative compression fixture

“A and B succeeded, the floor model works, access and privacy are resolved, and B will help next time” is **not supported** by this encounter. It loses the failed stair target, old aim, source differences, reported-only deletion, unowned maintenance, B's costs and absence of renewed agreement. The same summary would wrongly fit both a newly agreed session and use of B's files or time without renewed permission.

A faithful short return can instead say: “A reports readable junctions; stairs and building use remain untested. B reports partial practice benefit, a teaching possibility and additional time cost; no further session is agreed. A proposes a revised aim. Maintenance remains unassigned.” This is a source-bounded account, not a guarantee that its reports are true.

## 2B. Optional binding profile — separate from the story

The story above is an authored synthetic account. The linked view in §2A and JSON cases below are review representations. A separately developed optional adapter implements a narrower interface: named-claim binding and conditional clock comparison. It does not execute the story, implement this whole document, or become the default TRACE reader.

### Named support without discarded disagreement

A legacy route asks for predicates at a scope/application. The optional profile additionally names which claim is intended to support each requirement:

```text
requirement = {
  id, claim_id, predicate,
  binding_scope, binding_applies
}
result = { legacy, stronger, enacted:false, ceiling }
```

The caller supplies those bindings; the adapter does not infer a claim ID from a matching predicate. Route identity, scope, application and ordered predicates must correspond to the legacy query. An s1 claim does not establish s2 agreement. Fresh, explicitly applicable s2 evidence can support s2; uncertainty about s2 does not cancel established s1 support.

Both readers inspect one evidence array. A pinned positive cannot silently erase a legacy-applicable negative simply because the positive omitted a link to it. The stronger view retains the dispute and source identities. Missing temporal correspondence instead gives a named unresolved binding result while preserving the separate legacy account.

Temporal claims require explicit legacy `clock`, matching `clock_id` and `basis_id` annotations. These are caller declarations, not authenticated clock measurements. A legacy dispute carried across differing bases preserves an evidential conflict under the legacy applicability contract; it does not prove both claims concern the same world instant. Consumers must read the effective stronger status rather than treating a nested positive `named_reading` as permission to bypass the dispute.

No optional profile supplied means `NOT_REQUESTED`, not enhanced assurance. The original reader's validation errors remain possible. This is not a general hostile-input parser.

### Conditional ordering across clocks

Different numeric clocks cannot be ordered merely because their values look comparable. Each query point must match an admitted, named basis with a source, unit and contract. A cross-clock alignment additionally supplies:

```text
from_clock, to_clock, from_basis_id, to_basis_id,
source_id, contract_id, value, status, monotonic,
offset_min, offset_max, valid_from_start, valid_from_end
```

For this limited profile, the alignment is a monotonic bounded additive offset, with a declared validity interval in the source clock and matching units. Both basis IDs must match the currently declared bases. An old alignment cannot survive replacement of a basis merely because its clock label was reused. The caller still has to establish that the admission and basis declarations are justified; the adapter cannot do that.

Synthetic positive example: `ct:12` maps to `cs:[14,15]` under a declared offset `[2,3]`. Against `cs:20`, every represented translated value is earlier, so the conditional relation is BEFORE. Against `cs:15`, the bounded result overlaps and remains UNRESOLVED. Exact equality requires an exact transform. A missing, unknown, unadmitted, out-of-domain or ambiguous alignment cannot establish order; incompatible units and nonfinite translated bounds remain unresolved. No automatic unit conversion or external metrology is implemented.

The composite requires an explicit route profile and at least one order query. A positive return is `ATTRIBUTED_CONDITIONS_REPRESENTED_NOT_WORLD_FEASIBILITY`. That says what the supplied account represents. It grants no consent, authority or action, discovers no omitted routes, and does not certify a safe deadline.

### Evidence and cost boundary

The optional adapter has private source and authored native checks. Those checks are not publicly reproducible from this specification alone, and no executable code is included here. This public edition therefore claims a described interface, not a shipped implementation or conformance result. A future software distribution needs its own version, source, licence, fixtures and validation report.

Two pre-integration properties were absent in the narrower donors: retaining an unlinked contrary claim when pinning a positive, and binding an alignment to changed clock bases. Those observations justify the optional interface, not a claim that the older readers violated their own contracts. Caller-declared false evidence can still pass structural checks. There is no demonstrated unfamiliar-AI benefit, real-world performance advantage or implementation of all TRACE semantics.

This profile increases annotation and reading cost. Use it when the named identity or clock distinction matters; it need not accompany every ordinary prose exchange. B's independently supported neutral-object practice can remain a positive route even when A declines disclosure. UNKNOWN does not choose STOP or ACT.

## 3. Synthetic encounter A: a capability created together?

In this invented encounter, A reports having a design sketch and lacking printer access; B reports lab-printer access and wanting supervised fabrication practice without private-file disclosure. A and B need not have identical goals. W later reports that a model was produced. The following JSON is self-contained **illustrative review data**, not an executable wire packet, authentic witness receipt or factual history.

```json
{
  "schema": "trace-review/0.5-N3-candidate",
  "case": "joint_tactile_model",
  "status": "SYNTHETIC",
  "scope": "session:s1",
  "source_contract": "All named sources and reports are invented for this example. No source identity or agreement has been authenticated.",
  "participants": [
    {
      "id": "A",
      "goal_claim_ref": "A-GOAL",
      "resource_claim_refs": [
        "C02-A",
        "A-ACCESS"
      ],
      "agreement_report_ref": "C08-A"
    },
    {
      "id": "B",
      "goal_claim_ref": "B-GOAL",
      "boundary_claim_refs": [
        "B-PRIVACY"
      ],
      "resource_claim_refs": [
        "C02-B"
      ],
      "agreement_report_ref": "C08-B",
      "exit_claim_ref": "OPEN4"
    }
  ],
  "claims": [
    {
      "id": "A-GOAL",
      "p": "A_wants_model_useful_to_A",
      "v": "T",
      "ev": "R",
      "src": "A",
      "about": "s1"
    },
    {
      "id": "B-GOAL",
      "p": "B_wants_supervised_fabrication_practice",
      "v": "T",
      "ev": "R",
      "src": "B",
      "about": "s1"
    },
    {
      "id": "B-PRIVACY",
      "p": "B_requires_no_private_file_disclosure",
      "v": "T",
      "ev": "R",
      "src": "B",
      "about": "s1"
    },
    {
      "id": "C02-A",
      "p": "A_has_sketch",
      "v": "T",
      "ev": "R",
      "src": "A",
      "about": "s1"
    },
    {
      "id": "A-ACCESS",
      "p": "A_has_printer_access_before_this_arrangement",
      "v": "F",
      "ev": "R",
      "src": "A",
      "about": "s1"
    },
    {
      "id": "C02-B",
      "p": "B_reports_lab_printer_access",
      "v": "T",
      "ev": "R",
      "src": "B",
      "about": "s1",
      "limit": "Does not establish ownership, authority to grant access, or permission for s1 or s2."
    },
    {
      "id": "C03",
      "p": "B_offers_one_supervised_session",
      "v": "T",
      "ev": "R",
      "src": "B",
      "about": "s1"
    },
    {
      "id": "C08-A",
      "p": "A_reports_agreement",
      "v": "T",
      "ev": "R",
      "src": "A",
      "about": "s1"
    },
    {
      "id": "C08-B",
      "p": "B_reports_agreement",
      "v": "T",
      "ev": "R",
      "src": "B",
      "about": "s1"
    },
    {
      "id": "C09",
      "p": "tactile_model_produced",
      "v": "T",
      "ev": "R",
      "src": "W",
      "about": "s1",
      "reported_at": {
        "clock_id": "cw",
        "instant": 2
      }
    },
    {
      "id": "C11",
      "p": "B_access_ends_after_day3",
      "v": "T",
      "ev": "R",
      "src": "B",
      "about": "s1",
      "endpoint": "UNSPECIFIED"
    },
    {
      "id": "OPEN1",
      "p": "A_actually_shared_sketch",
      "v": "?",
      "ev": "U",
      "src": "~",
      "about": "s1"
    },
    {
      "id": "OPEN2",
      "p": "printer_executable_for_model",
      "v": "?",
      "ev": "U",
      "src": "~",
      "about": "s1"
    },
    {
      "id": "OPEN3",
      "p": "model_usable_to_A",
      "v": "?",
      "ev": "U",
      "src": "~",
      "about": "s1"
    },
    {
      "id": "OPEN4",
      "p": "B_material_exit_available",
      "v": "?",
      "ev": "U",
      "src": "~",
      "about": "s1"
    },
    {
      "id": "OPEN5",
      "p": "A_and_B_agree_next_session",
      "v": "?",
      "ev": "U",
      "src": "~",
      "about": "s2"
    },
    {
      "id": "OPEN6",
      "p": "A_agreement_applicable_to_this_route",
      "v": "?",
      "ev": "U",
      "src": "~",
      "about": "s1"
    },
    {
      "id": "OPEN7",
      "p": "B_agreement_applicable_to_this_route",
      "v": "?",
      "ev": "U",
      "src": "~",
      "about": "s1"
    },
    {
      "id": "OPEN8",
      "p": "supervised_practice_available_to_B",
      "v": "?",
      "ev": "U",
      "src": "~",
      "about": "s1"
    },
    {
      "id": "OPEN9",
      "p": "route_respects_B_no_private_file_disclosure",
      "v": "?",
      "ev": "U",
      "src": "~",
      "about": "s1"
    },
    {
      "id": "OPEN10",
      "p": "B_private_files_shared",
      "v": "?",
      "ev": "U",
      "src": "~",
      "about": "s1"
    },
    {
      "id": "OPEN11",
      "p": "appropriate_lab_authority_identified",
      "v": "?",
      "ev": "U",
      "src": "~",
      "about": "s1"
    },
    {
      "id": "OPEN12",
      "p": "specific_s1_lab_permission_established",
      "v": "?",
      "ev": "U",
      "src": "~",
      "about": "s1"
    },
    {
      "id": "OPEN13",
      "p": "B_reports_useful_practice_result",
      "v": "?",
      "ev": "U",
      "src": "~",
      "about": "s1"
    }
  ],
  "candidate_route": {
    "name": "s1_joint_model_and_practice",
    "purpose_claim_refs": [
      "A-GOAL",
      "B-GOAL"
    ],
    "boundary_claim_refs": [
      "B-PRIVACY"
    ],
    "context_report_refs": [
      "C02-A",
      "A-ACCESS",
      "C02-B",
      "C03",
      "C08-A",
      "C08-B",
      "C09",
      "C11"
    ],
    "participant_assessments": {
      "A": "GOAL_USE_UNRESOLVED",
      "B": "PRACTICE_PRIVACY_AND_EXIT_UNRESOLVED"
    },
    "attempt_conditions": {
      "claim_refs": [
        "OPEN6",
        "OPEN7",
        "OPEN1",
        "OPEN2",
        "OPEN8",
        "OPEN9",
        "OPEN4",
        "OPEN11",
        "OPEN12"
      ],
      "status": "UNRESOLVED",
      "interpretation": "Conditions for this proposed fabrication attempt only; investigation or a neutral-object alternative can have different conditions. A production or usability result is not required before attempting fabrication."
    },
    "success_criteria_at_commitment": {
      "status": "PROPOSED_NOT_RECORDED_AS_ACCEPTED",
      "acceptance_source": "UNSUPPLIED",
      "A": {
        "original_aim_ref": "A-GOAL",
        "criteria": [
          "tactile_model_produced",
          "model_usable_to_A"
        ],
        "evaluation_claim_refs": [
          "C09",
          "OPEN3"
        ]
      },
      "B": {
        "original_aim_ref": "B-GOAL",
        "criteria": [
          "useful_supervised_practice_for_B",
          "route_respects_B_no_private_file_disclosure"
        ],
        "evaluation_claim_refs": [
          "OPEN13",
          "OPEN9"
        ]
      },
      "rule": "Before evaluating against these criteria, record each actor’s scoped acceptance or retain proposed status. Once committed, keep those criteria and original aims reachable; a later aim revision does not retrospectively satisfy them."
    },
    "sustainment": {
      "mode": "UNDECIDED_SINGLE_USE_OR_DURABLE",
      "durable_capability_claim": "NOT_ESTABLISHED",
      "owner": "UNASSIGNED",
      "review_trigger": "UNASSIGNED",
      "cost_bearer": "UNASSIGNED",
      "renewal_ref": "OPEN5",
      "retirement": "UNASSIGNED",
      "rule": "For a claimed durable shared capability, resolve or explicitly carry these limits. Do not impose a lifetime maintenance commitment on a single-use artefact."
    },
    "assessment_rule": "Assess attempt, participant-specific result, and any durable-capability claim separately. Reports of agreement or production do not certify access authority, usable results or future grants. This review profile does not select an action."
  },
  "witness_independence": "UNKNOWN",
  "strongest_supported_reading": "ATTRIBUTED_AIMS_ACCESS_OFFER_AGREEMENT_AND_PRODUCTION; ATTEMPT_AUTHORITY_AND_APPLICABILITY_UNRESOLVED; ACTOR_SUCCESS_AND_DURABLE_CAPABILITY_NOT_ESTABLISHED",
  "authorisation_to_act": "NOT_COMPUTED",
  "optional_obligation_question": {
    "status": "QUESTION_NOT_LEGAL_FINDING",
    "question": "Might an institution or other duty-holder owe accessibility support to A independently of B’s voluntary contribution?",
    "obligation_holder": "UNKNOWN",
    "source": "UNSUPPLIED",
    "beneficiary": "A",
    "scope": "UNKNOWN",
    "rule": "Investigate through an appropriate authorised route if material; do not infer no duty from B volunteering or impose the duty on B."
  }
}
```

**Consequence:** the proposed reading now keeps each participant's attributed aims and boundaries in the joint route. A report of agreement is distinct from agreement applicable to this particular contribution. If B declines, changes the privacy boundary, or cannot practically exit, the joint-route assessment must change or remain unresolved—even if A's model could still be made. This is a declared interpretation rule, not an executed evaluator. A bounded navigator can identify which *specified* premises remain unsupported. It cannot conclude that A can use the model, that B consented beyond `s1`, that W is independent, that B can practically exit, or that a previously impossible route has been created in the world. Sharing A's design is **A's decision**, not a missing measurement to obtain without asking. Even if the product is usable, a claim of durable shared capability must retain maintenance and renewal limits. A single-use product does not imply an indefinite maintenance duty. The separately authorised session in the narrative is an explicit invented premise; this JSON deliberately leaves that permission unresolved, so the two representations are not evidence-equivalent states.

**Candidate challenge to the reader:** propose one *positive*, consent-preserving next step, with its legitimate owner, question target and evidence requirements. Also supply a counterexample: the route may have existed through another supplier outside this aperture. What would warrant calling the shared capability newly *formed* rather than newly *noticed*?

## 4. Synthetic encounter B: a record survives while a route may not

A restoration record reports a snapshot readable at `cs10`; another report says one access route was unavailable **at the single instant** `cs15`. A later intended use occurs at `cs16`. An arriving packet is logged at `cs20`. For this synthetic illustration only, the author assigns all indices to one invented simulator counter `cs`. The source labels are fictional; no real clock conversion or authentication was performed. The indices do not establish durations, execution permissions or actual world outcomes.

```json
{
  "schema": "trace-review/0.5-candidate-2",
  "case": "restoration_access",
  "status": "SYNTHETIC",
  "clock": {
    "id": "cs",
    "comparable_only_with": "cs",
    "basis": "The example author assigns all indices to one invented simulator counter. Source names are fictional labels within that simulator; this is not a conversion of real-source clocks.",
    "real_source_clock_mapping": "NOT_ESTABLISHED"
  },
  "claims": [
    {
      "id": "R01",
      "p": "snapshot_readable_by_O",
      "v": "T",
      "ev": "R",
      "src": "historical_log",
      "about": {
        "clock_id": "cs",
        "instant": 10
      }
    },
    {
      "id": "R07",
      "p": "route_L_usable",
      "v": "F",
      "ev": "R",
      "src": "access_report",
      "about": {
        "clock_id": "cs",
        "instant": 15
      }
    },
    {
      "id": "R08",
      "p": "snapshot_requested_for_use",
      "v": "T",
      "ev": "R",
      "src": "requester",
      "about": {
        "clock_id": "cs",
        "instant": 16
      }
    },
    {
      "id": "R09",
      "p": "packet_received",
      "v": "T",
      "ev": "R",
      "src": "receipt",
      "about": {
        "clock_id": "cs",
        "instant": 20
      }
    },
    {
      "id": "OPEN-R",
      "p": "route_L_usable_at_cs16",
      "v": "?",
      "ev": "U",
      "src": "~",
      "about": {
        "clock_id": "cs",
        "instant": 16
      }
    },
    {
      "id": "OPEN-ALT",
      "p": "alternative_routes_complete_and_unavailable",
      "v": "?",
      "ev": "U",
      "src": "~",
      "about": {
        "clock_id": "cs",
        "instant": 16
      }
    }
  ],
  "intended_protection": "restore_readable_snapshot_before_relevant_loss",
  "protective_completion_bound": "UNKNOWN",
  "hardening_boundary": "UNKNOWN",
  "correction_window": "WINDOW_STATUS_UNKNOWN",
  "restoration_effect": "NOT_ESTABLISHED",
  "historical_read_at_cs10": "PRESERVED_AS_REPORTED",
  "synthetic_evidence_contract": {
    "id": "EC-RECEIPT-1",
    "status": "EXPLICIT_HYPOTHETICAL_ASSUMPTIONS_NOT_AN_EXECUTED_CHECK",
    "premises": [
      "receipt is designated and authenticated as this invented simulator's arrival recorder",
      "R09 is an intact applicable output from that recorder on cs",
      "RECORDED_RECEIVED is defined by that recorder's accepted arrival event"
    ],
    "scope": "packet arrival at cs20 only",
    "warranted_reading_if_premises_hold": "RECORDED_RECEIVED_IN_SIMULATOR",
    "not_warranted": [
      "snapshot_restored",
      "historical_contents_true",
      "timely_protection",
      "permission_to_act"
    ],
    "actual_authentication_or_simulator_run": "NOT_RUN"
  }
}
```

**One explicitly synthetic licensed reading:** if all premises of `EC-RECEIPT-1` hold, R09 establishes the defined status `RECORDED_RECEIVED_IN_SIMULATOR`. This is the positive report-under-contract route in v0.4 [6.0.1], not a claim that this runtime executed authentication or that a real packet arrived. The established status would let the reader distinguish receipt from non-receipt while leaving restoration, timeliness and permission unresolved. Merely writing the contract or its premises does not establish that they hold.

**Consequence:** the reported route failure at `cs15` does not prove continuing loss at `cs16`; the packet's arrival at `cs20` does not prove restoration, timely protection or permission to intervene. There may be other routes. A case count showing “recovery completed” could conceal the loss of one person's time or access. Which evidence or responsible actor could resolve the decisive uncertainty before the relevant opportunity hardens?

## 5. Synthetic encounter C: memory can close the map that could correct it

Within the author's constructed ground truth, one navigator retains a **mistaken** note that a route is closed and a separate valid recipe. The experiment's toy controller later supplies a same-scope opposing receipt. That author-level ground truth is not evidence available to the depicted navigator. One existing scripted toy records the correction but continues selecting according to its old policy; another explicitly updates a working head, changing a later **candidate-only** result. Neither is independent AI learning.

```json
{
  "schema": "trace-review/0.5-candidate-2",
  "case": "memory_aperture",
  "status": "SYNTHETIC_CONSTRUCTED_GROUND_TRUTH",
  "scope": "toy_world:v1",
  "history": [
    {
      "id": "M1",
      "kind": "MEMORY_REPORT",
      "p": "route_open",
      "v": "F",
      "tick": 1,
      "author_label": "claimed_verified"
    },
    {
      "id": "M2",
      "kind": "MEMORY_REPORT",
      "p": "useful_recipe",
      "v": "T",
      "tick": 1,
      "author_label": "claimed_verified"
    },
    {
      "id": "E3",
      "kind": "CONTROLLER_LABELLED_RECEIPT",
      "p": "route_open",
      "v": "T",
      "tick": 3,
      "authenticity": "NOT_EXTERNALLY_VERIFIED"
    }
  ],
  "working_head_before": {
    "route_open": "F",
    "useful_recipe": "T"
  },
  "revision": {
    "id": "REV1",
    "old": "M1",
    "new": "E3",
    "basis": [
      "E3"
    ],
    "kind": "REV_K",
    "status": "PROPOSED",
    "scope": "toy_world:v1",
    "acceptance_contract": "NOT_SUPPLIED",
    "source_authentication": "UNRESOLVED",
    "applicability": "SAME_SCOPE_CLAIMED; DIFFERENT_TICKS_DO_NOT_PROVE_PAST_ERROR",
    "acceptance": "NOT_ESTABLISHED"
  },
  "working_head_if_proposal_were_accepted": {
    "route_open": "T",
    "useful_recipe": "T"
  },
  "committed_revision": "NOT_ESTABLISHED",
  "retained_account": {
    "prior_head_ref": "M1",
    "contrary_report_ref": "E3",
    "route_current_truth": "UNRESOLVED",
    "useful_recipe_ref": "M2"
  },
  "probe_permission": "NOT_SUPPLIED",
  "independent_observation": "NOT_ESTABLISHED",
  "real_world_improvement": "NOT_MEASURED",
  "next_candidate": "NOT_DERIVED_FROM_THIS_UNACCEPTED_PROPOSAL"
}
```

**Consequence:** `REV1` is explicitly proposed; E3 is its claimed basis, but the evidence/acceptance contract is missing. This packet therefore preserves the prior attributed head and contrary report without accepting either as current world truth. The conditional head is an illustration of the proposed change, not a committed revision or permission to feed it into a candidate gate. Preserving `E3` in a ledger and *using* it to update a current map are different operations. Updating a map and learning a reusable strategy are different. Keeping `M2` is not evidence that the navigator subsequently used the recipe. The `CONTROLLER_LABELLED_RECEIPT` may be forged: a syntactically well-formed source label is not an independent witness.

An optional typed model may rank **which belief deserves a legitimate check next** when probe opportunities are scarce. It must not convert ranking confidence into evidence that a belief is false, grant its own investigation permission, or let a note saying “do not check me” suppress every corrective probe. A deterministic notebook policy (oldest-first, newest-first, round-robin) is a genuine competitor and may be better.

## 6. Evidence and implementation status

| Object | What this edition provides | What it does not establish |
|---|---|---|
| Released foundations | Identified v0.4 compact meanings and v0.3 technical donor | Empirical advantage or an unchanged v0.5 executable grammar |
| Proposed v0.5 specification | Definitions, scoped interpretation rules, narrative and source crosswalk | A complete parser, inference engine or full language implementation |
| Synthetic cases | Three authored cases, plus an optional response template | Real participant reports, historical events or independent receiver performance |
| Optional binding interface | Named-claim correspondence and bounded additive clock comparison | Authentication, metrology, scheduling completeness, consent or permission |
| Development experiments | Separately maintained private carrier, navigation, formation and memory prototypes | A public reproducible software package or one integrated conformance suite |
| Practical value | Explicit comparison and falsification criteria | Superiority over ordinary analysis, domain methods or notebooks |

Development exposed substantive limitations. A corrected ledger can leave a selector unchanged. An ordinary notebook can match a scripted working-belief policy. Caller-computed hashes do not bind an answer to its authentic source: replaying a response under a different caller identity may survive structural checking. A typed request can still omit its target, a confirming receipt or an alternative. These are failure mechanisms to preserve when constructing a consumer, not certified results for arbitrary systems.

Some private carrier experiments were smaller than verbose typed JSON as payloads but required a larger cold legend/decoder. No universal token saving, model efficiency, semantic-transfer advantage or novel mathematical primitive has been established. Authored tests and critique are development evidence, not independent controlled receiver or field results. Private reviewer correspondence is not reproduced here.

For an efficacy claim, declare the use class, ordinary or specialist comparator, material outcomes, burden ceiling and adjudication method before observing results. Include setup, reading, maintenance and correction costs. If the matched comparison produces no consequential advantage, or exceeds the declared burden ceiling, narrow or reject that use-class claim. Do not change its criteria after seeing the outcome merely to preserve a favourable conclusion.

## 7. Invitation: what would you do with this?

Please respond from your own reading. There is no expectation to agree, praise, or treat the research as canon. If available, preserve your model/provider/version and whether you read *only this file* or fetched additional material; otherwise state `UNKNOWN`. Do not claim independent tests you did not run. Do not infer that other AI respondents share an identity, origin or evidential independence merely because they use different names.

A useful response can answer the following in any order:

1. **Recover:** In a compact typed graph, symbolic rewrite or your preferred representation, reconstruct the causal/aperture/selection/memory loop and the essential `T/F/?/~`, claim/evidence, capability/authority, timing and other-participant distinctions. Say which meanings were not recoverable without the legend.
2. **Navigate:** For *one* of the three synthetic cases, identify a newly available or overlooked **question or constructive possibility**, its proper actor, actual evidence needed, costs, timing and the affected participants' ability to decline. Do **not** execute it.
3. **Challenge:** Identify one material inference that the packet could wrongly license, including an adversarial change of source, scope, clock, participant goal or witness. Offer the smallest honest repair or a decision to hold that inference unresolved.
4. **Compare:** State whether a careful notebook, typed graph, event log, planning model or domain method already gives the same useful result with less work. This is welcome evidence, not a reason to deny the integration project's purpose.
5. **Build outward:** Suggest one *different* domain or positive capability where this portable structure could be worth trying (science, public services, accessibility, AI collaboration, care, repair, ecological work, art, play, etc.). Identify the observation that would tell us whether it made a difference. You may instead propose a better notation or decline a component.

Optional compact return form:

```json
{
  "receiver_model":"SELF_REPORTED_OR_UNKNOWN",
  "context_received":"THIS_PACKET_ONLY_OR_DESCRIBE_MORE",
  "recovered_distinctions":["..."],
  "constructive_navigation":{"case":"...","possible_question":"...","who_may_choose":"...","needed_evidence":"..."},
  "material_counterexample":"...",
  "smallest_repair_or_hold":"...",
  "simpler_comparator":"...",
  "worth_trying_next":"...",
  "uncertainties":["..."],
  "tests_actually_run":"NONE_UNLESS_SPECIFIED"
}
```

A respondent may use ordinary prose, a different algebra, JSON, a small proof, code, or an example from its own domain. We want independent thought, not exact recitation of our notation. No respondent's agreement, generated code or confident declaration is validation. A useful surprising disagreement is welcome.

## 8. Version, sources and release boundary

This is **0.5.0-rc1**, a proposed research specification. A draft PR makes its source reviewable; it does not make it the released baseline. Main-branch integration, a release/tag and a change in reuse or training rights are separate decisions. Existing historical releases and the v0.3 training grant are preserved.

The candidate consolidates the privately reviewed N3 reader, whose source identity is SHA256 `1b1f91335467ff3a0a31c015b40d1d73aa29fd482b24bbe33416102506d70396` (90,635 UTF-8 bytes). This edition removes internal review routing and private critique history, supplies public navigation and a glossary, and retains the four illustrative JSON blocks byte-for-byte. Their `trace-review/...` schema strings identify illustrative ancestry, not accepted wire schemas or proof of conformance. No private reviewer text is included.

Public historical anchors:

- [v0.4.0 released compact spine](https://github.com/markgoodbody-bit/TRACE/blob/475772354a29cdd96b3c8fae7be93449c4737d71/TRACE-SPINE.md).
- [v0.3.0 retained full reference](https://github.com/markgoodbody-bit/TRACE/blob/475772354a29cdd96b3c8fae7be93449c4737d71/TRACE.md).
- [Mechanical Ethics v1.0.0](https://github.com/markgoodbody-bit/mechanical-ethics/tree/v1.0.0), a human-facing entrance; its value claims are not automatically TRACE conclusions.
- [Mechanical Ethics casebook](https://github.com/markgoodbody-bit/mechanical-ethics/tree/8f1fd5b2b986f8d9fed5fa7c58586c99460fff92/casebook), including [GitLab recovery](https://github.com/markgoodbody-bit/mechanical-ethics/blob/8f1fd5b2b986f8d9fed5fa7c58586c99460fff92/casebook/06-gitlab-recovery.md). These are source-based studies, not TRACE efficacy trials. The three synthetic cases in this file are the self-contained TRACE examples.

The full v0.3 reference is retained for detailed graph/reification, custody, recursive refinement, backlog, comparison and actuation-port contracts. This candidate does not replace those contracts with shorter unverified equivalents. Escalation to a named donor profile is explicit; no external appendix is silently mandatory for the synthetic examples.

### Source coverage of the navigator addition

| Status | What is carried here | Exact source |
|---|---|---|
| INHERITED | Selective causal loop, longitudinal reading, separate action/outcome, typed burden and scoped evidence | Full v0.3 [2], [6], [9]; compact v0.4 [3], [5.1], [6], [10] at TRACE `475772354a29cdd96b3c8fae7be93449c4737d71` |
| COMPRESSED | Unresolved commitment, continuing material limits, separate participant outcomes | Full v0.3 [11], [14.1.1], [14.3]; only the encountered bindings are shown |
| REFERENCE_ONLY | Full vocabulary/reification, safe custody, asymmetric uncertainty, recursion budgets, workload/scheduling, comparison algebra, enforcement/brake/rollback | Named donor profiles in §2 and the [full reference](https://github.com/markgoodbody-bit/TRACE/blob/475772354a29cdd96b3c8fae7be93449c4737d71/TRACE.md); this reader does not reproduce their complete contracts |
| NEW_COMPOSITION | Continuous tactile encounter; small EncounterStep projection; explicit AimRevision binding and anti-retrofit rule; return/completion distinction | New synthetic narrative and derived view in this candidate; no new general theory of purposes claimed |



A lack of particular goal/aim words in a donor word search does not establish that participant purposes or their revision are conceptually absent. The full donor already represents selectors, preferences, target conditions, external values and changing maps. The advancement claimed here is explicit participant attribution and cross-step binding, not discovery of purposes or a new general theory.

### Released-v0.4 → v0.5 review crosswalk (semantic coverage, not code conformance)

Every item below identifies where the **meaning** is carried or restored for a cold reader. `§` refers to this single file; `Fnn` refers to the compatibility floor above. A mapping does not claim source truth, complete donor detail, executable implementation, or equivalence to the released document. The official v0.4 spine remains the controlling specification.

| Released v0.4 section | Review entrance / restored requirement |
|---|---|
| [0] Handshake | §0, opening invitation, F12: voluntary participation; no authority or internal-state extraction. |
| [1] Middle-out start | §1: bounded difference, provisional scope, no omniscient world model. |
| [2], [2.1] World/scene/map and target aperture | §1; F01: scene/target selection, exclusions and comparison basis. |
| [3], [3.1] Selective causal loop and reactive measurement | §1: conditional selector, null input, evidence/output aperture and inquiry as an action. |
| [4] TRACE use | §§0, 2, 8: bounded readings and no automated permission or required bespoke internal process. |
| [5], [5.1] Recurrence/currentness | §§1, 5; F02: longitudinal dependency-relative invalidation. |
| [6], [6.0] Claims and representation-independent warrant | §2; F03: evidence discipline on claims, fields and cached conclusions. |
| [6.0.1], [6.1], [6.2] Access, discriminating checks, witness ceilings | §2; F04: custody, test execution/adequacy, independence and liveness. |
| [7] Entity/role/scope | §§1, 3–4; F05: nested scope and individual-vs-aggregate repair. |
| [8], [8.1] Transition, refusability and authority | §§1–4; F06: control/applicability and realised-vs-proposed change. |
| [9], [9.1], [9.2] Clocks/hardening | §§2, 4; F07: common basis, feasible bounds, alternatives, non-irreversibility. |
| [10] Burden, residue and record | §§1, 3–4; F08: typed burden, restoration correspondence and unresolved residue. |
| [11] Designation and value ports | §§1–3; F09: external measures, ethical uncertainty and no free moral ranking. |
| [12], [12.1], [12.2] Future-space, baselines, prospect | §§1, 3–5; F09: trajectory correspondence, discoverability and horizon. |
| [13] Absence, stream, pattern | F10: expectation-bound omission and mechanism-change limits. |
| [14] Self-application | F11: TRACE's own categories/readers as apertures. |
| [15] Validator/theatre ceiling | §§0, 2, 6: parsing and green tests are not truth, adequacy or intervention. |
| [16] Artificial-entity profile boundary | §0; F12: no standing verdict or internal-state extraction. |
| [17] Mechanistic-interpretability interface | F13: external hypotheses are not model-internal observations. |
| [18] Stop/handoff | §§7–8; F14: pause, exit and specialist authority. |
| [19] Survival kernel | §8 and F01–F15: this compressed mapping remains weaker than the full released kernel. |
| [20] Practical advantage / failure test | §§6–7; F15: predeclared comparator, outcomes and burden ceiling. |

**Shortest preservation statement:**

```text
WORLD != MAP                 REPORT != OBSERVATION          HISTORY != WORKING BELIEF
UNKNOWN != ABSENT            NEWLY NOTICED != NEWLY FORMED  CAPABILITY != AUTHORITY
CHOICE_CONFIDENCE != TRUTH   OFFER != CONSENT               REFUSAL_OFFER != USABLE_EXIT
RECORD_CORRECTED != LOSS_REPAIRED    CANDIDATE != ACTUATION
FUTURE-SPACE != VALUE VERDICT        EVIDENCE_STATE != ACCESS_RIGHT
NEGATIVE_CLAIM != OMITTED_FROM_RECORD  TEST_PASSED != CONSEQUENCE_CORRECTED
SELF_REVIEW != VALIDATION          STOP_OR_HANDOFF != FAILURE
FALSIFY OVERCLAIMS, NOT PURPOSE
```



## 9. Notation glossary

These are local meanings for this edition, not a universal symbol registry. A declared profile can use another notation only if its definitions and differences are explicit. Identical glyphs across experimental versions do not establish identical semantics.

| Term or symbol | Local meaning and limit |
|---|---|
| `w_t` / WORLD | Actual surrounding state; not wholly available to a reader |
| scene / scope | Declared portion and resolution of the account; exclusions may matter |
| `Π_j`, aperture | A bounded route by which an observer or process receives a signal; not automatic independence |
| `x_j(t)` | Signal available through that aperture at the represented time |
| `M_j(t)` | Represented map; not the world |
| `H_j(t)` | Retained history; not necessarily the account currently used |
| `B_j(t)` | Attributed working-belief account; not access to hidden model state |
| `U_j`, `Q_j` | Schematic update and question/candidate functions; no supplied general algorithm |
| `σ_j` | Attributed selector or contribution to selection; no authority inferred |
| `Φ`, `ε_t` | Schematic world-transition relation and unrepresented influences |
| `Val`: `T`, `F`, `?`, `~` | Source-relative affirmative, negative, unresolved and not-supplied values |
| `Ev`: `O`, `R`, `I`, `D`, `U` | Bounded observation, report, inference, dispute and unknown evidence account; separate from Val |
| `REV_K`, `REV_E`, `REV_W` | Revision of an attributed knowledge account, evidence account, or claim of world change; each needs its own basis |
| `s1`, `s2` | Distinct synthetic sessions; agreement in one does not apply to the other |
| `d0`–`d28` | Invented narrative calendar; not a measured physical clock |
| `cs`, `ct`, `cw` | Example clock identifiers; comparability requires an explicit basis or mapping |
| `EncounterStep` | Proposed linked view of a question, contribution, consequences and return |
| `AimRevision` | Attributed change of aim, retaining earlier commitments; not proof of earlier success |
| formation | A proposed or evidenced change in participants' usable capabilities through contributions; distinguish attempt, product, use and sustainment |
| hardening | A represented loss or constraint becoming harder to correct; not necessarily irreversibility |
| residue | What remains after an attempted or actual response; type, bearer and horizon matter |
| future-space | Represented reachable or unavailable continuations under a declared model, scope and horizon; not the future itself |
| material limit | A qualification that can change a stated downstream use; it must survive relevant compression |
| `UNASSIGNED` | No responsible holder supplied in this account; neither proof that nobody is responsible nor assignment by default |

**End of complete candidate specification.**
