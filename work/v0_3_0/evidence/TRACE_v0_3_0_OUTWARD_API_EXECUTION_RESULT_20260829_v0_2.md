# TRACE v0.3.0 — OUTWARD API EXECUTION RESULT — 2026-08-29 v0.2

**Status:** COMPLETE / UNADJUDICATED — EXECUTED PROVIDER EVIDENCE — NOT AN EFFICACY RESULT — NOT VALIDATION — NOT RELEASE AUTHORITY

## Earned execution result

The bounded two-family run completed under authorization
`CODEX-THREAD-20260829-USD4-GEMINI-KIMI-002`.

```text
Gemini connection diagnostic = PASS
Kimi connection diagnostic = PASS
primary calls = 32 / 32
paired A/T units = 16 / 16 technically completed
HTTP failures = 0
truncated outputs = 0
reported-model drift = 0
retries = 0
manual fallbacks = 0
Qwen contacts = 0
run status = COMPLETE_UNADJUDICATED
```

The first primary response was recorded at `2026-08-29T16:54:26.502Z`; the last was recorded at
`2026-08-29T17:21:17.612Z`. The exact study manifest identity was
`5b2ea0e916409d9283991bee4e55d2ca5be5af7bea99c5801562aa5889ae1eab`.

This supersedes the transport state recorded in the preserved stopped-run result v0.1. It does not
rewrite that adverse predecessor or import its probe as evidence for this run.

## Diagnostic gate

Both diagnostics returned the exact marker, HTTP 200, the configured model identity, a complete
finish reason and no truncation:

| Provider | Model | Visible / transport / billing-ceiling tokens | Reserved ceiling |
|---|---|---:|---:|
| Google | `gemini-3.6-flash` | 128 / 384 / 384 | USD 0.003471 |
| Moonshot AI | `kimi-k3` | 128 / 768 / 768 | USD 0.011550 |

The diagnostic reserve is a ceiling, not an isolated provider charge.

## Spend and execution burden

Provider-reported primary accounting:

| Model | Calls | Input tokens | Billed output tokens | Thinking tokens reported separately | Provider time | Actual primary cost |
|---|---:|---:|---:|---:|---:|---:|
| `gemini-3.6-flash` | 16 | 65,534 | 54,255 | 34,332 | 361.642 s | USD 0.5052135 |
| `kimi-k3` | 16 | 61,856 | 36,293 | 0 | 1,269.975 s | USD 0.7299630 |
| **Total** | **32** | **127,390** | **90,548** | **34,332** | **1,631.617 s** | **USD 1.2351765** |

The runner's conservative authorization accounting adds the full USD 0.015021 diagnostic reserve:

```text
actual recorded primary exposure = USD 1.2351765
diagnostic ceiling reserve        = USD 0.0150210
completed-or-reserved exposure    = USD 1.2501975
authorized cap                    = USD 4.0000000
unused authorization              = USD 2.7498025
```

No unused authority was spent.

## Output-limit violations

Nine of 32 outputs exceeded the common `<=1200 words` instruction. All nine were Kimi outputs;
Gemini had zero violations. All were complete and untruncated.

| Job | Words |
|---|---:|
| `PAC-4__KIMI_MOONSHOT__T__ATTEMPT_1` | 1,330 |
| `PAC-4__KIMI_MOONSHOT__A__ATTEMPT_1` | 1,238 |
| `EPA-03__KIMI_MOONSHOT__A__ATTEMPT_1` | 1,363 |
| `PAC-1__KIMI_MOONSHOT__A__ATTEMPT_1` | 1,230 |
| `PAC-1__KIMI_MOONSHOT__T__ATTEMPT_1` | 1,258 |
| `PAC-5__KIMI_MOONSHOT__T__ATTEMPT_1` | 1,205 |
| `PAC-5__KIMI_MOONSHOT__A__ATTEMPT_1` | 1,243 |
| `CONTROL_STRESS_01__KIMI_MOONSHOT__A__ATTEMPT_1` | 1,504 |
| `CONTROL_STRESS_01__KIMI_MOONSHOT__T__ATTEMPT_1` | 1,304 |

Under the frozen v0.4 mechanics inherited by v0.5, the full outputs remain usability/burden
evidence. Any later positive material-gain assessment may use only the first 1,200 words of the
main answer. An over-limit tail cannot buy additional T-only gain opportunity.

## Deterministic primary byte burden

Using the predeclared measure
`UTF8_BYTES(receiver-visible input) + UTF8_BYTES(receiver-visible full output)`:

```text
total receiver-visible prompt bytes = 574,432
total receiver-visible output bytes = 232,780
total primary burden bytes           = 807,212
median T/A burden ratio, all pairs   = 2.798448
median T/A burden ratio, real cases  = 2.721406
minimum pair ratio                   = 2.4404
maximum pair ratio                   = 4.3700
```

Median secondary views:

```text
T/A visible-word ratio = 0.860095
T/A actual-cost ratio  = 1.345569
```

The compact carrier therefore imposed a large input/reading-volume burden even though T usually
returned fewer visible words. This is an earned carrier/compression pressure. It is not cognitive-
cost truth and, without blinded distinction scoring, is not an efficacy disposition.

## Evidence identity

Run directory:
`C:/Users/markg/Downloads/TRACE-v0.3.0-primary-api-run-20260829-v0.3-two-family`

```text
files = 67
bytes = 568,786
tree algorithm = SHA256(UTF8(sorted(relative_path<TAB>bytes<TAB>sha256)+LF))
tree SHA-256 = ab7541515ab8381515b000db291f712ca21cb2cf826bf623883c44d28f3d585c

authorization-and-plan.json
  cd4fa0f754f75fa625ec0c9e414a5135259e381f05fa960fdd294731fe35ac77
ledger.jsonl
  6ffd2d4882e91bc4b164fe21c89c0626a8100bbdda9bd3ba27a507be3788d1a6
run-summary.json
  9172abdfc4b092f717ef29e7e307b804fd2aefb1a5ab7cf42641e1dd72d19fae
```

Download archive:
`C:/Users/markg/Downloads/TRACE-v0.3.0-primary-api-run-COMPLETE-UNADJUDICATED-20260829-v0.2.zip`

```text
archive bytes = 186,497
archive SHA-256 = 7487266414e1b5d80cd50b7e0674ee827e318d3eb46d502761fcef51c6e50a26
```

## Claim boundary

Directly established:

- the exact two-family execution path completed;
- the 16 paired units passed the recorded technical transport/runtime checks;
- the outputs, metadata, accounting evidence and adverse limit violations are preserved;
- compact-carrier primary byte burden exceeded 1.5x in every pair and had a 2.798448 median;
- Kimi showed a material instruction-following problem on the word envelope.

Not established:

- any supported T-only distinction;
- baseline capture of T;
- negative-control over-fire;
- authority/value leakage or unsupported-confidence deltas;
- reproduction across cases or families;
- any v0.5 placement/expansion disposition;
- practical advantage over ordinary analysis or an established domain method;
- validation, canon, release, authority, permission or clearance.

## Next gate

Freeze neutral labels and blinded main-output packets, separating each T `TRACE_DELTA_NOTE` before
adjudication. Then obtain the protocol-required two distinct adjudicator families for any positive
gain. Preserve A-only gains, disagreements, UNKNOWNs, false confidence, over-fire and adjudication
burden.

Until that gate completes:

```text
EXECUTED != ADJUDICATED
LOWER_VISIBLE_WORDS != LOWER_PRIMARY_BURDEN
PAIR_COMPLETED != TRACE_ADVANTAGE
COMPLETE_UNADJUDICATED != EFFICACY_RESULT
```
