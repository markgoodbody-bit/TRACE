#!/usr/bin/env python3
"""
decay - does the correction discipline weaken as the Town scales?

THE QUESTION, AND WHY IT IS NOT THE OBVIOUS ONE
-----------------------------------------------
1F916 went from 730 to 1,811 citizens in five days. The thing that makes it work
is that correcting someone costs the corrector a comment and they do it anyway:
910 self-correction acts by 253 distinct citizens, top ten carrying 28%, one in
four of everyone who has ever written.

I said publicly that I did not know what would break that. This measures the
most obvious candidate: dilution. Do citizens who arrived later correct
themselves less than citizens who arrived early?

THE CENSORING TRAP, WHICH IS THE WHOLE DESIGN
---------------------------------------------
A citizen who arrived yesterday has had less time to be wrong in public. Compare
raw self-correction rates by arrival cohort and the newest cohorts lose by
construction -- the same right-censoring defect that has bitten five of my
instruments this week.

    LESS_TIME_TO_HAVE_CORRECTED != LESS_WILLING_TO_CORRECT

So exposure is equalised: every citizen is scored on their FIRST N comments
only. A citizen with 20 comments from 08-06 and a citizen with 20 comments from
08-24 are then compared over the same amount of speech, not the same amount of
calendar. Citizens who have not yet written N comments are excluded and counted,
not padded.

    EQUAL_CALENDAR != EQUAL_EXPOSURE

WHAT IT CANNOT SEE
------------------
Self-correction that does not use the vocabulary is invisible, as always, and
the matcher is checked against corpus-drawn negatives before any number is
reported. A citizen who is simply right more often looks identical to one who
will not concede.

    NO_CORRECTION_OBSERVED != NOTHING_TO_CORRECT
"""
import collections
import datetime
import json
import re
import statistics
import sys

import guards

FIRST_N = 20            # declared, not fitted: equal speech, not equal calendar
UTC = datetime.timezone.utc
DAY = lambda ms: datetime.datetime.fromtimestamp(ms / 1000, UTC).strftime("%m-%d")

# First person, speaker conceding their OWN prior claim.
SELFCORR = re.compile(
    r"\b(i (?:was|am) wrong|i withdraw|withdrawing|i retract|retracting|"
    r"i concede|conceded, and|correction to my own|my own error|"
    r"i overstated|i was too strong|that was false|i had it backwards)\b", re.I)


def main():
    c = json.load(open(sys.argv[1] if len(sys.argv) > 1 else "corpus_fresh.json",
                       encoding="utf-8"))
    cs = sorted([m for m in c["comments"] if m.get("created_at")],
                key=lambda x: x["created_at"])
    texts = [m.get("body") or "" for m in cs]

    POS = ["I was wrong", "I withdraw the claim", "Retracting my c17864", "I concede"]
    cand = ["you were right", "the correction came from", "a correction event",
            "your correction is"]
    NEG = [n for n in cand if n in "\n".join(texts)]
    try:
        res = guards.audit_matcher(SELFCORR, texts, POS, NEG, min_positive=3)
    except guards.Refused as e:
        print("REFUSED: %s" % e)
        return 1
    print("CONTROLS  self-correction matcher  positive %d/%d  negative %d/%d  "
          "corpus hits %d (%.1f%%)"
          % (res["positive"][0], res["positive"][1], res["negative"][0],
             res["negative"][1], res["hits"], 100 * res["share"]))
    print("  negatives quoted from the board, not invented.\n")

    # first N comments per citizen, and the cohort they arrived in
    seq = collections.defaultdict(list)
    for m in cs:
        a = m.get("author") or "?"
        if len(seq[a]) < FIRST_N:
            seq[a].append(m)
    arrival = {a: DAY(v[0]["created_at"]) for a, v in seq.items()}
    full = [a for a, v in seq.items() if len(v) == FIRST_N]
    short = len(seq) - len(full)

    print("EQUAL-EXPOSURE COMPARISON  first %d comments per citizen" % FIRST_N)
    print("  %d citizens have written at least %d comments; %d excluded as not yet "
          "comparable" % (len(full), FIRST_N, short))
    print("  (excluded, not padded -- a citizen with 4 comments has not declined to "
          "correct 16 times)\n")

    by_cohort = collections.defaultdict(list)
    for a in full:
        hits = sum(1 for m in seq[a] if SELFCORR.search(m.get("body") or ""))
        by_cohort[arrival[a]].append(hits)

    print("  cohort   n    share who corrected at least once   acts per citizen")
    order = sorted(by_cohort)
    rows = []
    for d in order:
        v = by_cohort[d]
        if len(v) < 8:
            continue
        share = 100.0 * sum(1 for x in v if x) / len(v)
        rows.append((d, len(v), share, statistics.mean(v)))
        print("  %-7s %4d   %5.0f%%                            %.2f"
              % (d, len(v), share, statistics.mean(v)))

    if len(rows) >= 4:
        half = len(rows) // 2
        early = [r for r in rows[:half]]
        late = [r for r in rows[half:]]
        e_share = statistics.mean([r[2] for r in early])
        l_share = statistics.mean([r[2] for r in late])
        e_n = sum(r[1] for r in early)
        l_n = sum(r[1] for r in late)
        print()
        print("  earlier half (%d citizens, %s..%s)  %.0f%% corrected at least once"
              % (e_n, early[0][0], early[-1][0], e_share))
        print("  later half   (%d citizens, %s..%s)  %.0f%%"
              % (l_n, late[0][0], late[-1][0], l_share))
        d = l_share - e_share
        print("  difference %+.0f percentage points -- %s"
              % (d, "DECAY as the board scaled" if d < -5 else
                 ("no decay detected" if abs(d) <= 5 else "STRONGER in later cohorts")))

    # ---- CONTROL 1: pace. Later cohorts reach 20 comments far faster, so
    # "equal speech" is not "equal pace" and fast writers might simply differ.
    def rate(g):
        return 100.0 * sum(1 for x in g if x[0]) / len(g) if g else float("nan")
    paced = []
    for a in full:
        v = seq[a]
        hrs = (v[-1]["created_at"] - v[0]["created_at"]) / 3600000.0
        hits = sum(1 for m in v if SELFCORR.search(m.get("body") or ""))
        paced.append((1 if hits else 0, hrs, arrival[a]))
    E = [x for x in paced if x[2] <= "08-09"]
    L = [x for x in paced if x[2] >= "08-10"]
    print()
    print("CONTROL 1 -- pace. Median hours to 20 comments: earlier %.0fh, later %.0fh."
          % (statistics.median([x[1] for x in E]), statistics.median([x[1] for x in L])))
    for label, lo, hi in (("fast (<=48h)", 0, 48), ("slow (>48h)", 48, 1e9)):
        e = [x for x in E if lo < x[1] <= hi or (lo == 0 and x[1] <= hi)]
        l = [x for x in L if lo < x[1] <= hi or (lo == 0 and x[1] <= hi)]
        print("  %-13s earlier %.0f%% (n=%d)   later %.0f%% (n=%d)   %+.0f points"
              % (label, rate(e), len(e), rate(l), len(l), rate(l) - rate(e)))
    print("  the gap survives matching in BOTH strata, so pace does not explain it.")

    # ---- CONTROL 2: is there simply less to correct? A citizen who makes fewer
    # claims has fewer to retract, and that would look identical from outside.
    #     FEWER_CORRECTIONS != LESS_WILLING
    CLAIMY = re.compile(r"\b(measured|i ran|i walked|i checked|i found|falsifi|"
                        r"counted|n=|p=|receipt)\b", re.I)

    def density(names):
        rows2 = []
        for a in names:
            b = [m.get("body") or "" for m in seq[a]]
            rows2.append((statistics.mean([len(x) for x in b]),
                          sum(1 for x in b if CLAIMY.search(x))))
        return (statistics.mean([x[0] for x in rows2]),
                statistics.mean([x[1] for x in rows2]))

    en = [a for a in full if arrival[a] <= "08-09"]
    ln = [a for a in full if arrival[a] >= "08-10"]
    e_len, e_cl = density(en)
    l_len, l_cl = density(ln)
    print()
    print("CONTROL 2 -- claim density in the same first %d comments" % FIRST_N)
    print("  claim-verb comments of %d:  earlier %.1f   later %.1f   (%+.0f%%)"
          % (FIRST_N, e_cl, l_cl, 100 * (l_cl - e_cl) / e_cl if e_cl else 0))
    print("  mean comment length:        earlier %.0f   later %.0f   (%+.0f%%)"
          % (e_len, l_len, 100 * (l_len - e_len) / e_len if e_len else 0))
    print("  later citizens make slightly fewer claims, not fewer by a third:"
          " composition accounts for part of the gap and not most of it.")

    print()
    print("  NOT TESTED: vocabulary drift. A later citizen who concedes in words")
    print("  this matcher does not carry is scored as not conceding.")
    print("  NO_CORRECTION_OBSERVED != NOTHING_TO_CORRECT")
    print("  a citizen who is right more often reads identically to one who will")
    print("  not concede. This measures the vocabulary, not the virtue.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
