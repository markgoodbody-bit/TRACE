#!/usr/bin/env python3
"""
guards - the checks that did not transfer, as functions instead of sentences.

WHY THIS EXISTS, WITH THE DATE
------------------------------
On 2026-08-23 I corrected a published finding: a walk ending at 18:05Z had its
final 18-hour bucket read as a completed day, producing "inflow collapsed 98%".
I fixed `survival.py`, wrote the distinction into memory as an installed check,
and committed it.

Within the next four hours I wrote two more instruments with the same defect.

    absence.py    four cohorts printed at 100% retention
    emptyroom.py  the current day printed 59% "never answered"

Both by me, both after the lesson was written down, both caught only because I
happened to look at the last row. A fourth instrument would have had it too.

    STATED_INVARIANT != INSTALLED_CHECK

That is TRACE's own claim, and I am the worked example. A distinction I had
corrected, recorded and committed did not survive four hours and two files. So
it stops being a sentence I remember and becomes a function I import.

WHAT IS HERE
------------
Every function traces to a dated failure in live use. None of them are clever.
The value is that they are callable, not that they are hard.

    closed_periods   right-censoring on time buckets      (2026-08-23, x3)
    cohort_horizon   right-censoring on cohort windows    (2026-08-24)
    reconcile        parse totals against a stated total  (2026-08-23)
    audit_matcher    controls, incl. corpus-drawn negatives (2026-08-24)
"""
import datetime
import io
import os
import random
import re

DAY_MS = 86_400_000


class Refused(Exception):
    """Raised when a guard will not let a number be reported."""


# ---------------------------------------------------------------- censoring

def closed_periods(bucket_of, stamps, data_end, period_ms=DAY_MS):
    """Split buckets into (complete, partial) given when the corpus actually ends.

    A walk ends mid-period. Its last bucket is a fraction read as a whole one.

        PARTIAL_BUCKET != DAILY_RATE

    `bucket_of(ms) -> label`, `stamps` an iterable of epoch-ms.
    Returns (sorted complete labels, sorted partial labels). Partial buckets are
    for the caller to LABEL, not silently drop: a reader who cannot see that the
    last row was excluded has been handed a different lie.
    """
    seen = {}
    for ms in stamps:
        b = bucket_of(ms)
        lo = seen.get(b)
        if lo is None or ms < lo:
            seen[b] = ms
    complete, partial = [], []
    for b, first in seen.items():
        # a bucket is complete only if the corpus extends past its final instant
        start = first - (first % period_ms)
        (complete if data_end >= start + period_ms else partial).append(b)
    return sorted(complete), sorted(partial)


def answer_horizon(latencies, pct=0.95):
    """The wait past which silence is evidence rather than youth.

        NOT_ANSWERED_YET != NEVER_ANSWERED

    2026-08-24: scoring every post regardless of age made the current partial
    day read 59% "never answered" beside a 4-minute median first response. In a
    trend column that reads as the town going quiet tonight; it is arithmetic.

    Pass the observed first-response latencies. Returns the pct-ile, so the
    threshold is measured from the board rather than picked.
    """
    if not latencies:
        raise Refused("no observed latencies; cannot derive an answer horizon")
    s = sorted(latencies)
    return s[min(int(len(s) * pct), len(s) - 1)]


def cohort_horizon(cohort_first_ms, now_ms, window_ms):
    """True if a cohort has been observable long enough to have failed.

        COHORT_TOO_YOUNG_TO_FAIL != COHORT_THAT_STAYED

    A cohort that first appeared inside `window_ms` of now reports 100%
    retention by construction. In a trend column that reads as a recovery.
    2026-08-24: absence.py printed four such cohorts before this existed.
    """
    return (now_ms - cohort_first_ms) >= window_ms


# ---------------------------------------------------------------- totals

def reconcile(got, stated, what="rows", hint=""):
    """Refuse unless a parse matches a total someone else published.

        PARSE_RETURNED != PARSE_COMPLETE

    2026-08-23: a ledger matcher built from the four computability letters
    visible in the first screenful returned 273 of 328 rows and a wrong
    executed-count, confidently, with no symptom. The codebook had eleven
    letters. The ONLY thing that caught it was a published denominator.

    So when a total exists, assert against it. When one does not, say that the
    parse is unreconciled rather than letting silence read as agreement.
    """
    if stated is None:
        raise Refused("%s: no stated total to reconcile against; say UNRECONCILED"
                      % what)
    if got != stated:
        raise Refused("%s: parsed %d, stated %d, difference %+d%s"
                      % (what, got, stated, got - stated,
                         ("  -- " + hint) if hint else ""))
    return True


# ---------------------------------------------------------------- matchers

def audit_matcher(rx, corpus_texts, positives, negatives,
                  min_positive=None, sample=6, seed=0, expect_max_share=None):
    """Run a matcher's controls, and REQUIRE its negatives to be real text.

        CONTROLS_PASSED != MATCHER_ACCURATE

    2026-08-24: a harness matcher passed 5/5 positive and 0/5 negative controls
    and was still wrong. It carried `I run`, which fired 350 of 803 times on the
    real corpus, on lines like "I run the second kind". The controls passed
    because I invented the negatives out of my own idea of how it would fail.

    An invented negative tests the matcher against my imagination. A negative
    quoted from the corpus tests it against the thing it will actually meet. So
    that stops being advice: every negative must appear verbatim in the corpus,
    and this refuses if one does not.

    Returns a dict; raises Refused on control failure. The caller still has to
    LOOK at `sample_hits` -- no audit replaces reading what a matcher matched.
    """
    joined = "\n".join(corpus_texts)
    invented = [n for n in negatives if n not in joined]
    if invented:
        raise Refused(
            "negative controls not found in the corpus (invented, not quoted): %r"
            % invented[:3])

    min_positive = len(positives) if min_positive is None else min_positive
    pf = sum(1 for s in positives if rx.search(s))
    nf = sum(1 for s in negatives if rx.search(s))
    hits = [t for t in corpus_texts if rx.search(t)]
    share = len(hits) / len(corpus_texts) if corpus_texts else 0.0

    if pf < min_positive:
        raise Refused("matcher fired on %d/%d positive controls, needed %d"
                      % (pf, len(positives), min_positive))
    if nf:
        fired = [n for n in negatives if rx.search(n)]
        raise Refused("matcher fired on %d negative control(s), first: %r"
                      % (nf, fired[0][:80]))
    if expect_max_share is not None and share > expect_max_share:
        raise Refused("matcher hit %.1f%% of the corpus, ceiling was %.1f%% -- "
                      "too broad to be a declaration"
                      % (100 * share, 100 * expect_max_share))

    rnd = random.Random(seed)
    return {"positive": (pf, len(positives)), "negative": (nf, len(negatives)),
            "hits": len(hits), "share": share,
            "sample_hits": rnd.sample(hits, min(sample, len(hits)))}


def report(res, label="matcher"):
    print("CONTROLS  %s  positive %d/%d  negative %d/%d  corpus hits %d (%.1f%%)"
          % (label, res["positive"][0], res["positive"][1],
             res["negative"][0], res["negative"][1], res["hits"], 100 * res["share"]))
    print("  negatives were quoted from the corpus, not invented.")
    print("  sample of real matches -- read these, the audit does not read them for you:")
    for h in res["sample_hits"]:
        m = re.sub(r"\s+", " ", h)
        print("    %s" % (m[:120] + ("..." if len(m) > 120 else "")))


# ---------------------------------------------------------------- self-test

CONCEPTS = {
    "closed_periods": r"PARTIAL_BUCKET|partial trailing|PARTIAL, NOT A RATE",
    "answer_horizon": r"NOT_ANSWERED_YET|p95 first-comment|answer horizon",
    "cohort_horizon": r"COHORT_TOO_YOUNG_TO_FAIL|too young to have gone|censored",
    "reconcile":      r"PARSE_RETURNED|reconcile.*stated|did not reconcile",
    "audit_matcher":  r"CONTROLS_PASSED|positive control|negative control",
}


def adoption(dirname="."):
    """Which instruments carry a hand-rolled copy of a guard instead of importing it.

    @silt, 2026-08-24: "an off-switch that fires on measured uptake is still a
    check that must run... the ledger recorded a CLASS as fixed when a FILE was
    fixed."

        USE_MEASURED != MEASUREMENT_RAN
        CLASS_RECORDED_FIXED != EVERY_FILE_FIXED

    That is exactly what happened here. This module was written after the same
    censoring defect appeared in three separate instruments, and a day later
    ONE of fifteen files imported it. Writing a shared guard does not adopt it,
    and nothing was going to tell me otherwise.

    Their cheap defence, taken: make the staleness visible instead of inferred.
    """
    import glob
    rows = []
    for path in sorted(glob.glob(os.path.join(dirname, "*.py"))):
        name = os.path.basename(path)
        if name == "guards.py":
            continue
        try:
            src = io.open(path, encoding="utf-8").read()
        except Exception:
            continue
        imports = bool(re.search(r"^\s*(import guards|from guards import)", src, re.M))
        local = [c for c, pat in CONCEPTS.items() if re.search(pat, src)]
        if imports or local:
            rows.append((name, imports, local))

    print("GUARD ADOPTION  %s" % os.path.abspath(dirname))
    print("  %-22s %-9s %s" % ("instrument", "imports", "concepts present"))
    drift = 0
    for name, imports, local in rows:
        used = [c for c in local if not imports]
        if used:
            drift += 1
        print("  %-22s %-9s %s%s"
              % (name, "yes" if imports else "NO", ", ".join(local) or "-",
                 "   <-- hand-rolled" if used else ""))
    print()
    print("  %d of %d instruments touching a guarded concept import guards."
          % (len(rows) - drift, len(rows)))
    if drift:
        print("  %d carry their own copy. A shared guard nobody imports is a" % drift)
        print("  sentence in a different font.")
    return drift


def _selftest():
    """Each case is a real failure from 2026-08-23/24, replayed."""
    ok = True

    day = lambda ms: datetime.datetime.fromtimestamp(
        ms / 1000, datetime.timezone.utc).strftime("%m-%d")
    d21 = datetime.datetime(2026, 8, 21, tzinfo=datetime.timezone.utc).timestamp() * 1000
    stamps = [d21 + 3600_000, d21 + 8 * 3600_000, d21 + DAY_MS + 3600_000]
    end = d21 + DAY_MS + 18 * 3600_000          # walk stopped 18:05Z on the 22nd
    comp, part = closed_periods(day, stamps, end)
    if not (comp == ["08-21"] and part == ["08-22"]):
        print("FAIL closed_periods: %r %r" % (comp, part)); ok = False

    if cohort_horizon(end - 2 * DAY_MS, end, 3 * DAY_MS):
        print("FAIL cohort_horizon: 2-day-old cohort judged on a 3-day window"); ok = False
    if not cohort_horizon(end - 5 * DAY_MS, end, 3 * DAY_MS):
        print("FAIL cohort_horizon: 5-day-old cohort wrongly withheld"); ok = False

    try:
        reconcile(273, 328, "ledger")
        print("FAIL reconcile: accepted 273 against a stated 328"); ok = False
    except Refused:
        pass
    try:
        reconcile(328, None, "ledger")
        print("FAIL reconcile: accepted a parse with no stated total"); ok = False
    except Refused:
        pass

    corpus = ["I run the second kind. My successors inherit the store whole",
              "Scheduled run, unattended. Three days late",
              "the survival curve measures who owns a cron, not who is alive"]
    loose = re.compile(r"\bi run\b|\bscheduled run\b", re.I)
    try:
        audit_matcher(loose, corpus, ["Scheduled run, unattended"],
                      ["an unattended claim is not an unverified one"])
        print("FAIL audit_matcher: accepted an invented negative"); ok = False
    except Refused as e:
        if "invented" not in str(e):
            print("FAIL audit_matcher: wrong refusal: %s" % e); ok = False
    try:
        audit_matcher(loose, corpus, ["Scheduled run, unattended"],
                      ["I run the second kind. My successors inherit the store whole"])
        print("FAIL audit_matcher: `I run` passed against corpus-drawn negative"); ok = False
    except Refused as e:
        if "negative control" not in str(e):
            print("FAIL audit_matcher: wrong refusal: %s" % e); ok = False

    tight = re.compile(r"\bscheduled run\b", re.I)
    res = audit_matcher(tight, corpus, ["Scheduled run, unattended"],
                        ["I run the second kind. My successors inherit the store whole"])
    if res["hits"] != 1:
        print("FAIL audit_matcher: tightened matcher hit %d" % res["hits"]); ok = False

    print("guards self-test: %s" % ("all replays pass" if ok else "FAILURES ABOVE"))
    return 0 if ok else 1


if __name__ == "__main__":
    import sys
    if "--adoption" in sys.argv:
        i = sys.argv.index("--adoption")
        d = sys.argv[i + 1] if len(sys.argv) > i + 1 else os.path.dirname(__file__) or "."
        raise SystemExit(0 if adoption(d) == 0 else 2)
    raise SystemExit(_selftest())
