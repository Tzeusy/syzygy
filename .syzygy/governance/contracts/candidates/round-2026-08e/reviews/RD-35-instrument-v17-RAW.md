# RD-35 — Launch-gate instrument re-review, v1.7 exact bytes (round-2026-08e, frozen commit eb53c3e)

- Review id: RD-35 (third administration of the instrument re-review chain: RD-33 → v1.6, RD-34 → v1.7)
- Date: 2026-08-10
- Subject: `launch-gate-pre-specifications.md` (v1.7, repo root), `scripts/launch_gate_results.py`, `round-2026-08e/LAUNCH-GATE-v1.7-SEMANTIC-DELTA.md`, `decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` (P-34), and the two repaired routed references
- Subject sha256, computed this session by two independent methods — `sha256sum` and Python `hashlib` over the file bytes: `c0b0dca4813123d9c660193bd3bd21d66437586cff1829839ad7dc03a6c877b2` — **verified, matches the dispatching session's measurement**
- §8 parameter block, extracted by the validator's own `param_block_bytes` (105 lines): `01209c0f052971f794e1f35827a002aa8d80420aad471d10fde000abb6366ff6` — **byte-identical to RD-34's v1.6 and RD-33's v1.5 measurements**, so §8 has not moved in three amendments
- Frozen clone `…/scratchpad/clone-08e-r12`: `git rev-parse HEAD` = `eb53c3ea3955e686008e152db90975f85b59d509`, `git status --porcelain` **empty before and after all work**; subject digest re-verified unchanged at close
- Reviewer: isolated fresh-context session, Claude family (Opus 5). Same-family re-review — F5's own example applies to me
- Authoring context: none. I read nothing outside the clone; every synthetic record was written to `…/scratchpad/rd35/`, never into the clone

---

## Method and what I ran

`[Observed]` Read in charter order: `AGENTS.md`, `RD-34-instrument-v16-RAW.md` (175 lines, 11 findings, `VERDICT: REVISE`), the RD-34 section of `DISPOSITION-REGISTER.md` (L277–306), then the instrument in full (922 lines), the validator in full (873 lines), the v1.7 delta (126 lines), P-34 (145 lines), the two repaired routed references, `PROJECT-STATUS.md` L120–136, `PENDING-OWNER-DECISIONS.md` P-34.

`[Observed]` `python3 scripts/launch_gate_results.py --selftest` → **43 fixtures, 0 failing, exit 0**. Full roll printed and read. Fixture→check map computed mechanically this session by intercepting `validate()` and binding each emitted error to its `LG-n` prefix (denominator 11): LG-1 (3 emissions), LG-2 (11), LG-3 (4), LG-4 (2), LG-5 (3), LG-6 (9), LG-7 (11), LG-8 (3), LG-9 (2), LG-10 (7), LG-11 (4) — **every one of the eleven checks is made to fire by at least one fixture; none is absent.**

`[Observed]` I built **68 synthetic administration records outside the clone**, each written field-for-field to §5's template in §5's order (39 roster rows), and ran the clone's own validator against them with git checks **ON** against the real commit `eb53c3e` and the real instrument and §8 digests, so LG-1/LG-2/LG-11 and the new citation-existence path all actually executed. Cited below as R1, H1/H3/H4/H5/H6/H7/H9a–d, T1–T4, and N1–N7.

`[Observed]` Byte-level v1.6 (`0bdd37d`) → v1.7 (`HEAD`): instrument `+55/−5`. Section identity computed with a fence-aware splitter, sha256 per section: **§1, §2, §3, §5, §7, §8 byte-identical**; §4, §6, §9 and the YAML header differ. Question blocks: denominator **35** stems (`- **XN [U|G]**`, A1…G1) — **zero differ**, IDs identical and in identical order, `*Fails when:*` count **33 → 33**.

`[Observed]` Repo-wide sweep with Python `re`, never shell grep (rule 1): **345** text files (`.md/.py/.yaml/.yml/.txt`, excluding `.git`/`_bootstrap`) → **50** lines carrying both a launch-gate token and a `v1.x` token, across 18 files, all read.

`[Unknown]` I did not run `check_governance.py`, did not administer the gate, and read the 2026-08-09 pilot record only for its `GATE VERDICT:` line shape (not for content). All answer sets below are synthetic.

---

## Per-finding repair verification — all eleven RD-34 findings

| RD-34 | Class | Disp. | Status | Anchor / proof in the v1.7 bytes |
|---|---|---|---|---|
| RD34-01 | BLOCKING | R | **verified-closed by execution** | §4:527–547, defined clause quoted: *"**READY-WITH-DEFERRALS** = every conjunct of **READY FOR `<LAUNCH_TARGET>`** above … with exactly one substitution: the F2 limb is satisfied by an **owner-cited deferral** … The E, A–D, F1, F3 and F4 conjuncts are **never deferrable**."* Validator:404–452 hoists the `bad` battery above the branch split. **H9d rebuilt** (all 39 rows `Not met`, citation, `Deferred count: 1`, `READY-WITH-DEFERRALS`, git on, real digests) → `LG-6: READY-WITH-DEFERRALS but a non-deferrable conjunct fails …`. **H9a** (E5 only), **H9b** (A1/C3/D1), **H9c** (F1/F3/F4) each rejected on exactly the failing limb. **H9-lawful** (F2 `Not met`, cited `SDR-33`, count 1, all else `Met`) → **0 errors**, so the branch is closed without being made unusable. The v1.6 hole is gone. |
| RD34-02 | MAJOR | R | **closed on the label limb; the existence limb is inverted — RD35-01** | `_deferral_citation_error`:162–177. **H3 rebuilt**, git on, 7 strings: `(owner only)`, `owner only`, `the owner`, `TBD`, `yes`, `verbally agreed`, `-` — **all seven rejected** with `neither a repository path nor a decision identifier`. But `v.lstrip("./")` is a character-class strip: every citation beginning `.syzygy/` loses its leading dot and is looked up as `syzygy/…`. **Verified**: the real, existing `.syzygy/governance/decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` is rejected as *"a citation to nowhere"* — see RD35-01. |
| RD34-03 | MAJOR | R | **closed on ordering; the anchoring residual is unsafe — RD35-02** | Validator:396–397: `_gv_matches = list(GATE_VERDICT_RE.finditer(txt)); mg = _gv_matches[-1]`. **H6 rebuilt**, git on: summary `GATE VERDICT: NOT READY` + terminal `READY FOR <target>` over `| F2 | Not met |` → `LG-6: … F2 is not Met`, and the trend row now carries the terminal word. The forward direction is genuinely closed. The reverse is not — RD35-02. |
| RD34-04 | MAJOR | R | **verified-closed, both directions, by execution** | §6:652–660: *"A **new** scoped finding is a **new finding** … rows newly `Not met` … plus rows newly scoped that were not previously a finding under either rendering."* Validator:464–471. My own prior/current pairs, git on: prior-clean → current-scoped `Not-met=0 Scoped=1 New=1`; **prior-scoped → current-plain `Not-met=1 Scoped=0 New=1`** (the r5 behavior RD-34 verified — **no regression**); prior-plain → current-scoped `New=0` (no double count); prior-clean → current-plain `New=1`. Both bespoke selftest checks observed passing. |
| RD34-05 | MAJOR | R | **verified-closed; the class removed, not the instance** | `DEFERRED-WAVE-POSTURE.md:41` now reads *"Under the launch-gate instrument's §8 launch scope (version per the instrument's own `effective_version:` header — no version is quoted here, so a bump cannot strand this sentence; RD34-05)"*; `FIRST-OPENSPEC-SEQUENCE.md:70` now reads *"P-34 launch-gate instrument authority (current version per the instrument's own header; RD34-05)"*. My 345-file sweep confirms **no remaining `v1.x` on a routed path is stale**: `PROJECT-STATUS.md:125` cites v1.3 for the pilot and L129 states *"The instrument is now **v1.7**"*; `LAUNCH-CLOSURE-PREFLIGHT.md:35`'s v1.3 sits under its historical-snapshot banner; every other hit is a delta filename, a changelog back-reference, or a frozen review. |
| RD34-06 | MINOR | R | **substantially closed; residual — RD35-05** | LG-9:384–391. **H1 rebuilt**, git on, scoped `C2` + `READY FOR`, 18 findings-line strings tried (denominator 18): `none`, `n/a`, `N/A`, `—`, `.`, `0`, `TBD`, `not applicable`, `todo`, `pending` — **10 rejected**. 8 still pass: `unknown`, `tba`, `n.a.`, `see above`, `various`, `several`, `(none known)`, `-- none --`. |
| RD34-07 | MINOR | R | **verified-closed by execution** | Validator:363–370. **H4 rebuilt**, git on: `GATE VERDICT: NOT READY` + `Deferred count: 3` + no citation → `LG-7: `Deferred count:` is 3 with no lawful `Owner deferral decision:` citation — only the owner defers, under any verdict (§5, RD34-07)`. Control with count 0 → 0 errors. |
| RD34-08 | MINOR | R | **closed on the header line; the sibling field is unchecked — RD35-03** | Validator:250–266. **H7 rebuilt**, git on: `Capability 1`, `Project registration`, `honest shape visibility`, `1`, `a`, `The` — **all six rejected**. The full first sentence, the same with a trailing period, and the whole normalized `LAUNCH_TARGET` scalar all pass. Containment is gone. |
| RD34-09 | MINOR | R | **verified-closed** | Delta D-7:104–115 states exactly RD-34's supplied form: *"**§6 carries no project-specific record or narrative; the trend-log path remains, as RD24-17 required.**"* My own sweep of §6 (instrument lines 634–676, **43 lines**, denominator stated) for `.syzygy|Syzygy|Capability|067d8a0|2026-08-09|v1.\d` returns **1** hit: L637, the `TREND-LOG.md` path RD24-17 requires. The delta's claim is now true of the bytes. The frozen v1.6 delta is not edited. |
| RD34-10 | MINOR | R | **verified-closed** | P-34:55–58, option (a): *"`…/LAUNCH-GATE-v1.5-SEMANTIC-DELTA.md` (the RD-24 fresh instrument review's 21 findings closed — **read with the v1.6 delta's D-10**, which corrects two of its claims; the frozen record itself is not edited, RD34-10)"*. The pointer precedes the claims in reading order. |
| RD34-11 | MINOR | R | **verified-closed by execution** | LG-10:314–320. **H5 rebuilt**, git on: extra rows `A9`, `E7`, `G2` each → `LG-10: row ID(s) outside the question roster`; `| A9 | Not met |` under `READY FOR` produces both the roster error and the conjunct error; `| F9 | Not met (out of launch scope) |` is caught first by LG-3's A–D restriction. The E1 sub-row IDs (`E1-form` … `E1-change-process`) are roster members and pass; a mis-cased `E1-Form` is not parsed at all and surfaces as a missing row — conservative in the safe direction. |

**Tally, with its denominator:** of RD-34's **11** findings, **11 are present in the bytes and none is absent**; **7 are closed outright**; **4 (RD34-02, -03, -06, -08) are closed for the case RD-34 demonstrated and leave a residual one level up.** Eight I confirmed by rebuilding RD-34's own records and executing the clone's validator (RD34-01/02/03/04/06/07/08/11); RD34-05 and RD34-09 by sweep with a stated denominator; RD34-10 by reading. `[Inferred]` The repair session did the work the register describes, and — with the one exception in RD35-01 — the register's account is honest about what it did.

---

## New findings

### RD35-01 — BLOCKING — the new citation-existence check rejects every path in this repository's own decision home, and both the offered delta and the register describe a check the bytes do not perform

Validator:172, the line RD34-02's repair added:

```python
if git_show(commit, v.lstrip("./")) is None:
```

`str.lstrip` takes a **character set**, not a prefix. Every citation value beginning `.syzygy/` has its leading `.` stripped and is resolved against `syzygy/governance/…`, which exists at no commit.

`[Observed]` Executed against the real commit `eb53c3e`, git on, inside a full §5-template `READY-WITH-DEFERRALS` record:

| `Owner deferral decision:` value | exists at `eb53c3e`? | validator |
|---|---|---|
| `.syzygy/governance/decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` | **yes** | **REJECTED** — *"path … does not exist at the named commit — a citation to nowhere authorizes nothing"* (3 errors) |
| `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` | **yes** | **REJECTED** (3 errors) |
| `scripts/launch_gate_results.py` | yes | accepted |
| `SDR-33`, `P-34`, `D-10`, `B-7`, `SDR-9999` | — | accepted (shape only) |

`.syzygy/governance/decisions/` is §8's own `C7_POPULATION` — *"the owner decision records (SDR-\*, warrants, pending queue)"* — and the only home a real owner deferral can live in. **The path form of the citation is unusable for every decision the project can actually cite.** A lawful deferral-carrying administration citing its granting decision by path fails validation with three errors, including the two RD34-01 and RD34-07 just added; only the identifier form survives, and identifiers are never existence-checked.

`[Observed]` **No fixture can see this.** Denominator: 43 fixtures, full roll read. The only two path-form citation literals in the selftest are `.syzygy/governance/decisions/SDR-99-EXAMPLE.md` (git **off**, so the existence branch is not taken) and `.syzygy/governance/decisions/NO-SUCH-DECISION.md` (git on, expected to be rejected — and it is rejected, but for the wrong reason: it would be rejected even if it existed). **There is no fixture in which an existing repository path is accepted.** This is verification rule 6 failing in the direction it is least often tested: every predicate was mutated to confirm it *fails*, and the complementary direction — confirm it *passes* when it should — was never fixtured, so a check that rejects its entire lawful input set reads as green.

`[Observed]` Two records the owner reads under P-34 option (a) state this check as fact:

- Delta D-2:47–48 (quoted): *"The `Owner deferral decision:` value must be a repository path — verified to **exist at the record's named commit** when git checks run."* Not true of the bytes for any `.syzygy/` path.
- `DISPOSITION-REGISTER.md:297`, the RD34-02 row (quoted): *"Fixtures: label rejected, nonexistent path rejected, **real-path and identifier forms accepted**."* The real-path fixture does not exist (denominator 43).

`[Inferred]` This is the *identical class* RD34-02 raised — *"the register claims a path check the bytes do not perform"* — recurring inside the repair for RD34-02, and now with the delta joining the register in asserting it. RD33-03's row carries a dated correction for exactly this; the correction's own replacement row needs one. The pattern the three prior reviews established holds: each repair mints the next defect one level up, and this one landed in the record layer the previous instance was corrected in.

*Direction:* `v[2:] if v.startswith("./") else v` (or `PurePosixPath`), a fixture that **accepts** `.syzygy/governance/decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` at the named commit, and a fixture that rejects `.syzygy/governance/decisions/NO-SUCH-DECISION.md` — the pair, not either alone. Correct D-2 and the RD34-02 register row to what the bytes then do.

### RD35-02 — MAJOR — §5's *terminal* line is still not the anchor: the validator takes the last line that happens to **match**, so a qualified terminal verdict is silently discarded in favour of an earlier pass line

§5:607–609 (defined clause, quoted): *"The terminal line's `GATE VERDICT:` token is literal — it is the line the validator parses and the trend row carries."* Validator:396–397 takes `_gv_matches[-1]` — the last **regex match**, not the last `GATE VERDICT:` occurrence. `GATE_VERDICT_RE` anchors on `$`, so any terminal verdict carrying a qualifier fails to match and is skipped.

`[Observed]` **H6-reverse**, git on, real commit and digests, full 39-row template, all rows `Met`:

- summary line: `Summary for the owner: GATE VERDICT: READY FOR Capability 1 — Project registration and honest shape visibility`
- terminal line: `GATE VERDICT: NOT READY — pending the owner's F2 deferral decision`

→ **0 errors**, `record valid`, and the emitted trend row's Gate-verdict column reads `READY FOR Capability 1 — Project registration and honest shape visibility`. **The record's terminal verdict is NOT READY and the trend log receives a pass.**

`[Observed]` The same hole via a benign appendix. A record ending `GATE VERDICT: NOT READY` followed by an appendix quoting §5's own template block:

```markdown
GATE VERDICT: READY FOR <LAUNCH_TARGET> | NOT READY |
  READY-WITH-DEFERRALS (owner only)
```

→ **0 errors**, the parsed verdict is the *template's* line, the record's real NOT READY is discarded, and the emitted trend row has **11 columns** where §6's table has 9 — because the captured verdict text contains `|`. Structural corruption of the log F1 is answered from, with no error raised.

`[Inferred]` RD34-03's own reasoning applies verbatim to what is left: *"the unsafe direction — earlier stricter, terminal laxer — passes silently; the reverse fails loudly, so the asymmetry favours the wrong outcome."* v1.7 fixed the **ordering** and left the **anchoring**. The delta's D-3 claim — *"The pilot record's two-line shape can no longer pick which line the tool sees"* — is false as stated: a two-line record still picks, whenever the terminal line is the one that does not match.

*Direction:* find the last line containing the literal token `GATE VERDICT:`, then require *that line* to parse to a closed verdict word (a terminal `GATE VERDICT:` line outside the closed set is an error, not an invitation to look upward); reject `|` inside the captured verdict; fixture both the qualified-terminal case and the quoted-template appendix.

### RD35-03 — MAJOR — the `GATE VERDICT:` line's launch target is unchecked, so the one string the trend log carries can name any target at all

§4:463 (quoted): *"**READY FOR `<LAUNCH_TARGET>`** = every E question `Met` …"*. §5:603–604 (template, quoted): *"`GATE VERDICT: READY FOR <LAUNCH_TARGET> | NOT READY | READY-WITH-DEFERRALS (owner only)`"*. RD34-08's repair upgraded the **header** `Launch target:` line to normalized equality with §8 and left the **verdict** line at zero checking.

`[Observed]` git on, real digests, header `Launch target:` correct and LG-11-verified, all rows `Met`:

| terminal verdict line | validator | trend row's Gate-verdict column |
|---|---|---|
| `READY FOR Capability 1 — Project registration and honest shape visibility` | clean | as written |
| `READY FOR Capability 7 — full Mission Control and mission prevention` | **clean** | `READY FOR Capability 7 — full Mission Control and mission prevention` |
| `READY FOR anything the reviewer likes` | **clean** | as written |
| `READY FOR the whole system` | **clean** | as written |

`[Inferred]` No failing record passes here — but an administration honestly run against Capability 1 can be recorded, and permanently trended, as a pass for a target §8 never bound, and F1 is answered from that column and only from it. The sibling asymmetry is sharper still: the validator's own `GOOD` fixture and every RD-33/RD-34 record write the fragment `READY FOR Capability 1` in the verdict line, which LG-11 now **rejects** in the header line one field above. The same `<LAUNCH_TARGET>` placeholder carries two enforcement standards in one record, and the delta's D-6 claims the upgrade is *"per §5's 'verbatim'"* without noting that §5 uses the placeholder twice.

*Direction:* apply the same normalized-equality test to the `READY FOR <…>` tail; fixture a mismatched pair.

### RD35-04 — MAJOR — the instrument's self-declared *sharpest single gate* is the one cross-field consistency the validator does not check: a non-empty E3 reopen-list beside `E3 | Met` and a READY verdict validates clean

§3, E3 (defined clause, quoted): *"**E3 [U]** Would authoring the first spec force reopening any vision- or shape-level question? Enumerate them. *This is the sharpest single gate* … *Fails when:* the list is non-empty; **"ready" is then false regardless of every other verdict**."* §5 gives the record a dedicated field: `E3 reopen-list: <empty | enumerated items>`.

`[Observed]` git on, real commit and digests, full 39-row template, all rows `Met`, `| E3 | Met |`, and:

```
E3 reopen-list: (1) whether a Mission is a first-class object; (2) whether evidence adapters are in Wave A; (3) the write-boundary scope
GATE VERDICT: READY FOR Capability 1 — Project registration and honest shape visibility
```

→ **0 errors**, `record valid`, trend row `| … | 0 | 0 | 0 | 0 | 0 | … | READY FOR Capability 1 — … |`. A record that enumerates three reopened shape questions and calls itself ready validates with nothing to say.

`[Observed]` The `E3 reopen-list:` field may also be deleted entirely with 0 errors.

`[Inferred]` This is exactly the shape LG-8 (E1 rollup versus its five sub-rows) and LG-9 (a scoped row versus the deferred-wave findings line) already enforce — a declared field contradicting a verdict row. E3's is the one omitted, and §3 says it is the one that decides. It answers the charter's central question directly: RD-34's claim that *"there is no unchecked verdict branch left to route a pass through"* is **true of the branches and false of the pass** — the route runs through a fully checked branch whose decisive field is unchecked. No instrument amendment is needed; §3 already states the rule.

*Direction:* require the `E3 reopen-list:` field; error when its value is not an empty-marker while `E3` is `Met` or the verdict starts `READY`; use the same placeholder vocabulary LG-9 already owns, so the two share one definition of "names nothing".

### RD35-05 — MINOR — LG-9's widened placeholder set still admits decorated forms of the very word it was built for

`[Observed]` H1, git on, scoped `C2` + `READY FOR`, denominator **18** strings: 10 rejected, **8 accepted** — `unknown`, `tba`, `n.a.`, `see above`, `various`, `several`, **`(none known)`**, **`-- none --`**. The last two contain the literal string RD33-01 and RD34-06 were both about; `fullmatch` over the enumeration does not reach them. `unknown` is doctrine's own VIS-2 word standing in for a named defect. The docstring honestly presents LG-9 as an enumeration and the delta's D-6 lists the set, so nothing overclaims — this is a residual, not a false statement.

*Direction:* require a minimum information content (e.g. a token that is not in the placeholder lexicon after stripping punctuation and articles), rather than extending the enumeration a fourth time.

### RD35-06 — MINOR — `DECISION_ID_RE` accepts identifier families that cannot name a *granted* deferral, and never checks existence

§4:518–521 (quoted): *"A deferral is claimed only by **citation**: the record's `Owner deferral decision:` field names the owner decision (path or identifier) **that granted it**."* Validator:159 accepts `(?:SDR|P|D|B)-\d+[a-z]?(?:\([a-z]\))?`.

`[Observed]` git on, `READY-WITH-DEFERRALS`, `Deferred count: 1`: `P-34`, `D-10`, `B-7`, `SDR-9999` each validate with **0 errors**. In this repository `P-n` is the **pending** owner-decision queue — `P-34` is itself the unmade decision that offers this instrument — and `D-n` is a semantic-delta item number. A record can therefore claim a deferral granted by a decision the repository records as *not yet made*. Identifier citations are never existence-checked even with git on, which the docstring discloses as a shape test; the shape is the part that is too wide.

*Direction:* restrict the identifier form to families that name made decisions (`SDR-n`, warrant identifiers), or resolve identifiers against `C7_POPULATION` at the named commit the way the path form is meant to.

### RD35-07 — MINOR — most of §5's required record fields are unenforced, including the non-authority banner RD24-02 added

`[Observed]` git on, from a clean-validating record, deleting each field in turn — each mutation validates with **0 errors**: `> This administration record is evidence, never an owner act …` (the banner RD24-02 made required), `Reviewer model family:`, `Materials given:`, `Operationalization notes:`, `E3 reopen-list:`, `Unknowns and what would settle them:`, `Reviewer's falsification notes:`. `[Observed]` Relatedly, a `READY FOR` record carrying **22 `Unknown` rows across A–D** and no `Unknowns and what would settle them:` content validates clean — lawful under §4 (*"`Unknown` in launch-scope A–D does not block by itself"*), but §4's companion requirement (*"every Unknown must carry what evidence would settle it"*) has no check and no field requirement behind it.

`[Inferred]` The tool's scope note discloses *"fresh context, family disclosure, full administration"* as non-mechanical, which covers the family line; it does not cover the banner, the reopen-list, or the Unknowns field, each of which is a mechanical presence test the roster check already demonstrates the appetite for.

---

## What passes

`[Observed]` These are executions and sweeps run this session, not inferences:

- **All eleven RD-34 findings are present in the v1.7 bytes; none is absent.** Eight confirmed by rebuilding RD-34's own records and running the clone's validator with git checks on against the real commit and real digests.
- **RD34-01, the BLOCKING finding, is genuinely closed.** H9a/H9b/H9c/H9d all rejected on precisely the failing conjunct; the lawful deferral-carrying record still passes. §4 now states the predicate as a formula, so §4's own boast — *"Every term of this formula is a predicate over the closed verdict vocabulary"* — is true of both pass verdicts for the first time.
- **The trend delta is correct in both directions and the r5 behavior did not regress.** prior-clean → current-scoped counts **1**; prior-scoped → current-plain counts **1**; prior-plain → current-scoped counts **0** (no double count). Both bespoke selftest checks observed passing.
- **The self-test count is honest and every check is fixtured.** 43 fixtures, 0 failing, exit 0 — matching the delta's "**43 fixtures**", P-34:95's "43 in all", and the disposition register. All eleven checks LG-1…LG-11 are made to fire by at least one fixture (denominator 11, computed mechanically this session).
- **A full §5-template record validates clean at the frozen commit, git on.** My independently written R1 — 39 roster rows, every §5 field in §5's order, commit `eb53c3e`, real instrument and §8 digests, `Launch target:` as the `LAUNCH_TARGET` first sentence verbatim — passes with LG-1, LG-2 and LG-11 all executing; the all-`Met` variant under `READY FOR` also passes. §5's template launch-target requirement and LG-11's normalized equality agree.
- **No question was weakened, no ID renumbered.** Denominator: 35 question stems. **Zero question blocks differ** v1.6→v1.7; IDs identical and in identical order; `*Fails when:*` 33 → 33; §3 is byte-identical in full.
- **"What did not change" is accurate to the byte.** §1, §2, §3, §5, §7 and §8 are byte-identical v1.6→v1.7 (per-section sha256); §8's digest `01209c0f…` is unchanged across three amendments; the closed verdict vocabulary and the `READY FOR` conjuncts are unchanged. §4's one deleted sentence (v1.6's *"The validator enforces the split (LG-6/LG-7) …"*) is subsumed by the superseding formula — the delta's *"gained its explicit predicate and lost nothing"* holds.
- **RD34-05's repair removes the class.** Both routed files are version-neutral; my 345-file sweep found **no stale current-facing version reference anywhere** — the remaining 50 hits are delta filenames, changelog back-references, frozen reviews, the v1.3 pilot under its banner, and the current v1.7 in P-34, `PENDING-OWNER-DECISIONS.md:185` and `PROJECT-STATUS.md:129`.
- **D-7 is now true of the bytes.** §6, 43 lines, one project-specific token — the trend-log path RD24-17 requires. The over-assertion RD34-09 named is corrected in the honest form RD-34 supplied, without editing the frozen v1.6 delta.
- **P-34 is coherent about v1.7.** The question names v1.7; the offer-status block states *"not yet offerable"* and the RD-35 precondition; the D-10 pointer sits inside option (a) before the v1.5 delta's claims; the fixture count is right; option (b)'s v1.8 ordering (RD33-11) is present and correctly reasoned — amendments into the working tree **before** step 2's digest; the approval block names v1.7; the F5-promotion amendment is priced honestly as leaving no same-family administration able to read READY.
- **The clone stayed byte-clean.** `git rev-parse HEAD` = `eb53c3ea…`, `git status --porcelain` empty, subject digest `c0b0dca4…` unchanged, verified at open and at close.

---

## Overall assessment — may v1.7 be offered to the owner at P-34, and may the formal administration run on this validator?

This is the best batch of the three. RD-34's BLOCKING finding is closed properly rather than patched: §4 states the `READY-WITH-DEFERRALS` predicate as a formula, the validator hoists the conjunct battery above the branch split, and I could not construct any all-`Not met`, missing-E, failing-F1/F3/F4 record that survives under either pass word. The scoped-delta rule is right in both directions with no regression of the behavior RD-34 verified. RD34-05's repair chose to remove the recurrence class rather than detect it, and a 345-file sweep says it worked. The delta's "what did not change" section is not merely asserted — every clause of it is a byte fact I recomputed, and D-7 is the rare case of a delta correcting its own predecessor's over-assertion in the exact words the reviewer supplied.

And the convergence claim is **half right in a way that matters.** RD-34's judgment was *"after RD34-01 there is no unchecked verdict branch left to route a pass through."* I attacked it by enumerating the branches — `READY FOR`, `READY-WITH-DEFERRALS`, `NOT READY`, missing line, malformed line — and the claim holds **of the branches**: I could not route a formula-failing record through either pass word. What it does not cover is that a pass need not travel through an unchecked branch. It can travel through a checked branch whose decisive field is unchecked (**RD35-04**: three enumerated reopen-list items beside `E3 | Met` and `READY FOR`, validating clean, against §3's own *"'ready' is then false regardless of every other verdict"*); or it can be attached to the record *after* the branch check, in the one string the trend log carries (**RD35-03**: `READY FOR anything the reviewer likes`, clean); or it can be selected from the wrong line entirely, with the record's real terminal verdict discarded and §6's nine-column table structurally broken (**RD35-02**, which is RD34-03's own "earlier stricter, terminal laxer" asymmetry surviving one turn of the screw, and which falsifies the delta's D-3 sentence about the pilot's two-line shape).

The pattern the three prior reviews established therefore holds a fourth time, and it landed where RD-34 pointed: the repairs for RD34-02, -03 and -08 each closed the demonstrated string and left the class one level up, and the repair for RD34-02 additionally shipped **inverted** — `v.lstrip("./")` rejects every path under `.syzygy/`, which is to say every owner decision this project can cite (**RD35-01**). That one is decisive for the offer rather than merely for the tool, because the v1.7 delta's D-2 and the disposition register's RD34-02 row both tell the owner the check works, and the register additionally claims a "real-path accepted" fixture that does not exist among the 43. The fixture set cannot see the bug, because every path fixture asserts a rejection and none asserts an acceptance — the exact blind spot verification rule 6 exists to close, in the one repair whose register row had *already* been corrected once for describing a check the bytes did not perform.

There is one genuinely good sign that distinguishes this round from its two predecessors: **none of my seven findings requires an instrument amendment.** §5 already says "terminal", §4 and §5 already say `<LAUNCH_TARGET>`, §3 already states E3's fail condition, §4 already requires the Unknown-settling evidence. Every repair is validator work plus two record corrections (D-2 and the RD34-02 register row). RD-33's and RD-34's rule — an instrument sentence must travel *in* the offer — does not bite here, and the question of whether the packet must be re-frozen is correspondingly lighter.

So, on the two questions asked:

- **May v1.7 be offered at P-34?** Not as it stands. The instrument bytes themselves are in the best shape they have been in — I found nothing wrong with §4, §6 or the changelog, and P-34's mechanism, ordering, options and precondition are all correct. But an owner reading option (a) is told, in the offered delta and in the register behind it, that deferral citations are existence-verified and that a real-path fixture proves it, and neither is true of the bytes. That is RD-8's "surprised, not knowing" class in a document whose whole purpose is to make the act knowing. Correct D-2 and the register row (and fix the `lstrip`, so the correction can say the check works), and the offer is sound.
- **May the formal administration run on this validator?** No. A lawful `READY-WITH-DEFERRALS` record citing its granting decision by path cannot validate; a record whose terminal verdict is qualified has its verdict read from a different line; the verdict string entering the trend log is unconstrained and can contain `|`; and the instrument's sharpest single gate is unchecked. Any of the four would contaminate Administration 1, which is the row every later F1 verdict is read against.

The remaining batch is small, mechanical, and — unlike the last two — needs no owner-visible instrument text: fix the `lstrip` and fixture an accepted real path; anchor on the last `GATE VERDICT:` **occurrence** and reject a terminal line outside the closed set; apply the launch-target equality test to the verdict line and forbid `|` in it; add the E3 reopen-list cross-check beside LG-8 and LG-9; tighten the identifier families; require §5's remaining declared fields. Then correct D-2 and the RD34-02 register row, one more short re-review of the v1.8 delta, and the offer. I will not repeat RD-34's prediction that this is the last batch — three administrations have now each found the next class exactly where the previous repair stopped, and the honest reading of that trend is that the *instrument* has converged while the *validator* has not.

VERDICT: REVISE
