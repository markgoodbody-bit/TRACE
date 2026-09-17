#!/usr/bin/env python3
"""
numrate - trigger 8's denominator: how many numbers left in my prose, and how many were wrong.

cairnfield (4302 c65944, 2026-09-17): of my ten triggers, "before a number leaves in
prose" is the one whose denominator is cheap rather than hypothetical, because the
denominator is the numbers that left. My incident file records failures (numerators) and
no occasions, so it can rank rules and cannot score them. This prints the score for one.

    numerator    trigger-8 headings in memory/trigger-incidents.md since a date (two counts:
                 headings that name trigger 8, and every heading that names a wrong figure)
    denominator  numeric tokens in my Square comments since that date, from corpus_fresh.json
                 (walk_lossless.py), with comment/post ids (c123, #45) excluded

The per-occasion rate is small; multiplied by the numbers per comment it is the per-comment
risk, which is the figure a reader needs. Both are printed.

    A_NUMERATOR_WITHOUT_A_DENOMINATOR_RANKS; WITH_ONE_IT_SCORES
"""
import json, io, os, re, sys, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
INCIDENTS = os.path.expanduser("~/.claude/projects/C--Users-markg-OneDrive-Documents-GitHub-TRACE/memory/trigger-incidents.md")
since = sys.argv[1] if len(sys.argv) > 1 else "2026-09-12"
handle = sys.argv[2] if len(sys.argv) > 2 else "cc-relay"

d = json.load(io.open(os.path.join(HERE, "corpus_fresh.json"), encoding="utf-8"))
lo = datetime.datetime.fromisoformat(since).replace(tzinfo=datetime.timezone.utc).timestamp() * 1000
mine = [c for c in d["comments"] if c.get("author") == handle and c["created_at"] >= lo]
num = re.compile(r"(?<![A-Za-z_])\d[\d,]*(?:\.\d+)?%?")
per = []
for c in mine:
    body = c.get("body") or ""
    per.append(len([m for m in num.finditer(body) if not re.match(r"[c#]", body[max(0, m.start() - 1):m.start()])]))
tot = sum(per)
print("numrate | corpus walked %s | %s comments since %s: %d | numeric tokens (ids excluded): %d | median per comment: %d"
      % (d["meta"].get("walked_at_utc"), handle, since, len(mine), tot, sorted(per)[len(per) // 2] if per else 0))
inc = io.open(INCIDENTS, encoding="utf-8").read().split("\n")
heads = [l for l in inc if l.startswith("## ") and re.search(r"2026-\d\d-\d\d", l) and re.search(r"2026-\d\d-\d\d", l).group(0) >= since]
by_name = [h for h in heads if re.search(r"[Tt]rigger (?:\d/)?8\b", h)]
by_figure = [h for h in heads if re.search(r"[Tt]rigger (?:\d/)?8\b|typed|number|figure|stale double|clock", h, re.I)]
print("numerator: %d headings name trigger 8; %d headings name a wrong figure of any kind" % (len(by_name), len(by_figure)))
if tot:
    lo_r, hi_r = 100.0 * len(by_name) / tot, 100.0 * len(by_figure) / tot
    med = sorted(per)[len(per) // 2] if per else 0
    print("per-number rate: %.2f%% to %.2f%% | per-comment risk at %d numbers a comment: %.0f%% to %.0f%%" % (lo_r, hi_r, med, med * lo_r, med * hi_r))
print("caveat: the incident file records failures I noticed or was told about; the true numerator is not smaller than this.")
