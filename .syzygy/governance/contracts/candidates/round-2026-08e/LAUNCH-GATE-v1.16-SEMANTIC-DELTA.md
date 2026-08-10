# Launch-gate v1.15 → v1.16 — semantic delta record

> **Process record for a candidate instrument amendment.** The instrument
> (`launch-gate-pre-specifications.md`, repo root) is a process-policy
> candidate, never authority. This delta records every change of meaning so
> "no question was weakened" stays a reviewable claim. Owner approval of
> v1.16 is prepared, not performed:
> `.syzygy/governance/decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` (P-34) —
> and the offer waits on a fresh-context re-review of this delta
> (**RD-44**), because the session that authored these bytes may not
> confirm them.

Baseline: v1.15 as reviewed by RD-43 (subject sha256
`a3e5a4e711cccaceea7fa76e624a7909707ea68fe73d6d268fae4ee06faf0943` at
commit `4fd4a58`; validator sha256
`2606db6c30a51c5cd0aad03a92982406c15e9d58d6e58b9153eb11a505116e09`; raw
review `reviews/RD-43-instrument-v115-RAW.md`, storage digest
`c161cebff33ec328cc792317ab3fb2a26b99236240dd155cbb6a25562fd6ce7c`,
`VERDICT: REVISE`, 2 BLOCKING / 2 MAJOR / 3 MINOR). RD-43 verified all
thirteen RD-42 findings present — **eight closed outright**, two closed
for everything the finding constructed, one closed in its refusing
direction only, one partially, **one not closed** — reproduced the
fixture arithmetic by set difference of printed fixture names (exactly
19 new, 0 removed or renamed), reproduced twelve of thirteen mutation
denominators with the thirteenth at 0 exactly as disclosed, reproduced
both marker counts with and without a wrap-tolerant pattern, and
measured the git-skip hazard before running any mutant (**175 fixtures**
from a non-git directory — the twelve `_git=True` fixtures silently
absent). Every delta below closes an RD-43 finding; dispositions in
`reviews/DISPOSITION-REGISTER.md`. **This is a validator-and-records
batch a ninth time: no question block, no verdict word, and no section
§1–§8 of the instrument changed** (verified per-section against
`git show 4fd4a58:launch-gate-pre-specifications.md` — §1 794, §2 4388,
§3 15377, §4 5688, §5 3601, §6 2192, §7 1038, §8 6610 bytes, each
identical). The instrument bytes that move: the `effective_version:`
header, the appended §9 v1.16 entry, and **six** dated correction
markers in the §9 v1.15 entry (D-1 names them; counted over that entry's
span with the wrap-tolerant pattern RD42-05 made necessary). Validator
changes carry fixtures (`scripts/launch_gate_results.py --selftest`,
**205 fixtures** — the count read from the selftest's own printed
output); **twelve** mutation-reverts, **all twelve** failing exactly the
fixtures their repair added.

## The method changed, and it is the durable part of this batch

RD-43 settled every claim about what a reader sees by **rendering the
record** (`pandoc -f gfm` and `-f commonmark`) and **parsing the result
with an HTML5 parser**, then reading the DOM chain containing the field.
This batch adopts that as its rule, recorded in the disposition register:
a claim about a reader is a measurement of the rendered document, never a
reading of the CommonMark specification.

Applied, it did not merely confirm RD-43's four constructions. It also
falsified **two claims of this session's own** that no reviewer had
challenged — `<div/>` opens a `div` (HTML5 ignores the self-closing slash
on non-void elements), and the `<table><tr><td>` carrier does **not**
hide its field (it sits in a `td` a reader sees). Both are corrected
below. And it reversed one of RD-42's: an unescaped `<details>`
mid-sentence, which RD-42 measured lawful with `lxml.html`, is not
lawful under the algorithm browsers and GitHub implement.

`lxml.html` is libxml2's legacy HTML parser and disagrees with HTML5
about which elements close an open `<p>`. Two reviews and one repair
batch rested on that difference. Recorded here because the next batch
will be tempted to reach for whichever parser is installed.

## D-1 — corrections of the frozen v1.15 delta and the §9 v1.15 entry (the frozen record is not edited)

Per the D-10 convention the frozen record is **not** edited; six of the
seven also appear inside §9 — the bytes an approval digest binds — and
carry dated correction markers in place.

| # | frozen claim | corrected | in §9 too? |
|---|---|---|---|
| 1 | *"a close tag pops back to the element it names … so `<table><tr><td>` … closes **where a reader sees it close**"* | False in both directions, measured. It closed where a reader does **not** — an indented-code `</details>` and a backslash-escaped `\</details>` both render as literal text and leave the element open, and v1.15 popped on both. It failed to open where a reader **does** — a condition-6 element mid-sentence, and an opening tag split across two lines. (RD43-01) | yes |
| 2 | *"self-closing and void forms open nothing"* | True of void forms, false of self-closing ones: HTML5 ignores the slash on a non-void element, so `<div/>` opens a `div` and `<details/>` opens a `details`. Two v1.15 fixtures asserted the opposite and are flipped. (RD43-01, and this session's own error) | yes |
| 3 | *"three lawful records that v1.14 refused with 8, 8 and 1 errors now validate clean"* | Two of the three are lawful. The `<details>` named mid-sentence is not — it closes the paragraph and collapses everything below it. The acceptance is withdrawn at v1.16. (RD43-01, reversing RD42-09's first construction) | yes |
| 4 | the five carriers *"each hid a declared field from the reader"* | Four hid it; `<table><tr><td>` did not. The predicate refuses it anyway, and the reason is now stated as a choice rather than as harm prevented. (this session's own claim, caught by RD-43's method) | yes |
| 5 | LG-4's trailer exclusion, stated only in its refusing direction | The accepting direction was withdrawn in silence: G1 content written as a bulleted list, a numbered list, a blockquote, a fenced block or indented code was refused with *"opens an EMPTY section"*, a message untrue of the record. (RD43-04) | yes |
| 6 | the residual *"a record line whose own text begins with an inline tag … cannot carry a declaration; no fixture in the corpus is affected"* | Understated on two counts: the consequence is that **every line after it stops being the record's own**, terminal verdict included (a lawful record scored 8 errors); and the triggering shapes are autolinks and §5's own `<word …>` shorthand, which are not tags. "No fixture is affected" was true, and is VIS-2's own case — the corpus is the measurement, not the population. (RD43-03) | yes |
| 7 | *"All 37 stored attack records (21 + 12 + 4, across the three harnesses)"* | Not reproducible: no attack-record files exist in the repository and no partition of any fixture population yields 21 + 12 + 4. Replaced below by a sweep that is checkable, with its population named. (RD43-07) | no |

## D-2 — the block phase is decided first (RD43-01, BLOCKING)

**Before.** Tags were read out of every line, with code spans removed.

**After.** A tag can be read only out of text that survives markdown's
literal-text constructs. `_active_lines` already removed fences and HTML
comments; **indented code blocks** and **backslash escapes** join them,
because both render as literal text and neither closes an element.

| record | v1.15 | v1.16 |
|---|---|---|
| `</details>` written as an indented code block, field below | 0 errors, `READY FOR …` | 2 errors (`LG-6`, `LG-12`) |
| backslash-escaped `\</details>`, field below | 0 errors, `READY FOR …` | 2 errors (`LG-6`, `LG-12`) |

## D-3 — the region trigger is CommonMark's own start condition (RD43-01, BLOCKING)

**Before.** A region opened only at a line whose content *began* with a
tag.

**After.** CommonMark's HTML block **start condition 6** names the
elements that open a raw-HTML block from any position, including
interrupting a paragraph — and HTML5's "in body" insertion mode closes an
open `<p>` when it meets them. That list is quoted from the
specification, not chosen here. Condition 6 is also satisfied by an
opening tag whose `>` never arrives on the line (`<div` + newline).

Every other tag name is **condition 7**, which cannot interrupt a
paragraph: mid-sentence it renders as inline HTML and reaches only to the
end of its own paragraph. An inline element carries a declaration out of
sight only when it carries a **hiding attribute** (`hidden`,
`style="display:none"`, `aria-hidden="true"`) — which is what
`<span hidden>` uses, and what `<plus the parameter block>` does not.

| record | v1.15 | v1.16 |
|---|---|---|
| `… not an answer. <div style="display:none">`, field below | 0 errors, `READY FOR …` | 2 errors |
| `<div` / ` style="display:none">` split across two lines, field below | 0 errors, `READY FOR …` | 2 errors |
| `<div/>` then the field | 0 errors (field read) | 1 error — the field is inside a `div` the record opened |
| `<details/>` in prose | 0 errors | 1 error (`LG-6`) |
| `<details>` named mid-sentence, unescaped | 0 errors | 8 errors — **the withdrawn acceptance** |
| `` `<details>` `` in a code span *(control)* | 0 errors | 0 errors |
| `<details>` in a table cell *(control)* | 0 errors | 0 errors |
| `Materials given: … <plus the parameter block>` *(control)* | 0 errors | 0 errors |

## D-4 — the terminal-rule consequence (RD43-02, BLOCKING)

A record whose **last visible line read `GATE VERDICT: NOT READY`**, with
an indented-code `</details>` above a hidden `READY FOR <the verbatim
target>`, validated at **0 errors**, exit 0, and produced a trend row
reading READY. At v1.16 it is 1 error (`LG-6`, the ambiguity rule), trend
verdict blank. Fixtured in the silent direction, as the code-span form
already was.

## D-5 — an autolink is not a tag (RD43-03, MAJOR)

CommonMark autolinks (`<scheme:…>`, `<local@domain>`) are removed before
any tag is read, and the `<word …>` shorthand is left to the inline rule
of D-3. Each of these records scored **8 errors at v1.15 and 0 at
v1.16**: a URL autolink, an email autolink, and `<see appendix A>` on the
line after a declared field; plus an autolink standing alone in its own
paragraph, which the inline rule alone would not have saved.

## D-6 — a section's content is what a reader sees in it (RD43-04, MAJOR)

LG-4's emptiness test asked whether the section held a line of the
record's **own** — a containment question, and the wrong one for a
*section*. It is now asked over the raw lines: anything non-blank between
the heading and the next heading counts, except §5's declared trailer
labels and the terminal verdict.

| G1 content form | v1.15 | v1.16 |
|---|---|---|
| bulleted list | 1 error (`opens an EMPTY section`) | 0 |
| numbered list | 1 | 0 |
| blockquote | 1 | 0 |
| fenced block | 1 | 0 |
| indented code | 1 | 0 |
| *control:* nothing but §5's trailer | 1 | 1 |

## D-7 — three record corrections (RD43-05, RD43-06, RD43-07, MINOR)

- The disposition register's RD42-01 and RD42-08 rows described repairs
  the v1.15 batch **did not ship**; both carry dated correction markers
  in place, naming what shipped and why (RD43-05).
- The validator comment quoting "0 of 185" where the corpus was 187 no
  longer quotes a denominator at all — the measurement is stated with
  the version that owns it (RD43-06).
- The unreproducible "37 stored attack records (21 + 12 + 4)" sentence is
  replaced by the sweep below (RD43-07).

## Regression: the population, named

All **54** stored attack records of the RD-39, RD-40, RD-41 and RD-42
rounds — 12 + 4 + 21 + 17 across the four harnesses — were run through
the v1.15 validator and the v1.16 validator on identical bytes, with
`--prior` and the `_git` flag preserved, comparing error count, error
identity and trend row. **Exactly one record moves:** the `<details>`
named mid-sentence, 0 → 8 errors, which is D-3's deliberate withdrawal.
Every other diff is empty.

## Fixture arithmetic

187 (v1.15) + 18 = **205**, the count read from the selftest's printed
output:

| block | new fixtures |
|---|---|
| the four RD43-01 carriers (indented code, backslash escape, mid-line, split tag) | 4 |
| the laundered verdict behind an indented-code close (D-4) | 1 |
| autolinks and shorthand at the start of a line (D-5) | 3 |
| an autolink alone in its own paragraph (D-5, the separating case) | 1 |
| the five G1 content forms, accepting (D-6) | 5 |
| G1 with only §5's trailer, refusing (D-6) | 1 |
| inline with and without a hiding attribute (D-3) | 2 |
| an unclosed inline element does not reach past its paragraph (D-3, the separating case) | 1 |

4+1+3+1+5+1+2+1 = 18. Three v1.15 fixtures are **flipped** rather than
added (`<div/>`, `<details/>` in prose, `<details>` mid-sentence), and one
is renamed to say what it measures.

## Mutation-reverts

Twelve, each rebuilt from the **final** v1.16 source, each run **inside a
git repository** so all twelve `_git=True` fixtures register, each
measured by reading the selftest's printed FAIL lines against a
denominator of 205:

| revert | fixtures failed |
|---|---|
| n1 — indented code is not literal text | 2 |
| n2 — backslash escapes not removed | 1 |
| n3 — region trigger back to line-initial only | 15 |
| n4 — the split-tag rule removed | 1 |
| n5 — autolinks read as tags | 1 |
| n6 — inline elements never open a region | 1 |
| n7 — inline elements always open a region | 2 |
| n8 — table rows scanned for tags | 1 |
| n9 — G1 content measured over own lines only | 5 |
| n10 — inline regions survive the end of their paragraph | 1 |
| n11 — self-closing tags skipped | 2 |
| n12 — the condition-6 name set emptied | 16 |

**All twelve witness.** Two of them (n5, n10) failed **0 of 203** when
first built, because no fixture in the corpus separated them from the
layer beside them; the two constructions that separate them were
measured against the renderer and added, and are named in the fixture
table above. That hunt is RD-42's finding applied to this batch's own
work, and it is the reason the count is twelve of twelve rather than ten.

## Disclosed limits and residuals, each measured, none generalized

1. **The predicate refuses a declaration carried inside *any* raw-HTML
   element the record opens, whether or not that element hides it.**
   `<table><tr><td>` and a bare `<div/>` are both refused, and neither
   hides its content — measured. Deciding *hiding* means evaluating CSS
   this instrument cannot evaluate; the over-refusal is in the safe
   direction, and §5 never places a declared field inside raw HTML.
2. **The condition-6 name set is an enumeration** — of CommonMark's
   specification, quoted rather than invented, but an enumeration all the
   same. An element that a future HTML revision makes block-level, and
   that this list does not name, would render as a carrier and read as
   inline. Named here rather than left to the next review.
3. **The two v1.14 predicate clauses with no single-layer witness** (tab
   expansion, the ≤3-column bound) remain so.
4. **Blockquote laziness is still deliberately not implemented**, for the
   §5-template reason stated at v1.14.
5. **§5's non-authority banner** can still be satisfied by a quotation of
   itself in an appendix (RD42-12, carried forward).
6. **The depth scan is quadratic in nesting depth** (RD42-13, carried
   forward).
7. **An asymmetric `**Label:*` still satisfies presence**, and the trend
   row is still printed above the error list carrying the record's
   *claimed* verdict when the record is invalid — both carried forward.

## Where the records cited here live

Every construction in D-2 … D-6 is stored as a fixture in
`scripts/launch_gate_results.py --selftest`. The regression sweep names
its population (54 records, four harnesses) and its one mover, and is
reproducible from `git show 4fd4a58:scripts/launch_gate_results.py`
against the current file. The rendering measurements are reproducible
with `pandoc` and `html5lib`; the harness that produced them is a
scratch tool, and the claims it settled are each carried by a fixture
whose direction it fixed.
