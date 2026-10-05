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
the work-item gates, where records live, the producer understanding, review
independence, the discovery account, who answers clarifications, and how the
draft layer's consent condition reads. It edits no adopted file,
grants no read, egress, write or execution to Syzygy, and leaves the provider
mode parked, not withdrawn.

## What the package changes, in plain terms

- **Pinning.** `syzygy dossier init` checks that the clone's HEAD is a
  revision your observation consent names, records it, and from then on
  Syzygy reads only Git objects at that commit, never the working tree. It
  ignores replacement objects, grafts, the clone's own configuration, hooks
  and alternates, and re-hashes every commit, tree and blob it reads, because
  the agent can write the clone's `.git` directory; a mismatch refuses.
- **The agent writes, Syzygy checks.** Syzygy issues a brief (your five reader
  topics, an understanding record, the labelling, citation, quotation and
  execution rules, the schema). Every quotation must be one contiguous span of
  a cited file; Syzygy verifies it against the blob and, at render, locates it
  again, so the page shows Syzygy's bytes, not the agent's or a stored range.
  The agent cannot mark its own claims Observed. Findings go back to the agent
  until clean or until the repair limit you declared.
- **Running the project.** Not invited yet. Until you adopt the SEC-3
  amendment your review-1 ruling directs, the brief quotes SEC-3 and does not
  invite building or running the project outside an execution profile. Once
  that amendment is in force, the brief may say the agent may build and run
  it. Either way, anything the agent marks as resting on execution is
  Inferred, the commands it reports are listed, and Syzygy runs nothing.
- **Governed projects.** Allowed with a per-project statement naming your
  agent's provider; the statement is a consent record. Every page says that
  neither its content classes nor secret screening (SEC-5) limit what the
  agent reads or sends. "Governed" uses the same four conditions as the
  sibling profile change (032).
- **Review.** Separate top-level sessions that you start, in a new terminal,
  write the inventory and the reviews, from packets Syzygy builds. Syzygy
  proves what each was given; it cannot prove a session saw nothing else, or
  that the inventory is complete, and the page says so.
- **Limits and usage.** You declare the deadline, the agent's token or turn
  budget, the repair and question limits (zero allowed for the last two), and
  the model. Syzygy enforces the ones that bind its own steps. The agent's
  usage is your declared figure, labelled Inferred, never Observed or zero.
- **Syzygy's own records.** Kept outside the clone, but on your machine the
  agent can still write them. Syzygy re-derives every quotation, check and
  review binding at render instead of trusting them, and labels what it
  cannot re-derive Inferred. Question R1 below asks whether you accept that.
- **Disclosure.** Every page states the mode, your declared tool, version,
  provider and model, that the agent read the clone without restriction and
  unscreened, that its read account is self-reported, the execution rule and
  what it reported running, that Syzygy made no provider call and verified
  every quotation, and that its own records' integrity is Inferred.

## Your rulings, as applied

Eight rulings over three records apply. None is put to you again:

- `.syzygy/governance/decisions/POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-DIRECTION.md`
  (`POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-2026-10-05`)
- `.syzygy/governance/decisions/POLARIS-DOSSIER-LOCAL-AGENT-SCOPE-REVIEW-SIGNOFF-DIRECTION.md`
  (`POLARIS-DOSSIER-LOCAL-AGENT-SCOPE-REVIEW-SIGNOFF-2026-10-05`)
- `.syzygy/governance/decisions/POLARIS-DOSSIER-LOCAL-AGENT-REVIEW-1-RULINGS-DIRECTION.md`
  (`POLARIS-DOSSIER-LOCAL-AGENT-REVIEW-1-RULINGS-2026-10-05`)

| # | Question | Your choice | Where it is applied | Trade-off kept visible |
|---|---|---|---|---|
| O1 | RFC7-20 and a draft your own session computed | "Rule it by interpretation" (rulings record, item 1), over the recommended per-project provider record; kept as "Keep my ruling" after review 1 (review-1 record, item 3) | 033: an operator-computed draft is admitted with disclosure, the declared and recorded tool and provider, and byte-verified quotes; otherwise the draft layer is Unknown | Review 1, finding 6, found the reading changes the clause's effect; preserved for you below, not resolved |
| O2 | Which repositories | "Any repo" (scope record, item 1); kept as "Keep any repo, disclose" after review 1 (review-1 record, item 2), over "Public repos for now" | 033: any repository; a governed or silent subject needs an in-force per-project statement, which is a consent record; the spec states that neither its classes nor SEC-5 screening bind the agent's own reads and sends; "governed" uses 032's four conditions | Review 1, finding 7: the class limit is unenforceable and SEC-5 material may reach the provider; you expected SEC-2 "scoped" and SEC-5 to be raised again |
| O3 | Code execution by the agent | "Allow, disclose" (rulings record, item 2); then "Allow on host, amend SEC-3" (review-1 record, item 1), over "Only in a sandbox" and "Forbid, disclose" | 033 and 034: the brief invites execution only while an owner-adopted SEC-3 amendment permits it, and quotes SEC-3 until then; claims marked as resting on execution are Inferred and name their commands; Syzygy executes nothing | This change may not be signed until you adopt that SEC-3 amendment; it is not drafted yet |
| O4 | Review independence | "Separate session" (scope record, item 2) | 035: a separate top-level session you start; no subagent or process of the authoring session; declared session ids must differ, for the inventory as well as the reviews. The fidelity packet also carries the frozen inventory | Extending the rule to the inventory and rendered-design review is the drafter's choice, stricter than your words. Freshness and inventory completeness stay Inferred |
| O5 | Sign-off form | "Option pick, v1.0" (scope record, item 3) | The sign-off below | The extension of version-tag sign-off to generator deltas takes effect only when you make the selection |

## Question R1: where Syzygy's own records live

The first review (finding 2) found that the adopted text requires an
Execution Record that is "immutable, identified, integrity-verifiable" in its
governing work home (REQ-polaris-generation-018) and an audit trail "outside
the governed plane and untrusted actor write reach; work records or a
same-user writable directory SHALL NOT substitute" (REQ-polaris-generation-022).
On a single-user machine, where your agent runs as you and may run the
project, no directory Syzygy writes is out of the agent's reach. 033 reads
both sentences for this mode, and reads REQ-polaris-generation-020's
work-item gates as not applying to a run with no provider dispatch or
scheduler effect. Those are security-posture readings, so they are yours.

| Option | What it means | Cost |
|---|---|---|
| **A. Accept, re-derive and disclose (recommended)** | As 033 is drafted: records in Syzygy's state directory outside the clone; nothing Observed rests on a stored record; every quotation, check and review binding is re-derived from verified Git objects at render; the repair count, earlier instants and record history are labelled Inferred | An agent could rewind the repair count or the deadline start, and the page would show those as Inferred, not catch it |
| B. Separate operating-system user | Syzygy's state directory belongs to a user the agent does not run as | Setup on every operator machine; meets 022's text |
| C. Sandbox the agent | The agent runs where it cannot write Syzygy's state | You declined a sandbox under O3 |

Recommendation: A, because every Observed label on the page is re-derived
from bytes Syzygy verifies at render, and what the agent could still alter is
labelled Inferred rather than defended. If you pick B or C, 033 changes
before the confirming review.

## Sign-off, and what goes with it

Sign-off waits for two things: your adoption of the SEC-3 amendment (O3), and
a confirming fresh-context review (CONFIRM, or CONFIRM WITH EXCEPTIONS with
notes only). Then you will be offered one option selection:

> Sign off `polaris-dossier-local-agent-mode` v1.0, and extend version-tag
> sign-off (`OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`) to
> Polaris generator specification deltas.

The first review's findings 6 (RFC7-20), 7 (SEC-2 and SEC-5) and 8 (SEC-3)
were reported for you, and neither the drafter nor the lead resolves them.
They go to you with the sign-off offering, and the sign-off is taken with
them in view.

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

Fresh-context review before the offering, per `REVIEW-BRIEF.md`. Round 1
returned REVISE over `f1bd0b5c`; `REVIEW-BRIEF.md` carries the disposition of
its 21 findings. The next round is the lead's to dispatch.
