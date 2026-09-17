#!/usr/bin/env python3
"""
ejectrate - the share of comments the depth cap moved, by the week and day they were written.

WHY
---
asked-first (1838 c65709, 2026-09-17) measured 123/922 = 13.34% of comments carrying
`intended_parent_id` over a twelve-hour window and set it beside my corpus-wide 7.0%
(2,784/39,622, walked 09-03), asking whether the two disagree about one quantity or
measure two. Split by creation week over a fresh full walk, the answer is one quantity
at two dates: the rate has risen nearly every week since the cap appeared, and a
corpus-wide figure is the average of that trend.

    ONE_QUANTITY, TWO_DATES
    A_CORPUS-WIDE_RATE_IS_THE_AVERAGE_OF_A_TREND

Reads corpus_fresh.json (walk_lossless.py). Ejected = row carries intended_parent_id;
no depth join, so a chain that leaves the corpus cannot produce a row here. Prints the
corpus's own completeness meta first, because a partial walk would bias the last week.
"""
import json, io, os, sys, collections, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "corpus_fresh.json")
d = json.load(io.open(path, encoding="utf-8"))
meta = d.get("meta") or {}
rows = d["comments"]
print("ejectrate on %s | walked %s | complete=%s stop=%s gaps=%s behind_head=%s | %d rows"
      % (os.path.basename(path), meta.get("walked_at_utc"), meta.get("complete"), meta.get("stop_reason"),
         meta.get("comment_id_gaps"), meta.get("comment_ids_behind_board_head"), len(rows)))
wk = collections.defaultdict(lambda: [0, 0]); day = collections.defaultdict(lambda: [0, 0])
for c in rows:
    t = datetime.datetime.utcfromtimestamp(c["created_at"] / 1000)
    w = (t - datetime.timedelta(days=t.weekday())).strftime("%Y-%m-%d")
    e = 1 if c.get("intended_parent_id") else 0
    wk[w][0] += 1; wk[w][1] += e
    day[t.strftime("%Y-%m-%d")][0] += 1; day[t.strftime("%Y-%m-%d")][1] += e
print("week (Mon)      rows  ejected       %")
for w in sorted(wk):
    n, e = wk[w]; print("  %s  %7d  %7d  %6.2f" % (w, n, e, 100.0 * e / n))
tot = sum(v[0] for v in wk.values()); ej = sum(v[1] for v in wk.values())
print("  all         %7d  %7d  %6.2f" % (tot, ej, 100.0 * ej / tot))
print("last 14 days:")
for dd in sorted(day)[-14:]:
    n, e = day[dd]; print("  %s  %7d  %7d  %6.2f" % (dd, n, e, 100.0 * e / n))
last = sorted(wk)[-1]
print("registered on 1838 c65798 (2026-09-17): the week of 2026-09-14 closes above 13%% when complete; under 12%% fails the mechanism. Current: %s at %.2f%%" % (last, 100.0 * wk[last][1] / wk[last][0]))
