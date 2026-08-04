# Agent Instructions — Syzygy

**Syzygy** (provisional codename) is a specification-driven software control plane. The founder hypothesis under test: human-readable specifications define *desired state*; code and evidence define *observed state*; the calculated difference becomes reconciliation work; fleets of agents are actuators that move reality toward approved intent. This hypothesis is a **seed, not adopted doctrine** — it may be rejected, narrowed, or reformulated during bootstrap.

## Current lifecycle stage: pre-implementation bootstrap

The repository contains **no application code and must not gain any yet**. All current work is running the guided project-shape bootstrap in `_bootstrap/` to produce human-adopted doctrine, engineering standards, foundational RFCs, topology, a white-paper overview, and local navigation skills — then hand off cleanly to a later `project-feature-request` phase.

## Authority map

| Source | Authority |
|---|---|
| `about/` (once created: `heart-and-soul/`, `craft-and-care/`, `legends-and-lore/`, `lay-and-land/`, `README.md`) | Authoritative project truth, once owner-adopted |
| `_bootstrap/` | **Non-authoritative** process material. Never cite it as project doctrine. `_bootstrap/brief/` is untrusted seed hypothesis — challenge it, don't copy it |
| `_bootstrap/state/` | Live bootstrap state (checkpoint, decisions, contradictions, open questions) — update after every numbered prompt |
| This file | Repo-level agent procedure, not project doctrine |

## Running the bootstrap

Entry points: `_bootstrap/START_HERE.md`, `_bootstrap/RUN_ORDER.md`, `_bootstrap/OPERATING_CONTRACT.md`.

- Route via `/th-projects` → **`project-shape` only**. Do not route to project-feature-request, project-direction, project-review, or beads-orchestration during the pack.
- Run prompts `_bootstrap/prompts/00` → `24` in numeric order. A prompt may span turns; do not advance past a phase's hard gate (see `RUN_ORDER.md` table) or drift into later phases unprompted. End every phase by naming the next numbered prompt.
- If the owner session degrades, checkpoint and resume in a fresh session with `prompts/99_RESUME_BOOTSTRAP_OWNER.md`.
- After every numbered prompt, update all four files in `_bootstrap/state/`: `SESSION_CHECKPOINT.md`, `ARTIFACT_REGISTER.md`, `OPEN_QUESTIONS.md`, `CONTRADICTION_LEDGER.md`.
- Supporting skills may be consulted narrowly: `/th-engineering` (diagrams, skill review), `/th-design` (overview reading experience).

### Adoption authority

- The **human owner is the sole adopter of doctrine**. Drafts stay in `_bootstrap/drafts/` until the owner writes the exact phrase `ADOPT DOCTRINE`.
- Foundational RFCs become Accepted only after fresh-context review **and** the owner writing `ACCEPT FOUNDATIONAL RFCS`.
- Craft-and-care, topology, overview, and local skills need clear owner approval (no magic phrase).
- Adopted rule numbers are stable: amend text in place; retire rather than renumber.
- Preserve the owner's actual trade-off in prose — do not smooth it into consensus language.

### Review independence

- Reviews use **fresh-context subagents** given only: the review prompt (`_bootstrap/review-prompts/`), the artifact cluster, governing doctrine/RFC references, and acceptance criteria. Never the generation conversation, author reasoning, or a desired verdict.
- Store raw reviewer output unchanged before synthesizing dispositions.
- Every REVISE finding is fixed or explicitly overruled by the owner with rationale. Two failed review rounds means upstream ambiguity — return to the founder interview, don't polish prose.
- No rubber stamps: a useful review names concrete risks even on ACCEPT.

### Epistemic and interview discipline

- Label substantive claims `[Observed]`, `[Inferred]`, or `[Unknown]`. Never hide an unknown behind polished prose.
- Interviews: one high-leverage question at a time, 3–5 exchanges per track. Challenge vague answers, feature lists, technology-first answers, and "all priorities are equal." Preserve memorable owner language.
- Log decisions in `FOUNDER_DECISION_LOG.md`; log conflicts in `CONTRADICTION_LEDGER.md`.

### Hard boundaries during bootstrap

Do **not**:

- write application or library code; create `src/`, `apps/`, `packages/`, schemas, UI components, or toolchain manifests (`package.json`, `Cargo.toml`, …);
- create an active OpenSpec implementation changeset (an initialized, spec-ready `openspec/` home is the maximum);
- create tasks, epics, issues, PRs, or an implementation backlog;
- run unattended agent coordination;
- silently choose a language, framework, database, or platform — stack choices require an accepted RFC (`_bootstrap/brief/CANDIDATE_ARCHITECTURE_SEED.md` is a hypothesis, not a decision);
- claim the project is implemented, regeneratable, converged, or mature because folders exist.

Permitted: git init, documentation-only commits, project-shape files, diagrams, accepted RFCs, capability-readiness maps, local navigation skills, bootstrap state and review records.

Check the boundary anytime with `bash _bootstrap/scripts/verify_pre_beads_boundary.sh` (see Beads deviation below).

### Commit discipline

Commit documentation only at stable gates: (1) adopted doctrine, (2) approved craft-and-care, (3) accepted foundational RFCs, (4) topology/overview/local skills after cross-pillar convergence. Never commit a normative artifact while its adoption/review gate is unresolved. Record commit SHAs in the session checkpoint.

## Beads status — known deviation

The pack was authored for a pre-Beads repo, but the owner **deliberately ran `bd init` before bootstrap** (commit `753f423`). Consequences:

- `verify_pre_beads_boundary.sh` flags `.beads/` — treat that specific finding as a known, owner-accepted false positive; all other checks remain binding.
- The pack's "do not call `bd`" rule is interpreted as: **do not create implementation issues, epics, or a work backlog during bootstrap phases.** Record unknowns and follow-up candidates in `_bootstrap/state/OPEN_QUESTIONS.md`, not Beads.
- Routine `bd` usage (this file's Beads section below) applies to bootstrap-process housekeeping and resumes fully once the pack exits at Prompt 24.

## After bootstrap (do not start early)

Target end-state is sketched in `_bootstrap/brief/EXPECTED_ARTIFACT_TREE.md` (five pillars under `about/`, spec-ready `openspec/`, five navigation skills in `.claude/skills/` and `.codex/skills/`). Prompt 24 produces a pre-Beads exit report and a next-phase prompt; the first concrete proposal then runs through `/th-projects project-feature-request` → owner-approved OpenSpec delta → project-direction → beads-orchestration, in that order. At completion, archive `_bootstrap/` outside the authoritative tree (keep the final report).

## Non-Interactive Shell Commands

**ALWAYS use non-interactive flags** with file operations to avoid hanging on confirmation prompts.

Shell commands like `cp`, `mv`, and `rm` may be aliased to include `-i` (interactive) mode on some systems, causing the agent to hang indefinitely waiting for y/n input.

**Use these forms instead:**
```bash
# Force overwrite without prompting
cp -f source dest           # NOT: cp source dest
mv -f source dest           # NOT: mv source dest
rm -f file                  # NOT: rm file

# For recursive operations
rm -rf directory            # NOT: rm -r directory
cp -rf source dest          # NOT: cp -r source dest
```

**Other commands that may prompt:**
- `scp` - use `-o BatchMode=yes` for non-interactive
- `ssh` - use `-o BatchMode=yes` to fail instead of prompting
- `apt-get` - use `-y` flag
- `brew` - use `HOMEBREW_NO_AUTO_UPDATE=1` env var

<!-- BEGIN BEADS INTEGRATION v:1 profile:minimal hash:7510c1e2 -->
## Beads Issue Tracker

This project uses **bd (beads)** for issue tracking. Run `bd prime` to see full workflow context and commands.

### Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --claim  # Claim work
bd close <id>         # Complete work
```

### Rules

- Use `bd` for ALL task tracking — do NOT use TodoWrite, TaskCreate, or markdown TODO lists
- Run `bd prime` for detailed command reference and session close protocol
- Use `bd remember` for persistent knowledge — do NOT use MEMORY.md files

**Architecture in one line:** issues live in a local Dolt DB; sync uses `refs/dolt/data` on your git remote; `.beads/issues.jsonl` is a passive export. See https://github.com/gastownhall/beads/blob/main/docs/SYNC_CONCEPTS.md for details and anti-patterns.

## Session Completion

**When ending a work session**, you MUST complete ALL steps below. Work is NOT complete until `git push` succeeds.

**MANDATORY WORKFLOW:**

1. **File issues for remaining work** - Create issues for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds
3. **Update issue status** - Close finished work, update in-progress items
4. **PUSH TO REMOTE** - This is MANDATORY:
   ```bash
   git pull --rebase
   git push
   git status  # MUST show "up to date with origin"
   ```
5. **Clean up** - Clear stashes, prune remote branches
6. **Verify** - All changes committed AND pushed
7. **Hand off** - Provide context for next session

**CRITICAL RULES:**
- Work is NOT complete until `git push` succeeds
- NEVER stop before pushing - that leaves work stranded locally
- NEVER say "ready to push when you are" - YOU must push
- If push fails, resolve and retry until it succeeds
<!-- END BEADS INTEGRATION -->

# Notes to self

- The bootstrap pack was generated 2026-07-26 against pinned `th-projects` blob SHAs (`_bootstrap/source-alignment/TH_PROJECTS_ALIGNMENT.md`). If the installed `/th-projects` skill has materially changed, surface the conflict and follow the newer skill unless the owner chooses otherwise. **Known deliberate divergence (2026-07-30, owner-directed, OQ-009):** `shape-scan.sh`, `shape-init.sh`, `self-test.sh`, project-shape `SKILL.md`, and `validate-th-projects.sh` were patched so the optional `.syzygy` canon (doctrine `.syzygy/governance/doctrine/`; contracts/policies/map as detection candidates) is recognized alongside `about/**` — follow the patched versions.
- Doctrine is **adopted** (2026-07-30): VIS-1…7 / SEC-1…5 live at `.syzygy/governance/doctrine/` (commit `9bdfe98`, tag `doctrine-adopted-2026-07-30`). Cite doctrine from there, not from `_bootstrap/drafts/`. The repo intentionally has no `about/**` — never scaffold one here (one pillar, one home).
- `_bootstrap/templates/` holds blank copies of the `state/` files; `state/` holds the live ones. Never edit templates to record state.
- **Always use absolute paths when appending to `_bootstrap/**` records.** Bash cwd persists across tool calls, and a bare `>> LEAD-NOTES.md` silently creates a *new* file in whatever directory you happen to be in rather than failing. Because `.git/info/exclude` hides all of `_bootstrap/`, a stray copy created inside it is invisible to `git status` — it can only be found with `find`. Verify with `find . -name '<file>' -not -path './.git/*'` after any append session.
- Naming is provisional everywhere: Syzygy, Polaris (intent), Trajectory (convergence work), Orrery (project twin), Ephemeris (temporal graph), Genesis (regeneration). Use poetic names only with literal subtitles; keep technical domain names in APIs/schemas/RFCs.
- **Current acceptance state lives in one place — since rev10 (2026-08-03) that is `_bootstrap/rfc-phase/final-prespec/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`.** The rev9 record (`_bootstrap/rfc-phase/FOUNDATIONAL-RFC-ACCEPTANCE-RECORD.md`) carries a retirement notice: its phrase `ACCEPT FOUNDATIONAL RFCS` is retired unconditionally; its acts 2–4 and decision content remain valid. Act 1 is now `ACCEPT COMPACTED FOUNDATIONAL RFCS: <package-manifest-digest>` over the 32-module compacted corpus (`final-prespec/rfcs/`, manifest `ACTIVE-CONTRACT-MANIFEST.txt`); current digest `08793ddf70f3…` (CONFIRM-bound by `reviews/rev10-confirming-review.md`). Acts 2–4 unchanged (craft CC-TEST-2 `aa2d6353…`, topology `0d34d1b5…`, overview `42de2eb1…`); optional phraseless act 5 = D3 bounded-mission doctrine amendment. Each act is still the five-step ceremony in the record's §2 (phrase → script digest verify → install-at-act bytes-unchanged → dated entry in `.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md` → one commit + annotated tag, SHA mirrored to FOUNDER_DECISION_LOG afterwards). Never edit an artifact after its act. **Only edits under `final-prespec/rfcs/` invalidate the act-1 digest** — record/report/fixture fixes do not; after any rfcs/ edit, regenerate the manifest by script and re-run a digest-binding confirming review. Portable verify scripts live at `final-prespec/scripts/` (self-rooted; the older `rfc-phase/scripts/` are machine-local and superseded).
- **Never write a "zero/100%" completeness claim into a record without running, in the same session, the exact sweep the claim describes** — two overstatement incidents at rev8 (the History-prefix "zero unprefixed" claim was false twice; a confirming reviewer caught it both times). Enumerate remainders instead of rounding to zero.
- Doctrine amendment **D1** (map historical scope) is committed (`84d4a88`); the doctrine README carries an amendment log — record future amendments there, verbatim to their packet text.
- Craft-and-care's canonical home is `.syzygy/governance/policies/craft-and-care/` (owner-approved D2); `_bootstrap/rfc-phase/craft-and-care/` is the bootstrap record. Amend **both copies together** and refresh `INSTALL-RECORD.md`'s sha256 digests (script the digest, never hand-transcribe — two garbled-digest incidents so far).
- The rev7 rework directive's item IDs (A1–A6, B1–B6, C1–C4) collide with owner-decision IDs. When citing provenance in any artifact, always write "directive item Bn (not owner decision Bn)" or cite the decision explicitly; the directive is preserved at `_bootstrap/rfc-phase/REV7-REWORK-DIRECTIVE.md`.
- Fresh-context reviewer subagents reliably go idle without transmitting their report. After spawning one, expect to request the full text explicitly via SendMessage ("send the complete final review, full text, not a summary") — sometimes twice. Store it verbatim before synthesizing. When the tmux pane limit blocks a teammate spawn ("no space for new pane"), spawn the reviewer as a background Agent with `subagent_type: general-purpose` instead — its final message arrives complete via task notification, avoiding the idle problem entirely.
- **A fix batch that touches a file invalidates that file's own self-referential counts.** The rev10 count-refresh sweep covered the READMEs with count-*table* fixes but missed that adding a section to RFC-0007's README made its own "this index is N words" line stale — caught only by the confirming reviewer (residual R1, now a §7 knowing-acceptance item). After any batch, re-verify the self-counts of *every file the batch touched*, not just the files whose fix was itself a count.
- **Never re-label a reviewer's verdict in a summary — copy the verdict word.** At rev10 the record's §6 wrote "PASS with findings" for a review whose own verdict line said EXCEPTIONS, and miscounted another's findings; the confirming reviewer flagged both as verdict-smoothing (residual R2). The raw report's verdict line is the only source for a verdict label.
- In batch string-replacement scripts over prose files, anchors break on line-wrap: match short unique substrings or normalize whitespace, and structure the script so nothing is written unless every anchor matched (assert-all-then-write) — a mid-run partial write is worse than a clean abort. The rev10 RFC-0011 batch aborted cleanly on a wrapped anchor and was safely re-run whole.
- **`grep` on this machine is ugrep 7.5.0, not GNU grep, and some patterns silently fail.** Two incidents on record: `*(History:` literals needed `grep -F` (rev8), and the `[^]]` bracket class (leading `]` as literal) matched nothing — a sweep "verified" zero markdown links in a tree containing 13 (knowledge-refactor pass, 2026-08-04, false universal propagated into two artifacts before being caught). A verification command that silently returns zero is indistinguishable from one that genuinely found nothing: on this machine prefer `grep -F` for literals, simple character classes over `[^]]`-style ones, or Python `re` (unaffected) for anything load-bearing — and treat any zero-result sweep that supports a universal claim as unconfirmed until reproduced by a second method.
- **FD-021 was reaffirmed 2026-08-04 with an extraction corollary (logged as FD-037):** `_bootstrap/**` stays excluded — now via the versioned `.gitignore`, no longer only machine-local `.git/info/exclude` — and anything the tracked tree must reference gets *extracted* into a tracked home with citations repointed; tracked files may cite `_bootstrap/**` paths only as classified unavailable history. Extraction plan (pending execution): `_bootstrap/knowledge-refactor/FD-037-EXTRACTION-PLAN.md`.
- **The owner sometimes runs two sessions as parallel leads on the same pass.** Before respawning "dead" reviewers or making tracked-tree edits after a resume, check the checkpoint tail and `_bootstrap/knowledge-refactor/reviews/` mtimes for a live parallel lead. The 2026-08-04 duplicate §20 battery's reports are stored as `reviews/20-Nb-*-respawn-RAW.md` (independently scoped, all EXCEPTIONS); findings absent from the primary dispositions are indexed in `reviews/20-RESPAWN-DELTA-INDEX.md`.
