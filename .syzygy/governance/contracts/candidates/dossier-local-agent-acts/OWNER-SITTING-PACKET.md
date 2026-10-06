# Owner sitting packet — the Redis dossier on your own agent

> **Candidate — binds nothing.** This packet describes decisions you could
> make in one sitting. It performs no act and carries no digest by design:
> each act's argument is that record's row of
> `DOSSIER-LOCAL-AGENT-SITTING-MANIFEST.txt`, printed by
> `python3 scripts/build_dossier_local_agent_acts.py --digests`, never typed.
> Nothing here may be offered until a fresh-context review of these bytes
> returns CONFIRM, or CONFIRM WITH EXCEPTIONS with notes only.

## What this sitting is for

You signed off the local-agent mode (version 1.0, 2026-10-06) and adopted D9
the same day. In that mode your own Claude Code or Codex session writes the
Redis dossier from a clone on your machine, and Syzygy only checks it: it reads
the clone's Git objects itself, verifies every quotation against them, and
renders the result. Syzygy makes no model call.

Before Syzygy will start such a run it looks for owner acts, not for status
words or files. The mode's review asked for that explicitly (note R3-F8): a
consent, a registry entry, a per-project statement, D9 and your RFC7-20
reading each count only if an owner act binds their exact bytes. Today none
of the five has one. The Redis observation consent was drafted and reviewed
earlier and is offered again here; this packet drafts the other four.

## The decisions

| # | You decide | Signing it lets Syzygy | If you decline | Record |
|---|---|---|---|---|
| 1 | Redis observation consent | read the Git objects of the four consented Redis commits | no Redis run of any kind; every Redis claim is Unknown | `../public-repo-admission/instances/redis/OBSERVATION-CONSENT.md` (prepared and reviewed already) |
| 2 | The source-acquisition entry (entry version 2.0.0-candidate.1), signed as package version 1.0 | use its in-process reader as the one registered way to read the clone | every read is refused before an object is opened | `../public-git-source-acquisition-local-agent/proposed/POLARIS-PUBLIC-GIT-SOURCE-ACQUISITION-LOCAL-AGENT-CANDIDATE.json` |
| 3 | "Redis has no kernel evidence drawer" (recommended) | treat Redis as an ungoverned project, provided its tree at the pinned commit has no `openspec/` or `.syzygy/` path, so the agent brief can be issued without a provider statement | no brief for Redis unless you sign 3a or 3b instead | `instances/redis/NO-EVIDENCE-DRAWER-STATEMENT.md` |
| 3a | Claude Code with Anthropic may receive Redis content (optional) | issue the brief to a Claude Code session even if Redis counts as governed | nothing changes if 3 is signed and the tree check passes | `instances/redis/AGENT-PROVIDER-STATEMENT-ANTHROPIC.md` |
| 3b | Codex with OpenAI may receive Redis content (optional) | the same, for a Codex session | as 3a | `instances/redis/AGENT-PROVIDER-STATEMENT-OPENAI.md` |
| 4 | D9, bound to the current bytes of `security.md` and `v1.md` | tell your attended authoring session it may build and run Redis, once you also record a choice for that one run | every brief tells the agent not to build or run Redis outside an execution profile; the run still works | `instances/in-force/D9-IN-FORCE-RECORD.md` |
| 5 | Your RFC7-20 reading, bound to the current bytes of its direction, item 1 only | show your agent's draft as an editorial draft | the draft layer renders Unknown; source pages and disclosures stay readable, so the dossier has no narrative | `instances/in-force/RFC7-20-READING-IN-FORCE-RECORD.md` |

Each row is a separate act. None implies another, and declining one never
undoes another. For a useful Redis dossier you need 1, 2, one of 3 / 3a / 3b,
and 5. Row 4 is only needed if you want the agent to run Redis.

## Row 1 — the Redis observation consent

Already drafted, reviewed (round 7, notes only) and frozen; its recorder is
`scripts/record_public_repo_admission_acts.py`, key `redis-observation`. It is
listed here so one sitting covers everything a local-agent run needs.

Two things to know before you sign it for this mode:

- **How the clone is made.** The record says the operator fetches each
  consented commit alone (`git fetch --depth=1 <upstream> <commit>`). In this
  mode you make the clone, so make it that way: an empty repository, that one
  fetch, then check out the fetched commit. A normal full clone also carries
  history the consent does not name. Syzygy itself would still read only the
  consented commit's objects, but your agent reads whatever the clone holds.
- **Its SEC-3 line predates D9.** The record excludes "executing any code in
  the repository (SEC-3)". [Inferred] That sentence governs Syzygy's reads,
  which never execute anything; your agent's execution is governed by D9 and
  row 4. The wording is queued for the next consent version (`syzygy-i5qt`),
  not changed here, because the record is frozen.

## Row 2 — the source-acquisition entry

What it is: version 2.0.0-candidate.1 of the public Git source-acquisition
entry. The earlier version (parked with the provider mode) fetched each commit
into a run directory. This one fetches nothing: it reads your clone's `.git`
directory, in process, through the reader built in `syzygy-qkea.3` (PR #367).
It honours no refs, configuration, hooks, alternates, grafts or replacement
objects, starts no process, never reads the working tree, and re-hashes every
object it uses. `../public-git-source-acquisition-local-agent/SEMANTIC-DELTA.md`
lists every difference from the earlier version.

How you sign it: by version tag, `public-git-source-acquisition-local-agent-v1.0`,
under the Scope A direction of 2026-10-02. The two numbers differ on purpose:
2.0.0-candidate.1 is the entry's own version (the second version of this
observer), and 1.0 is the first sign-off of this package. Scope A names "the observer
registry entry" of the PWB work; it has never been used for a public-source
entry. So the question offers two choices in one: extend Scope A to this
entry, and sign version 1.0. The recorder
(`scripts/record_versioned_signoff.py`) writes a record that names the
installed entry and the SHA-256 of its bytes, because RFC3-16 says approving a
path never approves later content at it; a later edit to the entry is
unsigned until you sign a new version. Because RFC4-7 honours a registry
entry only under RFC3-16(a), that record also carries the rest of what
RFC3-16(b) asks of any owner act and a tag alone does not: the act type, the
instant of recording, the scope, what it supersedes, its state-(1)
provenance, and an explicit line that no independent audit record exists.

**What is built and what is not.** The reader implements the read rules
above. The entry also declares source limits (how many files, how large),
screening, the fact records a read produces and how each failure is shown;
those belong to the dossier gate that will call the reader, which is not
written yet. The entry lists the two halves under `implementationCoverage`.
Signing now is safe in one sense: no read happens without the gate. But you
would be approving declarations no code yet performs; you can instead sign
after the gate lands, at the cost of a later sitting.

Before it can be installed: PR #367 must merge (the install refuses while the
reader file is absent), and the earlier version must not be installed beside
it (one authority, one adapter).

## Row 3 — no drawer, or a provider statement

The mode calls a project governed if Syzygy holds a kernel evidence drawer for
it, or its tree at the pinned commit has any `openspec/` or `.syzygy/` path.
Your agent's session may receive a governed project's content only under a
recorded per-project consent naming its provider (SEC-2). For a project that
is not governed, the agent's sends are your own act and need no record.

The catch: Syzygy can check the tree itself, but whether a drawer exists has
to be stated in the project's input, and nothing states it for Redis today.
A silent input counts as governed. So something must be signed either way.

**Recommendation: sign 3, leave 3a and 3b.**

- It is true. [Inferred] Syzygy has never onboarded Redis. It would only
  observe Redis, and only under row 1, and it keeps no evidence drawer for a
  repository it only observes. The statement says this without assuming row 1
  is signed, so it stays true if you decline row 1.
- It is one record that works for whichever agent you use. Provider
  statements are one per tool and provider, and each is a consent you would
  have to keep current or withdraw.
- It matches what SEC-2 is for. SEC-2 protects governed-project content;
  Redis is a public project Syzygy does not govern.
- It fits an earlier choice. On 2026-10-05 you declined "Name my provider
  per project" for the RFC7-20 question in favour of the reading in row 5.
- It fails closed. If the pinned Redis tree does hold an `openspec/` or
  `.syzygy/` path, the run refuses at start and says so; you can then sign 3a
  or 3b. [Inferred] Redis's tree has neither (general knowledge; nothing has
  been read to check, because no read is authorised yet).

Sign 3a or 3b instead, or as well, if you would rather the run never depend
on the tree check, or if you expect to run this mode on projects that are
governed. Their content classes are the five of RFC5-14's vocabulary that the
first Anthropic egress record (`../public-repo-admission/instances/egress-anthropic/`)
names; the second version adds `project-documentation`, which is not yet in
the vocabulary. The statement says plainly that the classes do not limit what
the agent reads or sends: your agent reads the whole clone, and anything the
screening policy would withhold from Syzygy, secrets included, may still
reach its provider.

## Rows 4 and 5 — binding D9 and your RFC7-20 reading to exact bytes

Both were decided by your own words without a digest: D9 is logged in the
doctrine amendment log, and the RFC7-20 reading is item 1 of the direction
`POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-2026-10-05`. Doctrine in this
repository has always been adopted that way, without a digest act. Syzygy's
check before a step, though, looks for an owner act bound to exact bytes and
a stated scope (RFC3-16(a)), and RFC3-16 read literally calls an artifact
with no such act unadopted. These two records give the check what it looks
for. They change no byte of doctrine or of the direction.

Two readings here are new, and a reviewer may contest them; you should know
them before signing:

- that your words adopted D9 and the reading, and these acts only bind them to
  bytes for the check (the literal alternative: these acts are what makes
  them effective at all);
- that an act over a record which lists the files' digests binds those files,
  rather than an act over each file itself. The act's own digest is the
  record's; the doctrine and direction digests sit inside it.

- **Row 4 (D9).** Bound to the whole current files `security.md` and
  `v1.md`, for one use: the local-agent mode's execution rule. Signing it does
  not by itself let the agent run anything; each run still needs your choice
  for that run, your attendance and the credential check.
- **Row 5 (RFC7-20 reading).** Bound to the whole current direction file, for
  item 1 only. Item 2 of that direction (code execution) is not bound here;
  D9 governs it. The trade-off you made is kept: you chose the reading
  knowing a reviewer may call it a contract change, and this record does not
  settle that. Note what changes: the option you chose was described as "No
  extra record". The review of the mode (note R3-F8) later required every
  such ruling to be established by an owner act, so this row asks you for one
  record after all. Declining it keeps your original choice and the cost
  above.

**The cost of whole-file binding.** Any later edit to `security.md`, `v1.md`
or the direction file, even an unrelated one, leaves that record unmatched.
The failure is closed: briefs fall back to SEC-3's rule, or the draft layer
to Unknown, until a new version of the record is generated and you sign it.
Before the sitting the cost is wider: such an edit regenerates a record and
so the sitting manifest, which retires the review for every row of this
packet (and the entry's sign-off, which is bound to the same manifest), so
nothing here can be recorded until a new review round confirms the new
bytes. After an act is recorded, an edit affects only the record it touches.
A phrase act over doctrine or over a plain direction is new usage in this
repository; the alternative, binding only the D9 block or item 1's lines, is
not something RFC3-16's exact-digest rule describes, so it is not offered.

## What else a real Redis run still needs (not offered here)

- **The screening and classification policy acts.** The mode refuses a run
  without an effective classification policy act and public-source screening
  scope act. [Inferred] Those are the screening-scope rows of the earlier
  Redis sitting packet (PR #260); this packet does not repeat them.
- **The code.** PR #367 (the reader) must merge, and the dossier's gate code
  must be written: the source limits, screening and fact records the entry
  declares (row 2), and the reading of these act records and the version-tag
  sign-off record (the RFC3-16(a) cross-check). [Inferred] The gate code that exists today
  (`body-read-authority.ts`, `governance-inputs.ts`) reads digest act
  records only; a tag-signed registry entry is new to it.
- **Specification version 1.1.** PR #368 proposes version 1.1 of the mode,
  which adds scenarios for "D9 record without its owner act" and "RFC7-20
  reading record without its owner act". These records are written to satisfy
  both versions; if 1.1 changes the governed predicate, row 3 is re-read
  against it before it is offered.

## How you will be asked

The rows are asked in table order, so the Redis observation consent (row 1)
comes first and the drawer statement (row 3) after it. One structured
question per row, each naming the record "at the manifest row" (the
public-admission precedent), with "Sign it" and "Not now" options; row 3
is one question with the options "No drawer (Recommended)", "Claude Code with
Anthropic", "Codex with OpenAI" (more than one may be chosen) and "Not now";
row 2's option reads "Extend Scope A to this entry and sign v1.0". The
recorders (`scripts/record_dossier_local_agent_acts.py`, keys
`redis-no-evidence-drawer`, `redis-agent-anthropic`, `redis-agent-openai`,
`d9-in-force`, `rfc7-20-reading-in-force`; and
`scripts/record_versioned_signoff.py --record public-git-source-acquisition-local-agent --version 1.0`)
record your exact selection. The phrase each act takes is the record's label,
a colon and its manifest row; you never type it.

## What this packet does not do

It performs no act, adopts nothing and changes no doctrine, contract,
specification or performed act. It grants no read, egress, write or execution
by itself; each row grants only what its own record says, once you sign it.
It does not offer the provider-mode rows of the earlier Redis sitting.
