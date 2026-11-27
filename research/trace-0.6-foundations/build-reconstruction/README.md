# TRACE 0.6 working edition · mathematical companion

Begin with the [short spine](SPINE.md) or the [full working manuscript](CANDIDATE.md). The finite calculations here answer different questions about a declared case.

| Question | Calculation |
| --- | --- |
| Which choices fit this person’s recorded options and decisions? | [Possible choices and the supporting rows](#possible-next-choices) |
| Was a past option actually usable? | [Conditional answers for disputed entries](#when-one-past-menu-is-incomplete) |
| Which offers remain possible if the person’s priorities changed? | [Two periods with an uncertain boundary](#when-the-order-may-have-changed) |
| How late can an answer arrive and still meet the plan’s deadlines? | [Work back from the required events](#how-late-can-the-answer-arrive) |
| Would an observation arrive in time to change a booking? | [Workshop inquiry](simulator.py) and [dispatch replay](DISPATCH-REVIEW.md) |
| Would a single session meet the aim, or does access have to continue? | [One session or both?](#one-session-or-both) |

The construction began on 17 November with the [released 0.5 source](TRACE-v0.5-reference.md), the [integration brief](../INTEGRATION-20261117.md), the prior Build work at `8952a4f8`, [Codex’s reproduction](https://github.com/markgoodbody-bit/TRACE/pull/71) and [CC’s challenge](https://github.com/markgoodbody-bit/COM/issues/954#issuecomment-6932365622). The [ledger](review-decisions.json) tracks comparisons with the earlier source.

## Possible next choices

**Input.** One chooser, a finite history $H=((M_t,c_t))$ and the next usable menu $F$. Each $M_t$ contains exactly the options available at that choice, and $c_t$ is its observed winner. Each option counted in a recorded choice must fit the limits the chooser stated for that occasion. Carry a limit with the chooser's permission. Their reason can stay private. The model assumes the chooser selects the highest option under one fixed strict ordering. A changed aim or a different chooser calls for a separate comparison.

Build a directed graph on all option IDs. Add an edge from each winner to each alternative it beat. An option absent at the time contributes no comparison.

$$
E=\bigcup_t\{(c_t,y):y\in M_t\setminus\{c_t\}\}.
$$

A directed cycle refutes the assumptions for this history. Otherwise the exact set of possible next choices is

$$
P(H,F)=\{x\in F:\nexists y\in F\setminus\{x\},\;y\leadsto_E x\}.
$$

**Proof.** A ranking that explains the history is a topological ordering of the graph. Making $x$ first in $F$ adds edges from $x$ to the other members of $F$. These edges create a cycle exactly when one of those members already reaches $x$. Paths can run through options absent from $F$.

**Algorithm.** In topological order, mark a node if any predecessor is in $F$ or is already marked. Return the unmarked members of $F$ in input order. With $L$ supplied option occurrences, $V$ distinct options and $|E|$ distinct edges, expected time is $O(L+V+|E|)$ and auxiliary space is $O(V+|E|)$ for bounded-size IDs and hash tables.

Feed this request to `python3 choice_history.py --stdin`.

```json
{"history":[{"usable":["a","b"],"chosen":"a"},{"usable":["b","c"],"chosen":"b"}],"usable_next":["a","c","d"]}
```

```json
{"status":"compatible","possible_next_choices":["a","d"]}
```

The path through the unavailable `b` still rules out `c`. The history leaves `d` open. An empty history leaves every next option possible. An empty next menu yields an empty set when the history is compatible. A contradiction among comparisons returns a closed cycle of option IDs. Actual consent and future aims require their own evidence. [Implementation](choice_history.py) · [Worked choice after an option is restored](CANDIDATE.md#a-choice-after-the-options-change)

### Check one choice

Suppose a handover rules out brake practice. Which booking records support that conclusion? In the request above, let `a` mean puncture practice, `b` wheel truing, `c` brake practice and `d` declining today's session. Add `"explain":"c"`. The result includes this witness.

```json
{"kind":"excluded","option":"c","steps":[{"history_index":0,"chosen":"a","over":"b"},{"history_index":1,"chosen":"b","over":"c"}]}
```

Each index counts from zero in the supplied history. It identifies a choice and the rival recorded as usable that day. If the qualified brake helper had already withdrawn on the second occasion, the corrected menu for that row is `["b"]`. Both recorded choices stand. Running the corrected history leaves `a`, `c` and `d` possible. The organiser can offer the learner a turn with the tools once the helper is available and ask what they want. Include declining wherever that option was actually available. Silence supplies no observed choice.

The search runs backwards from the queried option. The first other member of the next menu reached by breadth-first search gives a chain with the fewest observed comparisons. Each edge cites its first supporting row. Other rows or chains can independently sustain the exclusion, so rerun after a correction.

If the search finds no rival, `kind:"possible"` gives one `example_ranking` consistent with every recorded choice and placing the queried option first among the next offers. Its strict ancestors come first, then the option, then the remaining nodes, preserving topological order within each group. This witnesses possibility. If the history contains a cycle anywhere, `kind:"inconsistent_history"` cites a row for each edge of that cycle. Requesting one witness keeps the time and space bounds above. Omitting `explain` or passing `null` returns the original compact result.

### Check a disputed availability entry

If the second row's brake slot is unresolved, add `"check_availability":{"history_index":1,"option":"c"}` to the example request. Keep `"explain":"c"` to get a witness in each branch. The result has two complete answers, `if_usable` and `if_unusable`. For the latter, the calculation drops `c` from that row and keeps the observed choice of `b`, the other rows and the next menu.

| Could the learner use the brake slot on the second occasion? | Possible next choices under the model |
| --- | --- |
| Yes | `a,d` |
| No | `a,c,d` |

Treat these as conditional results until the old availability is established. Ask whether a qualified helper was still available to check the learner’s work at the time of that choice. If both branches exclude brakes, the second witness shows which comparisons still support that result. Either branch may report a contradictory history. The comparison applies to one recorded unchosen option at a time and runs the same solver twice. The next offer still needs the support and choice appropriate to the new occasion.

The [late workshop booking](CANDIDATE.md#as-departure-and-the-next-offer) gives a known limit. A permits forwarding a 17:40 departure time. A check ending at 17:50 falls outside that menu. If A explicitly declined in this two-option comparison, the row would contain only `decline`, with no edge against a qualified check. If the record says only that A left with the check outstanding, leave the choice unobserved. The time suffices to correct the menu and the reason stays private.

### When one past menu is incomplete

A learner once chose a borrowed printer when the makerspace printer was also usable. On a later visit they chose card. The desk had listed both printers and drawing by hand that day. Which of those three entries would be worth checking before anyone infers that the learner would turn down a makerspace slot?

Use `check_availability.options` to identify every disputed rival on one listed menu. It computes the bounds from the confirmed graph and the graph with every compatible disputed comparison. The singular `option` request above keeps its two full witness reports.

This example assumes one chooser with a fixed strict ranking. For the next decision, card and the makerspace are both confirmed usable. This is a separate calculation from [A’s account of changing the tactile-map aim](CANDIDATE.md#what-can-each-map-maker-do-next).

```json
{"history":[{"chosen":"borrowed","usable":["borrowed","makerspace"]},{"chosen":"card","usable":["card","borrowed","makerspace","drawing"]}],"usable_next":["card","makerspace"],"check_availability":{"history_index":1,"options":["borrowed","makerspace","drawing"]},"explain":"makerspace"}
```

```json
{"status":"compatible","possible_in_some_completions":["card","makerspace"],"possible_in_every_compatible_completion":["card"],"conflict_if_usable":[],"availability_check":{"option":"makerspace","history_index":1,"each_alone_rules_out":["borrowed","makerspace"]}}
```

Card remains possible in all eight completions. Under this model, confirming either printer on the card day would rule out a future makerspace choice. The borrowed printer matters because the learner had previously chosen it over the makerspace. Confirming drawing alone changes nothing about that inference. Establishing that one printer was unavailable leaves the other printer’s availability open. The organiser can offer the now-usable slot directly to the learner.

**Exact bounds.** Let $G$ be the comparison graph from confirmed options, $w$ the observed winner on the incomplete row, $U$ the unconfirmed alternatives there and $F$ the verified next menu. Any subset of $U$ may have been usable. All other historical rows are complete. A cycle among confirmed comparisons returns the usual contradiction.

1. Find the strict ancestors of $w$ in $G$. Each unconfirmed alternative in that set would close a cycle if confirmed. The output lists it in `conflict_if_usable`. Evidence that it was usable would call the recorded facts or the ranking assumption into question.
2. Let $D$ contain the remaining unconfirmed alternatives. Add every edge $w\to d$ for $d\in D$ to obtain $G^+$. These edges can coexist. Any new simple cycle would have to leave $w$ once and follow an old path back to $w$, which would put its first destination among the ancestors already removed.
3. Use the [ordinary possible-choice rule](#possible-next-choices) on $G$ and $G^+$. Adding comparisons can only remove possible winners. Both endpoint graphs are compatible completions. Their winner sets therefore give the exact union and intersection, respectively, across all compatible completions. An option in the intersection can win in every completion. Several options can have that property.

With `explain`, the output also names each unconfirmed option whose usability on that row would **by itself** exclude the queried next choice. A newly excluded choice has a path from a rival in $F$ through $w$, one new edge and an old path to the queried choice (possibly of length zero). A backwards search from the query identifies those decisive edges. An already excluded choice has no newly decisive edge. For bounded-size IDs, the graph traversals and hash-table operations take expected $O(L+|U|+V+|E|)$ time and $O(V+|E|+|U|)$ auxiliary space. The calculation treats uncertainty on one dated row. Disputes on several rows or evidence that the aim changed require a different comparison.

Two dates can require two answers together. Suppose the learner chose card when the borrowed printer’s availability was disputed, and chose the borrowed printer on another day when makerspace availability was disputed. With card and makerspace on the next menu, either old comparison alone leaves makerspace possible. Both together give `card > borrowed > makerspace`, which excludes it under the model. Compare the full histories explicitly when the question depends on more than one date.

### When the order may have changed

One chooser made $n$ observed choices in chronological order. All listed menus used here have been checked. A supplied range $a\leq k\leq b$ contains the possible boundary between two periods. Exactly $k$ observations precede it. Each period can have its own strict preference order, and the next choice belongs to the second period. The orders are allowed to coincide. The evidence for using this model belongs with the account.

Send this [learner’s request](CANDIDATE.md#when-a-learners-aim-changes) to `python3 choice_history.py --stdin`.

```json
{"history":[{"chosen":"repair","usable":["repair","teach"]},{"chosen":"teach","usable":["teach","guide"]}],"usable_next":["teach","guide","decline"],"change_window":{"earliest":1,"latest":2}}
```

```json
{"status":"compatible","compatible_boundaries":{"earliest":1,"latest":2},"possible_at_some_boundary":["teach","guide","decline"],"possible_at_every_boundary":["teach","decline"]}
```

For each boundary, the prefix and suffix must both have acyclic comparison graphs. Growing a prefix keeps every cycle it already contains. Shortening a suffix can only remove comparisons. The compatible boundaries therefore form a single interval $[s,p]$, possibly empty. As the boundary moves later within that interval, the current order has fewer constraints. If $P_k$ denotes the possible next choices at $k$, then

$$
P_s=\bigcap_{k=s}^{p}P_k,\qquad P_p=\bigcup_{k=s}^{p}P_k .
$$

An option in $P_s$ can win under at least one order for every compatible boundary. Several options can meet that condition. The result supplies neither a choice nor a commitment from the person.

The first occurrence of a comparison decides whether it appears in a prefix. Its last occurrence decides whether it appears in a suffix. Index those two records per comparison, binary-search the two monotone cycle tests, then run the existing winner calculation at the endpoints. For $L$ supplied option occurrences, $V$ distinct options, $E$ distinct comparisons and $W=b-a+1$, the expected time is $O(L+(V+E)\log(W+1))$ and auxiliary space is $O(V+E)$, for bounded-size IDs and hash tables. With `explain`, endpoint witnesses cite original row indices or exhibit a compatible current order. If no split works, the cited prefix and suffix cycles together cover every requested boundary. More changes, errors in the record and other choice rules remain possible explanations. For unresolved menus and a change window together, run each evidenced menu scenario separately.

### How late can the answer arrive?

The illustrated guide is one option A might want. Consider one arranged kit booking on one common clock. It takes four minutes from receiving A’s choice for it to reach the duty desk, two more to complete the booking and ten more to have the kit ready. The booking must complete **before** 17:20. The kit must be ready **by** 17:30. Nobody has assumed how long A takes to decide.

Pass this plan to `python3 simulator.py --deadlines -` on standard input, or replace `-` with a JSON file. IDs name events. Each link supplies a required elapsed time between two events. Each deadline names an event, an instant and its equality rule.

```json
{"clock":"minutes after 17:00","events":["answer","desk","booking","kit"],"links":[["answer","desk",4],["desk","booking",2],["booking","kit",10]],"deadlines":[["booking",20,"before"],["kit",30,"by"]],"check":{"event":"answer","at":14}}
```

| Event | Bound on this clock |
| --- | --- |
| A’s answer is received | Before 17:14 |
| It reaches the duty desk | Before 17:18 |
| Booking is complete | Before 17:20 |
| Kit is ready | By 17:30 |

An answer received at 17:14 leaves time for the kit. It misses the booking lock exactly. The result cites links 0 and 1 and deadline 0. A different arrangement with the kit deadline alone would allow 17:14. If A has yet to answer, another slot can be offered. Booking evidence and the learner’s own decision are separate inputs.

For an acyclic plan each link $u\to v$ with elapsed time $d$ requires $t_v\geq t_u+d$. Write $D(u)$ for its tightest direct deadline, including whether equality is allowed. Working in reverse topological order, take the tightest among $D(u)$ and every downstream bound $B(v)-d$ on an outgoing link. Subtraction preserves the equality rule. At the same instant “before” is tighter than “by”. Each path to a deadline supplies exactly that deadline minus the sum of its lags. The recurrence takes the tightest across all paths without listing them. Time and space are $O(V+E+D)$ for bounded-size inputs and $D$ supplied deadlines. A requested witness follows one limiting path.

An event with no reachable declared deadline has a `null` bound. All links in one plan are required. Compare alternative plans separately. Parallel jobs that share a person or a tool need an actual allocation and ordering. New lags, missing authority, clock uncertainty or a withdrawn offer can change whether a plan works in practice. [Implementation](event_bounds.py) · [Correction and hardening in the released reference](TRACE-v0.5-reference.md#correction-and-hardening)

### Can the desk honour every held place?

A, B and C each have a workshop place held. The desk has three timed, staffed opportunities to confirm a booking before closing. Each can serve one person. A and B can call. C can reply in writing. Each could book if they were the only taker. With one phone slot and two written slots, A and B need the same slot if they both accept.

Feed this request to `python3 booking_capacity.py` on standard input. `slots` lists confirmation slots whose timing, staffing and authority are established together. Each offer identifies a recipient and the slots they can use before closing. Give any other candidate routes for those same slots as `unconfirmed`. Record the usable channel while leaving the person’s reasons private.

```json
{"slots":["phone-1","written-1","written-2"],"offers":[{"person":"A","confirmed":["phone-1"]},{"person":"B","confirmed":["phone-1"]},{"person":"C","confirmed":["written-1","written-2"]}]}
```

```json
{"status":"insufficient","shortfall":{"people":["A","B"],"slots":["phone-1"]}}
```

The desk can see which resource to change. An authorised clerk converts one writing slot to a second phone slot and keeps the other writing slot for C. Replace `written-1` in the slot list with `phone-2`. The desk has confirmed A and B can each use `phone-1` and C can use `written-2`. While B’s use of `phone-2` is still open, give B `"unconfirmed":["phone-2"]`. The result is `unconfirmed` with the same shortfall on confirmed routes and a candidate allocation of A to `phone-1`, B to `phone-2` and C to `written-2`. `routes_to_confirm` names B’s route to the second phone slot. When the desk confirms that route and moves it into B’s `confirmed` list, the same allocation is supported and the result is `confirmed`. Each recipient still decides whether to use the offer. Record actual bookings separately.

An existing promise also uses capacity. Keep a promised slot as the only route in that recipient’s row until they agree to a change and the desk confirms it in time. To check only the remaining offers, omit that recipient and their committed slot. Leave a slot that has already been used out of the remaining inventory.

**Exact check.** Treat recipients and slots as the two sides of a bipartite graph. Try to assign one new recipient at a time. A search from that person follows allowed routes to slots and from occupied slots to their current holders. Reaching a free slot lets the desk move the earlier assignments along the path. If the search runs out of routes, every reached slot belongs to a reached person. The reached people include those holders and the extra unassigned recipient. They collectively have fewer usable slots than people. The returned group and its complete set of usable slots certify the shortfall.

Try the confirmed graph first. A full allocation there supports honouring all the offers together. If it falls short, allow all declared unconfirmed routes for a second check. A shortfall even in that larger graph rules out an allocation among the supplied routes. A full allocation there identifies one set of unresolved routes to confirm together. Its viability depends on those confirmations and on preserving the timed, staffed slots. For $P$ recipients, $S$ slots and $E$ supplied routes, two such checks take $O(P(P+S+E)+S)$ time and $O(P+S+E)$ space with bounded-size IDs. [Implementation](booking_capacity.py) · [Workshop handover](CANDIDATE.md#who-had-a-way-to-book) · [Earlier account of shared capacity](https://github.com/markgoodbody-bit/TRACE/blob/475772354a29cdd96b3c8fae7be93449c4737d71/TRACE.md#L1759)

## One session or both?

For the [two Saturday bookings](CANDIDATE.md#does-c-need-one-quiet-saturday-or-both), let $U_i$ mean that C has a usable quiet session on date $i$. By the end of the second Saturday, access at least once is $U_1\cup U_2$. Access on both dates is $U_1\cap U_2$. The plans, information and dates stay fixed while C’s intended use determines which event matters. The same opening decision covers both dates at the second venue.

```python
from fractions import Fraction

# Each history records usable access on the first and second Saturday.
plans = {
    "first venue": [((True, False), Fraction(1))],
    "other venue": [((True, True), Fraction(1, 2)),
                    ((False, False), Fraction(1, 2))],
}

for venue, histories in plans.items():
    once = sum(weight for access, weight in histories if any(access))
    both = sum(weight for access, weight in histories if all(access))
    print(venue, once, both)
```

The columns are the probabilities of access at least once and access on both dates, respectively.

```text
first venue 1 0
other venue 1/2 1/2
```

The calculation uses only the two named dates. Continuous access between them would need its own evidence. [Comparing complete plans for a named goal](../SYNTHESIS.md#2-a-common-mathematical-setting) · [The corrected hope calculation](../MATH-REVIEW.md#2-corrected-hope-calculations)

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
- [TRACE 0.6.1-exp.4 — Why this future?](NAVIGATOR-0.6.1-exp.4.md) carries the learner's home aim and changing support through a handoff. It scopes the unchanged finite replay to today's checked attempt. The candidate's new departure passage integrates the [revised scene](GOOD-DAY-0.6.1-exp.5.md), including the learner's choice to keep their reason private. The existing 25 review decisions were retained after checking that the candidate outside the inserted section matches the previous source exactly. Their candidate digest was repinned; the addition does not establish semantic preservation or reader effectiveness.
- The [B0107 comparison](SEMANTIC-REVIEW.md#present-value-and-constructive-formation-23-november-2026) restores the present value of curiosity, care, creation and play alongside the distinction between represented possibilities and supported formation. It does not resolve the preceding formation sequence or its baseline and evidence conditions.
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

1. Continue from the 206-block inventory, splitting or joining blocks where their meanings require it. The [review ledger](review-decisions.json) records the current dispositions and outstanding gaps. Retain the source distinction between reproduced and reference-only donors.
2. The finite simulator examines a declared joint law, one observation with conditional likelihoods, allowed booking routes and shared capacity, plus a separate stipulated delivery/backup event predicate. General observation histories, multi-actor actions, delivery schedules, actual delivery evidence, partial-contributor burden, controlled UNKNOWN, preference formation, normative authority and complete consent/commitment records remain open. See Codex's other PR71 dependence cases for further tests.
3. Fresh AI readers used specific workshop and tactile-map excerpts at the revisions named in the [semantic review](SEMANTIC-REVIEW.md). Transfer to other decisions, comparison with ordinary prose and use by people in practice remain open.
4. The co-evolving social probe is an invented example, not a formal complexity model or validation of the method's treatment of emergence. Read the relevant primary literature before attributing claims. The separate two-track brief at COM b1f0515cbc6920236e2ae34292f35d7b395620f0 and updated integration contract at TRACE f928f04e99e1b87c3c9b65fc9bcad6375bcda739 supersede earlier direction; this draft branch remains based on the earlier contract commit and does not itself contain that updated contract.
5. This packet has not recovered the earlier reported simulator or 114-unit manifest. Retain a later recovered copy separately and compare rather than overwrite.

No new paid inference, provider action, live YAC change, Workshop runtime, model agency claim, semantic equivalence, canonical release or independent reproduction.
