# Review brief — Polaris dossier local-agent mode, version 1.2

> **Candidate — binds nothing.** This brief says what an independent
> reviewer is given and what they decide. It is not a review and carries no
> verdict. Stopping rule, set before round 1: at most three rounds; CONFIRM,
> or CONFIRM WITH EXCEPTIONS with notes only, clears the bytes (owner ruling
> of 2026-09-26: the notes go to a sibling record); a third REVISE goes to
> the owner with all three raws.

## What the reviewer is given, and nothing else

CC-REV-1 calls for a fresh context holding only the artifact, its governing
references and the acceptance criteria. Run on the default model.

**Network.** Do not fetch any content of any external or target repository:
no `gh api` contents, no raw URLs, no clone, no web access. The only network
use allowed is `git fetch` of this repository. Where a criterion turns on
how a coding-agent harness behaves (for example, how Claude Code applies an
`--allowedTools` rule), judge from general knowledge and label it
`[Inferred]`.

**The artifact under review.** In
`.syzygy/governance/contracts/candidates/polaris-dossier-local-agent-mode-v1-2/`:

- `proposed/spec.md.patch`, `proposed/design.md.patch`,
  `proposed/proposal.md.patch` (the subject);
- `SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`, `OWNER-DECISION-PACKET.md` and
  this brief.

Apply the patches to `openspec/changes/polaris-dossier-local-agent-mode/` in
a scratch worktree of the commit under review (`git worktree add --detach`,
then `npm ci` if you run anything under `packages/`, then `git apply`), and
read the post-apply bytes beside the v1.1 bytes; `git diff` is the change.

**Governing references.**

- The direction the change carries:
  `.syzygy/governance/decisions/POLARIS-DOSSIER-WAITING-SESSIONS-DIRECTION.md`,
  and decision 3 of
  `.syzygy/governance/decisions/DOSSIER-BLOCKERS-DECISION-PACKET-2026-10-08.md`.
- The owner direction of 2026-10-05 on who starts a session:
  `.syzygy/governance/decisions/POLARIS-DOSSIER-LOCAL-AGENT-SCOPE-REVIEW-SIGNOFF-DIRECTION.md`
  (item 2); and the direction of 2026-10-03, item 2:
  `.syzygy/governance/decisions/OWNER-DIRECTION-2026-10-03-OVERNIGHT-BEADS-LOOP.md`.
- The v1.1 sign-off record
  `.syzygy/governance/decisions/POLARIS-DOSSIER-LOCAL-AGENT-MODE-SIGNOFF-v1.1.md`.
- SEC-3 and D9 as adopted (`.syzygy/governance/doctrine/security.md`;
  `.syzygy/governance/decisions/DOCTRINE-AMENDMENT-LOG.md`, row D9), for
  whether a waiting session could carry the execution permission.
- `.syzygy/governance/contracts/candidates/policy-candidates/NORMATIVE-CHANGE-WORKFLOW.md`
  and `SEMANTIC-DELTA-TEMPLATE.md`; CC-SPEC-1 to CC-SPEC-11 and CC-IMPACT-1
  to CC-IMPACT-7 in that directory (in force under craft acts 6 and 7; the
  path still says candidate); CC-REV-1 and CC-REV-2.
- Doctrine VIS-1, VIS-2, VIS-3, VIS-4.
- `AGENTS.md`, "Hard prohibitions" (in particular "No unattended agent
  coordination") and "Verification rules".

You may read the implementation on the same branch
(`packages/polaris-dossier/src/waiting-sessions.ts`, `session-handover.ts`,
`render.ts`, `cli.ts` and `waiting-sessions.test.ts`) as evidence that the
text can be met. It is not the subject, and the specification must stand
without it.

The reviewer does not receive the drafting conversation, the drafter's
messages to the lead, or any signal of a desired verdict.

## Acceptance criteria

Each is a yes/no question with the evidence that settles it.

1. **Does the change do what the direction authorizes, and nothing more?**
   Each hunk maps to the direction's items 1, 2 or 4, or is a version or
   status line. A hunk that lets Syzygy or the authoring session start,
   resume or signal a session, admits a headless or subagent session, or
   widens a read, egress, write or execution, is blocking.
2. **Is the mitigation stated as the direction takes it?** Compare the
   pre-approval sentence with the option the owner selected ("with only read
   tools plus their one syzygy command pre-approved") and with item 4. Does
   the pre-approval admit any write, and is the hand-over (the session passes
   its inventory or verdict to the command; Syzygy writes the role's own file
   in the session's directory, and only there) a write by the session in
   another form, or within the owner's words? Is "where the agent tool offers
   no rules that narrow, Syzygy SHALL print no pre-approval and SHALL say so"
   right for Codex?
3. **Is the continuing reviewer disclosed as the owner required?** Is the
   disclosure required for every counted verdict, on the review page, with
   the anchoring cost stated? Is detecting continuity by delivered rounds
   or a repeated declared identifier enough, and is its absence correctly
   kept Inferred?
4. **Does any existing rule of 035 change in effect?** In particular: the
   rule that a revision retires the verdicts bound to it; the
   session-identifier rule; the launch-form rule; the packet's contents.
   Does a continuing reviewer's re-declared identifier collide with any of
   them?
5. **Is every Observed claim something Syzygy can observe?** Especially
   the delivery, the re-hash and the pre-approval: what Syzygy observes is
   what it wrote and the bytes it re-hashed; that the session read them, and
   that the agent tool honoured the printed rules, must be Inferred.
6. **Is the wait bounded and local as written?** "a bounded time, never past
   the run's declared deadline"; "reads only the local file system and makes
   no network request". Is either open to an unbounded or networked reading?
7. **Can each new scenario be falsified as written?** One WHEN/THEN pair, an
   independent oracle, a falsifier arm a wrong implementation would trip.
8. **Is the change class right?** The delta says Normative.
9. **Is the impact ledger reproducible?** Re-run its sweep predicate at
   the commit it names and compare every row; re-compute the digests and
   counts; re-run its scratch-tree checks and compare.
10. **Is the owner packet fair and plain?** Does it state the question with
    its options and costs, disclose the tooling prerequisite and the
    unattended-reading risk the owner accepted with option B, and steer no
    further than a labelled recommendation?
11. **Does `design.md` stay design?** No implementation code in
    `openspec/**`.

## Output

A raw review stored verbatim; the lead retains it as
`docs/reviews/R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-V1-2-<n>-RAW.md`. Its first
four non-blank lines are exactly

```text
# Review R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-V1-2-<n>
Reviewed commit: <40-hex commit the reviewer read>
Manifest SHA-256: <sha256 of openspec/changes/polaris-dossier-local-agent-mode/specs/polaris-generation/spec.md after applying proposed/spec.md.patch to that commit, computed by script>
Verdict: <CONFIRM | CONFIRM WITH EXCEPTIONS | REVISE>
```

with no blank line among them. This package has no manifest; the line
carries the v1.2 subject's digest, which the recorder reads as information.

Then `## Findings`, each numbered continuously as
`**Finding N — title** (blocking|revise|note)`, with the evidence, and say
for each whether it concerns the patches or the package prose. For
`CONFIRM WITH EXCEPTIONS` every finding must be a `note`.
