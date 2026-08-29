# TRACE v0.3.0 — CAMPFIRE v0.18.34 PRODUCTION ACTIVATION WITNESS — 2026-08-29

**Status:** ACTIVE / NO INFERENCE DISPATCH / EXECUTION AUTHORITY STILL ABSENT

## State transition

After the operator closed the elevated Campfire v0.18.33 server, port 4317 was observed free.
Codex started the previously hash-verified v0.18.34 package against the existing persistent state,
workspace and TRACE-module paths.

```text
health name = Campfire Relay
health version = 0.18.34
health ok = true
listener pid = 35664
observed at = 2026-08-29T16:51:26.4565982Z
```

Release provenance supplied to the process:

```text
source commit = 8ae012b7873e39ab33a1b337f90ae303c270eacd
source tree = f5fb4b37843ff489a23a51294ff5a0835dca12b8
package SHA-256 = faa056c0a1c4b221412658398ef3038873c0a224a1d504e66edc5914c04b5f15
```

## No-spend production preflight

The public production preflight returned:

```text
configured API connectors = 3
Gemini model = gemini-3.6-flash
Gemini visible / transport / billing tokens = 128 / 384 / 384
Gemini maximum diagnostic estimate = 0.003471 USD
Kimi model = kimi-k3
Kimi visible / transport / billing tokens = 128 / 768 / 768
Kimi maximum diagnostic estimate = 0.011550 USD
rolling 24-hour spend history complete = true
recorded 24-hour spend = 0.0029788017076402182 GBP
```

Persisted connection history was preserved rather than rewritten:

```text
Gemini = TEST FAILED at 2026-08-29T12:57:00.462Z
Kimi = API VERIFIED at 2026-08-29T12:39:37.182Z
Qwen = TEST FAILED at 2026-08-29T12:38:05.086Z
```

The health, connection, diagnostic-preflight and budget-cost reads made no model-inference call. A
subsequent Framework-status read performed one live Kimi balance lookup and reported 13.99359 USD;
that was a non-inference account read, not a model dispatch or study result.

## Remaining gate

The TRACE runner remains deliberately disabled for `--execute` and labels authority
`PENDING_NEW_AUTHORIZATION`. The prior stopped authorization cannot be reused.

The exact current maximum plan remains:

```text
two diagnostic probes = 0.015021 USD
32 primary calls = 3.2027535 USD
aggregate = 3.2177745 USD
proposed cap = 4.00 USD
Qwen / retry / manual fallback = 0 / 0 / 0
```

Activation is software readiness evidence only. It is not a connection-test pass, TRACE efficacy
evidence, validation, or permission to spend.
