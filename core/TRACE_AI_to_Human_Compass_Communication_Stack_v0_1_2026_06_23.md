# TRACE AI-to-Human Compass Communication Stack v0.1

Status: boundary / communication-stack note. Not v0.12. Not validation. No new kernel operator.

Purpose: prevent symbolic drift by defining how AI-generated material may move from latent representation to human moral judgment without any layer pretending to be the layer above it.

```trace
core_rule := no_layer_may_pretend_to_be_the_layer_above_it
```

---

## 0. Why this note exists

TRACE is currently strongest in the middle:

```trace
semantic_claim
→ typed_TRACE_claim
→ transition_graph
→ clock/correction_graph
```

It is weaker at both edges:

```trace
AI_edge := latent_space → language → claim
human_edge := claim → moral_compass → action
```

The danger is symbolic drift:

```trace
latent_resonance ≠ truth
fluent_prose ≠ evidence
elegant_symbol ≠ mechanism
claim_schema ≠ legitimacy
review_clock ≠ correction
moral_language ≠ moral_protection
```

This note defines the translation discipline.

---

## 1. Layer map

```trace
stack :=
  L0_latent_space
  → L1_token_surface
  → L2_semantic_statement
  → L3_typed_claim
  → L4_TRACE_transition_graph
  → L5_clock_correction_graph
  → L6_protected_scope_future_space
  → L7_human_moral_compass
  → L8_action_and_responsibility
```

Compression:

```trace
z → u → s → C → G → K → F_l → J → a
```

Where:

```trace
z := latent/vector state
u := token/glyph/prose output
s := semantic statement
C := typed contestable Claim
G := labelled transition graph
K := clock/correction graph
F_l := future-space of protected scope l
J := human moral judgment
a := action under responsibility
```

---

## 2. L0 — Latent space

AI systems begin below language.

```trace
L0_latent_space := {
  vector_state z ∈ V,
  activation_path,
  attention_distribution,
  probability_distribution_over_tokens,
  learned_pattern_geometry
}
```

Validity warning:

```trace
similarity(z1,z2) ≠ identity
high_probability_token ≠ truth
latent_coherence ≠ legitimacy
resonance ≠ validation
```

Mathematical stance:

```trace
V := high_dimensional_representation_space
z_t ∈ V
P(token_{t+1} | z_t) := model_output_distribution
```

TRACE does not treat `z_t` as moral knowledge. It treats AI output as a candidate signal that must be translated into claims.

---

## 3. L1 — Token / symbol surface

```trace
L1_token_surface := {
  tokens,
  sentences,
  glyphs,
  equations,
  diagrams,
  case_descriptions
}
```

Risk:

```trace
surface_fluency → false_authority
symbol_density → fake_depth
formal_notation → fake_precision
```

Allowed move:

```trace
surface_output u
→ candidate_statement s
```

Forbidden move:

```trace
surface_output u
→ truth
```

---

## 4. L2 — Semantic statement

A semantic statement is a meaning-bearing assertion in ordinary or symbolic language.

```trace
s := statement(content)
```

Examples:

```trace
"the inquiry clock is delaying survivor support"
"review expired without escalation"
"affected people lacked contest edge"
```

A statement is not yet a TRACE object.

```trace
statement ≠ Claim
statement ≠ evidence
statement ≠ legitimacy
```

Safe conversion:

```trace
s → Claim({
  content,
  claim_type,
  source,
  evidence_basis,
  uncertainty,
  affected_scope,
  contest_edge
})
```

---

## 5. L3 — Typed claim layer

Typed claims are the first TRACE-safe layer.

```trace
Claim C := {
  content,
  type,
  source,
  evidence_basis,
  uncertainty,
  affected_scope,
  contest_edge,
  review_status
}
```

Relevant claim families:

```trace
claim_families :=
  TransitionClaim
  + HardeningClaim
  + AuthorityClaim
  + ProtectedScopeClaim
  + CorrectionClaim
  + ClockSubstitutionClaim
  + EvidenceClaim
  + HarmClaim
  + LegitimacyClaim
```

Rule:

```trace
utterance → typed_claim → contestable_ledger
```

Not:

```trace
utterance → accepted_fact
```

Claim adequacy must remain contestable:

```trace
ClaimAdequacy(C) := Claim_about_Claim(C)
```

This creates evaluator recursion, so evaluator authority must be declared:

```trace
Evaluator(E).authority_status ∈ {ABSENT, CLAIMED, CAPTURED, PROVISIONAL, LEGITIMATE}
```

---

## 6. L4 — TRACE transition graph

TRACE should be represented as a typed labelled directed multigraph, not as a single moral scalar.

```trace
G_TRACE := (N, E, τ)
```

Nodes:

```trace
N :=
  States
  ∪ Actors
  ∪ Claims
  ∪ Clocks
  ∪ ProtectedScopes
  ∪ EvidenceObjects
  ∪ Actions
  ∪ Harms
  ∪ ReviewBodies
  ∪ RepairPaths
```

Edges:

```trace
E :=
  causes
  ∪ authorises
  ∪ contests
  ∪ pauses
  ∪ hardens
  ∪ repairs
  ∪ escalates
  ∪ captures
  ∪ substitutes
  ∪ burdens
  ∪ benefits
```

Edge typing:

```trace
τ : E → EdgeType
```

Current v0.11 invariants live here:

```trace
mode ⟂ authority_status ⟂ bind_status
PROVISIONAL ≠ LEGITIMATE
PROVISIONAL_ACTION ≠ DECIDED_TRAGIC
POTENTIAL_BIND ≠ STRUCTURED_TRAGIC_BIND
TransitionClaim required for state movement
```

---

## 7. L5 — Clock / correction graph

Time is not an annotation. It changes the graph.

```trace
Clock c := {
  trigger,
  affected_scope,
  controller,
  action_window,
  hardening_time,
  review_time,
  evidence_decay_time
}
```

Correction condition:

```trace
T_detect + T_route + T_correct < T_irreversible
```

Clock substitution pattern:

```trace
ClockSubstitution := c_A pauses c_B
```

Support candidate:

```trace
ClockSubstitutionClaim required iff:
  one_clock_is_used_to_pause_or_delay_another_clock
  ∨ one_clock_is_used_to_override_review_clock
  ∨ actor_benefits_from_clock_substitution
  ∨ affected_scope_claims_delay_harm_from_clock_substitution
  ∨ evidence_decay_or_repair_delay_is_material
```

Graph pattern:

```trace
Actor A controls c_A
∧ c_A pauses c_B
∧ affected_scope(c_B) bears delay_harm
∧ A benefits_or_avoids_burden
→ clock_laundering_risk
```

---

## 8. L6 — Protected scope / future-space

The object protected by TRACE is not only current welfare. It is future-space under uncertainty.

```trace
F_l(t) := possible_future_set_available_to protected_scope l at time t
```

Harm:

```trace
H_l(a,t) := ΔF_l(t | action a)
```

Material harm includes:

```trace
material_harm :=
  future_space_collapse
  ∨ agency_loss
  ∨ safety_loss
  ∨ truth_access_loss
  ∨ relation_loss
  ∨ repair_path_loss
  ∨ irreversible_burden_shift
```

Protected lower scopes cannot be silently netted away by whole-system viability.

```trace
whole_system_benefit ≠ automatic_permission_to_collapse F_l
```

Open wound:

```trace
protected_scope_membership := unresolved_foundational_boundary
```

Temporary operating discipline:

```trace
under_uncertainty:
  provisional_inclusion_better_than_silent_exclusion
  ∧ scope_status_must_be_marked
  ∧ exclusion_must_be_claimed_and_contestable
```

---

## 9. L7 — Human moral compass

The human moral compass is not replaced by TRACE. TRACE exists to protect it from laundering, panic, opacity, and false closure.

```trace
human_moral_compass :=
  harm_aversion
  + truth_respect
  + protected_scope_recognition
  + responsibility_under_uncertainty
  + repair_obligation
  + refusal_of_laundering
  + future_space_protection
  + humility_before_contested_cases
```

Human compass lines:

```trace
do_not_hide_harm
do_not_call_dirty_action_clean
do_not_use_uncertainty_as_permission
do_not_use_procedure_as_theatre
do_not_erase_affected_scopes
do_not_delay_repair_until_harm_hardens
preserve_truth_so_future_correction_remains_possible
```

TRACE can discipline the compass. It cannot replace it.

```trace
TRACE_supports(J)
TRACE_does_not_substitute_for(J)
```

---

## 10. L8 — Action and responsibility

Every decision under uncertainty is a transition.

```trace
action a : world_state_t → world_state_{t+1}
```

Missing information changes the action's status. It does not erase responsibility.

```trace
missing_information
→ provisionality
  + uncertainty_record
  + review_debt
  + loss_accounting
  + contest_edge

missing_information
↛ permission_not_to_decide
```

Action route:

```trace
J under uncertainty
→ choose a
→ record Claim/TransitionClaim
→ preserve correction path
→ review before hardening where possible
→ keep loss ledger open
```

---

## 11. Translation validity

A layer translation is valid only if it preserves contestability and does not smuggle authority.

```trace
valid_translation(L_i → L_{i+1}) iff:
  preserves_traceability
  ∧ exposes_uncertainty
  ∧ names_source
  ∧ preserves_contest_edge
  ∧ does_not_hide_affected_scope
  ∧ does_not_upgrade_authority_status_silently
```

Invalid translations:

```trace
latent_pattern → moral_truth
prose_fluency → evidence
symbolic_form → mechanism
Claim_schema → legitimacy
review_clock → actual_correction
AI_agreement → validation
human_intuition → public_proof
```

---

## 12. Drift paths

```trace
drift_paths :=
  latent_resonance_to_false_truth
  + symbol_elegance_to_fake_mechanism
  + claim_schema_to_fake_legitimacy
  + clock_index_to_paperwork_theatre
  + case_study_to_fake_validation
  + AI_review_to_external_authority_laundering
  + human_compass_to_private_revelation
```

Anti-drift test for every new symbol:

```trace
every_new_symbol_must_answer:
  what_does_it_distinguish?
  what_laundering_path_does_it_block?
  what_real_decision_changes?
  what_evidence_could_falsify_it?
  what_human_burden_does_it_protect?
```

If it cannot answer these, it remains sandbox language.

---

## 13. Current packet assessment

Strongest current region:

```trace
L2_semantic_statement
→ L3_typed_claim
→ L4_transition_graph
→ L5_clock_correction_graph
```

Weak edges:

```trace
L0/L1 → L3 := AI_output_to_claim_discipline_incomplete
L6/L7 → L8 := human_compass_to_action_discipline_incomplete
```

Immediate discipline:

```trace
no_more_symbol_expansion_without_layer_location
```

Every future packet element must state:

```trace
layer_location
input_type
output_type
failure_mode
anti_laundering_function
```

---

## 14. Compression

```trace
TRACE_AI_to_Human_Compass_Stack_v0_1 :=
  latent_space
  → token_surface
  → semantic_statement
  → typed_claim
  → transition_graph
  → clock_correction_graph
  → protected_scope_future_space
  → human_moral_compass
  → responsible_action
```

Governing rule:

```trace
no_layer_may_pretend_to_be_the_layer_above_it
```

Operational rule:

```trace
AI_output_is_safe_only_when:
  translated_into_typed_claims
  ∧ made_contestable
  ∧ uncertainty_exposed
  ∧ authority_not_silently_upgraded
  ∧ human_judgment_not_replaced
```

Status:

```trace
boundary_note := active_candidate
kernel_patch := no
review_needed := yes
```
