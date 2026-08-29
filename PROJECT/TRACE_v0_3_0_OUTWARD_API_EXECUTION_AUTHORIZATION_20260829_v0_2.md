# TRACE v0.3.0 — OUTWARD API EXECUTION AUTHORIZATION — 2026-08-29 v0.2

**Status:** HUMAN AUTHORIZATION RECORD — BOUNDED EXECUTION ONLY — NOT EFFICACY RESULT

## Authorization event

Immediately after Codex presented the exact proposal below, Mark replied `authorized`.

> Authorize up to USD 4 total for one Gemini 3.6 diagnostic, then only if it passes one Kimi K3
> diagnostic, then only if both pass the exact 32-call Gemini/Kimi TRACE study; no Qwen, retries, or
> manual fallbacks.

Authorization identity:
`CODEX-THREAD-20260829-USD4-GEMINI-KIMI-002`.

The prior authorization
`CODEX-THREAD-20260829-USD4-GEMINI-KIMI-001` stopped at its first connection gate and cannot be
reused.

## Exact current ceiling

The active Campfire v0.18.34 production preflight immediately before this record returned:

```text
Gemini 3.6 diagnostic = 0.003471 USD maximum
Kimi K3 diagnostic = 0.011550 USD maximum
two-probe reserve = 0.015021 USD maximum
32 primary calls = 3.2027535 USD maximum
aggregate = 3.2177745 USD maximum
authorized cap = 4.0000000 USD
remaining ceiling margin = 0.7822255 USD
```

The cap is not an instruction to spend it and not a guarantee of provider billing.

## Control

1. Gemini diagnostic runs first.
2. Any Gemini diagnostic failure stops before Kimi and before all primary calls.
3. Kimi diagnostic runs only after Gemini passes.
4. Any Kimi diagnostic failure stops before all primary calls.
5. The exact 32-call study runs only after both diagnostics pass.
6. Any primary HTTP or terminal failure stops the run.
7. Qwen, retry routes and manual-fallback routes remain structurally excluded.
8. Fresh effective server estimates and Money Guard fingerprints remain required.
9. Raw results, failures, truncation and null/adverse findings are preserved.

This authorizes bounded transport execution. It supplies no authority to validate TRACE, alter
Mechanical Ethics, contact FPF maintainers, merge a candidate, or hide an adverse result.
