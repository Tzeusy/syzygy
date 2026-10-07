# Polaris dossier for an arbitrary public repository

> **Candidate — binds nothing.** Drafted 2026-10-08 from the owner's
> direction of 2026-10-07, relayed by the lead session; revised the same day
> after round 1 (`docs/reviews/R-ARBITRARY-PUBLIC-REPO-1-RAW.md`, REVISE). It
> is not adopted, performs no act, and grants no read, egress, write or
> execution. Effect comes only from owner acts over exact reviewed bytes; the
> owner packet in this directory lists them.

**The operator should be able to point Polaris at any public Git repository,
fork or clone it locally, and get an honest dossier without signing a new
consent for that repository.** Today every repository needs its own signed
observation consent and, unless a drawer statement is signed for it, its own
signed agent-provider statement; Redis took a whole sitting.

## Why

**Warrant:** the owner direction `ARBITRARY-PUBLIC-REPO-DOSSIER-2026-10-07`
(`decisions/ARBITRARY-PUBLIC-REPO-DOSSIER-DIRECTION.md`), a plain owner
direction that directs this draft and performs no act. It records the
owner's words, of which this is the central part:

> "I want to apply this even to repositories that I don't own, part of the
> point is an expedited learning curve for any arbitrary git repository.
> Assume we can easily fork and maintain our own fork locally, but may not
> necessarily have 'authoritative knowledge' on the motivations behind the
> creation of the repository"

Its point 2 says reconstruction may draw on "the code and its history".
This draft keeps history off by default and offers it as packet Q2, because
reading history changes REQ-033's one-commit rule; that trade-off is the
owner's.

Two things block that today:

- **Per-repository acts.** [Observed] Reading a repository needs a recorded
  observation consent for that repository, stored as a governance act, with
  the repository's identity in a project declaration (doctrine
  `architecture.md`; RFC1-2, RFC1-3, RFC1-4, RFC3-6, RFC3-7, RFC3-30,
  RFC5-12; quoted in `design.md`). Redis has one, naming four commits
  (`decisions/PUBLIC-REPO-ADMISSION-REDIS-OBSERVATION-ACT.md`). The governed
  check also needs either a signed drawer statement or a signed
  agent-provider statement for each repository
  (`packages/polaris-dossier/src/gate-sources.ts`, `DRAWER_FORMS` and
  `STATEMENT_FORMS`, keyed on `redis-redis`).
- **Maintainer-stated only.** [Observed] The brief's reader topics are
  "maintainer-stated advantages and trade-offs" (REQ-polaris-generation-034),
  and ruling 10b keeps advantages maintainer-stated
  (`decisions/REDIS-LOCAL-AGENT-SITTING-DIRECTION.md`). For a repository whose
  authors wrote little about why, most of the "why" would be Unknown, even
  where the code and tests make it fairly clear.

## What changes

**Amendments first.** The per-repository rule is in adopted doctrine and in
accepted contracts, and no reading of their text admits a standing grant.
`AMENDMENTS.md` drafts the smallest set of semantic deltas this draft found:
one doctrine amendment (`architecture.md`) and contract amendments of
RFC1-2, RFC1-3, RFC1-4, RFC3-6, RFC3-7, RFC3-30 and RFC5-12. They add a
*standing observation consent*, a consent record whose subject is a class of
repositories, reaching one repository per run through a *run admission
entry*. Each needs its own owner act.

Three added requirements to `polaris-generation`, all in the operator-agent
mode:

- **037, standing public-observation consent.** Admits no run until the
  amendments and the standing consent are in force. Then any public
  repository the operator clones is read at the one commit the run pins.
  Repositories with their own consent, in any state, the owner's declared
  repositories and the exclusion list are refused, matched by identity, by
  commit and by URL. The governed check becomes a rule: the standing record
  states, in advance, that no evidence drawer exists, and the pinned tree is
  checked for `openspec` or `.syzygy` paths; a governed tree still needs a
  per-repository provider statement. History, and recording an execution
  choice, are off unless the standing record says otherwise.
- **038, reconstructed motivations.** Motivation, trade-off, advantage and
  position claims each declare a basis: maintainer-stated, anchored to a
  verified quotation of the repository's own text, or reconstructed, with
  premises and an evidence trail, rendered Inferred and marked as not the
  authors' stated intent. The fidelity review classifies every Inferred
  block, so an unmarked motive claim blocks readiness.
- **039, external comparisons.** Conditional: in effect only if the owner
  reverses ruling 10b; otherwise struck before sign-off.

No byte of any existing requirement changes. Each added requirement names the
predecessor text it reads for its runs.

## Scope and preserved boundaries

- **Redis keeps its admission.** Its consent, statements, admission basis and
  pinned revisions do not change, and the standing consent never applies to
  it. **REQ-038 does apply to Redis's runs**: its motivations and trade-offs
  could then be reconstructed, which narrows ruling 10b and REQ-034's
  "maintainer-stated" topic for Redis. Advantages stay under 10b. Whether
  038 should reach Redis is an owner question (packet Q5).
- **Nothing else widens.** No egress (the provider mode stays parked), no
  write, no issues, PRs, CI or other repositories, and by default no history
  and no recorded execution choice. Screening, secret exclusion (SEC-5) and
  the in-process reader are unchanged.
- **Syzygy makes no network request** to admit or verify a repository. That
  it is public and that the commit is published are the operator's
  declarations, labelled Inferred.

## Acts this needs before it can bind

1. The doctrine amendment and the contract amendments (`AMENDMENTS.md`,
   A1 to A4).
2. The standing public-observation consent (A5).
3. This spec, signed by version tag.
4. A new version of the source-acquisition entry naming the standing route.

The owner packet orders them and recommends answers.

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
