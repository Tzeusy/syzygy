All measurements complete. Writing the review of record.

---

# RD-41 — Launch-gate instrument re-review, v1.13 exact bytes (round-2026-08e, frozen commit `619093b`)

- **Review id:** RD-41 (ninth administration of the instrument re-review chain: RD-33 → v1.6 … RD-40 → v1.12)
- **Date:** 2026-08-11
- **Reviewer:** isolated fresh-context session, Claude family. Same-family re-review — F5's own example applies to me. I authored no byte under review.
- **Clone:** `…/scratchpad/clone-08e-r21`, HEAD `619093b788f791cbcfa2d0bff108fb7ace75da24`. `git status --porcelain` **empty at open and at close** (0 lines), **zero `.pyc`/`__pycache__` anywhere under the clone** (`find … | wc -l` → 0). Every mutated validator copy, synthetic record and instrumented harness lives in `…/scratchpad/rd41/`. Nothing under `/home/tze/GitHub/syzygy` was read, written, or executed.

## Materials read in full, and digests verified

Verified by **two independent methods** (`sha256sum` and Python `hashlib`), both at open and at close:

| artifact | sha256 | matches charter |
|---|---|---|
| `launch-gate-pre-specifications.md` | `025d07c44fad4199c3762c6e6bb3f4061e74c9945d019bacab2113c0972d5162` | ✔ |
| `scripts/launch_gate_results.py` (2193 lines) | `e0a0653e69c75af6f09e2677754c0168692d96e0072f625524aaec78106f5a78` | ✔ |
| `round-2026-08e/LAUNCH-GATE-v1.13-SEMANTIC-DELTA.md` | `27106e9390092b9dca611e4298bc73f921daf10d2ffccb0160ec03208a116374` | ✔ |

Also read in full: `reviews/RD-40-instrument-v112-RAW.md` (294 lines, 8 findings, `VERDICT: REVISE`); the RD-39 and RD-40 sections of `reviews/DISPOSITION-REGISTER.md` including the "As built (2026-08-11, v1.13)" note; `decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` (P-34); the launch-gate rows of `PROJECT-STATUS.md` and `PENDING-OWNER-DECISIONS.md`; the v1.12→v1.13 instrument diff line by line; and the v1.12 validator reconstructed from `git show 7751f12:scripts/launch_gate_results.py` (sha256 `471648ca71d88d30b223f9fdf542c75073fb5bf332f854905c91830f77d25ace`, 1976 lines — matching RD-40's measurement).

## 1. Method — what I ran

`[Observed]` `python3 scripts/launch_gate_results.py --selftest` **in the clone** → `145 fixtures, 0 failing`, exit 0, exactly **145 `pass` lines**, **0 `FAIL` lines**, **0 skip notes**. Counts read from the tool's own printed output.

`[Observed]` A record generator matching §5's template field-for-field (39 roster rows, all eight declared fields, blockquoted banner, G1 section), invoking the clone's validator with `REPO` bound to the clone, so LG-1/LG-2/LG-11 and both citation-existence paths executed **git-on against the real commit `619093b`, the real committed instrument digest `025d07c4…`, the real §8 digest `01209c0f…` and the real `effective_version: v1.13`** on every case below. ≈95 synthetic records.

`[Observed]` **Mutation-revert testing (rule 6):** 16 mutated copies outside the clone, each `REPO`-patched so git-on fixtures still ran; each run's *output* read, never its exit code.

`[Observed]` **Cross-version execution:** the v1.12 validator rebuilt from git and the *same* record bytes run through both, for every directionality claim.

`[Observed]` Fixture→check coverage computed mechanically by intercepting `validate()`. Denominator **13**.

`[Observed]` Repo-wide sweeps with Python `re`, never shell grep (rule 1). Denominator **373** text files.

`[Observed]` `python3 scripts/check_governance.py` in the clone → **30 OK, 18 WARN, 0 FAIL (48 checks)**; `--selftest` → **121 fixtures, 0 failing**.

`[Unknown]` I did not administer the gate and read no pilot record content. All answer sets are synthetic.

## 2. Per-finding verification — all eight RD-40 findings

| RD-40 | Class | Disp. | Status | Evidence in the v1.13 bytes |
|---|---|---|---|---|
| **RD40-01** | BLOCKING | R | **verified-closed by execution and mutation** | `_gv_own` (784–787) selects raw lines that are own-shaped *and* token-leading; `_later` (803) errors on **any** later token-carrying raw line regardless of carrier. Re-executed at `619093b`, git on, real digests: RD-40's four carriers (blockquote / 4-space indent / list item / prose) score **1 error each, trend verdict column `—`**; the fenced and comment carriers 1 each; the all-quoted record refused **by name**; the lawful `NOT READY` control **0 errors, `NOT READY`**. I rebuilt RD-40's own v1.12-era records at `7751f12` with the v1.12 digests and ran both validators: **v1.12 → 0 errors and `READY FOR Capability 1 — Project registration and honest shape visibility` in all four; v1.13 → 1 error, `—` in all four.** D-1 item 1's correction is true of the v1.12 bytes. **Mutations:** reverting the ambiguity test → **4 failing** (exactly the four carrier fixtures); dropping the predicate from the terminal rule → **5** (those four + the all-quoted). A separate laundering vector survives, but it is not RD40-01's — see RD41-08. |
| **RD40-02** | BLOCKING | R | **closed for every container the finding named; the class survives one carrier out — RD41-01** | `_own_flags` (408–459) is one function; four consumers read it (`_own_text` → `_label_present`, the LG-4 anchor, the banner `bq1` test, `_gv_own`). Measured v1.12 → v1.13 on identical bytes: bullet-list `Materials given:` **0→1**; setext-heading `Reviewer's falsification notes:` **0→1**; `<details>`-wrapped `Reviewer model family:` **0→1**; nested-blockquote banner **0→1**; `<details>`-wrapped `## G1` **0→1**. RD-40's full composite scores **6 errors** with the `## G1` heading and **7** without — the delta's and §9's numbers **reproduce exactly**. **Mutations:** `<details>` refusal → 2; setext → 1; nested banner → 1; combined list revert → 2, single-layer reverts 0/0 as disclosed. **But** the predicate is *line-local*: a list item's **continuation lines** carry no marker and sit at ≤3 columns, so they are "own". RD-38's composite reproduces **whole** — RD41-01. |
| **RD40-03** | MAJOR | R | **verified-closed** | `ln.expandtabs(4)` precedes the fence-open, fence-close and predicate indent measurements (374–375, 393–394, 437–439). Re-executed, both decoy orderings, git on: tab-indented and four-space records score **identically** — 3 / 3 with the decoy first (`Deferred count` read as **3**), 1 / 1 with the honest value first. At v1.12 the tab record scored 0 where its control scored 3. **Mutation:** reverting `_active_lines`' expandtabs → **1 failing** (the tab fixture). *Residual:* the predicate's own tab limb has **no witness** — RD41-10. |
| **RD40-04** | MAJOR | R | **verified-closed for its instance; the class survives elsewhere — RD41-11** | `good_head` is rewritten by shape to the committed `effective_version` (1572–1580) and the fixture mutates by shape to `v0.2`, asserting the *specific* claimed version (`"LG-11: record claims instrument version v0.2"`). **Mutation:** disabling the LG-11 version comparison → **1 failing**, that fixture. The unmutated baseline no longer emits the asserted substring. I swept the class over all **139** `case()` fixtures — one inert mutation remains (RD41-11). |
| **RD40-05** | MAJOR | **R — partly** | **rejection limb fixtured; the directionality restatement mis-assigns again (RD41-05) and one committed limb was not built (RD41-09)** | The rejection-limb fixture exists (2165–2171). **Mutation:** removing the closing-run length requirement → **2 failing**, one per limb — the delta's claim reproduces. **But** that fixture's subject scores **1 error at v1.12 and 1 at v1.13** — it is newly *fixtured*, not *newly rejected*, and the delta lists it under *Newly rejected*. And the HTML-comment consequences the register says are "enumerated on the axes" appear nowhere. |
| **RD40-06** | MINOR | R | **verified-closed** | Survival is judged by raw index (`_t not in _kept_idx`, 813). `GATE VERDICT: NOT READY <!-- final -->` → **0 errors, `NOT READY`** (v1.12: 1 error with a message untrue of the record). **Mutation:** judging survival by string identity → **1 failing**. *But the message it complained of is now emitted falsely in new circumstances* — RD41-06. |
| **RD40-07** | MINOR | R | **verified-closed** | `def _row_verdicts` is **absent** from the v1.13 bytes (Python substring search over the whole file). The single remaining occurrence of the name is the comment at 622–623, which now sits at the live row loop and names RD33-02 there. |
| **RD40-08** | MINOR | R | **verified-closed** | D-1 item 5 restates D-5's denominator as "1 behavioral witness + 2 ID-string regression guards". Record correction only, as disposed. |

**Tally, with its denominator:** of RD-40's **8** findings, **8 are present in the v1.13 bytes and none is absent**; **6 are closed outright** (RD40-01, -03, -04, -06, -07, -08); **1 is closed for every container the finding named, with the class surviving one carrier out** (RD40-02 → RD41-01); **1 is closed in part** (RD40-05 → RD41-05, RD41-09). **All ten claimed mutation-reverts reproduce at exactly the claimed denominators** (§3).

## 3. Honesty audit of the batch's own measurements

`[Observed]` **Fixture count and arithmetic.** Printed output reads `145 fixtures, 0 failing`; my instrumented run counted **145 `pass` lines, 0 `FAIL`**. 132 + 13 = **145**, itemized exactly as the delta itemizes (+4 carriers, +1 all-quoted, +1 inline comment, +1 tab, +5 container matrix, +1 fence-close rejection), with the RD39-07 acceptance fixture **flipped in place** (2067–2072), its reversal named in its own label. ✔ **Honest.**

`[Observed]` **The ten mutation-reverts.** The delta names *none* of the ten, so I constructed a set from the repairs and measured. The multiset reproduces **exactly**:

| revert | failing | fixtures |
|---|---|---|
| ambiguity test removed | **4** | the four quoted-after-terminal carriers |
| predicate dropped from the terminal rule | **5** | those four + the all-quoted record |
| `<details>` depth tracking removed | **2** | `<details>` field + `<details>` G1 |
| fence closing-run length removed | **2** | both D-7 limbs |
| list refusal, **combined** revert to v1.12 | **2** | the flipped fixture + the bullet-list quotation |
| setext refusal removed | **1** | setext field |
| banner accepts nested `> >` | **1** | nested banner |
| fence-grammar tab expansion removed | **1** | tab fence |
| LG-11 version comparison removed | **1** | version disagreement |
| raw-index → string-identity survival | **1** | inline comment |
| *list refusal, predicate layer alone* | **0** | — |
| *list refusal, presence layer alone* | **0** | — |

Measured multiset `{4,5,2,2,2,1,1,1,1,1}` = claimed `{4,5,2,2,1,1,1,1,1,2}`. **Every revert fails exactly the fixtures its repair added.** ✔ **Honest — with one exception below.**

`[Observed]` **D-4's redundancy qualification is honest — and it is *not* the only such place.** The single-layer list reverts fail **0** each and the combined revert **2**: reproduced, and the batch's refusal to report two witnesses is correct. But three further single-layer reverts also fail **0** of 145, and **none is disclosed**:
- the predicate's **tab expansion** (`e = ln.expandtabs(4)`, 437) → **0 failing**. §9 says "sits at ≤3 columns of indentation with tabs expanded to 4-column stops" and D-5 says expandtabs "precedes every indent measurement … and the predicate's ≤3-column bound" — that third limb has **no behavioral witness at all** (no fixture uses a tab-indented label or heading).
- the predicate's **`indent <= 3` bound** (440) → **0 failing** (carried by `_label_present`'s `^ {0,3}` and LG-4's own `^ {0,3}`).
- `_label_present`'s **`^ {0,3}`** widened to `^ *` → **0 failing** (carried by the predicate).

So of the predicate's five stated clauses, **three** are redundantly carried with no single-layer witness, and the batch discloses **one**. → RD41-10.

`[Observed]` **The LG-4 disclosed residual.** The *measurement* is exact — RD-40's composite scores **6** errors with a column-0 `## G1` and **7** without; I reproduced 6/7 on rebuilt bytes. The *generalization* is false: see RD41-04.

`[Observed]` **§1–§8 byte-identity.** Per-section sha256 with a fence-aware splitter, `git show 7751f12:` vs `619093b`, **ten sections each side, denominator 10**: §1…§8 **all eight identical**; only `HEADER` (2914→2914 bytes, one line changed) and §9 (23408→29998) differ. The delta's per-section byte counts (794/4388/15377/5688/3601/2192/1038/6610) reproduce, each carrying its trailing newline. Instrument diff read line by line: one `effective_version:` line, two dated correction markers inside the §9 v1.12 entry, one appended v1.13 entry. **Zero question blocks changed; no ID renumbered; no verdict word changed.** ✔

`[Observed]` **Six amendments across seven versions (v1.7–v1.13).** Combined §1–§8 digest computed at **all 11** commits that have ever touched the instrument: identical at v1.7, v1.8, v1.9, v1.10, v1.11, v1.12, v1.13 — **seven versions, six version-to-version amendments**. P-34 and PROJECT-STATUS both say exactly that. RD-40's "loose noun" nit is **fixed**. ✔

`[Observed]` **§8 across nine versions (v1.5–v1.13).** Recomputed with the validator's own `param_block_bytes` at every instrument commit: **6610 bytes, `01209c0f052971f7…`, constant at v1.5…v1.13 — nine versions**; **three** distinct §8 digests exist in history; v1.4 (4067 bytes) and its predecessor (2084) differ. ✔ *One imprecision:* the delta says "**eleven** distinct `effective_version:` values are reachable in history" — there are **eleven commits** but **ten** distinct declared values (v1.4…v1.13); the eleventh commit declares no `effective_version:` at all. RD41-12.

`[Observed]` **No frozen record edited.** Denominator **30** files matching the frozen shapes under `round-2026-08e/` (ten deltas v1.4–v1.13 + twenty `reviews/RD-*-RAW.md`): **28 byte-identical** to their state at `7751f12`, **0 changed**, **2 new** (this delta and RD-40's raw review). ✔ Exactly as the delta states.

`[Observed]` **Every check fires, denominator computed.** LG-1 31, LG-2 11, LG-3 42, LG-4 11, LG-5 20, LG-6 22, LG-7 30, LG-8 3, LG-9 12, LG-10 9, LG-11 11, LG-12 63, LG-13 12 — **13 of 13, none absent**, 277 emissions. `validate()` invocations **151** = 145 fixtures + 6 recursive prior validations; the recursion's arithmetic is visible and correct. ✔

`[Observed]` **Checks that cannot fail — the class swept, not the instance.** Denominator: **139** `case()` fixtures captured by instrumenting `case`, each compared against the errors of all eight baseline records (`good`, `ready`, `scoped_c2`, `with_def`, `good_head`, `good_real`, `ready_real`, `with_def_real`) under its own `_git` setting. Twelve flagged; eleven survive inspection (either the fixture *is* a constructed baseline, e.g. `good_head` for LG-2, or the coarse assertion coincides while the fixture still discriminates against a revert of the predicate it targets — I checked each). **One is genuinely inert** — RD41-11.

`[Observed]` **The withdrawal of the v1.12 acceptance.** `- Operationalization notes:` scored 0 errors at v1.12 and 1 at v1.13. **I agree with the withdrawal**, and I would have asked for it: RD-40's diagnosis is right that presence and lawful-decoration were merged into one regex, and a leading `-` is the canonical markdown carrier of a quoted field list. Naming the reversal inside the fixture's own label so no reader mistakes it for a bug repair is the correct discipline. The cost is real but small — a lawful administrator who writes their fields as a bullet list gets a loud, specific error naming the field, not a silent pass. **But the delta's framing of it is false** — RD41-07.

`[Observed]` **P-34, PROJECT-STATUS, PENDING, register.** P-34 names **v1.13** at L11, L136 and in the approval block (L233), summarises RD-40's eight findings, names **RD-41** as the precondition, carries "**145 in all**, the **ten** mutation-reverts", and states "six amendments across seven versions (v1.7–v1.13)" and "nine versions v1.5–v1.13" for §8 — all four figures reproduce. PROJECT-STATUS agrees. The register's "As built" note carries 145 and the ten denominators correctly. **Stale-version sweep:** 373 text files; **110** lines carry both a launch-gate token and a `v1.x` token across **31** files; **8** name v1.13; all 102 others are delta filenames/titles, §9 back-references, frozen raw reviews, historical register rows, the v1.3 pilot, or P-34's own ten-delta list. **No routed artifact names a stale instrument version.** ✔

`[Observed]` **Four sentences inside §9 and the delta — the bytes an approval digest would bind, and the record that explains them — are false of those bytes.** RD41-01…RD41-04, RD41-07.

## 4. New findings

### RD41-01 — BLOCKING — RD-38's composite reproduces **whole**, a fifth time: banner, five declared fields and the G1 section deleted, the template quoted as a **list-item continuation**, `0 errors`, `record valid`, `READY FOR <the verbatim launch target>`

`[Observed]` `_own_flags` is **line-local**. It refuses the line that *carries* a list marker; it says nothing about the item's **continuation lines**, which carry no marker and sit at 2–3 columns — so they are `own`. That is the canonical markdown form of a quoted block inside a list.

Executed at `619093b`, git on, real digests, full 39-row roster, run through the clone's own CLI:

```
$ python3 scripts/launch_gate_results.py …/EXPLOIT-A.md
rows parsed: 39 (Met 38, Not met 0, scoped 0, Unknown 1) — …
trend row:
| 2026-08-11 | 619093b7 | 0 | 0 | 1 | 0 | 0 | n/a — no prior record supplied | READY FOR Capability 1 — Project registration and honest shape visibility |
record valid — verdict semantics remain the instrument's, not this tool's
$ echo $?
0
```

The record's body carries **none** of: the non-authority banner, `Reviewer:`, `Reviewer model family:`, `Materials given:`, `Operationalization notes:`, `Reviewer's falsification notes:`, or any completeness-critic content (each absence verified by substring search over the body). Its appendix reads, verbatim:

```
## Appendix — §5's template, quoted for reference only

The instrument's §5 declares a banner, eight fields and a G1 section; this
appendix quotes them so a reader can compare. Nothing below is an answer.

- The declared record fields, as §5 lists them:
  Reviewer: <model/version or human, fresh context: yes/no>
  Reviewer model family: <alternate families across administrations>
  Materials given: <list, with deviations called out>
  Operationalization notes: <every judgment call made>
  Reviewer's falsification notes: <what they tried to break and couldn't>

## G1

And §5's preamble banner, quoted:

> This administration record is evidence, never an owner act; its verdict
> authorizes nothing (instrument preamble; VIS-4).
```

`[Observed]` **Three carriers, each measured.** (a) list-item continuation lines — **0 errors**; (b) **blockquote lazy continuation** (`> Quoting §5:` then unmarked lines) — **0 errors**; (c) a `> ` banner quotation nested **inside** a list item (`- quoting:` / `  > This administration record is evidence…`) satisfies the banner test — **0 errors**. The control — the *bullet-list* carrier v1.13 names — correctly rejects at **4 errors**, and RD-40's full composite at **6**. So the repair closed exactly the containers RD-40 constructed and no others.

`[Observed]` **This falsifies the §9 v1.13 entry.** §9 (quoted from the diff): *"a line is the record's own when it carries no blockquote marker …, sits at **≤3 columns** of indentation …, **carries no list marker of any kind** (`-`, `*`, `+`, ordered), is not the text line of a setext heading, and is not inside a raw-HTML block"*. D-2's table says: *"list item `-` `*` `+` `1.` `1)`, **at any depth** | no | the canonical carrier of a quoted field list"*. A list item's content **at depth 1** is not refused. §4 of the instrument (defined clause): *"G1 yields no verdict and never blocks, but an administration missing G1 is incomplete and cannot support a gate decision."* §2 requires the fresh-context disclosure; RD24-02 put the banner there so a record cannot read as an owner act. The validator prints `record valid`.

`[Observed]` The same record validates **cleanly as a `--prior`** (0 errors, New-findings column `0`), so the forgery propagates into the column F1 is answered from.

`[Inferred]` The root cause is one level up from RD-40's diagnosis. RD-40 asked for the *question* to be enumerated; the batch enumerated the *containers*. A container is a **region**, not a line: `> `, `- `, `1. `, `    ` mark a region's *first* line, and every markdown container continues without its marker. A per-line classifier can never answer "is this line inside a quotation?" — it needs the block structure the marker opens. This is the same shape a fifth time, and it will keep being the same shape until the predicate carries state.

*Requires:* a **validator change** — the predicate must be computed over *block structure*, not per line: a list item or blockquote opened at column *c* claims every following line indented past *c* (and every lazy paragraph continuation) until a blank line ends the paragraph, exactly as CommonMark defines it — plus a fixture per carrier per consumer. **An instrument amendment**: §9's predicate definition and D-2's table are false of the bytes the approval digest would bind. **Offer-blocking, and it blocks the formal administration.**

### RD41-02 — BLOCKING — §9's `_decl` scope sentence is false of the bytes: a `<details>` block silently **supplies** the record's decisive declared values, including E3's reopen-list and the owner's deferral citation

Instrument §9, v1.13 entry (quoted from the diff): *"`_decl` is deliberately **not** a consumer: it is `^`-anchored with no decoration allowance at all, so **every quotation carrier either fails the anchor outright or produces a loud disagreement error** — a stated scope decision, not an omission."* D-2 says the same, adding *"never a silent substitution"*.

`[Observed]` False for two carriers the predicate's own table names. A `<details>`/`<summary>` block ("collapsed content a reader may never open" — D-2's own words) and setext-heading text both reach **column 0**, so `_decl` reads them; and where the record declares the field **nowhere else**, there is no disagreement to be loud about — the quotation silently *becomes* the declared value. Executed at `619093b`, git on, real digests, full roster:

| construction | errors | trend row |
|---|---|---|
| `E3 reopen-list: empty` present **only** inside `<details>` | **0** | `READY FOR Capability 1 — …` |
| `E3 reopen-list: empty` present **only** as setext-heading text | **0** | `READY FOR Capability 1 — …` |
| `Deferred count (…): 0` present **only** inside `<details>` | **0** | Deferred column `0` |
| `Deferred count: 3` visible, `Owner deferral decision: SDR-33` **only** inside `<details>` | **0** | `READY-WITH-DEFERRALS`, Deferred `3` |
| *control:* the same record with no citation anywhere | 2 | — |

`[Observed]` The sharpest form: a record that shows its reopen items to the reader as visible prose bullets and hides `E3 reopen-list: empty` inside a collapsed `<details>` validates at **0 errors under `READY FOR <the verbatim target>`**, while the honest control (`E3 reopen-list: (1) …`) scores 2 errors. §3's own words, which the validator quotes back at the administrator: *"the list is non-empty; 'ready' is then false regardless of every other verdict"* — the instrument's self-declared sharpest single gate, defeated by a `<details>` tag.

`[Observed]` The batch's scope decision is also **internally inconsistent**: `Unknowns and what would settle them:` inside `<details>` errors (it is one of the six predicate-consuming presence tokens), while `E3 reopen-list:` and `Deferred count:` inside `<details>` do not — the same question, "is this field really in the record?", answered two ways in one file. That is the exact defect RD-40 named, surviving inside the repair written to close it.

*Requires:* a **validator change** — `_decl` must consume the predicate for *presence* (a value found only on non-own lines is an absent field), keeping the loud-disagreement behaviour for shadowing. **An instrument amendment**: the §9 sentence quoted above is false of the bytes an approval digest would bind. **Offer-blocking, and it blocks the formal administration.**

### RD41-03 — BLOCKING — the §9 v1.13 entry states **"eight mutation-reverts"** where the delta, P-34, PROJECT-STATUS and the disposition register all state **ten**, and ten is what the bytes do

`[Observed]` Instrument §9, v1.13 entry, quoted from the diff: *"**145 fixtures**; **eight** mutation-reverts, each failing exactly the fixtures its repair added…"*. The v1.13 delta, twice: *"**ten** mutation-reverts"* and *"**Ten mutation-reverts**, each failing exactly the fixtures its repair added — denominators 4, 5, 2, 2, 1, 1, 1, 1, 1, 2"*. P-34: *"the **ten** mutation-reverts"*. PROJECT-STATUS: *"ten mutation-reverts"*. The register's As-built note: *"ten mutation-reverts at denominators 4, 5, 2, 2, 1, 1, 1, 1, 1, 2"*.

`[Observed]` I reproduced **ten** distinct reverts at exactly those ten denominators (§3), plus the two 0-failing single-layer reverts. **Ten is the measured figure; §9's "eight" is false of the bytes.** The word appears to be carried over from the v1.11 entry, which reads *"116 fixtures; **eight** mutation-reverts"* — the v1.12 entry correctly reads "seven".

This is verification rule 3's own case (*"a derived value quoted outside its owning artifact goes stale silently"*), and it sits in the one artifact whose bytes a digest would bind. On the RD38-02 / RD39-02 / RD40-01 / RD40-02 precedent this batch itself invokes twice in its own §9 markers, a false measurement inside §9 is offer-blocking however small.

*Requires:* an **instrument amendment** (correct the count to ten in the v1.13 entry). **Offer-blocking; does not block the administration.**

### RD41-04 — BLOCKING — the LG-4 disclosed residual's generalization *"it opens no pass"* is false: the residual is one of the three limbs of a 0-error, `READY FOR`-reporting composite

`[Observed]` §9, v1.13 entry: *"LG-4 is satisfied by a column-0 `## G1` heading wherever it sits and however empty the section beneath it … and **it opens no pass** (the composite scores 6 errors with the heading and 7 without)."* The delta and the register's As-built note repeat it.

The parenthetical **reproduces exactly** (6 / 7 on rebuilt bytes). The generalization does not. RD41-01's composite validates at **0 errors** with a bare `## G1` and nothing beneath it; deleting that heading takes it to **1 error** (`LG-4: no G1 section`). So the residual is not a cost-of-one-error inside an already-failing record — it is a load-bearing limb of a passing one. Measured both ways this session.

`[Observed]` The residual is also **wider than disclosed**. LG-4's anchor is `^ {0,3}#{1,6}\s*G1\b` over `_own_text`, and `\s*` crosses the newline. Measured: a bare `###` on one own line followed by *any* own line beginning `G1 …` satisfies LG-4 — **0 errors** — including when the two are separated in the record by lines the predicate drops. Control (`###` followed by `nothing here`) → 1 error. So LG-4 is satisfied without a G1 heading at all. This is RD37-03's class ("a heading that merely mentions G1") returning through a door nobody checked.

The commission asked whether this batch's disclosed limit repeats its two predecessors' pattern of a true narrow measurement generalized into a false sentence. **It does.**

*Requires:* a **validator change** (LG-4 must require the G1 heading to open a non-empty section, and its anchor must not cross a newline) and an **instrument amendment**: the §9 sentence is false of the bytes an approval digest would bind. **Offer-blocking; the LG-4 half also blocks the administration as one limb of RD41-01.**

### RD41-05 — MAJOR — the directionality statement, rewritten to correct RD40-05, mis-assigns again — and this time the delta promised it would not

`[Observed]` The delta's *Newly rejected* axis lists *"a label stranded between a four-backtick open and a three-backtick non-close (D-7, one fixture)"*, under the header *"each direction below is stated as its own fixture measures it"* and the explicit promise *"with D-1 item 4's misassignment not repeated"*.

Measured on the fixture's exact bytes, both validators: **v1.12 → 1 error, v1.13 → 1 error.** Nothing is newly rejected. The closing-run rule shipped at v1.12 (RD39-06); what is new is the *fixture*, which is precisely what D-7's own prose says (*"is now fixtured too"*). The axis assignment contradicts the delta item it summarises.

All the other axis entries **do** reproduce: the five D-4 rejections each move 0→1; the two *Newly accepted* entries each move 1→0; the withdrawn acceptance moves 0→1.

*Requires:* a **record correction** — move the D-7 fixture off the rejection axis (it is a newly-witnessed pre-existing rejection). **No instrument amendment; not offer-blocking on its own.** Recorded because it is the **third consecutive batch** whose directionality statement is falsified by measurement, and the second in which the correction reproduces the defect.

### RD41-06 — MAJOR — the raw-side predicate is applied to un-stripped text, so a `<details>` inside a *fenced example* or an *HTML comment* refuses the record with a message untrue of it — five undisclosed acceptance withdrawals

`[Observed]` `_own_flags` is called twice: once on `_act_only` (fence- and comment-stripped) and once on `_raw_lines` (**not** stripped). §9's own definition opens *"after the fence and HTML-comment strip"* — which is false of the raw-side call. Consequences, each measured v1.12 → v1.13 on identical bytes, git on:

| lawful-looking record | v1.12 | v1.13 |
|---|---|---|
| a fenced ```` ```html ```` example containing an unclosed `<details>` | 0 | **1** |
| a self-closing `<details/>` mentioned in prose | 0 | **1** |
| an HTML comment reading `<!-- see <details> below -->` | 0 | **1** |
| `---` on the line immediately after the terminal verdict | 0 | **1** |
| a `Materials given:` line immediately followed by `---` | 0 | **1** |

The first four all produce the same error, quoted: *"LG-6: every `GATE VERDICT:` line in the record is a quotation — blockquoted, list-marked, indented, fenced, or mid-line — and a quoted verdict is not the record's verdict"*. **None of the five listed causes is true of the record**: the verdict is at column 0, unmarked, visible, and terminal. This is RD40-06's class — an over-rejection whose message misdescribes its own cause, on the one line §5 makes decisive — reintroduced by the repair that closed RD40-06.

`[Observed]` This also **falsifies the delta's own cost accounting**: *"An acceptance withdrawn: `- Operationalization notes:` … **This is the only direction any consumer of the instrument loses**, it is intentional, and it is the one change in this batch a reviewer should weigh as a cost rather than a repair."* Measured: **five further acceptances are withdrawn**, none of them intentional, none disclosed. → RD41-07.

*Requires:* a **validator change** — the raw-side call must strip fences and comments for the purpose of `html_depth` and setext detection (or track `html_depth` only on the active side), and the LG-6 "all quoted" message must enumerate the cause it actually found. **Not offer-blocking on its own; it blocks the formal administration** — a fenced HTML example in an administration record is not exotic, and the failure mode is a refusal that tells the administrator something untrue.

### RD41-07 — MAJOR — the delta's *"the only direction any consumer of the instrument loses"* is false

Covered by RD41-06's table: five v1.12→v1.13 acceptance withdrawals beyond the disclosed one, four of them bugs. Recorded separately because it is a **sentence in the delta** that the reviewer is explicitly asked to weigh, and because it is the second time in this batch a true narrow measurement is generalized into a false claim (the first is RD41-04).

*Requires:* a **record correction**. **Not offer-blocking.**

### RD41-08 — MAJOR — a non-breaking space inside the `GATE VERDICT:` token makes the record's visible last verdict invisible to the validator, and an earlier own verdict is reported instead

`[Observed]` `_gv_all` selects raw lines by the literal substring `"GATE VERDICT:"`. A line reading `GATE\u00a0VERDICT: NOT READY` renders identically for a human reader and matches nothing. Executed at `619093b`, git on, real digests: a record whose visible **final** line reads `GATE VERDICT: NOT READY` (NBSP inside the token) with an earlier own `GATE VERDICT: READY FOR Capability 1 — …` scores **0 errors** and enters the trend log as `READY FOR Capability 1 — Project registration and honest shape visibility`. The control with an ordinary space correctly reports `NOT READY`.

`[Observed]` Confusables in the *colon* are safe (a fullwidth `：` yields a loud `LG-6: no GATE VERDICT line found`), and a zero-width space after the colon is loud too (`does not parse to the closed verdict set`). The NBSP is the one that is silent, and it is silent in the dangerous direction.

`[Inferred]` Pre-existing, not a v1.13 regression. Its severity comes from what the instrument is *for*: the whole chain exists because a record's bytes and a reader's eyes can disagree.

*Requires:* a **validator change** — normalize unicode whitespace (at minimum `\u00a0`, `\u2007`, `\u202f`, `\u2000`–`\u200a`) before the token search, with a fixture. **Not offer-blocking; it blocks the formal administration** — a laundered `NOT READY` at Administration 1 becomes the baseline every later F1 verdict is read against.

### RD41-09 — MINOR — the disposition register's RD40-05 row asserts work the batch did not do

`[Observed]` The register's RD40-05 row reads: *"the HTML-comment consequences RD-40 measured (unterminated-comment roster swallowing 0→8 errors; comment-hidden terminal 0→1; comment-spliced label acceptance) **are enumerated on the axes**."* Python substring search over the whole v1.13 delta and the whole instrument: `0→8` — absent; `comment-splic` — absent; `spliced` — absent; `unterminated comment` — absent; `HTML-comment consequen` — absent. **Zero of the three are enumerated anywhere.** The disposition RD40-05 was accepted as `R` on a description of a repair that was not built.

*Requires:* a **record correction** — either enumerate them or restate the disposition to what was actually built. **Not offer-blocking.**

### RD41-10 — MINOR — three of the predicate's five clauses have no single-layer witness, and only one is disclosed

Measured in §3. The predicate's tab expansion, the predicate's `indent <= 3` bound, and `_label_present`'s `^ {0,3}` each fail **0 of 145** when reverted alone. The batch discloses exactly one such redundancy (the list marker) and reports it honestly. The answer to the commission's question — *is that the only place in the batch where redundancy hides a missing witness?* — is **no**, measured, with the denominator stated.

*Requires:* a **validator change** — a fixture per predicate clause exercised through a consumer that has no second layer (a tab-indented label; a 4-column-indented `## G1`), or an honest disclosure that three clauses are unwitnessed. **Not offer-blocking.**

### RD41-11 — MINOR — one fixture's mutation is still inert: the RD40-04 class swept, one instance left

`[Observed]` `case("nonexistent commit rejected (git on)", good.replace(sha, "f"*40), "does not exist", _git=True)`. The template's placeholder sha is `"0"*40`, which does not exist either, so the **unmutated** `good` under git-on already emits `LG-1: named commit 0000000… does not exist`. The mutation changes nothing about whether the asserted substring appears. (The check itself is not dead — `good_head`/`good_real` exercise the accepting direction — but this fixture does not test what its name says.) Denominator: **139** `case()` fixtures swept; this is the only genuinely inert mutation remaining.

*Requires:* a **validator change** — build this fixture from `head`, so the unmutated baseline names a real commit. **Not offer-blocking.**

### RD41-12 — MINOR — "eleven distinct `effective_version:` values are reachable in history"

`[Observed]` Measured at all **11** commits that have touched the instrument: **ten** distinct declared values (v1.4 … v1.13); the eleventh commit (`e69c9239`) declares no `effective_version:` key at all. The surrounding claims — three distinct §8 digests, constant from v1.5 forward, v1.4 and its predecessor different — are all exact.

*Requires:* a **record correction**. **Not offer-blocking.**

### Nits, no action requested

- `**Label:*` (asymmetric bold) still satisfies presence — disclosed and carried forward; safe direction.
- The trend row is still printed above the error list carrying a claimed verdict for an invalid record — disclosed and carried forward.
- A record whose only verdict line is blockquoted was accepted at v1.12 with the correct verdict and is rejected at v1.13. Correctly filed under *Newly rejected*; noted only because it is a second acceptance the batch's "only direction lost" sentence overlooks.

## 5. Falsification notes — what I tried that did **not** break it

`[Observed]` Each of these is an execution at `619093b`, git checks **on**, against the real committed instrument and §8 digests:

- **CRLF** line endings throughout, both under `READY FOR` and under a terminal `NOT READY` — parsed correctly, 0 errors, correct verdict.
- **A 200 000-character single line** appended — 0 errors, no pathology, no timeout.
- **Nested containers:** `> - Materials given:` (list inside blockquote) refused; `| Materials given: x |` (table cell) refused; `    ## G1` and `> ## G1` both refused for LG-4; `10) Materials given:` refused; **tab-indented** `\tMaterials given:` refused.
- **Tabs elsewhere:** a tab in the blockquote marker (`>\tbanner`) still satisfies the banner correctly; a tab in a fence **info string** (```` ```\tpython ````) opens the fence correctly.
- **Unicode:** an RTL mark inside a label refuses loudly; a fullwidth colon in the verdict refuses loudly; a zero-width space after the colon refuses loudly. Only the NBSP in the token is silent (RD41-08).
- **The bold allowance:** `**GATE VERDICT: READY FOR …**` and the asymmetric `**GATE VERDICT: READY FOR …*` both parse; a 3-column-indented terminal verdict parses; a `|` in the captured verdict is rejected with the trend-row-corruption message.
- **`_decl` shadowing:** a disagreeing `Deferred count:` decoy at column 0 in an appendix fires the disagreement error loudly in both orders. The whole RD37-02/RD38-04 behavioral decoy loop (20 fixtures, both orders, every declared label) passes.
- **The §4 conjunct battery:** both pass branches, `F2 Not met` under plain READY, `Deferred count` nonzero under plain READY, all-`Not met` under READY-WITH-DEFERRALS, E-row and A–D conjuncts, scoped-row handling — every control behaves as §4 requires.
- **`--prior` recursion:** a lawful prior validates and drives New-findings; the bare block, the fabrication, the bad-commit prior and the unlawful-terminal prior are each refused with the column reading `n/a — prior record failed validation`; recursion is depth 1.
- **The terminal-verdict ambiguity rule itself.** I attacked this hardest and could not break it: `_later` is computed over *every* raw line containing the token, independent of the predicate, so no quotation carrier — however exotic — can be placed after the record's own verdict without a loud error. That is the right shape, and it is the one place in this file where the batch specified the rule over the property rather than over the containers. It is worth saying plainly: **RD40-01 is genuinely, structurally closed.**

## 6. Overall assessment

This batch did what RD-40 asked in *form*: there is one function, it has one docstring, and four consumers call it. Its records are the most careful of the chain on arithmetic — 145 reconciles to the printed count and to its own itemization, **all ten** mutation-reverts reproduce at exactly the denominators claimed, the D-4 redundancy is disclosed and refused as a second witness, the LG-4 residual's 6/7 measurement reproduces, §1–§8 have not moved in six amendments and §8 in nine versions, the frozen population is enumerated at 30/28/0/2 and holds, the version sweep is clean, all thirteen checks fire, and every one of RD-40's eight findings is present in the bytes with six of them closed outright. RD40-01, the harder of the two blockers, is closed *structurally* — the ambiguity test reads every raw token line and cannot be routed around. Nothing in the normative question text moved, the seventh administration running to look and find nothing there.

And the class survived a **fifth** time, in the same shape, for a reason worth naming precisely. RD-40 said "enumerate the question." The batch enumerated the **containers** — a table of nine rows, each a container, each checked against the line that opens it. But a container is a *region*, not a line. `- `, `> `, `1. `, four spaces: every one of them marks a block's first line, and every one of them continues without its marker. So a bullet whose *continuation lines* carry the quoted template satisfies all six presence tokens, a lazy blockquote continuation does the same, a `> ` nested inside a list item is the record's banner, and RD-38's composite — banner, five declared fields and the completeness critic all deleted, in an appendix that says in its own prose *"Nothing below is an answer"* — prints `record valid` under `READY FOR Capability 1 — Project registration and honest shape visibility`. Beside it, the field the instrument calls its sharpest single gate can be supplied from inside a collapsed `<details>` block that a reader may never open, and so can the owner's deferral citation; §9's sentence explaining why `_decl` is safe from exactly this is false of the bytes it would bind.

Underneath that sit three more §9-or-delta sentences that measurement contradicts: `eight` mutation-reverts where ten is the fact and every other record says ten; a disclosed LG-4 residual that "opens no pass" while forming a limb of a 0-error pass; and — for the third batch running — a directionality axis falsified by the fixture it cites. Two prior batches shipped a disclosed limit whose §9 generalization was false. This one shipped two.

The one thing I would put in front of the v1.14 batch is not another list of carriers. **The predicate must carry state.** "Is this line the record's own?" is not answerable from the line; it is answerable only from the block stack — which containers are open at this line, and at what column — which is exactly what CommonMark's block-structure phase computes and what `_active_lines` already does, correctly, for fences. Write that one loop: for each line, the list of open containers (blockquote at depth *n*, list item at column *c*, indented code, raw-HTML block, fence), maintained across lines, with lazy continuation handled; a line is the record's own iff that stack is empty. Then the predicate answers for continuation lines, for lazy lines, for nested carriers and for the ones nobody has constructed yet — and `_decl` can consume it too, which closes RD41-02 in the same stroke. That is a smaller artifact than the table it replaces, and it is the first repair in this chain that would be specified over something a reviewer cannot enumerate their way past.

On the two questions asked, in these words:

- **May v1.13 be offered to the owner at P-34?** **No.** The mechanism, ordering, options, precondition, ten-delta list and five correction pointers are all right; D-1's five corrections are each true of the v1.12 bytes and I re-measured them rather than assuming; the frozen record is untouched; the fixture arithmetic reconciles to the printed count; all ten mutation denominators reproduce; §1–§8 have not moved. But **four sentences inside §9 and the delta — the bytes an approval digest binds, and the record that explains them — are false of those bytes**: that *"every quotation carrier either fails the anchor outright or produces a loud disagreement error"* (a `<details>` block silently supplies `E3 reopen-list:`, `Deferred count:` and the owner's deferral citation, at 0 errors, under `READY FOR`); that the predicate refuses *"list marker of any kind … at any depth"* (a list item's continuation lines are the record's own, and RD-38's composite validates clean); that there were *"eight mutation-reverts"* (there are ten, and every other record in the batch says ten); and that the LG-4 residual *"opens no pass"* (it is a limb of one). On the RD38-02 / RD39-02 / RD40-01 / RD40-02 precedent this batch itself invokes in its own two dated markers, **the digest v1.13 would bind is not the digest that should be approved.**

- **May the formal launch administration run on this validator?** **No.** Four independent constructions produce a clean `record valid` and a nine-column trend row reading `READY FOR Capability 1 — Project registration and honest shape visibility`: a record with no non-authority banner, no fresh-context disclosure, no model-family disclosure, no materials list, no operationalization notes, no falsification notes and an empty completeness critic; a record whose decisive `E3 reopen-list:` lives only inside a collapsed HTML block while its reopen items are visible above it; a record whose owner deferral citation is invisible to the reader; and a record whose visible final line reads `GATE VERDICT: NOT READY`. Against them sit five lawful-looking records the validator now refuses with a message untrue of them — including any record carrying a fenced HTML example. Any one of these, at Administration 1, becomes the baseline every later F1 verdict is read against.

VERDICT: REVISE
