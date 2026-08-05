# RB-8 — Public clone and validation review (RAW, fresh-context)

**Reviewer:** fresh-context subagent, review vertical 8 (public clone and
validation), 2026-08-05. This is the raw report, stored verbatim.

## 0. Provenance — clean-tree simulation setup

Setup command executed exactly as charged:

```sh
mkdir -p <scratchpad>/clone-sim && cd /home/tze/GitHub/syzygy && \
git ls-files --cached --others --exclude-standard | \
grep -v '^syzygy_fable_human_clarity_refactor_round_prompt.md$' | \
rsync -a --files-from=- . <scratchpad>/clone-sim/
```

- **Result:** 176 files copied. (`find clone-sim -type f | wc -l` → `176`.)
- **Git metadata:** `scripts/check_governance.py` requires a git repository
  (raw rsync tree yields `WARN corpus — git unavailable or not a
  repository; nothing examined (Unknown, not clean)`, exit 1). Since a real
  fresh clone has git metadata, the simulation was completed with `git init
  && git add -A && git commit` inside clone-sim (`git ls-files | wc -l` →
  `176`, identical file set). All subsequent commands ran inside clone-sim
  only.
- **Clone-reproducible-via-git checks** were run in the real repo
  READ-ONLY and are labeled as such (§4, tag check).

## 1. Charge item 1 — self-containment scorecard (charter §18)

Ten questions, answered from clone-sim alone. Score: **8.5/10**.

| # | Question | Answer from the clone | Evidence (file:line) | Pt |
|---|---|---|---|---|
| 1 | What is Syzygy? | A specification-driven control plane: humans define what should be true, evidence shows what is true, agent fleets do bounded work to close the difference | `README.md:3-5`; deeper: `.syzygy/intent/OVERVIEW.md` Layer 1 | 1 |
| 2 | What stage is it in? | Final pre-specification; no application code, no openspec, no backlog | `README.md:7-12`; `PROJECT-STATUS.md:12-14` | 1 |
| 3 | Which doctrine is adopted? | VIS-1…7 / SEC-1…5, adopted 2026-07-30, amendment D1 in force | `PROJECT-STATUS.md:20`; `.syzygy/governance/doctrine/README.md:3` (status line) and `:9` (D1 log row); `README.md:73` | 1 |
| 4 | Which contracts are candidates or accepted? | RFC 0001–0011 (32 modules) are **candidates**; nothing is accepted; the accepted home `contracts/rfcs/` deliberately does not exist | `README.md:76`; `.syzygy/governance/contracts/candidates/README.md:1-7`; `PROJECT-STATUS.md:23` | 1 |
| 5 | Which topology is candidate or accepted? | The 9-file bundle at `.syzygy/map/topology-candidates/` is **candidate**, act 3 pending; accepted home `.syzygy/map/topology/` created only by the act | `README.md:77`; `PROJECT-STATUS.md:25`; `.syzygy/map/topology-candidates/TRACKING-NOTE.md:1-8` | 1 |
| 6 | Which policies are binding or pending? | Doctrine binding (adopted); craft-and-care owner-approved (D2), clause-level force begins at the foundational acceptance act; CC-TEST-2 confirmation (act 2) pending at `3858820f…`; knowledge-hygiene / term-registry / change-workflow are candidates needing their own acts | `README.md:75`; `AGENTS.md:19-27` (authority table); `.syzygy/governance/policies/craft-and-care/INSTALL-RECORD.md:57-75` (correction block); `PROJECT-STATUS.md:24,28` | 1 |
| 7 | Which overview is draft or adopted? | `.syzygy/intent/OVERVIEW.md` is a reviewed presentation **draft**, act 4 pending | `README.md:86-87` ("draft; adoption pending"); `PROJECT-STATUS.md:26`; `OVERVIEW.md:1-4` (self-declaring header) | 1 |
| 8 | Which owner decisions remain? | Acts 1–5 (P-1..P-5), license (P-10 gate row / P-13), knowledge-hygiene act, plus the P-6..P-16 queue | `PROJECT-STATUS.md:16-38` (gate table, all ⏳ rows); `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md:18-40` — **but** the register is stale as-of 2026-08-04: P-1/P-5 owning-record pointers go to unavailable `_bootstrap/` paths although the tracked record now exists, and P-6/P-7/P-8 are listed open though executed this round (SD-1..SD-4). Answerable only by cross-reading the round records | 0.5 |
| 9 | How do I validate all of this? | `PROJECT-STATUS.md:62-69` ("How to verify this page") + `CONTRIBUTING.md:59-66` ("Public-clone validation is part of done") name the exact commands — **but running them does not produce the promised clean result**: `check_governance.py` exits 1 (CG-7b FAIL) while `PROJECT-STATUS.md:52` claims "Known blocking defects: None known at this revision" | 0.5 |
| 10 | What should I read to amend a craft policy? | `CONTRIBUTING.md:38-57` (owning artifact, semantic delta, stable IDs, fresh review) → `policy-candidates/SEMANTIC-DELTA-TEMPLATE.md` + `policy-candidates/NORMATIVE-CHANGE-WORKFLOW.md` (process; honestly labeled candidate) → `.syzygy/governance/policies/craft-and-care/README.md:1` (canonical home + precedence) → `INSTALL-RECORD.md:42-75` (amendment record, act mechanics, current digests). Discoverable in ≤3 hops from the README's Start-here list | 1 |

## 2. Charge item 2 — `_bootstrap/` dependency sweep (charter §21 Test E)

Independent sweep by Python `re` (not grep — known ugrep hazard):
**61 files, 166 occurrences** of `_bootstrap/` in clone-sim.

Classification:

- **(a) Properly marked historical/unavailable — 60 of 61 files.** Buckets:
  - Frozen packet history and provenance: `04-CLAUSE-MIGRATION-MATRIX.md`
    (20), `matrix-rows/*` (20 across 9 files), `history/**` (39 across 16
    files), rev10 `reviews/*` raw reports (12 across 6 files), rev10 packet
    reports `00`/`01`/`09`/`10` (6). All cite frozen rev9 sources by
    construction; `candidates/README.md` and `history/README.md` label the
    lane historical/non-binding.
  - Round process records (`round-2026-08/*`, 20 across 9 files) — each
    carries a file-level disclosure that the pointers are git-excluded.
  - Rule text *about* the exclusion (not a dependency): `AGENTS.md:66-68,117`,
    `CONTRIBUTING.md:64`, `.claude/.codex` `SKILL.md:39`, `.gitignore:14`,
    fixtures 6/7/8 ("historical lane, never a default reading"),
    `scripts/check_governance.py` (the checker's own CG-12 logic, 14 hits).
  - Extraction provenance headers: `DOCTRINE-AMENDMENT-D1-MAP-HISTORICAL.md:1`,
    `OWNER-ANSWERS-2026-08-01.md:1`, `LICENSE-DECISION-PACKET.md:2`
    ("founder-local history"), `CRAFT-KNOWLEDGE-HYGIENE-POLICY.md:357`,
    `INSTALL-RECORD.md:4,13` ("founder-local, unavailable in clones"),
    `SURFACE-DECISION-RECORD.md:8,229` ("Do not load that corpus").
- **(b) Required for essential meaning — 0 files.** The acceptance record,
  manifest, 32 modules, topology bundle + manifest, craft digests, scripts,
  fixtures, and decision queue are all resolvable in-tree. Cross-checked
  against the clone's own `check_governance.py`: `CG-12 … 28 citations
  examined, 0 findings`.
- **Near-miss, filed as F4 (staleness, not hidden dependency):**
  `PENDING-OWNER-DECISIONS.md:22-28` still names
  `_bootstrap/rfc-phase/final-prespec/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`
  as P-1/P-5's owning record even though that record is now tracked at
  `.syzygy/governance/contracts/candidates/`. The file discloses the
  `_bootstrap` unavailability generically (:12-15), so meaning survives,
  but the pointer sends the reader away from the tracked copy.

**No blocking Test-E finding.**

## 3. Charge item 3 — validation from the clone, verbatim results

All commands run inside clone-sim (git-initialized, §0). Verbatim final
lines:

| Command | Verbatim final line | Exit | Matches documents' claim? |
|---|---|---|---|
| `python3 scripts/check_governance.py` | `12 OK, 7 WARN, 1 FAIL (20 checks) — counts derived, not asserted` | 1 | **NO** — `PROJECT-STATUS.md:52` claims no known blocking defects; the FAIL is CG-7b (see F1) |
| `python3 .syzygy/governance/contracts/candidates/scripts/verify_final_prespec.py` | `PASS — all checks clean` | 0 | Yes (note: reports **99,080 words** / 322 clauses; acceptance record §3 and `LEAD-SWEEP-NOTES.md:161` still say 99,067 — part of F1's staleness cluster) |
| `python3 …/scripts/build_contract_index.py --check` | `index matches regeneration — no drift` | 0 | Yes |
| `python3 …/scripts/build_dependency_index.py --check` | `dependency index matches regeneration — no drift` | 0 | Yes |
| `sha256sum -c ACTIVE-CONTRACT-MANIFEST.txt` (from `candidates/`) | `rfcs/RFC-0011-context-compiler.md: OK` — **32/32 lines OK, 0 failed** | 0 | Yes |
| Topology `sha256sum -c` against `BUNDLE-MANIFEST.md:14-22` digest block (from `topology-candidates/`) | `README.md: OK` — **9/9 members OK, 0 failed** | 0 | Yes |
| (supplementary) craft `INSTALL-RECORD.md` **current** 2026-08-05 digest block, `sha256sum -c` | 9/9 OK | 0 | Yes. (The *historical* install-time block in the same file fails by design — it is explicitly superseded and labeled historical; not a finding) |

- **Absolute founder paths:** Python sweep for `/home/` and `/Users/` —
  hits only inside raw review evidence and a finding *about* such paths
  (`01-REV9-ADVERSARIAL-FINDINGS.md:64`,
  `reviews/rev10-confirming-review.md:12,51`,
  `reviews/rev10-portability-review.md:40`). Zero in any script, manifest,
  index, or active artifact. No finding.
- **Missing files / import errors:** none. All four scripts import stdlib
  only (`re`, `sys`, `os`, `hashlib`, `subprocess`, `argparse`,
  `pathlib`) and derive their roots from their own location.
- **CG-1c/CG-1d WARNs** are by-design declared-forward/frozen-packet
  references, printed with rationale by the checker; verified sane.

## 4. Charge item 4 — digest chain (charter §21 Test D), independently recomputed

| Artifact | Recomputed sha256 (this review, from clone-sim bytes) | What the documents offer | Status |
|---|---|---|---|
| `ACTIVE-CONTRACT-MANIFEST.txt` (act-1 argument) | `5c4d6798354135bd860b3a2637c282f535c519bdd1a3cbab67d7555367af6caa` | Acceptance record §1/§3 offers `08793ddf70f3c2a30b5dcec51cac9266a81d03e9db48aa8b7071953f7687c936` — **MISMATCH**. Round records carry the new value (`round-2026-08/ARTIFACT-INVENTORY.md:14` `5c4d6798…`; `SEMANTIC-DELTAS-THIS-ROUND.md` SD-1 records the regeneration and schedules a new digest-binding review) but the offering document does not | **F1 (blocking)** |
| `.syzygy/map/topology-candidates/BUNDLE-MANIFEST.md` (act-3 argument) | `89279260e4b2a74c0c32503e082802bee5811b54b42d329d265cd7df3e671ef9` | Acceptance record §1 row 3 offers `0d34d1b5…` and claims "Unchanged from rev9 — the rev10 pass altered no topology file" — **MISMATCH** (SD-2 changed README.md; `BUNDLE-MANIFEST.md:9` and `TRACKING-NOTE.md` disclose the regeneration; `ARTIFACT-INVENTORY.md:23` carries `89279260…`) | **F1** |
| `.syzygy/governance/policies/craft-and-care/testing-and-verification.md` (act-2 CC-TEST-2) | `3858820f64768ef20e6514fe8adb28076263f071ac77e66a5520a612f3bcb26d` | `INSTALL-RECORD.md:68,72` correction block offers exactly this value and names the old `aa2d6353…` "stale and satisfies nothing" — **MATCH** at the current offering home. Acceptance record §1 row 2 still carries `aa2d6353…` | MATCH (record row stale → F1) |
| `.syzygy/intent/OVERVIEW.md` (act-4 candidate digest) | `49a1a09c2f45ac6df9be19f48f1c136e37f52e4f627cbdcd097e91a3452e61fa` | Acceptance record §1 row 4 offers `42de2eb1…` ("Unchanged from rev9", committed `fcb05c0`) — no longer true; **no tracked document anywhere carries the current `49a1a09c…` value**. Reported here per charge | **F1**; also F6-adjacent |

Clone-reproducible-via-git (run in the real repo, READ-ONLY, labeled):
`git tag --list 'doctrine-*'` → `doctrine-adopted-2026-07-30` — the tag
`PROJECT-STATUS.md:68` tells a cloner to check exists.

## 5. Charge item 5 — CI (`.github/workflows/governance-docs.yml`)

- Three steps: `check_governance.py`, `verify_final_prespec.py`,
  `build_contract_index.py --check`, on checkout@v4 + setup-python@v5
  (3.11). All referenced files exist in clone-sim; scripts are
  stdlib-only, self-rooted, no network, no absolute paths. Permissions
  `contents: read`. Structurally sound.
- **Would it pass on a fresh checkout of clone-sim's content? NO.** Step 1
  (`check_governance`) exits 1 on CG-7b (stale act-1 argument). The first
  push of this round's content turns main red. Same root cause as F1;
  filed as F2 so the CI consequence is explicit.

## 6. Charge item 6 — Beads posture

- Tracked hooks under `.beads/hooks/` are disclosed exactly where a cloner
  looks: `SECURITY.md:7-9` — "tracked git hooks under `.beads/hooks/` …
  **not installed by cloning — `git clone` never activates hooks**". This
  is the correct statement of git behavior.
- Scope for cloners: `CONTRIBUTING.md:68-73` ("Where Beads applies" —
  process housekeeping only, no product backlog); `AGENTS.md:196` restates
  the phase scope; `.beads/README.md` explains the tool.
- **Nothing requires `bd` for basic comprehension**: all ten scorecard
  questions were answered without it; `.beads/issues.jsonl` is a passive
  1-line export.
- Minor residual (F7): `.claude/settings.json` runs `bd prime` on
  SessionStart/PreCompact for anyone opening the clone in Claude Code;
  bd-not-installed makes the hook fail (non-fatally). Disclosed nowhere —
  SECURITY.md's executable-content inventory covers `.beads/hooks/` and
  the Python scripts but not this settings hook.

## 7. Findings

| # | Severity | Finding |
|---|---|---|
| **F1** | **Blocking** | The acceptance authority (`candidates/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`) offers stale digest arguments for **all four** phrase-bearing acts: act 1 `08793ddf…` vs actual `5c4d6798…`; act 2 `aa2d6353…` vs actual `3858820f…`; act 3 `0d34d1b5…` vs actual `89279260…`; act 4 `42de2eb1…` vs actual `49a1a09c…`. §1 rows 2–4 assert "Unchanged from rev9" — now false in all three; §3 asserts "The phrase in §1 always carries the current manifest digest" — false; §3/`LEAD-SWEEP-NOTES.md:161` word accounting (99,067) no longer matches the verifier (99,080). The regeneration **is** recorded in the round records (SD-1/SD-2, `ARTIFACT-INVENTORY.md`, `PUBLIC-CLONE-AUTHORITY-MATRIX.md` "supersede with round record") — but the offering document itself carries no pending-regeneration note, which is the charge's explicit condition for non-blocking. An owner following §1 as written would utter a void phrase (§2 step 2 would abort it); the clone's own checker FAILs (CG-7b). Fix: re-offer §1 with current digests (or stamp the record itself "digests pending re-offer this round") before the round commits. |
| **F2** | **Blocking** (same root cause as F1) | CI `governance-docs.yml` fails on a fresh checkout of this content: step `check_governance` exits 1 on CG-7b. Committing the round as-is puts main permanently red until F1 is fixed. |
| **F3** | Material | `PROJECT-STATUS.md:52` — "Known blocking defects: None known at this revision" (as-of 2026-08-05) is false at this revision: the file's own §"How to verify this page" command exits 1. Violates the file's stated contract that it is corrected in the same change. |
| **F4** | Material | `PENDING-OWNER-DECISIONS.md` (as-of 2026-08-04) is stale in ways the round has already superseded: P-1/P-5 owning-record pointers go to git-excluded `_bootstrap/` paths although the acceptance record, manifest, and D3 draft are now tracked under `candidates/`; P-6/P-7/P-8 are listed as open defects though executed this round (SD-1..SD-4). Regeneration is scheduled (`REFRACTOR-PREFLIGHT-REPORT.md:122-123`) but has not happened in the tree that would commit. |
| **F5** | Minor | `.syzygy/map/topology-candidates/README.md:3` banner still says "grounded in **proposed** foundational contracts" while SD-2's own rationale corrected line 45's "proposed"→"candidate" for lifecycle vocabulary — a residual inside the act-3 digest set (fixing it churns the bundle digest again; bundle it with the F1 re-offer or accept knowingly). |
| **F6** | Minor | Acceptance record §2 retention paragraph (lines 110-114) — "Until an act fires, the package lives in the deliberately git-excluded `_bootstrap/` working tree plus the delivered review packet" — is no longer true: the package is tracked (`candidates/README.md:9-14`). Honest-retention framing should be updated with the F1 re-offer. |
| **F7** | Minor | `.claude/settings.json` `bd prime` hooks assume bd is installed on any cloner's machine running Claude Code; failure is non-fatal but undisclosed (SECURITY.md's executable inventory omits it). |

Properly-historical stale digests in `00-README.md:39-40` and the rev10
reviews were checked and are **not** findings — they live in labeled packet
history / verbatim evidence lanes.

## 8. Verdict

The clone is remarkably self-contained: 8.5/10 orientation from cold, zero
hidden `_bootstrap` dependencies, portable stdlib-only validation, honest
Beads posture, and a checker that catches the round's own outstanding
defect. That defect is real and blocking-by-charge-rule: the single
acceptance authority offers four digests reality no longer matches, and CI
goes red on it. It is one repair (re-offer §1 + the F3/F4 same-change
refreshes), already anticipated by the round's own records.

EXCEPTIONS
