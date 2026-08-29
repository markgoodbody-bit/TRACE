# TRACE v0.3.0 — primary prompt build record — 2026-08-29 v0.1

**Status:** DETERMINISTIC PROMPT-IDENTITY BUILD PASS — NO DISPATCH — NO RECEIVER OUTPUT — NOT VALIDATION

## Result

The frozen primary prompt contract now has an executable, no-network builder:

```text
tools/build_trace_v030_primary_prompts.py
```

It constructs 16 unique canonical prompts in memory:

```text
8 packet objects x 2 arms = 16 unique prompt byte strings
16 prompt objects x 3 receiver families = 48 maximum manual dispatches
24 A/T pairs
```

The prompt bytes are family-independent. Receiver family, pair attempt and
deterministic arm order remain dispatch/evidence metadata rather than text
inserted into the receiver-visible prompt.

Committed identity manifest:

```text
PROJECT/TRACE_v0_3_0_OUTWARD_PRIMARY_PROMPT_MANIFEST_v0_1.json
bytes:      13,712
SHA-256:    6e282ae69d08b9e73f8b41b9af59e988738d0dc0adcbe11c2315995931fbfc8f
Git blob:   4939ecdf681caaca87bd62f9701513308a2547ba
status:     PASS
```

The Git blob is the pre-commit object identity observed in the working tree and
must be reacquired after commit rather than treated as an enduring branch-head
identity.

## Verified inputs

The builder fails closed unless all of these reproduce their frozen byte
length, Git blob SHA-1 and SHA-256:

- compact spine v0.11;
- six selected real packets;
- low-complexity negative control;
- synthetic stress control.

It also verifies that:

- the exact A and T instruction strings occur once in the frozen assembly
  contract;
- all 24 computed order hashes/orders match the frozen dispatch-plan table;
- canonical input is UTF-8 without BOM and LF-only;
- committed manifest content equals deterministic regenerated content.

No prompt body has been committed because the 16 bodies are deterministic
products of already committed inputs. They can be emitted to a separate
directory only by an explicit `--emit-dir` invocation.

## First failure preserved

The first Windows run failed because Git checkout had converted packet LF line
endings to CRLF:

```text
frozen RAIB-2 bytes:  4,135
checkout bytes:       4,166
frozen blob/SHA:      mismatch before recovery
```

This exposed a real transport risk: copying packet text directly from a Windows
working tree would not reproduce the frozen prompt bytes.

The repair permits CRLF-to-LF recovery only when:

1. every carriage return belongs to a CRLF pair;
2. normalization reproduces the exact frozen byte length;
3. the exact frozen Git blob SHA-1 is reproduced; and
4. the exact frozen SHA-256 is reproduced.

Otherwise the build fails. This is canonical-byte recovery, not silent content
normalization.

## Claim boundary

```text
PROMPT BUILD PASS != DISPATCH
PROMPT IDENTITY != CLIPBOARD ROUND-TRIP
CLIPBOARD ROUND-TRIP != PROVIDER INTERNAL BYTES
RECEIVER CONTACT != VALID PAIR
VALID PAIR != TRACE GAIN
```

No provider was contacted. No clipboard was changed. No model output, runtime
identity, efficacy result, cost result or validation evidence was produced.

## Next gate

Before first manual dispatch:

1. reacquire the live PR #38 state and rerun the builder check;
2. confirm the receiver family's actual current runtime/model label;
3. emit or copy only the exact prompt selected for that pair/arm;
4. verify clipboard round-trip identity against the manifest SHA-256;
5. use a fresh separate context with no paired-output exposure;
6. preserve raw return, witnessed identity, timestamps, word count and any
   transport deviation.

Dispatch and any provider cost remain separate human-authorized actions.
