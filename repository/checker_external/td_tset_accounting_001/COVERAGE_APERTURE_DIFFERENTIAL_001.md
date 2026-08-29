# TD-TSET coverage-aperture differential 001

Status: **constructed applied witness**

TRACE change: **none**

Checker change: **none**

## Question

The search-coverage checker can test only the targets supplied through its external comparison envelope. What happens when two apertures supply different target sets for the same TRACE packet?

## Frozen packet

Both runs use the same schema-valid ritual-search packet from applied fixture N:

- the `INFORMATION` transition observes the current working map;
- the ritual aperture searches only current-map categories;
- the field team is an explicit blindspot;
- a `CANNOT_ACCESS` relation binds that aperture to the field team.

Only the checker comparison aperture changes.

## Aperture Z1 — operator working map

The operator-supplied target set requires coverage of the hog population. The packet contains a declared path:

```text
INFORMATION transition
→ OBSERVES working map
→ CONTAINS hog population
```

Result:

```text
PASS / DECLARED_REACHABILITY_CHAIN
```

## Aperture Z2 — dispatch-record comparison

The external-record target set requires coverage of the field team. The same packet declares that target outside the ritual aperture.

Result:

```text
FAIL / TD-TSET-SEARCH-COVERAGE-CONTRADICTION
```

## Finding

```text
same TRACE packet
+ different supplied target-set aperture
= different checker result
```

The checker has not changed its mind about the packet. It has received a different comparison target.

Therefore:

> Search-coverage checking inherits the aperture of target selection.

This is not a defect that can be solved by pretending the checker knows the complete target set. It establishes why source provenance, independence and disagreement over the comparison envelope must remain visible.

## Boundary

The witness does not establish that the dispatch aperture is actually independent, complete or authoritative. Those are declared statuses. The differential preserves:

- the same packet hash;
- each aperture’s target-set provenance;
- separate checker results;
- unresolved authority between apertures.

A system can still launder coverage by choosing a narrow target set. Detecting that requires another aperture or source capable of contesting target selection; it cannot be derived from the selected target set alone.
