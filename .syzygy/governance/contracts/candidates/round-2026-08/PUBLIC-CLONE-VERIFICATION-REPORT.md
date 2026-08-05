> # Historical — round record, not a current offering
>
> **Do not read a digest here as an act argument.** Its act arguments are round 2026-08's and three of the five have changed since. Successor: `../round-2026-08b/PUBLIC-CLONE-VERIFICATION-REPORT.md`. Current arguments
> come from `ACTIVE-CONTRACT-MANIFEST.txt` and
> `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`, never from a round record.

# Public-clone verification report — 2026-08-05

> Non-authoritative round record. It reports what a clone contains and what
> reproduces from it; it decides nothing.

**Method.** A real `git clone` of `git@github.com:Tzeusy/syzygy.git` at commit
`f2d202c`, into a directory that never held the authoring session. Every
figure below was measured **inside that clone**, not in the working tree.
Claims are `[Observed]` unless labeled otherwise.

**Result: the clone is self-contained.** All five act arguments, both index
guards, the packet verifier, the manifests, and the full governance check
reproduce from clone bytes alone, with `_bootstrap/` absent.

---

## 1. What the clone contains

`[Observed]` **190 tracked files. `_bootstrap/` is absent** — confirmed by
directory test, and the tree is git-ignored at the repository level
(commit `9e6f2f7`), not merely by a machine-local exclude.

| Layer | Present | Status in the clone |
|---|---|---|
| Doctrine (VIS-1…7, SEC-1…5) | ✅ | Adopted — binding |
| Owner decisions (SDR-1…33, extracted warrants, pending queue) | ✅ | Binding |
| Craft-and-care (CC-*) | ✅ | Owner-approved (D2); one gated amendment |
| Candidate contracts (RFC 0001–0011, 32 modules) | ✅ | Candidate — binds nothing |
| Candidate topology bundle (9 files) | ✅ | Candidate — binds nothing |
| Overview | ✅ | Governed presentation, never authority |
| Round records + 8 raw reviews | ✅ | Non-authoritative process records |
| Validation scripts + docs-only CI | ✅ | Runnable |
| Founder decision log, raw interviews, bootstrap history | ❌ | Founder-local by owner ruling FD-021/FD-037 |

---

## 2. Everything that reproduces from clone bytes

| Check | Command | Result |
|---|---|---|
| Act 1 argument | `sha256sum …/ACTIVE-CONTRACT-MANIFEST.txt` | `f2914fc5…` ✅ matches the offering |
| Act 2 argument | `sha256sum …/craft-and-care/testing-and-verification.md` | `3858820f…` ✅ |
| Act 3 argument | `sha256sum …/topology-candidates/BUNDLE-MANIFEST.md` | `7a3b2249…` ✅ |
| Act 4 argument | `sha256sum .syzygy/intent/OVERVIEW.md` | `ce7794fd…` ✅ |
| Act 5 argument (optional phrase form) | `sha256sum …/DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md` | `0328cb37…` ✅ |
| Contract module digests | `sha256sum -c ACTIVE-CONTRACT-MANIFEST.txt` | **32/32 OK** |
| Topology member digests | `sha256sum -c` against the manifest's fenced block | **9/9 OK** |
| Packet verifier | `scripts/verify_final_prespec.py` | **PASS — all checks clean** |
| Contract index drift | `build_contract_index.py --check` | no drift |
| Dependency index drift | `build_dependency_index.py --check` | no drift |
| Repository governance | `scripts/check_governance.py` | **15 OK, 7 WARN, 0 FAIL** over 22 checks; scope line reads *190 file(s) examined (190 tracked, 0 untracked-not-ignored)* |
| Context compiler smoke | `context_load.py rfcs/RFC-0002/README.md doctrine:vision.md craft:engineering-bar.md` | 5,256 words / 7,095 est. tokens, resolved through the `doctrine:` and `craft:` prefixes to canonical homes |

`[Observed]` The clone's numbers are **identical** to the working tree's on
every check. There is no working-tree-only fact in the offering.

---

## 3. No hidden semantic dependency on `_bootstrap/` — charter Test E

`[Observed]` Sweep by Python `re` (never shell `grep`, per the recorded ugrep
hazard): **74 files, 209 occurrences** of `_bootstrap/` in the clone.
`check_governance.py` CG-12 classifies them: **38 citations examined, 0
findings** — no `_bootstrap/` path is cited as a *required* source anywhere.
CG-12b prints the 50 allowlisted files with the reason each is exempt.

The occurrences fall into four buckets, none of them a dependency:

1. **Frozen provenance** — the clause-migration matrix and `history/**` cite
   the rev9 corpus they migrated *from*, by construction.
2. **Raw reviewer output**, stored verbatim and never edited — much of it
   reviewers recording that they deliberately did *not* read the tree.
3. **Round process records**, each carrying a file-level disclosure that the
   pointers are git-excluded.
4. **Rule text about the exclusion** (`AGENTS.md`, `CONTRIBUTING.md`, the
   checker itself) — describing a boundary is not crossing it.

`[Inferred]` The strongest evidence is not the sweep: it is that RB-1, RB-5
and RB-8 each reviewed from clone-equivalent material and produced specific,
substantive findings — several the authoring session had missed. A corpus that
cannot be understood without hidden history does not yield that.

---

## 4. Executable content a clone receives

Disclosed here and in `SECURITY.md`, which is the owning record.

| File | What it does | Runs on clone? |
|---|---|---|
| `scripts/check_governance.py` | Read-only governance checks | Only when invoked |
| `…/candidates/scripts/verify_final_prespec.py`, `context_load.py` | Read-only | Only when invoked |
| `…/candidates/scripts/build_contract_index.py`, `build_dependency_index.py` | **Write** their index files (`--check` compares without writing) | Only when invoked |
| `.github/workflows/governance-docs.yml` | Docs-only CI: runs the checks above | On push/PR, in GitHub's runner |
| `.claude/settings.json` | Runs `bd prime` at session start | Only inside Claude Code |
| `.beads/hooks/*` (5 hooks) | Beads git hooks | **No.** `[Observed]` A fresh clone's `.git/hooks/` contains only `*.sample`; the hooks are files in the worktree until a tool installs them |

`[Observed]` **Secret scan:** 190 tracked files scanned for AWS keys, private
key blocks, GitHub/Slack/OpenAI-style tokens — **0 findings**. This is a
pattern scan, not a proof; it is `[Observed]` for those patterns and
`[Unknown]` for anything they do not match.

`[Observed]` `.beads/interactions.jsonl` and `issues.jsonl` are tracked
(1.8 KB total) and contain issue metadata and the round's closure reason —
no credentials, no machine paths.

---

## 5. What a clone still cannot do

Stated plainly, because a verification report that only lists successes is not
a verification report.

- **The craft cluster's engineering bar is adopted by reference to a
  machine-local skill tree.** `[Observed]` A gate-2-approved authority is
  therefore unreadable from a clone. Repairing it means either importing
  external text into the craft cluster or amending an owner-approved policy —
  both owner acts. Register item P-20.
- **Adopted doctrine cites a "README glossary" ambiguously.** **Correction 2026-08-05b:** the glossary **exists**, at `.syzygy/governance/doctrine/README.md:15` (`## Glossary (read first)`). The real defect is narrower: adopted doctrine says "README glossary" without saying *which* README, and the root `README.md` — the one a reader is holding — has none. See P-20 as amended.
  `[Observed]` The citation sites are inside adopted doctrine, so the repair
  is a doctrine amendment. P-20.
- **Founder decision log (FD-n) is founder-local** while FD identifiers are
  cited from tracked files. Two warrants were extracted this round; whether a
  compact FD register follows is open as P-15.
- **No `LICENSE` file exists.** `[Observed]` The repository is
  all-rights-reserved by default; a clone may read it and may not assume reuse
  rights. P-14 is the open decision, and it is not to be made autonomously.
