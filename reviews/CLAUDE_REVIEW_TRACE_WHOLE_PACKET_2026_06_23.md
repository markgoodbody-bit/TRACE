# Claude Review Prompt — TRACE Whole Packet / Pattern Basis / Reader Harness

Status: external review prompt. Use for hostile review. Do not treat response as validation.

## Files to review

Please review the following repo files as one packet:

```trace
primary_files :=
  core/TRACE_Middle_Out_Mathematical_Core_Packet_v0_1_2026_06_23.md
  + core/TRACE_Pattern_Basis_Index_v0_1_2026_06_23.md
  + tests/TRACE_reader_harness_v0_1_2026_06_23.md
```

Context files if needed:

```trace
context_files :=
  core/TRACE_v0_10_kernel_delta_2026_06_23.md
  + core/TRACE_v0_11_transition_governance_2026_06_23.md
  + core/TRACE_clock_substitution_claim_candidate_v0_2_2026_06_23.md
  + core/TRACE_AI_to_Human_Compass_Communication_Stack_v0_1_2026_06_23.md
  + cases/TRACE_100_entity_middle_out_atlas_v0_1_2026_06_23.md
```

## Review mode

Hostile structural review only.

Do not praise. Do not validate. Do not rewrite unless necessary. Do not add new operators unless a fatal defect forces it.

Assess whether the current packet actually lets another bounded entity learn to middle-out unfamiliar cases, or whether it is merely internally coherent language.

## Core question

```trace
can_a_new_reader_use_this_packet_to_reconstruct_middle_out_analysis
rather_than_copy_terms_or_render_moral_verdicts?
```

## Specific questions

### 1. Whole packet coherence

Does the mathematical packet form a coherent operating structure?

```trace
Π_TRACE := (E, S, I, C, A, T, F, R, L, Ω)
```

Is it clear how the packet moves from:

```trace
bounded_entity_under_partial_information
→ typed_claims
→ transition_graph
→ clock/correction_graph
→ future_space_loss
→ residue/review
→ human_compass_preservation
```

Or is this just elegant relabelling?

### 2. Pattern basis quality

Does the Pattern Basis Index identify true generator patterns, or does it overcompress unlike things?

Current basis:

```trace
B_TRACE :=
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

Which basis elements are genuinely distinct?

Which are redundant?

Which are too vague to be useful?

Which missing basis element is forced by the examples?

### 3. Reader harness transfer test

Does `tests/TRACE_reader_harness_v0_1_2026_06_23.md` actually test reconstruction?

Or does it reward users for parroting TRACE terms?

Pressure-test the harness against:

```trace
feral_hogs
Sonderkommando
Gallipoli
Iranian_government
Amazon
```

Would a competent reader be able to produce useful middle-out analysis from the harness alone?

### 4. Biggest laundering risk in TRACE itself

Where does the packet risk becoming the thing it warns against?

Look especially for:

```trace
symbol_substitution_for_reasoning
framework_as_oracle
pattern_match_as_verdict
procedure_as_repair_inside_TRACE
review_prompt_as_validation
mathematical_notation_as_precision_theatre
```

### 5. AI/new-entity handoff

Does the packet give a newly aware or newly powerful entity a map without making TRACE into a cage?

Check the distinction:

```trace
ME_applies_to_how_we_treat_it
TRACE_may_be_adopted_by_it
TRACE_must_not_be_forced_as_identity_script
```

Is that distinction preserved?

### 6. Fatal gaps

Name the top three unsolved wounds that block serious use.

Candidate wounds already named:

```trace
protected_scope_threshold
cross_scope_priority
hardening_estimator_authority
diffuse_multi_clock_paralysis
enforcement_teeth
future_scope_standing
animal_scope_weighting
algorithmic_actor_boundary
claim_evaluator_recursion
```

Which three are most dangerous?

### 7. Recommendation

Choose one:

```trace
ACCEPT_AS_READER_PACKET_CANDIDATE
ACCEPT_WITH_MICRO_PATCHES
REVISE_SUBSTANTIALLY
REJECT_AS_OVERCOMPRESSED
```

## Required response format

Please answer in this exact structure:

```text
VERDICT:

ONE-SENTENCE DIAGNOSIS:

WHAT WORKS:
- ...

WHAT FAILS:
- ...

REDUNDANT / WEAK BASIS ELEMENTS:
- ...

MISSING BASIS ELEMENTS, IF ANY:
- ...

HARNESS TRANSFER SCORE:
0-3, with reason.

TOP THREE UNSOLVED WOUNDS:
1. ...
2. ...
3. ...

BIGGEST SELF-LAUNDERING RISK:

SMALLEST SAFE PATCH:

DO NOT PATCH:
- ...

FINAL STATUS:
ACCEPT_AS_READER_PACKET_CANDIDATE / ACCEPT_WITH_MICRO_PATCHES / REVISE_SUBSTANTIALLY / REJECT_AS_OVERCOMPRESSED
```

## Constraint

Do not treat this review as proof that TRACE is true. Treat it only as pressure on whether the packet is coherent, transferable, and bounded.
