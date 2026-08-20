# How to author a Syzygy specification

> **Generated-style router — never authority.** Every rule here is owned
> elsewhere; this file cites the owner and invents nothing. Where this
> file and an owning source disagree, the source wins and this file is
> stale. **Capability 1's specification is authored and ADOPTED** — the
> owner's launch decision of 2026-08-20 authorized the authoring
> (`decisions/CAPABILITY-1-SPECIFICATION-AUTHORING-DECISION.md`) and the
> owner's adoption act (dated 2026-08-20, recorded at
> `decisions/CAPABILITY-1-SPECIFICATION-ADOPTION-ACT.md`) adopted the one
> change `openspec/changes/project-registration-and-honest-shape-visibility/`
> at exact digests. Implementation stays separately unauthorized. Every
> other capability's authoring stays unauthorized; the prerequisites table
> in `FIRST-OPENSPEC-SEQUENCE.md` (routed below at E2) is the gate-state
> record.

## The five questions and their owners (E1)

| Question | Owner | Where |
|---|---|---|
| **Form / version** — what medium, which OpenSpec | Owner decision **P-39** (**ruled 2026-08-16** — OpenSpec pinned at 1.9.0) + the adapter contract | substrate lock `openspec` block (the ruling's record); `decisions/OPENSPEC-FORM-AND-VERSION-DECISION.md` (the packet); RFC 0004 (adapter contract) |
| **Home / identity** — where specs live, how they are identified | RFC 0003 / RFC 0004 (candidate, Wave A) | `rfcs/RFC-0003/manifests-and-namespace.md` (spec root `openspec/`, fixed; closed declaration fields; RFC3-26 migration boundary); RFC 0004 for identity-survival obligations |
| **Granularity** — what one specification comprises | Owner decision **P-40** (**ruled 2026-08-16** — recorded as **SDR-37**: one change, one coherent capability, one acceptance decision) | `decisions/SURFACE-DECISION-RECORD.md` (SDR-37, the ruling); `decisions/SPECIFICATION-GRANULARITY-DECISION.md` (the packet) |
| **Acceptance authority** — who adopts a spec | Doctrine **VIS-4** (adopted) | `doctrine/vision.md` — the owner, until the compound doctrine-amendment event VIS-4 defines; no agent adopts |
| **Change process** — how a spec changes after adoption | Craft **CC-REV-2** (owner-approved) + `/th-projects project-feature-request` workflow | `policies/craft-and-care/review-and-documentation.md` (same-logical-change merge invariant); the th-projects workflow (referenced, never authority) |

## Which side of the shape/spec boundary a sentence falls on (E4)

One classification rule, owned by the eleven phase-rule clauses
(RFC1-33, RFC2-26, RFC3-33, RFC4-30, RFC5-27, RFC6-28, RFC7-38, RFC8-32,
RFC9-52, RFC10-16, RFC11-12) and the
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

Owned by the craft rule set
`policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` —
**CC-SPEC-1…11, in force as of 2026-08-17** (craft act 6, P-41 executed;
recorded in `decisions/ACCEPTANCE-ACT-RECORD.md` and the craft
`INSTALL-RECORD.md`; the file binds at its committed home, uncopied and
unedited).

## What happens when shape changes after specs exist (E6)

Owned by craft CC-REV-2 (the merge invariant) with the propagation path
recorded in `round-2026-08e/SHAPE-TO-SPEC-PROPAGATION-FIXTURE.md`'s
governing description:

```text
shape delta
→ affected-spec enumeration (blast-radius sweep, denominator recorded)
→ interim contradiction/Unknown rendered, never hidden
→ responsible amendment named — same logical change (CC-REV-2)
→ re-evaluation of affected acceptance criteria
```

**Two honesty limits, disclosed (RD28-04):** the affected-spec enumeration
step has **no craft owner today** — it is proposed in the candidate
normative-change workflow, whose own disclaimer says its script-checkable
sweeps "do not exist as checks yet"; and CC-REV-2 contains **no exception
limb** — its only carve-out is doctrine's owner gate (VIS-4), so a shape
change's author owns the spec amendments in the same logical change,
full stop. The launch-gate pilot failed E6 on detection; the paper dry-run
fixture repairs the *worked-example* gap, not the detection gap.

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
implementation. The Capability 1 specification **was adopted by the owner
at an exact digest** (act dated 2026-08-20;
`decisions/CAPABILITY-1-SPECIFICATION-ADOPTION-ACT.md`, per VIS-4 and
CC-SPEC-10) — and **implementation stays forbidden**: the adoption
authorizes none, and the separate implementation-authorization act has
not been performed.
