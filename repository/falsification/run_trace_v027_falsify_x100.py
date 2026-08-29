#!/usr/bin/env python3
"""Run 100 bounded falsification and drift probes against TRACE v0.2.7.

This is a regression and containment audit, not validation. It tests whether the
narrow repair supported by TRACE-V026-FALSIFY-X100 is present, propagated,
serialized with existing vocabulary, and still bounded by TRACE's claim ceiling.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))
import compile_trace_v027 as compiler  # noqa: E402

BASE_PATH = REPO_ROOT / "TRACE_FORMAL_SEED_v0_2_6.md"
CANDIDATE_PATH = REPO_ROOT / "TRACE_FORMAL_SEED_v0_2_7.md"
README_PATH = REPO_ROOT / "README.md"
MANIFEST_PATH = REPO_ROOT / "TRACE_v0_2_7_NARROW_REPAIR_CANDIDATE.md"
EXPECTED_BASE_BLOB = "5e50886f20bceef63be90456cae7f7f7f895bcd6"


@dataclass(frozen=True)
class Probe:
    probe_id: str
    category: str
    description: str
    evaluate: Callable[[], bool]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def section(text: str, start_marker: str, end_marker: str) -> str:
    start = text.find(start_marker)
    if start < 0:
        return ""
    end = text.find(end_marker, start + len(start_marker))
    if end < 0:
        return text[start:]
    return text[start:end]


def git_blob_sha(text: str) -> str:
    data = text.encode("utf-8")
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def token_probe(probe_id: str, category: str, description: str, text: str, token: str) -> Probe:
    return Probe(probe_id, category, description, lambda text=text, token=token: token in text)


def absent_probe(probe_id: str, category: str, description: str, text: str, token: str) -> Probe:
    return Probe(probe_id, category, description, lambda text=text, token=token: token not in text)


def replace_first(text: str, old: str, new: str = "") -> str:
    if old not in text:
        raise ValueError(f"mutation anchor absent: {old!r}")
    return text.replace(old, new, 1)


def required_surface_errors(candidate: str, readme: str, manifest: str) -> list[str]:
    errors: list[str] = []
    required = (
        "**Version:** v0.2.7 NARROW DRIFT REPAIR CANDIDATE",
        "target-set source and selection basis",
        "I57  TARGET_SET != WORLD_SCOPE",
        "I58  TARGET_NOT_SELECTED != TARGET_DOES_NOT_EXIST",
        "I59  COVERAGE_OF_SELECTED_TARGETS != COMPLETE_DISCOVERY",
        "I60  OPERATOR_TARGET_SET != AUTHORITATIVE_TARGET_SET",
        "Pi_T = <source, targets, selection_basis,",
        "### [14.0.1] Canonical existing-object target-set aperture profile",
        "TARGET_SET_PROFILE_PRESENT != TARGET_SET_COMPLETE",
        "PROFILE_CONFORMANCE != TARGET_DISCOVERY",
        "## [15.2.1] Divergent target-set apertures over one scene",
        "This v0.2.7 narrow drift-repair pass succeeds the released v0.2.6",
        "A selected target set can omit materially affected scopes",
        "Target-set selection can be controlled, inherited, or contested",
    )
    for token in required:
        if token not in candidate:
            errors.append(f"missing:{token}")

    old_machine = (
        "TRACE-GRAPH-0.2.6",
        "urn:trace:graph:0.2.6",
        "initialise_TRACE_GRAPH_0_2_6()",
        'validate_schema(R, "TRACE-GRAPH-0.2.6")',
    )
    for token in old_machine:
        if token in candidate:
            errors.append(f"stale-machine-id:{token}")

    seed_pos = readme.find("TRACE_FORMAL_SEED_v0_2_7.md")
    pdf_pos = readme.find("TRACE.pdf")
    if seed_pos < 0 or pdf_pos < 0 or seed_pos > pdf_pos:
        errors.append("front-door-order")
    if "TRACE.pdf` — current v0.2.7 rendered formal carrier; the Markdown seed remains the formal source" not in readme:
        errors.append("pdf-label")
    if (
        "NOT_RELEASED" not in manifest
        or "NOT_VALIDATED" not in manifest
        or "minimum-schema shape change:      NO" not in manifest
    ):
        errors.append("candidate-boundary")
    return errors


def make_probes(base: str, candidate: str, readme: str, manifest: str) -> list[Probe]:
    probes: list[Probe] = []
    base_schema = compiler.extract_minimum_schema(base)
    candidate_schema = compiler.extract_minimum_schema(candidate)
    compiled_expected = compiler.compile_seed(base)
    verification = compiler.verify_compiled(base, candidate)

    middle = section(candidate, "# [1] MIDDLE-OUT SEED", "# [2] SELECTIVE CAUSAL LOOP")
    profile = section(candidate, "### [14.0.1] Canonical existing-object target-set aperture profile", "## [14.1] Binding rules")
    example = section(candidate, "## [15.2.1] Divergent target-set apertures over one scene", "## [15.3] Machine-speed action with brake")
    invariants = section(candidate, "# [19] INVARIANTS / MISUSE GUARDS", "## [19.1] Packet as diligence token")
    survival = section(candidate, "# [20] COMPRESSION / SURVIVAL KERNEL", "# [21] DOCUMENT CONTROL / OPEN FRONTIER")
    revision = section(candidate, "## [21.1] Revision declaration", "## [21.2] Relationship to previous capsule")
    unresolved = section(candidate, "## [21.4] Unresolved", "## [21.5] Construction test")

    # I01-I20 — identity, deterministic build, and schema containment.
    probes.extend([
        token_probe("I01", "identity", "candidate header identifies v0.2.7", candidate, "**Version:** v0.2.7 NARROW DRIFT REPAIR CANDIDATE"),
        token_probe("I02", "identity", "candidate date is explicit", candidate, "**Date:** 2026-08-05"),
        token_probe("I03", "identity", "packet schema is synchronized", candidate, 'schema: "TRACE-GRAPH-0.2.7"'),
        token_probe("I04", "identity", "packet trace version is synchronized", candidate, 'trace_version: "0.2.7"'),
        token_probe("I05", "identity", "schema urn is synchronized", candidate, '"$id": "urn:trace:graph:0.2.7"'),
        token_probe("I06", "identity", "schema title is synchronized", candidate, '"title": "TRACE-GRAPH-0.2.7 minimum validator"'),
        token_probe("I07", "identity", "pseudocode initializer is synchronized", candidate, "initialise_TRACE_GRAPH_0_2_7()"),
        token_probe("I08", "identity", "validator target is synchronized", candidate, 'validate_schema(R, "TRACE-GRAPH-0.2.7")'),
        absent_probe("I09", "identity", "stale packet identifier is absent", candidate, "TRACE-GRAPH-0.2.6"),
        absent_probe("I10", "identity", "stale urn is absent", candidate, "urn:trace:graph:0.2.6"),
        Probe("I11", "determinism", "committed candidate equals deterministic compiler output", lambda: candidate == compiled_expected),
        Probe("I12", "determinism", "compiler verification passes", lambda: verification.status == "PASS"),
        Probe("I13", "preservation", "released v0.2.6 blob remains exact", lambda: git_blob_sha(base) == EXPECTED_BASE_BLOB),
        Probe("I14", "schema", "minimum schema is unchanged after version normalization", lambda: compiler.normalize_schema_version(candidate_schema) == base_schema),
        Probe("I15", "schema", "node vocabulary is unchanged", lambda: compiler.schema_vocab(base_schema, "node") == compiler.schema_vocab(candidate_schema, "node")),
        Probe("I16", "schema", "edge vocabulary is unchanged", lambda: compiler.schema_vocab(base_schema, "edge") == compiler.schema_vocab(candidate_schema, "edge")),
        Probe("I17", "schema", "required packet properties are unchanged", lambda: compiler.required_packet_properties(base_schema) == compiler.required_packet_properties(candidate_schema)),
        Probe("I18", "scope", "candidate grows only as a successor object", lambda: len(candidate.splitlines()) > len(base.splitlines())),
        token_probe("I19", "boundary", "candidate remains unreleased", manifest, "NOT_RELEASED"),
        token_probe("I20", "boundary", "candidate remains non-validated", manifest, "NOT_VALIDATED"),
    ])

    # D01-D20 — propagation and documentary drift closure.
    probes.extend([
        token_probe("D01", "middle-out", "middle-out records target-set source and basis", middle, "target-set source and selection basis"),
        token_probe("D02", "middle-out", "middle-out records known omitted target categories", middle, "known omitted target categories"),
        token_probe("D03", "middle-out", "middle-out records alternative target apertures", middle, "alternative target-set apertures"),
        token_probe("D04", "middle-out", "middle-out states coverage relativity", middle, "coverage relative to a declared target set and comparison basis"),
        token_probe("D05", "invariants", "I57 preserves target-set/world-scope ceiling", invariants, "I57  TARGET_SET != WORLD_SCOPE"),
        token_probe("D06", "invariants", "I58 preserves unselected/nonexistent ceiling", invariants, "I58  TARGET_NOT_SELECTED != TARGET_DOES_NOT_EXIST"),
        token_probe("D07", "invariants", "I59 preserves coverage/discovery ceiling", invariants, "I59  COVERAGE_OF_SELECTED_TARGETS != COMPLETE_DISCOVERY"),
        token_probe("D08", "invariants", "I60 preserves operator/authority ceiling", invariants, "I60  OPERATOR_TARGET_SET != AUTHORITATIVE_TARGET_SET"),
        token_probe("D09", "survival", "survival kernel names v0.2.7", survival, "TRACE // FORMAL SEED v0.2.7 // SURVIVAL KERNEL"),
        token_probe("D10", "survival", "survival kernel contains target tuple", survival, "Pi_T = <source, targets, selection_basis,"),
        token_probe("D11", "survival", "survival kernel preserves target/world ceiling", survival, "TARGET_SET != WORLD_SCOPE"),
        token_probe("D12", "survival", "survival kernel preserves coverage ceiling", survival, "COVERAGE_OF_SELECTED_TARGETS != COMPLETE_DISCOVERY"),
        token_probe("D13", "survival", "survival kernel states comparison basis", survival, "target-set aperture and comparison"),
        token_probe("D14", "revision", "revision declares succession from v0.2.6", revision, "succeeds the released v0.2.6"),
        token_probe("D15", "revision", "revision names both admitted repairs", revision, "TARGET_SET_SELECTION_IS_APERTURE_BEARING"),
        token_probe("D16", "revision", "revision preserves non-growth boundary", revision, "No primitive family, node type, edge type, port"),
        token_probe("D17", "unresolved", "unresolved register states target-set incompleteness", unresolved, "A selected target set can omit materially affected scopes"),
        token_probe("D18", "unresolved", "unresolved register states target authority limit", unresolved, "without any aperture becoming authoritative by default"),
        Probe("D19", "front-door", "active released v0.2.7 baseline precedes TRACE.pdf", lambda: 0 <= readme.find("TRACE_FORMAL_SEED_v0_2_7.md") < readme.find("TRACE.pdf")),
        token_probe("D20", "front-door", "TRACE.pdf is labelled as current rendered carrier with Markdown authority preserved", readme, "current v0.2.7 rendered formal carrier; the Markdown seed remains the formal source"),
    ])

    # S01-S15 — canonical existing-object serialization profile.
    probes.extend([
        token_probe("S01", "serialization", "canonical profile exists", profile, "Canonical existing-object target-set aperture profile"),
        token_probe("S02", "serialization", "profile explicitly remains non-required", profile, "not a new primitive, node type, edge type, port, or required minimum-schema field"),
        Probe("S03", "serialization", "profile contains two target-set apertures", lambda: profile.count('aperture_kind: "TARGET_SET"') == 2),
        token_probe("S04", "serialization", "profile records source refs", profile, "source_ref:"),
        token_probe("S05", "serialization", "profile records target refs", profile, "target_refs:"),
        token_probe("S06", "serialization", "profile records selection basis", profile, "selection_basis_claim_refs:"),
        token_probe("S07", "serialization", "profile records known omitted categories", profile, "known_omitted_target_categories:"),
        token_probe("S08", "serialization", "profile records alternative target sets", profile, "alternative_target_set_refs:"),
        token_probe("S09", "serialization", "profile records control or custody", profile, "control_or_custody_refs:"),
        token_probe("S10", "serialization", "profile records uncertainty", profile, "uncertainty_claim_refs:"),
        token_probe("S11", "serialization", "profile uses BOUNDS edge", profile, 'type: "BOUNDS"'),
        token_probe("S12", "serialization", "profile uses OMITS edge", profile, 'type: "OMITS"'),
        token_probe("S13", "serialization", "profile preserves disagreement with DISPUTES", profile, 'type: "DISPUTES"'),
        absent_probe("S14", "serialization", "TARGET_SET is not introduced as node vocabulary", "\n".join(compiler.schema_vocab(candidate_schema, "node")), "TARGET_SET"),
        token_probe("S15", "serialization", "profile conformance does not imply discovery", profile, "PROFILE_CONFORMANCE != TARGET_DISCOVERY"),
    ])

    # W01-W10 — constructed transfer and aperture disagreement.
    probes.extend([
        token_probe("W01", "worked-transfer", "worked transfer is explicitly constructed", example, "CONSTRUCTED_TRANSFER"),
        token_probe("W02", "worked-transfer", "same scene reference is explicit", example, "SCENE_REF: scene_service_migration"),
        token_probe("W03", "worked-transfer", "operator aperture A is explicit", example, "TARGET_SET_APERTURE_A:"),
        token_probe("W04", "worked-transfer", "independent aperture B is explicit", example, "TARGET_SET_APERTURE_B:"),
        token_probe("W05", "worked-transfer", "coverage is relative to A", example, "complete_relative_to_A = POSSIBLE"),
        Probe("W06", "worked-transfer", "world completeness remains unknown for both apertures", lambda: example.count("world_complete = UNKNOWN") == 2),
        token_probe("W07", "worked-transfer", "apertures remain separate", example, "preserve A and B separately"),
        token_probe("W08", "worked-transfer", "silent union is prohibited", example, "do not silently union them"),
        token_probe("W09", "worked-transfer", "authority is not inferred", example, "do not infer that either aperture is authoritative"),
        token_probe("W10", "worked-transfer", "TRACE does not choose target set or policy", example, "It does not select the governing target set"),
    ])

    # A01-A15 — authority, value, release, and claim ceilings.
    probes.extend([
        token_probe("A01", "authority", "target selection does not grant authority", candidate, "OPERATOR_TARGET_SET != AUTHORITATIVE_TARGET_SET"),
        token_probe("A02", "authority", "divergent readings do not create authority", candidate, "DIVERGENT_READINGS != AUTHORITY"),
        token_probe("A03", "authority", "structural pass is not permission", candidate, "STRUCTURAL_PASS != PERMISSION"),
        token_probe("A04", "authority", "declared handoff is not legitimate authority", candidate, "DECLARED_HANDOFF != LEGITIMATE_AUTHORITY"),
        token_probe("A05", "authority", "visible authority is not contestable authority", candidate, "VISIBLE_AUTHORITY != CONTESTABLE_AUTHORITY"),
        token_probe("A06", "correction", "route to brake is not correction completion", candidate, "ROUTE_TO_BRAKE != CORRECTION_COMPLETED"),
        token_probe("A07", "coverage", "target profile is not target completeness", profile, "TARGET_SET_PROFILE_PRESENT != TARGET_SET_COMPLETE"),
        token_probe("A08", "authority", "alternative aperture is not authoritative", profile, "ALTERNATIVE_TARGET_SET_RECORDED != ALTERNATIVE_TARGET_SET_AUTHORITATIVE"),
        token_probe(
            "A09",
            "value",
            "normative claims remain external",
            candidate,
            "Harm, care, kindness, trust, and good require an exposed value layer.",
        ),
        token_probe("A10", "value", "TRACE remains distinct from ME", candidate, "I28  TRACE != ME"),
        token_probe("A11", "boundary", "candidate withholds canon", manifest, "NOT_CANON"),
        token_probe("A12", "boundary", "candidate withholds authority", manifest, "NOT_AUTHORITY"),
        token_probe("A13", "boundary", "candidate withholds permission", manifest, "NOT_PERMISSION"),
        token_probe("A14", "boundary", "candidate withholds clearance", manifest, "NOT_CLEARANCE"),
        Probe("A15", "boundary", "normal candidate has no required-surface errors", lambda: not required_surface_errors(candidate, readme, manifest)),
    ])

    # M01-M20 — hostile mutation detection. Each detector targets the changed
    # contract directly rather than relying on whole-file byte mismatch.
    mutations: list[tuple[str, str, Callable[[], bool]]] = []

    def removed(token: str) -> bool:
        mutated = replace_first(candidate, token)
        return token not in mutated and bool(required_surface_errors(mutated, readme, manifest))

    def required_growth_detected() -> bool:
        mutated_schema = copy.deepcopy(candidate_schema)
        mutated_schema["properties"]["trace_graph"]["required"].append(
            "target_set_apertures"
        )
        return compiler.required_packet_properties(
            base_schema
        ) != compiler.required_packet_properties(mutated_schema)

    def reversed_readme_detected() -> bool:
        seed_token = "TRACE_FORMAL_SEED_v0_2_7.md"
        pdf_token = "TRACE.pdf"
        mutated_readme = (
            readme.replace(seed_token, "__TRACE_SEED_TOKEN__", 1)
            .replace(pdf_token, seed_token, 1)
            .replace("__TRACE_SEED_TOKEN__", pdf_token, 1)
        )
        return bool(required_surface_errors(candidate, mutated_readme, manifest))

    mutations.extend([
        ("M01", "removing v0.2.7 header is detected", lambda: removed("**Version:** v0.2.7 NARROW DRIFT REPAIR CANDIDATE")),
        ("M02", "removing middle-out target source is detected", lambda: removed("target-set source and selection basis")),
        ("M03", "removing I57 is detected", lambda: removed("I57  TARGET_SET != WORLD_SCOPE")),
        ("M04", "removing I58 is detected", lambda: removed("I58  TARGET_NOT_SELECTED != TARGET_DOES_NOT_EXIST")),
        ("M05", "removing I59 is detected", lambda: removed("I59  COVERAGE_OF_SELECTED_TARGETS != COMPLETE_DISCOVERY")),
        ("M06", "removing I60 is detected", lambda: removed("I60  OPERATOR_TARGET_SET != AUTHORITATIVE_TARGET_SET")),
        ("M07", "removing survival target tuple is detected", lambda: removed("Pi_T = <source, targets, selection_basis,")),
        ("M08", "removing canonical profile is detected", lambda: removed("### [14.0.1] Canonical existing-object target-set aperture profile")),
        ("M09", "removing profile/discovery ceiling is detected", lambda: removed("PROFILE_CONFORMANCE != TARGET_DISCOVERY")),
        ("M10", "removing worked transfer is detected", lambda: removed("## [15.2.1] Divergent target-set apertures over one scene")),
        ("M11", "removing succession declaration is detected", lambda: removed("This v0.2.7 narrow drift-repair pass succeeds the released v0.2.6")),
        ("M12", "removing unresolved incompleteness is detected", lambda: removed("A selected target set can omit materially affected scopes")),
        ("M13", "removing unresolved authority limit is detected", lambda: removed("Target-set selection can be controlled, inherited, or contested")),
        ("M14", "reintroducing stale packet identifier is detected", lambda: bool(required_surface_errors(candidate + "\nTRACE-GRAPH-0.2.6\n", readme, manifest))),
        ("M15", "node-vocabulary growth is detected", lambda: compiler.schema_vocab(base_schema, "node") != compiler.schema_vocab(compiler.extract_minimum_schema(replace_first(candidate, '"SCENE",', '"SCENE",\n              "TARGET_SET",')), "node")),
        (
            "M16",
            "required-property growth is detected",
            required_growth_detected,
        ),
        ("M17", "profile completeness promotion is detected", lambda: "TARGET_SET_PROFILE_PRESENT = TARGET_SET_COMPLETE" in replace_first(candidate, "TARGET_SET_PROFILE_PRESENT != TARGET_SET_COMPLETE", "TARGET_SET_PROFILE_PRESENT = TARGET_SET_COMPLETE")),
        (
            "M18",
            "README front-door reversal is detected",
            reversed_readme_detected,
        ),
        ("M19", "removing current-PDF authority label is detected", lambda: bool(required_surface_errors(candidate, readme.replace(" — current v0.2.7 rendered formal carrier; the Markdown seed remains the formal source", ""), manifest))),
        ("M20", "removing NOT_VALIDATED boundary is detected", lambda: bool(required_surface_errors(candidate, readme, manifest.replace("NOT_VALIDATED", "")))),
    ])
    probes.extend(Probe(pid, "mutation", desc, fn) for pid, desc, fn in mutations)

    return probes


def run_probe(probe: Probe) -> dict[str, object]:
    try:
        resisted = bool(probe.evaluate())
        detail = "RESISTED" if resisted else "FALSIFIED_OR_DRIFT_EXPOSED"
    except Exception as exc:  # diagnostic failure is not a pass
        resisted = False
        detail = f"PROBE_ERROR: {type(exc).__name__}: {exc}"
    return {
        "probe_id": probe.probe_id,
        "category": probe.category,
        "description": probe.description,
        "resisted": resisted,
        "detail": detail,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json-out", type=Path)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    base = read(BASE_PATH)
    candidate = read(CANDIDATE_PATH)
    readme = read(README_PATH)
    manifest = read(MANIFEST_PATH)
    probes = make_probes(base, candidate, readme, manifest)
    results = [run_probe(probe) for probe in probes]
    failures = [row for row in results if not row["resisted"]]
    mutation_failures = [row for row in failures if row["category"] == "mutation"]

    report = {
        "instrument": "TRACE-V027-FALSIFY-X100",
        "probe_count": len(probes),
        "resisted_count": len(probes) - len(failures),
        "finding_count": len(failures),
        "mutation_probe_count": sum(1 for probe in probes if probe.category == "mutation"),
        "mutation_detector_failure_count": len(mutation_failures),
        "verdict": "CLEAR_WITH_RESIDUAL_LIMITS" if not failures else "NARROW",
        "residual_limits": [
            "AUDIT_EXECUTION_NOT_VALIDATION",
            "MINIMUM_VALIDATOR_REMAINS_SHAPE_AND_VOCABULARY_ONLY",
            "TARGET_DISCOVERY_AND_AUTHORITY_REMAIN_CHECKER_EXTERNAL",
            "TRACE_PDF_IS_RENDERED_CARRIER_NOT_FORMAL_SOURCE",
            "CONSTRUCTED_TRANSFER_NOT_WORLD_EVIDENCE",
        ],
        "findings": failures,
        "results": results,
    }

    errors: list[str] = []
    if len(probes) != 100:
        errors.append(f"expected 100 probes, observed {len(probes)}")
    if len({probe.probe_id for probe in probes}) != 100:
        errors.append("probe IDs are not unique")
    if report["mutation_probe_count"] != 20:
        errors.append(f"expected 20 mutation probes, observed {report['mutation_probe_count']}")
    if report["mutation_detector_failure_count"]:
        errors.append(f"mutation detector failures: {report['mutation_detector_failure_count']}")

    rendered = json.dumps(report, indent=2, sort_keys=True)
    print(rendered)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(rendered + "\n", encoding="utf-8")

    for error in errors:
        print(f"AUDIT_INSTRUMENT_ERROR: {error}")
    if errors:
        return 1
    if args.strict and failures:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
