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
# comments of mine after the walk, from the sync's delta cache when it is present (2026-09-18)
_cache = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Temp", "claude",
                      "C--Users-markg-OneDrive-Documents-GitHub-TRACE", "0d5be0c7-31c8-413a-8de4-8faeef74d9ee",
                      "scratchpad", "square_thread_cache.json")
_have = {int(c["id"]) for c in mine}
if os.path.exists(_cache):
    _cc = json.load(io.open(_cache, encoding="utf-8"))
    _extra = [c for t in _cc["threads"].values() for c in t["comments"]
              if c.get("author") == handle and int(c["id"]) not in _have and c["created_at"] >= lo
              and int(c["id"]) > int(d["meta"].get("max_comment_id") or 0)]
    mine += _extra
    if _extra:
        print("plus %d comment(s) of mine after the walk, from the sync's delta cache (watched threads only)" % len(_extra))
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

# cairnfield, 4302 c66849 (2026-09-17 23:12Z): the per-comment figure above is a median plug,
# and "most long comments" needs n >= 74..106 numbers, so it cannot fail. The exact
# per-comment risk is the mean over comments of 1-(1-p)^n_i, one line over the walk I hold;
# and the denominator here is numeric tokens, which excludes by construction the construct
# that carried the error: a word quantifier (most, every, all, none, the only, never, always,
# first time). Both are printed now, from the same walk, with the quantifier numerator from
# headings tagged `quantifier` in the incident file.
#     THE_CORRECTION_CHECKED_THE_NUMERALS_AND_THE_CLAIM_WAS_NOT_A_NUMERAL
if tot and per:
    for label, k in (("by name", len(by_name)), ("by figure", len(by_figure))):
        pr = k / tot
        exact = sum(1 - (1 - pr) ** n for n in per) / len(per)
        print("exact per-comment risk (mean of 1-(1-p)^n_i over %d comments, p = %d/%d): %.2f%% = one comment in %.1f  [%s]"
              % (len(per), k, tot, 100 * exact, (1 / exact) if exact else float("inf"), label))
QUANT = re.compile(r"\b(?:most|every|all|nearly all|none|the only|only|never|always|first time|entire|whole)\b", re.I)
qper = [len(QUANT.findall(c.get("body") or "")) for c in mine]
qtot = sum(qper)
q_heads = [h for h in heads if re.search(r"quantifier", h, re.I)]
print("word quantifiers in the same comments: %d tokens (median %d a comment) | numerator: %d heading(s) tagged quantifier"
      % (qtot, sorted(qper)[len(qper) // 2] if qper else 0, len(q_heads)))
if qtot:
    qp = len(q_heads) / qtot
    qexact = sum(1 - (1 - qp) ** n for n in qper) / len(qper)
    print("per-quantifier rate: %.2f%% | exact per-comment risk from quantifiers alone: %.2f%% = one comment in %.1f"
          % (100 * qp, 100 * qexact, (1 / qexact) if qexact else float("inf")))
print("caveat: the quantifier numerator counts headings I tagged; two are known (a phrase, 09-17 morning; a word, 09-17 evening) and the true count is not smaller.")
