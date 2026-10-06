# Redis dossier runbook (local-agent mode, S12)

**Candidate. Binds nothing.** This page is operating guidance for
`syzygy-qkea.13` (S12): two attended end-to-end dossier runs against Redis,
one in Claude Code and one in Codex. It performs no act, records no consent
and is never authority. The owner, as operator, starts and attends every
session. No agent starts one, and this page never lists an agent doing so.
Every state claim below is dated 2026-10-07. Re-read `PROJECT-STATUS.md` and
the act records before relying on any of them.

## Can the flow run before the sitting? No

[Observed] The production command reads its gate records from one place only:
the Syzygy checkout it runs from. In
`packages/polaris-dossier/src/cli.ts`, `RECORDS_ROOT` is the checkout root,
and there is no environment variable or flag that overrides it. The only seam
that injects other records is `CliPorts.sources`, and only tests use it. A
"scratch governance root" would therefore have to be a copy of Syzygy with
owner-act records written into it. Recorder-produced records in that copy
would claim acts the owner never performed (VIS-4), so no rehearsal is built
that way.

The end-to-end path is already exercised under injected fixture sources, by
`packages/polaris-dossier/src/full-run.testkit.ts` and the tests that use it.
A separate fixture repository would add nothing the binary could use, because
the binary cannot read fixture records. S12 therefore runs once, after the
sitting, against Redis itself.

## What must be true first

Each item is checked by the command named, never by reading a status word.

**Owner acts.** The rows of the dossier sitting packet are listed in
`.syzygy/governance/contracts/candidates/dossier-local-agent-acts/OWNER-SITTING-PACKET.md`.

| Needed for | Act | Packet |
|---|---|---|
| Both runs | Redis observation consent | dossier packet, row 1 (the earlier Redis packet's row 5, the same record) |
| Both runs | The source-acquisition entry, local-agent version, signed by tag v1.0 | dossier packet, row 2 |
| Both runs | The "no evidence drawer" statement, or the provider statement for that run's tool | dossier packet, row 3, 3a or 3b |
| Both runs, for a dossier with prose | The RFC7-20 reading in force | dossier packet, row 5 |
| Both runs | The classification policy and the public-source screening scope | [Inferred, as the dossier packet says] the earlier Redis sitting, row 1 (`docs/polaris-generation/REDIS-SITTING-RUNBOOK.md`); preflight is the check |
| Run B only | D9 in force | dossier packet, row 4 |

**Code.** S10 (`close`, PR 388) is on `main`. As of 2026-10-07 these are not:

- S11, the skill and the Codex instructions (PR 389).
- S10b, `syzygy-bur3`: each command's working directory and scope, flagged by `check`, `render` and `close`.
- `syzygy-qkea.21` (PR 377), which wires the G5 records into the gates. [Observed] Until it lands:
  - the registry gate reads the act over the parked provider-mode entry, which names another implementation, so it refuses;
  - the drawer and statement sources state nothing, so Redis counts as governed and the brief refuses;
  - `D9_ACT_FORM` and `RFC7_20_RULING_ACT_FORM` are `null`.
- Run B only: `PERMITTING_ARM_ENABLED` in `packages/polaris-dossier/src/execution-rule.ts` is `false`, and while it is false no brief permits execution. Switching it on is its own reviewed change, after `syzygy-qkea.21`.

**Check before each run.**

```
git -C <syzygy checkout> status --short
npm --prefix <syzygy checkout> ci
npm --prefix <syzygy checkout> run build
node <syzygy checkout>/apps/syzygy/dist/main.js dossier preflight https://github.com/redis/redis
```

The tree must be clean and on the commit you will record. Preflight must name
every start gate as in force and list the consented revisions. If it names any
gate as absent or refused, stop. Do not work around it.

Below, `syzygy` stands for `node <syzygy checkout>/apps/syzygy/dist/main.js`.

## The two runs

| | Run A | Run B |
|---|---|---|
| Tool | Claude Code | Codex |
| Execution | not permitted (the brief carries SEC-3's rule) | permitted for this run only, through `allow-execution` |
| Extra preconditions | none | dossier packet row 4, `PERMITTING_ARM_ENABLED`, a credential list |

Run them one after the other, each with its own clone and its own run
directory. A choice recorded for run A never carries to run B.

### 1. Make the clone (operator)

Use one of the revisions preflight names. Fetch that commit alone, as the
consent's stated form says:

```
git init <clones>/redis-<revision>
git -C <clones>/redis-<revision> fetch --depth=1 https://github.com/redis/redis <revision>
git -C <clones>/redis-<revision> checkout --detach FETCH_HEAD
```

Keep the clone outside the Syzygy checkout and outside the state root.

### 2. Start the authoring session (operator)

Start the session in the Syzygy checkout, so that its project skill loads.
Never start it in the clone.

- Run A: `claude`, then ask: generate me a Polaris dossier for https://github.com/redis/redis
- Run B: `codex`, with the same request.

[Inferred] The session can then write files in the checkout, the gate records
included. Every step re-checks those records and its report says so
(`RECORDS_WITHIN_REACH`), but nothing prevents the writes.

From here on, the skill drives the session. The steps below are what the
operator sees and does. Each command is printed by the session or typed by
the operator, as the step says.

### 3. Configure and init (session, with the operator's answers)

The session asks for the deadline, a token or turn budget, the repair-cycle
limit, the question limit and the model. It writes them as a run
configuration file with these fields:

- `operator`
- `agentTool` (`claude-code` or `codex`)
- `agentToolVersion`, `agentProvider`, `model` and optionally `modelVersion`
- `deadline`, as an ISO 8601 duration such as `PT3H`
- `agentTokenBudget` and/or `agentTurnBudget`
- `maxRepairCycles`, `maxQuestions`, `audience` and `operatorIsOwner`

[Inferred] Give a generous deadline. It runs on Syzygy's clock from `brief`,
and it must also cover the inventory, both reviews, `render` and `close`.

```
syzygy dossier init <clones>/redis-<revision> --url https://github.com/redis/redis --config <run.json> --state-root <state root>
```

### 4. Run B only: record the execution choice (operator, personally)

Type this in a new terminal, or after `!`. Never let the session type it.

```
syzygy dossier allow-execution <run> --revision <revision> --declare owner-started-session,owners-own-host,owner-attends
```

For every Run B step from `brief` through `close`, set
`SYZYGY_DOSSIER_CREDENTIAL_LIST` in the session's environment. It names a
`syzygy-adapter-credential-list/1` file listing every credential the host's
Syzygy adapters hold. An empty list must be declared explicitly.

### 5. Brief, draft, check (session)

```
syzygy dossier brief <run>
syzygy dossier check <run>
```

The session repairs and re-checks until `check` is clean or refuses. Read
`brief.md`'s execution rule:

- Run A: it must say the project is not to be built or run.
- Run B: it must state the permitting rule, and each command the session reports must name its working directory and scope.

### 6. Hand-overs (the operator starts every session)

Each hand-over has three parts, in this order.

1. The session prints the hand-over:
   - the inventory: `syzygy dossier session-prompt <run> inventory`;
   - the fidelity review: `syzygy dossier session-prompt <run> review --kind fidelity`;
   - the design review, after `syzygy dossier render <run>`: `syzygy dossier session-prompt <run> review --kind design`.
2. The operator starts the printed command in a new terminal, or with the `!` form, and attends that session until it finishes.
3. The operator records the launch form:
   - `syzygy dossier launch-form <run> inventory terminal|bang`;
   - `syzygy dossier launch-form <run> review terminal|bang --kind fidelity|design`.

A blocking finding sends the run back to step 5, and a new draft revision
retires the reviews.

### 7. Close before the deadline (session, with the operator's figures)

```
syzygy dossier close <run> --usage-tokens <n> --usage-turns <n>
syzygy dossier status <run>
```

Give only the figures the tool shows, or neither flag. Never give 0. After the
deadline, `close` refuses and the run gets no Execution Record.

## Evidence record (one per run)

Build it once the run is closed:

```
node <syzygy checkout>/scripts/dossier_run_evidence.mjs <run> > <syzygy checkout>/docs/evidence/polaris-dossier-s12-<tool>-<date>.json
```

`scripts/dossier_run_evidence.mjs` reads only three things: the run
directory, the `<run id>.sessions` directory beside it, and the checkout's Git
state. It copies no file body. Every digest is computed (rule 3), and the
record names its subject and the subject's digests (rule 11):

| Field | What it holds |
|---|---|
| `measuredOn` | the Syzygy commit, and whether the tracked tree was clean |
| `subject` | run id, repository, pinned revision, governed predicate; Inferred, because it is read from `run.json` |
| `declared` | the operator's run configuration, Inferred |
| `executionRule` | the rule `brief.json` issued |
| `outcome` | site revisions; the sha256 of the latest `machine.json` and of `record.json`; the agent usage and the credential check at close |
| `runDirectory`, `sessionsDirectory` | every regular file as path, size and sha256; symbolic links are listed and not followed |
| `operatorDeclared` | filled in by hand, null where unknown: owner attendance, launch forms, the tool version and usage shown. Inferred |

Before committing, check three things:

- `measuredOn.syzygyTrackedTreeClean` is `true`.
- `outcome.closed` is `true`.
- For run B, `executionRule` is the permitting arm. For run A, it is not.

A record that fails any of these is still kept, with a note saying why. It is
never edited into a pass.

## Known limits

- [Observed] Every gate record lies within the sessions' write reach. The
  record proves what the run directory held at the instant the script ran,
  and nothing about earlier instants.
- [Inferred] Redis has neither an `openspec/` nor a `.syzygy/` path at the
  consented revisions. This comes from general knowledge: nothing has been
  read to check it, because no read is authorised yet. If either path exists,
  `init` reports Redis as governed and the run needs row 3a or 3b.
- [Unknown] Whether the deadline, budgets and resource limits suit a
  repository of Redis's size. No run has measured them.
