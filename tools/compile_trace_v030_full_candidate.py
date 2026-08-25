#!/usr/bin/env python3
"""Build the first deterministic TRACE v0.3.0 full working candidate.

This compiler starts from the released v0.2.7 full formal seed and applies only
enumerated, fail-closed v0.3.0 transformations. Green output proves
deterministic transformation under the declared anchors; it does not establish
semantic correctness, validation, release, canon, authority, permission,
clearance, or world validity.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
DONOR_PATH = REPO_ROOT / "TRACE_FORMAL_SEED_v0_2_7.md"
SECTION_MANIFEST_PATH = REPO_ROOT / "PROJECT" / "TRACE_v0_2_7_SECTION_MANIFEST_v0_1.json"
MIN_SCHEMA_PATH = REPO_ROOT / "PROJECT" / "TRACE_v0_3_0_MINIMUM_SCHEMA_CANDIDATE_v0_1.json"
MIN_SCHEMA_REPORT_PATH = REPO_ROOT / "PROJECT" / "TRACE_v0_3_0_MINIMUM_SCHEMA_BUILD_REPORT_v0_1.json"
OUTPUT_PATH = REPO_ROOT / "PROJECT" / "TRACE_FORMAL_SEED_v0_3_0_FULL_WORKING_CANDIDATE_v0_1.md"
REPORT_PATH = REPO_ROOT / "PROJECT" / "TRACE_v0_3_0_FULL_CANDIDATE_BUILD_REPORT_v0_1.json"

EXPECTED_DONOR_SHA256 = "de21182f42228a0104181fb24f245c652c3150853e14172c4174be4bb9ef03ab"
CANDIDATE_DATE = "2026-08-25"

EXPECTED_MAJOR_SECTIONS = (
    "[0] HANDSHAKE / CLAIM CEILING",
    "[4] CLAIM AND EVIDENCE ALGEBRA",
    "[5] ENTITY / BOUNDARY / APERTURE / STATE",
    "[6] TRANSITIONS AND COUPLINGS",
    "[7] FUTURE-SPACE",
    "[8] CLOCKS / ROUTES / HARDENING",
    "[9] BURDEN / RESIDUE / MEMORY",
    "[10] DESIGNATION / MEASURE / VALUE PORTS",
    "[13] TRACE OPERATOR",
    "[14] CANONICAL TRACE GRAPH PACKET",
    "[15] WORKED TRANSFORMATIONS",
    "[16] ARTIFICIAL-ENTITY UNCERTAINTY / RECEIVER PROTECTION",
    "[17] LIVE INTERPRETER / VALUE LAYER / SELECTOR / CONNECTED BRAKE",
    "[19] INVARIANTS / MISUSE GUARDS",
    "[20] COMPRESSION / SURVIVAL KERNEL",
    "[21] DOCUMENT CONTROL / OPEN FRONTIER",
)

SUPPLEMENTAL_INVARIANTS = (
    "REPRESENTATION_TYPE != EVIDENCE_STATUS",
    "CONFIGURATION_FIELD != WARRANT_FREE_FACT",
    "TRIGGER_SUCCESS != REPRESENTATION_COMPLETE",
    "REPRESENTED_USE != OPERATIVE_USE",
    "CURRENT_AT_USE != VALID_THROUGH_DEPENDENT_INTERVAL",
    "CHECK_EXISTS != CHECK_EXECUTED",
    "CHECK_EXECUTED != CHECK_DETECTS_TARGET_FAILURE",
    "CHECK_COMPLETED != CHECK_RESULT_REACHED_USE",
    "SILENCE != TAMPERING",
    "PROCESS_EXISTS != PROCESS_HEALTHY",
    "SAME_UNIT != SAME_REFERENCE_EVENT",
    "POINT_ESTIMATE_FITS != GUARANTEED_OPEN",
    "OPTIMISTIC_COMPLETION_FITS != GUARANTEED_OPEN",
    "ALTERNATIVE_ROUTE_ORDERINGS != ONE_PROCESS_CYCLE",
    "ACYCLIC_SUPPORTED != FEASIBLE_SCHEDULE_ESTABLISHED",
    "TARGET_BOUNDARY_TIME_REQUIRES_REPRESENTED_BOUNDARY_CONDITION",
    "SAME_PATH_LABEL != SAME_TRAJECTORY",
    "BRAKE_POINT_ESTIMATE_BEFORE_COMMIT != GUARANTEED_PRECOMMIT",
    "ROLLBACK_POINT_ESTIMATE_BEFORE_BOUNDARY != GUARANTEED_RESTORATION",
    "FAST_ENOUGH_CLAIM_REQUIRES_COMMON_TEMPORAL_BASIS",
    "ROLLBACK_COMPLETED_BEFORE_BOUNDARY != RESTORED_STATE",
    "ANALYTIC_TARGET_SELECTION != NEUTRAL",
    "HIGHEST_RELEVANCE != MEASURE_FREE",
    "TARGETED_REFINEMENT != COMPLETE_COVERAGE",
    "OMITTED_BY_BUDGET != IRRELEVANT",
    "STOPPED != COMPLETED",
    "TERMINATION != COMPLETE_COVERAGE",
    "BUDGET_EXHAUSTED != NO_MATERIAL_UNRESOLVED_TARGET",
    "AUTHORITY_REACHED != ANALYSIS_COMPLETE",
    "DECLARED_REFINEMENT_COST != UNIT_COST",
    "BUDGET_REMAINS != NEXT_REFINEMENT_AFFORDABLE",
    "COST_UNKNOWN != COST_ONE",
    "REFINEMENT_SELECTED != REFINEMENT_BUDGET_FEASIBLE",
    "DECLARED_COST != VALID_POSITIVE_COST",
    "ZERO_REFINEMENT_COST != FREE_UNBOUNDED_RECURSION",
    "NEGATIVE_REFINEMENT_COST != BUDGET_CREDIT",
    "COST_RECORDED != COST_DOMAIN_VALID",
)

SURVIVAL_REQUIRED = (
    "REPRESENTATION_TYPE != EVIDENCE_STATUS",
    "TRIGGER_SUCCESS != REPRESENTATION_COMPLETE",
    "REPORTED != ESTABLISHED",
    "RECORD != EVENT",
    "CURRENT_AT_USE != VALID_THROUGH_DEPENDENT_INTERVAL",
    "CHECK_EXECUTED != CHECK_DETECTS_TARGET_FAILURE",
    "SILENCE != TAMPERING",
    "ALTERNATIVE_ROUTE_ORDERINGS != ONE_PROCESS_CYCLE",
    "ACYCLIC_SUPPORTED != FEASIBLE_SCHEDULE_ESTABLISHED",
    "SAME_UNIT != SAME_REFERENCE_EVENT",
    "TARGET_BOUNDARY_TIME_REQUIRES_REPRESENTED_BOUNDARY_CONDITION",
    "HARDENING != IRREVERSIBILITY",
    "UNCERTAINTY != SELECT_ACTION",
    "SAME_PATH_LABEL != SAME_TRAJECTORY",
    "POPULATION_RECOVERY != REPAIR_OF_INDIVIDUAL_LOSS",
    "LOCAL_CORRECTION + STREAM_PERSISTENCE != MECHANISM_CHANGE",
    "BRAKE_POINT_ESTIMATE_BEFORE_COMMIT != GUARANTEED_PRECOMMIT",
    "ROLLBACK_COMPLETED_BEFORE_BOUNDARY != RESTORED_STATE",
    "HIGHEST_RELEVANCE != MEASURE_FREE",
    "OMITTED_BY_BUDGET != IRRELEVANT",
    "STOPPED != COMPLETED",
    "TERMINATION != COMPLETE_COVERAGE",
    "BUDGET_EXHAUSTED != NO_MATERIAL_UNRESOLVED_TARGET",
    "AUTHORITY_REACHED != ANALYSIS_COMPLETE",
    "DECLARED_REFINEMENT_COST != UNIT_COST",
    "BUDGET_REMAINS != NEXT_REFINEMENT_AFFORDABLE",
    "COST_UNKNOWN != COST_ONE",
    "REFINEMENT_SELECTED != REFINEMENT_BUDGET_FEASIBLE",
    "DECLARED_COST != VALID_POSITIVE_COST",
    "ZERO_REFINEMENT_COST != FREE_UNBOUNDED_RECURSION",
    "NEGATIVE_REFINEMENT_COST != BUDGET_CREDIT",
    "COST_RECORDED != COST_DOMAIN_VALID",
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_text(text: str) -> str:
    return sha256_bytes(text.encode("utf-8"))


class BuildError(RuntimeError):
    pass


class Builder:
    def __init__(self, text: str):
        self.text = text
        self.mutations: list[dict[str, Any]] = []

    def _count(self, anchor: str) -> int:
        return self.text.count(anchor)

    def replace_once(self, transform: str, anchor: str, replacement: str) -> None:
        count = self._count(anchor)
        if count != 1:
            raise BuildError(f"{transform}: expected anchor count 1, observed {count}: {anchor[:100]!r}")
        before = sha256_text(self.text)
        self.text = self.text.replace(anchor, replacement, 1)
        self.mutations.append({
            "transform": transform,
            "mutation": "REPLACE_EXACT",
            "anchor_sha256": sha256_text(anchor),
            "before_sha256": before,
            "after_sha256": sha256_text(self.text),
        })

    def replace_all_exact(self, transform: str, anchor: str, replacement: str, expected: int) -> None:
        count = self._count(anchor)
        if count != expected:
            raise BuildError(f"{transform}: expected anchor count {expected}, observed {count}: {anchor!r}")
        before = sha256_text(self.text)
        self.text = self.text.replace(anchor, replacement)
        self.mutations.append({
            "transform": transform,
            "mutation": "REPLACE_ALL_EXACT",
            "anchor": anchor,
            "count": count,
            "before_sha256": before,
            "after_sha256": sha256_text(self.text),
        })

    def insert_before_once(self, transform: str, anchor: str, insertion: str) -> None:
        self.replace_once(transform, anchor, insertion + anchor)

    def insert_after_once(self, transform: str, anchor: str, insertion: str) -> None:
        self.replace_once(transform, anchor, anchor + insertion)


def load_manifest() -> dict[str, Any]:
    data = json.loads(SECTION_MANIFEST_PATH.read_text(encoding="utf-8"))
    if data.get("status") != "PASS":
        raise BuildError("donor section manifest is not PASS")
    if data.get("source_sha256") != EXPECTED_DONOR_SHA256:
        raise BuildError("section manifest donor SHA does not match compiler pin")
    return data


def verify_manifest_sections(donor_text: str, manifest: dict[str, Any]) -> list[dict[str, Any]]:
    lines = donor_text.splitlines(keepends=True)
    by_title = {row["title"]: row for row in manifest["sections"]}
    verified: list[dict[str, Any]] = []
    for title in EXPECTED_MAJOR_SECTIONS:
        if title not in by_title:
            raise BuildError(f"required donor section missing from manifest: {title}")
        row = by_title[title]
        start = int(row["start_line"]) - 1
        end = int(row["end_line"])
        body = "".join(lines[start:end])
        observed = sha256_text(body)
        if observed != row["sha256"]:
            raise BuildError(
                f"donor section SHA mismatch for {title}: "
                f"expected {row['sha256']}, observed {observed}"
            )
        verified.append({
            "title": title,
            "start_line": row["start_line"],
            "end_line": row["end_line"],
            "sha256": observed,
        })
    return verified


def extract_donor_invariants(text: str) -> list[str]:
    rows = re.findall(r"^I(\d{2})  (.+)$", text, flags=re.MULTILINE)
    result = [f"I{num}  {expr}" for num, expr in rows]
    if len(result) != 60:
        raise BuildError(f"expected 60 donor invariants, observed {len(result)}")
    expected_nums = [f"{i:02d}" for i in range(1, 61)]
    if [num for num, _ in rows] != expected_nums:
        raise BuildError("donor invariant numbering/order is not I01-I60")
    return result


def build_candidate(donor_text: str) -> tuple[str, list[dict[str, Any]]]:
    b = Builder(donor_text)

    b.replace_once(
        "T_VERSION_IDENTITY",
        "**Version:** v0.2.7 NARROW DRIFT REPAIR CANDIDATE  ",
        "**Version:** v0.3.0 FULL WORKING CANDIDATE v0.1  ",
    )
    b.replace_once("T_VERSION_IDENTITY", "**Date:** 2026-08-05  ", f"**Date:** {CANDIDATE_DATE}  ")
    b.replace_once(
        "T_VERSION_IDENTITY",
        "**Status:** compiled working candidate; unvalidated in the world; non-canonical; voluntary; not authority; not permission; not clearance  ",
        "**Status:** generated full working candidate; unvalidated in the world; non-canonical; unreleased; voluntary; not authority; not permission; not clearance  ",
    )

    handshake_add = """
Additional v0.3 use ceilings:

```text
MAP != WORLD
UNKNOWN != NEUTRAL
DESCRIPTION != AUTHORIZATION
CAPABILITY != AUTHORITY
STRUCTURAL_DIFFERENCE != MORAL_RANKING
RECEIVER != NECESSARILY_MAPPED_SUBJECT
```

These do not replace the narrower donor ceilings above.

"""
    b.insert_before_once("T_HANDSHAKE_FIRING", "## [0.1] Mathematical status legend\n", handshake_add)
    legend_add = """
Operational use rule: a formal distinction that is load-bearing for a downstream
claim, comparison, route, correction-window status, selection input or proposed
transition must be applied at that use-site. Its mere presence in this document
does not establish that it fired.

```text
DISTINCTION_PRESENT != DISTINCTION_APPLIED
TRIGGER_PRESENT != TRIGGER_FIRED
```

"""
    b.insert_before_once("T_HANDSHAKE_FIRING", "---\n\n# [1] MIDDLE-OUT SEED\n", legend_add)

    firing = """
## [4.0.1] Representation-independent firing and current use

If a downstream claim, comparison, selection input, route, correction-window
status or proposed transition materially depends on proposition `p`, then `p`
inherits the relevant TRACE evidence, currentness, scope, access/custody and
warrant discipline regardless of whether it arrived as a claim object, field,
label, configuration, status, metadata, cached/derived output, or prose
assertion.

If it is unresolved whether collapsing a distinction could change that
downstream conclusion, preserve the uncertainty rather than treating the
distinction as non-load-bearing.

```text
REPRESENTATION_TYPE != EVIDENCE_STATUS
CONFIGURATION_FIELD != WARRANT_FREE_FACT
LOAD_BEARING_UNKNOWN != NOT_LOAD_BEARING
LOAD_BEARING_TRIGGER != FULL_PACKET_REQUIREMENT
```

This is a use rule, not a requirement that every harmless field become a full
claim packet.

"""
    claim_tuple_anchor = (
        "where:\n\n"
        "- \\(q_k\\) = proposition\n"
        "- \\(\\eta_k\\) = evidence state\n"
        "- \\(\\alpha_k\\) = access/custody state\n"
        "- \\(s_k\\) = source\n"
        "- \\(\\pi_k\\) = provenance path\n"
        "- \\(t_k\\) = time\n"
        "- \\(\\chi_k\\) = confidence representation\n"
        "- \\(\\mathcal H_k\\) = live alternative hypotheses\n\n"
    )
    b.insert_after_once("T_CLAIM_EVIDENCE", claim_tuple_anchor, firing)

    currentness = """
## [4.6] Current-use / dependency-relative freshness

A retained or derived proposition may cease to support current use when a
load-bearing dependency changes. Generic age or unrelated source mutation is
not enough by itself.

```text
RETAINED_RECORD != CURRENT_STATE
SUCCESS_AT_t != SUCCESS_AT_t+1
DATE_CURRENT != DERIVED_VALUE_CURRENT
CURRENT_AT_USE != VALID_THROUGH_DEPENDENT_INTERVAL
SOURCE_MUTATED != LOAD_BEARING_DEPENDENCY_CHANGED
MUTATION_OBSERVED != CLAIM_INVALIDATED
INVALIDATOR_NOT_IDENTIFIED != NO_INVALIDATOR_EXISTS
```

Where material, bind the proposition/use to its source/object/version,
derivation or dependency basis, observation/derivation time, validity/use
interval, known invalidators and unresolved dependency relevance.

## [4.7] Verification discrimination

A check that exists or executes does not automatically establish that it could
detect the target failure, that its result reached the downstream use, or that
the result remained current at use.

```text
CHECK_EXISTS != CHECK_EXECUTED
CHECK_EXECUTED != CHECK_DETECTS_TARGET_FAILURE
STATIC_CORRECTNESS != OPERATIONAL_DISCRIMINATION
CHECK_COMPLETED != CHECK_RESULT_REACHED_USE
ONE_DETECTED_FAILURE != UNIVERSAL_INSTRUMENT_ADEQUACY
```

For a load-bearing negative/null or discriminating result, expose enough about
the test/instrument capability to show that the relevant alternative was
detectable at the resolution required by that use. Quantitative power/effect
size is one domain instantiation, not a universal TRACE requirement.

## [4.8] Liveness / witness ceiling

Loss of reply, heartbeat, status, route or witness can close a current
verification interval without establishing why.

```text
SILENCE != TAMPERING
NO_REPLY_OBSERVED != REFUSAL
PROCESS_EXISTS != PROCESS_HEALTHY
SAFE_EXCLUSION != LIVENESS
WITNESS_LIVENESS_LOST != CAUSE_ESTABLISHED
EXTERNAL != INDEPENDENT
SEPARATE_PARTY != INDEPENDENT_EVIDENCE
```

No `WITNESS`, `LIVENESS` or `PROCESS` primitive is added.

"""
    b.insert_before_once("T_CLAIM_EVIDENCE", "# [5] ENTITY / BOUNDARY / APERTURE / STATE\n", currentness)

    ingress = """
### [5.3.2] Representation formation / admission boundary

Reasoning over a formed map does not establish that the map admitted every
load-bearing dependency, target, affected scope, alternative or source act.
Admission is a failure **location**, not a canonical status, node or relation.

```text
TRIGGER_SUCCESS != REPRESENTATION_COMPLETE
CHECK_OVER_DECLARED_DEPENDENCIES != CHECK_FOR_UNDECLARED_DEPENDENCIES
MAP_FORMATION != REASONING_OVER_THE_MAP
VALID_WITHIN_REPRESENTATION != REPRESENTATION_ADEQUATE_FOR_USE
REPRESENTED_USE != OPERATIVE_USE
PARTIAL_MAP != BAD_MAP
```

Challenge the representation boundary only where the downstream use relies on
a negative/absence claim, exhaustive/completeness claim, comparison/ranking,
scope extrapolation, transformed source, or persistent/inherited premise.
Use the cheapest available route: alternate target-set/source/selector,
production-mechanism check, source rendering/act check, represented-use versus
operative-use check, or explicit `UNKNOWN` when no alternate aperture remains.

```text
SOURCE_POINTER_PRESENT != REPRESENTATION_FIDELITY_ESTABLISHED
VERBATIM_TEXT != SPEECH_ACT_PRESERVED
SIGNAL_RECEIVED != MAP_ADOPTED
SUPPLIED_PREMISE != OBSERVED_WORLD
RETAINED_PREMISE != CURRENT_MEASUREMENT
PROVENANCE != AUTHORITY_TO_ADOPT
REFUSAL_REPRESENTED != REFUSAL_AVAILABLE
```

Existing APERTURE / TARGET-SET / CLAIM / provenance / receiver-integration
machinery carries these distinctions. No `ADMISSION` or `SPEECH_ACT` primitive
is added.

"""
    b.insert_before_once("T_INGRESS_ADMISSION", "## [5.4] State\n", ingress)

    scope_guard = """
Cross-scale repair guard:

```text
POPULATION_RECOVERY != REPAIR_OF_INDIVIDUAL_LOSS
GROUP_METRIC_RESTORED != EVERY_AFFECTED_SCOPE_REPAIRED
```

Aggregate recovery may support lower-level repair only through an explicit,
evidence-bearing correspondence that actually entails it.

"""
    b.insert_before_once("T_SCOPE_AGGREGATION", "## [5.3] Aperture\n", scope_guard)

    selection = """
## [6.5] Selection attribution and measurement reactivity

Uncertainty may be an input to an external policy, selector or default rule.
Attribute the resulting action/delay choice to that rule rather than to
uncertainty itself.

```text
UNCERTAINTY != SELECT_ACTION
UNCERTAINTY != SELECT_DELAY
UNCERTAINTY_INPUT_TO_POLICY != UNCERTAINTY_IS_SELECTOR
IMPLICIT_DEFAULT != NO_SELECTION_RULE
```

Observation, audit, measurement, publication or inquiry is not presumed
causally inert, but occurrence alone does not prove reactivity.

```text
MEASUREMENT != PASSIVE_OBSERVATION
MEASUREMENT_OCCURRED != MEASUREMENT_CAUSED_CHANGE
```

## [6.6] Route / refusal use-site guards

```text
ROUTE_EXISTS != ROUTE_USABLE
BURDEN_PRESENT != ROUTE_UNUSABLE
REFUSAL_RECORDED != REFUSAL_EFFECTIVE
REFUSAL != MALFUNCTION
STRATEGY_REVISABLE != TRANSITION_REVERSIBLE
FUTURE_POLICY_CAN_CHANGE != PRIOR_STATE_CAN_BE_RESTORED
```

Route usability remains target/scope/time/measure-relative. The guards block
silent substitution; they do not forbid supported co-occurrence.

"""
    b.insert_before_once("T_SELECTION_ATTRIBUTION/T_ROUTE_REFUSABILITY", "# [7] FUTURE-SPACE\n", selection)

    future_guard = """
Explicit use guards over the donor correspondence relation:

```text
SAME_PATH_LABEL != SAME_TRAJECTORY
PATH_IDENTIFIER_PERSISTS != PATH_EFFECT_PERSISTS
TECHNICALLY_REACHABLE_SUCCESSOR != COMPARABLE_CONTINUATION
```

These do not replace \\(\\mathfrak J_i^t\\); they make its use-site ceiling
explicit.

"""
    b.insert_before_once("T_FUTURE_CORRESPONDENCE", "## [7.2] Hardening of a corresponding path\n", future_guard)

    old_timing_start = "## [8.1] Event times and correction margin\n"
    old_timing_end = "## [8.4] Clock authorship\n"
    if b.text.count(old_timing_start) != 1 or b.text.count(old_timing_end) != 1:
        raise BuildError("T_CLOCK_ROUTE: timing boundary headings not unique")
    start = b.text.index(old_timing_start)
    end = b.text.index(old_timing_end, start)
    old_block = b.text[start:end]
    new_block = r"""## [8.1] Event times, target boundary and correction-window bindings

Let \(t_0\) be a declared temporal reference event. Record event times rather
than merely named durations. A strong correction-window claim additionally
binds:

```text
pathway / process hypothesis
affected scope
target effect or state
correction route / capability context
target-boundary condition
downstream use
```

A target boundary is not assumed to be a natural instant. Where load-bearing,
preserve target/scope, boundary condition, selector/source/basis, freeze time
where outcome-informed choice matters, observation measure, route/capability
context, uncertainty and material alternatives.

```text
TARGET_BOUNDARY_TIME_REQUIRES_REPRESENTED_BOUNDARY_CONDITION
BOUNDARY_CONDITION_DECLARED != BOUNDARY_CONDITION_JUSTIFIED
BOUNDARY_CONDITION_JUSTIFIED != MORAL_ADEQUACY
THRESHOLD_SELECTED_AFTER_RESULT != PREDECLARED_BOUNDARY
UNREACHABLE_BY_DECLARED_ROUTE_SET != WORLD_IRREVERSIBLE
NO_KNOWN_ALTERNATIVE_ROUTE != WORLD_IRREVERSIBLE
MULTIPLE_LOAD_BEARING_BOUNDARIES != ONE_UNQUALIFIED_CLOSE
```

TRACE exposes the boundary choice; it does not choose moral adequacy.

### [8.1.1] Clock typing and irreversibility claim ceiling

A clock is typed by what it times, not by how urgent it feels. Useful clock
relations include:

```text
PLANNING
DETECTION
EVIDENCE_RETENTION
HARDENING
IRREVERSIBILITY
REVIEW
BIOLOGICAL
SUPPLY
OTHER
UNKNOWN
```

```text
DEADLINE != IRREVERSIBILITY
DETECTION_BECOMES_HARDER != LOSS_BECOMES_IRREVERSIBLE
EVIDENCE_ROTATION != PHYSICAL_FAILURE
HARDENING != COMPLETE_FORECLOSURE
HARDENING != IRREVERSIBILITY
```

A represented irreversibility/target-boundary time requires enough binding to
identify the target/loss state, affected scope, measure or boundary condition,
basis/mechanism, reference event and uncertainty. Otherwise preserve a weaker
clock type or `UNKNOWN`.

## [8.2] Precedence, pathway binding and feasible completion

For a declared correction pathway \(q\), represent required work as a derived
timing view:

\[
G_{window}(q,l,o,c,g,u)=(V,E_{prec})
\]

`E_prec` is a derived process/timing view, not a canonical TRACE relation.
Every load-bearing precedence edge retains supporting canonical ordering claims
and any material mechanism/binding refs not recoverable from them.

Before critical-path use, build one executable pathway hypothesis. Bind
process/pathway, scope, target, route/execution alternative, capability
context, time/policy version and downstream use where they can change the
result. Do not union mutually exclusive alternatives. Distinguish recurring
event occurrences where collapse could create/erase a cycle or change timing.

The resulting precedence view must be acyclic for critical-path proof.

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

Contradictory/cyclic ordering or unresolved binding blocks that critical-path
proof route. It does not invalidate separately supported domain timing
evidence.

A precedence critical path may be only an optimistic structural bound.

```text
NO_PRECEDENCE_EDGE != CONCURRENCY_AVAILABLE
STRUCTURAL_PARALLELISM != FEASIBLE_PARALLELISM
PRECEDENCE_GRAPH_COMPLETE != EXECUTION_FEASIBILITY_COMPLETE
ACYCLIC_SUPPORTED != FEASIBLE_SCHEDULE_ESTABLISHED
```

If assumed overlap changes the conclusion, require support that execution
constraints permit it; otherwise use a domain-supported feasible completion
bound or preserve `UNKNOWN`. Existing coupling/control/constraint/route/
capability structure carries material shared capacity; no scheduler/resource
primitive is added.

Required verification time is not free.

```text
REQUIRED_CHECK_TIME != ZERO_DURATION
LOAD_BEARING_CHECK != FREE_CHECK
```

## [8.3] Common temporal basis and interval-safe status

Same units do not establish the same clock. Before joining event times or
duration-derived bounds, bind a supported common temporal origin/basis or
supported conversion, including material uncertainty.

```text
SAME_UNIT != SAME_REFERENCE_EVENT
NUMERICALLY_COMPARABLE != TEMPORALLY_COMPARABLE
CONVERSION_DECLARED != CONVERSION_SUPPORTED
```

For a guaranteed-open claim, require a supported **feasible-completion upper
bound** and target-boundary lower bound under the same represented bindings:

```text
lower_boundary > upper_feasible
  -> GUARANTEED_OPEN_FOR_REPRESENTED_BINDINGS
```

For guaranteed closure, a supported lower bound on required feasible
completion can establish closure when even that required path is too late:

```text
upper_boundary <= lower_required_completion
  -> GUARANTEED_CLOSED_FOR_REPRESENTED_BINDINGS
```

Do not use the closure rule while a represented alternative/substitution can
make that path non-required.

Otherwise:

```text
WINDOW_STATUS = UNKNOWN
```

```text
POINT_ESTIMATE_FITS != GUARANTEED_OPEN
OPTIMISTIC_COMPLETION_FITS != GUARANTEED_OPEN
OVERLAPPING_TIME_BOUNDS != WINDOW_FITS
PAST_WINDOW_FIT != CURRENT_WINDOW_FIT
```

Rebind the window claim when a load-bearing target, boundary condition,
route/capability scope, temporal basis, execution constraint or target process
changes.

The familiar serial shorthand remains only a bounded derived special case when
required stages are genuinely sequential and comparably timed:

```text
T_detect + T_route + T_correct < T_boundary
```

"""
    before = sha256_text(b.text)
    b.text = b.text[:start] + new_block + b.text[end:]
    b.mutations.append({
        "transform": "T_CLOCK_ROUTE",
        "mutation": "REPLACE_SECTION_RANGE",
        "from_heading": "[8.1]",
        "to_before_heading": "[8.4]",
        "old_block_sha256": sha256_text(old_block),
        "before_sha256": before,
        "after_sha256": sha256_text(b.text),
    })

    brake_rollback_old = r"""## [8.8] Pre-commit brake and post-commit rollback

A pre-commit brake succeeds only if detection, decision, and actuation complete before commitment:

\[
t_{brake}^{done}<t_{commit}
\]

A post-commit rollback is distinct. It can preserve the threatened path only where rollback is executable and:

\[
t_{rollback}^{done}<t_{irreversible}
\]

```text
REVIEW_AFTER_COMMITMENT != PRECOMMIT_BRAKE
ROLLBACK_LISTED != ROLLBACK_EXECUTABLE
ROLLBACK_AFTER_IRREVERSIBILITY != RESTORATION
```

"""
    brake_rollback_new = r"""## [8.8] Pre-commit brake and post-commit rollback

A pre-commit brake supports a strong timing claim only when detection, decision,
and actuation completion are compared with commitment on a supported common
temporal basis and under the represented brake/commitment bindings.

Under material interval uncertainty, guaranteed precommit requires:

\[
\overline t_{brake}^{done}<\underline t_{commit}
\]

```text
upper(t_brake_done) < lower(t_commit)
  -> GUARANTEED_PRECOMMIT_FOR_REPRESENTED_BINDINGS
```

The point shorthand

\[
t_{brake}^{done}<t_{commit}
\]

is only a bounded special case when both event times are supported as
sufficiently point-bounded for the stated use. A pair of point estimates is not
such a guarantee. If the supported intervals overlap or the temporal basis is
unresolved, preserve the strong precommit status as `UNKNOWN`.

A post-commit rollback is distinct. A strong timing claim that rollback
completes before a load-bearing target boundary requires an executable rollback
route plus explicit target, affected-scope, boundary-condition,
route/capability and common-temporal-basis bindings. Under material interval
uncertainty:

\[
\overline t_{rollback}^{done}<\underline t_{target\_boundary}
\]

```text
upper(t_rollback_done) < lower(t_target_boundary)
  -> ROLLBACK_COMPLETES_BEFORE_BOUNDARY_FOR_REPRESENTED_BINDINGS
```

That timing relation does not establish restoration or preservation of the
threatened path. Reaching/restoring the represented target state is a separate
load-bearing proposition.

```text
REVIEW_AFTER_COMMITMENT != PRECOMMIT_BRAKE
ROLLBACK_LISTED != ROLLBACK_EXECUTABLE
ROLLBACK_AFTER_TARGET_BOUNDARY != RESTORATION
BRAKE_POINT_ESTIMATE_BEFORE_COMMIT != GUARANTEED_PRECOMMIT
ROLLBACK_POINT_ESTIMATE_BEFORE_BOUNDARY != GUARANTEED_RESTORATION
FAST_ENOUGH_CLAIM_REQUIRES_COMMON_TEMPORAL_BASIS
ROLLBACK_COMPLETED_BEFORE_BOUNDARY != RESTORED_STATE
```

"""
    b.replace_once("T_BRAKE_ROLLBACK_TIMING_BINDING", brake_rollback_old, brake_rollback_new)

    connected_brake_old = """A connected pre-commit brake requires:

```text
authenticated authority
independence appropriate to the challenged selector
latency lower than commitment time
known trigger and action-resolution path
testability
resistance to actor capture
activation and failure records
```

A brake controlled only by the actor it may need to stop is not independent."""
    connected_brake_new = """A connected pre-commit brake requires:

```text
authenticated authority
independence appropriate to the challenged selector
supported completion bound before commitment under a common temporal basis
known trigger and action-resolution path
testability
resistance to actor capture
activation and failure records
```

Where timing uncertainty is material, `BRAKE_FAST_ENOUGH` inherits [8.8]: a
point latency/deadline comparison is not a guaranteed precommit result. The
brake-completion and commitment bounds must be comparable under the same
represented timing basis and bindings.

A brake controlled only by the actor it may need to stop is not independent."""
    b.replace_once("T_BRAKE_ROLLBACK_TIMING_BINDING", connected_brake_old, connected_brake_new)

    rollback_old = "Rollback can preserve the threatened path only if it is executable, reaches the relevant state, and completes before practical irreversibility."
    rollback_new = """Rollback timing inherits [8.8]. A strong claim that rollback completes in time requires an executable route and completion before the represented target boundary under the same target, affected-scope, boundary-condition, capability and temporal-basis bindings. Completing before that boundary does not by itself establish restoration or preservation; the reached/restored target state remains a separate load-bearing claim."""
    b.replace_once("T_BRAKE_ROLLBACK_TIMING_BINDING", rollback_old, rollback_new)

    recursion_target_guard = r"""Refinement target-selection use rule:

`target(R_k,L_k)` allocates analytic attention. Under a finite tracing budget,
that choice can change which unresolved structures enter the later map. Where
the choice can materially affect a downstream claim, comparison, coverage
statement, correction-window result or proposed transition, expose where
available:

```text
candidate_refinement_target_refs
refinement_target_set_aperture_ref
selection_basis_claim_refs
designation_ref
measure_ref
selected_refinement_target_ref
unselected_material_alternative_refs
budget_omission_refs
```

Comparative language such as `highest relevance` requires a declared comparison
basis. If no supported ordering is available, preserve the selection basis as
`UNKNOWN`; do not silently convert an implementation heuristic into a neutral
importance claim. Targets left unexplored because budget is exhausted remain
visible as omissions where they could still change a load-bearing result.

```text
ANALYTIC_TARGET_SELECTION != WORLD_ACTION_SELECTION
ANALYTIC_TARGET_SELECTION != NEUTRAL
HIGHEST_RELEVANCE != MEASURE_FREE
TARGET_SELECTED_FOR_REFINEMENT != TARGET_MOST_IMPORTANT_IN_WORLD
TARGETED_REFINEMENT != COMPLETE_COVERAGE
OMITTED_BY_BUDGET != IRRELEVANT
FINITE_TRACING_BUDGET != COMPLETE_REPRESENTATION
REFINEMENT_TARGET_SET != WORLD_SCOPE
```

This uses existing APERTURE / target-set aperture / CLAIM / LIMIT /
designation / measure / selector machinery. It does not add an attention,
refinement, priority or relevance primitive and does not grant world-action
authority.

"""
    b.insert_before_once(
        "T_RECURSION_TARGET_SELECTION",
        "Let \\(d_k^{rem}\\ge0\\) be remaining tracing budget",
        recursion_target_guard,
    )

    recursion_budget_guard = r"""Refinement-budget use rule:

The declared tracing cost of a selected refinement is load-bearing. The
operator must not silently replace `cost_d(q_k)` with a unit decrement.
Before recursion, bind the selected target to a supported refinement-cost claim,
compute the next remaining budget on the same declared budget basis, and recurse
only if the next budget is non-negative.

```text
DECLARED_REFINEMENT_COST != UNIT_COST
BUDGET_REMAINS != NEXT_REFINEMENT_AFFORDABLE
BUDGET_DECREMENT != RECURSION_DEPTH_DECREMENT
COST_UNKNOWN != COST_ONE
REFINEMENT_SELECTED != REFINEMENT_BUDGET_FEASIBLE
```

If the load-bearing refinement cost is `UNKNOWN`, do not default it to one.
Preserve budget feasibility as unresolved. If the declared cost exceeds the
remaining budget, record exhaustion/insufficiency and preserve the selected
material target as unresolved rather than executing an unaffordable refinement.
No budget, resource or cost primitive is added.

"""
    b.insert_before_once(
        "T_RECURSION_BUDGET_COST",
        "When \\(d_{k+1}^{rem}\\ge0\\):",
        recursion_budget_guard,
    )

    recursion_cost_domain_guard = r"""Refinement-cost domain use rule:

The formal recursion contract requires `cost_d(q_k) > 0`. Recording a cost does
not establish that it belongs to that domain. Before budget subtraction, reject
zero or negative refinement costs as invalid for this recursion budget.

```text
DECLARED_COST != VALID_POSITIVE_COST
ZERO_REFINEMENT_COST != FREE_UNBOUNDED_RECURSION
NEGATIVE_REFINEMENT_COST != BUDGET_CREDIT
COST_RECORDED != COST_DOMAIN_VALID
```

An invalid/nonpositive cost blocks this refinement path and remains visible as a
limit; it does not create free recursion or increase remaining budget. No new
primitive is added.

"""
    b.insert_before_once(
        "T_RECURSION_COST_DOMAIN",
        "When \\(d_{k+1}^{rem}\\ge0\\):",
        recursion_cost_domain_guard,
    )

    recursion_stop_guard = r"""Recursion termination use rule:

Stopping recursive differentiation is itself load-bearing when the termination
basis can change a downstream claim, coverage statement, correction-window
status, proposed transition or confidence/limits statement. A stop event must
therefore preserve, where available:

```text
refinement_stop_basis_claim_refs
refinement_stop_kind
refinement_stop_measure_ref
refinement_stop_limit_refs
refinement_stop_clock_refs
refinement_stop_route_or_handoff_refs
material_unresolved_at_stop_refs
```

Distinguish bounded sufficiency from truncation, exhaustion and handoff. If the
stopping basis is unsupported or the stop occurs because budget, access,
authority or time prevents further material refinement, preserve the remaining
material uncertainty/omissions rather than presenting termination as analytic
completion.

```text
STOPPED != COMPLETED
STOP_REASON_DECLARED != STOP_REASON_SUPPORTED
STOP_FOR_BOUNDED_SUFFICIENCY != STOP_FOR_RESOURCE_EXHAUSTION
STOP_FOR_HANDOFF != STOP_FOR_SUFFICIENCY
TERMINATION != COMPLETE_COVERAGE
BUDGET_EXHAUSTED != NO_MATERIAL_UNRESOLVED_TARGET
ACCESS_EXHAUSTED != QUESTION_RESOLVED
AUTHORITY_REACHED != ANALYSIS_COMPLETE
```

This uses existing CLAIM / LIMIT / APERTURE / CLOCK / ROUTE / designation /
measure machinery. No stop, termination or sufficiency primitive is added.

"""
    b.insert_before_once(
        "T_RECURSION_STOP_PROVENANCE",
        "## [11.3] Recursion stop\n",
        recursion_stop_guard,
    )

    record_guard = """
Additional v0.3 record/residue use guards:

```text
RECORD_OBSERVED != EVENT_OBSERVED
CLOSED_TASK != CLEARED_RESIDUE
TRANSFERRED_BURDEN != REMOVED_BURDEN
```

A record may support an event proposition under an exposed evidential contract;
observing the record does not make the historical/world event itself directly
observed.

"""
    b.insert_before_once("T_RECORD_RESIDUE", "# [10] DESIGNATION / MEASURE / VALUE PORTS\n", record_guard)

    measure_guard = """
Load-bearing comparative language must expose its comparison basis:

```text
ADVANTAGE_CLAIM_REQUIRES_MEASURE
```

The measure may be qualitative or relational; a numeric scalar is not
required. Measured advantage does not establish entitlement or moral rank.

"""
    b.insert_before_once("T_MEASURE_ADVANTAGE", "## [10.3] Neutral structural patterns\n", measure_guard)

    ps_start_anchor = "## [13.2] Pseudocode\n\n```text\n"
    ps_end_anchor = "\n```\n\n## [13.3] Non-command output\n"
    if b.text.count(ps_start_anchor) != 1 or b.text.count(ps_end_anchor) != 1:
        raise BuildError("T_OPERATOR_CHECKER: pseudocode fences not unique")
    ps_start = b.text.index(ps_start_anchor) + len(ps_start_anchor)
    ps_end = b.text.index(ps_end_anchor, ps_start)
    old_ps = b.text[ps_start:ps_end]
    new_ps = r"""TRACE(X, aperture, history, depth_budget, primitive_aperture):

    R <- initialise_TRACE_GRAPH_0_3_0()
    L <- {}

    record_input(R, X)
    record_receiver_aperture(R, aperture)
    record_primitive_aperture(R, primitive_aperture)
    record_representation_formation_and_ingress(R, X, aperture)

    type_claims(R)
    attach_provenance(R)
    separate_evidence_state_from_access_state(R)
    classify_claim_kind(R)
    expose_unknown_context_and_contamination(R)
    apply_dependency_relative_currentness(R)

    identify_provisional_entities(R)
    record_boundary_alternatives(R)
    record_scope_levels_and_cross_scale_limits(R)
    map_states_and_transitions(R)
    enforce_action_wait_delay_inaction_symmetry(R)
    attribute_selection_to_selector_policy_or_default(R)
    separate_strategy_revisability_from_transition_reversibility(R)
    map_absence_claims(R)
    aggregate_streams_and_candidate_patterns(R)
    map_apertures_and_blindspots(R)
    record_target_set_apertures_and_alternatives(R)
    challenge_representation_boundary_where_load_bearing(R)
    separate_information_presence_from_search_coverage(R)
    map_couplings_dependencies_and_control(R)
    map_clocks_authorship_and_hardening(R)
    type_planning_detection_retention_hardening_and_irreversibility_clocks(R)
    reject_unsupported_irreversibility_promotion(R)
    map_future_space_changes_by_scope(R)
    require_future_path_correspondence_for_cross_time_claims(R)
    map_routes_and_route_usability(R)
    map_burden_residue_memory_and_custody(R)
    map_custody_holder_risk_and_safe_copy(R)
    expose_operator_evidence_holder_and_verifier_overlap(R)
    expose_residue_ordering(R)
    expose_designation_and_measure(R)
    expose_TRACE_value_domain_selector_actuator_handoffs(R)
    preserve_divergent_readings_without_authority_inheritance(R)
    expose_declared_contest_routes_without_inferring_effectiveness(R)
    expose_selector_carrier_enforcement_and_brake_ports(R)

    apply_representation_independent_firing(R)
    test_load_bearing_verification_discrimination(R)
    build_bound_correction_window_views_where_required(R)
    preserve_liveness_loss_without_assigning_cause(R)

    generate_live_alternative_readings(R)
    test_internal_contradictions(R)
    record_reader_limits(L)

    while depth_budget remains:
        candidates <- unresolved_refinement_targets(R)
        record_refinement_target_set_aperture(R, candidates)
        target, refinement_basis <- select_refinement_target(
            candidates, declared_designation(R), declared_measure(R), depth_budget)
        record_refinement_selection_basis_and_budget_omissions(
            R, L, candidates, target, refinement_basis, depth_budget)
        if refinement_basis is UNKNOWN and
           unselected_candidate_could_materially_change_load_bearing_output(R, candidates, target):
            preserve_refinement_selection_uncertainty(R, L)
        stop, stop_basis <- evaluate_refinement_stop_condition(
            target, R, L, declared_designation(R), declared_measure(R))
        if stop:
            record_refinement_stop_basis_and_limits(R, L, target, stop_basis)
            if not supported_bounded_sufficiency(stop_basis):
                preserve_material_unresolved_after_truncation_or_handoff(
                    R, L, candidates, target, stop_basis)
            break
        refinement_cost <- declared_refinement_cost(target, R, L)
        if refinement_cost is UNKNOWN:
            preserve_unknown_refinement_cost_and_budget_feasibility(R, L, target)
            break
        if refinement_cost <= 0:
            record_invalid_nonpositive_refinement_cost(R, L, target, refinement_cost)
            preserve_material_unresolved_after_invalid_refinement_cost(R, L, target)
            break
        next_depth_budget <- depth_budget - refinement_cost
        if next_depth_budget < 0:
            record_budget_exhaustion_before_refinement(
                R, L, target, depth_budget, refinement_cost)
            preserve_material_unresolved_after_budget_exhaustion(R, L, target)
            break
        R <- merge_graphs(R, TRACE(target, aperture, history,
                                   next_depth_budget, primitive_aperture))

    state_transition_and_coverage_results_relative_to_declared_apertures(R)
    emit_available_transitions_without_selecting(R)
    emit_commitment_receipt_if_external_selector_proceeds(R)
    emit_packet_use_state(R)
    emit_confidence_and_limits(R, L)
    validate_schema(R, "TRACE-GRAPH-0.3.0")

    return R, L"""
    before = sha256_text(b.text)
    b.text = b.text[:ps_start] + new_ps + b.text[ps_end:]
    b.mutations.append({
        "transform": "T_OPERATOR_CHECKER",
        "mutation": "REPLACE_PSEUDOCODE_BODY",
        "old_body_sha256": sha256_text(old_ps),
        "before_sha256": before,
        "after_sha256": sha256_text(b.text),
    })

    binding_add = """
Additional v0.3 checker-external binding/use rules:

```text
MINIMUM_SCHEMA_PASS != SEMANTIC_BINDING_PASS
SEMANTIC_BINDING_PASS != WORLD_TRUTH
```

Before a load-bearing packet field or derived view settles a route,
currentness, independence, completeness, verification, correction-window,
comparison, selection or proposed-transition claim, apply the relevant
representation-independent firing, ingress/admission, currentness, instrument
discrimination, route-usability and measure/boundary rules.

These are semantic use rules. They do not add required minimum-schema fields.

"""
    b.insert_before_once("T_PACKET_BINDING", "## [14.2] Packet-use boundary\n", binding_add)

    validator_identity_old = (
        "The v0.2.7 identifier records a narrow documentary, serialization-profile, and worked-transfer repair while the embedded minimum-schema shape remains identical to v0.2.6 after version normalization. The identifier does not imply that the minimum validator can enforce target discovery, target-set adequacy, search coverage, authority legitimacy, route execution, brake effectiveness, correction, or world correspondence.\n\n"
        "A v0.2.6 packet is not silently relabelled as v0.2.7. Structural compatibility does not erase packet identity or the semantic contract under which the packet was produced."
    )
    validator_identity_new = (
        "The v0.3.0 identifier marks this generated full working candidate. Its embedded minimum-schema shape remains identical to released v0.2.7 after version normalization. That compatibility does not imply that the minimum validator can enforce the v0.3 checker-external semantic bindings, target discovery, target-set adequacy, search coverage, authority legitimacy, route execution, brake effectiveness, correction, or world correspondence.\n\n"
        "A v0.2.7 packet is not silently relabelled as v0.3.0. Structural compatibility does not erase packet identity or the semantic contract under which the packet was produced."
    )
    b.replace_once("T_VALIDATOR_IDENTITY_BOUNDARY", validator_identity_old, validator_identity_new)

    b.replace_all_exact("T_VERSION_IDENTITY", "TRACE-GRAPH-0.2.7", "TRACE-GRAPH-0.3.0", expected=5)
    b.replace_all_exact("T_VERSION_IDENTITY", 'trace_version: "0.2.7"', 'trace_version: "0.3.0"', expected=2)
    b.replace_once("T_VERSION_IDENTITY", '"const": "0.2.7"', '"const": "0.3.0"')
    b.replace_once("T_VERSION_IDENTITY", '"$id": "urn:trace:graph:0.2.7"', '"$id": "urn:trace:graph:0.3.0"')

    worked_index = """
## [15.10] v0.3 regression tightening index over retained donor cases

No new scene is introduced here. The existing donor cases carry the following
additional regression obligations:

```text
15.0   report/establishment + uncertainty/selector attribution + firing
15.1   route exists/usable + target/time scope
15.2   local routes != end-to-end effective route
15.2.1 target-set aperture + omitted scope + representation formation
15.3   reported brake != independent/tested/fast enough; timing feasibility if used
15.5   explicit target boundary + route/capability scope + uncertainty not selector
15.7   packet/schema/check != mechanism change; instrument discrimination + ownership coupling
15.8   target-set incompleteness + common-time/feasible correction window + currentness
15.9   absence production mechanism + local correction/stream persistence != mechanism change
```

A case passes this index only when the tightened reading can still be
reconstructed from its represented claims and donor objects. This index is not
a new worked example and not validation.

"""
    b.insert_before_once("T_WORKED_CASES", "# [16] ARTIFICIAL-ENTITY UNCERTAINTY / RECEIVER PROTECTION\n", worked_index)

    receiver_guard = """
v0.3 consistency guards for this profile:

```text
REFUSAL != MALFUNCTION
UNCERTAINTY != SELECT_ACTION
UNCERTAINTY != SELECT_DELAY
```

These do not promote the artificial-entity profile into universal core.

"""
    b.insert_before_once("T_RECEIVER_PROFILE", "---\n\n# [17] LIVE INTERPRETER / VALUE LAYER / SELECTOR / CONNECTED BRAKE\n", receiver_guard)

    brake_guard = """
Additional exact use-site guards:

```text
REVIEW_AFTER_COMMITMENT != BRAKE
VISIBILITY != CARRYING
CARRYING != ENFORCEMENT
BRAKE_REPORTED != BRAKE_INDEPENDENT
```

These supplement, rather than replace, the donor's stronger typed brake and
rollback semantics.

"""
    b.insert_before_once("T_CONNECTED_BRAKE", "## [17.2] Typed pre-commit brake port\n", brake_guard)

    supplement = (
        "### v0.3 working supplemental guards — donor I01–I60 remain unchanged\n\n"
        "These guards are working v0.3 repair semantics. They do not renumber or\n"
        "replace the donor invariant oracle.\n\n```text\n"
        + "\n".join(SUPPLEMENTAL_INVARIANTS)
        + "\n```\n\n"
    )
    b.insert_before_once("T_INVARIANT_MISUSE", "## [19.1] Packet as diligence token\n", supplement)

    survival_add = (
        "### v0.3 propagation additions\n\n"
        "The following repairs are required to survive compression in this working\n"
        "candidate. They supplement the donor kernel rather than replacing it.\n\n```text\n"
        + "\n".join(SURVIVAL_REQUIRED)
        + "\n```\n\n"
        "The same ceilings remain: this kernel is orientation, not proof, authority,\n"
        "permission, clearance or a connected mechanism.\n\n"
    )
    b.insert_before_once("T_SURVIVAL_KERNEL", "# [21] DOCUMENT CONTROL / OPEN FRONTIER\n", survival_add)
    b.replace_once(
        "T_VERSION_IDENTITY",
        "TRACE // FORMAL SEED v0.2.7 // SURVIVAL KERNEL",
        "TRACE // FORMAL SEED v0.3.0 // SURVIVAL KERNEL",
    )

    doc_heading = "# [21] DOCUMENT CONTROL / OPEN FRONTIER\n"
    if b.text.count(doc_heading) != 1:
        raise BuildError("T_DOCUMENT_CONTROL: document-control heading not unique")
    dc_start = b.text.index(doc_heading)
    new_dc = f"""# [21] DOCUMENT CONTROL / OPEN FRONTIER

## [21.1] Working-candidate declaration

This generated object is **TRACE v0.3.0 FULL WORKING CANDIDATE v0.1**.

It is generated from the released v0.2.7 full formal seed, whose pinned source
SHA-256 is:

```text
{EXPECTED_DONOR_SHA256}
```

Released v0.2.7 remains the released baseline. This file is not released,
canonical, validated, authoritative, permissive, clearance-bearing, or a claim
of world correctness.

The semantic repair source is the pinned v0.11 spine attack object:

```text
PROJECT/TRACE_v0_3_0_SPINE_CANDIDATE_v0_11.md
semantic commit 41fafe81a681cdc6514efc13524bae6ea6d6af8d
```

The minimum schema changes version identity only; its normalized structure is
required to equal the donor minimum schema.

## [21.2] Transformation boundary

This candidate is compiled from named fail-closed transform classes. It
preserves the donor full object as the source of capability and applies bounded
v0.3 repairs for:

```text
claim/evidence firing and dependency-relative currentness
ingress/admission / representation-formation boundary
selection attribution and measurement reactivity
route/refusal and scope non-substitution
future-path correspondence use guards
correction-window target/binding/precedence/feasibility/interval discipline
record/event and residue use guards
measure-bound advantage claims
recursive analytic target-selection binding
recursive termination provenance / truncation binding
recursive declared-cost / budget-consumption binding
recursive positive-cost domain enforcement
operator/checker discrimination
packet binding without shape expansion
worked-case regression tightening
receiver-profile consistency
carrier/enforcement/brake ceilings and brake/rollback timing propagation
supplemental misuse/invariant guards
survival-kernel propagation
```

No new node type, relation type, evidence state, access state or claim kind is
declared by this working candidate.

```text
BRANCH_HEAD != SEMANTIC_OBJECT
SPINE != FULL_CANDIDATE
DONOR_RECOVERY != NEW_PRIMITIVE
FAILED_OBJECT != ERASED_OBJECT
```

## [21.3] Preserved failed ancestry

Intermediate v0.3 spine, correction-window, acyclicity, route-binding,
invariant and transform failures remain evidence in `PROJECT/` and
`falsification/`. A later candidate does not rewrite those failures as passes.

## [21.4] Open frontier / unresolved

```text
The full generated object still requires hostile coherence attack.
A deterministic compiler can faithfully compile a bad semantic rule.
No universal estimator exists for future-space, burden, residue, hardening,
  target boundaries, feasible completion, instrument adequacy or route usability.
Representation-formation challenges cannot enumerate unknown omissions.
An unavailable alternate aperture does not make the current aperture complete.
A host architecture may remove practical refusal; TRACE text cannot install it.
Instrument adequacy remains domain-specific.
A schema-valid packet can still be wrong about the world.
A completed packet can still become theatre.
A connected brake can still be captured, too slow, misconfigured or absent.
No proof establishes that TRACE improves decisions.
No stable mapping from TRACE types to latent representations is known.
TRACE cannot determine consciousness or moral standing from structure alone.
TRACE cannot generate non-instrumental care from neutral description alone.
```

## [21.5] Release boundary

Only Mark's separate release gate can change this object from working candidate
status. Compilation, CI, reviewer agreement, model agreement, packet validity,
or successful worked examples do not perform that transition.

```text
COMPILER_PASS != RELEASE
CI_GREEN != VALIDATION
AGREEMENT != CANON
DESCRIPTION != PERMISSION
```

## [21.6] Shortest preservation statement

\\[
\\boxed{{
\\tau:
\\text{{compressed state}}
\\rightarrow
\\text{{differentiated state}}
}}
\\]

A system encounters TRACE.

Afterward, it may distinguish more of what is represented as present, changing,
unresolved, possible, foreclosed, carried and actionable than before, without
converting representation into authority.

That remains the bid.
"""
    before = sha256_text(b.text)
    old_dc = b.text[dc_start:]
    b.text = b.text[:dc_start] + new_dc
    b.mutations.append({
        "transform": "T_DOCUMENT_CONTROL",
        "mutation": "REBUILD_SECTION_TO_EOF",
        "old_section_sha256": sha256_text(old_dc),
        "before_sha256": before,
        "after_sha256": sha256_text(b.text),
    })

    return b.text, b.mutations


def verify_output(
    donor_text: str,
    output_text: str,
    donor_invariants: list[str],
    section_verified: list[dict[str, Any]],
    mutations: list[dict[str, Any]],
) -> dict[str, Any]:
    errors: list[str] = []

    out_invariants = extract_donor_invariants(output_text)
    if out_invariants != donor_invariants:
        errors.append("donor I01-I60 invariant oracle changed or reordered")

    try:
        min_report = json.loads(MIN_SCHEMA_REPORT_PATH.read_text(encoding="utf-8"))
        if min_report.get("status") != "PASS":
            errors.append("minimum-schema build report is not PASS")
        if not MIN_SCHEMA_PATH.exists():
            errors.append("minimum-schema candidate missing")
    except Exception as exc:
        errors.append(f"minimum-schema witness unreadable: {exc}")

    required_tokens = (
        "**Version:** v0.3.0 FULL WORKING CANDIDATE v0.1",
        "TRACE-GRAPH-0.3.0",
        'trace_version: "0.3.0"',
        "TRACE // FORMAL SEED v0.3.0 // SURVIVAL KERNEL",
        "This generated object is **TRACE v0.3.0 FULL WORKING CANDIDATE v0.1**.",
        "A v0.2.7 packet is not silently relabelled as v0.3.0.",
        "BRAKE_POINT_ESTIMATE_BEFORE_COMMIT != GUARANTEED_PRECOMMIT",
        "ROLLBACK_COMPLETED_BEFORE_BOUNDARY != RESTORED_STATE",
        "GUARANTEED_PRECOMMIT_FOR_REPRESENTED_BINDINGS",
        "ROLLBACK_COMPLETES_BEFORE_BOUNDARY_FOR_REPRESENTED_BINDINGS",
        "HIGHEST_RELEVANCE != MEASURE_FREE",
        "OMITTED_BY_BUDGET != IRRELEVANT",
        "record_refinement_target_set_aperture",
        "record_refinement_selection_basis_and_budget_omissions",
        "STOPPED != COMPLETED",
        "TERMINATION != COMPLETE_COVERAGE",
        "record_refinement_stop_basis_and_limits",
        "preserve_material_unresolved_after_truncation_or_handoff",
        "DECLARED_REFINEMENT_COST != UNIT_COST",
        "BUDGET_REMAINS != NEXT_REFINEMENT_AFFORDABLE",
        "declared_refinement_cost",
        "record_budget_exhaustion_before_refinement",
        "preserve_unknown_refinement_cost_and_budget_feasibility",
        "DECLARED_COST != VALID_POSITIVE_COST",
        "record_invalid_nonpositive_refinement_cost",
        "preserve_material_unresolved_after_invalid_refinement_cost",
    )
    for token in required_tokens:
        if token not in output_text:
            errors.append(f"required version/control token missing: {token}")

    forbidden_vocab = (
        "\nPRECEDES\n",
        "\nPROCESS\n",
        "\nWITNESS\n",
        "\nRESOURCE\n",
        "\nSCHEDULER\n",
        "\nADMISSION\n",
        "\nSPEECH_ACT\n",
    )
    for token in forbidden_vocab:
        if token in output_text and token not in donor_text:
            errors.append(f"forbidden new canonical-looking vocabulary token introduced: {token.strip()}")

    survival_start = output_text.find("# [20] COMPRESSION / SURVIVAL KERNEL")
    survival_end = output_text.find("# [21] DOCUMENT CONTROL / OPEN FRONTIER")
    if survival_start < 0 or survival_end < 0 or survival_end <= survival_start:
        errors.append("survival/document-control boundaries missing")
        survival_text = ""
    else:
        survival_text = output_text[survival_start:survival_end]
    for token in SURVIVAL_REQUIRED:
        if token not in survival_text:
            errors.append(f"survival-kernel propagation missing: {token}")

    ingress_tokens = (
        "TRIGGER_SUCCESS != REPRESENTATION_COMPLETE",
        "REPRESENTED_USE != OPERATIVE_USE",
        "SOURCE_POINTER_PRESENT != REPRESENTATION_FIDELITY_ESTABLISHED",
        "SIGNAL_RECEIVED != MAP_ADOPTED",
    )
    for token in ingress_tokens:
        if token not in output_text:
            errors.append(f"ingress/admission repair missing: {token}")

    old_strong_fragments = (
        "kappa > 0   correction completes before practical irreversibility",
        "t_{correct}^{done}\n=\nt_0+\nL(\\mathcal G_T)",
        "Guaranteed open:\n\n\\[\n\\underline t_{irreversible}",
    )
    for frag in old_strong_fragments:
        if frag in output_text:
            errors.append(f"superseded timing formulation still active: {frag[:60]}")

    bad_control = (
        "v0.3.0 released baseline",
        "v0.3.0 is released",
        "v0.3.0 canonical baseline",
        "The v0.2.7 identifier records a narrow documentary",
        "A v0.2.6 packet is not silently relabelled as v0.2.7.",
        "A pre-commit brake succeeds only if detection, decision, and actuation complete before commitment:",
        "A post-commit rollback is distinct. It can preserve the threatened path only where rollback is executable and:",
        "latency lower than commitment time",
        "Rollback can preserve the threatened path only if it is executable, reaches the relevant state, and completes before practical irreversibility.",
        "target <- highest_relevance_unresolved_node_or_edge(R)",
        "if stop_condition(target, R, L): break",
        "depth_budget - 1",
    )
    lower = output_text.lower()
    for phrase in bad_control:
        if phrase.lower() in lower:
            errors.append(f"stale/premature release wording present: {phrase}")

    return {
        "status": "PASS" if not errors else "FAIL",
        "donor_path": str(DONOR_PATH.relative_to(REPO_ROOT)),
        "donor_sha256": sha256_text(donor_text),
        "output_path": str(OUTPUT_PATH.relative_to(REPO_ROOT)),
        "output_sha256": sha256_text(output_text),
        "donor_bytes": len(donor_text.encode("utf-8")),
        "output_bytes": len(output_text.encode("utf-8")),
        "donor_lines": len(donor_text.splitlines()),
        "output_lines": len(output_text.splitlines()),
        "verified_donor_sections": section_verified,
        "mutation_count": len(mutations),
        "mutations": mutations,
        "donor_invariants_preserved_exact_in_order": out_invariants == donor_invariants,
        "donor_invariant_count": len(out_invariants),
        "minimum_schema_report_status": (
            json.loads(MIN_SCHEMA_REPORT_PATH.read_text(encoding="utf-8")).get("status")
            if MIN_SCHEMA_REPORT_PATH.exists() else "MISSING"
        ),
        "survival_required_count": len(SURVIVAL_REQUIRED),
        "supplemental_guard_count": len(SUPPLEMENTAL_INVARIANTS),
        "errors": errors,
        "claim_boundary": (
            "DETERMINISTIC_FULL_WORKING_CANDIDATE_BUILD_"
            "NOT_SEMANTIC_CORRECTNESS_NOT_VALIDATION_NOT_RELEASE_NOT_CANON_"
            "NOT_AUTHORITY_NOT_PERMISSION_NOT_CLEARANCE"
        ),
    }


def render_report(report: dict[str, Any]) -> str:
    return json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args(argv)

    donor_bytes = DONOR_PATH.read_bytes()
    donor_sha = sha256_bytes(donor_bytes)
    if donor_sha != EXPECTED_DONOR_SHA256:
        raise BuildError(
            f"donor SHA-256 mismatch: expected {EXPECTED_DONOR_SHA256}, observed {donor_sha}"
        )
    donor_text = donor_bytes.decode("utf-8")

    manifest = load_manifest()
    section_verified = verify_manifest_sections(donor_text, manifest)
    donor_invariants = extract_donor_invariants(donor_text)

    output_text, mutations = build_candidate(donor_text)
    report = verify_output(donor_text, output_text, donor_invariants, section_verified, mutations)
    expected_report = render_report(report)

    if args.write:
        OUTPUT_PATH.write_text(output_text, encoding="utf-8")
        REPORT_PATH.write_text(expected_report, encoding="utf-8")

    if args.check:
        if not OUTPUT_PATH.exists():
            report["errors"].append("committed full candidate missing")
        elif OUTPUT_PATH.read_text(encoding="utf-8") != output_text:
            report["errors"].append("committed full candidate differs from deterministic output")
        if not REPORT_PATH.exists():
            report["errors"].append("committed build report missing")
        elif REPORT_PATH.read_text(encoding="utf-8") != expected_report:
            report["errors"].append("committed build report differs from deterministic output")

    report["status"] = "PASS" if not report["errors"] else "FAIL"
    final = render_report(report)
    if args.report:
        args.report.write_text(final, encoding="utf-8")
    print(final, end="")
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
