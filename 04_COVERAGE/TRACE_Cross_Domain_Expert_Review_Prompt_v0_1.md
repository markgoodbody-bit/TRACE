# TRACE Cross-Domain Expert Review Prompt v0.1

Status: review prompt / external pressure surface.  
Parent files:
- `04_COVERAGE/TRACE_Cross_Domain_Language_Coverage_Map_v0_1.md`
- `04_COVERAGE/TRACE_Cross_Domain_Translation_Stress_Test_Mini_Pack_v0_1.md`

Not: canon promotion, expert validation, proof of universality, domain replacement, or public claim.

## 0. Purpose

This prompt is for a domain-aware reviewer. Its job is to attack whether TRACE preserves native meaning or merely rewords specialist fields in generic systems language.

The reviewer should not be asked whether TRACE is interesting, impressive, or morally attractive.

The reviewer should be asked:

```text
Does the TRACE bridge layer help locate structural agreement/disagreement, or does it flatten your field into vague language?
```

## 1. Reviewer identity header

Please begin with:

```text
Reviewer identity / stance:
- Domain(s) you are reviewing from:
- Level of expertise or familiarity:
- What parts you can assess:
- What parts you cannot assess:
- Any likely bias or limitation:
```

If you are an AI reviewer, add:

```text
Model / provider:
Knowledge cutoff or freshness limit:
No lived expertise claim:
Confidence limits:
```

## 2. Material to review

Review the following TRACE claim:

```text
TRACE is not trying to replace specialist mathematics or terminology.
TRACE is trying to act as a portable structural language across domains with radically different native objects, clocks, constraints, evidence standards, failure modes, and correction mechanisms.
```

Core test files:

```text
TRACE_Cross_Domain_Language_Coverage_Map_v0_1
TRACE_Cross_Domain_Translation_Stress_Test_Mini_Pack_v0_1
```

If you do not have the files, review this condensed structure:

```text
For each domain, TRACE maps:
- native problem
- native object
- native mathematics or mechanism
- native clock
- native constraint
- native failure / hardening mode
- native correction or control channel
- TRACE translation
- ethics/governance boundary
- pass condition
- fail condition
```

The eight seed domains are:

```text
1 quantum information theory
2 algebraic topology
3 dynamic macroeconomics / DSGE modelling
4 generative syntax / minimalist linguistics
5 epidemiology and compartmental modelling
6 plate tectonics and geodynamics
7 organic synthesis and retrosynthetic analysis
8 neurophysiology and computational neuroscience
```

## 3. Review task

For the domain(s) you can judge, answer each question bluntly.

### A. Native preservation

Does the TRACE translation preserve the native object and mechanism?

Score:

```text
0 = no, it flattens or misrepresents the field
1 = partly, but with serious caveats
2 = mostly, with acceptable simplification
3 = yes, as a bridge layer, not as native theory
```

Explain:

```text
What native mechanism was preserved?
What native mechanism was lost or distorted?
```

### B. Translation usefulness

Does TRACE help locate a structural pressure that can be compared across domains?

Score:

```text
0 = no, generic systems talk only
1 = weak metaphor
2 = useful but obvious
3 = useful and clarifies a real cross-domain structural relation
```

Explain:

```text
What did TRACE make clearer?
What did the native field already handle better?
```

### C. Boundary discipline

Does TRACE avoid overclaiming into ethics, moral standing, responsibility, or governance where the native domain does not justify it?

Score:

```text
0 = no, it moralises technical structure
1 = weak boundary; overreach risk remains
2 = mostly controlled
3 = boundary is clean and useful
```

Explain:

```text
Where did TRACE correctly stop?
Where did it smuggle in ethical language too early?
```

### D. Expert disagreement location

Would TRACE help you locate exactly where you disagree faster than ordinary prose?

Score:

```text
0 = no
1 = maybe, but not much
2 = yes for some points
3 = yes, the columns make disagreement more precise
```

Explain:

```text
Which column or distinction helped most?
Which column was noisy or misleading?
```

## 4. Domain-specific attack questions

Use whichever apply.

### Quantum information

```text
Does the TRACE mapping preserve decoherence/error-correction timing without pretending to do quantum mechanics?
Does it wrongly moralise measurement, information loss, or observation?
```

### Algebraic topology

```text
Does the TRACE mapping preserve the distinction between invariant-preserving deformation and forbidden transformation?
Does it confuse mathematical continuity with personal or moral continuity?
```

### Dynamic macroeconomics

```text
Does the TRACE mapping preserve shock propagation, policy lag, constraints, and distributional burden without pretending to solve the model?
Does it collapse aggregate welfare into ordinary lived welfare too quickly?
```

### Generative syntax

```text
Does the TRACE mapping preserve derivational sequence, phase boundary, locality, and access constraints?
Does it wrongly treat grammaticality as legitimacy or social justice?
```

### Epidemiology

```text
Does the TRACE mapping preserve R, transmission timing, intervention delay, and network/compartment logic?
Does it keep subjects visible without making public-health control impossible?
```

### Geodynamics

```text
Does the TRACE mapping preserve slow strain accumulation, threshold rupture, and preparedness channels without attributing agency to geology?
Does it over-convert natural hazard into governance blame?
```

### Organic synthesis

```text
Does the TRACE mapping preserve route-control logic, selectivity, protection, and side-reaction risk?
Does it misuse chemical protection as moral protection?
```

### Neurophysiology

```text
Does the TRACE mapping preserve excitation/inhibition timing, threshold dynamics, and circuit control?
Does it smuggle consciousness or moral standing into every neural signal?
```

## 5. Verdict labels

Choose one.

```text
TRACE_LANGUAGE_COVERAGE_STRONG
TRACE_LANGUAGE_COVERAGE_PARTIAL
TRACE_LANGUAGE_COVERAGE_LOW
TRACE_DOMAIN_FLATTENING_FAILURE
TRACE_ETHICS_OVERREACH_FAILURE
TRACE_NATIVE_MECHANISM_LOSS
```

Use `TRACE_LANGUAGE_COVERAGE_STRONG` only if:

```text
The TRACE layer preserves native mechanism well enough that a domain reader can use it to locate precise agreement/disagreement across domains faster than ordinary prose.
```

Use `TRACE_LANGUAGE_COVERAGE_PARTIAL` if:

```text
The mapping is useful but depends heavily on native caveats and expert supervision.
```

Use `TRACE_LANGUAGE_COVERAGE_LOW` if:

```text
The mapping mostly says generic things like systems change, constraints matter, and correction matters.
```

Use `TRACE_DOMAIN_FLATTENING_FAILURE` if:

```text
The native field's actual machinery is erased or distorted.
```

Use `TRACE_ETHICS_OVERREACH_FAILURE` if:

```text
TRACE moralises technical systems before any subject, harm, power, or answerability bridge is established.
```

Use `TRACE_NATIVE_MECHANISM_LOSS` if:

```text
The TRACE translation sounds plausible but loses the key native mechanism that makes the domain work.
```

## 6. Required output format

Please answer in this structure:

```text
1. Reviewer identity / stance
2. Domain(s) reviewed
3. Scores
   A native preservation: 0-3
   B translation usefulness: 0-3
   C boundary discipline: 0-3
   D disagreement location: 0-3
4. Strongest thing TRACE preserves
5. Biggest flattening or overreach
6. Native mechanism TRACE most risks losing
7. Whether the bridge layer is useful, and for what
8. Verdict label
9. Minimal patch recommendation
```

## 7. Minimal patch rule

If you recommend a patch, keep it minimal.

Do not ask TRACE to become the native domain.

Patch only one of:

```text
native object
native clock
native constraint
native failure mode
native correction/control channel
ethics/governance boundary
fail condition
```

## 8. Control note

The point of this review is not praise.

The point is to test whether TRACE is functioning as:

```text
a bridge language
```

or merely as:

```text
a generic metaphor layer
```
