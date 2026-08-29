# TRACE external review guide

This guide is for people encountering TRACE for the first time and for reviewers who want to test it rather than merely read it.

TRACE is an attempt to make the structure of decisions and transitions more visible under uncertainty. It is not a moral authority, policy framework, certification system, truth oracle, or permission mechanism. An invitation to review it is not a claim that it works.

## A useful first pass

For a quick orientation:

1. Read the root [`README.md`](../README.md).
2. Read the compact current [`TRACE-SPINE.md`](../TRACE-SPINE.md).
3. Use the full current [`TRACE.md`](../TRACE.md) when the spine is
   insufficient for the review question.

For the released v0.2.7 baseline, use
[`TRACE_FORMAL_SEED_v0_2_7.md`](TRACE_FORMAL_SEED_v0_2_7.md). Its
[`TRACE.pdf`](TRACE.pdf) is the rendered carrier; the Markdown file remains the
formal source.

The formal source retains the wording of the reviewed compiled candidate. Its active release status is recorded separately in [`TRACE_v0_2_7_BASELINE_RELEASE.md`](TRACE_v0_2_7_BASELINE_RELEASE.md), so promotion did not rewrite the reviewed object.

## Reviewing the v0.3.0 working candidate

Begin at the root [`TRACE-SPINE.md`](../TRACE-SPINE.md), then consult the
[`work/v0_3_0/README.md`](work/v0_3_0/README.md) package and readiness audit
before making claims about current evidence.

The package deliberately excludes most intermediate build and experiment
history from the review path. That history remains available through its
immutable quarry pointer. The package verifier establishes copied byte identity
and selected status markers only; it is not a semantic or efficacy validator.

## Choose a review lane

### 1. Conceptual and semantic

Test whether the distinctions are coherent and necessary.

Questions include:

- Does TRACE expose information that ordinary prose, a causal graph, a safety case, or an audit record would otherwise lose?
- Does it keep world, scene, map, action, and transition separate?
- Does it preserve uncertainty without turning uncertainty into either permission to act or permission to delay?
- Are value choices, standing, comparison measures, and selection authority kept outside the structural description?
- Does any notation create more apparent precision than the evidence supports?

### 2. Formal and type-level

Test the typed graph, relations, invariants, serialization profile, and non-entailments.

Look for:

- type collapse;
- duplicate or unnecessary primitives;
- relations that silently upgrade evidence;
- contradictions between prose, equations, schema, and examples;
- required information that cannot be represented using the declared vocabulary;
- a derived view being treated as an independent source of truth.

### 3. Operational

Try to instantiate TRACE on a real decision or system.

Ask:

- What evidence would be required to populate the reading honestly?
- Which quantities lack a usable estimator?
- Can affected scopes, omitted target categories, available transitions, correction routes, and residue be identified in practice?
- Does the representation improve a decision, review, handoff, or later reconstruction compared with the existing process?
- What does the method cost in time, expertise, access, and institutional cooperation?

A schema-valid packet is not a world-valid reading. The embedded minimum validator checks shape and controlled vocabulary; it cannot establish truth, relevance, completeness, authority legitimacy, route executability, brake effectiveness, correction, or world effect.

### 4. Adversarial and institutional

Assume an operator wants the appearance of diligence without changing the underlying mechanism.

Test whether TRACE can be used to:

- produce procedural theatre;
- hide a narrow target set behind a completed checklist;
- cite a packet as authority or clearance;
- record a brake that is captured, unreachable, untested, or never activated;
- relabel a selected action as a resolved dispute;
- erase burden or residue through aggregation;
- convert delay into an apparently neutral outcome;
- treat a recorded handoff as legitimate authority.

The formal seed explicitly states that TRACE can represent procedural theatre but cannot prevent an actor from using TRACE as procedural theatre. Review whether its anti-compression rules make that misuse easier to detect or merely add documentation.

### 5. Empirical and transfer

TRACE has not established decision advantage, operational effectiveness, or world validity.

A strong empirical review would define:

- the baseline process;
- the scene and decision class;
- what counts as a materially relevant distinction;
- what outcome or reconstruction quality is being compared;
- costs and failure modes introduced by TRACE;
- conditions under which the result would count against the method.

Constructed examples and executable audits test declared structure. They are not field evidence.

## High-value review questions

The following questions are more useful than a general approval or rejection:

1. What important distinction is still compressed or absent?
2. What existing distinction is redundant, incoherent, or falsely precise?
3. Where can a reader confuse representation with world state, capability with effect, or record with repair?
4. Does target-set recording expose selection and omission, or merely formalize the operator's aperture?
5. Can two divergent readings remain separate without silently creating a selector or authority?
6. Does the correction-window structure distinguish detection, routing, attempted intervention, observable interruption, completed correction, and residue?
7. Which claim currently depends on an estimator, evidence source, or authority that the formal layer cannot supply?
8. What real case would provide a fair test, and what result would falsify or narrow the claim?

## Recommended finding format

Please make findings traceable and bounded:

```text
finding id / short title
review lane
exact file and section evidence
fact
inference
failure mode
why current safeguards do or do not contain it
smallest justified repair or test
severity / effect on use or release status
```

A useful hostile review may conclude that a component should be narrowed, demoted to guidance, replaced by an existing method, or removed.

## Current claim boundary

The active formal baseline is TRACE v0.2.7. It is released for use, citation, testing, and revision from that baseline, but it remains:

```text
NOT_CANON
NOT_VALIDATED
NOT_AUTHORITY
NOT_PERMISSION
NOT_CLEARANCE
```

The current executable evidence establishes declared source binding, deterministic construction, surface propagation, mutation detection, and stated containment. It does not establish semantic adequacy, complete target discovery, legitimate authority, moral correctness, operational effectiveness, or decision advantage.

## Submit feedback

Use the repository's **TRACE review feedback** issue template:

https://github.com/markgoodbody-bit/TRACE/issues/new?template=trace-review.md

Review and criticism are invited. Reuse and licensing terms have not yet been specified; public visibility alone should not be read as a reuse licence.
