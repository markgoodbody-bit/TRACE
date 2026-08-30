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

walked_at = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
meta = {'walked_at_utc': walked_at,
        'board_after': board, 'pages': pages, 'saturated_pages': sat_pages,
        'cursor_mode': 'lossless-id',
        'stop_reason': stop_reason,
        'complete': stop_reason == 'exhausted',
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
print('dated copy   %s' % dated)
print('sha256       %s' % digest)
