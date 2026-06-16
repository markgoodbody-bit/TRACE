# TRACE / ME Concordance v0.7 — Subtraction First

Date: 2026-06-16  
Status: subtraction patch after Claude Opus repo audit. Not validation. Not proof.

## Why v0.7 exists

v0.6 mapped many TRACE operators to established counterparts, but it still tended to manufacture a remainder for almost every row. That contradicts C16:

```trace
C16 :=
  TRACE_remainder_is_narrow:
    clocked
    + conjunctive_correction_before_hardening
    + power_or_trigger_dependence
```

v0.7 reverses the default.

```trace
remainder_default := none

remainder_allowed_only_if:
  named_prior_art_counterpart
  + specific_TRACE_delta
  + demoter
  + not_just_new_words
```

## Concordance Rule

A row does not earn a TRACE remainder because it is useful, elegant, morally important, or clear. It earns a remainder only if TRACE adds a distinct operational constraint not already carried by the comparator.

## Subtraction Table

| TRACE item | Established counterpart | TRACE remainder | Status after subtraction | Demoter |
|---|---|---|---|---|
| Model != measurement | scientific modelling; statistics; measurement theory | none | known boundary | Demote if used as novelty claim. |
| Compression != proof | epistemology; formal methods; model validation | none | known boundary | Demote if elegant notation is treated as evidence. |
| Structure != causation | causal inference; systems theory | none | known boundary | Demote if structure map is treated as causal proof. |
| World / state x_t | control theory; dynamical systems | none | support vocabulary | Demote if it adds only notation. |
| Observation / Witness | incident response; audit; safety engineering | none by itself | K-gate component | Remainder only emerges in conjunctive gate. |
| Record / trusted memory | audit trail; provenance; evidence law | none by itself | K-gate component | Demote if separate headline operator. |
| Authority / access | governance; administrative law; incident command | none by itself | K-gate component | Remainder only emerges in linkage/timing. |
| Time before hardening | golden hour; abort criteria; time-critical safety | partial | active spine | Keep only as correction-before-hardening condition. |
| Enforcement / consequence carrier | enforcement theory; safety assurance; governance | none by itself | K-gate component | Remainder only if linked to time/repair. |
| Repair capacity | restorative justice; remediation; incident recovery | none by itself | K-gate component | Keep as future-space repair support only. |
| K-Gate | Swiss Cheese; STAMP; HRO; incident response | yes, narrowly: conjunctive correction capacity under time pressure | active spine | Demote if it only says failure failed after the fact. |
| Correction Before Hardening | time-critical intervention; mission abort; golden hour | yes: explicitly ethical timing condition for repair/correction | active spine | Demote if clocks cannot be defined prospectively. |
| τ_correct < τ_harden | reliability / safety timing thresholds | yes, as compact live/late correction boundary | active spine | Demote if used without clock definitions. |
| P_trigger / correction dependence | capture theory; independence; conflict of interest | possible | hypothesis-ready | Demote if no measurable spread or no interaction. |
| H_immediacy | hazard immediacy; safety criticality | possible | hypothesis-ready | Demote if not predictive with P_trigger. |
| Method Floor | deontology; due process; human-rights floors | none as novelty | guard | Keep as guard, not remainder. |
| Method Laundering | legitimacy theory; procedural justice; administrative burden | partial as diagnostic phrase | support | Demote if every procedural dispute becomes laundering. |
| Exit Route | sanctuary; civil disobedience; whistleblower protection; safety planning | partial: branch activated when correction channel is harm carrier | earned branch | Demote if applied to every flawed institution. |
| Protective Secrecy | witness protection; confidentiality; security studies | none/partial boundary | boundary condition | Demote if secrecy shields power rather than subject. |
| Care With Teeth | care ethics; capability approach; safeguarding | none as standalone | teaching/support | Merge into repair/enforcement if no distinct test. |
| Option-Space Restoration | capability approach; restorative justice | none as novelty | repair support | Demote if metaphorical. |
| Memory Bridge | memory studies; evidence preservation; identity theory | none as standalone | teaching/support | Merge into Record/Witness. |
| Recursive Agency | compatibilism; learning theory; reinforcement learning | none proven | candidate/teaching | Demote if it becomes free-will proof. |
| Escape Condition | control objectives; RL termination conditions; game loops | none proven | candidate/teaching | Demote unless tested on real training/governance loop. |
| Mandelbrot Boundary | complex systems; recursion; fractal analogy | none | analogy/archive | Remove if used as proof. |
| Creator Responsibility | duty of care; engineering ethics; product liability; deployment governance | none yet | candidate/teaching | Demote if it adds nothing beyond lifecycle governance. |
| Created Subject Boundary | moral standing; recognition theory; bioethics | none as TRACE remainder | boundary candidate | Demote if used to prove AI personhood. |
| Repair Debt | tort-like causation; duty to repair; responsibility theory | none yet | merge into repair/governance | Demote if totalizing blame. |
| Lifecycle Answerability | AI lifecycle governance; safety cases; deployment monitoring | none yet | alignment hypothesis | Demote if ordinary governance covers it. |
| Demotion Protocol | falsification; preregistration; version governance | yes, as internal wrongability machinery for TRACE claims | core governance | Fails if no claims are actually demoted. |
| Pre-Registered Test | preregistration; evaluation science | partial: applies prereg discipline to TRACE operators | core governance | Demote if never used prospectively. |
| Cry-Wolf Check | calibration; false-positive evaluation | partial as TRACE governance control | core governance | Fails if false positives are ignored. |
| False-Negative Check | safety evaluation; missed-harm review | partial as TRACE governance control | core governance | Fails if goalposts move after misses. |
| Contested Legitimacy | legitimacy theory; political sociology; public trust | none yet | candidate only | Do not promote without breaker case. |

## Narrow Survivors

After subtraction, the current plausible TRACE remainder is:

```trace
TRACE_remainder_survivors :=
  correction_before_hardening
  + K_gate_as_conjunctive_live_correction
  + exit_branch_when_correction_channel_is_harm_carrier
  + wrongability_governance_for_TRACE_claims
```

Even these are not validation claims. They are the surviving candidate remainder after prior-art comparison.

## What Was Demoted

```trace
demoted_from_public_spine :=
  recursive_agency
  + escape_condition
  + Mandelbrot_boundary
  + creator_responsibility
  + created_subject_boundary
  + recognition_failure
  + repair_debt
  + lifecycle_answerability
  + broad_care_language
```

They remain preserved as teaching/candidate material, not as active TRACE spine.

## Apollo / Columbia Pair

The Apollo/Columbia pair remains useful because it tests discrimination:

```trace
Apollo := K_linked + correction_beats_hardening
Columbia := signal_exists + K_unlinked + hardening_wins
```

This pair is illustrative, not validation. Its value is that it asks whether the same operators distinguish live correction from failed correction without requiring a new operator.

## No-Remainder Default

Future Concordance rows must start as:

```trace
TRACE_remainder := none
```

Then earn a remainder only by surviving comparator pressure.

End.
