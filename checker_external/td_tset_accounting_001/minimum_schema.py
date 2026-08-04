"""Extract and apply TRACE v0.2.5's embedded minimum JSON Schema."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Mapping

from jsonschema import Draft202012Validator

SECTION_MARKER = "## [14.4] Minimum validator contract"
JSON_FENCE = "```json"
DEFAULT_SEED_PATH = Path(__file__).resolve().parents[2] / "TRACE_FORMAL_SEED_v0_2_5.md"


class MinimumSchemaError(ValueError):
    """Raised when the embedded schema cannot be extracted or used."""


def extract_minimum_schema(seed_path: Path = DEFAULT_SEED_PATH) -> dict[str, Any]:
    try:
        text = seed_path.read_text(encoding="utf-8")
    except OSError as exc:
        raise MinimumSchemaError(f"cannot read TRACE seed {seed_path}: {exc}") from exc

    try:
        section_start = text.index(SECTION_MARKER)
        fence_start = text.index(JSON_FENCE, section_start) + len(JSON_FENCE)
        fence_end = text.index("\n```", fence_start)
    except ValueError as exc:
        raise MinimumSchemaError(
            f"cannot locate the embedded minimum schema after {SECTION_MARKER!r}"
        ) from exc

    payload = text[fence_start:fence_end].strip()
    try:
        schema = json.loads(payload)
    except json.JSONDecodeError as exc:
        raise MinimumSchemaError(f"embedded minimum schema is not valid JSON: {exc}") from exc

    if not isinstance(schema, dict):
        raise MinimumSchemaError("embedded minimum schema must be a JSON object")

    Draft202012Validator.check_schema(schema)
    return schema


def schema_sha256(schema: Mapping[str, Any]) -> str:
    canonical = json.dumps(schema, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


def validation_errors(
    trace_graph: Mapping[str, Any],
    *,
    seed_path: Path = DEFAULT_SEED_PATH,
) -> list[str]:
    schema = extract_minimum_schema(seed_path)
    validator = Draft202012Validator(schema)
    envelope = {"trace_graph": dict(trace_graph)}
    errors = sorted(validator.iter_errors(envelope), key=lambda item: list(item.absolute_path))

    rendered: list[str] = []
    for error in errors:
        path = "/".join(str(part) for part in error.absolute_path) or "<root>"
        rendered.append(f"{path}: {error.message}")
    return rendered


def assert_schema_valid(
    trace_graph: Mapping[str, Any],
    *,
    seed_path: Path = DEFAULT_SEED_PATH,
) -> None:
    errors = validation_errors(trace_graph, seed_path=seed_path)
    if errors:
        raise MinimumSchemaError("minimum-schema validation failed:\n- " + "\n- ".join(errors))


def _main(argv: list[str] | None = None) -> int:
    from applied_scene_001 import APPLIED_FIXTURES

    parser = argparse.ArgumentParser(
        description="Validate the applied witnesses against TRACE v0.2.5's embedded schema."
    )
    parser.add_argument("--compact", action="store_true", help="emit compact JSON")
    parser.add_argument("--seed", type=Path, default=DEFAULT_SEED_PATH)
    args = parser.parse_args(argv)

    schema = extract_minimum_schema(args.seed)
    rows: list[dict[str, Any]] = []
    failed = False
    for fixture in APPLIED_FIXTURES:
        errors = validation_errors(fixture["trace_graph"], seed_path=args.seed)
        status = "FAIL" if errors else "PASS"
        failed = failed or bool(errors)
        rows.append(
            {
                "fixture_id": fixture["fixture_id"],
                "schema_status": status,
                "errors": errors,
            }
        )

    output = {
        "schema_id": schema.get("$id"),
        "schema_sha256": schema_sha256(schema),
        "seed_path": str(args.seed),
        "all_schema_valid": not failed,
        "results": rows,
    }
    print(json.dumps(output, indent=None if args.compact else 2, sort_keys=True))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(_main())
