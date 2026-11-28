# Conceptual challenge: honesty, regard, responsibility and hope

16 November 2026. Temporary session review, independent of the main synthesis. This is a critique and proposed construction, not an empirical evaluation, a release, or a moral theory proved by equations. Read BRIEF.md and the prior hope revision EVOLVED.md. No personal case or private correspondence is required for the examples below.

## Main finding

The four terms should not become four factors in one scalar. They describe different kinds of structure. Honesty concerns the warranted status of representations and corrections. Regard concerns whose interests, agency and objections enter the account. Responsibility concerns justified undertakings, roles and response to consequences. Hope concerns valued possibilities and the conditions that can keep, recover or create them. A coherent mathematical interface is possible without defining any of those human concepts exhaustively.

The promising connection is this: regard changes the scope and constraints of a planning problem; responsibility identifies and checks the commitments that may support its routes; honesty distinguishes actual support from expectations and statements; hope examines the resulting possibilities without requiring sole control, constant productivity or a rising forecast.

## Repairs required before integration

### 1. Separate self-undertakings from interpersonal promises

A self-undertaking may structure an agent's own future choices without having been announced to another agent or accepted by a recipient. A social promise may also create reliance. Use a declared `kind` field rather than silently identifying them. A public undertaking, an institutional obligation, a unilateral assurance and a negotiated contract need not have the same creation or release conditions.

Proposed record: `c = (kind, undertaker, beneficiary, content, trigger, due, authority, provenance, review_route)`. This record describes an asserted commitment; it does not prove validity. A separate status records whether its grounds are established, disputed or unknown. The exact moral status of self-promises remains a substantive normative question.

### 2. Keep commitment, capability and delivery on separate axes

A stated commitment is not delivered capacity. Conversely, loss of capability does not automatically erase an existing obligation or establish culpability. Use separate fields for the undertaking, physical support, forecast reliability and observed performance.

Proposed response rule: an active undertaking plus a newly discovered capacity gap triggers a check for assistance, early notification, authorised revision, substitution or repair. Which responses are owed depends on the undertaking and normative setting. None follows solely from the numeric size of the gap. A past voluntary overcommitment, an unforeseen failure and coercion must not receive identical blame simply because the same target was missed.

### 3. Avoid the false promise of exhaustive feasibility

Model-relative physical feasibility F_m differs from the set of routes we have checked. Use separate classifications for demonstrated executable routes, demonstrated blocked routes under stated assumptions, and unresolved routes. Empty demonstrated feasibility is not demonstrated impossibility. Robust failure over a declared model set only concerns that set; it is not a metaphysical statement about the future.

Normative status also needs its own uncertainty. `Unresolved permission` is not `permission granted`, and must not be treated as a physical impossibility either. The missing action may be an agreement, a correction, a resource, a measurement or a better model; those interventions have different meanings.

### 4. Regard is not a small positive weight

Counterexample: an optimiser chooses between outcomes (1000, -100) and (0, 0) for two people. With weights (1, 0.001), both people receive positive weight and the harmful first option still wins easily. Nonzero representation does not establish sufficient regard, consent or protection from domination.

A proposed regard record should retain whose interests are represented, their source or representative, burdens as well as benefits, whether participation is voluntary, and how the account can be challenged. It must permit an objection to the model's target or framing, not only an objection to the chosen numerical estimate. The suggested protections are normative commitments of this project, not consequences of probability theory.

Use a stakeholder-preservation check in comparisons: if a supposed improvement is obtained by deleting an affected person, changing that person's goal without attribution, or hiding a burden, it is not the same comparison. This is a useful audit invariant, not a complete ethical criterion.

### 5. Supported agency includes the supporters

A route can improve its beneficiary's prospects while exhausting its carriers. Resource and time constraints must therefore cover all participants and simultaneous promises. For a simple inventory, let a carrier's balance evolve as `b_(t+1) = b_t + replenishment_t - sum_i support_(i,t)`. The nonnegative-balance constraint is only one physical requirement; willingness, authority, substitution and the carrier's own valued activities also matter.

Counting two separately feasible commitments as jointly feasible is a direct error when they require the same exclusive resource. Moral regard cannot be certified by a plan that hides that collision or treats one participant's availability as unlimited. A sensible package may preserve a beneficiary's options through rotation, fallback or reduced burdens. It must not manufacture consent to those changes.

### 6. Cooperation does not by itself establish obligation

Two agents can coordinate successfully in a harmful activity, cooperate under coercion, or share a harmless project without promising continued participation. Descriptive joint success therefore does not prove moral legitimacy or a specific duty. The proposed model needs explicit grounds for each normative constraint and the authority to impose it. See the bounded Bratman source connection in SOURCES.md.

### 7. Keep a goal's authorship and its ethical evaluation distinct

An agent can hope for an outcome that would harm someone else. The existence or sincerity of that hope supplies no permission. Conversely, an ethically troubling plan does not prove that the person's underlying aim is worthless; a different route may honour it better.

Use `G_i` for an attributed target and a separate admissibility account for routes. Revising `G_i` requires its own provenance and loss record. The analyst must not improve the display by substituting an easier goal, and must not demand that a person abandon an uncertain goal merely because the analyst cannot certify a route.

### 8. Quantified uncertainty is not honesty itself

A numerical forecast can be honestly mistaken; a technically accurate statement can be deliberately misleading by omission. Calibration, traceable evidence and correction records help inspect representations but do not alone measure intent, sincerity or deception. Privacy and principled withholding are legitimate: a field may be withheld, unknown or outside scope without being false.

The operational honesty interface should therefore record claim, scope, evidence, date, uncertainty, omitted relevant conditions and revision status. A correction is incomplete for an action that still uses the old value. This makes downstream propagation a separate testable property, rather than treating storage as incorporation.

### 9. Continuity must have a carrier and assignment rule

A role can survive changes of personnel or software instances. That does not establish uninterrupted subjective identity or automatically assign all past obligations to any successor. Record what carries the commitment, who can act on it now, the basis of their assignment and the correction route if the carrier is lost. A successor record can preserve institutional obligations without pretending to settle philosophical personal identity.

### 10. Preserve the ordinary, non-instrumental value of support

Support, companionship, rest or creative activity need not earn legitimacy by increasing target probability. The model can include valued trajectory conditions, but should also acknowledge that its selected target may not exhaust what matters. A zero change in J is not proof an activity was pointless. Nor is a positive change proof that its burdens are acceptable.

## A stronger typed construction

Treat a local account as `A = (E, V, C, F, N, P)`:

- `E`: claim/evidence and correction records, including scope and uncertainty.
- `V`: attributed values, interests, burdens, standing and routes of objection.
- `C`: asserted or accepted undertakings, their grounds and performance history.
- `F`: model-relative physical opportunities and resource/support dependencies.
- `N`: stated normative requirements and their authorisation/dispute status.
- `P`: policy comparisons and valued trajectory prospects under declared models.

This is a proposed interface, not a theorem. Its benefit would be measured by whether it prevents consequential confusions without making action unmanageably burdensome. Honesty primarily constrains E and every transition; regard governs V and the scope of F/N/P; responsibility links C to actual resources and response; hope uses P alongside unresolved possibility and the subject's own account. The components interact but do not reduce to each other.

The mathematical core can remain the already repaired paired comparison: same target, horizon, evidence-responsive policy and declared model. The conceptual repair is to keep the conditions and authorship of that comparison attached. A value-vector comparison may reveal conflicting interests without licensing a weighted sum that conceals them.

## Hard cases the next version must retain

| Case | Required distinction |
|---|---|
| Strong undertaking, falling resources | Commitment status and capacity can move independently. |
| Helpful support during an overall decline | Beneficial counterfactual effect can coexist with lower absolute prospects. |
| One resource promised twice | Separate feasibility does not imply joint feasibility. |
| Unannounced self-undertaking | No recipient reliance is assumed. |
| Assurance causes abandonment of fallback | Communication can change exposure before delivery. |
| Jointly efficient coercive plan | Coordination does not establish legitimacy. |
| Forgotten subject or concealed burden | Apparent improvement changes the comparison's scope. |
| No demonstrated route | Unknown is not impossible and not a fabricated chance. |
| Fulfilment at one instant | Attainment need not satisfy a continuing undertaking. |
| Record updated, outgoing action stale | Saved correction does not prove downstream incorporation. |

## What would count as progress

First, show a case in which this interface changes a specific consequential distinction or action while retaining the person's aims and burdens. Then compare it with the same case without the interface. Predeclare the target confusion; preserve negative results and documentation costs. AI review agreement, increasing test counts and familiar terminology do not establish field advantage. They also do not erase the value of a repaired, inspectable proposal.

This review leaves moral standing, validity of undertakings, fair risk distribution, goal authority and burden allocation partly normative and contestable. That is an honest boundary for the maths, not a reason to abandon integration.
