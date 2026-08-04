#!/usr/bin/env python3
"""Run the TRACE v0.2.6 x100 audit with diagnostic closure output."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import trace_v026_falsify_x100 as audit


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json-out", type=Path)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    v25 = audit.read(audit.V25_PATH)
    v26 = audit.read(audit.V26_PATH)
    release = audit.read(audit.RELEASE_PATH)
    readme = audit.read(audit.README_PATH)

    probes = audit.make_probes(v25, v26, release, readme)
    results = [audit.run_probe(probe) for probe in probes]
    report = audit.summarise(results)

    rendered = json.dumps(report, indent=2, sort_keys=True)
    print(rendered)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(rendered + "\n", encoding="utf-8")

    errors: list[str] = []
    if len(probes) != 100:
        errors.append(f"expected 100 probes, observed {len(probes)}")
    if len({probe.probe_id for probe in probes}) != 100:
        errors.append("probe IDs are not unique")
    if report["mutation_probe_count"] != 20:
        errors.append(f"expected 20 mutation probes, observed {report['mutation_probe_count']}")
    mutation_failures = [
        row["probe_id"]
        for row in report["results"]
        if row["category"] == "mutation" and not row["resisted"]
    ]
    if mutation_failures:
        errors.append("mutation detector failures: " + ", ".join(mutation_failures))

    if errors:
        for error in errors:
            print(f"AUDIT_INSTRUMENT_ERROR: {error}")
        return 1
    if args.strict and report["material_finding_count"]:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
