# Governance-reduction plan — candidate

> **A plan, not a decision.** This file proposes how the process surface
> shrinks as the repository crosses from pre-specification governance
> into specification-driven work. It decides nothing, retires nothing,
> and schedules nothing; every retirement below happens only at the gate
> named for it, and the owner disposes. Written 2026-08-17
> (convergence pass, Workstream F). `[Inferred]` throughout except where
> a source's own text is cited.
>
> **Why it exists:** the governance corpus was built to make one launch
> decision safe. Left alone after that decision, it becomes exactly the
> kind of "process for its own sake" this plan itself warns against, not
> a phrase drawn from doctrine — every artifact below states what
> supersedes it, so the corpus can shrink on evidence rather than
> nostalgia.

## Principle

An artifact retires when the thing it existed to protect is protected by
something stronger — an accepted spec, a performed act, a generated view.
Retirement is a banner and a route change, never deletion: history stays
readable, but nothing retired sits on a default path (the
`round-*`/`history/` pattern already in force).

## 1. At the Wave A + B acts (P-1)

| Artifact | What happens |
|---|---|
| `wave-manifests/` + confirmations | Become the act record's evidence; rows for accepted waves stop being "candidate" state to re-verify each session |
| Wave semantic-delta chains (`round-2026-08e/`) | Already historical; no change — cited only from the acceptance record |
| `contracts/candidates/rfcs/` → `contracts/rfcs/` | Install shape (M), ruled: modules only, nothing else moves; the candidate tree's residual files stay put, off default paths |

## 2. At craft acts 6 + 7 (P-41/P-42)

| Artifact | What happens |
|---|---|
| `policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`, `…SHAPE-TO-SPEC-IMPACT…` | In force at the acted digest, recorded in the craft `INSTALL-RECORD.md`; the "candidate" banners retire at the act (the act, not an editing session, is what changes them — the acted digest binds the bytes as approved) |
| The RD-51/RD-69/RD-70 review chain and registers | Historical the moment the act binds; batched non-blocking findings (RD-69 N1–N5, RD-70 N1–N4) become the first post-act amendment's worklist, traveling by the normal amendment route |
| The P-44 offer | Rules independently; if declined (arm b), the offer file is banner-marked declined and CC-IMPACT-6's pointer text is the only trace |

## 3. When the first specification is accepted in OpenSpec

The largest reduction, and the charter names it itself: *"Once
Capability 1 is accepted in OpenSpec, the accepted specification
supersedes this charter for required behaviour and this file becomes
history."* `[Observed]`

| Artifact | What happens |
|---|---|
| `CAPABILITY-1-CHARTER.yaml` + generated views | Superseded by the accepted spec; banner-marked history; the view generators retire with it |
| `FIRST-OPENSPEC-SEQUENCE.md`, outline exercises (08f, 08i) | Purpose discharged; history |
| `SURFACE-CLAUSE-ROUTING-MATRIX.md` | Its coverage role transfers to the spec's own clause-to-requirement coverage matrix (CC-SPEC-8's deliverable); the matrix file stays as the routing record for *future* capabilities until each is spec-covered |
| `HOW-TO-AUTHOR-A-SYZYGY-SPEC.md` | Stops being router-only and becomes the live authoring guide — the one artifact that *grows* at this gate |

## 4. At and after the formal administration

| Artifact | What happens |
|---|---|
| `FORMAL-CAPABILITY-1-LAUNCH-PACKET/` | Purpose discharged at the first formal record in `decisions/launch-gate/`; banner-marked administered |
| Launch-gate semantic-delta chain (v1.4…v2.4, ~20 files) | Already historical in `round-*` trees; `HISTORY.md` remains the one index, never default context |
| Dry-run fixtures (`round-2026-08f/fixtures/`) | Retained — they are the validator's regression bed, not process surface |

## 5. Standing reductions, gate-independent

- **The battery shrinks with its subjects.** A check whose subject
  retires is itself retired *in the registry pattern* (an entry with a
  printed reason — the ACCEPTANCE-PHRASE-REGISTRY precedent), never
  silently deleted; CG-24's coverage figure keeps the denominator honest.
- **The decision surface stays two files**: open rows in
  `PENDING-OWNER-DECISIONS.md`, everything else in
  `DECISION-HISTORY.md` — the 2026-08-17 refactor is the model; packets
  of ruled decisions get the ✅ banner and leave default paths.
- **Context budget is the metric.** `scripts/context_load.py` and
  `06-CONTEXT-LOAD-MAP.md` own the measurement; a reduction that does not
  move the default-load figure is cosmetic and should not be claimed as
  reduction (verification rule 2 applies to this plan's own future
  claims).
- **AGENTS.md only shrinks.** Operating procedure grows by exception,
  paid for by a recorded incident (`PROCESS-LESSONS.md`), and every gate
  above should delete at least one routing row from it.

## What this plan refuses to do

No artifact is retired *by this plan*. No date is set. Nothing here
weakens doctrine, craft, or an accepted contract — reduction is of
*candidate scaffolding and completed process*, never of authority in
force. The owner may adopt, amend, or ignore this plan; until then it is
one more candidate, and it lists itself in §3's spirit: once the gates
above have all passed, this file too is history.
