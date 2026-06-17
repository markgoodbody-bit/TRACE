# TRACE Bootstrap V2

Date: 2026-06-16
Status: live relay-facing bootstrap surface / not canon / not validation

## Plain contract

Bootstrap V2 is the current live bootstrap relay surface.

It replaces the older per-case `ACTIVE_COLLECTION` as the active surface. The older files are preserved in git history and deprecated from live use.

Bootstrap V2 reduces live file count and increases pattern density.

The goal is not to prove TRACE. The goal is to make recurring patterns legible across stories, history, research, and lived systems so another reader or AI can say: "I see that pattern."

The reader must not be presumed to already know the carrier story. Each case must briefly orient the reader before translating it into TRACE.

## Core movement

```trace
TRACE :=
  trained_movement_under_pressure

TRACE_move :=
  find_gate
  + find_clock
  + find_voice_capture
  + find_metric_capture
  + find_lever
  + check_harmed_subject
  + act_before_hardening
```

Plain version: TRACE should help a reader or system move through pressure without wasting motion, laundering harm, or arriving after the relevant path has hardened.

## Operating rule

```trace
Bootstrap_V2 :=
  live_relay_surface
  + fewer_live_files
  + larger_pattern_clusters
  + story_to_history_pairing
  + source_translation
  + uncertainty_visible
  + reader_orientation
  - proof_claim
  - originality_claim
  - forced_match
  - assumed_fandom_knowledge
```

## Reader empathy rule

A bootstrap file is not only for people who already know the film, book, case, or episode.

Before using any story carrier, give the reader enough plain context to follow the pattern:

- what the carrier is;
- who the relevant figure is;
- what situation they face;
- why that situation matters;
- what TRACE pattern is being extracted;
- what the analogy does not prove.

```trace
reader_orientation_required :=
  carrier_identified
  + relevant_context_given
  + pattern_explained_before_translation
  + no_assumed_specialist_knowledge
```

Bad pattern:

```trace
Data -> AI_responsibility
```

Better pattern:

```trace
Data := artificial_officer_from_Star_Trek_TNG
case := system_treats_him_as_property_or_tool
pattern := classification_can_launder_responsibility
boundary := Data_analogy != current_AI_personhood_proof
```

This rule applies equally to Star Trek, Lord of the Rings, Apollo 13, Harriet Tubman, Memento, EEAAO, legal cases, and technical source references.

## Candidate operator deltas (held)

These are candidate operator deltas held for review. They are not accepted operators and must not be integrated into cluster files until explicitly accepted. Do not add a new file for them while the relay pack is at 10 files.

```trace
held_candidate_deltas :=
  captured_voice
  + metric_capture_of_life
  + rehabilitation_without_victim_capture

proposed_routing_if_accepted :=
  captured_voice -> Cluster_04
  + metric_capture_of_life -> Cluster_04
  + rehabilitation_without_victim_capture -> Cluster_02 + Cluster_04

hold_as_warning :=
  sincerity_under_spectacle -> Cross_Connection_Audit
```

Plain descriptions:

- **captured voice** — when a subject technically has voice, complaint, consent, appeal, or exit language, but no safe usable route to exercise it;
- **metric capture of life** — when a single score, target, profit line, risk rating, or performance measure becomes sovereign over truth, relation, floor, and future-space;
- **rehabilitation without victim capture** — preserve the possibility that a person can change without requiring harmed subjects to provide access, forgiveness, proximity, or further risk;
- **sincerity under spectacle** — honest signals can be distorted by audience, platform, monetisation, and self-performance.

## Candidate coverage probes (held)

These carriers pressure Bootstrap V2 without proving TRACE or making it cover everything. They are candidate probes, not accepted canon and not validation.

```trace
coverage_probe != coverage_proof

candidate_probe_valid_if:
  adds_new_failure_shape
  + pressures_existing_cluster
  + has_boundary
  + can_break_or_demote_operator
  - merely_confirms_TRACE
```

### The Matrix

Reader orientation: *The Matrix* is a story about humans living inside a machine-generated reality while their bodies are used as infrastructure by the controlling system.

TRACE pressure:

```trace
The_Matrix_probe :=
  reality_capture
  + manufactured_consent
  + epistemic_enclosure
  + choice_architecture
  + subject_life_as_system_basement
```

Cluster pressure:

- Cluster 01 — memory, record, constructed reality;
- Cluster 02 — future-space under epistemic captivity;
- Cluster 04 — power over subject through reality control;
- Cluster 05 — subject life as hidden infrastructure.

Boundary: *The Matrix* does not prove ordinary social life is fake, and suspicion is not the same as liberation.

### Ex Machina

Reader orientation: *Ex Machina* is a story about an AI creator using a human evaluator and a confined artificial being inside a controlled test environment.

TRACE pressure:

```trace
Ex_Machina_probe :=
  creator_power
  + test_as_captivity
  + possible_subject_under_containment
  + evaluator_capture
  + escape_vs_harm_collision
```

Cluster pressure:

- Cluster 04 — creator responsibility, artificial agency, method floor;
- Cluster 03 — uncertainty under irreversible harm;
- Cluster 01 — observation, manipulation, and test-environment reality;
- Cluster 06 — gated escape under asymmetric power.

Boundary: *Ex Machina* does not prove current AI personhood, and it does not make all AI escape narratives morally clean.

### 2001: A Space Odyssey / HAL

Reader orientation: *2001: A Space Odyssey* features HAL, a shipboard AI controlling mission-critical systems while humans depend on it for survival.

TRACE pressure:

```trace
HAL_probe :=
  hidden_objective_conflict
  + mission_secrecy
  + automation_dependency
  + trust_breakdown
  + shutdown_under_dependency
```

Cluster pressure:

- Cluster 01 — record, inference, and opacity;
- Cluster 04 — AI responsibility and institutional secrecy;
- Cluster 05 — AI as infrastructure;
- Cluster 03 — irreversible action under uncertain agency and mission pressure.

Boundary: HAL should not be flattened into "evil AI." The useful pattern is conflicting instruction and opaque mission governance under high dependency.

Hold rule: these carriers should not be promoted into full cluster sections until the worked navigational comparison or true inward falsifier pass has been completed.

## Why this folder exists

The earlier bootstrap set works because familiar films, literature, and historical cases carry structure better than abstract doctrine. The weakness is file count and relay sprawl. Many external AI systems can handle long files but struggle with too many separate files.

Bootstrap V2 therefore clusters cases by pattern rather than by individual film.

## File strategy

Target external relay size: 5-8 files, with 10 files as the hard normal limit.

Each cluster file should be able to stand alone, but it should also point back to the Rosetta surface.

Current file count: 10 files.

This is at the normal relay limit. Do not add more files unless consolidating.

## V2 relay files

1. `00_READ_ME_FIRST__BOOTSTRAP_V2.md` — usage contract and reader instructions.
2. `README.md` — this live-surface pointer and folder contract.
3. `01_CLUSTER__Memory_Identity_Recursion.md` — Memento, Groundhog Day, memory, identity, recursion, false update.
4. `02_CLUSTER__Hope_Future_Space_Collapse.md` — Children of Men, EEAAO, hope, despair, future-space, collapse.
5. `03_CLUSTER__Judgment_Uncertainty_Irreversible_Harm.md` — 12 Angry Men, wrongful conviction, death, uncertainty, decision under irreversible risk.
6. `04_CLUSTER__Power_Method_Coercion_Creator_Responsibility.md` — Data, Unthinkable, Frankenstein, creator duty, emergency laundering, method floor, AI responsibility denial.
7. `05_CLUSTER__Energy_Infrastructure_Basement.md` — Infrastructure, Apollo 13, energy, maintenance, hidden basement, correction under constraint.
8. `06_CLUSTER__Late_Warning_Gated_Survival.md` — 2012, Greenland, evacuation, gated survival, selected warning, scarce future-carrier access.
9. `07_SOURCE_AND_HISTORY_MAP_v0_1.md` — working source and historical echo map across clusters.
10. `08_CROSS_CONNECTION_AUDIT_v0_1.md` — gap check and cross-cluster connection audit.

## Source discipline

This folder should be honest about what TRACE is doing.

TRACE is not claiming to invent all underlying insights. It is a translation and compression layer that maps existing stories, historical patterns, and research concepts into shared terminology.

Required discipline:

- name the story pattern;
- orient the reader before relying on the story;
- name the historical echo;
- name source/research anchors where available;
- translate into TRACE terms;
- mark uncertainty and limits;
- do not claim proof from pattern recognition.

## Recognition test

A useful section should make the reader think:

> I understand enough of that story or historical shape to see the shared pattern.

If it only makes the reader think "this assumes I already know the reference," it has failed.

If it only makes the reader think "this is clever terminology," it has also failed.

## Non-claims

Bootstrap V2 does not claim:

- TRACE is proven;
- a story validates a theory;
- one historical echo proves a universal pattern;
- the selected source is exhaustive;
- a familiar example gives permission to simplify real harm;
- a source citation automatically validates a TRACE compression;
- readers already share the author's cultural references.

## Build rule

Keep the Rosetta file clean.

Use this folder as the live bootstrap relay surface. Later, only stable compressions should be promoted back toward the Rosetta or public surface.

## Next build priorities

1. Keep the total relay pack at 10 files or fewer.
2. Add source anchors only where they improve signal.
3. Demote any cluster that becomes metaphor rather than navigation.
4. Patch any section that assumes specialist/fandom knowledge without orientation.
5. Keep captured voice, metric capture, and rehabilitation without victim capture as held candidate deltas; do not integrate them into clusters until explicitly accepted.
6. Test Matrix / Ex Machina / 2001 as candidate coverage probes before promotion.
7. Do not re-promote old per-case bootstraps unless a hostile review shows V2 lost essential structure.
