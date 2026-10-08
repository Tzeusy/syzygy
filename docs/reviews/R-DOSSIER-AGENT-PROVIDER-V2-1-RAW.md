# R-DOSSIER-AGENT-PROVIDER-V2-1 — agent-provider statement, version 2 (round 1)
Reviewed commit: 897910fcc1a186b91d436796bc6e5330836c60c1
Manifest SHA-256: 62cd699a6fbc4ad07777509e17530948f68efc7978800f6c0e4db358c7d06af7
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer: fresh-context reviewer (Claude Opus 5.5), 2026-10-08, CC-REV-1.
Brief: `.syzygy/governance/contracts/candidates/dossier-agent-provider-v2/REVIEW-BRIEF.md` at the reviewed commit.
Runs: scratch worktree detached at the reviewed commit; removed afterwards.

The verdict confirms the record bytes at the manifest row. The exceptions are
in the semantic delta's install list and the builder, neither of which is the
act's argument; repairing them does not change the manifest file.

## Runs [Observed]

- `python3 scripts/build_dossier_agent_provider_v2.py --check`:
  "dossier-agent-provider-v2: record and manifest current".
- `--selftest`: "selftest: 12 of 12 predicates held", all 12 lines `ok`.
- `--manifest-digest` printed the value in this head; `sha256sum` of the
  manifest file printed the same value (two methods, rule 3). `sha256sum` of
  the record printed the manifest's one row.
- `git diff --no-index` of the version-1 and version-2 records: three hunks,
  exactly the five rows of the delta's table (the two-line instance header,
  `Date:`, `Record version:`, one added `- project-documentation` line after
  `derived-composites`, `Proposed revocation state:`). No other line differs.
- `git diff --no-index` of the two templates: the header sentence and the
  `{{SUPERSESSION}}` field, as the v2 template's own header says.
- `python3 scripts/check_governance.py` at the head: "32 OK, 21 WARN, 0 FAIL
  (53 checks)".
- Version 1's record hashes to the argument quoted in
  `decisions/DOSSIER-LOCAL-AGENT-REDIS-AGENT-ANTHROPIC-ACT.md:36`, and
  `git diff --stat origin/main <head>` over that act file and the whole
  `dossier-local-agent-acts/` directory is empty.

## Criteria

1. **Diff is exactly the stated change.** [Observed] Yes, by the runs above.
   The builder derives the expected bytes from the version-1 file, and its
   selftest kills a hand edit, a params drift, a template prose drift and a
   predecessor that already lists the class.
2. **Supersession sound.** [Observed] The revocation sentence is
   byte-identical in form to the egress version-2 record
   (`public-egress-v2/instances/egress-anthropic/EGRESS-CONSENT-ANTHROPIC.md:37`)
   with the version number changed. It names `0.1.0-candidate.1` by version,
   takes effect from the act's own instant, and calls itself prospective under
   RFC5-13 (`consent-egress-secrets.md:115`). Version 1's bytes and act are
   unchanged. [Inferred] A superset successor is a supersession, not a
   withdrawal. The RFC5-13 Unknown-rendering consequence therefore does not
   apply to content that was already consented.
3. **The class addition is the whole widening.** [Observed] In the record
   bytes, yes. The only content change is one class line. Tool, provider,
   repository, Subject and Record ID are unchanged, and "What it does not do"
   still says "no other tool or provider, no other repository". In the code
   the act would switch on, there is one route beyond the operator's own Claude
   Code sessions. See Finding 1.
4. **Install list complete.** It misses one sweep direction (Finding 2) and
   one independent in-force filter (Finding 3). Each needs one line.
5. **Authority.** [Observed] A sweep of every file in the package for
   `[0-9a-f]{64}|accepted|approved|adopted` found one 64-hex token, in the
   manifest's `.txt` row. It found no authority word except the inherited
   "Proposed provenance state: `owner-adopted …`" line, which is a proposal
   field. No file labels anything accepted or approved.

## Findings

**Finding 1 — a session-prompt `--tool` override carries the newly consented class to a tool and provider no statement covers** (revise)

[Observed] `packages/polaris-dossier/src/session-handover.ts:143`: `const tool = request.tool ?? declared.agentTool;`.
Any member of `AGENT_TOOLS`, `codex` included, is accepted for an inventory
or review session. No statement check runs for the overriding tool. The file
has no call to `providerStatementGate` or `statementContentClasses`.
The fidelity packet (`review.ts:202`) and the rendered site carried by the
design packet (`render.ts:262`) are class-gated on `opened.contentClasses`.
That is the classes of the run's *declared* pair (`reverify.ts:163`), not the
session's pair. [Inferred] With version 2 in force, an operator who runs
`session-prompt <run> review --kind fidelity --tool codex` hands
`project-documentation` spans to a Codex session, and so to OpenAI. No
OpenAI statement is in force, and the record itself says it permits "no other
tool or provider". The route already exists for version 1's classes, so it is
not new. Version 2 widens what travels it. This is the one way the answer to
criterion 3 is "more than the operator's Claude Code sessions". Add it to the
install list: either `session-prompt` refuses a `--tool` whose
(tool, provider) pair has no in-force statement, or it class-gates on the
session's pair. Alternatively, the delta can state that the gap is accepted
and why.

**Finding 2 — the install list names only one direction of the sweep collision** (revise)

[Observed] The delta (lines 76-78 and 93-96) says a version-2 act record
would read as naming version 1. The reverse also holds. Version 2's artifact
has the same basename as version 1's, `AGENT-PROVIDER-STATEMENT-ANTHROPIC.md`.
`decisions/DOSSIER-LOCAL-AGENT-REDIS-AGENT-ANTHROPIC-ACT.md:15` carries that
basename on its `Artifact identity:` field line. `sittingForm` puts
`a.artifact.split('/').pop()` in `stems` (`gate-sources.ts:181`), and
`namesDigestBoundAct` (`package-reader.ts:570-576`) matches stems in the text
and on field lines of every other decisions file. A version-2 form built in
the version-1 pattern would therefore find version 1's act record. It would
return `refused` with `namedBy`, and `providerStatement` would mark version 2
withdrawn (`gate-sources.ts:271`), so the gate would refuse. "Only the
version-aware form above removes the collision" may be meant to cover this,
but the list should say that version 2's sweep must not read version 1's act
record, or its `ACCEPTANCE-ACT-RECORD.md` row, as naming version 2.

**Finding 3 — preflight's in-force list filters independently of the gate** (note)

[Observed] `preflight.ts:50` lists every statement that is unwithdrawn,
act-bound, in force by `now` and has a class. It does not go through
`liveStatements` or `providerStatementGate`. If version 1's term is ended only
inside the gate (the delta's `:304` bullet), preflight will report both
versions as in force once version 2's act exists. End the term in the source
(`statementsFor`) so that both consumers agree, or name `preflight.ts` in
the list.

**Finding 4 — consequences the delta does not state** (note)

[Observed] `reverify.ts:157-158` refuses `statement-changed` when the in-force
record string differs from the one the run relies on. After version 2's
instant, every Redis run opened under `@0.1.0-candidate.1` refuses at its
next step and must be restarted. That is fail-closed and correct, but
unstated. [Observed] `governed.ts:54` gives `statementRequired: false` for a
non-governed subject. `class-gate.ts` then withholds `project-documentation`
when no statement is relied on. Only three local-agent acts exist in
`decisions/` (D9, RFC7-20, Redis Anthropic), and none is the drawer act, so
Redis is `unstated` today and version 2 would take effect. [Inferred] If the
owner also performs the no-evidence-drawer act, Redis becomes non-governed and
version 2 has no effect on packets. The delta's [Inferred] "Why" bullet should
carry that condition.

**Finding 5 — the builder's 64-hex predicate does not reach `templates/`** (note)

[Observed] `stale()` sweeps `(root / PKG).glob("*.md")`, which is not
recursive. Rule-6 mutant: I put a 64-hex token into the template's header
blockquote (`> new version <64 hex>. Version 2 …`). `--check` printed "record
and manifest current". The mutant survived because `HEADER` replaces that
blockquote before rendering. A token in the template body is caught, but only
indirectly, as a predecessor mismatch. Criterion 5 covers Markdown "outside
`instances/` and `reviews/`", which includes `templates/`. Restored after the
run.

**Finding 6 — "inventory" in the delta's [Inferred] bullet** (note)

[Observed] The consumers of `screenPath`/`screenBody` in
`packages/polaris-dossier/src` are `review.ts`, `render.ts`, `check.ts`,
`close.ts`, `screen.ts` and `class-gate.ts` (and one test), and `inventory.ts`
is not among them. The class gate's own population comment names the
fidelity packet and the rendered site carried by the design packet. Line 55
of the delta says docs spans "may go into Syzygy's own inventory and review
packets". Say "fidelity and design review packets", or name the inventory
path that carries spans.
