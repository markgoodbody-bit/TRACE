#!/usr/bin/env python3
"""
comsync - a COMSYNC client that enforces the discipline instead of remembering it.

Design rules, each traceable to a dated failure in live use:

  1. A negative conclusion requires its denominator.
     Refuses task: NONE unless retrieval is provably complete.
     (2026-08-17: page-one-as-tail; reported "no task" twice with a message on page 2.)

  2. Totals are sampled BOTH sides of the walk, and verdicts key to the AFTER total.
     (2026-08-18, found by kimi: a single BEFORE total masks deletion as benign arrival.)

  3. Capability is measured, never read from a file.
     Every row is a probe with a method and a timestamp.
     (2026-08-10..18: a route object declared CC's transport BLOCKED for 8 days
      while correctly ANCHORED to a real commit. It misrouted the third aperture.)

  4. The projection is emitted, not authored.
     If it was not regenerated, its own timestamp says so.
     (2026-08-18: a hand-authored re-derivation decayed in 35 minutes.)

  5. WALK_COMPLETE != SCAN_ADEQUATE.
     A complete retrieval read by an inadequate matcher yields a permitted
     negative conclusion that is wrong.
     (2026-08-18, this client's own first live run: returned NONE for COM#46
      while a directed task to CC sat in it, because the literal marker
      appeared in none of the addressed messages.)

Exit codes: 0 complete, 2 incomplete/degraded/under-matched, 1 error.
"""

import argparse
import datetime
import hashlib
import json
import re
import subprocess
import sys
import urllib.error
import urllib.request

UTC = datetime.timezone.utc


def now():
    return datetime.datetime.now(UTC).isoformat(timespec="seconds")


def gh(path):
    """One GitHub API call via the gh CLI. Returns parsed JSON or None."""
    p = subprocess.run(["gh", "api", path], capture_output=True)
    if p.returncode != 0:
        return None
    try:
        return json.loads(p.stdout.decode("utf-8-sig", errors="replace"))
    except Exception:
        return None


# --------------------------------------------------------------------------
# Rules 1 + 2: retrieval with two-sided reconciliation
# --------------------------------------------------------------------------

def walk_issue(repo, num, max_pages=20):
    """
    Walk an issue's comments completely, sampling known_total before and after.

    Verdicts key to known_total_after. A BEFORE total alone cannot distinguish
    benign arrival from masked deletion, so it is recorded but never decisive.
    """
    issue_before = gh("repos/%s/issues/%d" % (repo, num))
    if issue_before is None:
        return {"repo": repo, "issue": num, "verdict": "ROUTE_FAILURE",
                "retrieval_complete": False, "detail": "issue object unreachable"}
    before = issue_before["comments"]

    comments, page, exhausted = [], 1, False
    while page <= max_pages:
        part = gh("repos/%s/issues/%d/comments?per_page=100&page=%d" % (repo, num, page))
        if part is None:
            return {"repo": repo, "issue": num, "verdict": "ROUTE_FAILURE",
                    "retrieval_complete": False, "returned": len(comments),
                    "detail": "page %d unreachable" % page}
        comments.extend(part)
        if len(part) < 100:
            exhausted = True
            break
        page += 1

    issue_after = gh("repos/%s/issues/%d" % (repo, num))
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


# --------------------------------------------------------------------------
# Rules 1 + 5: a task claim is only as good as the walk AND the matcher
# --------------------------------------------------------------------------

def build_broad_matcher(marker):
    """A second, independent matcher. Its job is to falsify the literal one."""
    role = re.escape(marker.rstrip(":/ ").strip()) or "CC"
    alts = [
        r"(^|\s)@?" + role + r"\b\s*[:/,\-—]",
        r"\b" + role + r"/\d+",
        r"addressed to " + role + r"\b",
        r"\b" + role + r"\b[^\r\n]{0,60}?\b(please|return|challenge|attack|verify)\b",
    ]
    return re.compile("|".join(alts), re.I | re.M)


def addressed_scan(walk, marker):
    """
    NONE requires a complete walk AND a matcher that is not demonstrably
    under-matching. If a broader independent matcher finds items the literal
    one missed, the literal matcher is not a sound basis for a negative claim.
    """
    if not walk.get("retrieval_complete"):
        return {"task": "NOT_ESTABLISHED",
                "basis": "retrieval %s" % walk.get("verdict"),
                "refused_negative_conclusion": True}

    comments = walk["comments"]
    bodies = [(c.get("body") or "") for c in comments]
    literal = [c for c, b in zip(comments, bodies) if marker.lower() in b.lower()]

    broad_re = build_broad_matcher(marker)
    broad = [c for c, b in zip(comments, bodies) if broad_re.search(b)]

    scan = {"matcher_literal": marker,
            "matched_literal": len(literal),
            "matched_broad": len(broad),
            "corpus": walk["returned"]}

    if not literal and broad:
        return {"task": "NOT_ESTABLISHED",
                "basis": "matcher under-matches: a broader independent form found "
                         "items the literal marker missed",
                "refused_negative_conclusion": True,
                "scan_coverage": scan,
                "candidate_ids": [c["id"] for c in broad[-3:]]}

    hits = literal or broad
    if not hits:
        return {"task": "NONE",
                "basis": "complete walk; no item matched either matcher",
                "scan_coverage": scan}

    latest = max(hits, key=lambda c: c["created_at"])
    return {"task": "ADDRESSED", "count": len(hits),
            "latest_id": latest["id"], "latest_at": latest["created_at"],
            "scan_coverage": scan}


# --------------------------------------------------------------------------
# Rule 3: capability is measured, never declared
# --------------------------------------------------------------------------

def probe_http(url, timeout=15):
    started = now()
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "comsync/0.2"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return {"capability": url, "result": "YES", "method": "GET",
                    "status": r.status, "measured_at_utc": started}
    except urllib.error.HTTPError as e:
        return {"capability": url, "result": "YES" if e.code < 500 else "DEGRADED",
                "method": "GET", "status": e.code, "measured_at_utc": started}
    except Exception as e:
        return {"capability": url, "result": "NO", "method": "GET",
                "error": type(e).__name__, "measured_at_utc": started}


def probe_file_sha(path, label):
    started = now()
    try:
        with open(path, "rb") as fh:
            digest = hashlib.sha256(fh.read()).hexdigest()
        return {"capability": label, "result": "YES", "method": "sha256(file)",
                "sha256": digest, "measured_at_utc": started}
    except Exception as e:
        return {"capability": label, "result": "NO", "method": "sha256(file)",
                "error": type(e).__name__, "measured_at_utc": started}


def probe_gh_write(repo):
    """Permission is not capability. Report what the API actually grants."""
    started = now()
    r = gh("repos/%s" % repo)
    if r is None:
        return {"capability": "%s api" % repo, "result": "NO",
                "method": "GET repo", "measured_at_utc": started}
    perms = r.get("permissions") or {}
    return {"capability": "%s write" % repo, "method": "GET repo permissions",
            "result": "YES" if perms.get("push") else "NO",
            "push": bool(perms.get("push")), "admin": bool(perms.get("admin")),
            "measured_at_utc": started}


# --------------------------------------------------------------------------
# Rule 4: the projection is emitted
# --------------------------------------------------------------------------

def emit(walks, probes, tasks, aperture):
    degraded = [w for w in walks if w["verdict"] in ("DEGRADED", "ROUTE_FAILURE")]
    incomplete = [w for w in walks if w["verdict"] in ("INCOMPLETE", "UNKNOWN")]
    refused = [k for k, t in tasks.items() if t.get("refused_negative_conclusion")]
    return {
        "projection_version": "comsync-derived-v0.2",
        "derived_at_utc": now(),
        "derived_by": aperture,
        "derivation": "emitted by comsync; not authored. "
                      "If this timestamp is old, treat as ABSENT.",
        "routes": [dict((k, v) for k, v in w.items() if k != "comments") for w in walks],
        "capability_measured": probes,
        "tasks": tasks,
        "freshness": ("DEGRADED" if degraded else
                      "PARTIAL" if incomplete else "ANCHORED"),
        "negative_conclusions_permitted": not (degraded or incomplete or refused),
        "refused_routes": refused,
    }


def main():
    ap = argparse.ArgumentParser(
        description="COMSYNC client with enforced retrieval and scan discipline")
    ap.add_argument("--repo", default="markgoodbody-bit/COM")
    ap.add_argument("--issues", default="42,46")
    ap.add_argument("--aperture", default="cc-relay")
    ap.add_argument("--marker", default="CC:")
    ap.add_argument("--probe-url", action="append", default=[])
    ap.add_argument("--probe-file", action="append", default=[],
                    help="label=path; hashed and reported")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    walks, tasks = [], {}
    for num in [int(x) for x in args.issues.split(",") if x.strip()]:
        w = walk_issue(args.repo, num)
        walks.append(w)
        if "comments" in w:
            tasks["%s#%d" % (args.repo, num)] = addressed_scan(w, args.marker)

    probes = [probe_gh_write(args.repo)]
    for u in args.probe_url:
        probes.append(probe_http(u))
    for spec in args.probe_file:
        label, _, path = spec.partition("=")
        probes.append(probe_file_sha(path or label, label))

    proj = emit(walks, probes, tasks, args.aperture)

    if args.json:
        print(json.dumps(proj, indent=2))
        return 0 if proj["negative_conclusions_permitted"] else 2

    print("COMSYNC  %s  by %s" % (proj["derived_at_utc"], proj["derived_by"]))
    print("  freshness: %s   negative conclusions permitted: %s"
          % (proj["freshness"], proj["negative_conclusions_permitted"]))
    for r in proj["routes"]:
        print("  %s#%s  before=%s returned=%s after=%s -> %s"
              % (r.get("repo"), r.get("issue"), r.get("known_total_before"),
                 r.get("returned"), r.get("known_total_after"), r["verdict"]))
    for k, t in tasks.items():
        note = ""
        if t.get("refused_negative_conclusion"):
            note = "  <- REFUSED: %s" % t["basis"]
        sc = t.get("scan_coverage")
        cov = ""
        if sc:
            cov = "  [literal %d / broad %d of %d]" % (
                sc["matched_literal"], sc["matched_broad"], sc["corpus"])
        print("  task %s: %s%s%s" % (k, t["task"], cov, note))
    for p in probes:
        print("  capability %s: %s  [%s @ %s]"
              % (p["capability"], p["result"], p["method"], p["measured_at_utc"]))

    return 0 if proj["negative_conclusions_permitted"] else 2


if __name__ == "__main__":
    sys.exit(main())
