# Contributing to TRACE

TRACE is currently a small, human-authority research project. The most useful external contribution is usually a precise finding, failed transfer, counterexample, comparison, or bounded test rather than a broad rewrite.

Start with [`REVIEW_GUIDE.md`](REVIEW_GUIDE.md) and use the **TRACE review feedback** issue template where possible.

## Before opening a pull request

Open an issue first unless the change is an obvious typo or broken link. State:

- the exact file, version and section affected;
- what was directly observed;
- what is inferred;
- the failure mode or consequence;
- the smallest justified repair, removal, demotion or test;
- whether the proposal changes presentation, tooling, serialization, vocabulary, schema, semantics or release status.

Do not treat a completed template, passing test or model agreement as validation.

## Pull-request boundary

A pull request should:

- have one declared purpose;
- preserve exact provenance for copied or transformed material;
- keep formal-source changes separate from rendered-carrier, tooling and public-documentation changes;
- include tests or reconstruction evidence where the change is executable;
- preserve disagreement, failed attempts and unresolved limits rather than silently deleting them;
- state any effect on compatibility, claim ceilings and released objects;
- avoid introducing authority, permission, clearance or value choice through apparently structural language.

Changes to the released formal source require explicit versioning and human release authority. Do not edit an existing released object in place and continue calling it the same release.

## AI-assisted work

AI-assisted findings and patches are welcome as evidence, not as authority. Disclose substantial AI assistance, including the system or model used when known, what material it received, and what a human checked. Do not present model agreement as independent validation.

Do not submit private chain-of-thought, confidential material, credentials, personal data, or content you do not have the right to contribute.

## Licensing and acceptance

The repository does not currently specify a reuse licence. Public visibility, review, discussion and issue submission do not grant permission to copy, adapt, redistribute or incorporate TRACE material elsewhere.

Until contribution and licensing terms are formalized, external pull requests may be reviewed but are not guaranteed acceptance. By submitting material, you must have the right to submit it; acceptance does not by itself create a general licence for the repository or its contents.

See [`LICENSE_STATUS.md`](LICENSE_STATUS.md) for the current boundary.
