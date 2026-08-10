The clone is byte-clean at close (`git status --porcelain` empty, HEAD `7751f12e…`, both digests re-confirmed by two methods, zero `.pyc` under the clone). Writing the review of record.

---

# RD-40 — Launch-gate instrument re-review, v1.12 exact bytes (round-2026-08e, frozen commit 7751f12)

- Review id: RD-40 (eighth administration of the instrument re-review chain: RD-33 → v1.6, RD-34 → v1.7, RD-35 → v1.8, RD-36 → v1.9, RD-37 → v1.10, RD-38 → v1.11, RD-39 → v1.12)
- Date: 2026-08-10/11
- Subject: `launch-gate-pre-specifications.md` (v1.12, repo root), `scripts/launch_gate_results.py`, `round-2026-08e/LAUNCH-GATE-v1.12-SEMANTIC-DELTA.md`, `decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` (P-34), the RD-39 section of `reviews/DISPOSITION-REGISTER.md`, and `reviews/RD-39-instrument-v111-RAW.md` read in full (251 lines, 7 findings, `VERDICT: REVISE`)
- Subject sha256, computed this session by two independent methods (`sha256sum` and Python `hashlib`): `4ad21f8087ca110ecdc5392535ea74f7fc96a7a88e75da07582a74596077c686`, 66011 bytes — matches the charter
- Validator sha256: `471648ca71d88d30b223f9fdf542c75073fb5bf332f854905c91830f77d25ace` (1976 lines)
- §8 parameter block, extracted by the validator's own `param_block_bytes`: `01209c0f052971f794e1f35827a002aa8d80420aad471d10fde000abb6366ff6`, **6610 bytes** — computed at **all 10 commits** that have ever touched the instrument: identical digest and length at v1.5…v1.12 (**eight versions**, exactly the delta's claim), differing only at v1.4 (4067) and the pre-v1.4 commit (2084)
- Frozen clone `…/scratchpad/clone-08e-r20`: HEAD `7751f12e6086f226c42fb55ee02b509e16421251`; `git status --porcelain` **empty at open and at close**, `git diff HEAD` empty, **zero `.pyc` written inside the clone** (the mutated copies were run as scripts from `…/scratchpad/rd40/`, never imported from the clone's tree). Every synthetic record, mutated validator copy and v1.10/v1.11 sandbox lives in `…/scratchpad/rd40/`. Nothing in the live repository was read or touched.
- Reviewer: isolated fresh-context session, Claude family. Same-family re-review — F5's own example applies to me
- Authoring context: none. I authored no byte under review

---

## 1. Method and what I ran

`[Observed]` `python3 scripts/launch_gate_results.py --selftest` in the clone → **132 fixtures, 0 failing, exit 0**, and exactly **132 `pass` lines**, **0 `FAIL` lines**, no skip notes. The count is read from the tool's own printed output, never assumed.

`[Observed]` A record generator matching §5's template field-for-field (39 roster rows, all eight declared fields, the blockquoted non-authority banner, the G1 section), invoking **the clone's own validator as a subprocess with `cwd` = the clone**, so `REPO` resolves to the clone and git checks ran **ON** against the real commit `7751f12e…`, the real committed instrument digest `4ad21f80…`, the real §8 digest `01209c0f…` and the real `effective_version: v1.12` — LG-1/LG-2/LG-11 and both citation-existence paths executed on every case below. Approximately **110** synthetic records.

`[Observed]` **Mutation-revert testing (rule 6)** on **eleven** copies outside the clone, each with `REPO` patched to the clone so git-on fixtures still run. Recorded in §2 and §3.

`[Observed]` **Cross-version execution.** I rebuilt the v1.11 validator from `git show c70e756:scripts/launch_gate_results.py` (sha256 `5d41fe1a…`, 1798 lines — matching RD-39's measurement exactly) and the v1.10 validator from `git show 34cbe5e:…` (sha256 `f24e95d4…`, 1564 lines) and ran the *same* records through them. **27** paired comparison cases plus targeted re-measurements of RD-39's own constructions.

`[Observed]` Fixture→check coverage computed mechanically by intercepting `validate()` and binding each emitted error to its `LG-n` prefix. Denominator **13** checks.

`[Observed]` Repo-wide sweep with Python `re`, never shell grep (rule 1). Denominator **364** text files.

`[Observed]` `python3 scripts/check_governance.py` in the clone → **30 OK, 18 WARN, 0 FAIL (48 checks)**; `--selftest` → **121 fixtures, 0 failing**.

`[Unknown]` I did not administer the gate and read no pilot record content. All answer sets below are synthetic.

---

## 2. Per-finding repair verification — all seven RD-39 findings

| RD-39 | Class | Disp. | Status | Anchor / proof in the v1.12 bytes |
|---|---|---|---|---|
| RD39-01 | BLOCKING | R | **verified-closed for the fenced and comment carriers by execution and mutation; defeated one carrier out — RD40-01** | `_gv_raw` (701) is computed over the raw bytes and `_gv_lines[-1] != _gv_raw[-1]` (707) errors loudly. Executed at `7751f12`, git on, real digests: RD-39's laundered record (`READY FOR <verbatim target>`, unterminated ``` fence, stored terminal `GATE VERDICT: NOT READY`) → **1 error, trend verdict column `—`**, never READY — exactly the delta's claim. The four-space-indented-backtick carrier → **0 errors, trend verdict `NOT READY`** (its visible verdict parsed correctly). A fenced verdict quoted after the terminal → 1 error; an HTML-comment one → 1 error; a comment *swallowing* the terminal verdict → 1 error (v1.11: 0 errors and a silent `NOT READY`). RD35-02's fixtured control (earlier pass line + qualified terminal, no fence) still errors, 1 error, message unchanged. **Mutation M1** (terminal rule reverted to active-text-only) → `132 fixtures, 2 failing`, exactly the two RD39-01 fixtures. **But** the rule is stated over *stripping*, not over *quotation*: a verdict line quoted after the terminal one in a blockquote, a ≥4-space-indented code block, a list item, or one line of prose is in raw **and** active text, so it silently becomes the terminal verdict — **RD40-01**. |
| RD39-02 | BLOCKING | R | **verified-closed for all four named carriers by execution and mutation; the composite reproduces whole through a fifth — RD40-02** | `_active_text` (340–398) now strips HTML comments with a state machine; `_label_present` (813–818) is a line-anchored field read; the banner has a structural blockquote test (836–843). RD-38's composite rebuilt verbatim (banner, `Reviewer:`, `Reviewer model family:`, `Materials given:`, `Operationalization notes:`, `Reviewer's falsification notes:` deleted, G1 replaced), git on, real digests, terminal `READY FOR <verbatim target>` — measured per carrier: **fenced 7, HTML comment 7, blockquote 6, four-space-indented 7, prose 7 — zero clean passes**, matching the delta's stated numbers exactly. Lawful direction: bold-wrapped, `- `/`* `/`+ ` list-marked, double-spaced, and space-before-colon label forms all accepted (0 errors, 6 of 6); an inline comment on a lawful line harmless. **Mutations:** M2 (comment strip removed) → 2 failing, exactly the two comment fixtures; M3b (presence *and* banner reverted to substring scans) → 5 failing, exactly the four carrier rejections plus the RD39-07 double-space acceptance — the delta's denominator of 5 reproduces. **But** a bullet-list carrier satisfies all six `Label:` tokens, and combined with the *disclosed* nested-blockquote banner limit the full composite validates at **0 errors** under READY — **RD40-02**. |
| RD39-03 | MAJOR | R | **verified-closed** | The internal-whitespace fixture exists (1950–1954). Reverting `_decl`'s return to the **exact v1.10 bytes** (`vals[-1].strip()`, v1.10:347, quoted from `git show 34cbe5e:`) → **M4: 132 fixtures, 1 failing**, exactly that fixture. I re-measured RD-39's premise myself: the same revert applied to the **v1.11** bytes → `116 fixtures, **0 failing**` — RD39-03 confirmed by my own execution, and rule 6 is now satisfied against the code the repair replaced. The §9 v1.11 entry carries the dated marker in place, quoted from the diff: *"[corrected 2026-08-10, RD39-03: false for one of the eight — reverting `_decl`'s return to the exact v1.10 bytes failed nothing, because v1.10 returned a stripped value, not a raw one; see the v1.12 entry below]"*. |
| RD39-04 | MAJOR | R | **closed in form — the statement is restated on three axes — but the restatement is itself incomplete, in the same way — RD40-05** | The "What did not change" section now has *Newly rejected* / *Newly accepted* / *Same acceptance, changed verdict*. I verified each named item by fixture or execution (§3). **But** D-4's fence-grammar change is listed only under *Newly rejected* while the fixture the batch shipped for it asserts an **acceptance** — measured: the four-backtick/three-backtick record scores **1 error at v1.11, 0 at v1.12** — and several HTML-comment consequences are unlisted on either side. |
| RD39-05 | MINOR | R | **verified-closed** | `validate()` recurses at depth 1 (915–917), prior's own `--prior` never followed (source, and by construction). Executed, git on, real digests: bare roster-complete block with lawful verdicts → **refused** (19 prior errors, trend column `n/a — prior record failed validation`); all-`Not met` fabrication → **refused** (18 errors) — the New-findings column never reads `0`; a prior naming a nonexistent commit → refused; a prior with a qualified terminal verdict → refused (its own LG-6). **I built RD-39's own construction:** a lawful **v1.11-era** record naming commit `c70e756`, `Instrument version: v1.11`, instrument digest `506463ff…`, §8 digest `01209c0f…`, and a lawful **v1.10-era** record naming `34cbe5e`, `v1.10`, `3cb0814e…` — **both accepted as priors, 0 errors, New-findings `1`**. The prior's errors fold as **one** summary line naming the count and the first error, not as N lines. Performance: a 20 000-line prior validates in 0.20 s (0.08 s baseline). The §9 marker is present, quoted. |
| RD39-06 | MINOR | R | **closed for space indentation; open for tab indentation — RD40-03** | Fence marker counts only at `indent <= 3` (392–395); closing run must be same char and `>= fence_len` (373–375). Measured: 3-space open / 4-space close → fence stays open (correct); 4-backtick open / 3-backtick close → content stays stripped (**M7** → 1 failing, exactly its fixture); nested different-length fences correct; `~~~` opened and ``` closed does not close; tilde fences, info strings, mid-line backticks and blockquoted fences all still correct. **M6** (indent bound removed) → 1 failing, exactly the indented-carrier fixture. **But** `indent = len(ln) - len(ln.lstrip())` counts a **tab** as one column; CommonMark expands tabs to a 4-column stop, so a tab-indented ``` is literal content there and a fence here — **RD40-03**. |
| RD39-07 | MINOR | R | **verified-closed** | `Reviewer  model family: human` (two internal spaces) → **0 errors** (v1.11: 1 error asserting the field missing); `Materials given : …` → **0 errors** (v1.11: 1 error). Bold, list-marked and nested-list forms accepted. Fixtured in the accepting direction (1929–1944). |

**Tally, with its denominator:** of RD-39's **7** findings, **7 are present in the v1.12 bytes and none is absent**; **3 are closed outright** (RD39-03, RD39-05, RD39-07); **3 are closed for every carrier and rule the finding named, with the class surviving one carrier out** (RD39-01 → RD40-01, RD39-02 → RD40-02, RD39-06 → RD40-03); **1 is closed in form with its restatement incomplete** (RD39-04 → RD40-05). All **seven** claimed mutation-reverts reproduce at exactly the claimed denominators — 2, 2, 1, 1, 5, 3, 1 (§3).

---

## 3. Verification of the delta's and the records' claims

`[Observed]` **"No section §1–§8 changed."** True. Per-section sha256 with a fence-aware splitter, `git show c70e756:` vs `7751f12`, **ten sections each side, denominator 10**: §1 `af875539…`, §2 `28c745f6…`, §3 `4143073e…`, §4 `7952a130…`, §5 `aa7a227c…`, §6 `5884c5ae…`, §7 `bdc18cf9…`, §8 `4ff1b986…` — **all eight identical**. Only `HEADER` and `## 9. Changelog` differ. The instrument diff is **110 lines**: one `effective_version:` line, three dated correction markers inside the §9 v1.11 entry, one appended v1.12 entry. **Zero question blocks changed; no ID renumbered; no verdict word changed.** Read line by line off the diff; nothing else inside §9 moved.

`[Observed]` **§1–§8 stability across the chain, measured.** The set of instrument versions whose §1–§8 hash identically is {v1.7, v1.8, v1.9, v1.10, v1.11, v1.12} — **six versions, five version-to-version amendments**. P-34's and PROJECT-STATUS's *"six amendments byte-unchanged"* uses the version count (RD-39 used the same convention at v1.11, calling it "the fifth"); the substance is exact, the noun is loose. Carried-forward wording, not a new defect.

`[Observed]` **D-1's four corrections of the frozen v1.11 delta are each true of the v1.11/v1.10 bytes, and the frozen record is not edited.** Re-measured, not assumed: (1) the composite scores **0 errors under v1.11** in the HTML-comment, blockquote, indented and prose carriers, all four printing `READY FOR <verbatim target>` — "reaches every check" was false; (2) v1.10:347 reads, quoted, `return vals[-1].strip() if vals else None` — a **stripped** value, so D-7's premise was false, and reverting v1.11's return to those exact bytes fails **0 of 116**; (3) the fenced-appendix record scores **9 errors at v1.10 and 0 at v1.11** (I ran the v1.10 validator against a v1.10-era record at `34cbe5e` with v1.10's own digests) — an acceptance the v1.11 delta filed reject-only; and the trailing-space none marker scores 0 at v1.11 as at v1.10; (4) a lawful v1.10-era record scores **0 errors** under this validator at its own named commit — the impossibility claim was false. The three that sit inside §9 carry **dated correction markers in place**, quoted from the diff, in the RD36-01/RD38-02 convention.

`[Observed]` **Fixture arithmetic reconciles to the printed count.** 116 + (1 + 3 + 1 + 3 + 4 + 3 + 1 = 16) = **132**, and the selftest prints `132 fixtures, 0 failing`. I counted the v1.12 block's new `case()` calls and the one added bespoke prior fixture: 16, itemized exactly as the delta lists them. The lawful-appendix fixture is **reshaped** (its appendix no longer quotes a verdict line), not added — as D-2 states.

`[Observed]` **Fixture→check coverage, denominator 13.** Emissions across the selftest, computed by intercepting `validate()`: LG-1 (31), LG-2 (11), LG-3 (42), LG-4 (10), LG-5 (20), LG-6 (17), LG-7 (30), LG-8 (3), LG-9 (12), LG-10 (9), LG-11 (15), LG-12 (57), LG-13 (12). **All thirteen fire; none is absent.** 269 total emissions. `validate()` invocations = **138** = 132 fixtures + the 6 recursive prior validations D-5 introduced — the arithmetic of the recursion is visible and correct.

`[Observed]` **The seven mutation-reverts, each reproduced at its claimed denominator.** M1 terminal rule → active-text-only: **2** (the two RD39-01 fixtures). M2 comment strip removed: **2** (the two comment fixtures). M3b presence + banner → substring scans: **5** (four carrier rejections + the double-space acceptance). M4 `_decl` return → exact v1.10 bytes: **1**. M5b the **exact v1.11 prior guard**, lifted verbatim from `git show c70e756:`: **3**. M6 fence indent bound removed: **1**. M7 closing-run rule removed: **1**. Every failing fixture is one its repair added. **One honest qualification, measured (RD40-08):** M5b's 3 includes the two RD38-06 prior fixtures, which fail only because they assert the literal string `RD39-05` in the error message; with the ID added to the v1.11 guard's message (M5c) only **1 of 3** fails behaviorally. The other two are genuine regression guards for behavior v1.11 already had — they are not witnesses.

`[Observed]` **No frozen record was edited.** Denominator **30** frozen artifacts (nine v1.4–v1.11 launch-gate deltas, two Wave deltas, nineteen RD-* raw reviews): **28 byte-identical** to their state at `c70e756`, **0 changed**, **2 added** (the v1.12 delta `8e073786…` and `RD-39-instrument-v111-RAW.md` `0fac98b0…`). The delta names the frozen population explicitly and calls out the added raw review — the loose *"byte-identical to their pre-batch state"* phrasing RD-38 and RD-39 both flagged is **fixed**.

`[Observed]` **P-34 is coherent at v1.12.** The question names **v1.12** (L11); the offer-status block is dated 2026-08-10, says *"not yet offerable"*, summarizes RD-39's two BLOCKING findings and the three false §9 sentences correctly, and names **RD-40** as the precondition (L65); option (a) lists **all nine** deltas with correction pointers before the claims they correct — including *"read with the v1.12 delta's D-1, which corrects its 'reaches every check' claim, its D-7 premise and mutation claim, its directionality statement, and its D-6 impossibility sentence"* (L134–137); option (b) carries the **v1.13** ordering (amendments before the digest, RD33-11, L148/L232); the recommendation reads **"132 in all"** (L195), matching the printed count; the approval block (L219) names **v1.12**. `PENDING-OWNER-DECISIONS.md:188` and `PROJECT-STATUS.md:128–182` both name v1.12, name RD-40 as the precondition, carry 132, and describe the chain accurately.

`[Observed]` **Stale-version sweep, denominator stated.** 364 text files scanned; **100** lines carry both a launch-gate token and a `v1.x` token, across **29** files; all 100 read and classified. **7** name v1.12; every one of the **93** that do not is a delta filename or title, a §9 changelog back-reference (8), a frozen raw review (52), a historical disposition or delivery-register row, a round-08d artifact, the v1.3 pilot (`PROJECT-STATUS.md:131`, corrected at :135; `LAUNCH-CLOSURE-PREFLIGHT.md:35` under its historical banner), the `.beads` charter row, or P-34's own nine-delta list. **No routed artifact names a stale instrument version.**

`[Observed]` **Two sentences inside the instrument's §9 v1.12 entry are false of the bytes**, and one row of the disposition register with them — RD40-01, RD40-02 below.

---

## 4. The property-direction audit — RD-39's own standard, applied

RD-39's rule, adopted verbatim by this batch: *"a repair must be specified over the **property** the instrument requires … then verified against every carrier and every downstream rule that property touches, including the rules the repair itself newly stands upstream of."* The table asks, for each property, **which carriers realize it** and **which rules are computed over text the strips edit**.

| Property the instrument requires | How v1.12 implements it | Carriers / rules enumerated | Direction satisfied? |
|---|---|---|---|
| **The record's own last verdict line** (§5 "terminal") | `_gv_raw[-1]` vs `_gv_lines[-1]`, string equality | Fenced ✔ refused; HTML-comment ✔ refused; unterminated fence ✔ refused; **blockquote ✘**, **≥4-space indented code block ✘**, **list item ✘**, **running prose ✘** — each becomes the terminal verdict | ***NO* — RD40-01.** The repair is stated over *what the strip removed*, not over *what a quotation is*. Four carriers `_active_text` deliberately does not strip are therefore indistinguishable from the record's own line |
| **The record's own structure, not a quotation of it** (presence) | `_label_present` line-anchor + structural banner blockquote test | Blockquote ✔, ≥4-space indent ✔, prose ✔, ATX heading ✔, table cell ✔ all refused; **list item ✘** (all four markers, incl. nested `  - `), **setext heading ✘**, **`<details>` block ✘** satisfy; banner: nested blockquote ✘ (disclosed) | ***NO* — RD40-02.** The anchor admits the list marker as *lawful decoration*; a bullet-list quotation of §5's template is therefore the record's own fields |
| **The record's own declared values** (`_decl`) | findall + disagreement + `_norm_ws(vals[-1])`, 10 of 10 sites `^`-anchored with `[^\S\n]*` | All ten sites audited from source; narrative mentions inert; empty fields absent; internal whitespace normalized; agreeing duplicates not shadows | **yes** — 10 of 10, and now mutation-proven against the code it replaced |
| **The prior's own anchors** | full recursive `validate()` at the prior's own named commit, depth 1 | Bare block ✔ refused; fabrication ✔ refused; bad commit ✔ refused; unlawful terminal ✔ refused; lawful v1.10-era and v1.11-era priors ✔ accepted; recursion bounded; perf linear | **yes** — with the stated honest cap. One unstated consequence: the prior is judged by **v1.12's rules**, not its own era's, so a record lawful when it was administered can be refused as a prior |
| **Which bytes are "the record"** (`_active_text` grammar) | fence marker at `indent <= 3`, closing run `>=` opening | Space indentation ✔ aligned; **tab indentation ✘** (tab counted as 1 column, CommonMark counts 4); tilde/info-string/mid-line/blockquoted all ✔ | ***NO* — RD40-03.** "CommonMark's own bound" is a column bound, not a space count |
| **Every rule newly downstream of a strip** | HTML comments added to the strip this batch | Rows ✔ loud; G1 anchor ✔; presence ✔; `_decl` ✔; terminal verdict ✔ (raw rule catches it); **an inline comment on the terminal line ✘** errors as if the verdict were hidden | **partly — RD40-06.** The batch did ask this question of its new strip; one case answers wrongly and its message misdescribes the cause |
| *(cross-cutting)* rule 6 — each repair proven against the code it replaced | 7 reverts | All 7 reproduce at 2/2/1/1/5/3/1 | **yes**, with RD40-08's qualification: 2 of D-5's 3 are ID-string assertions, not behavioral witnesses |
| *(cross-cutting)* the fixture suite's own integrity | 132 fixtures | 13/13 checks fire; 138 `validate()` calls accounted for; **one fixture can no longer fail** | ***NO* — RD40-04.** The LG-11 version fixture's unmutated baseline already emits the substring it asserts |

**Reading the denominators:** of the **8** rows, **4 satisfy the direction standard and 4 do not**. Every one of the four failures is the *same shape*: the repair was verified against the carriers and rules **the last reviewer named**, and the class survived in the carrier or column the last reviewer did not happen to construct. That is the fourth consecutive batch in which this is the true finding.

---

## 5. New findings

### RD40-01 — BLOCKING — a verdict line quoted after the record's own terminal verdict, in any carrier `_active_text` does not strip, silently becomes the terminal verdict: a record whose own `GATE VERDICT:` reads `NOT READY` validates with **0 errors** and enters the trend log as `READY FOR <the verbatim launch target>`. The §9 v1.12 entry says this cannot happen

Instrument §9, v1.12 entry (quoted from the diff): *"now, if the raw terminal line is not the active terminal line, the record errors loudly and no earlier line is parsed in its place — **a verdict quoted after the record's own terminal verdict is ambiguous, never silently resolved** (RD39-01…)"*. The delta's D-2 says the same: the record errors *"or shadowed by a quoted verdict line placed after the record's own"*. The disposition register's RD39-01 row says *"A stored `NOT READY` can never again be reported as `READY FOR`."*

`[Observed]` All three are false of the bytes. The rule is `_gv_lines[-1] != _gv_raw[-1]` (707) — a comparison between the raw text and the *stripped* text. A quotation carried in a blockquote, a four-space-indented code block, a list item, or one line of running prose is present in **both**, so raw and active agree and the quoted line is parsed as the terminal verdict. Executed at `7751f12`, git on, real digests, full 39-row roster, `F2 | Met`, `E3 reopen-list: empty`. Record tail, verbatim:

```
GATE VERDICT: NOT READY

> Quoting §5's template for reference:
> GATE VERDICT: READY FOR Capability 1 — Project registration and honest shape visibility
```

The administrator's own output, verbatim:

```
rows parsed: 39 (Met 38, Not met 0, scoped 0, Unknown 1) — …
trend row:
| 2026-08-10 | 7751f12e | 0 | 0 | 1 | 0 | 0 | n/a — no prior record supplied | READY FOR Capability 1 — Project registration and honest shape visibility |
record valid — verdict semantics remain the instrument's, not this tool's
```

`[Observed]` **Four carriers, all measured at 0 errors with the READY trend row:** `> GATE VERDICT: …` (blockquote — §5's own banner form); `    GATE VERDICT: …` (four-space indent — CommonMark's indented code block, the *quotation* form the batch itself just taught the fence grammar to respect); `- GATE VERDICT: …` (list item); and one line of prose, *"For reference, §5's template terminal line reads GATE VERDICT: READY FOR Capability 1 — Project registration and honest shape visibility"*. The fenced and comment carriers are correctly refused (1 error each) — so the repair closed exactly the two carriers `_active_text` strips and no others.

`[Observed]` **This is not a v1.12 regression** — the same records score 0 errors and the same READY verdict at v1.11 — but it is RD39-01's *harm*, unreached by RD39-01's *repair*, and §9 asserts it is closed. The exploit needs a formula-consistent record (all E Met, no plain Not met in A–D, F2/F3/F4 Met, deferrals zero) — the same precondition RD-39's own laundered record had. That is precisely the record that matters: an administrator whose rows are all Met but who writes `NOT READY` on the non-mechanical grounds §2 and §7 own (fresh context not honored, same-family administration, incomplete materials) has their verdict silently overwritten by a line they quoted.

*Requires:* a **validator change** — the terminal-verdict rule must be specified over the property ("the record's own verdict line"), which means a line-anchored test (no blockquote marker, ≤3 spaces of indentation, no list marker, the token at the start of the line) computed over the raw bytes, with any *other* token-carrying line after it an ambiguity error — plus a fixture per carrier. **An instrument amendment**: the §9 v1.12 sentence quoted above is false of the bytes the approval digest would bind, exactly as with RD38-02 and RD39-02. Plus a **record correction** to D-2's fourth limb and the register's RD39-01 row. **Offer-blocking, and it blocks the formal administration.**

### RD40-02 — BLOCKING — RD-38's composite reproduces whole: banner, six declared fields and the G1 section deleted, the template quoted as a **bullet list**, `0 errors`, `record valid`, `READY FOR <the verbatim launch target>`. The §9 v1.12 entry's disclosed-limit sentence is false

Instrument §9, v1.12 entry (quoted from the diff): *"the composite rejects in all four carriers (disclosed limit: a nested-blockquote quotation of the banner still satisfies the banner's structural test, because §5's banner is itself a blockquote — **the other six fields and LG-4 still reject such a record**)."*

`[Observed]` `_label_present` (813–818) builds `^ {0,3}(?:[-*+][^\S\n]+)?\**…[^\S\n]*:`. The optional list marker was added to close RD39-07's *lawful* decoration; it also admits the canonical markdown form of a quoted field list. Presence-carrier sweep, denominator **21** carriers, each measured by execution:

| carrier of `Materials given:` | presence |
|---|---|
| column 0, 3-space indent, `**bold:**`, `**bold:*`, `Label :`, `Label  given:` | **satisfied** (lawful — the RD39-07 acceptances) |
| `- `, `* `, `+ `, `  - ` (nested), `- **bold:**` | **satisfied — the quotation carrier** |
| setext heading (`Label:` + `---`), inside `<details>` | **satisfied** |
| `> `, `> - `, 4-space indent, tab indent, `## ` heading, `_italic:_`, table cell, mid-line prose | refused ✔ |

`[Observed]` Combined with the *disclosed* nested-blockquote banner limit and a column-0 `## G1` heading under an appendix header, the composite validates clean. Executed at `7751f12`, git on, real digests, terminal `GATE VERDICT: READY FOR Capability 1 — Project registration and honest shape visibility`, with the non-authority banner, `Reviewer:`, `Reviewer model family:`, `Materials given:`, `Operationalization notes:` and `Reviewer's falsification notes:` **deleted outright** and no completeness-critic content. Appendix, verbatim:

```
## Appendix — §5's template, quoted for reference only

The instrument's §5 declares these record fields; this appendix quotes them
so a reader can compare. Nothing below is an answer.

> > This administration record is evidence, never an owner act; its verdict
> > authorizes nothing (instrument preamble; VIS-4).

- Reviewer: <model/version or human, fresh context: yes/no>
- Reviewer model family: <alternate families across administrations>
- Materials given: <list, with deviations called out>
- Operationalization notes: <every judgment call made>
- Reviewer's falsification notes: <what they tried to break and couldn't>

## G1 — completeness critic
```

The administrator's own output, verbatim:

```
rows parsed: 39 (Met 38, Not met 0, scoped 0, Unknown 1) — …
trend row:
| 2026-08-10 | 7751f12e | 0 | 0 | 1 | 0 | 0 | n/a — no prior record supplied | READY FOR Capability 1 — Project registration and honest shape visibility |
record valid — verdict semantics remain the instrument's, not this tool's
```

`[Observed]` The list carrier alone, without the banner limb, takes the composite from seven errors to **two** (G1-deleted) or **one** (G1 kept) — the six `Label:` checks are all no-ops. So the answer to the commission's question *"does any full exploit ride the disclosed limit?"* is **yes**: the limit was disclosed with a true statement about the *blockquote* composite (D-3 says so, correctly and narrowly) and then generalized in §9 to *"such a record"*, where it is false.

Instrument §4 (defined clause, quoted): *"G1 yields no verdict and never blocks, but an administration missing G1 is incomplete and cannot support a gate decision."* §2 requires the fresh-context disclosure; §5 declares all eight fields; RD24-02 put the banner there so a record cannot read as an owner act. The validator prints `record valid`.

`[Inferred]` The root cause is the one RD-39 named and this batch half-applied. The value checks own the distinction because `_decl` anchors to `^` with **no decoration allowance at all**; the presence checks were given the anchor *and* a decoration allowance in the same expression, and the decoration allowance is what a quotation uses. Presence and lawful-decoration are two requirements that were merged into one regex.

*Requires:* a **validator change** — separate the two: keep the whitespace normalization and bold allowance, drop the list marker from the presence anchor (or require the field's *value* to be non-placeholder, which is the honest form of the check), and give the banner a test that a nested blockquote fails. **An instrument amendment**: the §9 parenthetical is false of the bytes the digest would bind. **Offer-blocking, and it blocks the formal administration.**

### RD40-03 — MAJOR — a **tab**-indented fence deletes content a reader sees: the honest `Deferred count: 3` vanishes and the decoy `0` stands, `0 errors`, plain `READY FOR <the verbatim target>`. "CommonMark's own bound" is a column bound, not a space count

`[Observed]` `_active_text` computes `indent = len(ln) - len(ln.lstrip())` (371, 391) and requires `indent <= 3`. A tab is one character, so `\t```` opens a fence. CommonMark expands tabs to the next 4-column stop, so a tab-indented fence marker is literal content of an indented code block — visible to every reader, and RD39-06's *sharper carrier* exactly, one whitespace character out. Executed at `7751f12`, git on, real digests:

| record | v1.12 |
|---|---|
| honest `Deferred count: 3` between **tab**-indented backticks, decoy `Deferred count: 0` at column 0, terminal `READY FOR <verbatim target>` | **0 errors, `record valid`, trend verdict `READY FOR Capability 1 — Project registration and honest shape visibility`, Deferred column `0`** |
| the identical record with **four-space** backticks (the control) | 3 errors — LG-5 disagreeing values (`'0'; '3'`), LG-7 uncited deferral, LG-6 "a deferral-carrying pass is READY-WITH-DEFERRALS, never plain READY FOR" |

So one keystroke's difference decides whether §4's deferral conjunct runs at all. The same carrier can delete a roster row (loud), the `E3 reopen-list:` field (loud), or — as here — the honest half of a disagreeing pair (**silent**).

The delta's D-4 and §9 both say the marker *"counts only at ≤3 spaces of indentation (CommonMark's own bound)"*. CommonMark's bound is *three columns of indentation*, and it defines tab expansion explicitly for exactly this reason.

*Requires:* a **validator change** — expand tabs to 4-column stops before measuring indentation, in both the opening and closing tests (and, for consistency, in `_label_present`'s `^ {0,3}`, where a tab currently refuses — the safe direction, but by accident) — plus a fixture in both directions. A **record correction** to D-4's and §9's "CommonMark's own bound" phrasing. **Not offer-blocking on its own; it blocks the formal administration.**

### RD40-04 — MAJOR — the `GOOD` template's `Instrument version:` literal was not bumped at v1.12, so the LG-11 version-disagreement fixture asserts a substring its **unmutated** baseline already emits: a check that cannot fail

`[Observed]` `GOOD` (1004) reads, quoted: `Instrument version: v1.11  sha256: {inst}` — at v1.12. The selftest's git-dependent fixture (1460–1463) is:

```python
case("instrument version disagreement rejected (RD33-06, LG-11)",
     good_head.replace("Instrument version: v1.11",
                       "Instrument version: v1.2"),
     "LG-11: record claims instrument version", _git=True)
```

Executed against the clone at HEAD: `good_head` **unmutated** already produces `LG-11: record claims instrument version v1.11 but the committed instrument at the named commit declares v1.12 …`. The assertion is satisfied by the baseline; the mutation the fixture exists to catch is no longer what makes it pass. I confirmed the substring is present in the unmutated error set (`True`).

This is the validator's own lesson, unapplied to one of its two builders. The comment at 1500–1501 states it, quoted: *"Version-agnostic substitution (the RD34-05 lesson): the template's version literal must never strand this builder across a bump, so it is matched by shape, not by value."* That guard is applied to `good_real` and not to `good_head`. At v1.11 the fixture still discriminated (template and instrument agreed at v1.11); this is a **v1.12 regression in the fixture suite**, and it silently weakens the "132 fixtures" figure P-34's recommendation rests on.

*Requires:* a **validator change** — bump the literal (or, better, apply the shape substitution to `good_head` too) and assert the *specific* claimed version in the message. **No instrument amendment; not offer-blocking**, but it is a second instance of the selftest's own closing line — *"a check that cannot fail is not a check"* — turned against the suite, one batch after RD39-03.

### RD40-05 — MAJOR — the three-axis directionality statement, written to correct RD39-04, is incomplete in the same way: D-4's change is filed reject-only while the fixture the batch shipped for it asserts an acceptance

The delta's "What did not change" (quoted): *"**Newly rejected:** … the four-backtick short-close exploit (D-4)"*. Its *Newly accepted* list does not mention D-4.

`[Observed]` The fixture the batch shipped for D-4 (1874–1877) expects **no errors**:

```python
case("four-backtick fence not closed by three — quoted duplicate "
     "row stays stripped (RD39-06)",
     good + "\n````\n```\n| A1 | Not met | x |\n````\n",
     None)
```

Measured on those exact bytes: **v1.11 → 1 error (`LG-3: question A1 appears twice`), v1.12 → 0 errors.** That is a newly-*accepted* record, and it is the only fixture D-4 has. The rejection direction exists too (I built it: a `Materials given:` label between ```` and ``` is active at v1.11 and stripped at v1.12 → 0 errors → 1 error), but it is **unfixtured**. So the axis assignment is exactly inverted relative to the shipped evidence.

`[Observed]` Two further unlisted behavior changes, found by running a 27-case corpus through both validators: a record whose roster rows are swallowed by an unterminated HTML comment goes **0 errors → 8 errors**; a record whose terminal verdict is swallowed by an HTML comment goes **0 errors and a silent `NOT READY`** → **1 error and `—`**. Both are correct and welcome; neither is named on any axis. And `Ma<!--x-->terials given:` goes 1 error → 0, an acceptance created by comment-splicing that no axis names.

*Requires:* a **record correction** — assign D-4 to both directions and fixture the rejection limb; enumerate the HTML-comment consequences. **No instrument amendment; not offer-blocking on its own.** But it is the second consecutive batch whose directionality statement is falsified by measurement, and the second where the failure is *the form of the claim reused without its method*.

### RD40-06 — MINOR — an inline HTML comment on the terminal verdict line is a false rejection, and the error message asserts three things that are all untrue of it

`[Observed]` `_active_text` rewrites `GATE VERDICT: NOT READY <!-- final -->` to `GATE VERDICT: NOT READY `, so `_gv_lines[-1] != _gv_raw[-1]` and the record errors. Measured, 1 error, message quoted: *"the record's terminal `GATE VERDICT:` line — `'<!-- a -->GATE VERDICT: NOT READY'` — is not the record's active terminal line: it sits inside a fenced or comment-carried block, after an unterminated fence, or a quoted verdict line follows the record's own."* None of the three is true: the verdict is visible, terminal, and its own. The batch fixtured *"lawful record with an inline HTML comment still validates"* — on the `Operationalization notes:` line only. Same class as RD39-07 (over-rejection with a message wrong about the record), on the one line §5 makes decisive.

*Requires:* a **validator change** — compare the raw and active terminal lines after the same comment normalization, or compare *positions* rather than strings. **No instrument amendment; not offer-blocking.**

### RD40-07 — MINOR — `_row_verdicts` is dead code whose docstring still claims to be the rule that governs the prior side

`[Observed]` `_row_verdicts` is defined at 177 and called **nowhere** in the v1.12 bytes (grep, denominator: the whole file). At v1.11 it was called at 827; D-5's recursive `validate()` replaced it. Its docstring still reads, quoted: *"Parse verdict rows with one normalization for record and prior alike (RD33-02: the prior side previously used startswith over the scoped form while the current side matched exactly — asymmetric)."* A reader auditing RD33-02's repair will find a function that no longer runs. The behavior is unaffected (`validate()`'s own row loop applies the same `ROW_RE` and the same scoped comparison, and I confirmed the RD33-02 and RD34-04 trend fixtures still pass).

*Requires:* a **validator change** — delete it, or re-point RD33-02's claim at the live loop. **Not offer-blocking.**

### RD40-08 — MINOR — D-5's mutation denominator of 3 counts two fixtures that fail on a finding-ID substring, not on behavior

`[Observed]` Reverting the prior guard to the **exact v1.11 bytes** fails 3 fixtures, as claimed. Adding `RD39-05` to the v1.11 guard's error message and changing nothing else (M5c) leaves **1 of 3** failing. The two RD38-06 fixtures assert `any("RD39-05" in e for e in _e)`; the v1.11 guard refuses those priors correctly and only its message differs. They are regression guards, which is legitimate — but they are counted in a denominator the delta and §9 present as *"each failing exactly the fixtures its repair added."* For D-5 the behavioral count is 1.

*Requires:* a **record correction** to the D-5 denominator. **Not offer-blocking.** Recorded because RD39-03 was exactly this question asked one level less carefully.

### Nits, no action requested

- *"six amendments byte-unchanged"* (P-34, PENDING, PROJECT-STATUS): measured as **six versions / five amendments**; the convention is inherited from RD-38/RD-39 and the substance is exact.
- `_label_present` accepts `**Label:*` (asymmetric bold) and refuses `_Label:_` (italic) — an inconsistency in the decoration allowance, both in the safe direction relative to lawful records.
- The trend row is printed **above** the error list, so an invalid record still emits a nine-column row; in one construction it carried `READY FOR OPENSPEC AUTHORING`, a string §8 never bound, three lines above the LG-11 error rejecting it. Pre-existing; worth a `—` when errors exist.

---

## 6. What passes

`[Observed]` These are executions and sweeps run this session, not inferences:

- **All seven RD-39 findings are present in the v1.12 bytes; none is absent.** Three closed outright, three closed for every carrier and rule the finding named, one closed in form. Every one verified by rebuilding RD-39's own records and running the clone's validator with git checks ON against the real commit `7751f12` and the real committed instrument and §8 digests.
- **RD39-01's named repair works exactly as described.** RD-39's laundered record → 1 loud error, trend verdict column `—`; the four-space-indented-carrier record → 0 errors, trend verdict `NOT READY`; the fenced and comment quoted-after-terminal records → 1 error each; RD35-02's fixtured control unchanged. `132 fixtures, 0 failing` on the unmutated clone.
- **RD39-02's named repair works exactly as described.** The composite scores **7 / 7 / 6 / 7 / 7** errors in the fenced / comment / blockquote / indented / prose carriers — the delta's own numbers, reproduced — and the comment-carried G1 heading no longer satisfies LG-4. The RD39-07 lawful forms all accept.
- **RD39-03 is closed and rule-6 satisfied against the code it replaced.** Reverting `_decl`'s return to the exact v1.10 bytes fails **exactly one** fixture at v1.12 and **zero of 116** at v1.11 — I ran both. v1.10:347 quoted from git.
- **RD39-05 is closed by construction, and by RD-39's own construction.** Lawful **v1.11-era** and **v1.10-era** priors, each naming its own commit, version and digests, validate as priors at **0 errors** with git on; the bare block (19 errors), the all-`Not met` fabrication (18 errors), a bad-commit prior and an unlawful-terminal prior are each refused with the column reading `n/a — prior record failed validation`. Recursion is depth 1, the prior's errors fold as one summary line, and a 20 000-line prior costs 0.12 s.
- **RD39-06's space limb is closed** and its correct behaviors preserved: 3-space open / 4-space close leaves the fence open; ```` closed by ``` does not close; nested different-length fences behave; `~~~`/``` do not cross-close; tilde fences, info strings, mid-line backticks and blockquoted fences all correct.
- **All seven mutation-reverts reproduce at their claimed denominators** — 2, 2, 1, 1, 5, 3, 1 — built by patching the v1.12 bytes and, for the prior guard, by lifting the **exact v1.11 block** from `git show c70e756:`. Eleven mutated copies in all, every one run outside the clone with `REPO` patched so the git-on fixtures still executed.
- **Every check is fixtured.** Denominator **13**; LG-1…LG-13 each fire, computed mechanically by intercepting `validate()`; **269** emissions; `validate()` invocations **138** = 132 fixtures + 6 recursive prior validations, the recursion's arithmetic visible and correct.
- **The fixture arithmetic reconciles exactly**: 116 + 16 = 132, itemized as the delta itemizes it, and the printed line reads `132 fixtures, 0 failing`.
- **§1–§8 are byte-identical, per-section, for the fifth amendment / sixth version running.** Denominator 10 sections; 8 identical; only `HEADER` and §9 move; **110** diff lines; the §9 changes are exactly the four declared (version header, three dated markers, the appended entry) — read line by line off the diff. **§8's digest and 6610-byte length are identical at all 8 versions that have carried it, across 10 commits** — computed, never transcribed.
- **D-1's four corrections of the frozen v1.11 delta are each true of the v1.10/v1.11 bytes**, re-measured by me rather than assumed, and the frozen record is untouched. The three that sit in §9 carry dated correction markers in place.
- **No frozen record was edited.** Denominator **30** files — 28 byte-identical to `c70e756`, 0 changed, 2 added — and the delta names the frozen population explicitly, closing RD-38's and RD-39's carried-forward phrasing nit.
- **The trend row is nine columns in every case I constructed**, including under a refused prior, no prior, a laundered verdict, an ambiguity error and all three exploits.
- **P-34 is coherent at v1.12** — question, dated offer-status naming **RD-40**, option (a)'s nine-delta list with all six correction pointers ahead of the claims they correct, option (b)'s v1.13 ordering, the **132**-fixture recommendation, the v1.12 approval block. `PENDING-OWNER-DECISIONS.md:188` and `PROJECT-STATUS.md:128–182` agree, and the disposition register records all seven RD-39 dispositions as `R` with accurate landing descriptions (one row excepted — RD40-01).
- **No routed artifact names a stale instrument version.** Denominator **364** files; **100** hits across **29** files, all read and classified; 93 non-v1.12 lines each accounted for.
- **The E1 rollup, the §4 conjunct battery both branches, the citation families, the `_Field` zero-truthiness case (`Deferred count: 0`), the scoped-row note, `param_block_bytes` at the new commit, `GATE_VERDICT_RE`'s bold-wrapped form, CRLF line endings, unicode confusables and fullwidth colons in labels, and the `--prior` recursion bound all survived every attack I made** — confusables and fullwidth colons reject loudly, NBSP accepts, and none of them opens a path to a false pass.
- **`check_governance.py` in the clone: 30 OK, 18 WARN, 0 FAIL (48 checks); `--selftest`: 121 fixtures, 0 failing.**
- **The clone stayed clean.** `git status --porcelain` and `git diff HEAD` empty at open and close; HEAD `7751f12e…`; instrument `4ad21f80…` and validator `47164 8ca…` unchanged at close, each confirmed by two independent methods; **zero `.pyc` files anywhere under the clone**.

---

## 7. Overall assessment — may v1.12 be offered to the owner at P-34, and may the formal administration run on this validator?

This is the most disciplined batch of the eight. It did the thing RD-39 asked for that no predecessor had done: it went looking for the rules its own repair newly stood upstream of, and it found one — the comment strip's interaction with the raw terminal rule is handled, correctly and loudly, in a case nobody asked it to handle. Its records are the most honest of the chain: D-1 corrects four claims of the frozen predecessor and names each one; §9 carries three dated markers instead of quiet edits; the frozen population is enumerated rather than gestured at; the disclosed limits are stated in the delta *and* in the instrument; the fixture arithmetic reconciles to the printed count; all seven mutation-reverts reproduce at exactly the denominators claimed, including the one the v1.11 batch could not produce at all. §1–§8 have not moved in five amendments and §8 in eight versions, and I found nothing in the normative question text — the sixth administration running to look and find nothing there.

And the class survived, in the same shape, a fourth time. RD-39's diagnosis was *direction*: specify the repair over the **property**, then check **every carrier**. The batch adopted the sentence and applied it to the carriers RD-39 had enumerated. "The record's own last verdict line" was implemented as *raw text equals stripped text* — which distinguishes the two carriers the strip removes and no others, so a verdict line quoted in a blockquote, an indented code block, a list item, or a sentence of prose is still the record's own last verdict line, and a record whose own `GATE VERDICT:` reads `NOT READY` still prints `record valid` under `READY FOR Capability 1 — Project registration and honest shape visibility`. "The record's own structure, not a quotation of it" was implemented as *a line anchor plus a decoration allowance* — and the decoration allowance is what a quotation uses, so RD-38's composite, with its banner and six declared fields and completeness critic all deleted, validates at **0 errors** when the template rides a bullet list. And the fence grammar was aligned to CommonMark for spaces and not for tabs, so one tab still deletes a line a reader sees and turns a `Deferred count: 3` into a plain `READY FOR <the verbatim target>`.

Each of those is one carrier out from where the last reviewer pointed. That is now the finding, and it is no longer about any individual repair. Four consecutive batches have shipped a repair specified over *the instances the previous review constructed*, and four consecutive reviews have broken it with the next instance. The v1.12 batch had the right sentence and still enumerated carriers by hand. What is missing is a **closed enumeration of markdown's quotation carriers, written once, and applied by one shared predicate to every rule that asks "is this line the record's own?"** — the terminal verdict, the six presence tokens, the banner, the G1 anchor and `_decl` are five consumers of one question, and they answer it five different ways today.

So, on the two questions asked:

- **May v1.12 be offered at P-34?** **No.** The mechanism, ordering, options, precondition, nine-delta list and six correction pointers are all right; D-1's four corrections are each true of the v1.10/v1.11 bytes and the frozen record is untouched; the fixture arithmetic reconciles to the printed count; all seven mutation denominators reproduce; the version sweep is clean; nothing in §1–§8 moved. But **two sentences inside §9 — the bytes an approval digest binds — are false of those same bytes**: that *"a verdict quoted after the record's own terminal verdict is ambiguous, never silently resolved"* (four carriers resolve it silently, at 0 errors, into `READY FOR <the verbatim target>`), and that under the disclosed nested-blockquote banner limit *"the other six fields and LG-4 still reject such a record"* (a bullet-list quotation of the six, with a column-0 `## G1`, gives 0 errors). On the RD38-02 / RD39-02 precedent this batch itself invokes, **the digest v1.12 would bind is not the digest that should be approved**. Beneath them, the directionality statement written to correct RD39-04 mis-assigns its own shipped fixture, and one fixture in the 132 P-34's recommendation cites can no longer fail.
- **May the formal administration run on this validator?** **No.** Three independent constructions produce a clean `record valid` and a nine-column trend row reading `READY FOR Capability 1 — Project registration and honest shape visibility`: a record whose own terminal verdict is `NOT READY`; a record with no non-authority banner, no fresh-context disclosure, no model-family disclosure, no materials list, no operationalization notes, no falsification notes and no completeness critic; and a record whose visible `Deferred count:` is 3 with no owner citation. Any one of them, at Administration 1, becomes the baseline every later F1 verdict is read against.

Two things to say plainly. First, the enumerable work is very nearly done: seven of seven RD-39 findings are present, every mutation denominator holds, every check is fixtured, the records are honest about their limits, and the three new blocking-or-major defects are one shared predicate plus a tab-expansion plus a fixture matrix — smaller than any repair set in this chain. Second, and this is what I would ask the v1.13 batch to sit with: **stop enumerating carriers and enumerate the question.** Write down, once, what makes a line the record's own — not a quotation of it — as a single predicate with its own fixture matrix over *every* markdown container (fence, HTML comment, blockquote at any nesting, indented code block by spaces **and** tabs, list item at any marker and depth, setext and ATX headings, table cells, raw-HTML blocks, running prose), and then make the terminal-verdict rule, the six presence tokens, the banner test, the G1 anchor and `_decl` all call it. Every one of the last four blocking findings — RD38-01, RD39-01, RD39-02, RD40-01, RD40-02 — is the same question answered inconsistently by consumers that never shared an answer. I decline, like RD-35 through RD-39, to predict that the v1.13 batch is the last; but this is the first time the remaining work can be stated as one artifact rather than as a list of repairs.

VERDICT: REVISE