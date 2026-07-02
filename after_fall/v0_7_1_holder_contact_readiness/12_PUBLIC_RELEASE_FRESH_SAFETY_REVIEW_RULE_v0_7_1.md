# Public Release Fresh Safety Review Rule v0.7.1

Status: holder-contact readiness patch. Candidate only. Not legal advice, validation, proof, permission, clearance, compliance, safety guarantee, field test, or release.

## 1. Rule

No public release of a Witness Pack, public summary, aggregate, excerpt, evidence item, screenshot, document, image, or holder response should occur without a fresh safety review.

```trace
no_public_release_without_fresh_safety_review
```

## 2. Why this rule exists

Risk changes over time.

A detail that was safe yesterday may become identifying after:

```text
new complaint
new retaliation
new media attention
new legal process
new actor knowledge
new aggregation
new housing or workplace change
new document leak
```

## 3. Safety review questions

Before public release, ask:

```text
Could this identify the affected person or group?
Could the actor infer the source using side knowledge?
Does this include names, addresses, flat numbers, children, medical material, private messages, exact dates, or metadata?
Has metadata been checked?
Could this trigger retaliation?
Has the affected side or safe intermediary approved the public version?
Is a safer summary possible?
Is publication necessary now?
What is the least revealing version that preserves the record?
```

## 4. Required field

Add to relevant witness-pack files:

```yaml
public_release_safety_review:
  status: required | completed | not_safe | unknown
  reviewed_by: affected_scope | trusted_intermediary | holder | other | none
  reviewed_at:
  unsafe_details_removed:
  metadata_checked: true | false | unknown
  small_N_identification_checked: true | false | unknown
  retaliation_risk_checked: true | false | unknown
  release_decision: do_not_release | safe_summary_only | release_limited | release_to_holder_only | unknown
```

## 5. Default outputs

If not reviewed:

```trace
PUBLIC_RELEASE_NOT_REVIEWED
+ SAFE_SUMMARY_ONLY_OR_SEALED
```

If metadata is unchecked:

```trace
METADATA_RISK_UNRESOLVED
+ ORIGINAL_FILES_NOT_PUBLIC
```

If small-N risk is unresolved:

```trace
AGGREGATION_UNSAFE_SMALL_N
+ NO_PUBLIC_AGGREGATE
```

If retaliation risk is high and no mitigation exists:

```trace
WITNESS_RISK_UNCARRIED
+ NO_PUBLIC_RELEASE
```

## 6. Boundary

This rule does not guarantee safety. It prevents public release from being treated as an automatic escalation step.

End.
