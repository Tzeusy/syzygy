# Owner decision packet — Polaris dossier local-agent mode

> **Candidate — binds nothing.** Drafted 2026-10-05 under the owner direction
> `POLARIS-DOSSIER-LOCAL-AGENT-MODE-2026-10-05`. It performs no act and
> carries no digest. Effect comes only from the owner's sign-off of the exact
> reviewed bytes, after a confirming review. A commit, a review or a merged
> pull request performs no act.

## What this is, in one paragraph

You directed that Polaris dossiers be written by your own Claude Code or Codex
session over a local clone, with Syzygy supplying the brief, the checks, a
fresh-context review step and the renderer, and making no provider call. This
package adds requirements 033 to 036 to the generator specification so that
the mode is specified, and says exactly which adopted sentences it replaces
for such a run: budgets, provider receipts, the registered provider route,
review independence, the discovery account, who answers clarifications, and
how the draft layer's consent condition reads. It edits no adopted file,
grants no read, egress, write or execution to Syzygy, and leaves the provider
mode parked, not withdrawn.

## What the package changes, in plain terms

- **Pinning.** `syzygy dossier init` checks that the clone's HEAD is a
  revision your observation consent names, records it, and from then on
  Syzygy reads only Git objects at that commit, never the working tree.
- **The agent writes, Syzygy checks.** Syzygy issues a brief (your five reader
  topics, the labelling, quotation and execution rules, the schema). Every
  quotation must be one contiguous span of a cited file; Syzygy verifies it
  against the blob, and the page shows Syzygy's bytes, not the agent's. The
  agent cannot mark its own claims Observed. Findings go back to the agent
  until clean or until the repair limit you declared.
- **Running the project.** The agent may build and run it; anything it
  concludes from that is Inferred, and the commands it reports are listed.
  Syzygy runs nothing.
- **Review.** Separate top-level sessions that you start write the inventory
  and the reviews, from packets Syzygy builds. Syzygy proves what each was
  given; it cannot prove a session saw nothing else, and the page says so.
- **Limits and usage.** You declare the deadline, the agent's token or turn
  budget, the repair and question limits. Syzygy enforces the ones that bind
  its own steps. The agent's usage is your declared figure, labelled Inferred,
  never Observed or zero.
- **Disclosure.** Every page states the mode, your declared tool, version and
  provider, that the agent read the clone without restriction, that its read
  account is self-reported, what it reported running, and that Syzygy made no
  provider call.

## Your rulings, as applied

All five questions the draft raised are ruled. Each is applied in the
specification; none is put to you again. The records:

- `.syzygy/governance/decisions/POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-DIRECTION.md`
  (`POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-2026-10-05`)
- `.syzygy/governance/decisions/POLARIS-DOSSIER-LOCAL-AGENT-SCOPE-REVIEW-SIGNOFF-DIRECTION.md`
  (`POLARIS-DOSSIER-LOCAL-AGENT-SCOPE-REVIEW-SIGNOFF-2026-10-05`)

| # | Question | Your choice | Where it is applied | Trade-off kept visible |
|---|---|---|---|---|
| O1 | RFC7-20 and a draft your own session computed | "Rule it by interpretation" (rulings record, item 1), over the recommended per-project provider record | 033: an operator-computed draft is admitted with disclosure, the declared and recorded tool and provider, and byte-verified quotes; otherwise the draft layer is Unknown | You chose it knowing "a reviewer may call it a contract change". The review is asked to say whether it is one and report it to you; the package neither concedes nor rebuts it |
| O2 | Which repositories | "Any repo" (scope record, item 1), over the recommended observed-only restriction | 033: any repository; for a governed project, or one whose input is silent, `init` refuses unless an in-force per-project statement names your agent's provider and content classes (SEC-2's "explicit, recorded, per-project consent"); an observed, non-governed repository needs no record | The reconciliation with SEC-2 is the amendment's reading, not yours; the review is asked whether it reaches doctrine and to report, not resolve, that |
| O3 | Code execution by the agent | "Allow, disclose" (rulings record, item 2), over the recommended "Forbid, disclose" | 033 and 034: the brief allows building and running the project; such claims are Inferred and name their commands; the run record lists the reported commands; Syzygy executes nothing (SEC-3) | Claims may rest on behaviour Syzygy cannot observe or reproduce; they stay Inferred |
| O4 | Review independence | "Separate session" (scope record, item 2) | 035: a separate top-level session you start, declared session id different from the author's; a subagent of the authoring session does not count. The fidelity packet also carries the frozen inventory, because REQ-polaris-generation-006 measures coverage against it | Whether a session was top-level, fresh and operator-started stays Inferred |
| O5 | Sign-off form | "Option pick, v1.0" (scope record, item 3) | The sign-off below | The extension of version-tag sign-off to generator deltas takes effect only when you make the selection |

## The one remaining question: sign-off

After a confirming fresh-context review (CONFIRM, or CONFIRM WITH EXCEPTIONS
with notes only), you will be offered one option selection:

> Sign off `polaris-dossier-local-agent-mode` v1.0, and extend version-tag
> sign-off (`OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`) to
> Polaris generator specification deltas.

The selection binds a git tag, `polaris-dossier-local-agent-mode-v1.0`, on the
commit that carries the package bytes you were shown, which must equal the
bytes the confirming review read. The record is written by
`scripts/record_versioned_signoff.py` once this package has the builder that
recorder requires: it moves `proposed/polaris-generation/spec.md` to `specs/`
and generalizes the effective-scenario recount. That builder is post-sign-off
work (`tasks.md`), and the profile change (032) can reuse it. Implementation
of the `syzygy dossier` commands waits for this sign-off (mode direction,
item 5).

## What it does not do

It grants Syzygy no read, egress, write, execution or release. It admits no
repository, creates no per-project statement, withdraws no act, deletes no
parked package, and amends no doctrine, accepted contract or adopted byte. It
binds nothing until reviewed and signed off.

## Review

Fresh-context review before the offering, per `REVIEW-BRIEF.md`. No round has
run.
