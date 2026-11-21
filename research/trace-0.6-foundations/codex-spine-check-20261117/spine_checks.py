"""Targeted generator checks for the exact new Build pin, not a semantic audit."""

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys


def run(source, work, acquisition):
    a = json.loads(acquisition.read_text(encoding="utf-8"))
    names = [Path(x["path"]).name for x in a["files"]]
    for row, name in zip(a["files"], names):
        assert hashlib.sha256((source / name).read_bytes()).hexdigest() == row["sha256"]
    outcomes = []

    def cli(target, script, *args):
        r = subprocess.run([sys.executable, "-E", "-S", "-B", str(target / script), *args],
                           capture_output=True, text=True, encoding="utf-8")
        tail = r.stderr.strip().splitlines()
        return {"exit_code": r.returncode, "stdout": r.stdout.strip(),
                "stderr_last_line": tail[-1] if tail else ""}

    def clone(name):
        target = work / name
        target.mkdir(parents=True, exist_ok=False)
        for filename in names:
            shutil.copyfile(source / filename, target / filename)
        return target

    for script, args in (("build_views.py", ("--check",)), ("check_reviews.py", ())):
        result = cli(source, script, *args)
        assert result["exit_code"] == 0, result
        outcomes.append({"case": "baseline_" + script, **result})

    t = clone("regenerate")
    before = (t / "review-decisions.json").read_bytes()
    assert cli(t, "build_views.py")["exit_code"] == 0
    assert cli(t, "build_views.py", "--check")["exit_code"] == 0
    assert cli(t, "check_reviews.py")["exit_code"] == 0
    assert before == (t / "review-decisions.json").read_bytes()
    assert (source / "SPINE.md").read_text(encoding="utf-8") == (t / "SPINE.md").read_text(encoding="utf-8")
    review_rows = json.loads(before.decode("utf-8"))["reviews"]
    blocks = json.loads((t / "crosswalk.json").read_text(encoding="utf-8"))["review_blocks"]
    assert all(row["status"] == "UNRESOLVED" for row in blocks)
    outcomes.append({"case": "unchanged_regeneration", "review_file_byte_equal": True,
                     "spine_text_equal": True, "partial_reviews": len(review_rows),
                     "unresolved_blocks": len(blocks)})

    spec = importlib.util.spec_from_file_location("tested_build_views", source / "build_views.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    candidate = (source / "CANDIDATE.md").read_text(encoding="utf-8")
    first = candidate.replace("An entity, group or institution", "FIRST_PARAGRAPH_SENTINEL An entity, group or institution", 1)
    late = candidate.replace("The room opens.", "OMITTED_LATE_PARAGRAPH_SENTINEL The room opens.", 1)
    assert first != candidate and late != candidate
    assert "FIRST_PARAGRAPH_SENTINEL" in module.render_spine(first)
    assert "OMITTED_LATE_PARAGRAPH_SENTINEL" not in module.render_spine(late)
    for malformed in (candidate.replace("## 7. Paired worked probe", "## Missing worked probe", 1),
                      candidate + "\n## 2. Duplicate section\n\nSynthetic duplicate.\n"):
        try:
            module.render_spine(malformed)
        except ValueError:
            pass
        else:
            raise AssertionError("Malformed section structure accepted")
    outcomes.append({"case": "selection_and_structure", "first_paragraph_change_carried": True,
                     "later_paragraph_omitted_as_declared": True, "missing_and_duplicate_sections_rejected": True,
                     "limit": "This is authored selection, not semantic materiality detection."})

    t = clone("changed_candidate")
    changed = candidate.replace("The room opens.", "The room does not open.", 1)
    assert changed != candidate
    (t / "CANDIDATE.md").write_bytes(changed.encode("utf-8"))
    review_before = (t / "review-decisions.json").read_bytes()
    drift = cli(t, "build_views.py", "--check")
    stale = cli(t, "check_reviews.py")
    assert drift["exit_code"] != 0 and stale["exit_code"] != 0
    assert cli(t, "build_views.py")["exit_code"] == 0
    assert cli(t, "build_views.py", "--check")["exit_code"] == 0
    stale_after = cli(t, "check_reviews.py")
    assert stale_after["exit_code"] != 0
    assert review_before == (t / "review-decisions.json").read_bytes()
    outcomes.append({"case": "changed_later_claim", "derived_drift_before_regeneration": drift,
                     "review_stale_before": stale, "review_stale_after_regeneration": stale_after,
                     "review_file_not_rewritten": True,
                     "limit": "Regeneration makes the derived view consistent; it does not reassess the review."})
    for row, name in zip(a["files"], names):
        assert hashlib.sha256((source / name).read_bytes()).hexdigest() == row["sha256"]
    return {"source": a["source"], "status": "PASS", "source_files_unchanged": len(names),
            "scope": "Changed generator, drift and review-anchor interaction only; no numerical baseline rerun.",
            "results": outcomes}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--work-dir", type=Path, required=True)
    parser.add_argument("--acquisition", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run(args.source.resolve(), args.work_dir.resolve(), args.acquisition.resolve())
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k != "results"}, indent=2))
