# Owner decision packet — launch-gate process-policy authority

> **This file decides nothing, adopts nothing, approves nothing.** It is
> the exact owner decision required to put the launch-gate instrument into
> force as process policy. Queued in `PENDING-OWNER-DECISIONS.md` as
> **P-34**. Until this decision is recorded, the instrument is a candidate:
> its administrations are evidence the owner may weigh, and nothing more.

## Question

Approve `launch-gate-pre-specifications.md` **v1.16** as this repository's
owner-approved **process policy** for evaluating pre-specification
readiness?

> **Offer status (2026-08-11, fourth revision):** not yet offerable.
> Eleven re-reviews, eleven `REVISE` verdicts: v1.5's (RD-33) closed by
> v1.6 … v1.13's (RD-41) by v1.14; v1.14's (RD-42) by v1.15; and v1.15's
> re-review (**RD-43**, `VERDICT: REVISE`) is closed by v1.16.
>
> RD-43 verified all thirteen RD-42 findings present — **eight closed
> outright**, one **not closed** — and changed the chain's method: it
> settled every claim about what a reader sees by **rendering the record
> and parsing the result with an HTML5 parser**, rather than by reading
> the CommonMark specification. On that footing it returned **two
> BLOCKING** findings. v1.15's raw-HTML region still did not begin or
> end where a reader sees it: a close tag written as an indented code
> block, and a backslash-escaped one, each render as literal text and
> left the element open; a block-level tag mid-sentence, and an opening
> tag split across two lines, each opened an element the validator never
> saw. Four carriers followed, every one of them supplying the
> instrument's sharpest declared field from content whose DOM ancestor
> is `details` or a display:none `div`, at **0 errors** under `READY FOR
> <the verbatim target>` — and one laundered a verdict below a record
> whose last visible line read `GATE VERDICT: NOT READY`. Alongside
> them: a line beginning with a **URL or email autolink** blanked every
> line after it, terminal verdict included, refusing a lawful record
> with 8 errors; and LG-4's new emptiness requirement silently withdrew
> **five lawful forms of G1 content** — a bulleted list among them,
> which is the natural form for a completeness critic's output.
>
> v1.16 is a **validator-and-records batch** a ninth time; instrument
> §1–§8 have now gone **ten versions** (v1.7–v1.16 — nine amendments;
> the §8 parameter block alone is unchanged across twelve, v1.5–v1.16,
> each figure swept this session) byte-unchanged, each verified
> per-section. **The block phase is decided first** — fences, comments,
> indented code, backslash escapes and code spans are literal text —
> and tags are read only out of what survives; the region trigger is
> **CommonMark's own start condition 6**, quoted from the specification;
> an autolink is not a tag; and a section's content is what a reader
> sees in it. Two decisions the owner should read as decisions rather
> than repairs. **One acceptance is withdrawn on purpose:** a
> `<details>` named mid-sentence without escaping, which the previous
> review called lawful on a legacy HTML parse and which the HTML5
> algorithm collapses — the code-span and table-cell forms stay lawful
> and are how a reviewer writes about a carrier safely. And the
> predicate **refuses a declaration carried inside any raw-HTML element
> the record opens, whether or not that element hides it**, because
> deciding hiding means evaluating CSS the instrument cannot evaluate;
> that over-refusal is named and fixtured rather than described as harm
> prevented. **205 fixtures; twelve mutation-reverts, all twelve
> witnessing** — the first batch of this chain with no unwitnessed
> repair. Because the same session that authored the v1.16 bytes may not
> confirm them, the offer waits on a fresh-context re-review of the
> v1.16 delta (**RD-44**). The formal administration must not run on any
> earlier validator (the closing directions of RD-33 through RD-43).

## What approval binds — and what it never binds

Approval makes the instrument the governing rule for **how readiness is
evaluated**: the question set, administration protocol, closed verdict
vocabulary, launch-scope parameters (§8), verdict formula, results-record
format, and trend log. That this list and the instrument's own `governs:`
header state the same scope is a **reviewable claim by the repair pass**
(RD24-03 asked for the alignment), not a settled fact: the owner verifies
it by comparing the two lists at the act, and rejecting the alignment —
narrowing either list — is open under option (b). Administration records
produced under it are evidence at a named commit.

Approval never delegates the launch decision itself: no administration
verdict — including `READY FOR <target>` — authorizes specification
authoring. That authorization is a separate owner act, taken reading the
evidence (VIS-4). The instrument's own header states this and approval
ratifies that statement.

## Current authority

None. The instrument is self-declared "not authority"; v1.3 was
administered once (2026-08-09, pilot) without any owner approval of the
instrument. The pilot's `NOT READY` verdict is steering evidence the owner
has already directed this pass to respect.

## Options

- **(a) Approve v1.16 as offered.** The amendment records are
  `contracts/candidates/round-2026-08e/LAUNCH-GATE-v1.4-SEMANTIC-DELTA.md`
  (twelve deltas; no question weakened; three questions added from the
  pilot's G1; launch-scope parameters for Capability 1 fixed in §8),
  `…/LAUNCH-GATE-v1.5-SEMANTIC-DELTA.md` (the RD-24 fresh instrument
  review's 21 findings closed — **read with the v1.6 delta's D-10**,
  which corrects two of its claims; the frozen record itself is not
  edited, RD34-10), `…/LAUNCH-GATE-v1.6-SEMANTIC-DELTA.md` (the RD-33
  re-review's twelve findings closed),
  `…/LAUNCH-GATE-v1.7-SEMANTIC-DELTA.md` (the RD-34 re-review's eleven
  findings closed — the `READY-WITH-DEFERRALS` predicate stated and
  checked, the citation shape test, the terminal-line parse; **read with
  the v1.8 delta's D-1**, which corrects D-2's existence-check claim),
  `…/LAUNCH-GATE-v1.8-SEMANTIC-DELTA.md` (the RD-35 re-review's
  seven findings closed — the citation-existence check un-inverted with
  its passing direction fixtured, the terminal line made the parsed
  anchor, the verdict-line target bound, E3's reopen-list enforced;
  **read with the v1.9 delta's D-1 and D-4**, which correct D-6's false
  `B-n` family claim and D-5's over-readable removal claim), and
  `…/LAUNCH-GATE-v1.9-SEMANTIC-DELTA.md` (the RD-36 re-review's seven
  findings closed — `B-n` out of the identifier family with the false
  taxonomy corrected everywhere it was asserted, empty fields made
  absent rather than borrowed, shadowed fields made errors, both
  citation forms existence-guarded; **read with the v1.10 delta's D-1**,
  which corrects D-4's false claim that the negation edge fails "never
  as a silent pass"), `…/LAUNCH-GATE-v1.10-SEMANTIC-DELTA.md` (the
  RD-37 re-review's six findings closed — LG-13's emptiness made a
  positive closed-marker test with the shared predicate split, every
  declared field parsed through one disagreement-detecting helper, the
  G1 test anchored, the `--prior` record validated before trusted, the
  SDR guard anchored and scoped to made decisions; **read with the
  v1.11 delta's D-1**, which corrects its false vocabulary attribution,
  its both-directions claim, and its meta-fixture claim),
  `…/LAUNCH-GATE-v1.11-SEMANTIC-DELTA.md` (the RD-38 re-review's seven
  findings closed — fenced quotations stripped, the three §2 anchors
  line-anchored, the marker vocabulary corrected to validator policy
  and published in the error message, the meta-fixture replaced by the
  behavioral decoy loop, the prior bound to the closed verdict
  vocabulary and duplicate rules; **read with the v1.12 delta's D-1**,
  which corrects its "reaches every check" claim, its D-7 premise and
  mutation claim, its directionality statement, and its D-6
  impossibility sentence), and `…/LAUNCH-GATE-v1.12-SEMANTIC-DELTA.md`
  (the RD-39 re-review's seven findings closed — the terminal verdict
  measured over the raw record bytes so a stored NOT READY can never
  be reported READY, the presence checks made line-anchored field
  reads with a structural banner test, HTML comments stripped with
  fences, the fence grammar aligned with CommonMark, the prior
  validated as a record at its own named commit, the
  internal-whitespace fixture closing the rule-6 gap; validator and
  records only — no question weakened; no ID renumbered; instrument
  §1–§8 byte-unchanged through five amendments, six versions; **read
  with the v1.13 delta's D-1**, which corrects D-2's fourth limb, its disclosed-limit
  generalization, its "CommonMark's own bound" phrasing, its
  directionality assignment, and its D-5 mutation denominator), and
  `…/LAUNCH-GATE-v1.13-SEMANTIC-DELTA.md` (the RD-40 re-review's eight
  findings closed — one own-line predicate written once and consumed by
  the terminal-verdict rule, the six presence tokens, the banner test
  and the G1 anchor, so a verdict quoted after the record's own
  terminal line is an ambiguity error and a bullet-list quotation of
  §5's template satisfies nothing; tabs expanded before every
  indentation measurement; the LG-11 version fixture rebuilt on the
  RD34-05 shape so it can fail again; the fence-close rejection limb
  fixtured; validator and records only — no question weakened; no ID
  renumbered; instrument §1–§8 byte-unchanged through **seven
  versions, v1.7–v1.13** — six amendments. One acceptance is deliberately withdrawn:
  `- Operationalization notes:` satisfied presence at v1.12 and does
  not at v1.13, because the decoration allowance was the quotation
  carrier; **read with the v1.14 delta's D-1**, which corrects its
  predicate definition, its `_decl` scope sentence, its mutation count,
  its disclosed-limit generalization, its directionality assignment and
  its version-count figure), and
  `…/LAUNCH-GATE-v1.14-SEMANTIC-DELTA.md` (the RD-41 re-review's twelve
  findings closed — the predicate rewritten to carry the block stack
  across lines, `_decl` made a consumer of it, declarations read only
  at or above the record's own terminal verdict, §5's own placeholder
  refused as an answer, LG-4 required to open a non-empty section with
  its anchor matched per line, unicode whitespace folded before the
  verdict token is searched for, and four lawful records restored that
  v1.13 refused with a message untrue of them; **read with the v1.15
  delta's D-1**, which corrects its "raw-HTML block" predicate
  description, its "all ten `_decl` sites" claim, its mutation-witness
  count, its correction-marker count, its restoration claim, one
  directionality assignment and one unverifiable nit), and
  `…/LAUNCH-GATE-v1.15-SEMANTIC-DELTA.md` (the RD-42 re-review's
  thirteen findings closed — a raw-HTML region made an element-nesting
  decision rather than a two-tag-name counter, closing five carriers
  and the code-span reopen and the verdict laundered below a visible
  `NOT READY`; the tenth `_decl` site made a consumer with the sites
  enumerated mechanically; LG-4's emptiness requirement made effective
  in the record shape §5 mandates; one heading regex requiring the
  space CommonMark requires; the placeholder message made true of what
  it matched; and the previous round's restoration fixtures rebuilt so
  they witness the repair they were written for; validator and records
  only — no question weakened; no ID renumbered; instrument §1–§8
  byte-unchanged through **nine versions, v1.7–v1.15**, eight
  amendments; **read with the v1.16 delta's D-1**, which corrects its
  element-nesting sentence, its self-closing clause, its claim that
  three lawful records were restored, its carrier claim, its LG-4 claim,
  its inline-tag residual and its unreproducible regression figure), and
  `…/LAUNCH-GATE-v1.16-SEMANTIC-DELTA.md` (the RD-43 re-review's seven
  findings closed — the block phase decided before any tag is read, so
  indented code and backslash escapes are literal text; the region
  trigger taken from CommonMark's own start condition 6, so a
  block-level tag mid-sentence and a tag split across lines both open
  what the renderer opens; autolinks excluded from the tag grammar; and
  a section's content measured as what a reader sees in it; validator
  and records only — no question weakened; no ID renumbered; instrument
  §1–§8 byte-unchanged through **ten versions, v1.7–v1.16**, nine
  amendments. Five lawful G1 forms and four lawful angle-bracket shapes
  the previous version refused are newly accepted; one acceptance is
  deliberately withdrawn with its measurement stated; and every one of
  the twelve mutation-reverts witnesses a repair).
- **(b) Approve with amendments** — state them; the changelog takes a
  v1.17 entry and the semantic delta extends. One prepared amendment the
  owner may take here: **promote F5 (assurance independence) from a
  recorded question to a verdict conjunct** — v1.16 deliberately leaves it
  non-gating at Administration 1 and discloses instead (RD24-12); making
  it a conjunct means no same-family administration can ever read READY.
- **(c) Decline** — the gate remains an informal checklist; readiness
  claims fall back to ad-hoc reports, the class this repository has twice
  found stale in the documents owners were sent to.

## Consequences

- (a/b): the next administration can be **formal** (Administration 1 of
  the trend log) once the §2 integrity requirements are met; F1 trend
  claims become possible at Administration 2.
- (c): no administration can be more than advisory; E-section closure has
  no agreed evaluator, and "ready" returns to being asserted rather than
  administered.

## Recommendation

`[Inferred]` **(a)**. The pilot demonstrated the instrument finds real
defects (its C1 finding — a retired phrase standing as the live gate in
two digest sets — was independently confirmed by the round-08d reviews),
v1.4's changes are exactly the pilot's own recorded gaps, v1.5's are
exactly the fresh instrument review's (RD-24: three of its findings were
mutation-proven against the named validator), v1.6's are exactly the
first re-review's (RD-33: five findings proven by constructing records
that validated clean and should not have), v1.7's are exactly the
second re-review's (RD-34: its BLOCKING finding was an all-Not-met record
validating clean under `READY-WITH-DEFERRALS`), v1.8's are exactly the
third re-review's (RD-35: its BLOCKING finding was the new existence
check rejecting every real decision path, invisible because no fixture
tested the passing direction), v1.9's are exactly the fourth
re-review's (RD-36: a pass verdict could rest on a deferral "granted"
by a review finding, certified by an accepting fixture asserting a
false taxonomy), v1.10's are exactly the fifth re-review's (RD-37: a
record enumerating live E3 reopen items beside `E3 | Met` under a
READY verdict validated clean — the exact record §3 says cannot be
ready — because one predicate served three checks with two polarities),
v1.11's are exactly the sixth re-review's (RD-38: a record deleting
its completeness critic and six declared §5 fields validated clean
under `READY FOR <the verbatim target>` by quoting §5's own template
in a fenced appendix), v1.12's are exactly the seventh
re-review's (RD-39: the fence strip silently redefined the
terminal-line rule so a stored NOT READY entered the trend log as
READY FOR the verbatim target, and the quotation repair had closed
one carrier of four), v1.13's are exactly the eighth re-review's
(RD-40: a verdict *quoted after* the record's own terminal line was
parsed as the terminal verdict in four carriers, and a bullet-list
quotation of §5's template satisfied all six presence tokens — both
of them the same question, "is this line the record's own?", answered
five different ways by five consumers). Each repair now has a fixture
that fails without it — **145 in all**, the ten mutation-reverts
failing exactly the fixtures their repairs added, with the one
two-layer redundancy reported as one behavioral witness rather than
two; and RD-40's attack records re-executed against the repaired
validator: the four quoted-after-terminal carriers each error with
the trend verdict blank, the composite that scored 0 errors now
scores 6, and the tab-fence record scores exactly what its four-space
control scores. The one residual those records disclosed did not
survive review: LG-4 was satisfied by a column-0 `## G1` heading
however empty the section beneath it, disclosed as opening no pass,
and RD-41 measured it to be a limb of one — v1.14 closes it. And
v1.14's repairs are exactly the ninth re-review's
(RD-41: the own-line predicate was line-local, so a list item's
continuation lines counted as the record's own and the composite
validated whole a fifth time; a `<details>` block silently supplied the
record's decisive declared values). v1.15's repairs are exactly the
tenth re-review's (RD-42: the HTML limb was the enumeration the
previous batch said it had abandoned, so four unnamed carriers and an
inline code span each hid a declared field — or a whole verdict — from
the reader while the validator read it as the record's own; §2's
integrity anchor was the one `_decl` site still reading hidden text;
and LG-4's new emptiness requirement was inert in the record shape §5
mandates). Each repair now has a fixture that fails without it —
**187 in all**, with twelve of thirteen mutation-reverts failing
exactly the fixtures their repair added and the one disclosed as
unwitnessed; RD-42's attack records re-executed against the repaired
validator: each of the five carriers reports its hidden field absent,
the laundered `READY FOR` below a visible `NOT READY` is an ambiguity
error rather than the record's verdict, the hidden `Parameter block
sha256:` is reported absent rather than mismatched, a bare `## G1` in
§5's own shape opens an empty section, and the three lawful records the
previous validator refused — a `<details>` named mid-sentence, a
`` `<summary>` `` in a code span, a `<details>` in a table cell —
validate clean. All 37 stored attack records from the three earlier
rounds produce byte-identical output under v1.14 and v1.15. And
v1.16's repairs are exactly the eleventh re-review's (RD-43: the
raw-HTML region still did not begin or end where a reader sees it —
an indented-code close tag, a backslash-escaped close tag, a mid-line
opening tag and a tag split across two lines each carried a declared
field, or a whole verdict, past the validator at 0 errors; a line
beginning with an autolink blanked every line after it; and LG-4's
emptiness requirement withdrew five lawful forms of G1 content). Each
repair now has a fixture that fails without it — **205 in all**, with
**all twelve** mutation-reverts failing exactly the fixtures their
repair added; RD-43's attack records re-executed against the repaired
validator: each of the four carriers is refused, the laundered verdict
is an ambiguity error rather than the record's verdict, the four
angle-bracket shapes and the five G1 forms validate clean, and across
the 54 stored attack records of the four earlier rounds exactly one
record moves — the withdrawn acceptance, whose measurement is stated.

## Mechanism (the lawful transaction, prepared not performed)

The owner-act model here is digest-bound approval, as with craft policy
(D2 / `INSTALL-RECORD.md`), not a magic phrase. The order matters: the
status edit comes **first**, so the digest the approval binds is the digest
of the bytes that will actually be in force (RD24-01 — binding the
pre-edit digest would leave the approval attesting bytes that exist
nowhere once the header flips). To approve:

1. Edit the instrument's `status:` header — a governance-lifecycle state —
   from candidate to in-force, in the working tree. That edit is part of
   the act, not a later drift.
2. Compute the digest of the result:
   `sha256sum launch-gate-pre-specifications.md`
   This digest names the exact bytes being placed in force.
3. Record in this file, below this line, an approval block:

   ```text
   APPROVED — launch-gate v1.16 as process policy
   date: <date>
   instrument sha256: <the digest computed in step 2, post-status-edit>
   scope: process policy for pre-specification readiness evaluation;
          no administration verdict is an owner act
   by: the owner
   ```

4. Commit the status edit and the approval block in one change, with the
   approval in the message. Every later administration quotes and verifies
   this same digest (instrument §2 / LG-2), so the approval and the
   in-force bytes can never disagree.

Under **option (b)**, the ordering extends the same way (RD33-11): the
owner's amendments are applied to the instrument **in the working tree
before step 2's digest is computed** — together with the status edit and
the changelog's v1.17 entry — so the digest always binds the amended
bytes; the amendments, status edit, changelog entry, and approval block
travel in the one commit of step 4. An amendment applied after step 2
would recreate exactly the approval-attests-bytes-that-exist-nowhere
defect RD24-01 closed.

## Earliest required gate

Before the **formal** launch administration (the one a Capability 1 launch
decision would rely on). The pilot has already run; nothing else waits.

## Independent work

Everything — repairs, packets, reviews — proceeds regardless. Only the
formal administration's standing waits on this.
