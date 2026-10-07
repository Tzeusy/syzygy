# Design — Polaris dossier for an arbitrary public repository

> **Candidate — binds nothing.** Design sketch for the three added
> requirements in `proposed/polaris-generation/spec.md`. Line numbers are at
> `origin/main` `3409ef5a`.

## Which clauses require per-repository consent

The lead's working reading was that SEC-2 governs egress, not reads, so the
per-repository requirement comes from specifications and acts. **The first
half holds; the second does not.** The requirement is also in accepted
contracts and in adopted doctrine prose.

| Source | Text (quoted) | What it requires |
|---|---|---|
| SEC-2, `.syzygy/governance/doctrine/security.md:42-45` | "No governed-project content, or anything derived from it, is sent to a store or service the owner does not control — model providers included — without explicit, recorded, per-project consent." | [Observed] Egress only. It says nothing about reads. Local-agent mode makes Syzygy send nothing (REQ-033), so SEC-2 binds here only through REQ-033's per-project statement for governed subjects. |
| SEC-4, `security.md:116-117` | "writes need recorded per-repository consent (onboarding)." | [Observed] Writes only. |
| Doctrine, `.syzygy/governance/doctrine/architecture.md:26-27` | "Onboarding is recorded, per-repository consent (security.md SEC-4). **Every observed repository consents, governance root or not.**" | [Observed] Every observed repository, reads included. Unnumbered prose in adopted doctrine, so it carries no identifier and cannot appear in a warrants block. |
| Doctrine, `architecture.md:62-64` | "Every edge from Syzygy is gated: each observed repository, governance root included, has consented (SEC-4)" | [Observed] Same. |
| Doctrine glossary, `doctrine/README.md:25-26` | "every observed repository needs consent (architecture.md; security.md SEC-4)." | [Observed] Same. |
| RFC1-3, `contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md:178-181` | "Every observed repository — governance root or not — requires a recorded **Consent record** (SEC-4). No consent means no observation, and therefore **Unknown**" | [Observed] One recorded consent record per observed repository. Accepted contract. |
| RFC5-12, `contracts/rfcs/RFC-0005/consent-egress-secrets.md:99-100` | "**Observation consent** — per repository: Syzygy may read and index it (RFC1-3)." Line 111: "Every consent record names its class, subject, scope, granting principal, grant instant, and revocation state." | [Observed] The observation consent class is per repository, with six named fields. Accepted contract. |
| RFC3-30, `contracts/rfcs/RFC-0003/manifests-and-namespace.md:519-521` | "Role and consent are properties of the *(Project, repository)* pair (RFC3-7), never global: Project A observing repository R requires A's own consent record for R" | [Observed] Per pair. Accepted contract. |
| REQ-polaris-generation-025, `openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md:1400` | "Each consent record SHALL grant exactly one class with subject, scope, granting principal, grant instant and revocation state: observation/write consent per repository" | [Observed] The specification restates RFC5-12. |
| REQ-polaris-generation-033, `openspec/changes/polaris-dossier-local-agent-mode/specs/polaris-generation/spec.md:13` | "Before it issues a brief, Syzygy SHALL verify that the clone's checked-out HEAD commit equals a revision that the in-force observation consent for the repository names" | [Observed] The run-time gate. |
| REQ-033's governed predicate, same file, line 11 | "For a governed subject, and for a subject whose project input does not state whether a drawer exists, Syzygy SHALL refuse to issue a brief unless an in-force, recorded, per-project statement names the operator's agent provider" | [Observed] The source of the per-repository drawer or provider statement. |

**What this means for the act type.** [Inferred] A spec sign-off can read or
displace specification text (REQ-025, REQ-033) for these runs, as the
local-agent mode did. It cannot displace RFC1-3, RFC5-12, RFC3-30 or
doctrine. Two routes:

- **Reading (recommended).** The owner records that a standing admission,
  reaching one repository per run through an instance record that names the
  repository and carries every RFC5-12 field, *is* a recorded per-repository
  consent record. The literal text is met: each observed repository has a
  record naming it. What a reader could dispute is whether a grant given in
  advance, for repositories the owner has not named, is that repository's
  consent; only the owner can rule on that (VIS-4). Precedents: the bounded
  mission interpretation act
  (`decisions/BOUNDED-MISSION-DOCTRINE-INTERPRETATION-ACT.md`) and the
  RFC7-20 reading, bound to exact bytes by its in-force record.
- **Amendment.** A doctrine amendment to `architecture.md` (next log row
  after D9) plus an RFC-0005 amendment adding a standing class form to
  RFC5-12 and, by consistency, RFC1-3. Heavier, and leaves no room for a
  reader to dispute it. The D9 in-force record binds `security.md` and
  `v1.md` only (`gate-sources.ts:196`), so an `architecture.md` amendment
  would not disturb D9 [Observed].

## Decisions in this draft

### 1. One standing record, one instance per run

The standing admission is one record with its own owner act, drafted like the
Redis observation consent (`public-repo-admission/templates/OBSERVATION-CONSENT-TEMPLATE.md`).
It fixes: the class, observation; the subject form,
(`project:syzygy`, `repository:<declared identity>`), with the identity
format; the host rule; whether history is in scope; the exclusion list; and
the statement that no kernel evidence drawer exists for any repository
admitted only under it [Inferred true by construction: Syzygy keeps no
drawer for a repository it never onboards].

Each run writes an instance record in its state directory. It is not an act
and adds none. It carries RFC5-12's six fields, with the grant instant taken
from the standing act. The run's pinned commit is HEAD at that moment, which
is how REQ-033 already pins.

*Alternatives:* a per-repository act signed quickly (rejected, the owner asked
for none); a per-run owner confirmation command like the execution choice
(packet Q5; not recommended, see there).

### 2. Precedence: per-repository records win, permanently

A pair with **any** per-repository observation consent record, in force,
withdrawn or revoked, is outside the standing admission. This keeps Redis
exactly as it is. It also means a withdrawn consent can never be quietly
replaced by the standing one (RFC5-13: revocation is prospective and must
hold). A repository declared in any Syzygy project declaration (Syzygy
itself, Butlers) is excluded too: those keep their own consents.

### 3. No network request; public status is declared

Syzygy reads only the local `.git` through the registered in-process reader.
It cannot tell whether a repository is public without contacting the host,
and contacting the host would be a new effect needing its own adapter
(RFC4-1). So "public", "this commit is published upstream" and "the fork
mirrors upstream" are the operator's declarations, labelled Inferred. A
private repository or a private fork is outside the act's scope by its own
words, and a run that breaks that is the operator's breach, disclosed as
declared.

### 4. The governed rule

The drawer half comes from the standing record. The tree half uses the
predicate the gate already implements (`packages/polaris-dossier/src/governed.ts:4-12`):
a path segment `openspec` or `.syzygy` at any depth, after NFKC, case folding
and trailing dot and space removal. That reading was reviewed (R3-F9) as
"never less strict than a root-only, exact-case match"; this draft keeps it
rather than narrowing it. The cost: a repository that vendors a dependency
holding an `openspec/` directory counts as governed. Packet Q2 offers
root-only as an alternative.

**A governed tree** under the standing admission is refused at brief time
unless a per-repository agent-provider statement (the Redis 3a/3b form) is in
force, and is then composed under the governed readings of REQ-004, not the
non-governed profile. [Inferred] This keeps REQ-033 and SEC-2 exactly as
they are and costs one signature for what should be a rare repository.
*Alternative (packet Q2):* treat a third-party public tree as non-governed
for SEC-2 regardless, on the reading that SEC-2's "governed-project content"
means a project the owner brought under Syzygy, not any repository that
happens to use OpenSpec. That needs a reading of REQ-033's predicate and,
arguably, of SEC-2.

### 5. Reconstructed motivations

The adopted rule (REQ-002, base spec line 52) already allows source-supported
inference of motives and forbids speculation: "Motives, history, definitions
and relationships without sufficient source premises SHALL remain absent or
Unknown; an Inferred label alone SHALL NOT make speculation eligible." REQ-038
gives "sufficient premises" a checkable form for operator-agent runs:

- every motivation, trade-off, advantage or position block declares
  `maintainer-stated` (a verified quotation of maintainer text) or
  `reconstructed` (premises plus a trail);
- Syzygy checks the mechanics (basis present, quotation verifies, premises
  resolve, trail present);
- the fidelity review checks the substance (the span states it; the trail
  supports it), and an unsupported one blocks readiness;
- a reconstruction never replaces a maintainer statement, and a motive about
  people stays Unknown without a maintainer statement.

**History.** The owner named commit history as a source. The Redis consent
excludes ancestors, and the clone preflight now refuses a clone holding more
than one commit (open PR #392). A commit-message premise is therefore only
checkable if the standing record admits the pinned commit's ancestry (packet
Q1d). Without it, history premises fail the check rather than render
unverified.

### 6. Ruling 10b

Kept as the default: advantages stay maintainer-stated, and REQ-038 refuses a
reconstructed advantage. REQ-039 is drafted so that the owner can reverse 10b
and allow external comparisons as a separate, clearly marked section of the
agent's unverified report. Syzygy fetches nothing for it. If the owner keeps
10b, REQ-039 is struck before sign-off and the change is two requirements.

## What this change does not settle

- [Unknown] Whether a standing-admitted repository must also be declared as
  an observed-source repository in `project:syzygy`'s project declaration
  (RFC1-2, RFC1-4: role and membership come from the declaration). Redis is
  in the same position today; this change neither fixes nor worsens it.
- [Unknown] The exact form of the repository identity
  (`repository:<host>-<owner>-<name>` is the obvious candidate). Fixed in the
  standing record, not here.
- The source-acquisition entry's subject reads "each (project:syzygy,
  repository) pair that has its own in-force observation consent naming the
  pinned revision" (`public-git-source-acquisition-local-agent/proposed/POLARIS-PUBLIC-GIT-SOURCE-ACQUISITION-LOCAL-AGENT-CANDIDATE.json:58`).
  Whether the instance record satisfies "its own" under the reading, or the
  entry needs a successor version, is slice 3's question; this draft assumes
  a successor version.
- Requirement numbers 037 to 039 were free at `3409ef5a` (sweep F in
  `IMPACT-LEDGER.md`); a sibling change drafted in parallel could take them
  first.

## Implementation slices (after sign-off; not filed as beads)

Each is one cohesive, separately verifiable outcome. None starts before the
owner's acts are recorded.

0. **Record the owner's 2026-10-07 direction** as a plain owner direction in
   `decisions/` (no digest), so the warrants can cite it by identifier.
1. **Standing admission record and act.** Template and instance in
   `scripts/build_public_repo_admission.py`; a recorder row in
   `scripts/record_public_repo_admission_acts.py` (`ACTS`); the phrase in
   `check_governance.py` `_act_subjects()` and the packet copy in
   `ACT_DIGEST_COPY_FILES`, at drafting time.
2. **The reading (or amendment) record and its in-force act**, in the D9 and
   RFC7-20 form of `scripts/build_dossier_local_agent_acts.py`, with a
   gate-sources form beside `D9_ACT_FORM`.
3. **Source-acquisition entry successor** whose subject admits a
   standing-admitted pair; version-tagged sign-off.
4. **Gate.** `gate-sources.ts`: per-repository forms first (Redis unchanged);
   otherwise the standing route, the instance record, the drawer statement
   from the standing record, and the exclusion and project-declaration
   checks. Generalize `DRAWER_FORMS` and `STATEMENT_FORMS` off the
   `redis-redis` key so a governed public tree can carry its own statement.
5. **Run start and disclosures.** `init`/`preflight` take URL, fork and
   identity; run record and pages disclose the basis (REQ-037's list). If
   history is admitted, the one-commit clone rule (PR #392) relaxes for
   standing runs and the reader admits ancestor commits.
6. **Draft schema, checker and renderer for REQ-038** (basis field, premise
   and trail, commit-message citations, reconstructed marker); fidelity
   verdict fields.
7. **REQ-039**, only if 10b is reversed: the section, the marker and the
   repair finding when it is not.
8. **Brief and agent texts.** Reader topics in `brief.ts` and the
   `/polaris-dossier` skill.
9. **Install.** `proposed/` to `specs/`, `--write-additions`, recount,
   `PROJECT-STATUS.md` figures, `DIRECTIVE-REGISTER.md`, the
   `openspec/README.md` row, in one install script in the style of
   `scripts/install_redis_local_agent_sitting.py`.
