#!/usr/bin/env python3
"""
Validate TRACE case graphs against the repository JSON schemas.

Status: runnable drift-control fixture, not validation of TRACE claims.

This script checks whether files under cases/graphs/*.json conform to
schemas/CaseGraph.schema.json and its referenced schemas. Passing this script
means only that the JSON shape matches the schema. It does not mean the claims
inside the graph are true, justified, complete, or decision-useful.

Usage:
  python tests/validate_case_graphs.py
  python tests/validate_case_graphs.py --schema-dir schemas --graph-dir cases/graphs
  python tests/validate_case_graphs.py --json

Exit codes:
  0 = all discovered case graphs validate
  1 = one or more validation failures or no graph files found
  2 = setup/dependency/schema loading failure
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

try:
    import jsonschema
    from jsonschema import Draft202012Validator, FormatChecker
    from jsonschema.exceptions import SchemaError, ValidationError
except ImportError as exc:  # pragma: no cover
    print(
        "ERROR: missing dependency 'jsonschema'. Install with: pip install jsonschema",
        file=sys.stderr,
    )
    raise SystemExit(2) from exc


@dataclass
class ValidationResult:
    path: str
    ok: bool
    errors: list[str]


def repo_root_from_script() -> Path:
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> Any:
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as exc:
        raise RuntimeError(f"Could not load JSON from {path}: {exc}") from exc


def build_store(schema_dir: Path) -> dict[str, Any]:
    """Build a resolver store for local schemas and their $id values."""
    store: dict[str, Any] = {}
    for schema_path in schema_dir.glob("*.schema.json"):
        schema = load_json(schema_path)
        file_uri = schema_path.resolve().as_uri()
        store[file_uri] = schema
        store[schema_path.name] = schema
        if isinstance(schema, dict) and "$id" in schema:
            store[str(schema["$id"])] = schema
            # Also support common relative resolution against the TRACE schema namespace.
            store[f"https://trace.local/schemas/{schema_path.name}"] = schema
    return store


def make_validator(case_graph_schema_path: Path, schema_dir: Path) -> Draft202012Validator:
    schema = load_json(case_graph_schema_path)
    store = build_store(schema_dir)
    resolver = jsonschema.RefResolver(
        base_uri=schema_dir.resolve().as_uri() + "/",
        referrer=schema,
        store=store,
    )
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        raise RuntimeError(f"CaseGraph schema is invalid: {exc}") from exc
    return Draft202012Validator(schema, resolver=resolver, format_checker=FormatChecker())


def format_error(error: ValidationError) -> str:
    path = "/".join(str(p) for p in error.absolute_path)
    if not path:
        path = "<root>"
    schema_path = "/".join(str(p) for p in error.absolute_schema_path)
    return f"{path}: {error.message} [schema: {schema_path}]"


def validate_graph(path: Path, validator: Draft202012Validator) -> ValidationResult:
    try:
        instance = load_json(path)
    except RuntimeError as exc:
        return ValidationResult(str(path), False, [str(exc)])

    errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.absolute_path))
    return ValidationResult(
        path=str(path),
        ok=not errors,
        errors=[format_error(e) for e in errors],
    )


def parse_args(argv: list[str]) -> argparse.Namespace:
    root = repo_root_from_script()
    parser = argparse.ArgumentParser(description="Validate TRACE case graph JSON files.")
    parser.add_argument("--schema-dir", default=str(root / "schemas"), help="Schema directory")
    parser.add_argument("--graph-dir", default=str(root / "cases" / "graphs"), help="Case graph directory")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON report")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    schema_dir = Path(args.schema_dir)
    graph_dir = Path(args.graph_dir)
    case_graph_schema_path = schema_dir / "CaseGraph.schema.json"

    setup_errors: list[str] = []
    if not schema_dir.exists():
        setup_errors.append(f"Schema directory not found: {schema_dir}")
    if not graph_dir.exists():
        setup_errors.append(f"Graph directory not found: {graph_dir}")
    if not case_graph_schema_path.exists():
        setup_errors.append(f"CaseGraph schema not found: {case_graph_schema_path}")

    if setup_errors:
        if args.json:
            print(json.dumps({"ok": False, "setup_errors": setup_errors}, indent=2))
        else:
            for err in setup_errors:
                print(f"ERROR: {err}", file=sys.stderr)
        return 2

    try:
        validator = make_validator(case_graph_schema_path, schema_dir)
    except Exception as exc:
        if args.json:
            print(json.dumps({"ok": False, "setup_errors": [str(exc)]}, indent=2))
        else:
            print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    graph_paths = sorted(graph_dir.glob("*.json"))
    if not graph_paths:
        if args.json:
            print(json.dumps({"ok": False, "setup_errors": ["No case graph JSON files found"]}, indent=2))
        else:
            print(f"ERROR: no case graph JSON files found in {graph_dir}", file=sys.stderr)
        return 1

    results = [validate_graph(path, validator) for path in graph_paths]
    ok = all(result.ok for result in results)

    if args.json:
        print(json.dumps({"ok": ok, "results": [asdict(r) for r in results]}, indent=2))
    else:
        print("TRACE case graph schema validation")
        print("NOTE: schema-valid != true, justified, complete, or decision-useful")
        print(f"Schema: {case_graph_schema_path}")
        print(f"Graphs: {len(graph_paths)}")
        print("")
        for result in results:
            marker = "PASS" if result.ok else "FAIL"
            print(f"[{marker}] {result.path}")
            for err in result.errors:
                print(f"  - {err}")
        print("")
        print("RESULT:", "PASS" if ok else "FAIL")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
