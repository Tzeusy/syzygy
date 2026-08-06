# RD-7 — Public clone verification review

**Clone source commit:** a7b3375
**Commissioned:** 2026-08-07, independent, no authoring context.

# VERDICT
VERDICT: EXCEPTIONS

All five acceptance acts are **performable from a fresh clone**. Every act
argument recomputes to its subject from clone bytes alone, the full battery
runs and reports identically to the source tree, and no ceremony step needs
anything git does not track. The exceptions below are real and two of them
touch the artifact act 1 binds — but none of them prevents an act, and none
changes what an act binds.

The sharpest: **performing act 1 as the record documents it breaks eight
pointers inside the accepted modules**, and the record claims the opposite in
the same paragraph that instructs the install.

---

## 0. Method and scope

Clone made with `git clone /home/tze/GitHub/syzygy clone-check` into the
scratchpad. No `_bootstrap/`, no `.claude/settings.local.json`, no untracked
founder files. Verified at `a7b337522f50ea440903200cf9811226c2b62d1c`.

Everything below was run **in the clone**. The source tree was run only to
diff outputs, and was not modified. Six mutation copies (`mut`, `mut2`,
`mut3`, `mut4`, `m-craft`, `m-topo`, `m-ovw`), one no-git copy (`nogit`), and
one post-act simulation (`actsim`) were made from the clone, never from
source.

`grep` here is ugrep, so every load-bearing sweep in this review is Python
`re`, not a bracket class.

---

## 1. The battery in the clone

[Observed] All seven commands run to completion in the clone and their
**output** — not merely their exit code — is readable and complete.

| Command | Clone result |
|---|---|
| `scripts/check_governance.py` | `26 OK, 14 WARN, 0 FAIL (40 checks)` |
| `scripts/check_governance.py --selftest` | `77 fixtures, 0 failing` |
| `$CS/verify_final_prespec.py` | `PASS — all checks clean` |
| `$CS/build_contract_index.py --check` | `index matches regeneration — no drift` |
| `$CS/build_dependency_index.py --check` | `dependency index matches regeneration — no drift` |
| `$CS/build_budget_report.py --check` | `fixture anchors match regeneration` |

[Observed] **Diffed against the source tree, every output is identical except
for six lines, and all six are explained by one untracked file.** The source
working tree carries `syzygy_claude_surgical_final_prespec_closure_prompt.md`
(untracked, not ignored). The full diff of `check_governance.py` output is:

```
scope:     clone — 260 file(s) (259 tracked, 1 untracked)   [source]
scope:     clone — 259 file(s) (259 tracked, 0 untracked)   [clone]
CG-2a  249 -> 248 files examined
CG-3   243 -> 242 files examined
CG-12   43 ->  42 citations examined
CG-16   53 ->  48 mentions examined
CG-22  155 -> 154 files examined
```

Every verdict word, every finding count, and every detail line is unchanged.
`verify_final_prespec.py` differs only in its `root:` line. The other three
scripts are byte-identical.

[Observed] **No check behaves differently in the clone.** That is the
headline for commission item 1.

### 1a. Degradation without git

[Observed] Removing `.git` entirely does not break the battery. It reports:

> `scope: filesystem walk — 259 file(s) examined. git is unavailable here, so
> tracked/ignored status is Unknown: CG-11 cannot run and `--scope tracked` is
> not honored. Every other check runs over the walked corpus.`

Result becomes `25 OK, 15 WARN, 0 FAIL`. The lost check degrades to **Unknown
and says so**, rather than to green. That is VIS-2 behavior in the checker
itself.

### 1b. The checks can fail

[Observed] Mutation-tested per predicate (verification rule 6), each in a
fresh copy of the clone:

| Mutation | Caught by |
|---|---|
| Act-1 argument falsified in the ceremony record | CG-7b, CG-7d, CG-7e (3 FAIL) |
| A contract module edited (`RFC-0010`, one appended line) | CG-7a, CG-18 (2 FAIL) |
| Act-2 subject edited (`testing-and-verification.md`) | CG-7c, CG-7d, CG-7e, CG-18 (4 FAIL) |
| Act-3 subject edited (`BUNDLE-MANIFEST.md`) | CG-7c, CG-7d, CG-7e (3 FAIL) |
| Act-4 subject edited (`OVERVIEW.md`) | CG-7c, CG-7d, CG-7e (3 FAIL) |
| Act-5 subject edited (`…-D3.md`) | **CG-7e only** (1 FAIL) |

Every act subject is guarded. Act 5 is guarded by exactly one predicate — see
finding E-4.

---

## 2. The five acts are performable

[Observed] **Navigation from `README.md` is two hops.**

1. `README.md:12` → `PROJECT-STATUS.md` ("See `PROJECT-STATUS.md` for the
   exact gate state"). `README.md:102-103` also points at
   `.syzygy/governance/contracts/candidates/` as "the candidate contract
   corpus (RFC 0001–0011) and its acceptance record."
2. `PROJECT-STATUS.md:38-42` names the offering by full path:
   `.syzygy/governance/contracts/candidates/round-2026-08b/FINAL-OWNER-ACCEPTANCE-RECORD.md`
   "(the `round-2026-08/` one is superseded and banner-marked)".
3. That file's own header, lines 3-6, defers the ceremony:
   > "Where this file and `../FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`
   > disagree, **that record wins** — it owns the exact phrases and the
   > ceremony."

[Observed] Both hops resolve in the clone. The deferral is consistent with
`AGENTS.md`, which says "The acceptance record owns the phrases and the
ceremony." No contradiction between the two records was found: the four
digest-bound arguments are identical in both.

### 2a. Phrases and digests, recomputed by me with `sha256sum`

[Observed] Each digest below was computed by me from clone bytes, not read
from prose. All five match.

| Act | Phrase location | Digest computed by me | Match |
|---|---|---|---|
| 1 | `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:15` — `` `ACCEPT COMPACTED FOUNDATIONAL RFCS: 2862b2f5…f057d7` `` | `sha256sum ACTIVE-CONTRACT-MANIFEST.txt` = `2862b2f54e39e6d477129147eb2e1d0cb4ca714c26edabd75505e2e38ff057d7` | ✅ |
| 2 | `…:16` — `` `CONFIRM CRAFT AMENDMENT: CC-TEST-2@7a716090…690a0` `` | `sha256sum …/craft-and-care/testing-and-verification.md` = `7a716090bc827121b3f70c4f7e252fc5680cd8a56d7b4121b70f3673489690a0` | ✅ |
| 3 | `…:17` — `` `ACCEPT TOPOLOGY: 7a3b2249…bfaeb45` `` | `sha256sum …/topology-candidates/BUNDLE-MANIFEST.md` = `7a3b22494a08d888901c1f0cec76833dc926e89b6f510b5abf8963071fbaeb45` | ✅ |
| 4 | `…:18` — `` `ADOPT PROJECT OVERVIEW: 01d62951…c7cd1` `` | `sha256sum .syzygy/intent/OVERVIEW.md` = `01d629515993188338f6a0e2d84d67543d8569003759a7c8f571a90b129c7cd1` | ✅ |
| 5 | `…:19` — no phrase: "VIS-4 owner adoption, no magic phrase"; argument at `round-2026-08b/FINAL-OWNER-ACCEPTANCE-RECORD.md:43` | `sha256sum …/DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md` = `e973e8e025c93b5d1e59d16d8661b0ae1f9804304c8f8de8957950acf3d8f9c9` | ✅ |

### 2b. Digest independence — all 32 modules, not a sample of six

[Observed] The commission asked for at least six. I recomputed **all 32**:

```sh
cd .syzygy/governance/contracts/candidates
find rfcs -name '*.md' | sort | xargs sha256sum
```

diffed against the manifest body (`grep -v '^#'`): **zero differences, 32/32.**
No mismatch to report.

### 2c. The ceremony steps execute

[Observed] Act 1 step 3 says the copy "is digest-verified by running
`sha256sum -c ACTIVE-CONTRACT-MANIFEST.txt` **from
`.syzygy/governance/contracts/`**". Simulated in `actsim`: copied
`candidates/rfcs`, `candidates/history`, `candidates/matrix-rows` to
`contracts/`, ran the command from `contracts/` — **32/32 `OK`**, exactly as
written.

[Observed] Act 3's manifest carries its own `sha256sum -c` block. Extracted
and run from the bundle directory: **9/9 `OK`**.

[Observed] `ACCEPTANCE-ACT-RECORD.md` is absent, which `PROJECT-STATUS.md:34-36`
declares is correct — it is created by the first act. CG-1c prints it as a
declared forward reference rather than a broken link.

[Observed] The ceremony's only `_bootstrap/` step is explicitly excluded from
itself (`FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:124-129`):

> "**That mirror is not part of the ceremony.** `_bootstrap/` is git-excluded
> and absent from every clone, so a step that required it would make the
> ceremony unexecutable by anyone but the founder … Skipping it loses nothing
> an act depends on."

**Conclusion for commission item 2: 5 of 5 acts are performable from the
clone.**

---

## 3. Findings

### E-1 (material) — the link checker cannot detect a wrong-depth relative path

[Observed] `scripts/check_governance.py:283-299`, `_resolve`, falls back to
suffix matching after relative and root resolution fail:

```python
t = os.path.normpath(target).replace(os.sep, "/").lstrip("./")
if not t:
    return False
return any(p == t or p.endswith("/" + t) for p in all_paths)
```

`str.lstrip("./")` strips *characters*, not a prefix. So
`normpath("../../decisions/PENDING-OWNER-DECISIONS.md")` becomes
`decisions/PENDING-OWNER-DECISIONS.md` — **the traversal is discarded
entirely** — and then matches any tracked path with that suffix.

[Observed] Mutation-proved. Appending to
`round-2026-08b/FINAL-OWNER-ACCEPTANCE-RECORD.md`:

```markdown
A deliberately wrong-depth link: [overview](../../../../../../../intent/OVERVIEW.md)
```

— seven levels up, which from that directory points outside the repository
entirely — yields:

```
OK    CG-1a  markdown links resolve — 128 links examined, 0 findings
26 OK, 14 WARN, 0 FAIL (40 checks)
```

The denominator incremented; the finding count did not.

[Inferred] The docstring's stated intent — "suffix matching models how they
are actually written", for bare citations like `RFC-0002/README.md` — is
sound and covers 670 of the 701 references that resolve only by suffix. The
defect is that the same branch also absorbs the **31 references written with
explicit `../` traversal** (23 unique), where the author did state a depth and
stated it wrongly.

[Observed] Independent sweep, Python `re`, denominator stated: of **126**
markdown links and **1277** code-span references in tracked `.md` files, **701
resolve only via the suffix fallback**; of those, **31 occurrences / 23 unique
carry explicit traversal**. Breakdown:

| Class | Count | Assessment |
|---|---|---|
| Raw reviewer output (`reviews/**`: RB-2, RC-2, RC-3, RD-6, rev10-digestibility) | 8 | **By design** — never edited; CG-1f classifies three of these and silently absorbs the rest |
| Historical packet (`04-CLAUSE-MIGRATION-MATRIX.md`) | 9 | **Historical** — rev9-era matrix |
| Superseded round (`round-2026-08/**`) | 3 | **Historical** — banner-marked |
| Active candidate (`CONTEXT-BUDGET-REPORT.md:74,92,101,110` → `../round-2026-08b/reviews/RC-12-budget-waiver-RAW.md`) | 1 unique | **Genuinely broken** — correct is `round-2026-08b/…` |
| **Inside act 1's digest set** (`rfcs/RFC-0010-mission-control-autonomy.md`) | 1 unique, 4 occurrences | **Genuinely broken** — see E-2 |

Note that CG-1a has **no** historical or raw-review branch at all
(`check_governance.py:309-321` classifies only forward refs and vendored
gaps); markdown links in those lanes pass solely because `_resolve` absorbs
them. CG-1b does have those branches (`:336-339`). The asymmetry is why CG-1f
prints three references while eight exist.

### E-2 (material) — a module inside act 1's digest set points at a file that exists at no depth

[Observed] `rfcs/RFC-0010-mission-control-autonomy.md` cites
`` `../../history/RFC-0010-history.md` `` at lines **26, 705, 746, and 781**.
Line 26 is the module's amendment-history pointer:

> `.syzygy/governance/contracts/candidates/rfcs/RFC-0010-mission-control-autonomy.md:25-26`
> "predecessor. **Amendment history and rationale:**
> `../../history/RFC-0010-history.md` (non-normative)."

[Observed] From `candidates/rfcs/`, `../../history/` resolves to
`.syzygy/governance/contracts/history/`, which **does not exist**. The correct
target is `../history/` → `candidates/history/RFC-0010-history.md`, which does
exist.

[Observed] The depth is wrong because RFC-0010 is a **flat** module while the
`../../` form is correct for the **nested** ones (`rfcs/RFC-0002/README.md`
etc.). Swept all 32 modules for backtick-quoted `..` paths: **RFC-0010 is the
only module with the defect, at 4 occurrences.** RFC-0001, RFC-0006 and
RFC-0011 — the other flat modules — are clean.

[Observed] It is broken **both before and after** act 1: after the install it
resolves to `.syzygy/governance/history/`, also absent.

[Inferred] Severity is bounded — the target is explicitly non-normative
rationale, and the pointer's brokenness does not change what act 1 binds or
whether its digest verifies. But the owner is being asked to bind bytes in
which the contract's own route to its rationale is dead, and CG-1b reports
`0 findings` over it because of E-1.

### E-3 (material) — performing act 1 breaks eight pointers, and the record claims it fixes them

[Observed] `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:105-110` states:

> "**Companion material, installed but not accepted:** act 1's install also
> copies `history/` and `matrix-rows/` to
> `.syzygy/governance/contracts/history/` and `…/matrix-rows/` **so the
> modules' 68 Tier-2 rationale backlinks and the RFC-0003 README's census link
> resolve from the governed tree.**"

[Observed] Simulated the install exactly as documented (`actsim`) and swept
the 32 installed modules for relative backlinks: **81 examined, 12
unresolved.** Of those 12:

- **8 break as a direct consequence of the act.** Six package READMEs cite
  `` `../../CONTEXT-BUDGET-REPORT.md` `` (RFC-0002:53, RFC-0004:54,
  RFC-0005:52, RFC-0007:49, RFC-0008:52, RFC-0009:58, RFC-0009:216) and
  `` `../../03-ACTIVE-CONTRACT-COMPACTION-REPORT.md` `` (RFC-0009:209). These
  **resolve today** in the candidate tree (`../../` = `candidates/`) and
  **stop resolving after the act** (`../../` = `governance/`), because act 1's
  install copies only `rfcs/`, `history/` and `matrix-rows/` — the two reports
  stay behind in `candidates/`.
- **4 are the RFC-0010 occurrences of E-2**, broken in both trees.

[Observed] So the record's claim that the companion install makes the Tier-2
backlinks "resolve from the governed tree" is **false for 12 of the 81
relative backlinks the installed modules carry**, and the act is what falsifies
eight of them.

[Observed] CG-14 does not catch this. Its docstring
(`check_governance.py:1338-1356`) and body (`:1364-1389`) scope it to
**directory paths named in ceremony §2**, checking each for presence or absence
per its declared role — `11 paths examined, 0 findings`. It validates install
*sources and destinations*; it does not re-resolve the installed content's
*internal* backlinks at their destination depth.

[Inferred] This is the same defect class the record already records having
fixed once, one paragraph earlier — "this step previously named a source path
`topology/` that exists in no clone … the ceremony was unexecutable as
written" (`:99-104`). CG-14 was built for that class. The post-move backlink
case sits just outside its predicate.

### E-4 (minor) — act 5's phrase form exists only as a retired value and a template

[Observed] `check_governance.py:717-719` defines act 5's subject with the
regex `ADOPT DOCTRINE AMENDMENT:\s*D3@([0-9a-f]{64})`, commented "The round
charter offers a phrase form anyway, so it is made available and checked."

[Observed] Swept every tracked non-`.py` file for `D3@` or
`ADOPT DOCTRINE AMENDMENT`. **No current instance of that phrase form exists.**
The complete population:

- `round-2026-08/FINAL-OWNER-ACCEPTANCE-RECORD.md:148` —
  `RETIRED — ADOPT DOCTRINE AMENDMENT: D3@0328cb37…` (superseded file, stale
  digest, explicitly marked retired)
- `round-2026-08/OWNER-ROUND-CHARTER.md:1226-1227` — a
  `D3@<digest>` **template**, superseded round
- three prose/disposition mentions and two raw-review mentions

[Inferred] CG-7d's act-5 predicate therefore has a **zero live denominator** —
it can never fire. Act 5's digest is guarded by CG-7e alone, which is why the
act-5 mutation produced exactly one FAIL where the other four produced three
or four.

[Observed] This does **not** make act 5 unperformable: the defining record
(`:19`) says act 5 needs no phrase — "VIS-4 owner adoption, no magic phrase" —
and its current argument `e973e8e0…` is present and correct at
`round-2026-08b/FINAL-OWNER-ACCEPTANCE-RECORD.md:43`. Recorded because the
same observation appears at `round-2026-08b/reviews/RC-9-public-clone-RAW.md:458`,
so it is a **carried, unrepaired** finding, not a new one.

---

## 4. Founder-local leakage — commission item 5

[Observed] Denominator: **254** `_bootstrap/` citations across tracked
non-`.py` files, in 92 files. Classified by whether the citation instructs the
reader to *consult* the tree.

**Permitted (history / disclosure): 254.**
**Defects (cited as an authority the reader must open): 0.**

[Observed] Fourteen citations are imperative-*shaped* and were read
individually. All fourteen are one of: a disclosure that the tree is
git-excluded and absent; a reviewer stating they did **not** read it; or a
historical disposition recording that an old pointer was wrong. None
instructs a clone-reader to open it.

[Observed] The one such citation in the ceremony file itself is a **retraction**
(`FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:167-172`):

> "**Corrected 2026-08-05.** This paragraph previously stated that the package
> 'lives in the deliberately git-excluded `_bootstrap/` working tree plus the
> delivered review packet'. That was true when it was written and became false
> when the package was tracked; it survived because nothing checked it. The
> claim is retired rather than deleted, because a reader who saw the old text
> needs to know it was wrong, not merely that it is gone."

[Observed] The adjacent live text now reads "Nothing the ceremony needs lives
outside the clone: a collaborator with only `git clone` can recompute every act
digest and run every validation" (`:161-163`). **I independently confirmed
that claim is true** — see §2.

[Observed] This is consistent with the repo's own CG-12, which reports
`no _bootstrap/ cited as a required source — 42 citations examined, 0 findings`
(its denominator is scoped more narrowly than my 254; both agree on zero
findings).

---

## 5. Script robustness — commission item 6

[Observed] Six tracked `.py` files. Findings:

- **No founder-path dependency.** The only `/home/` literals in
  `check_governance.py` are `:1777`, the `LOCAL_LOCATOR` **detector** regex
  (`/home/|/Users/|%USERPROFILE%` — the check that catches founder-local paths),
  and `:2368`, `:2373`, which are `--selftest` **fixture inputs** for that
  detector. Neither is a path the script reads.
- **git is optional and its absence is disclosed**, not silently tolerated —
  see §1a.
- **Nothing writes outside the repo.** `build_budget_report.py` derives all
  targets from `__file__` (`:40-46`: `CANDIDATES = os.path.dirname(HERE)`,
  `ROOT = …join(CANDIDATES, "..","..","..","..")`,
  `REPORT = …join(CANDIDATES, "CONTEXT-BUDGET-REPORT.md")`). Its three write
  calls (`:390`, `:399`, `:446`) are the generator and the selftest mutator.
- **`--check` mode is read-only.** After running the entire battery in the
  clone, `git status --porcelain` is **empty**. No script mutated the clone.

---

## 6. Dangling references — commission item 4, denominators stated

[Observed] Tracked `.md` files swept with Python `re`. **126 markdown links**
(excluding external and anchor-only) and **1277 code-span path references**.

Repo-reported classification (`check_governance.py`, clone run):

| Bucket | Count | Assessment |
|---|---|---|
| CG-1a broken markdown links | 0 | but see E-1 — the predicate is weak |
| CG-1b broken code-span references | 0 | same |
| CG-1c declared forward references | 10 | **By design** — an owner act creates these (`ACCEPTANCE-ACT-RECORD.md`, `contracts/rfcs/**`, `.syzygy/project.yaml`) |
| CG-1d frozen-packet references | 26 | **Historical** — the rev9 packet lived under `_bootstrap/` |
| CG-1e vendored-substrate scope gaps | 39 | **By design** — `th-engineering` subskills deliberately not vendored; `GOVERNANCE-SUBSTRATE-LOCK.yaml` `th_engineering.vendored.scope_note` names the boundary. Covers all 46 of my raw `.claude/` + `.codex/` hits after dedup |
| CG-1f raw-review shorthand | 3 | **By design** — verbatim output, never edited |

[Observed] My independent sweep found **52 unresolved markdown links of 126**
by strict relative resolution. 46 are the CG-1e vendored gaps. The remaining
**6** — one in a superseded record, five in raw review output — fall into
**none of the four printed buckets** yet are absorbed silently by `_resolve`'s
suffix fallback. That is E-1's visible symptom: the classification the repo
prints is narrower than the exemption it actually applies.

**Genuinely broken, after classification: 2 unique targets** — E-2
(`RFC-0010`, 4 occurrences, inside act 1's digest set) and
`CONTEXT-BUDGET-REPORT.md`'s `../round-2026-08b/reviews/RC-12-budget-waiver-RAW.md`
(4 occurrences, active candidate lane). Plus the **8** post-act breakages of
E-3, which are not visible to any sweep of the pre-act tree.

---

## 7. What I did not do — [Unknown]

- I did not read anything under `round-2026-08c/reviews/`, per the
  commission. Where this review's findings overlap prior reviewers, I know
  only what non-review files quote (E-4 cites RC-9 via
  `round-2026-08b/reviews/`, which was not excluded).
- I did not read commit messages.
- I did not evaluate **clause content** — whether the contracts say the right
  things is outside this commission. I verified only that the bytes the acts
  bind are the bytes the clone has, and that the ceremony over them executes.
- I did not verify the "68 Tier-2 rationale backlinks" figure in the
  acceptance record against its own definition; I measured **81 relative
  backlinks** in the installed modules by my own predicate (backtick-quoted
  relative paths ending `.md`/`.txt`), which may not be the same population
  the record counts. The 12 unresolved are unresolved under either count.

---

## 8. Summary

[Observed] **5 of 5 acts performable from a fresh clone.** All five arguments
recompute from clone bytes; all 32 module digests match; both `sha256sum -c`
ceremony steps execute as written; the battery is clone-identical, fails when
it should, degrades honestly without git, and writes nothing.

Exceptions, in severity order:

1. **E-3** — act 1's install breaks 8 backlinks in 6 accepted modules, and the
   record's install paragraph claims the opposite. CG-14 checks install routes,
   not installed content's internal links.
2. **E-1** — `_resolve`'s suffix fallback discards `../` traversal, so no
   wrong-depth path can ever fail CG-1a/CG-1b. Mutation-proved with a link
   pointing outside the repository.
3. **E-2** — `RFC-0010`, inside act 1's digest set, points at its amendment
   history at a depth that exists in neither the candidate nor the governed
   tree, 4×.
4. **E-4** — act 5's digest-bound phrase form exists only as a retired value
   and a template; CG-7d's act-5 predicate has a zero live denominator, leaving
   CG-7e as its sole guard. Carried from RC-9, unrepaired.

E-1 is the root cause of E-2's invisibility and contributes to E-3's. Fixing
`_resolve` to preserve traversal — and adding a post-install link resolution
pass to CG-14 — would surface all three mechanically.
