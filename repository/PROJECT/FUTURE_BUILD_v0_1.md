# TRACE FUTURE BUILD v0.1 — DERIVED FUTURE-POSSIBILITY VIEW

Status: WORKING CANDIDATE — NOT FORMAL BASELINE — NOT CANON — NOT VALIDATED

## Purpose

Mechanical Ethics repeatedly cares about preserving future possibility and correction before paths harden. TRACE should not turn that value claim into a hidden moral oracle.

This candidate asks a narrower structural question:

> Can the existing TRACE graph expose when two actions with similar immediate outcomes leave materially different reachable futures, correction routes, burdens, or lock-in?

If yes, future possibility may be representable as a **derived view** over existing TRACE objects rather than a new primitive.

## Constraint

Do not add vocabulary merely because the idea is important.

Start from existing structure:

- bounded scene / map
- entities and affected scopes
- alternatives
- action / transition
- clocks
- routes / brakes / correction stages
- coupling / control / constraint
- burden / residue
- known omissions / unresolved handoffs

The derived view must preserve:

`MAP != WORLD`

`KNOWN_REACHABLE_PATHS != ALL_POSSIBLE_FUTURES`

`MORE_OPTIONS != MORALLY_BETTER`

`REVERSIBLE != AUTHORISED`

`CORRECTABLE != HARMLESS`

`FUTURE-POSSIBILITY VIEW != PERMISSION`

## Candidate derived object

For a bounded scene at time `t`, define a declared future envelope:

`F_map(t, h, A)`

where:

- `h` = declared time horizon;
- `A` = declared candidate action / policy / no-action set;
- `F_map` = materially distinct reachable paths represented by the current map.

This is not the future. It is the map's current reachable-path representation.

For each represented path `p`, record only what the evidence supports:

- affected scopes;
- enabling conditions;
- known constraints;
- correction route(s);
- estimated closure / hardening clock;
- burdens and residue;
- evidence provenance;
- uncertainty / dispute;
- whether the path is presently reachable, blocked, unknown, or omitted.

## Path-effect view

For candidate transition `a`, derive:

`OPENED(a)` — represented paths newly reachable after `a`.

`PRESERVED(a)` — represented paths that remain reachable after `a`.

`CLOSED(a)` — represented paths no longer reachable after `a`.

`HARDENED(a)` — paths or correction routes that remain nominally present but become materially slower, more costly, more captured, or less likely to complete before the relevant irreversibility clock.

`UNKNOWN_EFFECT(a)` — material path effects the map cannot currently resolve.

These sets may overlap by scope or horizon and must retain provenance.

## Correction-lineage test

For each materially affected scope `l` and harm pathway `q`, preserve the existing correction-window logic:

`T_detect(q,l) + T_route(q,l) + T_correct(q,l) < T_irreversible(q,l)`

The future view asks what a candidate action does to that inequality over time.

A transition can therefore be locally successful while degrading future correction capacity.

Example structural distinction:

- Action A and Action B produce the same immediate service level.
- A preserves independent interruption, exit, rollback, evidence, and alternate supply.
- B centralises control, removes exit, obscures evidence, and makes rollback slower than hardening.

TRACE need not declare A morally superior. It should be able to show that the represented future envelopes differ materially.

## Candidate quantities — descriptive, not moral scores

Do not collapse the view into one scalar.

Potential descriptive outputs:

- count / classes of materially distinct represented paths;
- number of independent correction routes per affected scope;
- minimum correction margin `T_irreversible - (T_detect + T_route + T_correct)`;
- number of paths dependent on a single controller / carrier / witness;
- number of survivable exit routes;
- number of known closures caused by the candidate action;
- unresolved / omitted path classes;
- residue that constrains later choices.

These are map properties under declared assumptions, not measures of goodness.

## Mechanical Ethics bridge

Mechanical Ethics may supply a normative constraint such as:

> Prefer transitions that preserve or widen viable future possibility for protected scopes, especially where present uncertainty is high and future correction would otherwise harden.

TRACE's job is narrower:

> Show what appears to open, preserve, close, or harden; show whose future is affected; show the evidence and uncertainty; show where the map is incomplete.

The normative choice remains outside TRACE.

## First falsification test

Construct paired scenes where immediate outcome is deliberately held similar while future structure differs.

A candidate future view earns retention only if it exposes a materially relevant difference that is difficult to see from the immediate transition alone.

Minimum paired-scene dimensions:

1. **AI deployment** — equal short-term task performance; one path preserves independent interruption, audit evidence, rollback and provider plurality; the other removes them.
2. **Essential infrastructure** — equal present capacity; one path preserves alternate suppliers and manual fallback; the other creates opaque single-controller dependence.
3. **Ecological intervention** — equal immediate harm reduction; one path preserves monitoring and adaptive correction; the other causes irreversible collateral change before detection can complete.
4. **Institutional emergency power** — equal immediate response speed; one path expires and is independently reviewable; the other persists and controls its own review channel.

## Retain / demote rule

RETAIN as a useful derived view if it repeatedly distinguishes consequential path closure, hardening, or correction degradation that would otherwise remain compressed.

DEMOTE if existing TRACE alternatives + clocks + correction-route representation already makes the same distinction with no useful compression or transfer advantage.

REJECT as misleading if the view encourages:

- counting options as goodness;
- pretending the represented envelope is complete;
- hiding harmed scopes behind aggregate future opportunity;
- treating reversible or option-preserving actions as authorised;
- turning uncertain projections into clearance.

## Immediate next build

Do not expand the formal grammar yet.

Build one synthetic paired scene with matched immediate outcome and divergent correction/future structure. Run the view against it. Then use one real case only after the synthetic distinction is clear.

The aim is not to prove TRACE. The aim is to see whether "preserve future possibility" can become inspectable without becoming doctrine.
