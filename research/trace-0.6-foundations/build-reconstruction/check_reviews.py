#!/usr/bin/env python3
"""Check review anchors, not the semantic correctness of the reviews."""
import json
from pathlib import Path
import build_views

ROOT = Path(__file__).resolve().parent


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('duplicate JSON field: ' + key)
        result[key] = value
    return result


def validate(data, source, candidate, evidence_exists):
    if not isinstance(data, dict):
        raise ValueError('review document must be an object')
    if type(data.get('schema')) is not int or data['schema'] != 1:
        raise ValueError('unsupported review schema')
    if 'reviews' not in data or not isinstance(data['reviews'], list):
        raise ValueError('reviews must be an explicit array; an empty array means zero reviews')
    if data.get('source_sha256') != build_views.digest(source):
        raise ValueError('stale source review')
    if data.get('candidate_sha256') != build_views.digest(candidate):
        raise ValueError('stale candidate review: reassess before repinning')
    blocks = build_views.review_blocks(source, build_views.partition(source))
    by_id = {block['id']: block for block in blocks}
    seen = set()
    for review in data['reviews']:
        if not isinstance(review, dict):
            raise ValueError('each review must be an object')
        block_id = review.get('block_id')
        if not isinstance(block_id, str) or block_id not in by_id or block_id in seen:
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
    result = validate(json.loads((ROOT / 'review-decisions.json').read_text(encoding='utf-8'),
                                 object_pairs_hook=unique_object),
                      build_views.SOURCE.read_bytes(), build_views.CANDIDATE.read_bytes(),
                      lambda name: (ROOT / name).is_file())
    print(f'{result[0]} partial reviews anchored; {result[1]} source blocks remain unresolved overall')
