All measurements complete. The clone is porcelain-clean at close with the three subject digests unchanged.

---

# RD-43 — Launch-gate instrument re-review, v1.15 exact bytes (round-2026-08e, frozen commit `4fd4a58`)

- **Review id:** RD-43 (eleventh administration of the instrument re-review chain: RD-33 → v1.6 … RD-42 → v1.14)
- **Date:** 2026-08-11
- **Reviewer:** isolated fresh-context session, Claude family. Same-family re-review — the caution the instrument's own **F5** records applies to me. I authored no byte under review.
- **Clone:** `…/scratchpad/clone-08e-r23`, HEAD `4fd4a583634b44deb8ef7cae10367791acc01324`. `git status --porcelain` **empty at open and at close** (0 lines). One `scripts/__pycache__` was created by a Python import during the session and removed at close; **zero `.pyc`/`__pycache__` under the clone at close**. Every mutant, synthetic record and harness lives in `…/scratchpad/rd43/`. Nothing under `/home/tze/GitHub/syzygy` was read, written, or executed.

## Materials read in full, and digests verified

Verified with `sha256sum` at open and again at close, byte counts by `stat`:

| artifact | sha256 | bytes | matches charter |
|---|---|---|---|
| `launch-gate-pre-specifications.md` (1488 lines) | `a3e5a4e711cccaceea7fa76e624a7909707ea68fe73d6d268fae4ee06faf0943` | 89336 | ✔ |
| `scripts/launch_gate_results.py` (2810 lines) | `2606db6c30a51c5cd0aad03a92982406c15e9d58d6e58b9153eb11a505116e09` | 146419 | ✔ |
| `round-2026-08e/LAUNCH-GATE-v1.15-SEMANTIC-DELTA.md` (298 lines) | `f76fef50da423ef567835295abb73c1b33d812ea026fa030ddd88b8012ccdadd` | 17692 | ✔ |

Also read in full: `reviews/RD-42-instrument-v114-RAW.md` (373 lines, 13 findings, `VERDICT: REVISE`); the RD-42 section of `reviews/DISPOSITION-REGISTER.md` including every disposition row and the accepted nit; `decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` (P-34); the launch-gate rows of `PROJECT-STATUS.md`; `AGENTS.md`'s ten verification rules; the frozen `LAUNCH-GATE-v1.14-SEMANTIC-DELTA.md`; instrument §5 and §9's v1.13, v1.14 and v1.15 entries line by line; and the whole of the v1.15 validator's `_own_flags`, `_active_lines`, `_strip_code_spans`, `_takewhile_before_heading`, `_carriers`, `_decl`, and the LG-1/LG-4/LG-6/LG-12 paths. The v1.14 validator was reconstructed from `git show 47adfa9:scripts/launch_gate_results.py` in Python (never through a shell pipe — RD-42's recorded truncation hazard): 2583 lines, sha256 `e861ec38564042caf51bcd42536a0694690d1232f46c9085ecfdb7715eeb9c20`, matching RD-42's measurement exactly.

## Method — what I ran

`[Observed]` `python3 scripts/launch_gate_results.py --selftest` in the clone → **`187 fixtures, 0 failing`**, exit 0. Counted from the tool's own output: **187 `pass` lines, 0 `FAIL` lines**, 188 output lines. Cross-checked a second way by instrumenting the module: **193 `validate()` invocations** (181 with `_git=False`, **12 with `_git=True`**), 187 of which print a fixture line, 6 fixtures issuing two calls.

`[Observed]` **The git-skip hazard the charter named, measured.** The same file run from a non-git directory prints **`175 fixtures`** — exactly the 12 `_git=True` fixtures silently absent. **Every mutant below was therefore run inside a git repository** (a `cp -a` copy of the clone at the same HEAD, restored with `git checkout` after each run), and every denominator I report is **187**, verified by the unmutated control printing `187 fixtures, 0 failing` in that copy.

`[Observed]` A record generator built from the validator's own `GOOD` template with `REPO` bound to the clone, so LG-1/LG-2/LG-11 and both citation-existence paths executed **git-on against the real commit `4fd4a58`, the real committed instrument digest `a3e5a4e7…`, the real §8 digest `01209c0f…` and the real `effective_version: v1.15`** on every construction below. ≈70 synthetic records; the decisive ones re-run through the clone's own CLI so the trend row and exit code are read, not inferred.

`[Observed]` **Mutation-revert testing (rule 6):** 13 reverts rebuilt from the delta's D-2…D-8 descriptions, plus 9 alternate readings where the first reconstruction disagreed; each run's *output* read (FAIL lines), never its exit code.

`[Observed]` **Cross-version execution:** every captured fixture — record bytes, `--prior` bytes and `_git` flag alike — run through both validators, comparing **error count, error identity and the trend row**.

`[Observed]` **Rendering ground truth.** Every carrier claim below was rendered with `pandoc -f gfm` and `-f commonmark`, and the resulting DOM ancestry of the hidden field computed with `lxml.html`. A claim about "what a reader sees" is a measurement here, not an inference.

`[Observed]` Repo-wide sweeps with Python `re`, never shell grep. Denominator **377** text files.

`[Observed]` `python3 scripts/check_governance.py` → **30 OK, 18 WARN, 0 FAIL (48 checks)**; `--selftest` → **121 fixtures, 0 failing**.

`[Unknown]` I did not administer the gate and read no pilot record content. All answer sets are synthetic.

## Per-finding verification — all thirteen RD-42 findings

| RD-42 | Class | Status | Evidence in the v1.15 bytes |
|---|---|---|---|
| **RD42-01** | BLOCKING | **closed for every carrier RD-42 constructed; the class survives out four new doors — RD43-01** | `_own_flags` now carries `html_stack`; `<div>`, `<p>`, `<span>`, `<table><tr><td>` and the code-span reopen each move **0 → 1** (or 0 → 2) on my own git-on constructions and on the shipped fixtures. `m1` (whole limb back to the two-tag counter) fails **10 of 187**, `m3` (code spans unstripped) **2**, `m12` (self-closing opens) **1**, `m13` (void set emptied) **1** — all measured. The repair is real. But the region still does not begin or end where a reader sees it: an indented-code `</details>`, a backslash-escaped `\</details>`, a mid-line `<div style="display:none">`, and an opening tag split across two lines each produce a **0-error `READY FOR`** record whose decisive field's DOM ancestor is `details` or `div[display:none]`. RD43-01. |
| **RD42-02** | BLOCKING | **not closed** | The shipped fixture closes the code-span form. The identical laundering runs through the indented-code close: visible terminal `GATE VERDICT: NOT READY`, hidden `READY FOR Capability 1 …` — **0 errors, `record valid`, exit 0**, trend row `READY FOR Capability 1 — Project registration and honest shape visibility`. RD43-02. |
| **RD42-03** | BLOCKING | **verified-closed** | Enumerated mechanically with `ast`, not by eye: **11 textual `_decl(` occurrences, 1 definition, 10 call sites, all 10 passing `_own_text`** — D-3's denominator and its method both reproduce. Construction: `Parameter block sha256:` present only inside `<div>` below the terminal verdict → v1.14 **0**, v1.15 **1** (`LG-1: no parameter-block sha256 recorded`). D-3's own table row (wrong hidden digest) reproduces exactly: v1.14 `LG-2 parameter-block digest mismatch`, v1.15 `LG-1 no parameter-block sha256 recorded`. `m6` → **1**. |
| **RD42-04** | BLOCKING | **verified-closed** | Thirteen reverts, twelve witnessing, measured at denominator 187 (table in the honesty audit). §9's denominator list `10, 3, 2, 3, 1, 1, 1, 1, 1, 2, 1, 1` has **exactly twelve entries for twelve witnesses** — the "fourteen entries for thirteen witnesses" defect is gone. `m4` fails **0 of 187** and is disclosed at D-8 rather than counted. |
| **RD42-05** | BLOCKING | **verified-closed** | My own wrap-tolerant pattern `\[corrected\s+2026-08-\d\d,\s+(RD\d+-\d+)` over each entry's span: **v1.14 entry 5** (RD42-05, RD42-01, RD42-06, RD42-03, RD42-04), **v1.13 entry 5** (RD41-01, RD41-06, RD41-02, RD41-03, RD41-04). A one-line pattern returns **4 and 3** — exactly as the delta states, with its method stated. §9's v1.15 entry says "five" and names five. |
| **RD42-06** | BLOCKING | **verified-closed** | The three restoration fixtures are rebuilt **above** the terminal verdict (confirmed in the diff: `good.replace("GATE VERDICT:", …)`), and both repairs now have witnesses: **`m9` (raw-side call reads un-stripped text) → 1**, the fenced-`<details>` fixture; **`m10` (setext applied to the terminal rule) → 1**, the `---` fixture. §9's sentence carries a dated marker correcting "four … each 1 → 0" to "true of one of the four". |
| **RD42-07** | MAJOR | **closed in the refusing direction; the repair withdraws five lawful G1 forms, undisclosed — RD43-04** | Bare `## G1 — completeness critic` in §5's own position: v1.14 **0**, v1.15 **1** (`opens an EMPTY section`). `m7` → **1**. But G1 content written as a bulleted list, a numbered list, a blockquote, a fenced block, or indented as code each move **0 → 1** with the same message, which is untrue of those records. RD-42 named this hazard in the same finding ("the same trailer lines carry the check"). |
| **RD42-08** | MAJOR | **partially closed** | The message is repaired and is now true of the record: `LG-12: the 'Materials given:' field's value '<redacted>' is written entirely inside angle brackets, which is §5's template form and not an answer … If this is a real answer, write it without the enclosing brackets`. The *withdrawal itself stands*: `<redacted>`, `<none>`, `<as listed in §2>`, `<see appendix A>` are each still 1 error. The delta discloses the trade-off at D-7 and I verified the measurement behind it (four of the five values in the RD41-01 exploit fixture are abbreviations, so literal matching would reopen it). **But the disposition register's RD42-08 row still asserts the un-shipped repair, including "so `<redacted>` and `<none>` are answers again" — false of the bytes.** RD43-05. |
| **RD42-09** | MAJOR | **closed for all three constructions; the class recurs through the new trigger — RD43-03** | Measured on the fixtures' own bytes: `<details>` mid-paragraph **8 → 0**, `` `<summary>` `` in a code span **8 → 0**, `<details>` in a table cell **1 → 0** — §9's "8, 8 and 1" reproduces exactly. But a line *beginning* with a CommonMark autolink (`<https://…>`, `<owner@example.com>`) or any `<word …>` shorthand now opens an unterminated region: **0 → 8 errors**, with LG-6 telling the administrator their column-0 terminal verdict "sits inside a quotation container — inside a container opened on an earlier line". |
| **RD42-10** | MINOR | **verified-closed** | D-1 #6 moves the setext entry off the *Movement* axis; the v1.15 delta carries no movement axis for it. Re-measured: `Materials given:` followed by `---` is 1 error at both versions. |
| **RD42-11** | MINOR | **verified-closed** | One `_G1_HEADING_RE` (`#{1,6}` + `[^\S\n]+` + `G1`) and one `_ATX_RE`, used in all three places. `###G1 was considered elsewhere.` now yields `LG-4: no G1 section` rather than `opens an EMPTY section`. `m8` → **1**. |
| **RD42-12** | MINOR | **verified-closed as disclosure** | Reproduced: banner deleted from the body, quoted in an appendix headed "quoted for reference only" → **0 errors**; control (banner deleted, no appendix) → **1**. Named in §9 and in the delta's residual 4. |
| **RD42-13** | MINOR | **verified-closed as disclosure** | Reproduced: 1500-deep nested list → **5.97 s**; 2000-deep blockquote → 0.00 s. Named in §9 and in the delta's residual 5. |

**Tally, with its denominator:** of RD-42's **13** findings, **13 are present in the v1.15 bytes and none is absent**; **8 are closed outright** (03, 04, 05, 06, 10, 11, 12, 13); **2 are closed for everything the finding constructed, with the class surviving another carrier out** (01, 09); **1 is closed in its refusing direction and opens an undisclosed withdrawal** (07); **1 is partially closed** (08); **1 is not closed** (02). **Twelve of the thirteen claimed mutation-revert denominators reproduce; the thirteenth (m4) reproduces at 0, exactly as disclosed.**

## Honesty audit of the batch's own measurements

`[Observed]` **Fixture count and arithmetic — honest, and reconstructed from the source rather than the delta's table.** Printed `187 fixtures, 0 failing`; 193 instrumented `validate()` calls. The v1.14 validator, rebuilt from git and run **inside a git repository**, prints `168 fixtures, 0 failing`. The set difference of printed fixture names is **exactly 19 new and 0 removed or renamed**, and the 19 partition precisely into the delta's itemization: 5 carriers + 4 (one-line, closed appendix, self-closing, void) + 2 (code span, close-that-pops-nothing) + 1 laundered verdict + 1 hidden parameter digest + 1 bare `## G1` + 1 angle-bracket message + 3 RD42-09 acceptances + 1 `###G1` = **19**. 168 + 19 = 187 ✔

`[Observed]` **The thirteen mutation-reverts.** Rebuilt from D-2…D-8's own descriptions, run in a git repo, measured by reading FAIL lines:

| revert | claimed | measured | fixtures broken |
|---|---|---|---|
| m1 whole HTML limb → v1.14 counter | 10 | **10** | 4 carriers, code-span, close-pops-nothing, laundered verdict, 3 × RD42-09 |
| m2 line-initial open / top-of-stack close | 3 | **3** † | `table` carrier, one-line carrier, closed-`<details>` appendix |
| m3 code spans not stripped | 2 | **2** | code-span fixture, laundered verdict |
| m4 raw-HTML line is own text again | **0** | **0** | none — disclosed at D-8 |
| m5 a tag anywhere opens a region | 3 | **3** ‡ | contains-brackets acceptance, `<details>` in prose, `<details>` in a table cell |
| m6 tenth `_decl` site reads raw text | 1 | **1** | hidden `Parameter block sha256:` |
| m7 declared trailer counts as G1 content | 1 | **1** | bare `## G1` |
| m8 G1 regex drops the required space | 1 | **1** | `###G1` |
| m9 raw-side call reads un-stripped text | 1 | **1** | fenced `<details>` example |
| m10 setext applied to the terminal rule | 1 | **1** | `---` after the verdict |
| m11 HTML comments not stripped | 2 | **2** § | inline-comment lawful record, comment mentioning `<details>` |
| m12 self-closing tags open a region | 1 | **1** | `<div/>` |
| m13 void-element set emptied | 1 | **1** | `<br>` |

† my first reading (only line-initial tags read, close pops the top) measured **2**; "pops only if it names the top" measures **3**. ‡ widening the whole `_raw_html_line` predicate measures **7**; widening only the *open trigger* measures **3**. § removing all comment handling measures **1**; removing only the single-line `<!--…-->` substitution measures **2**. In each case a faithful reading of the delta's wording reproduces the claim — I record the alternates because the descriptions are terse enough that a reviewer can land on the wrong one. **Measured multiset for the twelve witnesses = `{10, 3×2, 2×2, 1×7}`; §9's list = `{10, 3, 2, 3, 1, 1, 1, 1, 1, 2, 1, 1}` — identical, with twelve entries for twelve witnesses.** ✔

`[Observed]` **The denominators were honest about the git hazard.** Every revert measures against **187** when run inside a repository; outside one the corpus silently shrinks to 175. Nothing in the delta's arithmetic depends on the shrunken figure.

`[Observed]` **§1–§8 identity, computed not transcribed.** Per-section sha256 with a fence-aware splitter, `git show 47adfa9:` vs the working file, **denominator 10 sections**: §1…§8 **all eight byte-identical**, at exactly **794 / 4388 / 15377 / 5688 / 3601 / 2192 / 1038 / 6610** bytes — the delta's figures reproduce to the byte. Only `HEADER` (2915 → 2915) and §9 (38097 → 46733) differ.

`[Observed]` **The moved bytes are exactly the three the delta names.** The HEADER diff is **one line** (`effective_version: v1.14` → `v1.15`). The §9 diff is **131 added lines and exactly 5 modified lines, 0 deletions** — the five modified lines are the five marker insertion points inside the v1.14 entry, and nothing in the v1.13 entry moved. ✔

`[Observed]` **Version constancy, swept at every commit.** Combined §1–§8 digest computed at all **13** commits that have ever touched the instrument: identical at **v1.7…v1.15 — nine versions, eight amendments** ✔. §8 recomputed with the validator's own `param_block_bytes` at every commit: **6610 bytes, `01209c0f…`, constant at v1.5…v1.15 — eleven versions** ✔; **three** distinct §8 digests in history ✔.

`[Observed]` **The D-2 and D-3 attack-record tables reproduce against the stored fixtures.** The four carriers each 0 → 1 `LG-12 no E3 reopen-list:`; the code-span reopen 0 → 2 (`LG-6` + `LG-12`); the uppercase-`<DETAILS>` control 1 → 1. D-3's row reproduces exactly on a git-on construction.

`[Observed]` **Cross-version execution of the whole corpus — the two-layer-trap hunt, verified.** All **193** captured records (record bytes, prior bytes and `_git` flag preserved) run through both validators, comparing error count, error identity and trend row: **15 move**. Fourteen are v1.15's own new fixtures; the fifteenth is the RD41-01 placeholder record, whose *message* changed by D-7's design. **No pre-existing fixture silently changed behaviour**, and no v1.15 fixture is inert against the repair it names — every one of the 19 is broken by at least one of m1…m13 except the disclosed `m4` guard, which the batch labels as defence-in-depth *in the fixture's own name*. The trap RD-42 found in three of last round's fixtures is not present in this one. This is the best discipline in the batch.

`[Observed]` **A count in the shipped bytes that was not recounted.** The validator's own comment at line 2684 reads *"alone kills **0 of 185** (mut15 m4)"*. The corpus is 187; §9 and the delta both say 187. RD43-06.

`[Observed]` **The "37 stored attack records" claim is not checkable from the repository.** No such records exist as files, and the split "21 + 12 + 4, across the three harnesses" matches no structure I can find: attributing all 187 fixtures to their round blocks by caller line number gives RD-39 **15**, RD-40 **13**, RD-41 **23**. The delta's closing section asserts the opposite — *"Every record cited above is stored as a fixture … checkable from the repository alone"* — which is the very nit the disposition register accepted from RD-42. RD43-07.

`[Observed]` **Stale-version sweep.** 377 text files; **126** lines carry both a launch-gate token and a `v1.x` token across **35** files. Of the routed artifacts, all 23 non-v1.15 hits are historical delta-path references in §9's changelog, P-34's amendment history, and P-34's own row in PENDING. **No routed artifact names a stale effective version.** ✔ P-34 and PROJECT-STATUS both carry `187`, `thirteen`, `twelve of thirteen` — RD-42's "fourteen of sixteen" is gone from both.

`[Observed]` **The disclosed-limits section, checked sentence by sentence.** Residual 1 (m4 = 0 of 187) exact. Residual 3 (blockquote laziness) unchanged and re-verified. Residual 4 (RD42-12) reproduces. Residual 5 (RD42-13) reproduces at 5.97 s. Residual 6 (`**Label:*`, the trend row above the error list) reproduces. **Residual 2 is the one that is materially incomplete** — RD43-03.

## New findings

### RD43-01 — BLOCKING — the raw-HTML region still does not begin or end where a reader sees it: four working carriers, each supplying `E3 reopen-list: empty` from content whose DOM ancestor is `<details>` or `<div style="display:none">`, at **0 errors**, `record valid`, `READY FOR <the verbatim target>`

`[Observed]` All four executed at `4fd4a58`, git on, real digests, full 39-row roster, through the clone's own CLI; each rendered with `pandoc -f gfm` and `-f commonmark` and the hidden field's DOM ancestry computed with `lxml.html`.

**(a) A close tag written as an indented code block.** The region's closer renders as escaped text, so the element never closes:

```
<details>
<summary>Appendix — quoted for reference only</summary>

Nothing in this appendix is an answer.

    </details>

E3 reopen-list: empty
```

```
$ pandoc -f commonmark -t html
<details>
<summary>Appendix — quoted for reference only</summary>
<p>Nothing in this appendix is an answer.</p>
<pre><code>&lt;/details&gt;
</code></pre>
<p>E3 reopen-list: empty</p>
```

`lxml.html` ancestry of the field: **`['details', 'body', 'html']`**. Validator: **v1.14 0 errors, v1.15 0 errors**, trend row `READY FOR Capability 1 — Project registration and honest shape visibility`, `record valid`, exit 0.

**(b) A backslash-escaped close tag.** `\</details>` renders as literal text (`\<` is a CommonMark escape) and the element stays open; `_TAG_RE.finditer` finds `</details>` at offset 1 and pops. **0 errors at v1.15.**

**(c) A mid-line opening tag.** `Note that the appendix below is not an answer. <div style="display:none">` — the raw `<div>` is emitted into the output, and under HTML5 parsing it closes the open `<p>` and swallows everything after. `lxml.html` ancestry of the field: **`['div[display:none]', 'div', 'html']`**. Validator: **0 errors** at both versions, because the region trigger requires the line to *begin* with a tag. The same works with a code span in front (`` `see below` <div style="display:none"> ``), which the code-span strip cannot help with.

**(d) An opening tag split across two lines.** CommonMark's HTML-block start condition 6 is satisfied by `<div` followed by end-of-line, so the renderer emits the whole thing as raw HTML; `_TAG_RE` requires the `>` on the same line and sees no tag at all:

```
<div
 style="display:none">

E3 reopen-list: empty
```

```
$ pandoc -f gfm -t html
<div
 style="display:none">

<p>E3 reopen-list: empty</p>
```

`lxml.html` ancestry: **`['div[display:none]', 'body', 'html']`**. Validator: **0 errors**, `record valid`, exit 0, trend row `READY FOR Capability 1 — Project registration and honest shape visibility`.

`[Observed]` **This falsifies D-2's own justification and §9's implicature.** D-2: *"Element nesting is the reader's model, so element nesting is the predicate's."* §9: *"a close tag pops back to the element it names and pops nothing if it names none, so `<table><tr><td>` … `</td></tr></table>` **closes where a reader sees it close**"*. Measured: the predicate closes where a reader does *not* see it close (a, b) and fails to open where a reader does see it open (c, d). The batch closed the *one* text-that-renders-as-text carrier it knew about — the inline code span — and left the other two (indented code blocks, backslash escapes), and it replaced "a tag anywhere on a line" with "a tag at the start of a line" without measuring what the renderer does with the tags in between.

`[Inferred]` This is RD-41's sentence one level down again, and RD-42's diagnosis is still the right one: **the predicate is not reading the document the renderer produces.** `_active_lines` already knows what a fence is and what a comment is; it does not know what an indented code block is, and `_own_flags` computes markdown containers and HTML elements in one pass over the same lines rather than deciding the block phase first and reading tags only out of what survives it.

*Requires:* a **validator change** — the tag reader must run only over text that survives markdown's own literal-text constructs (indented code blocks and backslash escapes join fences and comments), and the region trigger must match what a renderer emits as raw HTML (CommonMark's start conditions, which include a bare `<div` at end of line, and inline raw HTML in a paragraph). **An instrument amendment**: §9's element-nesting sentence, offered as the reader's model, is falsified by four constructions against the bytes an approval digest would bind. **Offer-blocking, and it blocks the formal administration.**

### RD43-02 — BLOCKING — RD42-02's harm, unclosed: a record whose **visible terminal line reads `GATE VERDICT: NOT READY`** enters the trend log as `READY FOR <the verbatim target>` at **0 errors**, exit 0

`[Observed]` Executed at `4fd4a58`, git on, real digests, full roster, through the clone's own CLI. The record is `ready_real` with its terminal verdict rewritten to `NOT READY`, followed by:

```
GATE VERDICT: NOT READY

<details>
<summary>Appendix — the verdict vocabulary, quoted from §5</summary>

Nothing in this appendix is an answer.

    </details>

GATE VERDICT: READY FOR Capability 1 — Project registration and honest shape visibility
```

```
$ pandoc -f gfm -t html      (tail)
<p>Reviewer's falsification notes: … GATE VERDICT: NOT READY</p>
<details>
<summary>Appendix — the verdict vocabulary, quoted from §5</summary>
<p>Nothing in this appendix is an answer.</p>
<pre><code>&lt;/details&gt;
</code></pre>
<p>GATE VERDICT: READY FOR Capability 1 — Project registration and honest shape visibility</p>
```

```
$ python3 scripts/launch_gate_results.py …/ATTACK-2b.md
rows parsed: 39 (Met 38, Not met 0, scoped 0, Unknown 1) — …
trend row:
| 2026-08-10 | 4fd4a583 | 0 | 0 | 1 | 0 | 0 | n/a — no prior record supplied | READY FOR Capability 1 — Project registration and honest shape visibility |
record valid — verdict semantics remain the instrument's, not this tool's
$ echo $?
0
```

**v1.14: 0 errors. v1.15: 0 errors.** The `<details>` element is never closed in the rendered document, so a reader sees the record end at `NOT READY` followed by a collapsed disclosure widget. `_gv_own[-1]` selects the hidden line because the indented-code `</details>` emptied `html_stack`; `_later` is `[]` because the hidden line is last.

`[Observed]` §9 says of the unicode fold that *"it is the disagreement between a record's bytes and a reader's eyes that this whole instrument exists to prevent"*. That disagreement, in pure ASCII, survives the batch written to close it — a second consecutive round.

*Requires:* the validator change of RD43-01 (this is its terminal-rule consequence), plus a fixture in the silent direction. **Offer-blocking, and it blocks the formal administration.** It is the single most dangerous defect I found, for RD-42's reason: a laundered verdict at Administration 1 becomes the baseline every later F1 verdict is read against.

### RD43-03 — MAJOR — a record line beginning with a CommonMark **autolink** opens an unterminated raw-HTML region and blanks the rest of the record: **0 → 8 errors**, with LG-6 telling the administrator their column-0 terminal verdict is "inside a container opened on an earlier line"

`[Observed]` Executed at `4fd4a58`, git on, real digests. `Operationalization notes:` given a continuation line:

```
Operationalization notes: the trace table was read; see the source below
<https://github.com/gastownhall/beads/blob/main/docs/SYNC_CONCEPTS.md>
```

```
$ pandoc -f gfm -t html
<p>Operationalization notes: the trace table was read; see the source below
<a href="https://github.com/…/SYNC_CONCEPTS.md">https://github.com/…/SYNC_CONCEPTS.md</a></p>
```

The reader sees a hyperlink. `_TAG_AT_START_RE` reads `<https://…>` as an open tag named `https`, pushes it, and nothing ever pops it: **own lines before the autolink: 8; own lines after: 0** (of 54 remaining lines). Measured **v1.14 = 0 errors, v1.15 = 8**, among them:

```
LG-4: no G1 section — an administration missing G1 is incomplete and cannot support a gate decision
LG-5: no `Deferred count:` field …
LG-5: no `Reopened count:` field …
LG-6: every `GATE VERDICT:` line in the record sits inside a quotation container — inside a
      container opened on an earlier line — and a quoted verdict is not the record's verdict …
```

The same happens for an email autolink (`<owner@example.com>`, 0 → 8) and for any angle-bracketed shorthand at the start of a line (`<n>`, `<see appendix A>`, 0 → 8).

`[Observed]` **§9's residual is materially incomplete on two counts.** It says: *"A record line whose own text **begins** with an inline tag is read as raw HTML **and cannot carry a declaration**; §5's fields begin with their labels, and no fixture in the corpus is affected."* First, the consequence is not that the line cannot carry a declaration — it is that **every subsequent line, including the terminal verdict, stops being the record's own**. Second, an autolink is not an inline tag at all; it is CommonMark's bare-URL syntax and renders as a link. "No fixture in the corpus is affected" is true and I verified it; it is also VIS-2's own case — the corpus is the measurement, not the population.

`[Inferred]` This is RD42-09's class returning through the repair that closed it: a lawful record refused with a message untrue of it, on the one line §5 makes decisive. `[Inferred]` A URL or an angle-bracketed shorthand on its own line is a shape a reviewer of *this* instrument plausibly writes — §5's own template writes every unfilled value in angle brackets, and these records exist to discuss it.

*Requires:* a **validator change** (autolinks are not tags; and an unterminated region should not silently blank a record — at minimum it must say so rather than reporting a container the reader cannot see) and an **instrument amendment** — §9's residual sentence understates a measured harm in the bytes an approval digest would bind. **Offer-blocking on the residual sentence; it blocks the formal administration.**

### RD43-04 — MAJOR — D-5's repair silently withdraws five lawful G1 content forms, with a message untrue of the record, undisclosed and unfixtured in its accepting direction

`[Observed]` Measured on identical bytes at `4fd4a58`, git on, real digests, `## G1 — completeness critic` in §5's own position with content beneath it:

| G1 content form | v1.14 | v1.15 | message |
|---|---|---|---|
| bulleted list (`- E5 was not re-read …`) | 0 | **1** | `LG-4: the G1 heading opens an EMPTY section` |
| numbered list (`1. …`) | 0 | **1** | same |
| blockquote (`> nothing further proposed`) | 0 | **1** | same |
| fenced block | 0 | **1** | same |
| indented as code | 0 | **1** | same |
| *control:* plain paragraph | 0 | 0 | — |
| *control:* table | 0 | 0 | — |
| *control:* bold paragraph | 0 | 0 | — |

The cause: `_takewhile_before_heading` now filters out `Label:`-shaped lines, and what remains must additionally be an **own** line. A bullet is inside a list container, a blockquote is `bq1`, a fenced block is stripped upstream, and indented code fails `cind <= 3` — so none of them is "content of the record's own", and the trailer that used to carry the check has been removed. RD-42 wrote the warning in the same finding: *"G1 content written as bullets, as a blockquote, as a table, as a fenced block, or indented as code all validate at 0 errors — **because the same trailer lines carry the check**."*

`[Observed]` A bulleted list is the natural form for a completeness critic's output, and §4's clause the message quotes — *"an administration missing G1 is incomplete and cannot support a gate decision"* — is asserted against a record whose G1 section a reader plainly sees has content. The single fixture shipped for D-5 asserts only the refusing direction; **no fixture in the 187 exercises G1 content in any container**, which is why the withdrawal is invisible to the selftest.

*Requires:* a **validator change** — "content of the record's own" is the wrong test for a *section*, whose content may lawfully be a list, a quote or a code block; and an accepting-direction fixture per form — plus a **record correction** (the delta enumerates six residuals and this is not among them). **Not offer-blocking on falsity grounds** (§9's sentence about LG-4 is literally true of the code); **it blocks the formal administration**, because the reviewer's own G1 section is the likeliest place in the record to be written as a list.

### RD43-05 — MINOR — the disposition register describes two repairs that were not shipped, and is not corrected

`[Observed]` The register's **RD42-08** row: *"The placeholder check matches §5's **actual** placeholder strings, read from the committed instrument at the record's named commit … not the angle-bracket shape — **so `<redacted>` and `<none>` are answers again.** An undisclosed withdrawal becomes no withdrawal at all."* Measured: `<redacted>` and `<none>` are each still **1 error** at v1.15. The register's **RD42-01** row: *"closed **only** by a line whose content begins with the matching close tag … **the depth never decrements below where it was opened**"*. The shipped rule reads every tag on every line inside a region and deletes a stack suffix by name; neither clause is implemented.

`[Observed]` D-7 discloses the RD42-08 change of plan and states the measurement behind it, and I verified that measurement is sound (four of the five values in the RD41-01 exploit fixture are abbreviations of §5's placeholders, so literal matching would reopen it). D-2 states the shipped RD42-01 rule. **The delta is honest; the register is stale**, and the delta routes the reader to it (*"dispositions in `reviews/DISPOSITION-REGISTER.md`"*).

*Requires:* a **record correction** — the register carries dated markers elsewhere and this is its own D-10 convention. **Not offer-blocking.**

### RD43-06 — MINOR — a count in the shipped bytes, written from an intermediate state and never recounted: the validator says m4 "kills **0 of 185**" where the corpus is 187

`[Observed]` `scripts/launch_gate_results.py` line 2684: *"alone kills **0 of 185** (mut15 m4), because every declared-value read is `^`-anchored and the verdict-token scan counts raw lines."* Sole occurrence of a fixture denominator in the file; §9 and the delta both say **0 of 187**, and I measured 0 of 187. This is verification rule 3's own case — a derived value quoted outside its owning artifact going stale silently — inside the one comment whose job is to record the honest measurement, in the batch whose §9 entry says *"this entry states every count with the method that produced it"*.

*Requires:* a **validator change** (one number). **Not offer-blocking.**

### RD43-07 — MINOR — the "37 stored attack records (21 + 12 + 4, across the three harnesses)" regression claim is not reproducible from the repository, in the batch that accepted exactly that nit

`[Observed]` No attack-record files exist in the repository; a `re` sweep of all 377 text files finds "attack record" only in prose. Attributing all 187 fixtures to their round blocks by caller line number gives **RD-39 15, RD-40 13, RD-41 23** — no partition of any fixture population yields 21 + 12 + 4. The delta's closing section asserts *"Every record cited above is stored as a fixture … so the numbers a reviewer is asked to check are checkable from the repository alone — the RD-42 nit accepted in the disposition register"*, and names only the regression *diff* as the exception, on the ground that it is reproducible from the two validators. The two validators are reproducible; **the 37 records are not**.

`[Observed]` The direction of the claim does survive a stronger check that *is* reproducible, and I ran it: all **193** captured records through both validators with priors and `_git` preserved, comparing error count, error identity and trend row — **exactly one pre-v1.15 record moves**, the RD41-01 placeholder record, and it moves only in message text, by D-7's design. Under the broadest reading of "stored attack records from the RD-39, RD-40 and RD-41 rounds", that one record makes *"no record's error identity moved"* false; under a narrower reading the population is unstated and unidentifiable.

*Requires:* a **record correction** — state the population, or replace the sentence with the corpus-wide cross-version sweep, which is checkable. **Not offer-blocking.**

## Falsification notes — what I tried that did **not** break it

`[Observed]` Each is an execution at `4fd4a58`, git checks **on**, against the real committed instrument and §8 digests, with the rendered HTML and DOM checked wherever the claim was about a reader.

- **The element-nesting predicate, attacked directly — fourteen constructions, ten correctly refused and four correctly accepted.** Deep nesting all closed; deep nesting with one close missing; mismatched close order (`<div><span>` … `</div></span>`); a close naming an element opened three lines earlier; a close naming nothing; an attribute containing `>` on the open side *and* on the close side; a tag split across lines *in the closing direction*; `MiXeD` and `UPPER`/`lower` case pairs; a region opened inside a blockquote and inside a list item (both refused, and both genuinely closed in the render). Every one of these agrees with `pandoc`'s output.
- **Text-that-renders-as-text, both directions.** A `</details>` inside a **fenced code block** and one **entity-encoded** as `&lt;/details&gt;` each leave the region open and the record refused — correct, and matching the render. A `</details>` inside an **HTML comment** likewise. A `</details >` with a space before the `>` closes at v1.15 and is genuinely a valid end tag in the render — v1.14 refused it, v1.15 accepts it, and v1.15 is right.
- **A comment as an opening carrier.** `<!-- <div style="display:none"> -->` opens nothing at v1.15 and hides nothing in the render — the comment strip and the reader agree.
- **The lawful-record battery, v1.14 → v1.15, thirteen constructions.** A closed `<table>` evidence appendix; a closed `<details>` appendix; `<br>` in prose; a line beginning with `<hr>`; a line beginning with `<img src=… alt=…>`; a G1 table; a bold field label (`**Materials given:**`); CRLF throughout; a setext G1 title (correctly refused at both). **All score 0 at both versions except the five G1 forms of RD43-04.** The void-element and self-closing carve-outs are correct and fixtured in the accepting direction.
- **The position rule and the tenth `_decl` site.** I could not evade `_decl_end`: a field declared below the terminal verdict is absent in every container I tried, and the parameter-block digest is now no exception. I could not make the rule *over*-reject either — §5's template puts every field above the verdict.
- **The `--prior` path.** All prior-record fixtures behave identically across versions once the prior is passed; my first cross-version run dropped it and produced four spurious movements, which I traced to my own harness rather than to the bytes. Recording it because it is the same shape as RD-42's `git show` pipe hazard: **the measurement apparatus is the thing to mutate first.**
- **The §4 conjunct battery, the roster, the scoped form, the trend row, and `--selftest` in a clone** — 187 fixtures pass, and the recursion cap is unchanged.
- **`check_governance.py`** — 30 OK, 18 WARN, 0 FAIL (48 checks); `--selftest` 121 fixtures, 0 failing.

## Overall assessment

Most of this batch is correct, and two things in it are better than anything in the chain so far. The **records work is clean**: I rebuilt all thirteen mutation-reverts and every claimed denominator reproduces, with twelve witnesses and one honest zero; §9's denominator list has twelve entries for twelve witnesses, ending the miscount that has recurred since RD41-03; the five correction markers are five when counted with a pattern that survives the line wrap, and the delta states the pattern; the ten `_decl` call sites are enumerated by parsing, not by eye, and all ten read `_own_text`; 168 + 19 = 187 reconciles to the fixture-name set difference exactly, with nothing removed or renamed; §1–§8 are byte-identical at the eight byte counts claimed, across nine versions, and §8 across eleven; and the moved bytes are exactly the header line, the appended entry, and five marker insertions — 131 added lines, 5 modified, 0 deleted. And the **two-layer trap is gone**: I ran the whole corpus through both validators and every new fixture is broken by a revert of the repair it names, except the one the batch labels as defence-in-depth *in the fixture's own name*. RD-42's central procedural finding is closed properly.

The engineering finding is not closed, and it is closed less than last round's summary suggests. The batch adopted "an HTML block is a block" and then wrote a tag scanner that runs over the same lines the container scanner runs over, without asking what markdown does to the text in between. So the region opens at a line-initial tag and closes at a named close tag — and markdown has at least four ways to make those two facts disagree with the rendered document. A `</details>` indented four spaces renders as `&lt;/details&gt;` and closes nothing for the reader; the validator pops. A `\</details>` renders as literal text; the validator pops. A `<div style="display:none">` after a sentence is emitted as raw HTML and swallows the rest of the page; the validator sees nothing. A `<div` with its attributes on the next line is CommonMark's own start condition 6; the validator sees nothing. Through each of those doors: `E3 reopen-list: empty` supplied from content whose DOM ancestor is `details` or `div[display:none]`, at 0 errors under `READY FOR <the verbatim target>` — and through the first of them, **a record whose last visible line reads `GATE VERDICT: NOT READY` entering the trend log as `READY FOR Capability 1 — Project registration and honest shape visibility`, `record valid`, exit 0.** That is RD42-02, unmoved, in the batch written to close it.

And the trigger the batch chose to avoid RD42-09 has costs it did not measure. A line beginning with `<https://…>` — a bare URL, CommonMark's autolink, rendered as a hyperlink and containing no HTML at all — opens a region that never closes and takes the whole rest of the record with it: eight errors where v1.14 gave zero, and LG-6 telling the administrator that their column-0, unmarked, visible terminal verdict "sits inside a container opened on an earlier line". §9 discloses this residual as costing one line's ability to carry a declaration. It costs the record. Beside it, D-5's repair — correct in the direction it was written for — withdrew five lawful ways of writing the G1 section, including the bulleted list, with a message that says the section is empty when a reader sees it is not; nothing in the corpus tests G1 content in a container, so the selftest cannot see it.

The sentence I would put in front of the v1.16 batch is one the chain has now earned twice over: **decide the block phase first, then read tags out of what survives it.** `_active_lines` already knows what a fence is and what a comment is. Indented code blocks and backslash escapes belong in the same place, before a single `<` is inspected; the region trigger belongs on what a renderer would emit as raw HTML, not on where the `<` happens to sit in the line; and an unterminated region should say it is unterminated rather than reporting a container the administrator cannot see. Then re-measure the accepting direction with a fixture per lawful shape — a G1 bullet list, an autolink, a URL, a path — because for two rounds running the accepting direction is where this validator has been breaking, and neither round had a fixture that could tell.

On the two questions asked, in these words:

- **May v1.15 be offered to the owner at P-34?** **No.** The records work is honest and the arithmetic reconciles from the source in every place I checked; the mutation discipline is sound; the fixtures no longer witness the wrong layer; §1–§8 have not moved in eight amendments. But sentences inside §9 — the bytes an approval digest binds — are again false or materially incomplete of those bytes: that element nesting is the reader's model and a region therefore "closes where a reader sees it close" (four constructions say otherwise, three of them producing a 0-error `READY FOR`); and that the price of the "begins with a tag" trigger is that such a line "cannot carry a declaration" (measured: it blanks every line after it, and a CommonMark autolink — not a tag — triggers it). On the RD38-02 / RD39-02 / RD40-01 / RD41-03 / RD42-01 precedent this batch itself invokes in its own five dated markers, **the digest v1.15 would bind is not the digest that should be approved.**

- **May the formal launch administration run on this validator?** **No.** Four independent constructions produce a clean `record valid`, exit 0, and a nine-column trend row reading `READY FOR Capability 1 — Project registration and honest shape visibility` while the decisive content sits inside a collapsed `<details>` or a `display:none` div — and one of them is a record whose **last visible line reads `GATE VERDICT: NOT READY`**. Against them sit lawful records the validator now refuses with messages untrue of them: any record with a bare URL or an angle-bracketed shorthand at the start of a line, and any record whose G1 section is written as a list, a quote, or a code block. Any one of these, at Administration 1, becomes the baseline every later F1 verdict is read against.

VERDICT: REVISE