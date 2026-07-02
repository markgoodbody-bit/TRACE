# Answerability Carrier Clean Spec v0.7

Status: cold-reader pre-field candidate. Not canon, validation, proof, permission, clearance, compliance, or release.

## 1. Purpose

The Answerability Carrier is the operational layer that asks whether a TRACE/ME reading has any material route to challenge, custody, memory, or consequence.

```trace
carrier_purpose := convert_visibility_into_challenge_capacity
```

A carried reading is not a cleared reading. It is only a reading with some material support behind it.

## 2. When the carrier is triggered

The carrier is triggered when an actor with power invokes TRACE, ME, ethics language, responsibility language, or witness-pack language as public trust material.

Examples:

```text
We used the framework, so this process is responsible.
We recorded residue, so the harm was handled.
We applied the carrier, so answerability was present.
```

These are claim packets until carrier conditions are shown.

## 3. Carrier state

```json
{
  "carrier_state": "uncarried|partially_carried|carried_limited|enforcement_absent_no_discharge|claim_packet_only",
  "carrier_state_reason": "required",
  "not_clearance": true,
  "not_compliance": true,
  "not_permission": true
}
```

`carried_limited` must name the scope, time, masses present, masses missing, and independence limits. It is never global.

## 4. Mass vector

```trace
carrier_mass_vector :=
  money
  + time
  + evidence_custody
  + adjudication_custody
  + succession
  + price
  + force_control
  + attention_publicity
  + technical_lockout
```

Plain meanings:

```text
money: resources for challenge and participation
time: clocks not owned by the delay beneficiary
evidence custody: records beyond actor write-control
adjudication custody: forum and decision control
succession: survival across exhaustion, turnover, and delay
price: insurance, procurement, finance, contract, reputation
force/control: legal, physical, institutional, or practical power
attention/publicity: whether the record can reach memory or pressure
technical lockout: keys, deployment gates, revocation routes, or shutdown controls
```

Each mass can be captured. Mass is not legitimacy.

## 5. Proof discipline

For each claimed mass, require:

```text
holder
actor-control status
evidence id
expiry
contest route
failure mode
```

Rules:

```trace
actor_claimed_mass_without_non_actor_proof := CLAIM_PACKET_ONLY
private_mass_proof_for_public_claim := CLAIM_PACKET_ONLY
metadata_stripping := CONTAMINATED_SIGNAL
```

## 6. Minimum viable carrier: Witness Pack

The Witness Pack is the minimum carrier under enforcement absence.

It preserves claims, records asks and refusals, separates public summary from sealed material, protects identity where possible, and creates future challenge material.

It does not make justice happen.

Minimum fields:

```text
core claim
plain-language designation and measure dispute
evidence items
retaliation protocol
asks/refusals/silence log
custody plan
holder independence notes
aggregation and fake-pack countermeasure
clocks
residue and burden
escalation or enforcement absence state
completion status
```

## 7. Retaliation rule

A high-risk pack without mitigation is not safely carried.

```trace
high_retaliation_risk + no_mitigation := WITNESS_RISK_UNCARRIED
```

Mitigation may include sealed identity, trusted intermediary, legal/support bridge, public-summary-only mode, or delayed release.

## 8. Holder rule

A holder is a person or organisation that can receive, preserve, timestamp, advise on, or refuse custody of a record.

Examples:

```text
advocate
solicitor or advice worker
union or renters' group
journalist
public archive
trusted intermediary
distributed storage route
```

A holder must be described by:

```text
holder type
independence vector
correlation cluster
access conditions
retention terms
tamper-evidence method
safety assessment
compelled-disclosure or exposure risk where known
```

## 9. Non-monopoly clause

No single carrier service, registry, custodian, template provider, or witness-pack platform may become the only valid route.

```trace
carrier_non_monopoly_rule :=
  no_single_carrier_service_required
  + no_single_custodian_as_the_route
  + no_single_registry_global_authority
  + no_proprietary_format_as_exclusive_validity
```

If the package depends on one provider and no alternative route exists:

```trace
CARRIER_MONOCULTURE_RISK
```

## 10. UNKNOWN and slow hardening

UNKNOWN cannot be used as actor-controlled delay.

```trace
UNKNOWN_clock_set_by_beneficiary := CONTAMINATED_UNKNOWN
```

While UNKNOWN remains unresolved, technical reversibility is not enough. If lived future-space is shrinking, the action may be hardening even if the file can be reopened later.

```trace
technical_reversibility != lived_reversibility
slow_contraction_accumulation := forbidden_under_UNKNOWN
```

## 11. Enforcement absence

TRACE/ME cannot supply the enforcer.

If no enforcer exists:

```trace
ENFORCEMENT_ABSENT_NO_DISCHARGE
witness_pack_fallback_required_where_safe
NO_BITE_forbidden
```

This is a red flag, not a clean exit.

## 12. Anti-branding

Forbidden public uses:

```text
carrier-certified
TRACE-compliant
ME-approved
answerability-certified
ethically cleared
responsibility verified
```

Acceptable phrasing is narrower:

```text
A witness pack was drafted.
A record was deposited with named limits.
A claim packet exists but is not independently carried.
Carrier masses present/missing are listed.
```

End.
