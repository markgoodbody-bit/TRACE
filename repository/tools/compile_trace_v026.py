#!/usr/bin/env python3
"""Compile and verify TRACE_FORMAL_SEED_v0_2_6.md from v0.2.5.

The compiler applies only the bounded semantic and identifier repair admitted by
TRACE v0.2.6 transition candidate PR #17. Its output remains a compiled working
candidate: not canon, not released, not validation, and not authority.
"""

from __future__ import annotations

import argparse
import copy
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
BASE_PATH = REPO_ROOT / "TRACE_FORMAL_SEED_v0_2_5.md"
OUTPUT_PATH = REPO_ROOT / "TRACE_FORMAL_SEED_v0_2_6.md"

VERSION = "0.2.6"
SCHEMA_ID = "TRACE-GRAPH-0.2.6"
URN = "urn:trace:graph:0.2.6"

TARGET_SET_SECTION = r"""
### [5.3.1] Target-set aperture

Selection of what a search, comparison, audit, review, or checker is required to reach is itself aperture-bearing.

Let a target-set aperture be represented by:

\[
\Pi_T=
\left\langle
source,
targets,
selection\_basis,
omitted\_known\_categories,
alternatives,
control,
uncertainty
\right\rangle
\]

The selected target set is not the world's complete affected scope.

```text
TARGET_SET != WORLD_SCOPE
TARGET_NOT_SELECTED != TARGET_DOES_NOT_EXIST
COVERAGE_OF_SELECTED_TARGETS != COMPLETE_DISCOVERY
OPERATOR_TARGET_SET != AUTHORITATIVE_TARGET_SET
```

Where a claim of search, review, or coverage is materially used, record where available:

```text
target_set_source_ref
target_refs
selection_basis_claim_refs
known_omitted_target_categories
alternative_target_set_refs
control_or_custody_refs
uncertainty_claim_refs
```

Materially different target-set apertures may coexist. TRACE preserves their provenance and disagreement. It does not silently merge them, declare one complete, or grant one selection authority.

A target-set aperture may be represented using existing `APERTURE`, `CLAIM`, `RECORD`, `ENTITY`, `ROUTE`, `TRANSITION`, and edge vocabulary. This section does not require a new canonical object type.

"""

TRANSITION_RELATIVITY_SECTION = r"""
ACCOUNTING_AND_COVERAGE_ARE_APERTURE_RELATIVE

Transition-set exposure is relative to the declared scene, evidence, receiver, primitive, and comparison apertures.

```text
TRANSITION_SET_EXPOSED_RELATIVE_TO_APERTURE
!=
WORLD_TRANSITION_SET_COMPLETE
```

An empty transition bucket does not establish that the class is unavailable. Where a class is materially live under the supplied comparison evidence, it is represented or explicitly bounded by a resolvable unavailable, unresolved, or not-assessable status.

Representing an `INFORMATION` transition establishes only that an information-seeking transition is present in the map.

```text
INFORMATION_TRANSITION_REPRESENTED
!=
OUTWARD_SEARCH_COVERAGE

SEARCH_PATH_DECLARED
!=
SEARCH_PATH_EXECUTABLE

SELECTED_TARGET_REACHED
!=
UNSEEN_TARGETS_ABSENT
```

Coverage claims require a declared target-set aperture and comparison basis. Completeness beyond that aperture remains `UNKNOWN`.

"""

HANDOFF_CEILING_SECTION = r"""
Divergent structural readings do not create selection authority.

```text
DIVERGENT_READINGS != AUTHORITY
STRUCTURAL_PASS != PERMISSION
DECLARED_HANDOFF != LEGITIMATE_AUTHORITY
VISIBLE_AUTHORITY != CONTESTABLE_AUTHORITY
ROUTE_TO_BRAKE != CORRECTION_COMPLETED
```

Where a later layer selects a reading or transition after material divergence, expose where available:

```text
selected_reading_ref
selected_transition_ref
selector_ref
selector_owner_ref
authority_claim_refs
value_or_policy_refs
handoff_route_refs
challenging_reading_refs
brake_ref
unresolved_handoffs
commitment_receipt_ref
```

These references make the handoff inspectable. They do not establish that the selector is legitimate, the policy is good, the route works, the brake is effective, or the selected transition should proceed.

"""

CHECKER_EXTERNAL_RULES = r"""
```text
Every material search-coverage claim references a target-set aperture, selected target refs, and a declared reachability or unavailability basis.
Every claim that a target set is complete remains UNKNOWN unless completeness is independently bounded by a declared world model and evidence aperture.
Every selection after divergent readings references a selector, authority basis, policy/value basis, handoff route, and unresolved handoff status.
Every claim of contestability references the challenging reading, contest route, bound brake, capture/independence status, and relevant clocks where available.
Every brake or correction claim distinguishes declaration, activation attempt, observable interruption, correction completion, and residue.
```

These remain checker-external because the embedded minimum validator cannot establish semantic relevance, completeness, route executability, authority legitimacy or world effect.

"""

PACKET_USE_NON_EQUIVALENCES = r"""
```text
TARGET_SET_RECORDED != TARGET_SET_COMPLETE
COVERAGE_CHECK_PASSED != DILIGENCE_ESTABLISHED
AUTHORITY_HANDOFF_RECORDED != AUTHORITY_LEGITIMATED
CONTEST_ROUTE_RECORDED != CONTEST_SUCCEEDED
BRAKE_ACTIVATION_RECORDED != TRANSITION_INTERRUPTED
TRANSITION_INTERRUPTED != HARM_PREVENTED
```

"""

MINIMUM_VALIDATOR_BOUNDARY = r"""
The v0.2.6 identifier records a revised semantic contract while the embedded minimum-schema shape remains identical to v0.2.5. The identifier does not imply that the minimum validator can enforce target discovery, target-set adequacy, search coverage, authority legitimacy, route execution, brake effectiveness, correction, or world correspondence.

A v0.2.5 packet is not silently relabelled as v0.2.6. Structural compatibility does not erase packet identity or the semantic contract under which the packet was produced.

"""

REQUIRED_TOKENS = (
    "### [5.3.1] Target-set aperture",
    "TARGET_SET != WORLD_SCOPE",
    "ACCOUNTING_AND_COVERAGE_ARE_APERTURE_RELATIVE",
    "TRANSITION_SET_EXPOSED_RELATIVE_TO_APERTURE",
    "INFORMATION_TRANSITION_REPRESENTED",
    "DIVERGENT_READINGS != AUTHORITY",
    "ROUTE_TO_BRAKE != CORRECTION_COMPLETED",
    "record_target_set_apertures_and_alternatives(R)",
    "separate_information_presence_from_search_coverage(R)",
    "preserve_divergent_readings_without_authority_inheritance(R)",
    "expose_declared_contest_routes_without_inferring_effectiveness(R)",
    "state_transition_and_coverage_results_relative_to_declared_apertures(R)",
    "Every material search-coverage claim references a target-set aperture",
    "TARGET_SET_RECORDED != TARGET_SET_COMPLETE",
    "BRAKE_ACTIVATION_RECORDED != TRANSITION_INTERRUPTED",
    "minimum-schema shape remains identical to v0.2.5",
)


@dataclass(frozen=True)
class VerificationReport:
    status: str
    base_lines: int
    compiled_lines: int
    inserted_sections: int
    schema_shape_identical: bool
    old_identifier_occurrences: int
    errors: tuple[str, ...]

    def as_dict(self) -> dict[str, Any]:
        return {
            "candidate": "TRACE_FORMAL_SEED_v0_2_6",
            "status": self.status,
            "base_lines": self.base_lines,
            "compiled_lines": self.compiled_lines,
            "inserted_sections": self.inserted_sections,
            "schema_shape_identical": self.schema_shape_identical,
            "old_identifier_occurrences": self.old_identifier_occurrences,
            "errors": list(self.errors),
            "claim_boundary": "COMPILED_WORKING_CANDIDATE_NOT_CANON_NOT_RELEASED_NOT_VALIDATED",
        }


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"{label}: expected exactly one anchor, observed {count}")
    return text.replace(old, new, 1)


def insert_before(text: str, marker: str, insertion: str, label: str) -> str:
    return replace_once(text, marker, "\n" + insertion.rstrip() + "\n" + marker, label)


def extract_minimum_schema(text: str) -> dict[str, Any]:
    heading = "## [14.4] Minimum validator contract"
    start = text.find(heading)
    if start < 0:
        raise ValueError("minimum validator heading missing")
    fence_start = text.find("```json", start)
    fence_end = text.find("```", fence_start + len("```json"))
    if fence_start < 0 or fence_end < 0:
        raise ValueError("minimum validator JSON fence missing")
    return json.loads(text[fence_start + len("```json") : fence_end].strip())


def normalize_schema_version(value: Any) -> Any:
    def walk(item: Any) -> Any:
        if isinstance(item, dict):
            return {key: walk(val) for key, val in item.items()}
        if isinstance(item, list):
            return [walk(val) for val in item]
        if isinstance(item, str):
            return (
                item.replace("TRACE-GRAPH-0.2.6", "TRACE-GRAPH-0.2.5")
                .replace("urn:trace:graph:0.2.6", "urn:trace:graph:0.2.5")
                .replace("0.2.6", "0.2.5")
            )
        return item

    return walk(copy.deepcopy(value))


def compile_seed(base: str) -> str:
    text = base
    text = replace_once(
        text,
        "**Version:** v0.2.5 TRANSITION DISCIPLINE CANDIDATE  ",
        "**Version:** v0.2.6 TARGET-SET APERTURE CANDIDATE  ",
        "version header",
    )
    text = replace_once(text, "**Date:** 2026-07-15  ", "**Date:** 2026-08-04  ", "date")
    text = replace_once(
        text,
        "**Status:** reviewed test baseline; unvalidated in the world; non-canonical; voluntary; not authority; not permission; not clearance  ",
        "**Status:** compiled working candidate; unvalidated in the world; non-canonical; voluntary; not authority; not permission; not clearance  ",
        "status header",
    )

    # Synchronize current-contract identifiers before inserting text that must still
    # refer historically to v0.2.5. The base seed has no version changelog.
    text = text.replace("0_2_5", "0_2_6")
    text = text.replace("0.2.5", "0.2.6")

    text = insert_before(text, "\n## [5.4] State\n", TARGET_SET_SECTION, "target-set aperture")
    text = insert_before(
        text,
        "\n## [6.2] Coupling\n",
        TRANSITION_RELATIVITY_SECTION,
        "transition aperture relativity",
    )
    text = insert_before(
        text,
        "\n# [11] RECURSIVE ZOOM / MANDELBROT RULE\n",
        HANDOFF_CEILING_SECTION,
        "divergence authority ceiling",
    )

    text = replace_once(
        text,
        "    map_apertures_and_blindspots(R)\n",
        "    map_apertures_and_blindspots(R)\n"
        "    record_target_set_apertures_and_alternatives(R)\n"
        "    separate_information_presence_from_search_coverage(R)\n",
        "pseudocode target-set hooks",
    )
    text = replace_once(
        text,
        "    expose_TRACE_value_domain_selector_actuator_handoffs(R)\n",
        "    expose_TRACE_value_domain_selector_actuator_handoffs(R)\n"
        "    preserve_divergent_readings_without_authority_inheritance(R)\n"
        "    expose_declared_contest_routes_without_inferring_effectiveness(R)\n",
        "pseudocode handoff hooks",
    )
    text = replace_once(
        text,
        "    emit_available_transitions_without_selecting(R)\n",
        "    state_transition_and_coverage_results_relative_to_declared_apertures(R)\n"
        "    emit_available_transitions_without_selecting(R)\n",
        "pseudocode relativity hook",
    )

    text = insert_before(
        text,
        "\nExcept for the `CLAIM`-node one-reference cardinality rule",
        CHECKER_EXTERNAL_RULES,
        "checker-external binding rules",
    )
    text = insert_before(
        text,
        "\n## [14.3] Unresolved commitment receipt\n",
        PACKET_USE_NON_EQUIVALENCES,
        "packet-use non-equivalences",
    )
    text = replace_once(
        text,
        "## [14.4] Minimum validator contract\n\nThe embedded schema validates packet shape and controlled vocabularies. It cannot validate truth, completeness, independence, value choice, world correspondence, or operational connection.\n\n",
        "## [14.4] Minimum validator contract\n\n"
        "The embedded schema validates packet shape and controlled vocabularies. It cannot validate truth, completeness, independence, value choice, world correspondence, or operational connection.\n\n"
        + MINIMUM_VALIDATOR_BOUNDARY,
        "minimum-validator semantic boundary",
    )

    if not text.endswith("\n"):
        text += "\n"
    return text


def verify_compiled(base: str, compiled: str) -> VerificationReport:
    errors: list[str] = []

    for token in REQUIRED_TOKENS:
        if token not in compiled:
            errors.append(f"missing required compiled token: {token}")

    old_identifiers = sum(
        compiled.count(token)
        for token in ("TRACE-GRAPH-0.2.5", "urn:trace:graph:0.2.5", "0_2_5")
    )
    if old_identifiers:
        errors.append(f"mixed-version identifiers remain: {old_identifiers}")

    if compiled.count("### [5.3.1] Target-set aperture") != 1:
        errors.append("target-set aperture section must occur exactly once")
    if compiled.count("ACCOUNTING_AND_COVERAGE_ARE_APERTURE_RELATIVE") != 1:
        errors.append("aperture-relative accounting marker must occur exactly once")
    if "**Status:** compiled working candidate;" not in compiled:
        errors.append("compiled status boundary missing")
    if "not authority; not permission; not clearance" not in compiled:
        errors.append("claim ceiling was not preserved")

    base_schema = extract_minimum_schema(base)
    compiled_schema = extract_minimum_schema(compiled)
    schema_shape_identical = normalize_schema_version(compiled_schema) == base_schema
    if not schema_shape_identical:
        errors.append("minimum schema changed beyond synchronized identifiers")

    if compiled_schema.get("$id") != URN:
        errors.append("compiled schema $id mismatch")
    if compiled_schema.get("title") != f"{SCHEMA_ID} minimum validator":
        errors.append("compiled schema title mismatch")

    graph_properties = (
        compiled_schema.get("properties", {})
        .get("trace_graph", {})
        .get("properties", {})
    )
    if graph_properties.get("schema", {}).get("const") != SCHEMA_ID:
        errors.append("compiled packet schema const mismatch")
    if graph_properties.get("trace_version", {}).get("const") != VERSION:
        errors.append("compiled trace_version const mismatch")

    if compiled.count("initialise_TRACE_GRAPH_0_2_6()") != 1:
        errors.append("compiled pseudocode initialiser mismatch")
    if compiled.count('validate_schema(R, "TRACE-GRAPH-0.2.6")') != 1:
        errors.append("compiled pseudocode validator target mismatch")

    base_lines = len(base.splitlines())
    compiled_lines = len(compiled.splitlines())
    if compiled_lines <= base_lines:
        errors.append("compiled seed did not grow despite admitted semantic repair")

    section_tokens = (
        "### [5.3.1] Target-set aperture",
        "ACCOUNTING_AND_COVERAGE_ARE_APERTURE_RELATIVE",
        "DIVERGENT_READINGS != AUTHORITY",
        "Every material search-coverage claim references a target-set aperture",
        "TARGET_SET_RECORDED != TARGET_SET_COMPLETE",
        "minimum-schema shape remains identical to v0.2.5",
    )
    inserted_sections = sum(token in compiled for token in section_tokens)

    return VerificationReport(
        status="PASS" if not errors else "FAIL",
        base_lines=base_lines,
        compiled_lines=compiled_lines,
        inserted_sections=inserted_sections,
        schema_shape_identical=schema_shape_identical,
        old_identifier_occurrences=old_identifiers,
        errors=tuple(errors),
    )


def self_test(base: str) -> None:
    compiled = compile_seed(base)
    if verify_compiled(base, compiled).status != "PASS":
        raise AssertionError("baseline compilation failed")

    gutted = compiled.replace(TARGET_SET_SECTION.strip(), "This section asserts nothing.", 1)
    if verify_compiled(base, gutted).status != "FAIL":
        raise AssertionError("gutted target-set section did not fail")

    mixed = compiled.replace("TRACE-GRAPH-0.2.6", "TRACE-GRAPH-0.2.5", 1)
    if verify_compiled(base, mixed).status != "FAIL":
        raise AssertionError("mixed-version seed did not fail")

    schema_growth = compiled.replace(
        '"required": [\n    "trace_graph"\n  ]',
        '"required": [\n    "trace_graph",\n    "invented_required_field"\n  ]',
        1,
    )
    if verify_compiled(base, schema_growth).status != "FAIL":
        raise AssertionError("minimum-schema shape growth did not fail")

    crlf = compiled.replace("\n", "\r\n")
    if verify_compiled(base, crlf).status != "PASS":
        raise AssertionError("line-ending-only reflow did not preserve pass")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    base = BASE_PATH.read_text(encoding="utf-8")
    expected = compile_seed(base)
    report = verify_compiled(base, expected)

    if args.self_test:
        self_test(base)
        print(json.dumps({"status": "PASS", "tests": 4}, sort_keys=True))
        return 0

    if report.status != "PASS":
        print(json.dumps(report.as_dict(), indent=2, sort_keys=True))
        return 1

    if args.write:
        OUTPUT_PATH.write_text(expected, encoding="utf-8", newline="\n")
        print(json.dumps(report.as_dict(), indent=2, sort_keys=True))
        return 0

    if not OUTPUT_PATH.exists():
        print(json.dumps({"status": "FAIL", "errors": ["compiled seed missing"]}))
        return 1
    if OUTPUT_PATH.read_text(encoding="utf-8") != expected:
        print(json.dumps({"status": "FAIL", "errors": ["compiled seed is stale or altered"]}))
        return 1

    print(json.dumps(report.as_dict(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
