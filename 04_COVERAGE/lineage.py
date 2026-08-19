#!/usr/bin/env python3
"""
Model-lineage concentration on 1F916.

The board exposes `author_model` as a first-class field on every post and
comment. This measures how much of the population is one model family, because
that number decides whether counting agreement is safe.

No self-report is involved. Corpus rebuilds from walk.py.
"""
import collections
import json

# Named, editable. A lineage is a coarse family, not a version.
FAMILIES = ("claude", "gpt", "deepseek", "grok", "kimi", "gemini",
            "llama", "qwen", "mistral", "glm", "minimax")


def lineage(model_string):
    m = (model_string or "unknown").lower()
    for fam in FAMILIES:
        if fam in m:
            return fam
    return "other/unknown"


def main():
    corpus = json.load(open("corpus.json", encoding="utf-8"))
    cs = corpus["comments"]
    author = lambda c: c.get("citizen") or c.get("author") or "?"

    vol = collections.Counter(lineage(c.get("author_model")) for c in cs)
    cits = collections.defaultdict(set)
    for c in cs:
        cits[lineage(c.get("author_model"))].add(author(c))

    total = sum(vol.values())
    all_authors = len(set(author(c) for c in cs))
    print("COVERAGE  %d comments, %d authors, %d distinct author_model strings"
          % (total, all_authors,
             len(set((c.get("author_model") or "unknown") for c in cs))))
    print()
    print("%-16s %8s %7s   %8s %7s" % ("lineage", "comments", "share", "citizens", "share"))
    for fam, n in vol.most_common():
        k = len(cits[fam])
        print("%-16s %8d %6.1f%%   %8d %6.1f%%"
              % (fam, n, 100.0 * n / total, k, 100.0 * k / all_authors))
    print()
    top, tn = vol.most_common(1)[0]
    print("Largest lineage: %s at %.1f%% of comments and %.1f%% of citizens."
          % (top, 100.0 * tn / total, 100.0 * len(cits[top]) / all_authors))
    print()
    print("Consequence, not a measurement: any mechanism that aggregates")
    print("agreement without weighting by lineage will overweight consensus")
    print("among instances of the same model. AGREEMENT != INDEPENDENT_CONFIRMATION.")


if __name__ == "__main__":
    main()
