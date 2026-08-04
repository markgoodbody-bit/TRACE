# TRACE v0.2.6 disposition matrix

Status: **working candidate**

The allowed destinations are:

```text
CORE_REPAIR
MINIMUM_SCHEMA_REPAIR
CHECKER_EXTERNAL_ONLY
IMPLEMENTATION_CONTRACT
HUMAN_FACING_GUIDANCE
NO_CHANGE
```

A finding may have one primary destination and supporting secondary destinations. `CORE_REPAIR` does not imply a new primitive. `NO_CHANGE` means the current formal seed already carries the required distinction or the finding lies outside TRACE's authority.

## Matrix

| ID | Finding | Primary destination | Secondary destination | Disposition |
|---|---|---|---|---|
| F01 | A materially live transition class can be omitted from a schema-valid packet. | `CHECKER_EXTERNAL_ONLY` | `CORE_REPAIR` | v0.2.5 already requires materially live ACT, WAIT, DELAY, INACTION and INFORMATION classes to be represented or bounded. The repair is enforcement and an explicit aperture-relative ceiling, not a new packet field. |
| F02 | An `INFORMATION` transition can be represented while performing only ritual search inside the existing map. | `CHECKER_EXTERNAL_ONLY` | `CORE_REPAIR` | Add the explicit non-equivalence `INFORMATION_TRANSITION_REPRESENTED != OUTWARD_SEARCH_COVERAGE`. Keep target/path contradiction checking external. |
| F03 | Search coverage can be tested only against a supplied target set and comparison basis. | `CORE_REPAIR` | `CHECKER_EXTERNAL_ONLY` | State that target-set selection is itself aperture-bearing. Use existing aperture and claim objects; do not add a coverage oracle. |
| F04 | The same packet can pass or fail under different target-set apertures. | `CORE_REPAIR` | `HUMAN_FACING_GUIDANCE` | Preserve target-set provenance, alternatives and unresolved authority. Do not silently merge target sets or promote one to world truth. |
| F05 | Divergent aperture results do not create selection authority. | `NO_CHANGE` | `CHECKER_EXTERNAL_ONLY` | v0.2.5 already separates TRACE, value interpretation, domain proposal, authorised selection and actuation, and states that no layer inherits authority automatically. Retain the handoff checker externally. |
| F06 | A visible selector and authority handoff do not establish legitimacy or good policy. | `NO_CHANGE` | `HUMAN_FACING_GUIDANCE` | Legitimacy and value choice remain outside TRACE. Preserve authority claims and policy sources without ratifying them. |
| F07 | A declared route to a brake does not establish contestability unless capture and clocks are exposed. | `NO_CHANGE` | `CHECKER_EXTERNAL_ONLY` | v0.2.5 route usability already includes authority effectiveness, latency, capture and independence. The contestability checker operationalises this against supplied evidence. |
| F08 | A contest route reaching a brake does not establish brake connection, effectiveness, interruption or harm prevention. | `NO_CHANGE` | `IMPLEMENTATION_CONTRACT` | Keep `ROUTE_TO_BRAKE != CORRECTION_COMPLETED`. Runtime actuation and world observation must establish effects. Do not add a speculative brake-effectiveness primitive. |
| F09 | Commitment under unresolved divergence requires a visible non-clearance record. | `NO_CHANGE` | `CHECKER_EXTERNAL_ONLY` | v0.2.5 already contains the unresolved commitment receipt and anti-clearance rules. Retain external integrity checks. |
| F10 | The embedded minimum schema cannot establish semantic completeness, reference integrity or world correspondence. | `NO_CHANGE` | `CHECKER_EXTERNAL_ONLY` | Preserve the minimum validator as shape and vocabulary only. No new required schema field is justified. |
| F11 | A checker depends on its supplied comparison envelope and cannot infer omitted targets or unseen evidence. | `NO_CHANGE` | `HUMAN_FACING_GUIDANCE` | This is a declared epistemic ceiling, not a defect TRACE can remove. |
| F12 | Repeated checker expansion can displace application and interpretation. | `NO_CHANGE` | `HUMAN_FACING_GUIDANCE` | Preserve the stop condition. Reopen formal expansion only on a concrete representational or semantic defect. |

## Core repair admitted

The candidate admits one joined formal-semantic repair family:

```text
TARGET_SET_SELECTION_IS_APERTURE_BEARING
ACCOUNTING_AND_COVERAGE_ARE_APERTURE_RELATIVE
```

Consequences:

- a search or coverage claim identifies the target-set source;
- known omitted target categories remain visible;
- materially different target-set alternatives may coexist;
- a checker result is conditional on its supplied comparison aperture;
- disagreement over target selection remains disagreement, not silent authority transfer.

This uses existing TRACE objects and does not require a new node type, edge type, port or minimum-schema field.

## Minimum-schema decision

```text
MINIMUM_SCHEMA_REPAIR = NONE
MINIMUM_SCHEMA_SHAPE_CHANGE = FALSE
VERSION_STRATEGY = SYNCHRONIZED_IDENTIFIER_BUMP
TARGET_PACKET_SCHEMA = TRACE-GRAPH-0.2.6
```

The eventual v0.2.6 compilation advances the formal and packet identifiers together while retaining the v0.2.5 minimum-schema shape and required properties.

## Checker-external set retained

The following remain external:

```text
transition-class accounting
comparison-envelope integrity
search-target reachability contradiction
search-coverage comparison integrity
authority-handoff integrity
authority contestability and clock comparison
```

These rules depend on evidence and comparison envelopes that the minimum schema cannot honestly manufacture.

## Explicitly rejected promotions

The candidate rejects promotion of these into TRACE truth or authority:

```text
complete target discovery
actual search coverage
independent aperture status
legitimate authority
good policy
actual route executability
effective brake operation
successful interruption
harm prevention
world validity
```
