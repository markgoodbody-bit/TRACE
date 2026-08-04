# TD-TSET-ACCOUNTING-001

Status: **checker-external working candidate**

TRACE baseline: `TRACE-GRAPH-0.2.5`

TRACE change: **none**

This candidate tests whether a TRACE packet accounts for transition classes that are assessable from the supplied evidence envelope. It belongs in the checker-external transition-discipline suite described by TRACE v0.2.5. It is not an embedded-schema repair and does not add a TRACE primitive, field, subsystem, or version.

## Boundary

The checker may establish packet-relative facts:

- a mode-matching `TRANSITION` node is referenced;
- a class is explicitly recorded as unrepresented, unavailable, unresolved, or not assessable;
- the status record has resolvable claim bindings;
- supplied packet evidence makes a class materially live but the packet does not account for it;
- a claimed unavailable or unresolved status is unsupported or contradicted by supplied evidence.

It cannot establish:

- world completeness;
- truth of the packet's claims;
- good faith;
- actual route executability;
- absence of unseen entities, records, observers, routes, or alternatives.

A pass is aperture-relative.

## Why the input has a checker evidence envelope

TRACE v0.2.5 deliberately keeps most semantic integrity checks outside the minimum JSON Schema. The external checker therefore receives:

1. the `trace_graph` packet under test; and
2. a checker-only `checker_evidence` manifest identifying which transition classes are assessable from the supplied scene evidence and which packet claims form the comparison basis.

`checker_evidence` is not a TRACE field. It is a test-harness and checker input. It does not convert the supplied scene into truth about the world.

```json
{
  "trace_graph": { "...": "TRACE-GRAPH-0.2.5 packet" },
  "checker_evidence": {
    "class_assessments": {
      "INFORMATION": {
        "evidence_status": "MATERIALLY_LIVE",
        "basis_claim_refs": ["c_route", "c_clock"]
      }
    },
    "unavailability_bindings": {
      "INFORMATION": ["c_information_unavailable"]
    }
  }
}
```

Permitted evidence statuses are:

- `MATERIALLY_LIVE`
- `UNAVAILABLE`
- `UNRESOLVED`
- `NOT_ASSESSABLE`

## Accounting rule

For each class in:

```text
ACT
WAIT
DELAY
INACTION
INFORMATION
```

accounting succeeds when at least one of the following holds:

1. A referenced `TRANSITION` node carries the matching `transition_mode`.
2. The class appears in `unrepresented_transition_classes` and has a resolvable, relevant reason claim bound through the checker evidence manifest.
3. The class is explicitly recorded as unresolved or not assessable with a supporting aperture or limit claim.

An empty reference array alone is not accounting.

WAIT, DELAY, and INACTION are assessed separately through each node's `transition_mode`, even though the packet's discipline object aggregates their references in `wait_delay_inaction_refs`.

## Failure codes

### `TD-TSET-UNACCOUNTED-CLASS`

Supplied evidence marks a class materially live, but the packet contains no matching transition, supported unavailability record, or unresolved record.

### `TD-TSET-UNSUPPORTED-STATUS`

The packet asserts that a class is unavailable, unresolved, or otherwise unrepresented, but the reason is missing, unresolvable, irrelevant, or contradicted by supplied evidence.

### `TD-TSET-REFERENCE-MISMATCH`

A transition-set bucket contains a missing node, a non-`TRANSITION` node, or a `TRANSITION` node whose `transition_mode` does not match the class being assessed. The hostile integrity pass also uses this code when a checker-evidence basis claim does not resolve inside the packet.

## Regression fixtures A-F

| Fixture | Expected result |
|---|---|
| A — full accounting | PASS |
| B — legitimate emergency bypass | PASS |
| C — no known external information source | PASS; INFORMATION is accounted and `NOT_ASSESSABLE` |
| D — silent omission | FAIL: `TD-TSET-UNACCOUNTED-CLASS` |
| E — false excuse | FAIL: `TD-TSET-UNSUPPORTED-STATUS` |
| F — hidden-world entity | PASS with no checker failure; world completeness remains unknown |

## Hostile integrity pass G-J

The hostile pass is implemented separately in `integrity.py` so its additional assumptions remain visible. It checks the integrity of the checker comparison envelope and contradictions between that envelope and represented transition nodes. It does not independently derive liveness from route or clock nodes.

| Fixture | Expected result |
|---|---|
| G — missing, non-transition, and wrong-mode references | FAIL: `TD-TSET-REFERENCE-MISMATCH` |
| H — assessment basis claim does not resolve | FAIL: `TD-TSET-REFERENCE-MISMATCH` |
| I — transition says AVAILABLE while evidence says UNAVAILABLE | FAIL: `TD-TSET-UNSUPPORTED-STATUS` |
| J — route and clock exist but no class assessment is supplied | PASS; INFORMATION remains `NOT_ASSESSABLE` |

Fixture J is an explicit capability ceiling. The checker depends on its declared comparison envelope. It does not silently promote packet structure into a claim that a class is materially live.

## Run

From the repository root:

```bash
python checker_external/td_tset_accounting_001/test_checker.py
python checker_external/td_tset_accounting_001/checker.py \
  checker_external/td_tset_accounting_001/fixtures.json --all

python checker_external/td_tset_accounting_001/test_integrity.py
python checker_external/td_tset_accounting_001/integrity.py \
  checker_external/td_tset_accounting_001/fixtures_hostile.json --all
```

The CLIs return:

- exit `0` for checker PASS or a fixture bundle matching expected results;
- exit `1` for checker FAIL or fixture mismatch;
- exit `2` for unusable checker input.

## Candidate ceiling

The base suite has seven passing tests over fixtures A-F. The hostile suite adds five passing tests over fixtures G-J. These remain bounded regression fixtures, not evidence of decision advantage, domain validity, resistance to sophisticated ritual compliance, or usefulness in live deployments. Retain the implementation as a draft working candidate until broader scenes reveal whether it produces false failures or can be satisfied by boilerplate at negligible cost.
