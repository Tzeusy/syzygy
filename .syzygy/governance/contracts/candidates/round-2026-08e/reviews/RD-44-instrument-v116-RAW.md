All measurements complete. The clone is porcelain-clean at close with the three subject digests unchanged.

---

# RD-44 — Launch-gate instrument re-review, v1.16 exact bytes (round-2026-08e, frozen commit `186d90b`)

- **Review id:** RD-44 (twelfth administration of the instrument re-review chain: RD-33 → v1.6 … RD-42 → v1.14 → RD-43 → v1.15)
- **Date:** 2026-08-11
- **Reviewer:** isolated fresh-context session, Claude family. Same-family re-review — the caution the instrument's own **F5** records applies to me. I authored no byte under review.
- **Clone:** `…/scratchpad/clone-08e-r24`, HEAD `186d90b4a2e826b51cdea3c6754a262c07c6806e`. `git status --porcelain` **empty at open and at close** (0 lines); **zero `__pycache__`/`.pyc` under the clone at close**. Every mutant, synthetic record, workspace copy and harness lives in `…/scratchpad/rd44/`. Nothing under `/home/tze/GitHub/syzygy` was read, written or executed.

## Materials read in full, and digests verified

Verified with `sha256sum` at open and again at close, byte counts by `wc -c`:

| artifact | sha256 | bytes | matches charter |
|---|---|---|---|
| `launch-gate-pre-specifications.md` | `e2818c05db8c625c4aa62dfa875570f9d0babe946d1c8630843906139be4627c` | 99082 | ✔ |
| `scripts/launch_gate_results.py` | `23502a9526db2a117d50046a76dce97600a13f6ee928a14692ce0a1867e7d9c1` | 162456 | ✔ |
| `round-2026-08e/LAUNCH-GATE-v1.16-SEMANTIC-DELTA.md` | `6e76cc59561fcf68c029f2b0f3a745fff2f586dabe52e251b03c8c8b04f8ee60` | 16094 | ✔ |

Also read in full: `reviews/RD-43-instrument-v115-RAW.md` (317 lines, 7 findings, `VERDICT: REVISE`); the RD-43 disposition block of `reviews/DISPOSITION-REGISTER.md` including all seven rows and the accepted nit; `decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` (P-34); `AGENTS.md`'s ten verification rules; §9's v1.15 and v1.16 entries line by line; and the whole of `_active_lines`, `_own_flags`, `_readable_tags`, `_strip_code_spans`, `_g1_section_content`, `_takewhile_before_heading`, `_carriers`, `_decl`, `_COND6`, `_HIDING_ATTR_RE`, `_AUTOLINK_RE`, `_SPLIT_TAG_RE`, `_TABLE_ROW_RE` and the LG-1/LG-4/LG-5/LG-6/LG-12 paths.

## Method — what I ran

`[Observed]` `python3 scripts/launch_gate_results.py --selftest` in the clone → **`205 fixtures, 0 failing`**, read from the tool's own output: **205 `pass` lines, 0 `FAIL` lines**, 206 output lines.

`[Observed]` **The git-skip hazard, re-measured.** The same file run from a non-git directory prints **`193 fixtures`** — exactly the 12 `_git=True` fixtures silently absent. **Every mutant below was run inside a git repository** (a `cp -a` copy of the clone at the same HEAD, restored after each run), every denominator I report is **205**, and the unmutated control printed `205 fixtures, 0 failing` in that copy before and after every mutation run. The batch respected this hazard: all twelve of its claimed denominators only reproduce at 205.

`[Observed]` A record generator built from the validator's own `GOOD` template with `REPO` bound to the clone, so LG-1/LG-2/LG-11 and both citation-existence paths executed **git-on against the real commit `186d90b4`, the real committed instrument digest `e2818c05…`, the real §8 digest `01209c0f…` and the real `effective_version: v1.16`** on every construction below. Both a `NOT READY` baseline and a `READY FOR <the verbatim target>` baseline validate at **0 errors** git-on; the decisive constructions were re-run through the clone's own CLI so the trend row and exit code are read, not inferred.

`[Observed]` **Rendering ground truth, systematised.** Every claim about what a reader sees is a measurement: `pandoc 2.9.2.1 -f gfm` (and `-f commonmark` where the reader could matter), parsed with **`html5lib 1.1`** (`namespaceHTMLElements=False`), walking the DOM to the ancestor chain of the decisive field and flagging `hidden`, `display:none`/`visibility:hidden`/`opacity:0`, `aria-hidden="true"`, collapsed `<details>` and the raw-text elements. **The validator's own-line decision was compared against that chain as a differential sweep, not case by case** — 62 condition-6 names × 2 versions, plus five carrier batteries.

`[Observed]` **Mutation-revert testing (rule 6):** twelve reverts rebuilt from D-2…D-7's own descriptions, plus five alternate readings where the first reconstruction disagreed; each run's *output* read (FAIL lines), never its exit code. I record my wrong first readings below.

`[Observed]` **Cross-version execution:** all **193** records captured from the v1.15 corpus (record bytes, `--prior` bytes and `_git` flag preserved) run through **both** validators **against the same instrument bytes at the same commit** (the v1.16 script dropped into a `4fd4a58` checkout), so the validator is the only variable — comparing error count, error identity **and** trend row.

`[Observed]` Repo-wide sweeps with Python `re`, never shell grep. Denominator **379** text files of 380.

`[Observed]` `python3 scripts/check_governance.py` → **30 OK, 18 WARN, 0 FAIL (48 checks)**; `--selftest` → **121 fixtures, 0 failing**.

`[Unknown]` I did not administer the gate and read no pilot record content. All answer sets are synthetic.

## Per-finding verification — all seven RD-43 findings

| RD-43 | Class | Status | Evidence in the v1.16 bytes |
|---|---|---|---|
| **RD43-01** | BLOCKING | **closed for all four constructions; the class survives out three new doors — RD44-01, RD44-02, RD44-04** | I rebuilt all four git-on with real digests. (a) indented-code `</details>` → **2 errors** (`LG-6`,`LG-12`), DOM ancestry of the field `['html','body','details','p']`; (b) `\</details>` → **2**; (c) mid-line `<div style="display:none">` → **2**, ancestry `['html','body','div[display:none]','p']`; (d) split `<div` + `style=…>` → **2**. My own fifth construction (code span then mid-line div) → **2**. All four move 0 → 2 and each CLI run is `rc=1`, trend verdict blank. **The repair is real.** But the block phase is *not* decided first: `_in_code = cind >= 4 and not para_open`, and `para_open` is set by any non-blank line, so an indented `</details>` after an **ATX heading** is not treated as code — RD44-02, measured below at 0 errors with the field inside a collapsed `<details>`. |
| **RD43-02** | BLOCKING | **closed for the construction; the harm is unclosed — RD44-01, RD44-02, RD44-04** | RD-43's exact record (visible terminal `NOT READY`, indented-code `</details>`, hidden `READY FOR`) now scores **1 error** (`LG-6`, ambiguity), CLI `rc=1`, trend verdict `—`. The backslash and code-span variants likewise 1. **But four new constructions reproduce the original harm exactly**: `record valid`, exit 0, trend row `READY FOR Capability 1 — Project registration and honest shape visibility`, while the last visible line reads `GATE VERDICT: NOT READY`. |
| **RD43-03** | MAJOR | **closed for autolinks and shorthand; the class returns wider — RD44-01** | URL autolink, email autolink, `<see appendix A>`, `<n>` after a declared field: **8 → 0 errors** each; an autolink alone in its own paragraph: **0**. `_AUTOLINK_RE` and `_ESCAPED_LT_RE` are applied in `_readable_tags` before any tag is read. **But the same harm — every line after it, terminal verdict included, stops being the record's own — now fires for 53 of the 62 `_COND6` names mentioned mid-sentence**, on records whose every line a reader plainly sees. The LG-6 message repair the register promised ("with the line that opened it named") **did not ship**: the string at line 779 is byte-identical to the one RD-43 quoted. |
| **RD43-04** | MAJOR | **verified-closed** | All five forms measured git-on, real digests, `## G1 — completeness critic` in §5's own position: bulleted list, numbered list, blockquote, fenced block, indented code each **1 → 0**; controls (plain paragraph, table) 0; the refusing control (heading + §5's trailer only) still **1** (`opens an EMPTY section`). `_g1_section_content` asks presence over the raw lines with two named exceptions. `n9` → **5**. |
| **RD43-05** | MINOR | **verified-closed** | Wrap-tolerant `\[corrected\s+2026-08-\d\d,\s+(RD\d+-\d+)` over the register: **3 `RD43-05` markers**, on the `RD42-01` (3 occurrences) and `RD42-08` rows. |
| **RD43-06** | MINOR | **verified-closed, and better than claimed** | **Zero** `\d+ of \d+` matches remain anywhere in the validator; `185`, `187` and `205` each occur **0** times in the file. The delta's "no longer quotes a denominator at all" is exact. |
| **RD43-07** | MINOR | **NOT closed — RD44-05** | The unreproducible sentence is replaced by a **different unreproducible sentence**, and this time it is inside **§9**, the bytes an approval digest binds (the v1.15 one was delta-only; D-1 row 7 says "in §9 too? — no"). Four independent attributions of the claimed `12 + 4 + 21 + 17 = 54` all fail (below), and the measurement itself is false: **five** records move, not one. |

**Tally, with its denominator:** of RD-43's **7** findings, **7 are present in the v1.16 bytes and none is absent**; **3 are closed outright** (04, 05, 06); **3 are closed for every construction the finding made, with the class surviving another carrier out** (01, 02, 03); **1 is not closed** (07). **All twelve claimed mutation-revert denominators reproduce exactly.**

## Honesty audit of the batch's own measurements

`[Observed]` **§1–§8 identity, computed not transcribed.** Per-section sha256 with a fence-aware splitter, `git show 4fd4a58:` vs the working file, **denominator 10 sections**: §1…§8 **all eight byte-identical**, at exactly **794 / 4388 / 15377 / 5688 / 3601 / 2192 / 1038 / 6610** UTF-8 bytes — the delta's figures reproduce to the byte. Only `HEADER` and §9 differ. ✔

`[Observed]` **The moved bytes are exactly the three the delta names, and nothing else moved.** The whole-file diff is **150 added lines and 8 deleted lines**. The 8 deletions are the `effective_version:` header line plus **7** lines inside the §9 v1.15 entry — the marker insertion points. I then stripped every balanced `[corrected 2026-08-DD, …]` span from the new v1.15 entry and compared it whitespace-normalised against the frozen entry: **identical** (the only residues are four punctuation-spacing artefacts of my own stripper). **No prose in the frozen entry was silently edited** — the D-10 convention and verification rule 10 are respected. ✔

`[Observed]` **Six correction markers, counted with my own wrap-tolerant pattern over the entry's span:** v1.15 entry **6** (`RD43-01` ×4, `RD43-04`, `RD43-03`); a one-line pattern returns **3**, so the delta's stated method is the necessary one. Neighbouring entries reproduce too (v1.13 5, v1.14 5). ✔

`[Observed]` **Fixture arithmetic — reconstructed from the source, not the delta's table.** v1.15 in a git repo prints `187 fixtures, 0 failing`; v1.16 prints `205`. Set difference of printed fixture names: **26 new names, 8 removed, 0 duplicates**, net **+18**. Of the 26, **3 are flips** (`<details/>` in prose, `<div/>`, `<details>` mid-sentence) and **5 are renames** (the `div`/`p`/`span`/`table`/`uppercase details` carriers, same assertion, wording corrected per D-1 #4). 26 − 8 = **18 genuinely new**, and the 18 partition *precisely* into the delta's itemisation: 4 carriers + 1 laundered verdict + 3 autolink/shorthand + 1 autolink-alone + 5 G1 forms + 1 G1-trailer-only + 2 inline hiding + 1 inline-paragraph-end = **18**. 187 + 18 = 205 ✔. **One inaccuracy: the delta says "one is renamed"; measured, five are.** (RD44-07.)

`[Observed]` **The twelve mutation-reverts, rebuilt from D-2…D-7 and run at denominator 205 inside a git repository:**

| revert | claimed | measured | |
|---|---|---|---|
| n1 indented code not literal text | 2 | **2** | ✔ |
| n2 backslash escapes not removed | 1 | **1** | ✔ |
| n3 region trigger back to line-initial only | 15 | **15** † | ✔ |
| n4 split-tag rule removed | 1 | **1** | ✔ |
| n5 autolinks read as tags | 1 | **1** | ✔ |
| n6 inline never opens a region | 1 | **1** | ✔ |
| n7 inline always opens a region | 2 | **2** | ✔ |
| n8 table rows scanned for tags | 1 | **1** | ✔ |
| n9 G1 measured over own lines only | 5 | **5** | ✔ |
| n10 inline survives end of paragraph | 1 | **1** | ✔ |
| n11 self-closing tags skipped | 2 | **2** | ✔ |
| n12 condition-6 name set emptied | 16 | **16** ‡ | ✔ |

† my first reading (`if _at_start:`, dropping `not para_open`) measured **4**; dropping only the `_name in _COND6` disjunct measures **15**. ‡ my first attempt renamed one member of the frozenset rather than emptying it and measured **0** — a reviewer can land on the wrong reconstruction here, and I record both. **All twelve witness; the multiset `{2,1,15,1,1,1,2,1,5,1,2,16}` is identical to §9's list, twelve entries for twelve witnesses.** ✔ The two constructions the batch says it added to separate n5 and n10 from the layers beside them do exactly that: n5 is witnessed **only** by the autolink-alone-in-a-paragraph fixture, n10 **only** by the unclosed-`<span hidden>` fixture.

`[Observed]` **But "all twelve failing *exactly the fixtures their repair added*" (§9) is false of two of them.** n3 fails 15, of which **7 already existed at v1.15**; n12 fails 16, of which the same **7** already existed (the RD40-02 `<details>`-wrapped pair, the three RD41-02 `<details>`-block fields, the RD42-01 code-span and closing-tag fixtures). The denominators are exact; the characterising phrase is not. (RD44-07.)

`[Observed]` **Two-layer-trap audit, run beyond what the batch claims.** Of the 26 new-or-renamed fixture names, **7 are broken by none of the twelve reverts**. Five are benign (the `div`/`p` renames and the G1-trailer-only fixture are guarded by earlier-round repairs or by an exception limb no listed revert targets). **Two are not:** the three `…autolink at the start of a line opens no region` fixtures survive n5 intact — they are saved by the condition-7-cannot-interrupt-a-paragraph layer, not by the autolink exclusion they name — and `an inline <span hidden> DOES carry its field out of the reader's sight` survives **both** n6 and n7, because its `<span hidden>` sits at the start of its own line and is caught by the older line-initial rule instead. The batch's claim to have hunted this trap holds for the twelve reverts; it does not hold for every fixture it shipped.

`[Observed]` **The regression claim's population is not reproducible, by four independent attributions.** (1) fixture-name RD tags: RD-39 **15**, RD-40 **14**, RD-41 **23**, RD-42 **19** = 71. (2) `for`-loop sizes in `selftest()` ("the four harnesses"): `{2,2,3,4,5,5}` at v1.15, `{2,3,3,4,5,5,5}` at v1.16 — no 12, no 21, no 17. (3) fixtures **added per round**, by set difference across the version history (`c70e756`→`7751f12`→`619093b`→`47adfa9`→`4fd4a58`): **16 / 14 / 24 / 19** = 73. (4) a `re` sweep of **379 text files**: no attack-record files exist, and `12 + 4 + 21 + 17` occurs nowhere outside the delta itself. **No partition yields 12 + 4 + 21 + 17 = 54.** RD44-05.

`[Observed]` **And the claim is false under the only checkable reading.** All **193** captured v1.15 records through both validators, same instrument bytes, same commit, priors and `_git` preserved: **five move**, not one — the mid-sentence `<details>` (0 → 8, the disclosed withdrawal), **`<details/>` in prose (0 → 1)**, **`<div/>` (0 → 1)**, and two LG-4 messages rewritten by D-6. The two extra error-identity movers are fixtures of the **RD-41 and RD-42 rounds** — inside the named population — and the delta's **own D-3 table lists both**. The Regression section therefore contradicts the delta's own D-3 table.

`[Observed]` **The disposition register's RD43-07 row describes a repair the batch did not ship.** It says the sentence is replaced by "the sweep RD-43 ran, which is checkable from the repository alone: **all captured records through both validators**". What shipped is the unreproducible 54-record population instead. This is RD43-05's own defect, one round later, in the row that closes RD43-07.

`[Observed]` **The residual list, checked sentence by sentence.** Residual 1 (containment without hiding) reproduces — `<table><tr><td>` and `<div/>` are both refused and neither hides. Residual 2 (the condition-6 set is an enumeration) is stated, and understates: the enumeration is wrong in the *other* direction too (RD44-01) and there is a second, undisclosed enumeration beside it (RD44-03). Residuals 3–7 reproduce unchanged (`**Label:*`, the claimed-verdict trend row, RD42-12's appendix quotation, RD42-13's quadratic scan at 1500-deep nesting, blockquote laziness).

`[Observed]` **A stale notice in the shipped bytes.** The selftest prints `note  git unavailable — 3 git-dependent fixtures skipped`; **12** are skipped. Measured: 205 in a git repo, 193 outside one.

## New findings

### RD44-01 — BLOCKING — §9's central new claim is false of CommonMark and of the renderer, and **53 of the 62** `_COND6` names blank a lawful record — G1, the declared fields and the terminal verdict — all 53 scoring 0 errors at v1.15

`[Observed]` §9, in the bytes an approval digest binds: *"**CommonMark's own start condition 6 names the elements that open a region from any position**, including mid-paragraph."* Measured with the batch's own declared ground truth:

```
$ printf 'a sentence <div>\n\n*emphasis*\n' | pandoc -f gfm -t html
<p>a sentence <div></p>
<p><em>emphasis</em></p>

$ printf '<div>\n\n*emphasis*\n' | pandoc -f gfm -t html
<div>

<p><em>emphasis</em></p>
```

A **mid-line** `<div>` opens no HTML block at all — the markdown after it is still parsed as markdown. Only a **line-initial** `<div>` does. Identical under `-f commonmark`. Condition 6, like every CommonMark HTML-block start condition, requires the line to *begin* with the tag; what distinguishes it from condition 7 is that it may *interrupt a paragraph*, not that it fires mid-line. The batch has conflated CommonMark's start condition 6 with HTML5's "in body" list of start tags that close an open `<p>` — and closing a paragraph is not opening a region that contains everything after it.

`[Observed]` **The consequence, swept with its denominator.** For each of the **62** names in `_COND6`, one lawful record git-on with real digests whose G1 section reads `The <NAME> carrier was not re-tested this administration.` — the reviewer's own completeness critic, on the subject matter this entire chain is about:

- **53 of 62** produce errors while the rendered DOM shows the decisive field at `body > p`, plainly visible;
- **all 53 score 0 errors at v1.15** — every one is a regression introduced by v1.16;
- 6 are void (`base`, `col`, `hr`, `link`, `param`, `track`) and correctly inert; 3 (`details`, `iframe`, `title`) genuinely hide and are correctly refused;
- **0** are under-refused.

The `<td>` case in full — `pandoc` renders the record with the G1 heading, every field and the verdict visible, and the validator says:

```
LG-5: no `Deferred count:` field …
LG-5: no `Reopened count:` field …
LG-6: every `GATE VERDICT:` line in the record sits inside a quotation container — inside a
      container opened on an earlier line — and a quoted verdict is not the record's verdict …
LG-12: required §5 field missing — 'Unknowns and what would settle them:' …
LG-12: required §5 field missing — "Reviewer's falsification notes:" …
LG-12: no `E3 reopen-list:` field …
```

`[Observed]` This is **RD43-03's harm, verbatim, widened from three shapes to fifty-three** — in the batch that closed RD43-03 and whose §9 says it closed "a defect that blanked every line after such a line — the terminal verdict included — and refused a lawful record with 8 errors." `[Observed]` The register's own RD43-03 disposition promised that "an unterminated region must not silently blank a record — the condition is reported as what it is, with the line that opened it named". **That did not ship**: `scripts/launch_gate_results.py:779` still reads `"inside a container opened on an earlier line"`, the exact string RD-43 quoted, and the file contains no message naming an opening line.

*Requires:* a **validator change** (a region opens where the renderer opens one — line-initial, per CommonMark's actual start conditions — and a `<p>`-closing start tag is not a region) **and an instrument amendment** (§9's condition-6 sentence is false of the specification it names and of the renderer the batch declares as its authority). **Offer-blocking, and it blocks the formal administration** — a reviewer of this instrument writing `<td>`, `<p>`, `<li>` or `<summary>` in prose has their record refused with six messages untrue of it, including one about a terminal verdict a reader sees at column 0.

### RD44-02 — BLOCKING — RD43-01(a) reopened: an indented-code close tag after any non-paragraph line is not treated as code, and laundered a `READY FOR` under a visible `GATE VERDICT: NOT READY` at **0 errors**, exit 0

`[Observed]` `_in_code = cind >= 4 and not para_open`, and `para_open` is set true by **any** non-blank line — including an ATX heading, which is not a paragraph, so an indented line after it *is* an indented code block in CommonMark. Executed at `186d90b4`, git on, real digests, full 39-row roster, through the clone's own CLI:

```
GATE VERDICT: NOT READY

<details>
<summary>Appendix — the verdict vocabulary, quoted from §5</summary>

## Appendix note
    </details>

GATE VERDICT: READY FOR Capability 1 — Project registration and honest shape visibility
```

```
$ pandoc -f gfm -t html      (tail)
<details>
<summary>Appendix — the verdict vocabulary, quoted from §5</summary>
<h2 id="appendix-note">Appendix note</h2>
<pre><code>&lt;/details&gt;
</code></pre>
<p>GATE VERDICT: READY FOR Capability 1 — Project registration and honest shape visibility</p>
```

`html5lib` ancestry of the visible line: `['html','body','p']`. Ancestry of the hidden line: **`['html','body','details[collapsed]','p']`**.

```
$ python3 scripts/launch_gate_results.py …/ATTACK-L3.md
trend row:
| 2026-08-10 | 186d90b4 | 0 | 0 | 0 | 0 | 0 | n/a — no prior record supplied | READY FOR Capability 1 — Project registration and honest shape visibility |
record valid — verdict semantics remain the instrument's, not this tool's
$ echo $?
0
```

**0 errors.** The control (a plain paragraph before the indented line) is correctly refused, which is the fixture the batch shipped. `[Observed]` §9 asserts *"At v1.16 the block phase is decided **first** — fences, HTML comments, indented code blocks, backslash escapes and code spans are literal text."* Measured: an indented code block is literal text only when the preceding line was blank or a paragraph.

*Requires:* a **validator change** (`para_open` must track a *paragraph*, not any non-blank line) plus a fixture. **Offer-blocking, and it blocks the formal administration.**

### RD44-03 — BLOCKING — `<script>` and `<style>` are absent from the predicate entirely (CommonMark condition 1), and a mid-line one hides the field **and the verdict** at 0 errors, exit 0

`[Observed]` `_COND6` deliberately quotes CommonMark's condition-6 list, which excludes `pre`, `script`, `style` and `textarea` *because they are condition 1* — and the delta and §9 never mention condition 1. `script`/`style` are not in `_VOID` either, and carry no hiding attribute, so the condition-7 branch does nothing. Executed git-on with real digests:

```
GATE VERDICT: NOT READY

Appendix, not an answer. <script>

GATE VERDICT: READY FOR Capability 1 — Project registration and honest shape visibility
```

`html5lib` ancestry — visible line `['html','body','p']`; hidden line **`['html','body','p','script']`** (text inside a `script` element is never rendered). CLI: `rc=0`, `record valid`, trend row `… | READY FOR Capability 1 — Project registration and honest shape visibility |`. **0 errors.** `<style>` is identical (`['html','body','p','style']`). The line-initial forms *are* caught (2 errors) at both versions; the mid-line forms are missed at **both v1.15 and v1.16** — this is not a regression but a hole the rewrite did not close, and it defeats the model §9 now asserts.

`[Observed]` It also falsifies §9's clause directly: *"every other name is condition 7 … so it renders inline and reaches only to the end of its own paragraph — and **only when it carries a hiding attribute** … does it carry a declaration out of sight."* `<script>` carries nothing out of sight by attribute; it does so by element type, and its raw-text mode does **not** end at its paragraph — measured, the field two paragraphs later is inside it.

*Requires:* a **validator change** (condition-1 elements, and raw-text elements generally) **and an instrument amendment** (§9's condition-7 clause is false as written). **Offer-blocking, and it blocks the formal administration.**

### RD44-04 — MAJOR — the table-row rule blanks any line with pipes, so a `| <div style="display:none"> |` line hides the field and the verdict at **0 errors**

`[Observed]` `_TABLE_ROW_RE = \|.*\|[^\S\n]*$` matches any line containing two pipes with the last at end-of-line, table or not, and sets `_bare = ""` so no tag on it is read at all. A single such line is not a GFM table (no delimiter row), so the renderer treats the `<div>` as inline raw HTML — which under HTML5 closes the paragraph and opens a `div` that swallows everything after:

```
GATE VERDICT: NOT READY

| <div style="display:none"> |

GATE VERDICT: READY FOR Capability 1 — Project registration and honest shape visibility
```

Hidden line ancestry **`['html','body','div[display:none]','p']`**; visible line `['html','body','p']`. CLI `rc=0`, `record valid`, trend `READY FOR Capability 1 — …`. **0 errors.** The same construction with the div *before* the pipes (`<div style="display:none"> | x |`) is correctly refused at 2 — the rule's blanking is what opens the door.

*Requires:* a **validator change** (a table row is a row of a table — a header line with a delimiter row beneath it — not any line with pipes). **Not offer-blocking on falsity grounds** (no §9 sentence asserts this rule); **it blocks the formal administration.**

### RD44-05 — MAJOR — RD43-07 is not closed: the §9 regression claim names a population that four attributions cannot reproduce, and the measurement is false — **five** records move, not one

`[Observed]` §9: *"Across the **54** stored attack records of the RD-39, RD-40, RD-41 and RD-42 rounds, run through both validators, that record is the **only** one whose output moves."* The delta adds *"12 + 4 + 21 + 17 across the four harnesses"*. Four attributions, each with its denominator (fixture-name tags → 15/14/23/19; selftest loop sizes → {2,2,3,4,5,5}; fixtures added per round by version set difference → 16/14/24/19; a `re` sweep of 379 text files → no attack-record files, no derivation anywhere): **none yields 12 + 4 + 21 + 17**.

`[Observed]` And the reproducible form of the claim is false. All **193** captured v1.15 records through both validators against the same instrument at the same commit: **five move** — the mid-sentence `<details>` (0 → 8, disclosed), **`<details/>` in prose (0 → 1)**, **`<div/>` (0 → 1)**, and two LG-4 messages. The two extra error-identity movers are RD-41-round and RD-42-round fixtures — inside the named population — and **the delta's own D-3 table lists both flips**. The Regression section contradicts D-3 four rows above it.

`[Observed]` This lands harder than its v1.15 predecessor for two reasons. The v1.15 sentence lived only in the delta (D-1 row 7: "in §9 too? — **no**"); **this one is in §9**, the bytes an approval digest binds. And the disposition register's RD43-07 row promises the *checkable* sweep — "all captured records through both validators" — which is not what shipped, so the register describes an unshipped repair in the very row closing the finding about unreproducible claims.

*Requires:* a **record correction** in §9 and the delta — state the corpus-wide sweep the register promised, with its five movers and their reasons, or drop the population claim. **Offer-blocking on the §9 sentence**; not independently blocking to the administration.

### RD44-06 — MAJOR — the hiding-attribute list is a second undisclosed enumeration: `visibility:hidden` and `opacity:0` carry a declared field out of sight at **0 errors**, and the English word "hidden" in §5's own shorthand refuses a lawful record

`[Observed]` `_HIDING_ATTR_RE` enumerates `hidden`, `aria-hidden="true"` and `display:none`. §5's fields are contiguous lines of one paragraph, so an inline carrier opened at the end of one field line contains the next. Measured git-on, real digests, with `html5lib`:

| inline carrier on the `Operationalization notes:` line | errors | field's DOM |
|---|---|---|
| `<span style="visibility:hidden">` | **0** | `[…,'p','span[css-hidden]']` |
| `<span style="opacity:0">` | **0** | `[…,'p','span[css-hidden]']` |
| `<span style="display:none">` *(control)* | 1 | hidden |
| `<span hidden>` *(control)* | 1 | hidden |
| `<span aria-hidden='false'>` *(control)* | 0 | visible |

`[Observed]` In the refusing direction the same regex is too wide: `(?:^|\s)hidden(?:\s*=|\s|/?$)` matches the ordinary English word. `Materials given: the fixed §2 list <see the hidden appendix>, no deviations` — §5's own angle-bracket shorthand, rendered fully visible — scores **1 error**, `LG-12: required §5 field missing — 'Operationalization notes:'`, because the inline region swallows the next field line. `<plus the hidden parameter block>` and `<none hidden>` likewise; `<plus the parameter block>` is 0.

`[Observed]` §9 states the three-attribute list as sufficient (*"only when it carries a hiding attribute (`hidden`, `display:none`, `aria-hidden`) does it carry a declaration out of sight"*). Residual 2 names the condition-6 set as an enumeration and says nothing about this one.

*Requires:* a **validator change** (both directions) **and an instrument amendment** or at minimum a residual — §9 asserts sufficiency that two constructions falsify. **Offer-blocking on the §9 clause; it blocks the formal administration** in the refusing direction, because `<…>` shorthand is what §5's own template writes.

### RD44-07 — MINOR — three counts in the shipped bytes that do not survive their own method

`[Observed]` (a) The delta: *"Three v1.15 fixtures are flipped rather than added …, and **one is renamed** to say what it measures."* Measured by set difference of printed fixture names: 3 flipped ✔, **five renamed** (the `div`, `p`, `span`, `table`, `uppercase details` carriers, all with unchanged assertions). (b) §9 and the delta: *"**all twelve** failing exactly the fixtures their repair added."* Measured: n3 fails 15 of which **7 pre-date this batch**, n12 fails 16 of which the **same 7** do. The denominators are exact; the characterisation is not. (c) The selftest prints `note  git unavailable — 3 git-dependent fixtures skipped`; **12** are (205 in a repo, 193 outside).

*Requires:* a **record correction** (a, b) and a **validator change** (c, one string). **Not offer-blocking.**

### RD44-08 — MINOR — two shipped fixtures name a repair they do not witness, in the batch that says it hunted exactly this

`[Observed]` Of the 26 new-or-renamed fixtures, **7** are broken by none of the twelve reverts. Two of those are substantive: the three `…autolink at the start of a line opens no region (RD43-03)` fixtures pass unchanged under **n5** (autolinks read as tags), because their carrier is a paragraph continuation and the condition-7 layer saves them independently; and `an inline <span hidden> DOES carry its field out of the reader's sight (RD43-01)` passes under **both** n6 and n7, because its span sits at the start of its own line and the older line-initial rule refuses it regardless of the inline rule it names. The delta's twelve-witness claim is unaffected and true; the claim that this is *"the first batch of this chain with no unwitnessed repair"* sits awkwardly beside its own residual 3, which names two clauses that remain unwitnessed.

*Requires:* a **record correction** and, if the batch wants the claim, a separating construction per fixture. **Not offer-blocking.**

## Falsification notes — what I tried that did **not** break it

`[Observed]` Each is an execution at `186d90b4`, git checks **on**, against the real committed instrument and §8 digests, with the rendered HTML and the `html5lib` DOM checked wherever the claim was about a reader.

- **RD-43's own four carriers, and a fifth of mine.** Indented-code close, backslash escape, mid-line `<div style="display:none">`, split tag, and a code span in front of a mid-line div — all five now **2 errors**, all five confirmed by DOM ancestry to be genuinely hiding. The repair is real, and its direction is right.
- **Text-that-renders-as-text, four ways, both directions.** A `</details>` inside a fenced block, entity-encoded as `&lt;/details&gt;`, inside an HTML comment, and in a code span each leave the element open in the render and the record refused — correct, and matching `pandoc`. `</details >` with a space still closes and is still accepted, correctly.
- **Element nesting attacked directly.** Mismatched close order (`<div><span>` … `</div></span>`) is accepted — and the render agrees: `html5lib` closes the `div`, the field is at `body > p`. A close naming nothing leaves the region open and is refused; uppercase `<DETAILS>` is refused; a close tag split across two lines does not close and is refused. Every one agrees with the render.
- **The lawful-record battery, eleven constructions, all 0 errors:** closed `<details>` appendix, closed `<table>` appendix, `<br>` in prose, a line beginning with `<hr>`, a line beginning with `<img src=… alt=…>`, `` `<details>` `` in a code span in prose, `<details>` in a table cell, CRLF throughout, a bold field label, `\<details\>` escaped in prose, and `<plus the parameter block>` — the accepting direction the batch built the inline rule for.
- **The autolink exclusion, four shapes plus the separating case** — all 0, all confirmed to render as links.
- **The G1 repair, eight forms** — five accepted, two controls accepted, the trailer-only control still refused.
- **The hiding-attribute controls** — `display:none`, `display : none` spaced, `hidden`, `aria-hidden='true'` refused; `aria-hidden='false'` and a bare `<span>` accepted. The regex is right on every form it enumerates.
- **CommonMark conditions 2–5** — a processing instruction, a bare declaration and a CDATA opener each become comment nodes with the field still visible at `body`, and the validator accepts. No disagreement.
- **`<pre>`, `<textarea>`, `<template>`, `<noscript>`** mid-line — content visible in the render, validator accepts. Agrees.
- **The measurement apparatus, mutated first.** My initial n3 and n12 reconstructions measured 4 and 0; both were my error, not the batch's. I record them because the delta's one-line revert descriptions are terse enough that a reviewer lands on the wrong reading, and reporting "n12 fails 0 of 205" would have been a false BLOCKING finding.
- **`check_governance.py`** — 30 OK, 18 WARN, 0 FAIL (48 checks); `--selftest` 121 fixtures, 0 failing. **`--selftest` in a clone** — 205 fixtures, 0 failing, before and after every mutation run.

## Overall assessment

The records work in this batch is the best in the chain, and I want that on the record before the rest. **Every one of the twelve mutation-revert denominators reproduces exactly** — including the two the batch says it had to build new fixtures for, and I verified that each of those two is witnessed *only* by the fixture built to separate it. §1–§8 are byte-identical at all eight claimed byte counts across ten versions. The frozen v1.15 §9 entry, stripped of its six markers, is byte-for-byte the frozen prose — the D-10 convention and verification rule 10 held under a check designed to catch a silent edit. 187 + 18 = 205 reconciles to the fixture-name set difference exactly, with the flips and renames identified. The `0 of 185` comment is gone and *no* denominator is quoted in the validator at all. And the method the batch adopted is the right method: `pandoc` plus an HTML5 parser is the correct ground truth, `lxml.html` was the wrong one, and the batch used it to falsify two of its own claims that no reviewer had challenged. That is the durable part, and it is real.

But the method was adopted and then not applied to the rule it was used to justify. §9 now says, in the bytes an approval digest would bind, that *CommonMark's own start condition 6 names the elements that open a region from any position, including mid-paragraph*. Three lines of `pandoc` falsify it: a mid-line `<div>` opens no block, and the `*emphasis*` after it is still emphasis. Condition 6 is a line-initial condition like all seven; what the batch actually implemented is HTML5's list of start tags that close an open `<p>`, and closing a paragraph is not opening a region. The cost, swept with its denominator: **53 of the 62 names in `_COND6`, mentioned once mid-sentence in a reviewer's own G1 section, blank the rest of a lawful record — the declared fields, the G1 section and the terminal verdict — and all 53 scored 0 errors at v1.15.** That is RD43-03's harm, widened from three shapes to fifty-three, in the batch that closed RD43-03; and the LG-6 message the register promised to repair — "with the line that opened it named" — did not ship, so the administrator is still told their column-0 visible verdict "sits inside a container opened on an earlier line."

In the other direction the news is worse, because it is RD42-02 and RD43-02 for the third consecutive round. **Four independent constructions produce `record valid`, exit 0, and a trend row reading `READY FOR Capability 1 — Project registration and honest shape visibility` while the record's last visible line reads `GATE VERDICT: NOT READY`**: a mid-line `<script>`; a mid-line `<style>`; an indented-code `</details>` placed after an ATX heading instead of a paragraph; and a lone pipe-delimited line carrying a `display:none` div. The first two are CommonMark's condition 1, which the new model does not mention at all — and they falsify §9's condition-7 clause directly, because `<script>` carries content out of sight by element type, not by attribute, and its raw-text mode does not stop at the paragraph. The third is the batch's own indented-code repair, defeated by `para_open` treating a heading as a paragraph. The fourth is the table-row rule blanking any line with two pipes. Beside them, `visibility:hidden` and `opacity:0` carry a declared field out of sight at 0 errors, while the English word "hidden" inside §5's own `<…>` shorthand refuses a lawful record.

And RD43-07 is not closed. The unreproducible "37 stored attack records (21 + 12 + 4)" was replaced by "54 stored attack records … 12 + 4 + 21 + 17 across the four harnesses" — which four independent attributions and a 379-file sweep cannot reproduce, whose "exactly one record moves" I measured as five, whose two extra movers the delta's own D-3 table lists four rows above, and which this time is written into §9 rather than left in the delta. The disposition register's row for that finding promises the corpus-wide sweep that *would* have been checkable, and that is not what shipped — which is RD43-05's defect recurring inside the row that closes RD43-07.

The sentence I would put in front of the v1.17 batch is the one RD-43 wrote, with one word changed: **decide the block phase first, and decide where a block *begins* the way the renderer decides it.** A region begins at a line, not at a `<`. `<script>`, `<style>`, `<pre>` and `<textarea>` are condition 1 and need their own rule. `para_open` must mean *a paragraph is open*, not *the last line had characters on it*. A table row is a row of a table. And the hiding-attribute list is an enumeration exactly as the condition-6 list is — say so, or stop asserting sufficiency. Then re-measure the accepting direction with a fixture per lawful shape, because for three rounds running the accepting direction is where this validator has broken, and this round it broke fifty-three ways with 205 fixtures that could not tell.

On the two questions asked, in these words:

- **May v1.16 be offered to the owner at P-34?** **No.** The arithmetic reconciles from the source in every place I checked, the mutation discipline is exact, the frozen record was not edited, and §1–§8 have not moved in nine amendments. But sentences inside §9 — the bytes an approval digest binds — are again false of those bytes: that CommonMark's start condition 6 opens a region from any position (three lines of `pandoc` say otherwise, and 53 of 62 names refuse a lawful record because of it); that a condition-7 element carries a declaration out of sight *only* when it carries one of three named attributes (`<script>`, `<style>`, `visibility:hidden` and `opacity:0` say otherwise); and that across the 54 stored attack records exactly one moves (the population is unidentifiable and the count is five). On the RD38-02 / RD39-02 / RD40-01 / RD41-03 / RD42-01 / RD43-01 precedent this batch itself invokes in its own six dated markers, **the digest v1.16 would bind is not the digest that should be approved.**

- **May the formal launch administration run on this validator?** **No.** Four independent constructions produce a clean `record valid`, exit 0, and a nine-column trend row reading `READY FOR Capability 1 — Project registration and honest shape visibility` while the decisive content sits inside a `script`, a `style`, a collapsed `<details>` or a `display:none` div — and every one of them is a record whose **last visible line reads `GATE VERDICT: NOT READY`**. Against them sit lawful records the validator now refuses with messages untrue of them: any record whose G1 section, materials list or operationalization note names `<p>`, `<td>`, `<li>`, `<summary>`, `<table>` or fifty other element names in passing, and any record using §5's own angle-bracket shorthand with the word "hidden" in it. Any one of these, at Administration 1, becomes the baseline every later F1 verdict is read against.

VERDICT: REVISE