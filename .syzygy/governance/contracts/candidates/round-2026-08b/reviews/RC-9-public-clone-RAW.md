# RC-9 — Public-clone / fresh-collaborator review (RAW)

**Reviewer posture.** Independent fresh-context session. No authoring history
sought or read. All work performed inside a real `git clone` at
`/tmp/claude-1000/-home-tze-GitHub-syzygy/6fa92108-6a63-4a26-ac34-6b673a23458a/scratchpad/clean-clone`.
The owner's working tree at `/home/tze/GitHub/syzygy` was never read.

**Clone identity.** `HEAD = d65fd42` ("ci: run the dependency-index drift guard
alongside the contract-index one"), branch `main`, working tree clean, **191
tracked files**, `_bootstrap/` absent (verified by `find` and by directory
test). Tags: `doctrine-adopted-2026-07-30` (only).

**Simulated task.** A new collaborator asked to help the owner execute the
pending governance acceptance acts.

**Tooling note.** `grep` on this machine is ugrep; every load-bearing sweep in
this report was run with `grep -F` or with Python `re` over `git ls-files`, and
every "zero" claim was reproduced by two independent methods.

---

## 1. Reproducing the project stage from the clone alone

Reproducible in full, from the front door, without guessing. Every row below
was read from the clone; no fact required outside knowledge.

| Fact | Value read from the clone | Source |
|---|---|---|
| Lifecycle stage | **Final pre-specification** | `PROJECT-STATUS.md:12`; `README.md:7-12`; `AGENTS.md` "Current lifecycle stage" |
| Doctrine | **Adopted** 2026-07-30, amendment D1 in force | `PROJECT-STATUS.md:20`; tag `doctrine-adopted-2026-07-30` (confirmed present, only tag); `.syzygy/governance/doctrine/README.md` |
| Craft-and-care | **Owner-approved (D2)**; clause force begins at foundational-contract acceptance | `PROJECT-STATUS.md:21`; `.syzygy/governance/policies/craft-and-care/INSTALL-RECORD.md:7-8,17-26` |
| Surface decisions | **Recorded** SDR-1…33 | `PROJECT-STATUS.md:22`; `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md` |
| Contracts RFC 0001–0011 (32 modules) | **Candidate — no act performed** | `PROJECT-STATUS.md:23`; `contracts/candidates/README.md:1-7` |
| Topology bundle (9 files) | **Candidate — no act performed** | `PROJECT-STATUS.md:25`; `.syzygy/map/topology-candidates/BUNDLE-MANIFEST.md` |
| Overview | **Draft, awaiting adoption (act 4)** | `PROJECT-STATUS.md:26`; `.syzygy/intent/OVERVIEW.md:1-11` |
| D3 bounded missions | **Proposed (act 5, optional)**, rev1 supersedes DRAFT | `PROJECT-STATUS.md:27`; `DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md:1-8` |
| Knowledge-hygiene policy, license | **Candidate / undecided** | `PROJECT-STATUS.md:28-29`; `PENDING-OWNER-DECISIONS.md:58,59` |
| OpenSpec, implementation | **Do not exist** | verified absent: `openspec/`, `src/`, `apps/`, `packages/` all absent |
| Accepted homes | **Do not exist — correct** | verified absent: `.syzygy/governance/contracts/rfcs/`, `.syzygy/map/topology/`, `.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md`. Corroborated by check CG-6 |

`[Observed]` Absence checks were run explicitly, not inferred:

```
absent (correct): .syzygy/governance/contracts/rfcs
absent (correct): .syzygy/map/topology
absent (correct): .syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md
absent (correct): openspec / src / apps / packages
```

**Could not determine from the clone:** nothing about the *stage*. Two content
questions are unanswerable from clone bytes and are treated as findings, not
gaps in my reading: the external `th-engineering` engineering baseline
(finding 1) and the founder decision log FD-n (disclosed at
`PENDING-OWNER-DECISIONS.md:60`, P-15).

---

## 2. Running every advertised validation

Advertised in `PROJECT-STATUS.md:81-87`, `AGENTS.md` "Validation",
`CONTRIBUTING.md:59-66`, and `.github/workflows/governance-docs.yml:31-43`.
Every command exists, runs, and examines a non-empty set. **No command
referenced a path missing from the clone. No command failed.**

### 2.1 `python3 .syzygy/governance/contracts/candidates/scripts/verify_final_prespec.py`
**Exit 0.** Substantive output — this is *not* a PASS over zero items:

```
active corpus (RFC files): 99094 words across 32 modules
numbered clauses defined: 322
note: rfcs/RFC-0001-...md: 8353 words over the 7,000 ceiling — JUSTIFIED: ...
note: total 99094 exceeds the 35–50k target band plus new RFCs; owner-facing
      justification required (charter)
PASS — all checks clean
```

32 modules and 322 clauses examined. The two `note:` lines are disclosed
overruns, printed rather than suppressed — correct behavior.

### 2.2 `build_contract_index.py --check` — **exit 0**, `index matches regeneration — no drift`
### 2.3 `build_dependency_index.py --check` — **exit 0**, `dependency index matches regeneration — no drift`

### 2.4 `python3 scripts/check_governance.py`
**Exit 0.** `scope: clone — 191 file(s) examined (191 tracked, 0 untracked-not-ignored)`.
Final line: **`15 OK, 7 WARN, 0 FAIL (22 checks) — counts derived, not asserted`.**

This exactly matches the claim at `PROJECT-STATUS.md:89-93`. Per-check
examined-counts (recorded because a PASS over zero items verifies nothing):

| Check | Examined | Result |
|---|---|---|
| CG-1a markdown links | 51 links | OK, 0 findings |
| CG-1b code-span paths | 714 references | OK, 0 findings |
| CG-1c forward references | 8 targets | WARN (by design) |
| CG-1d frozen-packet references | 26 references | WARN (by design) |
| CG-2a retired phrase confined | 180 files | OK |
| CG-2b retired-phrase allowlist | 21 files | WARN (declared) |
| CG-2c/2d `about/` | 2 / 3 files | OK / WARN |
| CG-3 stale bootstrap routing | 175 files | OK |
| CG-4 candidate banners | 6 files | OK |
| CG-5 craft banners truthful | 10 files | OK |
| CG-6 accepted homes not created | 2 homes | OK |
| **CG-7a manifest digests** | **32 entries** | **OK** |
| **CG-7b act-1 argument** | 1 argument | **OK** |
| **CG-7c acts 2/3/4 arguments** | 3 arguments | **OK** |
| **CG-7d act digests quoted anywhere** | 10 quotations | **OK** |
| CG-8 context budgets | 34 artifacts, 7 findings | WARN (report-only) |
| CG-9 duplicate authority homes | 16 files | OK |
| CG-10 register as-of | 1 register | WARN (human judgement) |
| CG-11 cache/local ignored | 2 patterns | OK |
| CG-12 `_bootstrap/` not required | 38 citations | OK |
| CG-12b `_bootstrap/` allowlist | 50 files | WARN (declared) |

No check reported a PASS over an empty set. The seven WARNs each print a
rationale; all are declared-by-design.

### 2.5 `git tag --list 'doctrine-*'` — **exit 0**, `doctrine-adopted-2026-07-30`
### 2.6 `context_load.py` (AGENTS.md example) — **exit 0**, resolves `doctrine:`/`craft:` prefixes to canonical homes; `5256 TOTAL words / 7095 estimated tokens`.

### 2.7 CI parity
`.github/workflows/governance-docs.yml` runs exactly the four checkers above
(lines 31-43). All four pass locally in the clone. **CI is reproducible from
the clone with only a Python 3.11 interpreter** — no missing tooling, no
stack choice smuggled in.

**Section verdict: all advertised validation reproduces from clone bytes.**

---

## 3. Acceptance ceremony — dry run (no act performed)

I performed **no owner act**, edited **no governance artifact**, and created
**no accepted home**. All work below is read-only recomputation.

**Records found.** Defining:
`contracts/candidates/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`
(§1 phrases, §2 ceremony, §7 owner-attention). Presentation:
`contracts/candidates/round-2026-08/FINAL-OWNER-ACCEPTANCE-RECORD.md`, which
explicitly subordinates itself ("Where the two disagree, that record wins and
this one is stale", `:12-13`). Register: `decisions/PENDING-OWNER-DECISIONS.md`
P-1…P-5. The routing between the three is consistent and unambiguous.

### 3.1 Independent digest recomputation — all five reproduce

```
$ sha256sum .syzygy/governance/contracts/candidates/ACTIVE-CONTRACT-MANIFEST.txt
f2914fc56cd2aa069b952747b9c78b00dc41d908830887ecd2f1addd37e61fc4
$ sha256sum .syzygy/governance/policies/craft-and-care/testing-and-verification.md
3858820f64768ef20e6514fe8adb28076263f071ac77e66a5520a612f3bcb26d
$ sha256sum .syzygy/map/topology-candidates/BUNDLE-MANIFEST.md
7a3b22494a08d888901c1f0cec76833dc926e89b6f510b5abf8963071fbaeb45
$ sha256sum .syzygy/intent/OVERVIEW.md
ce7794fd8c0e528ae50434f5c63ce27df998441cdd07b20a903627ecaf885b06
$ sha256sum .syzygy/governance/contracts/candidates/DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md
0328cb379cab1ffa462cc5bf2205241b96dec21b0917d485b0906d4fe7dcd96c
```

Every value equals the offered act argument, character for character.

Member-level verification:

- `sha256sum -c ACTIVE-CONTRACT-MANIFEST.txt` → **32 lines, 32 `OK`, 0 non-OK**
  (counted programmatically; `rc=0`).
- Topology members recomputed against the manifest's fenced block in Python →
  **9 OK, 0 mismatched, 9 members**.
- Craft cluster: all nine files recomputed against `INSTALL-RECORD.md:61-69`
  (the 2026-08-05 correction block) → **9/9 identical**.
- D3 rev1 cites the superseded DRAFT's digest at `:6`
  (`30efb7c5fc933e18…`); recomputed → **matches**.

### 3.2 Per-act dry run

| | Act 1 | Act 2 | Act 3 | Act 4 | Act 5 (optional) |
|---|---|---|---|---|---|
| **Phrase** | `ACCEPT COMPACTED FOUNDATIONAL RFCS: f2914fc5…1fc4` | `CONFIRM CRAFT AMENDMENT: CC-TEST-2@3858820f…b26d` | `ACCEPT TOPOLOGY: 7a3b2249…eb45` | `ADOPT PROJECT OVERVIEW: ce7794fd…5b06` | VIS-4 adoption in the owner's own words; optional digest form `ADOPT DOCTRINE AMENDMENT: D3@0328cb37…d96c` |
| **Digest computed at** | `ACTIVE-CONTRACT-MANIFEST.txt` (own sha256) | `INSTALL-RECORD.md` 2026-08-05 block | `BUNDLE-MANIFEST.md` (own sha256) | acceptance record §1 row 4 over `OVERVIEW.md` | acceptance record (presentation) §1 act 5 |
| **Recomputed?** | ✅ exact | ✅ exact | ✅ exact | ✅ exact | ✅ exact |
| **Source path** | `contracts/candidates/rfcs/` (32 modules) + manifest | `policies/craft-and-care/testing-and-verification.md` | `.syzygy/map/topology-candidates/` | `.syzygy/intent/OVERVIEW.md` | `contracts/candidates/DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md` |
| **Destination** | `.syzygy/governance/contracts/rfcs/` + manifest one level up at `.syzygy/governance/contracts/`; companions to `…/history/`, `…/matrix-rows/` | none — binds content already at its canonical home | `.syzygy/map/topology/` | none — binds content in place | two verbatim doctrine insertions |
| **Transaction** | defining record §2 steps 1-5 | §2 steps 1,2,4,5 | §2 steps 1-5 | §2 steps 1,2,4,5 | VIS-4 |
| **Validation before** | `check_governance.py` CG-7a/b/d | CG-7c | CG-7c | CG-7c | CG-7d if phrase form used |
| **Validation after** | `sha256sum -c ACTIVE-CONTRACT-MANIFEST.txt` from `.syzygy/governance/contracts/` | re-run CG-7c | bundle `sha256sum -c` from installed dir | re-run CG-7c | — |
| **Defect found** | — | **finding 1** (baseline unreadable) | **findings 3** (source path does not exist) | — | **finding 4** (phrase form only in the subordinate record) |

The ceremony is otherwise complete and unambiguous: five steps, one act at a
time, no bundling, ordering recommendation (act 1 before act 5) stated with a
reason, and rework/reject alternatives given for act 1.

### 3.3 Every copy of every act digest, checked against source

Not trusting CG-7d, I re-ran the sweep independently in Python over
`git ls-files`, matching every act-phrase occurrence and, separately, every
64-hex string in the repository against a digest→file map of all tracked files.

**Act-phrase occurrences carrying a full digest: 10. All 10 match their current
subject.** They are `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:15,16,17,18`
and `round-2026-08/FINAL-OWNER-ACCEPTANCE-RECORD.md:35,65,83,99,122`. (The
tenth is act 5's, which only the presentation record carries — finding 4.)

**Two act-phrase occurrences carry a retired digest** (`08793ddf…`, the
superseded act-1 argument), both inside stored-verbatim raw reviewer output:

- `contracts/candidates/reviews/rev10-confirming-review.md:26`
- `round-2026-08/reviews/RB-4-contract-compaction-RAW.md:533`

Per the repository's own rule (raw reviewer output is never edited, only
allowlisted) these are correct and must stay. **No live act argument anywhere
is stale.**

**Broader sweep:** 52 further 64-hex digests match no tracked file. I inspected
all 52. Every one is either (a) inside `INSTALL-RECORD.md:31-39,48,52`, which
labels that block "historical — superseded by the 2026-08-05 correction block
below" and marks `aa2d6353…` "now-**retired**", or (b) inside stored-verbatim
raw reviewer output. **Zero undisclosed stale digests.**

This is the round's headline defect (four stale act arguments) genuinely fixed,
and CG-7d genuinely covers it. Confirmed by two independent methods.

---

## 4. Stale provenance claims

Swept with Python `re` over all 191 tracked files for: "lives in/resides
in/stored in `_bootstrap`", "founder-local", "delivered packet", "shipped in
packet", "not committed / not clone-visible", and `` `topology/` ``.

### FALSE of this clone

**4.1 `contracts/candidates/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:142-146`**

> "**Retention before the act, stated honestly.** Until an act fires, the
> package lives in the deliberately git-excluded `_bootstrap/` working tree
> plus the delivered review packet; step 2 makes tampering detectable, not
> recoverable from this repository alone."

**FALSE.** The package is tracked and clone-visible at
`contracts/candidates/` — as that directory's own README states at `:9-14`,
and as P-9 records "Executed" at `PENDING-OWNER-DECISIONS.md:49`. This is a
false statement inside the **defining** ceremony record, and it understates the
project's actual retention posture. Already found as **RB-8 F6**
(`round-2026-08/reviews/RB-8-public-clone-RAW.md:164`) — and I can find **no
disposition of RB-8 F6 anywhere**: `ROUND-DISPOSITIONS.md` cites RB-8 only at
lines 19, 36, 37, 38, 64, 73, and its residual bucket §4 L lists RB-1/2/3/4/5/7
findings but no RB-8 F6. The record is not digest-bound, so the fix is free.

**4.2 `contracts/candidates/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:92`**

> "act 3 installs the bundle (shipped in this packet at `topology/`) to
> `.syzygy/map/topology/`"

**FALSE.** Verified two ways: `ls contracts/candidates/topology` → "No such
file or directory"; `find . -type d -name 'topology*'` → only
`./.syzygy/map/topology-candidates`. A collaborator following act 3's
transaction literally cannot locate the source. The correct location is stated
only in a *different* file (`contracts/candidates/README.md:36-37`).

**4.3 `.syzygy/map/topology-candidates/BUNDLE-MANIFEST.md:25`**

> "Verify anytime with `sha256sum -c` against this block (from `topology/`)."

**FALSE** for the pre-act state ("anytime"). Found previously as **RB-1 F9**
(`RB-1-fresh-engineer-RAW.md:581,683`) and swept into `ROUND-DISPOSITIONS.md:95`
§4 L ("minor accounting residuals … left for the next round"). Note this file
**is** act 3's digest subject, so repairing it retires act 3's argument — the
disposition is defensible, but the statement is still false today.

**4.4 `round-2026-08/REFRACTOR-PREFLIGHT-REPORT.md:38-45,52-57`** — under a
heading reading "## 2. Current governance state":

> "**Contract corpus — candidate, founder-local.** … Lives only under
> `_bootstrap/rfc-phase/final-prespec/` — invisible to clones before this
> round." / "**Topology — candidate, founder-local.** … also `_bootstrap/`-only
> before this round." / "**A clone cannot see:** any RFC module, the manifest,
> the acceptance record, topology, the verification scripts …"

**FALSE now, TRUE at round start.** The file header (`:1-7`) discloses it is a
round process record and §1 is titled "Repository state at round start", and
two of the three passages carry the qualifier "before this round" — so this is
disclosed, not deceptive. But §2's title says "**Current**", and `:52-57` has
no such qualifier. A skimming collaborator could take `:52-57` as live.

### TRUE of this clone (checked, not findings)

- `.gitignore:13` "founder-local, never committed" — TRUE (`_bootstrap/` absent).
- `contracts/candidates/README.md:12` "promoted byte-verbatim from the
  founder-local rev10 packet" — a provenance statement about the past; TRUE.
- `round-2026-08/ARTIFACT-INVENTORY.md:29`, `HISTORICAL-ARCHIVE-INDEX.md:9`,
  `PUBLIC-CLONE-AUTHORITY-MATRIX.md:40`, `KNOWLEDGE-HEALTH-BRIEF.md:11`,
  `MISSION-CONTROL-REVIEW.md:33`, `INSTALL-RECORD.md:13`,
  `LICENSE-DECISION-PACKET.md:2`, `PENDING-OWNER-DECISIONS.md:13`,
  `SURFACE-DECISION-RECORD.md:8,229` — all correctly describe `_bootstrap/**`
  as unavailable history. TRUE.
- File counts "190 tracked": `FINAL-OWNER-ACCEPTANCE-RECORD.md:218`,
  `FINAL-PRE-SPECIFICATION-READINESS-REPORT.md:110`,
  `PUBLIC-CLONE-VERIFICATION-REPORT.md:19,51,98`. **Not a finding** — all are
  explicitly pinned to commit `f2d202c`, and `git ls-tree -r --name-only
  f2d202c | wc -l` = **190**. The clone at `d65fd42` has 191 because
  `PUBLIC-CLONE-VERIFICATION-REPORT.md` was itself added afterward. Correctly
  scoped derived values.

---

## 5. External baseline

**What it is.** The craft cluster **adopts by reference** the `th-engineering`
skill package — its `engineering-bar` subskill (biases 1–9 + Definition of
Done), `test-rigor` (rules 1–8), and `dependency-hygiene` (rules 1–7)
(`policies/craft-and-care/README.md:14-20`). It is precedence tier 3
(`:32`) and is declared the default for silence: "The cluster **does not
restate** the canonical bar… Where a file is silent, the canonical bar applies
unmodified" (`:22-24`).

**Can a clone-only holder obtain it? NO.**

| Locator | Present? | Where |
|---|---|---|
| Name | ✅ | `README.md:15,32,37` |
| Repository URL | ❌ | nowhere in the clone |
| Commit / tag / revision | ❌ | none |
| Path inside a repo | ❌ | only the machine path `~/.claude/skills/th-engineering/subskills/` (`README.md:18`) |
| Content digest / sha256 | ❌ | none — `INSTALL-RECORD.md` digests the nine **local** files twice over and never mentions `th-engineering` |
| Version | ❌ | none |
| Date | ⚠️ | `README.md:37` — "as read on 2026-07-30". This is the entire pin. |

`[Observed]` Verified two ways that no baseline content exists in the clone:
`find . -iname '*th-engineering*'` → **no results**; Python `re` over
`git ls-files` → **9 lines mention the string**, of which only
`README.md:15,18,32,37` and `engineering-bar.md:5` are the reference itself;
the rest are a review and an authority matrix. **Zero bytes of the baseline.**

**Exactly what is missing:** a retrievable location (no URL/repo/submodule/
vendored copy), an integrity anchor (no sha256/commit/version — so even a copy
found elsewhere could not be shown to be *the* text), and the text itself. The
"pin" at `README.md:36-43` is a bare read-date, and its own maintenance
mechanism ("if the installed bar changes materially against that pin … the
conflict is surfaced to the owner") is inoperable for anyone who cannot read
the installed bar.

**What depends on it.** Totally: **CC-BAR-1** (`engineering-bar.md:10-35`) and
**CC-BAR-2** (`:36-38`, "in addition to the canonical Definition of Done"), plus
every silent clause in all nine files via `README.md:22-24`. Partially:
**CC-TEST-1**, **CC-TEST-4** (`testing-and-verification.md:82,86`),
**CC-TEST-6** (`:128`), **CC-DEP-1** (`interfaces-and-dependencies.md:28`),
**CC-DEP-5** (`:115-116`), **CC-REV-1** (`review-and-documentation.md:40`),
**CC-REV-2** (`:58`). Five of the nine files carry a "Baseline:" preamble
defining the whole file as a delta.

**Disclosure state — disclosed, but not where a reader meets it.** Honestly
recorded at `PENDING-OWNER-DECISIONS.md:65` (P-20),
`ROUND-DISPOSITIONS.md:86` (§4 C), `PUBLIC-CLONE-VERIFICATION-REPORT.md:114-118`,
`FINAL-OWNER-ACCEPTANCE-RECORD.md:76-78` (under Act 2, "Knowingly imperfect"),
`FINAL-HUMAN-CLARITY-REVIEW.md:50-52`, and `RB-1-fresh-engineer-RAW.md:240-265`
(F5, "MATERIAL"). **But:** the craft cluster itself never says it — `README.md`,
`INSTALL-RECORD.md` and all nine policy files present the reference as a live
`[Observed]` citation. `CONTRIBUTING.md:59-66` scopes its clone-completeness
test to `_bootstrap/**` only, so the test structurally cannot catch this, even
though `PUBLIC-CLONE-AUTHORITY-MATRIX.md:35` directs "disclose in CONTRIBUTING
(do not import)".

An `[Observed]` label on a source no clone reader can observe is precisely the
epistemic-labeling defect VIS-2 exists to prevent — inside an owner-approved
artifact.

---

## 6. Hidden-dependency sweep — `_bootstrap/`

**219 mentions across 75 tracked files** (Python `re` over `git ls-files`;
cross-checked against CG-12's 38 citations + CG-12b's 50 allowlisted files,
which count citations rather than raw mentions — consistent).

| Class | Count | Notes |
|---|---:|---|
| **(c)** raw reviewer output quoting it | **51** | `reviews/**`, `DISPOSITIONS.md`. Stored verbatim, never edited — acceptable by the repository's own rule |
| **(b)** historical / provenance pointer, disclosed unavailable | **165** | `history/`, `matrix-rows/`, `fixtures/`, `round-2026-08/`, `decisions/`, `policies/`, `.gitignore`, `AGENTS.md`, `CONTRIBUTING.md`, `scripts/check_governance.py` (19 — checker logic), skills |
| **(a)** essential meaning depends on it — BLOCKING | **0 strictly** | see below |

**The three requiring individual judgement** are all in
`FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`:

- `:5` — supersedes the rev9 record at a `_bootstrap/` path. **Class (b)** —
  pure provenance; nothing about the current gates needs it.
- `:111` — ceremony **step 5** requires the commit SHA be "mirrored afterwards
  to `_bootstrap/state/FOUNDER_DECISION_LOG.md` (process mirror only —
  CT-027's rule)". A collaborator cannot perform this step. Disclosed inline as
  a process mirror, and steps 1-4 fully determine the act. **Class (b) with a
  caveat** — see finding 8.
- `:143` — the retention paragraph. Not a dependency but a **false claim**;
  reported as finding 2, not as class (a).

**Class (a) list: empty.** No tracked artifact requires reading `_bootstrap/**`
to recover its essential meaning. CG-12's result ("38 citations examined, 0
findings") reproduces under my independent method. This test genuinely passes.

---

## 7. Verdict on Test F

| Capability | Verdict | Evidence |
|---|---|---|
| Project stage | **YES** | `PROJECT-STATUS.md` gate table 1-12 reproduces every gate; all absence claims verified by direct test |
| Authority map | **YES** | `README.md:77-85`, `AGENTS.md` table, `round-2026-08/ACTIVE-AUTHORITY-MAP.md` agree; CG-9 (16 files) finds no duplicate authority home |
| Candidate manifest | **YES** | `sha256sum -c ACTIVE-CONTRACT-MANIFEST.txt` → 32/32 OK; manifest self-digest `f2914fc5…` = act-1 argument exactly |
| Dependency index | **YES** | `build_dependency_index.py --check` → "no drift"; `build_contract_index.py --check` → "no drift" |
| Context fixtures | **PARTIAL** | Fixture 1 reproduces byte-exact (13,864 words / 18,716 est. tokens, recomputed); but `CONTEXT-COMPILER-FIXTURE-REPORT.md:246-250` records fixtures 2/4/5 measuring 18,315 / 10,893 / 12,843 against stated 18,302 / 10,854 / 12,830 with three mismatched digests — disclosed, dispositioned, unfixed; charter fixture-class coverage incomplete (P-20) |
| Owner-gate interface | **PARTIAL** | All five act phrases present and all five digests recompute exactly; but act 3's install source `topology/` does not exist (finding 3) and act 5's digest-bound phrase form appears only in the subordinate presentation record (finding 4) |
| Validation results | **YES** | All four advertised checkers + `git tag` + `context_load.py` run clean from clone bytes; `15 OK, 7 WARN, 0 FAIL over 22 checks` matches `PROJECT-STATUS.md:89-93` exactly; CI needs only Python 3.11 |

**Overall.** This is a genuinely self-verifying clone. The round's headline
defect — stale act arguments — is fixed and now machine-guarded, and I could
not break it with two independent sweep methods. What remains is a small set of
stale prose statements and one material external dependency, all of which
mislead a collaborator without endangering an act.

---

## VERDICT: EXCEPTIONS

### 1. [Blocking] The owner-approved engineering bar is unobtainable from a clone, and the cluster itself does not say so
`policies/craft-and-care/README.md:14-20,22-24,32,36-43`; `engineering-bar.md:5`.
The `th-engineering` baseline has no URL, commit, path-in-repo, digest, or
version — only `~/.claude/skills/th-engineering/subskills/` and a read-date.
`README.md:22-24` makes it the default rule for every unaddressed question, so
its extent is unbounded from inside the clone. Act 2's subject
(`testing-and-verification.md`) is written as a delta against it. Disclosed at
P-20 / `ROUND-DISPOSITIONS.md:86` / `FINAL-OWNER-ACCEPTANCE-RECORD.md:76-78`,
but **not in the cluster**, and `CONTRIBUTING.md:59-66` scopes its clone test to
`_bootstrap/**` so no check can catch it.
**Minimal fix:** append one sentence to `craft-and-care/README.md:20` — "This
baseline is machine-local and unreadable from a clone; see register item
P-20" — and widen `CONTRIBUTING.md:64-66` beyond `_bootstrap/**` to "any
source outside the clone". Note this touches `README.md` only, **not** act 2's
digest subject, so act 2 is unaffected; regenerate `INSTALL-RECORD.md:61`'s
`README.md` line afterward. Vendoring or digest-pinning the baseline is an
owner act and should stay P-20.

### 2. [Blocking] Act 3's install source path does not exist
`FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:92` — "shipped in this packet
at `topology/`". Verified absent two ways. A collaborator executing act 3's
written transaction cannot find the source; the correct path is stated only in
`contracts/candidates/README.md:36-37`.
**Minimal fix:** change `topology/` to `.syzygy/map/topology-candidates/` at
`:92`. The acceptance record is not digest-bound — this costs nothing.

### 3. [Non-blocking] The defining record's retention paragraph is false
`FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:142-146` claims the package
"lives in the deliberately git-excluded `_bootstrap/` working tree", contradicted
by `contracts/candidates/README.md:9-14` and P-9's "Executed"
(`PENDING-OWNER-DECISIONS.md:49`). Raised as RB-8 F6
(`RB-8-public-clone-RAW.md:164`) and, as far as I can find, **never
dispositioned** — `ROUND-DISPOSITIONS.md` §4 L lists no RB-8 finding.
**Minimal fix:** rewrite to "the package is tracked at
`.syzygy/governance/contracts/candidates/`; step 2 makes tampering detectable
against the manifest", and add an RB-8 F6 row to `ROUND-DISPOSITIONS.md`.

### 4. [Non-blocking] Act 5's digest-bound phrase exists only in the subordinate record
`round-2026-08/FINAL-OWNER-ACCEPTANCE-RECORD.md:122` offers
`ADOPT DOCTRINE AMENDMENT: D3@0328cb37…`, while the defining record's §1 row 5
(`:19`) defines act 5 with **no digest and no phrase**. The presentation record
declares itself losing on disagreement (`:12-13`), so the phrase form is offered
by a document that cannot define it.
**Minimal fix:** add the optional phrase form to the defining record §1 row 5,
or state at `:122` that it is a presentation convenience with no defining force.

### 5. [Non-blocking] `BUNDLE-MANIFEST.md:25` names a nonexistent verification directory
"(from `topology/`)" — false today; the directory is `topology-candidates/`.
Already RB-1 F9, dispositioned into `ROUND-DISPOSITIONS.md:95` §4 L.
**Minimal fix:** none available without retiring act 3's argument (this file
*is* the digest subject). Correct action is to carry it into the next
re-offer; recommend adding it explicitly to `FINAL-OWNER-ACCEPTANCE-RECORD.md`'s
act-3 "Knowingly imperfect" line, which currently lists nothing.

### 6. [Non-blocking] The link checker cannot see the pointer classes that actually broke
`scripts/check_governance.py:172` — `CODE_PATH` requires a file extension, so
bare directory references (`` `topology/` ``) and `~`-rooted paths are never
counted. CG-1b reports "714 references examined, 0 findings" while two of my
three stale-path findings sit in exactly those blind spots. Automated link
health therefore overstates real pointer health.
**Minimal fix:** extend `CODE_PATH` to trailing-slash directory tokens, and add
a check that flags `~/`-rooted paths as unresolvable-by-construction.

### 7. [Non-blocking] Preflight §2 is titled "Current" but describes round start
`round-2026-08/REFRACTOR-PREFLIGHT-REPORT.md:38-45,52-57` — "founder-local",
"Lives only under `_bootstrap/…`", "A clone cannot see: any RFC module …". The
header at `:1-7` discloses the file's nature and two passages say "before this
round", but `:52-57` carries no qualifier under a heading reading "Current
governance state".
**Minimal fix:** retitle §2 to "Governance state at round start" and add
"(superseded by P-9's execution)" at `:52`.

### 8. [Non-blocking] Ceremony step 5 requires a write no collaborator can make
`FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:105-112` — step 5 mirrors the
commit SHA to `_bootstrap/state/FOUNDER_DECISION_LOG.md`. Disclosed as "process
mirror only", and steps 1-4 fully constitute the act, so this is not a hidden
dependency — but a collaborator executing the ceremony hits a step they cannot
complete and has to infer it is optional.
**Minimal fix:** mark step 5's mirror clause "owner-only; not part of the act's
validity" inline.

### 9. [Non-blocking] "The clone is self-contained" overstates its own report
`round-2026-08/PUBLIC-CLONE-VERIFICATION-REPORT.md:11-13` bolds "**Result: the
clone is self-contained.**"; its own §5 at `:114-118` is titled "What a clone
still cannot do" and lists the engineering bar. The following sentence scopes
the claim to act arguments and checks, but the bolded headline is what a
skimmer takes away.
**Minimal fix:** change to "**Result: the clone reproduces every act argument
and every advertised check** — with the exceptions in §5."

---

**Positive findings worth recording.** All five act digests recompute exactly
from clone bytes; 32/32 module digests, 9/9 topology members, and 9/9 craft
files verify; every live act-digest copy in the repository agrees with its
source under an independent sweep, with the only two retired-digest occurrences
correctly confined to never-edited reviewer output; class (a) `_bootstrap`
dependencies are genuinely zero under two methods; and all four CI checkers pass
from the clone with only a Python interpreter. The digest-staleness discipline
this project built after its last round demonstrably works.
