Clone verified clean and unchanged at the end. Writing the review.

# RD-34 — Launch-gate instrument re-review, v1.6 exact bytes (round-2026-08e, frozen commit 0bdd37d)

- Review id: RD-34
- Date: 2026-08-10
- Subject: `launch-gate-pre-specifications.md` (v1.6, repo root), `scripts/launch_gate_results.py`, `round-2026-08e/LAUNCH-GATE-v1.6-SEMANTIC-DELTA.md`, `decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` (P-34), `decisions/launch-gate/TREND-LOG.md`
- Subject sha256, recomputed by me this session with `sha256sum` and independently through the validator's own `git_show`/`sha256_bytes` path against `0bdd37d:launch-gate-pre-specifications.md`: `9d68fa3b8f588072b746a51243f66fa0c9de75c97c6ea945b08ea0cf44238544` — **verified, matches the dispatching session's measurement**
- §8 parameter block, extracted by the validator's own `param_block_bytes` (104 lines): `01209c0f052971f794e1f35827a002aa8d80420aad471d10fde000abb6366ff6` — **byte-identical to RD-33's v1.5 measurement**, so §8 did not move
- Frozen clone: `…/scratchpad/clone-08e-r9`, `git rev-parse HEAD` = `0bdd37d620379f29226c54e428113b16ffc38a3b`, `git status --porcelain` empty **before and after** all work (re-verified at close; subject digest re-verified unchanged at close)
- Reviewer: isolated fresh-context session, Claude family (Opus 5). Same-family re-review — not a family-diverse administration; F5's own example applies to me
- Authoring context: none. I read nothing outside the clone; all synthetic records were written to `…/scratchpad/rd34/`, never into the clone

---

## Method and what I ran

`[Observed]` Read in charter order: `AGENTS.md` (225 lines), `RD-33-instrument-v15-RAW.md` (181 lines, 12 findings, `VERDICT: REVISE`), the RD-33 section of `DISPOSITION-REGISTER.md` (L196–224), then the instrument in full (873 lines), the validator in full (713 lines), the v1.6 delta (175 lines), P-34 (139 lines), `TREND-LOG.md`, and `decisions/launch-gate/`.

`[Observed]` `python3 scripts/launch_gate_results.py --selftest` → **34 fixtures, 0 failing, exit 0**. Fixture-name roll printed and read in full.

`[Observed]` I built **26 synthetic administration records outside the clone** and ran the clone's own validator against them, all of them with git checks **ON** against the real commit `0bdd37d` and the real instrument and §8 digests, so LG-1/LG-2/LG-11 actually executed. My records are written field-for-field to §5's template in §5's own order (39 rows). Cited below as R1, r2–r5, p1/p2/p4/p5, and H1–H9.

`[Observed]` Byte-level comparison v1.5 (`997d9bd`) → v1.6 (`HEAD`): `git diff --numstat` = **+90 / −20**. Section-level identity computed with a fence-aware section splitter: §1, §2, §7, §8 **byte-identical**; §4's verdict-formula blockquote **byte-identical**; §4's five blocking conditions **byte-identical**; §2's closed-verdict-vocabulary bullet **byte-identical**. Of the **35** question blocks (denominator: all `- **XN [U|G]**` stems, A1…G1), exactly **one** differs — E4, additively. `*Fails when:*` count 33 at v1.5 and 33 at v1.6.

`[Observed]` Sweeps with Python `re`, never shell grep (rule 1), each with its denominator: over the instrument's **873** lines — `DEFAULT_ROUTE_SET` (4), default-reading/task-route/front-door (5), `LG-\d+` (9), version strings (17), §6 project-specific tokens (1 of §6's 38 lines). Repo-wide: **341** text files (`.md/.py/.yaml/.yml/.txt`, excluding `.git` and `_bootstrap`) → 56 launch-gate/version hits across 26 files, all read.

`[Unknown]` I did not run the `check_governance.py` battery, did not administer the gate, and read the 2026-08-09 pilot record only to count its `GATE VERDICT:` lines (not for content). All answer sets below are synthetic.

---

## Per-finding repair verification — all twelve RD-33 findings

| RD-33 | Class | Disp. | Status | Anchor / proof in the v1.6 bytes |
|---|---|---|---|---|
| RD33-01 | MAJOR | R | **verified-closed by execution** (residual — RD34-06) | §4:495–499: *"The disclosure is the scoped form's honesty, so it is checked, not trusted: a record with any scoped row whose deferred-wave findings line names no defect asserts a scoped defect exists and that none exists — a validation error (LG-9), never a lawful record."* Validator LG-9:316–333. **r2 rebuilt**: scoped `C2` + `findings…: none` + `READY FOR Capability 1`, git on → `LG-9: 1 scoped row(s) beside a deferred-wave findings line reading 'none'`. **r2-lawful** (same record, defect named) → 0 errors. The v1.5 self-contradiction is gone. |
| RD33-02 | MAJOR | R | **verified-closed on both limbs** (new residual — RD34-04) | §6:622 table gains **Scoped**; §6:630–636 *"A scoped finding is a finding."* Validator `_row_verdicts`:135–144 gives prior and current one normalization. **p1**: prior clean → current scoped prints `… | 0 | 1 | 0 | …` — the finding now has a column. **r5**: prior scoped → current plain `Not met` prints New-findings `1` (was `0` at v1.5). Asymmetry fixed; `startswith` is gone from the comparison. Header column count: §6 = 9, §6 separator = 9, `TREND-LOG.md` header = **byte-identical to §6's**, emitted row = 9. |
| RD33-03 | MAJOR | R | **verified-closed for the demonstrated string only** — see **RD34-02** | §5:592–596: *"The template's `(owner only)` parenthetical is a description of who may grant deferrals, never a satisfier … copying the template's own words meets no requirement (LG-7)."* LG-7 rewritten:371–382. **r3 rebuilt**: `READY-WITH-DEFERRALS (owner only)`, `Deferred count: 1`, no citation → `LG-7: … without an `Owner deferral decision:` field`. Fixtures for LG-7 and LG-2's mismatch limb now exist (both observed passing). But the new field is a bare non-emptiness test — RD34-02. |
| RD33-04 | MAJOR | R | **verified-closed by execution** (but see **RD34-01**) | §4:522–528: *"**Any deferral-carrying pass is `READY-WITH-DEFERRALS`.** … plain `READY FOR <LAUNCH_TARGET>` over any deferral, or over a nonzero `Deferred count:`, is a contradiction and a validation error."* The `f2_deferral` word-match regex is deleted. **r4 rebuilt**: `READY FOR` + `F2 | Not met | …treated as owner-deferred…` → `LG-6: … F2 is not Met — a pass resting on an F2 deferral is READY-WITH-DEFERRALS with an owner citation, never plain READY FOR (§4)`. Plain `READY FOR` + `Deferred count: 1` → also refused. |
| RD33-05 | MAJOR | R | **verified-closed by execution** | `ROSTER`:88–94 (39 entries); LG-10:271–278. **p2 rebuilt**: `READY FOR` with the `E5` row deleted → `LG-10: question rows missing: E5`. The 39-row denominator is now mechanical. |
| RD33-06 | MINOR | R | **verified-closed by execution** (weak containment — RD34-08) | LG-11:210–231. **p5 rebuilt**, git on, over the *correct* `0bdd37d` instrument and §8 digests: `Instrument version: v1.2` + `Launch target: Capability 7 — anything the reviewer names` → **two** errors, `LG-11: record claims instrument version v1.2 but the committed instrument … declares v1.6` and `LG-11: the record's launch target … is not the parameter block's LAUNCH_TARGET`. A missing `Launch target:` line errors with git off too (fixture observed). |
| RD33-07 | MINOR | R | **(a) verified-closed; (b) closed in substance, delta overstates — RD34-09** | (a) D-10 (delta:153–164) corrects the v1.5 delta's D-6 claim; my 873-line sweep confirms `DEFAULT_ROUTE_SET` appears at L315 (D2), L327 (D3), L689 (§8), L833 (changelog) — F4:421 and §4:482 still do not name it, exactly as D-10 states. (b) §6's pilot paragraph is gone from the instrument and present in `TREND-LOG.md`'s header with all four reasons intact; but §6:618 still carries a Syzygy path — RD34-09. |
| RD33-08 | MINOR | R | **verified-closed, all three limbs** | (a) `GOOD`:454–479 is now a full §5-template record built from `_template_rows()` (39 rows, every template field); **R1** — my own independently written full-template record — validates clean with git checks on. (b) P-34:28–32 now reads *"a **reviewable claim by the repair pass** … rejecting the alignment — narrowing either list — is open under option (b)"*; I compared the two lists item by item: seven items each, aligned. (c) Fixture→check map over all 11 checks, denominator 11: LG-1 (3 fixtures), LG-2 (1), LG-3 (4), LG-4 (2), LG-5 (3), LG-6 (7), LG-7 (3), LG-8 (2), LG-9 (1), LG-10 (2), LG-11 (3) — **the docstring's "each with a `--selftest` mutation fixture" is now true of the bytes at check granularity.** |
| RD33-09 | MINOR | R | **verified-closed** | §5:596–600: *"Of the trend row's figures, the Not-met, Scoped, and Unknown counts are **computed from the rows**; Deferred and Reopened are **declared required fields** the validator parses — declared, not computed, which is exactly why their absence errors instead of reading zero."* The per-run print (validator:411–417) says the same split; the blanket "never transcribed" sentence is gone. |
| RD33-10 | MINOR | R | **verified-closed by execution** | Subsumed by `ROSTER`, which contains `"E1"` as well as the five subs. **p4 rebuilt**: E1 rollup deleted, five sub-rows kept → `LG-10: question rows missing: E1`. LG-8 can no longer be silently disabled. |
| RD33-11 | MINOR | R | **verified-closed** | P-34:121–128: *"Under **option (b)**, the ordering extends the same way (RD33-11): the owner's amendments are applied to the instrument **in the working tree before step 2's digest is computed** — together with the status edit and the changelog's v1.7 entry … An amendment applied after step 2 would recreate exactly the approval-attests-bytes-that-exist-nowhere defect RD24-01 closed."* |
| RD33-12 | MINOR | R | **verified-closed** | E4:376–382, the only question block that changed between v1.5 and v1.6, additively: *"Where the routing authority is **silent** on a case … the silent case counts as neither agreement nor disagreement: E4 is judged over the cases the authority actually answers, with the silent ones enumerated in the row. Silence over a case the launch target *needs routed* is a finding in its own right."* No fail condition narrowed. |

**Tally, with its denominator:** of RD-33's **12** findings, **12 are present in the bytes and none is absent**; **11 are closed outright**; **1 (RD33-07b) is closed in substance with the delta's claim overstated**. Six I confirmed by execution rather than by reading (RD33-01/02/04/05/06/10). `[Inferred]` The repair session did the work the register describes, and the register's account is honest about what it did.

---

## New findings

### RD34-01 — BLOCKING — `READY-WITH-DEFERRALS` is checked against no conjunct of the §4 formula, and v1.6 made it the mandatory word for every deferral-carrying pass

§4:522–523 (defined clause, quoted): *"**Any deferral-carrying pass is `READY-WITH-DEFERRALS`.** The F2 deferral limb of the formula — and any other owner deferral a pass rests on — changes the verdict word."* A *pass* is the §4 formula satisfied. §4:463–472's formula requires every E `Met`, no plain `Not met` in launch-scope A–D, F1 `Met`-or-`Unknown`, F3 `Met`, F4 `Met`.

Validator:343 opens the conjunct battery with `if gv.startswith("READY FOR"):`; validator:371 opens the deferrals branch with `elif gv.startswith("READY-WITH-DEFERRALS"):`, which checks **only** the owner citation and a nonzero `Deferred count`. Not one formula conjunct is evaluated on that branch.

`[Observed]` **H9d**, git checks on, real commit and real digests: a record with **all 39 roster rows `Not met`** — every E question, all of A–D, F1, F3, F4 — carrying `Owner deferral decision: …/SDR-99-EXAMPLE.md`, `Deferred count: 1`, and `GATE VERDICT: READY-WITH-DEFERRALS` validates with **0 errors**, printing `record valid` and the trend row `| … | 39 | 0 | 0 | 1 | 0 | … | READY-WITH-DEFERRALS |`. **H9a** (E5 `Not met`), **H9b** (A1/C3/D1 `Not met`), **H9c** (F1/F3/F4 `Not met`) each also validate clean. `[Observed]` The control **H9d-control** — the identical rows under plain `READY FOR` — is refused with `an E question is not Met; Not met in A–D: A1 … D4; F3 is not Met; F4 …`.

`[Observed]` The hole pre-exists v1.6: the v1.5 validator (`997d9bd`) computed `bad` under `if gv.startswith("READY")` but raised it only `if bad and gv.startswith("READY FOR")`. What v1.6 changed is the *population routed onto it*. At v1.5, RD-33's own r4 shows a deferral-carrying pass travelled under plain `READY FOR` — where the E, A–D, F1, F3, F4 conjuncts did run and only the F2 limb was defeated. D-3 now forbids that route and **mandates** the branch with no formula check for every owner-deferred pass.

`[Observed]` The validator's own LG-6 docstring (validator:31–37) claims the gate-verdict line is checked as *"consistent with the §4 formula as computable from the rows"*. That is untrue on this branch.

`[Inferred]` This is RD-33's diagnosis recurring exactly: the repair for RD33-04 minted the next defect by making a previously-optional verdict word mandatory without giving it the check the word it replaced already had. The residual instrument work is small but real — §4 states the READY-WITH-DEFERRALS predicate only by implication ("a deferral-carrying *pass*"), against §4:469–470's own boast that *"Every term of this formula is a predicate over the closed verdict vocabulary"* — and an instrument amendment must travel **in** the P-34 offer, not after it (RD33-02's own reasoning, accepted by the repair session).

*Direction:* run the full conjunct battery on the `READY-WITH-DEFERRALS` branch too, omitting only the F2-`Met` and zero-deferrals limbs; state the READY-WITH-DEFERRALS predicate explicitly in §4; fixture the all-`Not met` case.

### RD34-02 — MAJOR — `Owner deferral decision:` is a non-emptiness test, so "(owner only)" satisfies it one field over; and the register claims a path check the bytes do not perform

§4:518–521: *"A deferral is claimed only by **citation**: the record's `Owner deferral decision:` field names the owner decision (path or identifier) that granted it."* Validator:309–314 accepts any value that is non-empty, does not start with `<`, and is not literally `none`/`n/a`.

`[Observed]` **H3**, git on: `READY-WITH-DEFERRALS` with `Deferred count: 1` validates with **0 errors** for every one of `owner only`, `(owner only)`, `the owner`, `yes`, `verbally agreed`, `TBD`, `-`, and a nonexistent path. `[Observed]` The value `(owner only)` — the exact string RD33-03 was about — satisfies the check that replaced the check it defeated; only its *location* changed.

`[Observed]` `DISPOSITION-REGISTER.md:215` (RD33-03 row) states the repair requires the field *"naming a path/identifier **that exists in the record's repo**"*. No such check is in the bytes, and the shipped positive fixture (validator:631–636) cites `.syzygy/governance/decisions/SDR-99-EXAMPLE.md`, which does not exist (directory listed, 17 entries, denominator stated) and expects `None` — the fixture set *encodes* the weaker behavior. RD-33's own direction was "matched against a path that exists". The v1.6 delta's D-3 does not make the existence claim, so the delta is honest here and the register is not.

*Direction:* require a path-or-identifier shape and reject template/label wording; either check existence or amend the register row to what the bytes do.

### RD34-03 — MAJOR — §5 says the *terminal* `GATE VERDICT:` line is parsed; the validator parses the *first*, and the project's only administration record has two

§5:588–589 (quoted): *"The terminal line's `GATE VERDICT:` token is literal — it is the line the validator parses and the trend row carries."* Validator:336 is `mg = GATE_VERDICT_RE.search(txt)` — leftmost match.

`[Observed]` **H6**, git on: a record carrying `GATE VERDICT: NOT READY` in a summary section and terminating in `GATE VERDICT: READY FOR Capability 1` over `| F2 | Not met |` validates with **0 errors** — LG-6 and LG-7 never see the real verdict — and the trend row prints `NOT READY`, a word the record's terminal line does not contain.

`[Observed]` This is not hypothetical: `round-2026-08d/reviews/LAUNCH-GATE-ADMINISTRATION-2026-08-09-RAW.md` (190 lines) carries **two** `GATE VERDICT:` lines, at L165 and L189. `GATE_VERDICT_RE.findall` over it returns `['NOT READY', 'NOT READY']`. The one administration this project has ever produced already has the two-line shape; the pilot escaped only because both lines agreed. `[Inferred]` The unsafe direction — earlier stricter, terminal laxer — passes silently; the reverse fails loudly, so the asymmetry favours the wrong outcome.

*Direction:* take the last match (`findall(...)[-1]` or `finditer` exhausted), and fixture a two-line record whose lines disagree.

### RD34-04 — MAJOR — v1.6's own new §6 rule is falsified by the validator it names: rendering a defect scoped improves the New-findings column

§6:631–632, added at v1.6 (quoted): *"rendering a defect scoped must never improve the read of any other column."*

`[Observed]` Same defect, same prior record, two renderings, both records otherwise identical:

| rendering of the one new C2 defect | Not-met | Scoped | **New findings vs prior** |
|---|---|---|---|
| `Not met` | 1 | 0 | **1** |
| `Not met (out of launch scope)` | 0 | 1 | **0** |

Validator:388–393 computes `new_vs_prior` from `{q: v == "Not met"}` on both sides; scoped rows are excluded from both, so a brand-new scoped finding never registers as new. `[Inferred]` D-2's repair gave scoped findings a *level* column but not a *delta* column, and §6:626–627 makes New-findings one of the two convergence signals F1 is read from. A round that repairs one scoped defect and mints another reads as zero change in Scoped and zero in New-findings. This is RD33-02's class surviving one column over, and the rule that names it is v1.6's own.

*Direction:* compute New-findings over `Not met ∪ scoped` (or emit a second scoped-delta figure), and fixture it.

### RD34-05 — MAJOR — two current-facing routed artifacts still name launch-gate **v1.5**; this is a recurrence at the exact two files RD25-03's disposition row names

`[Observed]` Repo-wide sweep, denominator **341** text files:

- `.syzygy/governance/contracts/candidates/DEFERRED-WAVE-POSTURE.md:41` — *"Under the launch-gate launch scope (v1.5 at this writing), a defect living only in these candidates blocks the Capability 1 verdict only if …"*. This file is §8's cited defining artifact for `LAUNCH_TARGET` and is reached directly from `AGENTS.md` — a `DEFAULT_ROUTE_SET` member. No banner.
- `.syzygy/governance/contracts/candidates/FIRST-OPENSPEC-SEQUENCE.md:70` — *"| P-34 launch-gate **v1.5** authority + formal administration READY |"*. This file is §8's `FIRST_SPEC_CANDIDATE`, the artifact E2 is answered from. P-34 asks about v1.6.

`[Observed]` `DISPOSITION-REGISTER.md:62`, the RD25-03 row: *"v1.5 re-quoted at P-34's queue row (+ v1.5 delta added to its record cell), `FIRST-OPENSPEC-SEQUENCE.md:52`, `DEFERRED-WAVE-POSTURE.md:41`"* — the same two files, recorded resolved at v1.4→v1.5 and stale again at v1.5→v1.6. In the gate's own vocabulary this is a **Reopened** finding, and §6:641–643 says *"a nonzero Reopened column indicts the resolution process, not just the finding."*

`[Observed]` No mechanical guard exists: sweeping `scripts/check_governance.py` (4,873 lines) for `launch[-_ ]?gate` returns **9** hits, all prose comments citing pilot findings; none checks instrument-version references.

`[Observed]` Everything else in the sweep is correct: `PENDING-OWNER-DECISIONS.md:181` reads v1.6 with the RD-34 precondition; `PROJECT-STATUS.md:125` cites v1.3 for the pilot and L129 states *"The instrument is now **v1.6**"*; `LAUNCH-CLOSURE-PREFLIGHT.md:35`'s v1.3 sits under an explicit *"Historical snapshot — non-authoritative round record"* banner; the v1.4/v1.5 delta filenames and the changelog's back-references are historically correct.

`[Inferred]` The meaning did not drift — I verified §4's formula blockquote and its five blocking conditions are byte-identical v1.5→v1.6, so the launch-scope sentence `DEFERRED-WAVE-POSTURE.md:41` relies on is still true. What is wrong is the version word, on a default route, without a banner — F4's stated fail condition, and RD-8's "surprised, not knowing" class.

### RD34-06 — MINOR — LG-9 catches "none" and the template placeholder, and nothing else

Validator:328–329 rejects a findings line matching `(?i)[\`*\s]*none[\`*.\s]*` or starting with `<`. `[Observed]` **H1**, git on, scoped `C2` + `READY FOR`: findings lines reading `n/a`, `—`, `N/A`, `not applicable`, `TBD`, `0`, and `.` each validate with **0 errors**. The check closes the exact string RD-33 demonstrated rather than the class. `[Observed]` **H2** — a findings line naming a defect for a *different* question than the scoped row — also validates; that limb is inherently non-mechanical and neither §4 nor the docstring overclaims it, so it is disclosed, not a defect.

### RD34-07 — MINOR — §5's "required whenever `Deferred count` is nonzero" is unenforced outside the `READY-WITH-DEFERRALS` branch

§5:579–581 (template, quoted): *"`Owner deferral decision:` … required whenever Deferred count is nonzero **or** the verdict is READY-WITH-DEFERRALS."* The validator checks only the second disjunct. `[Observed]` **H4**, git on: `GATE VERDICT: NOT READY` with `Deferred count: 3` and no `Owner deferral decision:` line validates with **0 errors**, and the trend row carries `Deferred = 3`. `[Inferred]` Uncited, reviewer-declared deferrals then enter the trend log, which §6:639–641 says must never let a deferral improve any other column's read.

### RD34-08 — MINOR — LG-11's launch-target check is substring containment, so any fragment passes

Validator:227 is `if tgt and tgt not in lt`. §5:553 requires *"`Launch target: <LAUNCH_TARGET, verbatim from the parameter block>`"*. `[Observed]` **H7**, git on: `Launch target:` values `Capability 1`, `Project registration`, `honest shape visibility`, `1`, `a`, and `The` all validate with 0 errors. RD-33's p5 is closed only because "Capability 7 …" happens not to be a substring. The docstring (validator:56–57) honestly says "whitespace-normalized containment", so the tool does not overclaim; §5's "verbatim" is what goes unenforced.

### RD34-09 — MINOR — D-7's project-invariance claim is not literally true of §6's bytes

Delta D-7 (delta:127–129): *"§7's 'everything project-specific lives in the parameter block' is now true of §6's bytes — the claim the v1.5 delta made prematurely."* §7's rule, quoted: *"everything project-specific lives in the parameter block."*

`[Observed]` §6 spans instrument lines 615–652. Sweeping those 38 lines for project-specific tokens (`.syzygy`, `Syzygy`, `Capability`, `067d8a0`, `2026-08-09`, `v1.3`) returns **1** hit: L618, `` `.syzygy/governance/decisions/launch-gate/TREND-LOG.md`; this is F1's `` — a Syzygy path, in §6, not in §8. `[Inferred]` The substantive move is real and good (the pilot narrative is gone, and moving it to `TREND-LOG.md` also narrows §2's withhold exposure, since the trend log is F1-only material). But the residual path is there because RD24-17 *required* §6 to name it, so the two requirements conflict and the delta resolves the conflict by asserting the stronger claim. This is the identical over-assertion D-10 was written to correct, recurring in the delta that corrects it. The honest form is "§6 carries no project-specific record or narrative; the trend-log path remains, as RD24-17 required."

### RD34-10 — MINOR — P-34 routes the owner to the v1.5 delta without noting that D-10 corrects two of its claims

`[Observed]` P-34:50–58, option (a), lists all three semantic deltas as "the amendment records". `[Observed]` `LAUNCH-GATE-v1.5-SEMANTIC-DELTA.md` (125 lines) contains no occurrence of `RD-34`, `v1.6`, `corrected`, `superseded`, or `D-10`, and carries no banner about its two claims RD-33 found untrue. `[Observed]` P-34 itself contains no occurrence of `D-10` or `corrected`. `[Inferred]` Not editing the frozen v1.5 delta is correct (rule 10). But an owner reading option (a) top-to-bottom meets two false claims before meeting their correction, and nothing tells them the correction exists. A one-line pointer in P-34's option (a) closes it; this is a packet edit, not an instrument edit.

### RD34-11 — MINOR — the roster binds presence, not membership: invented question IDs are accepted and counted

`[Observed]` **H5a/H5b**, git on: an extra row `| A9 | Met | … |` or `| E7 | Met | … |` validates with 0 errors and raises "rows parsed" to 40. `[Observed]` **H5c**: `| A9 | Not met |` under `READY FOR` produces `LG-6: … Not met in A–D: A9` — so extra rows fail *conservatively* for the pass branch. `[Inferred]` The residual is trend fidelity, not gate safety: an invented ID's verdict enters the computed Not-met/Scoped/Unknown columns of the appended trend row with no question behind it.

---

## What passes

`[Observed]` These are executions, not inferences:

- **All twelve RD-33 findings are present in the v1.6 bytes; none is absent.** Six confirmed by rebuilding RD-33's own records and running the clone's validator with git checks on.
- **A §5-template-shaped record validates.** R1 — 39 rows, every §5 field in §5's order, real commit `0bdd37d`, real instrument and §8 digests — passes with LG-1, LG-2, and LG-11 all executing. The same record with all rows `Met` and `GATE VERDICT: READY FOR Capability 1` also passes. RD-24's original complaint and RD33-08a's fixture complaint are both closed, and the `GOOD` fixture is now that shape.
- **The self-test is real and its count is honest.** 34 fixtures, 0 failing, exit 0; the count matches the delta's "**34 fixtures**" and P-34:88's "34 in all". Every one of the eleven checks LG-1…LG-11 has at least one fixture (map above, denominator 11), so the docstring's header claim is true of the bytes for the first time.
- **No question was weakened and no ID was renumbered.** Denominator: all 35 question stems. IDs identical and in identical order v1.5→v1.6; exactly one block (E4) differs and only by addition; `*Fails when:*` count 33 → 33; §2's closed-vocabulary bullet, §4's formula blockquote, and §4's five blocking conditions are **byte-identical**.
- **"What did not change" is accurate.** §1, §2, §7, and §8 are byte-identical v1.5→v1.6; §8's digest `01209c0f…` is unchanged from RD-33's independent v1.5 measurement.
- **The trend log's format matches §6 exactly.** `TREND-LOG.md`'s header row is byte-identical to §6:622; separator, header, and the emitted row are all 9 columns; the file correctly records *"zero rows is the correct current state, not a gap"* and now carries the pilot's four reasons in its own header.
- **LG-10 and delta administrations are consistent, not in conflict.** `[Observed]` **H8**: a 3-row steering delta record errors with `LG-10: question rows missing: A1 … F6` and the tool prints *"this record cannot support a gate decision as stored"* — which is precisely what §5:606–611 says should happen, while §2 keeps delta administrations lawful "for steering". The trend row is still emitted. No finding.
- **P-34 is coherent about v1.6.** Version references are v1.6 for the current offer and historically correct elsewhere; the fixture count is right; the RD-34 precondition is stated in the offer-status block (*"not yet offerable"*); RD33-11's option-(b) ordering extension is present and correctly reasoned; the governs-lists align item for item (seven each), now stated as a reviewable claim with rejection open under (b) as RD33-08b asked.
- **The clone stayed byte-clean.** `git status --porcelain` empty and the subject digest `9d68fa3b…` unchanged at close.

---

## Overall assessment — may v1.6 be offered to the owner at P-34?

The repair batch is genuine and better than its predecessor. Every one of RD-33's twelve findings is in the bytes, eleven are closed outright, six of them survived my attempt to break them by execution rather than by reading, and the two hardest — the scoped-row disclosure and the question roster — are now mechanical facts rather than prose. The delta is the most honest one in this sequence: D-10 volunteers two false claims from its own predecessor, and §8's unchanged digest, the byte-identical formula, and the single additive question edit all confirm its "What did not change" section rather than merely asserting it.

But RD-33's diagnosis holds a third time, and I can state it more sharply than the delta does. **v1.6's central repair moved the entire deferral-carrying-pass population onto the one verdict branch the validator does not check against the §4 formula at all.** Before D-3, a self-authorized deferral rode under `READY FOR`, where the E, A–D, F1, F3, and F4 conjuncts *did* run and only the F2 limb was defeated — which is exactly why RD-33's r4 was a MAJOR and not worse. After D-3, that route is forbidden and `READY-WITH-DEFERRALS` is mandatory, and a record with **all thirty-nine questions `Not met`** validates clean under it and prints a pass verdict into the trend row. The check that would have caught it, LG-6, advertises in its own docstring that it verifies "consistent[ency] with the §4 formula as computable from the rows". Three further MAJOR findings are the same shape: the new `Owner deferral decision:` field is a non-emptiness test that `(owner only)` satisfies, so RD33-03's string moved rather than died; §6's brand-new *"rendering a defect scoped must never improve the read of any other column"* is falsified by the New-findings column of the tool §6 names; and §5's stated "terminal line" is not the line the validator reads, in a repository whose only administration record already carries two such lines.

I would not call the packet unsafe to show. P-34's digest mechanism is right, its options are priced honestly, its RD-34 precondition is stated, and nothing in it misleads the owner about what approval binds. Most of what remains is validator work, and the validator is not digest-bound by the act. But two things push this past "patch it after": §4 states the `READY-WITH-DEFERRALS` predicate only by implication, against its own claim that every term of the formula is a predicate over the closed vocabulary — closing RD34-01 properly wants an instrument sentence, and an instrument sentence must travel *in* the offer, which is the exact reasoning the repair session itself accepted for RD33-02. And two artifacts on the routed path still ask the owner about launch-gate **v1.5** at the very two files RD25-03's disposition row named as fixed — a recurrence, which in this instrument's own vocabulary belongs in the Reopened column and indicts the resolution process rather than the finding.

So: **v1.6 is not yet what should be put in force, and the formal administration must not run on this validator either.** The remaining batch is small and mechanical — run the conjunct battery on the deferrals branch and state its predicate in §4; take the last `GATE VERDICT:` match; count new scoped findings as new; give the deferral citation a shape test; widen LG-9 past the literal word "none"; sweep the two stale v1.5 references and consider a `check_governance.py` guard so the next version bump cannot repeat it — each with a fixture, then a short re-review of the v1.7 delta, then the offer. RD-33 asked for one more repair batch and got a good one; this is the last one I can see a mechanism for, because after RD34-01 there is no unchecked verdict branch left to route a pass through.

VERDICT: REVISE
