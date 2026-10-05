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
  the agent can write the clone's `.git` directory; a mismatch refuses. At
  every later step it checks again that the recorded revision is one your
  consent names, and the draft, inventory and packets must name it too.
- **The agent writes, Syzygy checks.** Syzygy issues a brief (your five reader
  topics, an understanding record, the labelling, citation, quotation and
  execution rules, the schema). Every quotation must be one contiguous span of
  a cited file; Syzygy verifies it against the blob and, at render, locates it
  again, so the page shows Syzygy's bytes, not the agent's or a stored range.
  The agent cannot mark its own claims Observed. Findings go back to the agent
  until clean or until the repair limit you declared.
- **Running the project.** Not invited yet. The SEC-3 amendment your
  review-1 ruling directs is drafted as D9 and under review. The brief may
  say the agent may build and run the project only when D9 is in force, you
  are the operator, attending sessions you started on your own machine, and
  you recorded your choice to allow it before the brief. Otherwise the brief
  quotes SEC-3 and invites nothing outside an execution profile. Either way,
  anything the agent marks as resting on execution is Inferred, shown with
  the commands it names, and Syzygy runs and launches nothing.
- **Governed projects.** Allowed with a per-project statement naming your
  agent's provider; the statement is a consent record. Every page says that
  neither its content classes nor secret screening (SEC-5) limit what the
  agent reads or sends. "Governed" uses the same four conditions as the
  sibling profile change (032).
- **Review.** Separate top-level sessions that you start write the inventory
  and the reviews, from packets Syzygy builds. You start each one in a new
  terminal, or by typing `!` and the printed command in the authoring
  session's terminal; the second form is the lead's reading of your words
  (O4 below). Syzygy proves which packet it built and that the verdict names
  its digest; it cannot prove the reviewer read that packet unaltered, saw
  nothing else, or that the inventory is complete, and the page says so.
- **Limits and usage.** You declare the deadline, the agent's token or turn
  budget, the repair and question limits (zero allowed for the last two), and
  the model. Syzygy enforces the ones that bind its own steps. The agent's
  usage is your declared figure, labelled Inferred, never Observed or zero.
- **Syzygy's own records.** Kept outside the clone, but on your machine the
  agent can still write them. As you ruled (R1), Syzygy re-derives every
  quotation, check and review binding at each check and render instead of
  trusting them, and labels every value it shows from a stored record
  Inferred.
- **Disclosure.** Every page states the mode, your declared tool, version,
  provider and model, that the agent read the clone without restriction and
  unscreened, that its read account is self-reported, the execution rule and
  what it reported running, that Syzygy made no provider call and verified
  every quotation, and that every value shown from its stored records is
  Inferred.

## Your rulings, as applied

Nine rulings over four records apply. None is put to you again:

- `.syzygy/governance/decisions/POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-DIRECTION.md`
  (`POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-2026-10-05`)
- `.syzygy/governance/decisions/POLARIS-DOSSIER-LOCAL-AGENT-SCOPE-REVIEW-SIGNOFF-DIRECTION.md`
  (`POLARIS-DOSSIER-LOCAL-AGENT-SCOPE-REVIEW-SIGNOFF-2026-10-05`)
- `.syzygy/governance/decisions/POLARIS-DOSSIER-LOCAL-AGENT-REVIEW-1-RULINGS-DIRECTION.md`
  (`POLARIS-DOSSIER-LOCAL-AGENT-REVIEW-1-RULINGS-2026-10-05`)
- `.syzygy/governance/decisions/POLARIS-DOSSIER-LOCAL-AGENT-RECORDS-DIRECTION.md`
  (`POLARIS-DOSSIER-LOCAL-AGENT-RECORDS-2026-10-05`)

| # | Question | Your choice | Where it is applied | Trade-off kept visible |
|---|---|---|---|---|
| O1 | RFC7-20 and a draft your own session computed | "Rule it by interpretation" (rulings record, item 1), over the recommended per-project provider record; kept as "Keep my ruling" after review 1 (review-1 record, item 3) | 033: an operator-computed draft is admitted with disclosure, the declared and recorded tool and provider, and byte-verified quotes; otherwise the draft layer is Unknown | Review 1, finding 6, and review 2, finding 7, found the reading changes the clause's effect; review 2 adds that it now does work only for non-governed subjects. Preserved for you below, not resolved |
| O2 | Which repositories | "Any repo" (scope record, item 1); kept as "Keep any repo, disclose" after review 1 (review-1 record, item 2), over "Public repos for now" | 033: any repository; a governed or silent subject needs an in-force per-project statement, which is a consent record; the spec states that neither its classes nor SEC-5 screening bind the agent's own reads and sends; "governed" uses 032's four conditions | Review 1, finding 7: the class limit is unenforceable and SEC-5 material may reach the provider; you expected SEC-2 "scoped" and SEC-5 to be raised again. Review 2, finding 8, locates it in one sentence of 033, named below; your sign-off decides it |
| O3 | Code execution by the agent | "Allow, disclose" (rulings record, item 2); then "Allow on host, amend SEC-3" (review-1 record, item 1), over "Only in a sandbox" and "Forbid, disclose" | 033 and 034: the brief invites execution only while D9 is in force, you are the attending operator, and your choice is recorded first; it quotes SEC-3 otherwise; claims marked as resting on execution are Inferred and shown with their commands; Syzygy executes and launches nothing | This change may not be signed until you adopt D9 (draft PR #357, under review); 033 and 034 follow its adopted text |
| O4 | Review independence | "Separate session" (scope record, item 2) | 035: a separate top-level session you start, in a new terminal or with `!`; no subagent, and no headless session the authoring agent starts and reads; declared session ids must differ, for the inventory as well as the reviews; the launch form is recorded as you declare it. The fidelity packet also carries the frozen inventory | Admitting `!` is the lead's reading of your words "A second top-level Claude Code/Codex session you start", not your ruling. Facts: the printed command is headless (`claude -p` or `codex exec`); launched with `!` it runs as a child of the authoring tool's shell, inherits its environment, and its whole output lands in the authoring agent's context. The only difference from the excluded headless launch is who typed it, which Syzygy cannot observe. Your sign-off covers this reading. Extending the rule to the inventory and rendered-design review is the drafter's choice, stricter than your words. Freshness and inventory completeness stay Inferred |
| O5 | Sign-off form | "Option pick, v1.0" (scope record, item 3) | The sign-off below | The extension of version-tag sign-off to generator deltas takes effect only when you make the selection |
| R1 | Where Syzygy's own records live | "Re-derive, label Inferred (Recommended)" (records record), over "Separate OS user" and "Sandbox the agent" | 033: no Observed label rests on a stored record; quotations, checks and review bindings re-derived at each check and render; every value shown from a stored record labelled Inferred; no separate user or sandbox | Review 2, finding 5: the question did not cover the 020 reading, and the option's costs were understated; both carried to the sign-off below |

## Sign-off, and what goes with it

Two things remain open, and only two: your adoption of the SEC-3 amendment
drafted as D9 (O3), and the v1.0 sign-off itself. Sign-off follows D9's
adoption and a confirming fresh-context review (CONFIRM, or CONFIRM WITH
EXCEPTIONS with notes only). Then you will be offered one option selection:

> Sign off `polaris-dossier-local-agent-mode` v1.0, and extend version-tag
> sign-off (`OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`) to
> Polaris generator specification deltas.

These findings were reported for you, and neither the drafter nor the lead
resolves them. They go to you with the sign-off offering, and the sign-off is
taken with them in view:

- **RFC7-20** (review 1, finding 6; review 2, finding 7): the reading
  changes the clause's effect; under 033 as written it does work only for
  non-governed subjects.
- **SEC-2 "scoped" and SEC-5** (review 1, finding 7; review 2, finding 8,
  first part): your sign-off decides 033's sentence "The statement is a
  consent record: it is the "explicit, recorded, per-project consent" that
  SEC-2 requires before governed-project content reaches a model provider",
  while SEC-2's head reads "explicit, scoped consent" and nothing enforces
  the statement's class limit.
- **SEC-3** (review 1, finding 8): answered by D9, which you adopt or not
  before signing.
- **The 020 reading and option A's full cost** (review 2, finding 5): 033
  reads REQ-polaris-generation-020's Proposal, approval, scheduler-creation
  and materialization gates as not applying to a run with no provider
  dispatch or scheduler effect. R1 did not ask about that. Option A also
  means that the audit evidence of admissions, denials and refusals that
  REQ-polaris-generation-022 asks for is agent-editable (a refusal can be
  erased), and that the pinned revision and the emitted review packets are
  stored records, so which revision a run used is Inferred; the consent
  check on it, and the packet bindings, are re-done at each step.
- **The `!` launch form** (review 2, finding 4): the lead's reading, as O4
  states.

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
returned REVISE over `f1bd0b5c` (21 findings) and round 2 REVISE over
`af97611d` (17 findings); `REVIEW-BRIEF.md` carries both dispositions. Round
3 is the confirming round, dispatched after D9's text is fixed by its own
review. CONFIRM, or CONFIRM WITH EXCEPTIONS with notes only, clears the
bytes; a third REVISE comes to you with all three raws.
