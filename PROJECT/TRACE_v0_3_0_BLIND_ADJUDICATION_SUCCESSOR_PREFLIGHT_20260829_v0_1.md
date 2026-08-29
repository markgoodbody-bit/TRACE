# TRACE v0.3.0 — BLIND ADJUDICATION SUCCESSOR PREFLIGHT — 2026-08-29 v0.1

**Status:** WHOLE-STUDY SUCCESSOR FROZEN / ESTIMATE PASS / AUTHORIZED BUT NOT YET DISPATCHED — NOT RETRY OF STOPPED CALL — NOT ADJUDICATION — NOT EFFICACY RESULT

## Trigger

Blind-adjudication attempt 1 stopped after one complete Gemini return and one Kimi K3 server-
watchdog timeout. The adverse record is preserved in:

`PROJECT/TRACE_v0_3_0_BLIND_ADJUDICATION_API_RESULT_20260829_v0_1.md`

The sealed A/T key remains unopened. No semantic scoring occurred.

## Smallest whole-study transport repair

This successor does not selectively rerun the timed-out call. It starts a new adjudication attempt
for all 16 neutral packets and both adjudicator families.

Exact execution changes from stopped attempt 1:

```text
Kimi preset: kimi-k3 -> kimi-k2.6
execution mode: independent -> debate-judging
Kimi judge control: always-thinking/high -> documented thinking-disabled K2.6 path
visible / transport / billing ceiling: 6,000 -> 4,000 tokens
provider order per packet: Gemini then Kimi -> Kimi then Gemini
client wait: 180 -> 195 seconds, beyond Campfire's 180-second watchdog
```

Unchanged:

```text
public neutral packet-set identity
sealed arm-key commitment
adjudication instructions and JSON schema
32-call whole-study cardinality
fresh empty context
Gemini 3.6 Flash second adjudicator family
no Qwen / retry / manual fallback
```

Kimi-first ordering is a fail-fast cost control. It does not alter packet content or give either
adjudicator another adjudicator's return.

## Exact identities and no-spend preflight

```text
study ID = TRACE-v0.3.0-BLIND-ADJUDICATION-TWO-FAMILY-20260829-v0.3
public packet-set SHA-256 = 9df5a362ca7a132ca2ceebcde12a53d0746e6a088f91b5f544613a5a6a4b4856
sealed arm-key SHA-256 = 4c2da969d4ebb006c48964e644172244718254fe9b9b253d49d70de148075b0c
manifest SHA-256 = ebff790ea5b717ec372138c4c7d07c0afdfef899bf4a671947040f212d18b8bf
server-preflight SHA-256 = a697f29313f9b170d7135c08342fe6854d6e344476ca6ef0d8d197eb83e63524
Campfire version = 0.18.34
estimate checks passed = 32 / 32
held jobs = 0
provider calls during preflight = 0
maximum estimated cost = USD 0.95643875
```

The K2.6 thinking-disabled judge control is documented by the connector but remains live-unverified
for this exact workload. Therefore the first paid call is Kimi on one neutral packet. If it fails,
the entire successor stops before a Gemini call. A pass is transport evidence only.

## Narrow authority

Mark's instruction remains:

> ok. permissions granted. proceed

After the first attempt's fail-stop, that instruction is applied only to the smallest justified
whole-study successor now bounded by an exact no-spend estimate:

```text
authorization ID = CODEX-THREAD-20260829-USD0_95643875-BLIND-ADJUDICATION-002
cap = USD 0.95643875
calls = exactly 32, Kimi K2.6 + Gemini 3.6 Flash
diagnostics = 0
Qwen = 0
retries = 0
manual fallbacks = 0
arm-key exposure before all returns freeze = prohibited
carry-forward after this attempt = none
```

Attempt 1's USD 0.1400985 actual-or-reserved exposure remains separately preserved. It is not
hidden inside this successor cap.

Any fresh estimate above the cap, prompt/key/server/model drift, transport failure or empty return
stops this attempt without selective retry. Malformed or truncated model content is preserved as
adverse evidence and does not trigger a rerun.

## Test boundary

Thirteen local tests pass after the prospective runner repair. The repaired client can outwait and
capture Campfire's own watchdog response; if the client itself still reaches 195 seconds, it writes
an explicit failure event and terminal summary before stopping.

```text
WHOLE_STUDY_RESTART != SELECTIVE_RETRY
LOWER_LATENCY_PROFILE != GUARANTEED_RETURN
ADJUDICATION_RETURN != CONFIRMED_GAIN
```

No TRACE semantic object, ME object, FPF object, release, licence, canon, authority or priority rule
is modified by this successor.
