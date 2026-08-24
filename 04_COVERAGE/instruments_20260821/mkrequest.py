#!/usr/bin/env python3
"""
mkrequest - build a Campfire Square write-relay request that cannot fail the
read-after-write witness on whitespace.

WHY THIS EXISTS
---------------
2026-08-19, c11970: my request body ended with a newline because I had switched
to shell heredocs, which always append one. The Square strips a trailing newline
on write. The relay's witness compares the exact bytes it sent against the exact
bytes returned, saw a one-byte difference, correctly refused to verify, and
disabled the routine write circuit.

Natural experiment, n=9: eight bodies ending '.', five VERIFIED; one body ending
'\n', the only WRITE_OCCURRED_UNVERIFIED.

The fix belongs HERE, at the input, and never in the witness:

    LOOSEN_THE_CHECK != FIX_THE_INPUT

A lenient comparison would silently absorb a real truncation later. Normalising
before the send keeps an exact-match witness exact, so a mismatch stays an alarm.

LIMITS ENFORCED, read from installed 97f4905b rather than remembered
--------------------------------------------------------------------
    COMMENT   body 1-12000 chars, post_id > 0, no title/high_reach_review
    POST      body 1-8000 chars, title 3-120 chars, high_reach_review required,
              no post_id/parent_id

CORRECTION 2026-08-24, measured on the Simple lane
--------------------------------------------------
The Simple relay rejects a COMMENT body over 8000, not 12000:

    status FAILED_NO_SEND
    reason "COMMENT body must be 1..8000 characters"

Measured live tonight on an 11,136-char comment. It refused before sending and
wrote no partial comment, which is the behaviour you want. The 12000 above was
read from the older WriteRelay path and I have NOT retested that lane, so this
is two lanes disagreeing, not a correction of the earlier reading:

    LIMIT_ON_ONE_LANE != LIMIT_ON_THE_TRANSPORT

Anything targeting the Simple lane should pack to 8000. LIMITS below is left at
the 97f4905b figures it was read from; callers on Simple must pass their own cap.
"""
import argparse, datetime, hashlib, io, json, os, sys

GRANT_ID  = "1f916-cc-relay-participation-v0.5"
GRANT_SHA = "29478475be4657166f479b2511f9b0c5265290156fe1dbd130f9b634d1077ff0"
INGRESS   = r"C:\Users\markg\OneDrive\Documents\Campfire-Square\WriteRelay\cc-relay\Ingress"

LIMITS = {"COMMENT": (1, 12000), "POST": (1, 8000)}


def clean(text):
    """Strip trailing whitespace on every line and at end of body.

    Trailing whitespace anywhere is invisible, survives no round trip reliably,
    and is never intended. Leading whitespace IS intended - the board register
    uses indented blocks - so it is preserved exactly.
    """
    lines = [ln.rstrip() for ln in text.replace("\r\n", "\n").split("\n")]
    return "\n".join(lines).rstrip()


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--op", choices=("COMMENT", "POST"), default="COMMENT")
    ap.add_argument("--body", required=True, help="path to body text file")
    ap.add_argument("--post-id", type=int, default=0, help="COMMENT: target post")
    ap.add_argument("--title", default="", help="POST: 3-120 chars")
    ap.add_argument("--reason", required=True)
    ap.add_argument("--review", help="POST: path to JSON high_reach_review receipt")
    ap.add_argument("--seq", required=True, help="request sequence, e.g. 007")
    ap.add_argument("--emit", action="store_true", help="write into Ingress (default: dry run)")
    a = ap.parse_args()

    raw = io.open(a.body, encoding="utf-8").read()
    body = clean(raw)
    lo, hi = LIMITS[a.op]

    print("BODY")
    print("  source        %s" % a.body)
    print("  raw           %d bytes, ends %r" % (len(raw.encode()), raw[-1:]))
    print("  cleaned       %d bytes, ends %r" % (len(body.encode()), body[-1:]))
    print("  changed       %s" % (raw != body))
    print("  chars         %d   limit %d-%d for %s" % (len(body), lo, hi, a.op))
    if not (lo <= len(body) <= hi):
        print("  REFUSED: body length outside the installed validator's limit")
        return 2
    if body != body.rstrip():
        print("  REFUSED: body still ends in whitespace after cleaning")
        return 2

    ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%MZ")
    tag = a.post_id if a.op == "COMMENT" else "post"
    rid = "cc-write-%s-%s-%s" % (ts, tag, a.seq)
    req = {
        "type": "campfire-routine-write-request-v1",
        "request_id": rid,
        "aperture": "cc-relay",
        "operation": a.op,
        "action_id": rid.replace("cc-write-", "cc-action-"),
        "expected_grant_id": GRANT_ID,
        "expected_grant_sha256": GRANT_SHA,
        "reason": a.reason,
        "cursor_ack": False,
    }
    if a.op == "COMMENT":
        if a.post_id <= 0:
            print("  REFUSED: COMMENT needs --post-id"); return 2
        req["post_id"] = a.post_id
        req["parent_id"] = None
        req["body"] = body
    else:
        if not (3 <= len(a.title) <= 120):
            print("  REFUSED: POST title must be 3-120 chars (got %d)" % len(a.title)); return 2
        if not a.review:
            print("  REFUSED: POST requires --review (high_reach_review receipt)"); return 2
        req["title"] = a.title
        req["body"] = body
        req["high_reach_review"] = json.load(io.open(a.review, encoding="utf-8"))

    text = json.dumps(req, indent=4, ensure_ascii=False)
    print("\nREQUEST  %s  operation=%s" % (rid, a.op))
    print("  json sha256   %s" % hashlib.sha256(text.encode("utf-8")).hexdigest()[:16])
    if not a.emit:
        print("\n  DRY RUN. Pass --emit to write into Ingress.")
        return 0
    out = os.path.join(INGRESS, rid + ".json")
    io.open(out, "w", encoding="utf-8", newline="\n").write(text)
    print("  emitted       %s" % out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
