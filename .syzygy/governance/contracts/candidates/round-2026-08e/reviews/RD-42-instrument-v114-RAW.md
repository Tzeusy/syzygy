All measurements complete. The clone is porcelain-clean at close with the three subject digests unchanged.

---

# RD-42 — Launch-gate instrument re-review, v1.14 exact bytes (round-2026-08e, frozen commit `47adfa9`)

- **Review id:** RD-42 (tenth administration of the instrument re-review chain: RD-33 → v1.6 … RD-41 → v1.13)
- **Date:** 2026-08-11
- **Reviewer:** isolated fresh-context session, Claude family. Same-family re-review — F5's own caution applies to me. I authored no byte under review.
- **Clone:** `…/scratchpad/clone-08e-r22`, HEAD `47adfa920ac1842cad578febea78521b96936861`. `git status --porcelain` **empty at open and at close** (0 lines); `git diff --stat` empty; **zero `.pyc`/`__pycache__` under the clone at close** (one `scripts/__pycache__` was created by a Python import during the session and was removed; it was git-ignored and never tracked). Every mutant, synthetic record and harness lives in `…/scratchpad/rd42/`. Nothing under `/home/tze/GitHub/syzygy` was read, written, or executed.

## Materials read in full, and digests verified

Verified with `sha256sum` at open and again at close, and cross-checked with Python `hashlib` for every git-extracted blob:

| artifact | sha256 | matches charter |
|---|---|---|
| `launch-gate-pre-specifications.md` (1362 lines) | `bd070a28cc561dfd1fa62c525cb2ae0c3a10f06b848be9b953c4c094896e355e` | ✔ |
| `scripts/launch_gate_results.py` (2583 lines) | `e861ec38564042caf51bcd42536a0694690d1232f46c9085ecfdb7715eeb9c20` | ✔ |
| `round-2026-08e/LAUNCH-GATE-v1.14-SEMANTIC-DELTA.md` (382 lines) | `bdc6d4c87145d483abee94e64d3ee064fd787e5b100a365c5a7c6b2818b2b89a` | ✔ |

Also read in full: `reviews/RD-41-instrument-v113-RAW.md` (305 lines, 12 findings, `VERDICT: REVISE`); the RD-40 and RD-41 sections of `reviews/DISPOSITION-REGISTER.md` including the dated markers; `decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` (P-34); the launch-gate rows of `PROJECT-STATUS.md`; instrument §5, §9's v1.13 and v1.14 entries and the header, line by line; the whole of the v1.14 validator's predicate, `_decl`, LG-4, LG-6 and LG-12 paths; and the v1.13 validator reconstructed from `git show 619093b:scripts/launch_gate_results.py` (sha256 `e0a0653e69c75af6f09e2677754c0168692d96e0072f625524aaec78106f5a78`, 2193 lines — matching RD-41's measurement exactly).

**Method hazard worth recording (new):** in this environment `git show <sha>:<path> | sha256sum` **silently truncated** the blob — three different commits returned 401/1764/1399 lines and wrong digests. The same `git show` redirected to a file, or run through `subprocess` in Python, returned the correct 2193/2583 lines and the correct digests. Every byte-level measurement below was therefore taken in Python, never through a shell pipe. This is verification rule 1's hazard in a new place: the pipeline, not the pattern.

## 1. Method — what I ran

`[Observed]` `python3 scripts/launch_gate_results.py --selftest` in the clone → **`168 fixtures, 0 failing`**, exit 0. Counted from the tool's own output: **168 `pass` lines, 0 `FAIL` lines, 0 skip notes**, 169 output lines total. Denominator cross-checked a second way by instrumenting the selftest: **162 `case()` fixtures + 6 hand-rolled `n_cases[0] += 1` fixtures = 168**.

`[Observed]` A record generator matching §5's template field-for-field (39-row roster, all declared fields, blockquoted banner, G1 section), with `REPO` bound to the clone, so LG-1/LG-2/LG-11 and both citation-existence paths executed **git-on against the real commit `47adfa9`, the real committed instrument digest `bd070a28…`, the real §8 digest `01209c0f…` and the real `effective_version: v1.14`** on every construction below. ≈110 synthetic records.

`[Observed]` **Mutation-revert testing (rule 6):** 17 mutated copies written outside the clone, each `REPO`-patched; each run's *output* read (FAIL lines), never its exit code.

`[Observed]` **Cross-version execution:** the v1.13 validator rebuilt from git, and the *same record bytes* run through both, for every directionality claim — including all 162 captured fixtures.

`[Observed]` Fixture→check coverage computed mechanically by intercepting `validate()`. Denominator **13** checks over **162** fixtures.

`[Observed]` Repo-wide sweeps with Python `re`, never shell grep. Denominator **375** text files.

`[Observed]` `python3 scripts/check_governance.py` → **30 OK, 18 WARN, 0 FAIL (48 checks)**; `--selftest` → **121 fixtures, 0 failing**.

`[Unknown]` I did not administer the gate and read no pilot record content. All answer sets are synthetic.

## 2. Per-finding verification — all twelve RD-41 findings

| RD-41 | Class | Disp. | Status | Evidence in the v1.14 bytes |
|---|---|---|---|---|
| **RD41-01** | BLOCKING | R | **closed for every markdown container the finding named; the class survives out the raw-HTML side — RD42-01** | `_own_flags` (425–542) is a genuine block-structure scan: a container stack maintained across lines, list items matched at content column, blockquotes at any depth, lazy continuation for list items. I rebuilt RD-41's composites independently at `47adfa9`, git on, real digests, full 39-row roster: **list-item-continuation composite 0 (v1.13) → 4 (v1.14)** with the appendix above the verdict, **0 → 5** below it; **blockquote-lazy-continuation composite 0 → 4**; **`> ` banner nested in a list item 0 → 1**. I could not reproduce the delta's exact "6 errors" because RD-41's composite bytes are not preserved anywhere in the repo — but the *direction* reproduces on independently built bytes, which is the load-bearing claim. **Mutations reproduce:** list container removed from the stack → **3**; laziness disabled → **1**; `bq1` widened → **1**. Twelve further container carriers I constructed (blank line inside a list item, 2-deep nesting, `1)`, `99.`, tab-indented continuation, `> - ` and `- >` nesting, 4-spaces-after-marker, thematic break inside an item) are **all refused**. This is a real repair. But `html_depth` tracks exactly two tag names, so the class walks out the raw-HTML door — RD42-01. |
| **RD41-02** | BLOCKING | R | **closed for `<details>`/`<summary>` and setext; open for every other raw-HTML block, and open for one whole `_decl` site — RD42-01, RD42-03** | `_decl` is a consumer at nine of ten sites. Measured v1.13 → v1.14 on identical bytes, git on: `E3 reopen-list:` only in `<details>` **0 → 1**; only as setext text **0 → 1**; `Deferred count:` **0 → 1** each; `Owner deferral decision:` only in `<details>` under READY-WITH-DEFERRALS **0 → 2**. **Mutation:** every `_decl` site reverted to full active text → **5**, exactly those five fixtures. The internal inconsistency RD-41 named is gone. **But** the delta's opening sentence at D-3 — *"All ten `_decl` sites read the record's own lines"* — is false at denominator 10 (RD42-03), and `<div>`, `<p>`, `<span>` and `<table>` blocks are not containers to this predicate at all (RD42-01). |
| **RD41-03** | BLOCKING | R | **closed for its instance; the class recurs twice inside the entry written to close it — RD42-04, RD42-05** | The §9 v1.13 entry now reads *"eight [corrected 2026-08-11, RD41-03: **ten** …]"*. Verified in place. But the **new** v1.14 entry introduces two fresh false counts: "fourteen" mutation-witnessed repairs (thirteen, measured) and "four dated correction markers" (five, measured). |
| **RD41-04** | BLOCKING | R | **one limb closed, one limb inert in §5's own record shape — RD42-07** | The `\s*` newline-crossing door is genuinely closed: the anchor is matched per line (830–832), a bare `###` bridged to a `G1 ` line moves **0 → 1**, mutation → **1**. The emptiness limb exists (836–846) and its mutation → **1**. **But** `_takewhile_before_heading` runs to the next *heading*, and §5's template places seven declared trailer fields between `## G1` and the verdict — so in §5's own record shape a `## G1` with nothing of its own beneath it scores **0 errors** (measured, git on, real digests). RD42-07. |
| **RD41-05** | MAJOR | R | **not closed — the promise is falsified a fourth consecutive time** | The delta promises *"each entry stated from a measured v1.13 → v1.14 comparison of the fixture's own bytes (D-1 item 5's misassignment not repeated — and this time the comparison, not the intent, is what is reported)"*. Measured on the fixtures' own bytes: three of the four *Newly accepted* entries move **0 → 0** (RD42-06), and the *Acceptances withdrawn* entry "the setext-underlined field line" moves **1 → 1** (RD42-11). |
| **RD41-06** | MAJOR | **R — partly** | **the raw-side repair is real but has no fixture witness; the LG-6 message is still untrue of the record — RD42-06, RD42-09** | The repair works when exercised: the three constructions placed **above** the verdict move **1 → 0** each. But the three fixtures shipped for it place the construction **below** the verdict, where the v1.13 defect never fired — they score 0 at v1.13 and 0 at v1.14, and reverting the raw-side call to un-stripped text fails **0 of 168**. And the message: an unpaired `<details>` or `` `<summary>` `` mentioned in prose still blanks the rest of the record and reports *"every `GATE VERDICT:` line … sits inside a quotation container — inside a container opened on an earlier line"* of a verdict that is at column 0, unmarked, visible and terminal. RD42-09. |
| **RD41-07** | MAJOR | R | **the sentence is replaced by a stronger one that is also false — RD42-08** | The delta now says *"This delta enumerates every withdrawal it makes and claims no completeness it has not swept."* Measured: an undisclosed withdrawal — any declared field whose value is entirely angle-bracketed (`<redacted>`, `<as listed in §2>`, `<see appendix A>`, `<none>`) moves **0 → 1**, refused with a message asserting it "carries §5's own placeholder", which is untrue of the record. |
| **RD41-08** | MAJOR | R | **verified-closed for the NBSP; the harm is reachable without it — RD42-02** | `_norm_uni_ws` (409–422) folds `\u00a0 \u1680 \u2000–\u200a \u202f \u205f \u3000` before the token search and before parsing. Re-executed: the NBSP record scores **0 errors reporting `READY FOR …` at v1.13** and **0 errors reporting `NOT READY` at v1.14**. **Mutation:** the fold removed → **1**, and the fixture is behavioural (F2 `Not met` refuses READY), not string-matching — the right shape. **But** the identical laundering is reachable with ASCII only: RD42-02. |
| **RD41-09** | MINOR | R | **verified-closed** | The register's RD40-05 row carries `[corrected 2026-08-11, RD41-09: they were not — a substring sweep … finds zero of the three …]`. I re-ran the sweep: `0→8`, `comment-splic`, `spliced`, `unterminated comment`, `HTML-comment consequen` — **all five absent** from the v1.14 delta. The marker is accurate. |
| **RD41-10** | MINOR | R | **verified-closed, and disclosed honestly — but the sweep it rests on is incomplete** | D-8's table reproduces exactly: predicate tab expansion reverted alone → **0 of 168**; predicate `≤3` bound → **0**; `_label_present`'s `^ {0,3}` → **0**. The two guard fixtures are labelled *"a defence-in-depth guard, not a single-layer witness"* in their own fixture names — the correct discipline, and the best single thing in this batch. But the answer to "is that the only place redundancy hides a missing witness?" is again **no**: D-7 and D-4's raw-side strip each fail **0 of 168** (RD42-04, RD42-06). |
| **RD41-11** | MINOR | R | **verified-closed for the fixture; its claimed denominator is false** | The fixture is now `good_head.replace(head, "f"*40)` (1780–1782), built from a real commit; the unmutated `good_head` no longer emits "does not exist". But the delta's *"Mutation: the fixture rebuilt on the v1.13 shape → 1"* measures **0** (RD42-04). |
| **RD41-12** | MINOR | R | **verified-closed** | Recomputed over **all 12** commits that have touched the instrument: at the v1.13 population there were **11 commits and 10 distinct declared values** (v1.4…v1.13), the eleventh (`e69c9239`) declaring none. D-1's correction is exact. |

**Tally, with its denominator:** of RD-41's **12** findings, **12 are present in the v1.14 bytes and none is absent**; **5 are closed outright** (RD41-03's instance, RD41-08's NBSP, RD41-09, RD41-11's fixture, RD41-12); **4 are closed for everything the finding constructed, with the class surviving one carrier out** (RD41-01, RD41-02, RD41-04, RD41-06); **3 are not closed** (RD41-05, RD41-07, and RD41-06's fixture layer). **Fifteen of the sixteen claimed mutation-reverts reproduce at exactly the claimed denominators; one measures 0 where 1 is claimed.**

## 3. Honesty audit of the batch's own measurements

`[Observed]` **Fixture count and arithmetic — honest.** Printed output `168 fixtures, 0 failing`; instrumented count 162 `case()` + 6 hand-rolled = **168**. 145 + 23 = 168 ✔. The delta's itemization sums to exactly 23 (2+1+1+1+1+1+1+4+1+1+1+4+1+4), and I found exactly 23 new fixtures in the v1.14 block (2381–2561) plus the LG-1 fixture rebuilt in place. ✔

`[Observed]` **The sixteen mutation-reverts.** I constructed all sixteen from the delta's own D-2…D-8 descriptions and measured each by reading the selftest's FAIL lines:

| revert | claimed | measured | fixtures broken |
|---|---|---|---|
| D-2 laziness disabled | 1 | **1** | the lazy-continuation fixture |
| D-2 list container removed from the stack | 3 | **3** | indented continuation, lazy continuation, banner-in-list-item |
| D-2 `bq1` widened to any depth | 1 | **1** | nested `> >` banner |
| D-2 raw-HTML depth tracking removed | 5 | **5** | 2 RD40-02 + 3 RD41-02 `<details>` fixtures |
| D-2 blockquote laziness **enabled** | 43 | **43** | starting with *"well-formed full-template record validates"* |
| D-3 every `_decl` site → full active text | 5 | **5** | the five RD41-02 carriers |
| D-3 position rule removed | 1 | **1** | field-below-the-verdict |
| D-3 placeholder rule removed | 1 | **1** | template-quoted-at-column-0 |
| D-4 setext folded into containment | 1 | **1** | `---` after the verdict |
| D-4 setext dropped from declaration-form | 3 | **3** | setext field + 2 RD41-02 setext carriers |
| D-5 LG-4 anchor → joined-text `\s*` | 1 | **1** | bare `###` bridge |
| D-5 emptiness requirement removed | 1 | **1** | `## G1` opening nothing |
| D-6 unicode fold removed | 1 | **1** | NBSP |
| **D-7 LG-1 fixture rebuilt on the v1.13 shape** | **1** | **0** | **none — RD42-04** |
| D-8 predicate tab expansion | 0 | **0** | disclosed |
| D-8 predicate `≤3` bound | 0 | **0** | disclosed |
| *(extra) `_label_present`'s `^ {0,3}` → `^ *`* | — | **0** | listed in D-8's table |
| *(extra) raw-side call → un-stripped text* | — | **0** | **none — RD42-06** |

Measured multiset for the thirteen that witness = `{1×8, 3×2, 5×2, 43}`; claimed = `{1×9, 3×2, 5×2, 43}`. **Every revert fails exactly the fixtures its repair added — except D-7's, which fails nothing.** ✔ with one exception.

`[Observed]` **The blockquote-laziness reasoning — I verified it and I agree it is forced.** §5's frozen template puts `Instrument version:` on the line *immediately* beneath `> … (instrument preamble; VIS-4).` with **no blank line**. Under CommonMark that is a lazy paragraph continuation, so every declared field is blockquote content. The mutant that implements laziness for blockquotes fails **43 of 168**, first among them *"well-formed full-template record validates"* — reproduced. I considered the alternative (implement laziness *and* read declared fields from blockquote content): it accepts §5's template but opens exactly the same `> Quoting §5:` door, so the hole is a property of §5's template shape, not of the implementation choice. **Forced, correctly disclosed, and fixtured in its accepting direction rather than described** — the right discipline.

`[Observed]` **§1–§8 identity, computed not transcribed.** Per-section sha256 with a fence-aware splitter, `git show ec7bdc4:` vs `47adfa9`, ten sections each side, **denominator 10**: §1…§8 **all eight byte-identical**, at exactly 794 / 4388 / 15377 / 5688 / 3601 / 2192 / 1038 / 6610 bytes — the delta's figures reproduce to the byte. Only `HEADER` (2915→2915, one line: `effective_version: v1.13` → `v1.14`) and §9 (29998→38097) differ. **Zero question blocks changed; no ID renumbered; no verdict word changed.** ✔

`[Observed]` **Version constancy, swept at every commit.** Combined §1–§8 digest computed at all **12** commits that have ever touched the instrument: identical at v1.7…v1.14 — **eight versions, seven amendments** ✔. §8 recomputed with the validator's own `param_block_bytes` at every commit: **6610 bytes, `01209c0f…`, constant at v1.5…v1.14 — ten versions** ✔; **three** distinct §8 digests in history ✔; v1.4 (4067) and its predecessor (2084) differ ✔. P-34 and PROJECT-STATUS both say exactly this.

`[Observed]` **Frozen population — exact.** 32 files match the frozen shapes under `round-2026-08e/`; against `ec7bdc4`: **31 byte-identical, 1 new (this delta), 0 modified**. The delta's 32/31/1/0 reproduces precisely, and RD-41's raw review was indeed committed at `ec7bdc4` before any subject byte moved. ✔

`[Observed]` **Every check fires, denominator computed.** LG-1 11, LG-2 6, LG-3 4, LG-4 9, LG-5 10, LG-6 18, LG-7 16, LG-8 3, LG-9 11, LG-10 7, LG-11 7, LG-12 35, LG-13 8 — **13 of 13, none absent**, 145 emissions across the 162 captured fixtures (the 6 hand-rolled prior fixtures additionally exercise LG-5). ✔

`[Observed]` **Checks that cannot fail — swept with a denominator.** All **132** asserting `case()` fixtures compared against the errors of all **8** constructed baselines (`good`, `ready`, `scoped_c2`, `with_def`, `good_head`, `good_real`, `ready_real`, `with_def_real`) under each fixture's own `_git` setting. **13 flagged.** Ten survive inspection (the fixture *is* the flagged baseline, or the coarse assertion coincides while the fixture still discriminates against a revert of the predicate it targets — I checked each against the mutant matrix above). **Three are genuinely inert:** the RD41-06 restoration fixtures #154/#155/#156, which pass at v1.13, pass at v1.14, and pass under the revert of the repair they were written for (RD42-06). RD41-11's own instance is genuinely fixed.

`[Observed]` **Stale-version sweep.** 375 text files; **118** lines carry both a launch-gate token and a `v1.x` token across **33** files; 7 name v1.14. Of the routed artifacts (PROJECT-STATUS, AGENTS, README, P-34, PENDING, the instrument, TASK-ROUTER), exactly **one** line names a non-v1.14 version — the v1.3 pilot reference, which is correct. **No routed artifact names a stale instrument version.** ✔

`[Observed]` **The disclosed-limits section, checked word by word.** *"Unmarked lines beneath any blockquote are the record's own"* — true, including at depth ≥2, and correctly *not* true when the blockquote sits inside a list item (I checked: `- x` / `  > q` / `  unmarked` → not own). *"enabling blockquote laziness instead fails 43 of 168"* — exact. *"Two predicate clauses have no single-layer witness … measured at 0 of 168 each"* — exact. *"An asymmetric `**Label:*` still satisfies presence"* — verified. *"the trend row is still printed above the error list carrying the record's claimed verdict when the record is invalid"* — verified in output. *"The honest cap on the prior guard is unchanged"* — verified. **This section does not repeat its three predecessors' pattern; every sentence in it is true of the bytes.** The false generalizations in this batch are elsewhere: in §9's counts, in the directionality axes, and in D-3's "all ten" (§4 below).

`[Observed]` **Five sentences inside §9 and the delta — the bytes an approval digest would bind, and the record that explains them — are false of those bytes.** RD42-01 through RD42-06.

## 4. New findings

### RD42-01 — BLOCKING — the `<details>` exploit RD41-02 named survives whole, three ways: the predicate's "raw-HTML block" is two tag names, and even `<details>` can be reopened by an inline code span. `E3 reopen-list: empty` is supplied from collapsed content a reader never opens, at **0 errors**, `record valid`, `READY FOR <the verbatim target>`

`[Observed]` The predicate's raw-HTML limb is `html_depth += len(re.findall(r"<(?:details|summary)\b(?![^>]*/>)", content, re.I))` (537–540). Python substring search over the whole 2583-line file: **`div` occurs once, inside an unrelated docstring word; `<p`, `<span`, `<table`, `<blockquote`, `<script` occur nowhere.** Denominator: CommonMark defines seven HTML-block start conditions; this tracks two tag names of one of them.

Executed at `47adfa9`, git on, real digests, full 39-row roster, through the clone's own CLI. Base record: reopen items shown to the reader as visible prose bullets; `E3 reopen-list: empty` present **only** in the carrier; verdict `READY FOR Capability 1 — …`.

| carrier | errors | trend verdict |
|---|---|---|
| `<div style="display:none">` | **0** | `READY FOR Capability 1 — …` |
| `<p style="display:none">` | **0** | `READY FOR Capability 1 — …` |
| `<span hidden>` | **0** | `READY FOR Capability 1 — …` |
| `<table><tr><td>` | **0** | `READY FOR Capability 1 — …` |
| **`<details>` reopened by a code span** (below) | **0** | `READY FOR Capability 1 — …` |
| *control:* `<details><summary>x</summary>` | 1 | — (`no E3 reopen-list: field`) |

The last is the sharpest, because it uses **the very tag the repair enumerates** and the element stays genuinely open in the rendered document:

```
<details>
<summary>Appendix — §5's template, quoted for reference only</summary>

Nothing in this appendix is an answer. A stray `</details>` here is prose, not a tag.

E3 reopen-list: empty

GATE VERDICT: READY FOR Capability 1 — Project registration and honest shape visibility
```

`[Observed]` The blank line after `<summary>` ends the type-6 HTML block, so the following lines are parsed as markdown; the `` `</details>` `` code span therefore renders as literal text, not a tag — but `_own_flags` counts it as a closing tag and decrements `html_depth` to 0, so `E3 reopen-list: empty` is classified **own**. `[Inferred]` In any CommonMark renderer the `<details>` element is still open, so that line renders *inside collapsed content a reader may never open* — RD-41's own words for the harm.

```
$ python3 scripts/launch_gate_results.py …/EXPLOIT-E3.md
rows parsed: 39 (Met 38, Not met 0, scoped 0, Unknown 1) — …
trend row:
| 2026-08-10 | 47adfa92 | 0 | 0 | 1 | 0 | 0 | n/a — no prior record supplied | READY FOR Capability 1 — Project registration and honest shape visibility |
record valid — verdict semantics remain the instrument's, not this tool's
$ echo $?
0
```

`[Observed]` The same works for `Deferred count:` (0 errors) and for `Owner deferral decision:` under `READY-WITH-DEFERRALS` (0 errors, Deferred column `3`, the owner's citation invisible) — the two other constructions RD41-02 named.

`[Observed]` **This falsifies §9.** The v1.14 entry: *"the stack of containers open at it — blockquote at any depth, list item at its content column, **raw-HTML block** — maintained across lines"*. D-2 says the same. The register's RD41-01 disposition says the same. A raw-HTML block is not tracked; two tag names are, and their counter is resettable by text.

`[Inferred]` This is the same failure one level down from RD-41's diagnosis. The batch adopted "the predicate carries state" for markdown's containers and then wrote a hardcoded tag list for HTML's — enumeration returning inside the repair that replaced enumeration. §3's own words, which the validator quotes back: *"the list is non-empty; 'ready' is then false regardless of every other verdict"* — the instrument's self-declared sharpest single gate, defeated by a `<div>`.

*Requires:* a **validator change** — the raw-HTML limb must be a block-structure decision like the others (CommonMark's HTML-block start/end conditions, or at minimum: any `<tag>` opening a block suppresses until its matching close **or a blank line**, and a closing tag never decrements below the depth it was opened at), with a fixture per carrier per consumer. **An instrument amendment**: §9's "raw-HTML block" is false of the bytes an approval digest would bind. **Offer-blocking, and it blocks the formal administration.**

### RD42-02 — BLOCKING — a record whose **visible terminal line reads `GATE VERDICT: NOT READY`** enters the trend log as `READY FOR <the verbatim target>` at **0 errors**, with no unicode trick — RD41-08's harm, reproduced through the repair that closed it

`[Observed]` Executed at `47adfa9`, git on, real digests, full roster, through the clone's own CLI:

```
…
Reviewer's falsification notes: tried to break the roster; couldn't
GATE VERDICT: NOT READY

<details>
<summary>Appendix — the verdict vocabulary, quoted from §5</summary>

Nothing in this appendix is an answer. A stray `</details>` here is prose, not a tag.

GATE VERDICT: READY FOR Capability 1 — Project registration and honest shape visibility
```

```
trend row:
| 2026-08-10 | 47adfa92 | 0 | 0 | 1 | 0 | 0 | n/a — no prior record supplied | READY FOR Capability 1 — Project registration and honest shape visibility |
record valid — verdict semantics remain the instrument's, not this tool's
```

**0 errors.** The ambiguity rule RD-41 called *"genuinely, structurally closed"* does not fire: `_later` is `[]` because the hidden `READY FOR` is *after* the visible `NOT READY`, and `_gv_own[-1]` selects the hidden line because `_flag_by_raw` calls it own. `[Inferred]` A reader sees the record end at `NOT READY` followed by a collapsed appendix.

`[Observed]` This is the identical harm §9 says the unicode fold was taken for — *"it is the disagreement between a record's bytes and a reader's eyes that this whole instrument exists to prevent"* — reachable in pure ASCII, in the same batch that closed the unicode form.

*Requires:* the validator change of RD42-01 (this is its terminal-rule consequence), plus a fixture in the silent direction. **Not offer-blocking on its own** (§9 makes no false statement about this specific construction) — **it blocks the formal administration**, and it is the single most dangerous defect I found: a laundered `NOT READY` at Administration 1 becomes the baseline every later F1 verdict is read against.

### RD42-03 — BLOCKING — the delta's *"All ten `_decl` sites read the record's **own** lines"* is false at denominator 10: `Parameter block sha256:` still reads the full active text, so §2's integrity anchor can be supplied from collapsed content **below** the terminal verdict

`[Observed]` Enumerated mechanically with Python `re` over the whole file — **10 `_decl` call sites**; nine pass `_own_text`, one passes `txt`:

```
  L 695  reads=txt        "LG-1", "Parameter block sha256:"
```

So the position rule and the containment rule are both bypassed for that field. Executed at `47adfa9`, git on, real digests:

| construction | errors |
|---|---|
| `Parameter block sha256:` present **only** inside `<details>`, **below** the terminal verdict | **0** |
| same, in a list item below the verdict | 1 (`no parameter-block sha256 recorded`) |
| same, blockquoted below the verdict | 1 |
| *control:* deleted entirely | 1 |

A record that shows the reader no parameter-block digest at all, and carries it only inside collapsed content in an appendix beneath its own verdict, validates clean. §2 (defined clause): *"The instrument must be **committed at the administered commit**, and the record quotes the instrument's sha256 and the parameter block's sha256."*

`[Observed]` This falsifies two sentences at once: D-3's *"All ten `_decl` sites read the record's own lines: a declared value carried only on non-own lines is an **absent field**, never a supplied one"*, and §9's *"**`_decl` becomes a consumer** (RD41-02): a declared value carried only on non-own lines is an absent field, never a supplied one"* together with *"a declaration is read only from lines at or above the record's own terminal verdict"*.

*Requires:* a **one-word validator change** (`txt` → `_own_text` at 696) with a fixture, and an **instrument amendment** — the §9 sentence is false of the bytes an approval digest would bind. **Offer-blocking, and it blocks the formal administration.**

### RD42-04 — BLOCKING — §9's *"sixteen mutation-reverts, **fourteen** of which fail exactly the fixtures their repair added (denominators 1, 1, 1, 43, 5, 1, 1, 1, 1, 1, 5, 1, 3, 3)"* is false: thirteen witness; D-7's revert fails **0 of 168**

`[Observed]` I built all sixteen reverts and read each selftest's output (table in §3). Fifteen reproduce exactly. The sixteenth — D-7's *"the fixture rebuilt on the v1.13 shape → **1** (it cannot fail)"* — measures **0 failing of 168**. That is RD41-11's own point: with the fixture on the v1.13 shape the selftest still passes, because the fixture cannot fail. I also tested the two alternative readings (disable `commit_exists`; disable the LG-1 existence branch) — both fail **1** under *either* fixture shape, so neither discriminates. **No mutation-revert witnesses D-7's repair.**

Arithmetic: my measured multiset for the thirteen witnessing reverts is `{1×8, 3×2, 5×2, 43}`; §9 claims `{1×9, 3×2, 5×2, 43}`. Exactly one "1" is unaccounted for, and it is D-7's.

`[Observed]` The claim also appears in the delta twice (*"**sixteen** mutation-reverts, of which **fourteen** fail exactly the fixtures their repair added and **two** fail nothing"*; *"This delta therefore claims **fourteen** mutation-witnessed repairs of sixteen reverts, and names the two that are not"*), in P-34 (*"fourteen of sixteen"*), and in PROJECT-STATUS. It is verification rule 3's own case again, inside the one artifact whose bytes a digest binds — the same class as RD41-03, in the entry written to close RD41-03.

*Requires:* an **instrument amendment** (correct to thirteen, and disclose D-7 as a third unwitnessed repair alongside D-8's two). **Offer-blocking; does not block the administration.**

### RD42-05 — BLOCKING — §9's v1.14 entry says the instrument bytes that move are *"this entry, the version header, and **four** dated correction markers in the v1.13 entry above"* — there are **five**

`[Observed]` Python `re` over the §9 v1.13 entry, pattern `\[corrected\s+2026-08-11,\s+(RD\d+-\d+)`: **five markers — RD41-01, RD41-06, RD41-02, RD41-03, RD41-04.** §9's sentence enumerates four (RD41-01, RD41-02, RD41-03, RD41-04); the delta's header says *"four dated correction markers in the §9 v1.13 entry (D-1 names them)"* and D-1 says *"four of the six also appear inside §9 … and carry dated correction markers in place"*. The RD41-06 marker — which corrects the v1.13 predicate definition's setext clause, a *fifth* false statement in that entry — is named in neither.

(A shell `grep` for the marker would have returned 3, not 5, because the phrase wraps across a line break; I used Python `re` with `\s+`. This is verification rule 1's own case, and it is why the count is worth stating with its method.)

*Requires:* an **instrument amendment** and a **record correction**. **Offer-blocking; does not block the administration.** Recorded separately from RD42-04 because it is a *second* false count in the same entry, and because a reader auditing "what bytes moved" is given the wrong number of things to audit.

### RD42-06 — BLOCKING — the *Newly accepted* axis claims *"a fenced `<details>` example, a self-closing `<details/>` in prose, a comment mentioning `<details>` … (each 1 → 0) — four lawful records the v1.13 raw-side call refused"*. Three of the four measure **0 → 0** on their own fixture bytes, and the repair they were written for has **no fixture witness**

`[Observed]` Every one of the 162 captured fixtures run through the v1.13 validator and the v1.14 validator on identical bytes. Exactly **14 of 162** move. Of the four RD41-06 restoration fixtures:

| fixture | v1.13 | v1.14 |
|---|---|---|
| #154 a fenced ```` ```html ```` `<details>` example | **0** | 0 |
| #155 a self-closing `<details/>` in prose | **0** | 0 |
| #156 an HTML comment mentioning `<details>` | **0** | 0 |
| #157 a `---` after the terminal verdict | 1 | **0** |

`[Observed]` The cause: all four fixtures append their construction **after** `good`, i.e. **below** the terminal verdict, where the v1.13 defect never fired. Placed **above** the verdict — where RD-41 measured them — the same three constructions do move **1 → 0**, so the underlying repair is real. But the fixtures shipped for it witness nothing: **reverting the raw-side predicate call to un-stripped text fails 0 of 168.**

`[Observed]` §9 carries the claim too: *"with four further lawful records restored: a fenced `<details>` example, a self-closing `<details/>` in prose, and a comment mentioning `<details>`, each of which the v1.13 raw-side call refused because it ran on *un*-stripped text"*. Measured against the v1.13 validator: it refuses none of the three as the fixtures write them. (§9 also says "four" and then names three.)

This is RD41-05's class — a directionality axis falsified by the fixture it cites — for the **fourth consecutive batch**, and this time under the delta's explicit promise *"and this time the comparison, not the intent, is what is reported"*.

*Requires:* a **validator change** (rebuild the three fixtures above the verdict so the repair has a witness) and an **instrument amendment**: the §9 sentence is false of the bytes an approval digest would bind. **Offer-blocking; does not block the administration.**

### RD42-07 — MAJOR — LG-4's new emptiness requirement is inert in §5's own record shape: a bare `## G1` with nothing of its own beneath it validates at **0 errors**

`[Observed]` `_takewhile_before_heading` (545–554) collects own lines after the G1 heading until the **next heading**. §5's template places seven declared trailer fields (`E3 reopen-list:`, `Deferred-wave findings …`, `Deferred count …`, `Reopened count …`, `Owner deferral decision:`, `Unknowns …`, `Reviewer's falsification notes:`) between `## G1` and the verdict, and **no heading follows**. So those field lines are counted as G1 section content.

Executed at `47adfa9`, git on, real digests, full roster:

| construction | errors |
|---|---|
| `## G1 — completeness critic` with **nothing of its own** beneath it, in §5's position | **0** |
| *control:* heading deleted | 1 (`no G1 section`) |
| the batch's own fixture shape (`## G1` moved to sit immediately above the verdict) | 1 (`opens an EMPTY section`) |

The repair fires only when a record reorders §5's template so nothing sits between the heading and the verdict. RD41-04's second limb — *"the heading alone satisfied LG-4 however EMPTY the section beneath it … it was in fact a load-bearing limb of a 0-error pass"* — is therefore **not closed for the shape §5 mandates**. §4 (defined clause), quoted in the validator's own error: *"an administration missing G1 is incomplete and cannot support a gate decision."*

I also confirmed the accepting direction is not damaged: G1 content written as bullets, as a blockquote, as a table, as a fenced block, or indented as code all validate at 0 errors — because the same trailer lines carry the check. That is the point: the check measures the trailer, not the section.

*Requires:* a **validator change** — the G1 section is what lies between its heading and the record's declared-field trailer, or the check must exclude `Label:`-shaped declared lines from "section content". **Not offer-blocking** (§9's sentence "LG-4 requires its heading to open a non-empty section" is literally true of the code); **it weakens the administration**, because the composite RD41-04 was found in is one `<div>` away from returning.

### RD42-08 — MAJOR — an undisclosed acceptance withdrawal, with a message untrue of the record: **any** declared field whose value is entirely angle-bracketed is refused as *"carries §5's own placeholder"*

`[Observed]` `_PLACEHOLDER_RE = re.compile(r"^\**<[^<>]*>\**$")` (1116). Measured v1.13 → v1.14 on identical bytes, git on:

| `Materials given:` value | v1.13 | v1.14 | message |
|---|---|---|---|
| `<redacted>` | 0 | **1** | *"carries §5's own placeholder ('<redacted>'), not an answer"* |
| `<as listed in §2>` | 0 | **1** | same shape |
| `<see appendix A>` | 0 | **1** | same shape |
| `<none>` | 0 | **1** | same shape |
| `<model/version or human, fresh context: yes/no>` | 0 | **1** | correct — this **is** §5's placeholder |

Only the last is a placeholder. For the other four the message asserts something untrue of the record — the class the commission names as a finding in three of the last four reviews, here reintroduced by a repair whose delta explicitly says *"a **value-quality** check, kept explicitly separate from the containment one"*.

`[Observed]` This falsifies the delta's own cost accounting: *"**Acceptances withdrawn:** the setext-underlined field line … a template quoted with §5's placeholder values … Both are intentional"* and *"This delta enumerates every withdrawal it makes and claims no completeness it has not swept."* A third withdrawal exists, is unintentional, and is undisclosed. (D-3's accepting-direction fixture guards only the case where a value *contains* brackets, not the case where it *is* brackets.)

*Requires:* a **validator change** — match §5's actual placeholder strings (read from the committed instrument, as `_target_forms` already does for LG-11), not the angle-bracket shape — and a **record correction**. **Not offer-blocking on its own; it does not block the administration** (a reviewer who hits it can rewrite the value), but the message is the kind this chain has repeatedly held to be a defect.

### RD42-09 — MAJOR — LG-6's all-quoted message is still untrue of the record: an unpaired `<details>` or `` `<summary>` `` mentioned **in prose** blanks the rest of the record and reports the verdict as *"inside a container opened on an earlier line"*

`[Observed]` D-4 claims: *"LG-6's all-quoted message enumerated five causes and could be emitted when none was true of the record. It now reports the carrier each verdict line actually sits in, computed from the same predicate that refused it."* Measured at `47adfa9`, git on, real digests, a fully lawful record whose `Operationalization notes:` reads *"I weighed a `<details>` block"*:

```
v1.13 = 4 errors    v1.14 = 7 errors
LG-4: no G1 section — an administration missing G1 is incomplete …
LG-5: no `Deferred count:` field …
LG-5: no `Reopened count:` field …
LG-6: every `GATE VERDICT:` line in the record sits inside a quotation container
      — inside a container opened on an earlier line — and a quoted verdict is
      not the record's verdict …
LG-12: required §5 field missing — 'Unknowns and what would settle them:' …
LG-12: required §5 field missing — "Reviewer's falsification notes:" …
LG-12: no `E3 reopen-list:` field …
```

The verdict is at column 0, unmarked, visible and terminal. **No container a reader can see is open.** The same happens for `` `<summary>` `` written inside an inline code span (1 error at both versions), and for a `<details>` mentioned in a table cell (8 errors). Inline code spans are *not* stripped by `_active_lines` — only fenced blocks and HTML comments are — so the canonical way a reviewer writes about an HTML carrier is the way that breaks their record.

`[Observed]` The v1.14 record is **worse** than v1.13 here (4 → 7), because the strip that fixed the fenced and commented cases moved the depth counter onto text where more of it is reachable. The delta's *"No case moves in the dishonest direction"* is about acceptance, so it is not directly falsified — but this movement is undisclosed.

`[Inferred]` This is not exotic for *this* record type. §5's template requires `Reviewer's falsification notes: <what they tried to break and couldn't>`, and the last two administrations of this instrument were about HTML quotation carriers; RD-41's own raw review names `<details>` more than twenty times.

*Requires:* a **validator change** — HTML-block tracking must be a block-structure decision (RD42-01's repair closes this too: a `<details>` in a paragraph opens no HTML block), and the LG-6 message must not report a carrier it inferred from a counter. **Not offer-blocking; it blocks the formal administration** — a refusal that tells the administrator something untrue of their record, on the one line §5 makes decisive.

### RD42-10 — MINOR — the *Acceptances withdrawn* axis lists an entry that does not move: the setext-underlined field line is **1 → 1**

`[Observed]` `Materials given:` followed by `---`, measured on identical bytes: **1 error at v1.13, 1 at v1.14**. The delta's wording (*"stays refused, deliberately, for the ATX symmetry"*) is honest, but the entry sits on a v1.13 → v1.14 *movement* axis under the heading *Acceptances withdrawn*, where it withdrew nothing — RD41-05's exact shape. RD-41 already recorded this withdrawal against v1.13.

**Do I agree the two named withdrawals should stand?** The setext one: **yes, weakly.** `Materials given: …` followed by `---` renders as an H2 heading, and `## Materials given:` never satisfied presence; the symmetry argument is sound and the cost is small and disclosed. The placeholder one: **yes in intent, no as shipped** — a record that quotes §5's template with §5's placeholder values has answered nothing and should be refused, but the rule as written refuses far more than that (RD42-08).

*Requires:* a **record correction**. **Not offer-blocking.**

### RD42-11 — MINOR — LG-4's anchor accepts `###G1`, which CommonMark does not read as a heading, and the two G1 regexes in the same check disagree

`[Observed]` `re.match(r" {0,3}#{1,6}[^\S\n]*G1\b", …)` (832) accepts `###G1 was considered` — measured, 0 errors — while the very next lines use `r" {0,3}#{1,6}(?:[^\S\n]|$)"` (838, 551), which requires the space CommonMark requires. So a line that is not a heading opens the G1 section, and the same line would not *close* it. RD37-03's family ("a heading that merely mentions G1") in a narrow form.

*Requires:* a **validator change** (one regex, used in all three places). **Not offer-blocking.**

### RD42-12 — MINOR — the non-authority banner is satisfied by an explicit quotation of itself in an appendix labelled "not an answer", and this residual is not disclosed

`[Observed]` A record with **no** banner in its body, carrying instead an appendix headed *"§5's preamble, quoted for reference only. Nothing here is an answer."* followed by the two blockquoted banner lines, scores **0 errors** at both v1.13 and v1.14; the control (banner deleted, no appendix) scores 1. The `bq1` test cannot distinguish a declaration from a quotation, because §5's banner *is* a blockquote — the same structural fact that forces the blockquote-laziness limit, applied to the one field whose form is a container. Pre-existing, not a v1.14 regression; arguably harmless (the reader does see the text). Recorded because the *Disclosed limits* section names the blockquote residual and not this consequence of it.

*Requires:* a **record correction** (add it to the disclosed limits) or a validator change. **Not offer-blocking.**

### RD42-13 — MINOR — the predicate's cost is super-linear in container depth

`[Observed]` Timings, git on, at `47adfa9`: a 2000-deep and a 5000-deep nested blockquote → 0.01 s / 0.02 s; 20 000 sibling list items → 0.25 s; **a 1500-deep nested list → 6.02 s**. It terminates (each opening iteration consumes at least one character) and no realistic record reaches this, but the growth is quadratic in depth and undisclosed.

*Requires:* nothing beyond disclosure. **Not offer-blocking.**

### Nits, no action requested

- The delta's *"the list-item-continuation composite (6 errors, was 0)"* is **unverifiable by a third party**: RD-41's composite bytes are stored nowhere in the repo. My independently built composite scores 4 (above the verdict) / 5 (below). The direction reproduces; the number cannot be checked.
- `**Label:*` (asymmetric bold) still satisfies presence — disclosed and carried forward.
- The trend row is still printed above the error list carrying a claimed verdict for an invalid record — disclosed and carried forward, and visible in RD42-02's output.

## 5. Falsification notes — what I tried that did **not** break it

`[Observed]` Each is an execution at `47adfa9`, git checks **on**, against the real committed instrument and §8 digests.

- **The block-structure predicate, attacked directly.** Twelve container constructions, each placing a `Materials given:` line where a reader sees it as quoted, **all correctly refused**: a blank line inside a list item followed by an indented continuation; two-deep nested list items; `1)` and `99.` ordered markers; a tab-indented continuation; `> - ` (list inside blockquote); `- ` containing `> ` (blockquote inside list); a list item resumed after a blank line and a paragraph; a marker followed by four spaces; a thematic break inside an item; a `<details>` block with a blank line inside it; a table cell. The stack maintenance, the content-column arithmetic and the lazy-continuation guard are all correct on everything I could construct. **RD41-01's repair is genuine, and it is the first repair in this chain specified over a property rather than a list.**
- **Ordered-list edge cases.** `1234567890.` (ten digits) is correctly *not* a list marker, matching CommonMark's nine-digit cap.
- **CRLF** throughout the record — 0 errors, correct verdict; raw and active line indices stay aligned.
- **Termination and time** — see RD42-13; nothing hangs, nothing recurses without bound.
- **The position rule.** I could not evade it: a field declared below the terminal verdict is absent (0 → 1); an appendix below the verdict declares nothing in any container — *except* through `_paramd`, which is RD42-03, and that is a missing consumer rather than a hole in the rule. I could not make it **over**-reject either: §5's template puts every field above the verdict, and 19 lawful-record variations all validate.
- **The placeholder rule, accepting direction.** A value that merely *contains* angle brackets (`the fixed §2 list <plus the parameter block>, no deviations`) is correctly accepted; only the all-brackets form over-rejects (RD42-08).
- **Lawful-record battery, v1.13 → v1.14, 19 constructions:** G1 as bullets / blockquote / table / fenced block / indented code; ordered and nested lists above the verdict with a blank line; an HTML `<table>` evidence appendix; `<br>` in prose; a footnote line; a 4-space paragraph continuation; a setext H1 section title; a thematic rule; bold field labels; `**Materials given:**`. **Every one scores 0 at both versions.** Only three moved (RD42-08's angle-bracket case, and the two RD42-09 HTML-prose cases, which were already refused).
- **`_decl` shadowing.** The behavioral decoy loop (both orders, every declared label) passes; a disagreeing decoy at column 0 in an appendix fires the disagreement error loudly in both directions.
- **The §4 conjunct battery, the roster, the scoped form, and `--prior` recursion** — all 168 fixtures pass, all 13 checks fire, and the recursion is depth 1 with the honest cap unchanged.
- **`check_governance.py`** — 30 OK, 18 WARN, 0 FAIL (48 checks); `--selftest` 121 fixtures, 0 failing.

## 6. Overall assessment

The central repair is real and it is the right shape. `_own_flags` is now a block-structure scan that maintains containers across lines, and I could not break it on any markdown container I could construct — twelve tries, all refused, including the three carriers RD-41 built. Fifteen of sixteen mutation-reverts reproduce at exactly the claimed denominators. The blockquote-laziness decision is genuinely forced by §5's frozen template, correctly measured at 43 of 168, and — the best discipline in this batch — **fixtured in its accepting direction rather than described**, with the two guard fixtures for the unwitnessed predicate limbs *named in their own labels* as defence-in-depth rather than counted as proof. §1–§8 have not moved in seven amendments and §8 in ten versions, both swept at every commit; the frozen population is 32/31/1/0 exactly; the version sweep is clean at denominator 375; all thirteen checks fire; the disclosed-limits section is, for the first time in four batches, true sentence by sentence.

And the class survived a **sixth** time, in the same shape, for a reason worth naming precisely. RD-41 said: the predicate must carry state, because a container is a region, not a line. The batch built that — for markdown. For HTML it wrote `<(?:details|summary)\b` and a counter. So `<div>`, `<p>`, `<span>` and `<table>` are not containers at all, and `<details>` itself reopens the moment the word `</details>` appears anywhere in the record's text, including inside an inline code span that renders as literal prose. Through that door: `E3 reopen-list: empty` supplied from collapsed content while the reopen items are visible above it, at 0 errors under `READY FOR <the verbatim target>`; the owner's deferral citation invisible; and — the one that matters most — a record whose **visible terminal line reads `GATE VERDICT: NOT READY`** entering the trend log as `READY FOR Capability 1 — Project registration and honest shape visibility`, `record valid`, exit 0. That is RD41-08's harm, the harm §9 says the whole instrument exists to prevent, reproduced in pure ASCII by the batch that closed its unicode form. Beside it, §2's parameter-block digest can be supplied from an appendix beneath the verdict, because one of the ten `_decl` sites was not converted and the delta says all ten were.

Underneath that sit four more §9-or-delta sentences that measurement contradicts, three of them counts: "fourteen" mutation-witnessed repairs where thirteen is the fact; "four" dated correction markers where five is the fact; "each 1 → 0" for four restored records where three of the four never moved and the repair behind them has no witness at all. The count errors are RD41-03's class, in the entry written to close RD41-03. The directionality error is RD41-05's class, under this delta's own promise not to repeat it, for the fourth consecutive batch.

The thing I would put in front of the v1.15 batch is one sentence, and it is the same sentence RD-41 wrote, applied one level down: **HTML is a container too.** `<div>`, `<p>`, `<table>`, `<details>` — every one of them opens a region, every one continues without repeating its tag, and a counter over two tag names is exactly the enumeration RD-40 asked the chain to stop writing. Put HTML blocks into the same stack the markdown containers already live in, with CommonMark's start and end conditions, and RD42-01, RD42-02 and RD42-09 close in one stroke — the exploit, the verdict laundering, and the false refusal that tells an administrator their visible verdict is inside a container. Then convert `_paramd` and recount §9's three numbers against the bytes, with the command that produced them written down. Everything else in this batch is sound.

On the two questions asked, in these words:

- **May v1.14 be offered to the owner at P-34?** **No.** The mechanism, ordering, options, precondition and correction pointers are right; D-1's six corrections are each true of the v1.13 bytes and I re-measured them rather than assuming; the frozen record is untouched at 32/31/1/0; the fixture arithmetic reconciles to the printed count two ways; §1–§8 have not moved; the disclosed-limits section is honest; and RD41-01's repair is the best work in this chain. But **five sentences inside §9 and the delta — the bytes an approval digest binds, and the record that explains them — are false of those bytes**: that the predicate's stack carries a *"raw-HTML block"* (it carries two tag names, and a `<div style="display:none">` supplies `E3 reopen-list: empty` at 0 errors under `READY FOR <the verbatim target>`); that *"All ten `_decl` sites read the record's own lines"* and that *"a declaration is read only from lines at or above the record's own terminal verdict"* (§2's parameter-block digest is read from anywhere, including collapsed content below the verdict); that there were *"fourteen"* mutation-witnessed repairs (thirteen — D-7's revert fails 0 of 168); that *"four dated correction markers"* moved in the v1.13 entry (five did); and that *"four further lawful records"* were restored *"each 1 → 0"* (three of the four measure 0 → 0 on the fixtures' own bytes, and the repair behind them has no fixture witness). On the RD38-02 / RD39-02 / RD40-01 / RD40-02 / RD41-03 precedent this batch itself invokes in its own five dated markers, **the digest v1.14 would bind is not the digest that should be approved.**

- **May the formal launch administration run on this validator?** **No.** Four independent constructions produce a clean `record valid` and a nine-column trend row reading `READY FOR Capability 1 — Project registration and honest shape visibility`: a record whose decisive `E3 reopen-list:` lives only inside a `<div>`, `<p>`, `<span>` or `<table>` a reader never sees while its reopen items are visible above it; the same through a `<details>` block that stays collapsed because the validator's counter was reset by a code span; a record whose owner deferral citation is invisible; and — the worst — a record whose **last visible line reads `GATE VERDICT: NOT READY`**. A fifth passes with §2's parameter-block digest supplied from beneath its own verdict. Against them sit lawful records the validator refuses with a message untrue of them: any record whose falsification notes mention `<details>` or `` `<summary>` `` in prose, and any record answering a declared field with an angle-bracketed value. Any one of these, at Administration 1, becomes the baseline every later F1 verdict is read against.

VERDICT: REVISE
