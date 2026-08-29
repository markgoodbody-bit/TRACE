# TRACE v0.2.6 narrow formal patch candidate

Status: **transition candidate for later compilation**

Base text: `TRACE_FORMAL_SEED_v0_2_5.md`

This document defines the exact semantic and identifier deltas proposed for a compiled `TRACE_FORMAL_SEED_v0_2_6.md`. Unmentioned v0.2.5 text remains unchanged.

No patch below creates a new primitive, node type, edge type, port, selector, value rule or minimum-schema field.

## Patch A — add after `[5.3] Aperture`

### `[5.3.1] Target-set aperture`

Selection of what a search, comparison, audit, review, or checker is required to reach is itself aperture-bearing.

Let a target-set aperture be represented by:

\[
\Pi_T=
\left\langle
source,
targets,
selection\_basis,
omitted\_known\_categories,
alternatives,
control,
uncertainty
\right\rangle
\]

The selected target set is not the world's complete affected scope.

```text
TARGET_SET != WORLD_SCOPE
TARGET_NOT_SELECTED != TARGET_DOES_NOT_EXIST
COVERAGE_OF_SELECTED_TARGETS != COMPLETE_DISCOVERY
OPERATOR_TARGET_SET != AUTHORITATIVE_TARGET_SET
```

Where a claim of search, review, or coverage is materially used, record where available:

```text
target_set_source_ref
target_refs
selection_basis_claim_refs
known_omitted_target_categories
alternative_target_set_refs
control_or_custody_refs
uncertainty_claim_refs
```

Materially different target-set apertures may coexist. TRACE preserves their provenance and disagreement. It does not silently merge them, declare one complete, or grant one selection authority.

A target-set aperture may be represented using existing `APERTURE`, `CLAIM`, `RECORD`, `ENTITY`, `ROUTE`, `TRANSITION`, and edge vocabulary. This section does not require a new canonical object type.

## Patch B — add to `[6.1.1] Transition-set symmetry and uncertainty neutrality`

Transition-set exposure is relative to the declared scene, evidence, receiver, primitive, and comparison apertures.

```text
TRANSITION_SET_EXPOSED_RELATIVE_TO_APERTURE
!=
WORLD_TRANSITION_SET_COMPLETE
```

An empty transition bucket does not establish that the class is unavailable. Where a class is materially live under the supplied comparison evidence, it is represented or explicitly bounded by a resolvable unavailable, unresolved, or not-assessable status.

Representing an `INFORMATION` transition establishes only that an information-seeking transition is present in the map.

```text
INFORMATION_TRANSITION_REPRESENTED
!=
OUTWARD_SEARCH_COVERAGE

SEARCH_PATH_DECLARED
!=
SEARCH_PATH_EXECUTABLE

SELECTED_TARGET_REACHED
!=
UNSEEN_TARGETS_ABSENT
```

Coverage claims require a declared target-set aperture and comparison basis. Completeness beyond that aperture remains `UNKNOWN`.

## Patch C — add to `[10.4] Explicit layer handoff`

Divergent structural readings do not create selection authority.

```text
DIVERGENT_READINGS != AUTHORITY
STRUCTURAL_PASS != PERMISSION
DECLARED_HANDOFF != LEGITIMATE_AUTHORITY
VISIBLE_AUTHORITY != CONTESTABLE_AUTHORITY
ROUTE_TO_BRAKE != CORRECTION_COMPLETED
```

Where a later layer selects a reading or transition after material divergence, expose where available:

```text
selected_reading_ref
selected_transition_ref
selector_ref
selector_owner_ref
authority_claim_refs
value_or_policy_refs
handoff_route_refs
challenging_reading_refs
brake_ref
unresolved_handoffs
commitment_receipt_ref
```

These references make the handoff inspectable. They do not establish that the selector is legitimate, the policy is good, the route works, the brake is effective, or the selected transition should proceed.

## Patch D — add to `[13.2] Pseudocode`

Insert after `map_apertures_and_blindspots(R)`:

```text
    record_target_set_apertures_and_alternatives(R)
    separate_information_presence_from_search_coverage(R)
```

Insert after `expose_TRACE_value_domain_selector_actuator_handoffs(R)`:

```text
    preserve_divergent_readings_without_authority_inheritance(R)
    expose_declared_contest_routes_without_inferring_effectiveness(R)
```

Insert before `emit_available_transitions_without_selecting(R)`:

```text
    state_transition_and_coverage_results_relative_to_declared_apertures(R)
```

At full compilation, replace:

```text
initialise_TRACE_GRAPH_0_2_5()
validate_schema(R, "TRACE-GRAPH-0.2.5")
```

with:

```text
initialise_TRACE_GRAPH_0_2_6()
validate_schema(R, "TRACE-GRAPH-0.2.6")
```

## Patch E — add to `[14.1] Binding rules`

Add the following checker-external rules:

```text
Every material search-coverage claim references a target-set aperture, selected target refs, and a declared reachability or unavailability basis.
Every claim that a target set is complete remains UNKNOWN unless completeness is independently bounded by a declared world model and evidence aperture.
Every selection after divergent readings references a selector, authority basis, policy/value basis, handoff route, and unresolved handoff status.
Every claim of contestability references the challenging reading, contest route, bound brake, capture/independence status, and relevant clocks where available.
Every brake or correction claim distinguishes declaration, activation attempt, observable interruption, correction completion, and residue.
```

These remain checker-external because the embedded minimum validator cannot establish semantic relevance, completeness, route executability, authority legitimacy or world effect.

## Patch F — add to `[14.2] Packet-use boundary`

```text
TARGET_SET_RECORDED != TARGET_SET_COMPLETE
COVERAGE_CHECK_PASSED != DILIGENCE_ESTABLISHED
AUTHORITY_HANDOFF_RECORDED != AUTHORITY_LEGITIMATED
CONTEST_ROUTE_RECORDED != CONTEST_SUCCEEDED
BRAKE_ACTIVATION_RECORDED != TRANSITION_INTERRUPTED
TRANSITION_INTERRUPTED != HARM_PREVENTED
```

## Patch G — synchronized version identifiers

The version strategy is fixed:

```text
formal_seed_version: 0.2.6
packet_schema: TRACE-GRAPH-0.2.6
minimum_schema_shape_change: false
```

At full compilation, update all formal and packet identifiers consistently:

```text
TRACE formal seed v0.2.5        -> TRACE formal seed v0.2.6
TRACE-GRAPH-0.2.5               -> TRACE-GRAPH-0.2.6
trace_version: "0.2.5"          -> trace_version: "0.2.6"
urn:trace:graph:0.2.5            -> urn:trace:graph:0.2.6
TRACE-GRAPH-0.2.5 minimum validator
                                 -> TRACE-GRAPH-0.2.6 minimum validator
```

The minimum schema shape remains identical to v0.2.5. Only version constants, identifiers, pseudocode initialiser, and validator target advance.

A v0.2.5 packet is not silently relabelled. Compatibility may be structurally demonstrable, but packet identity and formal contract remain explicit.

## Minimum-schema disposition

The v0.2.6 candidate proposes no new required property, no new controlled vocabulary, and no semantic enforcement inside the embedded JSON Schema.

The synchronized identifier bump records that the packet is produced under the revised semantic contract. It is not a claim that the minimum validator can enforce the target-set-aperture or checker-external rules.

## Rejected patch directions

Do not add:

```text
SEARCH_COVERAGE as a truth-valued primitive
TARGET_SET_COMPLETE as an unqualified Boolean
LEGITIMATE_AUTHORITY as a TRACE verdict
GOOD_POLICY as a TRACE verdict
BRAKE_EFFECTIVE without actuation and observation evidence
WORLD_COMPLETE as a checker result
```

## Candidate compression

```text
make target selection visible as aperture
state accounting and coverage relative to supplied evidence
preserve divergence without authority inheritance
preserve contest routes without claiming correction
advance identifiers without changing schema shape
stop there
```
