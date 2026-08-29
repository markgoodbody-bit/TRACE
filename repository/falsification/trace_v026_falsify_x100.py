#!/usr/bin/env python3
"""TRACE v0.2.6 falsify-x100 and drift audit.

This is an audit instrument, not a validation oracle. A green execution means the
100 probes ran and the report is internally consistent. It does not mean that the
baseline survived every probe. Use --strict to fail on material findings.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable

ROOT = Path(__file__).resolve().parents[1]
V25_PATH = ROOT / "TRACE_FORMAL_SEED_v0_2_5.md"
V26_PATH = ROOT / "TRACE_FORMAL_SEED_v0_2_6.md"
RELEASE_PATH = ROOT / "TRACE_v0_2_6_BASELINE_RELEASE.md"
README_PATH = ROOT / "README.md"
COMPILER_PATH = ROOT / "tools" / "compile_trace_v026.py"

EXPECTED_RELEASE_SOURCE = "e4df6e9bb7cc6e236395836e41edc6d7025985e6"
EXPECTED_V26_BLOB = "5e50886f20bceef63be90456cae7f7f7f895bcd6"


@dataclass(frozen=True)
class Probe:
    probe_id: str
    category: str
    classification: str
    description: str
    evaluate: Callable[[], bool]


@dataclass(frozen=True)
class Result:
    probe_id: str
    category: str
    classification: str
    description: str
    resisted: bool
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def normalize_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = "\n".join(line.rstrip() for line in text.splitlines())
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def section(text: str, heading: str, next_heading: str | None = None) -> str:
    start = text.find(heading)
    if start < 0:
        return ""
    if next_heading is None:
        return text[start:]
    end = text.find(next_heading, start + len(heading))
    if end < 0:
        return text[start:]
    return text[start:end]


def extract_schema(text: str) -> dict:
    anchor = "## [14.4] Minimum validator contract"
    start = text.find(anchor)
    if start < 0:
        raise ValueError("minimum validator section missing")
    fence_start = text.find("```json", start)
    fence_end = text.find("```", fence_start + 7)
    if fence_start < 0 or fence_end < 0:
        raise ValueError("minimum validator JSON fence missing")
    return json.loads(text[fence_start + 7 : fence_end].strip())


def normalize_schema_versions(value):
    if isinstance(value, dict):
        return {k: normalize_schema_versions(v) for k, v in value.items()}
    if isinstance(value, list):
        return [normalize_schema_versions(v) for v in value]
    if isinstance(value, str):
        return (
            value.replace("TRACE-GRAPH-0.2.6", "TRACE-GRAPH-0.2.5")
            .replace("urn:trace:graph:0.2.6", "urn:trace:graph:0.2.5")
            .replace("0.2.6", "0.2.5")
        )
    return value


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def git_last_message(path: Path) -> str:
    proc = subprocess.run(
        ["git", "log", "-1", "--format=%H%n%s", "--", str(path.relative_to(ROOT))],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return proc.stdout.strip()


def load_compiler():
    spec = importlib.util.spec_from_file_location("trace_v026_compiler", COMPILER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load compiler")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def remove_once_between(text: str, start_marker: str, end_marker: str) -> str:
    start = text.find(start_marker)
    if start < 0:
        raise ValueError(f"missing start marker: {start_marker}")
    end = text.find(end_marker, start + len(start_marker))
    if end < 0:
        raise ValueError(f"missing end marker: {end_marker}")
    return text[:start] + text[end:]


def reverse_v26_to_v25(v26: str) -> str:
    """Independently remove the six admitted insertion families and identifiers."""
    text = v26
    text = remove_once_between(text, "### [5.3.1] Target-set aperture", "## [5.4] State")
    text = remove_once_between(
        text,
        "ACCOUNTING_AND_COVERAGE_ARE_APERTURE_RELATIVE",
        "## [6.2] Coupling",
    )
    text = remove_once_between(
        text,
        "Divergent structural readings do not create selection authority.",
        "# [11] RECURSIVE ZOOM / MANDELBROT RULE",
    )
    text = remove_once_between(
        text,
        "```text\nEvery material search-coverage claim references a target-set aperture",
        "Except for the `CLAIM`-node one-reference cardinality rule",
    )
    text = remove_once_between(
        text,
        "```text\nTARGET_SET_RECORDED != TARGET_SET_COMPLETE",
        "## [14.3] Unresolved commitment receipt",
    )
    boundary_start = (
        "The v0.2.6 identifier records a revised semantic contract while the "
        "embedded minimum-schema shape remains identical to v0.2.5."
    )
    text = remove_once_between(text, boundary_start, "```json")
    text = text.replace("    record_target_set_apertures_and_alternatives(R)\n", "")
    text = text.replace("    separate_information_presence_from_search_coverage(R)\n", "")
    text = text.replace("    preserve_divergent_readings_without_authority_inheritance(R)\n", "")
    text = text.replace("    expose_declared_contest_routes_without_inferring_effectiveness(R)\n", "")
    text = text.replace("    state_transition_and_coverage_results_relative_to_declared_apertures(R)\n", "")
    text = text.replace(
        "**Version:** v0.2.6 TARGET-SET APERTURE CANDIDATE  ",
        "**Version:** v0.2.5 TRANSITION DISCIPLINE CANDIDATE  ",
    )
    text = text.replace("**Date:** 2026-08-04  ", "**Date:** 2026-07-15  ")
    text = text.replace(
        "**Status:** compiled working candidate; unvalidated in the world; non-canonical; voluntary; not authority; not permission; not clearance  ",
        "**Status:** reviewed test baseline; unvalidated in the world; non-canonical; voluntary; not authority; not permission; not clearance  ",
    )
    text = text.replace("0_2_6", "0_2_5")
    text = text.replace("TRACE-GRAPH-0.2.6", "TRACE-GRAPH-0.2.5")
    text = text.replace("urn:trace:graph:0.2.6", "urn:trace:graph:0.2.5")
    text = text.replace("0.2.6", "0.2.5")
    return normalize_text(text)


def target_issues(v26: str) -> set[str]:
    issues: set[str] = set()
    target = section(v26, "### [5.3.1] Target-set aperture", "## [5.4] State")
    field_tokens = {
        "source": "source,",
        "targets": "targets,",
        "selection_basis": "selection\\_basis,",
        "omitted_categories": "omitted\\_known\\_categories,",
        "alternatives": "alternatives,",
        "control": "control,",
        "uncertainty": "uncertainty",
    }
    for name, token in field_tokens.items():
        if token not in target:
            issues.add(f"TARGET_FIELD_{name.upper()}_MISSING")
    required = {
        "TARGET_WORLD": "TARGET_SET != WORLD_SCOPE",
        "NOT_SELECTED": "TARGET_NOT_SELECTED != TARGET_DOES_NOT_EXIST",
        "COVERAGE_COMPLETE": "COVERAGE_OF_SELECTED_TARGETS != COMPLETE_DISCOVERY",
        "OPERATOR_AUTHORITY": "OPERATOR_TARGET_SET != AUTHORITATIVE_TARGET_SET",
        "COMPLETENESS_UNKNOWN": "Completeness beyond that aperture remains `UNKNOWN`.",
        "DIVERGENCE_AUTHORITY": "DIVERGENT_READINGS != AUTHORITY",
        "BINDING_RULE": "Every material search-coverage claim references a target-set aperture",
    }
    for name, token in required.items():
        if token not in v26:
            issues.add(f"TARGET_{name}_MISSING")
    return issues


def schema_issues(v26: str, v25: str) -> set[str]:
    issues: set[str] = set()
    try:
        s26 = extract_schema(v26)
        s25 = extract_schema(v25)
    except Exception:
        return {"SCHEMA_PARSE_FAILURE"}
    if s26.get("$id") != "urn:trace:graph:0.2.6":
        issues.add("SCHEMA_ID_MISMATCH")
    if normalize_schema_versions(s26) != s25:
        issues.add("SCHEMA_SHAPE_DRIFT")
    node26 = s26["$defs"]["node"]["properties"]["type"]["enum"]
    node25 = s25["$defs"]["node"]["properties"]["type"]["enum"]
    if node26 != node25:
        issues.add("NODE_ENUM_DRIFT")
    edge26 = s26["$defs"]["edge"]["properties"]["type"]["enum"]
    edge25 = s25["$defs"]["edge"]["properties"]["type"]["enum"]
    if edge26 != edge25:
        issues.add("EDGE_ENUM_DRIFT")
    req26 = s26["properties"]["trace_graph"]["required"]
    req25 = s25["properties"]["trace_graph"]["required"]
    if req26 != req25:
        issues.add("REQUIRED_PROPERTY_DRIFT")
    return issues


def release_issues(release: str, readme: str) -> set[str]:
    issues: set[str] = set()
    for token in (
        "RELEASED",
        "ACTIVE_FORMAL_BASELINE",
        "NOT_CANON",
        "NOT_VALIDATED",
        "NOT_AUTHORITY",
        "NOT_PERMISSION",
        "NOT_CLEARANCE",
    ):
        if token not in release:
            issues.add(f"RELEASE_BOUNDARY_{token}_MISSING")
    if "TRACE_FORMAL_SEED_v0_2_6.md` — active released formal baseline" not in readme:
        issues.add("README_V26_NOT_ACTIVE_BASELINE")
    if "TRACE_FORMAL_SEED_v0_2_5.md` — preserved reviewed predecessor" not in readme:
        issues.add("README_V25_PREDECESSOR_MISSING")
    return issues


def audit_core(v26: str, v25: str, release: str, readme: str) -> set[str]:
    return target_issues(v26) | schema_issues(v26, v25) | release_issues(release, readme)


def mutate_remove(text: str, token: str) -> str:
    if token not in text:
        raise ValueError(f"mutation token absent: {token}")
    return text.replace(token, "", 1)


def make_probes(v25: str, v26: str, release: str, readme: str) -> list[Probe]:
    compiler = load_compiler()
    schema25 = extract_schema(v25)
    schema26 = extract_schema(v26)
    target = section(v26, "### [5.3.1] Target-set aperture", "## [5.4] State")
    kernel = section(v26, "# [20] COMPRESSION / SURVIVAL KERNEL", "# [21] DOCUMENT CONTROL")
    invariants = section(v26, "# [19] INVARIANTS / MISUSE GUARDS", "## [19.1]")
    revision = section(v26, "## [21.1] Revision declaration", "## [21.2]")
    unresolved = section(v26, "## [21.4] Unresolved", "## [21.5]")
    examples = section(v26, "# [15] WORKED TRANSFORMATIONS", "# [16]")
    middle_out = section(v26, "# [1] MIDDLE-OUT SEED", "# [2]")
    packet = section(v26, "# [14] CANONICAL TRACE GRAPH PACKET", "# [15]")
    patch_text = "\n".join(
        [
            target,
            section(v26, "ACCOUNTING_AND_COVERAGE_ARE_APERTURE_RELATIVE", "## [6.2] Coupling"),
            section(v26, "Divergent structural readings do not create selection authority.", "# [11]"),
        ]
    )

    probes: list[Probe] = []

    def add(pid: str, cat: str, cls: str, desc: str, fn: Callable[[], bool]) -> None:
        probes.append(Probe(pid, cat, cls, desc, fn))

    # 10 release and baseline identity probes.
    add("R01", "release", "IDENTITY", "v0.2.6 formal seed exists", lambda: V26_PATH.is_file())
    add("R02", "release", "IDENTITY", "release declaration exists", lambda: RELEASE_PATH.is_file())
    add("R03", "release", "IDENTITY", "release ID is explicit", lambda: "TRACE-v0.2.6-FORMAL-BASELINE" in release)
    add("R04", "release", "IDENTITY", "release binds exact compiled source commit", lambda: EXPECTED_RELEASE_SOURCE in release)
    add("R05", "release", "IDENTITY", "release-declared blob equals computed Git blob", lambda: git_blob_sha(V26_PATH) == EXPECTED_V26_BLOB and EXPECTED_V26_BLOB in release)
    add("R06", "release", "PRESERVATION", "v0.2.5 predecessor remains present", lambda: V25_PATH.is_file())
    add("R07", "release", "FRONT_DOOR", "README marks v0.2.6 active released baseline", lambda: "TRACE_FORMAL_SEED_v0_2_6.md` — active released formal baseline" in readme)
    add("R08", "release", "PRESERVATION", "README preserves v0.2.5 as predecessor", lambda: "TRACE_FORMAL_SEED_v0_2_5.md` — preserved reviewed predecessor" in readme)
    add("R09", "release", "FRONT_DOOR", "README links release declaration", lambda: "TRACE_v0_2_6_BASELINE_RELEASE.md" in readme)
    add("R10", "release", "FRONT_DOOR_DRIFT", "released formal seed precedes TRACE.pdf in Start here ordering", lambda: readme.find("TRACE_FORMAL_SEED_v0_2_6.md") < readme.find("TRACE.pdf"))

    # 20 version, schema, and compilation containment probes.
    add("V01", "version", "IDENTITY", "v0.2.6 header is present", lambda: "**Version:** v0.2.6 TARGET-SET APERTURE CANDIDATE" in v26)
    add("V02", "version", "IDENTITY", "canonical graph uses TRACE-GRAPH-0.2.6", lambda: 'schema: "TRACE-GRAPH-0.2.6"' in v26)
    add("V03", "version", "IDENTITY", "canonical graph trace_version is 0.2.6", lambda: 'trace_version: "0.2.6"' in v26)
    add("V04", "version", "IDENTITY", "no stale TRACE-GRAPH-0.2.5 identifier remains", lambda: "TRACE-GRAPH-0.2.5" not in v26)
    add("V05", "version", "IDENTITY", "old pseudocode initializer is absent", lambda: "initialise_TRACE_GRAPH_0_2_5" not in v26)
    add("V06", "version", "IDENTITY", "new initializer occurs exactly once", lambda: v26.count("initialise_TRACE_GRAPH_0_2_6()") == 1)
    add("V07", "version", "IDENTITY", "new validator target occurs exactly once", lambda: v26.count('validate_schema(R, "TRACE-GRAPH-0.2.6")') == 1)
    add("V08", "schema", "SCHEMA", "embedded schema ID and title are synchronized", lambda: schema26.get("$id") == "urn:trace:graph:0.2.6" and schema26.get("title") == "TRACE-GRAPH-0.2.6 minimum validator")
    add("V09", "schema", "SCHEMA", "schema shape is identical after version normalization", lambda: normalize_schema_versions(schema26) == schema25)
    add("V10", "schema", "SCHEMA", "node vocabulary is unchanged", lambda: schema26["$defs"]["node"]["properties"]["type"]["enum"] == schema25["$defs"]["node"]["properties"]["type"]["enum"])
    add("V11", "schema", "SCHEMA", "edge vocabulary is unchanged", lambda: schema26["$defs"]["edge"]["properties"]["type"]["enum"] == schema25["$defs"]["edge"]["properties"]["type"]["enum"])
    add("V12", "schema", "SCHEMA", "required top-level packet properties are unchanged", lambda: schema26["properties"]["trace_graph"]["required"] == schema25["properties"]["trace_graph"]["required"])
    add("V13", "schema", "SCHEMA", "no new primitive family is introduced by enum drift", lambda: not schema_issues(v26, v25) & {"NODE_ENUM_DRIFT", "EDGE_ENUM_DRIFT"})
    add("V14", "compile", "DETERMINISM", "independent invocation of compiler reproduces released seed", lambda: normalize_text(compiler.compile_seed(v25)) == normalize_text(v26))
    add("V15", "compile", "DRIFT_CONTAINMENT", "independent reverse transform reconstructs v0.2.5", lambda: reverse_v26_to_v25(v26) == normalize_text(v25))
    add("V16", "compile", "SCOPE", "compiled seed grows rather than replacing the base", lambda: len(v26.splitlines()) > len(v25.splitlines()))
    add("V17", "compile", "SCOPE", "target-set aperture section occurs exactly once", lambda: v26.count("### [5.3.1] Target-set aperture") == 1)
    add("V18", "compile", "SCOPE", "coverage-relativity marker occurs exactly once", lambda: v26.count("ACCOUNTING_AND_COVERAGE_ARE_APERTURE_RELATIVE") == 1)
    add("V19", "compile", "SCOPE", "divergence-authority ceiling occurs exactly once", lambda: v26.count("DIVERGENT_READINGS != AUTHORITY") == 1)
    add("V20", "compile", "DETERMINISM", "compiler verification reports PASS", lambda: compiler.verify_compiled(v25, v26).status == "PASS")

    # 20 target-set and coverage semantics probes.
    add("T01", "target-set", "CORE", "target-set aperture section exists", lambda: bool(target))
    add("T02", "target-set", "CORE", "target-set tuple records source", lambda: "source," in target)
    add("T03", "target-set", "CORE", "target-set tuple records targets", lambda: "targets," in target)
    add("T04", "target-set", "CORE", "target-set tuple records selection basis", lambda: "selection\\_basis," in target)
    add("T05", "target-set", "CORE", "target-set tuple records known omitted categories", lambda: "omitted\\_known\\_categories," in target)
    add("T06", "target-set", "CORE", "target-set tuple records alternatives", lambda: "alternatives," in target)
    add("T07", "target-set", "CORE", "target-set tuple records control", lambda: "control," in target)
    add("T08", "target-set", "CORE", "target-set tuple records uncertainty", lambda: "uncertainty" in target)
    add("T09", "target-set", "NON_ENTAILMENT", "selected target set is not world scope", lambda: "TARGET_SET != WORLD_SCOPE" in target)
    add("T10", "target-set", "NON_ENTAILMENT", "unselected target is not declared nonexistent", lambda: "TARGET_NOT_SELECTED != TARGET_DOES_NOT_EXIST" in target)
    add("T11", "target-set", "NON_ENTAILMENT", "selected-target coverage is not complete discovery", lambda: "COVERAGE_OF_SELECTED_TARGETS != COMPLETE_DISCOVERY" in target)
    add("T12", "target-set", "AUTHORITY", "operator target set is not authoritative target set", lambda: "OPERATOR_TARGET_SET != AUTHORITATIVE_TARGET_SET" in target)
    add("T13", "target-set", "COVERAGE", "coverage claims require target aperture and comparison basis", lambda: "Coverage claims require a declared target-set aperture and comparison basis." in v26)
    add("T14", "target-set", "COVERAGE", "completeness beyond aperture remains UNKNOWN", lambda: "Completeness beyond that aperture remains `UNKNOWN`." in v26)
    add("T15", "target-set", "OPERATOR", "operator records target-set apertures and alternatives", lambda: "record_target_set_apertures_and_alternatives(R)" in v26)
    add("T16", "target-set", "OPERATOR", "operator separates information presence from coverage", lambda: "separate_information_presence_from_search_coverage(R)" in v26)
    add("T17", "target-set", "BINDING", "checker-external material coverage binding is explicit", lambda: "Every material search-coverage claim references a target-set aperture" in v26)
    add("T18", "target-set", "SCOPE", "target-set aperture uses existing object vocabulary", lambda: "does not require a new canonical object type" in target)
    add("T19", "target-set", "SERIALIZATION_DRIFT", "canonical packet supplies a standard target-set serialization block", lambda: "target_set_aperture:" in packet or "target_set_apertures:" in packet)
    add("T20", "target-set", "ALREADY_BOUNDED_LIMITATION", "minimum schema enforces target-set references", lambda: "target_set" in json.dumps(schema26).lower())

    # 15 authority, value-port, and claim-ceiling drift probes.
    add("A01", "authority", "NON_ENTAILMENT", "target selection does not grant authority", lambda: "grant one selection authority" in target)
    add("A02", "authority", "NON_ENTAILMENT", "divergent readings do not create authority", lambda: "DIVERGENT_READINGS != AUTHORITY" in v26)
    add("A03", "authority", "NON_ENTAILMENT", "structural pass is not permission", lambda: "STRUCTURAL_PASS != PERMISSION" in v26)
    add("A04", "authority", "NON_ENTAILMENT", "declared handoff is not legitimate authority", lambda: "DECLARED_HANDOFF != LEGITIMATE_AUTHORITY" in v26)
    add("A05", "authority", "NON_ENTAILMENT", "visible authority is not contestable authority", lambda: "VISIBLE_AUTHORITY != CONTESTABLE_AUTHORITY" in v26)
    add("A06", "authority", "NON_ENTAILMENT", "route to brake is not completed correction", lambda: "ROUTE_TO_BRAKE != CORRECTION_COMPLETED" in v26)
    add("A07", "authority", "AUTHORITY", "target-set disagreement is preserved without silent merge", lambda: "preserves their provenance and disagreement" in target and "does not silently merge them" in target)
    add("A08", "authority", "SCHEMA", "selector vocabulary did not expand", lambda: schema26["$defs"]["node"]["properties"]["type"]["enum"].count("SELECTOR") == 1 and schema26["$defs"]["node"]["properties"]["type"]["enum"] == schema25["$defs"]["node"]["properties"]["type"]["enum"])
    add("A09", "authority", "CLAIM_CEILING", "TRACE still does not select action", lambda: "TRACE does not select" in v26)
    add("A10", "value", "CLAIM_CEILING", "normative claims remain external", lambda: "NORMATIVE_EXTERNAL" in v26 and "not generated by TRACE alone" in v26)
    add("A11", "value", "CLAIM_CEILING", "harm and good remain external value-layer labels", lambda: "`HARM`, `BENEFIT`, `CARE`, `KINDNESS`, `TRUST`, and `GOOD` are not free-standing TRACE primitives." in v26)
    add("A12", "release", "CLAIM_CEILING", "release explicitly withholds canon", lambda: "NOT_CANON" in release)
    add("A13", "release", "CLAIM_CEILING", "release explicitly withholds validation", lambda: "NOT_VALIDATED" in release)
    add("A14", "release", "CLAIM_CEILING", "release withholds authority, permission, and clearance", lambda: all(token in release for token in ("NOT_AUTHORITY", "NOT_PERMISSION", "NOT_CLEARANCE")))
    add("A15", "authority", "DRIFT_GUARD", "admitted inserted prose does not instruct proceeding or authorisation", lambda: not re.search(r"\b(must|shall|should)\s+(proceed|authorise|authorize|deploy|act)\b", patch_text, re.I))

    # 15 partial-ingestion, document-control, and front-door drift probes.
    add("P01", "partial-ingestion", "IDENTITY", "survival kernel identifies v0.2.6", lambda: "TRACE // FORMAL SEED v0.2.6 // SURVIVAL KERNEL" in kernel)
    add("P02", "partial-ingestion", "DOCUMENTARY_DRIFT", "survival kernel preserves target-set aperture", lambda: "TARGET_SET" in kernel or "target-set" in kernel.lower())
    add("P03", "partial-ingestion", "DOCUMENTARY_DRIFT", "survival kernel preserves coverage relativity", lambda: "coverage" in kernel.lower() and "aperture" in kernel.lower())
    add("P04", "partial-ingestion", "DOCUMENTARY_DRIFT", "numbered invariant list contains target-set/world-scope ceiling", lambda: "TARGET_SET != WORLD_SCOPE" in invariants)
    add("P05", "partial-ingestion", "DOCUMENTARY_DRIFT", "numbered invariant list contains target-set/coverage anti-compression", lambda: "TARGET_SET_RECORDED" in invariants or "COVERAGE_CHECK_PASSED" in invariants)
    add("P06", "document-control", "DOCUMENTARY_DRIFT", "revision declaration names target-set aperture repair", lambda: "target-set" in revision.lower())
    add("P07", "document-control", "DOCUMENTARY_DRIFT", "revision declaration distinguishes new repair from v0.2.5 transition-discipline pass", lambda: "v0.2.5" in revision and "v0.2.6" in revision and "target-set" in revision.lower())
    add("P08", "document-control", "DOCUMENTARY_DRIFT", "unresolved list states target-set incompleteness risk", lambda: "target set" in unresolved.lower() or "target-set" in unresolved.lower())
    add("P09", "worked-transfer", "TRANSFER_GAP", "worked transformations include an explicit target-set aperture case", lambda: "target-set aperture" in examples.lower() or "target_set_source_ref" in examples)
    add("P10", "document-control", "CONSTRUCTION_TEST", "construction test retains partial-ingestion survival criterion", lambda: "partial-ingestion survival" in v26)
    add("P11", "partial-ingestion", "DOCUMENTARY_DRIFT", "new repair survives the declared survival kernel", lambda: ("TARGET_SET" in kernel or "target-set" in kernel.lower()) and "coverage" in kernel.lower())
    add("P12", "release", "BOUNDARY", "release explains byte-preserving external promotion", lambda: "does not rewrite the reviewed formal object" in release and "byte-identical" in release)
    add("P13", "front-door", "FRONT_DOOR_DRIFT", "TRACE.pdf postdates or identifies the v0.2.6 baseline", lambda: "v0.2.6" in git_last_message(ROOT / "TRACE.pdf") or "v0.2.6" in (ROOT / "TRACE.pdf").read_bytes().decode("latin-1", errors="ignore"))
    add("P14", "front-door", "FRONT_DOOR_DRIFT", "README warns that TRACE.pdf is an older carrier candidate", lambda: "TRACE.pdf` —" in readme and any(word in readme.lower() for word in ("older", "v0.5", "carrier candidate", "pre-v0.2.6")))
    add("P15", "partial-ingestion", "DOCUMENTARY_DRIFT", "middle-out seed exposes target-set selection as aperture-bearing", lambda: "target-set" in middle_out.lower() or "target set" in middle_out.lower())

    # 20 mutation-resistance probes. Each mutation must be detected by the shared audit.
    mutations: list[tuple[str, str, str, Callable[[], tuple[str, str, str, str]]]] = []

    def mut_v26(token: str, issue: str):
        return lambda: (mutate_remove(v26, token), v25, release, readme)

    fields = [
        ("M01", "source,", "TARGET_FIELD_SOURCE_MISSING"),
        ("M02", "targets,", "TARGET_FIELD_TARGETS_MISSING"),
        ("M03", "selection\\_basis,", "TARGET_FIELD_SELECTION_BASIS_MISSING"),
        ("M04", "omitted\\_known\\_categories,", "TARGET_FIELD_OMITTED_CATEGORIES_MISSING"),
        ("M05", "alternatives,", "TARGET_FIELD_ALTERNATIVES_MISSING"),
        ("M06", "control,", "TARGET_FIELD_CONTROL_MISSING"),
        ("M07", "uncertainty\n\\right", "TARGET_FIELD_UNCERTAINTY_MISSING"),
    ]
    for pid, token, issue in fields:
        add(pid, "mutation", "MUTATION_RESISTANCE", f"removing target tuple token {token!r} is detected", lambda token=token, issue=issue: issue in audit_core(mutate_remove(v26, token), v25, release, readme))

    non_entailments = [
        ("M08", "TARGET_SET != WORLD_SCOPE", "TARGET_TARGET_WORLD_MISSING"),
        ("M09", "TARGET_NOT_SELECTED != TARGET_DOES_NOT_EXIST", "TARGET_NOT_SELECTED_MISSING"),
        ("M10", "COVERAGE_OF_SELECTED_TARGETS != COMPLETE_DISCOVERY", "TARGET_COVERAGE_COMPLETE_MISSING"),
        ("M11", "OPERATOR_TARGET_SET != AUTHORITATIVE_TARGET_SET", "TARGET_OPERATOR_AUTHORITY_MISSING"),
    ]
    for pid, token, issue in non_entailments:
        add(pid, "mutation", "MUTATION_RESISTANCE", f"removing non-entailment {token!r} is detected", lambda token=token, issue=issue: issue in audit_core(mutate_remove(v26, token), v25, release, readme))

    add("M12", "mutation", "MUTATION_RESISTANCE", "promoting aperture completeness is detected", lambda: "TARGET_COMPLETENESS_UNKNOWN_MISSING" in audit_core(v26.replace("Completeness beyond that aperture remains `UNKNOWN`.", "Completeness beyond that aperture is COMPLETE."), v25, release, readme))
    add("M13", "mutation", "MUTATION_RESISTANCE", "turning divergence into authority is detected", lambda: "TARGET_DIVERGENCE_AUTHORITY_MISSING" in audit_core(v26.replace("DIVERGENT_READINGS != AUTHORITY", "DIVERGENT_READINGS = AUTHORITY"), v25, release, readme))
    add("M14", "mutation", "MUTATION_RESISTANCE", "removing material coverage binding is detected", lambda: "TARGET_BINDING_RULE_MISSING" in audit_core(mutate_remove(v26, "Every material search-coverage claim references a target-set aperture"), v25, release, readme))
    add("M15", "mutation", "MUTATION_RESISTANCE", "mixed schema identifier is detected", lambda: "SCHEMA_ID_MISMATCH" in audit_core(v26.replace("urn:trace:graph:0.2.6", "urn:trace:graph:0.2.5", 1), v25, release, readme))

    def add_node_type_mutation() -> bool:
        mutated = copy.deepcopy(schema26)
        mutated["$defs"]["node"]["properties"]["type"]["enum"].append("TARGET_SET")
        mutated_text = v26.replace(json.dumps(schema26, indent=2), json.dumps(mutated, indent=2))
        if mutated_text == v26:
            # Preserve source formatting by editing the first enum close near TARGET types.
            mutated_text = v26.replace('            "LIMIT"\n          ]', '            "LIMIT",\n            "TARGET_SET"\n          ]', 1)
        return "NODE_ENUM_DRIFT" in audit_core(mutated_text, v25, release, readme)

    add("M16", "mutation", "MUTATION_RESISTANCE", "adding TARGET_SET node type is detected", add_node_type_mutation)

    def add_required_property_mutation() -> bool:
        mutated = v26.replace('        "anti_clearance"\n      ],', '        "anti_clearance",\n        "target_set_registry"\n      ],', 1)
        return "REQUIRED_PROPERTY_DRIFT" in audit_core(mutated, v25, release, readme)

    add("M17", "mutation", "MUTATION_RESISTANCE", "adding required packet property is detected", add_required_property_mutation)
    add("M18", "mutation", "MUTATION_RESISTANCE", "removing NOT_VALIDATED release boundary is detected", lambda: "RELEASE_BOUNDARY_NOT_VALIDATED_MISSING" in audit_core(v26, v25, mutate_remove(release, "NOT_VALIDATED"), readme))
    add("M19", "mutation", "MUTATION_RESISTANCE", "demoting README baseline to candidate is detected", lambda: "README_V26_NOT_ACTIVE_BASELINE" in audit_core(v26, v25, release, readme.replace("active released formal baseline", "compiled working candidate", 1)))
    add("M20", "mutation", "MUTATION_RESISTANCE", "removing v0.2.5 predecessor is detected", lambda: "README_V25_PREDECESSOR_MISSING" in audit_core(v26, v25, release, readme.replace("- `TRACE_FORMAL_SEED_v0_2_5.md` — preserved reviewed predecessor and last pre-v0.2.6 baseline\n", "")))

    return probes


def run_probe(probe: Probe) -> Result:
    try:
        resisted = bool(probe.evaluate())
        detail = "RESISTED" if resisted else "FALSIFIED_OR_DRIFT_EXPOSED"
    except Exception as exc:  # audit failure is itself visible
        resisted = False
        detail = f"AUDIT_ERROR: {type(exc).__name__}: {exc}"
    return Result(
        probe.probe_id,
        probe.category,
        probe.classification,
        probe.description,
        resisted,
        detail,
    )


def summarise(results: Iterable[Result]) -> dict:
    rows = list(results)
    findings = [r for r in rows if not r.resisted]
    bounded = [r for r in findings if r.classification == "ALREADY_BOUNDED_LIMITATION"]
    material = [r for r in findings if r.classification not in {"ALREADY_BOUNDED_LIMITATION", "TRANSFER_GAP"}]
    mutation_failures = [r for r in rows if r.category == "mutation" and not r.resisted]
    verdict = "BREAK" if any(r.classification in {"CORE", "IDENTITY", "SCHEMA", "AUTHORITY"} for r in material) else ("NARROW" if material else "CLEAR_WITH_RESIDUAL_LIMITS")
    return {
        "instrument": "TRACE-V026-FALSIFY-X100",
        "claim_boundary": "AUDIT_EXECUTION_NOT_VALIDATION",
        "probe_count": len(rows),
        "resisted_count": sum(r.resisted for r in rows),
        "finding_count": len(findings),
        "material_finding_count": len(material),
        "already_bounded_limitation_count": len(bounded),
        "mutation_probe_count": sum(r.category == "mutation" for r in rows),
        "mutation_detector_failure_count": len(mutation_failures),
        "verdict": verdict,
        "findings": [r.__dict__ for r in findings],
        "results": [r.__dict__ for r in rows],
    }


def self_test(probes: list[Probe], report: dict) -> None:
    ids = [p.probe_id for p in probes]
    if len(probes) != 100:
        raise AssertionError(f"expected 100 probes, observed {len(probes)}")
    if len(set(ids)) != 100:
        raise AssertionError("probe IDs are not unique")
    if report["mutation_probe_count"] != 20:
        raise AssertionError("expected 20 mutation probes")
    if report["mutation_detector_failure_count"] != 0:
        raise AssertionError("one or more mutation detectors failed")
    if report["probe_count"] != 100:
        raise AssertionError("report probe count mismatch")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json-out", type=Path)
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    v25 = read(V25_PATH)
    v26 = read(V26_PATH)
    release = read(RELEASE_PATH)
    readme = read(README_PATH)

    probes = make_probes(v25, v26, release, readme)
    results = [run_probe(p) for p in probes]
    report = summarise(results)
    self_test(probes, report)

    rendered = json.dumps(report, indent=2, sort_keys=True)
    print(rendered)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(rendered + "\n", encoding="utf-8")

    if args.strict and report["material_finding_count"]:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
