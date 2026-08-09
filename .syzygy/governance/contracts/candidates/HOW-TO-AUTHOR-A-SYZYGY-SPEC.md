# How to author a Syzygy specification

> **Generated-style router — never authority.** Every rule here is owned
> elsewhere; this file cites the owner and invents nothing. Where this
> file and an owning source disagree, the source wins and this file is
> stale. **No specification may be authored yet** — the prerequisites
> table at the end is the current gate state, and `openspec/` does not
> exist until the owner authorizes it.

## The five questions and their owners (E1)

| Question | Owner | Where |
|---|---|---|
| **Form / version** — what medium, which OpenSpec | Owner decision **P-39** + the adapter contract | `decisions/OPENSPEC-FORM-AND-VERSION-DECISION.md`; RFC 0004 (adapter contract); substrate lock `openspec` pin |
| **Home / identity** — where specs live, how they are identified | RFC 0003 / RFC 0004 (candidate, Wave A) | `rfcs/RFC-0003/manifests-and-namespace.md` (spec root `openspec/`, fixed; closed declaration fields; RFC3-26 migration boundary); RFC 0004 for identity-survival obligations |
| **Granularity** — what one specification comprises | Owner decision **P-40** | `decisions/SPECIFICATION-GRANULARITY-DECISION.md` — one coherent capability, one product argument, one acceptance decision |
| **Acceptance authority** — who adopts a spec | Doctrine **VIS-4** (adopted) | `doctrine/vision.md` — the owner, until the compound doctrine-amendment event VIS-4 defines; no agent adopts |
| **Change process** — how a spec changes after adoption | Craft **CC-REV-2** (owner-approved) + `/th-projects project-feature-request` workflow | `policies/craft-and-care/review-and-documentation.md` (same-logical-change merge invariant); the th-projects workflow (referenced, never authority) |

## Which side of the shape/spec boundary a sentence falls on (E4)

One classification rule, owned by the six phase-rule clauses and the
routing matrix's route table (`SURFACE-CLAUSE-ROUTING-MATRIX.md` — the
matrix is enumeration, never authority):

```text
load-bearing semantic design                  → RFC (shape)
independently testable human/machine behavior → OpenSpec requirement
review / release discipline                   → craft policy
rationale                                     → informative text
```

A sentence with both an invariant limb and an observable limb splits: the
RFC keeps the invariant, the observable limb routes to OpenSpec (the
matrix's OS route). A reviewed "no independently testable behavior"
judgment (N/A) is a judgment on the record, never a default.

## What an acceptable specification is (E5)

Owned by the candidate craft rule set
`policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` (ten
conditions; candidate until its own craft act).

## What happens when shape changes after specs exist (E6)

Owned by craft CC-REV-2 (the merge invariant) with the propagation path
recorded in `round-2026-08e/SHAPE-TO-SPEC-PROPAGATION-FIXTURE.md`'s
governing description:

```text
shape delta
→ affected-spec enumeration (blast-radius sweep, denominator recorded)
→ interim contradiction/Unknown rendered, never hidden
→ responsible amendment named
→ same logical change, or an explicit recorded exception
→ re-evaluation of affected acceptance criteria
```

## The first specification (E2)

**Capability 1 — Project registration and honest shape visibility**, per
the single current sequence document `FIRST-OPENSPEC-SEQUENCE.md` (beside
this file). Its prerequisite states — satisfied / owner-waived /
blocking / not applicable — live in that document's table; the E3 trace
of every first-spec concept to its governing shape artifact is
`round-2026-08e/FIRST-SPEC-TRACE-TABLE.md`.

## Hard boundary, restated from authority

Doctrine (VIS-4, VIS-5) and every contract's phase rule: user-observable
behavior receives an approved OpenSpec requirement **before**
implementation; specifications are authored only after the owner's launch
decision; `openspec/` is created by that authorized first changeset,
never by preparation work — including this file's.
