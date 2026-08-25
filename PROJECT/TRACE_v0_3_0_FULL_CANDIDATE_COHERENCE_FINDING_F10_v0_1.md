# TRACE v0.3.0 full-candidate coherence finding F10

**Date:** 2026-08-25  
**Object attacked:** generated full working candidate after F09 / recursion closure  
**Surface:** packet / carrier survival of load-bearing limits  
**Status:** MATERIAL FINDING / WORKING / NON-CANON / UNVALIDATED

## Finding

F09 repaired recursive integration so qualifying child limits survive into parent `L` with target/scope/provenance association.

The canonical packet can represent limits: `LIMIT` is already a node type, the packet includes a `limits` object, node attributes are extensible, and the minimum validator permits additional properties under `limits`.

But the current semantic packet contract does not require a load-bearing item in `L` to survive serialization with the distinctions that made it load-bearing.

The canonical packet exemplar exposes only:

```yaml
limits:
  receiver_limits: []
  unavailable_evidence: []
  unresolved_claim_refs: []
  omitted_primitive_effects: []
```

and the operator ends with:

```text
emit_confidence_and_limits(R, L)
```

without a binding rule that preserves material limit kind, recursive target/scope, basis claim refs, relevant aperture/clock/route/handoff refs, and provenance through the canonical carrier.

A packet may therefore be structurally valid while collapsing materially different internal limit histories into the same generic limit summary.

## Counterexample pair

Hold the represented graph contribution and unresolved claim set fixed.

### Case A — access truncation on recursive target q

The child graph contributes a dependency. Its qualifying limit says source access for target `q` was unavailable, with the relevant aperture and source claim refs.

### Case B — budget exhaustion before refining recursive target q

The same represented dependency and unresolved claim refs remain, but refinement stopped because tracing budget was exhausted before the target could be investigated.

These histories imply different next correction routes. Case A calls for access/evidence routing; Case B calls for budget/priority/re-run handling.

A packet containing only the same generic `receiver_limits` text plus the same `unresolved_claim_refs` can erase that distinction while remaining schema-valid.

## Narrow diagnosis

This is a carrier/binding defect, not a representation-capacity defect.

```text
CAN_SERIALIZE_LIMIT_DETAIL != LIMIT_DETAIL_SURVIVED
LIMIT_VISIBLE_IN_ANALYSIS != LIMIT_CARRIED_IN_PACKET
UNRESOLVED_CLAIM_RECORDED != LIMIT_CAUSE_RECORDED
LIMIT_TEXT_PRESENT != LIMIT_PROVENANCE_PRESERVED
SCHEMA_VALID_LIMITS != SEMANTIC_LIMIT_SURVIVAL
INTERNAL_L_MERGED != CANONICAL_PACKET_L_CARRIED
```

No new primitive or semantic root is required. Existing `LIMIT`, `CLAIM`, `APERTURE`, `CLOCK`, `ROUTE`, target-set and provenance machinery is sufficient.

This is also a direct worked instance of the existing donor distinction:

```text
VISIBILITY != CARRYING
```

## Repair contract

For every load-bearing limit emitted into the canonical packet:

1. preserve a stable limit identity/reference;
2. preserve limit kind/reason rather than generic text alone;
3. preserve the represented target/scope to which the limit applies;
4. preserve basis claim refs and relevant aperture/clock/route/handoff refs where available;
5. preserve recursive parent/child provenance where the limit arrived through refinement;
6. ensure derived confidence/coverage/window/transition views can reference the carried limit;
7. prohibit packet emission from silently collapsing materially distinct limits merely because their prose summary or unresolved claim set is identical;
8. keep the minimum-schema shape unchanged and add no canonical primitive.

A bounded serialization profile may use existing `LIMIT` nodes plus packet `limits.limit_refs`; the minimum validator already permits the optional packet field and `LIMIT` is already in the controlled node vocabulary.

## Claim boundary

This is a source-level carrier-survival finding against the current full working candidate. It does not establish runtime loss in every implementation, world invalidity, release failure, a new primitive, a new semantic root, validation, or canon change. Released v0.2.7 remains untouched.
