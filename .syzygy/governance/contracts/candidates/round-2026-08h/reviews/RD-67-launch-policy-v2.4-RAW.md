# RD-67 — Launch-policy v2.4 semantic review (round-2026-08h)

| | |
|---|---|
| Review ID | **RD-67** — fourth administration of the RD-55 policy-semantics commission (charter §5 item 2) |
| Date | **2026-08-16** |
| Subject version | **v2.4** (candidate process policy) |
| Frozen commit | **`4dd6e2085237278b9f89e72be7755f5bf5c795c7`** |
| Subject digest | `launch-gate-pre-specifications.md` → `1852c2c3d31eff3afa0924b6b72e855481ab2516ba8fde5eda7b2ae8772f01e8` — **verified at start and at end** |
| Cross-ref digest | `launch-gate-administration.schema.json` → `e0167fb8af6a903c527d402d56c4fb85ebdfed9608de1a485f4f1563aa6a69fb` — **verified** |
| Also read (not authority) | `scripts/validate_launch_administration.py` `047098326af2f415…`, `scripts/render_launch_administration.py` `44d568e39727…` |
| Context | Fresh. No coordination with the parallel machinery reviewer |
| Model family | **Same as the corpus's authors** — this review supports repair and is **not** a formal launch administration (§2 family disclosure; F5) |
| Nothing edited | All probes ran in a throwaway clone under `/tmp/rd67/`, now removed. `git status --porcelain` in `/home/tze/GitHub/syzygy` shows only the two pre-existing untracked files, and both subject digests reproduce unchanged at the end of the session |

---

## A. Method

Every claim below was produced by reading committed bytes (`git show 4dd6e208:…`) or by executing code in a clone, never by trusting `LAUNCH-GATE-v2.4-SEMANTIC-DELTA.md`. The delta and the RD-65/RD-66 raws were read **after** the diff and the no-weakening sweep, as claims to be checked.

---

## B. The no-weakening sweep — findings: none

Two independent methods, both with stated denominators.

**Method 1 — section-span digests.** `[Observed]` I split each of v2.0/v2.1/v2.2/v2.3/v2.4 on `^## \d+\.`, asserted the spans re-concatenate to the whole file, and digested each. Denominator: **10 spans, exhausting the file at every version.**

| Span | v2.0 | v2.1 | v2.2 | v2.3 | v2.4 |
|---|---|---|---|---|---|
| §0 preamble | `9d47c028832d` | `08b200cd4581` | `3cff94f23005` | `fbfd5048181d` | `6e08cf62671e` |
| **§1 derivation tiers** | `1f2d1d60a28a` | `1f2d1d60a28a` | `1f2d1d60a28a` | `1f2d1d60a28a` | **`1f2d1d60a28a`** |
| §2 protocol | `0d7340f2ee9a` | `0d7340f2ee9a` | `0d7340f2ee9a` | `fb8b35a4eade` | `6c12f0aa6eae` |
| **§3 question series** | `fe0b051e136d` | `fe0b051e136d` | `fe0b051e136d` | `fe0b051e136d` | **`fe0b051e136d`** |
| §4 verdict computation | `f4a2a6423a89` | `84d5d3d456e7` | `8af5dbc5b7d8` | `f4e253572a4e` | `2aa2cecad2ce` |
| §5 record | `c6847ffa7812` | `0b6358554452` | `1fd518196e43` | `ae479eeaa24d` | `b07e9f2864aa` |
| **§6 trend log** | `9906fcac4540` | `9906fcac4540` | `9906fcac4540` | `9906fcac4540` | **`9906fcac4540`** |
| §7 generalization | `d24deb9c8eb3` | `9e17cb8de045` | `9e17cb8de045` | `9e17cb8de045` | `9e17cb8de045` |
| **§8 parameter block** | `01209c0f0529` | `01209c0f0529` | `01209c0f0529` | `01209c0f0529` | **`01209c0f0529`** |
| §9 changelog | `e49dde205d06` | `9301d992b12b` | `18029b54c3de` | `4d1ae72f6510` | `dddc4be0405a` |

`[Observed]` §1, §3, §6 and §8 are **byte-identical across all five v2.x versions**: no readiness question, no trend obligation, and no launch-scope parameter moved. The v2.3→v2.4 diff is **167 lines across 5 hunks**, confined to §0 (version bump), §2 (one clause), §4 (two blocks), §5 (one enumeration passage) and §9 (one changelog entry).

**Method 2 — population extraction from the deciding code and the schema.** `[Observed]`

| Population | Denominator | v2.0 → v2.4 |
|---|---|---|
| Question IDs in §3 (`^- \*\*([A-G]\d) \[UG\]\*\*`) | **35** (A1–A6, B1–B5, C1–C7, D1–D4, E1–E6, F1–F6, G1) | element-identical, same order, at all five versions |
| Row verdict vocabulary sentence, §2 | **4** words (`Met`, `Not met`, `Not met (out of launch scope)`, `Unknown(reason)`) | string-identical at all five versions |
| Gate verdict words, §4 table | **3** (+ `NONE`, four-valued from v2.2) | identical v2.1→v2.4 |
| Validator `ROSTER` | **39** rows | digest-identical `31d3620d` at all five versions |
| Computed formula conjuncts `_c(…)` | **6** | element-identical, same order, at all five versions |
| `NEVER_DEFERRABLE` | line-identical | unchanged |
| `LA-*` identifiers emittable | **17** (`LA-1…LA-16` + `LA-3b`) | empty symmetric difference v2.1→v2.4; §5's enumeration matches, and all 17 appear in `--selftest` fixture titles (**17/17**) |
| Schema row-verdict enum | **4** | schema byte-identical since v2.0 (`e0167fb8…`) |
| `--selftest` | validator **123**, renderer **38**, 0 failing | matches §9's claim exactly |

**Method 3 — differential execution on the one v2.4 formula-affecting change.** `[Observed]` The only v2.4 change that can move the row/formula outcome is the fail-closed `SDR-n` warrant. Over **6 constructed records** (clean; F2 `Not met` + SDR warrant; F2 `Not met` + repository-path warrant; F2 `Unknown` + SDR warrant; blocked core; bogus `SDR-777`), comparing `_git=True` against `_git=False`: **0 permissive-without-git**, 3 stricter-without-git, 3 same. `[Inferred]` The direction claim holds generally, because `_compute`'s only environment-dependent input is `resolved_deferrals`, and both citation branches require `_git`.

**Conclusion on the weakening question — with one exception.** `[Observed]` No readiness question, no row-level verdict word, no gate verdict word, no trend obligation, no §8 parameter, and no conjunct or branch of the §4 formula was dropped, renamed, or made unreachable at v2.4. The one check that v2.3 enforced and v2.4 does not is **finding 4** below.

---

## C. Findings

### 1 — BLOCKING `[Observed]`

**§5, the checks enumeration, lines 806–818:** *"the schema's own identity — read from the **committed bytes at the record's own commit**, exactly as the instrument is, **never the working tree and never `HEAD`**"* — and §9's v2.4 entry: *"The schema is read at the **record's own commit** … not at `HEAD` — so a committed widening at `HEAD` no longer governs an ancestor administration (RD-65 f3)."*

**Both claims are false for any record whose `repository_commit` is abbreviated,** and the schema itself permits abbreviation. `launch-gate-administration.schema.json` types `repository_commit` as `"pattern": "^[0-9a-f]{7,40}$"` — **7 to 40** hex. The v2.4 validator gates the record's-commit schema read on a stricter test:

```python
schema_commit = (raw_commit if isinstance(raw_commit, str)
                 and re.fullmatch(r"[0-9a-f]{40}", raw_commit) else None)
...
elif _git and schema_commit is not None:   # read at the record's commit
elif _git:                                 # ← falls through to HEAD
    blob = _git_show("HEAD", SCHEMA_NAME)
```

A 7–39-hex commit is schema-conformant, passes `LA-2` ancestry, resolves the instrument digest, resolves every evidence citation — and silently routes the schema read to **`HEAD`**, which is exactly the condition RD-65 f3 named and v2.4 claims to have removed.

**Constructed exploit, executed in a clone at `4dd6e208`.** `c0` = `4dd6e208…` (the frozen commit). I committed a one-token enum widening (`"Met (with caveats)"`) on top, making `HEAD` = `6a872515…`. I then bound three otherwise-lawful `formal`/`full`/`fresh` records to the **ancestor** `c0`, each answering **A1** with the forbidden word `Met (with caveats)`:

| `repository_commit` | errors | verdict | eligible | gate result |
|---|---|---|---|---|
| `4dd6e2085237…` (full 40 hex) | **2** — working-tree drift, *and* `'Met (with caveats)' is outside the closed set` | `None` | `None` | — |
| `4dd6e2085237` (12 hex) | **0** | `READY FOR Capability 1 …` | **`True`** | **`READY FOR Capability 1 — Project registration and honest shape visibility`** |
| `4dd6e20` (7 hex) | **0** | `READY FOR Capability 1 …` | **`True`** | **`READY FOR Capability 1 …`** |

**Why this is a readiness defect, not only a false sentence.** §2 closes the row vocabulary specifically so that *"a softened verdict is a schema error rather than a reading the next reader has to catch."* `_compute` blocks on A–D rows only for the literal `Not met` (`ad_blockers = [q for q in AD_ROWS if verdict_of.get(q) == NOT_MET]`), so a row reading `Met (with caveats)` on **any of the 22 A–D rows** is neither `Met` nor a blocker: it passes silently into an eligible `READY FOR`. This is RD-61 f1's incident — *"validated a forbidden verdict word into an eligible `READY` record"* — reproduced verbatim at a new address, in the same file family, three repair rounds later.

**Reachability is not hypothetical.** Seven-character SHAs are the repository's own house style: §6's own trend-row generator emits `rec["repository_commit"][:7]`, and every trend row in the log is abbreviated. A reviewer transcribing the commit as they see it everywhere else in the corpus writes exactly the value that opens this path.

This is the **class defect the owner's arm (c) ruling commissioned v2.4 to close** — a property repaired at the instance the reviewer named (40-hex commits) and then restated in §5 and §9 as a class property (*"never … `HEAD`"*) that the machinery does not deliver.

---

### 2 — MATERIAL `[Observed]`

**§4, Qualifications, lines 634–637:** *"F2 is the **only** limb a deferral can lawfully name, so 'any other owner deferral' is a **validation error**, never a verdict conversion"*, annotated *"(Check named accurately at v2.4, RD-65 f4 … The outcome is the same either way, so the clause named one check where two fire; 'a validation error' is the true statement.)"*

**"A validation error" is false in 2 of the 3 reachable populations.** `LA-11` errors only for `NEVER_DEFERRABLE` rows (E ∪ A–D ∪ {F1, F3, F4}); F5 and F6 are the 2 of 39 roster rows that are neither F2 nor never-deferrable, and they fall to `LA-12` — whose guard is `if n_deferred and branch == "blocked" and core`. Enumerating the three combinations a non-F2 deferral can sit in (denominator **3**):

| Case | branch | core | Errors raised | Result |
|---|---|---|---|---|
| F5 deferral alone, core passes, F2 `Met` | `blocked` | True | **1** (`LA-12`) | caught — the only fixture that exists |
| F5 (or F6) deferral **beside a lawful, resolving F2 deferral** | `deferrals` | True | **0** | `READY-WITH-DEFERRALS`, `eligible: True` |
| F5 deferral in a record whose core already fails | `blocked` | **False** | **0** | `NOT READY`, `eligible: True` |

`[Observed]` Executed at `4dd6e208`: a `formal` record with F2 `Not met` + a resolving `SDR-9` F2 deferral **and** F5 `Not met` + an `SDR-9` F5 deferral yields **errors=0, verdict `READY-WITH-DEFERRALS`, eligible `True`, deferred=2**. Same for an F6 deferral. `--selftest` has one fixture for the caught case (`LA-12 a deferral on a non-F2 limb beside a Not met F2 is an error`) and none for either uncaught one.

The v2.4 repair of RD-65 f4 replaced a **wrong identifier** with a **false universal**, in the same clause, in the pass commissioned to correct it. The second half of the sentence (*"plain `READY FOR` over a nonzero `len(owner_deferrals)` is a contradiction the branch predicates themselves make unconstructible"*) `[Observed]` **is** true — `branch == "plain"` entails `n_deferred == 0`.

---

### 3 — MATERIAL `[Observed]`

**§2, same-family clause, lines 148–151:** *"The trend log does **not** carry a family column — a disclosed limit (**§8 residual on F5**), not a claim."*

**There is no §8 residual on F5.** `[Observed]` Sweep of the §8 span (6,577 bytes, the whole section, extracted by the same contiguity-checked split as §B): occurrences of `"F5"` → **0**; `"residual"` / `"Residual"` → **0**; `"family"` → **0**. A whole-file `residual` sweep returns 5 hits — this one in §2, and 4 in §9's changelog, none of them a §8 residual on F5. §8 is `[Observed]` byte-identical (`01209c0f0529`) at every version v2.0–v2.4, so no such residual could have been added for v2.4; the delta's own "Disclosed limits" list is in the **delta**, which is a frozen round artifact, not §8.

RD-65 f1's finding was that §2's justifying clause pointed at something that does not exist (*"the reports its rows link"* — §6's rows link nothing). **v2.4 removed that pointer and installed another pointer at something that does not exist.** Same clause, same defect shape, one version later.

The rest of the f1 repair `[Observed]` **is** true and verified: §6's table has **9 columns** and no link (`Date | Commit | Not-met | Scoped | Unknown | Deferred | Reopened | New findings vs prior | Gate verdict`); the schema `required`s `reviewer.model_family` and `reviewer.same_family_as_corpus_authors`, with `model_family`'s own description reading *"F5's disclosure lives here"*; and the renderer emits `- Model family: …` plus the same-family warning line. §4 does state F5/F6 are not conjuncts. Only the cross-reference is false.

---

### 4 — MATERIAL `[Observed]`

**A check v2.3 enforced that v2.4 does not.** At v2.3 the schema read was a single `elif _git:` branch that **always** read `HEAD` and **always** ran the working-tree drift comparison:

```python
elif _git:
    blob = _git_show("HEAD", SCHEMA_NAME)
    ...
    if wt is not None and wt != schema_src:
        errors.append("LA-1: the working-tree … differs from the schema committed at HEAD …")
```

At v2.4 the drift comparison lives **only** inside `elif _git and schema_commit is not None:`. For the abbreviated-commit population of finding 1, the fallback `elif _git:` branch reads `HEAD`'s blob with **no drift comparison at all**. `[Observed]` In the exploit above, the full-40-hex record raised the drift error; the 12-hex and 7-hex records raised **nothing**, though the working tree and the record's commit disagreed on the schema by exactly the same bytes.

This is a literal instance of the commission's definition — *"removes a check the prior version enforced"* — for a population the schema itself admits. It shares a root cause with finding 1 but is a distinct loss: even where the widening is in the **working tree** rather than committed at `HEAD`, v2.3 flagged the drift and v2.4 does not.

---

### 5 — MINOR `[Observed]`

**§4, line 543–545 (the v2.4 replacement text):** *"The gate result is the one `NONE — <limbs>` string of §4's fourth outcome above, **on every surface**."* And, three paragraphs above: *"§6's column vocabulary is four-valued and all four values are defined here."*

`[Observed]` The trend-log surface does not carry that string. `trend_row()` appends a fifth component for ineligible records:

```python
col = (computed["gate_result"] + "; row outcome was " + computed["verdict"])
```

Executed at `4dd6e208`, a `formal: false` / `delta` record deposits into the Gate-verdict cell:

```
NONE — `formal: false`; `administration_kind: delta`; row outcome was READY FOR Capability 1 — Project registration and honest shape visibility
```

Three consequences: (a) the trend surface's string is **not** the terminal-line/validator string, falsifying the new "on every surface" absolute; (b) the Gate-verdict cell's value is none of the four defined words, falsifying "four-valued"; (c) the literal text `READY FOR Capability 1 …` appears **inside the Gate-verdict column** of a diagnostic administration — precisely the conflation §4 exists to prevent, and precisely what the generator's own docstring forbids (*"an ineligible administration whose rows all read `Met` must not deposit `READY FOR …` into the log F1 is answered from and only from"*).

§4's preceding sentence does disclose that "its row outcome travels beside it", which mitigates the reader hazard — hence MINOR rather than MATERIAL. But the absolute introduced at v2.4 to repair RD-65 f5 is still not true of the emitted bytes: v2.3 said `NONE — not eligible` (wrong), v2.4 says `NONE — <limbs>` (still short by one clause).

---

## D. What v2.4 repaired, verified true

Reported for balance; none of these is a finding. `[Observed]` each by construction at `4dd6e208`:

- **RD-65 f2** — §4's "never of the environment" is gone and the replacement is accurate. The `SDR-n` branch adds to `resolved_deferrals` only on `_git and _sdr_exists(...)`; the repository-path branch is gated on `_git` too. Differential over 6 records: **0 permissive-without-git**. The fail-closed claim, and the "one environment dependence … only in the stricter direction" framing, are true.
- **RD-66 f3 / `LA-2`** — §5's *"the instrument path — fixed by the tool … never selected by the record"* is true: `INSTRUMENT_NAME` is a module constant, and a record binding `docs/launch-gate-pre-specifications.md` yields 2 errors and `eligible: False`.
- **RD-66 f4** — §5's *"the record-declared prior read from its committed bytes at the record's commit, never the working tree"* is implemented (`_git_show(commit, relpath)`, with an uncommitted prior yielding `LA-15` and `new_findings = "unknown"`, never a forged integer).
- **RD-65 f1's substantive half** — record fields and report line, as in finding 3.
- **RD-65 f4's second half** — plain `READY FOR` over a nonzero deferral count is genuinely unconstructible.
- **§5's enumeration completeness** — `LA-1…LA-16` + `LA-3b` = **17/17** named in `--selftest` fixture titles; `--selftest` reports 123 and 38 fixtures, 0 failing, matching §9.

---

## E. Answer to the commissioned question

**Did v2.0→v2.4 weaken, drop, rename, or make unreachable any readiness question, row-level verdict word, trend obligation, or conjunct/branch of the verdict formula?** `[Observed]` No, on all four populations, by two independent methods with the denominators stated in §B — **except** finding 4, which removes a working-tree drift check v2.3 enforced for every record and v2.4 enforces only for 40-hex-commit records.

**Does the instrument's own prose (§2, §4, §5) make any claim that is false against the machinery it describes?** `[Observed]` **Yes — four.** §5's *"never … `HEAD`"* (finding 1, load-bearing: a not-ready state reaches an eligible `READY FOR`); §4's *"'any other owner deferral' is a validation error"* (finding 2); §2's *"(§8 residual on F5)"* (finding 3); §4's *"the one `NONE — <limbs>` string … on every surface"* (finding 5).

`[Inferred]` Three of the four false claims (1, 2, 3) sit in clauses **v2.4 rewrote in this very pass to repair RD-65 f3, f4 and f1** — the third round in a row in which a repair closes the named instance and restates the result as a class property the machinery does not hold. The mechanical forgery sweep (RD-66 f1) is a genuine class repair; the policy-side repairs in this pass are not. `[Unknown]` Whether the residual populations are exhaustible by inspection, or whether the schema/validator/prose triangle needs a mechanical agreement check of its own (e.g. deriving every commit-read gate from the schema's own pattern rather than a hand-written `re.fullmatch`), is a design question I am not commissioned to settle.

Findings 1 and 4 are repairable inside the machinery in one line each (accept the schema's own `^[0-9a-f]{7,40}$` for the schema read, or narrow the schema's pattern to 40 hex so the two agree by construction, and move the drift comparison out of the conditional). Findings 2, 3 and 5 are prose corrections. None requires a question, verdict word, or formula change.

Because finding 1 admits a not-ready state to an eligible `READY FOR` gate result with zero errors, and three further prose claims are false against the machinery they describe, v2.4 is not approvable as read.

VERDICT: REVISE
