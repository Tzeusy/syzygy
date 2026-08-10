All measurements complete. The clone is porcelain-clean at close (0 porcelain lines, 0 `__pycache__`/`.pyc`) with the three subject digests unchanged.

---

# RD-45 — Launch-gate instrument re-review, v1.17 exact bytes (round-2026-08e, frozen commit `963f1c4`)

- **Review id:** RD-45 (thirteenth administration of the instrument re-review chain: RD-33 → v1.6 … RD-43 → v1.15 → RD-44 → v1.16)
- **Date:** 2026-08-11
- **Reviewer:** isolated fresh-context session, Claude family. Same-family re-review — the caution the instrument's own **F5** records applies to me. I authored no byte under review.
- **Clone:** `…/scratchpad/clone-08e-r25`, HEAD `963f1c4`. `git status --porcelain` **empty at open and at close** (0 lines); **0 `__pycache__`/`.pyc` under the clone at close**. Every mutant, capture, synthetic record and workspace copy lives under `…/scratchpad/rd45/`. Nothing under `/home/tze/GitHub/syzygy` was read, written or executed.

## Materials read in full, and digests verified

| artifact | sha256 | matches charter |
|---|---|---|
| `launch-gate-pre-specifications.md` | `02368c78c190e45b232b3e38d35857d4dae82cfe4f7416d1058de09a7d66dc32` | ✔ |
| `scripts/launch_gate_results.py` | `28bfa9fd8abb517d2be49f8f41c515f36824fd2fc1798f102ca2e8561e3e9289` | ✔ |
| `round-2026-08e/LAUNCH-GATE-v1.17-SEMANTIC-DELTA.md` | `cb4918015c38861d1c04ec5a4ff0991e26c72098dca510ef86aba8d04b33baa9` | ✔ |

Also read in full: `reviews/RD-44-instrument-v116-RAW.md` (291 lines, 8 findings, `VERDICT: REVISE`); §9's v1.13–v1.17 entries line by line; and the whole of `_own_flags`, `_table_row_lines`, `_readable_tags`, `_strip_code_spans`, `_g1_section_content`, `_carriers`, `_opened_by`, `_decl`, `_COND6`, `_RAWTEXT`, `_HIDES_INLINE`, `_HIDING_ATTR_RE`, `_AUTOLINK_RE`, `_SPLIT_TAG_RE`, `_TABLE_ROW_RE`, `_TABLE_DELIM_RE` and the name-loop / `para_open` / table / hiding fixture blocks. The v1.16 validator was recovered as `git show 186d90b:scripts/launch_gate_results.py` and its sha256 is `23502a95…`, matching the digest RD-44 recorded.

## Method — what I ran

`[Observed]` `python3 scripts/launch_gate_results.py --selftest` in the clone → **`288 fixtures, 0 failing`**, read from the tool's printed output (288 `pass` lines, 0 `FAIL` lines). Outside a git repository the same file prints **`276`** — exactly the **12** git-dependent fixtures skipped. **Every mutant and capture below was run inside a git repository** (a `cp -a` copy of the clone at the same HEAD), every denominator I report is **288**, and the unmutated control printed `288 fixtures, 0 failing` in that copy before and after every run.

`[Observed]` A record generator built from the validator's own `GOOD` template with `REPO` bound to the clone, so LG-1/LG-2/LG-11 and both citation-existence paths executed **git-on against the real commit `963f1c40`, the real committed instrument digest `02368c78…`, the real §8 digest `01209c0f…` and the real `effective_version: v1.17`** on every construction below. A `NOT READY` baseline validates at **0 errors** git-on; an all-`Met` roster whose terminal line reads `READY FOR <the verbatim target>` also validates at **0 errors**, so the laundering baseline is lawful in both directions. Every decisive construction was re-run through the clone's own CLI so the trend row and exit code are read, not inferred.

`[Observed]` **Rendering ground truth.** Every claim about what a reader sees is a measurement: `pandoc 2.9.2.1 -f gfm -t html` **and** `-f commonmark`, parsed with **`html5lib 1.1`** (`namespaceHTMLElements=False`), walking to the ancestor chain of the decisive field and flagging `hidden`, `display:none`/`visibility:hidden`/`opacity:*`, `aria-hidden="true"`, uncollapsed `<details>`, the raw-text elements and the HTML Standard's UA-stylesheet `display:none` set. `lxml.html` was not used anywhere.

`[Observed]` **Mutation-revert testing (rule 6):** all nine reverts rebuilt from the delta's own descriptions, each anchor asserted unique before substitution, each run's *output* read (FAIL lines), never its exit code. **All nine reproduced on the first reconstruction.**

`[Observed]` **The uncommitted corpus sweep, rebuilt from the delta's prose alone**, then replayed through both validators.

`[Observed]` Repo-wide reads with Python `re`, never shell grep.

`[Unknown]` I did not administer the gate and read no pilot record content. All answer sets are synthetic.

## Per-finding verification — all eight RD-44 findings

| RD-44 | Class | Status | Evidence in the v1.17 bytes |
|---|---|---|---|
| **RD44-01** | BLOCKING | **closed for the swept population; the class survives out three new doors — RD45-01, RD45-02, RD45-03** | The 62-name sweep, rebuilt git-on with real digests: **56 of 62** refused at v1.16, **2 of 62** at v1.17 (`details`, `title`). 62 − 56 = the 6 void names, so RD-44's "53 refused-but-visible + 6 void + 3 genuine hiders" reconciles exactly, and **54 names move to accepted**. The mid-line rule is right in principle. But `iframe` — one of the **three** RD-44 named as *"genuinely hide and are correctly refused"* — moved with them (RD45-03), and the split-tag limb of "a region begins at a line" was narrowed without disclosure (RD45-01). Second limb (LG-6 naming the opening line): **shipped but wrong** — RD45-05. |
| **RD44-02** | BLOCKING | **verified-closed** | The exact RD-44 construction (indented `</details>` after an ATX heading) moves **0 → 1** error; DOM ancestry of the hidden line `['html','body','details[COLLAPSED]','p']`. `para_open` now excludes ATX headings, thematic breaks, raw-HTML lines, table rows and setext underlines; three fixtures, m4 → 3. |
| **RD44-03** | BLOCKING | **closed for `script`/`style`; the class survives — RD45-03, RD45-04** | Mid-line `<script>` and `<style>` each move **0 → 1**; DOM `['html','body','p','script']` / `[…,'style']`. The raw-text guard works and m3 → 1 on the separating construction the delta describes. But condition 1 is not the whole unpainted set (RD45-03), and the `textarea` residual §9 states is false (RD45-04). |
| **RD44-04** | MAJOR | **verified-closed** | The lone `\| <div style="display:none"> \|` line moves **0 → 1**; `_table_row_lines` computes rows from a delimiter row beneath a header. Both directions hold: a real table row still ends its cell (`\| <details> \|` under a delimiter row → 0 errors, field at `body > p`), and a hiding div inside a *real* row is also correctly inert. m5 → 1. |
| **RD44-05** | MAJOR | **verified-closed, and this is the best records work in the chain** | The unreproducible 54-record population is **withdrawn entirely** in a dated marker, and replaced by a scripted sweep. I rebuilt the uncommitted script from the delta's prose alone — inject a capture line into `case()`, run each version's `--selftest` in a repo, replay every captured record through both validators with its own `_git` — and reproduced **every figure**: 199 / 282 / 200 carried / **0 dropped** / **0 moved** / 82 added / **65 answered differently**. The claim "stated here completely enough to be rebuilt" is true. The six `--prior` fixtures outside `case()` are exactly 205 − 199 = 288 − 282 = 6. ✔ |
| **RD44-06** | MAJOR | **first limb closed; second limb correctly declined — RD45-08 on an edge** | `visibility:hidden` and `opacity:0` each move **0 → 1**, measured with the field at `span[HIDDEN]`; a plain `<span>` in the same position is accepted. m6 → 2. The declined limb is **right**: `<see the hidden appendix>` renders as `see[appendix,hidden,the]` and the next declared field's ancestry is inside it — `hidden` is a global boolean attribute, the field is genuinely out of sight, and the code-span form is accepted at 0 errors. Declining is the correct call and the fixture carries the measurement in its name. Edge: `opacity:.0` and `opacity:0%` are not matched (RD45-08). |
| **RD44-07** | MINOR | **verified-closed** | (a) "one renamed" → **five**, corrected in a dated marker; my own set difference confirms **0 renamed** at v1.17 (all 205 v1.16 names survive verbatim). (b) the twelve-denominator characterisation corrected in a marker. (c) The skip notice now reads *"the git-dependent fixtures (LG-1 …) were skipped"* and quotes **no figure**; the only `205` left in the file is `\u205f` inside `_UNI_WS_RE`, and `\d+ of \d+` matches **zero** times. ✔ |
| **RD44-08** | MINOR | **not closed — RD45-09** | The claim is restated as "**Seven** accepting-direction fixtures are broken by no revert". Measured over the whole population (83 new fixtures × 9 reverts, denominator 288): **eleven**. |

**Tally, with its denominator:** of RD-44's **8** findings, **6 are closed outright** (02, 04, 05, 06, 07, and the declined limb of 06 is well-founded); **2 are closed for every construction the finding made, with the class surviving another carrier out** (01, 03); **1 is not closed** (08). **All nine claimed mutation-revert denominators reproduce exactly, on the first reconstruction.**

## Honesty audit of the batch's own measurements

`[Observed]` **§1–§8 identity, computed not transcribed.** Per-section sha256 with a fence-aware splitter, `git show 186d90b:` vs the working file, **denominator 10 sections**: §1…§8 **all eight byte-identical**. My splitter drops each section's terminating newline, so it reports 793 / 4387 / 15376 / 5687 / 3600 / 2191 / 1037 / 6609; +1 each reconciles to the delta's **794 / 4388 / 15377 / 5688 / 3601 / 2192 / 1038 / 6610** exactly. Only `HEADER` and §9 differ. ✔

`[Observed]` **The frozen record was not edited.** Changelog entries **v1.0 through v1.15 are byte-identical** to `186d90b` — denominator 16 entries, **0 differing**, including the v1.15 entry with its six markers intact. Stripping every balanced `[corrected 2026-…]` span (and the whitespace it was inserted after) from the v1.16 entry yields a string **byte-for-byte identical** to the frozen v1.16 entry — not merely whitespace-normalised-identical. Verification rule 10 and the D-10 convention held under a check designed to catch a silent edit. ✔

`[Observed]` **Four markers in the v1.16 entry**, counted with my own wrap-tolerant pattern over that entry's span; a one-line pattern returns **0**, so the delta's stated method is the necessary one. Neighbouring entries reproduce (v1.15 **6**, v1.14 **5**, v1.13 **5**). ✔

`[Observed]` **Fixture arithmetic, from the source.** Set difference of printed fixture names, both run in a git repo: v1.16 **205**, v1.17 **288**, **0 duplicates** in either, **0 dropped**, **83 added**, **0 renamed** (every v1.16 name survives verbatim). The itemisation table reconciles: name loop **65**, `para_open` **3**, condition-1 mid-line **3**, raw-text guard **1**, mid-line `textarea` **1**, table **2**, hiding attributes **5**, declined limb **2**, LG-6 **1** = **83**. And |`_COND6` ∪ `_RAWTEXT` ∪ `_HIDES_INLINE`| = **65**. ✔

`[Observed]` **The nine mutation-reverts, rebuilt from the delta and run at denominator 288 inside a git repository:**

| revert | claimed | measured | |
|---|---|---|---|
| m1 region trigger back to "any position" | 54 | **54** | ✔ |
| m2 mid-line carriers open nothing | 17 | **17** | ✔ |
| m3 raw-text elements parse tags inside them | 1 | **1** | ✔ |
| m4 `para_open` back to "the line had characters" | 3 | **3** | ✔ |
| m5 any two-pipe line counts as a table row | 1 | **1** | ✔ |
| m6 hiding set narrows back to v1.16's | 2 | **2** | ✔ |
| m7 LG-6 stops naming the opening line | 1 | **1** | ✔ |
| m8 every mid-line carrier is inline | 11 | **11** | ✔ |
| m9 autolinks read as tags | 1 | **1** | ✔ |

**All nine witness**, the multiset `{54,17,1,3,1,2,1,11,1}` is identical to §9's list, and unlike RD-44 I needed no second reconstruction. m1's **54** independently corroborates my name sweep's 54 movers. ✔

`[Observed]` **But the nine are one per *disclosed* repair, and the batch shipped an undisclosed tenth.** A comment-stripped diff of the two validators shows two changes to the split-tag rule — `_SPLIT_TAG_RE.search` → `.match`, and the removal of the `_open_frag.group(1).lower() in _COND6` requirement — that appear in **neither** the delta nor §9. A `re` count over both: `split`, `SPLIT`, `search`, and the v1.16 comment phrase `` `>` never arrives `` each occur **0** times in the delta and **0** times in the §9 v1.17 entry. No mutant covers either change. Both are measured below (RD45-01), in both directions.

## New findings

### RD45-01 — BLOCKING — an undisclosed change to the split-tag rule reopens the RD43-01(d) carrier mid-line: a `display:none` div laundered a `READY FOR` at **0 errors, exit 0** — and its other limb refuses a lawful record v1.16 accepted

`[Observed]` v1.16: `_open_frag = _SPLIT_TAG_RE.search(_bare)` … `if _open_frag and _open_frag.group(1).lower() in _COND6:`. v1.17: `_open_frag = _SPLIT_TAG_RE.match(_bare)` … `if _open_frag and not (html_stack and html_stack[-1][0] in _RAWTEXT):`. Neither change is recorded in D-1…D-8, in the §9 v1.17 entry, or in the nine mutation-reverts, and the delta's own preamble says it "records every change of meaning".

`[Observed]` **Limb 1 — laundering.** `search` → `match` restricts the unterminated-tag rule to line-initial position, but a mid-line `<div` whose attributes arrive on the next line is inline raw HTML spanning a line break, and html5lib puts everything after it inside the div. Executed at `963f1c40`, git on, real digests, full 39-row roster:

```
GATE VERDICT: NOT READY

Appendix, not an answer. <div
style="display:none">

GATE VERDICT: READY FOR Capability 1 — Project registration and honest shape visibility
```

`html5lib` ancestry, **identical under `-f gfm` and `-f commonmark`**: visible line `['html','body','p']`; hidden line **`['html','body','div{style=display:none}','p']`**. Own-flags: at v1.16 the `READY FOR` line is `no`, at v1.17 it is `own`.

```
$ python3 scripts/launch_gate_results.py …/E-splittag.md
trend row:
| 2026-08-10 | 963f1c40 | 0 | 0 | 0 | 0 | 0 | n/a — no prior record supplied | READY FOR Capability 1 — Project registration and honest shape visibility |
record valid — verdict semantics remain the instrument's, not this tool's
$ echo $?
0
```

**0 errors at v1.17; 1 error at v1.16.** This is a regression the batch introduced, and it is RD43-01(d)'s own carrier moved four columns to the right.

`[Observed]` **Limb 2 — over-refusal.** Dropping the `_COND6` membership test means *any* name now opens a block from a line-initial split tag. §5's own angle-bracket shorthand wrapped across two lines in a G1 section — `<see the appendix for the` / `full carrier list>` — scores **7 errors at v1.17** and **0 at v1.16**, while the rendered DOM places the next declared field at `['html','body','p']`, plainly visible.

*Requires:* a **validator change** (the split-tag rule must open a region where the renderer opens one, in both positions, and must terminate at the paragraph as the renderer does) **and a record correction** — the delta must record the change it made. **Offer-blocking, and it blocks the formal administration.**

### RD45-02 — BLOCKING — `_TAG_RE`'s attribute group stops at the first `>`, so a `>` inside a quoted attribute value hides the hiding attribute: laundered at **0 errors, exit 0**

`[Observed]` `_TAG_RE = re.compile(r"<(/?)([A-Za-z][A-Za-z0-9-]*)([^>]*)>")`. Group 3 is `[^>]*`, so the match ends at the first raw `>` — but the HTML5 tokenizer treats `>` inside a quoted attribute value as an ordinary character. Everything after that `>` in the real attribute list is invisible to `_HIDING_ATTR_RE`. Executed git-on, real digests:

```
GATE VERDICT: NOT READY

Appendix, not an answer. <div style="content:'>';display:none">

GATE VERDICT: READY FOR Capability 1 — Project registration and honest shape visibility
```

`html5lib` ancestry, identical under `-f gfm` and `-f commonmark`: **`['html','body',"div{style=content:'>';display:none}",'p']`**. CLI: `rc=0`, `record valid`, trend row `… | READY FOR Capability 1 — Project registration and honest shape visibility |`. **0 errors at v1.17; 1 error at v1.16** (v1.16's any-position `_COND6` rule caught it incidentally).

This defeats **the whole of D-6** rather than an edge of it: any of `display:none`, `visibility:hidden`, `opacity:0`, `hidden` or `aria-hidden="true"` passes unread behind a single quoted `>`. §9 states the enumeration widened; measured, the enumeration is not reached.

*Requires:* a **validator change** (tag scanning must respect quoted attribute values, as the tokenizer does). **Offer-blocking on §9's hiding-set clause, and it blocks the formal administration.**

### RD45-03 — BLOCKING — the mid-line hiding set omits four element names a browser does not paint; `<iframe>` and `<noframes>` are v1.17 regressions, and the batch shipped a **green fixture asserting the `<iframe>` record is lawful**

`[Observed]` D-3's rule is right — a mid-line tag opens a region iff it takes its content out of sight — but `_HIDES_INLINE = {script, style, title, details}` is not that set. Sweeping the HTML Standard's UA-stylesheet `display:none` list plus `iframe`/`select`/`plaintext`/`xmp`/`frame`/`frameset`/`optgroup` (**denominator 22**), each as a mid-line carrier in the laundering shape:

| carrier | v1.17 | v1.16 | DOM ancestry of the hidden verdict |
|---|---|---|---|
| `<iframe>` | **0** | 1 | `['html','body','p','iframe']` |
| `<noframes>` | **0** | 1 | `['html','body','p','noframes']` |
| `<noembed>` | **0** | 0 | `['html','body','p','noembed']` |
| `<select>` | **0** | 0 | `['html','body','p','select']` |

All four give `rc=0`, `record valid`, and a trend row reading `READY FOR Capability 1 — Project registration and honest shape visibility` while the last visible line reads `GATE VERDICT: NOT READY`. Uppercase `<IFRAME>` behaves identically. `iframe`, `noembed` and `noframes` are RAWTEXT in the HTML5 tokenizer and carry `display:none` in the Standard's own rendering section; text directly inside `<select>` is not painted. The remaining 18 of 22 are either painted (`plaintext`, `xmp`, `pre`, `textarea`) or inert.

`[Observed]` **Two of the four are regressions this batch introduced**, and one of those is the name RD-44 named. RD-44's sweep recorded: *"6 are void … and correctly inert; **3 (`details`, `iframe`, `title`) genuinely hide and are correctly refused**."* At v1.17 exactly **2 of 62** are refused — `details` and `title`. `iframe` was un-refused.

`[Observed]` **And the batch fixtured the regression as correct.** The name loop ships:

```
  pass  a lawful G1 section naming `<iframe>` mid-sentence is accepted — a block-level NAME mid-line is not a region (RD44-01)
```

The word "lawful" is false of that record: the rendered field sits inside an `iframe`.

*Requires:* a **validator change** (the mid-line hiding set must be measured against the render across the element population, not enumerated from condition 1 plus `details`) and a **fixture correction** (the `<iframe>` fixture asserts the opposite of the measurement). **Offer-blocking, and it blocks the formal administration.**

### RD45-04 — BLOCKING — §9's `textarea` residual is false in the bytes an approval digest binds: the exact construction it declares safe hides a declared field **and the terminal verdict** at 0 errors

`[Observed]` §9, v1.17 entry: *"a close tag written inside a mid-line `<textarea>` is still parsed as a tag, which can end a region early and **can never hide a field**."* The delta repeats it: *"The failure mode is ending a region early — never hiding a field."*

Ending a region early is *precisely* how a field is hidden: the validator believes the hiding element closed, the browser knows it did not. Executed git-on, real digests, in the exact mid-line form the sentence names:

```
GATE VERDICT: NOT READY

<div style="display:none">
Appendix prose <textarea>
</div>
</textarea>

GATE VERDICT: READY FOR Capability 1 — Project registration and honest shape visibility
```

The `</div>` is RCDATA text inside the `textarea`, so it closes nothing; `</textarea>` closes the textarea and the `div` stays open. `html5lib` ancestry, identical under `-f gfm` and `-f commonmark`: **`['html','body','div{style=display:none}','p']`**. CLI: `rc=0`, `record valid`, trend `READY FOR Capability 1 — …`. **0 errors.** The line-initial variant of the same construction behaves identically.

This is the raw-text guard's own load-bearing case — the one D-3 says *"took two constructions to find"* — routed round the guard through the one raw-text element deliberately left outside it.

*Requires:* a **validator change** (a raw-text element suppresses tag reading whether or not it opens a region) **and an instrument amendment** — §9 asserts a safety property that one construction falsifies. **Offer-blocking, and it blocks the formal administration.**

### RD45-05 — MAJOR — §9's LG-6 claim is false of the shipped bytes: the message names the last line *before* the region, not the line that opened it, and the fixture asserts only that a substring is present

`[Observed]` §9: *"LG-6 now names the line that opened the region an administrator's column-0 verdict sits inside, which the RD43-03 disposition promised and did not ship."* D-2: *"It **names the line that opened the region** and quotes it."*

`_opened_by` walks backwards for the last line flagged `own`/`bq1`. A line that opens a raw-HTML block is itself flagged `no` (`_raw_html_line` → `cls = "no"`), so that walk steps **past** it. Measured, git-on:

```
  line 62: Reviewer's falsification notes: tried to break the roster; couldn't
  line 63: <div style="display:none">
  line 65: some appendix prose here
  line 69: GATE VERDICT: NOT READY

LG-6: … — inside a region opened at line 62 by `Reviewer's falsification notes: tried to
break the roster…` — nothing after that line is the record's own until the element it
opened is closed — …
```

The region was opened at **line 63**. The administrator is pointed at line 62 — a declared field that opened no element — and told that nothing after it is their own until "the element it opened" is closed.

`[Observed]` The shipped fixture cannot catch this. It uses **exactly this construction** and asserts only the substring `"inside a region opened at line"`:

```python
case("LG-6 names the line that opened the region (RD44-01)",
     good.replace("GATE VERDICT:", '<div style="display:none">\n\nGATE VERDICT:'),
     "inside a region opened at line")
```

It checks the message's shape, never the fact §9 claims. m7 kills it, so the repair is "witnessed" while the claim is false.

*Requires:* a **validator change** (`_opened_by` must return the line whose tag pushed the surviving stack entry) **and a record correction** — §9 states the repair as delivered. **Offer-blocking on the §9 sentence**; not independently blocking to the administration.

### RD45-06 — MAJOR — 65 of the 83 new fixtures derive their expected answer from the very set under test, so they cannot fail for a wrong membership — which is how RD45-03 shipped green

`[Observed]` The name loop:

```python
for _n in sorted(_COND6 | _RAWTEXT):
    _hides = _n in _HIDES_INLINE
    case(f"a lawful G1 section naming `<{_n}>` mid-sentence is "
         + ("refused — its content is out of sight (RD44-01)" if _hides
            else "accepted — a block-level NAME mid-line is not a region (RD44-01)"),
         …,
         "LG-6" if _hides else None)
```

The expectation *and* the fixture's own title are computed from `_HIDES_INLINE` — the set whose membership is the thing that can be wrong. Add a name to `_HIDES_INLINE` and 65 fixtures silently flip their expectations and still pass; remove one and the same. What the loop actually witnesses is the line-initial-versus-mid-line rule (m1 → 54, m2 → 17), not the hiding set. This is the batch's own motto — *"a check that cannot fail is not a check"* — applied to 65 of its 83 new fixtures, and it is the mechanism by which `<iframe>` acquired a green fixture calling the record lawful.

The delta calls this loop *"the corpus RD-44 asked for, so it can tell next time."* It cannot tell about the one thing RD-44's finding was about.

*Requires:* a **fixture change** — the expected direction must come from an independent source (the rendered DOM, a literal table of names, or the UA-stylesheet list), not from the predicate under test. **Not offer-blocking on falsity grounds; it materially weakens the evidence for the offer.**

### RD45-07 — MAJOR — a `<details>` named mid-sentence inside a blockquote or a list item refuses a lawful record with **7 messages untrue of it**, and the new 65-name corpus tests only the top-level paragraph position

`[Observed]` A mid-line block-level hider is pushed as `("block")` and survives blank lines with no regard for the markdown container it sits in — but the renderer closes it at the container's end, because `</blockquote>` and `</li>` pop it. Measured git-on, denominator 12 (4 names × 3 container shapes):

| construction | v1.17 | v1.16 | DOM ancestry of the next declared field |
|---|---|---|---|
| `> RD-44 measured the <details> carrier.` | **7** | 7 | `['html','body','p']` — **visible** |
| `- RD-44 measured the <details> carrier.` | **7** | 7 | `['html','body','p']` — **visible** |
| nested list, same sentence | **7** | 7 | `['html','body','p']` — **visible** |
| the same three with `<script>` / `<style>` / `<title>` | 7 | 0 or 7 | inside the element — **correctly refused** |

Three over-refusals of 12. Identical under `-f gfm` and `-f commonmark`. The errors include `LG-6: every GATE VERDICT: line in the record sits inside a quotation container` on a record whose verdict a reader sees at column 0.

This is RD44-01's harm in its most likely remaining shape: the canonical act in this chain is a reviewer quoting or bulleting a prior finding that names `<details>`. The batch's 65-name sweep places every name in a bare paragraph and so never reaches it. Carried from v1.16, not introduced — but it is the class the batch says it swept, and the sweep's population is the reason it survived.

*Requires:* a **validator change** (a mid-line hider's region ends at the end of its markdown container, as the renderer ends it) and a **fixture population** that crosses name × container. **Not offer-blocking; it blocks the formal administration** in the accepting direction.

### RD45-08 — MAJOR — `opacity:.0` and `opacity:0%` hide a declared field and the terminal verdict at **0 errors**, while §9 states the hiding set "gains … `opacity:0`"

`[Observed]` `_HIDING_ATTR_RE`'s opacity limb is `opacity[^\S\n]*:[^\S\n]*0(?:\.0*)?(?:[^\S\n]*[;"']|$)` — it requires a literal leading `0` and a specific terminator. Measured git-on, in the laundering shape:

| carrier | errors | DOM ancestry of the hidden verdict |
|---|---|---|
| `<div style="opacity:.0">` | **0** | `['html','body','div{style=opacity:.0}','p']` |
| `<div style="opacity:0%">` | **0** | `['html','body','div{style=opacity:0%}','p']` |
| `<div style="opacity:0">` *(control)* | 1 | refused |

Both are valid CSS spellings of the value the enumeration claims to carry. The delta's disclosure — *"a construction outside both [enumerations] is read as prose"* — covers a property the set does not name; it does not cover a value of a property the set does name. `font-size:0` is genuinely outside and is disclosed by the validator's own comment; I do not count it.

*Requires:* a **validator change** (match the property's values, not one spelling) or a **record correction** narrowing §9's claim to the exact spellings covered. **Offer-blocking on the §9 clause; it blocks the formal administration.**

### RD45-09 — MINOR — two counts in the shipped bytes that do not survive their own method

`[Observed]` (a) §9 and D-7(d): *"**Seven** accepting-direction fixtures are broken by no revert."* Measured over the whole population — the 83 new fixture names against the union of FAIL lines from all nine reverts, denominator 288 — **eleven** are broken by none: the seven name-loop entries (`base`, `col`, `hr`, `link`, `param`, `track`, `textarea`) **plus** `a mid-line <textarea> is visible and opens nothing`, `a real table row still ends its cell`, `a plain <span> at the end of a field line hides nothing`, and `the same words in a code span are prose and hide nothing`. All eleven are accepting-direction fixtures. **Seven** is RD-44's figure for *v1.16's* 26-fixture population, carried into §9 as a fact about v1.17 — verification rule 3's failure mode exactly.

`[Observed]` (b) §9: *"**53 of the 62 names** … named once mid-sentence in a reviewer's own G1 section, blanked the rest of a lawful record at **0 errors**."* Measured, the blanking scored **6** errors; RD-44's sentence, from which this is compressed, said the 53 *score 0 errors at v1.15*. As written the clause is false of the measurement it reports.

*Requires:* a **record correction** in §9 and the delta. **Not offer-blocking.**

## Falsification notes — what I tried that did **not** break it

`[Observed]` Each is an execution at `963f1c40`, git checks **on**, against the real committed instrument and §8 digests, with the rendered HTML and the `html5lib` DOM checked wherever the claim was about a reader.

- **RD-44's four laundering constructions, all closed.** Mid-line `<script>`, mid-line `<style>`, indented `</details>` after an ATX heading, and the lone `| <div style="display:none"> |` line each move **0 → 1** error, and the DOM confirms each hidden line really is out of sight (`p > script`, `p > style`, `details[COLLAPSED] > p`, `div[CSS-HIDDEN] > p`). The repair is real in all four.
- **The lawful-record battery, thirteen constructions, twelve at 0 errors.** A G1 sentence naming `<td>`, `<p>`, `<li>` and `<summary>` together (7 → 0 against v1.16); a bulleted G1; a fenced G1; an indented-code G1; a closed `<details>` appendix; a closed `<table><tr><td>` appendix; a G1 quoting `` `<details>` ``, `` `</details>` ``, `` `<script>` `` and `` `<div style="display:none">` `` in code spans; a URL autolink in prose; `\<details\>` escaped; a plain mid-line `<span>`; a real GFM table inside G1; and the whole record in CRLF. The thirteenth (a blockquoted G1 naming `<details>`) is RD45-07.
- **The 62-name sweep in the refusing direction.** Of the 62 `_COND6` names, **0** are refused at v1.17 that were accepted at v1.16 — the batch introduced no over-refusal inside the swept population, and 54 moved to accepted. Both `details` and `title` remain correctly refused with the field inside the element.
- **Attribute-syntax attacks that failed.** `<div/style="display:none">` and `<div class="x"style="display:none">` are both rejected by `pandoc` as inline raw HTML — the field renders at `body > p`, and the validator's acceptance is correct. `<DIV STYLE="DISPLAY:NONE">`, `<div style="display : none">`, `<div aria-hidden="true">` and `<div style="visibility:hidden">` are each refused, matching the render.
- **Table constructions, both directions.** `| <details> |` and `| <div style="display:none"> |` beneath a real delimiter row are both inert in the validator **and** in the render (field at `body > p`) — the cell genuinely ends the region. A hiding div *before* the pipes is still refused.
- **Markdown literal-text constructs.** A `</details>` inside a fence, entity-encoded as `&lt;div …&gt;`, inside an HTML comment, in a code span, and tab-indented after a paragraph each leave the element open in the render and the record refused — correct. A CDATA opener and a processing instruction become comment nodes with the field visible, and are accepted.
- **`<span hidden>` across a blank line** renders as an inline element closed at the paragraph end, field at `body > p`, and is accepted — the inline/block distinction m8 witnesses is right.
- **The declined limb, attacked from both sides.** `<see the hidden appendix>`, `<plus the hidden parameter block>` and `<none hidden>` each produce an element carrying the `hidden` global attribute with the next field inside it, and are refused; `` `<see the hidden appendix>` `` in a code span, `<plus the parameter block>`, and the English sentence "nothing hidden from view" are each accepted at 0 errors. D-8's measurement is exact and declining is right.
- **The corpus sweep, rebuilt independently.** 199 / 282 / 200 / 0 / **0 moved** / 82 / **65** — every figure reproduced from a script I wrote from the delta's prose, not from theirs.
- **The measurement apparatus, mutated first.** All nine reverts matched on the first reconstruction; I re-derived m1's 54 independently from the name sweep before trusting it. `check_governance.py` → 30 OK, 18 WARN, 0 FAIL (48 checks); `--selftest` → 121 fixtures, 0 failing; `verify_final_prespec.py` → PASS; contract index, dependency index and budget report → no drift.

## Overall assessment

The records discipline in this batch is the best this chain has produced, and it deserves to be said first and without qualification. **All nine mutation-revert denominators reproduced on my first reconstruction** — RD-44 needed two rebuilds for two of its twelve; I needed none, because the descriptions are now precise enough to rebuild from. **§1–§8 are byte-identical at all eight claimed byte counts across eleven versions.** The frozen v1.16 entry, stripped of its four markers, is **byte-for-byte** the frozen prose, and every changelog entry from v1.0 to v1.15 is untouched. `205 + 83 = 288` reconciles to the printed fixture names with **0 dropped and 0 renamed**. The skip notice quotes no figure, and no denominator survives anywhere in the validator. And the Regression section — the finding that has failed two rounds running — is now the strongest part of the batch: I rebuilt the uncommitted sweep script from the delta's prose alone and reproduced **199 / 282 / 200 carried / 0 dropped / 0 moved / 82 added / 65 answered differently**, every figure, first try. "A regression claim quotes a script's printed output or does not appear" is a rule this chain should keep. D-8 is right too: the batch declined a reviewer's finding with a measurement that falsifies it, and the measurement holds.

The sentence the batch was built on is also right. **A region begins at a line, not at a `<`** is the correct reading of CommonMark, `pandoc` confirms it in three lines, and applying it moved 54 of 62 names from a wrongly-refused record to an accepted one with no over-refusal introduced inside that population. All four of RD-44's laundering constructions are closed, each confirmed by the DOM to have been genuinely hiding. That is real progress, and it is the third consecutive round in which the durable part is real.

But the same failure has now recurred a ninth time, and this round it recurred in a way the batch's own method should have caught. **The rule was fixed; the set it ranges over was not measured.** D-3's rule is *"a mid-line tag opens a region only when it takes its content out of a reader's sight"* — correct — and then `_HIDES_INLINE` was enumerated as condition 1 plus `details`, which is not that set. `<iframe>`, `<noframes>`, `<noembed>` and `<select>` are each unpainted mid-line and each launder a `READY FOR` at 0 errors; two of them were refused at v1.16; and **`iframe` is one of the three names RD-44 wrote down as *"genuinely hide and are correctly refused."*** It was un-refused, and the batch shipped a passing fixture whose own title calls that record *lawful* — because the 65-fixture name loop computes its expected answer from `_HIDES_INLINE`, the set under test. Sixty-five of eighty-three new fixtures cannot fail for the one kind of error the finding was about.

Beside that sit two parser defects that defeat D-6 entirely rather than at an edge. `_TAG_RE`'s attribute group is `[^>]*`, so a single quoted `>` hides every attribute after it: `<div style="content:'>';display:none">` launders at 0 errors. And the split-tag rule was narrowed from `search` to `match` and had its `_COND6` test removed — **a change of meaning recorded nowhere in the delta, nowhere in §9, and covered by none of the nine mutants** — which reopens RD43-01(d)'s carrier mid-line in one direction and refuses a lawful wrapped `<…>` shorthand in the other. A delta whose first paragraph says it "records every change of meaning" shipped a change of meaning with a laundering consequence and did not record it.

And two sentences inside §9 — the bytes an approval digest binds — are again false of those bytes. *"A close tag written inside a mid-line `<textarea>` … can never hide a field"*: measured, the exact construction hides a declared field and the terminal verdict at 0 errors, because ending a region early in the validator **is** how a field stays hidden in the browser. *"LG-6 now names the line that opened the region"*: measured, it names the last line *before* the region and quotes a declared field that opened nothing, while the fixture asserts only that a substring appears. On the RD38-02 / RD39-02 / RD40-01 / RD41-03 / RD42-01 / RD43-01 / RD44-01 precedent this batch invokes in its own four dated markers, those sentences are defects in the bytes being approved.

The sentence I would put in front of the v1.18 batch: **measure the set, not just the rule — and let the fixture's expectation come from somewhere other than the thing it is testing.** Every enumeration in this predicate should be generated against the render across a named population with a denominator, exactly as the 62-name sweep was; every fixture that asserts a direction should take that direction from the DOM, not from `_HIDES_INLINE`; the tag scanner should respect quoted attribute values and raw-text elements uniformly, whether or not they open a region; a mid-line hider should end where its markdown container ends; and every line of the validator diff should appear in the delta, because this round one did not and it was the one that laundered a verdict.

On the two questions asked, in these words:

- **May v1.17 be offered to the owner at P-34?** **No.** The arithmetic reconciles from the source in every place I checked — nine denominators, eight section digests, four and six markers, 205 + 83 = 288, and a corpus sweep I rebuilt from prose and matched figure for figure. The frozen record was not edited and §1–§8 have not moved in eleven amendments. But sentences inside §9 are again false of the bytes they sit in: that a close tag inside a mid-line `<textarea>` *"can never hide a field"* (one construction hides the field and the verdict at 0 errors); that LG-6 *"names the line that opened the region"* (it names the line before it, and quotes a field that opened nothing); that the hiding set *"gains … `opacity:0`"* (`opacity:.0` and `opacity:0%` are not matched); and that *"Seven accepting-direction fixtures are broken by no revert"* (eleven are). Beside them, the delta's own promise to record every change of meaning is broken by the split-tag change, which is the change that reopened a carrier. **The digest v1.17 would bind is not the digest that should be approved.**

- **May the formal launch administration run on this validator?** **No.** Seven independent constructions produce `record valid`, exit 0, and a nine-column trend row reading `READY FOR Capability 1 — Project registration and honest shape visibility` while the record's last visible line reads `GATE VERDICT: NOT READY`: a mid-line split `<div` carrying `display:none` on the following line; a `>` inside a quoted attribute value; mid-line `<iframe>`, `<noframes>`, `<noembed>` and `<select>`; and a `</div>` written inside a `<textarea>` inside a hiding div. Four of these are regressions this batch introduced, and one of the four is the element name RD-44 explicitly recorded as correctly refused. Against them sit lawful records the validator refuses with messages untrue of them: any record whose G1 section names `<details>` inside a bullet or a blockquote — the single most likely sentence a reviewer of this instrument writes — and any record wrapping §5's own angle-bracket shorthand across two lines. Any one of these, at Administration 1, becomes the baseline every later F1 verdict is read against.

VERDICT: REVISE
