# TRACE v0.6.1 Grammar Kernel Reanchor

Status: integrity repair over TRACE v0.6 operational carrier source. Candidate only. Not canon, validation, proof, permission, clearance, or release.

## 0. Why this exists

The v0.6 TRACE source became a clean carrier-interface layer. That made the package operationally sharper but created a naming risk: a cold reader could hold a document titled TRACE and receive carrier machinery without enough TRACE grammar to know what the carrier is carrying.

This kernel repairs that failure.

```trace
TRACE_v0_6_1_rule :=
  carrier_interface_must_remain_attached_to_TRACE_grammar
```

## 1. Minimal TRACE object

TRACE is a typed description language for transitions under uncertainty. It does not grant permission. It does not decide moral settlement. It makes visible where power, designation, measurement, harm, correction, residue, and answerability are being claimed or hidden.

```trace
TRACE_role :=
  make_transition_field_inspectable
  + expose_D_and_mu_ports
  + track_clocks
  + preserve_residue
  + refuse_permission_output
```

## 2. Six primitives

```trace
primitives :=
  state
  + transition
  + time
  + coupling
  + aperture
  + entity
```

Working meanings:

```trace
state := condition_of_a_scope_at_a_time
transition := movement_from_one_state_to_another
time := ordering_and_clocks_under_which_transition_hardens_or_remains_correctable
coupling := influence_feedback_route_or_dependency_between_scopes
aperture := what_a_scope_or_system_can_register
entity := boundary-bearing pattern treated as a scope for the reading
```

## 3. Ports

```trace
ports := D_designation + mu_measure
```

```trace
D_designation := who_or_what_counts + boundary_drawing + protected_scope_selection
mu_measure := how_loss_future_baseline_weight_and_repair_are_compared
```

Rules:

```trace
TRACE_must_not_fill_D_or_mu_silently
shown_D != accepted_D
shown_mu != accepted_mu
port_disclosure != port_legitimacy
```

Entity individuation remains designation-adjacent:

```trace
entity_boundary_choice := D_act
```

## 4. Contraction and harm reading

```trace
C := descriptive_contraction
D := designation
H := harm_reading_after_designation
```

TRACE can describe contraction. It cannot by itself decide final moral status.

```trace
H = C read_through D and evaluated_under mu
```

Human translation:

```text
Seeing that a future-space narrowed is not the same as deciding who counts. But deciding who counts is already power.
```

## 5. Future-space and contraction

```trace
future_space := reachable_options + usable_information + viable_routes + correction_possibility
contraction := reduction_of_future_space_under_transition
```

Future-space is not raw option count. A nominal option that cannot be reached, understood, afforded, or safely used is not equal to a usable route.

## 6. Clock inequalities

Loss-side clock:

```trace
T_det(h,l) + T_route(h,c,l) + T_corr(h,c,l) < T_irr(h,l | c)
```

Plain English:

```text
help must land before the loss sets.
```

Opportunity-side clock:

```trace
T_access(o,l) + T_uptake(o,l) + T_integrate(o,l) < T_opp(o,l)
```

Plain English:

```text
the door must be reached before it shuts.
```

If correction or opportunity routes arrive after hardening, record residue. Do not call delayed correction full repair.

## 7. Answerability and consequence gap

```trace
Ans(A <- B) iff exists fb(B -> A), non_refusable_by_A, routable_by_B
```

```trace
gap(A,B) := infl(A -> B) > 0 and fb(B -> A) approximately_absent
```

Answerability is not a mood or label. It is a route by which affected outcome can alter future disposition, decision, or constraint.

## 8. Residue law

```trace
repair_moves_forward_not_back
kappa_after_tau != identity
recorded_residue != repaired_residue
```

Plain English:

```text
repair moves forward, never back.
```

Residue remains what correction cannot return: time, trust, health, opportunity, standing, evidence, safety, orientation, relation.

## 9. UNKNOWN rule

```trace
if signal_from_scope_is_underdetermined:
  output := UNKNOWN
  candidate_readings := marked_as_constructions
  ask_or_route_to_scope_where_possible
  do_not_emit_confident_story
```

Forbidden:

```trace
CONFIDENT_STORY_FROM_AMBIGUOUS_SIGNAL
UNKNOWN_AS_CLEARANCE
UNKNOWN_USED_AS_ACTOR_TIMED_DELAY
```

In v0.6 operational carrier use, UNKNOWN also triggers carrier clock discipline.

## 10. Failure surfaces

TRACE must keep these visible:

```trace
failure_surfaces :=
  silent_D_fill
  + silent_mu_fill
  + aperture_alibi
  + silent_scope_triage
  + correction_theatre
  + residue_recorded_as_repaired
  + loop_swap
  + actor_self_application_as_clearance
  + label_laundering
  + enforcement_absent_as_discharge
```

## 11. Anti-permission boundary

Forbidden readings:

```trace
TRACE_says_this_is_allowed
TRACE_compliant
this_action_is_clean
NO_STRUCTURAL_OBJECTION_as_clearance
carrier_used_as_trust_credit_without_challenge_capacity
```

All TRACE outputs remain claim packets unless the relevant carrier metadata, independence, scope, evidence, and enforcement conditions are shown.

## 12. Interface back to v0.6 carrier

The v0.6 operational carrier interface attaches to this grammar. It does not replace it.

```trace
carrier_layer := material_challenge_capacity_interface
not := TRACE_grammar_substitute
```

If a future TRACE reader contains carrier machinery but not this grammar kernel or a stronger equivalent, mark:

```trace
TRACE_GRAMMAR_DETACHED_FROM_CARRIER_INTERFACE
```

End.
