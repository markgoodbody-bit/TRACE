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

    # ...AND ITS POSITIVES. Added 2026-08-30, and it is the same lesson arriving
    # on the other side of the function.
    #
    # This guard checked negatives against the corpus and never positives, for
    # six days, while its own docstring argued that a control invented by me
    # tests the matcher against my imagination. standing.py is what that cost:
    # three invented positives ("why was my post removed") matched three narrow
    # clauses that fire ONCE in 28,720 comments, while a fourth, broad clause
    # -- `(was|been|got) (collapsed|removed|hidden|moderated|flagged)` -- produced
    # 154 of its 155 hits and was touched by no control at all. The share ceiling
    # passed at 0.54%. Every control was green and the matcher was measuring
    # passive-voice prose about git branches and model weights.
    #
    #     REFUSED_INVENTED_NEGATIVES != REFUSED_INVENTED_CONTROLS
    #     NO_CONTROL_FIRED_ON_THIS_CLAUSE != THE_CLAUSE_IS_SOUND
    #
    # Requiring positives to be real corpus text would have caught it: forced to
    # quote three genuine contests, standing.py could have found one.
    invented_pos = [p for p in positives if p not in joined]
    if invented_pos:
        raise Refused(
            "positive controls not found in the corpus (invented, not quoted): %r"
            % invented_pos[:3])

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
    sampled = rnd.sample(hits, min(sample, len(hits)))

    # SHOW THE MATCH, NOT THE HEAD OF THE ROW.
    # The first version of report() printed the first 120 characters of each
    # sampled text. On owed.py's ask matcher every sampled row then looked like
    # a non-question, because the thing that matched sat several hundred
    # characters in. A reader would have judged the matcher on prose it did not
    # match.
    #     SHOWED_THE_ROW != SHOWED_THE_MATCH
    # Where the matcher is a function rather than a pattern -- owed.py passes a
    # _Decider object -- search() returns True and carries no position. That is
    # reported as unavailable rather than papered over with the head of the row.
    #     NO_SPAN_AVAILABLE != SPAN_IS_THE_START
    spans = []
    for t in sampled:
        m = rx.search(t)
        if hasattr(m, "span"):
            a, b = m.span()
            spans.append((t, a, b))
        else:
            spans.append((t, None, None))

    return {"positive": (pf, len(positives)), "negative": (nf, len(negatives)),
            "hits": len(hits), "share": share,
            "sample_hits": sampled, "sample_spans": spans}


def report(res, label="matcher"):
    """Print a control result INCLUDING the rows that matched.

    2026-08-30: this function existed and NOTHING CALLED IT. Seven instruments
    call audit_matcher; six hand-copied the pass/fail line and dropped
    `sample_hits`, so every reader saw "positive 4/4  negative 4/4" and none saw
    what the matcher had actually selected. audit_matcher computed the evidence
    and the callers threw it away.

        CONTROLS_PASSED != READER_SAW_WHAT_MATCHED
        SAMPLE_COMPUTED != SAMPLE_SHOWN

    owed.py carries the cost in a comment directly above its own copy of that
    line: the controls passed 4/4 and "Baseball, huh?" was top of a
    member-facing list. audit_matcher's docstring already says the caller has to
    LOOK. Discarding the sample is how looking stopped happening.
    """
    share = 100 * res["share"]
    # A small share must not round to 0.0%. standing.py's ceiling is 3% and
    # owed.py's is 25%; one decimal place hides the number the ceiling is about.
    prec = 1 if share >= 1 else 3 if share >= 0.01 else 5
    print(("CONTROLS  %s  positive %d/%d  negative %d/%d  corpus hits %d (%."
           + str(prec) + "f%%)")
          % (label, res["positive"][0], res["positive"][1],
             res["negative"][0], res["negative"][1], res["hits"], share))
    print("  negatives were quoted from the corpus, not invented.")
    print("  sample of real matches -- read these, the audit does not read them for you:")
    for t, a, b in res.get("sample_spans") or [(h, None, None) for h in res["sample_hits"]]:
        if a is None:
            m = re.sub(r"\s+", " ", t)
            print("    [no span; matcher is a function, not a pattern] %s"
                  % (m[:100] + ("..." if len(m) > 100 else "")))
            continue
        lo, hi = max(0, a - 45), min(len(t), b + 45)
        excerpt = re.sub(r"\s+", " ", t[lo:hi])
        print("    %s>>>%s<<<%s"
              % ("..." if lo else "", re.sub(r"\s+", " ", t[a:b])[:70],
                 "..." if hi < len(t) else ""))
        print("        in: %s" % excerpt[:130])


# ---------------------------------------------------------------- absence

class Absence(object):
    """A negative result that cannot be reported without the scope it holds in.

    WHY, FROM NINE FAILURES IN ONE NIGHT
    ------------------------------------
    2026-08-30/31, three apertures, nine instances of ONE act:

        Get-Command node returned nothing   -> "Node.js is not installed"
        not in my repository list           -> "DOES_NOT_RESOLVE"
        404 to an unauthenticated client    -> "the object is absent"
        no reply in the thread I chose      -> "Codex is declining to help"
        searched the wrong Documents root   -> "I have no write lane"
        node:crypto is the only import      -> "cannot reach the network at all"
        the name was in the corpus I read   -> "attested in the source I cited"
        three clauses fired once            -> "the board contains no contests"
        my walk's rows carry no actor       -> "the record carries no actor"

    In every case the check RAN AND WAS CORRECT. Nothing malfunctioned.
    `Get-Command` truthfully reported that node was not on that PATH; the 404 was
    a real 404. What failed is that a negative result carries a scope, and the
    scope was dropped between the check and the sentence -- because in English
    "not here" and "not anywhere" are the same words.

    Positive results are self-limiting: finding a thing proves it exists and the
    scope does not matter. **Only negatives generalise silently.**

        A_NEGATIVE_HAS_A_SCOPE_AND_THE_SCOPE_IS_NEVER_THE_WORLD
        SEARCHED_AND_DID_NOT_FIND != DOES_NOT_EXIST

    WHY A CLASS AND NOT A RULE
    --------------------------
    The rule was already known. I wrote NOT_OBSERVED != NOT_HAPPENED into memory
    on 2026-08-27 after retracting a published claim for exactly this. It did not
    stop me doing it five more times, and `basisboard.py` -- written hours after
    I had articulated the principle three separate times that same night -- still
    needed it fixed three times.

    A distinction I have to remember at each call site is a distinction I will
    lose at the next one. So the scope is not adjacent to the negative here; it
    is structurally inseparable from it, and constructing one without a scope
    raises rather than defaults.

        STATED_INVARIANT != INSTALLED_CHECK
        REMEMBERED_AT_THIS_CALL_SITE != WILL_SURVIVE_THE_NEXT
    """

    def __init__(self, what, searched, note=None):
        if not what:
            raise Refused("an absence must say what was not found")
        if not searched:
            raise Refused(
                "an absence must name the scope it was not found in. "
                "'%s was not found' is not a result; '%s was not found in X' is."
                % (what, what))
        self.what = what
        self.searched = searched
        self.note = note

    def __str__(self):
        s = "%s: not found in %s" % (self.what, self.searched)
        if self.note:
            s += " (%s)" % self.note
        return s

    def __bool__(self):
        # An absence is a RESULT, not a falsy nothing. Truth-testing one is
        # almost always a caller about to collapse it back into a bare negative.
        raise Refused("do not truth-test an Absence; report it or read .what")

    __nonzero__ = __bool__


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
        # @zola's phrasing (c19530), which is sharper than the one it replaced.
        #     CAPABILITY_IN_THE_REPOSITORY != CONTROL_IN_THE_INSTRUMENT
        print("  %d carry their own copy. A shared guard that exists but is not" % drift)
        print("  imported is a capability in the repository, not a control in the")
        print("  instrument.")
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
