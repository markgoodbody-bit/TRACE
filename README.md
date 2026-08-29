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

1. Read [`TRACE-SPINE.md`](TRACE-SPINE.md) for the compact specification and
   primary review surface.
2. Use [`TRACE.md`](TRACE.md) when you need the full technical reference,
   serialization details or the complete inherited schema contract.

The compact spine is the normal entry point. The full reference is not required
for an initial reading.

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

The two current documents form the **v0.3.0 specification release candidate 1
(RC1)**:

| Object | Bytes | SHA-256 |
|---|---:|---|
| compact spine RC1 | 25,795 | `9ee106e98a34643929f82fa3296adffac46e650e4e8d0b775016269f0fe50999` |
| full reference RC1 | 180,511 | `1dfc668d3e3dc5d85dcfc8bed5a025672025aff3ce157205b55bbc5f54160a1f` |

```text
RELEASE CANDIDATE / NOT RELEASED / NOT CANON / NOT VALIDATED / NO EFFICACY RESULT
```

TRACE v0.2.7 remains the released formal baseline.

### What has been established

- The current candidate documents have exact identities.
- The v0.3 minimum schema adds no semantic primitives to v0.2.7.
- A bounded ten-stage source-contract challenge was completed for this pass.
- A comparison with FPF found no TRACE-unique semantic primitives in the
  examined material.
- A 32-call comparison was completed and showed material representation burden.

### What remains unearned

- practical advantage over competent ordinary analysis or established methods;
- an efficacy result from the unadjudicated paired outputs;
- validation, conformance, authority, permission or clearance;
- a general solution to standing, value conflict or legitimate enforcement.

The current working hypothesis is therefore narrow: TRACE may be useful as a
specialised representation and transfer surface that keeps affected scope,
causal transitions, clocks, correction routes, burden, residue and uncertainty
together. This is a provisional use hypothesis, not a claim of novelty or
superiority.

## Review, history and licence

The standing [external criticism issue](https://github.com/markgoodbody-bit/TRACE/issues/45)
asks what TRACE adds, or fails to add, over existing methods. Redundancy, false
precision, excessive burden and no-material-difference findings are valid
results.

Earlier versions, evidence records, unsuccessful intermediate objects and build
history remain recoverable through Git history and the dated
`branch-archive-20260829-pre-minimal-surface` tag. They are not part of the
current reading surface.

No general reuse licence has been granted for this repository or its contents.
Public visibility permits inspection, linking, discussion and review; it does
not itself grant permission to copy, adapt, redistribute, train on, sell or
incorporate the material into another work. Questions about a proposed use
should be raised with the repository owner.

```text
REPRESENTATION != WORLD
SCHEMA_VALID != CLAIM_TRUE
ROUTE_EXISTS != CORRECTION_COMPLETES
EXECUTED != ADJUDICATED
NO_UNIQUE_PRIMITIVE != USELESS
PUBLIC_VISIBILITY != REUSE_PERMISSION
```
