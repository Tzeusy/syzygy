# Preflight — contract-closure and context-routing round (2026-08-05b)

> **Non-authoritative process record.** This file records the repository's
> state at the start of one round of work, so the round's judgments can be
> audited rather than trusted. It binds nothing and adopts nothing. Where it
> disagrees with an owning record, the record wins and this file is stale.

**Round:** final human-clarity, contract-closure, context-routing and
mission-safety refactor. Second round of 2026-08-05; the first
(`../round-2026-08/`) was the human-clarity front-door round.

## 1. Git state at round start

| Fact | Value |
|---|---|
| Branch | `main` |
| HEAD | `d65fd42add1cbc3729504a574e13a90efca73ac5` |
| HEAD subject | `ci: run the dependency-index drift guard alongside the contract-index one` |
| Working tree | clean (`git status --porcelain` empty) |
| Tags | `doctrine-adopted-2026-07-30` (one, and only one) |
| Tracked files | 191 |
| Tracked markdown words | 434,019 |
| Untracked-not-ignored | 0 |

## 2. Tracked inventory, by area

| Area | Tracked files | Role |
|---|---|---|
| `.syzygy/governance/doctrine/` | 6 | **Adopted authority** |
| `.syzygy/governance/decisions/` | 5 | **Recorded owner rulings** |
| `.syzygy/governance/policies/` | 10 | **Owner-approved** (craft-and-care, D2) |
| `.syzygy/governance/contracts/candidates/` | 135 | **Candidate** — no act performed |
| `.syzygy/intent/` | 1 | Governed presentation draft (`OVERVIEW.md`) |
| `.syzygy/map/` | 11 | **Candidate** topology bundle |
| `.github/` | 1 | `governance-docs.yml` — documentation-only CI |
| `scripts/` | 1 | `check_governance.py` |
| `.claude/`, `.codex/` | 3 | `heart-and-soul` navigation skill, settings |

**Absent, correctly:** `openspec/`, `.syzygy/work/`,
`.syzygy/governance/contracts/rfcs/`, `.syzygy/map/topology/`,
`.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md`, any `src/`, any
toolchain manifest. Each is created only by an act or a later lifecycle
stage; absence is the correct current state, not a defect.

**Founder-local, git-excluded:** `_bootstrap/` — 374 files, 7.0 MB, ignored
by the versioned `.gitignore`. Not on any default reading path.

## 3. Authority layers at round start

| Layer | Artifact | Binding today? |
|---|---|---|
| Doctrine VIS-1…7, SEC-1…5 | `governance/doctrine/**` | **Yes** — adopted 2026-07-30, tag `doctrine-adopted-2026-07-30`, amendment D1 in force |
| Owner rulings SDR-1…33, D1, D2, extracted warrants | `governance/decisions/**` | **Yes** |
| Craft-and-care CC-* | `governance/policies/craft-and-care/**` | Owner-approved (D2); clause-level force begins at foundational-contract acceptance |
| Design contracts RFC 0001–0011 (32 modules) | `contracts/candidates/rfcs/**` | **No — candidate** |
| Topology bundle (8 views) | `map/topology-candidates/**` | **No — candidate** |
| Project overview | `intent/OVERVIEW.md` | Governed presentation, never authority; adoption pending |
| Term registry, knowledge-hygiene policy, normative-change workflow | `contracts/candidates/policy-candidates/**` | **No — candidate** |
| Doctrine amendment D3 (bounded missions) | `contracts/candidates/DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md` | **No — proposed** |
| Required observable behavior | *does not exist* | — |
| What exists (code, tests, CI, runtime) | *none* | — |

## 4. Owner gates open at round start

Five, none performed. `ACCEPTANCE-ACT-RECORD.md` does not exist, which is
correct. Digests are owned by the artifact each act names and are
deliberately not restated here — a quoted copy goes stale silently
(`check_governance.py` CG-7d exists precisely because that happened).

| Act | Accepts | Digest source |
|---|---|---|
| 1 | 32 compacted foundational contract modules | `ACTIVE-CONTRACT-MANIFEST.txt` |
| 2 | Craft amendment CC-TEST-2 | `craft-and-care/INSTALL-RECORD.md` current-digest block |
| 3 | Topology bundle | `map/topology-candidates/BUNDLE-MANIFEST.md` |
| 4 | Project overview | acceptance record |
| 5 (optional) | Doctrine amendment D3 | no digest — VIS-4 adoption of the D3 packet, rev1 |

## 5. Validation results at round start

All read-only. Output read, not exit codes.

| Check | Result at `d65fd42` |
|---|---|
| `verify_final_prespec.py` | **PASS** — 99,094 words across 32 modules; 322 numbered clauses; two declared over-ceiling notes (RFC-0001 at 8,353 words, justified; corpus total over the 35–50k target band, owner-facing justification required) |
| `build_contract_index.py --check` | no drift |
| `build_dependency_index.py --check` | no drift |
| `check_governance.py` | 15 OK, 7 WARN, 0 FAIL over 22 checks; 191 files examined |

**Critical distinction:** "no drift" on the dependency index means *the
generated file matches regeneration*. It does **not** mean the graph is
closed. The same generated file reports **20 asymmetric or dangling edges**
in its own "Graph consistency" section, by design — the generator reports
disagreements rather than repairing them. A green drift check over a
knowingly inconsistent graph is exactly the "PASS over zero examined items"
hazard the project's own rules warn about, in a subtler form.

## 6. External-review hypotheses — verified before acting

The round charter carried findings from a prior external review. Each was
treated as a hypothesis and checked against current bytes. Results:

| # | Hypothesis | Verified? | Evidence |
|---|---|---|---|
| 4.1 | `AGENTS.md` at its 1,500-word decomposition trigger, still carrying process lore | **TRUE** | `wc -w AGENTS.md` = 1,500 exactly; a "Verification hazards" and "Incident history" section is present |
| 4.1 | Root README passes 30-second orientation | referred to fresh reviewer RC-1 | — |
| 4.3 | Doctrine README glossary reportedly **absent** | **FALSE** | `.syzygy/governance/doctrine/README.md:15` = `## Glossary (read first)`. The real defect is an **ambiguous citation**: `vision.md:16` and `:39` say "README glossary" without saying *which* README (root vs doctrine). A missing artifact and an ambiguous pointer need different fixes; the carried finding would have caused the wrong one |
| 4.4 | Corpus ≈99,000 words | **TRUE** | 99,094, computed |
| 4.4 | ≈20 asymmetric/dangling dependency edges | **TRUE — exactly 20** | `CONTRACT-DEPENDENCY-INDEX.md`, "Graph consistency" |
| 4.7 | Acceptance record still describes the package as founder-local under `_bootstrap/**` | **TRUE** | `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:143` — "package lives in the deliberately git-excluded `_bootstrap/` working tree". The package is in fact tracked under `contracts/candidates/**` and present in a clean clone |
| 4.7 | No independent review over the exact current bytes | **TRUE** | `PROJECT-STATUS.md:66-70` discloses it as the round's principal residual |
| 4.8 | Craft-and-care adopts `th-engineering` via a founder-machine path | **TRUE** | `craft-and-care/README.md:18` cites `~/.claude/skills/th-engineering/subskills/` |
| 4.8 | A clean clone needs a publicly resolvable substrate revision and digest | **TRUE, and better than assumed** | The substrate is **public**: `~/.claude/skills/th-engineering` → `~/.dotfiles/ai-bootstrap/skills/personal/th-engineering`, and `github.com/Tzeusy/ai-bootstrap` is a **public MIT** repository. Only the *citation form* was unresolvable, not the material. `~/.dotfiles` itself is private and is not needed |

### 6.1 New finding, not in the carried set

Building the substrate lock surfaced a defect no prior review had:
**the adopted `th-engineering` baseline has materially drifted from its
pin, and the drift was never surfaced.**

`craft-and-care/README.md` pins "the installed `th-engineering` bar as read
on 2026-07-30 (engineering-bar biases 1–9 + Definition of Done; test-rigor
rules 1–8; dependency-hygiene rules 1–7)", and commits that "if the
installed bar changes materially against that pin … the conflict is
surfaced to the owner, not silently absorbed."

Resolved to public commits: the pin is `61bd8fa` (2026-07-27, the newest
commit at or before the pin date); what is installed now is `f4cf1c7`
(2026-08-02). Between them, in that repository's skill tree:

- The **test-rigor** skill — **numbered bars went from 1–8 to 1–10.** Two new
  bars exist that D2 did not approve: (9) suite tiering and targetability,
  (10) governed test growth. Bars 1 and 5 also gained text.
- The **engineering-bar** skill — **Definition of Done gained an item**
  ("Test delta accounted"). Biases 1–9 verified unchanged by diff.
- The **dependency-hygiene** skill — byte-identical; rules 1–7 unchanged.

The pin's own rule was therefore due to fire and did not, because nothing
mechanical could see the founder-machine path. Recorded in
`policies/GOVERNANCE-SUBSTRATE-LOCK.yaml` under `th_engineering.drift`,
raised as an owner item, and **not absorbed**. It bears on act 2 (whose
subject is craft policy text); it does not block acts 1, 3, 4, or 5.

## 7. Round-start defects carried into the fix batch

1. **20 asymmetric dependency edges** — a Context Compiler correctness
   blocker: a routing layer cannot be trusted over a graph whose two halves
   disagree.
2. **Acceptance-record provenance is stale** — points at a git-excluded home
   for material that is tracked.
3. **`AGENTS.md` at its decomposition trigger**, carrying incident history in
   default context.
4. **`vision.md`'s "README glossary" citation is ambiguous** — and a prior
   review recorded this as a *missing artifact*, which would have produced
   the wrong repair.
5. **`th-engineering` baseline drift, unsurfaced** (§6.1).
6. **No fresh review over current bytes** — nine were commissioned for this
   round.

## 8. Beads state

One issue total, closed; zero open, zero ready. No product backlog exists,
which is the required state for this phase (`AGENTS.md`: beads tracks
process housekeeping only). No implementation issue, epic, or backlog was
created by this round.

## 9. Method notes

- `grep` on this machine is **ugrep**; `[^]]`-style classes silently match
  nothing. Every load-bearing sweep in this round used `grep -F` or Python
  `re`, and every universal claim was reproduced by a second method.
- Every digest in this round's records was computed by command in the same
  session that wrote it. None was transcribed.
- The clean-clone reviewer worked against a real `git clone`, not a
  simulation, so `_bootstrap/` was absent by construction rather than by
  discipline.
