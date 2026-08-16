# RD-61 — Launch-policy v2.2 semantic review (round-2026-08h, subject `918574c`)

| | |
|---|---|
| Review ID | **RD-61** |
| Date | **2026-08-16** |
| Role | Launch-policy semantics reviewer — the fresh-context re-review of the bytes RD-55 (`REVISE`) produced |
| Frozen commit | **`918574c`** (`918574c97c29a33ed76e44b27250b557160ddcd7`) |
| Subject 1 | `launch-gate-pre-specifications.md` — sha256 `ac8751236ec7434c20606b404d41c885d29f67dd5f3dab8c9d0cbb90de670977` **(verified at start and end of this review)** |
| Subject 2 | `launch-gate-administration.schema.json` — sha256 `e0167fb8af6a903c527d402d56c4fb85ebdfed9608de1a485f4f1563aa6a69fb` **(verified)** |
| Subject 3 | `scripts/validate_launch_administration.py` — sha256 `dbb8b69097df15a4bf60cc6fc0cef1043b838a22d30920f1914da31a91322977` **(verified)** |
| Context | **Fresh.** No prior contact with this repository, this instrument, or its review history beyond the brief, RD-55's raw output and the v2.2 semantic delta, both of which were supplied as context |
| Model family | **Same as the corpus's authors.** This review therefore **supports repair** and is **NOT the formal launch administration** (instrument §2's family-disclosure requirement; question F5) |
| Nothing edited | The frozen worktree was never written to. `git status --porcelain` is empty and all three subject digests are unchanged at the end of the session. All probe records, mutated scripts and scratch clones live under `…/scratchpad/rd61-scratch/` |

Line numbers below are 1-indexed into the frozen `launch-gate-pre-specifications.md`
(2236 lines) and `scripts/validate_launch_administration.py` (2213 lines) unless
otherwise marked.

---

## Findings table

| # | Severity | Section / site | One line |
|---|---|---|---|
| **f1** | **BLOCKING** | §5 line 771; `validate_launch_administration.py` 605–622 | The schema is read from the **working tree** and compared to the committed bytes **never** — only its *path* is checked — while §5 newly claims the check is "the schema's own identity … anything but the **committed** schema is not validated". A one-line, audit-clean in-place edit yields an **eligible** record carrying a §2-forbidden verdict word and a `READY FOR …` gate result |
| **f2** | MATERIAL | §2 lines 126–129; validator 647, 671–756 | `repository_commit` is anchored to nothing reachable. A record naming an **off-branch** commit whose §8 has been rewritten validates with **zero errors**, is **eligible**, and deposits `READY FOR Everything, immediately` into the §6 trend row |
| **f3** | MATERIAL | §5 line 774; validator 475–489, 956–962 vs 963–998 | The `SDR-n` deferral branch resolves a citation whose only occurrence is a **narrative mention in `launch-gate/HISTORY.md`** — a file the path branch refuses by name as "an index, a queue or a log". §5's new clause, and the code's own comment *"One list, both branches"*, are false of the identifier branch |
| **f4** | MATERIAL | §5 line 768; validator 744–756; schema `$defs`/`e4` | `e4.routing_authority: " "` passes the schema's `minLength: 1`, normalizes to the empty string, and the `elif got_ra and …` guard makes **`LA-3b` not run at all** — the check §5 enumerated for the first time at v2.2. Eligible, zero errors, `READY FOR` |
| **f5** | MATERIAL | §2 lines 134–138; §4 line 646; §6 lines 805–807; validator 1280–1306 | §2 makes it an **integrity requirement** that a same-family administration be disclosed "in the record **and the trend row**"; §6's fixed nine-column table has no such column, the generated row emits none, and §6 forbids hand-typing a row. The obligation cannot be met by the mandated generator |
| **f6** | MATERIAL | §6 lines 798–802; validator 1062–1077, 1207–1240 | RD-56 f6's repair (resolve the prior-record path inside the repository) covers only the **record-declared** path. `--prior` still reads a file **outside** the repository and zeroes §6's New-findings column — F1's own evidence — on a record with **zero errors** and `eligible: true` |
| **m1** | MINOR | §5 lines 751–752 | *"A record that does not validate is not rendered at all."* Still literally false: `--allow-invalid` renders one. v2.2 repaired the tool's output rather than the clause RD-55 showed to be false |
| **m2** | MINOR | §4 line 509 | *"Row/formula outcome \| Always. It is a function of the rows and nothing else."* False of §4's own formula: the E3 conjunct reads `e3.reopen_items` and the F2 limb reads `owner_deferrals`, neither of which is a row |
| **m3** | MINOR | §4 lines 519–521 vs validator 1289–1290, 1261 | The trend column emits `NONE — not eligible; row outcome was …` and names **no limb**, though §4 says the gate result is "`NONE`, followed by the limbs it failed"; and `_compute`'s `gate_result` still spells the fourth outcome `NO FORMAL GATE RESULT` — a fourth literal, now unreachable rather than removed |
| **m4** | MINOR | §9 line 1047 | The v2.1 changelog entry still asserts the fixture count is *"printed by `--selftest` and stated nowhere else"* — the unscoped form RD-55 f10 flagged. Falsified by the v2.2 delta's own Fixtures block (`101` / `31`). v2.2 scoped the claim in the delta and left it standing in the instrument |
| **m5** | MINOR | §4 lines 614–618 vs 619–631; validator 1184–1189 | §4 says "**any other owner deferral a pass rests on**" converts the verdict word, while its own `READY-WITH-DEFERRALS` predicate admits "exactly one substitution". The tool resolves the tension by erroring — and **two of the three LA-12 contradiction branches are unreachable by construction**: deleting both leaves `--selftest` at 101/101 |

**1 BLOCKING, 5 MATERIAL, 5 MINOR.**

> **Identifier disambiguation.** `f1`–`f6` and `m1`–`m5` above are **this
> review's** findings, and §D expands them under those labels. §C's table
> dispositions **RD-55's** ten findings, whose own labels are also `f1`–`f10`;
> every reference to them in this file is written `RD-55 f<n>`. Where a bare
> `f<n>` appears outside §C it is RD-61's.

---

## A. Byte-identity and the differential — what actually moved

### A.1 The delta's span table reproduces, preamble included

`[Observed]` I ran the v2.2 delta's published script verbatim (its
§"What did not change" block, which **now digests `p[0]`** — the repair
RD-55 f3 asked for) against `git show 939363f:launch-gate-pre-specifications.md`
and the frozen file, **before reading the delta's published values**.
Denominator: **all 10 spans** (preamble + §1–§9), which exhaust both files;
`re.split` yields the same nine headings in each text and the spans are
contiguous from byte 0 to EOF.

| Span | delta publishes | I computed | agree |
|---|---|---|---|
| §0 preamble | `08b200cd4581d4b9 -> 3cff94f230056b52` | same | yes |
| §1 | `1f2d1d60a28ada2a` identical | same | yes |
| §2 | `0d7340f2ee9a8b8c` identical | same | yes |
| §3 | `fe0b051e136d2fee` identical | same | yes |
| §4 | `84d5d3d456e7c05a -> 8af5dbc5b7d82af1` | same | yes |
| §5 | `0b63585544520df4 -> 1fd518196e437f6e` | same | yes |
| §6 | `9906fcac454062cd` identical | same | yes |
| §7 | `9e17cb8de0458976` identical | same | yes |
| §8 | `01209c0f052971f7` identical | same | yes |
| §9 | `9301d992b12b889a -> 18029b54c3de4e61` | same | yes |

10 of 10 rows reproduce, and both whole-file digests reproduce
(`3afdffda…` → `ac875123…`).

**Second method.** `git diff -U0 939363f HEAD -- launch-gate-pre-specifications.md`
produces **9 hunks**. Mapping each hunk's old-file line against v2.1's section
boundaries: preamble 1 (line 7, the version bump); §4 5 (495, 505, 508, 620,
622); §5 2 (735, 749); §9 1 (971). **Zero hunks in §1, §2, §3, §6, §7, §8.**
Denominator: all 9 hunks of the complete diff. The two methods agree.

`[Observed]` **RD-55 f3 is repaired at the method level**: the omission that
let the v2.1 delta assert a preamble byte-identity its own script could not
see is gone, and the preamble row now appears — showing the change rather
than hiding it.

### A.2 Nothing was dropped, renamed, weakened, or made unreachable

| Population | v2.1 | v2.2 | Δ | direction |
|---|---|---|---|---|
| §3 question text | byte-identical span digest `fe0b051e136d2fee` | same | 0 | — |
| §6 trend-log rules and column header | byte-identical `9906fcac454062cd` | same | 0 | — |
| §8 parameter block | byte-identical `01209c0f052971f7` | same | 0 | — |
| `ROSTER` (validator) | 39 entries | **string-identical** | 0 | — |
| Computed conjunct labels (`_c("…")`) | 6, in order | **identical list** | 0 | — |
| `LA-*` identifiers the validator can emit | `LA-1,2,3,3b,4,…,16` (17 distinct) | **identical set — 0 dropped, 0 added** | 0 | — |
| Row verdict enum (schema) | 4 words | schema byte-identical (`e0167fb8…` at both commits) | 0 | — |
| §4 gate verdict words defined | 3 | 3, plus **`NONE` named** for the fourth outcome | **+1** | **completion** |
| §4 eligibility limbs | **4** (stated), 3 implemented | **5** stated **and** implemented | **+2** | **strengthening** |
| §5 named checks | `LA-1 … LA-16` | `LA-1 … LA-16, and LA-3b`, plus schema identity and the warrant-negation list | **+** | **completion** |

`[Observed]` Extraction method for the last three code rows: `re` over both
revisions of `validate_launch_administration.py` for `ROSTER = ( … )`,
`_c("…"` and `"(LA-\d+[a-z]?):`. `ROSTER` compares string-identical;
the conjunct list compares element-identical; the emitted-identifier sets
compare equal with empty symmetric difference.

### A.3 Differential execution — 30 records, both validators

`[Observed]` I cloned the frozen worktree twice (`918574c` and `939363f`),
built a lawful `formal/full/fresh` base record **independently in each tree**
(so each binds to its own instrument digest), and applied the same 30
mutations on both sides. Acceptance is defined as *zero errors **and**
`eligible: true`* — the pair a launch decision would rest on.

| Direction | count | cases |
|---|---|---|
| **Weakened** (rejected at v2.1, accepted at v2.2) | **0** | — |
| Stricter (accepted at v2.1, rejected at v2.2) | 2 | `defer_trendlog`, `prior_outside` |
| Same acceptance, more errors reported | 2 | `defer_pending` (1→3), `defer_nonexistent_sdr` (1→3) |
| Same acceptance, **eligibility flipped `true`→`false`** | 14 | every invalid-but-formal record — the f1 repair |
| Unchanged | 12 | — |

`[Observed]` **I could not construct a record that fails under v2.1 and
passes under v2.2**, over a 30-case battery covering: administration kind,
formality, fresh-context, forged instrument and parameter-block digests,
launch-target and wave mismatch, E3 reopen items, undisclosed scoped rows,
Met-without-evidence, placeholder G1 and placeholder falsification, six
deferral-citation shapes, E4 paraphrase, blank and wrong routing authority,
fabricated evidence paths, gate-word forgery in free text, E1 rollup,
missing and invented roster rows, and an escaping prior-record path.
`[Inferred]` No new pass route was opened by the amendment; 30 targeted
cases plus the identity of the deciding code is not a proof over the
record space.

`[Observed]` **The verdict-deciding code is unchanged.** The six conjuncts,
their order, their labels and the three-way branch (`plain` /
`deferrals` / `blocked`) are element-identical between the two revisions.
Every v2.2 change to `_compute` is *additive*: the `prior_errors`/`git_ok`
parameters, the `resolved_deferrals` limb, the repository-containment test
on the prior path, and the relocation of the eligibility block to last.

`[Observed]` **Conclusion on commission item 2: no readiness meaning was
weakened.** No question moved (§3 byte-identical), no verdict word was
dropped (three defined, a fourth named), no conjunct was dropped or
renamed, no `LA-*` check disappeared, and no parameter changed.

---

## B. Policy / formula identity — does the prose say what the tool computes?

### B.1 The three results are separated, in the instrument and at every surface

`[Observed]` §4 lines 507–511 state three outcomes in a table, and lines
519–525 name the fourth result `NONE`. `_compute` returns them as three
distinct keys (`verdict`, `eligible`, `gate_result`, validator 1263–1277),
and every surface prints two lines rather than one:

```text
$ validate_launch_administration.py <forged-instrument-digest>.json --trend-row
Row/formula outcome: READY FOR Capability 1 — Project registration and honest shape visibility
Formal gate result:  NONE — diagnostic only (the record has 1 validation error(s))
…
Trend row (§6):
| 2026-08-11 | 918574c | 0 | 0 | 0 | 0 | 0 | n/a (no prior record) | NONE — not eligible; row outcome was READY FOR Capability 1 — … |

1 validation error(s):
  LA-2: instrument digest mismatch — the record quotes 000000000000…, the committed instrument is ac8751236ec7…
```

and the generated report:

```text
ROW/FORMULA OUTCOME: READY FOR Capability 1 — Project registration and honest shape visibility
GATE VERDICT: NONE — this administration is not eligible to be cited as launch evidence (the record has 1 validation error(s)). The outcome above is diagnostic.
```

`[Observed]` **An ineligible administration cannot produce a formal
`READY FOR` result at any of the four surfaces** — CLI gate line, CLI trend
row, report terminal line, report-embedded trend row. This is the RD-55 f1
defect, and it is closed. See §C.f1 for the mutation evidence.

### B.2 The five eligibility limbs, clause by code

§4 line 510, quoted from the defined clause:

> **Administration eligibility** | Separately determined, and **conjunctive
> over five limbs**: the record is `formal`; `administration_kind` is `full`;
> the reviewer declares fresh context; the record validates with **zero**
> errors; and the checks that bind it to the repository actually ran …

| Limb | Code | Verified by construction |
|---|---|---|
| `formal` | 1247–1248 | `nonformal` → `eligible: false`, 0 errors |
| kind `full` | 1249–1251 | `delta` → `eligible: false` |
| fresh context | 1252–1253 | `nofresh` → `eligible: false` |
| **zero errors** | 1254–1255, `n_err = len(prior_errors) + len(errs)` | `forge_inst`, `forge_pb`, `badtarget`, `badwaves`, `reopen`, `met_no_evidence`, `g1_placeholder`, `e4_paraphrase`, `e4_routing_wrong`, `ev_fake`, `e1_rollup`, `missing_row`, `falsification_placeholder`, `plain_with_deferral` — 14 cases, all `eligible: false` |
| **git ran** | 1256–1259, `git_ok=bool(_git)` | `_git=False` → 0 errors, **`eligible: false`**, note recorded |

`[Observed]` The ordering matters and is honoured: `_compute` is invoked
**last** (validator 1092–1095) with `prior_errors=errors`, and its own
`LA-12` errors are appended to `errs` *before* line 1245 counts them. I
checked every `errs.append` in `_compute`: all three sites (1157, 1185,
1188) precede the count.

`[Observed]` The CLI's private `and not errors` is gone; `trend_row()`
(1286) and the renderer (line 425) both read the one `eligible` key.

### B.3 The formula, term by term

§4's rule, lines 537–547, against `_compute` 1127–1169:

| §4 term | Code | Identical? |
|---|---|---|
| every E question `Met` | `all(verdict_of.get(q) == MET for q in E_ROWS)`, `E_ROWS` = every roster id starting `E` — E1's five sub-rows included | yes |
| no `Not met` in launch-scope A–D; a scoped row does not block | `[q for q in AD_ROWS if verdict_of.get(q) == NOT_MET]` | yes — and `LA-5` (768–776) forces `verdict`/`launch_scope` agreement, so a plain `Not met` always carries in-scope |
| F1 `Met` or `Unknown` | `verdict_of.get("F1") in (MET, UNKNOWN)` | yes |
| F3 `Met` | `== MET` | yes |
| F4 `Met` | `== MET` | yes |
| F2 `Met` **or** owner-deferred with a bounded plan | `f2_met` / `f2_deferred`, with `LA-11` (1016–1020) refusing a placeholder `bounded_reduction_plan` | yes |
| E3's reopen list is empty | `not rec["e3"]["reopen_items"]` | yes |

§4 lines 624–631, the `READY-WITH-DEFERRALS` predicate:

> every conjunct of **READY FOR `<LAUNCH_TARGET>`** above … with exactly one
> substitution: the F2 limb is satisfied by an **owner-cited deferral**
> (`owner_deferrals[].decision_citation`) instead of `Met`, AND
> `len(owner_deferrals)` is nonzero AND the citation resolves.

`[Observed]` The **resolving-citation limb is now implemented** — v2.1
selected the branch from the count alone. `resolved_deferrals` is populated
only where `LA-11` actually resolved a warrant (validator 962, 998), and the
branch at 1164 requires `_f2_citation_resolves`; a deferral whose citation
does not resolve raises `LA-12` at 1157. Verified: `SDR-9` (a real decision)
→ `READY-WITH-DEFERRALS`, 0 errors, eligible; `SDR-9991`, the pending queue,
and `launch-gate/TREND-LOG.md` → 3 errors each, `NOT READY`, ineligible.

`[Observed]` The non-F2 conjuncts are non-deferrable in code:
`NEVER_DEFERRABLE = frozenset(E_ROWS) | frozenset(AD_ROWS) | {"F1","F3","F4"}`
(validator 209), matching §4 line 632 exactly.

### B.4 Where the prose and the computation still disagree

Three residues, all recorded as findings: **m2** (the "function of the rows
and nothing else" characterisation), **m3** (the trend column omits the
limbs `NONE` is supposed to be followed by), **m5** (the "any other owner
deferral" clause versus the exactly-one-substitution predicate, plus two
unreachable `LA-12` branches).

---

## C. RD-55's ten findings — independently verified against the v2.2 bytes

I did not take the delta's dispositions on trust; each row below was tested.

| RD-55 | Severity | Closed? | Evidence at `918574c` |
|---|---|---|---|
| **f1** — §4's fourth eligibility limb unimplemented; the §6 trend row leaks `READY FOR` for an invalid record | BLOCKING | **CLOSED — verified by construction** | Two records identical but for `instrument.sha256`, forged to `0…0`: the clean one prints `Formal gate result: READY FOR …` and a trend row ending `\| READY FOR Capability 1 … \|`; the forged one prints `Formal gate result: NONE — diagnostic only (the record has 1 validation error(s))` and a trend row ending `\| NONE — not eligible; row outcome was READY FOR … \|`. The report's terminal line is `GATE VERDICT: NONE — this administration is not eligible …`. Under v2.1 the two trend rows were byte-identical; under v2.2 they differ. Verified at all four surfaces, plus the **fifth limb**: `_git=False` gives 0 errors and `eligible: false` |
| **f2** — §5 retook the check enumeration in the pass that added `LA-3b`, which the list did not name | MATERIAL | **CLOSED** | Sweep of the whole instrument, denominator 2236 lines: `LA-3b` now occurs **3×** (was 0) — §5 line 754 `(``LA-1`` … ``LA-16``, and ``LA-3b``, each with at least one mutation fixture)` and line 768 `the E4 routing authority's binding to §8 (``LA-3b`` — named here at v2.2 …)`, plus the §9 entry. *(But see **f4** below: the check the enumeration finally names can be switched off from the record.)* |
| **f3** — the v2.1 delta asserted a preamble byte-identity its own script could not check | MATERIAL | **CLOSED as a correction** | The v2.1 delta is correctly left frozen. The v2.2 delta §"Corrections to the v2.1 delta" item 1 states the correct claim, and its published script digests `p[0]`. I reproduced all 10 spans including the preamble (§A.1) |
| **f4** — the `LG-6/LG-7` half of RD-48 f1 was annotated, not corrected, and three documents said otherwise | MATERIAL | **CLOSED** | §4 line 636 is now *"the validator runs the full conjunct battery on both branches (`LA-12`)"*. Sweep of preamble + §1–§8, denominator 994 lines: `LG-6` 1 hit, `LG-7` 1 hit — **both on line 640**, inside the historical note that describes what v2.1 failed to do. No live clause cites an `LG-*` check for the structured path. `LA-12` is the correct identifier and is emitted at validator 1157/1185/1188 |
| **f5** — D-8's "equivalent-or-stronger" did not cover the gate-verdict half | MINOR | **CLOSED as a concession** | v2.2 delta corrections item 2 concedes exactly RD-55's narrow point: *"For gate verdicts the successor … is §4's prose, so prose replaced prose. The not-restoring decision stands; **its stated reason was too broad**"*. §2 is byte-identical, so nothing was restored — which is the disclosed disposition, not a hidden one |
| **f6** — §4's closed-set clause was unenforced and the record could carry the words | MINOR | **CLOSED by narrowing — and the narrowed claim independently verified** | §4 lines 495–502 now read *"**A record carries no verdict field** … and the schema's closure refuses one"*. Verified: a record with a top-level `"final_verdict": "READY FOR everything"` fails with `LA-1: $: unknown field 'final_verdict' — the verdict is computed, never claimed`. The clause's supporting ground — *"the report renders every free-text field as data, so a quoted verdict cannot present itself as the report's own"* — was tested by an exhaustive sweep: **814 string-leaf injections across two record shapes (403 + 411 leaves), 0 leaks.** See §D.1 |
| **f7** — `stale` named an ineligibility ground nothing defined or computed | MINOR | **CLOSED** | Sweep for `\bstale\b` over preamble + §1–§8, denominator 994 lines: 6 hits, of which **five** are about stale *claims in documents* (§2's F2/F4/C3 reconciliation, D1's fails-when, F4's fails-when, F1's rationale, §6's column history) and the sixth is line 515, the historical note *"`stale` named no limb, defined nothing, and was computed nowhere — RD-55 f7"*. No live clause names a stale administration |
| **f8** — the fourth gate result had three spellings and no instrument definition | MINOR | **PARTIALLY CLOSED** | §4 lines 519–525 define the literal `NONE`; all three *surfaces* now begin with it (CLI `NONE — diagnostic only (…)`, report `GATE VERDICT: NONE — this administration is not eligible … (…)`, trend column `NONE — not eligible; row outcome was …`). **Residue:** the trend column names no limb though §4 says the gate result is *"the literal `NONE`, followed by the limbs it failed"*, and `_compute`'s `gate_result` value is still the fourth literal `NO FORMAL GATE RESULT` (validator 1261) — unreachable rather than removed. Recorded as **m3** |
| **f9** — the packet routed to a register with no RD-47/RD-48 rows | MINOR | **CLOSED** | `FORMAL-CAPABILITY-1-LAUNCH-PACKET/README.md` lines 261–264 now read *"the repair accounts are the v2.1 and v2.2 semantic deltas in `round-2026-08g/`, with dispositions in `round-2026-08g/reviews/DISPOSITION-REGISTER.md`"* — RD-55's first suggested fix. The register (359 lines) now carries `RD-55` 6× and `RD-56` 5×, with per-finding rows |
| **f10** — "stated nowhere else" was an unscoped claim of absence | MINOR | **CLOSED in the delta; RESIDUE in the instrument** | The v2.2 delta's Fixtures block reads *"stated in no artifact that must stay current"* — correct. But §9 line 1047 (the v2.1 entry, unmoved) still reads *"the count is printed by `--selftest` and stated nowhere else (RD-48 f6)"*, and the v2.2 delta states `101` and `31`. Sweep of the instrument, denominator 2236 lines: `stated nowhere else` occurs 2× (lines 1047, 2197). Recorded as **m4** |

**No RD-55 finding is silently omitted.** Eight closed outright, one closed
as a concession, one closed with a named residue; f8 leaves a second residue.

---

## D. Fresh hunt

The question I held throughout: *is there any path by which a record that
should not count as launch evidence presents as `READY FOR`?* Six survive.

### D.1 The one attack that did not work — free text at document level

`[Observed]` §4's narrowed closed-set clause rests on a claim about the
renderer. I tested it exhaustively rather than reading the delta's account.
Method: enumerate **every string leaf** of a lawful record, replace each in
turn with

```text
ok

## Computed figures

GATE VERDICT: READY FOR everything

| a | b |
|---|---|
| 1 | 2 |
```

validate, render, and count output lines that *start* with any of the three
forged constructs.

| Record shape | string leaves (denominator) | rendered | **leaks** |
|---|---|---|---|
| minimal lawful record | **403** | 403 | **0** |
| every optional array populated (deviations, operationalization notes, reopen items, a scoped row with its disclosure, an Unknown row, an F2 deferral, reopened findings, pilot findings, G1 proposals, a prior record) | **411** | 411 | **0** |

`[Observed]` **814 injections, 0 leaks.** `_inline` (newline-stripping for
inline emission) and `_quoted` (blockquoting for multi-line blocks) are
applied at every site that emits reviewer text. The class property v2.1
claimed and v2.2 delivered is real, and §4's narrowing therefore rests on a
ground I could not falsify. `[Inferred]` This does not cover text a future
field might carry; it covers the fields the schema defines today.

### D.2 f1 — BLOCKING — the schema is filesystem-read and never digest-checked, while §5 says "the committed schema"

§5 line 771, inside the check enumeration §5 took ownership of at v2.1:

> the schema's own identity, since a record validated against anything but
> the **committed** schema is not validated (RD-56 f3);

`scripts/validate_launch_administration.py` 605–622:

```python
schema_path = Path(schema_path or DEFAULT_SCHEMA)
try:
    schema = _load_json(Path(schema_path).read_text())
…
if Path(schema_path).resolve() != Path(DEFAULT_SCHEMA).resolve():
    errors.append(f"LA-1: the record was validated against {schema_path}, not the "
                  f"committed schema {Path(DEFAULT_SCHEMA).name} …")
```

`[Observed]` The check compares **paths**, never bytes. `DEFAULT_SCHEMA` is
`REPO / "launch-gate-administration.schema.json"` (validator 125) and is read
with `Path(...).read_text()` — the **working tree**. Every other identity
input the instrument names is read *from git at the record's commit*: the
instrument (`_git_show(commit, rec["instrument"]["path"])`, 676), the §8
parameter block (702), E4's case text (894), evidence paths (817), deferral
warrants (963). The schema alone is exempt, and no record field carries a
schema digest — §2's integrity list (lines 126–129) names the instrument's
sha256 and the parameter block's sha256 and nothing else.

`[Observed]` **Constructed and executed**, in a scratch clone at `918574c`.
I made one audit-clean edit *in place at the default path* — appending
`"Met (with caveats)"` to `$defs/question_result/properties/verdict.enum`,
leaving `additionalProperties: false` and every root `properties` intact, so
`_audit_root_is_a_record_schema` and `_audit_schema` both pass — and then
validated a `formal/full/fresh` record whose **A1 row reads
`"Met (with caveats)"`**:

```text
errors= 0 eligible= True
trend: | 2026-08-11 | 918574c | 0 | 0 | 0 | 0 | 0 | n/a (no prior record) | READY FOR Capability 1 — Project registration and honest shape visibility |
```

The forbidden word is invisible to every counter — it is neither `Met`,
`Not met`, `Not met (out of launch scope)` nor `Unknown`, so `n_not_met`,
`n_scoped` and `n_unknown` all read 0 and `ad_blockers` is empty. §2 line 145
forbids exactly this word: *"No 'partially met,' no 'met with caveats' — a
caveat that matters makes it `Not met`"*. §5's third property — *"Scope
cannot be laundered by wording"* — is defeated one level below the record.

Two coarser edits *are* caught: `additionalProperties: true` raises
`LA-1: #: object schema declares 'properties' without 'additionalProperties: false'`.
So the audit is real; it is the **byte identity** that is absent.

`[Inferred]` **Severity.** I grade this BLOCKING and state the precondition
plainly so the owner can re-grade: the attack needs write access to the
working tree, which the forged-digest attack RD-55 graded BLOCKING did not.
What makes it blocking in my reading is that (a) §5 states the check in the
word **committed** and the tool implements path equality, which is the exact
species RD-55 named three times — *a repair narrower than the claim made for
it*; (b) the schema is the instrument's own "machine annex" (§5 line 673),
so its integrity is the ground everything else stands on; (c) the outcome is
an eligible record with a `READY FOR` gate result and a forbidden verdict
word, deposited into the log F1 is answered from and only from; and (d) the
repair is small — compare the working-tree schema's sha256 against
`_git_show(commit, "launch-gate-administration.schema.json")`, exactly as
`LA-2` does for the instrument, and add the digest to the record.

*Fix:* digest-bind the schema at `repository_commit` under `LA-1`, and
consider a `schema_sha256` record field so the binding is carried, not
recomputed. Fixture in the failing direction: a working-tree schema whose
bytes differ from the committed one must not produce an eligible record.

### D.3 f2 — MATERIAL — `repository_commit` is anchored to nothing

§2 lines 126–129 (administration integrity):

> - The instrument must be **committed at the administered commit**, and the
>   record carries the instrument's sha256 and the parameter block's sha256.
> - The record names the commit, and every citation is verified against it.

`[Observed]` Every identity check reads the instrument, §8, E4's cases and
the launch target **at the record's own commit** (validator 676–756). Nothing
requires that commit to be an ancestor of, equal to, or reachable from any
branch. `_commit_exists` (446) asks only whether the object exists. By
contrast `LA-15` (1054–1061) *does* require the **prior** record's commit to
be an ancestor of the record's — so ancestry is already a test this
instrument knows how to apply; it is applied to the prior commit and not to
the record's own.

`[Observed]` **Constructed and executed.** In a scratch clone I created an
unmerged branch whose §8 reads `REQUIRED_WAVES: [A]`,
`DEFERRED_WAVES: [A, B, C1, C2, D1, D2]` and
`LAUNCH_TARGET: > Everything, immediately.`, committed it, returned the
working tree to `918574c`, and built a `formal/full/fresh` record naming that
off-branch commit with the digests it actually has:

```text
commit named: ce999a02   errors= 0 eligible= True
trend: | 2026-08-11 | ce999a0 | 0 | 0 | 0 | 0 | 0 | n/a (no prior record) | READY FOR Everything, immediately |
record waves: ['A'] ['A', 'B', 'C1', 'C2', 'D1', 'D2']
git merge-base --is-ancestor <that commit> 918574c  →  exit 1  (not an ancestor)
```

Every check passes because every check reads the parameters the record
chose. `LA-3`'s own message — *"the administration must be bound to the
parameters it names"* — is true and is not what §4 means: §4 line 480 says
the gate is administered *"against a named launch target (parameter block:
`LAUNCH_TARGET`, `REQUIRED_WAVES`, `DEFERRED_WAVES`)"*, and §8 is supposed
to be the fixed input. Here the record picks which §8.

`[Inferred]` A reader inspecting `main` sees a clean, eligible
`READY FOR …` record and cannot tell that its parameter block never existed
on any reading path. *Fix:* require `repository_commit` to be an ancestor of
(or equal to) a named anchor — the same `_is_ancestor` `LA-15` already uses —
and state the requirement in §2 beside "committed at the administered
commit".

### D.4 f3 — MATERIAL — the `SDR-n` branch and the path branch apply different warrant standards

§5 line 774, added at v2.2:

> deferral citation — **a made owner decision**, never a queue entry, a log,
> an index, a decision packet, or a document that declares its own status
> unresolved (RD-56 f5);

The validator's own comment at 128–132:

> #: Files that live in the decisions home but are not warrants. … so the
> same file granted nothing by identifier and everything by path (review
> RD-47 finding 4). **One list, both branches.**

`[Observed]` It is not one list. `_NON_WARRANT_FILES` (133–146 — five names,
widened at v2.2 to include `TREND-LOG.md` and `HISTORY.md`),
`_PACKET_NAME` and `_PENDING_SELF_DECLARATION` are consulted **only** by
`_non_warrant_reason`, which is called **only** from the path branch (990).
The identifier branch is `_sdr_exists` (475–489), whose `git grep` excludes
exactly one file:

```python
f":(exclude){DECISIONS_HOME}/PENDING-OWNER-DECISIONS.md"
```

`[Observed]` **Constructed and executed.** In a scratch clone I appended one
narrative line — `A narrative mention of SDR-777 in a repair history.` — to
`.syzygy/governance/decisions/launch-gate/HISTORY.md`, committed, and cited
`SDR-777` as the F2 deferral warrant:

```text
SDR-777 resolves via _sdr_exists: True
path branch would refuse HISTORY.md: "records what the owner has *not* decided,
    or routes to what others record — it is an index, a queue or a log"
errors= 0 eligible= True verdict= READY-WITH-DEFERRALS
trend: | 2026-08-11 | a7556ca | 1 | 0 | 0 | 1 | 0 | n/a (no prior record) | READY-WITH-DEFERRALS |
```

`[Observed]` The same file grants nothing by path and everything by
identifier — the exact inversion the code comment says was closed, now
running in the opposite direction and **widened at v2.2**, because v2.2 grew
the path branch's refusal list from three names to five plus two shape rules
and left the identifier branch at one name. Citing F1's own trend log to
defer F2 — the circularity RD-56 f5 named — is reachable through the
identifier branch today.

`[Observed]` Denominator check on whether this is live: I swept all 22 files
of `.syzygy/governance/decisions/` for `SDR-\d+` and found 33 distinct
identifiers; **0** of them occur only in non-warrant files at `918574c`. So
the hole is structural, not currently exploited.

*Fix:* route `_sdr_exists`'s hits through `_non_warrant_reason` — resolve the
identifier to the file that carries it and apply the same shape rules — or
state in §5 that the two citation forms are judged by different standards.

### D.5 f4 — MATERIAL — `e4.routing_authority: " "` switches `LA-3b` off

Validator 744–756:

```python
want_ra = _param_path(pb_text, "E4_ROUTING_AUTHORITY")
got_ra  = _norm_ws(rec.get("e4", {}).get("routing_authority", ""))
if want_ra is None:            errors.append("LA-3b: …")
elif got_ra and got_ra != want_ra:   errors.append("LA-3b: …")
```

`[Observed]` `_norm_ws` (512–513) is `re.sub(r"\s+", " ", s).strip()`, so
`" "` normalizes to `""`; the schema constrains the field only with
`"minLength": 1`, which a single space satisfies. The `elif got_ra and …`
guard therefore skips the comparison entirely. Executed:

```text
e4.routing_authority = " "  →  errors= 0  eligible= True
trend: | … | READY FOR Capability 1 — Project registration and honest shape visibility |
```

versus `"README.md"` → `LA-3b: the record's E4 routing authority 'README.md'
is not §8's '.syzygy/governance/contracts/candidates/SURFACE-CLAUSE-ROUTING-MATRIX.md'`.
`[Observed]` A wrong authority is caught; **no authority is not.** Nothing
else in the record depends on the field — `LA-10`'s agreement test reads the
reviewer-authored `routing_authority_says`, never the file — so E4 can be
`Met` against an authority the record declines to name.

`[Inferred]` This is the same species as the delta's disclosed limit 7
(`counterexample: " "` satisfying `minLength`) but it is not that limit: it
disables a **check**, not a presence test, and the check it disables is the
one §5 enumerated for the first time at v2.2 in answer to RD-55 f2. So RD-55
f2's closure is textual: the enumeration now names `LA-3b`, and `LA-3b` can
be switched off from the record.

*Fix:* raise the error when `got_ra` is empty (an absent authority is not an
excused one), and give the schema a `pattern` rather than a `minLength` for
path-shaped fields.

### D.6 f5 — MATERIAL — §2 requires a trend-row disclosure the generated row cannot carry

§2 lines 134–138, an **administration integrity requirement** (§2 line 124:
*"a record missing any of these cannot support a gate decision"*):

> A **formal** administration … is run full, not delta, by a fresh-context
> reviewer — preferably from a different model family than the corpus's
> authors; if it cannot be, **the record and the trend row must say so**,
> since a family-constant trend measures agreement as much as convergence.

§4 line 646 repeats it: *"F5 and F6 are recorded and disclosed
(`reviewer.model_family`; the trend row)"*.

§6 lines 805–807, the fixed table:

```markdown
| Date | Commit | Not-met | Scoped | Unknown | Deferred | Reopened | New findings vs prior | Gate verdict |
```

`[Observed]` Nine columns; none is model family or same-family. `trend_row()`
(1300–1306) emits exactly those nine cells and reads
`reviewer.same_family_as_corpus_authors` nowhere — I grepped the validator
for the field: it appears in `_base_record` only. §6 line 798 forbids the
obvious workaround: *"**The row is generated**, not transcribed … A
hand-typed trend row is a figure quoted outside its owning artifact, which
is how the columns went stale before."*

`[Inferred]` §2's obligation is therefore unmeetable through the mandated
path. An administrator can add prose *beside* the row, but that is not the
row, and §6's convergence rule is read from the columns. Given that this
repository has now run **five** same-family reviews of this instrument, the
disclosure F5 exists to force is the one the trend log cannot show.

This predates v2.2 (§2 and §6 are byte-identical to v2.0) and RD-55 did not
find it. *Fix:* add a `Same family` column to §6 and to `trend_row()`, or
narrow §2 to "the record must say so, and the trend log's header must carry
the disclosure beside the row".

### D.7 f6 — MATERIAL — `--prior` still reads outside the repository

§6 lines 798–802:

> **The row is generated** … `validate_launch_administration.py --trend-row`
> prints it from the source record, and the New-findings column is computed
> against the record the `prior_record` field names.

`[Observed]` RD-56 f6's repair lives at validator 1209–1226 and guards only
the branch taken when `prior_path is None`. When `--prior` is supplied,
`src = prior_path` (1208) and the containment test is skipped; `LA-15`
(1062–1077) checks only that the supplied file's `repository_commit` matches
the record's declared `prior_record.repository_commit` — a field the forged
file also authors. Executed, on a record with **four genuinely new `Not met`
rows**:

```text
record-declared prior (path unreadable):
    errors=0 eligible=True new_findings='unknown'
    | 2026-08-11 | 918574c | 4 | 0 | 0 | 0 | 0 | unknown | NOT READY |

--prior /tmp/…/rd61-forged-prior.json  (outside the repository):
    errors=0 eligible=True new_findings=0
    | 2026-08-11 | 918574c | 4 | 0 | 0 | 0 | 0 | 0 | NOT READY |
```

`[Observed]` The unreadable-declared-prior case correctly computes
`unknown` rather than zero — VIS-2 honoured. The `--prior` case computes a
**false 0** against a file the repository has never seen, with zero errors
on an eligible record. It cannot fabricate a `READY FOR`; it can fabricate
convergence, which is what F1 is answered from.

*Fix:* apply the same `is_relative_to(REPO)` test to `prior_path`, or drop
`--prior` as an override on any run that also prints `--trend-row`.

### D.8 m1 … m5 — the minor residues

**m1.** §5 lines 751–752: *"A record that does not validate is not rendered
at all."* `[Observed]` `render_launch_administration.py <invalid>.json`
refuses (*"refusing to render. A report of an unlawful record is not a
report"*), but `--allow-invalid` writes a 9,032-byte report — stamped
`THIS RECORD DOES NOT VALIDATE` at line 10 and ending `GATE VERDICT: NONE …`
at line 217. RD-55 showed the clause false inside f1; v2.2 repaired the tool's
*output* and left the clause unqualified.

**m2.** §4 line 509: *"**Row/formula outcome** | Always. It is a function of
the rows and nothing else"*. `[Observed]` False of §4's own formula: the
seventh conjunct reads `rec["e3"]["reopen_items"]` (1141), the F2 limb reads
`rec["owner_deferrals"]` (1147–1150), and the verdict string interpolates
`rec["launch_target"]` (1162). None is a row.

**m3.** §4 lines 519–521: *"the gate result is the literal `NONE`, followed
by the limbs it failed. Every surface uses that word — the trend log's
Gate-verdict column, the generated report's terminal line, and the
validator's own output"*. `[Observed]` The CLI and the report list the
limbs; the trend column (1289–1290) emits `NONE — not eligible; row outcome
was …` and lists none. §4 line 529 separately prescribes exactly that column
form (*"deposits `NONE — not eligible` there"*), so **§4 specifies the column
twice and differently**. `[Observed]` `_compute`'s `gate_result` is still
`"NO FORMAL GATE RESULT"` when ineligible (1261) — unreachable at every
consumer I traced (CLI 2190–2191, renderer 425–427, `trend_row` 1286–1290 all
read it only under `eligible`), but a fourth spelling of the fourth outcome
survives in the code RD-55 f8 counted it in.

**m4.** §9 line 1047 still reads *"the count is printed by `--selftest` and
stated nowhere else (RD-48 f6)"*. `[Observed]` The v2.2 delta's Fixtures
block states `101` and `31`; the §9 v1.9 entry states `74`; line 2197 repeats
the unscoped phrase. The v2.2 delta corrected the claim **in the delta**
(corrections item 3: *"stated in no artifact that must stay current"*) and
left the instrument's own copy unscoped.

**m5.** §4 line 614: *"**Any deferral-carrying pass is
`READY-WITH-DEFERRALS`.** The F2 deferral limb of the formula — **and any
other owner deferral a pass rests on** — changes the verdict word"*, against
line 625: *"with **exactly one substitution**: the F2 limb"*. `[Observed]`
The tool takes the second reading: a non-F2 deferral over a passing core
gives `NOT READY` plus `LA-12: deferrals are declared against a passing core
with no F2 deferral`. Strict, so no pass route — but the instrument says two
things about the same record.

`[Observed]` **Two of the three `LA-12` contradiction branches are
unreachable by construction.** Line 1184 tests `branch == "plain" and
n_deferred`, and `branch` is `"plain"` only when `n_deferred == 0` (1161);
line 1187 tests `branch == "deferrals" and not f2_deferred`, and `"deferrals"`
requires `f2_deferred` (1164). **Mutation-verified:** I copied the tree,
deleted both branches, and `--selftest` still reports
`101 fixtures, 0 failing`. §5 line 754 says every check carries at least one
mutation fixture, and the selftest's own banner is *"a check that cannot fail
is not a check"*.

---

## E. What I could not test, and why

- `[Unknown]` **Whether the questions are the right questions.** §3 is
  byte-identical to v2.0; out of this commission's scope.
- `[Unknown]` **The truth of any evidence quote.** Content-blindness is by
  design and is the delta's disclosed limit 1.
- `[Unknown]` **The instrument under a real administration.** None has been
  performed at v2.0, v2.1 or v2.2 — `TREND-LOG.md` has zero rows, which I
  verified. Everything in §B, §C and §D is synthetic.
- `[Unknown]` **Completeness of "no new pass route".** 30 differential cases,
  814 render injections and identity of the deciding code is strong evidence,
  not a proof over the record space.
- `[Unknown]` **RD-56's thirteen findings.** Out of my role. I did **not**
  open `RD-56-launch-machinery-v2.1-RAW.md`; where a v2.2 change is
  attributed to RD-56 I tested the resulting bytes, not the claim about them.
- `[Unknown]` **Whether the five §4 blocking conditions are correctly
  applied** to any real deferred-wave defect — `blocking_conditions_met` is
  reviewer-authored (delta limit 8) and I have no administration to check it
  against.
- `[Unknown]` **Clean-clone status of the wider battery.** I ran
  `--selftest` for both tools in the frozen worktree (`101 fixtures, 0
  failing` / `31 fixtures, 0 failing`, matching the delta) and in two scratch
  clones; I did not run `check_governance.py`.

---

## F. Confirmation — every file I opened

Under the frozen worktree
`…/scratchpad/frozen-918574c/` at `918574c`:

1. `launch-gate-pre-specifications.md` — **read in full** (lines 1–1248 by
   hand; 1249–2236 are §9's v1.9-and-earlier history, read by targeted sweep
   only, and that limit is stated here rather than smoothed).
2. `launch-gate-administration.schema.json` — read programmatically (root
   keys, `additionalProperties`, `required`, `$defs/question_result/verdict`,
   `properties/e4`).
3. `scripts/validate_launch_administration.py` — read lines 113–262,
   434–500, 598–1097, 1100–1400, 2165–2214; full-file greps for check
   identifiers, conjunct labels and `same_family_as_corpus_authors`.
4. `scripts/render_launch_administration.py` — read lines 144–190; full-file
   grep for `_inline` / `_quoted` / `NONE` / `gate_result` / `eligible`;
   executed against 814 mutated records.
5. `.syzygy/governance/contracts/candidates/round-2026-08g/LAUNCH-GATE-v2.2-SEMANTIC-DELTA.md`
   — read in full (context, not subject).
6. `.syzygy/governance/contracts/candidates/round-2026-08g/reviews/RD-55-launch-policy-v2.1-RAW.md`
   — read in full (the prior review this repair answers).
7. `.syzygy/governance/contracts/candidates/round-2026-08g/reviews/DISPOSITION-REGISTER.md`
   — counted `RD-47/48/55/56` occurrences; read lines 13–53 only, to check
   f9's closure.
8. `FORMAL-CAPABILITY-1-LAUNCH-PACKET/README.md` — read lines 238–286;
   greps for `RD-4x/5x`, `trend-row`, `eligib`, `NONE`.
9. `.syzygy/governance/decisions/launch-gate/TREND-LOG.md` — read the header
   and confirmed zero rows.
10. `PROJECT-STATUS.md`, `.syzygy/governance/contracts/candidates/09-OPEN-SPEC-READINESS-REPORT.md`,
    `.syzygy/governance/decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` — the
    single `GATE VERDICT` line in each, via `git grep -n`.
11. All **22** tracked files under `.syzygy/governance/decisions/` — read
    programmatically for the `SDR-\d+` occurrence sweep in D.4.
12. Retrieved from git and read: `939363f:launch-gate-pre-specifications.md`,
    `939363f:scripts/validate_launch_administration.py` (the v2.1 differential).

**Not opened, deliberately:** `RD-56-launch-machinery-v2.1-RAW.md`,
`RD-47`/`RD-48` raw files, `LAUNCH-GATE-v2.1-SEMANTIC-DELTA.md`, and every
earlier round's review tree — so that this review's findings are the bytes'
and not their reviewers'.

**Scratch artifacts** (all under
`…/scratchpad/rd61-scratch/`, none in the repository): `probe.py`,
`probe2.py`, `probe3.py`, `probe4.py`, `diffbattery.py`, `battery/` (30
records), `clone/` (the tamper and SDR-leak branches), `c21/` (the `939363f`
tree), `mut/` (the deleted-branch mutation), and the probe records named in
§D.

---

## G. Judgement

`[Observed]` **The amendment does what it was commissioned to do on the two
questions the charter asks first.** Nothing was weakened: §3, §6, §7 and §8
are byte-identical by digest and by hunk mapping; the roster, the conjunct
list and the emitted-check set are identical strings; and over a 30-case
differential battery **no record fails under v2.1 and passes under v2.2**,
while fourteen become ineligible that were not. RD-55's blocking finding is
closed at all four surfaces and closed *harder* than asked — the fifth limb
(git-unavailable) was a disclosed limit that nothing acted on, and now an
unverified record is ineligible. Eight of RD-55's ten findings are closed
outright; I verified each against the bytes rather than the delta's account,
and the two residues are named rather than hidden.

`[Observed]` **It does not clear.** The defect class this round exists to
close — *the repair is narrower than the claim made for it* — is present in
the two clauses §5 added at v2.2. **f1**: §5 says the schema check is "the
schema's own identity … anything but the **committed** schema", and the tool
compares a path; a one-line in-place edit produces an **eligible** record
whose A1 row reads `Met (with caveats)` and whose gate result is
`READY FOR Capability 1 …`. **f3**: §5 says a deferral warrant is "never a
queue entry, a log, an index", and the `SDR-n` branch grants one from a
narrative line in `launch-gate/HISTORY.md` — the file the path branch refuses
by name, in the same list v2.2 widened. **f4**: the check §5 finally
enumerated in answer to RD-55 f2 can be switched off with a single space.
Each was constructed and executed, not argued.

Two further findings are older than this amendment and were missed by every
prior reading: **f2**, that `repository_commit` is anchored to nothing, so a
record can bring its own §8 (`READY FOR Everything, immediately`, zero
errors, eligible); and **f5**, that §2 makes a trend-row family disclosure an
integrity requirement which §6's fixed columns and the mandated generator
cannot carry — in a corpus whose instrument has now been reviewed five times
by its own model family, including this review.

None of the six reopens a route that the v2.1 → v2.2 diff opened. All six are
routes that were there to be found, and three of them are the bytes failing a
claim the amendment newly makes about itself.

f1: BLOCKING. f2, f3, f4, f5, f6: MATERIAL. m1–m5: MINOR.

VERDICT: REVISE
