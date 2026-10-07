# Polaris dossier for an arbitrary public repository

> **Candidate — binds nothing.** Drafted 2026-10-08 from the owner's
> direction of 2026-10-07, relayed by the lead session. It is not adopted,
> performs no act, and grants no read, egress, write or execution. Effect
> comes only from owner acts over exact reviewed bytes; the owner packet in
> this directory lists them.

**The operator should be able to point Polaris at any public Git repository,
fork or clone it locally, and get an honest dossier without signing a new
consent for that repository.** Today every repository needs its own signed
observation consent and, unless a drawer statement is signed for it, its own
signed agent-provider statement; Redis took a whole sitting.

## Why

The owner's direction, verbatim as relayed:

> "I want to apply this even to repositories that I don't own, part of the
> point is an expedited learning curve for any arbitrary git repository.
> Assume we can easily fork and maintain our own fork locally, but may not
> necessarily have 'authoritative knowledge' on the motivations behind the
> creation of the repository."

Two things block that today:

- **Per-repository acts.** [Observed] Reading a repository needs a recorded
  observation consent for that repository (RFC1-3, RFC5-12, RFC3-30, and
  doctrine `architecture.md`; quoted in `design.md`). Redis has one, naming
  four commits (`decisions/PUBLIC-REPO-ADMISSION-REDIS-OBSERVATION-ACT.md`).
  The governed check also needs either a signed drawer statement or a signed
  agent-provider statement for each repository
  (`packages/polaris-dossier/src/gate-sources.ts`, `DRAWER_FORMS` and
  `STATEMENT_FORMS`, keyed on `redis-redis`).
- **Maintainer-stated only.** [Observed] The brief's reader topics are
  "maintainer-stated advantages and trade-offs" (REQ-polaris-generation-034),
  and ruling 10b keeps advantages maintainer-stated
  (`decisions/REDIS-LOCAL-AGENT-SITTING-DIRECTION.md`). For a repository whose
  authors wrote little about why, most of the "why" would be Unknown, even
  where the code, tests and history make it fairly clear.

## What changes

Three added requirements to `polaris-generation`, all in the operator-agent
mode:

- **037, standing public-repository admission.** One owner act admits any
  public repository the operator clones, at the commit the run pins. Each run
  writes an admission instance record naming the repository, URL, fork and
  commit. The governed check becomes a rule: the standing record states that
  no evidence drawer exists, and the pinned tree is checked for `openspec` or
  `.syzygy` paths. A governed tree still needs a per-repository provider
  statement.
- **038, reconstructed motivations.** Motivation, trade-off, advantage and
  position claims each declare a basis: maintainer-stated, anchored to a
  verified quotation, or reconstructed, with premises and an evidence trail,
  rendered Inferred and marked as not the authors' stated intent.
- **039, external comparisons.** Only if the owner reverses ruling 10b: a
  separate section for comparisons with other projects, shown as the agent's
  unverified report. If the owner keeps 10b, 039 is struck before sign-off.

No byte of any existing requirement changes. Each added requirement names the
predecessor text it reads for its runs.

## Scope and preserved boundaries

- **Redis is untouched.** A repository with any per-repository consent record
  stays on it; the standing admission never applies to it.
- **Nothing else widens.** No egress (the provider mode stays parked), no
  write, no execution beyond D9 as REQ-033 states it, and no issues, PRs, CI
  or other repositories. Screening, secret exclusion (SEC-5) and the
  in-process reader are unchanged.
- **Syzygy makes no network request** to admit or verify a repository. That
  it is public is the operator's declaration, labelled Inferred.
- **The owner's own repositories are excluded.** A repository declared in any
  Syzygy project keeps its own consents.

## The act this needs before it can bind

This change cannot work by spec sign-off alone. The per-repository consent
requirement is in accepted contracts and in doctrine prose (`design.md`,
"Which clauses require per-repository consent"). The owner must either record
a reading that a standing admission instantiated per run counts as a
per-repository consent record, or amend those texts. The packet recommends
the reading.

## Capabilities

- **Modified:** `polaris-generation`, by three added requirements (037 to
  039; the next free identifiers at `origin/main` `3409ef5a`).
- **New:** none.

## Amendment relation

- It extends the composition of `polaris-manifesto-generation`,
  `polaris-manifesto-understanding-amendment`,
  `polaris-non-governed-narrative-profile` and
  `polaris-dossier-local-agent-mode`. No byte of any of them is edited.
- **The candidate spec is held in `proposed/`, not `specs/`,** as the
  narrative profile's was, so the effective-scenario recount and the
  dependency-union tooling do not count it before an act
  (`scripts/build_polaris_dependency_unions.py` docstring). Moving it is a
  step of the installing change.
- `GOVERNING-DEPENDENCIES.md` was rendered by that script's own
  `render_understanding` over the proposed spec. It is review routing, and is
  regenerated by `--write-additions` when the spec is installed.
