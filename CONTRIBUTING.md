# Contributing

## Current posture: not accepting external contributions

Syzygy is in **final pre-specification**. There is no application code, and
**no license has been declared** — so there is no grant under which an
external code contribution could be made or accepted. Until the owner
declares a license, all rights are reserved. Issues and discussion are
welcome; pull requests cannot yet be accepted.

## The no-implementation boundary

Nothing in this repository may add application or library code, choose a
stack, create behavioral-specification changesets, or build an
implementation backlog until the foundational contracts are accepted and
specification authoring formally opens. This binds the project's own agents
today and would bind contributors later.

## Authority layers

Authority is typed; each question has one owning home (see the README's
authority table). The load-bearing distinction for any change:

- **Adopted/approved** — doctrine, decisions, craft-and-care policies.
  Changing these is an owner-gated amendment, always.
- **Candidate** — design contracts, topology, overview, policy additions.
  These may be revised by agents *as drafts*, but only the owner accepts
  them, and never implicitly.
- **Derived** — indexes, summaries, status pages, this file. Regenerate
  freely; they are never authority and never cited as such.

A rule about writes, often misread: doctrine VIS-5 confines **Syzygy the
system's** direct project-content writes to `openspec/**` and `.syzygy/**`.
That is a product rule, not a contributor rule — people and agents working
on this repository edit the front door, CI, and skills too. The contributor
rule is simpler: documentation and governance artifacts only, through the
disciplines below.

## How to propose a documentation or contract change

1. **Find the owning artifact** — one authoritative home per fact; edit the
   owner, cite it everywhere else.
2. **Write a semantic delta** for any normative change:
   `.syzygy/governance/contracts/candidates/policy-candidates/SEMANTIC-DELTA-TEMPLATE.md`
   records current meaning, proposed meaning, change class (Editorial /
   Clarifying / Normative / Structural), warrant, impact, and what
   explicitly does not change. "Editorial" and "no semantic change" are
   reviewable claims, not exemptions. Whole-file rewrites are exceptional
   and require justification plus a mapping.
3. **Preserve stable IDs** — clause and rule identifiers are amended in
   place or retired, never renumbered.
4. **Expect fresh-context review** — material normative changes are reviewed
   by a session given only the artifact, its governing references, and
   acceptance criteria; never the authoring conversation. Raw reviewer
   output is stored verbatim; verdict words are copied exactly.
5. **Never edit a digest-bound artifact after its act** — it voids the act.
   Propose a re-offer instead.

## Public-clone validation is part of done

Any governance change must leave a fresh `git clone` able to reconstruct the
project's current shape: run the validation commands in `PROJECT-STATUS.md`
("How to verify this page") plus `python3 scripts/check_governance.py`, and
confirm no active artifact depends on the git-excluded `_bootstrap/**` tree
for essential meaning (citing it as unavailable history is fine; needing it
is not).

## Vendored external material

`.claude/skills/th-engineering/` and `.codex/skills/th-engineering/` are a
byte-identical, MIT-licensed vendored copy of the `engineering-bar`,
`test-rigor`, and `dependency-hygiene` subskills that
`.syzygy/governance/policies/craft-and-care/` adopts by reference (owner
override, 2026-08-06). It is tooling configuration, not application or
library code, and not authored here — do not edit it to satisfy a local
checker or to add Syzygy-specific rules; overrides belong in
`craft-and-care/` instead. Provenance, exact commit, and recomputable
digests: `.syzygy/governance/policies/GOVERNANCE-SUBSTRATE-LOCK.yaml`
(`th_engineering`).

## Where Beads applies

`bd` (Beads) tracks process housekeeping during this phase. It is **not**
used for product work: no implementation issues, epics, or backlog exist,
and none may be created before specification authoring opens. Unknowns go to
the pending-decision queue, not the tracker.

## Reporting a problem in the governance material

Contradictions between artifacts are **surfaced, never silently
reconciled**. If two documents disagree, report both readings rather than
choosing one — a contradiction renders the affected conclusion Unknown and
routes to the owner.
