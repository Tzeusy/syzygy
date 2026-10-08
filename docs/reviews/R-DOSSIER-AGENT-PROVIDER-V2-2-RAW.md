# R-DOSSIER-AGENT-PROVIDER-V2-2 — agent-provider statement, version 2 (round 2)
Reviewed commit: 5db1dd720338edd7963653f7e19ff727e1e99f32
Manifest SHA-256: 62cd699a6fbc4ad07777509e17530948f68efc7978800f6c0e4db358c7d06af7
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer: fresh-context reviewer (Claude Opus 5.5), 2026-10-08, CC-REV-1.
Brief: `.syzygy/governance/contracts/candidates/dossier-agent-provider-v2/REVIEW-BRIEF.md` at the reviewed commit. Its
recording section still names round 1's file. The lead directed this raw's `-2-` name.
Runs: a scratch worktree detached at the reviewed commit, with `npm ci`; removed afterwards. No commits, pushes or PR comments.

The verdict confirms the record bytes at the manifest row, the same bytes round 1 confirmed. All three exceptions are notes on
the semantic delta's install list. None touches the act's argument, and repairing any of them does not change the manifest file.

## 1. Record and manifest unchanged since round 1 [Observed]

- `git merge-base --is-ancestor 897910fc… 5db1dd72…` exits 1, so the round-1 commit is not an ancestor of this head (it was
  rebased). Byte identity is therefore checked by content. `git diff --stat 897910fc 5db1dd72` over `instances/`, the manifest,
  `templates/`, the whole `dossier-local-agent-acts/` directory and
  `decisions/DOSSIER-LOCAL-AGENT-REDIS-AGENT-ANTHROPIC-ACT.md` prints nothing. Over the whole package and the builder it prints
  two changed files: `SEMANTIC-DELTA.md` (51 lines) and `scripts/build_dossier_agent_provider_v2.py` (20 lines), 63 insertions
  and 8 deletions in all.
- First method: `--manifest-digest` printed `62cd699a6fbc4ad07777509e17530948f68efc7978800f6c0e4db358c7d06af7`. Second
  method: `sha256sum` of the manifest file printed the same value. That is also the value in round 1's head.
- `sha256sum` of the version-2 record equals the manifest's one row (`--digests` prints the same row). The manifest at
  `897910fc` (`git show`) carries that identical row.
- `sha256sum` of the version-1 record equals the argument on `DOSSIER-LOCAL-AGENT-REDIS-AGENT-ANTHROPIC-ACT.md:36`.
  `git diff --stat origin/main 5db1dd72` over the version-1 package, its act, `gate-sources.ts`, `preflight.ts`, `reverify.ts`
  and `package-reader.ts` prints nothing.

## Runs [Observed]

- `--check`: "dossier-agent-provider-v2: record and manifest current".
- `--selftest`: "selftest: 13 of 13 predicates held", all `ok`. The new one is "a digest in a template's header refused".
- Rule 6, independently of the selftest: I put a 64-hex token into the first `> ` line of
  `templates/AGENT-PROVIDER-STATEMENT-TEMPLATE-V2.md`. `--check` failed with "FAIL
  templates/AGENT-PROVIDER-STATEMENT-TEMPLATE-V2.md: carries a 64-hex token". After restoring the file it passed again. Round 1's
  surviving mutant is now killed.
- `git diff --no-index` of the version-1 and version-2 records gives three hunks: the two-line instance header, `Date:`,
  `Record version:`, one added `- project-documentation` line, and `Proposed revocation state:`. These are exactly the five rows
  of the delta's table.
- `python3 scripts/check_governance.py` gives "32 OK, 21 WARN, 0 FAIL (53 checks)". The one untracked file it counted was my
  probe test, described below.
- Probe (`packages/polaris-dossier/src/zz-r2-probe.test.ts`, scratch only, run with vitest over the real decisions tree through
  an fs wrapper). It adds one synthetic version-2 act record, `DOSSIER-AGENT-PROVIDER-V2-REDIS-ANTHROPIC-ACT.md`, made from version
  1's act. The title, identity, artifact path, argument, label and tag are changed. The form has version 1's pattern: file
  stem, identity stem, artifact basename, heading, label, title, Record ID and Subject tuple. Results:
  - Baseline at this head: `statementsFor('redis-redis')` returns one record,
    `AGENT-PROVIDER-redis-redis-anthropic@0.1.0-candidate.1`, with the five classes, and the gate returns `ok`.
  - A. Version 1's real form, with the version-2 act present: `refused`, `namedBy`
    `decisions/DOSSIER-AGENT-PROVIDER-V2-REDIS-ANTHROPIC-ACT.md`.
  - B. The version-2 form, with both acts present: `refused`, `namedBy` `decisions/DOSSIER-LOCAL-AGENT-REDIS-AGENT-ANTHROPIC-ACT.md`.
  - C. The version-2 form, with version 1's act file hidden but `ACCEPTANCE-ACT-RECORD.md` unchanged: `ok`.
  - D. The admission reader and the class-act reader, with the plain version-2 act present: both `ok`. Then with one appended
    line citing `.syzygy/governance/contracts/candidates/public-egress-v2/`, the admission read threw `invalid-records`. With one
    appended line citing `RFC5-PROJECT-DOCUMENTATION-CLASS-AMENDMENT-ACT.md`, the class act read returned `refused`.
  - E. The version-2 form with the title stem "Redis agent-provider statement version 2", version 1's act hidden: `refused`,
    `namedBy` `decisions/PENDING-OWNER-DECISIONS.md`. That is the P-106 row.

## 2. Round-1 findings against the repairs

**Finding 1 (revise), the `--tool` override.** The new bullet, `SEMANTIC-DELTA.md` lines 107-118:
"**Prerequisite: the `--tool` override (`syzygy-up98`, being fixed in code separately).** … The version-2 act should not be
installed until `session-prompt` refuses a tool whose pair has no in-force statement, or gates on the session's pair."
[Observed] This makes the fix a precondition of installation, which round 1 offered as one remedy. The code fix is on
`origin/main` at `102be1fc`, which is not in this head. It adds `sessionStatementRefusal` to `session-handover.ts`, called
right after the `const tool = request.tool ?? declared.agentTool;` line. When the run relies on a statement, that function
requires `providerStatementGate(records, tool, declared provider, now)` to return `ok`, and requires the session pair's
statement to list every class in the run's statement. [Inferred] A `codex` session on a Redis run declared for Anthropic finds
no statement (the OpenAI form's pair is codex with openai), so it refuses. The widening therefore reaches only a session pair
holding a statement that lists `project-documentation`. Repaired. Note 1 below covers the now-stale wording.

**Finding 2 (revise), the reverse sweep direction.** The new bullet, lines 93-106: "Version 2's artifact has version 1's
basename … `sittingForm` puts the basename in the stems (`:181`), and `namesDigestBoundAct` … matches stems in the text and on
the field lines of every other decisions file … The version-aware form must exempt each version's own predecessor and successor
records from the other's sweep, in both directions." [Observed] Probes A and B reproduce both directions exactly as stated.
Repaired. One clause overstates the case; see note 2.

**Finding 3 (note), preflight.** New bullet, lines 119-123: "`preflight.ts` filters on its own (`:50`) … End the term in the
source (`statementsFor`), so the gate and preflight agree." [Observed] `preflight.ts:50` filters `statementsFor` output on its
own predicate. Ending the term in the source is the right remedy. Repaired.

**Finding 4 (note), unstated consequences.** Lines 60-71 now state the drawer-act condition and the `statement-changed` restart.
[Observed] `governed.ts:54` reads `statementRequired: kind !== 'non-governed'`. `class-gate.ts:33` withholds every class except
`code-content` when `consented === null`. `reverify.ts:159-160` is the `statement-changed` refusal. All three line citations
hold. Repaired.

**Finding 5 (note), the builder's 64-hex sweep.** `stale()` now uses `rglob("*.md")`, skips `instances/` and `reviews/` by
first path part plus round dispositions, and adds a selftest mutant. My independent mutant, above, is killed. Repaired.

**Finding 6 (note), "inventory".** Lines 55-59 now say: "Syzygy's fidelity review packet and … the rendered site that the design
review packet carries … the inventory brief carries no target bytes." [Observed] This matches the population comment at
`class-gate.ts:13-17`. That comment's residual (lines 19-21: agent-authored `draft`/`inventory` documents may quote a withheld
body) is a separate disclosure this package does not change. Repaired.

## 3. Install list: one in-force statement, and preflight agreement

I re-derived every line the list cites at this head [Observed]. In `gate-sources.ts`: `statementForm` is `:220-232`,
`STATEMENT_FORMS` is `:233-238`, the "supersedes nothing" template line is `:113-114`, the label is `:225`, the stems are `:181`,
the Record-ID stem is `:230`, `withdrawn: true` on `namedBy` is `:271`, `liveStatements` is `:287-288`, `statementContentClasses`
is `:291` and the ambiguity refusal is `:304`. In `package-reader.ts`, `namesDigestBoundAct` is `:570-576`. Also `preflight.ts:50`,
`reverify.ts:159-160` and `:163`, `session-handover.ts:143`, and line 15 of version 1's act. Every citation lands on the code it
describes.

Every consumer reads statements through `statementsFor`: `init.ts:133`, `reverify.ts:155`, `preflight.ts:49`, and
`session-handover.ts` on main. Each then calls `providerStatementGate`, `statementContentClasses` or preflight's own filter.
[Inferred] Suppose an installer adds a version-2 form whose sweep exempts version 1's records and whose predecessor's sweep
exempts version 2's, and ends version 1's term inside `statementsFor` at version 2's instant. Then the gate sees exactly one
live statement, `AGENT-PROVIDER-redis-redis-anthropic@0.2.0-candidate.1`, with six classes, and preflight's `inForce` lists the
same one record. Probe C supports the first half: once version 1's act file is out of version 2's sweep, nothing else in
today's decisions tree names version 2 under a version-1-pattern form. Probes A and B show the two collisions the list names
are real and are the only ones present. So for the paths the brief names, the list is complete. Three notes follow.

Criteria 2, 3 and 5, afresh:

- **Criterion 2.** [Observed] The supersession sentence is unchanged since round 1. It names `0.1.0-candidate.1`, takes effect
  from the version-2 act's instant, and calls itself prospective under RFC5-13. Version 1's bytes and act are unchanged.
- **Criterion 3.** [Observed] The record still adds only one class line. [Inferred] With `102be1fc` on main, the class reaches
  only session pairs that have an in-force statement listing it. Only Claude Code with Anthropic has one for Redis.
- **Criterion 5.** [Observed] A Python sweep of all six package files for `[0-9a-fA-F]{64}` found exactly one token, in the
  manifest's `.txt` row. The builder has none. The authority words found were "accepted" and "approved" inside criterion 5's own
  sentence, "adopted" in the proposed-provenance field, and conditional "in force". No file labels anything accepted or approved.

## Findings

**Finding 1 — the `--tool` prerequisite is described as pending, and it has landed** (note)

[Observed] `SEMANTIC-DELTA.md:107` says "`syzygy-up98`, being fixed in code separately". On `origin/main`, `102be1fc fix(session-prompt): refuse a --tool whose pair has no in-force statement [syzygy-up98]`
and `ff9a19b6` (rule-6 mutants, 9 of 9) have landed. This head is based below them. When the package is rebased, cite the
commit and say the precondition is met. The installer can then check it instead of re-deriving it.

**Finding 2 — the aggregate record does not name version 2** (note)

[Observed] Lines 103-104 say a version-1-pattern version-2 form "would read version 1's act record, and its
`ACCEPTANCE-ACT-RECORD.md` block, as naming version 2". `namesDigestBoundAct` exempts `ACCEPTANCE-ACT-RECORD.md` from the text
check (`package-reader.ts:572`). Version 1's block (`ACCEPTANCE-ACT-RECORD.md:1338-1366`) carries the basename only in table
rows that start with `|`, and the field-line regex at `:574` does not match those. Probe C returns `ok` with the block present.
The clause errs toward more exemption, which does no harm, but drop it or mark it [Inferred].

**Finding 3 — the list does not warn that the version-2 act's own prose and new stems can close other gates** (note)

[Observed, probes D and E] Every reader sweeps every decisions file:

- A version-2 act record citing the egress precedent (`public-egress-v2/`) refuses the whole admission read (`invalid-records`).
  That closes the observation consent for every repository.
- One citing the class act's file name refuses the RFC5-14 class act. That makes `screen.ts:103`'s prerequisite false, and
  through `checkClassAct` it refuses the admission read too.
- The delta's own Why cites both of those.
- A version-2 title or stem that already appears in a decisions file refuses version 2 itself. The P-106 row says "Redis
  agent-provider statement version 2", and the blockers packet says "provider statement, version 2".

[Observed] The first two hazards fail `polaris-generation-consent/src/real-tree.test.ts`'s "refuse nothing" test in CI. The
third fails `gate-acts.test.ts`'s `expectFollowsTree` real-tree pin only once that pin learns version 2's record. Today it
lists version-1 keys only (`:109-110`).

Add one bullet to the list:

- the version-2 recorder template must carry no other family's stems;
- version 2's new stems (file stem, identity stem, label, title) must be checked against `PENDING-OWNER-DECISIONS.md` and the
  blockers packet and its review notes, or those lines pinned with `citedRows` (the P-104 precedent, `package-reader.ts:550`);
- `expectFollowsTree` must cover both versions in the install commit.

`sittingForm` passes no `citedRows` today (`gate-sources.ts:175-185`), so any line-level exemption, including the one Finding 2
of round 1 asks for, needs that parameter threaded through.
