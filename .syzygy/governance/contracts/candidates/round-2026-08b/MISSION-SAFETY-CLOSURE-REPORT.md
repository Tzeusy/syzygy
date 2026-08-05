# Mission-safety closure — RC-7's eleven blocking seams, dispositioned

> **Non-authoritative round record.** RFC-0010's clause text is the authority
> for what the contract says; the raw review at
> `reviews/RC-7-mission-safety-RAW.md` is the authority for what the reviewer
> found. Where either disagrees with this file, this file is wrong.

## What was asked, and what came back

RC-7 was given RFC-0010, RFC-0011, the D3 packet, doctrine, and the prior
`MISSION-CONTROL-REVIEW.md`, and asked to attack the Mission material rather
than assess it: run concrete scenarios and report where the contract fails to
constrain an agent that is trying to escape.

It ran ten attacks and returned **eleven blocking findings, F1–F11**. Its own
summary of the shape of the problem is the sentence worth carrying forward:

> The contract has a prevention plane and no correction plane.

That is a precise diagnosis, not a rhetorical one. RFC-0010 was thorough about
stopping an agent from acquiring authority it was not granted, and nearly
silent about what happens after something has already gone wrong inside a grant
that was legitimate. Six clauses were added in response, and they are all on
the second side of that line.

## Disposition table

Every row states what closed the seam and — where nothing closed it — says so.

| # | Seam | Disposition | Where |
|---|---|---|---|
| F1 | `propose-only` is the cap the whole safety argument rests on, and the corpus never defines it | **Closed by definition.** RFC10-7 now defines `propose-only` as *no effect outside `.syzygy/**` and `openspec/**` that is not itself an owner-signed dispatch of one work item*, with the exclusions named | RFC10-7 |
| F2 | No budget reservation at dispatch; a contract-sanctioned unbounded, unrecorded post-exhaustion overrun; no rule when spend is Unknown | **Closed.** RFC10-17 requires reservation at dispatch for sibling runs, not only for child missions; bounds and records the overrun; and gives Unknown spend a defined behaviour rather than leaving it to the implementation. RFC10-11 gained the matching reservation constraint | RFC10-17, RFC10-11 |
| F3 | Completion is self-adjudicable — a decider is named for one transition and for no other | **Closed.** RFC10-18 names the adjudicator of a mission's completion predicate and forbids the executing party from being the sole establisher of its own success | RFC10-18 |
| F4 | No reversibility declaration, no compensation, no failure semantics, no recovery owner, no resumption | **Closed.** RFC10-19 requires effects to declare reversibility, owes a compensating action or an explicit statement that none exists, names the recovery owner, and defines the relationship between completed and failed sibling work | RFC10-19 |
| F5 | The unstated-is-narrowest rule covers grants but not obligations, so an unstated obligation reads as absent rather than as maximal | **Closed.** RFC10-7 now states the grants-versus-obligations rule explicitly: silence narrows a grant and does **not** narrow an obligation | RFC10-7 |
| F6 | Stop prevents new dispatch but guarantees nothing about running work, has no latency bound, and makes no consistency claim | **Closed.** RFC10-20 states what stop guarantees for in-flight work, bounds the latency, and states the consistency claim | RFC10-20 |
| F7 | A cross-project composite has no rule selecting whose egress consent governs — the highest-consequence leak, because it moves source across a consent boundary while every field reads green | **Closed.** RFC10-21 supplies the selection rule for cross-project consent: the lesser binds | RFC10-21 |
| F8 | The attention queue is unbounded in every dimension flooding exploits | **Closed.** RFC10-22 bounds the queue and defines pause-on-bound rather than silent drop | RFC10-22 |
| F9 | Two disagreeing evidence sources have no rule | **Closed.** RFC10-6 gained the disagreeing-evidence rule | RFC10-6 |
| F10 | D3's `vision.md` insertion pre-answers open question D4; its `architecture.md` floor omits any maximum autonomy level | **Not closed by text, and deliberately not.** RC-7's own disposition is that this "closes by an owner ruling, not only by text." The D3 packet now discloses the objection at its §6 and carries the reviewer's alternative wording unadopted; the ruling is owner item **P-24** | D3 §6; P-24 |
| F11 | `MISSION-CONTROL-REVIEW.md:16` records a digest RFC-0010 has never carried | **Closed as a record correction.** Independently re-verified: the only commit ever containing the file carries `dfcedbbf…`; `8481335836…` appears nowhere in its history. A correction banner is on the review; the wrong value is left visible because the table records what the review claims to have read | `round-2026-08/MISSION-CONTROL-REVIEW.md` header |

**Nine of eleven closed by clause text. One (F11) closed as a record
correction. One (F10) is an owner ruling and stays open by design.**

## The stage-placement question, which is not a drafting question

RC-7 was also asked whether bounded Missions belong in V0 or V1, and answered
**V1**, with three exceptions it would ship at V0: the mission and envelope
*record* schema, the approval ceremony and external audit trail, and read-only
mission rendering through the same semantic API with human/machine parity.

Its reasoning is worth stating because it is the argument, not the conclusion,
that should survive: a V0 that can only propose does not yet need reversal,
adjudication, or recovery machinery, because the prevention plane is sufficient
when nothing irreversible can happen. The correction plane and the autonomy
ceiling therefore have to move together. **The combination RC-7 rules out is a
V0 that can apply effects without RFC10-19 and RFC10-20** — prevention alone,
over effects that outlast the sandbox.

One consequence is sharper than it looks and is recorded here in the review's
own terms: **open-PR is not V0**. A pull request looks reversible and is not —
it consumes reviewer attention, is externally visible, triggers CI spend and
deploy previews on many configurations, and a push to a remote is a
default-blocked destructive class under RFC5-22 precisely because its effects
outlast the sandbox.

This is a scope decision. It is **owner item P-23**, not a change made here.

## What this closure does not claim

- **The six new clauses have been read by no reviewer.** They were written in
  response to RC-7 and RC-7 has not seen them. They sit inside act 1's digest
  set, so act 1 would bind text that no independent review has read. This is
  the single largest outstanding item against the current manifest.
- **Closure is closure at contract level, not at implementation level.** Every
  clause here states an obligation; none of them is executable, and nothing in
  this repository can yet check whether an implementation honours one.
- **F2, F3 and F6 were the three RC-7 judged live "under the cap, on day one"** —
  because propose-only missions still spend money, still declare themselves
  complete, and still cannot be reliably stopped. Their closure is the part of
  this report most worth attacking again.
- **The residual seams RC-7 recorded as non-blocking are not restated here.**
  They are in the raw review, which is the authority for them.

## Verification

```sh
# the six new clauses exist and the ceiling matches the front matter
python3 .syzygy/governance/contracts/candidates/scripts/verify_final_prespec.py
# RFC-0010's digest, which act 1 binds
grep RFC-0010 .syzygy/governance/contracts/candidates/ACTIVE-CONTRACT-MANIFEST.txt
```
