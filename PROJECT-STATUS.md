# Project status

> **As-of: 2026-08-10** (the commit introducing this revision of this file —
> `git log -1 --format=%h PROJECT-STATUS.md`). This file is a hand-authored
> pointer page with an as-of revision: it **must not be the sole source** for
> any fact it states — each row cites the owning record, and where they
> disagree, the record wins and this file is stale. It is regenerated or
> corrected in the same change whenever a gate fires.

## Lifecycle stage

**Final pre-specification.** No application code exists; none may be added
until the foundational contracts are accepted and behavioral specifications
are authored and approved.

## Gates

The single foundational-contract act was **restructured into six wave acts
at round-2026-08d** (owner work order; design:
`.syzygy/governance/contracts/candidates/round-2026-08d/ACCEPTANCE-WAVE-DESIGN.md`).
An **act** is an exact phrase the owner types once, binding one
script-computed digest of one artifact set; a **wave** is one of the six
contract subsets those acts accept independently. The acceptance record
owns the phrases and the ceremony — and its **§7** ("items requiring
explicit owner attention at the gate") is read **before any act** (§2
step 0): it lists the drafted arms and open questions each act ratifies
beyond its digest.
The rev9 and rev10 all-in-one acceptance phrases are retired and satisfy
nothing (the acceptance record's retirement paragraph names them).

**Launch scope (owner-directed, 2026-08-10).** The launch target is
**Capability 1 — Project registration and honest shape visibility**, whose
contract prerequisite is **Waves A + B only**. Waves C1/C2/D1/D2 — and the
P-29/P-30/P-32 rulings that gate their repairs — are **visibly deferred**,
not retired: candidate, not accepted, not used by the launch target, and no
C/D wave act is offered while that posture stands. The posture and its
per-wave reasons are
`.syzygy/governance/contracts/candidates/DEFERRED-WAVE-POSTURE.md`.

| # | Gate | Gate state | Owning record |
|---|---|---|---|
| 1 | Doctrine adoption | ✅ **Adopted** 2026-07-30, amendment D1 in force | tag `doctrine-adopted-2026-07-30`; `.syzygy/governance/doctrine/README.md` |
| 2 | Craft-and-care approval | ✅ **Approved** (owner decision D2) | `.syzygy/governance/policies/craft-and-care/INSTALL-RECORD.md` |
| 3 | Surface decisions | ✅ **Recorded** SDR-1…33 | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md` |
| 4a | Wave A — kernel/evidence/storage/admission/selection (RFC 0001–0006) | ⏳ **Candidate — no act performed** | acceptance record §1 + `wave-manifests/WAVE-A-MANIFEST.txt` |
| 4b | Wave B — the three surfaces (RFC 0007–0009) | ⏳ **Candidate — no act performed** | acceptance record §1 + `wave-manifests/WAVE-B-MANIFEST.txt` |
| 4c | Waves C1/C2 — context packets; selection policy (RFC-0011) | ⏸️ **Deferred — candidate, no act performed, not offered** while the deferred-wave posture stands | `DEFERRED-WAVE-POSTURE.md`; acceptance record §1 + `wave-manifests/WAVE-C1…C2-MANIFEST.txt` |
| 4d | Waves D1/D2 — mission prevention; correction plane (RFC-0010) | ⏸️ **Deferred — candidate, no act performed, not offered** while the deferred-wave posture stands | `DEFERRED-WAVE-POSTURE.md`; acceptance record §1 + `wave-manifests/WAVE-D1…D2-MANIFEST.txt` |
| 5 | Craft amendment CC-TEST-2 (act 2) | ⏳ **Awaiting confirmation** at the current digest | `INSTALL-RECORD.md` **2026-08-06** correction block — the 2026-08-05 block holds the retired `3858820f…` argument (review RD-8, finding S11) |
| 6 | Topology (act 3) | ⏳ **Candidate — no act performed** | `.syzygy/map/topology-candidates/BUNDLE-MANIFEST.md` |
| 7 | Project overview (act 4) | ⏳ **Draft — refactored, awaiting adoption** | `.syzygy/intent/OVERVIEW.md` header |
| 8 | Doctrine amendment D3 — bounded missions (act 5, optional) | ⏳ **Proposed** — adopt, amend, or decline | `.syzygy/governance/contracts/candidates/DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md` (rev1; supersedes the original `…-DRAFT.md`) |
| 9 | Knowledge-hygiene craft policy | ⏳ **Candidate — own craft act** (P-12) | `.syzygy/governance/contracts/candidates/policy-candidates/CRAFT-KNOWLEDGE-HYGIENE-POLICY.md` |
| 9b | Specification-acceptance craft standard (CC-SPEC-1…10) | ⏳ **Candidate — own craft act; blocking Capability 1 prerequisite** (P-41, added 2026-08-10) | `.syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`; queue row P-41 |
| 10 | License | ⏳ **Undecided — owner/legal** | `.syzygy/governance/decisions/LICENSE-DECISION-PACKET.md` |
| 11 | Behavioral specifications (OpenSpec) | ⛔ **Not started** — blocked on the wave acts | — |
| 12 | Implementation | ⛔ **Not started** — blocked on gate 11 | — |

**No owner acceptance act has been performed.**
`.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md` does not exist,
which is the correct state — it is created by the first act.

The full open-decision queue is
`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`. The exact
phrases, digest arguments, and the ceremony live in
`.syzygy/governance/contracts/candidates/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`,
which wins over any offering. The `round-2026-08c/`, `round-2026-08b/` and
`round-2026-08/` offerings are superseded and banner-marked. No Wave A or
Wave B offer stands yet. Both current wave arguments now carry
`VERDICT: CONFIRM` from their fresh exact-package reviews — Wave A's from
RD-31b, Wave B's from RD-32c (2026-08-10). The Wave A offer is withheld
solely by P-33 (§7 item 11); nothing withholds the Wave B offer itself,
which follows Wave A's on the A → B path (the register:
`.syzygy/governance/contracts/candidates/round-2026-08e/reviews/DELIVERY-AND-VERDICT-REGISTER.md`).

## What exists in this repository

Adopted doctrine; owner-approved engineering policy; recorded owner
decisions with tracked warrant extracts; the candidate contract corpus
(RFC 0001–0011, 39 modules — RFC-0010 split into a five-module package and
RFC-0011 into two at round-2026-08d) with its generated manifests (active +
six wave), acceptance record, ten context-selection fixtures, reviews, and
verification scripts; the candidate topology bundle; candidate policy
additions; the overview draft; navigation skills; documentation-only CI.
**No** `openspec/`, no accepted-contract home, no source tree, no product
CI, no implementation backlog.

## Open state, honestly

**The two blocking defects the 2026-08-07 readiness report named are
repaired in the candidate bytes, and the repairs are unreviewed.**

1. **Mission safety.** The RFC10-17-vs-RFC10-10 contradiction (budget
   invariant over the ledger, prevention demanded over consumption) is
   repaired by the round-2026-08d rewrite of RFC-0010's budget module
   (six-quantity accounting; enforced-limit admission at the RFC5-21
   launch gate and the RFC5-15 per-transmission predicate), and the
   correction plane was rebuilt against reviews RD-1/RD-1b's blocking
   findings. The pre-split disposition report and the frozen-bytes rule it
   described are historical:
   `…/round-2026-08c/MISSION-SAFETY-CLOSURE-REPORT-vNEXT.md` (banner-marked).
2. **Deterministic context selection.** RFC11-4's unsatisfiable universal
   is replaced by declared `implementation_boundary` metadata (RFC11-13),
   stated traversal/termination rules (RFC11-14), declared doctrine/craft
   ownership or stated judgment (RFC11-15), and clause-first `constrains`
   consumption (RFC11-16); RFC-0001…0005 now carry real phase-rule clauses
   (RFC1-33, RFC2-26, RFC3-33, RFC4-30, RFC5-27). The ten fixtures carry a
   task/answer boundary for blind derivation, and fixture 10 covers the
   Trajectory-lifecycle class whose double-count RD-5 found. [Inferred]
   Class coverage is claimed by construction only — no independent blind
   derivation has run over the restructured fixtures yet.

**The Wave A and Wave B repairs have landed, and both current wave
arguments carry `VERDICT: CONFIRM` — Wave A's from RD-31b, Wave B's from
RD-32c (both 2026-08-10)** *(this sentence said "no confirming review is
bound" until RD-31b delivered, and "Wave B's awaits RD-32c" until RD-32c
delivered — each corrected the same day, per RD32b-N5's discipline)*. The round-2026-08d fresh-context review
pass delivered fifteen reviews — **fifteen `REVISE` verdicts, zero
`CONFIRM`** — with all 173 findings disposed in
`…/round-2026-08d/reviews/DISPOSITION-REGISTER.md`. The round-2026-08e
launch-closure pass then repaired Waves A and B under the owner's
Capability 1 direction (semantic deltas:
`…/round-2026-08e/WAVE-A-SEMANTIC-DELTA.md`, `WAVE-B-SEMANTIC-DELTA.md`)
and regenerated their manifests; the C/D-wave findings remain disposed but
unrepaired, deliberately, under the deferred-wave posture. The 08e
fresh-context review fleet's wave gates have both resolved (the register
is the record): **RD-31b and RD-32c bound `VERDICT: CONFIRM` to the
current Wave A and Wave B arguments on 2026-08-10** *(this passage said
the offers still waited until each gate delivered — corrected the same
day, per RD32b-N5's discipline)*. Separately, a pilot administration of the
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

**One thing this project does not have, stated plainly:** there is no
mechanical task-to-context-packet compiler — `context_load.py` measures a
selection you have already made, and every fixture's selection is
hand-authored. The fixtures' verification checklists say so per fixture.

## Next lifecycle step

The Capability 1 path, per `DEFERRED-WAVE-POSTURE.md`: finish the
round-2026-08e fresh-context review fleet, ending with the exact-package
reviews of the regenerated **Wave A** and **Wave B** arguments; repair
anything those reviews find and re-bind; then the per-wave owner offers
(acts on Waves A and B only), the launch-gate formal administration under
the owner-approved instrument (P-34 first), and the owner's launch
decision — with the authoring-side prerequisites (P-39 form, P-40
granularity, **P-41 the specification-acceptance craft act**) ruled before
the first spec is authored. Waves C1/C2/D1/D2 and the P-29/P-30/P-32 rulings stay deferred
until the owner lifts that posture. After the waves an owner accepts, the
first concrete proposal runs through `/th-projects
project-feature-request` toward an owner-approved OpenSpec delta —
specification authoring, still no implementation.

## How to verify this page

```sh
python3 .syzygy/governance/contracts/candidates/scripts/verify_final_prespec.py
python3 .syzygy/governance/contracts/candidates/scripts/build_contract_index.py --check
python3 .syzygy/governance/contracts/candidates/scripts/build_dependency_index.py --check
python3 .syzygy/governance/contracts/candidates/scripts/build_budget_report.py --check
python3 .syzygy/governance/contracts/candidates/scripts/build_active_manifest.py --check
python3 scripts/check_governance.py
git tag --list 'doctrine-*'
```

Also run `python3 scripts/check_governance.py --selftest`, which puts a
synthetic failing input against **the checks that have a fixture** — not every
check. **CG-24 computes which families are covered and prints the figure every
run**; quote that, never "each check shown able to fail", which two independent
reviews found false while it sat beside a fixture count. The selftest exists
because this repository has shipped a validator that could not fail: the dependency index reported 20
asymmetric edges at every generation while its own drift check reported clean,
because regenerating a knowingly-broken graph reproduces the same
knowingly-broken file.

**The result figures that used to sit here are withdrawn.** They were correct
when written and stale within two commits, twice, in the two documents an owner
is sent to for evidence — the exact failure the battery was built to catch,
recurring in the description of the battery. Run the commands; every check
prints its own denominator and its own rationale, and the WARNs are
declared-by-design (forward references, frozen-packet pointers, report-only
budget and default-load figures, allowlists). **Read the output, not the exit
code** — a PASS over zero examined items verified nothing.

Run it in a **clone**, not only here. At one commit this round the two
disagreed — 0 FAIL in the working tree, 1 FAIL in a clone — because CG-14
asked the local filesystem whether a git-excluded directory existed, and the
founder machine has one. That divergence is the whole failure mode this
repository keeps re-acquiring, and it is invisible from the machine that has
the directory.
