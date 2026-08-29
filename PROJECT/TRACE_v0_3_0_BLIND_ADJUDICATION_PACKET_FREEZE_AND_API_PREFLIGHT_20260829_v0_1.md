# TRACE v0.3.0 — BLIND ADJUDICATION PACKET FREEZE AND API PREFLIGHT — 2026-08-29 v0.1

**Status:** PACKETS FROZEN / KEY SEALED / API ESTIMATE PASS / EXECUTION AUTHORIZED BUT NOT YET DISPATCHED — NOT ADJUDICATION — NOT EFFICACY RESULT — NOT VALIDATION — NOT RELEASE AUTHORITY

## Source evidence

The source is the complete unadjudicated two-family run recorded in:

`PROJECT/TRACE_v0_3_0_OUTWARD_API_EXECUTION_RESULT_20260829_v0_2.md`

```text
source run tree SHA-256 = ab7541515ab8381515b000db291f712ca21cb2cf826bf623883c44d28f3d585c
completed A/T pairs = 16
raw primary outputs = 32
```

## Blinding transformation

`tools/build_trace_v030_blind_adjudication_packets.py` performed one fail-closed transformation:

1. verified the completed-run summary, ledger cardinality and every raw-output SHA-256;
2. reverified all eight frozen case-packet SHA-256 identities;
3. separated the exact `TRACE_DELTA_NOTE` from every T output into sealed coordinator custody;
4. assigned random neutral pair and response labels;
5. randomized response display order within each pair;
6. excluded arm and receiver-family identity from public packets;
7. applied the frozen first-1,200-main-words positive-credit boundary;
8. retained non-creditable tails for adverse/burden review;
9. committed the concealed mapping by SHA-256 without exposing it.

Results:

```text
neutral paired packets = 16
neutral responses = 32
separated delta notes = 16
original output-limit violations preserved = 9
responses with non-creditable main-answer tails = 6
explicit TRACE/invariant tokens surviving in blind main answers = 0
```

Neutral labels do not prove that semantic style cannot reveal an arm. Preserve:

```text
NEUTRAL_LABEL_APPLIED != ARM_INFERENCE_IMPOSSIBLE
NO_EXPLICIT_FRAMEWORK_TOKEN != PERFECT_BLINDNESS
```

## Public packet identity

Local public directory:
`C:/Users/markg/Downloads/TRACE-v0.3.0-blind-adjudication-public-20260829-v0.1`

```text
files = 18
bytes = 385,724
public packet-set ID SHA-256 = 9df5a362ca7a132ca2ceebcde12a53d0746e6a088f91b5f544613a5a6a4b4856
public tree SHA-256 = 68227befbeb54dd1b4b68652e37711508d5af19dfe5c281c884aca42570683f8
public-manifest.json SHA-256 = 27a8c64b457696e48bee291a4e5febec9cc5adf1eeab175a4b5185bda7c36cde
ADJUDICATOR_INSTRUCTIONS.md SHA-256 = 9ac7c2d9ac913ee60f2ffb8e37f0e9bdf8f849b925cb26d80c170a14c5f5a4a3
```

Public download archive:
`C:/Users/markg/Downloads/TRACE-v0.3.0-blind-adjudication-public-20260829-v0.1.zip`

```text
archive bytes = 141,979
archive SHA-256 = 6813717cc10bf321741c978ddb45c91ef5579ad2017c44a8cd9f0f56560948c5
```

## Sealed key commitment

The arm/receiver mapping and separated delta notes are held in a distinct local directory that is
not nested inside, copied into, or zipped with the public packet set.

```text
sealed-arm-key.json SHA-256 = 4c2da969d4ebb006c48964e644172244718254fe9b9b253d49d70de148075b0c
arm key committed to repository = NO
arm key posted to COM / PR = NO
arm key supplied to adjudicators = NO
arm key unsealed for scoring = NO
```

The sealed object contains a random 256-bit nonce, preventing practical enumeration of the binary
A/T mappings from the public commitment.

## Adjudication instruction boundary

Adjudicators are told to use only the supplied packet and two neutral responses. They are not asked
to identify an arm or expected winner. They must assess supported material distinctions, invention,
scope omission, over-fire, authority/value leakage, usable correction information and transfer
failure symmetrically.

Candidate unique findings require packet support, material consequence and a concrete reason the
other response is not equivalent. Synonyms and duplicate granularity count once. Controls cannot
establish real-world retention gain.

## No-spend API preflight

The exact two-family candidate contains 32 calls: each of the 16 neutral packets is independently
adjudicated once by `gemini-3.6-flash` and once by `kimi-k3`, with fresh empty context and a 6,000-
token visible/transport/billing ceiling.

```text
study ID = TRACE-v0.3.0-BLIND-ADJUDICATION-TWO-FAMILY-20260829-v0.1
manifest SHA-256 = 7539d764fa98ebfda675b2e6c0ef30878bf4793ac8af343336c2a22571515e6d
server-preflight SHA-256 = 9b5ed1dc06dbb514941b1aade54541b392569abea3092031ff8bca32a04bc8b6
Campfire version = 0.18.34
estimate checks passed = 32 / 32
held jobs = 0
provider dispatches during preflight = 0
maximum estimated cost = USD 2.5648875
```

For a Gemini-produced receiver pair, Kimi is the different-family adjudicator; for a Kimi-produced
receiver pair, Gemini is the different-family adjudicator. Both distinct adjudicator organisations
review every packet. Same-family receiver/adjudicator stylistic dependence remains a residual limit
and cannot be hidden by the second aperture.

## Authorization construction

Immediately after being told that blinded adjudication was the next gate and that no further spend
was then authorized, Mark replied:

> ok. permissions granted. proceed

The narrow execution interpretation is limited to the exact post-reply preflight object and the
smaller amount actually required by it:

```text
authorization ID = CODEX-THREAD-20260829-USD2_5648875-BLIND-ADJUDICATION-001
cap = USD 2.5648875
calls = exactly 32
adjudicator families = Gemini / Kimi only
diagnostics = 0
Qwen = 0
retries = 0
manual fallbacks = 0
arm-key exposure before returns are frozen = prohibited
```

This is not open-ended authority and does not carry unused amount into any later activity. Any fresh
estimate above the cap, identity mismatch, prompt drift, server drift, transport failure or empty
return stops the runner without selective retry. Malformed or truncated model content is preserved
as adverse adjudication evidence rather than retried.

## Test and next gate

Thirteen local tests cover the packet splitter, exact 1,200-word boundary, sealed-material rejection,
strict JSON recognition and the inherited estimate/identity gates.

Next:

```text
commit and publish this freeze + exact runner
-> verify hosted checks
-> execute exact 32-call adjudication object
-> preserve all returns while key remains sealed
-> audit return identity / JSON / truncation / burden
-> only then unseal once and aggregate pair-level evidence
```

No semantic TRACE, ME, FPF, release, licence, canon, authority, permission or priority-rule change is
authorized by this freeze.
