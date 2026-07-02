# v0.7 Internal Cold Reader Review

Date: 2026-07-02

Reviewer: GPT-5.5 Thinking, internal project assistant.

Status: internal cold-review only. Not external validation, proof, permission, clearance, legal review, holder acceptance, safety result, or release.

## VERDICT

```text
PATCH_BEFORE_CONTACT
```

## Short reason

v0.7 is now intelligible as a cold-reader package. It has a clear entry path, a readable TRACE kernel, a human-facing ME booklet, a carrier spec, a user guide, a fillable template, a completed example, safety notes, and a reviewer prompt.

However, it is still not ready to show to a real holder. The package is understandable to a motivated reviewer, but too dense and too internally styled for a solicitor, advice worker, tenants' group, journalist, councillor, or archive contact. The next patch should not add theory. It should create a holder-facing contact brief, simplify the witness-pack intake path, and harden safety language around publication, metadata, and small-N exposure.

## TOP 5 BLOCKERS

### 1. No holder-facing contact brief

The package explains the system, but it does not yet give a potential holder a two-page object answering:

```text
What are you being asked to hold?
What would you not be responsible for?
What conditions would you need?
What are the risks?
How can you refuse usefully?
```

Without that, a real holder will have to infer their role from the full package. That is too much friction.

Required patch:

```text
10_HOLDER_CONTACT_BRIEF_v0_7_1.md
```

### 2. The fillable template is still too technical for the affected person

The template is clearer than v0.6, but a frightened tenant or worker should not be expected to fill YAML fields. It is still more like an implementation schema than an intake form.

Required patch:

```text
05A_Witness_Pack_Intake_Questions_v0_7_1.md
```

This should be plain questions in human order, then mapped to fields afterward.

### 3. Public release language remains too dangerous

The package correctly separates public summary from sealed evidence and warns about unsafe publication. But terms such as delayed public release, public summary release, and escalation to publicity still need a stronger rule:

```trace
no_public_release_without_fresh_safety_review
```

For retaliation-heavy situations, publicity can be a weapon against the witness.

### 4. Metadata guidance names the risk but does not give an operational method

The safety notes correctly say metadata can reveal location, device, time, author, file path, and editing history. But the package does not give a safe, practical workflow for a non-specialist.

Required patch:

```text
metadata_handling := do_not_upload_originals + copy_to_safe_folder + strip_or_convert + hash_redacted_copy + keep_original_sealed_if_needed
```

Do not rely on the user knowing what metadata is or how to strip it.

### 5. Holder refusal is not yet structured enough

The package says refusal is useful, but does not provide a holder-refusal form. A refusal from a solicitor, archive, journalist, or group is valuable only if it records why:

```text
capacity issue
legal risk
confidentiality risk
format problem
safety concern
no mandate
needs different holder type
```

Required patch:

```text
11_HOLDER_ACCEPTANCE_REFUSAL_FORM_v0_7_1.md
```

## SAFETY DEFECTS

### Retaliation risk

The package correctly states that a user should not use the template personally if it could make them easier to identify, punish, evict, dismiss, expose, or target. It also identifies high-risk retaliation and `WITNESS_RISK_UNCARRIED`.

Remaining defect: it still needs a stronger stop-rule:

```trace
if retaliation_risk == high and no trusted_intermediary:
  do_not_complete_identifying_fields
  output := INTAKE_PAUSED_FOR_SAFETY
```

### Metadata leakage

The package identifies metadata risk but lacks an operational checklist. Add a concrete workflow and a warning that screenshots, forwarded messages, PDFs, and cloud documents can also leak identity.

### Small-N deanonymisation

The package correctly flags small-N aggregation risk, including the fact that an actor may infer complainants from side knowledge. This is strong. Remaining defect: no threshold rule exists. It should not set a universal N, but it should require a case-specific anonymity floor:

```trace
anonymity_floor := N_required_given_actor_side_knowledge
```

### Holder capture

The holder fields are good: relationship, payment, access, retention, disclosure risk. Remaining defect: the pack needs to tell a non-specialist how to spot holder capture in plain English.

### False sense of safety

The repeated boundary language is good, but the package should include one blunt line in the intake form:

```text
Do not use this pack if using it would make you easier to punish and you do not have a safer route.
```

## CLARITY DEFECTS

### Too many files for first contact

The full package is useful for review, but not for first contact. A holder-facing version should have only:

```text
1. Holder Contact Brief
2. Witness Pack User Guide
3. Fillable Template or Intake Questions
4. Completed Example
5. Safety Notes
```

TRACE and ME can be linked as background, not foreground.

### TRACE is readable but still slightly abstract

The TRACE kernel now works as a clean summary. It is short enough and explains the basics. For non-technical reviewers, the code blocks may still feel like jargon. Add one paragraph at the top saying:

```text
You can ignore the code-like blocks on first read; they are compact labels, not software you need to run.
```

### The template mixes user, intermediary, and holder tasks

Some fields are for the affected person. Some are for an intermediary. Some are for a holder. The template should mark:

```text
filled_by_affected_person
filled_by_intermediary
filled_by_holder
filled_after_review
```

## MISSING FIELDS OR GUIDANCE

Add:

```text
intake_mode: self_filled | intermediary_assisted | holder_completed | unsafe_to_fill
public_release_safety_review: required | not_required | unknown
metadata_workflow_status: not_started | redacted_copy_created | original_sealed | unsafe_to_share
holder_refusal_reason
holder_conditions_for_acceptance
anonymity_floor_reasoning
who_should_not_receive_this_pack
what_to_do_if_actor_requests_the_pack
```

## WHAT TO REMOVE OR DEMOTE

Demote TRACE/ME prominence in any holder-contact packet. They are necessary background, but a potential holder should first see the practical object.

Demote any automatic or delayed publication language unless it is explicitly subject to fresh safety review.

Do not remove the carrier concepts. Move them behind the practical witness-pack route.

## MINIMUM PATCH BEFORE CONTACT

Create v0.7.1 with five small additions/edits:

```text
10_HOLDER_CONTACT_BRIEF_v0_7_1.md
11_HOLDER_ACCEPTANCE_REFUSAL_FORM_v0_7_1.md
05A_Witness_Pack_Intake_Questions_v0_7_1.md
07A_Metadata_Handling_Checklist_v0_7_1.md
Patch 04/05/06/07 to require fresh safety review before any public release.
```

No new theory. No new mass vector. No new philosophical layer.

## WHAT CAN REMAIN OPEN

These can remain open before limited holder contact:

```text
exact legal status
exact evidence admissibility
which organisations would accept custody
real-world holder capacity
field usability
jurisdiction-specific disclosure law
```

The package does not need to solve those before contact. It needs to make them visible enough that a holder can respond usefully.

## Bottom line

v0.7 is no longer unintelligible. It is not unsafe in the sense of making overclaims as a document. But it is still too heavy and not yet holder-shaped.

Next state:

```trace
v0_7_1 := holder_contact_readiness_patch
```

End.
