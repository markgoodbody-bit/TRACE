#!/usr/bin/env python3
"""Test the fixed-value declarations in the TRACE v0.3.0 minimum schema.

This is a bounded schema-discrimination and burden test. It does not test
whether a packet author understood or applied the declared non-entailments in
the world. Green output establishes only the mechanical facts reported here.
"""

from __future__ import annotations

import argparse
import copy
import importlib.metadata
import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = REPO_ROOT / "PROJECT" / "TRACE_v0_3_0_MINIMUM_SCHEMA_CANDIDATE_v0_1.json"

EXPECTED_FIXED_PATHS = {
    "transition_set.uncertainty_selects_transition",
    "clock_typing.deadline_entails_irreversibility",
    "clock_typing.hardening_entails_irreversibility",
    "scope_granularity.aggregate_recovery_repairs_individual_loss",
    "evidence_custody.control_alone_establishes_deception",
}


def resolve_ref(root: dict[str, Any], ref: str) -> dict[str, Any]:
    if not ref.startswith("#/"):
        raise ValueError(f"only local schema refs are supported: {ref}")
    value: Any = root
    for part in ref[2:].split("/"):
        value = value[part.replace("~1", "/").replace("~0", "~")]
    if not isinstance(value, dict):
        raise TypeError(f"schema ref did not resolve to an object: {ref}")
    return value


def minimal_instance(fragment: dict[str, Any], root: dict[str, Any]) -> Any:
    """Construct one mechanically minimal instance for this bounded schema."""

    if "$ref" in fragment:
        return minimal_instance(resolve_ref(root, fragment["$ref"]), root)
    if "const" in fragment:
        return copy.deepcopy(fragment["const"])
    if "enum" in fragment:
        choices = fragment["enum"]
        return copy.deepcopy("UNKNOWN" if "UNKNOWN" in choices else choices[0])

    type_name = fragment.get("type")
    if type_name == "object" or "properties" in fragment:
        properties = fragment.get("properties", {})
        return {
            name: minimal_instance(properties[name], root)
            for name in fragment.get("required", [])
        }
    if type_name == "array":
        count = int(fragment.get("minItems", 0))
        return [minimal_instance(fragment.get("items", {}), root) for _ in range(count)]
    if type_name == "string":
        return "x" * max(1, int(fragment.get("minLength", 0)))
    if type_name == "integer":
        return int(fragment.get("minimum", 0))
    if type_name == "number":
        return float(fragment.get("minimum", 0))
    if type_name == "boolean":
        return False
    if type_name == "null":
        return None
    if type_name is None:
        return {}
    raise ValueError(f"unsupported schema fragment type: {type_name!r}")


def discipline_schema(schema: dict[str, Any]) -> dict[str, Any]:
    return schema["properties"]["trace_graph"]["properties"]["discipline"]


def fixed_paths(schema: dict[str, Any]) -> set[str]:
    out: set[str] = set()
    discipline = discipline_schema(schema)
    for group_name, group_schema in discipline["properties"].items():
        for field_name, field_schema in group_schema.get("properties", {}).items():
            if field_schema.get("const") is False:
                out.add(f"{group_name}.{field_name}")
    return out


def discipline_counts(schema: dict[str, Any]) -> tuple[int, int, int]:
    discipline = discipline_schema(schema)
    group_count = len(discipline.get("required", []))
    field_count = sum(
        len(discipline["properties"][group].get("required", []))
        for group in discipline.get("required", [])
    )
    return group_count, field_count, group_count + field_count


def errors_for(validator: Draft202012Validator, instance: dict[str, Any]) -> list[str]:
    return [error.message for error in validator.iter_errors(instance)]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="emit JSON only")
    args = parser.parse_args(argv)

    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)
    baseline = minimal_instance(schema, schema)
    baseline_errors = errors_for(validator, baseline)

    observed_fixed_paths = fixed_paths(schema)
    group_count, field_count, total_required_elements = discipline_counts(schema)
    graph = baseline["trace_graph"]

    mutation_results: dict[str, dict[str, Any]] = {}
    for path in sorted(observed_fixed_paths):
        group_name, field_name = path.split(".", 1)

        missing = copy.deepcopy(baseline)
        del missing["trace_graph"]["discipline"][group_name][field_name]
        missing_errors = errors_for(validator, missing)

        flipped = copy.deepcopy(baseline)
        flipped["trace_graph"]["discipline"][group_name][field_name] = True
        flipped_errors = errors_for(validator, flipped)

        mutation_results[path] = {
            "missing_rejected": bool(missing_errors),
            "true_rejected": bool(flipped_errors),
            "false_accepted_in_baseline": not baseline_errors,
        }

    discipline_reference_arrays = []
    for group in graph["discipline"].values():
        for value in group.values():
            if isinstance(value, list):
                discipline_reference_arrays.append(value)

    basisless_declaration_control = {
        "valid": not baseline_errors,
        "all_discipline_reference_arrays_empty": all(
            not value for value in discipline_reference_arrays
        ),
        "meaning": (
            "The schema can require and discriminate the five declarations while "
            "accepting a mechanically minimal packet with no discipline references. "
            "It therefore validates declaration shape/value, not understanding or "
            "world application."
        ),
    }

    errors: list[str] = []
    if baseline_errors:
        errors.append(f"minimal positive control failed: {baseline_errors!r}")
    if observed_fixed_paths != EXPECTED_FIXED_PATHS:
        errors.append(
            "fixed-value path set drifted: "
            f"observed={sorted(observed_fixed_paths)!r}"
        )
    for path, result in mutation_results.items():
        if not result["missing_rejected"]:
            errors.append(f"missing fixed declaration was accepted: {path}")
        if not result["true_rejected"]:
            errors.append(f"true fixed declaration was accepted: {path}")
    if not basisless_declaration_control["all_discipline_reference_arrays_empty"]:
        errors.append("minimal control unexpectedly populated discipline references")

    report = {
        "status": "PASS" if not errors else "FAIL",
        "schema_path": str(SCHEMA_PATH.relative_to(REPO_ROOT)).replace("\\", "/"),
        "jsonschema_version": importlib.metadata.version("jsonschema"),
        "schema_draft_check": "PASS",
        "minimal_positive_control": "PASS" if not baseline_errors else "FAIL",
        "required_discipline_group_objects": group_count,
        "required_fields_inside_discipline_groups": field_count,
        "total_required_discipline_elements_counting_group_objects": total_required_elements,
        "fixed_false_declaration_count": len(observed_fixed_paths),
        "mutation_results": mutation_results,
        "basisless_declaration_control": basisless_declaration_control,
        "disposition": (
            "KEEP_PENDING_COMPARATIVE_BURDEN_EVIDENCE; do not call the declarations "
            "non-discriminating without qualification, and do not treat their schema "
            "acceptance as evidence that the distinctions were understood or applied."
        ),
        "claim_boundary": (
            "SCHEMA_SHAPE_AND_VALUE_DISCRIMINATION_ONLY_NOT_SEMANTIC_APPLICATION_"
            "NOT_WORLD_VALIDITY_NOT_RELEASE_NOT_CANON_NOT_VALIDATION"
        ),
        "errors": errors,
    }

    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(f"status: {report['status']}")
        print(f"required discipline group objects: {group_count}")
        print(f"required fields inside groups: {field_count}")
        print(f"total required discipline elements: {total_required_elements}")
        print(f"fixed false declarations: {len(observed_fixed_paths)}")
        for path, result in mutation_results.items():
            print(
                f"{path}: missing_rejected={result['missing_rejected']} "
                f"true_rejected={result['true_rejected']}"
            )
        print(
            "basisless declaration control valid: "
            f"{basisless_declaration_control['valid']}"
        )
        print(report["claim_boundary"])
        if errors:
            for error in errors:
                print(f"ERROR: {error}")

    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
