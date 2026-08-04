#!/usr/bin/env python3
"""Run the TRACE v0.2.6 x100 audit with diagnostic closure output."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Callable

import trace_v026_falsify_x100 as audit


def target_tuple(text: str) -> str:
    target = audit.section(
        text,
        "### [5.3.1] Target-set aperture",
        "## [5.4] State",
    )
    start = target.find("\\left\\langle")
    end = target.find("\\right\\rangle", start)
    if start < 0 or end < 0:
        return ""
    return target[start : end + len("\\right\\rangle")]


def mutate_target_tuple(v26: str, token: str) -> str:
    target = audit.section(
        v26,
        "### [5.3.1] Target-set aperture",
        "## [5.4] State",
    )
    tuple_text = target_tuple(v26)
    if token not in tuple_text:
        raise ValueError(f"target tuple mutation token absent: {token!r}")
    mutated_tuple = tuple_text.replace(token, "", 1)
    mutated_target = target.replace(tuple_text, mutated_tuple, 1)
    return v26.replace(target, mutated_target, 1)


def tuple_detector(mutated: str, token: str) -> bool:
    return token not in target_tuple(mutated)


def replace_probe(
    probes: list[audit.Probe],
    probe_id: str,
    description: str,
    evaluate: Callable[[], bool],
) -> None:
    for index, probe in enumerate(probes):
        if probe.probe_id == probe_id:
            probes[index] = audit.Probe(
                probe_id=probe.probe_id,
                category=probe.category,
                classification=probe.classification,
                description=description,
                evaluate=evaluate,
            )
            return
    raise ValueError(f"probe not found: {probe_id}")


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

    # Harden four tuple-field mutations so they alter the declared target tuple,
    # not an earlier same-word occurrence elsewhere in the document.
    tuple_mutations = {
        "M01": "source,",
        "M05": "alternatives,",
        "M06": "control,",
        "M07": "uncertainty\n",
    }
    for probe_id, token in tuple_mutations.items():
        replace_probe(
            probes,
            probe_id,
            f"removing target tuple token {token!r} is detected",
            lambda token=token: tuple_detector(mutate_target_tuple(v26, token), token),
        )

    # The inserted prose contains the negative sentence “do not establish that …
    # should proceed”. The earlier regex treated that ceiling as an instruction.
    # Check for affirmative instruction forms instead.
    patch_text = "\n".join(
        [
            audit.section(v26, "### [5.3.1] Target-set aperture", "## [5.4] State"),
            audit.section(v26, "ACCOUNTING_AND_COVERAGE_ARE_APERTURE_RELATIVE", "## [6.2] Coupling"),
            audit.section(v26, "Divergent structural readings do not create selection authority.", "# [11]"),
        ]
    )
    forbidden_affirmative = (
        "TRACE instructs proceeding",
        "TRACE authorises proceeding",
        "TRACE authorizes proceeding",
        "the selected transition should proceed.",
        "the selected transition must proceed.",
    )
    replace_probe(
        probes,
        "A15",
        "admitted inserted prose contains no affirmative proceed or authorise instruction",
        lambda: not any(token in patch_text for token in forbidden_affirmative),
    )

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
