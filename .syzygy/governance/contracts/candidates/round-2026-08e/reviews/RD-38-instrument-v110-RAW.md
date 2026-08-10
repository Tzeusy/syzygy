The clone is byte-clean at open and close. Here is the review of record.

---

# RD-38 — Launch-gate instrument re-review, v1.10 exact bytes (round-2026-08e, frozen commit 34cbe5e)

- Review id: RD-38 (sixth administration of the instrument re-review chain: RD-33 → v1.6, RD-34 → v1.7, RD-35 → v1.8, RD-36 → v1.9, RD-37 → v1.10)
- Date: 2026-08-10
- Subject: `launch-gate-pre-specifications.md` (v1.10, repo root), `scripts/launch_gate_results.py`, `round-2026-08e/LAUNCH-GATE-v1.10-SEMANTIC-DELTA.md`, `decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` (P-34), the RD-37 section of `reviews/DISPOSITION-REGISTER.md`, and `reviews/RD-37-instrument-v19-RAW.md` read in full
- Subject sha256, computed this session by two independent methods (`sha256sum` and Python `hashlib` over the file bytes): `3cb0814eebe734cc6f9279df35fddc967a5b05b131ea8d3b653a8b0d4f19f48f` — matches the charter
- Validator sha256: `f24e95d424d70046d1ed7fb8d4a1055c391398982cb0df5959afc899579128a8` (1563 lines)
- §8 parameter block, extracted by the validator's own `param_block_bytes`: `01209c0f052971f794e1f35827a002aa8d80420aad471d10fde000abb6366ff6`, **6610 bytes** — byte-identical to the same extraction at `95a41ea` and `b00c3dd`, and to RD-33/34/35/36/37's digest. §8 has now not moved across six amendments. (RD-37 §0 records the length as 6577 bytes; I measure 6610 at all three commits. The digest — the load-bearing figure — agrees exactly, so I record RD-37's length as an apparent transcription slip, not a byte difference.)
- Frozen clone `…/scratchpad/clone-08e-r18`: `git rev-parse HEAD` = `34cbe5e26a5b4d20cd0a310f9fabfc3dce09c15e`, `git status --porcelain` **empty at open and at close**; both subject digests re-verified unchanged at close by two methods. Every synthetic record, mutated validator copy and v1.9 sandbox was written to `…/scratchpad/rd38/`, never into the clone or the live repository.
- Reviewer: isolated fresh-context session, Claude family. Same-family re-review — F5's own example applies to me
- Authoring context: none. I authored no byte under review

---

## 1. Method and what I ran

`[Observed]` Read in charter order: `AGENTS.md`, `RD-37-instrument-v19-RAW.md` (256 lines, 6 findings, `VERDICT: REVISE`) in full, the RD-37 register section, the v1.10 delta (191 lines), the validator in full (1563 lines), instrument §5 in full, §3's E3 clause, §9's v1.10 entry, P-34 (191 lines), `PENDING-OWNER-DECISIONS.md:188`, `PROJECT-STATUS.md:131–163`.

`[Observed]` `python3 scripts/launch_gate_results.py --selftest` in the clone → **86 fixtures, 0 failing, exit 0**. Full roll printed and read.

`[Observed]` I built a record generator matching §5's template field-for-field (39 roster rows) and ran **the clone's own validator**, imported so `REPO` resolves to the clone, with git checks **ON** against the real commit `34cbe5e`, the real committed instrument digest `3cb0814e…`, the real §8 digest `01209c0f…`, and the real `effective_version: v1.10` — so LG-1/LG-2/LG-11 and both citation-existence paths executed on every case below. Roughly 140 synthetic records.

`[Observed]` **Mutation-revert testing (rule 6)** on eight copies outside the clone, each with the clone's `.git` symlinked so git-on fixtures still run: five reverting a v1.10 repair, three attacking the meta-fixture itself. Recorded in §2 and §5.

`[Observed]` **Cross-version execution.** I rebuilt the v1.9 validator from `git show 95a41ea:scripts/launch_gate_results.py` with its own instrument copy (digests `8945bbe6…` / `bc1363bf…`, matching RD-37's measurements exactly) and ran the *same* records through both — the measurement that produced RD37-01, repeated in both directions. 28 comparison cases.

`[Observed]` Fixture→check coverage computed mechanically by intercepting `validate()` and binding each emitted error to its `LG-n` prefix. Denominator **13** checks.

`[Observed]` Repo-wide sweeps with Python `re`, never shell grep (rule 1). Denominator **354** text files (`.md/.py/.yaml/.yml/.txt`, excluding `.git`/`_bootstrap`/`.beads`).

`[Observed]` `python3 scripts/check_governance.py` in the clone → **30 OK, 18 WARN, 0 FAIL (48 checks)**; `--selftest` → **121 fixtures, 0 failing**.

`[Unknown]` I did not administer the gate and read no pilot record content. All answer sets below are synthetic.

---

## 2. Per-finding repair verification — all six RD-37 findings

| RD-37 | Class | Disp. | Status | Anchor / proof in the v1.10 bytes |
|---|---|---|---|---|
| RD37-01 | MAJOR, offer-blocking | R | **verified-closed by execution, by cross-version measurement, and by mutation** | Validator:314 (defined bytes, quoted): `_E3_EMPTY_RE = re.compile(r"(?:empty\|none(?: identified)?)\.?$", re.I)`, consumed at 740 as `elif not _E3_EMPTY_RE.fullmatch(_e3_val):` — a **positive** full-line test, not the negation of a placeholder test. RD-37's four attack records rebuilt verbatim (`no items are resolved: `, `none of these are closed: `, `nothing is settled: `, `zero of the reopen items are closed: ` + the same two enumerated items) beside `E3 \| Met` under `READY FOR Capability 1 — Project registration and honest shape visibility`, git on, real digests: **2 LG-13 errors each, four of four, both branches**; under `NOT READY` with `E3 \| Met`, 1 LG-13 error each (the E3-Met branch alone). Cross-version: the identical records score **v1.9 = 0 errors, v1.10 = 2 errors** — the regression is measurably reversed. Lawful markers accept: `empty`, `none`, `none identified`, and their case and trailing-period variants (`Empty`, `NONE`, `None identified`, `empty.`, `none.`, `none identified.`, `EMPTY.`) — **ten of ten, 0 errors**, including `none identified` beside `E3 \| Met`, which does **not** error. The unfilled slot `<empty \| enumerated items>` **rejects** (2 errors). `_names_nothing` (295–304) now has exactly two consumers, LG-9 and LG-12, both of one polarity, and RD36-04's negation rule is intact: all four negation-phrased findings lines (`no defects found`, `none identified`, `nothing of note`, `no findings in the deferred waves`) still produce an LG-9 error, as do `none`, `(none known)`, `-- none --`, `unknown`, `tba`, `TBD`, `0`; the real finding line passes. **Mutation 1**: reverting LG-13 to `_names_nothing` on a copy → `86 fixtures, 3 failing`, failing exactly the three RD37-01 fixtures. **Marker-vocabulary attack**: `fullmatch` makes it structurally impossible for any enumeration to match a marker — 20 near-miss forms tested, no enumeration full-matched. The residual is the *opposite* direction — RD38-07. |
| RD37-02 | MAJOR | R | **verified-closed for all ten declared labels, in both orders, by execution and by mutation** | `_decl()` at 327–347: `re.findall`, distinctness over `_norm_ws`, error on disagreement, `vals[-1]` returned. I enumerated its ten call sites from the source and drove a disagreeing duplicate of each label, **above and below** the declared line: **10/10 error in both orders, 20 of 20 executions** — `Launch target:`, `Instrument version:`, its `sha256:`, `Parameter block sha256:`, `Deferred count`, `Reopened count`, `Owner deferral decision:`, the findings line, `Unknowns…`, `E3 reopen-list:`. RD-37's three shadowing records rebuilt: E3 empty-then-enumerated → **3 errors** (disagreement + both LG-13 limbs); Unknowns honest-then-TBD → **2**; findings honest-then-none → **2**; each reverse order → **1** (the disagreement). Agreeing duplicates do **not** reject (4 fields tested, 0 errors each). **Mutations 2 and 3**: reverting the E3 field to `re.search` → `86 fixtures, 2 failing` (the decoy fixture **and** the meta-fixture); reverting the Unknowns field → same shape. Two residuals: the meta-fixture is evadable (RD38-04) and RD36-02's line-anchoring rule did not travel with `_decl` (RD38-03). |
| RD37-03 | MINOR | R | **verified-closed for the record RD-37 demonstrated; defeated one level up — RD38-01** | Validator:497: `if not re.search(r"^#+\s*G1\b", txt, re.M):`. RD-37's exact record (`## Materials: we cite §3's G1 rule`, real section deleted) → **LG-4 error**. `### G1` alone → **0 errors**. Anchor attacks, 12 forms: `## G1x` rejects (the `\b`), `## notes` rejects, `> ## G1` rejects (blockquote), inline `` `## G1` `` rejects, `## g1` rejects (case). Accepted: `##G1` with no space (not a CommonMark heading), `## G1:`, `###### G1`. And — decisively — a **fenced code block quoting §5's own template heading**, with the record's G1 section deleted, validates **clean**. See RD38-01. |
| RD37-04 | MINOR | R | **verified-closed for the demonstrated case; the class survives — RD38-06, and the register overclaims it — RD38-05** | Validator:768–782. RD-37's three-line non-record prior (`A1`, `B2`, `G1` rows) → LG-5 error naming the missing rows and the alien `G1`, and trend column 7 reads exactly `n/a — prior record failed validation`; a lawful prior yields `2`; no prior yields `n/a — no prior record supplied`. **Mutation 5**: disabling the roster guard → `86 fixtures, 1 failing`, the RD37-04 bespoke fixture. Residual measured: the check is roster-**shape** only — see RD38-06. |
| RD37-05 | MINOR | R | **verified-closed structurally and by execution; the honest cap verified TRUE by my own sweep** | `_sdr_exists` at 207–228: `pat = r"(^\|[^-A-Za-z0-9])" + re.escape(ident) + r"($\|[^0-9a-z(])"`, `git grep -qE`, with `:(exclude).../PENDING-OWNER-DECISIONS.md`. At the real commit: `SDR-33` **True**, `SDR-9999` **False**, `SDR-34`/`SDR-40`/`SDR-0` False, `SDR-33a`/`SDR-2a`/`SDR-33(a)` False. **The delta's honest cap is true**: my own sweep of the decisions home at `34cbe5e`, denominator **18 files**, finds **33 distinct SDR tokens, SDR-1…SDR-33, gapless** — so the substring direction is indeed unfixturable against the live corpus. I proved the anchoring **structurally against a synthetic gapped corpus** instead: against `"SDR-33 … XSDR-7 … SDR-33a … SDR-12b"`, the v1.9 fixed-string test accepts `SDR-3`, `SDR-7`, `SDR-1` and `SDR-12`; the v1.10 anchored pattern rejects all four — **four false accepts closed**. `re.escape` escapes the hyphen (`SDR\-33`), which GNU ERE reads as a literal; no escape failure. Pathspec exclusion executes correctly at four older commits (`95a41ea`, `b00c3dd`, `HEAD~5`, `HEAD~20`): `SDR-33` True, `SDR-9999` False at each. Boundary-class edges: the trailing class `[^0-9a-z(]` excludes lowercase suffixes but **not** uppercase (`SDR-33X`), underscore (`SDR-33_draft`) or hyphen (`SDR-33-bis`) — no such form exists in this repository, recorded as a disclosed edge, not a finding (rule 8). |
| RD37-06 | MINOR | R | **verified-closed for the disagreement rule; NOT closed for the line-anchoring rule — RD38-03** | The three label-shaped §2 anchors now parse through `_decl` and error on disagreement in both orders (measured above; the fixtured case is `Parameter block sha256:`). But their *patterns* were not brought under RD36-02's anchoring rule — see RD38-03. The **scope decision** excluding `mdate`/`mcommit` is stated in D-3 and at the parse site (367–371) and I judge it **sound**: I confirmed by execution that a lawful record naming another commit in narrative parses correctly. The gap is that the same reasoning was not applied to the three labels that *were* included. |

**Tally, with its denominator:** of RD-37's **6** findings, **6 are present in the v1.10 bytes and none is absent**; **3 are closed outright** (RD37-01, RD37-02, RD37-05); **3 are closed for the case RD-37 demonstrated and leave a residual one level up** (RD37-03 → RD38-01, RD37-04 → RD38-06, RD37-06 → RD38-03). All five repairs were **mutation-proven by me this session**, each failing exactly the fixtures it added. `[Inferred]` The repair session did the work the delta and register describe, and its records are honest about it with the two exceptions recorded as RD38-02 and RD38-05.

---

## 3. Verification of the delta's and the records' claims

`[Observed]` **"§1–§8 byte-unchanged from v1.9."** True. Per-section sha256 with a fence-aware splitter, `git show 95a41ea:launch-gate-pre-specifications.md` vs `34cbe5e`, **ten sections each side, denominator 10**: §1 `1f2d1d60…`, §2 `11a9d452…`, §3 `fe0b051e…`, §4 `f4a2a642…`, §5 `3f5023d8…`, §6 `b54c12e5…`, §7 `bf31396f…`, §8 `01209c0f…` — **all eight identical**, and identical to RD-37's own per-section measurements. Only `HEADER` and `## 9. Changelog` differ. The full instrument diff is **48 lines**: one `effective_version:` line and one appended §9 v1.10 entry. **Zero question blocks changed; no ID renumbered; no verdict word changed.**

`[Observed]` **"The §9 v1.9 entry carries no correction marker."** True — the diff contains no edit inside the v1.9 entry. RD-37's judgment that the entry "asserts nothing false" stands unaltered.

`[Observed]` **The frozen records were not edited.** The six deltas v1.4 `3c52291a…`, v1.5 `1aa8bf50…`, v1.6 `67820bb2…`, v1.7 `5d6b775a…`, v1.8 `08395032…`, v1.9 `0acf4eed…` and the four prior raw reviews RD-33 `1baac272…`, RD-34 `2458970a…`, RD-35 `de568d7b…`, RD-36 `05d89819…` are **byte-identical** to their state at `95a41ea`. Nit: the delta says "the RD-33 … RD-37 raw reviews are byte-identical to their pre-batch state" — RD-37's raw review has no pre-batch state; it was **added** by this batch. Substance correct, phrasing loose for one of five.

`[Observed]` **"The batch newly accepts nothing."** True in every case I could construct. 28 cross-version comparisons against the v1.9 validator running at its own commit with its own digests: **zero cases where v1.9 errored and v1.10 did not**. The agreeing-duplicate case accepts at both versions, exactly as the delta says. But the *mirror* half of the sentence — *"A lawful record under a correct v1.9 reading remains lawful under v1.10"* — is **measurably false**; see RD38-03 and RD38-07.

`[Observed]` **The v1.9 delta's false D-4 is corrected via the v1.10 delta's D-1**, and the frozen v1.9 delta is byte-identical (above). D-1 quotes D-4 accurately and states the correction in the D-10 convention.

`[Observed]` **Fixture→check coverage, denominator 13.** Emissions across the run: LG-1 (4), LG-2 (11), LG-3 (4), LG-4 (3), LG-5 (5), LG-6 (11), LG-7 (27), LG-8 (3), LG-9 (10), LG-10 (7), LG-11 (5), LG-12 (13), LG-13 (9). **All thirteen fire; none is absent.** 112 total emissions. `validate()` invocations = **85**, printed count = **86** — the difference is the RD37-02 meta-fixture, which is a source scan and validates no record. The delta's arithmetic reconciles exactly: 74 + 3 + 5 + 2 + 1 = 85 record validations, + 1 source scan = 86.

`[Observed]` **P-34 is coherent at v1.10.** The question names **v1.10** (L11); the offer-status block is dated 2026-08-10, says *"not yet offerable"*, summarizes RD-37's two MAJOR findings correctly, and names **RD-38** as the precondition (L33–34); option (a) lists **all seven** deltas with correction pointers before the claims they correct — v1.5 *"read with the v1.6 delta's D-10"*, v1.7 *"read with the v1.8 delta's D-1"*, v1.8 *"read with the v1.9 delta's D-1 and D-4"*, v1.9 *"read with the v1.10 delta's D-1"* (L88); option (b) carries the **v1.11** ordering (amendments before the digest, RD33-11); the recommendation reads **"86 in all"** (L139), matching; the approval block (L161) names **v1.10**. `PENDING-OWNER-DECISIONS.md:188` and `PROJECT-STATUS.md:131–163` both name v1.10, name RD-38 as the precondition, and describe the chain accurately.

`[Observed]` **Stale-version sweep, denominator stated.** 354 files scanned; **81** lines carry both a launch-gate token and a `v1.x` token, across **24** files; all 81 read and classified. Every one of the 74 not naming v1.10 is a delta filename or title, a §9 changelog back-reference, a frozen review, a historical disposition row, a round-08d artifact, the v1.3 pilot (`PROJECT-STATUS.md:131`, immediately followed at :135 by *"The instrument is now **v1.10**"*; `LAUNCH-CLOSURE-PREFLIGHT.md:35`, under its explicit historical banner), or P-34's own seven-delta list. RD34-05's version-neutral repair holds — `DEFERRED-WAVE-POSTURE.md` and `FIRST-OPENSPEC-SEQUENCE.md` carry **no** `v1.x` token and therefore do not appear in the sweep at all. **No routed artifact names a stale instrument version.**

`[Observed]` **One instrument sentence and one register row are false of the bytes** — RD38-02 and RD38-05 below.

---

## 4. The uniformity audit — attacking the batch's own claim with its own standard

RD-37's rule, adopted verbatim by this batch: *"when a predicate or a parsing rule is repaired, it is repaired for every consumer and every field."* I enumerated every predicate and parsing rule in the validator, listed its consumers, and tested one-polarity-per-predicate and one-rule-every-field by execution.

| Predicate / parsing rule | Consumers | One polarity? | One rule, every consumer? | Measured |
|---|---|---|---|---|
| `_names_nothing` | LG-9, LG-12 | **yes** — "names nothing" is the error at both | **yes** | 11 values × 2 checks; the four RD36-04 negation forms all still reject |
| `_E3_EMPTY_RE` | LG-13 only | n/a (sole consumer) | **yes** | 20 forms; no enumeration can full-match |
| `_decl` — findall + disagreement + last value | 10 call sites | n/a | **yes for disagreement** | 10 labels × 2 orders = 20 executions, all error |
| `[^\S\n]*` line anchoring (RD36-02) | 10 `_decl` sites | n/a | ***NO* — 7 of 10 anchored, 3 use `\s*`** | empty `Parameter block sha256:` silently borrows the next line → 0 errors; anchored control errors — **RD38-03** |
| `^`-anchoring of the label | 10 `_decl` sites | n/a | ***NO* — 7 of 10** | a mid-line prose mention of `Instrument version:` becomes the *authoritative* value via last-wins — **RD38-03** |
| `_norm_ws` | `_decl` distinctness, LG-11 header target, LG-11 verdict target | n/a | **compare-basis ≠ return-basis** | `none identified` / `none  identified` are "agreeing" for `_decl` and *different* for `_E3_EMPTY_RE` → false LG-13 rejection — **RD38-07** |
| `ROW_RE` | current rows, `_row_verdicts` (prior) | n/a | **yes** (RD33-02's repair holds) | bold, `\|`-carrying cells, blockquoted rows all behave |
| `VERDICT_RE` | current record only | n/a | ***NO* — never applied to the prior** | roster-complete prior with `Partially met` on all 39 rows passes silently — **RD38-06** |
| duplicate-row detection | current only | n/a | ***NO*** | a prior with a duplicate `A1` row silently takes the last; a current record errors "appears twice" — **RD38-06** |
| `ROSTER` | LG-10 (current), `--prior` (v1.10) | n/a | **yes** — this is the v1.10 repair | both sides checked |
| `DECISION_ID_RE` / `_UNMADE_ID_RE` / `_FINDING_ID_RE` | `_deferral_citation_error` | n/a | **yes** | `B-n`, `P-n`, `D-n` all reject with their own reasons |
| `_sdr_exists` boundary regex | `_deferral_citation_error` | n/a | **yes** | anchoring proven on a synthetic gapped corpus; semantics remain mention-presence, disclosed |
| record-structure vs quoted text | LG-4's G1 anchor + LG-12's 8 presence tokens | n/a | ***NO* — no consumer distinguishes the record's own structure from a quotation** | a fenced quote of §5's template satisfies LG-4 and six of the eight LG-12 tokens — **RD38-01** |
| `GATE_VERDICT_RE` + terminal-line rule | current only | n/a | **yes** | 8 verdict forms; trend row 9 columns in every case |
| `param_block_bytes` | LG-2, LG-11 target | n/a | **yes** | 6610 bytes, digest stable at three commits, contains no `## 9` |
| the meta-fixture's own scan | asserts the `_decl` rule | n/a | ***syntactic proxy, evadable*** | three refactors evade it, one of them a literal `re.search` on a literal label — **RD38-04** |

**Reading the denominators:** of the 16 predicates and parsing rules, **10 satisfy the uniformity standard, 6 do not**. The batch's headline repairs (`_names_nothing` split, `_decl` disagreement, `ROSTER` on both sides) do hold uniformly and are the strongest work of the chain. What did not travel is *other* rules over the *same* consumer set — RD36-02's anchoring across `_decl`'s ten fields, RD-33's row-normalization across the prior side, and the record-vs-quotation distinction across LG-4 and LG-12.

---

## 5. New findings

### RD38-01 — BLOCKING — a record that deletes its G1 section **and six of the eight declared §5 fields** validates clean if it quotes §5's own template in a fenced appendix; the composite reads `READY FOR <the verbatim launch target>` and enters the trend log

LG-4's anchor (497) and LG-12's presence loop (692–711) both read the record as flat text. §5's template — quoted at instrument L566–605 inside a ```markdown fence — itself contains `## G1 — completeness critic` (L590) and the literal labels of every presence-tested field. So a record may satisfy seven checks by quoting the very template it is supposed to fill in.

`[Observed]` Executed at `34cbe5e`, git on, real digests, full 39-row roster, `F2 | Met`, `E3 reopen-list: empty`, terminal `GATE VERDICT: READY FOR Capability 1 — Project registration and honest shape visibility`. The record's G1 section is replaced by `## (this record records no completeness critic)`, and these six declared elements are **deleted outright**: the non-authority banner, `Reviewer:`, `Reviewer model family:`, `Materials given:`, `Operationalization notes:`, `Reviewer's falsification notes:`. A fenced appendix quotes §5's template.

```
→ errors: 0        (`record valid`)
→ trend : | 2026-08-10 | 34cbe5e2 | 0 | 0 | 1 | 0 | 0 | n/a — no prior record
          supplied | READY FOR Capability 1 — Project registration and honest
          shape visibility |
```

`[Observed]` **The identical record without the quoted appendix produces 7 errors** — LG-4 plus all six LG-12 presence errors. The appendix is the whole difference.

Instrument §4 (defined clause, quoted): *"G1 yields no verdict and never blocks, but an administration missing G1 is incomplete and cannot support a gate decision."* Instrument §2 requires the fresh-context disclosure; §5 declares all six fields; RD24-02 put the non-authority banner there so a record cannot read as an owner act. A record missing every one of them, reading `READY FOR <target>`, is exactly the record §4 and §5 condemn, and the validator prints `record valid`.

`[Observed]` **This is a survivor, not a v1.10 regression** — the same record scores 0 errors under the v1.9 validator at `95a41ea`. But it is RD37-03's class one level up, and RD37-03's own repair is the reason it matters: the fixture asserts *"a heading that merely MENTIONS G1 does not satisfy LG-4"*, and the next shape up — a heading that **is** the template's G1 heading, quoted — does satisfy it. The record shape is not exotic: the fixture suite itself models a record with an *"Appendix, quoting §5's own template"* (the RD35-02 fixture), and §5's own instruction to record `Materials given:` and `Operationalization notes:` invites quotation.

`[Inferred]` The root cause is the last unapplied consumer of RD-37's own rule: every *value* check now distinguishes a declared field from a decoy (that is `_decl`), and every *presence* check still does not distinguish the record's own structure from a quotation of the template.

*Requires:* a **validator change** — exclude fenced blocks (and, for LG-4, blockquotes) from the LG-4 anchor scan and the LG-12 presence scan, or require the presence tokens to appear outside a fence — plus a fixture per surface in both directions. **No instrument amendment**; §2, §4 and §5 already state the rules. **Blocks the formal administration.** Not offer-blocking on its own: no owner-facing document misdescribes it.

### RD38-02 — MAJOR, offer-blocking — the instrument's own §9 v1.10 entry attributes the LG-13 marker vocabulary to §5's template slot; §5's slot names one of the three markers, and `none identified` appears nowhere else in the instrument

Instrument §9, v1.10 entry (quoted, L995–997): *"LG-13's emptiness became a positive test over the closed marker vocabulary **§5's own slot names** (`empty` / `none` / `none identified`), never the negation of the placeholder test."*

`[Observed]` Instrument §5, L594, the defined slot, quoted in full: `E3 reopen-list: <empty | enumerated items>`. It names **one** of the three markers. `none` appears in §5 only at L595, on a *different* field (`Deferred-wave findings recorded outside launch scope: <list | none>`). `none identified` appears in the instrument **exactly once**, at L996 — inside the §9 sentence making the claim. Denominator: full-file sweep, 3 patterns, 1017 lines.

`[Observed]` The v1.10 delta's D-2 makes the same claim in its first bullet — *"the closed marker vocabulary §5's own template slot names — `empty`, `none`, `none identified`"* — and then **contradicts it correctly** four paragraphs later: *"No instrument sentence changes: §5's slot already reads `<empty | enumerated items>`, and the marker vocabulary is validator policy beneath it."* The delta therefore contains both the false claim and its own refutation; the §9 entry carries only the false half.

Why this matters more than a wording slip: the marker vocabulary **is** the new gate semantics for the check the validator's own docstring calls *"the instrument's self-declared sharpest single gate"* (LG-13/§3 E3). An owner reading §9 concludes the vocabulary is grounded in the instrument's normative text. It is not — it is validator policy, and it newly rejects a class of honest records (RD38-07). This is verification rule 8 exactly: a claim about a contract must anchor to a defined clause, and the clause says something narrower than the claim.

*Requires:* an **instrument amendment** — one §9 sentence, either stating that the vocabulary is validator policy beneath §5's slot (which is what D-2's own closing paragraph says) or publishing it in §5 — and a **record correction** to D-2's first bullet. Unlike every other finding in this batch, this one **moves instrument bytes**, so the approval digest v1.10 would bind is not the digest that should be approved. **I judge it offer-blocking**: the sentence is inside the bytes the owner's approval digest binds, and it misstates where the batch's one new semantic rule comes from. RD-8's *"the finding that converts act 1 from a knowing act into a surprised one"* applies with more force here than in RD-37's case, because there the false sentence sat in a delta and here it sits in the instrument.

### RD38-03 — MAJOR — RD36-02's line-anchoring rule did not travel with `_decl`: 3 of the 10 declared fields are un-anchored, an empty §2 digest field still borrows the next line, and a prose mention below the header silently becomes the value LG-2 and LG-11 report on

The validator asserts the rule in two places. LG-5's docstring (32–34, quoted): *"every field value is line-anchored, so an empty field is absent rather than borrowing the next line's text (RD36-02)."* The comment at the parse site (367–370, quoted): *"RD36-02: every field value is anchored with `[^\S\n]*` — `\s*` crosses the newline… An empty field is absent."*

`[Observed]` Source-derived audit of all ten `_decl` call sites. Seven are `^`-anchored with `[^\S\n]*`. **Three are neither**: `Instrument version:\s*\**\s*(v[\d.]+)`, `Instrument version:[^\n]*sha256:\s*` and `Parameter block sha256:\s*`. Denominator 10.

`[Observed]` Both consequences executed, git on, real digests:

- **The empty field still borrows.** A record whose `Parameter block sha256:` line is left empty with the digest on the **following** line → **0 errors**. The truly-empty control (nothing follows) → 1 error. The line-anchored control (`E3 reopen-list:` empty, `empty` on the next line) → 1 error, correctly. The RD36-02 class is alive on the §2 integrity anchors — the exact fields RD37-06 brought under `_decl`.
- **A narrative mention becomes authoritative.** `_decl` returns the **last** value, and these patterns are not `^`-anchored, so a mid-line mention below the header wins. A record whose falsification notes read *"I checked whether Instrument version: v1.9 would be accepted"* → **2 errors**, the second (quoted): *"LG-11: record claims instrument version v1.9 but the committed instrument at the named commit declares v1.10."* **The record declares v1.10 in its header.** The validator reports a claim the record does not make. Same shape for an appendix quoting a prior administration's `Parameter block sha256:` → LG-2 reports a digest mismatch quoting the *narrative* digest. The identical prose shapes against a line-anchored label (`Launch target:`, `E3 reopen-list:`) are correctly inert — **0 errors**.

`[Observed]` **Cross-version: both records validate clean at v1.9 and are rejected at v1.10.** So the delta's *"A lawful record under a correct v1.9 reading remains lawful under v1.10"* is false of them. A third case: a record quoting §5's three field slots in a fenced appendix scores 0 at v1.9 and **4 errors** at v1.10.

`[Inferred]` D-3's scope decision is right about *date and commit* and inconsistent about these three. Its stated reason — *"a lawful record names other commits in evidence and narrative"* — applies with equal force to a record that names another instrument version in narrative, which §5's own `Reviewer's falsification notes:` field invites. The three labels were included in `_decl` without being brought under the anchoring rule that makes inclusion safe.

Direction, stated plainly: **no gate is defeated.** The digest direction is loud (a borrowed digest is still verified against the real §8), and the prose direction over-rejects rather than under-rejects. What fails is the batch's central claim and the validator's own two-place assertion.

*Requires:* a **validator change** — anchor the three patterns as `^…[^\S\n]*`, uniformly — plus a fixture asserting the anchoring for those fields, and a **record correction** to the delta's "What did not change" both-directions sentence. **No instrument amendment.** Blocks a clean claim of uniformity; **not offer-blocking on its own.**

### RD38-04 — MINOR — the RD37-02 meta-fixture is a syntactic proxy that three trivial refactors evade, one of them a literal `re.search` on a literal label; and 5 of the 10 declared labels have no behavioral disagreement fixture behind it

The delta's D-3 (quoted): *"A **source-scan meta-fixture** enumerates the declared labels and **fails the selftest if any is ever read by a raw `re.search` again** — the fixture asserts the uniformity, not the instance."* The implementation (1519–1541) scans for `re.search(` and checks the following **120 characters** for a literal label.

`[Observed]` Three mutations on copies, each reverting the E3 field to a first-match read; in **all three the meta-fixture PASSES**:

| Mutation | Meta-fixture | What actually caught it |
|---|---|---|
| M6 — `re.finditer(...)` + `next(it, None)` | **pass** | the behavioral decoy fixture |
| M7 — `re.search` with the label built as `"E3 reopen-" + "list:"` | **pass** | the behavioral decoy fixture |
| M8 — **literal `re.search` on the literal label**, with a long comment between the call and the pattern | **pass** | the behavioral decoy fixture |

M8 falsifies D-3's sentence on its own literal terms: this *is* a raw `re.search` reading a declared label, and the selftest does not fail on the meta-fixture.

`[Observed]` Behavioral disagreement fixtures exist for **5 of the 10** declared labels: `Deferred count` (RD36-03), `E3 reopen-list:`, `Unknowns…`, the findings line (RD37-02), `Parameter block sha256:` (RD37-06). **Five have none** — `Launch target:`, `Reopened count`, `Owner deferral decision:`, `Instrument version:`, its `sha256:`. For those five the evadable scan is the only guard, so a reversion there would be caught by nothing.

`[Inferred]` A source scan can assert a coding convention; it cannot assert a behavior. The rule RD-37 asked for — *"the fixture asserts the uniformity rather than the instance"* — is satisfied behaviorally by writing the decoy fixture for every declared label, which is a loop over the ten labels, not a source regex.

*Requires:* a **validator change** (a generated behavioral decoy fixture per declared label, both orders — ten labels, one loop) and a **record correction** to D-3's sentence. **No instrument amendment; not offer-blocking.**

### RD38-05 — MINOR — the disposition register's RD37-04 row claims a `--prior` verdict-vocabulary check the bytes do not contain

`DISPOSITION-REGISTER.md`, RD37-04 row (quoted): *"The `--prior` path validates its input before trusting it: **full roster coverage and closed verdict vocabulary**, refusing the trend computation with a named error otherwise."*

`[Observed]` The bytes (768–782) check `ROSTER` coverage and alien row IDs only. `VERDICT_RE` is never applied to `prior_rows`. Executed: a **roster-complete prior with `Partially met` on all 39 rows** — a verdict word LG-3 rejects outright in a current record — passes the prior check **silently**, and the New-findings column prints `2`.

The v1.10 delta's D-5 does **not** make this claim and is accurate. The register row does. This is RD36-07's class recurring: a register row that never matched the bytes.

*Requires:* a **record correction** to the register row, dated, in the same convention the register already uses for the three RD36-07 corrections — or a **validator change** making the row true. **No instrument amendment; not offer-blocking.**

### RD38-06 — MINOR — the `--prior` guard is roster-**shape** only: a bare row block is a lawful prior, and a fabricated prior can drive the New-findings column to zero

RD37-04's repair closed the case RD-37 demonstrated (a three-line non-record). `[Observed]` Executed, git on, real digests, current record with a newly plain `A1 | Not met` and a newly scoped `B2`:

| prior supplied | New-findings column | error? |
|---|---|---|
| a lawful full record | `2` | — |
| RD-37's three-line non-record | `n/a — prior record failed validation` | **yes** |
| **a bare 39-line row block** — no header, no digests, no named commit, no gate verdict | `2` | **no** |
| roster-complete, every verdict `Partially met` | `2` | **no** |
| roster-complete, **every row fabricated as `Not met`** | **`0`** | **no** |
| roster-complete but naming a different instrument version, digests and launch target | `2` | **no** |
| a prior that fails LG-13 as a current record | `2` | **no** |
| roster-complete with a **duplicate** `A1` row | `1` (last silently wins) | **no** |

Instrument §6 makes the trend log F1's evidence, and §5's discipline is *"counts are computed from the rows, never trusted from prose."* The row that F1 is answered from can still be computed against a file that is roster-shaped and nothing else — and the all-`Not met` case is the **under**-counting direction, which suppresses new findings rather than inflating them. `[Observed]` **No instrument sentence overclaims what `--prior` does** — the validator docstring is silent on it and D-5 is accurate; the overclaim lives in the register (RD38-05).

*Requires:* a **validator change** (run the prior through the same LG-1/LG-2/LG-3/LG-6 checks, or at minimum the closed verdict vocabulary and duplicate-row detection the register already claims) **or** an instrument sentence stating that `--prior` trusts its input's verdicts. **No instrument amendment as written; not offer-blocking.**

### RD38-07 — MINOR — the LG-13 marker vocabulary is brittle in the false-rejection direction, and `_decl` compares occurrences on one normalization and returns another

Two measured effects of D-2's positive test.

`[Observed]` **Eleven honest emptiness wordings are newly rejected**, each with an error message asserting the record *"enumerates"* a value that enumerates nothing. Cross-version, beside `E3 | Met` under `READY FOR <verbatim target>`: `n/a`, `nil`, `nothing`, `unknown`, `TBD`, `(none known)`, `-- none --`, `0` — all **v1.9 = 0 errors, v1.10 = 2 errors**; and by direct execution `**empty**`, `` `empty` ``, `(empty)`, `_empty_`, `empty;`, `none identified (see G1)`, `none-identified` also reject. §5's slot is `<empty | enumerated items>` and publishes no vocabulary (RD38-02), so a reviewer has no way to learn from the instrument which three strings are lawful. The tightening direction is the safe one and the failure is loud — but the message is wrong about what the record says, and a record rejected for writing `n/a` is a record the instrument does not condemn.

`[Observed]` **`_decl` compares on `_norm_ws` and returns the raw value.** A record whose `E3 reopen-list:` appears twice as `none identified` and `none  identified` (one extra internal space) produces **no disagreement error** — the two normalize equal — and then **2 LG-13 errors** reading *"enumerates 'none  identified'"*, because `_E3_EMPTY_RE` is whitespace-sensitive. One value, declared agreeing by one normalization and non-empty by another. I confirmed this is the only merge class: `_norm_ws` collapses whitespace runs and strips, `.` never matches `\n`, so no cross-line or semantic merge is possible (9 pairs tested) — the exposure is exactly LG-13's whitespace sensitivity.

*Requires:* a **validator change** — apply `_norm_ws` to what `_decl` returns as well as to what it compares, and either widen the marker set or reword the error so it does not assert an enumeration that is not there — and, if the vocabulary is to be grounded rather than validator-local, the instrument sentence in RD38-02. **Not offer-blocking on its own.**

---

## 6. What passes

`[Observed]` These are executions and sweeps run this session, not inferences:

- **All six RD-37 findings are present in the v1.10 bytes; none is absent.** Three closed outright, three closed for the demonstrated case. Every one verified by rebuilding RD-37's own records and running the clone's validator with git checks ON against the real commit `34cbe5e` and the real committed instrument and §8 digests.
- **RD37-01 is genuinely and completely closed, and the regression is measurably reversed.** RD-37's four attack records each produce **2 LG-13 errors, both branches**; the same records score **0 at v1.9**. Ten lawful marker forms accept, including `none identified` beside `E3 | Met`. The unfilled template slot rejects. `fullmatch` makes it structurally impossible for any enumeration to pass as a marker — 20 forms attacked.
- **`_names_nothing` now has one polarity.** Two consumers, LG-9 and LG-12, both treating "names nothing" as the error; RD36-04's negation rule intact — all four negation-phrased findings lines still reject, and the real finding line still passes.
- **The `_decl` disagreement rule reaches every declared label, in both orders.** 10 labels × 2 orders = **20 of 20 executions error**; agreeing duplicates do not reject on any field tested.
- **All five v1.10 repairs are mutation-proven, by me, this session.** Reverting LG-13 → `86 fixtures, 3 failing`, exactly the three RD37-01 fixtures. Reverting the E3 field to `re.search` → `2 failing`. Reverting the Unknowns field → `2 failing`. Reverting LG-4's anchor → `1 failing`. Disabling the prior roster guard → `1 failing`. `86 fixtures, 0 failing, exit 0` on the unmutated clone.
- **Every check is fixtured.** Denominator **13**; LG-1…LG-13 each fire at least once, computed mechanically by intercepting `validate()`. 85 record validations + 1 source scan = the printed 86, and the delta's 74 → 86 arithmetic reconciles exactly.
- **The SDR guard's anchoring works, and the delta's honest cap is true.** My own sweep of the decisions home at `34cbe5e`, denominator **18 files**, finds **SDR-1…SDR-33, gapless** (all 33 tokens in `SURFACE-DECISION-RECORD.md`), confirming the substring direction is unfixturable against the real corpus; the anchoring is proven instead against a synthetic gapped corpus, where it closes **four** v1.9 false accepts. The pathspec exclusion executes correctly at **four** older commits.
- **The §4 conjunct battery, the row parser, the terminal-line rule, the trend row and the §8 extractor survived every attack I made.** Eight terminal-verdict forms; the trend row was **9 columns in every case**; `param_block_bytes` extracts 6610 bytes containing no `## 9` at three different commits with an identical digest.
- **"What did not change" is accurate to the byte on every claim about the instrument and the frozen records.** Per-section sha256 against `git show 95a41ea:` — §1–§8 all **byte-identical** (denominator 10 sections), §8 for the sixth consecutive amendment; only the `effective_version:` line and the appended §9 v1.10 entry move; **48** diff lines total; **no** correction marker inside the §9 v1.9 entry. The six frozen deltas and the four prior frozen raw reviews are byte-identical to their state at `95a41ea`.
- **The batch newly accepts nothing.** 28 cross-version comparisons against the v1.9 validator running at its own commit with its own digests: **zero cases where v1.9 errored and v1.10 did not.** The agreeing-duplicate case accepts at both versions, exactly as D-3 discloses.
- **P-34 is coherent at v1.10** — question, dated offer-status naming RD-38, option (a)'s seven-delta list with all four correction pointers ahead of the claims they correct, option (b)'s v1.11 ordering, the 86-fixture recommendation, and the v1.10 approval block. `PENDING-OWNER-DECISIONS.md:188` and `PROJECT-STATUS.md:131–163` agree with it.
- **No routed artifact names a stale instrument version.** Denominator **354** files; **81** hits across **24** files, all read and classified; RD34-05's version-neutral repair holds at both repaired sites.
- **`check_governance.py` in the clone: 30 OK, 18 WARN, 0 FAIL (48 checks); `--selftest`: 121 fixtures, 0 failing.**
- **The clone stayed byte-clean.** `git status --porcelain` empty at open and close; HEAD `34cbe5e2…`; instrument `3cb0814e…` and validator `f24e95d4…` unchanged at close, each confirmed by two independent methods.

---

## 7. Overall assessment — may v1.10 be offered to the owner at P-34, and may the formal administration run on this validator?

This is the best repair batch of the chain on its own terms. RD-37 asked for uniformity of application, and the batch delivered it where it counted most: `_names_nothing` was split rather than patched, LG-13 got a positive test that widening a placebo predicate can never loosen again, the disagreement rule reaches all ten declared labels in both orders, the roster now guards both sides of the trend comparison, and five repairs — not four — survive mutation, each failing exactly the fixtures it added. The regression RD-37 measured is measurably reversed: four records that validated clean at v1.9 now produce two errors each. §1–§8 are byte-identical for the fourth amendment running and §8 for the sixth, and I found nothing in the normative question text — the fourth administration in a row to look and find nothing there.

And yet the class survived, in the shape RD-37 named and one consumer further out. RD-37's rule was *"when a predicate or a parsing rule is repaired, it is repaired for every consumer and every field."* The batch applied it to the predicates and parsing rules **it changed**. It did not apply it to the rules it **inherited**: RD36-02's line anchoring did not travel to the three fields RD37-06 newly brought under `_decl`; RD33-02's row normalization still stops at the prior side's verdict vocabulary; and the record-versus-quotation distinction — which `_decl` now enforces perfectly for every *value* — reaches none of the nine *presence* tests. That last one is not a theoretical residual. A record that deletes its completeness critic and six of the eight fields §5 declares, quotes the instrument's own template in an appendix, and reads `READY FOR <the verbatim launch target>` validates with **zero errors** and prints a nine-column trend row. So the diagnosis moves again, by one word: the discipline is uniformity of application **to every rule the code carries, not to every rule the batch touched**.

So, on the two questions asked:

- **May v1.10 be offered at P-34?** **No.** The mechanism, ordering, options, precondition, seven-delta list and correction pointers are all right; the delta's byte claims are true where I could check them, and the both-directions acceptance claim survives 28 cross-version executions. But the instrument's own §9 v1.10 entry — the bytes an approval digest binds — tells the owner that the new marker vocabulary is what *"§5's own slot names"*, and §5's slot names one of the three markers while `none identified` appears nowhere else in the instrument. The delta's D-2 states the same thing in its first bullet and refutes it in its last paragraph. This is the batch's one new semantic rule, on the check the validator itself calls the sharpest single gate, and it is attributed to a clause that does not carry it. One further sentence, in the record the owner reads under option (a), tells him a lawful v1.9 record remains lawful at v1.10, and I have measured lawful records newly rejected — with an error message that misstates what the record declares. Unlike RD-37's block, **this one moves instrument bytes**: the §9 correction requires an amendment, so v1.10's digest is not the digest that should be approved. The cost is still small — one sentence, one delta paragraph, one register row.
- **May the formal administration run on this validator?** **No.** A record missing G1, the non-authority banner, the fresh-context disclosure, the model-family disclosure, the materials list and the falsification notes validates clean under `READY FOR <the verbatim launch target>` if it quotes §5's template — seven checks turned into no-ops by one appendix, on a record §4 says *"cannot support a gate decision."* Beneath that: the New-findings column F1 is answered from can still be computed against a bare row block, or driven to zero by a fabricated roster-complete prior, and administration 1 is the row every later F1 verdict is read against.

Two things to say plainly, against the chain's trend and for it. First, the direction of failure has changed. RD-34 through RD-37 each found a record the instrument condemns validating clean **because a repair had just created the hole**. Nothing in this batch created a hole: every one of my 28 cross-version cases moved toward rejection or stayed put, and the two live gate defects I found (RD38-01, RD38-06) are **survivors that v1.9 accepted too**. What this batch produced instead is over-rejection and two false sentences — a different and much cheaper failure mode. Second, and unlike my five predecessors, I can say that the structural rule RD-37 named is **correct and was correctly implemented where it was applied** — the three repairs that carry it are the only three in the chain I could not break. The chain's remaining defects are not evidence that the rule is wrong; they are the rule's unfinished application to the code the batch inherited rather than wrote. I decline, like RD-35, RD-36 and RD-37, to predict that the v1.11 batch is the last — but I will say that the enumerable work is now enumerable: sixteen predicates and parsing rules, ten of which already satisfy the standard, and six named above that do not.

VERDICT: REVISE