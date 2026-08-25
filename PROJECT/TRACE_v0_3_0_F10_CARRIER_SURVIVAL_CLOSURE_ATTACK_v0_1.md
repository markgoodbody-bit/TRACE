# TRACE v0.3.0 F10 carrier-survival closure attack

**Date:** 2026-08-25  
**Object attacked:** regenerated full working candidate after F10 repair  
**Surface:** canonical packet / load-bearing limit carrier survival  
**Status:** CLEAR_WITH_RESIDUAL_LIMITS / WORKING / NON-CANON / UNVALIDATED

## Evidence boundary

The first one-shot F10 build remained RED and is preserved as GitHub Actions run `32874096683`.

Its exact failure was mechanical and fail-closed: `T_LIMIT_CARRIER_SURVIVAL` expected one canonical packet anchor and observed zero because the migration omitted the donor YAML indentation. The released-donor section manifest and version-only minimum schema had already passed before that failure. The gate was not weakened.

The canonical packet anchor was corrected exactly and the retry, GitHub Actions run `32875935798`, completed successfully. It produced commit:

```text
f317410f1b0f56beb023d972d321a9bb429615f0
```

The regenerated build report records:

```text
status: PASS
errors: []
donor_invariant_count: 60
donor_invariants_preserved_exact_in_order: true
minimum_schema_report_status: PASS
mutation_count: 39
supplemental_guard_count: 58
survival_required_count: 49
output_lines: 6539
output_bytes: 179731
output_sha256: 32409ee8d91e9c4bc67ecbb2359cc7d1c68249cab457511a50e586733ee7598a
```

This evidence establishes deterministic source assembly against the pinned donor and unchanged minimum-schema shape only.

## Repaired source contract under attack

The operator now performs:

```text
material_limit_refs <- serialize_load_bearing_limits_with_provenance(R, L)
bind_packet_limit_refs(R, material_limit_refs)
emit_confidence_and_limits(R, L, material_limit_refs)
```

The canonical packet exemplar exposes:

```yaml
limits:
  receiver_limits: []
  unavailable_evidence: []
  unresolved_claim_refs: []
  omitted_primitive_effects: []
  limit_refs: []
```

The checker-external binding rule requires a load-bearing limit to retain the distinctions whose loss could change a downstream claim, coverage/window/transition view, confidence statement or correction/repair route. Existing `LIMIT` node identity and attributes carry kind, target/scope, basis and available aperture/clock/route/handoff/recursive provenance. Materially distinct limits must not be deduplicated merely because prose or unresolved-claim sets match.

`limits.limit_refs` remains optional in the minimum schema. Optional minimum-schema shape does not make semantic carrier survival optional when a load-bearing limit exists.

## Bounded attack cases

### 1. Access truncation versus budget exhaustion with the same unresolved claim set

Hold represented graph contribution and unresolved claim refs fixed.

- Case A stops because source access is unavailable.
- Case B stops because tracing budget is exhausted before refinement.

**Attack:** can both collapse to the same generic limit summary while satisfying the F10 semantic contract?

**Result:** no. The load-bearing cause changes the next repair route. Distinct limit kind/provenance must survive under stable `LIMIT` identity and cannot be silently deduplicated.

**Disposition:** RESISTS.

### 2. Identical prose, different target or scope

Two limits use the same human-readable description but apply to different recursive targets or protected scopes.

**Attack:** can prose equality justify one carried limit?

**Result:** no. `target_refs` / `scope_refs` are load-bearing where the affected object changes downstream interpretation or repair. Stable identities remain distinct.

**Disposition:** RESISTS.

### 3. Recursive child limit merged into parent

A child refinement contributes graph structure and a qualifying access/budget/clock limit.

**Attack:** can the child graph survive while its qualifying limit loses recursive origin at packet emission?

**Result:** no under the combined F09+F10 contract. F09 merges child `L` with recursive provenance; F10 serializes load-bearing limits with provenance and permits `recursive_parent_target_ref` / `source_limit_refs` to carry that history.

**Disposition:** RESISTS.

### 4. Provenance field unavailable

A load-bearing limit is known to exist, but one requested provenance relation cannot be supported from available evidence.

**Attack:** must the serializer invent a reference to satisfy the profile?

**Result:** no. Missing or unsupported fields remain unresolved; provenance must not be fabricated merely to populate the carrier profile.

**Disposition:** RESISTS.

### 5. Non-load-bearing limit

An internal `L` item cannot change any downstream claim, coverage/window/transition view, confidence statement or repair route under the declared reading.

**Attack:** does F10 force every internal limit-like note into a canonical `LIMIT` node?

**Result:** no. The rule is explicitly scoped to load-bearing limits. F10 does not turn all diagnostic residue into mandatory canonical nodes.

**Disposition:** RESISTS / SCOPE BOUNDED.

### 6. Minimum-schema-valid packet with semantic binding missing

Construct a packet that passes the unchanged minimum schema but omits the load-bearing cause/provenance needed to distinguish two materially different limits. Whether `limit_refs` is absent or present is not by itself decisive; the attack is loss of the required semantic distinction and reference path.

**Attack:** does schema validity establish F10 carrier survival?

**Result:** no. The binding rule is checker-external by design.

```text
MINIMUM_SCHEMA_PASS != SEMANTIC_BINDING_PASS
SCHEMA_VALID_LIMITS != SEMANTIC_LIMIT_SURVIVAL
```

**Disposition:** RESISTS.

### 7. `limit_refs` present but referenced `LIMIT` lacks load-bearing distinction

A packet indexes a `LIMIT` node but the node contains only generic text while material kind/target/provenance has been erased.

**Attack:** does presence of the reference establish survival?

**Result:** no. Stable identity is necessary but not sufficient when the erased distinction changes downstream interpretation or repair route.

```text
LIMIT node exists != carried limit provenance complete
LIMIT_TEXT_PRESENT != LIMIT_PROVENANCE_PRESERVED
```

**Disposition:** RESISTS.

### 8. Same prose and same unresolved claims, separate causal histories

Two limits share both description and unresolved claim refs, but one is caused by an access boundary and one by an authority/handoff boundary.

**Attack:** may a deduplicator collapse them because visible text matches?

**Result:** no. The rule explicitly prohibits deduplication where kind/provenance changes the next repair route.

**Disposition:** RESISTS.

### 9. Derived view references carried limit

A correction-window or coverage view depends on a specific carried timing/access limit.

**Attack:** can the derived view silently restate generic uncertainty without retaining connection to the load-bearing limit?

**Result:** the carrier contract supplies stable carried ids and states that derived confidence, coverage, correction-window and transition views may reference those ids. Where losing the relation would change a load-bearing conclusion, the opening MUST-carry rule applies.

**Disposition:** RESISTS at source-contract level.

### 10. Original F10 counterexample replay

Replay the original pair:

```text
A: access truncation on recursive target q
B: budget exhaustion before refining q
```

with the same represented dependency and unresolved claim refs.

**Attack:** can canonical emission still erase the distinction while conforming to the repaired operator/binding contract?

**Result:** no. The serializer is now explicitly called on load-bearing `L`, the packet binds carried refs, the semantic rule requires cause/provenance survival, and deduplication on matching prose/unresolved claims is prohibited.

**Disposition:** RESISTS.

### 11. Carrier versus enforcement boundary

A packet perfectly preserves every load-bearing limit and route distinction.

**Attack:** does F10 therefore establish that a downstream selector, brake, institution or actuator will honor it?

**Result:** no.

```text
VISIBILITY != CARRYING
CARRYING != ENFORCEMENT
```

F10 repairs the first boundary only. I27 remains a separate existing distinction and no enforcement expansion is earned by this repair.

**Disposition:** RESISTS / CLAIM CEILING HOLDS.

## Verdict

```text
CLEAR_WITH_RESIDUAL_LIMITS
```

No materially distinct carrier-survival failure survived this bounded source-level attack after the F10 repair.

No new primitive was earned. No new semantic root was earned. The repair remains an existing-object carrier/binding rule over `LIMIT`, claim/provenance, aperture, clock, route/handoff and recursive-target machinery.

F10 is therefore bounded-closed at the source-contract level. Do not reopen the recursion cluster or expand F10 into enforcement without a materially distinct counterexample.

## Residual limits / claim ceiling

```text
SOURCE_LEVEL_CARRIER_CLOSURE != RUNTIME_VALIDATION
BOUNDED_CARRIER_CASE_CLEAR != COMPLETE_CORRECTNESS
SERIALIZATION_PROFILE_PRESENT != IMPLEMENTATION_EXISTS
CARRIER_CLUSTER_CLEAR != TRACE_VALIDATED
MINIMUM_SCHEMA_PASS != SEMANTIC_BINDING_PASS
LIMIT_REF_PRESENT != LIMIT_PROVENANCE_COMPLETE
CARRYING != ENFORCEMENT
NO_NEW_FINDING_IN_BOUNDED_CASES != NO_OTHER_DEFECT
```

The candidate remains WORKING / NON-CANON / UNVALIDATED. Released v0.2.7 remains untouched. No merge, release, canon, authority, permission or clearance follows from this closure.