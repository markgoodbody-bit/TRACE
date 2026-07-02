# Witness Pack User Guide v0.7

Status: cold-reader pre-field candidate. Not canon, validation, proof, permission, clearance, compliance, or release.

## 1. What a Witness Pack is

A Witness Pack is a structured record of a contested situation.

It is for cases where something important may be happening, evidence may disappear, asks or refusals matter, and there may not be a clean route to force a response now.

A Witness Pack does not make justice happen. It makes disappearance harder.

## 2. When to use it

Use the template only where it is safe enough to do so.

Possible uses:

```text
housing disrepair or mould
workplace retaliation or ignored safety risk
platform or automated-system harm
institutional refusal or silence
denied route to complaint or review
repeat harm where each case is treated separately
```

Do not use it personally if filling it would make you easier to identify, punish, evict, dismiss, expose, or target. Use a safer intermediary or do not fill it yet.

## 3. The first decision: public, sealed, or mixed

A Witness Pack has two possible layers:

```text
public summary: safe, minimal description that can be shared
sealed evidence: sensitive material held privately or by a trusted holder
```

Do not put names, addresses, flat numbers, children's details, medical details, phone numbers, private messages, or photo metadata into a public summary unless there is a specific safe reason.

## 4. What to fill first

Fill in this order:

1. Core claim: what happened, who is affected, what changed.
2. Risk: could this make someone easier to punish or expose?
3. Evidence list: what exists, where it is, and whether it is sensitive.
4. Asks/refusals: what was requested, from whom, and what happened.
5. Clocks: what gets worse or impossible if delayed?
6. Custody: who could hold the record safely, if anyone?
7. Burden: who is paying the cost now?
8. Completion status: what is missing and what happens next?

## 5. Evidence handling

Describe evidence carefully. Do not overstate what it proves.

Examples:

```text
Photo of mould = observation.
Message asking for repair = document.
Tenant says symptoms worsened = testimony or claim.
Medical note says respiratory symptoms exist = document.
Mould caused the symptoms = inference unless professionally supported.
```

Use this distinction:

```text
observation | claim | inference | document | testimony | derived_analysis
```

## 6. Metadata and redaction

Photos and files can contain hidden metadata. That metadata may identify where, when, or by whom the file was made.

Before wider sharing, check whether metadata needs removing.

Use:

```text
metadata_redaction_check := passed | failed | not_checked | not_applicable
```

If metadata is not checked, do not treat the item as safe for public release.

## 7. Asks, refusals, and silence

Record asks in simple form:

```text
what was asked
who was asked
when they were asked
what route they required
what route was actually available
what response came back
what deadline passed
```

Silence after a reasonable route and clock is not consent. Record it as silence.

## 8. Retaliation and safety

Retaliation may be direct or indirect.

Examples:

```text
eviction threat
rent pressure
repair refusal
workplace pressure
account restriction
complaint route suddenly blocked
hostile message after complaint
```

If risk is high and no mitigation exists, output:

```trace
WITNESS_RISK_UNCARRIED
```

## 9. Custody and holders

A holder is someone who can receive, preserve, timestamp, advise on, or refuse custody of the record.

Possible holder types:

```text
advice worker
solicitor or legal support route
union or renters' group
journalist
public archive
trusted intermediary
distributed storage route
```

Use at least two different holder types where safe and possible. Do not rely on one convenient service or one person if the record is sensitive.

If nobody can safely hold it, say so. That is not a reason to pretend custody exists.

## 10. Aggregation without doxxing

Multiple packs can show a pattern, but aggregation can expose people.

A landlord, employer, platform, or institution may already know enough to infer who complained.

Before aggregation, ask:

```text
Would grouping these records identify anyone?
Who has side knowledge?
Is the group large enough?
Can a trusted intermediary aggregate without revealing identities?
```

If aggregation itself creates danger, keep it sealed.

## 11. Enforcement absence

If no route can force a response, output:

```trace
ENFORCEMENT_ABSENT_NO_DISCHARGE
```

This does not mean the actor is clean. It means the record has not found a force route.

## 12. Completion statuses

Use honest statuses:

```text
draft
sealed
deposited
public_summary
reviewed
abandoned_unknown
unsafe_to_use
```

Do not mark the pack complete merely because fields are filled. A pack can be structurally filled but not safely carried.

End.
