# Launch-gate v1.13 → v1.14 — semantic delta record

> **Process record for a candidate instrument amendment.** The instrument
> (`launch-gate-pre-specifications.md`, repo root) is a process-policy
> candidate, never authority. This delta records every change of meaning so
> "no question was weakened" stays a reviewable claim. Owner approval of
> v1.14 is prepared, not performed:
> `.syzygy/governance/decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` (P-34) —
> and the offer waits on a fresh-context re-review of this delta
> (**RD-42**), because the session that authored these bytes may not
> confirm them.

Baseline: v1.13 as re-reviewed by RD-41 (subject sha256
`025d07c44fad4199c3762c6e6bb3f4061e74c9945d019bacab2113c0972d5162` at
commit `619093b`; validator sha256
`e0a0653e69c75af6f09e2677754c0168692d96e0072f625524aaec78106f5a78`; raw
review `reviews/RD-41-instrument-v113-RAW.md`, storage digest
`2d01263430025b8c76b6d118aa993c322895106f4a63b1cb3c087f40e5026acd`,
`VERDICT: REVISE`, 4 BLOCKING / 4 MAJOR / 4 MINOR). RD-41 verified every
one of RD-40's eight findings present with six closed outright — RD40-01
*"genuinely, structurally closed"* in the reviewer's own words —
reproduced **all ten** mutation denominators, the 145 fixture
arithmetic and its itemization, the §1–§8 per-section identity at
denominator 10, the §8 constancy across nine versions, the 30/28/0/2
frozen population and a 373-file version sweep, and confirmed that the
disclosed D-4 redundancy was honestly refused as a second witness. Then
it broke the batch's central claim one level up. Every delta below
closes an RD-41 finding; dispositions in
`reviews/DISPOSITION-REGISTER.md`. **This is a validator-and-records
batch a seventh time: no question block, no verdict word, and no section
§1–§8 of the instrument changed** (verified per-section against
`git show ec7bdc4:launch-gate-pre-specifications.md` — §1 794, §2 4388,
§3 15377, §4 5688, §5 3601, §6 2192, §7 1038, §8 6610 bytes, each
identical; the §8 parameter block digest is recomputed with the
validator's own `param_block_bytes`, never transcribed here). The
instrument bytes that move: the `effective_version:` header, the
appended §9 v1.14 entry, and four dated correction markers in the §9
v1.13 entry (D-1 names them). Validator changes carry fixtures
(`scripts/launch_gate_results.py --selftest`, **168 fixtures** — the
count read from the selftest's own printed output); **sixteen**
mutation-reverts, of which **fourteen** fail exactly the fixtures their
repair added and **two** fail nothing, disclosed as such at D-8 rather
than counted as proven.

RD-41's prescription, adopted whole: **the predicate must carry state.**
*"'Is this line the record's own?' is not answerable from the line; it
is answerable only from the block stack — which containers are open at
this line, and at what column."* RD-40 asked the batch to enumerate the
question rather than the carriers; v1.13 enumerated the **containers**,
in a table of nine rows, each checked against the line that opens it.
But a container is a **region**, not a line. Like its seven
predecessors, this record predicts nothing about whether the batch is
the last.

## D-1 — corrections of the frozen v1.13 delta and the §9 v1.13 entry (the frozen record is not edited)

Six claims are false or misassigned. Per the D-10 convention the frozen
record is not edited; four of the six also appear inside §9 — the bytes
an approval digest binds — and carry dated correction markers in place
(the RD36-01/RD38-02/RD39-02/RD40-01 precedent).

1. **The predicate's own definition** — §9's *"carries no list marker of
   any kind (`-`, `*`, `+`, ordered)"* and D-2's table row *"list item …
   **at any depth**"*: **false** (RD41-01). The classifier was
   line-local. It refused the line that *carried* a marker and said
   nothing about the item's continuation lines, which carry none and sit
   at ≤3 columns. RD-38's composite reproduced **whole** — banner, five
   declared fields and the completeness critic deleted, the template
   quoted as list-item continuation — at **0 errors**, `record valid`,
   `READY FOR <the verbatim target>`; blockquote lazy continuation and a
   `> ` banner nested inside a list item did the same. Closed at D-2.
2. **The `_decl` scope sentence** — *"every quotation carrier either
   fails the anchor outright or produces a loud disagreement error … a
   stated scope decision, not an omission"*, and D-2's *"never a silent
   substitution"*: **false** (RD41-02). `<details>` blocks and setext
   heading text both reach column 0, and where a record declared the
   field nowhere else there was no disagreement to be loud about — the
   quotation silently *became* the value. Four constructions measured at
   0 errors, including a record whose reopen items are visible prose
   while `E3 reopen-list: empty` hides in collapsed content, and one
   whose owner deferral citation is invisible to the reader. Closed at
   D-3.
3. **"eight mutation-reverts"** in the §9 v1.13 entry: **false**
   (RD41-03). Ten is the measured figure and the figure the v1.13 delta,
   P-34, PROJECT-STATUS and the disposition register all state; "eight"
   was carried over from the v1.11 entry. Verification rule 3's own case
   — a derived value quoted outside its owning artifact went stale
   silently — inside the one artifact whose bytes a digest binds.
4. **The LG-4 residual's generalization** — *"it opens no pass"*:
   **false** (RD41-04). The parenthetical (6 errors with the heading, 7
   without) reproduces exactly; the generalization does not. The
   residual was a load-bearing limb of RD41-01's **0-error** pass, and
   it was wider than disclosed: LG-4's `\s*` crossed the newline, so a
   bare `###` followed by any own line beginning `G1 ` satisfied the
   anchor with no G1 heading at all — RD37-03's class returning through
   a door nobody checked. Closed at D-5. **This is the third batch
   running whose disclosed limit was true narrowly and false as
   stated.** The *Disclosed limits and residuals* section below states
   this batch's limits as measurements and nothing wider.
5. **The directionality statement's D-7 assignment**: **misassigned**
   (RD41-05) — and misassigned under this delta's own explicit promise
   *"with D-1 item 4's misassignment not repeated"*. The fence-close
   fixture's subject scores 1 error at v1.12 and 1 at v1.13: newly
   **fixtured**, not newly rejected, which is what D-7's own prose said.
   Every axis entry below states the v→v comparison it ran.
6. **"the only direction any consumer of the instrument loses"**:
   **false** (RD41-07). Five further acceptances were withdrawn at
   v1.13, four of them bugs (D-4) and one lawful (a record whose only
   verdict line is blockquoted). This delta enumerates every withdrawal
   it makes and claims no completeness it has not swept.

Also corrected: the v1.13 delta's *"eleven distinct `effective_version:`
values are reachable in history"* — there are **eleven commits** and
**ten** distinct declared values (v1.4…v1.13); the eleventh declares no
`effective_version:` key at all (RD41-12). The surrounding figures —
three distinct §8 digests, constant from v1.5 forward — were exact.

## D-2 — the predicate carries the block stack (RD41-01, BLOCKING)

`_own_flags` is now CommonMark's block-structure phase in the subset
this instrument needs. For each line it maintains the stack of
containers open at it — blockquote at any depth, list item at its
content column, raw-HTML block — matching open containers against the
line's markers, applying **lazy continuation**, then opening whatever
the remainder starts. A line is the record's **own** iff the stack is
empty; **bq1** iff the stack is exactly one blockquote (§5's banner
form, so a nested `> >` still fails).

Three decisions this repair had to make, each stated rather than
assumed:

- **Blockquote laziness is deliberately not implemented, and §5 is the
  reason.** §5's own frozen template places the declared fields on
  unmarked lines *directly beneath* the blockquote banner, with no blank
  line. Strict CommonMark laziness makes those fields blockquote
  content — which would refuse every lawful record, that template first.
  Measured: the mutant that applies laziness to blockquotes fails **43
  of 168** fixtures, starting with *"well-formed full-template record
  validates"*. A blockquote therefore ends at the first line not
  carrying its marker. The limit that leaves is **fixtured in its
  accepting direction** (`unmarked lines under a blockquote are the
  record's own — §5's template form, fixtured as the limit it is`), so
  it is a measured behaviour of this validator rather than a sentence
  about one.
- **Setext headings leave the predicate** — see D-4.
- **The predicate is computed once, over the stripped lines**, and the
  terminal rule maps back by raw index — so §9's "after the fence and
  HTML-comment strip" is true of every consumer, which at v1.13 it was
  not (D-4).

*Re-executed* at the named commit, git on, real digests, full 39-row
roster: RD-41's list-item-continuation composite scores **6 errors**
where it scored 0; its blockquote-continuation composite **6**; the
banner nested inside a list item **1**. v1.13's own container matrix
does not regress (the bullet-list composite moves 6 → **7**, gaining
LG-4).

*Mutations:* laziness disabled → **1** (the lazy-continuation fixture);
the list container removed from the stack → **3**; `bq1` widened to any
blockquote depth → **1**; raw-HTML depth tracking removed → **5**;
blockquote laziness enabled → **43**.

## D-3 — `_decl` becomes a consumer, and two rules close what containment cannot (RD41-02, BLOCKING; RD41-01's last limb)

All ten `_decl` sites read the record's **own** lines: a declared value
carried only on non-own lines is an **absent field**, never a supplied
one. The loud-disagreement behaviour on own-line shadowing is unchanged,
and the internal inconsistency RD-41 named — `Unknowns and what would
settle them:` inside `<details>` erroring while `E3 reopen-list:` inside
`<details>` supplied a value — is gone, because both now ask one
question.

Containment alone cannot finish the job, and this delta says why rather
than hoping. **At column 0, unmarked, above the verdict, a quotation of
a §5 field *is* a declaration of it** — §5 defines no marker that would
tell the two apart, and its template puts the fields in exactly that
position. Two further rules close the gap on properties a quotation
cannot shed:

- **Position.** A declaration is read only from own lines at or above
  the record's own terminal verdict line. §5 places every declared field
  there, and the verdict is terminal — an appendix below it declares
  nothing, in any container.
- **Value.** A field whose declared value is a bare angle-bracket
  placeholder (`<model/version or human, fresh context: yes/no>`) has
  not been answered. This is a **value-quality** check, kept explicitly
  separate from the containment one — the merge of two requirements into
  one regex is what RD-40 diagnosed and what this chain keeps paying
  for. Its accepting direction is fixtured: a value that merely
  *contains* angle brackets is not a placeholder.

*Re-executed:* `E3 reopen-list:` carried only in `<details>` → the field
is absent (1 error) where it validated at 0; the same as setext text →
absent; `Deferred count:` in `<details>` → absent; an
`Owner deferral decision:` in `<details>` under `READY-WITH-DEFERRALS` →
**2 errors**, the deferral unlicensed. A template quoted at column 0
above the verdict → **5 placeholder errors**. A field declared below the
verdict → absent.

*Mutations:* every `_decl` site reverted to the full active text →
**5**; the position rule removed → **1**; the placeholder rule removed →
**1**.

## D-4 — setext leaves the predicate; the raw side reads stripped text; the message names its cause (RD41-06, MAJOR)

Three defects with one shape: a repair specified over containment was
applied to things that are not containment, and to text the strip had
not touched.

- A **setext heading is the record's own visible text**, not a quotation
  of it. It is now a separate declaration-form requirement
  (`_is_setext_text`) consumed by the field reads, the banner and LG-4 —
  and **not** by the terminal-verdict rule, where v1.13's version made a
  `---` under the verdict hide the decisive line. Refusing a setext
  *field* line is kept, and the reason is symmetry: an ATX heading
  (`## Materials given:`) never satisfied a presence read either.
- The raw-side predicate call ran on **un-stripped** text where §9 said
  "after the fence and HTML-comment strip". There is now one call, over
  the stripped lines, mapped back by raw index.
- LG-6's all-quoted message enumerated five causes and could be emitted
  when none was true of the record. It now reports the carrier each
  verdict line actually sits in, computed from the same predicate that
  refused it.

*Re-executed*, each measured v1.13 → v1.14 on identical bytes: a fenced
`<details>` example **1 → 0**; a self-closing `<details/>` in prose
**1 → 0**; a comment mentioning `<details>` **1 → 0**; `---` after the
terminal verdict **1 → 0**. The fifth (`Materials given:` followed by
`---`) stays refused, deliberately, for the ATX symmetry above — and it
is listed as a withdrawal at D-9, not hidden.

*Mutations:* setext folded back into the containment predicate → **1**;
setext dropped from the declaration-form requirement → **3**.

## D-5 — LG-4 requires a section, and its anchor stops crossing the newline (RD41-04, BLOCKING)

The G1 anchor is matched **per line**, so `\s*` can no longer bridge a
bare `###` to a following `G1 …` paragraph; and the heading must open a
**non-empty** section — own content before the next heading, with the
record's terminal verdict never counting as content. §4's clause is
quoted in the error: *"an administration missing G1 is incomplete and
cannot support a gate decision."* A heading with nothing beneath it is a
missing section.

*Re-executed:* the bare-`###` construction → `no G1 section`; a `## G1`
opening nothing → refused; a lawful G1 section → 0 errors.

*Mutations:* the anchor reverted to the joined-text `\s*` search → **1**;
the emptiness requirement removed → **1**.

## D-6 — unicode whitespace is folded before the token search (RD41-08, MAJOR)

`_gv_all` selected verdict lines by the literal substring
`GATE VERDICT:`. A non-breaking space inside the token renders
identically for a human reader and matched nothing, so a record whose
**visible final line** read `GATE VERDICT: NOT READY` was reported as
the earlier `READY FOR <the verbatim target>` it also carried — 0
errors, the wrong verdict in the trend row. Unicode whitespace
(` `, ` `, ` `–` `, ` `, ` `, `　`) is
folded to ASCII spaces before the search and before the verdict is
parsed. Pre-existing, not a v1.13 regression; taken now because it is
the disagreement between a record's bytes and a reader's eyes that this
whole instrument exists to prevent.

The fixture is **behavioural, not string-matching**: the record carries
`F2 | Not met`, which refuses READY, so reading the hidden line fires
§4's conjunct and reading the visible one fires nothing. *Mutation:* the
fold removed → **1**.

## D-7 — the LG-1 commit-existence fixture can fail again (RD41-11, MINOR)

Built from a real commit and mutated to `f`*40. The v1.13 form mutated
the template record, whose placeholder sha is `0`*40 and does not exist
either, so the unmutated baseline already emitted the asserted
substring — the RD40-04 class with one instance left, found by a sweep
of all 139 `case()` fixtures. *Mutation:* the fixture rebuilt on the
v1.13 shape → **1** (it cannot fail).

## D-8 — two clauses with no single-layer witness, disclosed rather than counted (RD41-10, MINOR)

RD-41's question was whether the v1.13 batch's one disclosed redundancy
was the only place redundancy hid a missing witness. It was not: three
clauses failed 0 of 145. Measured again at v1.14, against 168:

| clause | reverted alone | why |
|---|---|---|
| predicate: tab expansion | **0** | every consumer either requires `bq1` or carries its own `^ {0,3}` anchor, and a tab is not a space |
| predicate: `≤3 columns` | **0** | same |
| `_label_present`'s `^ {0,3}` | **0** | carried by the predicate |
| list-marker refusal (from v1.13) | **0** each layer, **2** combined | carried twice, disclosed at v1.13's D-4 |

Two guard fixtures were added for the tab and indent limbs and are
**labelled as defence-in-depth guards, not single-layer witnesses**,
because that is what measurement says they are. This delta therefore
claims **fourteen** mutation-witnessed repairs of sixteen reverts, and
names the two that are not.

## What did not change

- **No section §1–§8 of the instrument changed** — verify per-section
  against `git show ec7bdc4:launch-gate-pre-specifications.md` (byte
  counts in the header above). The §8 parameter block is unchanged
  across the ten versions **v1.5–v1.14** (recompute with the
  validator's own `param_block_bytes`, never from this record); §1–§8
  together are unchanged across the eight versions **v1.7–v1.14**,
  seven amendments. Both figures swept this session over every commit
  that has touched the instrument.
- **No frozen record is edited.** The frozen population, swept with its
  denominator: **32** files match the frozen shapes under
  `round-2026-08e/` (the ten deltas v1.4–v1.13 and every
  `reviews/RD-*-RAW.md`, RD-41's included — it was stored verbatim and
  committed at `ec7bdc4` before any subject byte moved). **31** are
  byte-identical to their state at `ec7bdc4`, **1** is new at this
  commit (this delta), and **0** are modified. The v1.13 delta's six false or misassigned claims
  are corrected by D-1, in the D-10 convention. The disposition register
  is a living record and takes its RD40-05 correction as a dated marker
  in place, its own convention.
- **No question weakened, no ID renumbered, no verdict word changed.**
- **Directionality**, each entry stated from a measured v1.13 → v1.14
  comparison of the fixture's own bytes (D-1 item 5's misassignment not
  repeated — and this time the comparison, not the intent, is what is
  reported):
  *Newly rejected:* the list-item-continuation composite (6 errors, was
  0), the blockquote-continuation composite (6, was 0), the banner
  nested in a list item (1, was 0); `E3 reopen-list:`, `Deferred count:`
  and `Owner deferral decision:` carried only in `<details>` or as
  setext text (1/1/2, each was 0); a template quoted at column 0 above
  the verdict (5, was 0); a field declared below the verdict (1, was 0);
  a bare `###` bridged to a `G1 ` line (1, was 0); a `## G1` opening an
  empty section (1, was 0).
  *Newly accepted:* a fenced `<details>` example, a self-closing
  `<details/>` in prose, a comment mentioning `<details>`, and a `---`
  under the terminal verdict (each 1 → 0) — four lawful records the
  v1.13 raw-side call refused with a message untrue of them.
  *Same acceptance, changed verdict:* the NBSP record — accepted at both
  versions (0 errors), reporting `READY FOR <the verbatim target>` at
  v1.13 and the record's own visible `NOT READY` at v1.14. This is the
  axis RD39-04 added to the vocabulary, and it is where this batch's
  most dangerous defect lived.
  *Acceptances withdrawn:* the setext-underlined field line
  (`Materials given:` followed by `---`) stays refused for ATX symmetry;
  a template quoted with §5's placeholder values is now refused wherever
  it sits. Both are intentional, and both are costs a reviewer should
  weigh rather than repairs.
  No case moves in the dishonest direction.

## Fixture arithmetic

145 → **168** (+23, one fixture rebuilt in place): +2 RD41-01
continuation carriers (indented, lazy), +1 the §5 blockquote limit in
its accepting direction, +1 banner-in-list-item, +1 placeholder
rejection, +1 declaration-below-the-verdict, +1 placeholder accepting
direction, +4 RD41-02 `_decl` carriers (`E3 reopen-list:` and
`Deferred count:` × `<details>` and setext), +1 hidden owner deferral
citation, +2 RD41-04 LG-4 doors, +4 RD41-06 restored acceptances, +1
RD41-08 NBSP, +4 RD41-10 predicate-limb guards. The LG-1
commit-existence fixture is **rebuilt** on a real commit, not added.

Count read from the selftest's own printed output (`168 fixtures, 0
failing`). All LG-1…LG-13 checks still fire. **Sixteen mutation-reverts**
— denominators 1, 1, 1, 43, 5, 1, 1, 1, 1, 1, 5, 1, 3, 3 for the
fourteen that witness, and **0, 0** for the two disclosed at D-8.

## Disclosed limits and residuals, each measured, none generalized

- **Unmarked lines beneath any blockquote are the record's own.** Forced
  by §5's frozen template (D-2), fixtured in its accepting direction,
  and measured: enabling blockquote laziness instead fails 43 of 168
  fixtures. The exploit this would otherwise carry is closed by the
  position rule and the placeholder rule, each separately fixtured — but
  the *limit itself* is real, and closing it properly needs a §5
  amendment, which is an owner act and not a batch's to make.
- **Two predicate clauses have no single-layer witness** (D-8), measured
  at 0 of 168 each.
- **A setext-underlined field line is refused**, deliberately, for
  symmetry with ATX headings — a withdrawal, listed as one.
- **An asymmetric `**Label:*` still satisfies presence**, and **the
  trend row is still printed above the error list carrying the record's
  claimed verdict when the record is invalid**. Both carried forward
  from RD-40, unchanged and still disclosed.
- **The honest cap on the prior guard is unchanged**: a forged but fully
  lawful-shaped prior naming a real commit remains representable.
