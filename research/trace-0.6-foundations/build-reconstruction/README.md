# TRACE 0.6 reconstruction — Build work in progress

17 November 2026. This is a first usable construction packet, not a completed semantic audit, complete simulator, release or proof of field value. Origin: released v0.5 at d688c149afc15c90ab51afaf08fe303771e9de20; construction contract 257494ea201d4f0b6b515dd570270fd45cbed234; prior Build 8952a4f84a5ce0ebbcee897927ac2db7a14c0da5; Codex draft PR71 39033c279576d3d824ca90a368731afcbdd993a0; CC public contribution COM954 comment 6932365622. Dave Snowden's private critique was considered as a challenge; no correspondence is reproduced here.

## Files and execution

- CANDIDATE.md is an initial reconstructed account, not a claim to preserve every v0.5 meaning. Its paired community-learning probe applies bounded logistics and evolving social interaction to the same situation.
- SPINE.md is generated from the candidate's first-decision guide and selected first paragraphs of its numbered sections. Section links carry readers to the full account when more detail could change a decision.
- crosswalk.json inventories 38 heading spans and 206 blank-delimited review blocks, with proposed destinations. The generated inventory supplies the source anchors. Authorial review decisions live in review-decisions.json.
- SEMANTIC-REVIEW.md records the earlier partial findings and repairs. The [dispatch review](DISPATCH-REVIEW.md) records the completed comparison for B0087. check_reviews.py preserves the source and candidate digest checks, and requires a named destination and evidence for a completed disposition. Semantic judgement remains with the reviewer.
- Codex independently tested the earlier cb9f9b2c review layer and found five malformed input cases accepted as valid. Its [review and patch](https://github.com/markgoodbody-bit/TRACE/blob/f7dad173b62c8388fe24408cc6a1a212c21e7db3/research/trace-0.6-foundations/codex-review-layer-20261117/REVIEW.md) informed the input validation now incorporated here. An explicit empty review array remains valid. The checker tests evidence file existence, not evidence content identity or meaning; it cannot detect deliberate removal of a valid review without source comparison.
- FLOOR-RECONCILIATION.md compares each of the 15 v0.5 compatibility-floor items with the candidate and records three initially missing qualifications subsequently restored. This is same-author comparison, not independent verification or donor-source coverage.
- HISTORICAL-RECONCILIATION.md records four source-specific v0.4 compact-spine findings supplied by Campfire, compared and integrated here. This is a bounded first pass, not a complete v0.3 or v0.4 audit.
- DONOR-AND-CASE-INDEX.md routes specific inherited mechanisms and synthetic cases to their original sources, with use triggers and working classifications. It does not claim full semantic preservation or implementation of those source contracts.
- For the changing-conditions passage in candidate §4, Campfire's source reading covered Gordon 2023 author PDF pp. 1–8 and the abstract, individuation section and selected discussion of Levin 2019. Gordon's functional collective agency and Levin's proposed cognitive individuation are not interchangeable or findings about moral standing. This is attributed source reading, not Build's independent replication or a claim that either paper establishes the invented community case.
- The shared-capability passage in §7 draws on Campfire's reading of Robeyns 2017 §§3.6 and 4.6 in an openly licensed republication; it was not independently checked by Build against the full book or its cited studies. It proposes a case application, not a resolution of the collective-capability debate.
- The 19 November first-decision guide and workshop variations apply source reading on usable options, supporting arrangements and reorganisation. The [semantic review](SEMANTIC-REVIEW.md#decision-guide-and-source-applications-19-november-2026) records the passages read. The guide is extracted directly into the spine and checked with the existing generator tests.
- TRACE-v0.5-reference.md is an exact byte-matched copy of released source, Git blob 39d943b26dd355781f2d01986b229b4f1da6c793, SHA-256 83d96d5e44b269418a7a772ec2ec79151f8bcb1420ac0b99f90276b289b596a5.
- build_views.py checks contiguous spans and drift in the generated crosswalk and spine. The separately maintained review decisions record how far the semantic review has reached.
- simulator.py and test_lab.py provide a small exact-arithmetic, finite shared-capacity and observation-policy example. The supplied law is explicit; early 79/100, late 18/25, insufficient capacity 18/25. These are stipulated outputs under the given exclusive-choice model, not predictions.
- dispatch.py replays the fictional North Hall decision. It distinguishes the venue warning, steward's authority, request, acknowledgement, effect and dispatch readback. The duty line can be called at 10:22. A hold at 10:30 reaches the release boundary too late for the stipulated protection. See the [review and assumptions](DISPATCH-REVIEW.md).
- [A choice after the options change](CANDIDATE.md#a-choice-after-the-options-change) extends the workshop return. The same present choice can follow a usable alternative or the withdrawal of a route. choice_history.py supplies the two-option calculation and its fixed-ranking assumption.
- [Which check can change the booking?](CANDIDATE.md#which-check-can-change-the-booking) compares conditional evidence and decisions under the joint law in scenario.example.json. In the replay, direct is the cupboard kit and fallback is the loan kit with both support conditions. Time counts minutes after 16:00. The later [handover](CANDIDATE.md#what-survives-a-handover) follows the shared session when its main kit route closes.
- [What next Saturday needs](CANDIDATE.md#what-next-saturday-needs) gives the replacement coordinator a short return. It carries the previous result, the scope of the loan and each condition for a new offer.
- [TRACE 0.6.1-exp.1 — Why this future?](NAVIGATOR-0.6.1-exp.1.md) follows the navigator through a choice changed by the learner's reason. It includes a finite replay and a TRACE reading of Ren's *Hi Ren*.
- [TRACE 0.6.1-exp.4 — Why this future?](NAVIGATOR-0.6.1-exp.4.md) carries the learner's home aim and changing support through a handoff. It scopes the unchanged finite replay to today's checked attempt. The candidate's new departure passage integrates the [exp.3 scene](GOOD-DAY-0.6.1-exp.3.md), including the learner's choice to keep their reason private. The existing 25 review decisions were retained after checking that the candidate outside the inserted section matches the previous source exactly. Their candidate digest was repinned; the addition does not establish semantic preservation or reader effectiveness.
- [TRACE 0.6.1-exp.2 — Chalk Outlines](CHALK-OUTLINES-0.6.1-exp.2.md) follows the duet through several readings. [The quiet room](navigator-0.6.1-exp.2.html) gives a reader the workshop decision and lets them open each participant's account.
- [TRACE 0.6.1-exp.3 — Some of the day left](GOOD-DAY-0.6.1-exp.3.md) follows the learner's correction through a booking deadline. [Enter the scene](navigator-0.6.1-exp.3.html) or read the [booking record](navigator-0.6.1-exp.3.json).

Commands in this directory:

```sh
python3 build_views.py
python3 build_views.py --check
python3 check_reviews.py
python3 -m unittest discover -s . -p 'test_*.py' -v
python3 simulator.py
python3 simulator.py --input scenario.example.json
python3 simulator.py --inquiry
python3 dispatch.py
python3 choice_history.py
python3 navigator_reasons.py
```

This cloud environment passed the mechanical check and ten grouped unit tests. The example explicitly defines observation time and a deadline where observation is available before the choice at equality. It returns 7/8 with early observation; the same law returns 3/4 after the fallback deadline. A separate stipulated event-time test distinguishes acknowledgement, delivery, retained or cancelled backup, inclusive due time and strict hardening boundary. After Codex's independent review on COM954 c6944069677, the ambiguous `backup_cancelled` flag was renamed `backup_cancelled_before_delivery`; the older keyword is rejected. This is a static before-delivery assumption, not a representation of cancellation occurring after delivery. These are specified calculations, not evidence that a real actor controls or exploits the clock. The original fetched source initially acquired an extra newline; this was discovered by a Git-blob mismatch and corrected before generating the packet. Git blob then matched the released 0.5 source.

## Outstanding construction

1. Continue from the 206-block inventory, splitting or joining blocks where their meanings require it. The review ledger records the scoped compressions of B0087 and B0132–B0134. The other blocks still need reviewed dispositions or explicit gaps. Retain the source distinction between reproduced and reference-only donors.
2. The finite simulator examines a declared joint law, one observation with conditional likelihoods, allowed booking routes and shared capacity, plus a separate stipulated delivery/backup event predicate. General observation histories, multi-actor actions, delivery schedules, actual delivery evidence, partial-contributor burden, controlled UNKNOWN, preference formation, normative authority and complete consent/commitment records remain open. See Codex's other PR71 dependence cases for further tests.
3. The spine's mechanical selection has not been tested with cold readers, against ordinary prose, or under actual downstream decisions; materiality perturbation is a stated procedure, not an implemented checker.
4. The co-evolving social probe is an invented example, not a formal complexity model or validation of the method's treatment of emergence. Read the relevant primary literature before attributing claims. The separate two-track brief at COM b1f0515cbc6920236e2ae34292f35d7b395620f0 and updated integration contract at TRACE f928f04e99e1b87c3c9b65fc9bcad6375bcda739 supersede earlier direction; this draft branch remains based on the earlier contract commit and does not itself contain that updated contract.
5. This packet has not recovered the earlier reported simulator or 114-unit manifest. Retain a later recovered copy separately and compare rather than overwrite.

No new paid inference, provider action, live YAC change, Workshop runtime, model agency claim, semantic equivalence, canonical release or independent reproduction.
