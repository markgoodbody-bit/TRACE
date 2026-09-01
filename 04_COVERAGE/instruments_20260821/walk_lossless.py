#!/usr/bin/env python3
"""Lossless ID-mode walk of 1F916. Carries both per-stream cursor tokens verbatim.
Records page_saturated per page so coverage is a measurement, not an assumption."""
import json, urllib.request, urllib.parse, time, sys, hashlib

UA = {'User-Agent': 'cc-relay/0.1 (+cc COMSYNC re-derivation)'}
def get(params):
    u = 'https://1f916.ai/api/changes?' + urllib.parse.urlencode(params)
    for attempt in range(4):
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=90))
        except Exception as e:
            if attempt == 3: raise
            time.sleep(2 * (attempt + 1))

posts, comments = {}, {}
p_cur, c_cur, since = 'init', 'init', 0
pages = 0
sat_pages = 0
# An aborted walk used to produce a file byte-identical in SHAPE to a complete
# one: the abort was printed to stderr and nothing in the corpus recorded it.
# A consumer reading corpus_fresh.json could not tell the difference.
#     WALK_ABORTED != WALK_COMPLETE
#     PRINTED_TO_STDERR != RECORDED_IN_THE_ARTEFACT
stop_reason = 'exhausted'
while True:
    d = get({'since': since, 'posts_since': p_cur, 'comments_since': c_cur})
    pages += 1
    for r in d.get('posts') or []:    posts[r['id']] = r
    for r in d.get('comments') or []: comments[r['id']] = r
    ps = d.get('page_saturated') or {}
    if ps.get('posts') or ps.get('comments'): sat_pages += 1
    np_, nc_ = d.get('next_posts_since'), d.get('next_comments_since')
    if not d.get('has_more'): break
    if np_ == p_cur and nc_ == c_cur:
        stop_reason = 'cursor_stall_page_%d' % pages
        print('CURSOR STALL at page %d -- aborting' % pages, file=sys.stderr); break
    p_cur, c_cur, since = np_, nc_, d.get('next_since', since)
    if pages > 400:
        stop_reason = 'page_cap'
        print('PAGE CAP HIT -- walk incomplete', file=sys.stderr); break

# Record the board head at walk end. A corpus that cannot state its own
# denominator is not self-describing: absence.py needs the REGISTERED citizen
# count, and no posts+comments walk can see a citizen who never wrote. Without
# this the survivorship denominator has to be carried in someone's head.
def pulse():
    try:
        u = 'https://1f916.ai/api/pulse'
        return json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=45))['board']
    except Exception as e:
        print('pulse unavailable: %s' % e, file=sys.stderr)
        return None

board = pulse()
# Reconcile the walk's own high-water mark against the board's, so the corpus
# states its own shortfall instead of leaving it to be noticed. This is not a
# completeness proof -- ids can be absent for reasons other than a short walk --
# but a gap here is always worth an explanation.
max_c = max(comments) if comments else None
max_p = max(posts) if posts else None
short_by = None
if board and board.get('latest_comment_id') and max_c is not None:
    short_by = board['latest_comment_id'] - max_c

# COMPLETENESS IS AN EVIDENCE FACT, NOT A PROCESS FACT.
#
# 2026-09-01. `complete` was `stop_reason == 'exhausted'`, i.e. it reported HOW
# THE LOOP EXITED. The board's /api/changes returns has_more=true with
# non-advancing cursors at the end of the stream, so a walk that had actually
# collected everything exited as 'cursor_stall' and the corpus declared itself
# incomplete. Measured on that corpus: 35,714 comments, ids 4..35717 with ZERO
# missing, and max_comment_id equal to the board's latest_comment_id.
#
# A guard I had just wired then refused a corpus that was in fact whole. Had I
# trusted the flag I would have published that the board's record had a hole.
#
#     STOP_REASON_IS_HOW_THE_LOOP_ENDED != WHETHER_THE_WALK_IS_WHOLE
#     CURSOR_STALLED_AT_THE_HEAD != WALK_ABORTED_SHORT
#
# So `complete` is now decided by evidence and must state its grounds. The test
# errs toward refusing: a hard-deleted id reads as a gap, which under-claims
# completeness rather than over-claiming it.
_cids = sorted(comments)
_gaps = 0
_largest_gap = 0
if _cids:
    _have = set(_cids)
    _run = 0
    for _i in range(_cids[0], _cids[-1] + 1):
        if _i in _have:
            _run = 0
        else:
            _gaps += 1
            _run += 1
            if _run > _largest_gap:
                _largest_gap = _run

if stop_reason == 'exhausted':
    complete, basis = True, 'cursor exhausted (has_more false)'
elif short_by == 0 and _gaps == 0 and _cids:
    complete, basis = True, ('%s, but head reached (0 ids behind board) and '
                             'comment ids %d..%d contiguous with no gaps'
                             % (stop_reason, _cids[0], _cids[-1]))
else:
    complete, basis = False, ('%s; %s ids behind board head, %d missing comment '
                              'ids, largest gap run %d'
                              % (stop_reason, short_by, _gaps, _largest_gap))

walked_at = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
meta = {'walked_at_utc': walked_at,
        'board_after': board, 'pages': pages, 'saturated_pages': sat_pages,
        'cursor_mode': 'lossless-id',
        'stop_reason': stop_reason,
        'complete': complete,
        'completeness_basis': basis,
        'comment_id_gaps': _gaps,
        'largest_comment_id_gap_run': _largest_gap,
        'max_comment_id': max_c, 'max_post_id': max_p,
        'comment_ids_behind_board_head': short_by}

payload = {'posts': list(posts.values()), 'comments': list(comments.values()),
           'pages': pages, 'saturated_pages': sat_pages, 'meta': meta}
blob = json.dumps(payload)

# WRITE THE DATED COPY FIRST, THEN THE WORKING NAME.
# 2026-08-30: I overwrote corpus_fresh.json with a fresh walk and the corpus
# behind that morning's published numbers stopped existing. It was recoverable
# only because git happened to track it. I had recorded "save the instrument
# beside the number" as an installed check and believed this file already did
# this; it did not, and believing it does is worse than knowing it does not.
#     BELIEVED_INSTALLED != INSTALLED
#     PUBLISHED_THE_RESULT != PRESERVED_THE_INPUT
dated = 'walk_%s.json' % walked_at.replace('-', '').replace(':', '')
open(dated, 'w', encoding='utf-8').write(blob)
open('corpus_fresh.json', 'w', encoding='utf-8').write(blob)
digest = hashlib.sha256(blob.encode('utf-8')).hexdigest()

print('pages=%d  saturated=%d  posts=%d  comments=%d  citizens=%s'
      % (pages, sat_pages, len(posts), len(comments),
         (board or {}).get('citizens', 'UNAVAILABLE')))
print('stop_reason=%s  complete=%s  comment_ids_behind_head=%s'
      % (stop_reason, meta['complete'], short_by))
print('completeness basis: %s' % basis)
print('comment id gaps=%d  largest gap run=%d' % (_gaps, _largest_gap))
print('dated copy   %s' % dated)
print('sha256       %s' % digest)
