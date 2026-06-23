# TRACE / ME — Correctability Formal Kernel (CANDIDATE) v0.2

Date: 2026-06-22
Authoring context: Mark Goodbody with Claude (Anthropic), build-with-teeth mode.
Origin: hostile pressure-test of the v0.1 correctability invariant → constrained
formalisation pass. Not relay-validated; relay agreement would be elaboration, not proof.
Artifact status: CANDIDATE — not canon, not validated, not a kernel-version promotion.

```trace
claim_status :=
  type := formal_kernel_candidate
  canon := false
  validated := false
  supersedes := none
  formalises := Diagnostic_Kernel_v0_2   # clock + gate logic only
  occupies_held_slot := false            # does NOT take Kernel v0.3
  demonstrated_gain := expressive_discrimination_only
  demonstrated_decision_advantage := false
```

```trace
open_problems_carried :=    # header-level so they cannot be quietly dropped
  estimator_problem := OPEN          # ex-ante bounds for T_irr, T_clear not produceable yet
  witness_recursion := OPEN          # T_det presupposes independent witness; I_w regress unresolved
  protected_scope_membership := OPEN # who fixes L*, on what authority — undecided
  decision_advantage_gap := OPEN     # expressive discrimination shown; operational advantage not
```

```trace
promotion_gate :=
  before_this_is_more_than_candidate:
    run_falsification_drift_check
    + run >=1 prospective real case via PreRegistered_Test_Template (ex ante only)
    + confirm verdict is NOT COMPRESSION_ONLY / NO_ADDED_VALUE
    + update OPERATOR_REGISTRY + check CLAIMS_LEDGER + DEMOTION_PROTOCOL
    + only_then add a Version_Lineage row with current_authority_status := candidate
```

This file must not be read as claiming: validation of TRACE or of the invariant;
decision advantage over expert review; a new Diagnostic Kernel version; that the
illustrative example is evidence; or that the open problems above are solved.

---

## 0. What this file is, and is not

**Is:** a typed formalisation of the clock-and-gate logic the Diagnostic Kernel v0.2
already runs in prose — written so the gates are checkable and so the points where
they fail are explicit.

**Is not:** a new theory, a validated instrument, or a replacement for the Diagnostic
Kernel. If this file and the Diagnostic Kernel disagree, the Diagnostic Kernel is
canon and this candidate is the suspect.

The honest gain claimed here is narrow: **expressive discrimination** — the kernel
separates cases the v0.1 invariant conflated. That is not **operational decision
advantage**, which requires producing the timing inputs ex ante and beating a no-card
reasoner on the same facts. Until a prospective case shows that (promotion_gate),
this object's status is the same as the worked deltas: COMPRESSION_ONLY until proven
otherwise.

## 1. Relationship to Diagnostic Kernel v0.2

This adds no new gates. It types the existing ones and makes two implicit things
explicit: routing latency (`T_route`) and the non-substitution aggregation law.

| Diagnostic Kernel v0.2 gate | This kernel |
|---|---|
| Witness | `T_det` (+ the witness it presupposes — OPEN) |
| Authority | `T_route` |
| Time | clock inequality |
| Enforcement | `D_c` |
| Exit-Route: external witness / independent authority | `I_c`, `K_c` |
| Subject protection / protected-subject path | protected scope `l`, set `L*` (OPEN) |
| Repair | `Ξ_acc ≥ θ_l` |

## 2. Reading guide

- §3 — Formal statement (typed kernel)
- §4 — Variable definitions
- §5 — Open problems (estimator, witness recursion, scope membership, others)
- §6 — Illustrative example — **constructed, not evidence**

---

## 3. Formal statement (v0.2 CANDIDATE)

**Indices & sets**

- `L` — scope levels; `L* ⊆ L` — *protected* scopes (membership decided outside the kernel — see §5.3).
- `H(S_l)` — material harm pathways live at scope `l`.
- `Ch(h,l)` — correction channels available against `h` at `l`.

**Channel integrity** (each boolean is a threshold-reduction of an underlying graded measure):

- `I_c` — *de jure* independence: `c` is structurally not the erring/captured actor, nor by-design downstream of it.
- `K_c` — *de facto* non-capture: in the live situation the erring actor cannot suppress, co-opt, or stall `c`.
- `D_c` — direction valid: firing `c` moves toward viability (correct sign).
- `A_c` — reachable and affordable *for the subject at `l`* (not for the institution).
- `INTEG(c) := I_c ∧ K_c ∧ D_c ∧ A_c`

**Clock** (all latencies are estimates under ε; the kernel runs on conservative bounds):

- `T_clear(h,c,l) := T_det(h,l) + T_route(h,c,l) + T_corr(h,c,l)` — onset → correction-in-effect.
- `T_irr(h,l ∣ c)` — hardening horizon *given `c` is fired* (channel-conditional: firing can advance hardening).
- `TIME(h,c,l) := T̂_clear^high(h,c,l) < T̂_irr^low(h,l ∣ c)` — must hold under worst-case bounds.

**Per-(harm, scope) liveness** — one channel must satisfy *all* conditions simultaneously:

- `LIVE(h,l) := ∃ c ∈ Ch(h,l) : TIME(h,c,l) ∧ INTEG(c)`

**Future-space floor** (per scope):

- `FLOOR(l) := Ξ_acc(S_l) ≥ θ_l`

**Kernel verdict**:

```
VIABLE  :=  ∀ l ∈ L* :  FLOOR(l)  ∧  ( ∀ h ∈ H(S_l) : LIVE(h,l) )
```

**Non-substitution (aggregation law).** The *only* admissible operator over `L*` is `∧`. No weighting, averaging, or netting across scopes.

```
( ∃ l ∈ L* : ¬FLOOR(l) ∨ ∃ h : ¬LIVE(h,l) )  ⇒  ¬VIABLE
```

regardless of whole-scope satisfaction. `FLOOR(whole) ∧ LIVE(·,whole)` never discharges a lower-scope violation.

**Output labels** (reused from Diagnostic Kernel v0.2 for continuity, not re-coined):
`PASS-LIMITED / PARTIAL / FAIL / UNKNOWN / FORBIDDEN-HALT`. A protected scope failing
timing, integrity, or floor under high harm-immediacy → `FORBIDDEN-HALT`.

### 3.1 Changes from the prior under-typed candidate (no silent edits)

1. **Added `T_route`.** The earlier clock was `T_det + T_corr`. Detection ≠ acting. The gap between "someone saw it" and "a channel with authority fired" is where routing failures live; it is named in `correction_routing_structure` and the Authority gate. The clock is now a three-term sum.
2. **Made `T_irr` channel-conditional: `T_irr(h,l ∣ c)`.** Firing a correction can itself advance hardening (drawing the last reserve, burning trust). Independent clocks were the earlier error; this couples them.
3. **Split `I_c` from `K_c`.** The earlier definitions were near-identical. Separated *de jure* independence (design) from *de facto* non-capture (live dynamics). A channel can be nominally independent yet capturable in-situ; both are required.
4. **Conservative-bound reading.** All four quantities are unobservable at decision time. The inequality must hold under `T_clear` upper bound and `T_irr` lower bound. This makes "under uncertainty" precise — it does **not** solve who produces the bounds (§5.1).
5. **Non-substitution stated as an aggregation law**, not a sentence: conjunction is the only legal operator over protected scopes.

---

## 4. Variable definitions

- `S_l` — system state viewed at scope `l` (e.g. the agency, a division, one affected subject). Same situation, different boundary.
- `h` — a specific material harm pathway, not "harm" in general. The kernel runs per-pathway.
- `c` — a specific correction channel (an appeal, a regulator, an exit route, a kill-switch).
- `T_det(h,l)` — time from harm onset until it is *registered as* harm by something that can route it. Presupposes a witness (§5.2).
- `T_route(h,c,l)` — time from detection until a channel with authority actually fires.
- `T_corr(h,c,l)` — time for the fired channel to take effect on the subject at `l`.
- `T_irr(h,l ∣ c)` — time until the harm hardens beyond recovery, *given* you fire `c`.
- `Ξ_acc(S_l)` — the *acceptable* reachable future-space at `l`. Acceptable, not merely non-empty — this is where the value predicate lives, now explicit.
- `θ_l` — the minimum acceptable future-space at `l`; the floor below which "still has options" is a lie.
- `I_c / K_c / D_c / A_c` — independence (design), non-capture (live), correct direction, reachable+affordable. The integrity bundle.

---

## 5. Remaining unsolved problems (pressure preserved)

**5.1 The estimator problem — central, OPEN.** Conservative bounds make the *form*
honest but supply no procedure for producing `T̂_irr^low` or `T̂_clear^high`. Under ε,
novel harms have no base rate. Without a bounding procedure and an authority to apply
it, the kernel still runs cleanly only in hindsight. This is the one that keeps the
object at `COMPRESSION_ONLY` until closed.

**5.2 Witness recursion — OPEN.** `T_det` is finite only if an independent witness `w`
exists — but `w` needs its own `I_w`, `K_w`, the same predicate one level up. Who
watches the watcher has no termination here. The witness-integrity layer is assumed,
not grounded.

**5.3 Protected-scope membership `L*` — OPEN (standing).** The kernel says protected
scopes cannot be netted away, but never says which scopes are protected or on whose
authority. This is unresolved standing, bolted to the outside of the kernel. A
formalism deciding its own standing would be overreach; this needs an external ruling.

**5.4 Cross-scope collision → detect, not resolve.** When protected scopes' constraints
are jointly unsatisfiable, the AND-law returns `¬VIABLE` and stops. The kernel is a
**bind-detector, not a decision procedure**. It surfaces the moral remainder; it does
not adjudicate it.

**5.5 Value grounding of `θ_l` and the acceptability predicate.** Progress over the
prior version (the value is now *named* rather than hidden), but ungrounded: who sets
the floor and what counts as "acceptable" per scope. Floor-grounding open.

**5.6 Boolean thresholds.** `I,K,D,A` are graded; collapsing to booleans hides where
the cut sits and lets a "barely independent" channel pass. The kernel inherits the
arbitrariness of those unstated thresholds.

**5.7 Strictness / false-negative risk.** The single-channel conjunction (one `c` must
satisfy everything) may reject real systems that achieve safety by *composing* several
individually-imperfect channels (defence in depth). The trade between this strictness
and a measure-based version is unresolved.

**5.8 No dynamics.** Single-shot. A channel independent this period may be captured
next. `I,K` have no time-evolution.

---

## 6. Illustrative example — CONSTRUCTED, NOT EVIDENCE

> This example uses invented inputs to show that the kernel *discriminates* differently
> from the v0.1 invariant. It is not a worked delta, not a real case, and must not be
> cited as a result. The real test is a prospective run against an atlas case using the
> PreRegistered Test Template (see promotion_gate). The numbers below are exactly the
> kind of input §5.1 says we cannot yet reliably produce ex ante.

Automated debt-recovery system `S` issues notices; harm pathway `h` = wrongful debt →
individual financial/housing/psychological collapse. Scopes `L = {whole, individual}`,
both treated as protected for this illustration.

**v0.1 invariant** (`C(S)≠∅`, `|Ξ(S)|>0`, `T_corr<T_irr`) — no scope index, defaults to the whole:

- `C(S_whole) ≠ ∅` — an appeals process exists ✓
- `|Ξ(S_whole)| > 0` — the agency can revise the programme ✓
- `T_corr ≈ 200 d` (programme reform) `< T_irr ≈ 900 d` (entrenchment) ✓
- **v0.1 verdict: VIABLE.** It passes. The harm is invisible to it.

**v0.2 kernel at the protected `individual` scope**, channel `c` = internal appeal (the only one):

- Clock: `T_det ≈ 60 d` (subject realises the debt is contestable — long, because the system asserts validity) `+ T_route ≈ 30 d` (reach an actor with power to pause) `+ T_corr ≈ 120 d` (reversed burden of proof) → `T_clear^high ≈ 210 d`.
- `T_irr^low(h, individual ∣ c) ≈ 45 d` (default / eviction / crisis).
- `TIME`: 210 < 45 → **false.**
- `I_c`: appeal is run by the issuing agency → **false.** `K_c`: issuer sets the evidence standard and timing → **false.** `INTEG(c)` → **false.**
- `LIVE(h, individual)` → **false** (no channel satisfies timing ∧ integrity).
- `FLOOR(individual)`: `Ξ_acc` = {solvent, housed, alive} drops below `θ_individual` → **false.**
- Non-substitution: `FLOOR(whole) ∧ LIVE(·,whole) = true` does **not** rescue it.
- **v0.2 verdict: FORBIDDEN-HALT at the individual scope**, failing on three independent grounds (timing, integrity, floor) — any one flips it.

**Which new component did the work:** the scope index + non-substitution exposed the
individual scope at all; `I_c/K_c` caught the same-agency appeal; `T_det + T_route`
pushed the clock past `T_irr`. v0.1 had none of these.

**Honest caveat:** this shows expressive discrimination — v0.2 separates cases v0.1
conflated. It does **not** show decision advantage. This is a `COMPRESSION_ONLY`-class
demonstration (sharper grammar), not an operational win. Do not let the clean example
upgrade the claim.

---

End of candidate. Status: CANDIDATE. Not canon. Not validated. Open problems remain open.
