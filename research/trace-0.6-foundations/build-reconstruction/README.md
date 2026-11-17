# TRACE 0.6 reconstruction — Build work in progress

17 November 2026. This is a first usable construction packet, not a completed semantic audit, complete simulator, release or proof of field value. Origin: released v0.5 at d688c149afc15c90ab51afaf08fe303771e9de20; construction contract 257494ea201d4f0b6b515dd570270fd45cbed234; prior Build 8952a4f84a5ce0ebbcee897927ac2db7a14c0da5; Codex draft PR71 39033c279576d3d824ca90a368731afcbdd993a0; CC public contribution COM954 comment 6932365622. Dave Snowden's private critique was considered as a challenge; no correspondence is reproduced here.

## Files and execution

- CANDIDATE.md is an initial reconstructed account, not a claim to preserve every v0.5 meaning.
- SPINE.md is generated directly from selected first paragraphs and carries explicit omissions and an expansion condition. It is not a separate source of authority.
- crosswalk.json inventories 38 exact heading-to-next-heading source spans and 206 blank-delimited review blocks, proposes candidate-section destinations and marks **every one UNRESOLVED**. These mechanical blocks are not the earlier unrecovered reported 114 semantic units. Explicit mapping is a review prompt, not a reviewed correspondence.
- SEMANTIC-REVIEW.md compares selected high-value source blocks against the candidate and names omissions and repairs; it does not complete the crosswalk.
- TRACE-v0.5-reference.md is an exact byte-matched copy of released source, Git blob 39d943b26dd355781f2d01986b229b4f1da6c793, SHA-256 83d96d5e44b269418a7a772ec2ec79151f8bcb1420ac0b99f90276b289b596a5.
- build_views.py generates the crosswalk and spine and verifies source hash and generated outputs; it checks contiguous spans and drift, not preservation of meaning. Hand-reviewed dispositions are not yet supported; regeneration replaces this WIP manifest.
- simulator.py and test_lab.py provide a small exact-arithmetic, finite shared-capacity and observation-policy example. The supplied law is explicit; early 79/100, late 18/25, insufficient capacity 18/25. These are stipulated outputs under the given exclusive-choice model, not predictions.

Commands in this directory:

```sh
python3 build_views.py
python3 build_views.py --check
python3 -m unittest discover -s . -p 'test_lab.py' -v
python3 simulator.py
python3 simulator.py --input scenario.example.json
```

This cloud environment passed the mechanical check and eight grouped unit tests. The example explicitly defines observation time and a deadline where observation is available before the choice at equality. It returns 7/8 with early observation; the same law returns 3/4 after the fallback deadline. These are specified calculations, not evidence that a real actor controls or exploits the clock. The original fetched source initially acquired an extra newline; this was discovered by a Git-blob mismatch and corrected before generating the packet. Git blob then matched the released 0.5 source.

## Outstanding construction

1. Audit the 206 mechanical blocks, splitting or joining as necessary into meaning-bearing units, against the candidate, assigning reviewed dispositions and explicit gaps. Retain the source distinction between reproduced and reference-only donors. Selected high-value cases are in SEMANTIC-REVIEW.md; they are not a blanket reviewed disposition.
2. The finite simulator does not yet model general observations/histories, arbitrary multi-actor actions, full delivery deadlines, actual delivery events, partial-contributor burden, controlled UNKNOWN in evidence, preference formation, valid normative authority, or complete consent/commitment records. It examines a declared joint law with one observation/action deadline and shared capacity, plus a few separate predicates. Codex's other PR71 dependence and delivery cases remain unimplemented here. Never use these passes as proof of complete acceptance.
3. The spine's mechanical selection has not been tested with cold readers, against ordinary prose, or under actual downstream decisions; materiality perturbation is a stated procedure, not an implemented checker.
4. The co-evolving social probe is an invented example, not a formal complexity model or validation of the method's treatment of emergence. Read the relevant primary literature before attributing claims.
5. This packet has not recovered the earlier reported simulator or 114-unit manifest. Retain a later recovered copy separately and compare rather than overwrite.

No new paid inference, provider action, live YAC change, Workshop runtime, model agency claim, semantic equivalence, canonical release or independent reproduction.
