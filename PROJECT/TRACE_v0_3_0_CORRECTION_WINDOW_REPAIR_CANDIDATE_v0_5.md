# TRACE v0.3.0 — CORRECTION WINDOW REPAIR CANDIDATE v0.5

**Status:** WORKING REPAIR CANDIDATE — ATTACK OBJECT — NOT FORMAL BASELINE — NOT SPINE TEXT — NOT CANON — NOT VALIDATED — NOT AUTHORITY — NOT PERMISSION — NOT CLEARANCE  
**Target:** correction-window material for later consideration against `PROJECT/TRACE_v0_3_0_SPINE_CANDIDATE_v0_2.md`  
**Lineage:** v0.4 x100 -> collapse map v0.1 -> ROOT B/A/D attacks -> collapse map v0.2 -> 25-probe closure pass -> immediate source-level self-attack on verification-time omission  
**Purpose:** reconstruct the smallest correction-window rule that survives the known attacks without turning epistemic status, independence, triggering, role labels, or aperture coverage into new primitives.

This file is intentionally standalone for its declared attack use. It does not require a reader to recover load-bearing semantics from v0.1-v0.4.

---

# 0. Claim ceiling

This candidate describes structural conditions under which a represented correction path may still fit before a represented target hardens.

It does **not** decide whether the correction should be attempted, whether the target is morally adequate, whether an actor is authorised, whether estimates are true, whether all affected scopes have been found, or whether the resulting transition is harmless.

```text
CORRECTION_WINDOW_FITS != CORRECTION_EXECUTED
CORRECTION_WINDOW_FITS != AUTHORIZATION
CORRECTION_WINDOW_FITS != MORAL_ADEQUACY
CORRECTION_WINDOW_FITS != RESTORATION
CORRECTABLE != HARMLESS
DESCRIPTION != PERMISSION
CAPABILITY != AUTHORITY
```

Where evidence does not settle a load-bearing claim, preserve `UNKNOWN`, dispute, or the narrower supported claim.

```text
UNKNOWN != ZERO_DURATION
UNKNOWN != ABSENT
UNRESOLVED != FALSE
NO_KNOWN_DEPENDENCY != INDEPENDENT
```

---

# 1. Local bindings

For one represented correction-window question, bind:

```text
q = threatened harm / failure / correction pathway
l = represented affected scope for the claim being tested
o = observation / diagnosis aperture(s)
c = correcting aperture / system / route under evaluation
g = declared correction target
u = downstream use / decision / binding event for the window result, when material
```

These are local bindings to ordinary TRACE objects/claims, not new primitives.

A valid reading may use multiple `o`, `c`, `l`, or `g` values. Compact notation is permitted only where the abstraction is honest.

---

# 2. Timing centre: use an event graph first

The primary object is a declared event/precedence graph for the correction path, not an equation that silently makes required work free.

Let:

```text
G_window(q,l,o,c,g,u)
```

represent the load-bearing events and precedence constraints between the chosen reference event and reaching target `g`.

Where material, this graph includes:

```text
signal arrival
diagnosis / interpretation
required load-bearing verification events
required result-return events
required activation / decision-conditioning events
routing / handoff
correction execution
reaching target g
use / commitment event u where the result must still be current
```

A load-bearing check does not disappear from the clock merely because it is described in another section.

```text
REQUIRED_CHECK_TIME != ZERO_DURATION
REQUIRED_REVIEW_TIME != ZERO_DURATION
RESULT_EVENTUALLY_RETURNED != PRE_USE_CHECK
```

If required checking, diagnosis or routing occurs in parallel, model the precedence graph and take its critical path. Do not add parallel durations merely because they are listed separately.

```text
SERIAL_SUM != PARALLEL_CRITICAL_PATH
```

## 2.1 Optional scalar shorthand

Only for a declared sequential case, a useful shorthand is:

[SCHEMATIC_MODEL]

```text
T_complete(q,l,o,c,g,u)
:= T_signal
 + T_diagnose
 + T_required_verify
 + T_route
 + T_correct
```

where `T_required_verify` includes only verification/review work that lies on the declared critical path and is not already included in another term.

```text
FAULT_SIGNALLED != FAULT_DIAGNOSED
CHECK_REQUIRED != CHECK_ALREADY_INCLUDED
```

If no load-bearing verification is required before the use/action being modelled, `T_required_verify` may be zero only for that declared reason—not because the duration is unknown.

```text
NOT_REQUIRED != UNKNOWN_DURATION
```

---

# 3. Preserve path closure, target closure and world irreversibility separately

## 3.1 Corrector-path closure

```text
T_path_close(q,l,c,g)
```

is the represented boundary after which this particular path through `c` can no longer complete because of route, access, authority, capability, dependency, credential, or other path-specific loss.

```text
REPAIR_UNREACHABLE_BY_c != WORLD_IRREVERSIBLE
PATH_CLOSURE != TARGET_HARDENING
```

## 3.2 Target closure / hardening

```text
T_target_close(q,l,g)
```

is the represented boundary after which reaching target `g` is too late to produce the specific claimed effect on pathway `q` for represented scope `l`.

It may be physical, biological, computational, evidentiary, institutional, contractual, political, social, or mixed.

```text
TARGET_FACING_DEADLINE != INDEPENDENT_HARDENING_BOUND
SOCIAL_DEADLINE != UNREAL_DEADLINE
DEADLINE != IRREVERSIBILITY
```

A target-facing deadline can be real and still be controlled or mutable.

---

# 4. Target g must remain inspectable

A correction target is not hidden inside a timing term.

Where load-bearing, preserve:

```text
target reference
specific threatened state / transition / edge in q addressed by g
claimed effect of reaching g
represented affected scope l reached by that effect
target selector / source
selection basis / provenance
selection or freeze time where relevant
known residue / what g does not restore
known omitted affected scopes / alternative target apertures
challenge / alternative linkage if live
```

Guards:

```text
TARGET_REACHABLE != TARGET_ADEQUATE
PREDECLARED_TARGET != LOAD_BEARING_TARGET
TARGET_NAMED != TARGET_LINK_ESTABLISHED
TARGET_LINK_ESTABLISHED != MORAL_ADEQUACY
PARTIAL_CORRECTION != RESTORATION
```

The linkage `g -> q,l` is itself a proposition with evidence/provenance, not a priority rule.

---

# 5. A load-bearing target-close clock carries control, not a binary independence label

Where deadline control can change the downstream window claim, preserve enough to expose:

```text
clock / closure reference
reference event / time origin
source / basis
controller set, if represented
available control modes / movement bounds, if represented
conditions / authority required to move it
observability / contestability of movement
estimator / evidence
current status / unknowns
```

Possible control modes are domain attributes, not universal vocabulary:

```text
advance
delay
waive
suspend
replace
selectively apply
UNKNOWN
```

Guards:

```text
CONTROLLER_NAMED != CONTROL_COMPLETE
CONTROL_POSSIBLE != CONTROL_EXERCISED
CONTROL_ABSENT_FROM_RECORD != CONTROL_ABSENT
BOUNDED_CONTROL_SET != COMPLETE_CONTROL_SET
```

---

# 6. ROOT B becomes a derived dependency diagnostic

For a load-bearing proposition/check/use, ask:

```text
independent of what dependency,
for which proposition,
for which use,
over which causal/evidential/control path,
and from what time?
```

Represent actual topology using ordinary provenance, `DEPENDS_ON`, `CONTROLS`, custody, carrier, instrument and actor relations.

A compact derived diagnostic may return:

```text
DEPENDENCY_OBSERVED
DEPENDENCY_NOT_OBSERVED
INDEPENDENCE_NOT_ESTABLISHED
```

with the dependency dimension and basis.

Preserve:

```text
SEPARATE_PARTY != INDEPENDENT_EVIDENCE
SAME_AUTHOR != USELESS_CHECK
PREFERENCE_BLIND_CHECK != INDEPENDENT_EVIDENCE_SOURCE
PRECOMMITTED != EXTERNALLY_SOURCED
DIFFERENT_OBSERVATION_TIME != DIFFERENT_CONTROL_ROOT
NO_OBSERVED_DEPENDENCY != INDEPENDENCE_ESTABLISHED
```

No new `INDEPENDENCE` primitive is proposed.

---

# 7. ROOT C — verification is a routed, timed, bounded causal process

A verifier does useful work only to the extent that the process actually supports the load-bearing proposition at the relevant use.

For each material verification event/history, preserve as applicable:

```text
exact proposition q_k actually tested
object / version / state identity tested
evidence source and provenance
selection / coverage mechanism
known omitted categories / alternate apertures
instrument / procedure / estimator
instrument capability / resolution / limits
access / authority / custody boundary
start / observation time
measurement interval and closure condition
completion time
result return route / return time
intended use / decision / binding event u
validity interval / freshness condition at u
time/cost if the check lies on the correction critical path
side effects / capacity consumed
actor / control / dependency topology
event outcome
contrary evidence / competing checks
remaining unknowns
explicit falsifier / expected counterevidence where available
```

This is a profile over existing TRACE objects/events, not a new `PROCESS` primitive.

Key guards:

```text
CHECKED_EVIDENCE != CHECKED_LOAD_BEARING_PROPOSITION
NO_COUNTEREXAMPLE_IN_SELECTED_SET != NO_COUNTEREXAMPLE
EVENTUALLY_CHECKABLE != CHECKABLE_BEFORE_USE
CHECK_COMPLETED != CHECK_RESULT_REACHED_USE
RESULT_REACHED_USE != RESULT_CURRENT_AT_USE
CHECKED_OBJECT_v1 != USED_OBJECT_v2
FULL_ROW_COVERAGE != CLOSED_MEASUREMENT_WINDOW
CHECKED_AT_t != SURVIVED_FOR_CLOSED_INTERVAL
CHECK_AVAILABLE != CHECK_AFFORDABLE_WITHOUT_MATERIAL_SIDE_EFFECT
REQUIRED_CHECK_TIME != ZERO_DURATION
```

## 7.1 Check-to-use binding

A successful check can decay between completion and use.

Where that interval is load-bearing, bind verification to `u` or state an explicit validity/freshness condition.

```text
SURVIVED_AT_CHECK_TIME != SUPPORTED_AT_USE_TIME
```

If object/version, relevant world state, target set, authority, route, or evidence changes before `u`, re-evaluate the affected claim or narrow it to the earlier time.

## 7.2 Verification cost belongs on the path when the path waits for it

If a downstream correction cannot honestly proceed until a load-bearing check returns/applies, that check's time is part of `G_window`.

If the check runs in parallel and does not extend the critical path, it need not be serially added.

```text
LOAD_BEARING_CHECK != FREE_CHECK
CHECK_IN_PARALLEL != SERIAL_DELAY
```

This closes the immediate v0.5 self-attack in which semantic verification was required while the timing equation pretended verification consumed no time.

---

# 8. ROOT A — epistemic transition / warrant remains distinct from C

C records what verification process existed and happened.

A constrains what epistemic status that represented history licenses.

```text
C = PROCESS / HISTORY
A = WARRANTED STATUS TRANSITION
```

This distinction survives the no-process case:

```text
no checker
no check path
no verification event
but representation emits EXPOSED -> CHECKED
```

The failure is an unsupported epistemic transition, not a defective C process.

Similarly:

```text
DEPENDENCE_UNSEEN -> DEPENDENCE_EXPOSED
```

may be licensed by provenance inspection without making the proposition more verified.

Preserve at least:

```text
EXPOSED != CHECKABLE
CHECKABLE != CHECKED
CHECKED != SURVIVED
SURVIVED != TRUE
PAST_SURVIVAL != CURRENT_SURVIVAL
CHECK_FAILED_TO_FALSIFY != CLAIM_PROVEN
PROCESS_CORRECT != STATUS_LABEL_CORRECT
```

A compact status view may be derived/reconstructed from canonical history. It must not become an irreversible truth ladder.

## 8.1 Conflicting histories

If material checks conflict, preserve the conflict or expose the rule/evidence that resolves it.

```text
LAST_CHECK_WINS != WARRANTED_STATUS
ONE_SURVIVED_CHECK != ALL_RELEVANT_COUNTEREVIDENCE_RESOLVED
```

Do not overwrite a dispute merely because a later event arrived.

---

# 9. Admission / aperture entry is load-bearing when represented-set sufficiency is load-bearing

A trigger cannot fire on an object that never entered the represented set.

```text
OBJECT_NOT_IN_MODEL != TRIGGER_NOT_FIRED
SCOPE_NOT_REPRESENTED != SCOPE_QUALIFIER_DROPPED
CLAIM_OMITTED != CLAIM_LABELLED_NON_LOAD_BEARING
```

When a downstream correction-window result depends on treating a represented claim/scope/route set as sufficient, the aperture/selection that produced that set is itself load-bearing.

Preserve, where material:

```text
target-set / claim-set source
selection basis
coverage comparison basis
known omitted categories
alternative apertures / registries / source sets
control / custody of selection
completeness claim and its evidence state
```

## 9.1 NEVER_ADMITTED / ADMISSION-OMISSION

The material object/scope/claim never enters the represented set.

```text
NOT_SELECTED != IRRELEVANT
VISIBLE_SCOPE != COMPLETE_AFFECTED_SCOPE
```

## 9.2 ADMITTED_ALTERED / ADMISSION-ALTERATION

The source object enters, but its meaning/relation is transformed at intake.

```text
ADMITTED != TRANSCRIBED_FAITHFULLY
EDGE_PRESENT != EDGE_FAITHFUL
OBSERVED_RENDERING != SOURCE_OBJECT
```

Where that transformation is load-bearing, preserve a source-facing reconstruction, re-execution, or other fidelity check sufficient for the declared use.

`ADMISSION` is a failure location over existing aperture/source semantics, not a proposed primitive.

---

# 10. Activation is cross-cutting: returned is not applied

A distinction may exist and still fail to condition the downstream claim/use.

```text
DISTINCTION_PRESENT != DISTINCTION_APPLIED
TRIGGER_PRESENT != TRIGGER_FIRED
RESULT_RETURNED != RESULT_APPLIED
```

For a downstream result `r`, a distinction is load-bearing when collapsing it can change the supported status, qualifier, scope, path, reachability, timing, dependency account, or other declared property of `r`.

This is an inspection rule, not a universal materiality oracle.

```text
LOAD_BEARING_UNKNOWN != NOT_LOAD_BEARING
```

Where application is itself required before the correction path may continue, that activation event belongs in `G_window` and can affect its critical path.

## 10.1 Do not use endpoint-only perturbation as the universal trigger

Adaptive systems may compensate:

```text
remove claim k -> route B activates -> endpoint X preserved
```

Therefore:

```text
SAME_ENDPOINT != SAME_CAUSAL_DEPENDENCE
COMPENSATED_COUNTERFACTUAL != NON_LOAD_BEARING
```

Where path dependence/adaptation cannot be bounded, preserve trigger/load-bearing uncertainty rather than declaring the distinction irrelevant.

Where observable, preserve whether the load-bearing result actually conditioned downstream use. If not observable, do not manufacture application from delivery.

---

# 11. Role labels are not the mechanism

Do not require a universal roster of `selector / declarer / beneficiary / controller / producer / custodian / verifier` fields.

Carry a role distinction only where it changes a load-bearing relation or supplied rule.

Deletion test:

```text
change role label only
AND no change in dependency, control, authority, evidence/provenance,
burden, scope, route, external policy/value input, or downstream inference
-> role distinction not load-bearing for this use
```

Where the distinction matters, represent the actual relation.

```text
ROLE_LABEL != CAUSAL_RELATION
ROLE_COUNT != INDEPENDENCE
```

A policy, legal or value layer may make a role label directly material. Preserve that supplied normative source rather than pretending TRACE generated the priority.

---

# 12. Window calculations and qualified outputs

Let `T_complete` be the represented critical-path completion time derived from `G_window` for the declared abstraction.

Then:

```text
PATH_FITS_c
:= T_complete(q,l,o,c,g,u) < T_path_close(q,l,c,g)
```

and:

```text
TARGET_WINDOW_FITS_AT_DECLARED_CLOSE
:= T_complete(q,l,o,c,g,u) < T_target_close_declared(q,l,g)
```

These are claims under declared evidence, estimates and abstractions.

If control over the target-close clock is load-bearing, carry a qualifier derived from represented control evidence, for example:

```text
CONTROL_SENSITIVE
ROBUST_TO_REPRESENTED_CONTROL
CONTROL_UNKNOWN
```

`ROBUST_TO_REPRESENTED_CONTROL` means only that the result survives the represented feasible control set.

```text
ROBUST_TO_REPRESENTED_CONTROL != IMMUTABLE
ROBUST_TO_REPRESENTED_CONTROL != COMPLETE_CONTROL_SET
```

A higher-level derived result may be emitted only when constituent claims are supported to the declared level:

```text
CORRECTION_WINDOW_FITS_FOR(c,g)
```

At minimum carry:

```text
path feasibility basis
target-close basis
target linkage g -> q,l
scope/aperture qualifier where load-bearing
control qualifier where load-bearing
verification/status qualifier where load-bearing
use-time/freshness binding where load-bearing
activation/application qualifier where load-bearing
residue / non-restoration
```

Do not hide these qualifiers behind one Boolean.

---

# 13. Minimal derived attack profile

A bounded implementation may expose the following **only where load-bearing**:

```yaml
correction_window:
  pathway_ref: q
  affected_scope_refs: [l]
  observation_aperture_refs: [o]
  corrector_ref: c
  target_ref: g
  use_binding_ref: u

  completion:
    model: event_graph | sequential | other
    event_refs: []
    critical_path_refs: []
    required_verification_refs: []
    unknowns: []

  path_close:
    claim_ref: null
    source_refs: []
    time_or_event: null

  target_close:
    claim_ref: null
    source_refs: []
    time_or_event: null
    controller_refs: []
    feasible_control_refs: []

  target_linkage:
    proposition_ref: null
    evidence_refs: []
    residue_refs: []

  aperture_coverage:
    source_ref: null
    selection_basis_refs: []
    known_omission_refs: []
    alternative_aperture_refs: []

  verification_refs: []
  dependency_diagnostic_refs: []
  activation_witness_refs: []
  falsifier_refs: []

  derived_outputs: []
  unresolved: []
```

This profile is scaffolding, not canonical schema.

```text
PROFILE_FIELD != PRIMITIVE
PROFILE_COMPLETE != WORLD_COMPLETE
```

A smaller implementation is preferable if it reconstructs the same load-bearing distinctions.

---

# 14. Worked transfer specimens

## 14.1 Published is not checked

```text
claim q is posted publicly
provenance is intact
no verifier exists
```

Allowed:

```text
EXPOSED
CHECK_PATH: NONE ESTABLISHED
```

Not allowed:

```text
CHECKED
```

The failure is ROOT A even though no C process exists.

## 14.2 Complete rows, open day

```text
all rows through 18:05 observed
downstream q = full-day rate
```

```text
FULL_ROW_COVERAGE != CLOSED_MEASUREMENT_WINDOW
```

C records the intended interval and closure condition. A refuses `SURVIVED_FOR_CLOSED_INTERVAL` until warranted.

## 14.3 Required verifier takes twenty minutes

```text
target closes in 15 min
raw correction mechanics take 5 min
required load-bearing check takes 20 min and must return before route opens
```

A formula that counts only the 5-minute mechanics falsely prints a fit.

`G_window` correctly places the check on the critical path, so the represented completion exceeds the target close.

```text
REQUIRED_CHECK_TIME != ZERO_DURATION
```

If the same check began earlier and runs in parallel without extending the critical path, do not add twenty minutes again.

## 14.4 True premises, fictional join

```text
q1, q2, q3 inputs are individually checked
derived proposition q4 joins them through an unsupported flattering inference
```

```text
TRUE_INPUTS != VALID_JOIN
CHECKED_INPUTS != SURVIVED_DERIVED_PROPOSITION
```

Verification must target `q4` or its inferential dependency, not inherit premise status.

## 14.5 Omitted household

```text
registry R omits affected household h
all represented claims over R are handled correctly
```

If output depends on `R` being sufficient for affected scope, the selection aperture for `R` is load-bearing. No trigger over represented households substitutes for admission accounting.

## 14.6 Controlled administrative deadline

```text
current close = Friday
correction completes Thursday
controller can extend but cannot advance close
```

The window may be robust to the represented control set even though the deadline is socially controlled.

If the controller can advance to Wednesday, the Thursday result is control-sensitive and cannot be emitted as robust.

## 14.7 Correct record, non-restored loss

```text
g = publish correction that accurately records a mismatch
lost intended wording cannot be recovered
```

```text
PARTIAL_CORRECTION != RESTORATION
```

Carry the residue.

---

# 15. Explicit falsifiers for v0.5

Hold or repair this candidate if any of the following survives:

1. a correction-window failure survives correct A, correct C, dependency topology, activation, admission/aperture accounting and intact carrier;
2. the A/C distinction adds no protection after the no-process false-upgrade case is represented correctly;
3. a result is represented as current at use despite version/world/target-set change between check and `u`;
4. competing verification histories are silently resolved by event order;
5. result delivery is treated as proof that downstream use incorporated it;
6. a required load-bearing verification/review delay is omitted from the critical path;
7. parallel verification is double-counted as serial delay;
8. a negative or complete-scope claim survives while its selection/aperture basis is insufficient or omitted;
9. an admitted-altered source passes because presence is mistaken for fidelity;
10. endpoint compensation makes a load-bearing claim disappear from the trigger surface;
11. role labels are required where they change no relation/inference;
12. multiple parties/models/carriers upgrade independence despite a shared dependency root;
13. a reachable weak target silently inherits the semantics of a stronger threatened loss;
14. an interested actor's controllable close is treated as independent merely because it is named;
15. verification destroys correction capacity but is still counted as a usable pre-use check;
16. `WINDOW_FITS` is used to infer permission, legitimacy or obligation;
17. a bounded reader of this file cannot recover a load-bearing rule without an unseen predecessor;
18. the conditional machinery becomes effectively a universal checklist rather than firing only where distinctions are load-bearing.

One worked counterexample is enough to keep v0.5 out of the spine.

---

# 16. Current disposition

The smallest surviving centre is not a longer inequality. It is a disciplined claim about what the inequality can mean.

> A correction-window result is support for a particular represented path reaching a particular represented target before a particular represented target-state closure, under an explicit proposition/scope/aperture, evidence/verification history, dependency/control account, critical-path timing, and use-time boundary. It must not upgrade exposure to checking, party count to independence, delivery to application, selected scope to complete scope, reachable target to adequate repair, or path closure to world hardening.

Compression:

```text
WINDOW CLAIM
  = critical-path timing
  + target timing
  + target linkage
  + proposition/scope/aperture binding
  + warranted epistemic status
  + verification process/history
  + dependency/control qualifiers
  + check-to-use binding
  + activation where load-bearing
  + residue/non-restoration
```

No new primitive is proposed by this candidate.

Do not integrate v0.5 into the spine merely because it is cleaner than v0.4. Attack it as a new object.
