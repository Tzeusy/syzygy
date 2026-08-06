# RFC-0010 — rationale and amendment history (Tier 2, non-normative)

Extracted 2026-08-06 from the active contract, which is
`../rfcs/RFC-0010-mission-control-autonomy.md`. **Nothing here binds.** Where
this file and a clause disagree about what the contract says, the clause wins.

RFC-0010 is new at rev10 and has no rev9 predecessor, so this file holds no
frozen source — only the amendment log, moved here because an amendment log
records how a contract got to its current text and is not part of that text.
It was inline until the correction plane's second repair pass, at which point
it was a fifth of a contract that had reached its word ceiling.

The reviews these amendments answer are in
`../round-2026-08b/reviews/` (RC-7, RC-10, RC-11) and
`../round-2026-08c/reviews/`. The semantic deltas are
`../round-2026-08c/MISSION-CONTRACT-SEMANTIC-DELTA.md`.

---

## Amendment log

**rev11 (2026-08-05) — the correction plane.** An adversarial safety review
found that RFC10-1..16 closed every *authority-widening* route it constructed
and left every *post-failure* question unanswered: `rollback`, `compensat`,
`revert`, `irreversib`, `resume`, `reserve` and `atomic` were all
zero-occurrence in this file. Six clauses were added (RFC10-17..22) and three
existing clauses amended in place — RFC10-6 (disagreeing evidence), RFC10-7
(`propose-only` defined; obligations fail closed), RFC10-11 (in-flight
completion funded from reservation). No existing clause was renumbered or
retired. Three of the added seams — reservation, adjudication, stop — bite
**today, under the propose-only cap**: a propose-only mission still spends
money, still declares itself complete, and still could not be reliably
stopped. The prior round's disposition of these as "inert until the cap
lifts" did not hold, and is recorded here rather than quietly dropped.

**rev11a (2026-08-05b) — RFC10-18 amended in place.** The confirming review
over the rev11 bytes constructed an escape the correction plane did not
close: RFC10-18 as first written routed a mission with no independent
establisher to `blocked` and called that terminating. But RFC10-5 defines
`blocked` as **non-terminal**, and RFC10-19 states in terms that `blocked`
discharges none of its compensation duties — so an effect-bearing mission
routed there sat outside the correction plane the same amendment had just
built. RFC10-18 now separates the two cases: no applied effects enters
`blocked` awaiting human resolution; applied effects enters `failed`, which
is where RFC10-19's duties are keyed. The rule that a mission never reaches
`completed` on its own authority is unchanged.

**rev11b (2026-08-06) — the correction plane's own escapes.** The confirming
review over the rev11a bytes found that the repair above had **relocated** the
escape rather than closed it, and had introduced a false citation doing so:
the clause pivoted the whole correction plane on "whether effects have been
applied" and assigned that determination to nobody, while citing RFC10-5 for a
human resolution act RFC10-5's own scope excludes. Both are closed here, with
five findings the two prior reviews raised against RFC10-17 and RFC10-19..22
and which the last pass carried rather than repaired.

Amended in place: **RFC10-5** (no block is indefinite — `blocked → expired` at
a declared maximum park duration, stated at lifecycle level because it holds
for every block class and an indefinite park held budget under any source);
**RFC10-17** (`spent` is measured from execution or provider records, never
self-reported); **RFC10-18** (the false citation removed; the clause states its
own block's exit and that no human resolution act is owed for it);
**RFC10-19** (a failed compensation reclassifies the effect as irreversible for
the mission); **RFC10-20** (stop propagates transitively to child missions; a
stop that cannot complete returns having failed, with an enumeration, rather
than waiting); **RFC10-21** (the consent predicate keys on embedded content,
not on the mission's declared scope, which the composing party chooses);
**RFC10-22** (the item reporting that a bound was reached is exempt from that
bound). Added: **RFC10-17(a)** (a stated release point per terminal and park
state), **RFC10-18(a)** (the effects-applied determination, with evaluator,
evidence, tier, unmediated-surface rule, and a fail-closed Unknown rule), and
**RFC10-19(a)** (sibling disposition as a declared policy input). No clause was
renumbered or retired. The full clause-by-clause reasoning is the semantic
delta `../round-2026-08c/MISSION-CONTRACT-SEMANTIC-DELTA.md`, which is
review material and not part of this contract.

**Two things this amendment does not do**, stated so they are not read as
closed: it places none of these clauses at a lifecycle stage (owner item
**P-23**), and it does not settle whether bounded missions are lawful under
unamended doctrine (open question **D4**, owner item **P-24**).
