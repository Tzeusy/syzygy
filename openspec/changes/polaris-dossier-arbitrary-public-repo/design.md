# Design — Polaris dossier for an arbitrary public repository

> **Candidate — binds nothing.** Design sketch for the three added
> requirements in `proposed/polaris-generation/spec.md` and the amendments in
> `AMENDMENTS.md`. Line numbers are at `origin/main` `3409ef5a`. Revised
> after round 1 (`docs/reviews/R-ARBITRARY-PUBLIC-REPO-1-RAW.md`, REVISE).

## Which clauses require per-repository consent

The lead's working reading was that SEC-2 governs egress, not reads, so the
per-repository requirement comes from specifications and acts. **The first
half holds; the second does not.** The requirement is also in accepted
contracts and in adopted doctrine prose, and those texts cannot be read to
admit a standing grant: they have to be amended (`AMENDMENTS.md`).

| Source | Text (quoted) | What it requires |
|---|---|---|
| SEC-2, `.syzygy/governance/doctrine/security.md:42-45` | "No governed-project content, or anything derived from it, is sent to a store or service the owner does not control — model providers included — without explicit, recorded, per-project consent." | [Observed] Egress only. Local-agent mode makes Syzygy send nothing (REQ-033), so SEC-2 binds here only through REQ-033's per-project statement for governed subjects. Not amended. |
| SEC-4, `security.md:116-117` | "writes need recorded per-repository consent (onboarding)." | [Observed] Writes only. Not amended. |
| Doctrine, `.syzygy/governance/doctrine/architecture.md:26-27` | "Onboarding is recorded, per-repository consent (security.md SEC-4). **Every observed repository consents, governance root or not.**" | [Observed] Every observed repository, reads included. Unnumbered. **Amended by A1.** |
| Doctrine, `architecture.md:62-64` | "Every edge from Syzygy is gated: each observed repository, governance root included, has consented (SEC-4)" | [Observed] Same. **Amended by A1.** |
| Doctrine glossary, `doctrine/README.md:25-26` | "every observed repository needs consent (architecture.md; security.md SEC-4)." | [Inferred] Met by a standing consent once A1 is in force: it does not say "per repository", and line 19 says "consent" means the owner's. Not amended; contestable. |
| RFC1-2, `contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md:169-176` | "Repository identity is a declared identity in the project declaration, never a remote URL or path" | [Observed] Identity lives in a project declaration. **Amended by A2.** |
| RFC1-3, same file, `:178-181` | "Every observed repository — governance root or not — requires a recorded **Consent record** (SEC-4). No consent means no observation, and therefore **Unknown**" | [Observed] One consent record per observed repository. **Amended by A2.** |
| RFC1-4, same file, `:188-191` | "A repository's role and membership are answered by the project declaration" | [Observed] Membership comes from the declaration. **Amended by A2.** |
| RFC3-6, `contracts/rfcs/RFC-0003/manifests-and-namespace.md:249-254` | "An entry whose consent reference does not resolve to an in-force consent record is **not observed**" | [Observed] Observation goes through a repository entry. **Amended by A3.** |
| RFC3-7, same file, `:256-264` | "**Consent records** are governance acts stored in `.syzygy/governance/decisions/`, referenced — never embedded — from the declaration … subject is the pair *(observing Project, repository)* … Every observed repository requires one, governed root or not." | [Observed] One governance act per (Project, repository) pair. **Amended by A3.** |
| RFC3-30, same file, `:519-521` | "Role and consent are properties of the *(Project, repository)* pair (RFC3-7), never global: Project A observing repository R requires A's own consent record for R" | [Observed] Per pair. **Amended by A3.** |
| RFC5-12, `contracts/rfcs/RFC-0005/consent-egress-secrets.md:99-101`, `:111-112` | "**Observation consent** — per repository: Syzygy may read and index it (RFC1-3)." / "Every consent record names its class, subject, scope, granting principal, grant instant, and revocation state." | [Observed] The observation class is per repository. **Amended by A4.** |
| REQ-polaris-generation-025, `openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md:1400` | "Each consent record SHALL grant exactly one class with subject, scope, granting principal, grant instant and revocation state: observation/write consent per repository" | [Observed] Restates RFC5-12. REQ-037 reads it for standing runs; not edited. |
| REQ-polaris-generation-033, `openspec/changes/polaris-dossier-local-agent-mode/specs/polaris-generation/spec.md:13` | "Before it issues a brief, Syzygy SHALL verify that the clone's checked-out HEAD commit equals a revision that the in-force observation consent for the repository names" | [Observed] The run-time gate. REQ-037 reads it; not edited. |
| REQ-033's governed predicate, same file, line 11 | "For a governed subject, and for a subject whose project input does not state whether a drawer exists, Syzygy SHALL refuse to issue a brief unless an in-force, recorded, per-project statement names the operator's agent provider" | [Observed] The source of the per-repository drawer or provider statement. |

**Round 1 history.** This draft first recommended an owner *reading* that a
standing grant instantiated per run "is" a per-repository consent record, on
the claim that "the literal text is met". Round 1 (B1) found that it is not:
RFC3-7 makes a consent record a governance act in `decisions/` per pair, and
RFC1-2 and RFC3-6 put identity in a declaration; a run-written file in a
state directory is neither. The reading route is withdrawn.

## Decisions in this draft

### 1. One standing record, one admission entry per run

The standing public-observation consent is one record with its own owner act
(A5 in `AMENDMENTS.md`), drafted like the Redis observation consent
(`public-repo-admission/templates/OBSERVATION-CONSENT-TEMPLATE.md`). It fixes:
the class, observation; the subject form, (`project:syzygy`, every
repository meeting its conditions), with the identity format; the host rule;
whether history is in scope (default: no); whether an execution choice may
be recorded (default: no); the exclusion list (identities, URLs and commits);
and the owner's statement, made in advance, that no kernel evidence drawer
exists for a repository observed only under it.

Each run writes a run admission entry in its state directory before the
brief. It is not an act, not a consent record and grants nothing; amended
RFC5-12 (A4) defines it. Its pinned commit is HEAD at that moment, which is
how REQ-033 already pins.

*Alternatives:* a per-repository act signed quickly (rejected: the owner
asked for none); a per-run owner confirmation command (packet Q7; not
recommended).

### 2. Exclusions: by name and by content

Round 1 (B2) showed that an identity-only exclusion can be laundered: a
repository whose consent was withdrawn could be re-admitted under a new
identity and a mirror URL. REQ-037 now refuses the standing route when any
of these match, with no network request:

- **identity**: any per-repository observation consent record naming it, in
  any state; the exclusion list; any Syzygy project declaration;
- **commits**: the pinned commit, and every parent identifier recorded in the
  pinned commit object (read from that object, not fetched), against every
  revision any per-repository consent record names, in any state, and the
  exclusion list's commits; with history admitted, every reachable ancestor
  too;
- **URL**: the normalised upstream URL (scheme and host lower-cased; user
  information, default port, trailing `/` and `.git` removed) against the
  upstream and locator hints of consent records, declarations and the
  exclusion list.

[Inferred] **Residual:** a *different* commit of a withdrawn repository,
whose recorded parents are not named in any record, reached through a URL
that normalises differently (another host's mirror), is told apart only by
the operator's declaration. Every page discloses it. Redis's consent names
four commits; a later Redis commit through a mirror would pass the content
checks, but the identity check would still catch `redis-redis` if declared.

### 3. No network request; publication is declared; one commit only

Syzygy reads only the local `.git` through the registered in-process reader.
It cannot tell whether a repository is public, or whether a commit is
published, without contacting the host, which would be a new effect needing
its own adapter (RFC4-1). So "public", "the pinned commit is published at
the upstream URL" and "the fork reproduces it" are the operator's
declarations, labelled Inferred.

**Local commits (round 1 note on Q1c).** By default the clone must hold the
pinned commit alone, the shape PR #392 adds to `init` (`.git/shallow` names
exactly the pinned commit, and every object is that commit or under its
tree). [Observed in #392's diff] A local commit on top of a fetched commit
therefore makes two commits and is refused. [Inferred] A *single* locally
authored commit with no parents, or a shallow commit whose parents were
never fetched, cannot be told from a published one without the network; the
publication declaration is what excludes it, and SEC-5 screening still
applies to every blob.

### 4. The governed rule

The drawer half comes from the standing record, labelled as the owner's
statement made in advance; its truth for a given repository is Inferred
from the exclusions (a repository with a drawer would have been onboarded,
hence declared or consented, hence excluded).

The tree half reuses the predicate the gate implements
(`packages/polaris-dossier/src/governed.ts:4-11`): a path segment `openspec`
or `.syzygy` at any depth, after NFKC, case folding and trailing dot and
space removal. **Attribution, corrected after round 1:** R3-F9, quoted at
`governed.ts:6`, is about the word "adopted"; the "never less strict than a
root-only, exact-case match" property is the code comment's own claim
(`governed.ts:7-8`), checked by the S3 gates review
(`docs/reviews/R-POLARIS-DOSSIER-S3-GATES-2-RAW.md:54`). That review also
lists what the fold does not reach, which REQ-037 now carries as a disclosed
residual: default-ignorable code points inside the segment (U+200C, U+200D,
U+200B, U+FEFF, U+00AD), a trailing tab, the NTFS stream form and the 8.3
short name. It over-counts too (line 52): a vendored `node_modules/openspec/`
counts as governed.

**The premise changes for third-party trees.** The S3 review called the gaps
a disclosure item because "the project the statement protects has no motive
to hide its own governance tree". [Inferred] For an arbitrary public
repository the tree's author is not the owner, so that premise no longer
holds by construction. The harm a hidden tree could cause is limited: in
local-agent mode Syzygy sends nothing, and the provider receiving the
content is the owner's own agent provider. This draft keeps the residual as a
disclosure item and says so; packet Q3 offers root-only as the alternative.

**A governed tree** under the standing consent is refused at brief time
unless a per-repository agent-provider statement (the Redis 3a/3b form) is in
force, and is then composed under the governed readings of REQ-004.
*Alternative (packet Q3):* treat a third-party public tree as non-governed
for SEC-2, which would need a reading or amendment of SEC-2.

### 5. Reconstructed motivations

The adopted rule (REQ-002, base spec line 52) already allows source-supported
inference of motives and forbids speculation: "Motives, history, definitions
and relationships without sufficient source premises SHALL remain absent or
Unknown; an Inferred label alone SHALL NOT make speculation eligible." REQ-038
gives "sufficient premises" a checkable form:

- every motivation, trade-off, advantage or position block declares
  `maintainer-stated` (a verified quotation of text at the repository's own
  paths) or `reconstructed` (premises plus a trail);
- Syzygy checks the mechanics, and sees only what the agent marked;
- **the fidelity verdict classifies every Inferred block, marked or not**
  (round 1, B5): an unmarked block that states a motive, or any block that
  attributes an intention to the authors without a quotation that states it,
  is a blocking finding against the marking;
- **vendored and third-party text is not maintainer-stated** (round 1 note):
  authorship is Inferred from the path, using the frozen profile's path
  classes; such text may still be a premise of a reconstruction;
- a reconstruction never replaces a maintainer statement, and a motive about
  people stays Unknown without one.

### 6. History: off by default

Round 1 (B4) found that recommending history contradicted REQ-033's "every
read … at the pinned revision" and PR #392's one-commit clone. The default
is now **no history**: commit-message premises fail the check. History is a
separate owner option (packet Q2) whose text names the REQ-033 sentences and
falsifier arm it reads, admits ancestor *commit objects* only (re-hashed,
never their trees or blobs), and withholds every author, committer and
signature line hash-not-body, because names and email addresses are personal
data the privacy posture has never been asked about.

### 7. Execution under the standing consent: refused by default

[Observed] D9 lets the owner record an execution choice per run, letting the
attended agent session run the repository's code on the owner's host.
SEC-3's "What the permitted case costs" (`security.md:95-101`) says the
session "runs with the owner's own credentials and network", that observed
code it runs "can reach them, and can change any file the owner can", and
that "Nothing contains it". For a repository of unknown authorship that cost is higher
than for Redis [Inferred]. REQ-037 refuses an execution choice for standing
runs unless the standing record permits it (packet Q1f, default no).

### 8. Redis and REQ-038

Round 1 (B3) found the earlier "Redis is untouched" false: REQ-038 applied to
every operator-agent run. It still does, and that is now its own owner
question (packet Q5, recommended yes). For Redis it narrows ruling 10b and
REQ-034's "maintainer-stated advantages and trade-offs" topic: Redis's
motivations and trade-offs may be reconstructed; its advantages stay under
10b and packet Q6. Redis's admission basis, consent, statements and pinned
revisions do not change.

### 9. Ruling 10b and REQ-039

Kept as the default: advantages stay maintainer-stated. REQ-039 is
conditional on a recorded reversal, scope `v1-reserved` ("schema defined,
implementation may stub", th-projects `spec-format.md:99`), and is struck
before sign-off if 10b is kept. Its source check relies on the agent's
marking; the fidelity review is the backstop.

## What this change does not settle

- [Observed] No project declaration is tracked (`git ls-files` for
  `*project.yaml` and `.syzygy/governance/declarations/*` lists only two
  adapter-registry entries), so Redis's identity too lives only in its
  consent record. A2 and A3 make that lawful for standing runs; Redis's own
  position is not changed here.
- [Unknown] The exact form of the repository identity
  (`repository:<host>-<owner>-<name>` is the obvious candidate). Fixed in the
  standing record.
- **The source-acquisition entry.** Its subject reads "each (project:syzygy,
  repository) pair that has its own in-force observation consent naming the
  pinned revision", in the candidate package
  (`public-git-source-acquisition-local-agent/proposed/POLARIS-PUBLIC-GIT-SOURCE-ACQUISITION-LOCAL-AGENT-CANDIDATE.json:58`)
  **and in the installed copy the gate reads**
  (`.syzygy/governance/declarations/adapter-registry/POLARIS-PUBLIC-GIT-SOURCE-ACQUISITION-LOCAL-AGENT-CANDIDATE.json:58`,
  named as `installed` at `packages/polaris-generation-consent/src/package-reader.ts:773`).
  Slice 3 versions both; a version-tagged sign-off installs the new copy.
- Requirement numbers 037 to 039 were free at `3409ef5a` (sweep F in
  `IMPACT-LEDGER.md`); lane-doctrine's work adds none (checked 2026-10-08).

## Implementation slices (after sign-off; not filed as beads)

Each is one cohesive, separately verifiable outcome. None starts before the
owner's acts are recorded.

0. **The owner's 2026-10-07 direction**, recorded by the lead in a separate
   PR as a plain owner direction.
1. **Amendment packages A1 to A4** (`AMENDMENTS.md`): patches, manifests,
   reviews, acts, active-manifest regeneration; rebased over D7 and D8 if
   those land first.
2. **Standing consent record and act (A5).** Template and instance in
   `scripts/build_public_repo_admission.py`; a recorder row; the phrase in
   `check_governance.py` `_act_subjects()` and the packet copy in
   `ACT_DIGEST_COPY_FILES`, at drafting time.
3. **Source-acquisition entry successor**, candidate and installed copies,
   whose subject admits a standing-admitted pair; version-tagged sign-off.
4. **Gate.** `gate-sources.ts`: per-repository forms first (Redis
   unchanged); otherwise the standing route, the admission entry, the
   identity, commit and URL exclusions, and the drawer statement from the
   standing record. Generalize `DRAWER_FORMS` and `STATEMENT_FORMS` off the
   `redis-redis` key so a governed public tree can carry its own statement.
5. **Run start and disclosures.** `init`/`preflight` take URL, fork,
   identity and the publication declaration; the one-commit clone shape
   stays; run record and pages disclose REQ-037's list. If the owner admits
   history: the reader admits ancestor commit objects and withholds identity
   lines.
6. **Draft schema, checker and renderer for REQ-038** (basis field, premise
   and trail, reconstructed marker, path-class check), and the fidelity
   verdict's per-block classification.
7. **REQ-039**, only if 10b is reversed.
8. **Brief and agent texts.** Reader topics in `brief.ts` and the
   `/polaris-dossier` skill.
9. **Install.** `proposed/` to `specs/`, `--write-additions`, recount,
   `PROJECT-STATUS.md` figures, `DIRECTIVE-REGISTER.md`, the
   `openspec/README.md` row, in one install script in the style of
   `scripts/install_redis_local_agent_sitting.py`.
