# Holder Contact Brief v0.7.1

Status: holder-contact readiness patch. Candidate only. Not canon, validation, proof, permission, clearance, compliance, legal advice, field test, holder acceptance, or release.

## 1. Purpose of this brief

This brief is for a possible holder: a person or organisation that might receive, preserve, timestamp, review, advise on, or refuse custody of a Witness Pack.

You are not being asked to endorse TRACE, Mechanical Ethics, or any ethical framework.

You are being asked a practical custody question:

```text
Could you receive or advise on a sealed record like this, under what conditions, and what would make it unsafe or impossible?
```

## 2. What a Witness Pack is

A Witness Pack is a structured record of a contested situation.

It may include:

```text
public summary
sealed evidence list
asks and refusals
risk and retaliation notes
custody plan
clocks and urgency notes
burden and residue notes
```

It does not prove the claim. It does not create safety. It does not force action. It does not replace legal advice or professional judgment.

## 3. What a holder might do

A holder might do one or more of these:

```text
receive a sealed copy
timestamp receipt
hold a public summary but not sealed evidence
hold only hashes or an index
advise that the pack is unsafe
refer to a better holder
refuse custody with reasons
state conditions for possible future custody
```

A refusal with reasons is useful. It tells us what the carrier lacks.

## 4. What a holder is not being asked to do

You are not being asked to:

```text
validate the framework
certify the claim
accept legal responsibility without agreement
publish sensitive evidence
act as investigator by default
promise safety
promise enforcement
keep records without retention terms
```

## 5. Conditions we need you to evaluate

Please consider:

```text
Could you hold a public summary only?
Could you hold sealed evidence?
Could you hold hashes or timestamps only?
What would you need before accepting anything?
What should never be sent to you?
What would create risk for the affected person?
What would create risk for your organisation?
What format would be easiest to receive?
What would make you refuse?
Who would be a better holder?
```

## 6. Safety defaults

The default is:

```trace
no_public_release_without_fresh_safety_review
```

Sensitive material should remain sealed unless there is a clear safe route.

Examples of sealed-by-default material:

```text
names
addresses
flat numbers
children's details
medical material
private messages
original photos with unchecked metadata
precise dates or location clues where identifying
```

## 7. Possible responses

Please return one of:

```text
HOLDER_ACCEPTS_WITH_CONDITIONS
HOLDER_REFUSES_WITH_REASONS
HOLDER_REQUIRES_DIFFERENT_FORMAT
HOLDER_CAN_HOLD_PUBLIC_SUMMARY_ONLY
HOLDER_CAN_HOLD_HASH_OR_INDEX_ONLY
HOLDER_UNREACHABLE_OR_NO_CAPACITY
SAFETY_RISK_TOO_HIGH
BETTER_HOLDER_SUGGESTED
```

## 8. Minimal response form

```yaml
holder_response:
  organisation_or_role:
  response_type:
  can_receive_public_summary: yes | no | maybe
  can_receive_sealed_evidence: yes | no | maybe
  can_receive_hash_or_index_only: yes | no | maybe
  conditions_for_acceptance:
  reasons_for_refusal_or_limits:
  safety_concerns:
  format_preferences:
  retention_or_deletion_requirements:
  better_holder_suggestion:
  permission_to_record_this_response: yes | no | anonymised_only
```

## 9. Boundary sentence

A Witness Pack is a record. It is not justice or safety by itself.

End.
