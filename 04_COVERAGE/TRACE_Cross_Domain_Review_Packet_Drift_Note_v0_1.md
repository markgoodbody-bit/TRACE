# TRACE Cross-Domain Review Packet Drift Note v0.1

Status: instrument-drift note / external-review correction.  
Not: validation, canon promotion, theory expansion, or applied patch.

## 0. Trigger

External review responses to `TRACE_Cross_Domain_External_Review_Packet_v0_1` produced a material correction.

Qwen and Gemini found useful bridge-language coverage, while Z.ai and Claude identified native-mechanism loss risks. Claude's review made the strongest instrument-level objection:

```text
The review packet may be testing the wrong TRACE grammar.
```

## 1. Drift identified

The packet built from the recent coverage branch emphasised the kernel-style grammar:

```text
state -> transition -> constraint -> clock -> failure/hardening -> correction/control
```

That grammar is useful for timing, correction, and hardening cases.

But Claude reported that the repo's atlas/cross-domain machinery uses a stronger invariant-profile grammar:

```text
TRACE_form(D) := {S, T, C, O, K, B, I}
```

Expanded:

```text
S := state
T := transformation
C := composition
O := observation
K := constraint
B := boundary
I := invariant / measure
```

with:

```text
named native invariant
+ loss register
+ back-translation gate
```

## 2. Why this matters

The first external review packet asked reviewers whether TRACE preserved native meaning, but its condensed material omitted the tools designed to test that preservation:

```text
invariant / measure
loss register
back-translation gate
```

This contaminates review results.

A reviewer may correctly criticise the packet for generic clock/correction language even if the repo contains a more precise invariant/back-translation layer.

## 3. Correct interpretation of returned reviews

Treat the returned reviews as signals about the packet, not as final judgments about TRACE.

Current interpretation:

```text
Qwen := strong positive signal for bridge-language usefulness, especially disagreement location
Gemini := partial signal; useful clock grammar but native-mechanism loss in quantum/syntax risk
Z.ai := partial/negative signal; native constraints too generic
Claude := instrument-level correction; pack tests clock skeleton, not full atlas grammar
```

Result:

```text
TRACE_EXTERNAL_REVIEW_PACKET_V0_1_CONTAMINATED_BY_GRAMMAR_SUBSTITUTION
```

Not:

```text
TRACE_LANGUAGE_COVERAGE_VALIDATED
```

Not:

```text
TRACE_LANGUAGE_COVERAGE_FAILED
```

## 4. Required correction

Create a corrected external review pack that tests the invariant-profile / back-translation grammar directly.

Minimum corrected columns:

```text
native domain
native object
S state
T transformation
C composition
O observation
K constraint
B boundary
I invariant / measure
named native invariant or distinction
loss register
back-translation test
ethics/governance boundary where applicable
fail condition
```

The corrected review question should be:

```text
Can the reviewer recover the native distinction from the TRACE form?
```

If not, the translation fails or remains partial.

## 5. Status of the clock/correction grammar

Do not discard the clock/correction grammar.

It remains useful for:

```text
temporal power
correction gap
hardening
review delay
harm propagation
control lag
```

But it should not be treated as the only cross-domain language test.

Current split:

```text
clock/correction grammar := timing and control-failure bridge
invariant/back-translation grammar := native-structure preservation bridge
```

## 6. Next action

Build:

```text
TRACE_cross_domain_invariant_review_pack_v0_1.zip
```

and/or repo artifact:

```text
04_COVERAGE/TRACE_Cross_Domain_Invariant_Backtranslation_Review_Packet_v0_1.md
```

Status:

```text
corrected review instrument / not validation
```

## 7. Control note

This is a good failure.

It shows the review machinery can detect not only theory overclaim, but also test-instrument drift.

The lesson:

```text
Do not let a convenient compression silently replace the actual grammar under test.
```
