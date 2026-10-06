# No kernel evidence drawer — redis-redis

> Instance filled from `../../templates/NO-EVIDENCE-DRAWER-STATEMENT-TEMPLATE.md` by
> `scripts/build_dossier_local_agent_acts.py`. Candidate — binds nothing
> until the owner acts on this record's exact bytes.

Date: 2026-10-06 (drafted); the act, if performed, records its own instant

Owner: Tzeusy

Record ID: `NO-EVIDENCE-DRAWER-redis-redis`

Record version: `0.1.0-candidate.1`

Record class: project-input statement (REQ-polaris-generation-001, admitted
project input; read by REQ-polaris-generation-033's governed predicate)

Subject: `(project:syzygy, repository:redis-redis)`

Statement: no kernel evidence drawer (RFC-0006 §3.5) exists for this
repository in `project:syzygy`.

Basis: `project:syzygy` has never onboarded this repository: it is a public repository offered for observation only, and observed only while the observation consent `PUBLIC-OBS-REDIS-2026-10-03` is in force; Syzygy keeps no evidence drawer for a repository it would only observe. This statement stays true whether or not that consent is signed. The owner states the absence; Syzygy cannot observe it.

Proposed provenance state: `owner-adopted (bootstrap, uncorrelated)` —
state (1), RFC3-16; A1 audit-record identity explicitly absent

Proposed revocation state: active; supersedes no earlier statement

## What it decides

REQ-polaris-generation-033 calls a subject non-governed only when the admitted
project input states that no kernel evidence drawer exists for it and the
tree at the pinned revision holds no `openspec/**` path and no `.syzygy/`
path. This record is that statement for this repository, and only that
statement. The tree half is not decided here: Syzygy checks it by path, at
the pinned revision, when the run starts, and a run whose tree holds either
kind of path is governed whatever this record says.

For a non-governed subject Syzygy issues the agent brief without a
per-project agent-provider statement; the agent sessions' sends to their own
provider are then the operator's own act, and every page says so.

## What it does not do

It is not a consent. It permits no read, egress, write or execution, and it
gives no provider any content. It does not make the repository's content
public or non-public, and it says nothing about any other repository or about
any repository in another project.

## Withdrawal and change

Withdrawal is a later owner act naming this record. Withdrawn, the project
input no longer states whether a drawer exists, so the subject is treated as
governed: Syzygy refuses to issue a brief unless an in-force agent-provider
statement covers it, and refuses every later step of a run that relied on
this record. If Syzygy ever creates a kernel evidence drawer for this
repository, this record becomes false and must be withdrawn in the same
change.
