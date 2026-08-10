# RD-36 — Launch-gate instrument re-review, v1.8 exact bytes (round-2026-08e, frozen commit b00c3dd)

- Review id: RD-36 (fourth administration of the instrument re-review chain: RD-33 → v1.6, RD-34 → v1.7, RD-35 → v1.8)
- Date: 2026-08-10
- Subject: `launch-gate-pre-specifications.md` (v1.8, repo root), `scripts/launch_gate_results.py`, `round-2026-08e/LAUNCH-GATE-v1.8-SEMANTIC-DELTA.md`, `decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` (P-34), the RD-35 section and the corrected RD34-02 row of `reviews/DISPOSITION-REGISTER.md`
- Subject sha256, computed this session by two independent methods — `sha256sum` and Python `hashlib` over the file bytes: `49b0b5e5ad70d1eb6c1c0b78976ff4bf1d786e95d4c900bfd5a518636f868a51`
- Validator sha256: `2415dcf3aa3c3479976a113dc9fb7f2fbccee9a21c635e66f128c0042cadc65c` (1175 lines)
- §8 parameter block, extracted by the validator's own `param_block_bytes`: `01209c0f052971f794e1f35827a002aa8d80420aad471d10fde000abb6366ff6` — **byte-identical to RD-35's v1.7, RD-34's v1.6 and RD-33's v1.5 measurements**; §8 has now not moved across four amendments
- Frozen clone `…/scratchpad/clone-08e-r15`: `git rev-parse HEAD` = `b00c3dd5542250a9999a1726ccaa90b9793be6cd`, `git status --porcelain` **empty at open and at close**; both subject digests re-verified unchanged at close. Every synthetic record and every mutated validator copy was written to `…/scratchpad/rd36/`, never into the clone
- Reviewer: isolated fresh-context session, Claude family. Same-family re-review — F5's own example applies to me
- Authoring context: none. I authored no byte under review

---

## 1. Method and what I ran

`[Observed]` Read in charter order: `AGENTS.md`, `RD-35-instrument-v17-RAW.md` (201 lines, 7 findings, `VERDICT: REVISE`) in full, the RD-35 section and the corrected RD34-02 row of `DISPOSITION-REGISTER.md`, the v1.8 delta (153 lines), the validator in full (1175 lines), instrument §4 and §5 in full, P-34 (159 lines), `PROJECT-STATUS.md` L118–140, `PENDING-OWNER-DECISIONS.md` P-34, `LAUNCH-CLOSURE-PREFLIGHT.md` L1–40.

`[Observed]` `python3 scripts/launch_gate_results.py --selftest` in the clone → **64 fixtures, 0 failing, exit 0**. Full roll printed and read.

`[Observed]` I built a record generator matching §5's template field-for-field in §5's order (39 roster rows) and ran **the clone's own validator**, imported so `REPO` resolves to the clone, with git checks **ON** against the real commit `b00c3dd`, the real committed instrument digest `49b0b5e5…`, the real §8 digest `01209c0f…`, and the real `effective_version: v1.8` — so LG-1/LG-2/LG-11 and the citation-existence path all actually executed on every case below. Roughly 90 synthetic records, cited as R1, N1–N5, and the per-finding matrices.

`[Observed]` **Mutation-revert testing (verification rule 6), on a copy outside the clone** with the clone's `.git` symlinked so git-on fixtures still run. Four repairs reverted one at a time; in each case the selftest went from 0 failing to failing exactly the fixture(s) that repair added. Recorded in §2.

`[Observed]` Fixture→check coverage computed mechanically this session by intercepting `validate()` and binding each emitted error to its `LG-n` prefix over the whole selftest run. Denominator **13** checks; `validate()` invoked **64** times, matching the printed count.

`[Observed]` Repo-wide sweeps with Python `re`, never shell grep (rule 1). Denominator **348** text files (`.md/.py/.yaml/.yml/.txt`, excluding `.git`/`_bootstrap`).

`[Unknown]` I did not run `check_governance.py`, did not administer the gate, and read no pilot record content. All answer sets below are synthetic.

---

## 2. Per-finding repair verification — all seven RD-35 findings

| RD-35 | Class | Disp. | Status | Anchor / proof in the v1.8 bytes |
|---|---|---|---|---|
| RD35-01 | BLOCKING | R | **verified-closed by execution and by mutation** | Validator:209 now reads `path = v[2:] if v.startswith("./") else v` — a prefix strip; `lstrip` is gone from the file (Python `re` sweep, 0 hits). Executed at `b00c3dd`, git on, inside a full `READY-WITH-DEFERRALS` record: `.syzygy/governance/decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` → **0 errors, ACCEPTED**; `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` → **ACCEPTED**; `./scripts/launch_gate_results.py` → **ACCEPTED** (the `./` limb works); `.syzygy/governance/decisions/NO-SUCH-DECISION.md` → **REJECTED**, *"path … does not exist at the named commit"*. **Mutation 1**: re-applying `v.lstrip("./")` to a copy → selftest `64 fixtures, 1 failing`, failing exactly *"existing repository path as deferral citation ACCEPTED at the named commit (RD35-01)"*. The fixture sees the bug it exists to prevent; the untested-passing-direction blind spot rule 6 exists to close is closed for this check. |
| RD35-02 | MAJOR | R | **verified-closed by execution and by mutation, both directions** | Validator:463–483: `_gv_lines = [ln for ln in txt.splitlines() if "GATE VERDICT:" in ln]`, `mg = GATE_VERDICT_RE.search(_gv_lines[-1])`. **H6-reverse rebuilt** (summary `GATE VERDICT: READY FOR <verbatim target>` above, terminal `GATE VERDICT: NOT READY — pending the owner's F2 deferral decision`, all rows Met, git on): now **1 error**, *"the terminal `GATE VERDICT:` line … does not parse to the closed verdict set … a qualified or quoted verdict is not a verdict"*, and the trend row's gate column is `—`, not a pass. **Quoted-§5-template appendix rebuilt**: **1 error**, *"the terminal verdict contains '|' — it would corrupt the nine-column trend row"*; **trend row is 9 columns, not 11**. A quoted terminal verdict (`GATE VERDICT: "READY FOR …"`) also errors. **Mutation 2** (v1.7 `finditer[-1]` anchoring restored) → `1 failing`. |
| RD35-03 | MAJOR | R | **verified-closed by execution and by mutation** | Validator:504–518. git on, header `Launch target:` correct, all rows Met, denominator 7 verdict tails: `Capability 1 — Project registration and honest shape visibility` **CLEAN**; the same with a trailing period **CLEAN**; the whole normalized `LAUNCH_TARGET` scalar **CLEAN**; `Capability 1` (RD-35's own fragment, which the header line already rejected) **REJECTED**; `Capability 7 — full Mission Control and mission prevention` **REJECTED**; `anything the reviewer likes` **REJECTED**; `the whole system` **REJECTED**. One placeholder, one standard — the sibling asymmetry RD-35 named is gone. **Mutation 4** (check disabled) → `1 failing`. |
| RD35-04 | MAJOR | R | **verified-closed by execution and by mutation** | New LG-13, validator:576–597. git on, full 39-row template: three enumerated reopen items beside `E3 \| Met` **and** `READY FOR` → **2 errors** (*"E3's own fail condition"* and *"'ready' is then false regardless of every other verdict"*); the same beside `E3 \| Met` under `NOT READY` → 1 error; deleted `E3 reopen-list:` field → *"absence reads as empty, and absence is never a pass"*. The lawful control — non-empty list beside `E3 \| Not met`, `NOT READY` — is **0 errors**, so the check is closed without being made unusable. **Mutation 3** (LG-13 removed) → `2 failing`. |
| RD35-05 | MINOR | R | **substantially closed; residual — RD36-04** | `_names_nothing()` at validator:233–237, shared by LG-9 and LG-13. Rebuilt H1, git on, scoped `C2` + `READY FOR`, denominator **26** strings: **22 rejected**, including **all 18 of RD-35's own set** — the ten already rejected at v1.7 plus the eight residuals `unknown`, `tba`, `n.a.`, `see above`, `various`, `several`, `(none known)`, `-- none --`, and I added `nil`, `nothing`, `none.`, `[none]`. A real finding line (`RFC-0010 mission-profile drift (Wave D1)`) passes. **4 accepted** — see RD36-04. |
| RD35-06 | MINOR | R | **closed on the P-n/D-n limb; the replacement family is wrong — RD36-01** | `DECISION_ID_RE` narrowed from `(?:SDR\|P\|D\|B)-\d+…` to `(?:SDR\|B)-\d+…` (both bytes read at `eb53c3e` and at HEAD). git on, `READY-WITH-DEFERRALS`, count 1: `P-34` **REJECTED** with *"names the pending-decision queue (P-n) or a semantic-delta item (D-n) — a deferral is granted only by a made decision"*; `D-10` **REJECTED** likewise; `SDR-33` **ACCEPTED**; `B-1` **ACCEPTED**. The reason string names the pending queue as commissioned. But `B-n` names no decision in this repository — RD36-01. Existence is still unchecked for identifiers — RD36-06. |
| RD35-07 | MINOR | R | **closed for the seven fields named; the eighth is unenforced — RD36-05** | New LG-12, validator:550–574. git on, deleting each in turn from a clean-validating record: the non-authority banner → error; `Reviewer model family:` → error; `Materials given:` → error; `Operationalization notes:` → error; `E3 reopen-list:` → error; `Unknowns and what would settle them:` → error; `Reviewer's falsification notes:` → error. **Seven of seven.** `Deferred count`/`Reopened count` deletions still error under LG-5. Six `Unknown` A-rows beside `Unknowns … : TBD` → *"§4 requires every Unknown to carry what evidence would settle it"*. §5's eighth declared field, `Reviewer: … fresh context: yes/no`, deletes with **0 errors** — RD36-05. |

**Tally, with its denominator:** of RD-35's **7** findings, **7 are present in the v1.8 bytes and none is absent**; **5 are closed outright** (RD35-01, -02, -03, -04, -07-for-its-seven); **2 (RD35-05, RD35-06) are closed for the case RD-35 demonstrated and leave a residual one level up.** All four decisive repairs were additionally **mutation-proven** by reverting them on a copy and observing the selftest fail on exactly the fixture that repair added. `[Inferred]` The repair session did the work the register describes, and — with the RD36-01 exception — its records are honest about what it did.

---

## 3. Verification of the delta's and the records' claims

`[Observed]` **"§1–§8 byte-unchanged from v1.7."** True. Per-section sha256 with a fence-aware splitter, `git show eb53c3e:launch-gate-pre-specifications.md` vs HEAD: §1 `af875539…`, §2 `28c745f6…`, §3 `4143073e…`, §4 `7952a130…`, §5 `aa7a227c…`, §6 `5884c5ae…`, §7 `bdc18cf9…`, §8 `4ff1b986…` — **all eight identical**. Only `HEADER` and `S9` differ. The full `git diff` of the instrument is `-effective_version: v1.7` / `+effective_version: v1.8` plus one appended §9 changelog entry (33 lines). **Zero question blocks changed; no ID renumbered.** The delta's "a narrower footprint than any amendment in this chain" is true of the bytes.

`[Observed]` **The frozen records were not edited.** v1.4 delta `3c52291a…`, v1.5 `1aa8bf50…`, v1.6 `67820bb2…`, v1.7 `5d6b775a…` — all four byte-identical to their state at `eb53c3e`. The D-2 correction travels in the v1.8 delta's D-1, in the D-10 convention, as claimed.

`[Observed]` **The D-1 correction's claims are true-at-v1.8 and false-at-v1.7.** At `eb53c3e` the validator line reads `if git_show(commit, v.lstrip("./")) is None:` — the character-class strip, confirmed in the committed bytes. The v1.7 selftest's only two path-form citation literals were `.syzygy/governance/decisions/SDR-99-EXAMPLE.md` (git **off**) and `…/NO-SUCH-DECISION.md` (git on, rejected): **no accepting-path fixture existed**, denominator 43 (41 `case(` invocations + 2 bespoke trend checks). At v1.8 the accepting literal `…/LAUNCH-GATE-AUTHORITY-DECISION.md` is present (62 `case(` + 2 = **64**, matching the printed count, the delta's "64 fixtures", and P-34's "64 in all").

`[Observed]` **The dated correction on the RD34-02 register row** (`DISPOSITION-REGISTER.md:297`) is present, dated `2026-08-10`, attributed to RD35-01, states both corrected claims, and states that both are true of the v1.8 bytes — each of which I verified independently above. It also records that this is the second dated correction on this check's trail. Accurate. One residual: RD36-07.

`[Observed]` **P-34 is coherent at v1.8.** The question names **v1.8** (L11); the offer-status block is dated 2026-08-10, states *"not yet offerable"*, summarizes RD-35's BLOCKING finding correctly, and names **RD-36** as the precondition (L25); option (a) lists all five deltas with the v1.5→D-10 and v1.7→D-1 pointers **before** the claims they correct; option (b) carries the v1.9 ordering (amendments into the working tree before step 2's digest, RD33-11) and prices the F5-promotion honestly; the recommendation's fixture count is **64**, matching; the approval block (L129) names **v1.8**. `PENDING-OWNER-DECISIONS.md:185` and `PROJECT-STATUS.md:129` both name v1.8 and describe the chain accurately.

`[Observed]` **Stale-version sweep, denominator stated.** 348 files scanned; **61** lines carry both a launch-gate token and a `v1.x` token, across **20** files; all 61 read and classified. Every hit is a delta filename or title, a §9 changelog back-reference, a frozen review, a historical disposition row, the v1.3 pilot (`PROJECT-STATUS.md:125`, immediately followed by *"The instrument is now **v1.8**"*; `LAUNCH-CLOSURE-PREFLIGHT.md:35`, under its explicit *"Historical snapshot — non-authoritative round record"* banner at L3–8), or the current v1.8. **RD34-05's version-neutral repair holds**: `DEFERRED-WAVE-POSTURE.md:41` and `FIRST-OPENSPEC-SEQUENCE.md:70` carry no version word and no longer appear in the hit set at all. **No routed artifact names a stale instrument version.**

`[Observed]` **Fixture→check coverage, denominator 13.** Emissions across the 64-fixture run: LG-1 (3), LG-2 (11), LG-3 (4), LG-4 (2), LG-5 (3), LG-6 (11), LG-7 (17), LG-8 (3), LG-9 (5), LG-10 (7), LG-11 (5), LG-12 (8), LG-13 (3). **All thirteen checks are made to fire by at least one fixture; none is absent.** The two new checks (LG-12, LG-13) are both fixtured, and LG-13 is mutation-proven.

---

## 4. New findings

### RD36-01 — MAJOR — `B-n` is accepted as a citation family that "names made decisions", and in this repository it is a *review-finding numbering scheme*; the §9 changelog, the offered delta, the docstring and a fixture all assert otherwise

Validator:187 (defined bytes, quoted): `DECISION_ID_RE = re.compile(r"(?:SDR|B)-\d+[a-z]?(?:\([a-z]\))?$")`, under the comment *"only families that name MADE decisions may claim a granted deferral."*

`[Observed]` Repo-wide sweep with Python `re`, denominator **348** files: the token `B-n` occurs as `B-1`…`B-7` and **every single occurrence outside the validator and RD-35's own quotation of it is a review finding number** — `round-2026-08c/reviews/RD-2-human-clarity-RAW.md` (`### B-1.`, `### B-2.` … `### B-6.`), `RD-3-vocabulary-RAW.md` (`### B-1 — Missing from core…`), `HUMAN-CLARITY-CLOSURE-REPORT.md`, `PROJECT-SHAPE-FACETS-BRIEF.md`, `PUBLIC-VOCABULARY-COMPREHENSION-REPORT.md`. `[Observed]` **Zero `B-n` tokens appear anywhere in `.syzygy/governance/decisions/`** (denominator: every `.md` under that tree). `[Observed]` No numbered warrant identifier family exists either — sweeping `decisions/` for `W-n`/`WARRANT-n` returns nothing; `AGENTS.md:21` names the families as *"SDR-1…33, warrants, pending queue"*, and the SDR population is exactly **SDR-1…33** (33 identifiers).

`[Observed]` Executed at `b00c3dd`, git on, real digests, full 39-row §5 template, `Deferred count: 1`, `GATE VERDICT: READY-WITH-DEFERRALS (owner only)`, `Owner deferral decision: B-1`:

```
errors: 0
trend : | 2026-08-10 | b00c3dd5 | 1 | 0 | 0 | 1 | 0 | n/a — no prior record supplied | READY-WITH-DEFERRALS (owner only) |
```

**A pass verdict resting on a deferral granted by RD-2's first human-clarity review finding validates clean and enters the trend log.** `B-7`, `B-999` likewise. This is §4's own condition — *"A deferral is claimed only by **citation**: the record's `Owner deferral decision:` field names the owner decision (path or identifier) **that granted it**"* — satisfied by a thing that granted nothing, which is the exact defect RD34-02 and RD35-06 were both raised for.

`[Observed]` Four artifacts assert the contrary, one of them an **instrument byte the owner's approval would bind**:

- `launch-gate-pre-specifications.md` §9, the v1.8 changelog entry (quoted): *"the deferral-identifier families narrow to made decisions — SDR-n/B-n; P-n (the pending queue) and D-n (delta items) grant nothing (RD35-06)"*.
- v1.8 delta D-6 (quoted): *"The identifier form now accepts `SDR-n`/`B-n` (made decisions)"*.
- Validator docstring LG-7 (quoted): *"an identifier of a MADE decision (SDR-n/B-n shape)"*.
- Selftest fixture label (quoted): *"B-n (made owner decision) as deferral citation accepted (RD35-06)"* — the fixture set positively certifies the wrong taxonomy, so it cannot see this.

`[Observed]` The disposition register disagrees with the bytes in a *different* direction: its RD35-06 row (quoted) says the form narrows to *"(`SDR-n` and warrant identifiers)"* — naming a family the validator does not implement and omitting the one it does.

`[Inferred]` RD-35's direction was *"restrict the identifier form to families that name made decisions (`SDR-n`, warrant identifiers)"*. The repair dropped `P` and `D` — the two RD-35 demonstrated — and retained `B`, which RD-35 had listed among the accepted-shape-only values (`B-7`) without adjudicating it. This is the chain's established shape a fifth time: the demonstrated instances are closed and the class survives in the limb the predecessor did not name.

*Requires:* a **validator change** (drop `B` from `DECISION_ID_RE`, or replace it with the actual warrant family if one is minted), a **fixture change** (the accepting `B-1` fixture must be replaced — an accepting fixture asserting a false taxonomy is worse than none), an **instrument amendment** (the §9 changelog sentence — §1–§8 untouched, so the v1.9 footprint stays as narrow as v1.8's), and **record corrections** to D-6, the docstring, and the register's RD35-06 row. **This blocks the P-34 offer**, because the false description sits in the instrument's own §9 bytes and in the delta the owner reads under option (a).

### RD36-02 — MAJOR — §5's field values are parsed with a newline-crossing `\s*`, so a field written with an *empty* value silently takes the next line's text as its answer; two checks are defeated under `READY FOR`

Five field regexes share the shape `^<Field>:\s*(\S.*)$` (or `(.+)$`) with `re.M`. `\s` matches `\n`, so when the field carries no value the engine consumes the newline and captures the **following line**.

`[Observed]` Executed at `b00c3dd`, git on, real digests, full 39-row template. Limb (a) — LG-9:

- one scoped row (`| C2 | Not met (out of launch scope) |`), `Deferred-wave findings recorded outside launch scope:` written with **no value**, `GATE VERDICT: READY FOR <verbatim target>` → **0 errors, `record valid`**, trend row `| … | 0 | 1 | 0 | 0 | 0 | … | READY FOR Capability 1 — … |`.
- The captured value was `'Deferred count (owner-deferred findings this administration): 0'` — the next field's own line.
- Control with the value `none` → correctly **rejected** by LG-9.
- Control with the line **deleted entirely** → correctly **rejected**: *"1 scoped row(s) but no deferred-wave findings line."*

The asymmetry is inside one check: **absence errors, emptiness passes.** §4 (defined clause, quoted): *"a record with any scoped row whose deferred-wave findings line names no defect asserts a scoped defect exists and that none exists — a validation error (LG-9), never a lawful record."* This record names no defect and is not an error.

`[Observed]` Limb (b) — LG-12's Unknown-settling check: six `Unknown` A-rows, `Unknowns and what would settle them:` written with **no value**, `READY FOR <verbatim target>` → **0 errors**, trend row Unknown column `6`. Captured value: `"Reviewer's falsification notes: tried to break the roster; couldn't"`. Control with `TBD` → correctly rejected. §4's *"every Unknown must carry what evidence would settle it"* is defeated by one newline.

`[Observed]` No fixture can see either: every LG-9 and LG-12 fixture supplies a non-empty value. Denominator 64, full roll read. This is verification rule 6's untested direction again — the same blind spot RD35-01 was, in the checks built to close RD35-05 and RD35-07.

`[Observed]` The same spill affects `Launch target:`, `Owner deferral decision:` and `E3 reopen-list:`, but there it fails **loudly** (a mismatch, a bad citation, or a spurious LG-13 error), so those limbs are conservative.

*Requires:* a **validator change** — anchor each field's value with `[^\S\n]*` (or `re.match` per line) so a blank field is absent rather than borrowed — plus a fixture per limb, in **both** directions. No instrument amendment; §4 and §5 already state the rule. **Blocks the formal administration**; does not block the offer, since no owner-facing record claims otherwise.

### RD36-03 — MINOR — `re.search` takes the *first* match, so a narrative line can shadow a declared §5 field; a nonzero `Deferred count:` becomes 0 in the trend row

`[Observed]` git on, real digests: a record whose real field reads `Deferred count (owner-deferred findings this administration): 3`, with **no** `Owner deferral decision:` citation and `GATE VERDICT: READY FOR <verbatim target>`, preceded anywhere earlier by a line `Deferred count summary for the reader: 0` → **0 errors**, and the trend row's Deferred column prints **0**. Three checks are bypassed at once: LG-5's declared-figure honesty, LG-7's *"required under ANY verdict"* (RD34-07), and §4's *"plain `READY FOR <LAUNCH_TARGET>` over any deferral, or over a nonzero `Deferred count:`, is a contradiction and a validation error."* Same root cause as RD36-02 and the same one-line repair family. *Requires:* a validator change; no instrument amendment.

### RD36-04 — MINOR — the names-nothing lexicon narrows the class but does not remove it, and it introduces a symmetric false-rejection on the new LG-13

`[Observed]` Denominator **26** findings-line strings, scoped `C2` + `READY FOR`, git on: **22 rejected** (including all 18 of RD-35's set), **4 accepted** — `no defects found`, `none identified`, `nothing of note`, `no findings in the deferred waves`. Each says exactly what `none` says, using one contentful noun. The lexicon is still an enumeration; it enumerates tokens instead of strings.

`[Observed]` The mirror image, on the check the same rule now drives: `E3 reopen-list: none identified` beside `E3 | Met` → **error**, *"a non-empty reopen-list is E3's own fail condition."* A lawful record — an empty reopen list, phrased naturally — is rejected. Loud, so not dangerous, but LG-13's correctness now depends on the reviewer choosing a word from a lexicon the instrument never publishes.

`[Inferred]` The delta's D-5 (quoted) — *"No fourth enumeration extension; the residual class is removed rather than chased"* — is defensible if "the residual class" means the eight strings RD-35 named, which are genuinely removed; it is not true if read as a claim that LG-9 is now complete. I do not call it a false claim; I do call it an invitation to the wrong reading, and it belongs in the same correction pass. *Requires:* a validator change (a minimum-information rule that is not token-set membership, or an instrument sentence publishing the empty-marker vocabulary §5's `<empty | enumerated items>` presupposes) plus a one-sentence record correction to D-5.

### RD36-05 — MINOR — §5's eighth declared field, the fresh-context disclosure, is the one LG-12 does not check

§5 (template, quoted): `Reviewer: <model/version or human, fresh context: yes/no>`.

`[Observed]` git on: deleting the `Reviewer:` line from a clean-validating record → **0 errors**. Its seven siblings all now error. `[Inferred]` The tool's scope note discloses *"fresh context, family disclosure, full administration"* as non-mechanical — but the same sentence covers `Reviewer model family:`, which LG-12 **does** presence-test, and "full administration" is now mechanically bound by LG-10's roster. The note does not consistently excuse the omission; RD35-07's repair closed the seven fields RD-35 enumerated and left the eighth. `[Observed]` Relatedly, presence tests are content-blind by design: `Reviewer model family: TBD` validates clean, and deleting the non-authority banner while quoting its phrase inside the falsification notes validates clean (the check is `token not in txt` over the whole record). *Requires:* a validator change; no instrument amendment.

### RD36-06 — MINOR — identifier citations are still never existence-checked, and a bare directory path is accepted

`[Observed]` git on, `READY-WITH-DEFERRALS`, count 1: `SDR-9999` **ACCEPTED** (the SDR population is SDR-1…33; 9999 names nothing), `B-999` **ACCEPTED**, and the bare directory `.syzygy/governance/decisions/` **ACCEPTED** (`git show <commit>:<dir>` returns a tree with exit 0). The path form is existence-verified; the identifier form is a shape test only. RD-35 offered two directions for RD35-06 — narrow the families, or resolve identifiers against `C7_POPULATION` — and the batch took the first; nothing overclaims, since the docstring says *"shape"*. Recorded as the disclosed residual, and as the reason RD36-01 costs what it costs: the identifier form is now the only citation form with no existence guard behind it. *Requires:* a validator change if taken; no instrument amendment; not offer-blocking on its own.

### RD36-07 — MINOR — three record inaccuracies in the disposition register, one of them in a row this batch edited

`[Observed]` `DISPOSITION-REGISTER.md:297`, the RD34-02 row, was edited this batch to carry the dated RD35-01 correction — and its third stale claim was left standing: it still describes the citation shape test as *"a decision identifier (`SDR-n`/`P-n`/`D-n` shape)"*, which the **same v1.8 batch** made false (RD35-06 rejects `P-n` and `D-n`). Two claims in one row were corrected; a third that went stale in the same commit was not. `[Observed]` The RD35-06 row states the accepted set as *"(`SDR-n` and warrant identifiers)"* — the bytes implement `SDR-n` and `B-n` and no warrant form (see RD36-01). `[Observed]` The RD35-07 row enumerates six enforced fields and omits `Operationalization notes:`, which the validator does check — an under-statement, harmless in direction. *Requires:* record corrections only; the register is not in P-34's option (a) list, so not offer-blocking.

---

## 5. What passes

`[Observed]` These are executions and sweeps run this session, not inferences:

- **All seven RD-35 findings are present in the v1.8 bytes; none is absent.** Five closed outright, two closed for the demonstrated case. Every one confirmed by rebuilding RD-35's own records and running the clone's validator with git checks on against the real commit `b00c3dd` and the real committed instrument and §8 digests.
- **RD35-01, the BLOCKING finding, is genuinely closed, and its blind spot with it.** The prefix strip is in the bytes; the real `.syzygy/governance/decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` is **ACCEPTED** at the named commit inside a full lawful `READY-WITH-DEFERRALS` record, and `…/NO-SUCH-DECISION.md` is rejected. The path form of the citation is usable for the first time.
- **Four repairs are mutation-proven, by me, this session.** Reverting `lstrip`, the regex anchoring, LG-13, and the verdict-target test on copies outside the clone made the selftest fail on exactly 1, 1, 2 and 1 fixtures respectively — the fixtures those repairs added. `64 fixtures, 0 failing, exit 0` on the unmutated clone.
- **Every check is fixtured.** Denominator **13**. LG-1…LG-13 each fire at least once across the 64-fixture run (emission counts in §3), computed mechanically by intercepting `validate()`. `validate()` invocation count = 64 = the printed fixture count = the delta's figure = P-34's figure.
- **The §4 conjunct battery is closed on both pass branches.** Under `READY-WITH-DEFERRALS` with a lawful `SDR-33` citation and count 1: `E5` not Met, a plain `A1` Not met, `F3` not Met, `F4` not Met, `F1` Not met, and all 39 rows Not met were each **BLOCKED** on precisely the failing limb. The lawful H9 record (F2 `Not met`, cited, count 1, all else Met) is **0 errors**. `E1 | Met` over an `Unknown` sub-row is caught twice. `F5`/`F6` `Not met` under `READY FOR` passes — deliberate and disclosed by §4.
- **The terminal-line and verdict-target repairs hold in both directions.** The nine-column trend row survived every attack I made on it, including the `|`-carrying quoted-template appendix; bolded and trailing-whitespace verdict lines still parse correctly.
- **"What did not change" is accurate to the byte.** Per-section sha256 against `git show eb53c3e:` — §1–§8 all **byte-identical**; only the `effective_version:` header line and the appended §9 changelog entry move; zero question blocks changed. The four frozen prior deltas are byte-identical to their state at `eb53c3e`.
- **The D-1 correction and the dated RD34-02 register correction are honest.** Both claims they correct are verified false of the v1.7 bytes (`lstrip("./")` in the committed source; no accepting-path fixture among the 43 path literals) and true of the v1.8 bytes.
- **P-34 is coherent at v1.8** — question, dated offer-status naming RD-36, option (a)'s five-delta list with both correction pointers ahead of the claims, option (b)'s v1.9 ordering, the 64-fixture recommendation, and the v1.8 approval block.
- **No routed artifact names a stale instrument version.** Denominator **348** files; **61** hits across **20** files, all read and classified; RD34-05's version-neutral repair holds at both repaired sites.
- **The clone stayed byte-clean.** `git status --porcelain` empty at open and close; HEAD `b00c3dd5…`; instrument `49b0b5e5…` and validator `2415dcf3…` unchanged at close.

---

## 6. Overall assessment — may v1.8 be offered to the owner at P-34, and may the formal administration run on this validator?

The repair quality is the highest of the four batches. RD35-01 was not merely patched: the strip is correct, the passing direction is fixtured for the first time in this chain's history, and I proved by mutation that the fixture fails without the repair — the specific epistemic failure RD-35 diagnosed (*"a check that rejected its entire lawful input set read as green"*) has been closed as a **method**, not just as a line. RD35-02, -03 and -04 are closed in both directions with lawful controls that still pass. The instrument's footprint is the narrowest in the chain: §1–§8 byte-identical, zero question blocks touched, and I recomputed every clause of "what did not change" rather than taking it. The delta and P-34 tell the truth about all of that.

And RD-35's closing sentence — *"the instrument has converged while the validator has not"* — survives a fourth administration, in the same shape and for the same reason. Each repair closed the instance its predecessor demonstrated and left the class in the limb the predecessor had not named:

- RD35-06 dropped `P-n` and `D-n` because RD-35 demonstrated them, and kept `B-n`, which RD-35 had listed but not adjudicated — and `B-n` in this corpus is RD-2's review-finding numbering, so a `READY-WITH-DEFERRALS` pass can rest on a deferral granted by a review finding (**RD36-01**). That one is worse than a validator bug, because the §9 changelog — instrument bytes an approval digest would bind — and the offered delta both tell the owner the family names made decisions, and a fixture certifies it.
- RD35-07's presence checks landed for the seven fields RD-35 enumerated and not the eighth (**RD36-05**); RD35-05's lexicon removed the eight strings RD-35 listed and admits four of the same kind (**RD36-04**).
- And the two brand-new checks, LG-9's tightening and LG-12's Unknown-settling limb, are both defeated by a single newline: a §5 field written with an empty value silently borrows the next line as its answer, so a record with a scoped row and no named defect, and a record with six Unknown rows and no settling evidence, each validate clean under `READY FOR` with real digests (**RD36-02**). Deleting those lines errors correctly; leaving them blank does not. No fixture in the 64 supplies an empty value, so the fixture set is blind to it — rule 6's untested direction, one turn after the batch that closed rule 6's untested direction.

So, on the two questions asked:

- **May v1.8 be offered at P-34?** **No.** The mechanism, ordering, options, precondition and correction pointers are all right, and I found nothing wrong with §1–§8. But the instrument's own §9 changelog entry states that the accepted deferral-identifier families "name made decisions — SDR-n/B-n", and `B-n` names no decision anywhere in this repository (denominator 348 files; every instance is a round-2026-08c review finding). An owner approving v1.8 would bind a digest over that sentence, and the delta he reads under option (a) repeats it. That is RD-8's *"the finding that converts act 1 from a knowing act into a surprised one"* — the same test RD-35 applied to D-2, applied now to an instrument byte rather than a process record. The repair is small (one character class, one fixture, one changelog sentence, three record corrections) but it moves instrument bytes, so the packet re-freezes.
- **May the formal administration run on this validator?** **No.** A record §4 explicitly calls *"a validation error (LG-9), never a lawful record"* validates clean under `READY FOR`; §4's Unknown-settling requirement is defeated by the same newline; a declared `Deferred count: 3` can be shadowed to 0 in the trend row with no citation; and a pass can be granted by a citation to a review finding. Administration 1 is the row every later F1 verdict is read against, and each of those four would contaminate it.

Two things distinguish this REVISE from RD-35's. First, **the offer is blocked by one finding, not by a class**: RD36-01 is a single wrong character class with four honest records built on top of it, and RD36-02 through -07 are validator-and-record work that no owner-facing document misdescribes. Second, and worth stating plainly against the chain's trend: **the instrument's normative text has now gone two full amendments without a finding against it.** RD-35 found nothing in §1–§8 and neither did I. What keeps failing is the layer that measures, and it is failing in a stable, recognizable way — each pass closes the demonstrated instances and the next reviewer finds the class in whichever limb the previous reviewer happened not to name. Like RD-35, I decline to predict that the v1.9 batch is the last, and I will name the reason more precisely than the trend alone: **five of my seven findings are cases where a fixture exists, passes, and cannot see the defect, because the fixture set tests one direction of each predicate.** Until the fixture discipline changes — every predicate fixtured in both directions, and every §5 field fixtured absent, empty, and shadowed — a fifth administration will find a sixth class.

VERDICT: REVISE
