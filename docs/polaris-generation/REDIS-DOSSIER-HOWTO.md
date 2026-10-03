# How to ask for the Redis dossier

**Candidate. Binds nothing.** It mints no act, grants no read or egress and is
never authority; the acts named in the sitting packet decide what binds. It is
written for someone reading it cold. Every claim carries a label:
**[Observed]** is cited to code on main or to a named PR head,
**[Inferred]** is a reading of that code, and **[Unknown]** has no evidence
yet. Pieces that are not merged are named by PR number and may have moved.
Last refreshed 2026-10-03 against the heads named below; the lead refreshes it
as the PRs land.

## The goal in one line

After the owner's one sitting, this is the whole request:

```
npm run poc:dossier -- https://github.com/redis/redis
```

[Observed, PR 268, branch `agent/dossier-engine-6`] That command exists on that
branch. It is not on main yet. [Observed, same head] It stops by design unless
every admission record exists, and as of that head it also stops after reading
because no real model call is wired (exit 5, below). So "a single action after
the sitting" is the target, not today's state; sections 2 and 4 say what is
still missing. The end-to-end wiring (provider route, records port, screening
and the credential variable) is tracked as bead syzygy-bc0g (P0); this page is
refreshed when it lands.

## 1. What the sitting decides

The owner decides a short list of things, once, before anything is read:
which provider route to use, the screening scope for public repositories, the
read and egress consents for the Redis revision, and a few rulings. The list,
its order, who depends on whom and what each row's PR status is live in the
sitting packet, PR 260 (the file OWNER-SITTING-PACKET.md in the candidates folder redis-dossier-sitting).
This page does not repeat it. Nothing in the rest of this page happens until
the rows that packet marks as blocking have been given.

## 2. What happens mechanically after the sitting

Each act the owner gives is written into the repository by a small recorder
script that checks the exact reviewed bytes, writes a dated record (with the UTC
instant, so the act is in force from that moment) and appends to the
acceptance record. Then one install step makes the code see those records.

- [Observed, on main] Recorders exist for the public-repository consents and
  egress (`scripts/record_public_repo_admission_acts.py`), the registry entries
  (`scripts/record_public_admission_registry_entries_acts.py`), the screening
  scope policy (`scripts/record_public_source_screening_scope_act.py`) and the
  RFC5-14 class (`scripts/record_rfc5_project_documentation_act.py`).
- [Observed, PR 286, `governance/redis-sitting-simulation`] The order of
  operations, the conflicts a dry run found and the install-change steps are in
  REDIS-SITTING-RUNBOOK.md in docs/polaris-generation on that branch.
- [Unknown] the script install_redis_sitting.py, the one-command install after
  the recorders, is being written by the owner of PR 286 and is not on any head
  I read. Until it exists, the install change is made by hand from the runbook.
- [Observed, PR 260 and the policy recorder] The screening-scope act replaces
  the policy file, and the existing Butlers read path then needs a re-pin
  (`governance-inputs.ts` and related). The Redis run does not use that pin; it
  needs the act record itself [Inferred: the screening code that reads the
  policy is being written, bead syzygy-vjqd].
- [Observed, PR 268] The command reads the three admission records through a
  record store that is not wired yet ("no record store is wired into this
  command"). Until it is, the command always reports all three records
  missing, even after the acts are recorded [Unknown: which PR wires it; the
  reader is on branch `agent/dossier-consent`; tracked in syzygy-bc0g].

## 3. What you provide

- **A provider credential.** [Observed, the confirmed bytes and PR 264] Both
  routes are API-key only: there is no sign-in route, and billing is the API
  account. [Inferred] Whichever route wins, you need an API key with access to
  the model the entry pins (`claude-opus-5-5`, effort `high`).
- **Route B (Messages API, PRs 264 and 273).** The proposed variable is
  `SYZYGY_POLARIS_PROVIDER_API_KEY`. [Unknown, tracked in syzygy-bc0g] No code at any head I read
  reads that name: the Messages API adapter on PR 264's branch takes the key as
  a configuration value (`apiKey`), and PR 273's entry labels the variable name
  a proposal. Treat the name as the intended one until the wiring PR lands.
- **If route A (Agent SDK, merged entry in PR 255) wins instead.**
  [Observed, PR 264's branch] The Agent SDK adapter also takes the key as a
  configuration value and sets its own child environment from it. [Unknown, tracked in syzygy-bc0g]
  Which variable you export for route A is not defined in any code I read; the
  entry pins a bundled CLI and a runtime loopback egress gate, so the
  difference you will notice is a different runtime, not a different command.
- **Variables that must not be set.** [Observed, PR 264's branch,
  `messages-api-provider.ts`] The Messages API adapter refuses to be built, and
  refuses to start a call, while any variable whose name starts with
  `ANTHROPIC_` is set, or while the Node TLS or proxy variables it lists
  (for example `NODE_TLS_REJECT_UNAUTHORIZED`, `NODE_EXTRA_CA_CERTS`, the
  `HTTPS_PROXY` family) are set. Unset all of them in the shell you run from.
  [Inferred] The same caution is sensible under route A, whose adapter builds
  its own `ANTHROPIC_*` environment for the CLI.
- **Network.** [Observed, PR 268] The run needs outbound HTTPS to GitHub for
  `git ls-remote` and a shallow fetch of the one pinned commit, and to the
  provider for the model calls. Nothing else.

## 4. The command and its exit codes

```
npm run poc:dossier -- https://github.com/redis/redis [--out <dir>] [--json]
```

[Observed, PR 268, `dossier-main.ts`] It accepts only `https://github.com/<owner>/<repo>`
with an optional `/tree/<ref>`. It resolves the revision with `git ls-remote`
(ref names and commit ids only, no bodies), checks the admission records, and
only then fetches and reads. The exit code is the outcome:

| Exit | Meaning | What to do |
|---|---|---|
| 0 | `complete`: the dossier was rendered | Open it (section 5) |
| 1 | Unexpected failure; the message is on stderr | Keep the output; report it. [Observed: the catch in `dossier-main.ts`] |
| 2 | `invalid-input`: not a supported URL, or wrong arguments | Fix the command. The usage line is printed |
| 3 | `admission-missing`: one or more of the three records (observation consent, screening policy, egress consent) is missing. The report lists each as OK or MISSING with what is needed | Give or record the missing act. No repository body was read and no provider was called |
| 4 | `unresolved-revision`: `git ls-remote` could not pin the revision | Check the network and the URL or tag. Nothing was read |
| 5 | `generation-unavailable`: admission is satisfied, but a piece the run needs is not wired (no checkout, no generate port, or no renderer). The corpus, discovery and clarification record is saved | [Observed at PR 268's head] Today this is the end of the road: no real model call is wired (tracker items G2 and G3; syzygy-bc0g). Wait for the provider PRs; the saved run record shows what was read |
| 6 | `generation-stopped`: the pipeline stopped (budget, deadline, repair exhausted, a provider failure and similar); the reason is in the detail line | Read the reason, then adjust the budget or retry; the run record is saved |

The `--json` flag prints the same outcome as JSON.

## 5. Where the output lands, and how to open it

- [Observed, PR 268] Without `--out`, the run is written under a new
  temporary directory, in a `site` folder (`syzygy-dossier-…/site` under the
  system temp directory). With `--out <dir>` it goes there. The command prints
  `Run directory: <path>` on exit 0, 5 and 6.
- [Observed, PR 269 on main] The renderer refuses a directory inside a Git work
  tree, so use a path outside the repository.
- Open `index.html` in that directory in a browser. [Observed, PR 269,
  `dossier-render.ts`] The files are:
  - `index.html` (the entry): title, introduction and open questions at the
    first reading level, then one section per question, each linking its deep
    dives;
  - `contents.html`, `glossary.html` and `sources/index.html`;
  - `deep-dives/<id>.html`, one per produced deep dive;
  - `sources/<digest>.html`, one per quotable source, with its exact admitted
    text;
  - `dossier.json`, `size-report.json` and `size-report.html` (what a reader
    pays in bytes and words);
  - `run-record.json`: the pinned revision, the records that admitted the run,
    the discovery report and receipts, and any clarification questions it
    recorded instead of asking.
- [Observed, PR 269] Every page carries a banner "Generated dossier draft - not
  reviewed or adopted". It is a local draft, never published.

## 6. Time and budget

- [Observed, PR 268, `dossier-trigger.ts`] The generation budget is at most 7
  model calls, 8,000,000 input bytes, 1,000,000 output bytes, 1,000 usage
  units, 3,600,000 ms (one hour) elapsed and 1 repair cycle.
- [Observed, `discovery.ts` at PR 268's head] Discovery is allowed up to 40 map
  calls plus a reduce, selecting at most the pipeline's quotable cap.
- [Observed, PR 259's `dossier-profile.ts`] The five reader questions are core
  ideas, end-to-end workflows, mechanisms, maintainer-stated advantages and
  trade-offs. The run is zero-interaction: clarification questions (at most 3)
  are recorded in `run-record.json` and not asked.
- [Unknown] Wall-clock time and provider cost for Redis. Nothing has been run
  against a real model, so no measurement exists; the one-hour budget is a
  ceiling, not an estimate. The first run is also the first measurement
  (sitting row 10's page-budget ruling waits on it).

## 7. What can go wrong, and what the page shows

- **A refusal before anything is read.** Exit 3 or 4: nothing was fetched and
  no provider was called.
- **Withheld or excluded content.** [Observed, PR 260 and the screening scope]
  README and LICENSE files stay unsent until the `project-documentation` class
  (row 7) and the further egress version (row 8) exist, so a first Redis run is
  built from code, tree and specification text only. A file that embeds
  markup-like bytes outside a valid inert code context, or any secret-like
  match, is withheld whole [Inferred: the first run measures how many]. A file
  over the size limit is split into pieces or excluded. The sources index says
  "N sources counted, M with admitted text".
- **How Unknown shows.** [Observed, PR 269] A generated sentence is an
  assertion by a language model, so it is marked Inferred when the fidelity
  review judged it supported and Unknown otherwise; open questions and
  unresolved items are marked Unknown; glossary terms are Inferred. Nothing is
  marked Observed except what a diagram record says is. A deep dive that was
  not produced shows a notice in place of a link. [Inferred] A page full of
  Unknown means the evidence was thin or the review did not confirm it, not
  that the repository lacks the thing.
- **A stop mid-run.** Exit 5 or 6 keeps the run record. Re-running starts a new
  run directory.
- **A stale record.** [Observed, PR 268] Each provider call is permitted only
  while the egress record that admitted the run still holds; withdrawing the
  consent stops the next call.

## Where this page may be wrong

It cites heads that move: PR 268 (trigger), 259 (run profile), 264 and 273
(route B), 255 (route A entry), 286 (runbook), 260 (sitting packet), 278
(exclusion reasons) and the screening loader in bead syzygy-vjqd. Rule 7: it is
valid only for the heads it names.
