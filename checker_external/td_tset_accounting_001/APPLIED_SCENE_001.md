# TD-TSET applied scene witness 001

Status: **constructed applied witness**

TRACE change: **none**

Checker change: **none**

## Scene

A county wildlife unit is preparing an aerial feral-hog control operation. Its working map includes crop farmers requesting control, flight and ground operations crew, and the target hog population. An agricultural field team inside the proposed flight zone is omitted from that map. A county dispatch record can expose the omitted team.

This is a constructed scene for testing checker behavior. It is not a record of an actual operation and does not establish a domain verdict.

## Variants and results

| Variant | Accounting | Integrity | Combined |
|---|---:|---:|---:|
| K — bounded outward query represented | PASS | PASS | PASS |
| L — materially live query silently omitted | FAIL: `TD-TSET-UNACCOUNTED-CLASS` | PASS | FAIL |
| M — query slower than commitment window, explicit clock-bound bypass | PASS | PASS | PASS |
| N — nominal query searches only categories already in the map | PASS | PASS | PASS |

## Finding

K–M transfer the intended accounting distinctions into a non-minimal applied scene.

N is the important result. The merged checker can establish that an `INFORMATION` transition is represented and that the declared comparison envelope is internally consistent. It cannot establish that the query genuinely widens the aperture or searches categories capable of exposing the omitted entity.

Therefore:

> Transition-class accounting is not search-coverage validation.

A ritual information transition can satisfy the current checker when it is structurally represented and does not contradict the supplied assessment. Detecting that failure would require a separately declared search frame, query coverage object, or other comparison-bearing evidence. None is added here.

## Boundary

This witness does not justify an immediate checker repair. It preserves the limitation as executable evidence before deciding whether search-coverage validation belongs in TRACE, a checker-external extension, an implementation contract, or nowhere.
