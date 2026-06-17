# TRACE Spine Wording Drift Note v0.1

Date: 2026-06-17
Status: control note / drift flag / not validation / not proof / not active spine / not Kernel v0.3

## Plain purpose

This note records a live wording drift in the current TRACE active spine.

It does not resolve the drift.

It exists so the ambiguity cannot silently change branch activation.

```trace
spine_wording_drift_note :=
  record_conflict
  + block_silent_harmonisation
  + preserve_source_wording
  + require_explicit_decision
  - active_spine_edit
  - validation_claim
```

## The conflict

Most current public/control surfaces use:

```trace
exit_when_correction_channel_is_harm_carrier
```

The canonical Operator Registry v0.2 public definition uses:

```trace
exit_when_correction_channel_is_predatory
```

This matters because the Operator Registry is a high-authority memory file, while the current README / public surface / handoff surface use the broader phrase.

## Why it matters

`harm_carrier` is broader.

A correction channel can carry harm through:

- predation,
- capture,
- negligence,
- dependency,
- design failure,
- delay,
- retaliation risk,
- procedural burden,
- or structural conflict of interest.

`predatory` is narrower and more intention-like.

It suggests that the system or channel is actively hunting, exploiting, or targeting the subject.

```trace
predatory_system ⊂ harm_carrier_system
```

If both phrases are used silently, the Exit Route branch may activate differently depending on which file a reader treats as controlling.

That is unacceptable drift.

## Temporary rule

Until Framework / Mark explicitly decides the canonical wording:

```trace
temporary_rule :=
  do_not_harmonise_silently
  + quote_source_wording_used
  + mark_uncertainty_if_branch_activation_depends_on_distinction
```

When applying TRACE, use the exact wording from the file being applied.

If a case would fail under `predatory` but trigger under `harm_carrier`, record the ambiguity.

## Candidate resolution options

This note does not choose among these.

### Option A — Harmonise to `harm_carrier`

Use `exit_when_correction_channel_is_harm_carrier` everywhere.

Reason:

- broader;
- captures systems that carry harm without requiring predatory intent;
- better fits the existing Diagnostic Kernel v0.2 wording around official channel as harm carrier.

Risk:

- may over-trigger Exit Route branch if too broad;
- may label ordinary institutional weakness as system danger.

### Option B — Keep `predatory` as subset

Use `harm_carrier` as the broad branch and `predatory_system` as a narrower high-risk subtype.

Reason:

- preserves both meanings;
- allows stronger caution where exposure to the channel itself increases danger;
- keeps predation language from doing too much work.

Risk:

- adds vocabulary complexity;
- may invite premature subtype expansion.

### Option C — Split branch thresholds

Define separate activation thresholds:

```trace
harm_carrier_channel :=
  official_route_carries_or_preserves_harm

predatory_system :=
  official_route_targets_or_exploits_subject
```

Reason:

- clearer discrimination;
- supports different escalation levels.

Risk:

- may become Kernel v0.3 by stealth;
- requires comparator pressure and branch tests before promotion.

## Current provisional preference

No binding decision is made here.

However, the safest likely future direction is:

```trace
harm_carrier := broad_branch_language
predatory := high_risk_subtype
```

This should not be treated as canonical until deliberately patched through affected files.

## Demoters / removal conditions

Remove this note if:

```trace
remove_if :=
  canonical_wording_decided
  + affected_files_updated
  + read_order_or_control_index_updated
```

Demote this note if:

```trace
demote_if :=
  deliberate_scope_distinction_already_documented_elsewhere
  OR apparent_conflict_is_redundant
```

Keep this note if:

```trace
keep_if :=
  ambiguity_remains_live
  OR branch_activation_changes_by_wording
```

## Must not claim

```trace
must_not_claim :=
  this_note_resolves_spine
  OR this_note_creates_Kernel_v0_3
  OR predatory_equals_harm_carrier
  OR harm_carrier_implies_bad_faith
  OR Claude_or_Framework_agreement_validates_TRACE
```

## Final line

The conflict is now visible.

Do not resolve it silently.

End.
