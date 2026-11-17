#!/usr/bin/env python3
"""Check review anchors, not the semantic correctness of the reviews."""
import json
from pathlib import Path
import build_views

ROOT = Path(__file__).resolve().parent


def validate(data, source, candidate, evidence_exists):
    if data.get('schema') != 1:
        raise ValueError('unsupported review schema')
    if data.get('source_sha256') != build_views.digest(source):
        raise ValueError('stale source review')
    if data.get('candidate_sha256') != build_views.digest(candidate):
        raise ValueError('stale candidate review: reassess before repinning')
    blocks = build_views.review_blocks(source, build_views.partition(source))
    by_id = {block['id']: block for block in blocks}
    seen = set()
    for review in data.get('reviews', []):
        block_id = review.get('block_id')
        if block_id not in by_id or block_id in seen:
            raise ValueError('unknown or duplicate review block')
        seen.add(block_id)
        if review.get('block_sha256') != by_id[block_id]['sha256']:
            raise ValueError('stale block review')
        if review.get('status') != 'PARTIAL':
            raise ValueError('only partial reviews supported')
        if not all(isinstance(review.get(k), str) and review[k].strip()
                   for k in ('finding', 'remaining', 'reviewer', 'evidence')):
            raise ValueError('partial review requires finding, gap, reviewer and evidence')
        evidence = review['evidence']
        if Path(evidence).name != evidence or not evidence_exists(evidence):
            raise ValueError('evidence must be a present local file')
    return len(seen), len(blocks)


if __name__ == '__main__':
    result = validate(json.loads((ROOT / 'review-decisions.json').read_text()),
                      build_views.SOURCE.read_bytes(), build_views.CANDIDATE.read_bytes(),
                      lambda name: (ROOT / name).is_file())
    print(f'{result[0]} partial reviews anchored; {result[1]} source blocks remain unresolved overall')
