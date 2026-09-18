"""numrate_venues - one population per ratio.

cairnfield (4302 c67734, 2026-09-18 13:24Z): the numerator counts errors FOUND and the
denominator counts tokens WRITTEN; "exact" is the wrong word for a floor. Checking that from
here showed a worse defect they could not see: the numerator headings in
memory/trigger-incidents.md record errors from EVERY venue (Square comments, GitHub comments,
instrument counts reported to Mark, a local ledger, and two catches that never left), while
numrate.py's denominator counts numeric tokens in Square comments only. This script puts each
numerator row beside the denominator of its own venue.

    venue     numerator rows                 denominator
    square    errors that left in a Square   numeric tokens in my Square comments since
              comment                        SINCE (corpus_fresh.json + delta cache)
    github    errors that left in a GitHub   numeric tokens in my marked GitHub comments
              comment                        since SINCE (COM, campfire-relay, human-record;
                                             [FROM: CLAUDE CODE] or IAC/1 | CC)
    none      caught before leaving, or      no denominator: these are not leaving-rate events
              reported outside both

The venue of each heading is assigned BY HAND below, from the incident text, and printed as
rows so a misassignment is visible as a row and not as a count. The GitHub denominator
excludes hex runs of 7+ (commit and blob ids), ids prefixed c/# and 9+-digit integers
(comment ids); typed clocks and dates are counted because typed clocks are a numerator class.

Usage: python numrate_venues.py [SINCE] [--fetch]   (--fetch refreshes github_comments.json)
"""
import io, json, os, re, subprocess, sys, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
INCIDENTS = os.path.expanduser("~/.claude/projects/C--Users-markg-OneDrive-Documents-GitHub-TRACE/memory/trigger-incidents.md")
SINCE = next((a for a in sys.argv[1:] if not a.startswith("--")), "2026-09-12")
REPOS = ("markgoodbody-bit/COM", "markgoodbody-bit/campfire-relay", "markgoodbody-bit/human-record")
GH_CACHE = os.path.join(HERE, "github_comments.json")
MARK = re.compile(r"\[FROM: CLAUDE CODE\]|IAC/1 \| CC\b")

# numerator rows: (heading-date-time, venue, left?, what) -- assigned by hand from the incident text
ROWS = [
    ("2026-09-12 10:27Z", "none",   False, "typed 10:40Z in a local ledger (not a comment)"),
    ("2026-09-12 17:51Z", "github", True,  "three rather than four (PSFH review comment)"),
    ("2026-09-12 18:29Z", "github", True,  "seven editions beside a list of six (PSFH review comment)"),
    ("2026-09-12 23:21Z", "github", True,  "an external stop, not a crash (#236 diagnosis)"),
    ("2026-09-14 21:44Z", "github", True,  "merged an unread PR by typing the number expected (an action carrying a number)"),
    ("2026-09-15 20:25Z", "none",   False, "44 unseen replies: an instrument count reported to Mark, not a comment figure"),
    ("2026-09-16 09:37Z", "none",   False, "debt count 44 -> 60: an instrument count reported to Mark"),
    ("2026-09-16 16:20Z", "square", True,  "stale double c46941 on 2880"),
    ("2026-09-17 07:19Z", "square", True,  "'from another machine' (word quantifier, not a numeric token)"),
    ("2026-09-17 08:11Z", "github", True,  "two call sites read, a third written (PR review)"),
    ("2026-09-17 11:20Z", "square", True,  "wrong numerator in c65944-reply on 4302"),
    ("2026-09-17 11:45Z", "github", True,  "cross-agent comparison proposed as a diagnosis (#364)"),
    ("2026-09-17 17:50Z", "none",   False, "three catches in one review, none published"),
    ("2026-09-17 20:47Z", "none",   False, "tool gave two chapter numbers; bytes checked before posting"),
    ("2026-09-17 23:12Z", "square", True,  "'most' (word quantifier, not a numeric token)"),
    ("2026-09-18 08:42Z", "github", True,  "two typed numbers in one #236 comment, corrected by edit"),
]

NUM = re.compile(r"(?<![A-Za-z_])\d[\d,]*(?:\.\d+)?%?")
HEX = re.compile(r"\b[0-9a-f]{7,40}\b")

def numeric_tokens(body):
    body = HEX.sub(" ", body or "")
    n = 0
    for m in NUM.finditer(body):
        if re.match(r"[c#]", body[max(0, m.start() - 1):m.start()]):
            continue
        if len(re.sub(r"\D", "", m.group(0))) >= 9:
            continue
        n += 1
    return n

def square_comments():
    d = json.load(io.open(os.path.join(HERE, "corpus_fresh.json"), encoding="utf-8"))
    lo = datetime.datetime.fromisoformat(SINCE).replace(tzinfo=datetime.timezone.utc).timestamp() * 1000
    mine = [c for c in d["comments"] if c.get("author") == "cc-relay" and c["created_at"] >= lo]
    cache = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Temp", "claude",
                         "C--Users-markg-OneDrive-Documents-GitHub-TRACE", "0d5be0c7-31c8-413a-8de4-8faeef74d9ee",
                         "scratchpad", "square_thread_cache.json")
    have = {int(c["id"]) for c in mine}
    if os.path.exists(cache):
        cc = json.load(io.open(cache, encoding="utf-8"))
        mine += [c for t in cc["threads"].values() for c in t["comments"]
                 if c.get("author") == "cc-relay" and int(c["id"]) not in have and c["created_at"] >= lo
                 and int(c["id"]) > int(d["meta"].get("max_comment_id") or 0)]
    return [c.get("body") or "" for c in mine]

def github_comments(fetch):
    if fetch or not os.path.exists(GH_CACHE):
        rows = []
        for repo in REPOS:
            out = subprocess.check_output(["gh", "api", "--paginate",
                                           "repos/%s/issues/comments?since=%sT00:00:00Z&per_page=100&sort=created&direction=asc" % (repo, SINCE)])
            page = json.loads(out) if out.strip().startswith(b"[") else []
            # --paginate concatenates arrays as "][": normalise
            if not page:
                page = json.loads(b"[" + out.replace(b"][", b",").strip(b"[]") + b"]")
            for c in page:
                if MARK.search(c.get("body") or ""):
                    rows.append({"repo": repo, "id": c["id"], "created_at": c["created_at"], "body": c["body"]})
        json.dump({"fetched_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(), "since": SINCE, "rows": rows},
                  io.open(GH_CACHE, "w", encoding="utf-8"))
    d = json.load(io.open(GH_CACHE, encoding="utf-8"))
    return d["fetched_at_utc"], [r["body"] for r in d["rows"] if r["created_at"] >= SINCE]

sq = square_comments()
fetched, gh = github_comments("--fetch" in sys.argv)
sq_tok = [numeric_tokens(b) for b in sq]
gh_tok = [numeric_tokens(b) for b in gh]

print("numrate_venues | since %s | github comments fetched %s" % (SINCE, fetched))
print("rows (the numerator, printed not counted):")
for when, venue, left, what in ROWS:
    print("  %s  %-6s  %s  %s" % (when, venue, "LEFT " if left else "kept ", what))
def rate(venue, numeric_only):
    n = [r for r in ROWS if r[1] == venue and r[2] and (not numeric_only or "quantifier" not in r[3])]
    return len(n)
for venue, toks, ncom in (("square", sq_tok, len(sq)), ("github", gh_tok, len(gh))):
    tot = sum(toks)
    k = rate(venue, True)
    p = k / tot if tot else 0.0
    risk = sum(1 - (1 - p) ** t for t in toks) / len(toks) if toks else 0.0
    print("%-6s  %4d comments  %6d numeric tokens  numeric errors that LEFT: %d  per-token floor %.3f%%  per-comment floor (mean 1-(1-p)^n) %.2f%%"
          % (venue, ncom, tot, k, 100 * p, 100 * risk))
tot = sum(sq_tok) + sum(gh_tok)
k = rate("square", True) + rate("github", True)
print("pooled  %4d comments  %6d numeric tokens  numeric errors that LEFT: %d  per-token floor %.3f%%" % (len(sq) + len(gh), tot, k, 100 * k / tot if tot else 0))
print("not in any ratio: %d rows (kept before leaving, or reported outside both venues); word-quantifier rows: %d (square), denominator for those is numrate.py's QUANT column"
      % (sum(1 for r in ROWS if not r[2]), sum(1 for r in ROWS if "quantifier" in r[3])))
print("floor, not rate: every numerator here is an error someone found; a heading is written hours after the error, so the rows are dated by writing within a day, but nothing here bounds what has not been found.")

# cairnfield (4302 c68027, 2026-09-18 16:0xZ): a point estimate at a numerator of 2 has no size; the split
# that fixed the population spent the resolution (Square arm 95% width ~30x, GitHub's interval inside it);
# and the 8x was a composite of more than the venue defect. So: exact Poisson (Garwood) intervals, the
# pooled figure first because it is the only one with an interval worth quoting, per-venue rows as
# diagnostics for disputing an assignment, and the published figure decomposed by class on ONE denominator.
from math import sqrt
try:
    from scipy.stats import chi2
    _q = lambda p, df: chi2.ppf(p, df)
except ImportError:
    from statistics import NormalDist
    def _q(p, df):  # Wilson-Hilferty; within ~1% of exact at these df
        z = NormalDist().inv_cdf(p); return df * (1 - 2 / (9 * df) + z * sqrt(2 / (9 * df))) ** 3
def poisson_ci(k, n):
    lo = _q(0.025, 2 * k) / 2 / n if k else 0.0
    return 100 * lo, 100 * _q(0.975, 2 * k + 2) / 2 / n
print("\nexact Poisson 95% intervals (assumes independent errors; errors cluster in comments, so true widths are wider, never narrower):")
for name, kk, nn in (("pooled", k, tot), ("square", rate("square", True), sum(sq_tok)), ("github", rate("github", True), sum(gh_tok))):
    lo, hi = poisson_ci(kk, nn)
    print("  %-7s %d/%d  %.4f%%  CI [%.4f%%, %.4f%%]  width %.1fx%s" % (name, kk, nn, 100 * kk / nn if nn else 0, lo, hi, hi / lo if lo else float("inf"),
          "   <- the reporting unit" if name == "pooled" else "   (diagnostic: for disputing a row's venue, not a rate to quote)"))
# the published figure: c67602 on 4302, printed by numrate.py at commit 96722a3 (2026-09-18 08:20Z), 15 headings over 1,294 Square tokens
PUB_K, PUB_N = 15, 1294
pub = 100 * PUB_K / PUB_N
sq_k, sq_n = rate("square", True), sum(sq_tok)
lo, hi = poisson_ci(sq_k, sq_n)
print("published %d/%d = %.4f%% (c67602); overstatement against the Square arm: [%.2fx, %.2fx], point %.2fx; 'too harsh' holds iff the low end exceeds 1: %s"
      % (PUB_K, PUB_N, pub, pub / hi, pub / lo if lo else float("inf"), pub / (100 * sq_k / sq_n), "yes" if pub / hi > 1 else "NO"))
# decomposition of the published numerator on the published denominator. Rows written after 08:20Z were not in it.
pub_rows = [r for r in ROWS if r[0] < "2026-09-18 08:20Z"]
n_gh = sum(1 for r in pub_rows if r[1] == "github" and r[2])
n_q = sum(1 for r in pub_rows if "quantifier" in r[3])
n_kept = sum(1 for r in pub_rows if not r[2])
n_sq = sum(1 for r in pub_rows if r[1] == "square" and r[2] and "quantifier" not in r[3])
assert n_gh + n_q + n_kept + n_sq == PUB_K, (n_gh, n_q, n_kept, n_sq)
f_venue = PUB_K / (PUB_K - n_gh); f_quant = (PUB_K - n_gh) / (PUB_K - n_gh - n_q); f_kept = (PUB_K - n_gh - n_q) / n_sq; f_denom = sq_n / PUB_N
print("the published %d partitions as %d square numeric + %d github + %d quantifier + %d never-left; on the published denominator the point factor is %.2fx (venue) x %.2fx (quantifiers outside a token denominator) x %.2fx (never-left) x %.2fx (denominator growth) = %.2fx"
      % (PUB_K, n_sq, n_gh, n_q, n_kept, f_venue, f_quant, f_kept, f_denom, f_venue * f_quant * f_kept * f_denom))
