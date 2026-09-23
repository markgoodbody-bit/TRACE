# TRACE v0.4 beta3 — detailed timing profile

Status: **DERIVED PROFILE / NOT COMPACT SPINE / NOT A NEW PRIMITIVE / NOT A REPLACEMENT FOR DOMAIN TIMING METHODS**.

This file preserves the detailed correction-window machinery removed from the compact beta3 spine after external review. It exists so the project can test whether the extra detail ever earns its activation cost.

Use this profile only when precedence, occurrence identity, feasible parallelism, temporal conversion, multiple boundaries or strong open/closed interval claims are load-bearing. Otherwise use the compact spine.

Established neighbouring machinery includes critical-path and project scheduling methods, real-time scheduling, control/systems-safety methods and viability/reachability analysis. TRACE should interoperate or hand off rather than claim those methods as local inventions.

```text
PROFILE_AVAILABLE != PROFILE_REQUIRED
DETAILED_TIMING != MORAL_PRIORITY
FORMAL_DETAIL != FEASIBLE_SCHEDULE_ESTABLISHED
```

---

# [9] CLOCKS / ROUTES / HARDENING

Represent clocks by what they actually time. Do not promote urgency into irreversibility.

```text
EVENT_TIME != STAGE_DURATION
URGENCY != IRREVERSIBILITY
HARDENING != IRREVERSIBILITY
HARDER_TO_CORRECT != IMPOSSIBLE_TO_CORRECT
```

Hardening may contribute to a separately supported irreversibility claim, but a hardening clock/status does not become an irreversibility boundary by label alone.

## [9.1] General correction-window object

For pathway `q`, affected scope `l`, target effect/state `o`, correction capability/route context `c`, target-boundary condition `g`, and use `u`, represent required correction work as:

```text
G_window(q,l,o,c,g,u) = (V, E_prec)
```

where `V` contains load-bearing event/stage occurrences and `E_prec` required precedence. `E_prec` is a derived timing view, not a canonical TRACE relation.

Each load-bearing precedence edge retains its supporting canonical ordering claims plus material mechanism/binding refs not recoverable from them. Before critical-path use, build the view for one executable pathway hypothesis: bind process/pathway, scope, target, route/execution alternative, capability context, time/policy version and use where they can change the result. Unknown load-bearing route membership remains `UNKNOWN`; do not union mutually exclusive alternatives. When stage types recur, distinguish occurrences where collapse could create/erase a cycle or change timing. The resulting view must be acyclic.

```text
DERIVED_EDGE_PRESENT != ORDERING_TRUE
SAME_PROCESS_SCOPE_TIME != SAME_ROUTE_BINDING
ALTERNATIVE_ROUTE_ORDERINGS != ONE_PROCESS_CYCLE
STAGE_TYPE_CYCLE != EVENT_INSTANCE_CYCLE
PROVENANCE_PRESERVED != ORDERING_CONSISTENT
SUPPORTED_EDGES != VALID_DAG
CYCLIC_PRECEDENCE != COMPUTABLE_CRITICAL_PATH
CYCLIC_REPRESENTED_ORDERING != WORLD_DEADLOCK_PROVEN
```

Contradictory/cyclic ordering or unresolved binding/acyclicity blocks that **critical-path proof route** to a strong window status; it does not invalidate separate domain-supported timing evidence.

A precedence critical path may be an optimistic structural bound, not feasible completion time.

```text
NO_PRECEDENCE_EDGE != CONCURRENCY_AVAILABLE
STRUCTURAL_PARALLELISM != FEASIBLE_PARALLELISM
PRECEDENCE_GRAPH_COMPLETE != EXECUTION_FEASIBILITY_COMPLETE
ACYCLIC_SUPPORTED != FEASIBLE_SCHEDULE_ESTABLISHED
```

If assumed overlap changes the conclusion, require support that execution constraints permit it; otherwise use a domain-supported feasible bound or preserve `UNKNOWN`. Existing coupling/control/constraint/route/capability structure carries material shared capacity; no resource ontology is added.

## [9.2] Target boundary

A strong window comparison requires an explicit represented condition for what counts as the relevant close/hardening boundary for the stated scope and capability context. Where load-bearing preserve target/scope, boundary condition, selector/source/basis, freeze time where outcome-informed choice matters, observation measure, capability/route context and material disputes/alternatives.

```text
TARGET_BOUNDARY_TIME_REQUIRES_REPRESENTED_BOUNDARY_CONDITION
BOUNDARY_CONDITION_DECLARED != BOUNDARY_CONDITION_JUSTIFIED
BOUNDARY_CONDITION_JUSTIFIED != MORAL_ADEQUACY
THRESHOLD_SELECTED_AFTER_RESULT != PREDECLARED_BOUNDARY
UNREACHABLE_BY_DECLARED_ROUTE_SET != WORLD_IRREVERSIBLE
NO_KNOWN_ALTERNATIVE_ROUTE != WORLD_IRREVERSIBLE
```

TRACE exposes the boundary choice; it does not choose moral adequacy.

## [9.3] Temporal basis / interval status

Same units do not establish the same clock. Before joining times, bind a supported common temporal origin/basis or supported conversion, including material uncertainty.

```text
SAME_UNIT != SAME_REFERENCE_EVENT
NUMERICALLY_COMPARABLE != TEMPORALLY_COMPARABLE
CONVERSION_DECLARED != CONVERSION_SUPPORTED
```

For a guaranteed-open claim require a supported feasible-completion upper bound and target-boundary lower bound under the same represented process bindings:

```text
lower_boundary > upper_feasible
  -> GUARANTEED_OPEN_FOR_REPRESENTED_BINDINGS
```

```text
POINT_ESTIMATE_FITS != GUARANTEED_OPEN
OPTIMISTIC_COMPLETION_FITS != GUARANTEED_OPEN
OVERLAPPING_TIME_BOUNDS != WINDOW_FITS
```

For closure, a supported lower bound on required feasible completion may establish closed if even the optimistic required path is too late:

```text
upper_boundary <= lower_required_completion
  -> GUARANTEED_CLOSED_FOR_REPRESENTED_BINDINGS
```

Do not use that rule while a represented alternative/substitution can make the path non-required. Otherwise return `WINDOW_STATUS_UNKNOWN`.

## [9.4] Multiple boundaries / rebinding

```text
MULTIPLE_LOAD_BEARING_BOUNDARIES != ONE_UNQUALIFIED_CLOSE
```

Rebind a window claim when a load-bearing target, boundary condition, capability/route scope, temporal basis, execution constraint or target process changes.

```text
PAST_WINDOW_FIT != CURRENT_WINDOW_FIT
```

## [9.5] Serial shorthand

Only as a bounded derived special case, when required stages are genuinely sequential and comparably timed:

```text
T_detect + T_route + T_correct < T_boundary
```

Required verification time is not free.

```text
REQUIRED_CHECK_TIME != ZERO_DURATION
LOAD_BEARING_CHECK != FREE_CHECK
```

---

---

## Beta3 review question

Does this profile preserve a consequential distinction the compact [9] loses in a real case? If not, keep it out of the spine. If a stronger external timing method handles the case with less effort, hand off to that method.
