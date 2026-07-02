# Safety and Risk Notes v0.7

Status: cold-reader pre-field candidate. Not canon, validation, proof, permission, clearance, compliance, or release.

## 1. Core warning

A witness pack can help preserve a record. It can also create risk.

The first safety question is not "is the record complete?" The first question is:

```text
Could this make someone easier to identify, punish, pressure, evict, dismiss, expose, or target?
```

If yes, do not publish. Use sealed or intermediary routes only, or pause.

## 2. Public summary vs sealed evidence

Keep these separate.

Public summary may include:

```text
general issue
general actor type
general affected scope
safe description of what changed
what route is missing
```

Sealed evidence may include:

```text
names
addresses
flat numbers
medical details
children's details
private messages
photos
metadata
precise dates if identifying
```

Do not move sealed details into public text just to make the pack look stronger.

## 3. Metadata risk

Files can reveal hidden information.

Examples:

```text
photo location
device details
time and date
author name
file path
editing history
```

If metadata has not been checked, mark:

```trace
metadata_redaction_check := not_checked
public_release := unsafe
```

## 4. Small-N identification risk

Aggregation can reveal people even when names are removed.

If three tenants in a small building file packs, the landlord may know exactly who they are.

Before aggregation, ask:

```text
What does the actor already know?
Would grouping records identify anyone?
Is N large enough?
Can an intermediary aggregate safely?
```

If not:

```trace
AGGREGATION_UNSAFE_SMALL_N
```

## 5. Retaliation risk

Retaliation may be direct or indirect.

Examples:

```text
access denied
repair delayed
complaint route blocked
rent pressure
threats
disciplinary action
account restriction
hostile correspondence
```

A high-risk pack without mitigation is not carried safely.

```trace
high_retaliation_risk + no_mitigation := WITNESS_RISK_UNCARRIED
```

## 6. Holder risk

A holder can help. A holder can also become a target, leak point, subpoena point, bottleneck, or single point of failure.

Record for every holder:

```text
who selected them
who pays them
relationship to actor
what they can access
how long they keep it
what could force disclosure
what happens if they stop responding
```

If all custody goes through one route:

```trace
CARRIER_MONOCULTURE_RISK
```

## 7. No safety guarantee

Do not write:

```text
this pack makes the witness safe
this pack proves the claim
this pack forces response
this pack creates justice
```

Write instead:

```text
this pack preserves a structured record with named limits
```

## 8. No legal-status claim

This package does not decide legal rights, evidence admissibility, disclosure obligations, limitation periods, professional duties, privilege, or reporting duties.

If a legal route matters, the pack should say:

```trace
LEGAL_ROUTE_NEEDED_OR_UNKNOWN
```

not pretend the pack itself supplies that route.

## 9. If no route exists

If there is no safe holder, no safe publication route, and no reachable support route, the honest output is:

```trace
ENFORCEMENT_ABSENT_NO_DISCHARGE
+ CUSTODY_MASS_ABSENT
+ PUBLICITY_ROUTE_UNAVAILABLE_OR_UNSAFE
+ RESIDUE_DEBT_OPEN
```

That is not a failure of honesty. It is the point of the record.

End.
