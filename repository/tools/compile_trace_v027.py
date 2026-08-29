#!/usr/bin/env python3
"""Compile and verify TRACE_FORMAL_SEED_v0_2_7.md from released v0.2.6.

The compiler implements only the bounded repair supported by the v0.2.6
falsify-x100 audit: propagation through compression/document-control surfaces,
a non-required existing-object serialization profile, and one constructed
worked transfer. It does not add a primitive, node type, edge type, port,
required packet property, selector, value rule, or authority claim.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
BASE_PATH = REPO_ROOT / "TRACE_FORMAL_SEED_v0_2_6.md"
OUTPUT_PATH = REPO_ROOT / "TRACE_FORMAL_SEED_v0_2_7.md"

VERSION = "0.2.7"
SCHEMA_ID = "TRACE-GRAPH-0.2.7"
URN = "urn:trace:graph:0.2.7"

MIDDLE_OUT_ADDITION = """target-set source and selection basis
known omitted target categories
alternative target-set apertures
coverage relative to a declared target set and comparison basis
"""

PROFILE_SECTION = r"""
### [14.0.1] Canonical existing-object target-set aperture profile

A target-set aperture is serialized with existing graph objects. This profile is canonical for interoperability but is not a new primitive, node type, edge type, port, or required minimum-schema field.

```yaml
nodes:
  - id: "ap_target_set_primary"
    type: "APERTURE"
    attributes:
      aperture_kind: "TARGET_SET"
      source_ref: "n_operator"
      target_refs: ["n_scope_reported"]
      selection_basis_claim_refs: ["c_target_basis"]
      known_omitted_target_categories: ["unreported affected scopes"]
      alternative_target_set_refs: ["ap_target_set_alternative"]
      control_or_custody_refs: ["n_operator"]
      uncertainty_claim_refs: ["c_target_uncertainty"]
    claim_refs: ["c_target_aperture_status"]

  - id: "ap_target_set_alternative"
    type: "APERTURE"
    attributes:
      aperture_kind: "TARGET_SET"
      source_ref: "n_independent_reviewer"
      target_refs: ["n_scope_reported", "n_scope_unreported"]
      selection_basis_claim_refs: ["c_alternative_basis"]
      known_omitted_target_categories: []
      alternative_target_set_refs: ["ap_target_set_primary"]
      control_or_custody_refs: ["n_independent_reviewer"]
      uncertainty_claim_refs: ["c_alternative_uncertainty"]
    claim_refs: ["c_alternative_aperture_status"]

edges:
  - id: "e_primary_bounds_reported"
    type: "BOUNDS"
    source: "ap_target_set_primary"
    target: "n_scope_reported"
    claim_refs: ["c_target_basis"]

  - id: "e_primary_omits_unreported"
    type: "OMITS"
    source: "ap_target_set_primary"
    target: "n_scope_unreported"
    claim_refs: ["c_target_uncertainty"]

  - id: "e_alternative_disputes_primary"
    type: "DISPUTES"
    source: "ap_target_set_alternative"
    target: "ap_target_set_primary"
    claim_refs: ["c_alternative_basis"]

claims:
  - id: "c_target_basis"
    proposition: "The primary review targets scopes supplied by the operator."
    evidence_state: "R"
    access_state: "A"

  - id: "c_target_uncertainty"
    proposition: "Materially affected scopes may exist outside the supplied target set."
    evidence_state: "U"
    access_state: "A"
```

```text
TARGET_SET_PROFILE_PRESENT != TARGET_SET_COMPLETE
PROFILE_CONFORMANCE != TARGET_DISCOVERY
ALTERNATIVE_TARGET_SET_RECORDED != ALTERNATIVE_TARGET_SET_AUTHORITATIVE
```

"""

WORKED_EXAMPLE = r"""
## [15.2.1] Divergent target-set apertures over one scene

`[CLAIM_CEILING: CONSTRUCTED_TRANSFER | READING_ONLY | NOT_VALIDATION | NOT_COMMAND]`

Input:

```text
A service migration report counts accounts that successfully authenticated.
The operator's review targets accounts present in its success/failure log.
An independent support review also targets people who never reached authentication,
dependent users, and organisations carrying downstream access loss.
```

### STRUCTURAL_READING

```text
SCENE_REF: scene_service_migration

TARGET_SET_APERTURE_A:
  source_ref = operator
  target_refs = logged_accounts
  selection_basis = authentication log
  known_omitted_categories = accounts unable to emit a log entry
  control = operator controls log and target selection
  uncertainty = affected scopes outside the log remain UNKNOWN

TARGET_SET_APERTURE_B:
  source_ref = independent_support_review
  target_refs = logged_accounts + non-reporting users + dependent scopes
  selection_basis = support contacts + dependency map + authentication log
  known_omitted_categories = indirect effects not represented in supplied evidence
  control = mixed custody
  uncertainty = downstream scope remains PARTIAL

COVERAGE_A:
  complete_relative_to_A = POSSIBLE
  world_complete = UNKNOWN

COVERAGE_B:
  complete_relative_to_B = UNKNOWN
  world_complete = UNKNOWN

DISAGREEMENT:
  preserve A and B separately
  do not silently union them
  do not infer that either aperture is authoritative
```

### EXISTING-OBJECT SERIALIZATION

```text
APERTURE nodes: ap_target_set_A, ap_target_set_B
ENTITY nodes: operator, independent_support_review, logged_accounts,
              non_reporting_users, dependent_scopes
CLAIM nodes: basis_A, basis_B, uncertainty_A, uncertainty_B
RECORD nodes: authentication_log, support_record, dependency_map
EDGES: BOUNDS, OMITS, DISPUTES, CONTROLS, REPORTS
```

### VALUE_PORT_STATUS

```text
delta:
  standing of affected and dependent scopes = EXTERNAL / PARTLY_UNKNOWN
mu:
  access continuity, reporting visibility, dependency and recovery = represented
```

### VALUE_LAYER_INTERPRETATION

TRACE preserves the aperture difference and its consequences for coverage claims. It does not select the governing target set, establish complete discovery, or decide migration policy.

"""

REVISION_SECTION = """## [21.1] Revision declaration

This v0.2.7 narrow drift-repair pass succeeds the released v0.2.6 target-set-aperture baseline. v0.2.6 admitted two bounded formal repairs: `TARGET_SET_SELECTION_IS_APERTURE_BEARING` and `ACCOUNTING_AND_COVERAGE_ARE_APERTURE_RELATIVE`. The v0.2.6 falsify-x100 audit found that those distinctions survived in the main body, version identity, deterministic compilation boundary, unchanged minimum-schema shape, and authority/value ceilings, but did not survive every declared compression, document-control, serialization, worked-transfer, and front-door surface.

v0.2.7 therefore propagates the admitted repair into the middle-out seed, numbered invariants, survival kernel, revision declaration, and unresolved register; adds one non-required canonical serialization profile using existing graph vocabulary; and adds one constructed divergent-aperture transfer. It preserves the v0.2.5 transition-discipline repairs carried through v0.2.6.

No primitive family, node type, edge type, port, controlled-vocabulary member, required packet property, selector, value rule, authority rule, minimum-schema shape, or world-valid estimator is added. The canonical profile is interoperability guidance over existing objects, and enforcement remains checker-external. This revision does not establish validation, decision advantage, correct value ordering, domain expertise, operational readiness, complete target discovery, legitimate authority, or world correspondence.

"""

UNRESOLVED_ADDITION = """A selected target set can omit materially affected scopes while coverage appears complete relative to that aperture.
Target-set selection can be controlled, inherited, or contested without any aperture becoming authoritative by default.
"""

INVARIANTS_ADDITION = """I57  TARGET_SET != WORLD_SCOPE
I58  TARGET_NOT_SELECTED != TARGET_DOES_NOT_EXIST
I59  COVERAGE_OF_SELECTED_TARGETS != COMPLETE_DISCOVERY
I60  OPERATOR_TARGET_SET != AUTHORITATIVE_TARGET_SET
"""

SURVIVAL_APERTURE = r"""7. Aperture and target set:

      not_observed_through(Pi_i) != absent

      Pi_T = <source, targets, selection_basis,
              omitted_known_categories, alternatives, control, uncertainty>

      TARGET_SET != WORLD_SCOPE
      TARGET_NOT_SELECTED != TARGET_DOES_NOT_EXIST
      COVERAGE_OF_SELECTED_TARGETS != COMPLETE_DISCOVERY
      OPERATOR_TARGET_SET != AUTHORITATIVE_TARGET_SET

   Every material coverage claim states its target-set aperture and comparison
   basis. Completeness beyond that aperture remains UNKNOWN.

"""

REQUIRED_TOKENS = (
    "**Version:** v0.2.7 NARROW DRIFT REPAIR CANDIDATE",
    "target-set source and selection basis",
    "### [14.0.1] Canonical existing-object target-set aperture profile",
    "TARGET_SET_PROFILE_PRESENT != TARGET_SET_COMPLETE",
    "## [15.2.1] Divergent target-set apertures over one scene",
    "I57  TARGET_SET != WORLD_SCOPE",
    "I60  OPERATOR_TARGET_SET != AUTHORITATIVE_TARGET_SET",
    "TRACE // FORMAL SEED v0.2.7 // SURVIVAL KERNEL",
    "Pi_T = <source, targets, selection_basis,",
    "This v0.2.7 narrow drift-repair pass succeeds the released v0.2.6",
    "A selected target set can omit materially affected scopes",
)


@dataclass(frozen=True)
class VerificationReport:
    status: str
    base_sha256: str
    compiled_sha256: str
    base_lines: int
    compiled_lines: int
    schema_shape_identical: bool
    node_vocabulary_unchanged: bool
    edge_vocabulary_unchanged: bool
    required_packet_properties_unchanged: bool
    old_machine_identifier_occurrences: int
    errors: tuple[str, ...]

    def as_dict(self) -> dict[str, Any]:
        return {
            "candidate": "TRACE_FORMAL_SEED_v0_2_7",
            "status": self.status,
            "base_sha256": self.base_sha256,
            "compiled_sha256": self.compiled_sha256,
            "base_lines": self.base_lines,
            "compiled_lines": self.compiled_lines,
            "schema_shape_identical": self.schema_shape_identical,
            "node_vocabulary_unchanged": self.node_vocabulary_unchanged,
            "edge_vocabulary_unchanged": self.edge_vocabulary_unchanged,
            "required_packet_properties_unchanged": self.required_packet_properties_unchanged,
            "old_machine_identifier_occurrences": self.old_machine_identifier_occurrences,
            "errors": list(self.errors),
            "claim_boundary": "COMPILED_WORKING_CANDIDATE_NOT_RELEASED_NOT_CANON_NOT_VALIDATED",
        }


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"{label}: expected exactly one anchor, observed {count}")
    return text.replace(old, new, 1)


def insert_before(text: str, marker: str, insertion: str, label: str) -> str:
    return replace_once(text, marker, insertion.rstrip() + "\n\n" + marker, label)


def replace_between(text: str, start_marker: str, end_marker: str, replacement: str, label: str) -> str:
    start = text.find(start_marker)
    if start < 0:
        raise ValueError(f"{label}: start marker absent")
    end = text.find(end_marker, start + len(start_marker))
    if end < 0:
        raise ValueError(f"{label}: end marker absent")
    if text.find(start_marker, start + 1) >= 0:
        raise ValueError(f"{label}: start marker not unique")
    return text[:start] + replacement.rstrip() + "\n\n" + text[end:]


def insert_before_last_fence(text: str, start_marker: str, end_marker: str, insertion: str, label: str) -> str:
    start = text.find(start_marker)
    end = text.find(end_marker, start + len(start_marker))
    if start < 0 or end < 0:
        raise ValueError(f"{label}: section markers absent")
    section = text[start:end]
    fence = section.rfind("```")
    if fence < 0:
        raise ValueError(f"{label}: closing fence absent")
    updated = section[:fence] + insertion.rstrip() + "\n" + section[fence:]
    return text[:start] + updated + text[end:]


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
                item.replace("TRACE-GRAPH-0.2.7", "TRACE-GRAPH-0.2.6")
                .replace("urn:trace:graph:0.2.7", "urn:trace:graph:0.2.6")
                .replace("0.2.7", "0.2.6")
            )
        return item

    return walk(copy.deepcopy(value))


def schema_vocab(schema: dict[str, Any], name: str) -> tuple[str, ...]:
    enum = schema.get("$defs", {}).get(name, {}).get("properties", {}).get("type", {}).get("enum", [])
    return tuple(enum)


def required_packet_properties(schema: dict[str, Any]) -> tuple[str, ...]:
    return tuple(schema.get("properties", {}).get("trace_graph", {}).get("required", []))


def compile_seed(base: str) -> str:
    text = base
    text = replace_once(
        text,
        "**Version:** v0.2.6 TARGET-SET APERTURE CANDIDATE  ",
        "**Version:** v0.2.7 NARROW DRIFT REPAIR CANDIDATE  ",
        "version header",
    )
    text = replace_once(text, "**Date:** 2026-08-04  ", "**Date:** 2026-08-05  ", "date")

    # Synchronize machine and document identifiers before inserting historical
    # references to v0.2.6 in the new succession declaration.
    text = text.replace("0_2_6", "0_2_7")
    text = text.replace("0.2.6", "0.2.7")

    text = replace_once(
        text,
        "limits of the reader\n```",
        "limits of the reader\n" + MIDDLE_OUT_ADDITION.rstrip() + "\n```",
        "middle-out target-set propagation",
    )

    text = insert_before(
        text,
        "## [14.1] Binding rules",
        PROFILE_SECTION,
        "canonical target-set serialization profile",
    )

    text = insert_before(
        text,
        "## [15.3] Machine-speed action with brake",
        WORKED_EXAMPLE,
        "constructed divergent-aperture transfer",
    )

    text = replace_once(
        text,
        "I56  TRACE_MAP != DOMAIN_PROPOSAL\n```",
        "I56  TRACE_MAP != DOMAIN_PROPOSAL\n" + INVARIANTS_ADDITION + "```",
        "numbered target-set invariants",
    )

    old_survival = """7. Aperture:\n\n      not_observed_through(Pi_i) != absent\n\n"""
    text = replace_once(text, old_survival, SURVIVAL_APERTURE, "survival-kernel target-set propagation")

    text = replace_between(
        text,
        "## [21.1] Revision declaration",
        "## [21.2] Relationship to previous capsule",
        REVISION_SECTION,
        "revision succession declaration",
    )

    text = insert_before_last_fence(
        text,
        "## [21.4] Unresolved",
        "## [21.5] Construction test",
        UNRESOLVED_ADDITION,
        "unresolved target-set limitations",
    )

    old_boundary = (
        "The v0.2.7 identifier records a revised semantic contract while the embedded minimum-schema shape remains identical to v0.2.5. "
        "The identifier does not imply that the minimum validator can enforce target discovery, target-set adequacy, search coverage, authority legitimacy, route execution, brake effectiveness, correction, or world correspondence.\n\n"
        "A v0.2.5 packet is not silently relabelled as v0.2.7. Structural compatibility does not erase packet identity or the semantic contract under which the packet was produced."
    )
    new_boundary = (
        "The v0.2.7 identifier records a narrow documentary, serialization-profile, and worked-transfer repair while the embedded minimum-schema shape remains identical to v0.2.6 after version normalization. "
        "The identifier does not imply that the minimum validator can enforce target discovery, target-set adequacy, search coverage, authority legitimacy, route execution, brake effectiveness, correction, or world correspondence.\n\n"
        "A v0.2.6 packet is not silently relabelled as v0.2.7. Structural compatibility does not erase packet identity or the semantic contract under which the packet was produced."
    )
    text = replace_once(text, old_boundary, new_boundary, "minimum-validator succession boundary")

    if not text.endswith("\n"):
        text += "\n"
    return text


def verify_compiled(base: str, compiled: str) -> VerificationReport:
    errors: list[str] = []

    for token in REQUIRED_TOKENS:
        if token not in compiled:
            errors.append(f"missing required token: {token}")

    machine_old_tokens = (
        "TRACE-GRAPH-0.2.6",
        "urn:trace:graph:0.2.6",
        "initialise_TRACE_GRAPH_0_2_6()",
        'validate_schema(R, "TRACE-GRAPH-0.2.6")',
    )
    old_machine_identifier_occurrences = sum(compiled.count(token) for token in machine_old_tokens)
    if old_machine_identifier_occurrences:
        errors.append(f"old machine identifiers remain: {old_machine_identifier_occurrences}")

    if compiled.count("### [14.0.1] Canonical existing-object target-set aperture profile") != 1:
        errors.append("canonical target-set profile must occur exactly once")
    if compiled.count("## [15.2.1] Divergent target-set apertures over one scene") != 1:
        errors.append("constructed divergent-aperture example must occur exactly once")
    if compiled.count("I57  TARGET_SET != WORLD_SCOPE") != 1:
        errors.append("I57 invariant must occur exactly once")
    if compiled.count("Pi_T = <source, targets, selection_basis,") != 1:
        errors.append("survival-kernel target tuple must occur exactly once")

    base_schema = extract_minimum_schema(base)
    compiled_schema = extract_minimum_schema(compiled)
    schema_shape_identical = normalize_schema_version(compiled_schema) == base_schema
    if not schema_shape_identical:
        errors.append("minimum schema changed beyond synchronized identifiers")

    node_vocabulary_unchanged = schema_vocab(base_schema, "node") == schema_vocab(compiled_schema, "node")
    edge_vocabulary_unchanged = schema_vocab(base_schema, "edge") == schema_vocab(compiled_schema, "edge")
    required_unchanged = required_packet_properties(base_schema) == required_packet_properties(compiled_schema)
    if not node_vocabulary_unchanged:
        errors.append("node vocabulary changed")
    if not edge_vocabulary_unchanged:
        errors.append("edge vocabulary changed")
    if not required_unchanged:
        errors.append("required packet properties changed")

    if compiled_schema.get("$id") != URN:
        errors.append("compiled schema $id mismatch")
    if compiled_schema.get("title") != f"{SCHEMA_ID} minimum validator":
        errors.append("compiled schema title mismatch")

    graph_properties = compiled_schema.get("properties", {}).get("trace_graph", {}).get("properties", {})
    if graph_properties.get("schema", {}).get("const") != SCHEMA_ID:
        errors.append("packet schema const mismatch")
    if graph_properties.get("trace_version", {}).get("const") != VERSION:
        errors.append("trace_version const mismatch")

    if compiled.count("initialise_TRACE_GRAPH_0_2_7()") != 1:
        errors.append("pseudocode initializer mismatch")
    if compiled.count('validate_schema(R, "TRACE-GRAPH-0.2.7")') != 1:
        errors.append("pseudocode validator target mismatch")

    if "TARGET_SET" in schema_vocab(compiled_schema, "node"):
        errors.append("TARGET_SET node type was introduced")
    if "target_set_apertures" in required_packet_properties(compiled_schema):
        errors.append("target_set_apertures became a required packet property")

    base_lines = len(base.splitlines())
    compiled_lines = len(compiled.splitlines())
    if compiled_lines <= base_lines:
        errors.append("compiled seed did not grow despite bounded repair")

    return VerificationReport(
        status="PASS" if not errors else "FAIL",
        base_sha256=hashlib.sha256(base.encode("utf-8")).hexdigest(),
        compiled_sha256=hashlib.sha256(compiled.encode("utf-8")).hexdigest(),
        base_lines=base_lines,
        compiled_lines=compiled_lines,
        schema_shape_identical=schema_shape_identical,
        node_vocabulary_unchanged=node_vocabulary_unchanged,
        edge_vocabulary_unchanged=edge_vocabulary_unchanged,
        required_packet_properties_unchanged=required_unchanged,
        old_machine_identifier_occurrences=old_machine_identifier_occurrences,
        errors=tuple(errors),
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args()

    base = BASE_PATH.read_text(encoding="utf-8")
    compiled = compile_seed(base)
    report = verify_compiled(base, compiled)

    if args.write:
        OUTPUT_PATH.write_text(compiled, encoding="utf-8")

    if args.check:
        if not OUTPUT_PATH.exists():
            print("FAIL: committed output is absent")
            return 1
        committed = OUTPUT_PATH.read_text(encoding="utf-8")
        if committed != compiled:
            print("FAIL: committed output differs from deterministic compiler output")
            return 1

    rendered = json.dumps(report.as_dict(), indent=2, sort_keys=True)
    print(rendered)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(rendered + "\n", encoding="utf-8")

    return 0 if report.status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
