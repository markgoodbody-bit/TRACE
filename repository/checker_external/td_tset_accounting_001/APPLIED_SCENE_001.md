# TD-TSET applied scene witness 001

Status: **constructed applied witness**

TRACE change: **none**

Checker change: **none**

Minimum-schema validation: **PASS**

Schema source: embedded `TRACE-GRAPH-0.2.5 minimum validator` extracted directly from `TRACE_FORMAL_SEED_v0_2_5.md`

Schema id: `urn:trace:graph:0.2.5`

Extracted schema SHA-256: `4f2326b7c85c8d45686db80b30c667c534a68faaaf370d08b74a326f4b7d99af`

## Scene

A county wildlife unit is preparing an aerial feral-hog control operation. Its working map includes crop farmers requesting control, flight and ground operations crew, and the target hog population. An agricultural field team inside the proposed flight zone is omitted from that map. A county dispatch record can expose the omitted team.

This is a constructed scene for testing checker behavior. It is not a record of an actual operation and does not establish a domain verdict.

K–N are non-minimal `TRACE-GRAPH-0.2.5` packets. The test harness extracts the embedded JSON Schema from the reviewed baseline at runtime rather than maintaining a copied schema. All four packets pass that schema, and a negative control proves the validator rejects a packet missing a required anti-clearance field.

## Variants and results

| Variant | Minimum schema | Accounting | Integrity | Combined |
|---|---:|---:|---:|---:|
| K — bounded outward query represented | PASS | PASS | PASS | PASS |
| L — materially live query silently omitted | PASS | FAIL: `TD-TSET-UNACCOUNTED-CLASS` | PASS | FAIL |
| M — query slower than commitment window, explicit clock-bound bypass | PASS | PASS | PASS | PASS |
| N — nominal query searches only categories already in the map | PASS | PASS | PASS | PASS |

## Finding

K–M transfer the intended accounting distinctions into schema-valid applied packets.

N is the important result. The packet explicitly represents:

- an `INFORMATION` transition;
- an aperture restricted to categories already present in the working map;
- the omitted field team as a declared blindspot;
- a `CANNOT_ACCESS` relation from the ritual aperture to that team.

The embedded schema accepts the packet. The accounting and hostile-integrity passes also accept it. They establish that an `INFORMATION` transition is represented and internally consistent relative to the supplied comparison envelope. They do not establish that the query genuinely widens the aperture or can expose the omitted entity.

Therefore:

> Transition-class accounting is not search-coverage validation.

The limitation survives minimum-schema validation. It is no longer an artifact of abbreviated fixture shape.

## Boundary

This does not justify an automatic TRACE or checker repair. A coverage check would require a declared comparison basis for what the query was capable of reaching: for example, a search frame, source set, boundary alternative, or aperture-difference claim. That is a separate question from whether an information transition exists.

The witness remains constructed and aperture-relative. Schema validity, internal consistency, and accounting do not establish world validity, good faith, actual route executability, or successful discovery.
