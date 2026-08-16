# RD-65 — Launch-policy v2.3 semantic review (round-2026-08h, subject `494acab`)

| | |
|---|---|
| Review ID | **RD-65** — third administration of the RD-55 commission |
| Date | **2026-08-16** |
| Role | Launch-policy semantics reviewer — the fresh-context re-review of the bytes RD-61 (`REVISE`) and RD-62 (`REVISE`) produced |
| Frozen commit | **`494acab`** (`494acabc431d70fd9febfaa7c4a635b4083d50d9`) |
| Subject | `launch-gate-pre-specifications.md` — sha256 `3e65aaa39bd6525c70ce589fb3f0c029af91b1bb74b29966563d3f3dcf376294` **(verified at start and end)** |
| Cross-ref 1 | `launch-gate-administration.schema.json` — `e0167fb8af6a903c527d402d56c4fb85ebdfed9608de1a485f4f1563aa6a69fb` **(verified)** |
| Cross-ref 2 | `scripts/validate_launch_administration.py` — `c3e20de8304430ff94ad68f65b1ec62695779a632b09fff8a64d1be94f40e52c` **(verified)** |
| Cross-ref 3 | `scripts/render_launch_administration.py` — `678dab0a232958116993c6736af9f3b2d72120db8de93e6880aa480e9df13ceb` **(verified)** |
| Context | **Fresh.** No prior contact with this repository beyond the brief and the RD-61 raw output, which the brief supplied as the subject of question 2 |
| Model family | **Same as the corpus's authors.** This review therefore **supports repair** and is **NOT the formal launch administration** (instrument §2's family-disclosure requirement; question F5) |
| Nothing edited | `git status --porcelain` is empty in both the frozen worktree and `/home/tze/GitHub/syzygy`. All probes ran in throwaway clones under `/tmp/rd65/`, never in either repository |

All four digests in the brief reproduce exactly. Line numbers are 1-indexed into the frozen `launch-gate-pre-specifications.md` (2297 lines) and `scripts/validate_launch_administration.py` (2657 lines).

---

## Findings table

| # | Severity | Section / site | One line |
|---|---|---|---|
| **1** | **MATERIAL** | §2 lines 140–147; §4 line 658 | The f5 repair moved the same-family obligation from the trend row to the generated report and justified it with *"the trend log's family reading runs through the reports its rows link"* — **the rows link nothing.** §6 is byte-identical: nine columns, no link, no report path. RD-61 f5's substance is relocated off the one artifact F1 is answered from |
| **2** | **MATERIAL** | §4 line 517 | *"a function of the record's own content … and **never of the environment**"* is false. **One byte-identical record** yields `NOT READY` with git available and `READY-WITH-DEFERRALS` without it — and the divergence runs in the **permissive** direction |
| **3** | **MATERIAL** | §5 lines 786–790; validator 674–692, 759–763 | The schema now governs from **`HEAD`**, while the instrument governs from the record's **named commit** — and v2.3's own new ancestry rule guarantees `HEAD` is the later of the two. A **committed** enum widening at `HEAD` validates a §2-forbidden verdict word in a record at any ancestor commit: **0 errors, `eligible: true`, `READY FOR Capability 1 …`** |
| **4** | MINOR | §4 lines 623–631 | *"'any other owner deferral' is an **`LA-11`** error"*. The check that actually fires is **`LA-12`**. Verified for F5 and F6 — the 2 of 39 roster rows that are neither F2 nor `NEVER_DEFERRABLE` |
| **5** | MINOR | §4 line 529 | *"deposits `NONE — not eligible` there"*. The m3 repair changed the emitted string to `NONE — \`formal: false\`; …`; the words *"not eligible"* are **gone**. v2.3 repaired half of RD-61 m3 and falsified the clause that specifies the same column |

**0 BLOCKING, 3 MATERIAL, 2 MINOR.**

> **Identifier disambiguation.** Findings **1–5** are RD-65's. RD-61's findings are written `RD-61 f<n>` / `RD-61 m<n>` throughout.

---

## A. Method

Every claim below was produced by reading bytes or executing code, never by reading the v2.3 semantic delta. **I did not open `LAUNCH-GATE-v2.3-SEMANTIC-DELTA.md` at any point**, so that its account could not colour a finding. I also did not open `RD-62-launch-machinery-v2.2-RAW.md`; where a v2.3 change is attributed to RD-62 I tested the resulting bytes, not the claim about them.

`[Observed]` Probes ran in five throwaway clones of the frozen worktree under `/tmp/rd65/` (`c23`, `c23b`–`c23f`, and `c22` at `918574c`). The frozen worktree and the main repository were read-only throughout, confirmed by empty `git status --porcelain` at the end of the session and by the four digests reproducing unchanged.

---

## B. Commission item 1 — the no-weakening diff

### B.1 The real bytes, two independent methods

`[Observed]` I obtained the v2.2 bytes with `git show 918574c:launch-gate-pre-specifications.md` (sha256 `ac8751236ec7434c20606b404d41c885d29f67dd5f3dab8c9d0cbb90de670977`, matching RD-61's recorded subject digest) and diffed against the frozen v2.3 file. **Method 1** — `diff -u`: 118 lines of diff output across **9 hunks**. **Method 2** — split both texts on `^## <n>\.` and digest each span; contiguity confirmed (`"".join(spans) == whole file`) and the whole-file digest reproduces.

| Span | v2.2 | v2.3 | Same |
|---|---|---|---|
| §0 preamble | `3cff94f230056b52` | `fbfd5048181d58c4` | changed — version bump only |
| **§1** | `1f2d1d60a28ada2a` | `1f2d1d60a28ada2a` | **identical** |
| §2 | `0d7340f2ee9a8b8c` | `fb8b35a4eadedeaa` | changed |
| **§3 — the question set** | `fe0b051e136d2fee` | `fe0b051e136d2fee` | **identical** |
| §4 | `8af5dbc5b7d82af1` | `f4e253572a4e326a` | changed |
| §5 | `1fd518196e437f6e` | `ae479eeaa24d705f` | changed |
| **§6 — trend log** | `9906fcac454062cd` | `9906fcac454062cd` | **identical** |
| **§7** | `9e17cb8de0458976` | `9e17cb8de0458976` | **identical** |
| **§8 — parameter block** | `01209c0f052971f7` | `01209c0f052971f7` | **identical** |
| §9 changelog | `18029b54c3de4e61` | `4d1ae72f65102334` | changed |

`[Observed]` Denominator: **all 10 spans**, which exhaust both files. **No readiness question moved** (§3 identical), **no trend obligation changed** (§6 identical), **no §8 parameter changed** (§8 identical, and the parameter block extracted by `param_block_bytes` digests `01209c0f052971f794e1f358` at both commits, with `LAUNCH_TARGET` unchanged).

### B.2 The deciding code is unchanged

`[Observed]` Extracted by `re` from both revisions of `validate_launch_administration.py`:

| Population | v2.2 → v2.3 | direction |
|---|---|---|
| `ROSTER` (39 rows) | **string-identical** | 0 |
| Computed conjunct labels `_c("…")` | **6, element-identical, same order** | 0 |
| `LA-*` identifiers emittable | **17 distinct, empty symmetric difference** — 0 dropped, 0 added | 0 |
| `NEVER_DEFERRABLE`, `E_ROWS`, `AD_ROWS` | **line-identical** | 0 |
| Row verdict enum (schema) | schema byte-identical (`e0167fb8…` at both commits) | 0 |
| §4 eligibility limbs | 5 stated and implemented at both | 0 |

### B.3 The one deletion, and why it weakens nothing

v2.3 removed two `LA-12` guard branches. `[Observed]` I verified their unreachability from the branch predicates directly rather than from the changelog. `_compute` (validator 1287–1295):

```python
if core and f2_met and n_deferred == 0:
    verdict = f"READY FOR {rec['launch_target']}";  branch = "plain"
elif core and f2_deferred and n_deferred > 0 and _f2_citation_resolves:
    verdict = "READY-WITH-DEFERRALS";               branch = "deferrals"
else:
    verdict = "NOT READY";                          branch = "blocked"
```

with `n_deferred = len(rec["owner_deferrals"])` (1245) and `f2_deferred = bool(f2_deferrals)` (1276). `branch == "plain"` therefore **entails** `n_deferred == 0`, and `branch == "deferrals"` **entails** `f2_deferred` — so both deleted guards were unconstructible. `[Inferred]` The deletion removes dead code and weakens no obligation.

### B.4 Differential execution — 31 mutations, both revisions

`[Observed]` I cloned the frozen worktree at `494acab` and at `918574c`, built a lawful `formal`/`full`/`fresh` base record **independently in each tree** (so each binds its own instrument digest), and applied the same 31 mutations on both sides. Acceptance = *zero errors **and** `eligible: true`*.

| Direction | count | cases |
|---|---|---|
| **Weakened** (rejected at v2.2, accepted at v2.3) | **0** | — |
| Stricter (accepted at v2.2, rejected at v2.3) | 1 | `ra_blank` (RD-61 f4's repair) |
| Unchanged | 30 | — |

Coverage: administration kind, formality, fresh-context, forged instrument and parameter-block digests, launch-target and wave mismatch, E3 reopen items, Met-without-evidence, plain `Not met` in A–D and in E, an Unknown row, missing / extra / duplicate roster rows, blank and wrong routing authority, seven deferral-citation shapes (`P-n`, the pending queue, the trend log, `HISTORY.md`, a nonexistent `SDR-n`, a real `SDR-n`, an `E1` deferral), an `F5` deferral, fabricated evidence paths, a placeholder G1, a top-level `final_verdict` field, an off-branch commit, and a nonexistent commit.

`[Observed]` **I could not construct a record that fails under v2.2 and passes under v2.3.** `[Inferred]` No readiness meaning was weakened. 31 targeted cases plus the identity of the deciding code is strong evidence, not a proof over the record space.

**Conclusion on commission item 1:** `[Observed]` **Nothing was weakened.** No readiness question, verdict word, formula branch, eligibility limb, §8 parameter, or trend obligation was dropped, renamed, or loosened.

---

## C. Commission item 2 — RD-61's eleven findings, independently verified

I did not take any delta's dispositions on trust; each row was constructed and executed.

| RD-61 | Sev | Status | Evidence at `494acab` |
|---|---|---|---|
| **f1** — schema read from the working tree, never digest-checked, while §5 claims *"the **committed** schema"* | BLOCKING | **PARTIALLY REPAIRED** | `[Observed]` The working-tree route is **closed by construction**. I reproduced RD-61's exact attack in a clone — appending `"Met (with caveats)"` to `$defs/question_result/…/verdict.enum` **in place at the default path**, leaving the audit clean — then validated a record whose A1 row carries the forbidden word. Result: **2 errors**, `eligible=None`: `LA-1: the working-tree launch-gate-administration.schema.json differs from the schema committed at HEAD` **and** `LA-1: $/question_results[0]/verdict: 'Met (with caveats)' is outside the closed set ['Met', 'Not met', 'Not met (out of launch scope)', 'Unknown']` — validation ran against the committed bytes, exactly as §5 now claims. Code: `blob = _git_show("HEAD", SCHEMA_NAME)` (675) with a drift comparison (687–692). **Residue:** the governing commit is `HEAD`, not the record's named commit — see **finding 3** |
| **f2** — `repository_commit` anchored to nothing reachable | MATERIAL | **REPAIRED — verified by construction** | `[Observed]` I rebuilt RD-61's attack faithfully: an unmerged branch rewriting §8's `LAUNCH_TARGET` to `Everything, immediately.`, then a `formal`/`full`/`fresh` record **self-consistently bound to that off-branch commit** (its own instrument sha256, its own parameter-block digest, its own launch target, evidence commits repointed). At v2.2 this was 0 errors / eligible. At v2.3: **1 error**, `eligible=False`, `gate_result = NONE`. The error is `LA-2: named commit a09bf316… is not reachable from the repository's current HEAD — an administration anchored off-branch can quote bytes no branch carries` (validator 759–763). `_is_ancestor(OFF, "HEAD")` → `False` |
| **f3** — the `SDR-n` branch granted a warrant from a narrative line in `launch-gate/HISTORY.md` | MATERIAL | **REPAIRED — and the repair is precise** | `[Observed]` I appended `A narrative mention of SDR-777 in a repair history.` to `HISTORY.md` and committed. `_sdr_exists("SDR-777")` → **`False`** (was `True`); `_sdr_exists("SDR-9")` → `True`. I then tested the **stronger** claim §5 makes — resolution against the owning record's *own rows* — by appending a narrative aside naming `SDR-777` to `SURFACE-DECISION-RECORD.md` itself and committing: still **`False`**. The rewritten `_sdr_exists` (509–528) greps `\*\*SDR-n\*\*` against `SURFACE-DECISION-RECORD.md` alone, so the two branches are consistent *by construction* rather than by parallel lists |
| **f4** — `e4.routing_authority: " "` switched `LA-3b` off | MATERIAL | **REPAIRED — verified by construction** | `[Observed]` `e4.routing_authority = " "` now yields **1 error**, `eligible=False`: `LA-3b: the record's E4 routing_authority is empty after whitespace normalization — E4 is judged against the authority §8 binds, and a blank restatement…`. The `elif got_ra and …` guard is replaced by an explicit `elif not got_ra:` limb (validator 839–848). This is the single **STRICTER** case in the 31-mutation differential |
| **f5** — §2 required a trend-row family disclosure §6's fixed columns and the mandated generator cannot carry | MATERIAL | **PARTIALLY REPAIRED — relocated, and the relocation rests on a false claim** | `[Observed]` The **report** half is real and implemented: rendering a record with `same_family_as_corpus_authors: true` emits at line 25 `- Model family: fixture` and at line 27 `- **Same model family as the corpus's authors — a family-constant administration measures agreement as much as convergence (instrument §2, F5).**` (renderer 227–234). §2's obligation is now meetable by the mandated generator. **But** §6 is byte-identical, `trend_row()` still emits exactly nine cells none of which is a link, and `TREND-LOG.md`'s header carries no link column — so §2's justifying clause *"the trend log's family reading runs through the reports its rows link"* is false. **Finding 1** |
| **f6** — `--prior` read a file outside the repository and zeroed the New-findings column | MATERIAL | **REPAIRED — verified by construction** | `[Observed]` On a record with four genuinely new `Not met` rows and a forged prior at `/tmp/rd65/forged-prior.json`: **`LA-15: --prior '/tmp/rd65/forged-prior.json' resolves outside the repository — the new-findings column is computed from it, so it is evidence and must live where evidence lives`**, `eligible=False`, and `new_findings='unknown'` — **not** the false `0` v2.2 produced. Containment test at validator 1177–1187, and the declared-identity test at 1341–1364 |
| **m1** — *"A record that does not validate is not rendered at all"* was false of `--allow-invalid` | MINOR | **REPAIRED** | `[Observed]` §5 now reads *"not rendered **by the default invocation**; `--allow-invalid` exists for inspection and stamps its output `THIS RECORD DOES NOT VALIDATE`"*. Both halves execute: default invocation **exits 1 and writes no file**; `--allow-invalid` writes a report carrying `> **THIS RECORD DOES NOT VALIDATE.**` at line 10 and `GATE VERDICT: NONE — …` at line 217 |
| **m2** — *"a function of the rows and nothing else"* was false of §4's own E3 and F2 conjuncts | MINOR | **NOT REPAIRED — a different false claim replaced it** | `[Observed]` The enumeration is now correct as far as it goes, but the appended absolute *"and never of the environment"* is falsifiable and false. **Finding 2** |
| **m3** — the trend column named no limb; a fourth literal `NO FORMAL GATE RESULT` survived | MINOR | **PARTIALLY REPAIRED** | `[Observed]` **Limbs half repaired:** a `nonformal` + `delta` record now emits `NONE — \`formal: false\`; \`administration_kind: delta\`` at the gate line *and* in the trend column, and the git-unavailable case names its limb in full. **Fourth literal repaired:** `NO FORMAL GATE RESULT` survives only inside a comment at validator 1408 — `grep` over both scripts returns no live occurrence. **Residue:** the new string falsified §4 line 529. **Finding 5** |
| **m4** — §9's v2.1 entry still asserted the unscoped *"stated nowhere else"* | MINOR | **REPAIRED** | `[Observed]` §9 now carries the inline scoping *"(claim scoped at v2.3, RD-61 m4: the v2.2 semantic delta — a frozen record — states the counts it measured; the accurate form is 'stated in no artifact that must stay current')"*. The frozen v2.1 entry is correctly left frozen and annotated rather than rewritten |
| **m5** — §4 said *"any other owner deferral"* converts the verdict while its own predicate admits *"exactly one substitution"*; two `LA-12` branches unreachable | MINOR | **PARTIALLY REPAIRED** | `[Observed]` The **tension is resolved** — §4 now states one rule, and the unconstructibility claim is true (§B.3). The **dead branches are removed** and `--selftest` reports `119 fixtures, 0 failing`. **Residue:** the replacement clause cites the wrong check. **Finding 4** |

**No RD-61 finding is silently omitted.** Six repaired outright (f2, f3, f4, f6, m1, m4); five partially repaired (f1, f5, m2, m3, m5), each with the residue named as a finding below.

---

## D. Commission item 3 — internal coherence, and item 4 — false-READY paths

### D.1 What the machinery does that the policy correctly describes

`[Observed]` `--selftest` reports **`119 fixtures, 0 failing`** (validator) and **`34 fixtures, 0 failing`** (renderer) in a clean clone at `494acab`, matching §9's claimed counts. The five eligibility limbs are implemented and separable; I confirmed the three-outcome separation holds at every surface:

```text
A1 Not met      errs=0 elig=True  verdict='NOT READY'  gate='NOT READY'
E2 Not met      errs=0 elig=True  verdict='NOT READY'  gate='NOT READY'
F3 Not met      errs=0 elig=True  verdict='NOT READY'  gate='NOT READY'
forged digest   errs=1 elig=False verdict='READY FOR …' gate='NONE — the record has 1 validation error(s)'
```

`[Observed]` An ineligible administration deposits no `READY FOR` into the trend log at any surface. RD-55 f1's defect remains closed at v2.3.

`[Observed]` Pre-existing and unchanged: an `Unknown` row in A–D does **not** block a `READY FOR` (§4's formula names only `Not met`). §4's formula prose is unchanged at v2.3 and §6 carries an Unknown column, so this is disclosed, not hidden. Out of scope for "new path"; noted so it is not silently green.

### D.2 Finding 1 — MATERIAL — the f5 relocation rests on a link that does not exist

§2 lines 140–147, an **administration integrity requirement** (§2: *"a record missing any of these cannot support a gate decision"*):

> …if it cannot be, the record and the **generated report** must say so, since a family-constant trend measures agreement as much as convergence. *(Corrected at v2.3, RD-61 f5: … The report states `Model family` from the record; **the trend log's family reading runs through the reports its rows link**.)*

§4 line 658 repeats the relocation: *"F5 and F6 are recorded and disclosed (`reviewer.model_family`; the **generated report**)"*.

`[Observed]` The report half is real (§C, f5 row). **The bridging claim is not.** §6 is byte-identical to v2.2 and v2.0; its fixed table is

```markdown
| Date | Commit | Not-met | Scoped | Unknown | Deferred | Reopened | New findings vs prior | Gate verdict |
```

`[Observed]` Nine columns; **none is a link, a report path, or a record path.** `trend_row()` (validator 1440–1460) emits exactly those nine cells, and I read every one: `date`, `repository_commit[:7]`, five counts, `new_findings`, and the gate column. `TREND-LOG.md`'s committed header carries the same nine and no link. §6 line 798 forbids the workaround: *"**The row is generated**, not transcribed … A hand-typed trend row is a figure quoted outside its owning artifact."*

`[Inferred]` **RD-61 f5's substance is not repaired; it is relocated off the artifact that matters.** §6 states that F1 *"is answered from this log and only from it."* After v2.3 the trend log carries **no family signal at all** — v2.2 at least stated the obligation and failed it visibly, whereas v2.3 discharges the obligation onto a report the log does not reach and asserts a link to close the gap. In a corpus whose instrument has now been reviewed six times by its own model family, including this review, the disclosure F5 exists to force is again the one the trend log cannot show.

*Fix:* add a `Report` (or `Record`) column to §6 and to `trend_row()` so the asserted link exists, **or** add a `Same family` column, **or** narrow §2's parenthetical to claim only what is true — that the disclosure lives in the record and the report, and that the trend log does not carry it.

### D.3 Finding 2 — MATERIAL — *"never of the environment"* is false, and false permissively

§4 line 517:

> | **Row/formula outcome** | Always. It is a function of the record's own content — the rows, `e3.reopen_items`, and the declared `owner_deferrals` — and **never of the environment** *(scoped at v2.3, RD-61 m2…)* |

`[Observed]` **Constructed and executed.** One record file, byte-identical across both runs, with `F2` = `Not met` and an F2 deferral citing `SDR-9991` (which resolves nowhere). Only the environment varies:

```text
  _git=True  -> row/formula verdict = 'NOT READY'
  _git=False -> row/formula verdict = 'READY-WITH-DEFERRALS'
```

`[Observed]` The mechanism is `LA-11`'s citation loop (validator 1057): `if _git and not _sdr_exists(cite, commit): <error> else: resolved_deferrals.add(qid)`. With git unavailable the citation check does not run and the warrant is **added to `resolved_deferrals` anyway**, so `_f2_citation_resolves` is true and §4's `READY-WITH-DEFERRALS` branch is taken. A control confirms the record is otherwise well-formed: with a real warrant (`SDR-9`) both environments give `READY-WITH-DEFERRALS`.

`[Inferred]` Three things follow. **(a)** The clause is false as written: the row/formula outcome *is* a function of the environment. **(b)** The falsity runs in the **permissive** direction — an unfindable warrant is treated as a found one, which is the shape VIS-2 forbids ("no evidence yields Unknown — never green"), not merely a reproducibility nuisance. **(c)** §4 line 517's own table places this outcome under "Always", and §6's Gate-verdict column carries it as `…; row outcome was READY-WITH-DEFERRALS` — depositing a falsely-permissive diagnostic into the log F1 is answered from and only from.

`[Observed]` The fifth eligibility limb correctly makes such a record **ineligible**, so **no formal `READY FOR` gate result is reachable this way.** The defect is confined to the row/formula outcome and to §4's claim about it.

`[Inferred]` **Severity.** I grade this MATERIAL rather than MINOR because RD-61 m2 was raised against exactly this clause, the repair replaced a vacuous overclaim with a *checkable and false* one, and the direction of error is permissive on the surface §6 makes F1's sole evidence. I grade it below BLOCKING because eligibility contains it.

*Fix:* either delete "and never of the environment", or make the claim true — treat an uncheckable citation as unresolved (`resolved_deferrals` should not gain a member the checks never confirmed), which would also align `LA-11` with VIS-2.

### D.4 Finding 3 — MATERIAL — the schema governs from `HEAD`, the instrument from the record's commit

§5 lines 786–790, the check enumeration §5 owns:

> the schema's own identity — read from the **committed bytes at `HEAD`**, never the working tree, with a drifted working-tree copy an error of its own (RD-56 f3; byte-bound at v2.3, RD-61 f1…)

`[Observed]` The tool does exactly this — `blob = _git_show("HEAD", SCHEMA_NAME)` (validator 675). **There is no gap between the prose and the code**, which is why this is not a repeat of RD-61 f1's species. The defect is the rule itself.

`[Observed]` Every other identity input is read at the **record's named commit**: the instrument (764), the §8 parameter block, E4's case text, evidence paths, deferral warrants. The schema alone is read at `HEAD`. And v2.3's **new** ancestry rule (`LA-2`, 759) *requires* the named commit to be an ancestor of `HEAD` — so the schema is now **systematically read at a commit at or later than the one the administration was performed at**. §2 lines 126–131 state the opposing principle: *"The record names the commit … and every citation is verified against it."*

`[Observed]` **Constructed and executed.** In a clone I committed the enum widening to `HEAD` (rather than leaving it in the working tree), then built a `formal`/`full`/`fresh` record bound to `HEAD~1` — an ancestor, so `LA-2`'s new ancestry check passes — with its A1 row reading `Met (with caveats)`:

```text
record at ANCESTOR commit, schema widened at HEAD (committed):
  errs= 0 eligible= True verdict= READY FOR Capability 1 — Project registration and honest sha…
  gate= READY FOR Capability 1 — Project registration and honest shape visibility
```

`[Observed]` This is RD-61 f1's outcome — an **eligible** record carrying a §2-forbidden verdict word and a `READY FOR` gate result — reached through the route v2.3's own prose sanctions. §2 line 145 forbids the word: *"No 'partially met,' no 'met with caveats' — a caveat that matters makes it `Not met`."* §5's third property, *"Scope cannot be laundered by wording,"* is still defeated one level below the record.

`[Inferred]` **Severity.** I grade this MATERIAL, not BLOCKING, and state the precondition so the owner can re-grade. Against BLOCKING: v2.3 is strictly stricter than v2.2 here (which admitted both routes), §5 promises nothing the tool fails to do, and the precondition is now a **committed** change to a governed artifact — auditable in history and itself a governance violation, where RD-61's working-tree edit left no trace. For MATERIAL: the outcome is an eligible `READY FOR` over evidence that does not support it; the schema is the instrument's own machine annex, so its binding is the ground everything else stands on; and the consequence is that **an administration's lawfulness is not stable against its own commit** — the same record's verdict can change as `HEAD` advances, with no change to its bytes and nothing in the record recording which schema judged it.

*Fix:* read the schema at `rec["repository_commit"]`, exactly as the instrument is read, and keep the `HEAD`-drift error as a separate warning; **or** carry a `schema_sha256` field in the record so the binding is recorded rather than recomputed. Fixture in the failing direction: a schema committed at `HEAD` but differing from the schema at the record's commit must not silently govern.

### D.5 Finding 4 — MINOR — §4 names `LA-11` where `LA-12` fires

§4 lines 623–631:

> …F2 is the **only** limb a deferral can lawfully name, so "any other owner deferral" is an **`LA-11`** error, never a verdict conversion…

`[Observed]` Constructed and executed. `NEVER_DEFERRABLE = frozenset(E_ROWS) | frozenset(AD_ROWS) | {"F1", "F3", "F4"}` (validator 223) covers **36 of the 39** roster rows. The remaining three are `F2`, `F5`, `F6`. A deferral against `F5` or `F6` whose row is `Not met` (so `LA-11`'s vacuity check does not fire) and whose citation resolves produces **exactly one error, and it is not `LA-11`**:

```text
F5=Not met + deferral on F5 (non-vacuous)  errs=1 ['LA-12'] elig=False verdict=NOT READY
   - LA-12: deferrals are declared against a passing core with no F2 deferral — the only deferrable limb is F2
F6=Not met + deferral on F6 (non-vacuous)  errs=1 ['LA-12'] elig=False verdict=NOT READY
```

`[Observed]` `LA-11` fires for the other 36 rows (*"a deferral is claimed against F1 — §4 makes every conjunct but F2 non-deferrable"*) and for vacuous deferrals against a `Met` row — so the clause is right for most of the roster and wrong for exactly **2 of 39**.

`[Inferred]` The clause's **outcome** claim is true: no such deferral converts a verdict, and the record is ineligible either way. Only the identifier is wrong. I considered MATERIAL — §5's own construction makes check-naming load-bearing (*"a check the tool runs that this list does not name is a finding"*), and v2.3 replaced a vacuously-true statement with a specifically-false one — but graded MINOR because no record's verdict, eligibility, or gate result turns on it. The practical cost is maintenance: a future repair grepping `LA-11` for this rule will not find it.

*Fix:* say `LA-12`, or say "a validation error" without naming a check.

### D.6 Finding 5 — MINOR — the m3 repair falsified §4's own column specification

§4 line 529, unchanged at v2.3:

> …an ineligible administration deposits `NONE — not eligible` there and its row outcome travels beside it as the diagnostic it is.

`[Observed]` v2.3 changed what is actually deposited. Executed:

```text
nonformal+delta  trend tail: NONE — `formal: false`; `administration_kind: delta`; row outcome was READY FOR Capability 1 …
nofresh          trend tail: NONE — the reviewer declares no fresh context; the record has 1 validation error(s); row outcome was …
```

`[Observed]` The words *"not eligible"* **no longer appear** in the emitted string for the `formal`, `administration_kind`, `fresh_context` or zero-errors limbs. At v2.2 the emitted string was `NONE — not eligible; row outcome was …`, so §4 line 529 was at least a correct prefix; at v2.3 it is not. `[Inferred]` RD-61 m3 flagged that *"§4 specifies the column twice and differently"*; v2.3 repaired the limb-naming half and made the double specification **contradictory** rather than merely redundant. No readiness consequence — this is a display string.

*Fix:* restate line 529 as "deposits the gate result there — `NONE` followed by the limbs it failed", so §4 specifies the column once.

---

## E. What I could not test, and why

- `[Unknown]` **Whether the questions are the right questions.** §3 is byte-identical to v2.0; out of this commission's scope.
- `[Unknown]` **The truth of any evidence quote.** Content-blindness is by design.
- `[Unknown]` **The instrument under a real administration.** None has been performed at v2.0–v2.3; `TREND-LOG.md` has zero rows, which I verified by reading it. Everything in §B, §C and §D is synthetic.
- `[Unknown]` **Completeness of "no new pass route".** 31 differential mutations plus the identity of the deciding code is strong evidence, not a proof over the record space.
- `[Unknown]` **RD-62's findings.** Out of my role, and RD-66 owns the machinery. I did **not** open `RD-62-launch-machinery-v2.2-RAW.md`; where a v2.3 change is attributed to RD-62 I tested the resulting bytes, not the claim about them. The renderer's `\r` neutralizers, the Unicode-category stripping, the anchored schema patterns and the `--check` `Unknown` state are **untested by me** and are RD-66's.
- `[Unknown]` **Whether the 119/34 fixtures discriminate.** I ran `--selftest` and read its output, and I mutation-verified five repairs directly (f1, f2, f3, f4, f6 by construction); I did not audit the remaining fixtures for the property §5 requires of each.
- `[Unknown]` **Clean-clone status of the wider battery.** I did not run `check_governance.py`.

---

## F. Confirmation — every file I opened

Under the frozen worktree at `494acab`:

1. `launch-gate-pre-specifications.md` — the v2.2→v2.3 diff read in full; §2, §4, §5, §6, §8 and §9's v2.3 entry read directly; span-digested end to end.
2. `launch-gate-administration.schema.json` — read programmatically (`properties/owner_deferrals`, `properties/prior_record`, `$defs/question_result/verdict`, `properties/reviewer`, `family` occurrences).
3. `scripts/validate_launch_administration.py` — read lines 200–225, 505–530, 639–780, 1020–1110, 1150–1220, 1226–1340, 1440–1560; full-file greps for schema/git/ancestry/prior/family/`NO FORMAL GATE RESULT`.
4. `scripts/render_launch_administration.py` — grep for family/gate/`allow-invalid`; executed against valid, invalid and `--allow-invalid` records.
5. `.syzygy/governance/contracts/candidates/round-2026-08h/reviews/RD-61-launch-policy-v2.2-RAW.md` — read in full (the prior review this repair answers).
6. `.syzygy/governance/decisions/launch-gate/TREND-LOG.md` — read header, confirmed zero rows and nine columns with no link.
7. Retrieved from git: `918574c:launch-gate-pre-specifications.md` and `918574c:scripts/validate_launch_administration.py` (the v2.2 differential).

**Not opened, deliberately:** `LAUNCH-GATE-v2.3-SEMANTIC-DELTA.md`, `RD-62-launch-machinery-v2.2-RAW.md`, `RD-55`/`RD-56`/`RD-47`/`RD-48` raw files, and every earlier round's review tree — so that this review's findings are the bytes' and not their reviewers'.

**Scratch artifacts:** all under `/tmp/rd65/` — `probe.py`, `probe2.py`, `diff_battery.py`, six throwaway clones (`c22` at `918574c`; `c23`, `c23b`–`c23f` at `494acab`), and the probe records named in §D. **Nothing was written to the frozen worktree or to `/home/tze/GitHub/syzygy`**; `git status --porcelain` is empty in both and all four subject digests reproduce unchanged at the end of this session.

---

## G. Judgement

`[Observed]` **v2.3 does what the charter asks first, and does it well.** Nothing was weakened: §1, §3, §6, §7 and §8 are byte-identical by span digest and by hunk mapping; the roster, the conjunct list, the emittable check set and `NEVER_DEFERRABLE` are identical strings; the only deletion is two provably-dead guard branches; and over a 31-case differential battery **no record fails under v2.2 and passes under v2.3**, while one becomes stricter. Six of RD-61's eleven findings are repaired outright, and I verified the five hardest — f1's working-tree route, f2's off-branch anchor, f3's `SDR-n` leak, f4's blank routing authority, f6's escaping `--prior` — **by rebuilding each attack and watching it fail**, not by reading any account of them. The f3 repair is stronger than asked: it closes the narrative-mention route even inside the owning record.

`[Observed]` **It does not clear.** The defect class this round exists to close — *the bytes failing a claim the amendment newly makes about itself* — is present in three clauses v2.3 wrote. **Finding 1**: §2 discharges the same-family obligation onto the generated report and justifies it by "the reports its rows link", when §6's byte-identical nine columns link nothing — so the disclosure F5 exists to force is once again absent from the log §6 says F1 is answered from *and only from*. **Finding 2**: §4's replacement for RD-61 m2 asserts the row outcome is "never of the environment", and one byte-identical record yields `NOT READY` with git available and `READY-WITH-DEFERRALS` without it, because an uncheckable warrant is counted as resolved — permissive, and against VIS-2. **Finding 3**: the f1 repair bound the schema to `HEAD` while everything else stays bound to the record's commit, and v2.3's own new ancestry rule guarantees `HEAD` is the later of the two; a committed enum widening therefore still produces an eligible record carrying `Met (with caveats)` and a `READY FOR` gate result. Each was constructed and executed, not argued.

`[Inferred]` None of the three is a route the v2.2 → v2.3 diff *opened* in the weakening sense — finding 3 is narrower than the hole it replaced, and findings 1 and 2 change no record's eligibility. But two of them are false statements the instrument newly makes about itself, and the third is a rule the instrument newly adopts under which an administration's lawfulness is not stable against its own commit. On the commission's fourth question I report: **no new false-`READY` path was opened by the amendment**, and **one pre-existing path survives it** — finding 3.

The two minors are residues of otherwise-good repairs: §4 names `LA-11` where `LA-12` fires (finding 4), and the m3 repair falsified §4's own specification of the column it fixed (finding 5).

Findings 1, 2, 3: MATERIAL. Findings 4, 5: MINOR.

VERDICT: REVISE
