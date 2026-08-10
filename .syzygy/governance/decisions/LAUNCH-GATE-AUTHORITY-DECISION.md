# Owner decision packet — launch-gate process-policy authority

> **This file decides nothing, adopts nothing, approves nothing.** It is
> the exact owner decision required to put the launch-gate instrument into
> force as process policy. Queued in `PENDING-OWNER-DECISIONS.md` as
> **P-34**. Until this decision is recorded, the instrument is a candidate:
> its administrations are evidence the owner may weigh, and nothing more.

## Question

Approve `launch-gate-pre-specifications.md` **v1.15** as this repository's
owner-approved **process policy** for evaluating pre-specification
readiness?

> **Offer status (2026-08-11, third revision):** not yet offerable.
> Ten re-reviews, ten `REVISE` verdicts: v1.5's (RD-33) closed by
> v1.6; v1.6's (RD-34) by v1.7; v1.7's (RD-35 — the new
> citation-existence check shipped inverted) by v1.8; v1.8's (RD-36) by
> v1.9; v1.9's (RD-37) by v1.10; v1.10's (RD-38) by v1.11; v1.11's
> (RD-39) by v1.12; v1.12's (RD-40) by v1.13; v1.13's (RD-41) by v1.14;
> and v1.14's re-review (**RD-42**, `VERDICT: REVISE`) is closed by
> v1.15.
>
> RD-42 verified all twelve RD-41 findings present, reproduced the
> fixture arithmetic, constructed all sixteen mutation-reverts from the
> delta's own descriptions and measured each, and confirmed the §1–§8
> identity and the frozen population. It then ran **every captured
> fixture through both validators on identical bytes** — and returned
> **six BLOCKING** findings, the first of which is the same class for
> the **sixth** time, and the reason it keeps recurring is worth the
> owner's attention: v1.14 replaced enumeration with state for
> markdown's containers and **kept an enumeration for HTML's**. Four
> carriers the enumeration did not name — `<div style="display:none">`,
> `<p style="display:none">`, `<span hidden>`, `<table><tr><td>` — each
> hid a declared field from the reader while the validator read it as
> the record's own, and an inline `` `</details>` `` code span reopened
> the one element the counter did know. The same door laundered a
> verdict: a `READY FOR` hidden in collapsed content below a record's
> visible terminal `NOT READY` was reported as the record's verdict, in
> pure ASCII. Alongside it: `Parameter block sha256:` — §2's integrity
> anchor — was the tenth `_decl` site and still read hidden text, where
> the delta claimed all ten read the record's own lines; LG-4's new
> emptiness requirement was **inert in the record shape §5 mandates**;
> and three of the four fixtures shipped for the previous round's
> restoration repair witnessed a different rule than the one they were
> written for, alongside two counts (`fourteen` witnesses, `four`
> markers) that were false of the bytes.
>
> v1.15 is a **validator-and-records batch** an eighth time; instrument
> §1–§8 have now gone **nine versions** (v1.7–v1.15 — eight
> amendments; the §8 parameter block alone is unchanged across eleven,
> v1.5–v1.15, each figure swept this session) byte-unchanged, each
> verified per-section. **A raw-HTML region is now element nesting**,
> like every other container in the predicate: it opens at a line whose
> content begins with a tag of any name, every tag inside it is read, a
> close tag pops back to the element it names and pops nothing if it
> names none, code spans are removed before any tag is read, and
> self-closing and void forms open nothing. One decision the owner
> should read as a decision rather than a repair: **outside a region a
> line must begin with a tag to open one**, which is what lets a
> reviewer write *about* a carrier — three lawful records that v1.14
> refused with 8, 8 and 1 errors now validate clean — and which costs a
> record line that itself begins with an inline tag, paid in the
> refusing direction. One clause is disclosed as having **no
> single-layer witness** (0 of 187) rather than counted as proven, and
> one message is made true of what it matched rather than of §5's text,
> with the literal-matching alternative rejected **by measurement**.
> Because the same session that authored the v1.15 bytes may not confirm
> them, the offer waits on a fresh-context re-review of the v1.15 delta
> (**RD-43**). The formal administration must not run on any earlier
> validator (the closing directions of RD-33 through RD-42).

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

- **(a) Approve v1.15 as offered.** The amendment records are
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
  amendments. Three lawful records the previous version refused are
  newly accepted, and one clause is disclosed as unwitnessed rather
  than counted as proven).
- **(b) Approve with amendments** — state them; the changelog takes a
  v1.16 entry and the semantic delta extends. One prepared amendment the
  owner may take here: **promote F5 (assurance independence) from a
  recorded question to a verdict conjunct** — v1.15 deliberately leaves it
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
rounds produce byte-identical output under v1.14 and v1.15.

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
   APPROVED — launch-gate v1.15 as process policy
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
the changelog's v1.15 entry — so the digest always binds the amended
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
