# TRACE

**A structural language for examining decisions and transitions under uncertainty.**

TRACE asks a narrow question:

> Before a system acts, what distinctions must remain visible so that uncertainty, affected scopes, alternatives, correction routes, burdens, and residue are not compressed away?

It is being developed as a typed graph, a machine-readable packet structure, and a set of anti-compression rules. TRACE does not choose values or policy, confer authority, establish moral status, prove its world model, or grant permission to act.

## Name disambiguation

This repository's TRACE is not affiliated with the separate [`agentrust-io/trace-spec`](https://github.com/agentrust-io/trace-spec) project, which expands TRACE as **Trust, Runtime Attestation, and Compliance Evidence** and defines hardware-attested governance records for AI agents. The two projects use the same short name for different objects.

When citing or discussing this work, use the repository identity `markgoodbody-bit/TRACE` and the exact TRACE version so the intended project is clear.

## The problem

A person, institution, model, or controller may receive something like:

```text
AUTHORISE ACTION a*
reported_confidence = 0.93
time_to_commit = 4 s
```

That representation is actionable but structurally thin. It does not show:

- who supplied the instruction or confidence;
- what was observed, reported, inferred, disputed, or unavailable;
- which entities and scopes may be affected;
- which target categories were omitted or never searched;
- what action, delay, or inaction would close;
- whether correction can happen before harm or evidence hardens;
- who carries the burden and what residue remains afterward;
- where value choice, measurement, selection, authority, and enforcement enter.

TRACE attempts to differentiate that compressed input before selection. The external scene has not changed; the representation has.

## What TRACE represents

A TRACE reading can distinguish:

```text
world state / bounded scene / map
entity / state / signal / aperture
action / realised or projected transition
claims / provenance / uncertainty / dispute
coupling / control / constraint
clocks / irreversibility / future paths
routes / brakes / correction stages
burdens / residue / records / absences
designation / measure / selector / policy
receiver limits / omitted primitives / unresolved handoffs
target-set source / selection basis / known omissions / alternatives
```

The central discipline is separation. Examples include:

```text
WORLD_STATE != SCENE
SCENE != MAP
ACTION != TRANSITION
READING != CLEARANCE
MODEL != WORLD
UNKNOWN != ABSENT
TARGET_SET != WORLD_SCOPE
COVERAGE_OF_SELECTED_TARGETS != COMPLETE_DISCOVERY
BRAKE_ACTIVATION_RECORDED != TRANSITION_INTERRUPTED
TRANSITION_INTERRUPTED != HARM_PREVENTED
```

## Start here

### Five minutes

Read [`REVIEW_GUIDE.md`](REVIEW_GUIDE.md). It explains what TRACE claims, what it does not claim, and how to submit a useful finding.

### Exact formal source

Use [`TRACE_FORMAL_SEED_v0_2_7.md`](TRACE_FORMAL_SEED_v0_2_7.md) for exact wording, identifiers, equations, schema material, invariants, and formal review.

The Markdown file is the formal source. The PDF changes presentation, pagination, typography, and line wrapping only.

### Human-readable formal carrier

Read [`TRACE.pdf`](TRACE.pdf). It is the current rendered carrier of TRACE v0.2.7.

A useful first pass is:

1. **Handshake / Claim Ceiling**
2. **Middle-Out Seed**
3. **Canonical Object / Typed Graph**
4. the worked transformations
5. **Packet Construction** and the unresolved limits

### Release and provenance

- [`TRACE_v0_2_7_BASELINE_RELEASE.md`](TRACE_v0_2_7_BASELINE_RELEASE.md) records the human release decision, exact object identity, review history, and claim boundaries.
- [`TRACE_v0_2_7_RENDERED_CARRIER_REPORT.md`](TRACE_v0_2_7_RENDERED_CARRIER_REPORT.md) records source binding, deterministic build evidence, visual inspection, and carrier limits.
- [`falsification/TRACE_v0_2_7_FALSIFY_X100_REPORT.md`](falsification/TRACE_v0_2_7_FALSIFY_X100_REPORT.md) records the declared executable audit surface and residual limits.

The formal source retains the wording of the reviewed compiled candidate. Its active release status is recorded in the separate release declaration so promotion did not rewrite the reviewed bytes.

## Current status

TRACE v0.2.7 is the active released formal baseline to use, cite, test, and revise from unless a later version explicitly supersedes it.

```text
RELEASED
ACTIVE_FORMAL_BASELINE
NOT_CANON
NOT_VALIDATED
NOT_AUTHORITY
NOT_PERMISSION
NOT_CLEARANCE
```

The embedded minimum validator checks packet shape and controlled vocabulary. It cannot establish truth, semantic relevance, completeness, independent evidence, legitimate authority, route executability, brake effectiveness, correction, moral correctness, or world effect.

The current audits and build checks establish declared source binding, deterministic construction, surface propagation, mutation detection, and stated containment. They do not establish operational effectiveness or decision advantage.

## Current development candidate

TRACE v0.3.0 is under review in [draft PR
#38](https://github.com/markgoodbody-bit/TRACE/pull/38). It exposes two
different working objects:

- the [compact v0.11 spine](https://github.com/markgoodbody-bit/TRACE/blob/framework/trace-v0-3-0-working/PROJECT/TRACE_v0_3_0_SPINE_CANDIDATE_v0_11.md) for semantic review;
- the [full v0.1 candidate](https://github.com/markgoodbody-bit/TRACE/blob/framework/trace-v0-3-0-working/PROJECT/TRACE_FORMAL_SEED_v0_3_0_FULL_WORKING_CANDIDATE_v0_1.md) for donor-survival, schema, operator and worked-transformation review.

Read the [current readiness audit](https://github.com/markgoodbody-bit/TRACE/blob/framework/trace-v0-3-0-working/PROJECT/TRACE_v0_3_0_READINESS_AUDIT_20260829_v0_1.md) before treating either as a finished object. Neither supersedes v0.2.7.

The current comparison found no TRACE-unique semantic primitive. A 32-call
primary run established execution and material carrier burden, but no efficacy
result; blind adjudication remains incomplete. The live question is whether
TRACE's compilation prevents consequential omissions at acceptable total cost,
not whether its vocabulary is novel.

## Who may find it relevant

TRACE may be worth examining for people working on:

- AI safety, alignment, agent governance, and model evaluation;
- systems engineering, safety cases, incident reconstruction, and assurance;
- institutional decision processes, audit, law, regulation, and public administration;
- causal modelling, mechanistic interpretability, and human-machine handoffs;
- philosophy of action, uncertainty, responsibility, harm, and correction.

No domain endorsement is implied. The useful question is whether TRACE preserves materially relevant structure that existing methods lose, and whether that preservation changes anything in practice.

## What useful feedback looks like

General reactions are welcome, but concrete breaks are more valuable.

A strong finding identifies:

```text
exact file and section
what was directly observed
what is inferred
failure mode or consequence
why current safeguards do or do not contain it
smallest justified repair, removal, demotion, or test
```

Use the repository's **TRACE review feedback** issue template:

https://github.com/markgoodbody-bit/TRACE/issues/new?template=trace-review.md

A reviewer may reasonably conclude that a component is redundant, incoherent, untestable, better handled by an existing method, or useful only in a narrower setting.

## Citation

GitHub-compatible citation metadata is provided in [`CITATION.cff`](CITATION.cff). Cite the exact TRACE version and formal source used; citation does not imply validation, endorsement, authority, or permission to reuse the material.

## Repository map

- `TRACE_FORMAL_SEED_v0_2_7.md` — active formal source
- `TRACE.pdf` — current v0.2.7 rendered formal carrier; the Markdown seed remains the formal source
- `REVIEW_GUIDE.md` — external review paths and finding format
- `CITATION.cff` — machine-readable citation metadata
- `CONTRIBUTING.md` — contribution, provenance and review guidance
- `LICENSE_STATUS.md` — current no-general-reuse-licence boundary
- `TRACE_v0_2_7_BASELINE_RELEASE.md` — release decision and exact provenance
- `TRACE_v0_2_7_RENDERED_CARRIER_REPORT.md` — render and source-binding evidence
- `falsification/` — executable audits, reports, and residual limits
- `tools/` — deterministic compilation and carrier build tools
- `carrier/` — generated carrier source and build inputs
- `checker_external/` — checks that cannot be established by the embedded minimum validator
- `02_CURRENT_SURFACE/` — preserved transition and repair material
- `PROJECT/PROJECT.md` and `PROJECT/MAP.md` — project purpose and layer map

Released predecessors remain preserved as separate objects rather than silently rewritten.

## Related project

Mechanical Ethics is the human-facing ethical and philosophical side of the wider project. TRACE is the structure-facing language. They approach the same underlying problem from different directions, but this repository contains the TRACE formal lane.

## Review, contribution and reuse

Review, criticism and bounded testing are invited. Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before proposing a patch.

No general reuse licence has been granted. Public repository visibility alone should not be read as permission to copy, adapt, redistribute or incorporate the material elsewhere. See [`LICENSE_STATUS.md`](LICENSE_STATUS.md).
