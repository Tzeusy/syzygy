# Semantic delta — agent-provider statement, version 2 (Redis, Claude Code with Anthropic)

> **Candidate — binds nothing.** Drafted 2026-10-08 for the provider-statement
> blocker of the first Redis run (PR #403, review R-PR403-SCREEN-DOCS-1,
> finding F1). Effect comes only from a new owner act over the record's exact
> bytes at this package's manifest row. No act is recorded here.

## Class

Normative: a per-project consent (SEC-2) widened by one RFC5-14 class. It
adds no tool, provider, repository, read, egress route or execution.

## Subject and change

Subject: version `0.1.0-candidate.1` of the record `AGENT-PROVIDER-redis-redis-anthropic`,
`../dossier-local-agent-acts/instances/redis/AGENT-PROVIDER-STATEMENT-ANTHROPIC.md`,
bound by the act recorded at
`.syzygy/governance/decisions/DOSSIER-LOCAL-AGENT-REDIS-AGENT-ANTHROPIC-ACT.md`
(2026-10-07). Those bytes stay as they are.

The successor, `instances/redis/AGENT-PROVIDER-STATEMENT-ANTHROPIC.md` in this
package, is the same record with exactly these lines changed;
`scripts/build_dossier_agent_provider_v2.py --check` derives the expected bytes
from the version-1 file and fails on any other difference:

| Line | Version 1 | Version 2 |
|---|---|---|
| Instance header | names the version-1 template and builder | names this package's template and builder |
| `Date:` | 2026-10-06 (drafted) | 2026-10-08 (drafted) |
| `Record version:` | `0.1.0-candidate.1` | `0.2.0-candidate.1` |
| Content classes | `governance-text`, `code-structure`, `code-content`, `evidence-content`, `derived-composites` | the same five, then `project-documentation` |
| `Proposed revocation state:` | "active; supersedes no earlier statement" | "active; supersedes version 0.1.0-candidate.1 of this record, if an act over that version is in force, from the effective instant of the act on this version (prospective, RFC5-13); with none in force it supersedes nothing" |

The supersession sentence is the egress record's version-2 form
(`../public-egress-v2/instances/egress-anthropic/EGRESS-CONSENT-ANTHROPIC.md`).

## Why [Observed] / [Inferred]

- [Observed] The version-1 class list omits `project-documentation`; the class
  did not exist when it was drafted. The RFC5-14 class act says "No existing
  consent gains the class"
  (`.syzygy/governance/decisions/RFC5-PROJECT-DOCUMENTATION-CLASS-AMENDMENT-ACT.md:66`).
- [Observed, as relayed by the lead and an exploration of the PR branch] the
  PR #403 review's F1 found that the dossier's review packet carries
  project-documentation spans to the agent session while the only Redis
  provider record does not list the class, and asked for "an owner ruling or a
  statement successor that lists `project-documentation`". This package is the
  successor. The raw lives on the PR #403 branch, not on this base.
- [Inferred] With version 2 in force, README and docs spans that screening
  admits may go into Syzygy's own inventory and review packets for Redis; a
  dossier's overview can then be fidelity-reviewed against the project's own
  explanation of itself instead of rendering Unknown.

## Why a new package

The version-1 recorder (`scripts/record_dossier_local_agent_acts.py`) freezes
every non-review file of `dossier-local-agent-acts/` and requires exactly five
acts, so a new file there would break the recorder of an act already
performed. The public egress record took the same route
(`public-egress-v2/`).

## Install-time requirements (code, after the act; not in this package)

[Observed by reading `packages/polaris-dossier/src/gate-sources.ts`] the
statement gate knows only version 1:

- `STATEMENT_FORMS` (`:233-238`) and `statementForm` (`:220-232`) fix the
  package path, the act file name, the phrase label and the act template,
  whose text says "supersedes nothing" (`:113-114`); a version-2 act record
  matches none of them.
- The withdrawal sweep reads the Record ID as a stem (`:230`), and the
  version-2 act names the same Record ID, so without a version-aware form the
  version-2 act record would read as a record naming version 1.
- `providerStatementGate` refuses when more than one in-force statement names
  the pair (`:295`): version 2 must end version 1's term at its own instant,
  as `package-reader.ts` does for the policy chain.
- The gate checks only that a statement lists some class
  (`gate-sources.ts:293`); gating packet spans by class against the in-force
  version is PR #403's own fix.
- `gate-acts.test.ts` hard-codes version 1's classes and version; a new
  recorder and its `check_governance.py` registrations come with the act, not
  before (the version-1 and egress-v2 registrations were added with their
  recorders). Label suggested: `CONSENT TO ANTHROPIC AGENT PROVIDER VERSION 2
  FOR REDIS`. The egress precedent appended "VERSION 2" to version 1's label,
  but here version 1's label is a stem of version 1's sweep (`:225`, `:181`), so a
  label that contains it would read as naming version 1. The label avoids only
  that one stem. A version-2 act record still carries the artifact basename,
  the heading and the Record ID, which are also stems. Only the version-aware
  form above removes the collision (round-1 review of PR #404, finding 8).

## What it does not change

The version-1 bytes and act; the OpenAI statement (no act binds it, and none
is proposed); the egress record (this is not one: Syzygy makes no provider
call in the operator-agent mode); screening and classification of what Syzygy
reads, stores and renders; the agent's own unrestricted reading of the clone,
which the record already discloses.
