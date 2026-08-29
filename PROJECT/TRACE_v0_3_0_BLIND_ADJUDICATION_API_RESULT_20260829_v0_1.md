# TRACE v0.3.0 — BLIND ADJUDICATION API RESULT — 2026-08-29 v0.1

**Status:** STOPPED AT SERVER WATCHDOG — ADVERSE TRANSPORT RESULT PRESERVED — KEY STILL SEALED — NOT ADJUDICATION COMPLETION — NOT EFFICACY RESULT

## Earned result

The exact two-family blind-adjudication run began under authorization
`CODEX-THREAD-20260829-USD2_5648875-BLIND-ADJUDICATION-001`.

```text
planned calls = 32
authorized calls = 2
completed calls = 1
server-watchdog timeouts = 1
unattempted calls = 30
retries = 0
manual fallbacks = 0
Qwen contacts = 0
arm key unsealed = NO
```

Call 1, Gemini on neutral packet `PAIR-09F86168CA`, returned HTTP 200, reported
`gemini-3.6-flash`, finished `STOP`, and was not truncated. It wrapped its JSON object in a Markdown
code fence despite the strict bare-JSON instruction. The enclosed object is parseable after removal
of that single presentation wrapper; the strict-format violation remains evidence and is not retried.

Call 2, Kimi K3 on the same neutral packet, reached Campfire's 180-second watchdog. Campfire's
persisted session state records:

```text
status = timed_out
attempts = 1
duration = 180,003 ms
abort reason = server_watchdog_timeout
provider response received = false
actual cost = unknown
unconfirmed cost ceiling = USD 0.104823
```

The runner's own 180-second client wait expired at the same boundary, so it failed closed before it
could write its ordinary terminal summary. A read-only retrieval of the already-persisted Campfire
session supplied `server-timeout-witness.json`; no call route was invoked and no provider retry was
created. `run-summary.json` records the recovered boundary explicitly rather than pretending the
runner received a provider result.

## Accounting boundary

```text
Gemini actual recorded exposure = USD 0.0352755
Kimi unconfirmed timeout ceiling = USD 0.1048230
completed-or-reserved exposure   = USD 0.1400985
unspent authorization            = USD 2.4247890
```

The Kimi amount is a conservative unconfirmed ceiling, not an observed charge. Unspent authority is
not carried into a new attempt automatically.

## Frozen stopped-run identity

Directory:
`C:/Users/markg/Downloads/TRACE-v0.3.0-blind-adjudication-run-20260829-v0.1-two-family`

```text
files = 6
bytes = 18,865
tree SHA-256 = 57ab473511aea3d6fa47da97dd8fbf6cc5fb85ef2c951cb311a2c1a72f8b5627
run-summary.json SHA-256 = a98c907373d49d92c4ab9db4c326a89a398a42a2f8694d69d17843bb6f084ded
server-timeout-witness.json SHA-256 = 5444bb964895b2a2ef50569cb701ec52d5a15c4f68223e69aa15d25b6ffa986f
```

Download archive:
`C:/Users/markg/Downloads/TRACE-v0.3.0-blind-adjudication-run-STOPPED-20260829-v0.1.zip`

```text
archive bytes = 7,833
archive SHA-256 = cf05efff07eab7b769ca6b60caa2320b6590c46d46d00df9178cd4a5bca86f43
```

## What this does and does not establish

Established:

- the public blind packet reached Gemini without arm-key exposure;
- one Gemini adjudicator return exists and must be preserved;
- the Kimi K3 standard-profile adjudication path did not return within the server watchdog;
- the exact run stopped without retrying or dispatching the remaining 30 calls.

Not established:

- that the Kimi provider produced no billable work;
- that another Kimi profile or a smaller judge envelope will pass;
- two-family confirmation of any candidate gain;
- aggregate baseline capture, reproduction, over-fire disposition or placement;
- any TRACE efficacy, validation, release or canon result.

## Narrow prospective repair candidate

Estimate-only inspection shows that Campfire's explicit `debate-judging` mode changes the Kimi
request-control identity. A `kimi-k2.6` preset in that mode carries documented thinking suppression
and a lower 4,000-token ceiling; for the witnessed packet its no-spend estimate is USD 0.02069395.
Gemini's matching 4,000-token judge estimate is USD 0.0374115.

This is a prospective transport/latency repair candidate only. It must become a new exact manifest,
preflight, authorization and adjudication attempt. It cannot rewrite or selectively retry this
stopped attempt. If run, both adjudicator families must start again on all 16 neutral packets under
the same new frozen attempt object.
