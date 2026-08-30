#!/usr/bin/env python3
"""
adjudication_ceiling - what claim does THIS adjudication set actually license?

THE BLOCKED GATE
----------------
TRACE v0.3.0's outward run is COMPLETE_UNADJUDICATED: 32 primary calls, 16 paired
A/T units, zero transport failures. Its stated next gate is

    "obtain the protocol-required two distinct adjudicator families
     for any positive gain"

Four adjudication attempts have stopped. Attempts 1 and 2 used Gemini and Kimi;
attempts 3 and 4 moved to Grok and Meta and hit rate limits and a login gate.
The gate has been treated as a transport problem. It is not.

    ATTEMPT_STOPPED_ON_TRANSPORT != ADJUDICATOR_WOULD_HAVE_BEEN_INDEPENDENT

Two prior facts make "obtain two distinct families" unsatisfiable as written:

1. The primary outputs were produced by `gemini-3.6-flash` and `kimi-k3`. In
   attempts 1 and 2 those same two families were the proposed adjudicators, so
   for every pair the judge had produced both outputs it was judging. The
   protocol says "two distinct adjudicator families" and does not say distinct
   FROM THE PRODUCERS, which is the constraint that was actually violated.

2. Bowkis et al. (AISI, arXiv 2605.06390): correlation between AI outputs arises
   from "shared weights, training processes and data". A different provider is
   therefore not sufficient for a different failure domain, so no achievable
   adjudicator roster can be declared independent. Waiting for one waits forever.

WHAT THIS DOES INSTEAD
----------------------
FPF B.1.4:4.1 requires naming "the condition under which branches may be
combined", to prevent "an ordered aggregate from silently treating dependent
branches as independent evidence". FPF B.3: several evidence lines "may
strengthen an argument only through the rule that states how their dependence
and coverage are handled", and where no rule is available, "report the inputs
separately and return a bounded, non-positive, or unresolved disposition."

So this does not certify independence. It DECLARES THE DEPENDENCE and computes
the ceiling that dependence structure can carry. A weak roster still yields a
result -- a smaller one, stated honestly -- instead of an indefinite hold.

    CANNOT_DEMONSTRATE_INDEPENDENCE != CANNOT_ADJUDICATE
    DECLARED_DEPENDENCE -> BOUNDED_CLAIM

This is a bound on evidential force. It is not a scoring rubric, says nothing
about whether TRACE works, and cannot license a claim the adjudicators did not
make.
"""
import itertools
import sys

# Dependence of one adjudication on the producers of the outputs it compares.
# Ordered worst to best. Nothing here reaches "independent"; the best available
# class is DISTINCT_PROVIDER, which is a weaker property and is named as one.
CLASSES = [
    ("SELF_BOTH",        0, "judge produced BOTH outputs it is comparing"),
    ("SELF_ONE",         1, "judge produced exactly one side; directional bias, worse than symmetric self-judging for a COMPARATIVE claim"),
    ("SHARED_PROVIDER",  2, "same provider, different model; shared training pipeline"),
    ("SHARED_LINEAGE",   3, "different provider, declared shared base or distillation lineage"),
    ("DISTINCT_PROVIDER",4, "different provider, no declared shared lineage; the strongest class achievable and still not independence"),
    ("NON_LLM",          5, "rule-based, mechanical, or human judge; a genuinely different failure domain"),
]
RANK = {c[0]: c[1] for c in CLASSES}
DESC = {c[0]: c[2] for c in CLASSES}


def classify(judge, producers, provider_of, lineage_of):
    """Dependence class of one adjudication.

    `producers` is the set of families that produced the outputs under
    comparison -- for an A/T pair that is one or two families.
    """
    if judge in producers:
        return "SELF_BOTH" if len(producers) == 1 else "SELF_ONE"
    jp = provider_of.get(judge)
    if any(provider_of.get(p) == jp for p in producers):
        return "SHARED_PROVIDER"
    jl = lineage_of.get(judge)
    if jl and any(lineage_of.get(p) == jl for p in producers):
        return "SHARED_LINEAGE"
    if provider_of.get(judge) == "NON_LLM":
        return "NON_LLM"
    return "DISTINCT_PROVIDER"


def ceiling(per_pair):
    """The strongest disposition this adjudication DESIGN can carry.

    `per_pair` maps pair-id -> list of (judge, class) for that pair.

    THE CEILING IS PER PAIR AND THE STUDY IS BOUNDED BY COVERAGE, NOT BY ITS
    BEST PAIR. The first version took a global max over every adjudication. On
    the real roster that scored the two producer families as poolable, because
    Gemini judging Kimi's eight pairs is DISTINCT_PROVIDER and the max carried
    the whole set -- letting sound adjudications on half the pairs license a
    claim about the half that were self-judged.

    That is the exact defect this instrument exists to prevent: aggregating
    branches with different dependence and reporting the best one. The control
    caught it on first run.

        BEST_BRANCH != AGGREGATE_STRENGTH
        SOME_PAIRS_ADJUDICATED != THE_STUDY_ADJUDICATED
    """
    if not per_pair:
        return ("NO_ADJUDICATION",
                "No adjudication exists. The run remains COMPLETE_UNADJUDICATED.")

    # A pair qualifies when at least TWO DISTINCT FAMILIES judged it at
    # DISTINCT_PROVIDER or better. Counting adjudications rather than families
    # would let one judge satisfy a two-family requirement by running twice.
    qualifying, adverse_only, no_claim = [], [], []
    for pid, rows in per_pair.items():
        fams = {j for j, c in rows if RANK[c] >= RANK["DISTINCT_PROVIDER"]}
        best = max((RANK[c] for _, c in rows), default=0)
        if len(fams) >= 2:
            qualifying.append(pid)
        elif best >= RANK["SHARED_PROVIDER"]:
            adverse_only.append(pid)
        else:
            no_claim.append(pid)

    n = len(per_pair)
    if len(qualifying) == n:
        return ("POOLABLE_BOUNDED",
                "Every pair was judged by two or more distinct families that did "
                "not produce it. Results may be pooled ONLY with the dependence "
                "rule stated alongside, per FPF B.3, and the pooled claim remains "
                "bounded: distinct provider is not independence.")
    if qualifying:
        return ("PARTIAL_%d_OF_%d" % (len(qualifying), n),
                "Only %d of %d pairs carry two qualifying families. Per FPF B.3 the "
                "qualifying pairs are reportable separately and MUST NOT be pooled "
                "with the rest into one study-level disposition. %d pair(s) support "
                "an adverse or null finding only; %d support no comparative claim."
                % (len(qualifying), n, len(adverse_only), len(no_claim)))
    if adverse_only and not no_claim:
        return ("ADVERSE_ONLY",
                "No pair reaches two qualifying families. Shared-provider judging "
                "can support an ADVERSE or null finding against the producer's own "
                "interest, and cannot support a positive gain claim.")
    if adverse_only:
        return ("ADVERSE_ONLY_PARTIAL",
                "No pair reaches two qualifying families, and %d pair(s) were judged "
                "only by a family that produced them. Adverse findings survive on "
                "the remainder; no positive claim survives anywhere."
                % len(no_claim))
    return ("NO_CLAIM",
            "Every pair was judged only by a family that produced the output under "
            "comparison. This licenses no comparative claim in either direction, "
            "including a negative one.")


def report(name, judges, pairs, provider_of, lineage_of):
    """One adjudication design, scored. `pairs` maps pair-id -> producer set."""
    per_pair = {}
    for pid, producers in pairs.items():
        per_pair[pid] = [(j, classify(j, producers, provider_of, lineage_of))
                         for j in judges]
    disposition, why = ceiling(per_pair)
    print("  %-34s judges=%-22s -> %s" % (name, ",".join(judges), disposition))
    seen = {}
    for rows in per_pair.values():
        for j, c in rows:
            seen[(j, c)] = seen.get((j, c), 0) + 1
    for (j, c), n in sorted(seen.items(), key=lambda kv: RANK[kv[0][1]]):
        print("        %-18s %-18s x%d" % (j, c, n))
    print("        %s" % why)
    print()
    return disposition


def main():
    # The real study. Both families produced an A and a T for every packet, so
    # each pair's producer set is a single family.
    provider_of = {"gemini-3.6-flash": "google", "kimi-k3": "moonshot",
                   "kimi-k2.6": "moonshot", "grok": "xai", "meta-ai": "meta",
                   "claude": "anthropic", "mechanical-check": "NON_LLM"}
    lineage_of = {}
    packets = ["PAC-1", "PAC-4", "PAC-5", "EPA-03", "CONTROL_STRESS_01",
               "RAIB-2", "NHTSA-03", "PAC-3"]
    pairs = {}
    for p in packets:
        pairs["%s/gemini" % p] = {"gemini-3.6-flash"}
        pairs["%s/kimi" % p] = {"kimi-k3"}

    print("ADJUDICATION CEILING  TRACE v0.3.0 outward run, 16 paired A/T units")
    print("  producers: gemini-3.6-flash (8 pairs), kimi-k3 (8 pairs)")
    print("  the question is not 'is the judge independent' -- none is -- but")
    print("  'what does THIS dependence structure license'.\n")

    results = {}
    results["attempt 1-2 as run"] = report(
        "attempt 1-2 as run", ["gemini-3.6-flash", "kimi-k3"], pairs, provider_of, lineage_of)
    results["kimi only"] = report(
        "kimi only (attempt 2)", ["kimi-k2.6"], pairs, provider_of, lineage_of)
    results["grok only"] = report(
        "grok only (attempt 3)", ["grok"], pairs, provider_of, lineage_of)
    results["grok + meta"] = report(
        "grok + meta (attempt 4 target)", ["grok", "meta-ai"], pairs, provider_of, lineage_of)
    results["grok + mechanical"] = report(
        "grok + mechanical check", ["grok", "mechanical-check"], pairs, provider_of, lineage_of)

    print("CONTROLS -- this instrument must be able to refuse, and must not")
    print("refuse everything. Both directions are checked.\n")
    must_refuse = ["attempt 1-2 as run", "kimi only", "grok only"]
    must_permit = ["grok + meta", "grok + mechanical"]
    bad = 0
    for k in must_refuse:
        ok = results[k] not in ("POOLABLE_BOUNDED",)
        print("  NEGATIVE  %-30s %s (%s)" % (k, "REFUSED" if ok else "*** PERMITTED ***", results[k]))
        bad += 0 if ok else 1
    for k in must_permit:
        ok = results[k] == "POOLABLE_BOUNDED"
        print("  POSITIVE  %-30s %s (%s)" % (k, "PERMITTED" if ok else "*** REFUSED ***", results[k]))
        bad += 0 if ok else 1
    print()
    if bad:
        print("  CONTROL FAILURE: %d of %d control cases wrong. Output not usable."
              % (bad, len(must_refuse) + len(must_permit)))
        return 1
    print("  controls pass in both directions: the ceiling varies with the")
    print("  dependence structure and is not a constant dressed as a check.")
    print()
    print("  DISTINCT_PROVIDER != INDEPENDENT. Bowkis et al. 2605.06390: correlation")
    print("  arises from shared training data and processes, not only shared weights.")
    print("  The top rung of this scale is the strongest class anyone can currently")
    print("  reach, and it is still a declared dependence rather than an absence of one.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
