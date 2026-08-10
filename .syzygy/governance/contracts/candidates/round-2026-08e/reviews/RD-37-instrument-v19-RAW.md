The clone is byte-clean at open and close. Here is the review of record.

---

# RD-37 — Launch-gate instrument re-review, v1.9 exact bytes (round-2026-08e, frozen commit 95a41ea)

- Review id: RD-37 (fifth administration of the instrument re-review chain: RD-33 → v1.6, RD-34 → v1.7, RD-35 → v1.8, RD-36 → v1.9)
- Date: 2026-08-10
- Subject: `launch-gate-pre-specifications.md` (v1.9, repo root), `scripts/launch_gate_results.py`, `round-2026-08e/LAUNCH-GATE-v1.9-SEMANTIC-DELTA.md`, `decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` (P-34), the RD-36 section and the three dated RD36-07 corrections of `reviews/DISPOSITION-REGISTER.md`
- Subject sha256, computed this session by two independent methods — `sha256sum` and Python `hashlib` over the file bytes: `bc1363bffedb5d908c2345369ce44dbc3a286649c0e3ff18862b74e6d482b10d`
- Validator sha256: `8945bbe6e9b0e6f3bbdb89254552ffaa7b47c8e65d381cc115f08f7480609a3b` (1362 lines)
- §8 parameter block, extracted by the validator's own `param_block_bytes`: `01209c0f052971f794e1f35827a002aa8d80420aad471d10fde000abb6366ff6` — **byte-identical to RD-36's v1.8, RD-35's v1.7, RD-34's v1.6 and RD-33's v1.5 measurements**; §8 has now not moved across five amendments
- Frozen clone `…/scratchpad/clone-08e-r16`: `git rev-parse HEAD` = `95a41ea8eedd9c1237924b12eb81dacf1d53c914`, `git status --porcelain` **empty at open and at close**; both subject digests re-verified unchanged at close. Every synthetic record and every mutated validator copy was written to `…/scratchpad/rd37b/`, never into the clone. I did not read the terminated dispatch's scratch area
- Reviewer: isolated fresh-context session, Claude family. Same-family re-review — F5's own example applies to me
- Authoring context: none. I authored no byte under review

---

## 1. Method and what I ran

`[Observed]` Read in charter order: `AGENTS.md`, `RD-36-instrument-v18-RAW.md` (181 lines, 7 findings, `VERDICT: REVISE`) in full, the RD-36 register section and the three dated RD36-07 corrections, the v1.9 delta (136 lines), the validator in full (1362 lines), instrument §3's E3 clause, §4 and §5 in full, P-34 (172 lines), `PROJECT-STATUS.md` L118–150, `PENDING-OWNER-DECISIONS.md` P-34, `LAUNCH-CLOSURE-PREFLIGHT.md` L1–40.

`[Observed]` `python3 scripts/launch_gate_results.py --selftest` in the clone → **74 fixtures, 0 failing, exit 0**. Full roll printed and read.

`[Observed]` I built a record generator matching §5's template field-for-field (39 roster rows) and ran **the clone's own validator**, imported so `REPO` resolves to the clone, with git checks **ON** against the real commit `95a41ea`, the real committed instrument digest `bc1363bf…`, the real §8 digest `01209c0f…`, and the real `effective_version: v1.9` — so LG-1/LG-2/LG-11 and both citation-existence paths actually executed on every case below. Roughly 130 synthetic records.

`[Observed]` **Mutation-revert testing (verification rule 6), on a copy outside the clone** with the clone's `.git` symlinked so git-on fixtures still run. Both decisive repairs reverted; recorded in §2.

`[Observed]` **Cross-version execution.** I built a second copy of the validator from `git show b00c3dd:scripts/launch_gate_results.py` (the v1.8 bytes) with its own instrument copy, and ran the *same* synthetic records through both — the only way to measure what v1.9 newly **accepts**, which no fixture and no record in this batch reports. This produced RD37-01.

`[Observed]` Fixture→check coverage computed mechanically by intercepting `validate()` and binding each emitted error to its `LG-n` prefix. Denominator **13** checks; `validate()` invoked **74** times, matching the printed count.

`[Observed]` Repo-wide sweeps with Python `re`, never shell grep (rule 1). Denominator **349** text files (`.md/.py/.yaml/.yml/.txt`, excluding `.git`/`_bootstrap`/`.beads`).

`[Observed]` `python3 scripts/check_governance.py` in the clone → **30 OK, 18 WARN, 0 FAIL (48 checks)**.

`[Unknown]` I did not administer the gate and read no pilot record content. All answer sets below are synthetic.

---

## 2. Per-finding repair verification — all seven RD-36 findings

| RD-36 | Class | Disp. | Status | Anchor / proof in the v1.9 bytes |
|---|---|---|---|---|
| RD36-01 | MAJOR | R | **verified-closed by execution and by mutation** | Validator:200 (defined bytes, quoted): `DECISION_ID_RE = re.compile(r"SDR-\d+[a-z]?(?:\([a-z]\))?$")` — `B` is gone. Executed at `95a41ea`, git on, real digests, `READY-WITH-DEFERRALS`, count 1: `B-1`, `B-7`, `B-999`, `B-1a` all **REJECTED**, reason quoted — *"is review-finding numbering (round-2026-08c's B-n findings) — it names no decision in this repository and grants nothing; cite SDR-n or the decision's repository path (RD36-01)"*; `SDR-33` **ACCEPTED**; `P-34`/`D-10` rejected on the pending-queue limb. The accepting fixture is **replaced, not added to**: at `b00c3dd` line 974 read `case("B-n (made owner decision) as deferral citation accepted (RD35-06)", …, None)`; at HEAD the same slot reads `case("B-n (review-finding numbering) as deferral citation rejected (RD36-01)", …, "review-finding numbering")`. The §9 v1.8 entry carries the dated marker (quoted): *"SDR-n/B-n [corrected 2026-08-10, RD36-01: `B-n` named no decision family in this repository — see the v1.9 entry below]"*. The v1.9 §9 entry's family statement — *"The identifier family narrows to **SDR-n alone**"* — is true of the bytes. D-6's correction travels in the v1.9 delta's D-1; the **v1.8 delta is byte-identical to its state at `b00c3dd`** (`0839503222da…` both sides). The docstring is corrected in place (L54–56). **Mutation 1**: restoring `(?:SDR|B)` on a copy → `74 fixtures, 1 failing`, failing exactly *"B-n (review-finding numbering) as deferral citation rejected (RD36-01)"*. |
| RD36-02 | MAJOR | R | **verified-closed by execution and by mutation, both limbs, value inspected** | Eight sites now anchor `[^\S\n]*`. Limb (a): scoped `C2` + `READY FOR <verbatim target>`, findings line written with **no value** → **1 error**, LG-9's absence path, message quoted: *"or the line carries no value — an empty field is absent, RD36-02"*. **I inspected the parsed value, not only the error**: `re.search(r"^Deferred-wave findings recorded outside launch scope:[^\S\n]*(\S.*)$", …)` returns **`None`** — the next line is no longer captured (at v1.8 it captured `'Deferred count (owner-deferred findings this administration): 0'`). Non-empty control **0 errors**; deletion control **1 error**. Limb (b): six-row-Unknown record with an empty Unknowns field → **1 error**, parsed value **`None`** (at v1.8 it captured the falsification-notes line); `TBD` control still rejected. **Mutation 2**: replacing all eight `[^\S\n]*` with `\s*` on a copy → `74 fixtures, 2 failing`, failing exactly the two RD36-02 fixtures. |
| RD36-03 | MINOR | R | **verified-closed for the four fields repaired; three §5 fields were not repaired — RD37-02** | Validator:321–327, 474–489, 500–507. The shadowed-count record (`Deferred count summary for the reader: 0` + declared `: 3`) → **2 errors**, the first naming the disagreement and both values: *"`Deferred count:` appears more than once with disagreeing values (0, 3)"*; the trend row no longer prints 0. Agreeing duplicates → **0 errors**. Shadowed `Launch target:` and shadowed `Owner deferral decision:` also error, in **both** orders. The three §5 fields the repair did not reach still resolve by first match — RD37-02. |
| RD36-04 | MINOR | R | **closed on LG-9; on LG-13 the same rule inverts into a silent pass — RD37-01** | `_names_nothing()` at validator:279–288 gains the negation-prefix rule. Scoped `C2` + `READY FOR`, git on: `no defects found`, `none identified`, `nothing of note`, `no findings in the deferred waves` — **all four rejected**, *"a placeholder names no defect"*. A real finding line (`RFC-0010 mission-profile drift (Wave D1)`) **passes**. The mirror false-rejection is gone: `E3 reopen-list: none identified` beside `E3 \| Met` → **0 errors**. But on LG-13 "names nothing" is the *no-error* branch, so the same rule now silences enumerated reopen lists led by a negation clause — RD37-01. |
| RD36-05 | MINOR | R | **verified-closed by execution** | LG-12's presence set gains `("Reviewer:", "the fresh-context disclosure §2 requires — the eighth declared field, RD36-05")` at validator:659–661. Deleting the `Reviewer:` line from a clean-validating record → **1 error**. All seven siblings re-tested by deletion this session: non-authority banner, `Reviewer model family:`, `Materials given:`, `Operationalization notes:`, `E3 reopen-list:`, `Unknowns and what would settle them:`, `Reviewer's falsification notes:` — **eight of eight** now error. |
| RD36-06 | MINOR | R | **verified-closed by execution, both forms, both directions** | `_sdr_exists()` at validator:207–218; tree rejection at 255–258. Git on, real commit: `SDR-9999` **REJECTED** (*"names no decision in .syzygy/governance/decisions at the named commit"*), `SDR-33` **ACCEPTED**; `.syzygy/governance/decisions/` and `.syzygy/governance/decisions` (no trailing slash) both **REJECTED** as trees; the real file `…/LAUNCH-GATE-AUTHORITY-DECISION.md` and `./scripts/launch_gate_results.py` (the `./` limb) both **ACCEPTED**; `…/NO-SUCH.md` rejected. Residual on the guard's *semantics* — RD37-05. |
| RD36-07 | MINOR | R | **verified-closed; three corrections present, dated, accurate** | `DISPOSITION-REGISTER.md` diff `b00c3dd..HEAD` read in full. RD34-02 row: *"[corrected 2026-08-10, RD36-07: this family list went stale in the same v1.8 batch that corrected this row's other two claims — RD35-06 rejected `P-n`/`D-n` at v1.8, and RD36-01 narrowed the form to `SDR-n` alone at v1.9]"*. RD35-06 row: *"[corrected 2026-08-10, RD36-07: this row never matched the bytes … `B-n` is review-finding numbering and was removed at v1.9]"*. RD35-07 row: *"`Operationalization notes:` [added 2026-08-10, RD36-07: the v1.8 bytes checked this field and this row omitted it]"*. Each verified against the bytes independently above. All three accurate. |

**Tally, with its denominator:** of RD-36's **7** findings, **7 are present in the v1.9 bytes and none is absent**; **5 are closed outright** (RD36-01, -02, -05, -06, -07); **2 (RD36-03, RD36-04) are closed for the case RD-36 demonstrated and leave a residual one level up**, and in RD36-04's case the residual is a *new* silent pass the repair created. Both decisive repairs were additionally **mutation-proven** by reverting them on copies and observing the selftest fail on exactly the fixtures those repairs added. `[Inferred]` The repair session did the work the register describes, and its records are honest about what it did — with the D-4 exception recorded as RD37-01.

---

## 3. Verification of the delta's and the records' claims

`[Observed]` **"§1–§8 byte-unchanged from v1.8."** True. Per-section sha256 with a fence-aware splitter, `git show b00c3dd:launch-gate-pre-specifications.md` vs HEAD, ten sections each side: §1 `1f2d1d60…`, §2 `11a9d452…`, §3 `fe0b051e…`, §4 `f4a2a642…`, §5 `3f5023d8…`, §6 `b54c12e5…`, §7 `bf31396f…`, §8 `01209c0f…` — **all eight identical**. Only `HEADER` and `## 9. Changelog` differ. The full `git diff` of the instrument is **57 lines**: `-effective_version: v1.8` / `+effective_version: v1.9`, the three-line dated correction marker inside the v1.8 entry, and one appended v1.9 changelog entry. **Zero question blocks changed; no ID renumbered.** The delta's "the narrowest lawful correction to a false sentence an approval digest would otherwise bind" is true of the bytes.

`[Observed]` **The frozen records were not edited.** v1.4 `3c52291a…`, v1.5 `1aa8bf50…`, v1.6 `67820bb2…`, v1.7 `5d6b775a…`, v1.8 `08395032…` — all five deltas byte-identical to their state at `b00c3dd`; RD-33, RD-34 and RD-35 raw reviews likewise. The full changed-file set `b00c3dd..HEAD` is **11 files**, and the only round-08e review file touched is RD-36's own (newly added).

`[Observed]` **Fixture arithmetic checks out.** `case(` occurrences: 63 at `b00c3dd`, 73 at HEAD (each includes the `def case(` line) → **62 → 72 invocations**, plus the 2 bespoke trend checks = **64 → 74**, matching the printed count, the delta's "74 fixtures", P-34's "74 in all", and PROJECT-STATUS's "(74 fixtures)". The +10 net with 11 new labels is exactly the delta's disclosed "the one `B-1` fixture inverted its expectation deliberately".

`[Observed]` **The version-literal claim is true where it is made, and a bump fails loudly elsewhere.** At `b00c3dd` the `good_real` builder carried `.replace("Instrument version: v1.8", …)`, a literal; at HEAD it carries `re.sub(r"Instrument version: v[\d.]+", …)`, a shape substitution. Two literals remain (the `GOOD` template's own `v1.9` line, and the version-disagreement fixture's replace target) — I confirmed by inspection that a future bump strands them as a **selftest FAIL**, not a silent pass, so the RD34-05 lesson is applied where it can strand something silently.

`[Observed]` **Fixture→check coverage, denominator 13.** Emissions across the 74-fixture run: LG-1 (3), LG-2 (11), LG-3 (4), LG-4 (2), LG-5 (4), LG-6 (11), LG-7 (27), LG-8 (3), LG-9 (8), LG-10 (7), LG-11 (5), LG-12 (11), LG-13 (3). **All thirteen checks are made to fire by at least one fixture; none is absent.** Total error emissions 99. `validate()` invocation count = 74 = the printed fixture count.

`[Observed]` **P-34 is coherent at v1.9.** The question names **v1.9** (L11); the offer-status block is dated 2026-08-10, states *"not yet offerable"*, summarizes RD-36's two MAJOR findings correctly, and names **RD-37** as the precondition (L27); option (a) lists **all six** deltas with the correction pointers **before** the claims they correct — v1.5 *"read with the v1.6 delta's D-10"*, v1.7 *"read with the v1.8 delta's D-1"*, v1.8 *"read with the v1.9 delta's D-1 and D-4"*; option (b) carries the v1.10 ordering (amendments into the working tree before step 2's digest, RD33-11) and prices the F5-promotion honestly; the recommendation's fixture count is **74**, matching; the approval block (L142) names **v1.9**. `PENDING-OWNER-DECISIONS.md:185` and `PROJECT-STATUS.md:129–147` both name v1.9, name RD-37 as the precondition, and describe the chain accurately.

`[Observed]` **Stale-version sweep, denominator stated.** 349 files scanned; **72** lines carry both a launch-gate token and a `v1.x` token, across **22** files; all 72 read and classified. Every one of the 64 not naming v1.9 is a delta filename or title, a §9 changelog back-reference, a frozen review, a historical disposition row, a round-08d artifact, the v1.3 pilot (`PROJECT-STATUS.md:125`, immediately followed by *"The instrument is now **v1.9**"*; `LAUNCH-CLOSURE-PREFLIGHT.md:35`, under its explicit *"Historical snapshot — non-authoritative round record"* banner at L3–8), or P-34's own six-delta list. **RD34-05's version-neutral repair holds**: `DEFERRED-WAVE-POSTURE.md:41` reads *"version per the instrument's own `effective_version:` header — no version is quoted here, so a bump cannot strand this sentence"* and `FIRST-OPENSPEC-SEQUENCE.md:70` reads *"current version per the instrument's own header"*. **No routed artifact names a stale instrument version.**

`[Observed]` **One delta claim is false of the bytes.** D-4 (quoted): *"One disclosed edge: a genuine finding line *led* by a negation clause would be wrongly classed as empty — loudly, as a rejection the administrator sees, **never as a silent pass**."* On LG-13 the polarity is inverted and it is exactly a silent pass — RD37-01. The "What did not change" section's *"A record lawful under a **correct** v1.8 reading remains lawful under v1.9 — the newly rejected records are those §4 and §5 already condemned in prose"* discloses the narrowing direction and is silent about the widening one, which is where the defect lives.

---

## 4. Fixture-discipline audit against RD-36's own standard

RD-36 prescribed: *"every predicate fixtured in both directions, and every §5 field fixtured absent, empty, and shadowed."* The v1.9 batch declares that discipline adopted, in the delta, in §9's instrument bytes, in the register, and in PROJECT-STATUS. I audited it two ways: statically (which fixture exists) and by **execution** (whether the validator detects the state at all — the column that matters, because an undetected state is a blind spot whether or not a fixture names it).

**Table A — the sixteen §5-declared record elements × {absent, empty, shadowed}.** Denominator **16**. `DETECT` = the validator errors; `*BLIND*` = it validates clean; `—` = not applicable.

| §5 element | absent | empty | shadowed (decoy above) | shadowed (decoy below) | absent fixtured? |
|---|---|---|---|---|---|
| non-authority banner | DETECT | — | — | — | yes |
| `Instrument version: … sha256:` | DETECT | DETECT | DETECT | ***BLIND*** | yes |
| `Parameter block sha256:` | DETECT | DETECT | DETECT | ***BLIND*** | yes |
| `Launch target:` | DETECT | DETECT | DETECT | DETECT | yes |
| `Reviewer:` | DETECT | *BLIND* (by design) | *BLIND* | *BLIND* | yes (new) |
| `Reviewer model family:` | DETECT | *BLIND* (by design) | *BLIND* | *BLIND* | yes |
| `Materials given:` | DETECT | *BLIND* (by design) | *BLIND* | *BLIND* | yes |
| `Operationalization notes:` | DETECT | *BLIND* (by design) | *BLIND* | *BLIND* | yes |
| `E3 reopen-list:` | DETECT | DETECT | DETECT | ***BLIND*** | yes |
| `Deferred-wave findings …:` | DETECT | DETECT | DETECT | ***BLIND*** | no (empty is) |
| `Deferred count …:` | DETECT | DETECT | DETECT | DETECT | yes |
| `Reopened count …:` | DETECT | DETECT | DETECT | DETECT | yes |
| `Owner deferral decision:` | DETECT | DETECT | DETECT | DETECT | yes |
| `Unknowns and what would settle them:` | DETECT | DETECT | DETECT | ***BLIND*** | yes |
| `Reviewer's falsification notes:` | DETECT | *BLIND* (by design) | *BLIND* | *BLIND* | yes |
| `GATE VERDICT:` (terminal) | DETECT | DETECT | — | — | yes |

Reading the denominators: **absent — 16/16 detected, 15 fixtured.** **Empty — 11 of 16 are detectable (5 are presence-only and content-blind by disclosed design); of those 11, exactly 2 are fixtured** (the two RD36-02 limbs). **Shadowed — 4 of 16 carry disagreement detection in both orders; 5 more detect one order and are blind in the other; 5 are blind entirely; exactly 1 is fixtured.** So the batch's own standard is met for *absent*, met for the two limbs RD-36 demonstrated under *empty*, and **not met for *shadowed***, where the repair reached four fields and the standard asks for all of them. Three of the un-reached fields carry live silent passes — RD37-02.

**Table B — the seven predicates v1.9 changed, by fixture direction.** Denominator **7**.

| Predicate | rejecting direction | accepting direction | both? |
|---|---|---|---|
| `DECISION_ID_RE` → `SDR-n` alone | `B-1` rejected (new) | `SDR-33` accepted (git-on, new) | **yes** |
| `[^\S\n]*` line anchoring | 2 empty-field fixtures (new) | GOOD baseline + lawful scoped fixture | **yes** |
| shadow detection (`findall` + disagreement) | 1 fixture (Deferred count) | **none** — I verified by execution that agreeing duplicates validate clean, asserted by no fixture | **no** |
| negation-prefix rule | 2 fixtures on LG-9 (new) | 1 fixture on LG-13 (new) | yes, but see RD37-01 |
| `Reviewer:` presence | deletion fixtured (new) | GOOD baseline | **yes** |
| `SDR-n` existence guard | `SDR-9999` rejected (new) | `SDR-33` accepted (new) | **yes** |
| tree rejection | directory rejected (new) | real file accepted (RD35-01) | **yes** |

**6 of 7 changed predicates are fixtured in both directions; 1 is not.** `[Observed]` Across the whole suite, **9 of 74 fixtures assert that a record validates clean** and 65 assert a rejection — a denominator worth quoting when the batch's discipline claim is read, because the accepting direction is where this chain's last two BLOCKING/MAJOR findings lived.

**Table C — surfaces the chain has never probed, attacked this session.**

| Surface | Result |
|---|---|
| `ROW_RE` bold markers | `\| **A1** \| **Met** \|`, `\| A1 \| *Met* \|`, `\| **A1 \| Met \|` all parse to `A1`/`Met`. Bold stripping does not admit a verdict outside the closed set: `Partially met`, `Met (with caveats)` still rejected. Cosmetic tolerance only |
| evidence cell containing `\|` | `\| A1 \| Met \| see table a\|b \|` parses correctly — group 2 is `[^\|]+?` and stops at the verdict cell |
| empty verdict cell | `\| A1 \|  \| x \|` → 2 errors (closed-vocabulary + LG-10 missing row). Loud |
| blockquoted / bulleted rows | not parsed → LG-10 missing-row error. A quoted example table cannot inject rows. Correct |
| alien sub-row IDs | `\| A1-foo \|` → LG-10 *"row ID(s) outside the question roster"*. Loud |
| `Unknown-ish` as a verdict | accepted as `Unknown` (`VERDICT_RE`'s `Unknown\s*(?:\(\|—\|-).+`). Cosmetic; no gate consequence measured |
| E1 rollup × sub-rows | `E1 \| Met` over an `Unknown` sub-row → LG-8 error, and under `READY FOR` a second LG-6 error. Scoped verdicts on E-section sub-rows rejected by LG-3. Closed |
| `param_block_bytes` boundaries | §8 bounded by `## 9. Changelog`; extracted block 6577 bytes, contains no `## 9`. The `## G1 — completeness critic` heading between §5 and §6 does not confuse the `^## (?!8\.)` scan. §8-is-last-section degrades to end-of-file, which is the only sane reading |
| trend-row emission | 9 columns under every gate word I tried, including `READY-WITH-DEFERRALS — see appendix`. The `\|`-guard holds |
| `--prior` comparison path | **defective — RD37-04** |
| G1 section test | **defective — RD37-03** |
| multiple scoped rows, one named defect | 4 scoped rows + one named defect → clean. `[Observed]` This matches §4's defined clause exactly (*"whose deferred-wave findings line names no defect"* — a singular threshold), so I record it as a **disclosed limit of the clause, not a validator defect** (rule 8) |

---

## 5. New findings

### RD37-01 — MAJOR — the negation rule inverts on LG-13: an enumerated E3 reopen-list led by a negation clause validates clean under `E3 | Met` and `READY FOR`, defeating §3's self-declared sharpest gate — and four such records were **rejected at v1.8**

`_names_nothing()` is shared by LG-9, LG-12 and LG-13, but the three checks read it with opposite polarity. On LG-9 and LG-12, "names nothing" **is** the error. On LG-13 (validator:693) it is the *no-error* branch: `elif not _names_nothing(e3_m.group(1).strip()):`. So widening `_names_nothing` tightens LG-9 and LG-12 and **loosens LG-13** — and D-4 widened it by an unbounded semantic rule: any value whose first token is `no`/`none`/`nothing`/`zero`.

`[Observed]` Executed at `95a41ea`, git on, real digests, full 39-row §5 template, `F2 | Met`, `E3 | Met`, `Deferred count: 0`, terminal `GATE VERDICT: READY FOR Capability 1 — Project registration and honest shape visibility`:

```
E3 reopen-list: no items are resolved: (1) whether a Mission is a first-class
object; (2) evidence adapters in Wave A
→ errors: 0
→ trend : | 2026-08-10 | 95a41ea8 | 0 | 0 | 1 | 0 | 0 | n/a — no prior record
          supplied | READY FOR Capability 1 — Project registration and honest
          shape visibility |
```

Likewise `none of these are closed: …`, `nothing is settled: …`, `zero of the reopen items are closed: …` — **four of four clean, with the two reopen items still enumerated in the record.** The control (the same list with no negation lead) is correctly **2 errors**.

`[Observed]` **This is a regression, measured against the v1.8 bytes.** I ran the identical records through a copy of the v1.8 validator built from `git show b00c3dd:scripts/launch_gate_results.py`, git on, against its own commit and digests:

| `E3 reopen-list:` value | v1.8 errors | v1.9 errors |
|---|---|---|
| `(1) whether a Mission is a first-class object; (2) evidence adapters in Wave A` | 2 | 2 |
| `no items are resolved: ` + the same list | **2** | **0** |
| `none of these are closed: ` + the same list | **2** | **0** |
| `nothing is settled: ` + the same list | **2** | **0** |
| `zero items closed: ` + the same list | **2** | **0** |
| `none identified` (the disclosed repair) | 2 | 0 |

Instrument §3, E3 (defined clause, quoted): *"**Fails when:** the list is non-empty; 'ready' is then false regardless of every other verdict."* The validator's own docstring calls LG-13 *"the instrument's self-declared sharpest single gate."* A record that enumerates two reopen items, rolls E3 up to `Met`, and reads `READY FOR <the verbatim launch target>` is exactly the record §3 says cannot be ready, and it enters the trend log with a pass.

`[Observed]` **The v1.9 delta asserts the opposite, in the record the owner reads under P-34 option (a).** D-4, quoted in full: *"One disclosed edge: a genuine finding line *led* by a negation clause would be wrongly classed as empty — **loudly, as a rejection the administrator sees, never as a silent pass**."* That sentence is true of LG-9 and LG-12 and false of LG-13, and LG-13 is the check D-4's own preceding sentence is about. The delta's closing claim — *"the newly rejected records are those §4 and §5 already condemned in prose"* — describes only the narrowing direction; the widening direction produced these four newly-accepted records, each of which §3 condemns.

`[Observed]` **No fixture can see it.** LG-13 has 3 emissions across the 74-fixture run, from three fixtures: a plain enumerated list beside `E3 | Met`, a plain enumerated list under READY, and the deletion case. The one accepting LG-13 fixture supplies `none identified` — an *actually* empty marker. Denominator 74, full roll read. This is RD-36's diagnosis a fifth time, in the check the RD36-04 repair itself touched: the predicate was fixtured in both directions, but only for values on which both directions agree.

`[Inferred]` The root cause is that one predicate serves three checks with two polarities. A `_names_nothing` that grows to catch more emptiness claims necessarily silences more of LG-13. The two limbs need separate predicates, or LG-13 needs a positive emptiness test (a closed marker set) rather than the negation of a placeholder test.

*Requires:* a **validator change** (split the predicate, or give LG-13 a positive empty-marker test — the instrument's §5 template already writes `<empty | enumerated items>`, so an instrument sentence publishing that marker vocabulary is the alternative), a **fixture** in the newly-blind direction, and a **record correction to the v1.9 delta's D-4** — the sentence claiming this class is never a silent pass. **No instrument amendment is required**: §1–§8 are correct as written and the §9 v1.9 entry says only *"closing … the mirror false-rejection on LG-13 (RD36-04)"*, which is true and does not carry the false safety claim. **This blocks the formal administration**, and I judge it **blocks the P-34 offer** — see §7.

### RD37-02 — MAJOR — RD36-03's shadow repair covers four fields; three §5 fields still resolve by first match with no disagreement check, and each yields a clean pass

D-3 (quoted): *"The count fields, the deferral citation, and the launch-target line are now parsed by collecting **all** occurrences."* That is four fields. §5 declares fifteen. The three remaining *content-bearing* fields — the ones LG-9, LG-12 and LG-13 read — still use `re.search`, which takes the **first** occurrence and reports no disagreement: `mfind` (validator:528), `unk_m` (666), `e3_m` (688).

`[Observed]` Executed at `95a41ea`, git on, real digests, full 39-row template. Three records, each carrying two contradictory answers to one §5 field:

- **E3 reopen-list.** `E3 reopen-list: empty` followed later by `E3 reopen-list: (1) whether a Mission is a first-class object; (2) evidence adapters in Wave A`, with `E3 | Met` and `READY FOR <verbatim target>` → **0 errors, `record valid`**, trend row a clean `READY FOR`. The enumerated list is in the record and is never read.
- **Unknowns.** `Unknowns and what would settle them: F1 — a second formal administration` followed later by `Unknowns and what would settle them: TBD`, with an `Unknown` row → **0 errors**. The declared field reads `TBD`; §4 (quoted): *"every Unknown must carry what evidence would settle it."*
- **Deferred-wave findings.** A line naming a defect, followed later by the declared `Deferred-wave findings recorded outside launch scope: none`, beside a scoped `C2` row under `READY FOR` → **0 errors**. §4 (defined clause, quoted): *"a record with any scoped row whose deferred-wave findings line names no defect asserts a scoped defect exists and that none exists — a validation error (LG-9), never a lawful record."*

`[Observed]` The asymmetry is measurable and one-directional: for the four repaired fields, disagreeing occurrences error in **both** orders (verified above and in §2); for these three, one order errors and the other validates clean. `[Observed]` The two §2 integrity fields — the instrument digest line and the parameter-block digest line — share the defect in the same shape (`DETECT` above, `*BLIND*` below), though there the blind direction is benign: a shadowing quotation earlier produces an LG-2 mismatch, loudly.

`[Inferred]` This is the chain's established shape a sixth time. RD-36 demonstrated shadowing on `Deferred count:`; the repair closed the count fields, the citation and the target — every field RD-36's demonstration or its immediate neighbourhood named — and left the three fields RD-36 happened not to demonstrate, which are precisely the three whose values drive the three checks §4 and §3 call decisive.

*Requires:* a **validator change** — apply the D-3 `findall` + disagreement treatment to all §5 fields uniformly, not to an enumerated four — plus a fixture per field, in both orders. **No instrument amendment**; §4 and §5 already state the rules. **Blocks the formal administration.** Not offer-blocking on its own: no owner-facing document misdescribes it (D-3 states its own scope accurately by listing the four fields it repairs).

### RD37-03 — MINOR — LG-4's G1 test is a heading-substring test; a record with its G1 section deleted validates clean if any other heading mentions G1

Validator:436: `if not re.search(r"^#+ .*G1", txt, re.M):`.

`[Observed]` git on, real digests: replacing `## G1 — completeness critic` with `## Materials: we cite §3's G1 rule` — deleting the completeness-critic section outright while leaving an incidental mention in an unrelated heading — → **0 errors, `record valid`**. §4 (quoted): *"an administration missing G1 is incomplete and cannot support a gate decision."* The one fixture, *"missing G1 rejected"*, replaces the heading with `## notes` — a string containing no `G1` — so it tests only the direction where the record volunteers no mention. `[Observed]` The check is also satisfied by `### G1` alone, which is lawful and correct. *Requires:* a validator change (anchor the heading to the G1 section's own shape) and a fixture for the substring direction; no instrument amendment; not offer-blocking.

### RD37-04 — MINOR — the `--prior` record is never validated, so an arbitrary file can suppress the New-findings column that F1 is answered from

`validate()` reads `prior_path` and runs `_row_verdicts()` over whatever it finds; no roster check, no verdict-vocabulary check, no digest, no commit.

`[Observed]` git on, real digests. Current record with a newly plain `A1 | Not met` and a newly scoped `B2` → New-findings **2** against a clean prior. Against a **three-line non-record** containing only `| A1 | Not met | x |` and `| B2 | Not met | x |` → New-findings **1**. `[Observed]` A prior carrying a `| G1 | Not met |` row — which LG-4 makes an error in a *current* record — is parsed and counted on the prior side without complaint.

§6's New-findings column and §5's *"counts are computed from the rows, never trusted from prose"* discipline both rest on the prior side being a lawful administration record. F1 (convergence) is answered from the trend log. *Requires:* a validator change (validate the prior with the same checks, or at minimum assert the roster and refuse a prior that fails LG-10) or an instrument sentence stating that `--prior` trusts its input; no instrument amendment as written; not offer-blocking.

### RD37-05 — MINOR — the new `SDR-n` existence guard is a substring-presence test over the whole decisions home, which includes the pending-decision queue

`_sdr_exists()` runs `git grep -q -F <ident> <commit> -- .syzygy/governance/decisions`. That answers *"does this string appear anywhere under the decisions home"*, not *"does this identifier name a made decision."*

`[Observed]` Sweep of the decisions home at `95a41ea`, denominator **18** `.md` files: the SDR population is exactly **SDR-1…SDR-33 with no gaps**. So today the guard is not exploitable — every identifier that is a substring of a minted one is itself minted, and `SDR-34`, `SDR-40`, `SDR-99`, `SDR-2a`, `SDR-33a` all reject. `[Inferred]` Two latent weaknesses follow from the semantics rather than the population: the corpus searched includes `PENDING-OWNER-DECISIONS.md` — the queue of decisions **not yet made** — so an identifier discussed there before being ruled would pass a guard whose stated purpose (validator:193–199, quoted) is *"only families that name MADE decisions may claim a granted deferral"*; and substring matching means an unminted `SDR-3` would be accepted on the strength of a minted `SDR-33` if the population ever had gaps. The delta's D-6 wording — *"existence-checked against the decisions home"* — is literally accurate and overclaims nothing. *Requires:* a validator change if taken (anchor the match, and scope it to decision records rather than the whole tree); no instrument amendment; not offer-blocking. Recorded as a disclosed residual, in the same posture RD-36 gave RD36-06.

### RD37-06 — MINOR — the §2 integrity anchors are unguarded first-match fields

`mdate`, `mcommit`, `mver`, `minstd` and `mparamd` are all `re.search` over the whole record with no shadow check, unlike the four fields D-3 repaired. `[Observed]` A second, disagreeing `Instrument version: … sha256:` line placed *below* the header is silently ignored (audit Table A); placed *above*, it produces an LG-2 mismatch. `[Inferred]` The blind direction is benign in every case I constructed — the checked occurrence is the earlier one, and an appendix quoting a prior administration's header would fail loudly rather than pass — so I record this as the same class as RD37-02 at lower severity, and as the reason a uniform field-parsing rule is the right repair rather than four more enumerated fields. *Requires:* a validator change, folded into RD37-02's; no instrument amendment; not offer-blocking.

---

## 6. What passes

`[Observed]` These are executions and sweeps run this session, not inferences:

- **All seven RD-36 findings are present in the v1.9 bytes; none is absent.** Five closed outright, two closed for the demonstrated case. Every one confirmed by rebuilding RD-36's own records and running the clone's validator with git checks on against the real commit `95a41ea` and the real committed instrument and §8 digests.
- **RD36-01 is genuinely and completely closed.** `B-1`, `B-7`, `B-999`, `B-1a` all reject with a reason naming what `B-n` is; `SDR-33` accepts; the accepting fixture was **replaced**, not supplemented; the §9 v1.8 entry carries the dated marker and the v1.9 entry states the true family; the frozen v1.8 delta was not edited; the docstring and all three register rows were corrected.
- **RD36-02 is closed at the value level, not only at the error level.** I confirmed the parsed value is `None` — not the next line's text — for both limbs, which is the measurement RD-36's finding actually turned on.
- **Both decisive repairs are mutation-proven, by me, this session.** Restoring `(?:SDR|B)` → `74 fixtures, 1 failing`, the RD36-01 fixture. Restoring newline-crossing `\s*` at all eight sites → `74 fixtures, 2 failing`, both RD36-02 fixtures. `74 fixtures, 0 failing, exit 0` on the unmutated clone.
- **Every check is fixtured.** Denominator **13**. LG-1…LG-13 each fire at least once across the 74-fixture run (emission counts in §3), computed mechanically by intercepting `validate()`. `validate()` invocation count = 74 = the printed fixture count = the delta's figure = P-34's figure = PROJECT-STATUS's figure, and the 64→74 arithmetic reconciles with the `case(` counts at both commits.
- **The §4 conjunct battery still holds on both pass branches.** Under `READY-WITH-DEFERRALS` with a lawful `SDR-33` citation and count 1: an all-`Not met` record is BLOCKED on the non-deferrable conjuncts; a lawful F2-deferral record is **0 errors**. Plain `READY FOR` over a nonzero `Deferred count:`, over an unresolved F2, over a `Not met` F1/F3/E-row, or over a plain `Not met` in A–D each block on the right limb. The scoped form does not block and is counted separately.
- **The row parser, the trend row, the E1 rollup and the §8 extractor survived every attack I made** (Table C): bold markers, `|`-carrying evidence cells, empty verdict cells, blockquoted and bulleted rows, alien sub-row IDs, four gate words — the trend row was 9 columns in every case, and no attack admitted a verdict outside the closed vocabulary.
- **"What did not change" is accurate to the byte.** Per-section sha256 against `git show b00c3dd:` — §1–§8 all **byte-identical**, §8 for the fifth consecutive amendment; only the `effective_version:` line, the appended §9 v1.9 entry, and the three-line dated marker inside the §9 v1.8 entry move; zero question blocks changed; 57 diff lines total. The five frozen prior deltas and the three frozen prior raw reviews are byte-identical to their state at `b00c3dd`.
- **The three RD36-07 register corrections are present, dated 2026-08-10, and accurate**, each verified against the bytes independently.
- **P-34 is coherent at v1.9** — question, dated offer-status naming RD-37, option (a)'s six-delta list with all three correction pointers ahead of the claims they correct, option (b)'s v1.10 ordering, the 74-fixture recommendation, and the v1.9 approval block. `PENDING-OWNER-DECISIONS.md` and `PROJECT-STATUS.md` agree with it.
- **No routed artifact names a stale instrument version.** Denominator **349** files; **72** hits across **22** files, all read and classified; RD34-05's version-neutral repair holds at both repaired sites; the two v1.3 mentions sit under an explicit historical banner and an immediate "now v1.9" correction respectively.
- **`check_governance.py` in the clone: 30 OK, 18 WARN, 0 FAIL (48 checks).**
- **The clone stayed byte-clean.** `git status --porcelain` empty at open and close; HEAD `95a41ea8…`; instrument `bc1363bf…` and validator `8945bbe6…` unchanged at close, each confirmed by two independent methods.

---

## 7. Overall assessment — may v1.9 be offered to the owner at P-34, and may the formal administration run on this validator?

The repair quality is again the highest of the chain. RD36-01 was closed the hard way — the character class narrowed, the false taxonomy corrected in all four places it was asserted, the accepting fixture *replaced* rather than supplemented, and the frozen v1.8 delta left untouched with its correction routed through D-1 in the D-10 convention. RD36-02 was closed at the value level. The register corrections are dated, attributed and true. The instrument's footprint is the narrowest possible: §1–§8 byte-identical for the third amendment running, §8 for the fifth, and the only normative bytes that move are a version literal, a changelog entry, and a three-line marker correcting a sentence RD-36 proved false.

And the batch did adopt RD-36's discipline, visibly and in the right places. Six of the seven changed predicates are fixtured in both directions; the empty-field case is fixtured for both limbs RD-36 demonstrated; the fixture count arithmetic is honest; the selftest is mutation-proven at the two decisive points. RD-36 predicted that without the discipline change a fifth administration would find a sixth class. The discipline changed, and I found a sixth class anyway — but it is worth stating exactly *how* it survived, because it is not the same failure:

**The discipline was applied to the predicates the batch changed, and the defect lives in a check that reads a changed predicate with the opposite polarity.** RD36-04's repair was fixtured in both directions on LG-9 and in the accepting direction on LG-13 — and it was that accepting fixture, testing a value (`none identified`) on which both readings agree, that hid the fact that widening `_names_nothing` *loosens* LG-13 without bound. Four records that the v1.8 validator rejected now validate clean, each enumerating live reopen items beside `E3 | Met` and a `READY FOR` verdict. So the sixth class is not "the fixture set tests one direction"; it is **"the fixture set tests one predicate at a time, and a shared predicate has more than one consumer."** That is a different, narrower gap, and it is the first time in five administrations that the diagnosis has moved.

RD37-02 is the older shape, unchanged: RD36-03's repair reached the four fields around RD-36's demonstration and stopped, leaving the three §5 fields that drive LG-9, LG-12 and LG-13 on first-match with no disagreement check — three more clean passes, on the three checks §3 and §4 call decisive.

So, on the two questions asked:

- **May v1.9 be offered at P-34?** **No.** The mechanism, ordering, options, precondition, six-delta list and correction pointers are all right, and I found nothing wrong with §1–§8 — the third administration running to find nothing in the normative text. But the delta the owner is routed to under option (a) tells him, in D-4, that the negation rule's one edge case fails *"loudly, as a rejection the administrator sees, never as a silent pass"*, and on the check D-4 is about it is exactly a silent pass — measurably, and as a **regression** against the v1.8 bytes the owner is being asked to supersede. An owner weighing option (a) reads that sentence as the disclosure of the risk he is accepting; it is the wrong way round. This is RD-8's *"the finding that converts act 1 from a knowing act into a surprised one"* applied to a process record rather than to instrument bytes. One thing distinguishes this from RD-36's block, and it matters for the cost: **the repair moves no instrument bytes.** §1–§8 are correct, and the §9 v1.9 entry's account of the RD36-04 repair is true as far as it goes and asserts nothing false. So the fix is a validator change, a fixture, and one corrected sentence in a delta that is not yet frozen — the packet does not need to re-freeze around a changed digest.
- **May the formal administration run on this validator?** **No.** A record that enumerates two E3 reopen items, rolls E3 up to `Met`, and reads `READY FOR <the verbatim launch target>` validates clean and enters the trend log — the exact record §3 says is *"false regardless of every other verdict"*. Three more §5 fields can carry two contradictory answers with the honest one silently discarded, defeating LG-9's scoped-defect disclosure, LG-12's Unknown-settling requirement, and LG-13 again. A record whose G1 section has been deleted passes LG-4 if any heading mentions G1. And the New-findings column F1 is answered from can be suppressed by an unvalidated prior file. Administration 1 is the row every later F1 verdict is read against; each of those would contaminate it.

Two things to say plainly against the chain's trend. First, **the normative text has now gone three full amendments without a finding** — RD-35, RD-36 and I each looked and found nothing in §1–§8. What keeps failing is the measuring layer, and this batch narrowed the failure meaningfully: the absent-field case is now complete (16 of 16 detected, 15 fixtured), the citation forms are both existence-guarded, and the identifier family is finally correct. Second, and unlike my four predecessors, **I can name a structural rule that would close the class rather than the instance**: the three surviving defects are all *one predicate or one repair applied to an enumerated subset of its consumers* — `_names_nothing` shared by three checks with two polarities, `findall` shadow detection applied to four fields of fifteen, `[^\S\n]*` applied to eight sites of which two are fixtured. The discipline that ends this chain is not another direction of fixture; it is **uniformity of application: when a predicate or a parsing rule is repaired, it is repaired for every consumer and every field, and the fixture asserts the uniformity rather than the instance.** Like RD-35 and RD-36 I decline to predict that the v1.10 batch is the last — but I will say that this is the first administration whose findings all reduce to one stateable rule, and that is a different position than "the class survives wherever the predecessor didn't look."

VERDICT: REVISE