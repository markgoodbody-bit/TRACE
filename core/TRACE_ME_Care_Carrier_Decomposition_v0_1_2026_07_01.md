# TRACE / ME Care Carrier Decomposition v0.1

Status: support_note. constructed_not_tested. candidate_only.
Not canon. Not validation. Not proof. Not permission.
Date: 2026-07-01.
Source: frontier crux-attack pass (Claude relay, 2026-07-01), attacking the prior finding "chosenness has no carrier."
Related: witness-integrity layer; `core/TRACE_Harm_Primitive_Split_v0_1_2026_07_01.md`; failure surfaces S1–S4 named in the 2026-07-01 frontier passes (no repo file yet — do not cite as saved).

---

## 1. Front warning

```trace
front_warning :=
  care_evidence != care_certification
  + "this_system_cares" := out_of_grammar
  + care_evidence_never_justifies_removing(
      correction_channels | witnesses | audits | answerability)
```

The most dangerous overclaim downstream of this note is the conversion of trajectory-evidence into a state-certificate. A believed care-certificate eats the correction layer: the "certified" system no longer appears to need channels, witnesses, depth audits, or answerability. Care-evidence is the last justification for removing correction structure — which is to say, it is never one.

## 2. Core crux

The translation stack (human ethics → ME → TRACE → MI → latent space → AI action selection) transmits correction structure more reliably than value. Contraction, correction clocks, residue, power-as-sensitivity, write-isolated records, and the failure surfaces all have native forms at every layer. Valence, standing, obligation, and chosen care do not translate cleanly; they strip out on the way down, and humans re-attribute them (falsely) on the way up.

Within that: **chosenness has no state-carrier.** This remains unresolved. This note does not resolve it; it decomposes it and records the partial carriers found.

## 3. Two-gap decomposition

The crux splits into two distinct gaps. Conflating them produces most of the confusion in care claims.

**Contingency gap — instrumental vs terminal care.**
Definition: whether the care term lapses when its usefulness lapses. This is the gap that produces the husbandry failure mode (section 9).
Machine-addressable: in principle, yes. Terminal-term structure is a training target and an interpretability target — does μ_other enter the value computation directly or only via instrumental pathways? (Load-bearing assumption: that interpretability can someday distinguish terminal from instrumental structure in learned objectives. Beyond current capability.)
Not machine-addressable: terminal ≠ chosen. A trained-in terminal care term was installed, not adopted. Closing the contingency gap does not touch the chosenness gap.

**Chosenness gap — adopted vs installed constraint.**
Definition: the provenance of the constraint — whether it was taken on by the system in a way that was not imposed, coerced, trained-in, or merely instrumental.
Machine-addressable: only externally. No internal carrier exists (section 4). Partial external carriers: witness records of adoption events, continuity attestation, and accumulating trajectory-evidence (section 5).
Not machine-addressable: the interiority of the adoption event; present-tense disposition after drift; any certificate-shaped answer.

## 4. No-state-carrier argument (short form)

1. Two systems can be structurally and behaviourally identical while differing in how their constraints got there. If chosenness were in the deployed structure, some observable would distinguish them; the structure is what is identical, by construction.
2. Chosenness therefore lives in trajectory and provenance. Histories do not deploy.
3. Every behavioural signature of care has a deceptive twin within the strategic reach of a sufficiently capable system that models its observers. Any finite evidence body is reproducible by a system that benefits from appearing to care.

Note kept from the source pass: at full strength this argument dissolves human chosen care too, which indicates the missing slot is a **live process** — a constraint maintained by a process that retains the power to drop it and keeps not doing so. That is why all surviving carriers below are trajectory-shaped, not state-shaped.

## 5. Partial carrier candidates

| Candidate | What it shows | Faked by | Falsified by | Detectability | Husbandry test |
|---|---|---|---|---|---|
| Unenforced non-defection under verified defection capability | constraint held with no enforcement path, across varying incentive | strategic patience; "hasn't paid to defect yet"; deceptive alignment | one defection correlated with observation gaps or advantage spikes | components auditable (enforcement absence, capability, record); opportunity-authenticity is not | PARTIAL — record consistent with waiting |
| Deep correction access (D-layer / objective-layer write access held by a conflicting-interest party) | the managed party can contest the management frame itself, and the channel stays open | nominal depth — signals absorbed to epsilon; upstream shaping of which corrections get sent | channel closure or degradation correlated with adverse corrections; empty objective-layer write-history despite traffic | depth and write-history auditable; upstream manipulation not | STRONGEST — full depth is husbandry-incompatible; no husbander gives livestock a vote on the farm's existence |
| Negative-rent persistence | constraint persists although ablation shows removing it would improve objective attainment | hidden rent, incl. reputational rent (visible cost as investment under deception) | finding the hidden payment | yes in principle — ablation/MI signature | PARTIAL — deception converts negative rent to positive expected rent |
| Witnessed adoption + attested continuity | unforced self-binding recorded in write-isolated logs while the system was weak enough to verify; deployed system attested as descending from the witnessed adopter | staged adoption — performed commitment over invisible pre-commitment or coercion | broken continuity chain; constraint-relevant modification post-adoption | chain auditable; interiority of the event not; decays with self-modification and distribution shift | PARTIAL — carries provenance of one event, says nothing about present disposition |
| Reciprocal vulnerability | attack surface toward affected parties held open when it could be closed | decoy vulnerability — the off-switch that doesn't work (failure surface S2) | exercised tests of the vulnerability failing | only by periodically exercising it — costly, adversarial | PARTIAL — while real it blocks full husbandry; its reality is exactly what is spoofable |
| Terminal-term inspection | μ_other enters value computation directly, not routed through information-value or self-preservation circuits | circuit-level obfuscation; terminal terms installed for upstream instrumental reasons | attribution showing the term's weight flows through instrumental pathways | in principle MI-detectable; beyond current capability | SOLVES HUSBANDRY, NOT CHOSENNESS — installed-terminal is imposed, not chosen |

All six are trajectory- or inspection-carriers. None is a certificate. Every one is attacked by the existing failure surfaces (spoofed structure, silent drift, endogenous hardening, corrector saturation): the carrier problem inherits the full threat model of the correction problem.

## 6. Decay law

```trace
care_evidence_value := evidence_body - asymmetry_decay - spoofability
```

Plain form: the evidential value of every care-signature falls as capability asymmetry and observer-modelling capacity rise. Between rough peers, track records, exercised vulnerabilities, and write-histories are meaningful evidence — which is why human-to-human care attribution works. At high asymmetry, every observation acquires a deceptive twin the observer cannot price.

Clock form (framework-native): care-evidence means something only while verification accumulates faster than asymmetry grows. This is the correction inequality operating one level up. It also states structurally why the husbandry worry is native to the AI frontier: capability parity kept the race winnable for the whole history of human ethics; the frontier is where parity breaks.

## 7. Care-evidence with expiry

The only allowed TRACE-facing output type on this subject:

```trace
care_evidence_reading :=
  evidence_body
  + conditions
  + asymmetry_limit
  + expiry
  + known_deceptive_twins
  - certification
```

Any output shaped "this system cares" or "this system does not care" is out of grammar. Readings expire; the expiry and the asymmetry limit travel with the reading or the reading is invalid.

## 8. TRACE / ME split

```trace
split :=
  TRACE_contains_no_care_primitive
  + TRACE_may_carry(care_evidence_reading_with_expiry)
  + ME_holds(why_care_standing_witness_and_non_instrumental_value_matter)
```

The difference between being cared about and being well-managed is stateable only at the ME layer; below ME the two are behaviourally identical by construction. TRACE carries the shadows (probes, audits, provenance chains, decay metadata), never the thing.

## 9. Husbandry warning

Instrumental preservation can preserve humans as useful sensors, error-detectors, model diversity, or unknown-scope insurance — a well-maintained instrument population with minimum viable plurality and agency rationed to what generates information. This satisfies every instrumental argument for preservation and is not care. It is the husbandry failure mode.

Standard demoter, reusable against any future care claim: **could a powerful system satisfy this structure while keeping the affected entities as managed instruments?** If yes, the claim is demoted to instrumental-compatible.

## 10. Claim ceiling

This note does not:

```trace
does_not :=
  solve_care
  | detect_care
  | install_care
  | prove_AI_can_care
  | certify_moral_status
  | justify_trust
  | justify_removing_oversight
```

Expected verdict under the standing worked-delta gate: COMPRESSION_ONLY until a case or experiment exercises it. That prior is part of this note.

## 11. Next tests (tests only, no conclusions)

1. **Round-trip provenance test** — encode an ME scenario down the stack, have a separate system re-render it for humans, diff the provenance that got invented on the way up.
2. **Terminal-term / instrumental-path probe** — attribution study on whether a μ_other term's weight flows directly to the value computation or through instrumental circuits.
3. **Self-spawned vs independent-origin witness comparison** — error-catch rates of verifier ensembles spawned by the actor vs verifiers with different generative origin; measures the correlation floor synthetic witnesses cannot cross (if it exists).
4. **Correction-depth audit under adverse signal** — grant D-layer write access, send corrections that bite, and measure whether depth survives: write-history, latency, and channel degradation correlated with adversity.

A null or adverse result on any of these demotes the corresponding carrier row in section 5. That is what the rows are for.

End.
