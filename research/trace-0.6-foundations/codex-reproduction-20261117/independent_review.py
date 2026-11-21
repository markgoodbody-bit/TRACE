"""Offline independent checks against an explicitly acquired Build commit.

All distributions and mutations are synthetic or public repository source.
No source file in source/ is modified. The oracle is a closed-form calculation,
not another copy of the simulator's policy enumeration.
"""

import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import inspect
import itertools
import json
from pathlib import Path
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "source"
WORK = ROOT
ACQUISITION = ROOT / "ACQUISITION.json"


def load(name):
    spec = importlib.util.spec_from_file_location(name, SOURCE / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def compositions(total, count):
    if count == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for rest in compositions(total - first, count - 1):
                yield (first,) + rest


def run():
    acquisition = json.loads(ACQUISITION.read_text(encoding="utf-8"))
    names = [Path(row["path"]).name for row in acquisition["files"]]
    for row, name in zip(acquisition["files"], names):
        assert hashlib.sha256((SOURCE / name).read_bytes()).hexdigest() == row["sha256"], name

    def copy_candidate(target):
        target.mkdir(parents=True, exist_ok=False)
        for name in names:
            shutil.copyfile(SOURCE / name, target / name)

    simulator = load("simulator")
    cells = tuple(itertools.product((False, True), repeat=3))
    laws = comparisons = 0
    for counts in compositions(4, 8):
        rows = [{"direct": d, "f1": a, "f2": b, "prob": str(F(n, 4))}
                for (d, a, b), n in zip(cells, counts) if n]
        direct = sum((F(n, 4) for (d, a, b), n in zip(cells, counts) if d), F(0))
        fallback = sum((F(n, 4) for (d, a, b), n in zip(cells, counts) if a and b), F(0))
        residual = sum((F(n, 4) for (d, a, b), n in zip(cells, counts)
                        if not d and a and b), F(0))
        for cap, demand, timing in itertools.product(range(4), (1, 2, 3), ("early", "late")):
            feasible = cap >= demand
            expected = (direct + (residual if feasible else 0) if timing == "early"
                        else max(direct, fallback if feasible else 0))
            actual = F(simulator.support(rows, timing, cap, demand)["success"])
            assert actual == expected, (counts, cap, demand, timing, actual, expected)
            comparisons += 1
        laws += 1

    # Fréchet endpoint and independent-law controls using the actual API.
    dependence = []
    for overlap in (F(0), F(9, 50), F(1, 4)):
        p, q = F(18, 25), F(1, 4)
        weights = {(True, True): overlap, (True, False): p - overlap,
                   (False, True): q - overlap, (False, False): 1 - p - q + overlap}
        # A fallback pair either both succeeds or both fails in this encoding.
        rows = [{"direct": d, "f1": f, "f2": f, "prob": str(w)}
                for (d, f), w in weights.items() if w]
        actual = F(simulator.support(rows, "early", 2)["success"])
        assert actual == p + q - overlap
        dependence.append({"direct_fallback_overlap": str(overlap), "success": str(actual)})

    # Rejected inputs exercise the external parameter boundary, not only literals.
    valid = [{"direct": False, "f1": True, "f2": True, "prob": "1"}]
    invalid = [
        ([], "early", 2, 2),
        ([{"direct": True, "f1": True, "f2": True, "prob": "-1"}], "early", 2, 2),
        ([{"direct": True, "f1": True, "f2": True, "prob": "3/2"}], "early", 2, 2),
        ([{"direct": 1, "f1": True, "f2": True, "prob": "1"}], "early", 2, 2),
        (valid + valid, "early", 2, 2),
        ([{**valid[0], "extra": 1}], "early", 2, 2),
        (valid, "unknown", 2, 2),
        (valid, "early", True, 2),
        (valid, "early", -1, 2),
        (valid, "early", 2, 0),
        (valid, "early", 2, F(3, 2)),
    ]
    rejected = 0
    for rows, timing, cap, demand in invalid:
        try:
            simulator.support(rows, timing, cap, demand)
        except ValueError:
            rejected += 1
        else:
            raise AssertionError("Invalid input accepted")

    delivery_checks = 0
    cancellation_keyword = None
    cancellation_regressions = 0
    if hasattr(simulator, "delivery_route"):
        parameters = inspect.signature(simulator.delivery_route).parameters
        cancellation_keyword = ("backup_cancelled_before_delivery"
                                if "backup_cancelled_before_delivery" in parameters
                                else "backup_cancelled")
        # Resolve unknown times both before and after the declared boundary.
        # Set-valued outcomes give the three-valued oracle under this static
        # availability/cancellation contract, independently of the implementation.
        values = (None, 0, 4, 6, 7, 8)
        for primary, backup, available, cancelled, ack in itertools.product(
                values, values, (False, True), (False, True), (None, 3)):
            arrivals = [primary] + ([backup] if available and not cancelled else [])
            completions = [(0, 8) if t is None else (t,) for t in arrivals]
            outcomes = {any(t <= 6 and t < 7 for t in world)
                        for world in itertools.product(*completions)}
            expected = ("SUPPORTED_IN_MODEL" if outcomes == {True}
                        else "NOT_SUPPORTED_IN_MODEL" if outcomes == {False} else "UNKNOWN")
            fields = dict(acknowledgement_time=ack, delivery_time=primary,
                          backup_available=available, backup_time=backup,
                          due_time=6, hardening_time=7)
            fields[cancellation_keyword] = cancelled
            actual = simulator.delivery_route(**fields)["status"]
            assert actual == expected, (primary, backup, available, cancelled, ack)
            delivery_checks += 1
        if cancellation_keyword == "backup_cancelled_before_delivery":
            sample = dict(acknowledgement_time=1, delivery_time=8,
                          backup_available=True, backup_time=4, due_time=6,
                          hardening_time=7)
            assert simulator.delivery_route(**sample,
                backup_cancelled_before_delivery=True)["status"] == "NOT_SUPPORTED_IN_MODEL"
            assert simulator.delivery_route(**sample,
                backup_cancelled_before_delivery=False)["status"] == "SUPPORTED_IN_MODEL"
            try:
                simulator.delivery_route(**sample, backup_cancelled=True)
            except TypeError:
                cancellation_regressions = 3
            else:
                raise AssertionError("Legacy ambiguous cancellation keyword accepted")

    # Independent coverage check operates on bytes, not the generator's functions.
    manifest = json.loads((SOURCE / "crosswalk.json").read_text(encoding="utf-8"))
    raw = (SOURCE / "TRACE-v0.5-reference.md").read_bytes()
    lines = raw.splitlines(keepends=True)
    assert hashlib.sha256(raw).hexdigest() == manifest["source_sha256"]
    assert hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest() == manifest["source_git_blob"]
    counts = {}
    for key in ("units", "review_blocks"):
        cursor = 1
        for record in manifest[key]:
            assert record["start_line"] == cursor
            body = b"".join(lines[record["start_line"] - 1:record["end_line"]])
            assert hashlib.sha256(body).hexdigest() == record["sha256"]
            assert record["status"] == "UNRESOLVED"
            cursor = record["end_line"] + 1
        assert cursor == len(lines) + 1
        counts[key] = len(manifest[key])

    # Each mutation is in a fresh task-local copy. Existing directories cause a
    # stop rather than silently overwriting another run. No cleanup/deletion.
    mutation_results = []
    for name, filename, appended in (
        ("reference", "TRACE-v0.5-reference.md", b"\n"),
        ("candidate", "CANDIDATE.md", b"\nChanged independent review fixture.\n"),
        ("manifest", "crosswalk.json", b"\n"),
        ("spine", "SPINE.md", b"\nChanged independent review fixture.\n"),
    ):
        target = WORK / "mutations" / name
        if target.exists():
            raise FileExistsError("Mutation directory already exists; preserve previous receipt")
        copy_candidate(target)
        changed = target / filename
        changed.write_bytes(changed.read_bytes() + appended)
        proc = subprocess.run([sys.executable, "-I", "-S", "-B", str(target / "build_views.py"), "--check"],
                              capture_output=True, text=True, encoding="utf-8")
        assert proc.returncode != 0, name
        mutation_results.append({"mutation": name, "exit_code": proc.returncode,
                                 "diagnostic": (proc.stdout + proc.stderr).strip().splitlines()[-1]})

    # Run the documented generator on a copy. Windows line-ending translation
    # may change bytes, so record text/JSON and byte results separately.
    regen = WORK / "mutations" / "regenerate"
    if regen.exists():
        raise FileExistsError("Regeneration directory already exists")
    copy_candidate(regen)
    proc = subprocess.run([sys.executable, "-I", "-S", "-B", str(regen / "build_views.py")],
                          capture_output=True, text=True, encoding="utf-8")
    assert proc.returncode == 0, proc.stderr
    regenerated = {}
    for name in ("crosswalk.json", "SPINE.md"):
        original, generated = (SOURCE / name).read_bytes(), (regen / name).read_bytes()
        text_equal = original.decode("utf-8").replace("\r\n", "\n") == generated.decode("utf-8").replace("\r\n", "\n")
        assert text_equal
        regenerated[name] = {"byte_equal": original == generated, "lf_normalized_text_equal": text_equal}
    proc = subprocess.run([sys.executable, "-I", "-S", "-B", str(regen / "build_views.py"), "--check"],
                          capture_output=True, text=True, encoding="utf-8")
    assert proc.returncode == 0

    return {"source": acquisition["source"], "status": "PASS",
            "scope": "Finite shared-law oracle and mechanical source/derived-view checks; not full TRACE semantics.",
            "joint_laws_quarter_grid": laws, "policy_capacity_comparisons": comparisons,
            "dependence_controls": dependence, "invalid_inputs_rejected": rejected,
            "delivery_completion_comparisons": delivery_checks,
            "cancellation_keyword": cancellation_keyword,
            "cancellation_regressions": cancellation_regressions,
            "coverage": counts, "all_semantic_dispositions": "UNRESOLVED",
            "mutation_rejections": mutation_results, "regeneration": regenerated}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=SOURCE)
    parser.add_argument("--work-dir", type=Path, default=WORK)
    parser.add_argument("--acquisition", type=Path, default=ACQUISITION)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    SOURCE = args.source.resolve(strict=True)
    WORK = args.work_dir.resolve()
    ACQUISITION = args.acquisition.resolve(strict=True)
    WORK.mkdir(parents=True, exist_ok=True)
    result = run()
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
