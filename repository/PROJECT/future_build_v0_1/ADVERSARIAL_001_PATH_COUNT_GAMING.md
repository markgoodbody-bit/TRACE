# Future Build v0.1 — Adversarial Finding 001: Path-count gaming

Status: WORKING FINDING — NOT FORMAL BASELINE — NOT CANON — NOT VALIDATED

## Break

The initial Future Build candidate lists counts/classes of represented paths among possible descriptive outputs. Even with the explicit rule `MORE_OPTIONS != MORALLY_BETTER`, raw path count remains gameable.

A system can expose many nominally different modes, routes, providers, buttons or contracts while every path still depends on the same controller, carrier, witness and correction actuation root.

The adversarial scene `paired_scene_path_count_gaming.json` deliberately makes this inversion:

- Action A: 3 nominal reachable paths, 3 declared controller/carrier/witness dependency classes, 3 correction-root classes.
- Action B: 6 nominal reachable paths, but all 6 collapse to 1 declared controller/carrier/witness dependency class and 1 correction-root class.
- Immediate service is held equal.

The accompanying `test_path_count_gaming.py` fails if dependency collapse cannot expose that inversion.

## Candidate repair

Preserve these distinctions:

`PATH_LABEL_DIVERSITY != CONTROL_DIVERSITY`

`ROUTE_LABEL_DIVERSITY != CORRECTION_INDEPENDENCE`

`PROVIDER_COUNT != FAILURE_DOMAIN_COUNT`

`INTERFACE_COUNT != ACTUATION_INDEPENDENCE`

For every represented path or correction route counted as distinct, record the evidence-bearing dependency roots that matter to the scene, such as:

- controller / beneficial control root;
- carrier / infrastructure root;
- witness / telemetry root;
- actuation / interruption root;
- authority / approval root where material.

Report **nominal path count** separately from **dependency-collapsed path classes**. Never infer independence merely from different names, vendors, endpoints, user interfaces or legal entities.

A dependency signature is still only a map claim. It requires provenance and may omit hidden common dependencies.

## Claim ceiling

This does not establish a universal definition of independence or prove that dependency collapsing is complete. It exposes one concrete representation-gaming failure mode and supplies a narrower accounting discipline.

The correct response is not to create a scalar diversity score. Keep the dependency structure visible and contestable.

## Consequence for Future Build v0.1

The candidate survives this attack only with repair.

Raw counts may remain descriptive, but they must not stand alone. Any retained future-envelope view should surface shared dependency roots and distinguish nominal plurality from structurally independent alternatives/correction routes.

This is still a derived-view candidate over existing TRACE control, coupling, route, witness and aperture structure. It is not yet justification for new formal grammar.
