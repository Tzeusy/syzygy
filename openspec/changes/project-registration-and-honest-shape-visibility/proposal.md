# Proposal — project-registration-and-honest-shape-visibility

> **Candidate specification.** Authoring was authorized by the owner's
> launch decision of 2026-08-20
> (`.syzygy/governance/decisions/CAPABILITY-1-SPECIFICATION-AUTHORING-DECISION.md`
> — authorization to author only, never a product-behavior warrant).
> Adoption is a separate exact-digest owner act (VIS-4; CC-SPEC-10);
> until that act, this change binds nothing.

## Why

An owner running a portfolio of projects cannot today ask one trustworthy
place "is this project registered, what may be inspected, and what shape
is it actually in?" — and get an answer that is honest about what is not
known. Tools that answer optimistically (a green badge computed from no
evidence, a coverage report that hides unconsented sources, a single
health score) are worse than no answer. Capability 1 establishes the
truthful project foundation every later view and every machine consumer
builds on: registration, consent boundaries, a fixed human entry, seven
independent shape answers, explanations, and repository discoverability —
with every Unknown carrying its reason.

**One-sentence capability:** A project can be registered and its shape
read honestly: every project answer stands on its own, every Unknown
carries its reason and owning authority, and humans and machines receive
the same facts — without registration being mistaken for certification.

**Why this capability is first:** every later capability's evidence is
uninterpretable without it — a comprehension view, a work view, or a map
over an unregistered project with an undisclosed consent boundary cannot
be trusted. The first-specification sequence's ordering rule ("the
capability whose absence would make the next one's evidence
uninterpretable goes first") selects it.

## What Changes

- **New capability**: project registration and honest shape visibility,
  specified as observable behavior in six groups — project declaration;
  consent and coverage; human project entry; independent project-shape
  answers; "Why this answer?" and human/machine parity; repository
  discoverability — plus cross-cutting no-false-success, parity,
  identity, and write-boundary requirements.
- No existing capability is modified (none exists; this is the first
  specification).

## Capabilities

- **New Capabilities**:
  - `project-registration-and-honest-shape-visibility` — one coherent
    capability, one owner-readable product argument, one future
    acceptance decision (SDR-37).
- **Modified Capabilities**: none.

## Scope

In scope: reading and validating the project declaration; recording and
showing consent and repository coverage; serving the fixed human entry
`.syzygy/intent/OVERVIEW.md`; computing and presenting the seven
owner-ratified project-shape answers independently; explaining every
answer with the same facts to humans and machines; reporting
per-repository discoverability in the closed four-value vocabulary; and
proposing (never writing) a repository-entry link.

## Non-goals

Capability 1 does **not**: certify a project; produce any overall health
or maturity score; implement Polaris's full project white paper;
implement Trajectory work ingestion or execution accounting; implement
Orrery's 3D project map; execute or monitor Missions; generate
task-specific context packets; calculate complete intent-to-code
convergence; modify source code; edit a repository root README; create
Beads work; select an implementation language, framework, database,
renderer, graph store, or deployment model; register or onboard a real
external project during specification authoring; implement anything.
These are true scope boundaries, not promises that every item is next.

## User-visible outcomes

A human can: register a project by declaration and see exactly why an
invalid declaration failed; see what Syzygy may and may not inspect, as
facts; open one fixed entry path and be routed to exact authority; read
seven independent shape answers with no combined score; ask "Why this
answer?" of any answer and reach its facts; and see, per repository,
whether its ordinary entry helps a newcomer find the project entry.

## Machine-consumer outcomes

A machine client retrieves the same registration facts, coverage
boundary, shape answers, explanations, and discoverability findings the
human sees — same project identity, same revision, same evaluation
identity, same epistemic labels, verbatim vocabulary — through the
machine-queryable plane. No endpoint-only or UI-only facts exist.

## Unknowns

Stated in the specification's requirements and coverage tables. The
material ones: the concrete evidence basis for the `Human-understandable`
answer before any comprehension walkthrough exists (renders Unknown);
`Mission-ready` semantics (deferred with Waves C/D; renders
`not evaluated / deferred / Unknown`); reconciliation computation (V0
renders uncomputed reconciliation Unknown); and whether OpenSpec
requirement identities survive edit/rename (an RFC 0004 adapter
obligation, acknowledged and not resolved here).

## Impact

No code, APIs, or systems exist to be affected. Affected artifacts:
`openspec/**` (this change) and the repository's current-state pointer
documents. Implementation impact is deliberately unplanned — this change
authorizes nothing to be built.

## Acceptance approach

Owner adoption at an exact digest (VIS-4; CC-SPEC-10), judged under the
in-force CC-SPEC-1…11 standard, with the shipped capability-coverage and
contract-coverage tables (CC-SPEC-8, CC-SPEC-11) and three bounded
fresh-context reviews plus one confirming review as review material.
