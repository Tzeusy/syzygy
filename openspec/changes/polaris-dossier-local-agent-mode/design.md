# Design: the operator-agent mode and the `syzygy dossier` commands

> **Candidate — binds nothing.** Explains the candidate requirements in
> `proposed/polaris-generation/spec.md`; not adopted, and not an
> implementation. It contains no code. The command surface below is a design
> for implementation after the owner's sign-off (direction item 5); the
> requirements are the controlling text, and doctrine, accepted contracts,
> the adopted requirements and the owner's rulings
> (`POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-2026-10-05`,
> `POLARIS-DOSSIER-LOCAL-AGENT-REVIEW-1-RULINGS-2026-10-05`) remain
> controlling over both.

**The agent writes; Syzygy pins, checks, packages the review and renders.**
Every step Syzygy takes is a local command over its state directory for the
run and the clone's Git objects. Syzygy holds no model credential and opens no network
connection; the agent sessions do all the model work under the operator's
own account. The owner has confirmed this tooling is the end goal, so the
design aims at the whole path from one sentence typed by the operator to a
rendered site.

## The full loop, from one line to a site

The operator types one line in Claude Code or Codex, for example
`/polaris-dossier https://github.com/redis/redis` (Claude Code) or "write a
Polaris dossier of https://github.com/redis/redis" (Codex, with the
instructions below installed). Everything after that is driven by the skill
and Syzygy's commands, with the operator answering at most three kinds of
question in-session: the run's limits, the consequential clarifications, and
the usage figure at the end.

```text
 1 agent:    syzygy dossier preflight <url>        consent, registry, policy acts; consented revisions;
                                                   for a governed project, the per-project provider statement
             └─ missing ─► stop: name the record the owner must make (Syzygy creates none)
 2 agent:    git clone <url> <dir>; git checkout <consented revision>     the operator's session fetches; Syzygy fetches nothing
 3 operator: answers one structured question: deadline, token or turn budget, repair and question limits
 4 agent:    syzygy dossier init <dir> --url <url> --config <answers>   ─► state dir, pinned revision
 5 agent:    syzygy dossier brief <run>
 6 agent:    explores the clone under the brief's execution rule, listing every command it reports running
 7 agent:    asks the operator ≤ maxQuestions consequential questions; records answers verbatim
 8 agent:    writes understanding, then draft ─► syzygy dossier check ─► findings ─► repair ─► …   (≤ maxRepairCycles)
 9 operator: starts a fresh inventory session with the command `session-prompt <run> inventory` prints
10 operator: starts a fresh fidelity-review session (`session-prompt <run> review --kind fidelity`)
11 agent:    syzygy dossier render <run>
12 operator: starts a fresh design-review session (`session-prompt <run> review --kind design`)
             └─ a blocking finding ─► back to 8 (a new revision retires the reviews)
13 operator: declares the agents' usage; agent runs syzygy dossier close <run> --usage …
14 agent:    reports the site path, `syzygy dossier status <run>` verbatim, and what is still Unknown
```

At steps 9, 10 and 12 the authoring session stops and hands over: it runs
`syzygy dossier session-prompt`, which prints the fixed prompt and a
ready-to-paste command (`claude -p "<prompt>"` or `codex exec "<prompt>"`,
with the run's state directory as working directory). The **operator**
opens a new terminal and starts that session there with the exact prompt
printed, so it is a separate top-level session the operator starts and the
authoring session never writes the reviewer's instructions (owner direction
`POLARIS-DOSSIER-LOCAL-AGENT-SCOPE-REVIEW-SIGNOFF-2026-10-05`, item 2). A
subagent of the authoring session does not count. When the session finishes,
the operator returns to the authoring session, which resumes at the next
step. The loop is therefore attended at each hand-over, and no agent
coordinates another.

One other launch form counts: the operator may type the printed command
behind Claude Code's `!` shell-escape prefix in the authoring session's
terminal. The operator types it and the prompt is Syzygy's, so it is a
session the operator starts (035); its output returns to the authoring
session's context, which harms nothing in the review. A headless session
that the authoring agent starts and reads is not offered: it is not a
session the operator starts, and it brushes against "No unattended agent
coordination" (first review, finding 9; the lead's ruling). The operator
declares the launch form, `terminal` or `bang`, with each session's
identifier; Syzygy records it as operator-declared and refuses any other.

At step 3 the skill may offer presets, but the operator selects or types the
values; Syzygy records them as operator-declared, conveyed by the agent
session. Syzygy chooses no default (REQ-polaris-generation-033).

## Decisions in this change

1. **Pin by commit, read by object, re-hash every object.** `init` resolves
   the clone's HEAD to a commit, refuses unless the in-force observation
   consent names that exact revision, and records it. Every later read is by
   object identifier at that commit (the batch reader `readGitBlobsBatch` in
   `apps/three-surface-poc/src/git-blob-batch.ts`, and a tree listing at the
   commit for path existence). The working tree is never read. The clone's
   `.git` directory is also the agent's to write, and the first review showed
   that `git replace`, or an overwritten loose object, returns other bytes
   under the consented identifier without error. So the reader honours no
   replacement objects, grafts, repository-local configuration, hooks or
   alternates, and recomputes the identifier of every commit, tree and blob
   on the path down from the pinned commit from the bytes it got; a mismatch
   refuses the step. Two routes meet that, and the choice is implementation
   [Unknown]: `git` with the flags and environment of
   `apps/three-surface-poc/src/polaris-generation/isolated-git.ts`
   (`--no-replace-objects`, `GIT_NO_REPLACE_OBJECTS=1`, no system or global
   configuration, hooks to `/dev/null`, no fsmonitor) plus an in-process
   re-hash and a refusal of any clone that declares alternates; or an
   in-process object reader that consults none of the clone's configuration
   at all. The first still reads the clone's own `.git/config`, so it needs
   an allowlist check of that file before any `git` call; the second does
   not. The walk goes down from the commit and never to its parents, so
   grafts and shallow boundaries cannot change what is read. Reading HEAD
   is a ref read, not a body read.
2. **The agent cannot label its own claim Observed.** "An LLM assertion is
   Inferred" (AGENTS.md); the only Observed things on the page are quotations
   Syzygy verified and Syzygy's own reads and steps. This keeps RFC7-2's three
   kinds intact: a claim is anchored through its verified quotation,
   non-normative, or labelled Inferred or Unknown.
3. **Rendered quotations come from Syzygy's read, never the agent's text.**
   The check locates the agent's quotation in the cited blob after the
   existing normalisation and records the byte range for the finding report;
   `render` locates the quotation again in the blob it re-reads and
   re-hashes, and slices that. The stored range is never trusted, because the
   agent can write the state directory. The agent's copy is used only to find
   the span.
4. **What Syzygy can enforce, it enforces; what it cannot, it labels.**
   Repair cycles, the deadline (on Syzygy's clock, from `brief`) and the
   question count are Syzygy's own steps or checkable from the draft, so they
   are refused past the limit. The cycle count and the deadline's start
   instant are stored where the agent can write them, so their integrity is
   labelled Inferred. The agent's tokens and turns are invisible to Syzygy,
   so they are operator-declared at `close` and labelled Inferred, or
   recorded as not recorded. Nothing is presented as a provider receipt.
5. **Independence is packaged, not proved.** Syzygy builds each review packet
   itself and binds the verdict to the packet digest, rebuilding the packet
   from the frozen subject at `review-check` and again at `render`, so what
   the reviewer was given is Observed. Whether the reviewer had nothing else is not
   observable, so session freshness stays Inferred and the page says so.
   Each inventory and review runs in a separate top-level session that the
   operator starts, with a declared session identifier that must differ from
   the author's, and for a review from the inventory's; a subagent or a
   process of the authoring session does not count (owner ruling; the
   extension to the inventory is the drafter's). The reviewer verifies each
   inventory entry's accuracy against the spans in its packet; it has no
   way to verify the inventory's completeness, so that stays the inventory
   session's self-report, Inferred. A different agent tool for review (a Codex review of a Claude
   Code draft, or the reverse) is allowed and recorded. The fidelity packet
   carries the frozen inventory as part of its criteria, because
   REQ-polaris-generation-006 measures coverage against it.
6. **Excluded files make blocks Unknown, not findings.** A quotation from a
   file that screening excludes cannot be verified without using excluded
   content, so the block renders `excluded-content` (RFC2-24 #7) and no
   finding carries the bytes. Re-pointing the claim at a readable file is the
   agent's choice, not a requirement.
7. **No new Unknown reason.** RFC2-24's twelve are closed. Unobserved agent
   usage is "a fact of the render", stated in the disclosure, never a reason
   code and never zero.
8. **Execution follows SEC-3; Syzygy never runs anything.** The owner
   chose to let the agent build and run the observed project on the host,
   and directed a SEC-3 amendment to permit it before this change is signed
   (review-1 rulings, item 1). `brief` writes the execution rule in force:
   until that amendment is adopted, SEC-3's own rule, quoted, with no
   invitation to run the project outside an execution profile; after, the
   amendment's permission. Either way each command the agent reports goes in
   the draft's `executions` list, and each claim it marks as resting on one
   names it and is Inferred. Syzygy sees only the marking, records the list
   as the agent's report and runs nothing. A verified quotation is still the
   only Observed content on the page.
9. **The RFC7-20 reading is applied narrowly.** The draft layer renders as an
   editorial draft only when the three conditions of the owner's reading hold
   (disclosure, declared and recorded tool and provider, byte-verified
   quotations); `render` checks all three and otherwise renders the draft
   layer Unknown (`unconsented-source-or-provider`). The run record cites
   the ruling. The owner knew a reviewer may call the reading a contract
   change; the design takes no position on that.
10. **Any repository, with SEC-2 kept whole.** The owner allowed the mode on
    any repository, governed projects included, and left SEC-2 unchanged
    (scope record, item 1; review-1 rulings, item 2). A subject is governed
    under the four conditions the sibling profile change (032) uses: a
    kernel evidence drawer recorded in the project input, or an
    `openspec/**` specification, an adopted capability declaration or
    declared topology among the source classes of the pinned tree, which
    `preflight` reads by path only. A governed subject, or one whose input is
    silent about the drawer, needs an in-force per-project statement naming
    the operator's agent provider and content classes, which `preflight`
    reports and `init` requires. The statement is a consent record, not an
    egress record. Every page says that neither its classes nor SEC-5
    screening limit what the agent reads or sends.
11. **Syzygy's records are re-derived, not trusted.** The state directory
    lies outside the clone, but on a single-user host the agent, and any
    project code it runs, can write it. So nothing Observed rests on a stored
    file: `check` and `render` re-read and re-hash the objects, re-locate the
    quotations, re-run the checks and rebuild the packets; what cannot be
    re-derived carries an Inferred integrity label. No Syzygy credential is
    issued for a run or written where the agent can read it. This reads
    REQ-polaris-generation-018's work home and 022's trail location for this
    mode, and is owner question R1 in the packet, with a separate
    operating-system user and a sandbox as the alternatives.

## Command surface

One binary, `syzygy`, with a `dossier` command family. Every command is
non-interactive, takes the run's state directory as its first argument after `init`,
prints a human summary and, with `--json`, the same content as one JSON
document. Exit status: 0 clean, 1 findings or refusal (reason printed), 2
usage error.

| Command | Who runs it | Does | Built from (existing code) | New |
|---|---|---|---|---|
| `syzygy dossier preflight <url>` | agent | Reports whether observation consent, the observer registry entry and the classification and screening policy acts are in force for the repository, which revisions the consent names, and whether a per-project statement names the operator's agent provider; prints the clone and checkout commands; refuses with the missing record named | consent reader (`packages/polaris-generation-consent`, on `main` since PR #263); `evaluateBodyReadAuthority`; `parseGithubUrl` | the report; no network access (the URL is parsed, not fetched) |
| `syzygy dossier session-prompt <run> <inventory\|review> [--kind fidelity\|design]` | agent, at a hand-over | Prints the fixed prompt for a fresh session and a ready command for the operator to start it, and records the prompt's digest, so the authoring session does not write it | — | the prompt texts |
| `syzygy dossier init <clone> --url <repo-url> --config <run.json> [--out <run-dir>]` | agent, on the operator's answer (or the operator, in the strict form) | Reads the observation consent, registry entry and policy acts; verifies HEAD is a consented revision; decides governed or not from the project input and the pinned tree's paths, and for a governed or silent subject requires the per-project statement; checks the config's declared tool, provider, model and limits; writes `run.json` in the state directory | consent reader (`packages/polaris-generation-consent`: `inForceRecords`, `createConsentPorts`, `withConsent`; on `main` since PR #263); `evaluateBodyReadAuthority` (`packages/three-surface-poc-core/src/body-read-authority.ts`); `parseGithubUrl` (`dossier-trigger.ts`) | HEAD-to-consent comparison (the trigger's `pinRevision` reads `ls-remote`, not a local clone); isolated, re-hashing object reads; the governed predicate; config validation |
| `syzygy dossier brief <run>` | agent | Writes `brief.md` and `draft.schema.json`, with the execution rule in force; starts the deadline clock | `promptForStage(stage, 'dossier')` (`prompts.ts`); `OWNER_TOPICS` (`dossier-evaluation.ts`); `DOSSIER_READER_QUESTIONS` (`dossier-profile.ts`) | the local-agent schema (claims cite path + line range, not `sourceIds`); brief text for labels, quotation and clarification rules |
| `syzygy dossier check <run> [--draft <file>]` | agent | Freezes the draft as revision N; runs schema, path, range, quotation and label checks; writes `<run>/checks/rev-N.json`; refuses past the repair limit or deadline | `checkBlockQuotes` / `inspectBlockQuotes` / `normaliseForQuote` (`quote-fidelity.ts`); `validateStage` / `validateDraftRecord` (`provider-draft.ts`); `readGitBlobsBatch`; screening from `public-source-screening.ts` and `classifySource` / `detectSecrets` / `scanActiveContent` | line-range restriction; a normalisation offset map so a normalised match yields a byte range; per-path citations; label and citation rules by block kind; the understanding record; cycle counting |
| `syzygy dossier inventory-brief <run>` / `inventory-check <run> --inventory <file>` | inventory session | Brief without the draft; checks and freezes the inventory like a draft; refuses an inventory declared under the authoring session's identifier | as `brief` / `check`; `ProviderInventory` types | inventory schema with path + line-range citations |
| `syzygy dossier review-packet <run> --kind fidelity\|design` | operator or review session | Builds the packet (frozen subject, frozen inventory, cited spans as Syzygy read them, criteria, verdict schema) and prints its digest | `ProviderReview` shape (`inventoryCoverage`, `blockSupport`, `findings`) | packet assembly and digest; the design packet holds the rendered pages |
| `syzygy dossier review-check <run> --verdict <file>` | review session | Rebuilds the packet and validates schema, packet digest, completeness, entry accuracy, quotations, consistency, session-identifier distinctness and the declared launch form; records the verdict as counted or refused | `reviewVerdict` (`provider-draft.ts`) | digest binding; session-identifier rule; subject list from 006 |
| `syzygy dossier render <run> [--out <dir>]` | agent or operator | Re-reads and re-hashes every object, re-locates every quotation, re-runs the checks and rebuilds the review packets, then renders the multi-page site from the latest checked revision; source pages only for screened blobs Syzygy read and verified; disclosure block on every page, including the reported commands and the Inferred integrity of stored records; draft layer only when the three conditions of the owner's RFC7-20 reading hold | `renderDossier` / `writeDossierRun` (`apps/three-surface-poc/src/polaris-generation/dossier-render.ts`, `dossier-render-main.ts`); `sourceRoute` | an adapter from the local draft to the renderer's input (today a `PipelineResult`); RFC7-10 anchors of class evidence artifact identifier with integrity digest, from the recomputed object id, byte range and revision; the disclosure block; the two discovery populations |
| `syzygy dossier evaluate <run>` | operator | Optional measurement of the rendered dossier | `evaluateDossier`, `resolveQuote` (`dossier-evaluation.ts`); `poc:dossier-evaluation` | none beyond wiring |
| `syzygy dossier close <run> [--usage-tokens N] [--usage-turns N]` | agent, on the operator's answer | Records operator-declared usage and closes the run record | — | the record |
| `syzygy dossier status <run>` | anyone | Prints the run's state, limits spent, open findings and reviews still required | — | — |

The existing `poc:dossier` command (`dossier-main.js`) stays as the provider
mode's entry point and stays parked; the new family does not call its
`runPipeline` port.

### The run configuration

`run.json`, from the operator's answers at step 3: `operator`, `agentTool`
(`claude-code` or `codex`), `agentToolVersion`, `agentProvider`, `model`,
`modelVersion` (where the tool shows one), `deadline` (ISO-8601 duration,
positive), `agentTokenBudget` and/or `agentTurnBudget` (positive),
`maxRepairCycles` and `maxQuestions` (nonnegative integers, 0 allowed),
`audience`. Every value is recorded as operator-declared and Inferred; the
record states that no provider-reported model version exists in this mode.
A missing, unlimited, negative or non-integer limit, or a zero deadline or
budget, refuses `init`; there is no default (INTERFACES.md: "There is no implicit unlimited value or
agent-selected spending default.").

### The state directory

Syzygy's own directory for the run, outside the clone, so nothing Syzygy
writes touches the clone's working tree, and never a location derived from
the clone's path: `run.json`, `brief.md`, `draft.schema.json`,
`<run>/drafts/rev-N.json`, `<run>/checks/rev-N.json`, `inventory/`,
`reviews/<kind>-packet-<digest>/`, `reviews/<kind>-verdict-N.json`, `site/`,
`record.json`. The Execution Record (REQ-polaris-generation-018) is
`record.json`; it carries no prompt or transcript body. The agent sessions
write their drafts, inventory and verdicts here, and on a single-user host
they can write every other file too; decision 11 says how Syzygy stays
honest about that.

### The local-agent draft schema

The existing `ProviderDraft` (title, introduction, sections, diagrams,
deepDives, unresolved) with three changes: each paragraph cites
`{path, startLine, endLine}` instead of `sourceIds`; each block carries
`label` (`inferred` | `unknown` | `non-normative`) and, for `unknown`, a
`reason` from RFC2-24; an `inferred` block cites at least one source, an
`unknown` block cites what it considered or nothing, and a `non-normative`
block cites nothing. Four new top-level sections: `understanding` (purpose,
beneficiary, proposition, capabilities, components, choices, tradeOffs,
limits, terminology, contradictions, openQuestions, each item with
citations, scope and label, or `unknown` with a reason), `discovery`
(inspected, selected, excluded, deferred, stoppingReason), `clarifications`
(question, evidence, consequence, options, answer, answerKind, attribution),
and `executions` (each command the agent reports having run, with its
working directory and purpose). A claim the agent marks as resting on
execution carries `basis: execution` and the identifiers of the executions
it rests on. Quotations keep the existing lead-in form (`QUOTE_LEAD_IN`),
and each names its citation.

## What remains open in the implementation

These are implementation questions, not owner rulings. Each is Unknown until
built and measured.

- **Byte ranges from a normalised match.** `normaliseForQuote` is lossy, so the
  check must carry an index map from normalised to raw offsets. Whether the
  rendered span is the exact raw range or widened to whole lines is a
  rendering choice; the requirement asks only that it be Syzygy's own bytes.
- **Session identifiers.** [Unknown] whether Claude Code and Codex expose a
  stable session identifier to the session itself, and whether `claude -p`
  and `codex exec` report one the verdict can carry. If not, the operator
  supplies one per session; either way it is operator-declared.
- **Which object reader.** The two routes of decision 1; either meets 033.
- **The non-governed profile.** A Redis dossier also needs requirement 032 for
  its composition. This change works with or without it; the renderer applies
  032 only where it is adopted and applies.
- **The consent precondition.** `preflight` can only report consent records
  that exist. Making one for a public repository is the owner's act under
  the observation-consent route that the direction keeps (item 4); this
  design does not make it.

## Agent-harness instructions (proposed text, not installed)

These drive the loop. They are prose for the operator's tools, not code, and
are installed only after sign-off. Neither text grants anything: the
requirements and Syzygy's checks decide what counts.

### Claude Code skill, `polaris-dossier`

```markdown
---
name: polaris-dossier
description: Write a Polaris dossier (a multi-page explanatory site) for a public repository with the syzygy binary. Use when the operator asks for a Polaris dossier of a repository URL, or invokes /polaris-dossier <url>. Also used, with a role, by the fresh inventory and review sessions the loop launches.
---

# Polaris dossier

You write; `syzygy dossier` pins, checks and renders. Its output, not yours,
decides what is verified. Quote it exactly; a refusal is a refusal, never a
success to summarise.

Always:
- Write only your drafts, inventory or verdict inside the run's state
  directory, and nothing else of Syzygy's. Syzygy re-checks everything it
  relies on; editing its files only makes the run's record less trustworthy.
- Follow the execution rule in `brief.md`. Unless it says otherwise, do not
  build or run the cloned project outside an explicit, opt-in execution
  profile. Add every command you do run to `executions`; a claim that rests
  on one has `basis: execution`, names it, and is `inferred`.
- Label claims `inferred`, `unknown` (with a reason the brief lists) or
  `non-normative`. Never `observed`.

With a URL (the author, driving the loop):
1. `syzygy dossier preflight <url>`. If it refuses, tell the operator which
   record is missing and stop.
2. Clone and check out a revision the preflight names, with the commands it
   prints, into a directory the operator agrees.
3. Ask the operator, in one AskUserQuestion, for the deadline, a token or
   turn budget, the repair-cycle limit and the question limit. Offer presets;
   never pick for them.
4. `syzygy dossier init <clone> --url <url> --config <answers>`;
   `syzygy dossier brief <run>`; read `brief.md` and `draft.schema.json`.
5. Explore the clone for the five reader topics. Keep `discovery`: what you
   inspected and selected, what you left out and why, and why you stopped.
   Write `understanding` before the argument.
6. Ask the consequential questions, at most the brief's limit, with
   AskUserQuestion; record each with the operator's exact answer.
7. Write `<run>/drafts/next.json`; `syzygy dossier check <run>`; repair every
   finding and re-run until clean or refused.
8. For each of inventory, review --kind fidelity, then (after
   `syzygy dossier render <run>`) review --kind design: run
   `syzygy dossier session-prompt <run> <role> [--kind <kind>]`, show the
   operator the command it prints, and wait. The operator starts that
   session in a new terminal, or by typing `!` followed by the printed
   command here. Never start it yourself, headless or otherwise, and never
   use a subagent for it. Ask the operator which launch form they used and
   pass it to `review-check` or `inventory-check` with the session
   identifier. Resume
   when the operator says it has finished, and run `syzygy dossier status`.
9. On a blocking finding, go back to 7.
10. Ask the operator for the usage figure their tool shows (or none);
    `syzygy dossier close <run> --usage-…`. Report the site path and
    `syzygy dossier status <run>` verbatim.

With a role (a fresh session launched in step 8):
- inventory: `syzygy dossier inventory-brief .`; never open `drafts/` or
  `checks/`; write `<run>/inventory/next.json`; `syzygy dossier
  inventory-check .` until clean.
- review: `syzygy dossier review-packet . --kind <kind>`; read only the
  packet directory it names; write the verdict with the packet digest and
  your session identifier; `syzygy dossier review-check . --verdict <file>`.
```

### Codex instructions (installed as an `AGENTS.md` the operator's Codex reads)

```markdown
# Polaris dossiers

When asked for a Polaris dossier of a repository URL, follow the loop
below with the `syzygy dossier` commands. Their output decides what is
verified; quote it exactly, and treat a refusal as a refusal.

- `syzygy dossier preflight <url>`; stop if it refuses, naming the missing
  record. Clone and check out a revision it names.
- Ask the operator for the deadline, a token or turn budget, the repair and
  question limits; never choose them. `syzygy dossier init`, then
  `syzygy dossier brief`.
- Explore. Follow the execution rule in `brief.md`; unless it says
  otherwise, do not build or run the project outside an explicit, opt-in
  execution profile. Every command you do run goes in `executions`; claims
  resting on one are `inferred` and name it. Never label a claim `observed`.
- Write `understanding` before the argument.
- Ask at most the brief's question limit; record answers verbatim.
- Draft, `syzygy dossier check`, repair until clean or refused.
- For inventory, fidelity review and (after `syzygy dossier render`) design
  review: `syzygy dossier session-prompt <run> <role>`, show the operator the
  command it prints, and wait; the operator starts that session in a new
  terminal. Never start it yourself, headless or otherwise, or delegate it
  to a sub-agent. Record the launch form the operator reports (`terminal`)
  with the session identifier.
- Ask the operator for usage; `syzygy dossier close`; report the site path
  and `syzygy dossier status` verbatim.
- In a session started from a session-prompt, do only what that prompt says.
```

[Inferred] Codex reads `AGENTS.md` from its working directory and its home
configuration, and `codex exec` starts a fresh non-interactive session; the
exact flags are confirmed at implementation, not here. A review in the other
tool (a Codex review of a Claude Code draft) needs only that tool installed
and is recorded as such.
