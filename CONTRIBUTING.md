# Contributing

## Current posture: licensed, but not accepting code contributions

The repository is licensed **MIT** (owner ruling P-14, 2026-08-18 — see the
root `LICENSE` and
`.syzygy/governance/decisions/LICENSE-CHOICE-DECISION.md`), so reuse rights
are granted. External **code** contributions still cannot be accepted, because
contributor-agreement posture is an open owner decision — not because the
project has no code. Issues and discussion are welcome; documentation and
governance proposals follow the disciplines below.

*Superseded, dated:* until 2026-09-05 this section opened "Syzygy is in
**final pre-specification**" and gave the reason for refusing code as "there
is no application code and the no-implementation boundary below binds
everyone." Both were true when written on 2026-08-19 and stopped being true on
2026-08-21, when Capability 1 implementation was authorized. What is
implemented today, and under which act, is `PROJECT-STATUS.md`'s row, not
this page's.

## The implementation boundary

Implementation is not open-ended: code may be added only where a **named owner
act** authorizes it, and anything no act covers is forbidden. Find the act
before writing code — `AGENTS.md` ("Where authority lives") routes to it, and
`PROJECT-STATUS.md` says which acts are in force. This binds the project's own
agents today and would bind contributors later.

*Superseded, dated:* this section was headed "The no-implementation boundary"
and read "Nothing in this repository may add application or library code,
choose a stack, create behavioral-specification changesets, or build an
implementation backlog until the foundational contracts are accepted and
specification authoring formally opens" until 2026-09-05. That described the
pre-specification stage correctly and was overtaken by the acts that opened
specification authoring and then authorized implementation. The gate did not
disappear; it moved from "none at all" to "only what an act names.

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

`bd` (Beads) tracks process housekeeping, the implementation backlog, and the
POC improvement cycles — see `AGENTS.md`, "Beads scope", which owns this rule.
Unknowns still go to the pending-decision queue, not the tracker: an open
question for the owner is not a task.

*Superseded, dated:* until 2026-09-05 this section read "It is **not** used
for product work: no implementation issues, epics, or backlog exist, and none
may be created before specification authoring opens." True when written on
2026-08-19; false from the first implementation epic onward.

## Reporting a problem in the governance material

Contradictions between artifacts are **surfaced, never silently
reconciled**. If two documents disagree, report both readings rather than
choosing one — a contradiction renders the affected conclusion Unknown and
routes to the owner.
