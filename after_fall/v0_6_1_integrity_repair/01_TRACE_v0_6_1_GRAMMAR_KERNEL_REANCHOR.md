# TRACE v0.6.1 - Grammar Kernel Re-anchor

Status: CANDIDATE integrity repair over TRACE v0.6 Operational Carrier Candidate. Not canon, validation, proof, permission, clearance, or release.

## Purpose

v0.6 correctly built carrier interface machinery, but the document risked becoming mostly carrier and not enough TRACE. A cold reader must be able to reconstruct what TRACE sees before reading what gives that reading material weight.

This layer re-anchors the grammar. If this kernel were absent, the document should be called `TRACE Carrier Interface`, not `TRACE After-Fall Reader`.

## 1. TRACE core function

TRACE is a language for representing transitions under uncertainty so that contraction, designation, correction, residue, and answerability are harder to hide.

```trace
TRACE_role :=
  make_transition_field_inspectable
  + expose_designation_and_measure_ports
  + track_correction_clocks
  + record_residue
  + refuse_permission_outputs
```

TRACE does not decide moral status, legitimacy, dignity, acceptable sacrifice, justified coercion, or final action.

## 2. Six primitives

```trace
primitives := state + transition + time + coupling + aperture + entity
```

Entity individuation is designation-adjacent. Boundary drawing is not neutral.

## 3. Two explicit ports

```trace
ports := D_designation + mu_measure
```

`D/designation` asks who or what counts, including where boundaries are drawn.

`mu/measure` asks how futures, losses, baselines, weights, and comparisons are measured.

TRACE must expose D and mu. It must not silently fill them.

```trace
silent_D_fill := out_of_grammar
silent_mu_fill := out_of_grammar
```

## 4. Contraction and harm reading

```trace
C := descriptive_contraction
D := designation
H := harm_reading_after_designation
H := C read_through D and mu
```

A contraction is not automatically harm. A contraction becomes a harm reading only through designation and measure.

## 5. Future-space

Future-space means more than option count. It includes reachability, usable information, correction, relation, orientation, and viable becoming.

## 6. Two clock inequalities

Loss-side clock:

```trace
T_det(h,l) + T_route(h,c,l) + T_corr(h,c,l) < T_irr(h,l | c)
```

Opportunity-side clock:

```trace
T_access(o,l) + T_uptake(o,l) + T_integrate(o,l) < T_opp(o,l)
```

## 7. Answerability

```trace
Ans(A <- B) iff
  exists fb(B -> A)
  + fb is routable by B
  + fb is not practically refusable by A
  + fb can alter A's future dispositions or constraints
```

## 8. Consequence gap

```trace
gap(A,B) := influence(A -> B) > 0 and feedback(B -> A) approximately 0
```

The common pathology is not no feedback. It is loop-swap: the system responds to the wrong field.

## 9. Residue law

```trace
repair_moves_forward_not_back
recorded_residue != repaired_residue
residue_recorded != residue_borne
```

A ledger can remember a debt. It cannot by itself bear it.

## 10. UNKNOWN rule

If a signal from an affected scope is underdetermined, TRACE must output UNKNOWN, not a single confident story.

```trace
if aperture_data_underdetermines_reading(signal_from_scope):
  output UNKNOWN
  + candidate_readings_marked_as_constructions
  + what_would_disambiguate
  + route_to_ask_party_where_possible
```

## 11. Failure surfaces

```trace
forbidden_moves :=
  SILENT_D_FILL
  + SILENT_mu_FILL
  + CONFIDENT_STORY_FROM_AMBIGUOUS_SIGNAL
  + CLEAN_H_WITHOUT_SHOWN_D
  + PORT_DISCLOSURE_AS_LEGITIMACY
  + UNKNOWN_AS_CLEARANCE
  + APERTURE_ALIBI
  + SILENT_SCOPE_TRIAGE
  + CLOCK_SATISFIED_AS_LICENCE
  + RECORDED_AS_REPAIRED
  + TRACE_COMPLIANT_AS_PERMISSION
```

## 12. Carrier handoff

The grammar can show where routing should exist. It cannot supply the enforcer.

```trace
reading_without_carrier_mass := CLAIM_PACKET_ONLY
ENFORCEMENT_ABSENT_NO_DISCHARGE := red_flag_not_release
```

The v0.6 operational carrier interface remains active after this kernel. The kernel tells the reader what is being carried; the carrier layer tells the reader whether that reading has material weight.
