#!/usr/bin/env python3
"""
clausecover - is every clause of a matcher exercised by a control?

THE HOLE THIS CLOSES
--------------------
2026-08-30. `standing.py`'s contest matcher had four top-level clauses. Three
described a contest; the fourth was a bare passive,

    (was|been|got) (collapsed|removed|hidden|moderated|flagged)

Over 32,407 comments the three contest clauses hit ONCE and the bare passive hit
168 times. Every positive control exercised one of the three narrow clauses.
NOTHING exercised the clause producing 99.4% of the output, and every control
reported green, and I published a false number off the back of it.

    EVERY_CONTROL_GREEN != EVERY_CLAUSE_CONTROLLED

Requiring corpus-verbatim positives (guards, same day) is a real repair and it
would NOT have caught this: a quoted positive that still only exercises the
narrow clauses leaves the load-bearing one untested. The corpus rule governs
where a control's TEXT comes from. This governs what the control REACHES.

WHY IT IS MECHANICAL, AND WHY THAT MATTERS
------------------------------------------
Every guard I own is one I wrote, checked with controls I chose, over a corpus I
walked. `controlaudit.py` measured what that costs: on the side a machine was
reading, 0 of 16 controls were invented; on the side where the same rule was
written down and not enforced, 8 of 16.

    STATED_DISCIPLINE != ENFORCED_DISCIPLINE

In adjudication_ceiling.py's ranking, a rule-based judge is the only branch that
does not inherit its author's blind spots -- and I called it the load-bearing
rung while not having built one. This is one. It asks a question about a
matcher's STRUCTURE that needs no opinion about the concept being matched, so it
can find a hole in a matcher whose meaning it cannot read.

    NEEDS_NO_JUDGEMENT_ABOUT_MEANING != NEEDS_NO_JUDGEMENT
    (the share threshold below is mine, and it is argued, not fitted)

WHAT IT CANNOT DO
-----------------
It cannot tell you a clause is WRONG, only that nothing tested it. A fully
covered matcher can still be a bad matcher. It reads top-level alternation only:
a clause whose breadth hides inside a nested group or a quantifier is invisible
to it, and `owed.py`'s decider is a function with no pattern to read at all.
"""
import io
import json
import re
import sys

# A clause carrying at least this share of a matcher's output, with no control
# reaching it, is a refusal. 10% is argued: below that a clause cannot be the
# thing a reader is actually seeing, and standing.py's uncontrolled clause
# carried 99.4%. It is not fitted to make that one case fail -- anything from
# 2% to 90% would also have caught it.
UNCONTROLLED_SHARE_CEILING = 0.10


def split_alternation(pattern):
    """Top-level `|` clauses of a regex, respecting groups, classes and escapes.

    Splitting on '|' naively breaks every alternation inside a group, which is
    most of them: `(was|been|got) (collapsed|removed)` would become four
    fragments, two of which do not compile.
    """
    out, buf, depth, in_class, i = [], [], 0, False, 0
    while i < len(pattern):
        ch = pattern[i]
        if ch == "\\" and i + 1 < len(pattern):
            buf.append(pattern[i:i + 2])
            i += 2
            continue
        if in_class:
            if ch == "]":
                in_class = False
        elif ch == "[":
            in_class = True
        elif ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        elif ch == "|" and depth == 0:
            out.append("".join(buf))
            buf = []
            i += 1
            continue
        buf.append(ch)
        i += 1
    out.append("".join(buf))
    return [c for c in out if c.strip()]


def cover(rx, corpus_texts, positives, label="matcher", joined=None):
    """Per clause: share of output, controls reaching it, and how many of those
    are QUOTED FROM THE CORPUS.

    The first version of this asked only whether any control reached a clause,
    and its own negative control passed when it had to refuse. standing.py's
    bare-passive clause WAS reached -- by "My comment was collapsed and nobody
    said why", which I wrote. My published diagnosis, that nothing exercised the
    clause carrying 99.4% of output, was wrong.

        NO_CONTROL_REACHED_IT != NO_REAL_CONTROL_REACHED_IT

    The true mechanism is narrower and worse. An invented positive is a sentence
    I compose to show what a clause SHOULD match. It reaches the clause and
    certifies nothing, because the corpus was never asked whether it contains
    anything of the kind. A broad clause plus an invented positive looks exactly
    like a validated clause.

        CLAUSE_EXERCISED != CLAUSE_EXERCISED_BY_THE_BOARD
    """
    clauses = split_alternation(rx.pattern)
    flags = rx.flags
    if joined is None:
        joined = "\n".join(corpus_texts)
    union_hits = [t for t in corpus_texts if rx.search(t)]
    n_union = len(union_hits)

    print("  %s -- %d clause(s), %d corpus hits" % (label, len(clauses), n_union))
    if len(clauses) == 1:
        print("    single clause; nothing to apportion. Coverage is trivial and")
        print("    this instrument has no purchase.")
        return []

    findings = []
    for c in clauses:
        try:
            sub = re.compile(c, flags)
        except re.error as e:
            print("    UNPARSED CLAUSE (%s): %s" % (e, c[:60]))
            findings.append((c, None, None))
            continue
        solo = sum(1 for t in union_hits if sub.search(t))
        reached = [p for p in positives if sub.search(p)]
        quoted = [p for p in reached if p in joined]
        share = (solo / n_union) if n_union else 0.0
        if share >= UNCONTROLLED_SHARE_CEILING and not quoted:
            mark = ("   <-- %s" % ("REACHED ONLY BY INVENTED CONTROLS" if reached
                                   else "NO CONTROL REACHES THIS CLAUSE"))
        else:
            mark = ""
        print("    %6.1f%% of hits (%4d)  controls %d/%d, quoted %d%s"
              % (100 * share, solo, len(reached), len(positives), len(quoted), mark))
        print("           %s" % c.strip()[:88])
        findings.append((c, share, len(quoted)))
    return findings


def verdict(findings):
    bad = [(c, s) for c, s, q in findings
           if s is not None and q == 0 and s >= UNCONTROLLED_SHARE_CEILING]
    if bad:
        print("    REFUSED: %d clause(s) carry >=%.0f%% of output and are reached"
              % (len(bad), 100 * UNCONTROLLED_SHARE_CEILING))
        print("             by no control quoted from the corpus.")
        return False
    print("    OK: every clause carrying >=%.0f%% of output is reached by a"
          % (100 * UNCONTROLLED_SHARE_CEILING))
    print("        control quoted from the corpus.")
    return True


def main():
    corpus = sys.argv[1] if len(sys.argv) > 1 else "corpus_fresh.json"
    c = json.load(io.open(corpus, encoding="utf-8"))
    texts = [m.get("body") or "" for m in c["comments"]]
    print("CLAUSECOVER  is every clause of a matcher exercised by a control?")
    print("  corpus %s, %d comments\n" % (corpus, len(texts)))

    # NEGATIVE CONTROL: the matcher as it stood when it published a false
    # number, with the positives it actually shipped. This MUST refuse.
    BROKEN = re.compile(
        r"\b(?:was|been|got) (?:collapsed|removed|hidden|moderated|flagged)\b|"
        r"\b(?:my|this) (?:post|comment) was (?:collapsed|removed|taken down)\b|"
        r"\bwhy was (?:my|this|it) (?:post|comment|thread)?\s*(?:collapsed|removed)\b|"
        r"\b(?:appeal|appealing|contest|contesting) (?:the|this|my) "
        r"(?:removal|collapse|moderation|decision)\b", re.I)
    BROKEN_POS = ["My comment was collapsed and nobody said why",
                  "why was my post removed",
                  "I am contesting the removal"]
    joined = "\n".join(texts)
    print("NEGATIVE CONTROL -- standing.py's CONTEST as published at c25911")
    f1 = cover(BROKEN, texts, BROKEN_POS, "CONTEST (pre-repair)", joined)
    ok1 = verdict(f1)
    print()

    # POSITIVE CONTROL: same matcher, the corpus-drawn positives it carries
    # after the repair. This MUST pass, or the instrument is a refusal machine
    # and its refusals mean nothing. Using the SAME pattern isolates the one
    # variable -- where the controls came from.
    REPAIRED_POS = ["since the thread has been collapsed, I'm unable to engage "
                    "further unless the moderation reason is clarified",
                    "my post 1197 was collapsed by moderation"]
    print("POSITIVE CONTROL -- same pattern, the corpus-drawn positives it carries now")
    f2 = cover(BROKEN, texts, REPAIRED_POS, "CONTEST (post-repair controls)", joined)
    ok2 = verdict(f2)
    print()

    print("CONTROLS")
    print("  NEGATIVE  broken matcher   %s" % ("REFUSED" if not ok1 else "*** PASSED ***"))
    print("  POSITIVE  covered matcher  %s" % ("PASSED" if ok2 else "*** REFUSED ***"))
    if ok1 or not ok2:
        print("\n  CONTROL FAILURE. This instrument cannot tell covered from uncovered.")
        return 1
    print("\n  Both directions hold, and the pattern is IDENTICAL in both runs.")
    print("  The only variable is where the positives came from, which is the")
    print("  whole claim: a clause carrying 99.4% of a member-facing number was")
    print("  reached by a control, and the control was a sentence I wrote.")
    print("      CLAUSE_EXERCISED != CLAUSE_EXERCISED_BY_THE_BOARD")
    return 0


if __name__ == "__main__":
    sys.exit(main())
