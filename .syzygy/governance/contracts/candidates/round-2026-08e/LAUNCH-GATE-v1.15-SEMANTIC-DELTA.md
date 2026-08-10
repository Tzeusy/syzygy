# Launch-gate v1.14 → v1.15 — semantic delta record

> **Process record for a candidate instrument amendment.** The instrument
> (`launch-gate-pre-specifications.md`, repo root) is a process-policy
> candidate, never authority. This delta records every change of meaning so
> "no question was weakened" stays a reviewable claim. Owner approval of
> v1.15 is prepared, not performed:
> `.syzygy/governance/decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` (P-34) —
> and the offer waits on a fresh-context re-review of this delta
> (**RD-43**), because the session that authored these bytes may not
> confirm them.

Baseline: v1.14 as reviewed by RD-42 (subject sha256
`bd070a28cc561dfd1fa62c525cb2ae0c3a10f06b848be9b953c4c094896e355e` at
commit `47adfa9`; validator sha256
`e861ec38564042caf51bcd42536a0694690d1232f46c9085ecfdb7715eeb9c20`; raw
review `reviews/RD-42-instrument-v114-RAW.md`, storage digest
`3ca204d8b6019ba37a647550d40ad48e4c9e2a2a46c8778173a1d772d0d287ae`,
`VERDICT: REVISE`, 6 BLOCKING / 3 MAJOR / 4 MINOR). RD-42 verified all
twelve RD-41 findings present, reproduced the 168-fixture arithmetic and
its itemization, constructed all sixteen mutation-reverts from the
delta's own descriptions and measured each, confirmed the §1–§8
per-section identity and the frozen population — and then ran **every
captured fixture through both validators on identical bytes**, which is
how three of this round's findings were found rather than argued. Every
delta below closes an RD-42 finding; dispositions in
`reviews/DISPOSITION-REGISTER.md`. **This is a validator-and-records
batch an eighth time: no question block, no verdict word, and no section
§1–§8 of the instrument changed** (verified per-section against
`git show 47adfa9:launch-gate-pre-specifications.md` — §1 794, §2 4388,
§3 15377, §4 5688, §5 3601, §6 2192, §7 1038, §8 6610 bytes, each
identical; the §8 parameter-block digest is recomputed with the
validator's own `param_block_bytes`, never transcribed here). The
instrument bytes that move: the `effective_version:` header, the
appended §9 v1.15 entry, and **five** dated correction markers in the §9
v1.14 entry (D-1 names them, and the count is read from the bytes with a
pattern that tolerates the marker's line wrap — 5 in the v1.14 entry and
5 in the v1.13 entry, where a one-line pattern reports 4 and 3 — not from
the list of findings that motivated them, which is RD42-05's exact
failure).
Validator changes carry fixtures (`scripts/launch_gate_results.py
--selftest`, **187 fixtures** — the count read from the selftest's own
printed output); **thirteen** mutation-reverts, of which **twelve** fail
exactly the fixtures their repair added and **one** fails nothing,
disclosed as such at D-8 rather than counted as proven.

RD-42's finding, adopted whole: the batch that replaced enumeration with
state **kept an enumeration**. v1.14's predicate carried a block stack
for blockquotes, list items and indentation, and for raw HTML it carried
a counter over two tag names. *"A container is a region, not a line"* was
answered for markdown's containers and left unanswered for HTML's, which
is the same question the chain has now answered inconsistently six times
(RD-38 → RD-39 → RD-40 → RD-41 → RD-42). Like its eight predecessors,
this record predicts nothing about whether the batch is the last.

## D-1 — corrections of the frozen v1.14 delta and the §9 v1.14 entry (the frozen record is not edited)

Seven claims in the v1.14 delta are false of the bytes it described. Per
the D-10 convention the frozen record is **not** edited; five of the
seven also appear inside §9 — the bytes an approval digest binds — and
carry dated correction markers in place (the
RD36-01/RD38-02/RD39-02/RD40-01/RD41-01 precedent).

| # | frozen claim | corrected | in §9 too? |
|---|---|---|---|
| 1 | the predicate's third container is a *"raw-HTML block"* | It was a counter over the two tag names `<details>` and `<summary>`, decrementable by an inline code span. Four other carriers (`<div style="display:none">`, `<p style="display:none">`, `<span hidden>`, `<table><tr><td>`) passed a declared field through it, and a `` `</details>` `` code span reopened the element it named. (RD42-01) | yes — marker on "raw-HTML block" |
| 2 | *"All ten `_decl` sites read the record's **own** lines"* | Nine did. `Parameter block sha256:` — §2's integrity anchor — read the full active text, so it could be supplied from collapsed content **below** the terminal verdict, and the record was then refused for a digest *mismatch* it did not have. (RD42-03) | yes — marker on "**`_decl` becomes a consumer**" |
| 3 | *"sixteen mutation-reverts, **fourteen** of which fail exactly the fixtures their repair added"* | Thirteen witness. D-7's revert — the raw-side predicate call — fails **0 of 168**, a third unwitnessed repair beside the two the entry already disclosed. (RD42-04) | yes — marker on "fourteen" |
| 4 | *"**four** dated correction markers in the v1.13 entry"* | Five: RD41-01, RD41-06, RD41-02, RD41-03, RD41-04. The number was written from the four findings the sentence then names and never recounted against the bytes. (RD42-05) | yes — marker on "four" |
| 5 | *Newly accepted:* three `<details>`-related records *"(each 1 → 0) — four lawful records the v1.13 raw-side call refused"* | Three of the four measure **0 → 0** on their own fixture bytes: they were written *below* the terminal verdict, where v1.14's own new rule already refuses to read anything, so they witnessed that rule and not this repair. Only the `---` case moved 1 → 0. (RD42-06) | yes — marker on "four further lawful records restored" |
| 6 | the *Movement* axis lists the setext change as a directionality entry | It belongs with #5: measured on the shipped fixture bytes it did not move. (RD42-06) | no |
| 7 | a nit recorded as *"6 errors, was 0"* without a stated construction | Unverifiable as written; a reader cannot reproduce it. Withdrawn rather than restated. (RD42-10) | no |

Two things this table is careful about, because the same care was
missing last round. Every "corrected" cell is a **measurement of the
frozen bytes**, made by running the v1.14 validator against the fixture's
own construction — not a re-reading of the v1.14 delta's prose. And #5's
underlying repair is real: it now has a witness (D-4 below), which is a
different claim from the one the frozen record made.

## D-2 — a raw-HTML region is element nesting, not a tag list (RD42-01, BLOCKING)

**Before.** `html_depth` incremented on `<details`/`<summary` anywhere in
a line and decremented on `</details>`/`</summary>`, floor 0.

**After.** The predicate carries `html_stack`, and the decision is the
one a reader makes:

- a region **opens** at a line whose content *begins* with a tag of any
  name (`<div …>`, `<p …>`, `<span …>`, `<table>`, `<DETAILS>` — the name
  is folded to lower case);
- **inside** a region every tag on every line is read;
- a **close** tag pops back to the element it names, and pops **nothing**
  if it names none — so `<table><tr><td>` … `</td></tr></table>` closes
  where a reader sees it close;
- **code spans are removed before any tag is read**, so a `` `</details>` ``
  written as prose closes nothing;
- **self-closing** (`<div/>`) and **void** (`<br>`, `<img …>`, …) forms
  open nothing.

**Why this shape and not a stricter one.** A CommonMark HTML block ends
at a blank line, which is the wrong authority here: content after that
blank line is still *visually inside* the element a reader sees, and
hiding a declared field there is precisely the exploit. Element nesting
is the reader's model, so element nesting is the predicate's.

**Measured on the attack records** (validator run with git checks on,
against the real commit and the real digests; each row is one record):

| record | v1.14 | v1.15 |
|---|---|---|
| `<div style="display:none">` hiding `E3 reopen-list:` | 0 errors, trend `READY FOR …` | 1 error, `LG-12 no E3 reopen-list: field` |
| `<p style="display:none">` hiding it | 0 errors, `READY FOR …` | 1 error, same |
| `<span hidden>` hiding it | 0 errors, `READY FOR …` | 1 error, same |
| `<table><tr><td>` hiding it | 0 errors, `READY FOR …` | 1 error, same |
| `<details>` reopened by a `` `</details>` `` code span | 0 errors, `READY FOR …` | 2 errors, `LG-6` + `LG-12` |
| *control:* the v1.14-closed `<details><summary>` carrier | 1 error | 1 error |

## D-3 — the tenth `_decl` site (RD42-03, BLOCKING)

`Parameter block sha256:` now reads `_own_text` like the other nine. The
call sites were **enumerated mechanically** this time, by parsing each
`_decl(` occurrence's second argument rather than reading the file:
**11 occurrences — one is the `def _decl(pattern, txt, …)` definition,
and all ten call sites pass `_own_text`.** The denominator is stated
with its method because "all ten" was last round's false claim, and
counting by eye is how it became false.

| record | v1.14 | v1.15 |
|---|---|---|
| `Parameter block sha256:` present only inside `<div>` below the terminal verdict | 1 error: `LG-2 parameter-block digest mismatch` (an accusation untrue of the record) | 1 error: `LG-1 no parameter-block sha256 recorded` (true of it) |

The error **count** does not move; the error does. A movement table that
counted errors alone would have called this repair inert, which is the
mistake D-1 #5 records.

## D-4 — the RD41-06 restoration fixtures acquire witnesses (RD42-06, BLOCKING)

The three `<details>`-related fixtures are rebuilt **above** the
terminal verdict (the fourth tests a `---` *after* the verdict and
belongs where it is). Both underlying repairs are now witnessed by a
mutation-revert rather than asserted:

| revert | fixtures failed |
|---|---|
| the raw-side predicate call reads un-stripped text again (v1.13's D-7) | **1** — the fenced `<details>` example |
| the setext requirement is applied to the terminal-verdict rule again (v1.13's shape) | **1** — the `---` after the terminal verdict |

Both failed **0 of 168** at v1.14.

## D-5 — LG-4 stops measuring §5's trailer (RD42-07, MAJOR)

§5's template places seven declared fields between `## G1` and the
verdict with **no heading after**, so v1.14's new emptiness requirement
counted the trailer as G1 content and fired only for records that
reorder the template. The G1 section's content now excludes lines that
begin with a §5 declared label.

| record | v1.14 | v1.15 |
|---|---|---|
| bare `## G1 — completeness critic` in §5's own position | **0 errors**, trend `READY FOR …` | 1 error, `LG-4 … opens an EMPTY section` |
| *control:* lawful G1 with content | 0 errors | 0 errors |

## D-6 — one heading regex, requiring the space CommonMark requires (RD42-11, MINOR)

`###G1` is not an ATX heading. Two near-duplicate patterns became one
`_G1_HEADING_RE` (`#{1,6}` + at least one space + `G1`) and one `_ATX_RE`
for "the next heading".

| record | v1.14 | v1.15 |
|---|---|---|
| `###G1 was considered elsewhere.` standing in for the section | 1 error: `LG-4 … opens an EMPTY section` (it was accepted as the heading) | 1 error: `LG-4 no G1 section` |

Same count, different — and now true — message. Recorded here for the
same reason as D-3.

## D-7 — the placeholder message says what it matched (RD42-08, MAJOR)

The rule keeps its shape: a value written entirely inside angle brackets
has not been answered. The **message** no longer claims the value is
§5's own placeholder text, which it need not be; it now names the shape
it matched and tells the writer how to comply.

Matching §5's literal placeholder strings instead was **considered and
rejected by measurement**: the working exploit abbreviates the template
it quotes (`<alternate families across administrations>` against §5's
two-line placeholder), so a literal match would reopen RD41-01's last
limb. The in-code comment records that trade-off beside the pattern.

| record | v1.14 | v1.15 |
|---|---|---|
| `Materials given: <redacted>` | 1 error claiming the value *is* §5's placeholder | 1 error naming the shape: *"written entirely inside angle brackets, which is §5's template form and not an answer … If this is a real answer, write it without the enclosing brackets"* |

## D-8 — one clause with no single-layer witness, disclosed rather than counted (RD42-04's class)

| clause | reverted alone | why |
|---|---|---|
| raw-HTML **line classification** (a line whose own content begins with a tag is not the record's own text) | **0 of 187** | every declared value is read `^`-anchored, and the verdict-token scan counts raw lines — so a one-line carrier such as `<div hidden>E3 reopen-list: empty</div>` is already refused by anchoring |
| predicate: tab expansion (from v1.14) | **0** | carried forward, unchanged |
| predicate: `≤3 columns` (from v1.14) | **0** | carried forward, unchanged |

The classification is kept as defence in depth and **counted as
unproven**. The fixture that exercises the one-line carrier is labelled
for the rule it does witness (the element-nesting rule, m2), not for
this one — the two-layer trap RD-42 found in three of last round's
fixtures.

## What did not change

No question in §3 changed text, weight or verdict vocabulary. §4's
conjunctive READY rule, §5's record template, §6's trend row, §7's
generalization ban and §8's parameter block are byte-identical. No
identifier was renumbered or retired. The instrument still answers
`NOT READY` on the repository as it stands, and this batch does not
touch that answer.

## Fixture arithmetic

168 (v1.14) + 19 = **187**, the count read from the selftest's printed
output and reconciled against the new fixture block:

| block | new fixtures |
|---|---|
| five HTML carriers hiding `E3 reopen-list:` (D-2) | 5 |
| one-line carrier; closed-`<details>` appendix accepted; self-closing; void (D-2) | 4 |
| code span cannot close; close tag never pops what it did not push (D-2) | 2 |
| the laundered verdict below the visible one (D-2's LG-6 consequence) | 1 |
| hidden `Parameter block sha256:` (D-3) | 1 |
| bare `## G1` in §5's shape (D-5) | 1 |
| angle-bracket value refused with a true message (D-7) | 1 |
| `<details>` in prose / in a code span / in a table cell — accepting direction (D-2) | 3 |
| `###G1` is not a heading (D-6) | 1 |

5+4+2+1+1+1+1+3+1 = 19.

## Mutation-reverts

Thirteen, each rebuilt from the **final** v1.15 source and each measured
by reading the selftest's printed FAIL lines against a denominator of
187:

| revert | fixtures failed |
|---|---|
| m1 — the whole HTML limb back to v1.14's two-tag-name counter | 10 |
| m2 — element nesting back to line-initial open / top-of-stack close | 3 |
| m3 — code spans not stripped before tags are read | 2 |
| m4 — a raw-HTML line is the record's own text again | **0** (disclosed at D-8) |
| m5 — a tag anywhere on a line opens a region | 3 |
| m6 — the tenth `_decl` site reads raw text | 1 |
| m7 — declared trailer fields count as G1 content | 1 |
| m8 — the G1 heading regex drops the required space | 1 |
| m9 — the raw-side predicate call reads un-stripped text | 1 |
| m10 — the setext requirement applied to the terminal rule | 1 |
| m11 — HTML comments not stripped | 2 |
| m12 — self-closing tags open a region | 1 |
| m13 — the void-element set emptied | 1 |

## Regression: the earlier attack records

All **37** stored attack records from the RD-39, RD-40 and RD-41 rounds
(21 + 12 + 4, across the three harnesses) were re-executed against v1.15
with git checks on and the real digests, and their output **diffed
against the same records run under the v1.14 validator**: all three
diffs are empty — no record's error count, error identity or trend
verdict moved. The three records this batch newly *accepts* are named in
D-2 and were refused by v1.14 with 8, 8 and 1 errors.

## Disclosed limits and residuals, each measured, none generalized

1. **The raw-HTML line classification has no single-layer witness** —
   D-8, measured 0 of 187.
2. **A record line whose own text begins with an inline tag is read as
   raw HTML** and cannot carry a declaration. §5's fields begin with
   their labels; no fixture in the corpus is affected. This is the price
   of using "begins with a tag" as the region trigger, and it is paid in
   the refusing direction.
3. **Blockquote laziness is still deliberately not implemented**, for
   the §5-template reason stated at v1.14 and re-verified here.
4. **§5's non-authority banner can still be satisfied by a quotation of
   the banner in an appendix** (RD42-12, carried forward). The banner is
   the one line whose quotation is indistinguishable from its assertion;
   closing it would require §5 to define a marker it does not define.
5. **The depth scan is quadratic in nesting depth** on adversarial input
   (RD42-13, carried forward). Records are short and the scan is
   read-only.
6. **An asymmetric `**Label:*` still satisfies presence**, and the trend
   row is still printed above the error list carrying the record's
   *claimed* verdict when the record is invalid — both carried forward.

## Where the attack records live

Every record cited above is stored as a fixture in
`scripts/launch_gate_results.py --selftest`, so the numbers a reviewer
is asked to check are checkable from the repository alone — the RD-42
nit accepted in the disposition register. The one exception is the
regression diff, which compares two validator versions and is therefore
reproducible from `git show 47adfa9:scripts/launch_gate_results.py`
against the current file.
