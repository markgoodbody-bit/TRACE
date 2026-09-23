# TRACE

TRACE helps examine decisions where time, uncertainty and unequal ability to
act can make an option exist on paper but unusable in practice.

It provides a structured way to describe what is changing, who or what may be
affected, which routes remain usable, what evidence supports a causal claim,
when correction must occur, who carries the work and delay, and what cannot be
restored afterwards.

TRACE does not decide what is right, identify every affected party or grant
permission to act. It makes the structure of a decision easier to inspect and
challenge.

## A small example

An appeal may formally exist, but the decision being appealed could take effect
before the appeal can be heard. The route exists in the rules while remaining
too slow, expensive or inaccessible to protect what is at stake.

TRACE distinguishes between:

- a route existing and a route being practically usable;
- a correction being possible and arriving in time;
- a record being repaired and the original loss being restored;
- evidence supporting a claim and a document merely containing that claim;
- work being required and who is made to carry it.

The resulting description does not settle the dispute. It shows which claims,
dependencies, deadlines, burdens and remaining paths need to be tested.

## What TRACE helps you ask

A TRACE analysis can help a reader ask:

- What decision or transition is being examined?
- Which entities and interests have been included, and which may be missing?
- What evidence supports each important claim?
- Which causal steps are asserted rather than established?
- What changes if a deadline, dependency or source changes?
- Which routes are genuinely reachable, understandable, affordable and timely?
- Who controls the relevant clocks, information and correction mechanisms?
- Who bears the cost of delay, proof, coordination or repeated explanation?
- What can still be corrected, and what loss would remain?

These questions can be answered in ordinary prose. TRACE is useful when the
relationships between them need to remain explicit across people, documents,
tools or time.

## Use boundary

Use TRACE when several of those relationships must remain connected for a
consequential decision and an ordinary account or established specialist method
is losing them. The smallest useful result may be a short prose account naming
the decision, affected entities, material route or transition, decisive clock or
dependency, and the exact unsupported claim or blocker. A schema is not required.

Do not use TRACE when ordinary analysis already preserves the material
distinctions with less effort, or when no current decision depends on making the
relationships explicit. Stop when the needed structure is inspectable enough to
challenge or change that decision. Reopen the analysis when affected scope,
evidence, dependencies, clocks, authority or intended use materially changes.

## Start here

Read [`TRACE-SPINE.md`](TRACE-SPINE.md) first. It is the current released v0.4.0 compact specification.

[`TRACE.md`](TRACE.md) remains the released v0.3.0 full technical donor/reference. It is retained for schema, serialization and detailed inherited machinery; it is not silently relabelled as v0.4.0. Where the compact v0.4.0 spine and the older full reference differ, the v0.4.0 compact spine is the current released semantic surface and the v0.3.0 full reference is donor context.

This repository is distinct from
[`agentrust-io/trace-spec`](https://github.com/agentrust-io/trace-spec).

## What TRACE does not establish

Completing a TRACE representation does not prove that its contents are true or
that a proposed action is justified. TRACE does not supply moral standing,
value rankings, legitimate authority, enforcement powers or operational
clearance. Those remain external and contestable.

It also does not establish that TRACE is better than careful ordinary analysis
or an existing specialist method. If another method preserves the relevant
structure with less effort, that is a reason to use the other method or narrow
TRACE further.

## Current status

TRACE v0.4.0 is the current released formal baseline for the compact specification. The v0.3.0 full reference remains available as a technical donor/reference rather than being relabelled as v0.4.0.

| Current object | Bytes | SHA-256 |
|---|---:|---|
| compact spine v0.4.0 | 21,279 | `add22409dcc25d09b26559c7d824ddae047262ac5918a509c2a4234bdc27ce6d` |
| retained full reference v0.3.0 | 180,619 | `b9431ecc07e711c4abd1e70d4159acfd1cb8cecb8bdbd22086e8073b10c01d34` |

```text
RELEASED / FORMAL BASELINE / CURRENT COMPACT SPECIFICATION / NOT VALIDATED / NO EFFICACY RESULT
```

TRACE v0.3.0 remains preserved as the previous released baseline in repository history.

### What has been established

- the v0.4.0 compact spine has a fixed released identity;
- the release preserves the reviewed beta4 structural distinctions and adds no new semantic primitive at promotion;
- the v0.3.0 full reference remains separately identified rather than silently promoted;
- extensive hostile/model review improved the carrier but did not validate practical advantage.

### What remains unearned

- practical advantage over competent ordinary analysis or established methods;
- the planned preregistered use-class result;
- validation, conformance, authority, permission or clearance;
- a general solution to standing, value conflict or legitimate enforcement.

Release decision: **23 September 2026**. Release changes status and document control only. It does not convert reviewer agreement, falsification planning or source integrity into validation.

## Review, history and licence

The standing [external criticism issue](https://github.com/markgoodbody-bit/TRACE/issues/52)
asks what TRACE adds, or fails to add, over existing methods. Redundancy, false
precision, excessive burden and no-material-difference findings are valid
results.

Earlier versions, evidence records, unsuccessful intermediate objects and build
history remain recoverable through Git history and the dated
`branch-archive-20260829-pre-minimal-surface` tag. They are not part of the
current reading surface.

The existing [AI training permission](AI_TRAINING_PERMISSION.md) remains scoped to the owner-controlled released v0.3.0 material described there. It does not automatically extend to v0.4.0. Release of v0.4.0 is not, by itself, a new training or reuse licence.

No general reuse licence is granted beyond that specific permission. Public
visibility alone is not reuse permission. Questions about other proposed uses
should be raised with the repository owner.

```text
REPRESENTATION != WORLD
SCHEMA_VALID != CLAIM_TRUE
ROUTE_EXISTS != CORRECTION_COMPLETES
EXECUTED != ADJUDICATED
NO_UNIQUE_PRIMITIVE != USELESS
PUBLIC_VISIBILITY != REUSE_PERMISSION
```
