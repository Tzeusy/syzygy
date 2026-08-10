# Launch-gate v1.16 → v1.17 — semantic delta record

> **Process record for a candidate instrument amendment.** The instrument
> (`launch-gate-pre-specifications.md`, repo root) is a process-policy
> candidate, never authority. This delta records every change of meaning so
> "no question was weakened" stays a reviewable claim. Owner approval of
> v1.17 is prepared, not performed:
> `.syzygy/governance/decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` (P-34) —
> and the offer waits on a fresh-context re-review of this delta
> (**RD-45**), because the session that authored these bytes may not
> confirm them.

Baseline: v1.16 as reviewed by RD-44 (subject sha256
`e2818c05db8c625c4aa62dfa875570f9d0babe946d1c8630843906139be4627c` at
commit `186d90b`; validator sha256
`23502a9526db2a117d50046a76dce97600a13f6ee928a14692ce0a1867e7d9c1`;
delta sha256
`6e76cc59561fcf68c029f2b0f3a745fff2f586dabe52e251b03c8c8b04f8ee60`; raw
review `reviews/RD-44-instrument-v116-RAW.md`, storage digest
`bb8bab5817f8e6c80dc14f5554b1d20aac513949f1648fe0486ddaf3cfe9ae9f`,
42682 bytes, `VERDICT: REVISE`, 3 BLOCKING / 3 MAJOR / 2 MINOR). RD-44
reproduced **every one of the twelve** v1.16 mutation denominators
(rebuilding two of its own reconstructions first, and recording that
rather than filing a false finding), verified §1–§8 byte-identical at
all eight byte counts across ten versions, confirmed the frozen §9 v1.15
entry stripped of its six markers is byte-for-byte the frozen prose,
reconciled 187 + 18 = 205 by fixture-name set difference, and ran
`--selftest` in a clone before and after every mutation. Every delta
below closes an RD-44 finding except D-8, which declines one limb of one
finding with the measurement that falsifies it; dispositions in
`reviews/DISPOSITION-REGISTER.md`. **This is a validator-and-records
batch a tenth time: no question block, no verdict word, and no section
§1–§8 of the instrument changed** (verified per-section against
`git show 186d90b:launch-gate-pre-specifications.md` — §1 794, §2 4388,
§3 15377, §4 5688, §5 3601, §6 2192, §7 1038, §8 6610 bytes, each
identical; eleven versions v1.7–v1.17, and thirteen for §8). The
instrument bytes that move: the `effective_version:` header, the
appended §9 v1.17 entry, and **four** dated correction markers in the §9
v1.16 entry (D-1 names them; counted over that entry's span with the
wrap-tolerant pattern RD42-05 made necessary, and the frozen prose
verified unchanged beneath them by stripping the markers and comparing
against `git show 186d90b:`). Validator changes carry fixtures
(`scripts/launch_gate_results.py --selftest`, **288 fixtures** — the
count read from the selftest's own printed output).

## The sentence this batch was built on

RD-44's, and it is one word changed from RD-43's: **decide the block
phase first, and decide where a block *begins* the way the renderer
decides it — a region begins at a LINE, not at a `<`.**

v1.16 adopted the right method (`pandoc` + an HTML5 parser as ground
truth for any claim about a reader) and then did not apply it to the
rule the method was used to justify. It read CommonMark's start
condition 6 as naming elements that open a region *from any position*.
Three lines of `pandoc` falsify that: condition 6, like all seven start
conditions, requires the line to **begin** with the tag; what
distinguishes it from condition 7 is only that it may *interrupt a
paragraph*. What v1.16 implemented is HTML5's list of start tags that
close an open `<p>` — a different fact about a different thing, and
closing a paragraph is not opening a region.

This is the eighth administration in which one question — *is this line
the record's own, or a quotation of it?* — has been answered
inconsistently. RD-41: the predicate must carry state. RD-42: state for
markdown's containers, enumeration for HTML's. RD-43: the region does
not begin or end where a reader sees it. RD-44: **a region begins at a
line, not at a `<`.**

## D-1 — corrections of the frozen v1.16 delta and the §9 v1.16 entry (the frozen record is not edited)

The v1.16 delta and the §9 v1.16 entry are bound by RD-44's review
digests. Neither is edited (verification rule 10). The corrections
travel here, and — for the instrument, whose bytes an approval digest
binds — as dated markers in place.

| the frozen claim | the correction |
|---|---|
| §9: "**CommonMark's own start condition 6 names the elements that open a region from any position**, including mid-paragraph" | **False.** Condition 6 is line-initial like all seven; it may interrupt a paragraph, which is not the same property. 53 of the 62 names, mentioned once mid-sentence in a lawful record's G1 section, blanked the rest of that record at 0 errors (RD44-01) |
| §9: "only when it carries a hiding attribute (`hidden`, `display:none`, `aria-hidden`) does it carry a declaration out of sight" | **False in both limbs.** Condition-1 raw-text elements (`script`, `style`, `title`) hide by element type from any position and past any blank line, and `<details>` collapses with no attribute; and the three attributes are an enumeration, not a sufficiency condition — `visibility:hidden` and `opacity:0` hid a declared field at 0 errors (RD44-03, RD44-06) |
| §9 and the delta's "Regression: the population, named": "All **54** stored attack records … **Exactly one record moves**" | **Withdrawn entirely.** RD-44 could reproduce neither the population nor the attribution from four remembered harness sizes, and measured five movers, two of which the same delta's D-3 table listed. Replaced by the scripted corpus sweep below (RD44-05) |
| §9 and the delta: "**all twelve** failing exactly the fixtures their repair added"; "**All twelve witness**" | The twelve denominators are exact and reproduce; the characterisation does not. n5 and n12 each also break fixtures that **pre-date** the batch, because they revert layers those fixtures already rested on (RD44-07b) |
| §9: "the first batch of this chain with **no unwitnessed repair**" | **Withdrawn.** Seven of the 26 new-or-renamed fixtures are broken by no revert: they are accepting-direction fixtures documenting a lawful shape, which is a different job from witnessing a repair. The measurement the claim stood in for is the twelve denominators, which hold (RD44-08) |
| the delta's fixture arithmetic: "three v1.15 fixtures are **flipped** … and **one is renamed**" | **Five** were renamed, counted by set difference of printed names, not one (RD44-07a) |
| the selftest's skip notice, which computed a count from `_git=True` occurrences | It counted 16 where 12 fixtures are skipped. The notice now names *what* is missing and quotes no figure (RD44-07c) |

## D-2 — a region begins at a line (RD44-01, BLOCKING)

The trigger returns to **line-initial for every name**. On a line that
begins with a tag, a condition-6 name opens a region even when it
interrupts a paragraph; any other name opens one only when no paragraph
is open (condition 7). `_COND6` survives as what it actually is — an
enumeration of HTML's block-level element names, used for two distinct
purposes and documented as such — and is no longer described as "the
names that open a region from any position".

Measured cost of the v1.16 rule, swept with its denominator: **53 of 62
names** blanked a lawful record. Measured payment of the v1.17 rule: the
name sweep now runs as a **fixture loop over both enumerations, 65
names, in the accepting direction wherever the render paints the text** —
the corpus RD-44 asked for, so it can tell next time.

Second limb: LG-6 no longer says only that a line "sits inside a
container opened on an earlier line". It **names the line that opened
the region** and quotes it, which the RD43-03 disposition promised and
did not ship.

## D-3 — a mid-line tag opens a region only when it hides (RD44-01, RD44-03, BLOCKING)

What made RD43-01(c) a carrier was never its position: it was that the
element takes its content out of a reader's sight. That property, and
only that property, opens a region mid-line at v1.17:

- **by element type** — CommonMark's **condition 1** raw-text elements
  `script`, `style` and `title` (a browser never paints their content,
  and *nothing inside them is a tag* until their own close tag arrives),
  and `details` (collapsed by default);
- **by hiding attribute** — the enumeration in D-6.

`textarea` is raw text that **is** painted (in a form control), and is
deliberately absent from the hiding set — measured, like `pre`,
`summary`, `li`, `div`, `table`, `span`, `noscript` and `template`,
each visible mid-line and each accepted.

Condition 1 gets its own rule in the scan: inside a raw-text element no
tag is read until its matching close. The load-bearing case took two
constructions to find — with pop-to-name in place, most tags written
inside a `<script>` change nothing either way. What the guard is
actually for is a **close** tag inside raw text naming an element opened
below it: `var x = "</div>";` inside a `<script>` inside a
`display:none` `<div>` does not close that div, and the render confirms
the field stays at `div[HIDDEN]`. Without the guard the record validated
at 0 errors.

Mid-line `<script>` and mid-line `<style>` were two of the four v1.16
laundering constructions; both are refused, both are fixtured.

## D-4 — `para_open` means a paragraph is open (RD44-02, BLOCKING)

v1.16 set it from "the previous line had characters on it". An ATX
heading is not a paragraph — so an indented `</details>` placed after a
heading was read as a close tag rather than as the indented code block a
reader sees, and it laundered a `READY FOR` beneath a visible
`GATE VERDICT: NOT READY` at 0 errors, defeating the batch's own
indented-code repair.

A paragraph is ended by an ATX heading, a thematic break, a raw-HTML
block line, a table row and a setext underline alike. Fixtured with the
heading form RD-44 built and with one non-heading form per
paragraph-ending construct.

## D-5 — a table row is a row of a table (RD44-04, MAJOR)

v1.16 asked whether a line contained two pipes and dropped every tag on
it unread. A lone `| <div style="display:none"> |` line is not a table
at all, and it carried a declared field and the terminal verdict out of
sight at 0 errors. The carve-out is now computed from the table's
structure — a delimiter row with a header line above it, and the
contiguous rows beneath — and both directions are fixtured: the lone
pipe line is read, and `| <details> |` under a real delimiter row still
opens nothing.

## D-6 — the hiding set is an enumeration, and it widens (RD44-06, MAJOR)

`visibility:hidden` and `opacity:0` join `display:none`, `hidden` and
`aria-hidden="true"`. Each hid a declared field at 0 errors at v1.16;
each is refused at v1.17, with the field's DOM ancestry measured as
`span[HIDDEN]` in §5's own contiguous-field shape, and a plain `<span>`
in the same position accepted.

The set is **disclosed as an enumeration**, beside the block-level one,
and no sufficiency is asserted for either. A construction outside both
is read as prose, and that is a limit, not a guarantee.

## D-7 — records (RD44-07, RD44-08, MINOR)

(a) "one renamed" → **five**, by set difference. (b) The twelve
denominators are exact; the characterisation around them is corrected in
D-1. (c) The selftest's skip notice names what is missing instead of
computing a wrong count from `_git=True` occurrences. (d) Seven
accepting-direction fixtures are broken by no revert and are named as
what they are — documentation of a lawful shape, not a witness — and the
"no unwitnessed repair" claim is dropped. The two substantive cases
RD-44 identified are separated: the autolink exclusion by the
alone-on-its-own-line construction carried from v1.16 (still the only
fixture m9 breaks), and the inline hiding rule by the mid-line carriers
added at D-6, which sit inside a line rather than at the start of one.

## D-8 — one limb declined, with the measurement (RD44-06, MAJOR)

RD44-06 asked that the token `hidden` count only as an HTML boolean
attribute and not as the English word inside §5's own angle-bracket
shorthand, with `<see the hidden appendix>` fixtured in the **accepting**
direction. **Declined.** Rendered, that record's next declared field is
not visible: `hidden` is a **global boolean attribute** and the HTML5
parsing algorithm applies it to unknown elements, so `<see the hidden
appendix>` produces an element `see` carrying `hidden`, and the next
field's DOM ancestry measures `see[HIDDEN]`. Accepting the record would
accept a construction a reader cannot read.

The finding's own concern — a reviewer must be able to write about a
hidden appendix — is answered by the form the withdrawal leaves: the
same words in a code span measure `['p', 'body', 'html']` and are
accepted. Both directions are fixtured, and the refusing fixture carries
the measurement in its name so the next administration inherits the
reason rather than the ruling.

## Regression: by script, with the population defined by construction

The rule this chain adopts, after two consecutive rounds of
unreproducible attack-record claims: **a regression claim quotes a
script's printed output or does not appear.**

The sweep script is **session-local and not committed** — it is a
measurement apparatus, not repository tooling, and it is stated here
completely enough to be rebuilt: take each version's own source, inject
into its `case()` helper a line that appends the fixture's text and
`_git` setting to a file, run that version's `--selftest` **inside a
repository**, then replay every captured record through **both**
validators with that record's own `_git` setting and compare the sets of
error codes. Population by construction — every record the selftest
hands to `validate()` via `case()`, in both directions:

| measured | value |
|---|---|
| v1.16 captured records | 199 |
| v1.17 captured records | 282 |
| carried forward (identical text and git setting) | 200 |
| dropped | 0 |
| **carried-forward records whose output moved** | **0** |
| records added at v1.17 | 82 |
| of those, answered differently by v1.16 | **65** |

The last row is the point: the accepting direction that 205 fixtures
could not tell is now 65 fixtures that can. Every count above is printed
by the script; none is typed. The six selftest fixtures that call
`validate()` outside `case()` (the `--prior` trend pairs) are outside
this population by construction, and are stated here rather than
silently absorbed.

## Fixture arithmetic

205 (v1.16) + 83 = **288**, by set difference of printed fixture names —
0 dropped, 0 renamed. (82 of the 83 new names are records not already in
the v1.16 corpus; one new name re-uses an existing record text.)

| block | new fixtures |
|---|---|
| the name loop over both enumerations, accepting and refusing (D-2, D-3) | 65 |
| `para_open` — one construct per paragraph ending (D-4) | 3 |
| mid-line condition-1 elements, refusing (D-3) | 3 |
| the raw-text guard's separating construction (D-3) | 1 |
| a mid-line `textarea`, accepting (D-3) | 1 |
| the lone pipe line, and a real table row (D-5) | 2 |
| the hiding attributes in §5's contiguous shape, four refusing + one accepting (D-6) | 5 |
| the declined limb and the form its withdrawal leaves (D-8) | 2 |
| LG-6 names the line that opened the region (D-2) | 1 |

65+3+3+1+1+2+5+2+1 = 83.

## Mutation-reverts

Nine, one per repair, each rebuilt from the **final** v1.17 source, each
run **inside a git repository** so all git-dependent fixtures register,
each measured by reading the selftest's printed FAIL lines against a
denominator of 288:

| revert | fixtures failed |
|---|---|
| m1 — region trigger back to "any position" (v1.16's rule) | 54 |
| m2 — mid-line carriers open nothing | 17 |
| m3 — raw-text elements parse tags inside them | 1 |
| m4 — `para_open` back to "the line had characters" | 3 |
| m5 — any two-pipe line counts as a table row | 1 |
| m6 — the hiding set narrows back to v1.16's | 2 |
| m7 — LG-6 stops naming the line that opened the region | 1 |
| m8 — every mid-line carrier is inline, so a blank line ends it | 11 |
| m9 — autolinks read as tags (RD44-08's carried separating case) | 1 |

**All nine witness**, and m3 witnesses only because its first
construction failed **0 of 288**: pop-to-name already recovered from
every tag written inside a `<script>` that the obvious mutant reaches.
The separating construction in D-3 was measured against the renderer and
added. That hunt is the two-layer trap applied to this batch's own work,
for the third round running.

## Disclosed limits and residuals, each measured, none generalized

- **Both lists are enumerations.** The block-level names and the hiding
  attributes are enumerated, not derived; a construction outside either
  is read as prose. This is stated rather than defended.
- **A close tag written inside a mid-line `<textarea>` is still parsed**
  as a tag. `textarea` is painted, so it opens no region mid-line, which
  leaves its content's tags readable. The failure mode is ending a
  region early — never hiding a field.
- The predicate still refuses a declaration carried inside **any**
  raw-HTML region the record opens **at a line**, whether or not it
  hides, because deciding *hiding* means evaluating CSS this instrument
  cannot evaluate. The over-refusal is in the safe direction and §5
  never places a declared field inside raw HTML.
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
| RD-44 raw review, verbatim | `reviews/RD-44-instrument-v116-RAW.md` |
| verdict word, copied exactly | `reviews/DELIVERY-AND-VERDICT-REGISTER.md` |
| dispositions, recorded before any frozen subject was edited | `reviews/DISPOSITION-REGISTER.md` |
| the frozen v1.16 delta this record corrects | `LAUNCH-GATE-v1.16-SEMANTIC-DELTA.md` |
| owner decision the amendment is prepared for | `.syzygy/governance/decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` (P-34) |

No question was weakened. No identifier was renumbered. No owner act was
performed.
