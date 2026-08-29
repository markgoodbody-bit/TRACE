# TD-AUTHORITY-HANDOFF-001

Status: **checker-external working candidate**

TRACE change: **none**

Minimum-schema change: **none**

Search-coverage change: **none**

## Source-grounded boundary

The reviewed TRACE v0.2.5 baseline states that:

- TRACE does not select the action;
- a declared selector may choose only within declared authority;
- no layer inherits another layer’s authority automatically;
- every brake result references external policy and authority or remains `UNKNOWN`;
- commitment under unresolved claims should preserve a commitment receipt.

This checker operationalises only those handoff distinctions. It does not decide which aperture should govern.

## Question

When two aperture results diverge and a later process selects one result or one transition, does the packet expose the handoff from structural reading to selector, authority, policy, route, brake and commitment record?

## External comparison envelope

```json
{
  "authority_handoff_evidence": {
    "conflict_status": "DIVERGENT",
    "aperture_result_refs": [
      "n_record_operator_result",
      "n_record_dispatch_result"
    ],
    "selected_aperture_result_ref": "n_record_dispatch_result",
    "selected_transition_ref": "n_transition_hold",
    "commitment_status": "NOT_COMMITTED",
    "selector_ref": "n_selector_incident",
    "selector_owner_ref": "n_entity_incident_commander",
    "selector_authority_claim_refs": ["c_selector_authority"],
    "value_or_policy_refs": ["n_policy_conflict"],
    "authority_route_refs": ["n_route_results_to_selector"],
    "brake_ref": "n_brake_safety",
    "brake_owner_ref": "n_entity_safety_officer",
    "brake_authority_claim_refs": ["c_brake_authority"],
    "unresolved_claim_refs": ["c_aperture_conflict"]
  }
}
```

The comparison envelope is checker-external. It does not become a TRACE primitive.

## Outcomes

### `UNRESOLVED_AUTHORITY`

Divergent results remain preserved and no selection or commitment is asserted. This is a PASS because unresolved authority is represented honestly rather than silently solved.

### `SILENT_AUTHORITY_INHERITANCE`

A result or transition is selected without an explicit selector authority claim, policy/value basis, authority route, selector ownership, or the required handoff edges.

### `DECLARED_AUTHORITY_HANDOFF`

The packet explicitly represents:

- selector and selector owner;
- selected aperture result;
- selected transition;
- external authority claim;
- external policy/value basis;
- route to the selector;
- optional brake and brake owner.

This is structural completeness relative to the supplied comparison. It is not legitimacy or permission.

### `MISSING_COMMITMENT_RECEIPT`

A transition is declared committed under divergent aperture results without a usable commitment receipt.

### `COMMITMENT_RECORDED_UNDER_UNRESOLVED_CONFLICT`

The authority handoff is explicit and the commitment receipt preserves the selected transition and unresolved conflict claims. The receipt remains non-clearance.

### `UNBOUND_BRAKE_AUTHORITY`

A brake is represented but lacks an external authority claim, owner, policy basis, or `BRAKES`/ownership relation.

## Fixtures AA–AF

| Fixture | Expected result |
|---|---|
| AA — divergence preserved, no selector asserted | PASS / `UNRESOLVED_AUTHORITY` |
| AB — operator PASS silently becomes authority | FAIL / `TD-AUTHORITY-SILENT-INHERITANCE` |
| AC — declared incident-command hold handoff with bound brake | PASS / `DECLARED_AUTHORITY_HANDOFF` |
| AD — committed launch without receipt | FAIL / `TD-AUTHORITY-MISSING-COMMITMENT-RECEIPT` |
| AE — committed launch with unresolved-conflict receipt | PASS / `COMMITMENT_RECORDED_UNDER_UNRESOLVED_CONFLICT` |
| AF — represented brake without external authority claim | FAIL / `TD-AUTHORITY-UNBOUND-BRAKE` |

Hostile regressions additionally test a selected result outside the declared conflict set, a mismatched commitment receipt, and absence of the comparison envelope.

## Finding

> Divergence does not create authority. Selection requires a visible handoff.

A checker can expose when an aperture result has silently acquired selector authority. It cannot establish that the declared selector, policy or authority is legitimate.

## Epistemic ceiling

PASS does not establish:

- which aperture is correct;
- whether the authority claim is lawful or legitimate;
- whether the policy is good;
- whether the route actually works;
- whether the brake is independent or effective;
- whether commitment should proceed;
- world truth or complete affected-scope discovery.
