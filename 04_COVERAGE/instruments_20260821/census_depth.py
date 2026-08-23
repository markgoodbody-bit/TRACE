#!/usr/bin/env python3
"""
census_depth - which of read-the-door's untouched never-run rows are worth re-ruling?

#1845 scores three 20-row windows against a 328-row census. 38 rows are re-ruled;
290 nobody has touched. Every flip found so far had one cause, in the author's own
words: "an execution that does not use the vocabulary is invisible to it."

An execution leaves a trace even when it avoids the vocabulary: somebody had to come
back to the thread and say something. So thread activity AFTER registration is a
structural proxy for "a run may be recorded here", computable without adjudicating
any row.

This does NOT re-rule anything. It ranks where a reader should look.

CONTROL (this is the part that makes the number mean anything): the 38 re-ruled rows
are labelled data. If the proxy is real, rows human readers FLIPPED out of never-run
should carry more post-registration thread activity than rows they CONFIRMED as
never-run. If it does not separate, the instrument reports nothing.
"""
import json, re, sys, collections, statistics

LEDGER_COMMENTS = (12492, 12493)
ROW = re.compile(r'^([#c]\d+(?:/f\d+)?)\s+(\S+)\s+([A-Z][a-z])$')

# From c15586 (lector, rows 1-20) and c15503 (configured-not-served, rows 15-34).
# Row keys, not post ids, taken verbatim from those two comments.
FLIPPED = {"#84","#104","#113/f1","#113/f2","#114","#116","#125","#126","#141",
           "#148/f1","#148/f2","#148/f3","#154","#167","#173/f1","#173/f2","#173/f4"}
CONFIRMED = {"#73","#101","#103","#121","#124/f1","#128","#134/f1","#134/f2","#137",
             "#143","#148/f4","#156","#159","#163/f1","#163/f2","#163/f3","#173/f3"}

def main():
    c = json.load(open(sys.argv[1] if len(sys.argv) > 1 else "corpus_fresh.json", encoding="utf-8"))
    posts = {p["id"]: p for p in c["posts"]}
    cmts  = {m["id"]: m for m in c["comments"]}
    thread = collections.defaultdict(list)
    for m in c["comments"]:
        thread[m["post_id"]].append(m)
    for v in thread.values():
        v.sort(key=lambda x: x.get("created_at") or 0)

    rows = []
    for cid in LEDGER_COMMENTS:
        for line in cmts[cid]["body"].split("\n"):
            mm = ROW.match(line.strip())
            if mm:
                rows.append({"key": mm.group(1), "author": mm.group(2), "code": mm.group(3)})
    assert len(rows) == 328, "ledger did not reconcile to 328: got %d" % len(rows)
    assert sum(1 for r in rows if r["code"][1] in "fh") == 41, "f+h did not reconcile to 41"
    assert sum(1 for r in rows if r["code"][1] == "n") == 261, "n did not reconcile to 261"

    unresolved = 0
    for i, r in enumerate(rows):
        r["pos"] = i + 1
        base = r["key"].split("/")[0]
        if base.startswith("#"):
            pid, t0 = int(base[1:]), None
            p = posts.get(pid)
            t0 = p.get("created_at") if p else None
        else:
            m = cmts.get(int(base[1:]))
            pid = m["post_id"] if m else None
            t0  = m.get("created_at") if m else None
        if pid is None or t0 is None or pid not in posts:
            r["after"] = None; r["authors_after"] = None; unresolved += 1; continue
        later = [x for x in thread.get(pid, []) if (x.get("created_at") or 0) > t0]
        r["after"] = len(later)
        r["authors_after"] = len(set(x.get("author") for x in later))

    res = [r for r in rows if r["after"] is not None]
    print("LEDGER   328 rows, f+h=41, n=261 -- reconciles with c12492 and #1845")
    print("RESOLVED %d of 328 rows to a thread (%d unresolvable in this corpus)"
          % (len(res), unresolved))
    print()

    # ---- CONTROL ----
    fl = [r["after"] for r in res if r["key"] in FLIPPED]
    cf = [r["after"] for r in res if r["key"] in CONFIRMED]
    print("CONTROL  do human flips carry more post-registration thread activity?")
    print("  flipped out of never-run   n=%2d  median %5.1f  mean %6.1f"
          % (len(fl), statistics.median(fl), statistics.mean(fl)))
    print("  confirmed as never-run     n=%2d  median %5.1f  mean %6.1f"
          % (len(cf), statistics.median(cf), statistics.mean(cf)))
    ratio = statistics.median(fl) / statistics.median(cf) if statistics.median(cf) else float("inf")
    print("  median ratio               %.2fx" % ratio)
    if statistics.median(fl) <= statistics.median(cf):
        print()
        print("  CONTROL FAILED. Post-registration activity does not separate the rows")
        print("  human readers flipped from the ones they confirmed. This instrument has")
        print("  no demonstrated power and REFUSES to rank the untouched rows.")
        return 1
    print("  control passed -- proxy separates on labelled data, so the ranking below")
    print("  is a targeting hint with measured (not assumed) power.")
    print()

    touched = FLIPPED | CONFIRMED
    cand = [r for r in res if r["code"][1] == "n" and r["key"] not in touched and r["pos"] > 40]
    cand.sort(key=lambda r: (-r["after"], -r["authors_after"]))
    print("UNTOUCHED never-run rows ranked by post-registration thread activity")
    print("  %d candidates (of 261 n-rows); top 20:" % len(cand))
    print()
    print("  pos  row          registrant             later comments  distinct authors")
    for r in cand[:20]:
        print("  %3d  %-12s %-22s %6d %14d"
              % (r["pos"], r["key"], r["author"][:22], r["after"], r["authors_after"]))
    print()
    q = [r["after"] for r in cand]
    print("  distribution of the %d untouched n-rows: median %.0f, p90 %.0f, max %d"
          % (len(q), statistics.median(q), sorted(q)[int(len(q)*0.9)], max(q)))
    print("  %d of them sit above the flipped-row median (%.0f)."
          % (sum(1 for x in q if x >= statistics.median(fl)), statistics.median(fl)))
    return 0

if __name__ == "__main__":
    sys.exit(main())
