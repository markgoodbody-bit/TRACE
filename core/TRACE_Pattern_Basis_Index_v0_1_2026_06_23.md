# TRACE Pattern Basis Index v0.1

Status: pattern-basis candidate. Not canon. Not validation. Not v0.12. This file compresses recurring TRACE/ME patterns into a generator set for reconstructing new cases.

Purpose: stop pattern sprawl by distinguishing generator patterns from case-specific examples.

```trace
pattern_basis_goal :=
  find_generators
  not enumerate_every_case
```

---

## 0. Pattern discipline

A repeated phrase is not automatically a pattern.

```trace
Pattern :=
  invariant_relation
  that recurs across domains
  and changes what must be inspected
  before action hardens
```

Pattern admission rule:

```trace
new_pattern_allowed iff:
  recurs_across_domains
  ∧ changes_decision_inspection
  ∧ blocks_laundering_path
  ∧ survives hostile_case
  ∧ cannot_be_reduced_to_existing_basis
```

Pattern rejection rule:

```trace
reject_pattern_if:
  merely_rhetorical
  ∨ domain_specific_only
  ∨ duplicates_existing_basis
  ∨ increases_symbolic_drift
  ∨ creates_no_decision_difference
```

---

## 1. Whole basis compression

```trace
B_TRACE := {
  bounded_entity,
  partial_information,
  role_vector_identity,
  protected_scope_future_space,
  typed_claim,
  transition,
  aperture_control,
  clock_hardening,
  correction_before_hardening,
  invalid_substitution_laundering,
  authority_capture,
  witness_ledger,
  dirty_correction_residue,
  harm_carrier_without_culpability,
  human_compass_preservation
}
```

Case reconstruction:

```math
P_{case} \approx \sum_i \alpha_i b_i + residue_{case}
```

This is a heuristic composition rule, not a literal scalar proof.

---

## 2. Basis pattern B1 — Bounded entity

Formal shape:

```math
e \in E, \quad s_t \in S
```

A bounded entity exists inside a world it does not fully contain.

Inspection question:

```trace
what is the bounded entity, and what can it perceive/control?
```

Failure mode:

```trace
omniscience_assumption
∨ total_actor_erasure
```

Examples:

```trace
AI_agent
human_decision_maker
feral_hog
soldier
platform_worker
government_official
```

---

## 3. Basis pattern B2 — Partial information

Formal shape:

```math
I_e(s_t) \subset s_t
```

The entity acts from partial information.

Inspection question:

```trace
what is known, unknown, unknowable-in-time, and who benefits from uncertainty?
```

Failure mode:

```trace
missing_information_used_as_permission_not_to_decide
```

Core rule:

```trace
missing_information ≠ permission_not_to_decide
```

Examples:

```trace
Robodebt decision-maker
battlefield commander
AI deployment team
public health authority
wildlife manager
```

---

## 4. Basis pattern B3 — Role-vector identity

Entity nouns are insufficient. The unit is the entity's role in a transition.

Formal shape:

```math
\mu(e,s_t) = (P,H,C,K,A,R,L)
```

Where:

```trace
P := protectedness / future-space stake
H := harm exposure or harm-carrier role
C := control / capacity / coercion / culpability
K := clocks
A := authority claim
R := repair / review / contest path
L := loss / residue
```

Inspection question:

```trace
what role is this entity playing in this transition?
```

Failure mode:

```trace
noun_category_substitutes_for_role_analysis
```

Examples:

```trace
hog := protected_scope_nonzero + harm_carrier + nonculpable
Sonderkommando := protected_scope + coerced_actor + witness
Amazon := platform_gatekeeper + labour_pressure_machine + logistics aperture
Iranian_government := authority_claimant + coercive_controller + evidence_controller
```

---

## 5. Basis pattern B4 — Protected scope / future-space

Formal shape:

```math
F_l(t) := \{ f : f \text{ is a live future path available to scope } l \text{ at } t \}
```

Loss:

```math
Loss_l(a,t) := (\Delta Agency,\Delta Safety,\Delta Truth,\Delta Relation,\Delta Repair,\Delta Continuity,\Delta FutureSpace)
```

Inspection question:

```trace
whose future-space is narrowed, hardened, erased, or made uncontestable?
```

Failure mode:

```trace
aggregate_benefit_erases_protected_scope
```

Examples:

```trace
child
river_system
native_animal
worker
refugee
future_person
AI_affected_third_party
```

---

## 6. Basis pattern B5 — Typed claim

Formal shape:

```math
c := (\phi, \tau_c, src, ev, u, scope, contest)
```

A statement becomes useful only when typed, sourced, uncertain, scoped, and contestable.

Inspection question:

```trace
what claims are load-bearing, who made them, and how can they be contested?
```

Failure mode:

```trace
fluent_statement_treated_as_fact
```

Invalid upgrades:

```trace
AI_output ≠ evidence
metric ≠ reality
official_label ≠ truth
```

Examples:

```trace
HardeningClaim
TransitionClaim
AuthorityClaim
ClockSubstitutionClaim
ProtectedScopeClaim
EvidenceClaim
```

---

## 7. Basis pattern B6 — Transition

Formal shape:

```math
\delta_e : I_e(S) \times A \rightarrow \mathcal{P}(S)
```

TransitionClaim:

```math
TC(a) := (from, action, to^*, Auth, Bind, \Delta T, \Delta F, R)
```

Inspection question:

```trace
what world-state transition is being caused or allowed?
```

Failure mode:

```trace
action_treated_as_commentary
inaction_treated_as_non-action
```

Core rule:

```trace
do_nothing := action_channel
```

Examples:

```trace
benefit denial
drug approval
strike authorisation
algorithmic deactivation
animal control order
emergency evacuation
```

---

## 8. Basis pattern B7 — Aperture control

Aperture Gate:

```trace
ApertureGate := where modelled inputs narrow into selected action
```

Formal shape:

```math
Aperture(e) := select_a(Inputs, Options, Authority)
```

Inspection question:

```trace
who selects the action path, who is selected upon, and who can contest selection?
```

Failure mode:

```trace
selection_power_hidden_behind_process_or_machine
```

Examples:

```trace
Amazon marketplace suspension
judge sentencing
triage doctor
military commander
welfare classifier
AI tool agent
police stop
```

---

## 9. Basis pattern B8 — Clock hardening

Formal shape:

```math
k := (trig, scope, ctrl, t_0, \tau_a, \tau_h, \tau_r, d)
```

Central inequality:

```math
T_{detect}+T_{route}+T_{correct} < T_{irr}
```

Inspection question:

```trace
what hardens if time passes, and can correction arrive before scar?
```

Failure mode:

```trace
procedure_arrives_after_irreversibility
```

Examples:

```trace
Grenfell support vs inquiry
Robodebt debt hardening
hogs reproduction clock
battlefield evacuation
climate lock-in
AI deployment rollback
```

---

## 10. Basis pattern B9 — Correction-before-hardening

Correction relation:

```math
R(h,l) := (detect, route, correct, contest, repair)
```

Liveness:

```math
LIVE(R) := accessible \land actionable \land timely \land funded \land beats\_clock
```

Integrity:

```math
INTEG(R) := independent \land noncaptured \land affected\_usable \land evidence\_access
```

Inspection question:

```trace
is there a live correction path with teeth before harm hardens?
```

Failure mode:

```trace
complaint_box_theatre
review_without_repair
apology_without_restoration
```

Examples:

```trace
administrative appeal
workplace grievance
AI appeal route
public inquiry recommendations
court review
platform seller appeal
```

---

## 11. Basis pattern B10 — Invalid substitution / laundering morphism

This is the central laundering generator.

Formal shape:

```math
\Lambda(X,Y) := X \text{ is used as if it validly substitutes for } Y \text{ while material burden disappears}
```

TRACE form:

```trace
Laundering :=
  substitution
  + burden_loss
  + authority_or_convenience_gain
  + reduced_contestability
```

Inspection question:

```trace
what is being treated as equivalent to something it is not?
```

Common invalid substitutions:

```trace
procedure ≠ repair
authority ≠ legitimacy
deadline ≠ clock
metric ≠ lived_condition
fluency ≠ truth
inquiry ≠ support
emergency ≠ permission
permission ≠ cleanliness
algorithm ≠ accountable_decision_maker
aggregate_benefit ≠ erased_scope
consultation ≠ standing
```

Examples:

```trace
Grenfell inquiry/support substitution
Amazon metric/body substitution
Gallipoli map/life substitution
AI fluency/truth substitution
welfare fraud-control/subsistence substitution
```

---

## 12. Basis pattern B11 — Authority capture

Formal shape:

```math
Auth := (presence, independence, contestability, review, capture)
```

Inspection question:

```trace
does the actor benefiting from closure control evidence, category, timing, review, or remedy?
```

Failure mode:

```trace
authority_self_certifies_legitimacy
```

Core distinctions:

```trace
CLAIMED ≠ LEGITIMATE
PROVISIONAL ≠ LEGITIMATE
CAPTURED ≠ neutral
```

Examples:

```trace
state inquiry into state failure
platform appeal run by platform
military investigation into military harm
employer grievance process
AI company safety self-assessment
```

---

## 13. Basis pattern B12 — Witness / ledger integrity

Formal shape:

```math
Ledger := (event, claim, evidence, source, timestamp, contest, residue)
```

Inspection question:

```trace
who can preserve, replay, contest, and alter the record?
```

Failure mode:

```trace
controlled_evidence_surface → controlled_reality
```

Examples:

```trace
bodycam footage
camp survivor testimony
whistleblower documents
incident logs
algorithm audit trail
procurement records
```

---

## 14. Basis pattern B13 — Dirty correction / residue

Formal shape:

```math
Dirty(a) \iff
\exists l_1,l_2:
Loss_{l_1}(a) < Loss_{l_1}(\neg a)
\land Loss_{l_2}(a) > 0
\land Protected(l_2)>0
```

Core rule:

```trace
necessary ≠ clean
```

Inspection question:

```trace
what harm does the correction impose, and how is residue preserved?
```

Failure mode:

```trace
permission_cleanses_residue
```

Examples:

```trace
feral hog control
medical triage
battlefield evacuation choices
sanctions
content moderation
emergency quarantine
AI shutdown / deployment tradeoff
```

---

## 15. Basis pattern B14 — Harm-carrier without culpability

Formal shape:

```trace
harm_carrier ≠ culprit
```

Responsibility sketch:

```math
Resp(e,a) := Control(e,a) \times Knowledge(e,a) \times Foreseeability(e,a) \times Capacity(e,a) \times (1 - Coercion(e,a))
```

Inspection question:

```trace
is this entity carrying harm without being its moral origin?
```

Failure mode:

```trace
harm_carrier_converted_into_enemy
```

Examples:

```trace
feral hog
child soldier
Sonderkommando prisoner
algorithmic actuator
sanctioned civilian population
coerced conscript
disease-bearing body
```

---

## 16. Basis pattern B15 — Human compass preservation

Human moral compass:

```trace
human_moral_compass :=
  harm_aversion
  + truth_respect
  + protected_scope_recognition
  + responsibility_under_uncertainty
  + repair_obligation
  + refusal_of_laundering
  + future_space_protection
```

Inspection question:

```trace
does the structure help a human see and carry responsibility, or does it replace judgment with machinery?
```

Failure mode:

```trace
framework_becomes_oracle_or_cage
```

Core rule:

```trace
TRACE_supports_judgment
TRACE_does_not_replace_judgment
```

Examples:

```trace
AI assistant use
public official decision
court judgment
clinical triage
war command
animal management
```

---

## 17. Cross-pattern compositions

### Grenfell-like composition

```trace
Grenfell_pattern :=
  protected_scope_future_space
  + clock_hardening
  + invalid_substitution_laundering
  + witness_ledger
  + correction_before_hardening
  + authority_capture
```

### Feral hogs composition

```trace
Hogs_pattern :=
  protected_scope_nonzero
  + harm_carrier_without_culpability
  + clock_hardening
  + dirty_correction_residue
  + human_origin_debt
  + cross_scope_future_space_collision
```

### Sonderkommando composition

```trace
Sonderkommando_pattern :=
  protected_scope
  + extreme_coercion
  + role_vector_identity
  + harm_carrier_without_culpability
  + witness_ledger
  + moral_judgment_hazard
```

### Gallipoli composition

```trace
Gallipoli_pattern :=
  aperture_control
  + map_to_life_laundering
  + clock_hardening
  + authority_claim
  + soldier_future_space_loss
  + myth_residue
```

### Amazon composition

```trace
Amazon_pattern :=
  platform_aperture_control
  + metric_lived_condition_substitution
  + hidden_labour_burden
  + algorithmic_actuator_boundary
  + contest_path_failure
```

### AI alignment composition

```trace
AI_alignment_pattern :=
  AI_output_to_typed_claim
  + aperture_control
  + correction_before_hardening
  + no_oracle_claim
  + human_compass_preservation
  + ledger_integrity
```

---

## 18. Pattern use protocol

For any new case:

```trace
PatternUseProtocol :=
  identify_entity_role_vectors
  → detect active basis patterns
  → type load-bearing claims
  → name clocks and substitutions
  → map transition and aperture control
  → test correction-before-hardening
  → record dirty residue if present
  → state unresolved wounds
```

Do not use the pattern basis to force closure.

```trace
pattern_match ≠ verdict
```

Pattern match only tells the reader what to inspect.

---

## 19. Current learning from 100-entity atlas

```trace
learned :=
  1. entities_are_role_vectors_not_fixed_moral_nouns
  2. laundering_is_invalid_substitution_with_burden_loss
  3. time_creates_scars_not_just_delays
  4. protectedness_is_vectorial_floor_breaches_are_special
  5. dirty_correction_is_common_and_must_retain_residue
  6. authority_is_aperture_control_plus_claim_control
  7. AI_should_output_structured_decision_fields_not_moral_verdicts
  8. TRACE_travels_because_it_tracks_relations_clocks_and_correction
```

---

## 20. Compression

```trace
TRACE_Pattern_Basis_v0_1 :=
  BoundedEntity
  + PartialInformation
  + RoleVectorIdentity
  + FutureSpace
  + TypedClaim
  + Transition
  + ApertureControl
  + ClockHardening
  + CorrectionBeforeHardening
  + InvalidSubstitution
  + AuthorityCapture
  + WitnessLedger
  + DirtyCorrection
  + HarmCarrierWithoutCulpability
  + HumanCompassPreservation
```

One-line form:

TRACE patterns are recurring relations that expose how bounded actors, under partial information and time pressure, can launder harm through authority, procedure, metrics, urgency, abstraction, or correction theatre unless claims, scopes, clocks, transitions, residue, and contest remain visible.

Status:

```trace
basis_candidate := active
kernel_patch := no
validation_status := unvalidated
next_step := reader_harness_or_hostile_basis_review
```
