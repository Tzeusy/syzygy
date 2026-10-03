# Redis dossier run guide

**Candidate. Binds nothing.** It mints no act record, adopts nothing and is
never authority. The sitting packet (PR 260) and the acts it names decide what
binds; [REDIS-SITTING-RUNBOOK.md](REDIS-SITTING-RUNBOOK.md) is the order of
operations for the sitting itself. This page is for after the sitting: what you
do to get the Redis dossier, and what to expect.

Labels: [Observed] was read in code or run; [Inferred] follows from what was
read; [Unknown] was not run or has no evidence. The `poc:dossier` wiring is PR
334, still open. Everything about it was read at its head `d6601785` and none of
it has been run against a real provider; every command that depends on it is
marked [Unknown] until PR 334 merges, and this page must be re-checked then.

**You need an Anthropic API key, whichever route you choose.** Neither route
uses a Claude login or subscription; the run is billed to the API account.

## 1. What must be in force first

`poc:dossier` refuses to start unless these exist as performed owner acts
(sitting packet rows in brackets):

- Screening scope for public sources [row 1]. [Row 12, version 2, is what lets
  the repository's README and guides be read; without it the dossier is built
  from code, tree and specification text only.]
- One provider route [row 2a], and your decision to supply an API key and accept
  API-account billing [row 2b, a direction, not an act].
- The Git-hosting source-acquisition adapter [row 3] and the Redis observation
  consent [row 5].
- Egress consent that lists Redis [row 8; row 6 is the alternative]. Only the
  second egress version authorises the two discovery stages; the first
  authorises the six narrative stages only [Observed in
  `dossier-stage-authority.ts`: an unknown record digest opens no stage].
  What a run does when its discovery calls are refused is [Unknown].
- The RFC5-14 class [row 7] before row 8, and the narrative profile [row 9] if
  you want the page to have a specification basis.

Check that they are installed, before spending anything:

```
python3 scripts/install_redis_sitting.py --check
python3 scripts/check_governance.py
```

[Observed] The first reports what is not installed and changes nothing; it was
rehearsed in the dry run recorded in the runbook. The check that the stage map
in code equals the recorded act arguments does not exist yet [Unknown until it
lands].

The command itself is also a gate. [Observed in code, not run] It checks, in
this order, and stops at the first failure without reading Redis or calling a
provider: the route is an adopted registry entry (exit 5); the revision is
pinned with `git ls-remote`, which fetches ref names and commit ids only (exit
4); the observation, screening and egress records all exist for that repository
and revision (exit 3, naming which is missing). Running it with an unmet
prerequisite is therefore a safe way to see what is missing.

## 2. Route A or route B

Both routes use the same environment variable and neither uses your login.

| | Route A, `agent-sdk` | Route B, `messages-api` |
|---|---|---|
| Credential | `SYZYGY_POLARIS_PROVIDER_API_KEY` (an API key; no subscription login) | the same variable |
| Billing | the API account | the API account |
| What runs | a bundled Agent SDK command-line process, with every tool, setting and memory switched off, behind a local loopback gate | the Anthropic SDK library calling the Messages API directly |
| Fixed bytes beyond the generator's text | the runtime's own (a fixed system prefix, per-run device and session ids, headers naming OS, architecture and Node version) | the entry's listed fixed request, which includes the same three machine-identifying headers |
| Record in the sitting | PR 255 | PR 273 |

[Observed] Sources: the sitting packet's "Row 2 is one choice", the provider
package README and `dossier-generation.ts` at `d6601785`. The earlier idea that
route A would use your login does not hold: the adapter accepts only an API key
(`auth: { apiKey }`, "no subscription login or inherited environment"), and the
command refuses to start without the variable ([Observed] `credential-missing`).

How to choose: the packet makes no recommendation. [Inferred] Route B has one
fewer moving part (no bundled process, fewer fixed bytes you did not write).
Route A's isolation is tested under a network-namespace rig
(`egress-isolation.test.ts`, skipped where `strace` is unavailable). Choose the one whose entry you signed at the sitting; only one can
be in force (RFC4-1), and the command checks that its entry is installed and
matches its act before doing anything.

The key is read once from the environment and removed from it; it is handed to
the adapter and written to no file or log [Observed in `dossier-main.ts`].

## 3. The command

```
export SYZYGY_POLARIS_PROVIDER_API_KEY=...
npm run poc:dossier -- https://github.com/redis/redis/tree/8.10.2 --route agent-sdk --out ~/dossiers/redis-1
```

[Unknown] until PR 334 merges. The real flags at its head are:

- the URL, positional: `https://github.com/<owner>/<repo>` or
  `.../tree/<ref>` (a tag or branch; a bare commit id is refused because
  `ls-remote` cannot confirm it). Without a ref the default branch tip is
  pinned, which no consent names, so the run would stop with exit 3. Use
  `/tree/8.10.2`: [Observed] the Redis observation consent instance
  (`public-repo-admission/instances/redis/OBSERVATION-CONSENT.md`) admits tag
  `8.10.2` as one named full commit id, and `docs/polaris-generation/TARGETS.md`
  pins the same tag. The command pins the tag with `ls-remote` and checks the
  consent against the commit it resolves to; if the tag has moved, the consent
  no longer matches and the run stops with exit 3 before reading anything.
- `--route agent-sdk` or `--route messages-api`. There is no default and no
  `a`/`b` shorthand.
- `--out <dir>`: must not exist and must be outside any Git work tree
  (refused before anything is read, with exit 1). Beside it the run creates `<dir>.state`
  (private, mode 0700) for journals, receipts and the consent audit; that must
  not exist either. Without `--out` a temporary directory is used, which is
  rarely what you want.
- `--json` prints the outcome as JSON.

## 4. What happens, and for how long

[Observed in code, not run.] In order:

1. Pin the revision; check the three records; open the provider session. The
   credential, the gate and the state directory are set up before any
   repository object is fetched.
2. Fetch exactly the pinned commit into a scratch bare repository (shallow, no
   hooks, no execution) and read it through the screening scope.
3. Discovery: a map call per subsystem, each with an excerpt of each file, then
   one reduce and a ranked selection; what does not fit is counted
   `deferred-by-budget`. Excerpts are file bytes only; for C code the
   leading licence comment is skipped and the opening comment and declaration
   lines are shown.
4. Zero-interaction clarification, then five narrative calls: inventory, plan,
   author, edit, fidelity. If fidelity finds unsupported statements, a repair
   and a second fidelity pass follow, up to 3 cycles: at most 11 narrative
   calls.
5. Render the pages and write the run directory.

Budget [Observed in `dossier-run-profile.ts` at `d6601785`; [Inferred] every
figure is a proposal from code caps, unmeasured]: one run profile
(`DOSSIER_RUN_PROFILE`) holds the run total, the discovery share, the cost cap
of one discovery call and the wall clock (2 hours, discovery included). Units
are `dossier-units-v1`: 1 unit is 1,000 tokens (input, cache and output,
rounded up per call; unknown usage counts at the call's full ceiling). The
narrative gets the run total minus the discovery share; each stage has a
per-attempt unit ceiling and an output-token cap; the discovery budget
(excerpt size, items per call, number of map calls) is derived from the profile
by `discoveryBudgetFor`. The model, effort and thinking pins are in the same
profile (effort `high`, thinking off at that head). When a limit is reached the
run stops and renders what is complete. [Unknown] The figures are being
redesigned (a total derived from the selection cap) and must be read from the
profile on the merged code, not from this page.

[Unknown] How long a run takes and what it costs: no provider call has ever
been made. The wall clock is the ceiling, not an estimate. At `d6601785` the
profile's discovery excerpt is 800 characters; the lead reports it is being
raised to the 1,500-character bound with fewer items per call [Unknown until
merged].

Exit codes [Observed in `dossier-main.ts`]:

| Code | State | Meaning |
|---|---|---|
| 0 | complete | pages written |
| 2 | invalid-input | bad URL, missing or unknown `--route`, bad flag |
| 3 | admission-missing | an admission record is missing; nothing was read or sent |
| 4 | unresolved-revision | `ls-remote` could not pin the ref |
| 5 | generation-unavailable | route not in force, no credential, state directory unavailable, a refused corpus |
| 6 | generation-stopped | stopped (budget, wall clock, a refused call, discovery refused); the run record is written, pages are not |
| 7 | generation-stopped-partial | stopped, but the completed stages rendered some pages |
| 1 | any other | unexpected failure, including a `--out` that exists or sits inside a Git work tree (printed as "dossier trigger failed") |

## 5. Where the output lands and how to read it

In the `--out` directory [Observed in `dossier-render.ts`]: `index.html` (the
overview, reading level 0), `contents.html`, `glossary.html`, `deep-dives/`
(one per deep dive), `sources/` (one page per quotable source, with the exact
admitted text and byte offsets), `size-report.html`, `dossier.json`,
`size-report.json` and `run-record.json` (budget, spend, every call and gate
decision; no repository text). Open `index.html` in a browser. [Unknown] Whether
it opens correctly from a `file:` address: the pages have been rendered from
synthetic runs only; if it does not, serve the directory with any static server
bound to loopback.

Every page says "Generated dossier draft — not reviewed or adopted"; it is a
local editorial draft, never published (packet Q6). Labels:

- **Inferred**: a generated sentence the fidelity review judged supported by
  its cited sources. A model said it; the sources are one click away.
- **Unknown**: any other generated block, and every open question. Treat as
  unverified.
- **Observed**: appears only where a diagram record says so.
- **Quoted blocks**: the source pages show the exact admitted text with byte
  offsets; those are the evidence, not the model's wording.

[Inferred] Read the `run-record.json` first: it says what discovery mapped, what
it deferred and what was never read.

## 6. Known limitations

- [Unknown] The first real call: effort `high` and thinking off are unmeasured
  pins; request acceptance, usage accounting and the 64k output ceiling have run
  only against a local capture endpoint and loopback fixtures.
- [Observed] No real reader evaluation: the evaluation harness has a scripted
  reader only, so nothing says the page answers your five questions.
- README and docs are sendable only if row 12 is signed, after rows 1 and 7;
  without it "advantages as maintainers state them" rests on licence texts and
  code comments.
- Discovery excerpts are short (a few hundred to 1,500 characters, per the
  profile) and heuristic for code; a file whose mechanism lies past its declarations is under-described.
  Redis is mostly C: the declaration-line rules were measured only on a
  synthetic fixture.
- The budget figures are proposals, not measurements, and are being redesigned.
- [Observed] There is no resume. A stopped run keeps its record and state
  directory; it does not continue.

## 7. If it stops partway

Read the printed state and `run-record.json` in the `--out` directory (and the
`.state` directory beside it: `discovery-receipts.jsonl`, `consent-audit.jsonl`,
the narrative journal).

- Exit 3, 4, 5 before any read: fix the named cause (a missing record, the
  route, the key) and run again; nothing was spent.
- Exit 6 or 7: the budget or wall clock ended it, or a stage was refused. The
  partial pages (exit 7) are real output of completed stages. A new run is a
  fresh run: it needs a new `--out` and spends again; the earlier state
  directory is kept as evidence and is never reused.
- [Inferred] Do not raise the budget without telling the owner: the figures are
  what the egress record's packet tells you bounds what leaves the machine.
- A provider 429 or 529 is retried with backoff inside the run budget [Observed
  in the provider README]; any other provider failure is recorded as uncertain
  and stops the run.
- An egress record withdrawn mid-run stops the next call; nothing overrides it.
