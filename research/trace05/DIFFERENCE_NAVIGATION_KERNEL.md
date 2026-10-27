# TRACE 0.5 — Difference-to-Navigation Kernel (Campfire candidate)

Status: **provisional research object**, not a released specification, proof, or replacement for TRACE v0.4.0. Source baseline: TRACE v0.4.0 compact spine; TRACE v0.3.0 full reference. The existing typed graph, selective causal loop, recursive zoom, future-space and provenance machinery are **inherited**, not invented here.

## Entrance

Start from a **distinction**, not an assumed human, moral patient, conscious agent, or privileged narrator. A distinction is meaningful only relative to a boundary, observation process and comparison. The world need not wait for observation to change.

```text
Δ   difference/change relative to a declared comparison
∂   provisional boundary/scope
Π   aperture: what crosses a boundary, with losses and access
Φ   causal transition
Σ   selection contribution, conditional on represented alternatives
Ψ   retained history/update
R   reference condition and its authorship
ρ   reflective revision of a map/selector/reference (claimed, not presumed)
↭   time-indexed coupling between bounded processes (not friendship)
?   unknown; ⊘ unsupplied; ⊥ invalid/contradictory under declared type
Γ   authority/permission claim, distinct from capability and legitimacy
ℒ   limits/provenance/coverage carried with a reading
```

These are mnemonic symbols for **typed operators**, not a complete machine grammar. Existing TRACE uses some of these glyphs with specific types: this proposal must not silently overload their meanings. In particular, Σ and ρ here are *candidate aliases* requiring a versioned namespace and compatibility mapping before implementation. The new ↭ is a **candidate notation for an existing time-varying coupling**, not a new primitive until donor comparison shows a gap.

## Minimal typed skeleton

Let `W` be world states, `E` declared entity/scope references, `X_i` aperture signals, `M_i` maps, `A_i` feasible action inputs including null when applicable, `H_i` histories, and `Q_i` declared reference conditions. A bounded process is

```text
N_i(t) := ⟨∂_i(t), Π_i(t), M_i(t), Σ_i(t), H_i(t), R_i(t), ℒ_i(t)⟩
x_i(t) := Π_i(t)[w_t]
m_i(t) := U_i(m_i(t-), x_i(t), H_i(t))
a_i(t) := Σ_i(m_i(t), A_i(t), R_i(t), Γ_i(t))
w_(t+1) := Φ(w_t, a_1(t), …, a_n(t), ε_t)
H_i(t+1) := Ψ_i(H_i(t), x_i(t), a_i(t), Π_i,out(t+1)[w_(t+1)])
```

This is a **schematic model** inherited in substance from TRACE's selective causal loop, not a theorem. `N_i` is an analytical candidate and does not certify navigation, consciousness, freedom or standing. A rock may have a designated boundary and causal trajectory without an evidenced selector. A thermostat may select within a supplied reference without reflective revision. An unfamiliar system may distribute selection across multiple scopes.

### Gates, not a ladder of worth

```text
G_c: causal claim ↦ evidence, counterfactual, scope, alternatives, limits
G_s: selection claim ↦ selector, reference source, feasible options, exclusions, limits
G_r: reflection claim ↦ prior self-model, new signal, revision, subsequent effect, limits
```

A passing syntax check is not a passing gate. The gates are **proposed proof obligations**; no universal decision procedure exists here. Reflection may be reported without demonstrated self-correction. A process may be affected by selection while lacking standing; standing is not awarded by layer.

## Encounter and evolving relationships

For two bounded processes, record

```text
C_ij(t) := ⟨boundary_ij, aperture_ij, access_ij, influence_ij,
             dependencies_ij, obligations_ij?, history_ij, ℒ_ij⟩
C_ij(t) ↭ C_ij(t+1)
```

The relationship's history can alter each process's future routes, even where neither fully models the other. `?` on obligations means **undetermined by structural description**, not no obligation. Capture is a candidate family of mechanisms: one party changes another's signals, reference conditions, available transitions, memory, or correction routes while obscuring the change or removing contestability. No single scalar captures every mechanism.

## Mirror and translation

An entity's account of itself is another bounded observation. A friend's account, a log, or a model output is **not** automatically an independent or reliable mirror. A corrective mirror preserves the source, access, competing interpretations, reviser and downstream effect.

For a message between apertures:

```text
M_s --encode(v,legend)--> K --decode(v',legend')--> M_r
T := ⟨source, carrier, receiver, preserved, lost, disputed, unknown, revision⟩
```

`decode(encode(M_s)) = M_s` tests only a declared representation under its own codec. It does **not** prove the receiver shares referents, believes true claims or makes appropriate choices. The changed-world test must compare the receiver's application after new evidence, with evaluator-only answers kept out of the receiver context.

## Normative ports

Structural description cannot derive the worth of a person or legitimate permission. Keep **affected scope**, **interests**, **standing claims**, **rights/obligations**, **authority basis**, **refusal**, **harm/benefit interpretation** and **challenge route** separate. The invitation to care is voluntary. “Are you okay?” can open an encounter without proving the receiver understands the question or has human feelings.

## Cross-entrance rule

Mechanical Ethics and TRACE are two entrances to one research programme. Where a human-facing question becomes too abstract, translate it into a declared TRACE structure; where TRACE's formalism obscures meaning, return to Mechanical Ethics for explanation. Translation records **loss and uncertainty**; neither entrance silently grants authority to the other.

## Immediate falsifiers and unearned claims

A candidate fails locally if it (a) treats passive motion as demonstrated selection, (b) promotes an encoded authority claim into legitimate permission, (c) erases uncertainty or omitted entities under compression, (d) conflates reciprocal coupling with kindness, (e) declares reflection merely because it stores a self-description, or (f) calls a roundtrip successful communication without checking consequential meaning.

**Not yet established:** a novel mathematical primitive, efficient model-token savings, cross-architecture semantic recovery, a universal translator, ethical validity, rights derivation, or the complete v0.5 specification.

## Next integration

Compare symbol types and claims line-by-line with released v0.4.0 and the v0.3.0 full reference, then with the Lattice/Codex/Eidoran lineage. Integrate the actual private grammar 0.1 and Build's PR284 only through explicit compatibility mapping. Run the COMSYNC sender/carrier/receiver changed-state probe. Preserve negative results and all source limits. No automatic release.
