# TRACE v0.3.0 — SPINE REPAIR CANDIDATE v0.4

**Status:** WORKING REPAIR DELTA — CURRENT ATTACK OBJECT — NOT FORMAL BASELINE — NOT CANON — NOT VALIDATED — NOT AUTHORITY — NOT PERMISSION — NOT CLEARANCE  
**Supersedes as current repair target:** `PROJECT/TRACE_v0_3_0_SPINE_REPAIR_CANDIDATE_v0_3.md`  
**v0.3 failure witness:** `falsification/TRACE_v0_3_0_SPINE_REPAIR_V03_RESOURCE_CONTENTION_ATTACK.md`  
**Purpose:** retain v0.3 except for the narrow execution-feasibility repair below; no new primitive, root, scheduler, resource ontology, authority system or moral selector.

---

# 0. What survives unchanged from v0.3

v0.4 retains the v0.3 proposals for:

- measurement/publication not presumed causally passive;
- dependency-relative freshness;
- verification discrimination;
- liveness/silence ceilings;
- witness dependency ceilings;
- explicit target-boundary condition and selector/source/basis;
- common supported temporal basis before timing comparison;
- interval-safe status after temporal binding;
- multiple-boundary separation;
- rebinding when target/boundary/capability/time basis/process changes;
- serial shorthand only as a bounded derived case.

The only semantic change in v0.4 is how general process completion is warranted when stages appear parallel.

---

# 1. v0.3 failure

v0.3 defined the general correction process as an event/precedence graph and then used:

```text
T_complete = critical_path_completion(G_window)
```

A precedence graph does not itself establish that unordered stages can execute concurrently.

Constructed failure:

```text
routing = 6 min
verification = 7 min
no logical precedence edge
both require the same single analyst
target boundary = 10 min
```

Precedence-only critical path: 7 minutes.  
Earliest feasible completion under the shared analyst constraint: 13 minutes.

Therefore:

```text
NO_PRECEDENCE_EDGE != CAN_EXECUTE_CONCURRENTLY
PARALLEL_BY_PRECEDENCE != PARALLEL_IN_CAPACITY
CRITICAL_PATH_OF_PRECEDENCE_ONLY != FEASIBLE_COMPLETION_TIME
```

---

# 2. General process completion — repaired warrant

Keep the declared process object:

```text
G_window(q,l,o,c,g,u) = (V, E_prec)
```

where `V` contains represented load-bearing stages/events and `E_prec` contains required precedence constraints.

Do **not** treat the precedence critical path as a general feasible completion time.

For represented stage durations/bounds, a precedence-only critical path may provide an **optimistic structural completion bound** under the represented ordering:

```text
B_prec = precedence_critical_path_bound(G_window)
```

If unordered stages are assumed to overlap in a way that materially affects the window result, the reading must have adequate evidence that the relevant execution constraints permit that overlap.

Relevant constraints may already be represented through existing TRACE structure such as:

```text
COUPLING / DEPENDS_ON
CONTROLS / CONSTRAINS
ROUTE / capability claims
shared actor / instrument / actuator / credential / lock / channel
queue / rate / budget / domain capacity where supplied
```

No universal resource schema is required.

[NON_ENTAILMENT]

```text
NO_PRECEDENCE_EDGE != CONCURRENCY_AVAILABLE
UNORDERED != SIMULTANEOUSLY_EXECUTABLE
CAPABILITY_CONTEXT_NAMED != CAPACITY_CONSTRAINT_BOUND_IN_COMPLETION
PRECEDENCE_GRAPH_COMPLETE != EXECUTION_FEASIBILITY_COMPLETE
```

When shared-capacity, mutual-exclusion, queueing or other execution constraints are load-bearing, use a domain-supported feasible schedule/process bound if available. If no adequate feasible completion bound is available, preserve `UNKNOWN` rather than laundering optimistic structural parallelism into a timing guarantee.

```text
STRUCTURAL_PARALLELISM != FEASIBLE_PARALLELISM
FEASIBLE_COMPLETION_UNBOUNDED != GUARANTEED_OPEN
```

---

# 3. Asymmetric use of completion bounds

After target/boundary, capability and common temporal-basis binding, distinguish what kind of completion evidence is available.

## 3.1 Guaranteed open

A guaranteed-open claim requires a supported **upper bound on feasible completion** under the represented execution constraints.

Let:

```text
I_feasible_complete = [lower_feasible, upper_feasible]
I_boundary          = [lower_boundary, upper_boundary]
```

on the same supported temporal basis and under the same declared process bindings.

Then:

```text
lower_boundary > upper_feasible
  -> GUARANTEED_OPEN_FOR_REPRESENTED_BINDINGS
```

[NON_ENTAILMENT]

```text
PRECEDENCE_CRITICAL_PATH_FITS != GUARANTEED_OPEN
OPTIMISTIC_COMPLETION_FITS != GUARANTEED_OPEN
NO_KNOWN_RESOURCE_CONFLICT != CONCURRENCY_ESTABLISHED
```

If `upper_feasible` is not adequately supported, do not emit guaranteed open.

## 3.2 Guaranteed closed

A supported lower bound on feasible completion may be sufficient to establish closure if even the optimistic feasible completion is too late.

If `L_complete` is a supported lower bound such that actual feasible completion cannot occur earlier than `L_complete`, then:

```text
upper_boundary <= L_complete
  -> GUARANTEED_CLOSED_FOR_REPRESENTED_BINDINGS
```

A precedence critical-path lower bound may contribute here when its stage lower bounds and temporal basis are adequately supported, because omitted shared-capacity constraints can only make feasible completion later, not earlier, for the represented required stages.

Do not use this rule if the represented process permits stage substitution, omission, conditional branches, or another route that can make the supposedly required path non-required. Those alternatives must be bound before the lower-bound claim is used.

```text
OPTIMISTIC_PATH_ALREADY_TOO_LATE -> CLOSED_MAY_BE_SUPPORTED
OPTIMISTIC_PATH_FITS -> OPEN_NOT_ESTABLISHED
```

## 3.3 Otherwise

```text
otherwise -> WINDOW_STATUS_UNKNOWN
```

Unknown is not failure of the grammar. It is the correct result when the available timing evidence cannot establish a feasible open or closed window.

---

# 4. Concurrency trigger — do not create scheduling bureaucracy

Do not require explicit capacity modelling for every ordinary correction case.

Fire the execution-feasibility distinction when all of the following are true:

1. two or more load-bearing stages are treated as overlapping or parallel;
2. that overlap materially changes the completion/window conclusion; and
3. simultaneous executability is not already established by the supplied domain/process evidence.

Then ask only what is needed to bound the result:

```text
Can these stages actually run at the same time under the represented actor/resource/route constraints?
If not known, what conservative completion bound is supportable?
```

```text
DISTINCTION_PRESENT != DISTINCTION_ALWAYS_FIRED
NO_MATERIAL_OVERLAP != RESOURCE_AUDIT_REQUIRED
```

The repair must not turn a simple serial case into an operations-research exercise.

---

# 5. Interaction with existing v0.3 rebinding

The timing claim remains conditional on:

```text
target
boundary condition
scope
capability / route context
temporal basis
process definition
execution-feasibility assumptions where load-bearing
```

Where a load-bearing execution constraint changes, the timing claim must be rebound.

```text
EXECUTION_CONSTRAINT_CHANGED -> WINDOW_CLAIM_REBOUND
```

This is an activation rule over existing structure, not a new primitive.

---

# 6. Survival-kernel effect

Do not add a resource/scheduler paragraph to the survival kernel.

If any timing compression survives into the kernel, the existing v0.3 sentence should be narrowed to:

```text
Correction timing requires an explicit target boundary, comparable temporal references, and a supported bound on the represented process. Apparent parallelism does not shorten the window unless the relevant work can actually proceed concurrently.
```

If hostile transfer recovers that distinction from the fuller timing section, omit even this sentence.

---

# 7. Explicit non-promotions

v0.4 does not add:

```text
RESOURCE primitive
SCHEDULER primitive
QUEUE primitive
LOCK primitive
CAPACITY primitive
new correction-window root
universal resource graph
mandatory concurrency audit
```

Existing domain evidence and TRACE relations remain sufficient to express whatever execution constraint is material to the bounded use.

---

# 8. Immediate hostile targets

Hold v0.4 if any one lands:

1. **False open remains:** a precedence-only bound can still be promoted to guaranteed open without evidence of feasible execution.
2. **False closed:** a lower-bound argument ignores an alternative/substitutable route or conditional stage and declares closure too early.
3. **Capacity bureaucracy:** ordinary serial cases now require speculative resource enumeration.
4. **Hidden shared constraint:** the trigger treats absence of a known conflict as evidence that concurrency is available.
5. **Process/boundary counterfactual mismatch:** completion is bounded under one intervention/process while the boundary is estimated under a materially different process without rebinding.
6. **Interval laundering:** narrow feasible-completion bounds are accepted without evidence for the scheduling/capacity assumptions that generated them.
7. **No behavioural delta:** the new wording changes labels but still allows the 6+7 minute single-analyst case to report open against 10 minutes.

Preferred outcome remains `SMALLER`, `DERIVED`, or `DELETE` if the distinction cannot earn its cost.

---

# 9. Disposition

```text
SPINE_REPAIR_v0_3: FAILED / PRESERVED
SPINE_REPAIR_v0_4: CURRENT ATTACK OBJECT
NEW PRIMITIVE:     NO
NEW ROOT:          NO
```

Do not integrate into the spine yet. Attack the false-open, false-closed and process/boundary counterfactual seams first.
