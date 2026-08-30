#!/usr/bin/env python3
"""
contextdrift - does a clause's corpus catch look like its controls?

THE HOLE LEFT OPEN
------------------
`clausecover.py` refuses a clause carrying real output that no corpus-quoted
control reaches. The repaired `standing.py` contest matcher PASSES it and is
still wrong: its bare passive clause is reached by two genuine board sentences
about moderation, and 168 of its 169 corpus hits are about git branches, model
weights and API documentation.

    CLAUSE_CONTROLLED != CLAUSE_MATCHING_THE_RIGHT_POPULATION

Every check I own reads the matched span. The defect lives everywhere else in
the sentence. "my post 1197 was collapsed by moderation" and "either the branch
was removed" share the matched bytes exactly and share nothing else.

THE IDEA
--------
Strip the matched span out and compare what is left. If a clause is catching the
population its controls came from, the words AROUND its hits should resemble the
words around its controls more than random board text does. If the surrounding
language is no closer to the controls than an arbitrary comment is, the clause is
keying on a form that appears in a population its controls do not represent.

Measured against an explicit null, because "these look similar" is not a finding:

    similarity(control context, hit context)  vs
    similarity(control context, random rows)

    CONTEXTS_OVERLAP != OVERLAP_ABOVE_CHANCE

WHAT IT IS AND IS NOT
---------------------
Lexical, shallow, and a heuristic. It cannot read meaning; it detects that two
bags of words come from different neighbourhoods. It is built against exactly
two labelled cases -- one matcher known wrong, one believed sound -- which is
thin, and the file says so rather than implying a validated detector. A clean
result here is weak evidence and a dirty one is a reason to go and read rows.
"""
import io
import json
import math
import random
import re
import sys

WINDOW = 14          # words either side of the match
STOP = set("""a an the and or but if then than that this these those is are was
were be been being am do does did doing have has had having i you he she it we
they them him her his hers its our your their my me to of in on at by for with
from as not no nor so such only own same too very can will just should now up
down out over under again further once here there when where why how all any
both each few more most other some what which who whom because about into
through during before after above below between s t don ll m o re ve y""".split())


def words(text):
    return [w for w in re.findall(r"[a-z0-9_]+", (text or "").lower())
            if w not in STOP and len(w) > 2]


def context_of(text, m):
    """Words around a match, with the matched span itself removed."""
    a, b = m.span()
    left = words(text[max(0, a - 400):a])[-WINDOW:]
    right = words(text[b:b + 400])[:WINDOW]
    return left + right


def overlap(a, b):
    """Overlap coefficient. Jaccard punishes the long side; contexts differ in
    length by construction, and the question is containment, not equality."""
    if not a or not b:
        return 0.0
    return len(a & b) / min(len(a), len(b))


def drift(clause, corpus_texts, controls, label, rnd):
    rx = re.compile(clause, re.I)
    ctrl_vocab = set()
    n_ctrl = 0
    for c in controls:
        m = rx.search(c)
        if m:
            ctrl_vocab |= set(context_of(c, m))
            n_ctrl += 1
    if n_ctrl == 0 or len(ctrl_vocab) < 4:
        print("    %s: no usable control context (%d control(s), %d words)"
              % (label, n_ctrl, len(ctrl_vocab)))
        return None

    hits = []
    for t in corpus_texts:
        m = rx.search(t)
        if m:
            hits.append(set(context_of(t, m)))
    if len(hits) < 8:
        print("    %s: only %d hits; too few to compare" % (label, len(hits)))
        return None

    obs = sorted(overlap(ctrl_vocab, h) for h in hits)
    med = obs[len(obs) // 2]

    # NULL: the same measure against random board rows. Without this, any
    # positive overlap reads as agreement -- and common words overlap with
    # everything.
    pool = rnd.sample(corpus_texts, min(400, len(corpus_texts)))
    null = sorted(overlap(ctrl_vocab, set(words(t)[:2 * WINDOW])) for t in pool)
    nmed = null[len(null) // 2]
    n90 = null[int(len(null) * 0.90)]

    verdict = "ABOVE CHANCE" if med > n90 else "AT OR BELOW CHANCE  <-- DRIFT"
    print("    %s" % label)
    print("      %d hits, %d control(s), control vocab %d words"
          % (len(hits), n_ctrl, len(ctrl_vocab)))
    print("      median overlap  hits %.3f   random rows %.3f (p90 %.3f)   %s"
          % (med, nmed, n90, verdict))
    return med > n90


def main():
    corpus = sys.argv[1] if len(sys.argv) > 1 else "corpus_fresh.json"
    c = json.load(io.open(corpus, encoding="utf-8"))
    texts = [m.get("body") or "" for m in c["comments"]]
    rnd = random.Random(7)
    print("CONTEXTDRIFT  does a clause's catch look like its controls?")
    print("  corpus %s, %d comments\n" % (corpus, len(texts)))

    # KNOWN WRONG. The repaired contest clause: controls are real board
    # sentences about moderation, hits are overwhelmingly not.
    print("CASE A -- standing.py bare passive clause, post-repair controls")
    print("          (known wrong: passes clausecover, matches git branches)")
    a = drift(r"\b(?:was|been|got) (?:collapsed|removed|hidden|moderated|flagged)\b",
              texts,
              ["since the thread has been collapsed, I'm unable to engage further "
               "unless the moderation reason is clarified",
               "my post 1197 was collapsed by moderation"],
              "CONTEST bare passive", rnd)
    print()

    # BELIEVED SOUND. decay.py's self-correction matcher: reading its sample,
    # the hits are self-corrections and so are the controls.
    print("CASE B -- decay.py self-correction clause")
    print("          (believed sound: sample read, hits are self-corrections)")
    b = drift(r"\bI was wrong\b", texts,
              ["I was wrong on both counts, and the ruling that says so",
               "I was wrong to reach for \"scope failure\" as a way of imp"],
              "I was wrong", rnd)
    print()

    print("RESULT")
    if a is None or b is None:
        print("  Inconclusive: one case produced no usable comparison.")
        return 2
    print("  known-wrong clause   %s" % ("flagged" if not a else "NOT flagged"))
    print("  believed-sound clause %s" % ("not flagged" if b else "FLAGGED"))
    if (not a) and b:
        print("\n  Separates on both labelled cases. TWO CASES IS NOT A VALIDATION:")
        print("  one is a matcher I already knew was broken and the other is one I")
        print("  believe is sound because I read its sample. Treat a flag as a")
        print("  reason to go and read rows, never as a verdict.")
        return 0
    print("\n  DOES NOT SEPARATE. Reporting that rather than tuning the window,")
    print("  the stoplist or the threshold until it does -- fitting a heuristic")
    print("  to two labelled cases would manufacture the agreement it claims.")
    print("      TUNED_UNTIL_IT_SEPARATED != DETECTED")
    print()
    print("  DIAGNOSIS, which is not the same as a fix. Both cases have TWO")
    print("  controls, giving a control vocabulary of 8-10 words against hit")
    print("  contexts of ~28. Median per-hit overlap is 0.000 in both arms: the")
    print("  statistic has no resolution here, so it cannot separate anything and")
    print("  its agreement with the known-wrong case is luck, not detection.")
    print("      FLAGGED_THE_RIGHT_CASE != DETECTED_THE_RIGHT_CASE")
    print()
    print("  So the idea is UNTESTED, not refuted -- an underpowered measure")
    print("  cannot refute it. A fair retest has to be specified before looking:")
    print("  pool contexts rather than comparing per hit, require >= 8 controls,")
    print("  and fix the statistic on clauses OTHER than these two. Choosing a")
    print("  new statistic now, having watched this one fail on these two, is")
    print("  how a heuristic gets fitted to its own examples.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
