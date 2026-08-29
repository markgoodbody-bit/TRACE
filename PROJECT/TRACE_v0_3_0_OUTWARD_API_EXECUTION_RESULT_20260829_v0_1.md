# TRACE v0.3.0 — OUTWARD API EXECUTION RESULT — 2026-08-29 v0.1

**Status:** STOPPED AT CONNECTION GATE — ADVERSE TRANSPORT RESULT PRESERVED — ZERO PRIMARY CALLS

## Earned result

The bounded runner began under authorization
`CODEX-THREAD-20260829-USD4-GEMINI-KIMI-001`. It aligned the local Gemini configuration from
`gemini-3.5-flash` to the manifest-bound `gemini-3.6-flash` without a provider call, then attempted
the first paid connection diagnostic.

Google returned a provider response reporting `gemini-3.6-flash`. The response ended with
`MAX_TOKENS`, was marked `truncated: true`, and did not contain the required
`CAMPFIRE_CONNECTION_OK` marker. Campfire therefore returned
`DIAGNOSTIC_MARKER_MISMATCH`, and the runner stopped as required.

```text
Gemini connection diagnostics attempted by this run = 1
Kimi connection diagnostics attempted by this run = 0
Qwen contacts by this run = 0
primary TRACE study calls = 0 / 32
retries = 0
manual fallbacks = 0
```

This is an adverse transport/probe result. It is not a TRACE efficacy result and supplies no basis
for changing the TRACE semantic candidate.

## What the evidence does and does not establish

Directly established:

- the credential and endpoint reached a Google provider response;
- the provider reported the exact requested model, `gemini-3.6-flash`;
- the connection probe used 128 visible, transport, and billing-ceiling tokens;
- the response exhausted that transport allowance before emitting the required marker;
- the fail-stop prevented every primary study dispatch.

Not established:

- that the Gemini credential is invalid;
- that 384 tokens, or any other untested allowance, will make the probe pass;
- that Gemini or Kimi can complete the frozen primary packets;
- that TRACE improves, harms, or has no effect on any receiver;
- that the separate earlier Kimi connection verification belongs to this authorized run.

The narrow engineering inference is that 128 transport tokens were insufficient for this exact
Gemini diagnostic response path. That inference supports testing a larger bounded probe allowance;
it does not support treating a future pass as guaranteed.

## Accounting boundary and correction record

The immutable stopped-run summary reports `connectionReserveUsd: 0.012525`, the full planned reserve
for both preliminary probes. Only the Gemini probe was attempted. Its pre-dispatch ceiling was
`0.000975 USD`; the unattempted Kimi ceiling was `0.01155 USD`.

Therefore:

```text
0.012525 USD = full two-probe planned reserve
0.000975 USD = attempted Gemini probe ceiling
provider actual charge = not isolated by the safe public API
```

Campfire recorded the incomplete provider response in its diagnostic-spend ledger. Its safe public
budget endpoint showed complete aggregate 24-hour recorded spend of
`0.0029788017076402182 GBP` at `2026-08-29T13:00:56.319Z`, but that aggregate also covers other
activity and cannot be attributed wholly to this run.

The runner is patched prospectively to distinguish attempted connection reserve from full planned
connection reserve. The original run artifacts are not rewritten.

## Separate pre-existing connection state

After the stop, the safe public connection endpoint showed a Kimi K3 verification timestamped
`2026-08-29T12:39:37.182Z`, before this runner began, with provider-reported model `kimi-k3` and a
complete marker-bearing response. It is useful configuration evidence but is not silently imported
as the second authorized preliminary test.

The same endpoint showed a pre-existing Qwen `HTTP_401` at `2026-08-29T12:38:05.086Z`. Qwen was
excluded from this study and was not contacted by this runner.

## Frozen run artifacts

Directory:
`C:/Users/markg/Downloads/TRACE-v0.3.0-primary-api-run-20260829-v0.2-two-family`

```text
authorization-and-plan.json
  c9609d3c6791b8cf546b8df1d79642c420f8b1ecbec678e264a69bfd471a904d
ledger.jsonl
  5c5d9a48196cac0d3b136e80185764aba12bfbe9cfdbe2f80e21fced97b35d4c
run-summary.json
  18be78966d3f49f54c179de3e2cea7faf680547c1a21782def0fa75d6ca84f2a
```

The empty `raw/` and `responses/` directories are consistent with zero primary dispatches.

## Next gate

No retry is authorized by the recorded scope. A later attempt requires all of the following:

1. a reviewed, non-paid Campfire change giving `gemini-3.6-flash` evidence-scoped diagnostic
   headroom;
2. deployment of that change to the active local server;
3. a fresh price/cap preflight, because the diagnostic ceiling will change;
4. explicit new authority for any further paid Gemini diagnostic or primary dispatch.

Until then the study remains stopped, not incomplete-by-omission and not failed TRACE evidence.
