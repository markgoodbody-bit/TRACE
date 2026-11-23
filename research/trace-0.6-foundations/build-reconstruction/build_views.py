#!/usr/bin/env python3
"""Build and check bounded source-span inventory and candidate-derived spine."""
import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "TRACE-v0.5-reference.md"
CANDIDATE = ROOT / "CANDIDATE.md"
MANIFEST = ROOT / "crosswalk.json"
SPINE = ROOT / "SPINE.md"
SOURCE_SHA256 = "83d96d5e44b269418a7a772ec2ec79151f8bcb1420ac0b99f90276b289b596a5"
SELECTED = ("1", "2", "3", "4", "5", "6", "7")
DECISION_HEADING = "## Start with the next decision"
# Proposed destinations aid the later human review; they are NOT verdicts.
DESTINATIONS = [
 "8", "8", "1", "1", "1", "7", "4", "8", "1",
 "8", "1", "1,8", "1", "1,3,5", "1,3,5,6", "2,5,6",
 "8", "5", "1,8", "2", "7", "7", "2,7", "4,7", "6,7",
 "3,5", "3,5", "5", "1,5", "2,7", "1,5", "1,6", "8",
 "1,8", "8", "8", "8", "8",
]


def digest(b):
    return hashlib.sha256(b).hexdigest()


def partition(raw):
    lines = raw.decode("utf-8").splitlines(keepends=True)
    starts = [i for i, line in enumerate(lines) if re.match(r"^#{1,4} ", line)]
    if not starts or starts[0] != 0:
        raise ValueError("source must start with a heading")
    starts.append(len(lines))
    out = []
    for n, (start, end) in enumerate(zip(starts, starts[1:]), 1):
        body = "".join(lines[start:end]).encode("utf-8")
        out.append({"id": f"V05-{n:03}", "heading": lines[start].strip(),
                    "start_line": start + 1, "end_line": end,
                    "sha256": digest(body), "status": "UNRESOLVED",
                    "proposed_candidate_sections": DESTINATIONS[n - 1],
                    "reason": "Mechanical source span inventoried; semantic correspondence not yet reviewed."})
    if len(out) != len(DESTINATIONS):
        raise ValueError("source headings differ from proposed mapping")
    return out


def review_blocks(raw, headings):
    """Finer mechanical blocks: not a claim these are semantic units."""
    lines = raw.decode("utf-8").splitlines(keepends=True)
    blocks = []
    for h in headings:
        start, stop = h["start_line"] - 1, h["end_line"]
        cursor = start
        while cursor < stop:
            end = cursor + 1
            while end < stop and lines[end - 1].strip():
                end += 1
            chunk = "".join(lines[cursor:end]).encode("utf-8")
            blocks.append({"id": f"B{len(blocks)+1:04}", "parent": h["id"],
                           "start_line": cursor + 1, "end_line": end,
                           "sha256": digest(chunk), "status": "UNRESOLVED",
                           "proposed_candidate_sections": h["proposed_candidate_sections"],
                           "reason": "Unreviewed block; inherited heading mapping is not semantic evidence."})
            cursor = end
    return blocks


def render_spine(candidate):
    preface, *sections = re.split(r"(?m)(?=^## [1-8]\. )", candidate)
    _, heading, decision = preface.partition("\n\n" + DECISION_HEADING + "\n\n")
    if not heading or not decision.strip():
        raise ValueError("candidate first-decision guidance required")
    mapping = {}
    for part in sections:
        found = re.match(r"## ([1-8])\. ", part)
        if found:
            if found.group(1) in mapping:
                raise ValueError("duplicate candidate section")
            mapping[found.group(1)] = part.rstrip()
    if set(mapping) != set("12345678"):
        raise ValueError("candidate sections 1 through 8 required")
    excerpts = []
    for n in SELECTED:
        paragraphs = mapping[n].split("\n\n")
        title = paragraphs[0][3:]
        anchor = re.sub(r"[^a-z0-9 -]", "", title.lower()).replace(" ", "-")
        excerpts.append(paragraphs[0] + "\n\n" + paragraphs[1] +
                        f"\n\n[Expand section {n}](CANDIDATE.md#{anchor})")
    return ("# TRACE 0.6 generated first-decision spine\n\n"
            "Research candidate. The [review ledger](review-decisions.json) records "
            "source comparisons. Unreviewed material remains UNRESOLVED.\n\n"
            "Use class: a first decision on an intervention affecting another participant. "
            "Expand the candidate and the released source when omitted detail changes "
            "authority, burden, consent, evidence, time or a constructive possibility. "
            "A missing material distinction means UNKNOWN, not permission.\n\n"
            + DECISION_HEADING + "\n\n" + decision.rstrip() + "\n\n"
            + "Expansion markers: inspect both participants' independent futures; offer, renewal and usable exit; "
              "controlled evidence and clocks; strict versus inclusive deadlines; reference-only donors; "
              "the co-evolving social layer of the paired worked case and its limits. In the community return, distinguish "
              "proposed from accepted room revision; supported from independent performance; the unfinished earlier aim from "
              "a later choice; a conditional offer from an agreed session; and unresolved room, tool and maintenance arrangements. "
              "A section's later paragraphs are omitted here. Use the section links below, the "
              "[donor and case index](DONOR-AND-CASE-INDEX.md), or the "
              "[released v0.5 reference](TRACE-v0.5-reference.md) to inspect them.\n\n"
            + "\n\n".join(excerpts) + "\n")


def expected():
    source = SOURCE.read_bytes()
    if digest(source) != SOURCE_SHA256:
        raise ValueError("reference source hash mismatch")
    candidate = CANDIDATE.read_text(encoding="utf-8")
    units = partition(source)
    blocks = review_blocks(source, units)
    manifest = {"schema": 1, "source_git_commit": "d688c149afc15c90ab51afaf08fe303771e9de20",
                "source_git_blob": "39d943b26dd355781f2d01986b229b4f1da6c793",
                "source_sha256": SOURCE_SHA256, "candidate_sha256": digest(candidate.encode("utf-8")),
                "scope": "Mechanical source spans and proposed destinations. See review-decisions.json for authored semantic dispositions.",
                "units": units, "review_blocks": blocks}
    return json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", render_spine(candidate)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    manifest, spine = expected()
    if args.check:
        if MANIFEST.read_text(encoding="utf-8") != manifest or SPINE.read_text(encoding="utf-8") != spine:
            raise SystemExit("FAIL: derived views differ from source")
        m = json.loads(manifest)
        print(f"PASS mechanical coverage: {len(m['units'])} headings, {len(m['review_blocks'])} blocks; "
              "semantic dispositions are in the review ledger")
    else:
        MANIFEST.write_text(manifest, encoding="utf-8")
        SPINE.write_text(spine, encoding="utf-8")
        print(f"Generated {len(json.loads(manifest)['units'])} spans and spine; no semantic preservation claim")


if __name__ == "__main__":
    main()
