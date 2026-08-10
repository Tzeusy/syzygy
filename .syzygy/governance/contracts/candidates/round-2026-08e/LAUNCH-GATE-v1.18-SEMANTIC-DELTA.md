# Launch-gate v1.17 → v1.18 — semantic delta record

> **Process record for a candidate instrument amendment.** The instrument
> (`launch-gate-pre-specifications.md`, repo root) is a process-policy
> candidate, never authority. This delta records every change of meaning so
> "no question was weakened" stays a reviewable claim. Owner approval of
> v1.18 is prepared, not performed:
> `.syzygy/governance/decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` (P-34) —
> and the offer waits on a fresh-context re-review of this delta
> (**RD-46**), because the session that authored these bytes may not
> confirm them.

Baseline: v1.17 as reviewed by RD-45 (subject sha256
`02368c78c190e45b232b3e38d35857d4dae82cfe4f7416d1058de09a7d66dc32` at
commit `963f1c4`; validator sha256
`28bfa9fd8abb517d2be49f8f41c515f36824fd2fc1798f102ca2e8561e3e9289`;
delta sha256
`cb4918015c38861d1c04ec5a4ff0991e26c72098dca510ef86aba8d04b33baa9`; raw
review `reviews/RD-45-instrument-v117-RAW.md`, storage digest
`c122c9a5ad53c9d947aca0ed5e3033f285e356735a50ac2dc4523f63662ca370`,
40567 bytes, `VERDICT: REVISE`, 4 BLOCKING / 4 MAJOR / 1 MINOR). RD-45
reproduced **all nine** v1.17 mutation denominators on its **first**
reconstruction, verified §1–§8 byte-identical at all eight counts,
confirmed every changelog entry v1.0–v1.15 byte-identical and the v1.16
entry byte-for-byte the frozen prose beneath its four markers,
reconciled 205 + 83 = 288 by fixture-name set difference with 0 dropped
and 0 renamed, and **rebuilt the uncommitted corpus sweep from this
delta's prose alone**, reproducing 199 / 282 / 200 / 0 / 0 moved / 82 /
65 figure for figure. Every delta below closes an RD-45 finding;
dispositions in `reviews/DISPOSITION-REGISTER.md`. **This is a
validator-and-records batch an eleventh time: no question block, no
verdict word, and no section §1–§8 of the instrument changed** (verified
per-section against `git show 963f1c4:launch-gate-pre-specifications.md`
— §1 794, §2 4388, §3 15377, §4 5688, §5 3601, §6 2192, §7 1038, §8 6610
bytes, each identical; twelve versions v1.7–v1.18, and fourteen for §8).
The instrument bytes that move: the `effective_version:` header, the
appended §9 v1.18 entry, and **six** dated correction markers in the §9
v1.17 entry (D-1 names them). The frozen prose beneath every marker in
every entry from v1.13 to v1.17 was verified unchanged by stripping the
markers — with a **wrap-tolerant** start pattern and a balanced-bracket
walk, because two of this round's markers contain a `]` inside them and
one wraps between `[corrected` and its date — and comparing against
`git show 963f1c4:`. Validator changes carry fixtures
(`scripts/launch_gate_results.py --selftest`, **329 fixtures** — the
count read from the selftest's own printed output).

## The sentence this batch was built on

RD-45's: **measure the set, not just the rule — and let a fixture's
expectation come from somewhere other than the thing it is testing.**

v1.17 got the rule right. A mid-line tag opens a region iff it takes its
content out of a reader's sight; `pandoc` and `html5lib` confirm it; 54
of 62 element names moved from wrongly-refused to accepted with no
over-refusal introduced inside that population. And then the set that
rule ranges over was enumerated from a specification list rather than
measured: `_HIDES_INLINE` shipped as CommonMark's condition 1 plus
`details`. `<iframe>`, `<noframes>`, `<noembed>` and `<select>` are each
unpainted mid-line, and each laundered a `READY FOR <the verbatim
target>` beneath a record whose last visible line read
`GATE VERDICT: NOT READY`, at **0 errors**. Two of the four had been
refused at v1.16. One of them — `iframe` — is a name RD-44 had written
down as *"genuinely hides and is correctly refused."*

The corpus could not tell, and that is the second half of the finding:
**65 of the 83 fixtures added at v1.17 computed their expected direction,
and their own titles, from `_HIDES_INLINE`.** A wrong membership
relabelled them instead of failing them. "A check that cannot fail is not
a check" is this validator's own printed motto; it was true of most of
its new corpus.

This is the ninth administration in which one question — *is this line
the record's own, or a quotation of it?* — has been answered
inconsistently. RD-41: the predicate must carry state. RD-42: state for
markdown's containers, enumeration for HTML's. RD-43: the region does not
begin or end where a reader sees it. RD-44: a region begins at a line,
not at a `<`. RD-45: **the rule was fixed and the set was never
measured.**

## D-1 — corrections of the frozen v1.17 delta and the §9 v1.17 entry (the frozen record is not edited)

The v1.17 delta and the §9 v1.17 entry are bound by RD-45's review
digests. Neither is edited (verification rule 10). The corrections travel
here, and — for the instrument, whose bytes an approval digest binds — as
dated markers in place.

| the frozen claim | the correction |
|---|---|
| **the change that was never claimed at all** — the split-tag rule was narrowed from `.search` to `.match` and its condition-6 membership test removed | A **change of meaning shipped unrecorded**, in a delta whose first paragraph says it records every change of meaning, and covered by none of the nine mutants. It reopened RD43-01(d)'s carrier four columns to the right (a mid-line `<div` with `style="display:none">` on the next line, laundered at 0 errors) and refused §5's own angle-bracket shorthand wrapped across two lines with 7 errors. This batch states it as an omission rather than folding it into a repair (RD45-01) |
| §9 and D-3: the mid-line rule, with `_HIDES_INLINE` as condition 1 plus `details` | The rule is right; **the set was never measured**. Four unpainted names were missing, two of them v1.17 regressions, one of them a name the previous review had recorded as correctly refused (RD45-03) |
| the v1.17 corpus: 65 of 83 new fixtures | Their expected direction and their titles came from the set under test, so they could not fail for a wrong membership. The `<iframe>` fixture shipped **green** with a title calling a laundering record "lawful" (RD45-06) |
| §9: "a close tag written inside a mid-line `<textarea>` … can never hide a field" | **False, and backwards.** Ending a region early is precisely how a field is hidden: the validator believed the `</div>` closed the hiding div; the browser knows it did not, and the field renders inside `div[style=display:none]` at 0 errors (RD45-04) |
| §9 and D-2: "LG-6 … **names the line that opened the region** and quotes it" | **False of the shipped bytes.** `_opened_by` walked back to the last line flagged as the record's own, which steps past the line that opened the region — that line is never own. The administrator was pointed at a declared field that opened nothing, and the fixture asserted only that the substring "opened at line" appeared (RD45-05) |
| §9 and D-6: the hiding set "gains … `opacity:0`" | One spelling of one value. `opacity:.0` and `opacity:0%` are the same CSS value and each hid a declared field at 0 errors (RD45-08) |
| §9 and D-7(d): "**Seven** accepting-direction fixtures are broken by no revert" | **Eleven**, measured over the whole population. Seven was RD-44's figure for v1.16's 26-fixture population, carried into §9 as a fact about v1.17 — verification rule 3's failure mode (RD45-09a) |
| §9: "53 of the 62 names … blanked the rest of a lawful record at **0 errors**" | The blanking scores **6** errors. The "0 errors" belongs to RD-44's sentence about v1.15, from which this one was compressed (RD45-09b) |

## D-2 — the mid-line hiding set is generated, not enumerated (RD45-03, BLOCKING)

Population by construction, with a denominator: CommonMark's condition-6
list ∪ the HTML5 raw-text and escapable-raw-text elements ∪ the HTML
Standard's UA-stylesheet `display:none` set ∪ every element whose content
model is fallback or non-painted content — **84 names**. Each was placed
mid-sentence in this instrument's own record shape, rendered with
`pandoc` under **both** `-f gfm` and `-f commonmark`, parsed with
`html5lib`, and judged by the ancestor chain of the following declared
field. **The two readers agreed on all 84.**

| result | count | names |
|---|---|---|
| hides — the field renders inside a non-painting ancestor | **8** | `details`, `iframe`, `noembed`, `noframes`, `script`, `select`, `style`, `title` |
| paints | **69** | the rest, including `textarea`, `pre`, `summary`, `div`, `table`, `td`, `li`, `p` |
| **unsettled** | **7** | `basefont`, `datalist`, `dialog`, `head`, `noscript`, `rp`, `template` |

The seven unsettled names are refused **in the safe direction and
disclosed as unsettled rather than counted as measured**: `html5lib` 1.1
closes each of them at the following `</p>`, so the field renders outside
them *here* — but each is a name whose content the UA stylesheet does not
paint, or whose paragraph-closing behaviour changed in HTML after this
parser was written (`dialog`), or whose visibility depends on scripting
(`noscript`), or which the parser treats as void while the stylesheet
hides it (`basefont`). Refusing them costs a reviewer who writes one of
those seven names mid-sentence about this instrument. Accepting them
would cost a laundered verdict if a browser disagrees with the parser.
The over-refusal is the choice, and this is where it is written down.

An element that hides **by type** keeps its region across blank lines —
measured: a mid-line `<iframe>` or `<select>` still contains the field two
paragraphs later. Only an element that hides by **attribute** alone
(`<span hidden>`) is inline and ends at its own paragraph.

## D-3 — the corpus takes its direction from the measurement, not from the predicate (RD45-06, MAJOR)

The 84 names are now a **literal table in the fixture source**, written
down with its date, method and denominator. The loop reads the table; the
predicate is the subject. A further fixture asserts that
`_HIDES_INLINE` and `_HIDES_INLINE_UNSETTLED` **equal** the table name for
name — so editing either set without re-measuring fails the selftest
instead of relabelling 65 fixtures.

## D-4 — the tag scanner respects quoted attribute values (RD45-02, BLOCKING)

`_TAG_RE`'s attribute group was `[^>]*`, so the match ended at the first
raw `>` — which the HTML5 tokenizer does not do inside a quoted value.
`<div style="content:'>';display:none">` therefore reached no hiding test
at all: not an edge of the widened hiding set but the whole of it,
unreached. Quoted values are consumed here as the tokenizer consumes
them. **The same defect existed one layer down**, in the hiding test's
own `style=[^>]*` limb, and survived the first repair; both are fixed and
both have a mutant.

## D-5 — a raw-text element suppresses tag reading whether or not it opened a region (RD45-04, BLOCKING)

v1.17 tied the suppression to the region and left `textarea` outside it,
reasoning that an early close "can never hide a field". Ending a region
early **is** how a field is hidden. Measured: `<div style="display:none">`
above `Appendix prose <textarea>` above `</div>` above `</textarea>`
renders the following field inside `div[style=display:none]` under both
readers, and validated at 0 errors. Raw-text state is now independent of
the region stack, so `</div>` written inside a `<textarea>` closes
nothing. Both the mid-line and line-initial forms are fixtured.

## D-6 — one rule for an opening tag whose `>` arrives on a later line (RD45-01, BLOCKING)

The continuation is read from **either** position, cancelled by a blank
line as the renderer cancels it, and then classified by the same rule as
any other tag — so a wrapped `<div style="display:none">` opens a region
and a wrapped `<see the appendix for the full carrier list>` does not.
Five fixtures, four of them accepting.

This is also the entry that records the change v1.17 made and did not
record.

## D-7 — a region ends where its markdown container ends (RD45-07, MAJOR)

`</blockquote>` and `</li>` pop an element the renderer opened inside
them. v1.17 let a `<details>` named mid-sentence inside a blockquote or a
list item swallow the rest of the record — three over-refusals of twelve,
on the most likely lawful sentence in this corpus: a reviewer quoting or
bulleting a prior finding that names `<details>`.

Containers now carry **identities**, not depths, so a sibling list item
does not inherit the previous item's region; and a **blank line
re-identifies a blockquote**, because a blank line ends one and the `>`
beneath it begins another — measured, the field in the second blockquote
renders outside a `<details>` named in the first, while a `>`-marked
blank line keeps one blockquote and the field stays inside. The container
stack itself is untouched: §5's own template depends on its blockquote
matching across blank lines, so the re-identification changes region
scope only, and no flag with it.

## D-8 — the hiding test reads a value, not a spelling (RD45-08, MAJOR)

`opacity:.0`, `opacity:0%` and `opacity:0.00` are the same CSS value as
`opacity:0`. The property's value is parsed and compared to zero;
`opacity:0.5` stays lawful, and is fixtured.

## D-9 — LG-6 names the line that opened the region (RD45-05, MAJOR)

The opening line is carried on the region's own stack entry and returned
directly, instead of being guessed by walking back to the last line
flagged as the record's own. The fixture asserts the **line number**,
derived from the record's own text.

## Regression: by script, population by construction

The rule RD44-05 established and RD-45 reproduced: **a regression claim
quotes a script's printed output or does not appear.** The script is
session-local and not committed; it is stated here completely enough to
be rebuilt, and RD-45 rebuilt the v1.17 one from this description alone.
Take each version's own source, inject into its `case()` helper a line
that appends the fixture's text and `_git` setting to a file, run that
version's `--selftest` **inside a repository**, then replay every
captured record through **both** validators with that record's own `_git`
setting and compare the sets of error codes.

| measured | value |
|---|---|
| v1.17 captured records | 282 |
| v1.18 captured records | 322 |
| carried forward (identical text and git setting) | 282 |
| dropped | 0 |
| **carried-forward records whose output moved** | **5** |
| records added at v1.18 | 40 |
| of those, answered differently by v1.17 | 17 |

**All five movers are named and deliberate**, each in the refusing
direction: `iframe` and `noframes` (RD45-03's repair — both laundered at
0 errors under v1.17), and `basefont`, `dialog` and `head` (the disclosed
safe direction of D-2). Every count above is printed by the script; none
is typed.

## Fixture arithmetic

288 (v1.17) + 106 new names − 65 renamed = **329**, by set difference of
printed fixture names, 0 dropped. The 65 renamed are the whole of v1.17's
name loop: every one of its titles was computed from the predicate under
test, so every one had to be rewritten (D-3).

| block | new fixtures |
|---|---|
| the measured 84-name table — 8 hiding, 7 unsettled, 69 painting | 84 |
| the table-versus-predicate equality assertion (D-3) | 1 |
| the split-tag rule, both positions and three accepting shapes (D-6) | 5 |
| the quoted `>`, both directions (D-4) | 2 |
| `</div>` inside a `<textarea>`, mid-line and line-initial (D-5) | 2 |
| markdown containers: blockquote, list item, sibling, and the two separating constructions (D-7) | 6 |
| the top-level control that must still refuse (D-7) | 1 |
| the opacity values, three refusing and one accepting (D-8) | 4 |
| LG-6's line number (D-9) | 1 |

84+1+5+2+2+6+1+4+1 = **106**.

## Mutation-reverts

Twelve, one per repair, each rebuilt from the **final** v1.18 source,
each run **inside a git repository**, each measured by reading the
selftest's printed FAIL lines against a denominator of 329:

| revert | fixtures failed |
|---|---|
| n1 — `_TAG_RE`'s attribute group stops at the first `>` | 1 |
| n2 — the hiding test's `style=` limb stops at the first `>` | 1 |
| n3 — the hiding set reverts to v1.17's four names | 5 |
| n4 — the unsettled names are accepted instead of refused | 8 |
| n5 — raw-text suppression tied to the region again | 1 |
| n6 — a region ignores the container it was opened in | 5 |
| n7 — containers compared by depth, not identity | 2 |
| n8 — an unterminated opening tag is never continued | 3 |
| n9 — the continuation is read only from a line-initial fragment | 1 |
| n10 — LG-6 walks backwards for the last own line | 1 |
| n11 — the opacity limb matches one spelling | 2 |
| n12 — a blank line no longer re-identifies a blockquote | 1 |

**All twelve witness.** n3's first construction removed only one name
from the set it claimed to revert and killed the wrong five fixtures;
the mutant was rebuilt before the number was believed, which is RD-44's
apparatus-first discipline applied to this batch's own work.

Of the 106 fixtures added, **24 are broken by at least one revert and 82
by none** — measured over the whole population, not remembered from a
previous round. Of those 82, **73** are the measured table's accepting
entries, whose job is to document a lawful shape rather than to witness a
repair, and the remaining **9** are second constructions of a repair
another fixture already witnesses. This is the figure RD45-09(a) found
carried forward wrongly last round; it is generated here.

## Disclosed limits and residuals, each measured, none generalized

- **Seven names are refused on an unsettled measurement** (D-2). This is
  an over-refusal in the safe direction and it is the only place in this
  predicate where a refusal rests on something other than a measurement
  the two readers agreed on.
- **The hiding attributes remain an enumeration** — `hidden`,
  `aria-hidden="true"`, `display:none`, `visibility:hidden`, and any
  zero value of `opacity`. A construction outside it is read as prose.
- The predicate still refuses a declaration carried inside **any**
  raw-HTML region the record opens **at a line**, whether or not it
  hides, because deciding *hiding* means evaluating CSS this instrument
  cannot evaluate. The over-refusal is in the safe direction and §5 never
  places a declared field inside raw HTML.
- The two v1.14 clauses with no single-layer witness (tab expansion, the
  ≤3-column bound) remain so.
- Blockquote laziness is still deliberately not implemented, for the
  §5-template reason stated at v1.14.
- §5's non-authority banner can still be satisfied by a quotation of
  itself in an appendix (RD42-12); the depth scan is still quadratic in
  nesting depth (RD42-13); an asymmetric `**Label:*` still satisfies
  presence; and the trend row is still printed above the error list
  carrying the record's *claimed* verdict when the record is invalid —
  all carried forward.

## Where the records cited here live

| record | path |
|---|---|
| RD-45 raw review, verbatim | `reviews/RD-45-instrument-v117-RAW.md` |
| verdict word, copied exactly | `reviews/DELIVERY-AND-VERDICT-REGISTER.md` |
| dispositions, recorded before any frozen subject was edited | `reviews/DISPOSITION-REGISTER.md` |
| the frozen v1.17 delta this record corrects | `LAUNCH-GATE-v1.17-SEMANTIC-DELTA.md` |
| owner decision the amendment is prepared for | `.syzygy/governance/decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` (P-34) |

No question was weakened. No identifier was renumbered. No owner act was
performed.
