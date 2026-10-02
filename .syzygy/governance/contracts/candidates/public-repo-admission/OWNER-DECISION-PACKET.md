# Owner decision packet — reusable public-repository admission

> **Candidate — binds nothing.** Drafted 2026-10-03 at the owner's request
> ("Yeah ok let's do it", answering the proposal to "draft the reusable
> public-repo admission template for your sign-off"). Effect comes only from
> owner acts over the exact records in this directory. A commit, a review, a
> merged pull request or a passing check performs no act. No act record is
> written here, and no target repository body has been read.

## What this is, in one paragraph

The generalized Polaris generator is to be proven on open-source repositories
(`docs/polaris-generation/TARGETS.md`: requests, Redis, Sentry). Before the
generator may read any of them or send any of their content to a model
provider, doctrine and the adopted generator specification require separate,
separately revocable records (SEC-2; RFC5-12, RFC5-14, RFC5-15;
REQ-polaris-generation-001 and 025). Drafting those as a bespoke package per
repository, the way the Butlers and self-observation acts were drafted, costs
several review rounds each. This package instead fixes **one shape** for
public repositories, so admitting a new target means filling the same two
templates and signing them, plus a one-time policy act shared by every target.

## The shape

**Once, for every public target:**

1. **Public-source screening scope** (`templates/PUBLIC-SOURCE-POLICY-SCOPE-TEMPLATE.md`).
   An extension of the observing project's secret-classification policy
   (currently `.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json`,
   which carries its own acts) adding a scope for public repositories, and the
   content-classification rules RFC5-14 needs to put concrete content into its
   closed classes. Screening still applies to public code: a public repository
   can contain committed secrets, and screening them out is the point.

**Per target, two records and one registry entry:**

2. **Observation consent** (`templates/OBSERVATION-CONSENT-TEMPLATE.md`) — per
   repository (RFC5-12): read-only reads of exact Git objects at the pinned
   revisions listed in the record, from a scratch clone the operator makes.
   No working tree outside that clone, no execution of the target's code
   (SEC-3), no writes anywhere in the target.
3. **Egress consent** (`templates/EGRESS-CONSENT-TEMPLATE.md`) — one record
   per (project, provider) pair naming the permitted content classes
   (RFC5-12, RFC5-14).
4. **Registry entry** for the target's source-acquisition observer and the
   provider execution route (REQ-polaris-generation-017; RFC4-1 permits one
   registered adapter per project per external authority). Its fields follow
   `openspec/changes/polaris-manifesto-generation/ADAPTER-DECLARATIONS.md`
   "Required registration fields"; it is drafted with the first
   implementation that reads it, not here, because a registry entry naming no
   implementation registers nothing.

Each numbered item is its own record with its own act, as REQ-025 requires
("These permissions SHALL remain separately revocable/renderable and SHALL
NOT imply one another"). Several acts may be given in one sitting.

`instances/requests/` fills items 2 and 3 for the first target, T1.

## Questions for the owner

Each has a recommendation. None is decided by this packet.

**Q1. Which provider and model?** Egress consent must name the provider
(SEC-2). *Recommended:* Anthropic, via the Claude API, with the model
recorded per run rather than fixed in the consent (the consent names the
provider; RFC5-14 does not ask for a model). A second provider later is a
fresh egress consent.

**Q2. Which content classes may be sent?** RFC5-14's closed vocabulary:
`governance-text`, `code-structure`, `code-content`, `work-history`,
`evidence-content`, `derived-composites`. *Recommended for public targets:*
all but `work-history` — understanding a codebase needs its bodies, and the
repositories are public; issue trackers and CI history stay out until a run
needs them. `derived-composites` is included because every prompt is one;
it never launders an unconsented class (RFC5-14).

**Q3. Retention of sent content and provider replies.** SEC-2 does not state
these fields; the generation kit proposes them (`docs/polaris-generation/README.md`,
"Start here" step 4). *Recommended:* provider replies and run records are
retained under the generator's run directory in the observing project's state
directory, not in git; source bodies are never retained beyond the run's
scratch clone; the provider's own retention is whatever its API terms say,
recorded in the consent as a disclosed fact rather than a Syzygy promise.

**Q4. Project identity.** Is each target its own project (`project:oss-requests`
observing `repository:psf-requests`) or a repository observed by
`project:syzygy`? *Recommended:* its own project. REQ-polaris-generation-001's
first scenario ("Two project identities") asks for distinct identities, and
egress consent is per project, so one project per target keeps each target's
consent revocable alone.

**Q5. Sign-off form.** The 2026-10-02 Scope A direction
(`decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`) allows
version-tag option-selection sign-off for PWB deltas, the observer registry
entry and queued contract successors — not consent or policy records.
*Recommended:* extend Scope A to the records of this package by a plain owner
direction, so each target's admission is one structured question. Without
it, each record needs the digest-and-phrase act form.

**Q6. Where generated pages may be served.** *Recommended:* only on the local
daemon's draft route, labelled editorial draft and non-release; never
published, and never presented as the target project's own site or as
endorsed by its maintainers.

## What it does not do

It grants no read, egress, write, execution or release. It changes no adopted
specification or policy. It admits no target. It does not touch the Butlers
consent, policy or registry records, or the self-observation package on PR
#120.

## Review

Not yet reviewed. Per Scope A item 3, a fresh-context round returning CONFIRM,
or CONFIRM WITH EXCEPTIONS with notes only, precedes offering it.
