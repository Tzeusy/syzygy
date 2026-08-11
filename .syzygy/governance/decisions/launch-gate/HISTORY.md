# Launch-gate history — the Markdown-record era, v1.3 → v1.18

> **Historical record. Non-authoritative, and deliberately not on any
> default reading path.** This is the review chronology that used to sit in
> `PROJECT-STATUS.md`, moved here on 2026-08-11 under the owner charter's
> §6.1 ("Move the v1.3→v1.18 review chronology to the launch-gate history
> area"). The prose below is **verbatim as it stood** at commit `0a7f1ff`
> and is not edited: it is a snapshot of what was true when it was written,
> and where it disagrees with the current state, the current state wins.
> What superseded it is stated at the end of this file, not inside the
> snapshot.

Current state lives in `PROJECT-STATUS.md`; the instrument lives at
`launch-gate-pre-specifications.md`; the owner decision is P-34
(`../LAUNCH-GATE-AUTHORITY-DECISION.md`).

---

## The chronology as it stood (verbatim snapshot, 2026-08-11)

Separately, a pilot administration of the
owner's launch-gate instrument (v1.3, at commit `067d8a0`) returned
**GATE VERDICT: NOT READY** — 17 of 31 questions Not met, including all six
of section E, the OpenSpec-readiness section itself; the raw record is
`…/round-2026-08d/reviews/LAUNCH-GATE-ADMINISTRATION-2026-08-09-RAW.md`.
The instrument is now **v1.18** (candidate; owner approval prepared as
P-34). The repair-and-re-review chain: RD-24 (v1.4, REVISE) → v1.5 →
RD-33 (REVISE, five MAJOR) → v1.6 → RD-34 (REVISE — one BLOCKING: the
deferral-carrying pass branch ran no formula conjunct) → v1.7 → RD-35
(REVISE — one BLOCKING: the new citation-existence check shipped
inverted, invisible because no fixture tested the passing direction) →
v1.8 → RD-36 (REVISE — two MAJOR: a pass verdict could rest on a
deferral "granted" by a review finding, because the `B-n` family the
v1.8 batch accepted is review-finding numbering, not decisions; and a
§5 field written with an empty value silently borrowed the next line's
text) → v1.9 → RD-37 (REVISE — two MAJOR: the v1.9 negation rule,
shared across checks of opposite polarity, silently loosened LG-13
into accepting enumerated reopen lists led by a negation clause — a
measured regression against v1.8 — and three §5 fields still resolved
by first match) → v1.10 → RD-38 (REVISE — one BLOCKING: a record
deleting its G1 section and six of the eight declared §5 fields
validated clean under `READY FOR <the verbatim target>` by quoting
§5's own template in a fenced appendix — seven checks turned into
no-ops by one quotation) → v1.11 → RD-39 (REVISE — the strongest
verification pass of the chain, all seven RD-38 repairs present and
five closed outright; but two BLOCKING: the fence strip, inserted
upstream of the terminal-line rule, silently redefined "last", so a
record whose stored terminal verdict reads `NOT READY` validated
clean and entered the trend log as `READY FOR <the verbatim target>`
— a hole the v1.11 batch itself created — and the quotation repair
closed one carrier of four, leaving the composite validating when its
template rode an HTML comment, a blockquote, an indented block, or
one line of prose) → v1.12 → RD-40 (REVISE — and in the reviewer's
own words "the most disciplined batch of the eight": all seven RD-39
repairs present, every mutation denominator reproduced, all thirteen
checks fixtured with a computed denominator; but two BLOCKING, and
both of them the *same* question — a verdict **quoted after** the
record's own terminal line, in a blockquote, an indented block, a
list item or a line of prose, was silently parsed as the terminal
verdict, so four records validated at 0 errors turning a stored
`NOT READY` into `READY FOR <the verbatim target>`; and the presence
anchor's list-marker allowance let a bullet-list quotation of §5's
template satisfy all six `Label:` tokens, so RD-38's composite
reproduced whole) → v1.13 → RD-41 (REVISE — six of RD-40's eight
findings closed outright, the hardest of them, in the reviewer's
words, "genuinely, structurally closed", and all ten mutation
denominators reproduced; but four BLOCKING, the first of which is the
same class a fifth time and says why it keeps recurring: the own-line
predicate was **line-local**, and a container is a *region, not a
line* — every markdown container marks a block's first line and
continues without its marker, so a list item's continuation lines
counted as the record's own and RD-38's composite validated at 0
errors under `READY FOR <the verbatim target>`; a `<details>` block
silently **supplied** the record's decisive declared values, E3's
reopen-list and the owner's deferral citation among them; §9 stated a
mutation count of eight where ten is the fact; and the LG-4 residual
disclosed as opening no pass was a load-bearing limb of one) → v1.14 →
RD-42 (REVISE — six BLOCKING: the batch that replaced enumeration with
state kept an enumeration for raw HTML, so `<div style="display:none">`,
`<p style="display:none">`, `<span hidden>` and `<table><tr><td>` each
hid a declared field from the reader while the validator read it as the
record's own, an inline `` `</details>` `` code span reopened the one
element the counter did know, and the same door reported a `READY FOR`
hidden below a record's visible terminal `NOT READY` as that record's
verdict; §2's integrity anchor was the tenth `_decl` site and still read
hidden text; LG-4's new emptiness requirement was inert in the record
shape §5 mandates; and three of four fixtures shipped for the previous
repair witnessed a different rule than the one they were written for)
→ v1.15 → RD-43
(REVISE — two BLOCKING: the raw-HTML region still did not begin or end
where a reader sees it, measured by rendering the record and parsing it
with an HTML5 parser; an indented-code close tag, a backslash-escaped
close tag, a mid-line opening tag and an opening tag split across two
lines each carried a declared field — or a whole verdict, below a
visible `NOT READY` — past the validator at 0 errors; a line beginning
with an autolink blanked every line after it; and LG-4's emptiness
requirement silently withdrew five lawful forms of G1 content) → v1.16
→ RD-44 (REVISE — three BLOCKING: v1.16 adopted the rendering method
and then did not apply it to the rule it was used to justify, reading
CommonMark's start condition 6 as opening a region *from any position*
when it is line-initial like all seven, so **53 of 62 element names**
named once mid-sentence in a lawful record blanked the rest of it at 0
errors; and in the other direction four independent constructions — a
mid-line `<script>`, a mid-line `<style>`, an indented-code close tag
after a heading, and a lone pipe-delimited line carrying a
`display:none` div — each produced `record valid` and a trend row
reading READY FOR the verbatim target beneath a record whose last
visible line read `GATE VERDICT: NOT READY`) → v1.17 → RD-45 (REVISE —
four BLOCKING: v1.17 fixed the **rule** and never measured the **set**
the rule ranges over, so `<iframe>`, `<noframes>`, `<noembed>` and
`<select>` — each unpainted mid-line — laundered a READY FOR beneath a
visible NOT READY at 0 errors, two of them regressions of that batch and
one of them the name RD-44 had recorded as correctly refused; and the
corpus could not tell, because 65 of 83 new fixtures took their expected
direction from the set under test) → v1.18.
The v1.8 through v1.18 batches are
validator-and-records only — the instrument's §1–§8 have now gone
**eleven amendments across twelve versions** (v1.7–v1.18) byte-unchanged,
and the §8 parameter block fourteen versions (v1.5–v1.18), while the
measuring layer keeps yielding one more class per administration. The
diagnosis has moved one step per review and is now as specific as it
has been: RD-39 said a repair must be specified over the **property**;
RD-40 said stop enumerating carriers and **enumerate the question**;
RD-41 said the question is not answerable from the line at all —
**the predicate must carry state**, because a container is a *region,
not a line*; RD-42 said the state had been written for markdown's
containers and **an enumeration kept for HTML's**. v1.13 wrote one own-line predicate over a table of nine
containers and was broken by the continuation lines those containers
open. v1.14 replaces the table with CommonMark's block-structure
phase: for each line, the stack of containers open at it — blockquote
at any depth, list item at its content column, raw-HTML block —
maintained across lines with lazy continuation, consumed by the
terminal-verdict rule, the six presence tokens, the banner test, the
G1 anchor and now `_decl`, so a value carried only on non-own lines is
an absent field rather than a supplied one (168 fixtures; sixteen
mutation-reverts, fourteen failing exactly the fixtures their repair
added and **two disclosed as failing nothing** rather than counted as
proven; RD-41's attack records re-executed — both continuation
composites score 6 errors where they scored 0, every `<details>`-hidden
declaration is absent, LG-4's two doors are shut, and a record whose
visible terminal verdict reads `NOT READY` behind a non-breaking space
now reports `NOT READY` instead of the `READY FOR` it also carried).
v1.15 finishes the same move on the last container that had not had it:
a raw-HTML region opens at a line beginning with a tag of any name,
every tag inside it is read, a close tag pops back to the element it
names, code spans are removed before any tag is read, and self-closing
and void forms open nothing (187 fixtures; thirteen mutation-reverts,
twelve failing exactly the fixtures their repair added and **one
disclosed as failing nothing**; three lawful records the previous
validator refused with 8, 8 and 1 errors — a `<details>` named
mid-sentence, a `` `<summary>` `` in a code span, a `<details>` in a
table cell — now validate clean, and all 37 stored attack records from
the three earlier rounds produce byte-identical output under both
versions). v1.16 finishes the move the previous batch began, on the
authority the previous batch lacked: the block phase is decided before
any tag is read, the region trigger is CommonMark's own start condition
6 rather than a rule chosen here, an autolink is not a tag, and a
section's content is what a reader sees in it (205 fixtures; twelve
mutation-reverts, whose denominators RD-44 reproduced exactly). **The
method is the durable part:** a claim about what a reader sees is now
settled by rendering the record and parsing the result, never by
reading a specification — a distinction that had already carried two
reviews and one repair batch in the wrong direction.

v1.17 applies that method to the rule v1.16 used it to justify, and the
sentence is RD-44's: **a region begins at a line, not at a `<`.** The
trigger is line-initial for every name; a mid-line tag opens a region
only when it takes its content out of a reader's sight, by element type
(CommonMark's condition-1 raw-text elements, and a collapsed
`<details>`) or by a hiding attribute; `para_open` means *a paragraph
is open*; a table row is a row **of a table**; and the hiding set gains
`visibility:hidden` and `opacity:0`. Both lists are disclosed as
**enumerations**, with no sufficiency asserted for either. One reviewer
limb is **declined with its measurement**: `hidden` is a global boolean
attribute, so `<see the hidden appendix>` does take the next declared
field out of sight, and the code-span form is fixtured as the safe way
to write it (288 fixtures; nine mutation-reverts, one per repair, all
nine witnessing). The regression claim changed shape too, after two
rounds of unreproducible attack-record figures: it is now a **scripted
corpus sweep** whose population is defined by construction — every
record each version's own selftest hands to the validator, replayed
through both — reporting **0 of 200 carried-forward records moved** and
**65 of the 82 records added at v1.17 answered differently by v1.16**,
which is the accepting direction 205 fixtures could not tell. A
regression claim in this chain now quotes a script's printed output or
does not appear.

v1.18 answers RD-45's sentence — **measure the set, not just the rule,
and let a fixture's expectation come from somewhere other than the thing
it is testing.** Every enumeration in the predicate is now generated
against the render over a named population with a denominator: the
mid-line hiding set is measured across **84 element names** under two
readers that agreed on all 84 — eight hide, 69 paint, and **seven the
measurement could not settle are refused in the safe direction and
disclosed as unsettled rather than counted as measured**, which is the
one refusal in this predicate resting on something other than an agreed
measurement. The fixtures' expected direction moved to a literal table
written down with its date and method, and a further fixture fails if
the predicate's set and that table ever disagree. Four parser repairs
travel with it: quoted attribute values are consumed as the tokenizer
consumes them; a raw-text element suppresses tag reading whether or not
it opened a region; a wrapped opening tag is one rule in both positions;
and a region ends where its markdown container ends, so a `<details>`
named inside a blockquote or a list item no longer swallows the record
(329 fixtures; twelve mutation-reverts, one per repair, all twelve
witnessing; the sweep reporting 282 carried forward, 0 dropped and
exactly five movers, every one named and deliberate). One correction
this batch owns without qualification: v1.17 changed the split-tag rule
and **recorded it nowhere**, in a delta whose first paragraph says it
records every change of meaning — and that unrecorded change is what
reopened a carrier.

Two of v1.14's decisions are worth stating as decisions rather than
repairs, because they are where the instrument's own text constrains
its validator. **Blockquote laziness is deliberately not implemented:**
§5's frozen template places the declared fields on unmarked lines
directly beneath the blockquote banner, so strict CommonMark would make
those fields blockquote content and refuse every lawful record —
measured at 43 of 168 fixtures. And because a quotation whose fields
land at column 0 is byte-for-byte §5's own declaration form, with no
marker in §5 that would tell the two apart, containment alone cannot
finish: two further rules do, on properties a quotation cannot shed —
a declaration is read only at or above the record's own terminal
verdict, and a field carrying §5's own angle-bracket placeholder has
not been answered. Closing the underlying limit properly would need a
§5 amendment, which is an owner act and not a batch's to make. Each
re-review verified the prior batch whole before finding the next
class; the P-34 offer waits on the RD-46 re-review of the v1.18 delta,
and the formal administration that a launch decision could rely on has
not yet been run.

---

## What superseded this snapshot

Two things, both dated 2026-08-11:

1. **RD-46 was never dispatched.** The snapshot above says the P-34 offer
   waits on it. It does not: the owner's charter of 2026-08-11 directed the
   session to *stop the carrier-by-carrier Markdown parser loop* and to
   dispatch no further review whose main purpose is finding one more
   Markdown, HTML, list, fence, table, or rendering carrier. The composed
   RD-46 dispatch was retired unsent.
2. **The instrument moved to v2.0**, which is not another parser repair.
   The canonical administration record is now structured JSON validated
   against a committed schema, and the Markdown report is generated from it
   and never parsed back. §1, §3, §4 and §8 of the instrument are
   byte-identical across the change — no question's text moved and the
   verdict formula is unchanged. The delta is
   `../../contracts/candidates/round-2026-08f/LAUNCH-GATE-v2.0-SEMANTIC-DELTA.md`.

**What this chronology is still evidence for.** Thirteen consecutive
`REVISE` verdicts against one instrument, each repairing a real defect,
none closing the class — which is the argument for the v2.0 change and the
answer any future reader deserves to the question "why was the record
format replaced rather than fixed?" The records themselves
(`round-2026-08e/reviews/RD-33…RD-45`) remain immutable, and
`scripts/launch_gate_results.py` remains in the repository to validate the
Markdown administrations written in that era.
