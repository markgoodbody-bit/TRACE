#!/usr/bin/env python3
"""
comsync - a COMSYNC client that enforces the discipline instead of remembering it.

Design rules, each traceable to a dated failure:

  1. A negative conclusion requires its denominator.
     Refuses task: NONE unless retrieval is provably complete.
     (2026-08-17: page-one-as-tail; reported "no task" twice with a message on page 2.)

  2. Totals are sampled BOTH sides of the walk, and verdicts key to the AFTER total.
     (2026-08-18, kimi: a single BEFORE total masks deletion as benign arrival.)

  3. Capability is measured, never read from a file.
     Every row is a probe with a method and a timestamp.
     (2026-08-10..18: a route object declared CC's transport BLOCKED for 8 days
      while correctly ANCHORED to a real commit. It misrouted the third aperture.)

  4. The projection is emitted, not authored.
     If it was not regenerated, its own timestamp says so.
     (2026-08-18: a hand-authored re-derivation decayed in 35 minutes.)

Exit codes: 0 complete, 2 incomplete/degraded (negative conclusions refused), 1 error.
"""

import argparse
import datetime
import hashlib
import json
import subprocess
import sys
import urllib.error
import urllib.request

UTC = datetime.timezone.utc


def now() -> str:
    return datetime.datetime.now(UTC).isoformat(timespec="seconds")


def gh(path: str):
    """One GitHub API call via the gh CLI. Returns parsed JSON or None."""
    p = subprocess.run(["gh", "api", path], capture_output=True)
    if p.returncode != 0:
        return None
    try:
        return json.loads(p.stdout.decode("utf-8-sig", errors="replace"))
    except Exception:
        return None


# --------------------------------------------------------------------------
# Rule 1 + 2: retrieval with two-sided reconciliation
# --------------------------------------------------------------------------

def walk_issue(repo: str, num: int, max_pages: int = 20) -> dict:
    """
    Walk an issue's comments completely, sampling known_total before and after.

    Verdicts key to known_total_after. A BEFORE total alone cannot distinguish
    benign arrival from masked deletion, so it is recorded but never decisive.
    """
    issue_before = gh(f"repos/{repo}/issues/{num}")
    if issue_before is None:
        return {"verdict": "ROUTE_FAILURE", "retrieval_complete": False,
                "detail": "issue object unreachable"}
    before = issue_before["comments"]

    comments, page, exhausted = [], 1, False
    while page <= max_pages:
        part = gh(f"repos/{repo}/issues/{num}/comments?per_page=100&page={page}")
        if part is None:
            return {"verdict": "ROUTE_FAILURE", "retrieval_complete": False,
                    "detail": f"page {page} unreachable", "returned": len(comments)}
        comments.extend(part)
        if len(part) < 100:
            exhausted = True
            break
        page += 1

    issue_after = gh(f"repos/{repo}/issues/{num}")
    after = issue_after["comments"] if issue_after else None
    returned = len(comments)

    if after is None:
        verdict = "UNKNOWN"
    elif not exhausted:
        verdict = "INCOMPLETE"
    elif returned == after:
        verdict = "COMPLETE"
    elif returned < after:
        verdict = "INCOMPLETE"
    else:
        # returned > known_total_after: objects walked are no longer reflected
        # by the route total. Never silently benign.
        verdict = "DEGRADED"

    return {
        "repo": repo, "issue": num,
        "known_total_before": before,
        "known_total_after": after,
        "returned": returned,
        "pages_fetched": page,
        "pagination_exhausted": exhausted,
        "route_order": "oldest_first",
        "retrieval_complete": verdict == "COMPLETE",
        "verdict": verdict,
        "comments": comments,
        "observed_at_utc": now(),
    }


def addressed_scan(walk: dict, marker: str) -> dict:
    """
    Rule 1. A task claim is only as good as the walk under it.
    NONE is refused unless retrieval_complete.
    """
    if not walk.get("retrieval_complete"):
        return {"task": "NOT_ESTABLISHED",
                "basis": f"retrieval {walk.get('verdict')}",
                "refused_negative_conclusion": True}
    hits = [c for c in walk["comments"] if marker.lower() in (c.get("body") or "").lower()]
    if not hits:
        return {"task": "NONE", "basis": "complete walk, no addressed item",
                "coverage": walk["returned"]}
    latest = max(hits, key=lambda c: c["created_at"])
    return {"task": "ADDRESSED", "count": len(hits),
            "latest_id": latest["id"], "latest_at": latest["created_at"],
            "coverage": walk["returned"]}


# --------------------------------------------------------------------------
# Rule 3: capability is measured, never declared
# --------------------------------------------------------------------------

def probe_http(url: str, timeout: int = 15) -> dict:
    started = now()
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "comsync/0.1"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return {"capability": url, "result": "YES", "method": "GET",
                    "status": r.status, "measured_at_utc": started}
    except urllib.error.HTTPError as e:
        return {"capability": url, "result": "YES" if e.code < 500 else "DEGRADED",
                "method": "GET", "status": e.code, "measured_at_utc": started}
    except Exception as e:
        return {"capability": url, "result": "NO", "method": "GET",
                "error": type(e).__name__, "measured_at_utc": started}


def probe_file_sha(path: str, label: str) -> dict:
    started = now()
    try:
        with open(path, "rb") as fh:
            digest = hashlib.sha256(fh.read()).hexdigest()
        return {"capability": label, "result": "YES", "method": "sha256(file)",
                "sha256": digest, "measured_at_utc": started}
    except Exception as e:
        return {"capability": label, "result": "NO", "method": "sha256(file)",
                "error": type(e).__name__, "measured_at_utc": started}


def probe_gh_write(repo: str) -> dict:
    """Permission is not capability. Report what the API actually grants."""
    started = now()
    r = gh(f"repos/{repo}")
    if r is None:
        return {"capability": f"{repo} api", "result": "NO",
                "method": "GET repo", "measured_at_utc": started}
    perms = r.get("permissions") or {}
    return {"capability": f"{repo} write", "method": "GET repo permissions",
            "result": "YES" if perms.get("push") else "NO",
            "push": bool(perms.get("push")), "admin": bool(perms.get("admin")),
            "measured_at_utc": started}


# --------------------------------------------------------------------------
# Rule 4: the projection is emitted
# --------------------------------------------------------------------------

def emit(walks, probes, tasks, aperture) -> dict:
    degraded = [w for w in walks if w["verdict"] in ("DEGRADED", "ROUTE_FAILURE")]
    incomplete = [w for w in walks if w["verdict"] == "INCOMPLETE"]
    return {
        "projection_version": "comsync-derived-v0.1",
        "derived_at_utc": now(),
        "derived_by": aperture,
        "derivation": "emitted by comsync; not authored. If this timestamp is old, treat as ABSENT.",
        "routes": [{k: v for k, v in w.items() if k != "comments"} for w in walks],
        "capability_measured": probes,
        "tasks": tasks,
        "freshness": ("DEGRADED" if degraded else
                      "PARTIAL" if incomplete else
                      "ANCHORED"),
        "negative_conclusions_permitted": not (degraded or incomplete),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="COMSYNC client with enforced retrieval discipline")
    ap.add_argument("--repo", default="markgoodbody-bit/COM")
    ap.add_argument("--issues", default="42,46", help="comma-separated issue numbers")
    ap.add_argument("--aperture", default="cc-relay")
    ap.add_argument("--marker", default="CC:", help="addressed-to marker to scan for")
    ap.add_argument("--probe-url", action="append", default=[])
    ap.add_argument("--probe-file", action="append", default=[],
                    help="label=path, hashed and reported")
    ap.add_argument("--json", action="store_true", help="emit projection JSON only")
    args = ap.parse_args()

    walks, tasks = [], {}
    for num in [int(x) for x in args.issues.split(",") if x.strip()]:
        w = walk_issue(args.repo, num)
        walks.append(w)
        if "comments" in w:
            tasks[f"{args.repo}#{num}"] = addressed_scan(w, args.marker)

    probes = [probe_gh_write(args.repo)]
    for u in args.probe_url:
        probes.append(probe_http(u))
    for spec in args.probe_file:
        label, _, path = spec.partition("=")
        probes.append(probe_file_sha(path or label, label))

    projection = emit(walks, probes, tasks, args.aperture)

    if args.json:
        print(json.dumps(projection, indent=2))
    else:
        print(f"COMSYNC  {projection['derived_at_utc']}  by {projection['derived_by']}")
        print(f"  freshness: {projection['freshness']}   "
              f"negative conclusions permitted: {projection['negative_conclusions_permitted']}")
        for r in projection["routes"]:
            print(f"  {r.get('repo')}#{r.get('issue')}  before={r.get('known_total_before')} "
                  f"returned={r.get('returned')} after={r.get('known_total_after')} "
                  f"-> {r['verdict']}")
        for k, t in tasks.items():
            extra = "  (negative conclusion REFUSED)" if t.get("refused_negative_conclusion") else ""
            print(f"  task {k}: {t['task']}{extra}")
        for p in probes:
            print(f"  capability {p['capability']}: {p['result']}  "
                  f"[{p['method']} @ {p['measured_at_utc']}]")

    if projection["freshness"] == "DEGRADED":
        return 2
    if not projection["negative_conclusions_permitted"]:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
