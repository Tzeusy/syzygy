# Amendments this change needs — semantic deltas

> **Candidate — binds nothing.** Drafted 2026-10-08 in the form of
> `contracts/candidates/policy-candidates/SEMANTIC-DELTA-TEMPLATE.md`, which
> leaves storage open ("a per-change file is fine"). Nothing here edits
> doctrine or a contract: each delta is a proposal, and only the owner's act
> over the exact patched bytes adopts it (VIS-4). Line numbers are at
> `origin/main` `3409ef5a`.

**Plainly: REQ-polaris-generation-037 is an amendment, not a reading.**
Adopted doctrine and four accepted contract clauses say that every observed
repository has its own consent record, and that a repository's identity
lives in a project declaration. A standing consent for repositories the
owner has never named does not meet that text, so the text has to change
first. The deltas below are the smallest set this draft found that makes the
standing route lawful; REQ-037 admits no run until all of them are in force.

## The shape of the amendment, and why this one

**One new kind of observation consent record, not a new class.** A
*standing observation consent* is a consent record like any other: a
governance act stored in `.syzygy/governance/decisions/`, granting the
observation class only, with every RFC5-12 field. What differs is its
subject: instead of one named repository, it names the conditions a
repository must meet (public, the host rule, not excluded) and the
exclusions. Each run then writes a *run admission entry* naming the one
repository and commit it reaches. That entry is the standing record's subject
list for that run; it is not an act, not a consent record and grants nothing.

[Inferred] This is smaller than the alternatives:

- **A new consent class** (a fifth RFC5-12 bullet) would also need RFC5-13 to
  RFC5-16 and RFC2-24 #6 reread for it. Extending the observation class keeps
  revocation, rendering and the `unconsented-source-or-provider` reason as
  they are.
- **Keeping RFC1-2, RFC1-4 and RFC3-6 unchanged** is possible only if the
  operator adds a repository entry to `project:syzygy`'s declaration for
  every repository, a governed-plane edit per repository, which is the
  per-repository step the owner asked to remove. [Observed] No project
  declaration is tracked today (`git ls-files` for `*project.yaml` and
  `.syzygy/governance/declarations/*` returns only the two adapter-registry
  entries), and Redis's identity lives only in its consent record. That
  pre-existing gap is Redis's, is not repaired here, and is recorded in
  `design.md`.
- **The glossary line** (`doctrine/README.md:25-26`, "every observed
  repository needs consent (architecture.md; security.md SEC-4)") needs no
  delta: it does not say "per repository", it cites `architecture.md` for the
  rule, and the same file says at line 19 that "consent" in doctrine means
  the owner's. It is listed under "does not change" below so a reviewer can
  contest that.

## Acts the owner would sign

| # | Delta | Artifact | Act type and form | Precedent |
|---|---|---|---|---|
| A1 | Doctrine: the standing form of observation consent | `doctrine/architecture.md` lines 27 and 62-64 | Doctrine amendment adoption: a new row of `decisions/DOCTRINE-AMENDMENT-LOG.md` (D10 if D7 and D8 keep their numbers), adopted in the owner's words over a confirmed package | D9 (`DOCTRINE-AMENDMENT-LOG.md:12`), package under `contracts/candidates/doctrine-amendment-sec3-attended-agent-session-d9/` |
| A2 | Contracts: RFC1-2, RFC1-3, RFC1-4 | `contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md` | One `contract-amendment` act per module, each over the one row of a package manifest holding the module with the patch applied; or one act over a multi-row manifest | `decisions/RFC5-PROJECT-DOCUMENTATION-CLASS-AMENDMENT-ACT.md` (act type `contract-amendment`); `CONTRACT-READABILITY-RESTYLE-ADOPTION-ACT.md` (one act, many modules) |
| A3 | Contracts: RFC3-6, RFC3-7, RFC3-30 | `contracts/rfcs/RFC-0003/manifests-and-namespace.md` | As A2 | As A2 |
| A4 | Contracts: RFC5-12 | `contracts/rfcs/RFC-0005/consent-egress-secrets.md` | As A2 | As A2 |
| A5 | The standing public-observation consent itself | a new record in `.syzygy/governance/decisions/` | A digest-bound consent act, like Redis's observation consent | `decisions/PUBLIC-REPO-ADMISSION-REDIS-OBSERVATION-ACT.md` |

A5 is not an amendment; it is the consent the amended texts permit, and it
cannot be performed before A1 to A4. Packaging each delta as an installable
patch with its manifest (as the RFC5-14 amendment was) is a step after this
change's review, not part of it.

**Collisions to know about.** [Observed by `arb_bound_check.py`, a scratch
script that hashes each target and searches every tracked file for the
digest:]

- `architecture.md`'s current digest is cited by the candidate D7 and D8
  packages (each package's `OWNER-DECISION-PACKET.md` and `SEMANTIC-DELTA.md`).
  Whichever of D7, D8 and A1 is adopted first changes the bytes the others
  were reviewed over; the later ones must be rebased and re-confirmed. D9's
  in-force record binds `security.md` and `v1.md` only, so A1 does not touch
  D9.
- `RFC-0001` and `manifests-and-namespace.md` are rows of
  `ACTIVE-CONTRACT-MANIFEST.txt` and of the readability restyle's
  `CONTRACT-AMENDMENT-MANIFEST.txt`; `consent-egress-secrets.md` is cited by
  the active manifest, the RFC5-14 package manifest, its act, the
  acceptance-act record, `PROJECT-STATUS.md` and
  `.github/workflows/governance-docs.yml`. Each act regenerates the active
  manifest in the RFC5-14 act's form.
- D9's log row queues "(c), an RFC 0005 amendment" for RFC5-12's effect
  change. A4 touches the same clause; whichever is drafted second must be
  drafted over the first's patched bytes.

---

# Semantic delta A1 — doctrine: standing observation consent

**Artifact(s):** `.syzygy/governance/doctrine/architecture.md`
**Stable IDs affected:** none (unnumbered doctrine prose); the sentences are
quoted below
**Change class:** Normative
**Author:** lane-arbitrary (agent), for the lead session
**Date:** 2026-10-08

## Current meaning

Lines 26-27:

> - Onboarding is recorded, per-repository consent (security.md SEC-4).
>   **Every observed repository consents, governance root or not.**

Lines 62-64:

> Every edge from Syzygy is gated: each observed repository, governance root
> included, has consented (SEC-4), and adapters act only when explicitly
> authorized.

## Proposed meaning

Lines 26-27 become:

> - Onboarding is recorded, per-repository consent (security.md SEC-4).
>   **Every observed repository consents, governance root or not**: by its own
>   consent record, or, for read-only observation of a public repository, by
>   the owner's standing observation consent, which states the conditions
>   every such repository meets and reaches each one through a recorded
>   admission that names it. A standing consent never grants write or
>   execution, and never covers a repository that has its own record.

Lines 62-64 become:

> Every edge from Syzygy is gated: each observed repository, governance root
> included, has consented (SEC-4) by its own record or, read-only, under the
> owner's standing observation consent, and adapters act only when explicitly
> authorized.

## What explicitly does NOT change

- "Onboarding is recorded, per-repository consent": onboarding (write
  access, SEC-4) stays per repository.
- SEC-2 to SEC-5, `security.md` and `v1.md`, D9's text and its in-force
  record.
- The glossary at `doctrine/README.md:25-26` (see above).
- That a governance root is observed only by its own consent: the standing
  form is limited to public repositories observed read-only, and the
  governance root is declared, so it is excluded.

## Warrant

The owner direction `ARBITRARY-PUBLIC-REPO-DOSSIER-2026-10-07`
(`decisions/ARBITRARY-PUBLIC-REPO-DOSSIER-DIRECTION.md`), which directs a
draft for "any arbitrary git repository" without per-repository acts and
leaves "any reading or amendment of the per-repository consent clauses" to
the owner's sign-off; round 1 of this
change's review (`docs/reviews/R-ARBITRARY-PUBLIC-REPO-1-RAW.md`), finding B1,
which found that no reading could meet the current text.

## Evidence or decision basis

The current text, quoted above; `doctrine/README.md:19` ("Wherever doctrine
says 'human sign-off' or 'consent,' it means the owner").

## Terms introduced / retired

Introduced: *standing observation consent*; *run admission entry* (A4
defines both). Retired: none.

## Downstream impact

Method: a tracked-file sweep for the quoted sentences and for the file's
current digest (scratch `arb_bound_check.py`, at `3409ef5a`). Citers of the
digest: the D7 and D8 candidate packages (above). Sentences restated
elsewhere: `doctrine/README.md:25-26` (not changed, above). Sweep B of
`IMPACT-LEDGER.md` lists the 181 files that say "observation consent", none
of which is edited by this delta.

## Migration / supersession plan

Adopted as one doctrine amendment log row; the D7 and D8 packages rebase
over whichever bytes land first. No digest-bound artifact is edited.

## Review

**Required class:** full review (Normative, doctrine).
**Reviewer:** fresh context, not this session.
**Verdict:** not yet reviewed.

---

# Semantic delta A2 — RFC 0001: identity, consent and membership

**Artifact(s):**
`.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`
**Stable IDs affected:** RFC1-2, RFC1-3, RFC1-4
**Change class:** Normative
**Author:** lane-arbitrary (agent)
**Date:** 2026-10-08

## Current meaning

RFC1-2, lines 169-176, final sentence:

> Repository
> identity is a declared identity in the project declaration, never a remote URL
> or path — URLs and default branches change; identity must not.

RFC1-3, lines 178-181:

> **RFC1-3.** Observed-source repositories are read-only to Syzygy unless
> separately onboarded. Every observed repository — governance root or not —
> requires a recorded **Consent record** (SEC-4). No consent means no
> observation, and therefore **Unknown** — never an empty graph read as absence.

RFC1-4, lines 188-191:

> **RFC1-4.** A repository's role and membership are answered by the project
> declaration; its content by the version-control authority through its typed
> adapter. Two questions, two authorities (architecture.md, typed authority); no
> kernel construct may merge them into one answer.

## Proposed meaning

RFC1-2's final sentence becomes:

> Repository
> identity is a declared identity in the project declaration or, for a
> repository observed only under a standing observation consent, in the run
> admission entry that names it (RFC5-12); never a remote URL or path — URLs
> and default branches change; identity must not.

RFC1-3's second sentence becomes:

> Every observed repository — governance root or not —
> requires a recorded **Consent record** (SEC-4): its own, or a standing
> observation consent record whose conditions it meets, reached through a run
> admission entry that names it (RFC5-12).

RFC1-4's first sentence becomes:

> **RFC1-4.** A repository's role and membership are answered by the project
> declaration or, for a repository observed only under a standing observation
> consent, by that consent record (role `observed-source`) and the run
> admission entry (membership for that run only); its content by the
> version-control authority through its typed adapter.

## What explicitly does NOT change

- RFC1-2's two roles and the rule that a URL or path is never identity: the
  admission entry's URL and location are locator hints.
- RFC1-3's "No consent means no observation, and therefore Unknown", and its
  egress sentence (provider consent stays a separate per-(Project, provider)
  record).
- RFC1-4's "Two questions, two authorities": declaration-side answers still
  never come from content.

## Warrant

As A1.

## Evidence or decision basis

The quoted text.

## Terms introduced / retired

As A1, defined in A4.

## Downstream impact

Method: as A1. The module's digest is a row of `ACTIVE-CONTRACT-MANIFEST.txt`
and of the readability restyle's `CONTRACT-AMENDMENT-MANIFEST.txt` (a
performed act's manifest, not edited; the active manifest is regenerated by
the act). Code that reads repository identity from a declaration
(`packages/polaris-dossier/src/gate-sources.ts`) is slice 4's.

## Migration / supersession plan

A `contract-amendment` package: the patch, a one-row manifest of the patched
module, a review, the act, the regenerated active manifest. Identifiers keep
their numbers.

## Review

**Required class:** full review (Normative, accepted contract).
**Reviewer:** fresh context.
**Verdict:** not yet reviewed.

---

# Semantic delta A3 — RFC 0003: repository entries, consent records, per-pair consent

**Artifact(s):**
`.syzygy/governance/contracts/rfcs/RFC-0003/manifests-and-namespace.md`
**Stable IDs affected:** RFC3-6, RFC3-7, RFC3-30
**Change class:** Normative
**Author:** lane-arbitrary (agent)
**Date:** 2026-10-08

## Current meaning

RFC3-6, lines 249-254:

> **RFC3-6.** **Repository entries.** Repository identity is the declared
> opaque identifier — never a URL, path, or branch (RFC1-2); locator hints may
> change without touching identity. An entry whose consent reference does not
> resolve to an in-force consent record is **not observed**: its content
> renders Unknown (`unconsented-source-or-provider`, RFC2-24 #6), never an
> empty graph read as absence (RFC1-3).

RFC3-7, lines 256-264 (opening and first bullet), and lines 274-275:

> **RFC3-7.** **Consent records** are governance acts stored in
> `.syzygy/governance/decisions/`, referenced — never embedded — from the
> declaration. Two kinds:
>
> - **Observation/write consent** (SEC-4): subject is the pair *(observing
>   Project, repository)*; scope enumerates what is consented — observe, write
>   (governance-root plane only), and, when the execution-profile RFC exists,
>   execute (SEC-3). Every observed repository requires one, governed root or
>   not.

> Every consent record carries attribution, grant timestamp, and scope, and is
> individually revertable.

RFC3-30, lines 519-521:

> - Role and consent are properties of the *(Project, repository)* pair
>   (RFC3-7), never global: Project A observing repository R requires A's own
>   consent record for R, regardless of R's role elsewhere.

## Proposed meaning

RFC3-6 gains a final sentence:

> A repository observed only under a standing observation consent (RFC5-12)
> has no repository entry: its declared identity and locator hints are carried
> by its run admission entry, and it is **not observed** unless that standing
> record is in force and its conditions hold for it.

RFC3-7's first bullet's last sentence becomes:

> Every observed repository requires one, governed root or not — its own, or,
> for read-only observation only, a **standing observation consent**: one such
> record whose subject is the pair *(observing Project, every repository that
> meets its stated conditions and none of its exclusions)*, whose scope is
> observe only, and which reaches one repository at a time through a run
> admission entry (RFC5-12). A repository with its own observation consent
> record, in any state, is never reached by a standing one.

RFC3-7's attribution paragraph is unchanged; a standing record carries the
same fields and is revertable as a whole.

RFC3-30's first bullet becomes:

> - Role and consent are properties of the *(Project, repository)* pair
>   (RFC3-7), never global: Project A observing repository R requires A's own
>   consent record for R, or A's own standing observation consent whose
>   conditions R meets, regardless of R's role elsewhere; another Project's
>   consent never suffices.

## What explicitly does NOT change

- Consent records are governance acts in `decisions/`; the run admission
  entry is not one and is not stored there.
- The egress-consent bullet of RFC3-7 and owner decision B8: no standing
  egress consent is created.
- Write and execute consent stay per repository.
- RFC3-30's dual-role rule and its "entire tree" bullet.
- RFC3-16: a standing record takes effect only through its owner act.

## Warrant

As A1.

## Evidence or decision basis

The quoted text; RFC3-7's own [Inferred] rationale for pairs ("consenting to
observation by one project must not silently admit another"), which the
standing form keeps by naming the observing Project.

## Terms introduced / retired

As A1.

## Downstream impact

Method: as A1. The module's digest is a row of the same two manifests as A2.

## Migration / supersession plan

As A2.

## Review

**Required class:** full review.
**Reviewer:** fresh context.
**Verdict:** not yet reviewed.

---

# Semantic delta A4 — RFC 0005: the standing form of observation consent

**Artifact(s):**
`.syzygy/governance/contracts/rfcs/RFC-0005/consent-egress-secrets.md`
**Stable IDs affected:** RFC5-12
**Change class:** Normative
**Author:** lane-arbitrary (agent)
**Date:** 2026-10-08

## Current meaning

RFC5-12, lines 99-101 and 111-112:

> - **Observation consent** — per repository: Syzygy may read and index it
>   (RFC1-3). Absent: no observation, Unknown — never an empty graph read as
>   absence.

> Every consent record names its class, subject, scope, granting principal, grant
> instant, and revocation state.

## Proposed meaning

The observation bullet becomes:

> - **Observation consent** — per repository: Syzygy may read and index it
>   (RFC1-3). Absent: no observation, Unknown — never an empty graph read as
>   absence. One record may instead be a **standing observation consent**
>   for one observing Project: its subject is the class of repositories that
>   meet its stated conditions (publicly readable, a host rule, and none of its
>   exclusions) and have no observation consent record of their own in any
>   state; its scope is read-only observation of the commit a run pins and,
>   only where it says so, that commit's ancestor commit objects. It grants no
>   write, execution or egress. It reaches one repository per run through a
>   **run admission entry** that the observing Project's tooling writes before
>   any read, naming the repository's declared identity, its locator hints, the
>   pinned commit and the standing record. An admission entry is not a consent
>   record, is not an act and grants nothing of its own; revoking the standing
>   record revokes every entry under it.

The fields sentence gains:

> For a standing observation consent the subject and scope are its stated
> conditions and exclusions; each run admission entry names the one
> repository and scope it reaches.

## What explicitly does NOT change

- The closed set of four classes; one record grants one class.
- Write, egress and execution consent and their granularity (B8).
- RFC5-13 to RFC5-16: revocation is prospective and renders dependent claims
  Unknown; a standing record's revocation, or a new version adding an
  exclusion, does the same for every repository it reached.
- RFC5-14's content classes, including the 2026-10-07 project-documentation
  class.

## Warrant

As A1.

## Evidence or decision basis

The quoted text.

## Terms introduced / retired

Introduced and defined here: *standing observation consent*, *run admission
entry*. They enter the term registry with the act (CC-KNOW-5).

## Downstream impact

Method: as A1. Citers listed under "Collisions". The D9-queued RFC5-12
amendment touches the same clause. REQ-polaris-generation-025 restates the
per-repository form; REQ-037 states how it reads for standing runs, and no
byte of REQ-025 changes.

## Migration / supersession plan

As A2; the active manifest and the workflow's pinned digest are regenerated
by the act, in the RFC5-14 act's form.

## Review

**Required class:** full review.
**Reviewer:** fresh context.
**Verdict:** not yet reviewed.
