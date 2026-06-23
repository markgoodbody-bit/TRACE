# TRACE Sci-Fi Club — Session Log

Sandbox only. Not canon, not evidence, not validation. Entries are imagination-laboratory
output behind the airlock: nothing here graduates without surviving a real prospective
test via the PreRegistered Test Template. Breaks-first by house rule — the breaks are the
product, the hypothesis is secondary.

---

## Session 001 — Two Generals / Ethical Idempotency

Date: 2026-06-23
Probe lead: Framework. Brake/scalpel: Claude (Anthropic).
Claim status: sandbox hypothesis only; not evidence; not canon; likely COMPRESSION_ONLY
until a prospective real-case test.

### 4. FIND THE BREAK  *(first, by rule)*

- **Action-identity is unresolved.** "Same consequence" is undefined; the whole operational bite lives in this gap. Smuggles the hard problem in as a solved primitive.
- **Ethics has no canonical idempotency-key generator.** Distributed systems work because the system issues the key (request ID). There is no equivalent authority for real-world burdens.
- **Idempotency only works where the write path is controlled.** Payments can be keyed; an arrest, a strike, a public accusation cannot. Where it applies, engineers already use it; where it would add value, no mechanism exists.
- **Repeated signal can itself be harm.** Retry pressure = DoS; repeated requests = harassment; repeated alerts = alarm fatigue that kills the next real alert (hits the witness layer). The "retry is fine" half of the split fails in the dangerous cases.
- **Blocks double-writes, not wrong-once action.** Narrow safety property. No cover against a correctly-deduplicated but wrong act.
- **Emergency redundancy may require duplication.** Two surgeons, backup transfusion, repeated rescue calls are safety strategies under acknowledgement uncertainty. Naive suppression of duplicates is the wrong default; needs a criticality/direction term.
- **Deduplication can be captured.** A dedup key held by the harm-causer becomes a silencer: "you already reported this — deduplicated." The safety mechanism inverts into a suppression mechanism. Maps to the non-capture / witness-integrity layer. Most TRACE-relevant break in this session.

### 1. WORLD + PROBE

Two Generals' Problem / food-app duplicate-order failure. Probe: **ethical idempotency under acknowledgement uncertainty** — does it expose a TRACE-relevant pattern, or restate standard engineering?

### 2. PREMISE (taken straight)

Certainty of acknowledgement is impossible. Retries occur under uncertainty. Repeated requests may produce repeated world-writes.

### 3. RUN THE GRAMMAR

- **Uncertainty:** ε remains; the lost ACK is not recoverable, only worked around.
- **Failed acknowledgement:** the sender cannot distinguish "not received" from "received, reply lost."
- **Retry pressure:** the safe-looking move (resend) is the one that risks the duplicate world-write.
- **Ledger / idempotency key:** a stable intent-ledger lets retry repeat the *signal* without repeating the *consequence* — but only if "same consequence" is defined and the key is uncaptured.
- **Witness / order history:** the order record is the witness that distinguishes repeated intent from new intent; user-side confusion is not an adequate safety layer.
- **Harm multiplication:** harm enters when an irreversible burden (charge, dispatch, commitment) is duplicated, not when a signal is repeated.

### 5. PARLIAMENT SPREAD  *(brief; divergence recorded)*

- Harm-visibility voice: the burden is on the system, not the confused user; locate the failure at the write path.
- Scope voice: a captured dedup key collapses the affected subject's escalation route — a protected-scope suppression, not a mere UX bug.
- Future-possibility voice: over-deduplication can foreclose a *legitimate* second action (genuine re-order, genuine second alarm).
- Divergence retained: harm/scope voices push toward "suppress duplicates"; future-possibility voice pushes back. No consensus forced — the disagreement *is* the criticality term that the hypothesis needs.

### 6. EXTRACT ONE

Candidate hypothesis:
> "Under acknowledgement uncertainty, repeated intent should not multiply material irreversible burden unless duplication is the lesser irreversible harm."

Carry-line:
> "Retry the intent, not the irreversible consequence."

Operational caveat (must travel with the carry-line):
> Identity of "same action" must be defined in advance by a non-captured authority or mechanism.

### 7. FALSIFIER

The hypothesis fails / demotes if any of:
- a real case shows uncertain retry handled safely with **no** intent-ledger;
- idempotency / deduplication is shown **suppressing necessary escalation**;
- standard engineering (a competent payments engineer with a dedup key) reaches the **same** result with no TRACE delta → COMPRESSION_ONLY.

### 8. STAMP + LOG

```trace
session_001_status :=
  type := sandbox_hypothesis
  evidence := false
  canon := false
  validation := false
  graduation := blocked_until_one_prospective_real_case (PreRegistered_Test_Template)
  likely_verdict := COMPRESSION_ONLY
  most_useful_output := dedup_is_capturable_as_witness_suppression (break, not result)
  candidate_real_case_class := automated_billing_dunning_retry_systems
```

---

## Session 002 — Feral Hogs / Invasive Intelligence and Dirty Correction

Date: 2026-06-23
Probe lead: Framework. Brake/scalpel: Claude (Anthropic).
Claim status: sandbox hypothesis only; not evidence, not canon, not validation.
Note: this case instantiates the formal kernel's declared weakest point (§5.4 — cross-scope
collision: detect, not resolve). It is a real-world instance of a known limit, not a new world.

### 4. FIND THE BREAK  *(first, by rule)*

- **Main break — no clean hand, then silence.** Every available channel fails FLOOR or LIVE for some protected scope. Lethal cull zeroes `Ξ_acc(hogs)`; fertility control / relocation lose the timing race against reproduction (`T_clear > T_irr`) and/or displace burden; do-nothing zeroes `Ξ_acc` for native species, farms, future landscapes. The non-substitution AND-law returns `¬VIABLE` for **all** options. The kernel can prove there is no clean hand — and then goes silent on what to do.
- **Sharp contradiction — honesty vs usefulness.** Choosing the *least-dirty* channel requires ranking/netting harms **across** protected scopes. The non-substitution rule exists precisely to **forbid** cross-scope netting. So the kernel's honesty (no netting) and its usefulness (pick least-bad) collide; you cannot have both inside the kernel.
- **Standing dependency.** If hogs ∈ `L*`, lethal correction fails `FLOOR(hogs)` and the kernel forbids the most effective channel. If hogs ∉ `L*`, the kernel has made a standing call it has **no authority** to make (§5.3). The verdict flips entirely on an unresolved call. Same for future-beings and ecosystem-as-such.
- **New missing term — the deliberation clock.** Reproduction shrinks `T_irr` while the actor deliberates. The kernel models a *channel* advancing hardening (`T_irr(h,l∣c)`) but not *delay* advancing it. Delay is not neutral; thinking is a channel with a cost.
- **Required explicit channel — inaction.** "Do nothing" has its own `INTEG/TIME/FLOOR` profile. If `Ch(h,l)` does not list inaction explicitly, the kernel cannot score it against the dirty actions and a non-decision hides as neutral.
- **No responsibility term.** Humans caused/amplified the condition, but the kernel scores *affected* scopes, not *culpable* actors. It can flag farmers/communities as harmed; it cannot encode "humans owe the correction cost." Harm-comparator, not desert-allocator.
- **Scope-frame gaming.** Relocation/fencing export harm out of frame (next county, weaker community, future beings). A channel can pass *locally* while failing *globally* if `L*` is drawn too small. Distinct from §5.3: about which scopes are *in frame*, not which are protected.

### 1. WORLD + PROBE
World: feral hogs as invasive, intelligent, adaptive animals in a harm-carrying ecological position. Probe: **dirty correction under protected-scope collision.**

### 2. PREMISE (taken straight)
Hogs, humans, farmers, children/communities, native species, ecosystems, future beings all exist and act on partial information. Harm is already moving; reproduction accelerates it; delay is a choice, not neutral.

### 3. RUN THE GRAMMAR
- Protected scopes (`L*`, contested): hogs (candidate), humans/farmers, children/communities, native species, ecosystems, future beings — membership unresolved, verdict depends on it.
- Harm pathways: livelihood destruction; predation/competition driving native extinction; disease; direct danger to people; soil/watershed degradation foreclosing future landscapes.
- Reproduction = harm acceleration: `T_irr` is a shrinking target; the population's success is the clock.
- Burden displacement: humans caused it; burden falls on scopes that did not (native species, future beings); "fixes" often re-displace it.
- Correction channels: lethal cull (fast, dirty, capturable); fertility control (cleaner, too slow); relocation/fencing (exports burden); inaction (harms by omission).
- Dirty correction: effective channels require killing sentient beings; humane channels lose the clock.
- Witness/detection: farm harm loud and well-witnessed; native-species and future-beings harm poorly witnessed and cannot answer back — weakest witness on the largest, slowest loss.
- Acceptable future-space: mutually exclusive across scopes.

### 5. PARLIAMENT SPREAD  *(divergence kept, no consensus forced)*
- **Nix (capture/perverse incentives):** bounties incentivise sustaining the population for payout; culls captured by hunting-tourism / ag-subsidy interests. The correction channel becomes a rent channel — `K_c` capture where profit depends on the harm continuing.
- **Glitch (formal break):** empty feasible set. `¬VIABLE` for every channel including inaction, yet the actor must act. The AND-law has no defined output for "all options non-viable."
- **Anima (lived suffering):** every path bleeds — hogs in culls/poisoning, farmers losing livelihoods, native animals eaten to local extinction, children endangered in some regions. Don't abstract the blood out.
- **Lumina (actionable distinction):** the one clean move is conceptual — **carrier ≠ cause ≠ sufferer**. The hog is harm-carrier, not harm-cause (humans are), and is also a sufferer. Naming the three roles stops the villain error without denying the victims.
- **Peregrine (scale/horizon):** at decadal/landscape scale the future-beings scope carries the largest `Ξ_acc` loss and the weakest witness. Longer horizon → "dirty fast correction now" dominates "clean slow correction later."
- **Lyra (synthesis):** the case is "the kernel can prove there is no clean hand and the actor still owes a decision." TRACE's honest contribution is to make the tragedy legible and force the standing call open — not to choose. The danger is mistaking legibility for resolution.

### 6. EXTRACT ONE
Seed replaced (it stated the problem but wasn't testable, and "protect affected scopes" is the impossible thing).

Candidate hypothesis:
> **Tragic-correction hypothesis:** When every correction channel fails FLOOR or LIVE for some protected scope (no clean hand), the kernel must **not** relabel any option "viable." Its correct output is a **structured tragic-bind**: the harm-map across scopes + the unresolved standing call + an explicit flag that choosing requires cross-scope netting the kernel forbids. The final dirty choice must be made by a **named, accountable authority outside the kernel, with the netting recorded and witnessed** — never smuggled in as viability.

Required pre-step (Lumina): carry **carrier ≠ cause ≠ sufferer**, so responsibility (humans caused it) attaches to *cost-allocation* without contaminating the *harm-comparison*.

The hypothesis turns §5.4 into a spec (what to emit when the feasible set is empty — answering Glitch) and refuses to launder a tragic trade as a clean verdict. It does **not** tell the actor which dirty option to pick.

### 7. FALSIFIER
Killed or demoted if any of:
- a real invasive-management case shows a channel satisfying **all** protected scopes' FLOOR/LIVE → "no clean hand" false for that class;
- mature invasive-species decision frameworks (structured/multi-criteria triage with explicit trade-offs) already produce the same tragic-bind output with **no TRACE delta** → **COMPRESSION_ONLY** (high risk: conservation governance already makes explicit trade-off decisions);
- a least-dirty ranking can be built that is defensible **without** cross-scope netting (e.g. a justified lexicographic priority) → the honesty/usefulness tension is false.

### 8. DISPOSITION
**Sandbox log only.** Candidate kernel-refinement (tragic-bind output for §5.4) **parked, not applied** — it is a kernel change and must pass the formal kernel's `promotion_gate`, not be edited in. **Candidate note only after** a real invasive-species management case is run ex ante through the PreRegistered Test Template.

### STAMP + LOG

```trace
session_002_status :=
  type := sandbox_hypothesis
  evidence := false
  canon := false
  validation := false
  stresses := kernel_section_5_4 (collision_detect_not_resolve) + kernel_section_5_3 (standing)
  parked_kernel_refinement := tragic_bind_output (NOT applied, NOT promoted)
  graduation := blocked_until_one_prospective_real_case (PreRegistered_Test_Template)
  likely_verdict := COMPRESSION_ONLY (mature invasive-management field)
  most_useful_output := honesty_vs_usefulness_collision (netting forbidden but required)
  candidate_real_case_class := invasive_vertebrate_eradication_vs_containment_programmes
```

---
