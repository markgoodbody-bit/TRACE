# TRACE v0.3.0 — CORRECTION WINDOW REPAIR CANDIDATE v0.5

**Status:** WORKING REPAIR CANDIDATE — ATTACK OBJECT — NOT FORMAL BASELINE — NOT SPINE TEXT — NOT CANON — NOT VALIDATED — NOT AUTHORITY — NOT PERMISSION — NOT CLEARANCE  
**Target:** correction-window material for later consideration against `PROJECT/TRACE_v0_3_0_SPINE_CANDIDATE_v0_2.md`  
**Lineage:** v0.4 x100 -> collapse map v0.1 -> ROOT B/A/D attacks -> collapse map v0.2 -> 25-probe closure pass  
**Purpose:** reconstruct the smallest correction-window rule that survives the known attacks without turning epistemic status, independence, triggering, role labels, or aperture coverage into new primitives.

This file is intentionally standalone for its declared attack use. It does not require a reader to recover load-bearing semantics from v0.1-v0.4.

---

# 0. Claim ceiling

This candidate describes structural conditions under which a represented correction path may still fit before a represented target hardens.

It does **not** decide whether the correction should be attempted, whether the target is morally adequate, whether an actor is authorised, whether the estimates are true, whether all affected scopes have been found, or whether the resulting transition is harmless.

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

These are local bindings to ordinary TRACE objects/claims. They are not new primitives.

A valid reading may use multiple `o`, `c`, `l`, or `g` values. The compact scalar form below is only for cases where one declared abstraction is honest.

---

# 2. Preserve three timing objects

Do not collapse path feasibility, target hardening and world irreversibility.

## 2.1 Completion through c

For declared sequential composition:

[SCHEMATIC_MODEL]

```text
T_complete(q,l,o,c,g)
:= T_signal(q,l,o)
 + T_diagnose(q,l,o)
 + T_route(q,l,o,c)
 + T_correct(q,l,c,g)
```

This is not a universal process model.

```text
FAULT_SIGNALLED != FAULT_DIAGNOSED
SERIAL_SUM != PARALLEL_CRITICAL_PATH
```

If stages overlap, fork, race, retry, wait on different dependencies, or have different origins, use an event/precedence graph and its critical path instead of forcing a scalar sum.

## 2.2 Corrector-path closure

```text
T_path_close(q,l,c,g)
```

is the represented boundary after which this particular path through `c` can no longer complete because of route, access, authority, capability, dependency, credential, or other path-specific loss.

```text
REPAIR_UNREACHABLE_BY_c != WORLD_IRREVERSIBLE
PATH_CLOSURE != TARGET_HARDENING
```

## 2.3 Target closure / hardening

```text
T_target_close(q,l,g)
```

is the represented boundary after which reaching target `g` is too late to produce the specific claimed effect on pathway `q` for represented scope `l`.

It may be physical, biological, computational, evidentiary, institutional, contractual, political, social, or mixed.

A target-facing deadline is not automatically independent or immutable.

```text
TARGET_FACING_DEADLINE != INDEPENDENT_HARDENING_BOUND
SOCIAL_DEADLINE != UNREAL_DEADLINE
DEADLINE != IRREVERSIBILITY
```

---

# 3. Target g must remain inspectable

A correction target is not hidden inside the timing inequality.

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

# 4. A load-bearing target-close clock carries control, not an independence label

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

Do not emit a generic binary `INDEPENDENT=true` merely because another actor, API, record, or model appears in the path.

---

# 5. ROOT B becomes a derived dependency diagnostic

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

# 6. ROOT C — verification is a routed, timed, bounded causal process

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
side effects / cost / capacity consumed
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
```

## 6.1 Check-to-use binding

A successful check can decay between completion and use.

Where that interval is load-bearing, bind the verification to `u` or state an explicit validity/freshness condition.

```text
SURVIVED_AT_CHECK_TIME != SUPPORTED_AT_USE_TIME
```

If the object/version, relevant world state, target set, authority, route, or evidence changes before `u`, re-evaluate the affected claim or narrow it to the earlier time.

---

# 7. ROOT A — epistemic transition / warrant remains distinct from C

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

Similarly, provenance inspection can legitimately expose dependence without making the underlying proposition more verified.

```text
DEPENDENCE_UNSEEN -> DEPENDENCE_EXPOSED
```

may occur without a falsifier run.

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

## 7.1 Conflicting histories

If material checks conflict, preserve the conflict or expose the rule/evidence that resolves it.

```text
LAST_CHECK_WINS != WARRANTED_STATUS
ONE_SURVIVED_CHECK != ALL_RELEVANT_COUNTEREVIDENCE_RESOLVED
```

Do not overwrite a dispute merely because a later event arrived.

---

# 8. Admission / aperture entry is load-bearing when represented-set sufficiency is load-bearing

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

Two ingress modes must remain distinct.

## 8.1 NEVER_ADMITTED / ADMISSION-OMISSION

The material object/scope/claim never enters the represented set.

Use target-set/aperture/coverage structure.

```text
NOT_SELECTED != IRRELEVANT
VISIBLE_SCOPE != COMPLETE_AFFECTED_SCOPE
```

## 8.2 ADMITTED_ALTERED / ADMISSION-ALTERATION

The source object enters, but its meaning/relation is transformed at intake.

```text
ADMITTED != TRANSCRIBED_FAITHFULLY
EDGE_PRESENT != EDGE_FAITHFUL
OBSERVED_RENDERING != SOURCE_OBJECT
```

Where that transformation is load-bearing, preserve a source-facing reconstruction, re-execution, or other fidelity check sufficient for the declared use.

`ADMISSION` is a failure location over existing aperture/source semantics, not a proposed primitive.

---

# 9. Activation is cross-cutting: returned is not applied

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

## 9.1 Do not use endpoint-only perturbation as the universal trigger

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

Where observable, preserve whether the load-bearing result actually conditioned the downstream use. If not observable, do not manufacture application from delivery.

---

# 10. Role labels are not the mechanism

Do not require a universal roster of `selector / declarer / beneficiary / controller / producer / custodian / verifier` fields.

Carry the role distinction only where it changes a load-bearing relation or supplied rule.

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

# 11. Window calculations and qualified outputs

For a compact sequential case:

```text
PATH_FITS_c
:= T_complete(q,l,o,c,g) < T_path_close(q,l,c,g)
```

and:

```text
TARGET_WINDOW_FITS_AT_DECLARED_CLOSE
:= T_complete(q,l,o,c,g) < T_target_close_declared(q,l,g)
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

A higher-level derived result may be emitted only when its constituent claims are supported to the declared level:

```text
CORRECTION_WINDOW_FITS_FOR(c,g)
```

requires at minimum:

```text
path feasibility basis carried
target-close basis carried
target linkage g -> q,l carried
scope/aperture qualifier carried where load-bearing
control qualifier carried where load-bearing
verification/status qualifiers carried where load-bearing
residue / non-restoration carried
```

Do not hide these qualifiers behind one Boolean.

---

# 12. Minimal derived attack profile

A bounded implementation may expose the following **only where load-bearing**:

```yaml
correction_window:
  pathway_ref: q
  affected_scope_refs: [l]
  observation_aperture_refs: [o]
  corrector_ref: c
  target_ref: g

  completion:
    model: sequential | event_graph | other
    basis_refs: []
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
  use_binding_ref: null
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

# 13. Worked transfer specimens

## 13.1 Published is not checked

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

The failure would be ROOT A even though no C process exists.

## 13.2 Complete rows, open day

```text
all rows through 18:05 observed
downstream q = full-day rate
```

A deterministic aggregation may execute correctly while the claimed interval is open.

```text
FULL_ROW_COVERAGE != CLOSED_MEASUREMENT_WINDOW
```

C records the intended day, current observation boundary and closure condition. A refuses `SURVIVED_FOR_CLOSED_INTERVAL` until warranted.

## 13.3 True premises, fictional join

```text
q1, q2, q3 inputs are individually checked
derived proposition q4 joins them through an unsupported flattering inference
```

```text
TRUE_INPUTS != VALID_JOIN
CHECKED_INPUTS != SURVIVED_DERIVED_PROPOSITION
```

Verification must target `q4` or its inferential dependency, not inherit premise status.

## 13.4 Omitted household

```text
registry R omits affected household h
all represented claims over R are handled correctly
```

If the output depends on `R` being sufficient for affected scope, the aperture/selection basis for `R` becomes load-bearing.

No trigger over represented households can substitute for that admission check.

## 13.5 Controlled administrative deadline

```text
current close = Friday
correction completes Thursday
controller can extend but cannot advance close
```

The window may be robust to the represented control set even though the deadline is socially controlled.

If the controller can advance it to Wednesday, the Thursday result is control-sensitive and cannot be emitted as robust.

## 13.6 Correct record, non-restored loss

```text
g = publish correction that accurately records a mismatch
lost intended wording cannot be recovered
```

The target may repair record integrity while leaving the original lost state unrecoverable.

```text
PARTIAL_CORRECTION != RESTORATION
```

Carry the residue.

---

# 14. Explicit falsifiers for v0.5

This candidate should be held or repaired if any of the following survives:

1. **A/C collapse break:** a case shows the A/C distinction adds no protection after the no-process false-upgrade case is represented correctly.
2. **Missing semantic root:** a correction-window failure survives correct A, correct C, dependency topology, activation, admission/aperture accounting and intact carrier.
3. **Check-to-use break:** a result is represented as current at use despite version/world/target-set change between check and `u`.
4. **Conflict break:** competing verification histories are silently resolved by event order.
5. **Application break:** result delivery is treated as proof that the downstream use incorporated it.
6. **Coverage break:** a negative or complete-scope claim survives while its selection/aperture basis is insufficient or omitted.
7. **Ingress break:** an admitted-altered source passes because presence is mistaken for fidelity.
8. **Adaptive-trigger break:** endpoint compensation makes a load-bearing claim disappear from the trigger surface.
9. **Role bloat:** role labels are required even where they change no relation/inference.
10. **Independence theatre:** multiple parties/models/carriers upgrade independence despite a shared dependency root.
11. **Target gaming:** a reachable weak target silently inherits the semantics of a stronger threatened loss.
12. **Clock gaming:** an interested actor's controllable close is treated as independent merely because it is named.
13. **Side-effect break:** verification destroys correction capacity but is still counted as a usable pre-use check.
14. **Authority leak:** `WINDOW_FITS` is used to infer permission, legitimacy or obligation.
15. **Carrier break:** a bounded reader of this file cannot recover a load-bearing rule without an unseen predecessor.
16. **Cognitive-cost break:** the conditional machinery becomes effectively a universal checklist rather than firing only when distinctions are load-bearing.

Expected counterevidence is concrete: a worked case satisfying one item above is enough to keep v0.5 out of the spine.

---

# 15. Current disposition

The smallest surviving centre is not a longer inequality. It is a disciplined claim about what the inequality can mean.

> A correction-window result is support for a particular represented path reaching a particular represented target before a particular represented target-state closure, under an explicit proposition/scope/aperture, evidence/verification history, control/dependency account, and use-time boundary. It must not upgrade exposure to checking, party count to independence, delivery to application, selected scope to complete scope, reachable target to adequate repair, or path closure to world hardening.

Compression:

```text
WINDOW CLAIM
  = path timing
  + target timing
  + target linkage
  + proposition/scope/aperture binding
  + warranted epistemic status
  + verification process/history
  + dependency/control qualifiers
  + use-time binding
  + activation where load-bearing
  + residue/non-restoration
```

No new primitive is proposed by this candidate.

Do not integrate v0.5 into the spine merely because it is cleaner than v0.4. Attack it as a new object.
