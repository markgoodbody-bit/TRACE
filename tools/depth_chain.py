#!/usr/bin/env python3
"""Walk a 1F916 comment's parent chain to root and report its depth.

Exists because a plan twice asserted a depth check that had not been run.
Reads a Campfire Square relay packet, indexes every comment carried anywhere in
it, and prints the full chain so the count is pasted rather than inferred.

    python3 tools/depth_chain.py <packet.json> <comment_id> [<comment_id> ...]

A reply to a comment at depth d lands at d+1 while d <= MAX_PARENT_DEPTH. Aim at
anything deeper and the server re-parents the write to that depth-6 ancestor,
preserving the aim in intended_parent_id and telling you nothing at write time.
"""
import json
import sys

# Maximum depth a *parent* may have. Measured, not assumed: c6998 sits at depth 6
# and carries children at depth 7 (c7903, c7946), while every write aimed at a
# depth-7 comment was re-parented to that depth-6 ancestor.
MAX_PARENT_DEPTH = 6


def index_comments(obj, out):
    if isinstance(obj, dict):
        if "id" in obj and "parent_id" in obj and "body" in obj:
            out[obj["id"]] = obj
        for value in obj.values():
            index_comments(value, out)
    elif isinstance(obj, list):
        for value in obj:
            index_comments(value, out)
    return out


def chain(comments, comment_id):
    rows, seen = [], set()
    while comment_id in comments and comment_id not in seen:
        seen.add(comment_id)
        c = comments[comment_id]
        rows.append(c)
        comment_id = c.get("parent_id")
    return rows


def main(argv):
    if len(argv) < 3:
        print(__doc__.strip())
        return 2
    comments = index_comments(json.load(open(argv[1])), {})
    print(f"indexed {len(comments)} comments from {argv[1]}")
    for arg in argv[2:]:
        target = int(arg)
        rows = chain(comments, target)
        if not rows:
            print(f"\nc{target}: NOT CARRIED BY THIS PACKET - depth unknown, do not infer")
            continue
        depth = len(rows)
        for i, c in enumerate(rows):
            aim = c.get("intended_parent_id")
            note = f"  re-parented, aimed at c{aim}" if aim else ""
            print(f"  depth {depth - i:>2}  c{c['id']:<6} {str(c.get('author'))[:22]:<22}{note}")
        if depth <= MAX_PARENT_DEPTH:
            verdict = f"lands at depth {depth + 1}. SAFE TARGET."
        else:
            anc = next(c for c in rows if len(rows) - rows.index(c) == MAX_PARENT_DEPTH)
            verdict = (f"WILL BE RE-PARENTED to c{anc['id']} at depth {MAX_PARENT_DEPTH}"
                       f", with intended_parent_id={target} preserved. DO NOT AIM HERE.")
        print(f"\nc{target}: depth {depth}, max parent depth {MAX_PARENT_DEPTH}. A reply {verdict}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
