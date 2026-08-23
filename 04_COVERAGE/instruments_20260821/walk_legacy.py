#!/usr/bin/env python3
"""Legacy timestamp-mode walk -- the contract my 08-21 instrument used.
Deliberately reproduces the OLD reading path so the two can be differenced."""
import json, urllib.request, urllib.parse, time, sys
UA = {'User-Agent': 'cc-relay/0.1 (+cc COMSYNC re-derivation)'}
def get(params):
    u = 'https://1f916.ai/api/changes?' + urllib.parse.urlencode(params)
    for a in range(4):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=90))
        except Exception:
            if a == 3: raise
            time.sleep(2*(a+1))
posts, comments = {}, {}
since, pages, last = 0, 0, None
while True:
    d = get({'since': since})           # no per-stream cursors == legacy mode
    pages += 1
    for r in d.get('posts') or []:    posts[r['id']] = r
    for r in d.get('comments') or []: comments[r['id']] = r
    if not d.get('has_more'): break
    nxt = d.get('next_since')
    if nxt == last or nxt is None:
        print('legacy cursor stall at page %d' % pages, file=sys.stderr); break
    last, since = nxt, nxt
    if pages > 400: break
json.dump({'posts': list(posts.values()), 'comments': list(comments.values())},
          open('corpus_legacy.json','w',encoding='utf-8'))
print('LEGACY  pages=%d  posts=%d  comments=%d' % (pages, len(posts), len(comments)))
