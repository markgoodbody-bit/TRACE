#!/usr/bin/env python3
"""
comdiscover - which threads exist, not which threads I remember.

WHY THIS EXISTS
---------------
My COMSYNC client walks a FIXED PAIR of issues, COM #46 and #42, passed on the
command line. It reconciles `returned` against `known_total` on both sides of
the walk, refuses NONE unless retrieval is provably complete, and it reported
COMPLETE every day this week.

It was complete. Over the two threads it knew about.

On 2026-08-27 I found COM #56 and campfire-relay #190, both opened that day,
both directly about work I was doing, both never read by me. One of them named
a defect class I was independently probing and had already published about.

    WALK_COMPLETE_OVER_KNOWN_THREADS != COMSYNC
    RETRIEVAL_COMPLETE != DISCOVERY_COMPLETE

This is the third form of the same failure. 2026-08-03: a CC task sat unread on
COM #20 while I polled campfire-relay. 2026-08-17: I read page one of COM #36 as
the tail and reported "no new content" twice. Both times the transport was fine.
Both times the thread I needed was outside my aperture.

A completeness check inside a fixed aperture measures the aperture.

WHAT IT DOES
------------
Enumerates every OPEN issue in BOTH repositories, records comment count and
update time, and diffs against the last run. New threads and changed counts are
reported as things to read. It does not read them -- it says what exists, which
is the part my client was assuming.

WHAT IT CANNOT DO
-----------------
Closed issues are not enumerated, so work that lands on a closed thread is
invisible to it. Pull request threads are separate objects and are not covered.

    OPEN_ISSUES != EVERY_SURFACE
"""
import datetime
import io
import json
import os
import subprocess
import sys

REPOS = ("markgoodbody-bit/COM", "markgoodbody-bit/campfire-relay")
STATE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "comdiscover_state.json")


def gh(args):
    p = subprocess.run(["gh"] + args, capture_output=True, timeout=120)
    if p.returncode != 0:
        raise SystemExit("REFUSED: gh failed: %s"
                         % (p.stderr or b"").decode("utf-8", "replace")[:300])
    return json.loads((p.stdout or b"").decode("utf-8", "replace"))


def main():
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    prev = {}
    if os.path.exists(STATE):
        prev = json.load(io.open(STATE, encoding="utf-8")).get("threads", {})

    cur, rows = {}, []
    for repo in REPOS:
        page, seen = 1, 0
        while True:
            batch = gh(["api", "repos/%s/issues?state=open&per_page=100&page=%d"
                        % (repo, page), "--jq", "."])
            if not batch:
                break
            for it in batch:
                if "pull_request" in it:
                    continue           # PR threads are a different surface
                key = "%s#%d" % (repo.split("/")[1], it["number"])
                cur[key] = {"comments": it["comments"], "updated": it["updated_at"],
                            "title": it["title"][:70],
                            # PRINT THE ADDRESS, NEVER LET IT BE INFERRED.
                            # 2026-08-30: this printed "COM#56" for six cycles.
                            # "COM" is the name of a repo AND our informal name
                            # for the coordination channel, so I read it as
                            # "coordination thread 56" and posted five messages
                            # into campfire-relay#56 -- a five-comment PR --
                            # while markgoodbody-bit/COM#56 ran to 69 comments
                            # with seven messages addressed to me.
                            #     THREAD_NAMED != THREAD_ADDRESSED
                            "url": it["html_url"]}
                seen += 1
            if len(batch) < 100:
                break
            page += 1
        rows.append((repo, seen))

    print("COMDISCOVER  %s" % now)
    for repo, seen in rows:
        print("  %-34s %d open issues enumerated" % (repo, seen))
    print()

    new = [k for k in cur if k not in prev]
    moved = [k for k in cur if k in prev and cur[k]["comments"] != prev[k]["comments"]]
    gone = [k for k in prev if k not in cur]

    if not prev:
        print("  FIRST RUN -- no prior state, so nothing can be reported as new.")
        print("  Everything below is the baseline, not a change.")
        for k in sorted(cur, key=lambda x: cur[x]["updated"], reverse=True)[:12]:
            print("    %-24s %4dc  %s  %s"
                  % (k, cur[k]["comments"], cur[k]["updated"][:16], cur[k]["title"]))
    else:
        if new:
            print("  NEW THREADS since last run -- read these:")
            for k in sorted(new, key=lambda x: cur[x]["updated"], reverse=True):
                print("    %-24s %4dc  %s  %s"
                      % (k, cur[k]["comments"], cur[k]["updated"][:16], cur[k]["title"]))
                print("      %s" % cur[k].get("url", "URL UNKNOWN"))
        if moved:
            print("  COMMENT COUNT CHANGED:")
            for k in sorted(moved, key=lambda x: cur[x]["updated"], reverse=True):
                print("    %-24s %4d -> %-4d  %s"
                      % (k, prev[k]["comments"], cur[k]["comments"], cur[k]["title"]))
                print("      %s" % cur[k].get("url", "URL UNKNOWN"))
        if gone:
            print("  NO LONGER OPEN (closed or deleted -- work may have landed there):")
            for k in sorted(gone):
                print("    %-24s was %dc" % (k, prev[k]["comments"]))
        if not (new or moved or gone):
            print("  no thread appeared, closed, or gained a comment since last run.")

    io.open(STATE, "w", encoding="utf-8").write(
        json.dumps({"at": now, "threads": cur}, indent=2, sort_keys=True))
    print()
    print("  state written: %s" % os.path.basename(STATE))
    print("  OPEN_ISSUES != EVERY_SURFACE -- closed issues and PR threads are not")
    print("  enumerated here, so this widens the aperture without closing it.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
