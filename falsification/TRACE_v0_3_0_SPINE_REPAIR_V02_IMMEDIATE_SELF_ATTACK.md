# TRACE v0.3.0 — SPINE REPAIR v0.2 IMMEDIATE SELF-ATTACK

**Status:** MATERIAL FINDINGS — v0.2 HELD AS WRITTEN  
**Target:** `PROJECT/TRACE_v0_3_0_SPINE_REPAIR_CANDIDATE_v0_2.md`  
**Frozen target commit:** `aa411f31956e57db346e5219ee318ec27b702b83`  
**Disposition:** REPAIR, NOT DELETE — both findings recover donor/existing dependency discipline; no new primitive earned.

---

# Finding 1 — interval-safe arithmetic still fails if the clocks do not share a reference

The v0.2 repair correctly restores interval comparisons:

```text
lower(I_boundary) > upper(I_complete)
  -> GUARANTEED_OPEN_FOR_REPRESENTED_BINDINGS
```

But it does not explicitly require the two intervals to be expressed on a common time reference or connected by an explicit conversion relation.

## Counterexample

Suppose the candidate is instantiated as:

```text
I_complete = [8,10] minutes after detection
I_boundary = [11,13] minutes after authorization
```

The raw interval rule returns:

```text
11 > 10 -> GUARANTEED_OPEN
```

Now represent one omitted fact:

```text
detection occurs [6,7] minutes after authorization
```

Then completion is actually:

```text
[14,17] minutes after authorization
```

which no longer fits before boundary `[11,13]`.

The arithmetic was correct over incomparable coordinates.

Preserve:

```text
NUMERICALLY_COMPARABLE != TEMPORALLY_COMPARABLE
SAME_UNIT != SAME_REFERENCE_EVENT
INTERVAL_BOUNDS != COMMON_CLOCK_BASIS
CLOCK_TYPED != CLOCKS_JOINABLE
```

## Classification

This is donor recovery from v0.2.7 clock typing / reference-event discipline plus Root C verification/process binding and Root A warrant.

No new `CLOCK_REFERENCE` primitive is required. The repair must require, where a timing comparison is load-bearing:

```text
reference event / origin
unit / scale
clock/source or conversion relation
interval semantics
```

or else return timing/window status `UNKNOWN` for that comparison.

---

# Finding 2 — source mutation is not automatically claim invalidation

The v0.2 repair says freshness may expire by source mutation and suggests preserving the invalidation basis.

That is directionally useful but too broad if a receiver treats any source mutation as invalidating every derivation from that source.

## Counterexample

A source object contains:

```text
A: machine temperature
B: operator display preference
```

A derived claim depends only on `A`:

```text
claim = temperature < 80 C
```

The source mutates only `B`:

```text
display preference: compact -> expanded
```

The source changed. The load-bearing derivation did not.

A blanket rule:

```text
SOURCE_MUTATED -> DERIVED_VALUE_NOT_CURRENT
```

would create false staleness and unnecessary reacquisition.

Preserve:

```text
SOURCE_MUTATED != LOAD_BEARING_DEPENDENCY_CHANGED
LOAD_BEARING_DEPENDENCY_CHANGED != DERIVED_PROPOSITION_CHANGED
MUTATION_OBSERVED != CLAIM_INVALIDATED
```

The useful rule is dependency-relative:

- if the represented mutation can alter a dependency used by the derivation, currentness may need reacquisition/recomputation;
- if the mutation is represented as outside the derivation dependency, it need not invalidate the claim;
- if relevance of the mutation to the derivation cannot be established, preserve that uncertainty rather than upgrading either to `CURRENT` or `STALE`.

## Classification

This is existing dependency-path / claim-evidence discipline, not a new freshness ontology.

---

# Result

```text
SPINE_REPAIR_v0_2:              HOLD AS WRITTEN
NEW PRIMITIVE:                  NO
NEW ROOT:                       NO
FINDING 1:                      MATERIAL / DONOR CLOCK RECOVERY
FINDING 2:                      MATERIAL / DEPENDENCY-SCOPED FRESHNESS REPAIR
CORRECTION-WINDOW DIRECTION:    SURVIVES WITH COMMON-TIME BINDING REQUIRED
MUTATION-RELATIVE FRESHNESS:    SURVIVES WITH DEPENDENCY BINDING REQUIRED
```

The next candidate should repair only these two defects and preserve the rest of v0.2 unchanged unless another attack earns a change.
