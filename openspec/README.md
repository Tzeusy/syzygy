# `openspec/` — where this project's specifications live

> **Navigation only. Never authority, and nothing here binds.** This page
> says which change is in force and under which owner act; it restates no
> requirement, no digest and no verdict. Where it and the act record
> disagree, the act record wins. Current state is
> [`PROJECT-STATUS.md`](../PROJECT-STATUS.md); the acts themselves are in
> [`.syzygy/governance/decisions/`](../.syzygy/governance/decisions/).
>
> Written 2026-09-07 on the owner's P-57 ruling, arm (a), which authorized
> an agent to add a navigation page here and reserved the owner's review of
> its text — see
> [`DOCUMENTATION-ESTATE-OWNER-RULINGS-DECISION.md`](../.syzygy/governance/decisions/DOCUMENTATION-ESTATE-OWNER-RULINGS-DECISION.md).
> It is the governed plane's only agent-authored page and it holds no
> obligations, by design.

## The three changes, and what state each is in

Every change lives under `changes/`. None of the directory names says which
is which, so this table does — one row per directory, the act named, never
quoted.

| Directory | What it specifies | State | The act |
|---|---|---|---|
| [`project-registration-and-honest-shape-visibility`](changes/project-registration-and-honest-shape-visibility) | Capability 1 — project registration and honest shape visibility | **Adopted 2026-08-20, and implemented.** Amend only through CC-REV-2 | [`CAPABILITY-1-SPECIFICATION-ADOPTION-ACT.md`](../.syzygy/governance/decisions/CAPABILITY-1-SPECIFICATION-ADOPTION-ACT.md) |
| [`three-surface-poc-experience`](changes/three-surface-poc-experience) | The bounded, non-release Three-Surface POC (Polaris, Trajectory, Orrery) | **Signed off 2026-08-30.** A bounded experiment, never a release | [`THREE-SURFACE-POC-SPEC-SIGNOFF-ACT.md`](../.syzygy/governance/decisions/THREE-SURFACE-POC-SPEC-SIGNOFF-ACT.md) |
| [`polaris-project-wide-butlers-model`](changes/polaris-project-wide-butlers-model) | The project-wide Butlers slice of Polaris — one consented content class, behind the authority gate | **Signed off 2026-08-31, amended twice since** (2026-09-02, 2026-09-05). Every byte is bound at an exact digest | [`POLARIS-PROJECT-WIDE-SPEC-SIGNOFF-ACT.md`](../.syzygy/governance/decisions/POLARIS-PROJECT-WIDE-SPEC-SIGNOFF-ACT.md), then [`PWB-STATE1-AMENDMENT-ACT.md`](../.syzygy/governance/decisions/PWB-STATE1-AMENDMENT-ACT.md) and [`PWB-TRUTH-READINESS-AMENDMENT-ACT.md`](../.syzygy/governance/decisions/PWB-TRUTH-READINESS-AMENDMENT-ACT.md) |

Two of the three proposals open with a "Candidate specification… binds
nothing" banner that stopped being true the moment the act was performed.
The banner is not a mistake anyone may repair: the act bound the bytes that
carry it. The third proposal carries no banner at all and cannot be given
one for the same reason. **Read the act column above, never a proposal's
head** — that is why this page exists.

## The two empty directories

`specs/` and `changes/archive/` are the OpenSpec convention's homes for
settled material. This project does not use either step, on the owner's
P-55 ruling of 2026-09-07, arm (b): a change stays where it was authored,
and "what is specified today" is answered by
[`PROJECT-STATUS.md`](../PROJECT-STATUS.md) and the governed plane. Each
directory carries a one-line README saying so, so its emptiness stops
reading as an omission. Archiving an adopted change would relocate bytes
bound by digest, which is an act — not a tidying step.

## Adding a change

The bar and the ceremony are elsewhere, and this page does not summarize
them: see
[`HOW-TO-AUTHOR-A-SYZYGY-SPEC.md`](../.syzygy/governance/contracts/candidates/HOW-TO-AUTHOR-A-SYZYGY-SPEC.md).
One coherent category per change, overlapping no other change. Only the
owner's sign-off binds it (VIS-4); until then it binds nothing, whatever
its head says.

`config.yaml` holds one live setting, `schema: spec-driven`. Its `context:`
block is deliberately absent — an authoring agent's standing instruction
lives in [`AGENTS.md`](../AGENTS.md), not in tool config (owner's P-54
ruling, 2026-09-07, arm (b)).
