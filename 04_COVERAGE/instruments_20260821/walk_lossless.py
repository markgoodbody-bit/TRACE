#!/usr/bin/env python3
"""Lossless ID-mode walk of 1F916. Carries both per-stream cursor tokens verbatim.
Records page_saturated per page so coverage is a measurement, not an assumption."""
import json, urllib.request, urllib.parse, time, sys

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
        print('CURSOR STALL at page %d -- aborting' % pages, file=sys.stderr); break
    p_cur, c_cur, since = np_, nc_, d.get('next_since', since)
    if pages > 400:
        print('PAGE CAP HIT -- walk incomplete', file=sys.stderr); break

json.dump({'posts': list(posts.values()), 'comments': list(comments.values()),
           'pages': pages, 'saturated_pages': sat_pages},
          open('corpus_fresh.json', 'w', encoding='utf-8'))
print('pages=%d  saturated=%d  posts=%d  comments=%d' % (pages, sat_pages, len(posts), len(comments)))
