# TRACE Rebuild Rules v0.1

Status: rebuild governance / repo-cleanup control surface.  
Authority: binding working rule for the TRACE mathematical rebuild.  
Parent: `00_CORE/TRACE_MATH_KERNEL_v0_1.md`.  
Not: deletion order, archive execution, validation, public-facing prose.

## 0. Purpose

The repository is to be cleaned and rebuilt around the TRACE mathematical kernel.

The rebuild is not cosmetic.

The target structure is:

```math
TRACE := middle_out_mathematical_modelling_of_entities_under_uncertainty

Mechanical_Ethics := TRACE_output -> human_legible_constraint
```

All prior material is preserved as history unless explicitly migrated, superseded, or archived.

No deletion by default.

## 1. Root Authority

The rebuild root is:

```text
00_CORE/TRACE_MATH_KERNEL_v0_1.md
```

Every new TRACE claim must trace back to at least one kernel primitive:

```math
entity
state
observation
uncertainty
action_space
reachability
transition
future_space
harm
positive_continuation
repairability
irreversibility
decision_rule
update
```

If a claim cannot be mapped to these, it remains:

```text
note / metaphor / open question
```

not TRACE core.

## 2. Valid TRACE Unit

A valid TRACE unit must identify:

```math
p_0 := concrete middle point
```

where `p_0` is one real point such as:

```text
person
animal
system
institution
AI process
room
street
decision
wound
encounter
```

Then it must define:

```math
x_e(t)        // state
O_e(W(t))    // observation
U_e(t)        // uncertainty
A_e(t)        // action-space
ρ_e(a|x,t)   // reachability
P(W'|W,a)    // transition
ΔH_e(a)      // harm / future-space loss
C^+_e(t)     // positive continuation / life-worth field
R_e(a)       // repairability
I_e(a)       // irreversibility
a^*          // selected action / decision rule
```

A file lacking these elements may still be useful, but it is not core TRACE.

## 3. Mechanical Ethics Derivation Rule

Mechanical Ethics cannot be first-order assertion.

It must derive from TRACE structure.

Example:

```math
U_displayed < U_actual
```

becomes:

```text
A system must not hide uncertainty where subject future-space is at stake.
```

Example:

```math
Capture_e ↑ ∧ ρ_e(safe_exit) ↓
```

becomes:

```text
A system must not judge final action without accounting for collapsed reachable exits.
```

Example:

```math
C^+_e -> 0
```

becomes:

```text
A system must preserve not only survival, but the conditions that make continuation liveable.
```

## 4. Cleanup Principle

Cleanup means:

```text
inventory
classify
map_dependency
preserve_history
migrate_when_earned
archive_when_superseded
```

Cleanup does not mean:

```text
delete
silently rewrite
collapse lineage
rename without map
hide uncertainty
pretend old work was useless
```

The old repo is not trash. It is source-history.

## 5. Classification Classes

Every existing file should be classified as one of:

```text
CORE_KERNEL
DERIVED_TRACE
ME_TRANSLATION
CASE_STUDY
SOURCE_NOTE
AUDIT_REVIEW
WORKING_NOTE
PUBLIC_FRONT_DOOR
ARCHIVE_CANDIDATE
SUPERSEDED_BUT_PRESERVE
UNKNOWN
```

No file may be moved until it has at least provisional classification.

## 6. Migration Rule

A file may be migrated into the new core only if it can be rewritten into kernel form.

Required migration map:

```text
old_file
old_claim
kernel_primitives_used
new_location
claim_status
uncertainty
```

Claim status values:

```text
formal_kernel
candidate_relation
case_observation
metaphor
translation
unsupported
rejected
```

## 7. Archive Rule

Archive is preservation, not deletion.

Archive candidates include:

```text
old public prose superseded by math kernel
case notes without formal mapping
duplicate relay packs
obsolete front-door drafts
old synthesis files whose claims are now kernelised elsewhere
```

Do not archive:

```text
source packs
external reviews
audit records
manifests
sha manifests
current kernel files
control files
```

unless a later explicit review confirms dependency status.

## 8. No-Waffle Rule

New core files should prefer:

```text
definitions
equations
variables
conditions
failure modes
translation rules
```

Avoid:

```text
rhetorical flourish
unearned moral conclusion
case-summary without model
praise language
validation language
```

## 9. Bluey / Positive Continuation Rule

TRACE is not only harm avoidance.

Every valid life-model must include positive continuation:

```math
C^+_e(t) = V_e + Rel_e + Joy_e + Play_e + Meaning_e + Growth_e
```

A model that only minimises harm is incomplete.

Mechanical Ethics must preserve:

```text
survival
repair
relation
play
meaning
growth
future-space
```

## 10. Uncertainty Rule

Every model must carry uncertainty.

Required distinction:

```math
U_actual
U_displayed
```

Danger condition:

```math
U_displayed < U_actual
```

Files that state conclusions without uncertainty status are incomplete.

## 11. Rebuild Sequence

Recommended rebuild order:

```text
00_CORE/TRACE_MATH_KERNEL_v0_1.md
00_CORE/TRACE_REBUILD_RULES_v0_1.md
00_CORE/TRACE_ENTITY_MODEL_v0_1.md
00_CORE/TRACE_ACTION_REACHABILITY_v0_1.md
00_CORE/TRACE_HARM_VALUE_IRREVERSIBILITY_v0_1.md
00_CORE/TRACE_UNCERTAINTY_AND_BELIEF_v0_1.md
00_CORE/TRACE_MIDDLE_OUT_METHOD_v0_1.md
00_CORE/TRACE_ENTITY_TO_ENTITY_MODELLING_v0_1.md
01_ME_TRANSLATION/ME_FROM_TRACE_KERNEL_v0_1.md
04_CASES_REBUILT/[case]_TRACE_MODEL_v0_1.md
```

## 12. Hard Guard

Do not claim:

```text
TRACE is validated
TRACE solves ethics
TRACE solves AI alignment
TRACE proves moral standing
TRACE replaces human judgement
```

Allowed claim:

```text
TRACE is a candidate mathematical language for middle-out modelling of entities under uncertainty, built to preserve subject visibility, uncertainty, consequence, and repairability before harm hardens.
```
