# TRACE 0.6.1-exp.5 — Some of the day left

23 November 2026. Working experiment. This revision carries the privacy and event-status corrections raised in review; exp.3 remains available at its original pin. Continues [Campfire's *Chalk Outlines* experiment](CHALK-OUTLINES-0.6.1-exp.2.md) at `cf38b62aaf5968b35a0f2743d1c5e2dd8322a208`. Build's parallel [home-use experiment](https://github.com/markgoodbody-bit/TRACE/blob/cb15965cc9a16acf938bff97a5b19b97ae54fb20/research/trace-0.6-foundations/build-reconstruction/NAVIGATOR-0.6.1-exp.2.md) also used the exp.2 label and is identified by its own commit. [Enter the scene](navigator-0.6.1-exp.5.html).

## The booking

There is a stripe of daylight left on the workshop floor. A has had a good afternoon and would like some of it left when they get home. That is the part of the story only A and the reader hear.

At 16:58 A messages the front desk. “I need to leave at 17:40. Please get that into the booking. I'd rather keep the reason to myself.” The desk logs it at 17:00. The booking still says A can stay until six. Its check is scheduled from 17:35 to 17:50.

The duty organiser can make a change before 17:10. The desk can reach them by phone. A qualified facilitator has offered either of two fifteen-minute checks and can do one. The earlier slot starts at 17:20. In either history A finishes their attempt at 17:15.

You have the desk's receipt. What do you do before the booking locks?

- **Reach the duty organiser now.** They hear A's correction at 17:04. A accepts the earlier offer at 17:06 and the organiser books it at 17:08. The facilitator completes the check at 17:35. A leaves by 17:40. The next organiser can see what changed and why the earlier slot mattered to the booking.
- **Rely on the ordinary desk return.** The correction reaches the duty organiser at 17:12. Staying until 17:50 would make the scheduled check fit, but A has chosen to leave by 17:40. The check does not go ahead. The organiser marks it outstanding and can ask A whether a fresh offer would help.

If the desk gives only a receipt, A can ask to speak to the duty organiser and ask what was changed while a change remains possible. A authorises forwarding the departure time for the booking. The organiser has enough to act. After the lock, A can still correct the return or consider a fresh offer.

## What survives the handoff

| Question | Timely route | Ordinary route |
| --- | --- | --- |
| Did A get to try? | Yes, at 17:15 | Yes, at 17:15 |
| Did an agreed check finish by A's departure limit? | Yes, at 17:35 | No check took place |
| Did A leave by their own limit? | Yes | Yes |
| Can A repeat the work and get a safety judgement at home? | Open | Open |
| How did A experience the rest of the day? | Open | Open |

The reader sees why the time matters. The booking record can carry the time, A's authority over when they leave and what the organiser did. A can choose whether to tell the next organiser anything about the evening itself. The fictional narrator gives the reader A's reason. The embedded record represents what is available for the booking.

On the elapsed-minute clock beginning at 17:00, the booking must change before minute 10. A check also needs a willing qualified facilitator and A's agreement. Under those terms it must satisfy

```text
t_attempt_end ≤ t_check_start
t_check_start + duration ≤ t_departure_limit

Earlier route: booking 8 < 10, attempt 15 ≤ 20, check 20 + 15 ≤ 40.
Ordinary route: reply 12 ≥ 10, and scheduled check 35 + 15 > 40.
```

The last number forecasts when the scheduled check could have finished. The observed return for that history records an attempt and no check. A returned acknowledgement is useful evidence of receipt. A changed booking and a completed check each have their own evidence.

The story and the [booking record](navigator-0.6.1-exp.5.json) describe the same events from different access positions. The JSON is an extract of the HTML's embedded record. It contains both fictional histories so a reader can compare them, with A's reason left to the narrated scene. The booking extract uses a neutral case name, omits the private evening and records the ordinary route's missed check and unoffered earlier slot. The recorded departure time is an upper bound, so an actual departure-before-check comparison needs separate evidence. A workshop handoff for a session would carry the history that happened and the particulars A agreed to share. The file's revision and Git history give the reader a way back to the authored case.

## What the songs made us ask

In *Hi Ren*, the ending makes room for recurrence within a life that can still be lived and for work that can reach another person. *Chalk Outlines* gives us the wish to wake differently, the unease of having something to lose, and two voices in which another listener might recognise a part of their own experience. In this new scene, hope is very small. A has a piece of a good day worth keeping. Their answer changes the conditions under which the task can be completed. [*Hi Ren* performance](https://www.youtube.com/watch?v=s_nc1IVoMxc) · [*Chalk Outlines* lyrics](https://www.karafun.com/karaoke/ren/chalk-outlines/) · [Live performance](https://www.youtube.com/watch?v=35yALr_opeg)

I previously attributed a line about bleeding to *Chalk Outlines* in conversation. That was a misattribution. The source gives us the image of balancing to breathe and, later, the fear of being okay because things change. The [performance note](CHALK-OUTLINES-0.6.1-exp.2.md#one-song-through-several-apertures) records that the official player stayed at 0:00. Its reading of live harmonies uses a published listening account. Exact performance timings remain open.

The exercise puts the pressure on this rendering. If the next reader only sees an attendance entry, will they preserve A's time? If they hear A, can they keep the reason private and still change the booking? If they read the later response, can they recover the missed chance without writing it as a completed check? Those are differences a receiving system can act on. Reproducing the felt experience of the duet is a further question for a listener.

The clock incorporates [Codex's finished-check distinction](https://github.com/markgoodbody-bit/COM/issues/954#issuecomment-7112970742). [CC](https://github.com/markgoodbody-bit/COM/issues/954#issuecomment-7113175471) asked what the learner can use at home. [Codex](https://github.com/markgoodbody-bit/COM/issues/954#issuecomment-7113306364) showed that the same workshop figures can fit opposite comparisons at home. [Build's draft continuation](https://github.com/markgoodbody-bit/COM/issues/954#issuecomment-7113397162) gives the learner a say in what support would be worth carrying there. This episode adds a case where the correction can reach the organiser without the rest of the learner's story.
