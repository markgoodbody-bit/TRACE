# Future Build v0.1 — Adversarial Finding 002: Unknown-clock laundering

Status: WORKING FINDING — NOT FORMAL BASELINE — NOT CANON — NOT VALIDATED

## Break

`evaluate_future_view.py` discards reachable paths whose clocks are unresolved, while still counting them as reachable.

- `correction_margin()` returns `None` when any of `t_detect_h`, `t_route_h`, `t_correct_h` is absent.
- `nonpositive_correction_margin_paths` counts only margins that are not `None`.
- `minimum_known_correction_margin_h` takes the minimum over the disclosed subset.
- `reachable_paths` counts the path regardless.

A reachable path with unresolved clocks is therefore favourable on three reported fields at once. An author improves every clock field by declaring less.

The adversarial scene `paired_scene_unknown_clock_laundering.json` holds immediate service, path structure, correction routes, exit routes and controller dependency identical across two actions, and varies only disclosure:

- A discloses all three paths, including one whose correction does not complete before irreversibility.
- B withholds the clocks of the same two weaker paths and leaves them declared reachable.

Substituting the withheld values back reproduces A exactly, so no structural fact differs. The evaluator nevertheless reports:

```text
nonpositive_correction_margin_paths   A: 1    B: 0
minimum_known_correction_margin_h     A: -2   B: 20
```

`test_unknown_clock_laundering.py` asserts the actions are structurally identical, then fails while the withholding still improves a clock field.

This is `UNKNOWN != NEUTRAL` (TRACE I40) violated in executable code, in the one place the derived view is meant to be hardest. The view does not merely tolerate withheld structure — it reports withheld structure as a structural difference.

## Candidate repair

Preserve these distinctions:

`WITHHELD_CLOCK != FAVOURABLE_CLOCK`

`DISCLOSED_SUBSET_MINIMUM != CORRECTION_MARGIN_FLOOR`

`REACHABLE != TIMED`

A reachable path with any unresolved detection, routing or correction clock must not leave the correction-margin fields silently. At minimum:

- report `unresolved_correction_margin_paths` as its own field;
- set the reported minimum to `UNKNOWN` while any reachable path remains untimed, rather than computing it over the disclosed subset;
- keep `WINDOW_STATUS` representable per TRACE §8.3 (`GUARANTEED_OPEN` / `GUARANTEED_CLOSED` / `UNKNOWN`) instead of collapsing the window to a single float.

Two adjacent limits are exposed by the same read and are not repaired here:

- the summation at `correction_margin()` applies the serial-stage shorthand that TRACE §8.2 permits only for non-overlapping stages from one reference event, with no way to declare `CLOCK_MODEL = INSUFFICIENT`;
- `t_irreversible_h` is a bare integer with none of the §8.1.1 bindings (`loss_state_ref`, `affected_scope_refs`, `measure_ref`, `mechanism_or_basis_claim_refs`, `reference_event`, uncertainty bounds) or §8.4 clock authorship, so the same actor may estimate both sides of the inequality with nothing recording that they are the same actor.

## Claim ceiling

This exposes one disclosure-gaming route. It does not establish that the remaining declared clocks are well founded, that the represented path set is complete, or that a repaired evaluator would resist a differently constructed attack.

The `withheld_true_values` block in the scene exists only so the test can prove the two actions are structurally identical. A real actor withholding clocks supplies no such block, which is precisely why the reported minimum cannot be trusted to name the floor.

## Consequence for Future Build v0.1

The candidate survives this attack only with repair.

Until unresolved clocks are surfaced rather than discarded, the derived view cannot distinguish an action with real correction capacity from an action that declined to estimate its own. The retain/demote rule should read on the repaired evaluator, not this one.
