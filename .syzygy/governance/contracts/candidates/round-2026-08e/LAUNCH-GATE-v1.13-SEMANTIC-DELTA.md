# Launch-gate v1.12 → v1.13 — semantic delta record

> **Process record for a candidate instrument amendment.** The instrument
> (`launch-gate-pre-specifications.md`, repo root) is a process-policy
> candidate, never authority. This delta records every change of meaning so
> "no question was weakened" stays a reviewable claim. Owner approval of
> v1.13 is prepared, not performed:
> `.syzygy/governance/decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` (P-34) —
> and the offer waits on a fresh-context re-review of this delta
> (**RD-41**), because the session that authored these bytes may not
> confirm them.

Baseline: v1.12 as re-reviewed by RD-40 (subject sha256
`4ad21f8087ca110ecdc5392535ea74f7fc96a7a88e75da07582a74596077c686` at
commit `7751f12`; validator sha256
`471648ca71d88d30b223f9fdf542c75073fb5bf332f854905c91830f77d25ace`; raw
review `reviews/RD-40-instrument-v112-RAW.md`, storage digest
`8dfb74e1671e405f7bd1f58ac5ebec77bdbdab25aee64ed804bd1cd43a86167a`,
`VERDICT: REVISE`, 2 BLOCKING / 3 MAJOR / 3 MINOR — and, in the
reviewer's own words, *"the most disciplined batch of the eight"*: all
seven RD-39 repairs present, every mutation denominator reproduced, all
thirteen checks fixtured with a computed denominator, and §1–§8
byte-identical for the fifth amendment running). Every delta below closes
an RD-40 finding; dispositions in `reviews/DISPOSITION-REGISTER.md`.
**This is a validator-and-records batch a sixth time: no question block,
no verdict word, and no section §1–§8 of the instrument changed**
(verified per-section against
`git show 7751f12:launch-gate-pre-specifications.md` — §1 794, §2 4388,
§3 15377, §4 5688, §5 3601, §6 2192, §7 1038, §8 6610 bytes, each
identical; the §8 parameter block digest is unchanged and is recomputed
with the validator's own `param_block_bytes`, never transcribed here).
The instrument bytes that move: the `effective_version:` header, the
appended §9 v1.13 entry, and two dated correction markers in the §9 v1.12
entry (D-1 names them). Validator changes carry fixtures
(`scripts/launch_gate_results.py --selftest`, **145 fixtures** — the
count read from the selftest's own printed output); **ten**
mutation-reverts, with one measured qualification stated at D-4 rather
than hidden in a denominator.

RD-40's prescription, adopted as this batch's discipline — and it is a
correction of method, not of a repair: **stop enumerating carriers and
enumerate the question.** *"The terminal verdict, the six presence
tokens, the banner, the G1 anchor and `_decl` are five consumers of one
question, and they answer it five different ways today."* Four
consecutive blocking findings — RD38-01, RD39-01, RD40-01, RD40-02 —
were that single question, "is this line the record's own, not a
quotation of it?", answered inconsistently by consumers that never
shared an answer. Each previous batch specified its repair over *the
instances the previous review constructed*, and each next review broke
it with the next instance. This batch writes the question down once.
Like its six predecessors, this record predicts nothing about whether
the batch is the last.

## D-1 — corrections of the frozen v1.12 delta and the §9 v1.12 entry (the frozen record is not edited)

Five claims of the v1.12 delta are false or misassigned; per the D-10
convention the frozen record is not edited, and this entry is the
correction of record. The two that also appear inside §9 — the bytes an
approval digest binds — carry dated correction markers in place (the
RD36-01/RD38-02/RD39-02 precedent; §9 is changelog, not §1–§8).

1. **D-2's fourth limb** (*"or shadowed by a quoted verdict line placed
   after the record's own"*) and the §9 sentence *"a verdict quoted
   after the record's own terminal verdict is ambiguous, never silently
   resolved"*: **false** (RD40-01). The v1.12 rule compared the raw
   text's last token-carrying line to the *stripped* text's last one. A
   verdict quoted in a blockquote, a four-space-indented block, a list
   item or a line of prose is present in **both**, so the two agreed and
   the quotation was parsed as the terminal verdict. RD-40 measured four
   such records at **0 errors**, each converting a stored `NOT READY`
   into a trend row reading `READY FOR <the verbatim target>`. The
   repair had closed exactly the two carriers the strip removes. Made
   true at D-3 below.
2. **The disclosed-limit sentence** in §9 and its narrow twin in D-3
   (*"the other six fields and LG-4 still reject such a record"*):
   **false as generalized** (RD40-02). D-3's own statement about the
   *blockquote* composite was correct and narrow; §9 widened it to
   *"such a record"*, where it is false. The presence anchor's optional
   list marker — added to close RD39-07's lawful decoration — is the
   canonical markdown form of a quoted field list, so a bullet-list
   quotation of §5's template satisfied all six `Label:` tokens; with a
   nested-blockquote banner and a column-0 `## G1` heading in the same
   appendix, a record carrying **none** of the eight declared fields
   validated at 0 errors under `READY FOR <the verbatim target>`. Made
   false-proof at D-4 below, with the one residual (LG-4) named and
   measured rather than asserted away.
3. **D-4's and §9's "CommonMark's own bound" phrasing**: **imprecise in
   a way that cost a check** (RD40-03). CommonMark's bound is three
   *columns*, and it defines tab expansion for exactly this reason;
   v1.12 counted characters, so a single tab opened a fence and deleted
   a line every reader sees. RD-40 measured a record whose honest
   `Deferred count: 3` sat between tab-indented backticks scoring **0
   errors** with the decoy `0` standing, where its four-space control
   scored 3. Corrected at D-5 below.
4. **The directionality statement's D-4 assignment**: **misassigned**
   (RD40-05). The *"four-backtick short-close exploit"* was listed
   under *newly rejected*; the shipped fixture asserts the opposite
   direction — that a four-backtick fence is **not** closed by three
   backticks, so the quoted content stays stripped. The rule's
   rejection limb was real but unfixtured. Both limbs are fixtured at
   D-7 below, and this delta's directionality section states each
   fixture's direction as the fixture itself measures it.
5. **D-5's mutation denominator of 3**: **honest count, misleading
   weight** (RD40-08, which RD-40 raised against its own verification
   rather than against a claim). Two of the three fixtures that failed
   under the v1.11-prior-guard revert failed only because they assert
   the literal string `RD39-05` in an error message; behaviorally the
   denominator is **1**. Restated: 1 behavioral witness + 2 ID-string
   regression guards. This delta applies the same standard to its own
   numbers at D-4.

## D-2 — one own-line predicate, written once, applied by every consumer (RD40-01 + RD40-02, BLOCKING)

The distinction "the record's own line, not a quotation of it" is now a
single function over the record's lines, and it is the only place the
question is answered. A line is the record's own when, after the fence
and HTML-comment strip:

| container | own? | why |
|---|---|---|
| column 0 … 3 columns of indentation | **own** | CommonMark's paragraph bound |
| ≥4 columns, spaces **or tabs** (tabs expanded to 4-column stops) | no | indented code block — literal content, D-5 |
| fenced (` ``` ` / `~~~`), any run length ≥3, indent ≤3 | no | stripped upstream |
| HTML comment, whole-line or inline | no | the one carrier no reader sees |
| blockquote `> ` | no — **except the banner** | §5's banner *is* a blockquote, so the banner test alone accepts single-level `> ` and refuses `> > ` |
| list item `-` `*` `+` `1.` `1)`, at any depth | no | the canonical carrier of a quoted field list — **reversing a v1.12 acceptance**, D-4 |
| setext heading text (`Label:` over `---`) | no | a heading rendering of a quoted label |
| raw-HTML block (`<details>` / `<summary>`) | no | collapsed content a reader may never open |
| ATX heading `## `, table cell, mid-line prose | no | already refused at v1.12; unchanged |

Its consumers, all four now reading the same answer: the
**terminal-verdict rule** (D-3), the **six `Label:` presence tokens**
(D-4), the **non-authority banner test**, and the **G1 anchor**.

`_decl` — the ten declared-value reads — is deliberately **not** a
consumer, and this is a stated scope decision rather than an omission.
`_decl` is `^`-anchored with no decoration allowance at all, so every
container in the table either fails the anchor outright (blockquote,
list, indent, heading, table cell, prose) or, where a quotation does
reach column 0, produces a **loud disagreement error** rather than a
silent substitution — which is the safe direction and the one RD-40
audited at 10 of 10 sites. Sharing the predicate with `_decl` would
change no verdict and would put a second policy on ten sites RD-40
found correct; the batch declines to move code it cannot show a
behavioral reason to move.

## D-3 — the terminal verdict is the record's own last verdict line, over raw bytes, in the predicate's shape (RD40-01, BLOCKING)

The rule is computed over the **raw** record bytes, and now asks the
predicate rather than comparing two strings. Three outcomes, each an
error rather than a resolution:

- **A quotation after the record's own terminal line** — blockquote,
  indented block, list item, prose — is an **ambiguity error**. The
  record errors, no earlier line is parsed in its place, and the trend
  verdict column is blank. (At v1.12, all four resolved silently to the
  quotation.)
- **Every `GATE VERDICT:` line in the record is a quotation** — the
  record is refused **by name**: *"a quoted verdict is not the record's
  verdict"*. The rule no longer reaches for the last quotation as a
  fallback.
- **The record's own terminal line does not survive the strip**
  (fenced, commented) — the v1.12 laundering error, unchanged, and
  re-verified.

Survival is judged by the line's **raw index**, not by string identity,
so an inline HTML comment appended to an otherwise lawful terminal line
is lawful rather than reported as hidden (RD40-06 — the v1.12 message
misdescribed its own cause).

*Re-executed* at the named commit, git checks on, real digests, full
39-row roster: the four quoted-after-terminal carriers score **1 error
each**, trend verdict blank; the all-quoted record scores 1 error; the
fenced and HTML-comment carriers still score 1 error each; and the
control — a lawful record whose own terminal reads `NOT READY` with no
quotation — scores **0 errors** and reports `NOT READY`.

## D-4 — presence is the predicate, not an anchor with a decoration allowance (RD40-02, BLOCKING)

The six `Label:` presence tokens are read over the predicate's own-line
text. Whitespace normalization and the bold allowance are kept; **the
list-marker allowance is removed**.

**This reverses a v1.12 acceptance, deliberately.** At v1.12,
`- Operationalization notes:` satisfied presence as lawful decoration
(RD39-07); at v1.13 it does not, because that decoration *is* the
quotation carrier. RD-40's diagnosis is adopted verbatim: *"presence and
lawful-decoration are two requirements that were merged into one
regex."* The v1.12 fixture asserting the acceptance is **flipped in
place**, with the reversal named in the fixture's own label so no reader
mistakes it for a repair of a bug.

The banner gets the single-level test its own form implies: `> ` yes,
`> > ` no. `<details>`-wrapped fields and setext-heading labels are
refused. LG-4's G1 anchor reads the same own-line text.

**Mutation, with the qualification measured rather than buried.** The
list refusal is carried **twice** — once by the predicate (a
list-marked line is not own) and once by the presence pattern (no
marker allowance). Reverting either layer alone fails **0** fixtures;
only the combined revert to v1.12's exact configuration fails **2** (the
flipped `- Operationalization notes:` fixture and the bullet-list
`Materials given:` quotation). The combined revert is the behavioral
witness; the redundancy is defense in depth, not two proofs, and this
record declines to report it as two.

*Re-executed*: RD-40's full composite — banner, `Reviewer:`, `Reviewer
model family:`, `Materials given:`, `Operationalization notes:` and
`Reviewer's falsification notes:` deleted outright, the template carried
as a bullet list, the banner nested-blockquoted, a column-0 `## G1`
heading in the appendix, terminal `READY FOR <the verbatim target>` —
scores **6 errors** (five `Label:` fields and the banner) where it
scored 0 at v1.12. The residual is stated at the end of this record.

## D-5 — tabs are expanded before every indentation measurement (RD40-03, MAJOR)

`ln.expandtabs(4)` precedes every indent measurement — the fence
opening test, the fence closing test, and the predicate's ≤3-column
bound. CommonMark's bound is three columns, and a tab advances to the
next 4-column stop.

*Re-executed*, both decoy orderings, git on, real digests: the
tab-indented and four-space-indented records now score **identically** —
3 errors each with the decoy first (LG-5 disagreeing values, LG-7
uncited deferral, LG-6 *"a deferral-carrying pass is
READY-WITH-DEFERRALS, never plain READY FOR"*, `Deferred count` read as
3), 1 error each with the honest value first. At v1.12 the tab record
scored **0** where its space control scored 3.

## D-6 — the LG-11 version-disagreement fixture can fail again (RD40-04, MAJOR)

The `GOOD` template's `Instrument version:` literal was not bumped at
v1.12, so the fixture's **unmutated** baseline already emitted the
substring it asserts — the RD34-05 class, recurring inside the batch
that named it. The RD34-05 remedy is applied: `good_head` rewrites the
template's version to the committed instrument's own
`effective_version`, read from the blob at the named commit, and the
fixture mutates **by shape** to `v0.2`. The literal is bumped as well,
so the template and the decoy loop agree.

*Mutation*: removing the LG-11 version comparison fails **1** fixture —
the version-disagreement fixture itself. It can fail again.

## D-7 — the fence-close rule's rejection limb gets its fixture (RD40-05, MAJOR)

The RD39-06 closing-run rule shipped with an acceptance-limb fixture
only (a four-backtick fence not closed by three keeps its content
stripped). The rejection limb — a label between a four-backtick open and
a three-backtick non-close is stripped, so presence errors — is now
fixtured too.

*Mutation*: removing the closing-run length requirement fails **2**
fixtures, one per limb.

## D-8 — two minor repairs (RD40-06, RD40-07)

- The inline-comment case is lawful and says so (RD40-06, folded into
  D-3's raw-index survival test; mutation: judging survival by string
  identity fails 1 fixture).
- A dead row-verdict helper is deleted, and the comment naming the
  **one** row normalization now sits at the loop that owns it, where
  RD33-02's one-normalization rule can be checked against the code
  rather than against a helper nothing called (RD40-07).

## What did not change

- **No section §1–§8 of the instrument changed** — verify per-section
  against `git show 7751f12:launch-gate-pre-specifications.md`
  (byte counts in the header above). The §8 parameter block hashes
  identically across the nine versions **v1.5–v1.13** — swept this
  session over every commit that touched the instrument, with the
  denominator stated: eleven distinct `effective_version:` values are
  reachable in history, three distinct §8 digests exist across them,
  and the current one is constant from v1.5 forward (v1.4 and its
  predecessor carried different parameter blocks). Recompute with the
  validator's own `param_block_bytes`, never from this record. The
  instrument bytes that move: the
  `effective_version:` header, the appended §9 v1.13 entry, and the two
  dated RD40-01/RD40-02 correction markers in the §9 v1.12 entry (D-1).
- **No frozen record is edited.** The frozen population, named
  explicitly, and swept with its denominator: **30** files match the
  frozen shapes under `round-2026-08e/` (the nine deltas v1.4–v1.12 and
  every `reviews/RD-*-RAW.md`); **28** are byte-identical to their state
  at `7751f12` and **2** are new at this commit — this delta and RD-40's
  raw review, which was delivered after `7751f12` and is frozen as
  stored (its storage digest is in the header above and in the delivery
  register). Zero are modified.
  The v1.12 delta's five false or misassigned claims are corrected by
  this delta's D-1, in the D-10 convention. The disposition register is
  a living record and takes its RD39-01 correction as a dated marker in
  place, its own convention.
- **No question weakened, no ID renumbered, no verdict word changed.**
- **Directionality, on three axes** (the RD39-04 restatement, with D-1
  item 4's misassignment not repeated — each direction below is stated
  as its own fixture measures it):
  *Newly rejected:* a verdict quoted after the record's own terminal
  line in any of four carriers, and a record whose every verdict line is
  a quotation (D-3, five fixtures); the bullet-list, setext-heading and
  `<details>` quotations of a declared field, the nested-blockquote
  banner, and the `<details>`-wrapped `## G1` (D-4, five fixtures); a
  label stranded between a four-backtick open and a three-backtick
  non-close (D-7, one fixture).
  *Newly accepted:* a terminal `NOT READY` between **tab**-indented
  backticks, which v1.12 deleted as fenced (D-5, one fixture); an
  inline HTML comment on an otherwise lawful terminal line (D-8, one
  fixture).
  *Same acceptance, changed verdict:* none this batch — the ambiguity
  cases move from *accepted with the quotation's verdict* to *rejected*,
  which is a rejection, not a re-verdict.
  *An acceptance withdrawn:* `- Operationalization notes:` satisfied
  presence at v1.12 and does not at v1.13 (D-4, fixture flipped in
  place). This is the only direction any consumer of the instrument
  loses, it is intentional, and it is the one change in this batch a
  reviewer should weigh as a cost rather than a repair.
  No case moves in the dishonest direction — no record reports READY
  where its own bytes say otherwise.

## Fixture arithmetic

132 → **145** (+13, one further fixture flipped in place rather than
added): +4 RD40-01 quoted-after-terminal carriers (blockquote, indented
block, list item, prose — one generated loop), +1 RD40-01 all-quoted
record, +1 RD40-06 inline comment on the terminal line, +1 RD40-03
tab-indented backticks, +5 RD40-02 container matrix (bullet-list
`Materials given:`, setext `Reviewer's falsification notes:`,
`<details>` `Reviewer model family:`, nested-blockquote banner,
`<details>` `## G1`), +1 RD40-05 fence-close rejection limb. The
RD39-07 list-marked acceptance fixture is **flipped**, not removed: same
subject, opposite expectation, the reversal named in its label.

Count read from the selftest's own printed output (`145 fixtures, 0
failing`). All LG-1…LG-13 checks still fire. **Ten mutation-reverts**,
each failing exactly the fixtures its repair added — denominators 4, 5,
2, 2, 1, 1, 1, 1, 1, 2 — plus the measured qualification at D-4: the
list refusal's two single-layer reverts fail 0 fixtures each and its
combined revert fails 2, so the batch claims **one** behavioral witness
there, not two.

## Disclosed limits and residuals, each measured

- **LG-4 is satisfied by a column-0 `## G1` heading wherever it sits,
  and however empty the section beneath it.** That heading is
  structurally the record's own, so this is an *emptiness* question, not
  a quotation question, and the predicate is the wrong instrument for
  it. Measured: RD-40's composite scores **6** errors with the heading
  present and **7** without, so the residual opens no pass — it costs
  one error of the seven. Left to a later batch, which would need §4's
  *"an administration missing G1 is incomplete"* read as a content
  requirement with its own fixture matrix.
- **An asymmetric `**Label:*` still satisfies presence** (RD40's minor
  finding, carried forward).
- **The trend row is still printed above the error list, carrying the
  record's *claimed* verdict, when the record is invalid** (carried
  forward). No trend log ever receives it — the record errors — but a
  reader skimming output sees a verdict beside a failed record.
- **The honest cap on the prior guard is unchanged** from v1.12: a
  forged but fully lawful-shaped prior naming a real commit remains
  representable. The guard raises the bar to the full lawful shape at
  the prior's own anchors and claims no impossibility.
