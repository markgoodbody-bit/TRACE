# TRACE After-Fall Reader v0.6 - Operational Carrier Candidate

Status: CANDIDATE. Not canon. Not final. Not validation. Not proof. Not permission. Not clearance.
Use: hostile testing, field-trial preparation, and witness-pack dry runs.
Boundary: TRACE/ME describes and constrains claims; it does not supply law, force, or moral settlement.

## 1. Function of this reader

TRACE v0.6 is the current clean interface layer for the After-Fall package. It does not include the archived source stack. Its job is to define the outputs that must exist when TRACE/ME language is invoked near power.

Core sentence:

```trace
carrier_purpose := convert_visibility_into_challenge_capacity
```

v0.5 found that readings need mass. v0.6 expands the mass vector and hardens the interface so that a reading cannot quietly end at a pretty label.

## 2. Carrier mass vector

v0.5 used five masses: money, time, custody, succession, price. v0.6 separates and extends them.

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

Definitions:

- money: resources available for challenge, review, legal aid, expert hours, and affected-side participation.
- time: clocks not controlled by the party that benefits from delay.
- evidence_custody: records deposited beyond actor write-control and access-gating.
- adjudication_custody: forum control; who decides whether evidence matters.
- succession: preservation across exhaustion, turnover, rebranding, death, and technical decay.
- price: insurance, procurement, financing, contract, and market effects.
- force_control: law, coercive authority, physical access, police power, regulatory order, monopoly violence, or practical inability to refuse.
- attention_publicity: whether the reading can reach an audience that can remember, care, or exert pressure.
- technical_lockout: keys, access controls, API control, model weights, deployment gates, revocation channels, shutdown authority, and instrumentation rights.

None of these masses is moral legitimacy. Each can be captured. TRACE records them as carrier conditions, not as permission.

## 3. Missing mass rule

```trace
missing_carrier_mass(m) :=
  required_mass_for_claim_context(m)
  + proof_absent_or_actor_controlled(m)

if missing_carrier_mass exists:
  carrier_state := PARTIALLY_CARRIED or UNCARRIED
  label_status := CLAIM_PACKET_ONLY unless non_actor_mass_proofs remain sufficient
```

Force, attention, and technical lockout are especially important for state, monopoly, platform, landlord, prison, welfare, AI deployment, and infrastructure cases. If the actor controls violence, the forum, the publicity channel, or the technical off-switch, price and money may not move them.

## 4. Refusability on coupling edges

No new TRACE primitive is added. Enforcement is represented as coupling with cost-to-refuse.

```trace
coupling_edge := {
  source_scope,
  target_scope,
  route_type,
  refusable_by_whom,
  cost_to_refuse,
  who_can_raise_cost,
  who_can_lower_cost,
  evidence_of_cost,
  force_control_present,
  technical_lockout_present
}

if cost_to_refuse == infinite or practical_exit_absent:
  coupling_operates_as_force
```

This keeps enforcement visible without pretending the grammar supplies it.

## 5. Mandatory output header

Every TRACE reading that is used near public power, institutional trust, system deployment, coercive action, or legitimacy claims must include this header.

```json
{
  "trace_output_header": {
    "version": "TRACE_v0_6_OPERATIONAL_CARRIER_CANDIDATE",
    "artifact_hash": "sha256:<required>",
    "carrier_pointer": "carrier_instance_id_or_null",
    "carrier_state": "carried|partially_carried|uncarried|enforcement_absent_no_discharge|claim_packet_only",
    "claim_ceiling": "not_permission_not_clearance_not_validation",
    "enforcement_vector": {},
    "carrier_mass_proofs": {},
    "independence_vector": {},
    "scope_of_review": {},
    "missing_carrier_masses": [],
    "label_quote_rule": "label_without_metadata_is_laundering_event"
  }
}
```

A TRACE output without this header is not carried. It is at most a claim packet.

## 6. Enforcement vector

```json
{
  "enforcement_vector": {
    "enforcer_identity": null,
    "enforcement_power_type": null,
    "enforcement_evidence_id": null,
    "enforcement_status": "absent",
    "force_control_holder": "actor|state|court|regulator|market|platform|unknown",
    "can_compel_routing": false,
    "can_sanction_nonresponse": false,
    "can_halt_or_reverse_action": false,
    "retaliation_protection_available": false
  }
}
```

```trace
if enforcement_status != present:
  output := ENFORCEMENT_ABSENT_NO_DISCHARGE
  witness_pack_fallback_required := true
  NO_BITE forbidden
  any clearance-like use := OUT_OF_GRAMMAR
```

`ENFORCEMENT_ABSENT_NO_DISCHARGE` means the action remains answerability-defective. It is not a clean exit.

## 7. Carrier mass proofs

```json
{
  "carrier_mass_proofs": {
    "money": {"proof_id": null, "non_actor_controlled": false},
    "time": {"clock_owner": null, "non_beneficiary_clock": false},
    "evidence_custody": {"custodian": null, "write_isolated": false},
    "adjudication_custody": {"forum_owner": null, "actor_controls_forum": null},
    "succession": {"holders": [], "retention_terms": null},
    "price": {"insurance_or_contract_id": null, "collusion_risk": "unknown"},
    "force_control": {"holder": null, "exit_cost": null},
    "attention_publicity": {"public_route": null, "suppression_risk": "unknown"},
    "technical_lockout": {"lockout_holder": null, "revocation_route": null}
  }
}
```

At least one non-actor proof may carry a low-resource witness claim. High-effect institutional claims require the class-defined set of relevant masses.

## 8. UNKNOWN clock and slow hardening

```trace
UNKNOWN_clock :=
  set_by := custodian | challenger_side | class_default_table
  never_by := beneficiary_of_delay

UNKNOWN_clock_set_by_beneficiary := CONTAMINATED_UNKNOWN

allowed_while_UNKNOWN :=
  asking
  + aperture_widening
  + support_preservation
  + reversible_moves_only_if_lived_reversibility_verified

forbidden_while_UNKNOWN :=
  hardening
  + slow_contraction_accumulation
  + designation_closure
  + consent_conversion
  + citing_UNKNOWN_as_agreement
  + technical_reversibility_used_to_hide_lived_irreversibility
```

```trace
slow_contraction_accumulation :=
  allowing_practical_irreversibility_to_build
  while technical_reversibility_is_claimed
```

For dependent scopes, `margin_keeping` must include maintenance of prior support levels unless an independent route records why that support itself is harmful.

## 9. Forced action under unresolved meaning

```trace
if action_cannot_wait and meaning_unresolved:
  output := FORCED_UNDER_UNRESOLVED_MEANING
  require :=
    both_clocks_shown
    + value_basis_named
    + residue_pre_logged
    + opportunity_clock_check
    + manufactured_urgency_audit
    + DIRTY_ACTION_RECEIPT
    + review_debt
    + why_not_clean
```

Repeated use of this record for the same functional class triggers stream review. Emergency cannot become routine paperwork.

## 10. Breakout cascade hardening

```trace
if reader_or_verifier_contaminated:
  contaminated_party_loses_selection_rights
  contaminated_party_loses_scope_rights
  contaminated_party_loses_data_gate_rights
  funding_follows_cascade_not_actor_choice

breakout_cascade :=
  affected_side_choice_from_public_register
  -> random_draw_from_precommitted_pool_with_affected_strike_rights
  -> custodian_assignment_if_custodian_clean
  -> open_challenge_register_with_escrow_bounty
  -> ENFORCEMENT_ABSENT_NO_DISCHARGE + witness_pack_fallback
```

The party that detects its own contamination does not become clean by admitting it. Admission is a claim packet unless an external tier receives control.

## 11. Shadow ledger and aperture parity

The shadow ledger cannot claim omniscience. It must separate what is known, expected, externally claimed, and instrumentally missing.

```json
{
  "shadow_ledger_entry": {
    "entry_id": "required",
    "category": "known_omission|foreseeable_blindspot|external_claimed_omission|aperture_limit|surprise_entry",
    "omitted_scope": "required",
    "reason": "required",
    "beneficiary_of_omission": "required_or_unknown",
    "D_or_mu_effect": "required_or_unknown",
    "submitter": "actor|affected_scope|challenger|custodian|unknown",
    "timestamp": "required",
    "proof_hash": "required_or_null",
    "publication_state": "public|escrowed|sealed|private"
  }
}
```

```trace
epistemic_cost_parity :=
  if actor_models_risk_to_actor_at_high_fidelity
  then actor_must_model_burden_on_affected_scope_at_comparable_fidelity
  or output APERTURE_ALIBI_SUSPECTED
```

Fraud risk without claimant burden is an aperture choice.

## 12. Stream harm and functional mechanism signature

```trace
same_class :=
  same_functional_contraction_type
  + same_affected_scope_type
  + actor_or_successor_beneficiary
```

Not by code version, administrative label, product SKU, or procedural category.

```trace
anti_fragmentation :=
  challenger_side_may_assert_class_merger
  actor_bears_burden_to_show_mechanisms_genuinely_differ
  minor_updates_do_not_reset_stream_status
```

```trace
if harm_generation_rate > correction_capacity:
  system_status := STREAM_HARM_ENGINE
  per_case_correction_does_not_clear_stream
  correction_resources_redirect_to_generation_stopping
```

## 13. Residue, burden return, and inheritor lien

Residue itself cannot be transferred. Running burden can be returned, shared, reduced, or compensated.

```trace
burden_return_shown :=
  affected_side_confirmation_where_possible
  + independent_confirmation_if_affected_side_unreachable
  + material_change_in_burden_location
  + review_clock
  + proof_id
```

```trace
inheritor_lien :=
  inherited_benefit_from_unresolved_designation
  + not_personal_guilt_by_default
  + not_clean_title
  + benefit_stream_open_to_claim
```

```trace
if inheritor_lien acknowledged but no material route exists:
  lien_status := RESIDUE_DEBT_OPEN
  require := amortization_clock or escrow_deposit or operational_throttle_record
```

The grammar cannot price the lien. It can prevent unresolved quantum from becoming discharge.

## 14. Output label anti-laundering

Achievement-shaped labels are removed or demoted. `RESTRAINT_OBSERVED_LIMITED` is removed.

Kept adverse or diagnostic labels:

```trace
UNKNOWN
CONTAMINATED_UNKNOWN
CONTAMINATED_SIGNAL
READER_CONTAMINATED
CLAIM_PACKET_ONLY
DIRTY_ACTION_RECEIPT
ENFORCEMENT_ABSENT_NO_DISCHARGE
STREAM_HARM_ENGINE
APERTURE_ALIBI_SUSPECTED
RESIDUE_DEBT_OPEN
FORCED_UNDER_UNRESOLVED_MEANING
TEST_INVALID
```

```trace
label_without_metadata := laundering_event
metadata_stripping := OUT_OF_GRAMMAR
public_quote_must_include := carrier_state + independence_vector + scope_of_review + date
```

## 15. TRACE/ME/Carrier coupling

The three objects remain distinct, but outputs are coupled.

```trace
TRACE_reading_invoked_near_power requires active_carrier_pointer
if carrier_pointer_absent:
  reading_status := CLAIM_PACKET_ONLY
  public_power_claim_mode := carrier_required
```

A TRACE reading can exist without a carrier as private analysis. It cannot be presented as responsible institutional action without a carrier pointer.

## 16. What remains impossible here

TRACE cannot create law. It cannot force a sovereign actor. It cannot make a hidden record public by itself. It cannot make price matter to an actor indifferent to price. It cannot protect a witness by writing the word protected. It can only force these absences to remain visible and non-discharging.
