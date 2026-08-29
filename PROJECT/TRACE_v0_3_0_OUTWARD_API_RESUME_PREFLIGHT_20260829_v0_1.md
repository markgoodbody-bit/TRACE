# TRACE v0.3.0 — OUTWARD API RESUME PREFLIGHT — 2026-08-29 v0.1

**Status:** NO-SPEND PREFLIGHT COMPLETE — EXECUTION DISABLED PENDING NEW AUTHORIZATION AND ACTIVE-SERVER REPLACEMENT

## Earned result

Campfire Relay v0.18.34 was built from exact source commit
`8ae012b7873e39ab33a1b337f90ae303c270eacd`, passed its dedicated hosted release gate, was sealed as
an exact 360-file package, merged, and published under immutable tag
`campfire-production-v0.18.34`.

Package SHA-256:
`faa056c0a1c4b221412658398ef3038873c0a224a1d504e66edc5914c04b5f15`.

Content-manifest SHA-256:
`b9c8fe0ea0701605b562b5d50fd0faecd5c234b644e18b79f13e4520a5df7b52`.

The extracted local package passed the pinned release verifier:

```text
version = 0.18.34
fileCount = 360
exactPathSet = true
allFileHashesMatched = true
symlinksRefused = true
treeSha256 = d647c0a32ad3a3d47bdfcfe00a45b8d14609a81dd1899d67aa5044e9509d103a
```

A temporary no-spend instance on loopback port 4318, using the existing configuration path without
exposing credentials and an isolated data directory, returned:

```text
server version = 0.18.34
Gemini configured model = gemini-3.6-flash
Gemini visible-answer tokens = 128
Gemini transport tokens = 384
Gemini billing-ceiling tokens = 384
Gemini maximum diagnostic estimate = 0.003471 USD
configured API connectors = 3
provider calls = 0
```

This verifies the repaired software path and effective server preflight. It does not verify that a
live Gemini diagnostic will pass.

## Corrected aggregate ceiling

The prospective TRACE runner now consumes Campfire's effective diagnostic preflight rather than
recalculating connection cost from catalogue presets. This matters because the active Gemini price
is an operator override of 9 USD per million output tokens, while the catalogue preset previously
used by the runner carried a different rate.

The exact no-spend plan is:

```text
Gemini diagnostic ceiling = 0.003471 USD
Kimi diagnostic ceiling = 0.011550 USD
two-probe reserve = 0.015021 USD
32-call primary ceiling = 3.2027535 USD
aggregate ceiling = 3.2177745 USD
margin below a 4.00 USD cap = 0.7822255 USD
Qwen calls = 0
retries = 0
manual fallbacks = 0
```

The runner is explicitly execution-disabled and labels its authorization
`PENDING_NEW_AUTHORIZATION`. The stopped authorization
`CODEX-THREAD-20260829-USD4-GEMINI-KIMI-001` cannot be reused.

## Remaining operational blocker

The v0.18.33 process on port 4317 is running with rights unavailable to the current Codex process.
The host refused termination with `Access is denied`. No replacement or concurrent shared-ledger
server was forced.

The extracted v0.18.34 package is ready at:
`C:/Users/markg/Downloads/CAMPFIRE_RELAY_v0_18_34`.

The operator must close the existing Campfire Relay server/PowerShell window. Codex can then start
v0.18.34 hidden on port 4317, verify public health and Money Guard state, and only afterward bind a
new paid authorization.

## Proposed new authorization text

After v0.18.34 is active on port 4317, the narrow authority required is:

> Authorize up to USD 4 total for one Gemini 3.6 connection diagnostic with a current server-owned
> ceiling of USD 0.003471, followed only if it passes by one Kimi K3 connection diagnostic with a
> current ceiling of USD 0.01155 and the exact 32-call Gemini/Kimi TRACE study with a current primary
> ceiling of USD 3.2027535; aggregate ceiling USD 3.2177745; no Qwen, retries, or manual fallbacks.

Fresh preflight values must still match immediately before execution. The authorization is a cap,
not an instruction to spend it and not a provider billing guarantee.
