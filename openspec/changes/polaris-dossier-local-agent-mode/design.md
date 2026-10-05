# Design: the operator-agent mode and the `syzygy dossier` commands

> **Candidate — binds nothing.** Explains the candidate requirements in
> `proposed/polaris-generation/spec.md`; not adopted, and not an
> implementation. It contains no code. The command surface below is a design
> for implementation after the owner's sign-off (direction item 5); the
> requirements are the controlling text, and doctrine, accepted contracts and
> the adopted requirements remain controlling over both.

**The agent writes; Syzygy pins, checks, packages the review and renders.**
Every step Syzygy takes is a local command over the run directory and the
clone's Git objects. Syzygy holds no model credential and opens no network
connection; the agent session does all the model work under the operator's
own account.

## The loop

```text
operator: syzygy dossier init  ──► run dir: run.json (pinned revision, limits, declared tool)
agent:    syzygy dossier brief ──► brief.md + draft schema
agent:    explores the clone (read-only; no build or run), asks the operator ≤ N questions
agent:    writes draft ─► syzygy dossier check ─► findings ─► repair ─► check …   (≤ repair limit)
operator: new session ─► syzygy dossier inventory-brief ─► inventory ─► inventory-check
syzygy:   dossier review-packet --kind fidelity  ──► packet + digest
operator: new session ─► review from packet only ─► verdict ─► syzygy dossier review-check
syzygy:   dossier render ──► site/ (editorial-draft pages, disclosures, source pages)
operator: new session ─► review-packet --kind design ─► verdict ─► review-check
operator: syzygy dossier close --usage … ──► record.json (operator-declared usage)
```

## Decisions in this change

1. **Pin by commit, read by object.** `init` resolves the clone's HEAD to a
   commit, refuses unless the in-force observation consent names that exact
   revision, and records it. Every later read is `git cat-file` by object
   identifier at that commit (the batch reader `readGitBlobsBatch` in
   `apps/three-surface-poc/src/git-blob-batch.ts`, and a `git ls-tree -r -z`
   listing at the commit for path existence). The working tree is never read,
   so an edit the agent makes in the clone, accidental or not, cannot reach a
   check, a quotation or a source page. Reading HEAD is a ref read, not a body
   read.
2. **The agent cannot label its own claim Observed.** "An LLM assertion is
   Inferred" (AGENTS.md); the only Observed things on the page are quotations
   Syzygy verified and Syzygy's own reads and steps. This keeps RFC7-2's three
   kinds intact: a claim is anchored through its verified quotation,
   non-normative, or labelled Inferred or Unknown.
3. **Rendered quotations come from Syzygy's read, never the agent's text.**
   The check locates the agent's quotation in the cited blob after the
   existing normalisation, records the byte range, and the renderer slices the
   blob at that range. The agent's copy is used only to find the span.
4. **What Syzygy can enforce, it enforces; what it cannot, it labels.**
   Repair cycles, the deadline (on Syzygy's clock, from `brief`) and the
   question count are Syzygy's own steps or checkable from the draft, so they
   are refused past the limit. The agent's tokens and turns are invisible to
   Syzygy, so they are operator-declared at `close` and labelled Inferred, or
   recorded as not recorded. Nothing is presented as a provider receipt.
5. **Independence is packaged, not proved.** Syzygy builds each review packet
   itself and binds the verdict to the packet digest, so what the reviewer
   was given is Observed. Whether the reviewer had nothing else is not
   observable, so session freshness stays Inferred and the page says so.
   Separate top-level sessions are the default; a different agent tool for
   review (a Codex review of a Claude Code draft, or the reverse) is allowed
   and recorded.
6. **Excluded files make blocks Unknown, not findings.** A quotation from a
   file that screening excludes cannot be verified without using excluded
   content, so the block renders `excluded-content` (RFC2-24 #7) and no
   finding carries the bytes. Re-pointing the claim at a readable file is the
   agent's choice, not a requirement.
7. **No new Unknown reason.** RFC2-24's twelve are closed. Unobserved agent
   usage is "a fact of the render", stated in the disclosure, never a reason
   code and never zero.

## Command surface

One binary, `syzygy`, with a `dossier` command family. Every command is
non-interactive, takes the run directory as its first argument after `init`,
prints a human summary and, with `--json`, the same content as one JSON
document. Exit status: 0 clean, 1 findings or refusal (reason printed), 2
usage error.

| Command | Who runs it | Does | Built from (existing code) | New |
|---|---|---|---|---|
| `syzygy dossier init <clone> --url <repo-url> --config <run.json> [--out <run-dir>]` | the operator, in their own shell | Reads the observation consent, registry entry and policy acts; verifies HEAD is a consented revision; checks the config's declared tool, provider and limits; writes `run.json` | consent reader of PR #263 (`packages/polaris-generation-consent`: `inForceRecords`, `createConsentPorts`, `withConsent`; open, not on main); `evaluateBodyReadAuthority` (`packages/three-surface-poc-core/src/body-read-authority.ts`); `parseGithubUrl` (`dossier-trigger.ts`) | HEAD-to-consent comparison (the trigger's `pinRevision` reads `ls-remote`, not a local clone); config validation |
| `syzygy dossier brief <run>` | agent | Writes `brief.md` and `draft.schema.json`; starts the deadline clock | `promptForStage(stage, 'dossier')` (`prompts.ts`); `OWNER_TOPICS` (`dossier-evaluation.ts`); `DOSSIER_READER_QUESTIONS` (`dossier-profile.ts`) | the local-agent schema (claims cite path + line range, not `sourceIds`); brief text for labels, quotation and clarification rules |
| `syzygy dossier check <run> [--draft <file>]` | agent | Freezes the draft as revision N; runs schema, path, range, quotation and label checks; writes `<run>/checks/rev-N.json`; refuses past the repair limit or deadline | `checkBlockQuotes` / `inspectBlockQuotes` / `normaliseForQuote` (`quote-fidelity.ts`); `validateStage` / `validateDraftRecord` (`provider-draft.ts`); `readGitBlobsBatch`; screening from `public-source-screening.ts` and `classifySource` / `detectSecrets` / `scanActiveContent` | line-range restriction; a normalisation offset map so a normalised match yields a byte range; per-path citations; label rules; cycle counting |
| `syzygy dossier inventory-brief <run>` / `inventory-check <run> --inventory <file>` | inventory session | Brief without the draft; checks and freezes the inventory like a draft | as `brief` / `check`; `ProviderInventory` types | inventory schema with path + line-range citations |
| `syzygy dossier review-packet <run> --kind fidelity\|design` | operator or review session | Builds the packet (frozen subject, frozen inventory, cited spans as Syzygy read them, criteria, verdict schema) and prints its digest | `ProviderReview` shape (`inventoryCoverage`, `blockSupport`, `findings`) | packet assembly and digest; the design packet holds the rendered pages |
| `syzygy dossier review-check <run> --verdict <file>` | review session | Validates schema, packet digest, completeness, quotations, consistency and session-identifier distinctness; records the verdict as counted or refused | `reviewVerdict` (`provider-draft.ts`) | digest binding; session-identifier rule; subject list from 006 |
| `syzygy dossier render <run> [--out <dir>]` | agent or operator | Renders the multi-page site from the latest checked revision; source pages only for screened blobs Syzygy read; disclosure block on every page | `renderDossier` / `writeDossierRun` (`apps/three-surface-poc/src/polaris-generation/dossier-render.ts`, `dossier-render-main.ts`); `sourceRoute` | an adapter from the local draft to the renderer's input (today a `PipelineResult`); RFC7-10 anchors from object id, byte range and revision; the disclosure block; the two discovery populations |
| `syzygy dossier evaluate <run>` | operator | Optional measurement of the rendered dossier | `evaluateDossier`, `resolveQuote` (`dossier-evaluation.ts`); `poc:dossier-evaluation` | none beyond wiring |
| `syzygy dossier close <run> [--usage-tokens N] [--usage-turns N]` | the operator | Records operator-declared usage and closes the run record | — | the record |
| `syzygy dossier status <run>` | anyone | Prints the run's state, limits spent, open findings and reviews still required | — | — |

The existing `poc:dossier` command (`dossier-main.js`) stays as the provider
mode's entry point and stays parked; the new family does not call its
`runPipeline` port.

### The run configuration

`run.json` as the operator writes it before `init`: `operator`, `agentTool`
(`claude-code` or `codex`), `agentToolVersion`, `agentProvider`,
`deadline` (ISO-8601 duration), `agentTokenBudget` and/or `agentTurnBudget`,
`maxRepairCycles`, `maxQuestions`, `audience`. Every value is recorded as
operator-declared. A missing or non-positive limit refuses `init`; there is no
default (INTERFACES.md: "There is no implicit unlimited value or
agent-selected spending default.").

### The run directory

Outside the clone, so nothing Syzygy writes touches the clone's working tree:
`run.json`, `brief.md`, `draft.schema.json`, `<run>/drafts/rev-N.json`,
`<run>/checks/rev-N.json`, `inventory/`, `reviews/<kind>-packet-<digest>/`,
`reviews/<kind>-verdict-N.json`, `site/`, `record.json`. The Execution Record
(REQ-polaris-generation-018) is `record.json`; it carries no prompt or
transcript body.

### The local-agent draft schema

The existing `ProviderDraft` (title, introduction, sections, diagrams,
deepDives, unresolved) with three changes: each paragraph cites
`{path, startLine, endLine}` instead of `sourceIds`; each block carries
`label` (`inferred` | `unknown` | `non-normative`) and, for `unknown`, a
`reason` from RFC2-24; and two new top-level sections, `discovery`
(inspected, selected, excluded, deferred, stoppingReason) and
`clarifications` (question, evidence, consequence, options, answer, answerKind,
attribution). Quotations keep the existing lead-in form
(`QUOTE_LEAD_IN`), and each names its citation.

## What remains open in the implementation

These are implementation questions, not owner rulings. Each is Unknown until
built and measured.

- **Byte ranges from a normalised match.** `normaliseForQuote` is lossy, so the
  check must carry an index map from normalised to raw offsets. Whether the
  rendered span is the exact raw range or widened to whole lines is a
  rendering choice; the requirement asks only that it be Syzygy's own bytes.
- **Session identifiers.** [Unknown] whether Claude Code and Codex expose a
  stable session identifier to the session itself. If not, the operator
  supplies one per session in the verdict; either way it is operator-declared.
- **Where the run record lives.** REQ-polaris-generation-018 puts the
  Execution Record in its "governing work home". For an observed public
  repository the run directory is the candidate home; whether a work item
  must be materialized (REQ-polaris-generation-020) for a local run is
  decided in implementation planning against 020's text, which is not
  displaced here.
- **The non-governed profile.** A Redis dossier also needs requirement 032 for
  its composition. This change works with or without it; the renderer applies
  032 only where it is adopted and applies.

## Agent-harness instructions (proposed text, not installed)

These drive the loop. They are prose for the operator's tools, not code, and
are installed only after sign-off. Neither text grants anything: the
requirements and Syzygy's checks decide what counts.

### Claude Code skill, `polaris-dossier`

```markdown
---
name: polaris-dossier
description: Write a Polaris dossier for a locally cloned repository with the syzygy binary. Use when the operator asks for a dossier of a repository they have cloned and run `syzygy dossier init` on. Roles - author, inventory, review.
---

# Polaris dossier

You write; `syzygy dossier` pins, checks and renders. Its output, not yours,
decides what is verified. Arguments: `<role> <run-dir>`; role is `author`,
`inventory` or `review`.

Always:
- Never run `syzygy dossier init` or edit `run.json`. If the run directory
  has no `run.json`, ask the operator to run init in their own shell and stop.
- Read the clone; never build, install, test or run anything in it.
- Never edit the clone. Write only inside the run directory.
- Label your claims `inferred`, `unknown` (with a reason from the brief) or
  `non-normative`. Never `observed`.

author:
1. `syzygy dossier brief <run>`; read `brief.md` and `draft.schema.json`.
2. Explore the clone for the five reader topics. Keep a list of what you
   inspected and selected, and why you left material out; it goes in
   `discovery`.
3. Ask the operator the consequential questions, at most the brief's limit,
   with AskUserQuestion; record each in `clarifications` with the operator's
   exact answer.
4. Write `<run>/drafts/next.json`; run `syzygy dossier check <run>`. Repair every
   finding and re-run, until it is clean or Syzygy refuses the next cycle.
   Never work around a refusal.
5. Stop. Tell the operator to start a new session for the inventory. Do not
   write the inventory or a review yourself.

inventory (a new session that has not seen the draft):
1. `syzygy dossier inventory-brief <run>`. Do not open `drafts/` or `checks/`.
2. Write `<run>/inventory/next.json`; run `syzygy dossier inventory-check` until
   clean.

review (a new session):
1. `syzygy dossier review-packet <run> --kind <fidelity|design>`. Read only
   the packet directory it names. Do not open the clone, `drafts/` history,
   or any other file.
2. Write the verdict to the schema, naming the packet digest and your
   session identifier; run `syzygy dossier review-check <run> --verdict <file>`.

Report Syzygy's output verbatim. Do not summarise a refusal as success.
```

### Codex instructions (an `AGENTS.md` placed in the run directory)

```markdown
# Polaris dossier run

This directory is a `syzygy dossier` run. Launch Codex with this directory as
the working directory and the clone readable. Your role is named by the
operator when the session starts: author, inventory or review.

- `run.json` is the operator's. Do not create or edit it, and do not run
  `syzygy dossier init`.
- Read the clone only. Never build, install, test or run its code, and never
  edit it.
- Claims are `inferred`, `unknown` with a brief-listed reason, or
  `non-normative`; never `observed`.
- author: `syzygy dossier brief .`, explore, ask the operator at most the
  brief's question limit and record answers verbatim, write
  `<run>/drafts/next.json`, then `syzygy dossier check .` and repair until clean or
  refused. Then stop.
- inventory (fresh session, has not seen the draft): `syzygy dossier
  inventory-brief .`, write `<run>/inventory/next.json`, `syzygy dossier
  inventory-check .` until clean. Never open `drafts/`.
- review (fresh session): `syzygy dossier review-packet . --kind <kind>`, read
  only the packet, write the verdict with the packet digest and your session
  identifier, `syzygy dossier review-check . --verdict <file>`.
- Quote Syzygy's output exactly; a refusal is a refusal.
```

Recommended operator setting for either tool (owner question O3): deny the
shell except `syzygy dossier` commands, so the agent reads the clone with its
file tools only. [Inferred] Claude Code's permission rules and Codex's
sandbox modes can express this; the exact settings are confirmed at
implementation. Syzygy cannot observe which setting was in force, so the run
record carries it as operator-declared.

[Inferred] Codex reads `AGENTS.md` from its working directory; the exact
launch flags that make the clone readable from a different working directory
are confirmed at implementation, not here.
