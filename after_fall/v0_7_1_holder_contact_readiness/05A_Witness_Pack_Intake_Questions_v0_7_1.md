# Witness Pack Intake Questions v0.7.1

Status: holder-contact readiness patch. Candidate only. Not canon, validation, proof, permission, clearance, compliance, legal advice, safety guarantee, or release.

## 0. Use

This is the plain-English intake path before the fillable template.

The affected person should not have to understand YAML, TRACE, ME, or carrier language to start.

```trace
intake_mode := self_filled | intermediary_assisted | holder_completed | unsafe_to_fill
```

If the person is at risk, prefer `intermediary_assisted` or pause.

## 1. Safety first

Before recording details, ask:

```text
Could writing this down make you or someone else easier to identify, punish, evict, dismiss, expose, or target?
```

If yes:

```trace
INTAKE_PAUSED_FOR_SAFETY
```

Continue only with a safe intermediary or with a public summary that excludes identifying details.

## 2. What happened?

Plain questions:

```text
What happened?
When did you first notice it?
Who or what is affected?
Who or what seems responsible, if known?
What changed after this happened?
What got worse, harder, more expensive, less safe, or less reachable?
What is still unknown?
```

Maps to:

```text
core_claim
public_summary
uncertainty_notes
```

## 3. What should stay private?

Ask:

```text
What details should not be public?
Names?
Addresses?
Flat numbers?
Children's details?
Medical details?
Private messages?
Photos?
Exact dates?
Location clues?
```

Maps to:

```text
unsafe_details_excluded
unsafe_details_to_keep_sealed
```

## 4. Who was counted, and who was ignored?

Ask in plain English:

```text
Whose situation was counted by the actor?
Whose situation was ignored or treated as less important?
What did the actor measure?
What did the actor ignore?
Who benefits from measuring it that way?
```

Maps to:

```text
D_plain_language
mu_plain_language
```

## 5. What evidence exists?

Ask:

```text
What records, photos, messages, documents, notes, or witness accounts exist?
Where are they now?
Who can access them?
Could sharing them identify anyone?
Do any files contain hidden metadata?
Have copies been made?
```

Do not ask the person to prove everything. The first task is to list what exists and what is sensitive.

Maps to:

```text
evidence_items
metadata_redaction_check
chain_of_custody
```

## 6. What was asked?

Ask:

```text
Who was asked to help, repair, explain, review, or respond?
How were they contacted?
Did they require an official route?
Could the affected person actually use that route?
What response came back?
Was there silence?
What deadline passed?
```

Maps to:

```text
asks_and_refusals
```

## 7. Is there retaliation risk?

Ask:

```text
Could making this record lead to eviction, job loss, worse treatment, access denial, account restriction, threats, or other pressure?
Has anything changed since the complaint or record began?
Who might retaliate?
What would make contact safer?
```

Maps to:

```text
retaliation_protocol
parallel_retaliation_log
```

If risk is high and there is no safer route:

```trace
WITNESS_RISK_UNCARRIED
+ INTAKE_PAUSED_FOR_SAFETY
```

## 8. What clocks are running?

Ask:

```text
What gets worse if nothing happens soon?
What evidence might disappear?
What opportunity might close?
What harm might become impossible to repair?
Who controls the deadlines?
Who benefits from delay?
```

Maps to:

```text
clocks
slow_hardening_risk
```

## 9. Who could hold the record?

Ask:

```text
Is there anyone outside the actor who could safely hold a copy, timestamp, advise, or refuse custody?
Could an advice worker, solicitor, renters' group, union, journalist, archive, trusted intermediary, or technical holder help?
Would using that holder create risk?
```

Maps to:

```text
custody_plan
holder_record
```

If no holder exists:

```trace
CUSTODY_MASS_ABSENT
```

## 10. Who is carrying the burden now?

Ask:

```text
Who is paying in time, money, health, fear, care work, legal work, proof labour, adaptation, or lost opportunity?
What would it take for that burden to move away from the affected person or group?
```

Maps to:

```text
residue_and_burden
```

## 11. What should happen next?

Ask:

```text
Should the pack stay private?
Should a safe public summary be drafted?
Should a holder be contacted?
Should more evidence be preserved?
Should the process pause because risk is too high?
```

Maps to:

```text
completion_status
next_action
enforcement_state
```

## 12. Minimum intake output

A valid first intake may be incomplete.

Minimum safe output:

```text
public summary or sealed-only reason
risk level
known unsafe details
evidence inventory without overexposure
asks/refusals summary
clock concern
custody status
next action or pause reason
```

End.
