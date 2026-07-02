# v0.7.1 Holder Contact Readiness Review

Date: 2026-07-02

Reviewer: GPT-5.5 Thinking, internal project assistant.

Status: internal readiness review only. Not external validation, proof, permission, clearance, compliance, legal review, holder acceptance, safety result, field test, or release.

## VERDICT

```text
READY_FOR_LIMITED_HOLDER_CONTACT
```

## Scope of verdict

This verdict is narrow.

It means the package is ready for limited contact with a possible holder **about the method and simulated materials**, not for sending real sensitive evidence, not for publishing a pack, and not for claiming that the framework is validated.

Allowed contact:

```text
one-to-one or very small number of contacts
method-review only
simulated or redacted example only
no real identifying material
no claim of endorsement
holder may refuse without pressure
response recorded using the holder acceptance/refusal form
```

Forbidden contact:

```text
public call-out
mass outreach
sending real sealed evidence
asking for legal advice through the package
asking anyone to endorse TRACE/ME
claiming holder acceptance before it exists
```

## Why the verdict changed from v0.7

v0.7 returned `PATCH_BEFORE_CONTACT` because it was intelligible but not holder-shaped.

v0.7.1 added the missing holder-contact layer:

```text
plain-English intake questions
metadata handling checklist
holder contact brief
holder acceptance/refusal form
fresh safety review rule before any public release
```

These additions make the first contact question concrete enough:

```text
Could you receive or advise on a sealed record like this, under what conditions, and what would make it unsafe or impossible?
```

## Readiness checks

### 1. Cold reader comprehension

Pass for limited contact.

The holder brief explains that the recipient is not being asked to endorse TRACE, Mechanical Ethics, or an ethical framework. It asks a practical custody question instead.

### 2. Holder role clarity

Pass.

The holder brief distinguishes possible holder actions:

```text
receive sealed copy
timestamp receipt
hold public summary only
hold hashes or index only
advise unsafe
refer to better holder
refuse with reasons
state conditions for future custody
```

This is now adequate for first contact.

### 3. Refusal pathway

Pass.

The acceptance/refusal form makes refusal useful rather than treating it as failure. It captures response type, what can be received, conditions, refusal reasons, safety concerns, better holder route, and follow-up.

### 4. Safety-first intake

Pass with caution.

The intake questions begin with the correct first question:

```text
Could writing this down make you or someone else easier to identify, punish, evict, dismiss, expose, or target?
```

They also permit `INTAKE_PAUSED_FOR_SAFETY`. This prevents the pack from pretending that completion is always desirable.

### 5. Metadata risk

Pass for limited contact.

The metadata checklist now names concrete file types and risks, gives a basic workflow, and defaults to safe summary only if metadata is unresolved.

### 6. Public release risk

Pass.

The fresh safety review rule is clear: no public release of a pack, summary, aggregate, excerpt, evidence item, screenshot, document, image, or holder response without fresh review.

## Remaining blockers before real case use

These are not blockers for limited holder contact, but they remain blockers before real case use.

```text
No jurisdiction-specific legal review.
No real holder has accepted custody.
No real user has attempted the intake.
No metadata workflow has been tested on real files.
No small-N anonymity threshold has been field-tested.
No storage or retention implementation exists.
No consent workflow has been tested.
```

## Safety constraints for first contact

First contact must use a low-risk contact packet:

```text
10_HOLDER_CONTACT_BRIEF_v0_7_1.md
11_HOLDER_ACCEPTANCE_REFUSAL_FORM_v0_7_1.md
05A_Witness_Pack_Intake_Questions_v0_7_1.md
07A_Metadata_Handling_Checklist_v0_7_1.md
12_PUBLIC_RELEASE_FRESH_SAFETY_REVIEW_RULE_v0_7_1.md
06_Tenant_Mould_Completed_Example.md as simulated example only
```

Do not send:

```text
real names
real addresses
real photos
medical notes
children's details
private messages
unredacted metadata
full TRACE/ME archive stack
```

## Suggested first holder types

Choose one, not many:

```text
renters' group / tenants' union
advice worker or housing support route
public-interest archive / documentation group
journalist only if safety and publication boundary are very clear
```

Avoid first contact with a formal legal route if the ask could be mistaken as a legal case request. If using legal-support contact, frame it as method/custody review, not legal advice.

## First-contact script boundary

The first contact should say:

```text
I am testing whether a witness-pack template is understandable and safe enough to be considered by possible holders. I am not sending real evidence and I am not asking for endorsement. Could you say whether an organisation like yours could ever receive, refuse, or advise on a sealed record like this, and what conditions or risks would matter?
```

## Minimum record of the contact

Every contact attempt should record:

```text
who was contacted or role-only description
what was sent
whether real evidence was excluded
response type
conditions or refusal reasons
safety concerns
permission to record response
next action
```

## Final gate state

```trace
v0_7_1_gate := READY_FOR_LIMITED_HOLDER_CONTACT
contact_scope := method_review_only
real_evidence := forbidden
holder_acceptance := not_yet_shown
field_test := not_yet_started
```

End.
