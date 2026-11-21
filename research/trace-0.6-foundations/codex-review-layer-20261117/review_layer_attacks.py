"""Exercise the pinned review checker through its actual CLI on public copies."""

import argparse
import copy
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys


def run(source, work, acquisition, checker_override_sha256=None):
    manifest = json.loads(acquisition.read_text(encoding="utf-8"))
    names = [Path(row["path"]).name for row in manifest["files"]]
    for row, name in zip(manifest["files"], names):
        expected = checker_override_sha256 if name == "check_reviews.py" and checker_override_sha256 else row["sha256"]
        assert hashlib.sha256((source / name).read_bytes()).hexdigest() == expected, name
    original = json.loads((source / "review-decisions.json").read_text(encoding="utf-8"))
    outcomes = []

    def invoke(target, name="check_reviews.py", *args):
        return subprocess.run([sys.executable, "-E", "-S", "-B", str(target / name), *args],
                              capture_output=True, text=True, encoding="utf-8")

    def case(name, expectation, change=None, raw=None, alter=None):
        target = work / name
        target.mkdir(parents=True, exist_ok=False)
        for filename in names:
            shutil.copyfile(source / filename, target / filename)
        if raw is not None:
            (target / "review-decisions.json").write_bytes(raw)
        elif change is not None:
            data = copy.deepcopy(original)
            change(data)
            (target / "review-decisions.json").write_bytes((json.dumps(data, ensure_ascii=False) + "\n").encode("utf-8"))
        if alter:
            alter(target)
        proc = invoke(target)
        combined = (proc.stdout + proc.stderr).strip().splitlines()
        outcomes.append({"case": name, "expected": expectation,
                         "accepted": proc.returncode == 0, "exit_code": proc.returncode,
                         "stdout": proc.stdout.strip(),
                         "last_diagnostic": combined[-1] if combined else ""})
        (target / "observed.json").write_text(json.dumps(outcomes[-1], indent=2), encoding="utf-8")
        return target

    def first_field(key, value=None, delete=False):
        def mutate(data):
            if delete:
                del data["reviews"][0][key]
            else:
                data["reviews"][0][key] = value
        return mutate

    case("valid", "accept_15")
    case("stale_source_anchor", "reject", lambda d: d.update(source_sha256="0" * 64))
    case("stale_candidate_anchor", "reject", lambda d: d.update(candidate_sha256="0" * 64))
    case("changed_source_bytes", "reject", alter=lambda t: (t / "TRACE-v0.5-reference.md").write_bytes((t / "TRACE-v0.5-reference.md").read_bytes() + b"\n"))
    case("changed_candidate_bytes", "reject", alter=lambda t: (t / "CANDIDATE.md").write_bytes((t / "CANDIDATE.md").read_bytes() + b"\n"))
    case("changed_block_hash", "reject", first_field("block_sha256", "0" * 64))
    case("unknown_block", "reject", first_field("block_id", "B9999"))
    case("duplicate_block", "reject", lambda d: d["reviews"].append(copy.deepcopy(d["reviews"][0])))
    case("promoted_status", "reject", first_field("status", "REPRODUCED"))
    for key in ("finding", "remaining", "reviewer", "evidence"):
        case("missing_" + key, "reject", first_field(key, delete=True))
        case("blank_" + key, "reject", first_field(key, " \t\n"))
    case("missing_evidence_file", "reject", first_field("evidence", "MISSING.md"))
    case("parent_evidence_path", "reject", first_field("evidence", "../SEMANTIC-REVIEW.md"))
    case("unknown_schema", "reject", lambda d: d.update(schema=2))
    case("boolean_schema", "reject", lambda d: d.update(schema=True))
    case("missing_reviews", "reject", lambda d: d.pop("reviews"))
    case("object_reviews", "reject", lambda d: d.update(reviews={}))
    case("string_reviews", "reject", lambda d: d.update(reviews=""))
    case("null_reviews", "reject", lambda d: d.update(reviews=None))
    case("nonobject_review", "reject", lambda d: d.update(reviews=["not a review"]))
    case("empty_document", "reject", raw=b"")
    case("nonobject_document", "reject", raw=b"[]")
    # Explicitly empty arrays are a valid zero-review state, not false completion.
    case("explicit_empty_reviews", "accept_0", lambda d: d.update(reviews=[]))
    duplicate = json.dumps(original).rstrip()[:-1] + ', "reviews": []}'
    case("duplicate_json_reviews_field", "reject", raw=duplicate.encode("utf-8"))
    # Limits: count is not a provenance/deletion policy, citation presence is not content identity.
    case("intentional_one_review_removed", "limit_accept_14", lambda d: d["reviews"].pop())
    case("evidence_content_replaced", "limit_accept_15", alter=lambda t: (t / "SEMANTIC-REVIEW.md").write_bytes(b"Unrelated synthetic replacement.\n"))

    for filename in ("crosswalk.json", "SPINE.md"):
        t = case("changed_" + filename.replace(".", "_"), "needs_combined_guard",
                 alter=lambda t, f=filename: (t / f).write_bytes((t / f).read_bytes() + b"\nSynthetic drift.\n"))
        proc = invoke(t, "build_views.py", "--check")
        outcomes[-1]["generated_view_check_exit"] = proc.returncode
        assert proc.returncode != 0

    t = case("regeneration", "accept_15")
    before = (t / "review-decisions.json").read_bytes()
    generated = invoke(t, "build_views.py")
    assert generated.returncode == 0
    after = (t / "review-decisions.json").read_bytes()
    assert before == after
    assert invoke(t).returncode == 0
    assert invoke(t, "build_views.py", "--check").returncode == 0
    inventory = json.loads((t / "crosswalk.json").read_text(encoding="utf-8"))
    assert all(row["status"] == "UNRESOLVED" for row in inventory["review_blocks"])
    outcomes[-1].update(review_file_byte_equal_after_regeneration=True,
                        unresolved_blocks=len(inventory["review_blocks"]))

    unexpected = [row["case"] for row in outcomes
                  if row["expected"] == "reject" and row["accepted"]]
    for row in outcomes:
        if row["expected"].startswith("accept_") or row["expected"].startswith("limit_accept_"):
            count = row["expected"].rsplit("_", 1)[1]
            assert row["accepted"] and row["stdout"].startswith(count + " partial reviews"), row
    return {"source_pin": manifest["source"], "cases": len(outcomes),
            "unexpected_acceptances": unexpected,
            "checker_sha256": hashlib.sha256((source / "check_reviews.py").read_bytes()).hexdigest(),
            "results": outcomes}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--work-dir", type=Path, required=True)
    parser.add_argument("--acquisition", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--checker-sha256", help="explicit digest of the sole proposed checker change")
    parser.add_argument("--expect-clean", action="store_true")
    args = parser.parse_args()
    result = run(args.source.resolve(), args.work_dir.resolve(), args.acquisition.resolve(), args.checker_sha256)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k != "results"}, indent=2))
    if args.expect_clean and result["unexpected_acceptances"]:
        raise SystemExit("Unexpected invalid input accepted")
