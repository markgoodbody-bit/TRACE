# TD-TSET-SEARCH-COVERAGE-001

Status: **checker-external working candidate**

TRACE change: **none**

Minimum-schema change: **none**

Transition-accounting change: **none**

## Question

`TD-TSET-ACCOUNTING-001` can establish that an `INFORMATION` transition is represented. The schema-valid ritual fixture N showed that this does not establish that the transition can reach a declared discovery target.

This candidate asks a narrower question:

> Given a supplied discovery target, a represented `INFORMATION` transition, its bound aperture, and a declared packet-internal reachability path, does the packet explicitly contradict or fail to support its own coverage claim?

It does not ask whether the search is genuinely exhaustive or whether the target set is complete.

## Checker-only comparison envelope

```json
{
  "coverage_evidence": {
    "assessment_status": "ASSESS",
    "information_transition_ref": "n_info_dispatch",
    "required_target_refs": ["n_entity_field_team"],
    "comparison_basis_claim_refs": ["c_omission", "c_record"],
    "target_path_edge_refs": {
      "n_entity_field_team": [
        "e_info_observes_record",
        "e_record_reports_team"
      ]
    }
  }
}
```

`coverage_evidence` is not a TRACE field. It supplies the external comparison target and the edge path to inspect.

Assessment states:

- `ASSESS`
- `UNAVAILABLE`
- `NOT_ASSESSABLE`

## Base coverage pass

For an `ASSESS` envelope, the base pass verifies that:

- the transition reference resolves to an `INFORMATION` `TRANSITION`;
- the transition binds to a resolvable `APERTURE`;
- required target and comparison-basis references resolve;
- each declared reachability path is contiguous, begins at the transition or aperture, and ends at the required target;
- path edges use a narrow reachability vocabulary;
- the selected aperture does not also declare the required target as a blindspot or bind a `CANNOT_ACCESS` edge to it.

## Hostile comparison-envelope integrity pass

`search_coverage_integrity.py` keeps additional assumptions separate and visible. It verifies that:

- an `ASSESS` or `UNAVAILABLE` comparison has at least one basis claim;
- basis and reason claim references resolve;
- unavailability reasons bind the supplied basis;
- declared path edges are directed;
- declared path edges carry resolvable claim references;
- each declared target path shares at least one claim with the comparison basis.

The integrity pass does not turn those claims into truth.

## One orchestration entry point

Run both passes on one JSON envelope:

```bash
python checker_external/td_tset_accounting_001/run_search_coverage.py check envelope.json
```

Run bounded O–R regressions:

```bash
python checker_external/td_tset_accounting_001/run_search_coverage.py regress
```

The orchestrator keeps result objects, failure codes and epistemic ceilings separate. A combined failure means at least one pass failed; it is not a replacement semantic verdict.

## Failure codes

### `TD-TSET-SEARCH-COVERAGE-CONTRADICTION`

A required discovery target is explicitly named as a blindspot of the selected aperture or is the target of a `CANNOT_ACCESS` edge from that aperture.

### `TD-TSET-SEARCH-COVERAGE-UNSUPPORTED-REACHABILITY`

The supplied target has no contiguous declared reachability path, the path uses relations that do not support the claimed access chain, or the comparison envelope lacks the basis needed for its claim.

### `TD-TSET-SEARCH-COVERAGE-REFERENCE-MISMATCH`

A transition, aperture, target, comparison-basis claim, reason claim, path edge or edge-support claim does not resolve to the required object.

## Fixtures O–R

| Fixture | Expected result |
|---|---|
| O — declared transition→record→target path | PASS / `DECLARED_REACHABILITY_CHAIN` |
| P — ritual aperture declares target as blindspot and `CANNOT_ACCESS` | FAIL / `TD-TSET-SEARCH-COVERAGE-CONTRADICTION` |
| Q — no coverage comparison envelope | PASS / `NOT_ASSESSABLE` |
| R — INFORMATION explicitly unavailable under bound clocks | PASS / `NOT_APPLICABLE_INFORMATION_UNAVAILABLE` |

Hostile tests additionally cover:

- missing declared path;
- missing target;
- non-contiguous path;
- empty comparison basis;
- undirected path edge;
- unresolved path-edge claim;
- unavailability reason unbound from its clock basis;
- a weak base PASS caught by the separate integrity pass.

## Epistemic ceiling

A contiguous declared path is still a representation. It does not establish:

- actual source contents;
- route executability;
- genuine aperture widening;
- good faith;
- complete target selection;
- discovery of unseen entities;
- world completeness.

The checker can catch an explicit self-contradiction or unsupported declaration. It cannot stop an actor from choosing a conveniently narrow target set or fabricating internally consistent claims.
