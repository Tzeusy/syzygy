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
> obligations, by design. **The owner approved this text 2026-09-08**; the
> reservation is discharged and this banner is not edited further to say so
> again.

## The five changes, and what state each is in

Five changes are in force by act; a Polaris addition bound later by a
sign-off or an owner direction is in force beside them and is not one of
the five. Each row names the act or record that adopted it and the
latest act or sign-off that binds its current bytes. Every change lives
under `changes/`, and none of the directory names says which is which, so
this table does — one row per directory, each act named, never quoted.
The sixth and seventh rows below are candidates that no act binds; they are
listed so that the table stays one row per directory, and neither is one of
the five.

| Directory | What it specifies | State | First act · latest binding outcome |
|---|---|---|---|
| [`project-registration-and-honest-shape-visibility`](changes/project-registration-and-honest-shape-visibility) | Capability 1 — project registration and honest shape visibility | **Adopted 2026-08-20, and implemented.** Amend only through CC-REV-2 | [`CAPABILITY-1-SPECIFICATION-ADOPTION-ACT.md`](../.syzygy/governance/decisions/CAPABILITY-1-SPECIFICATION-ADOPTION-ACT.md) · [`CAPABILITY-1-READABILITY-SUCCESSOR-ACT.md`](../.syzygy/governance/decisions/CAPABILITY-1-READABILITY-SUCCESSOR-ACT.md) (2026-09-29) |
| [`three-surface-poc-experience`](changes/three-surface-poc-experience) | The bounded, non-release Three-Surface POC (Polaris, Trajectory, Orrery) | **Signed off 2026-08-30.** A bounded experiment, never a release | [`THREE-SURFACE-POC-SPEC-SIGNOFF-ACT.md`](../.syzygy/governance/decisions/THREE-SURFACE-POC-SPEC-SIGNOFF-ACT.md) · [`THREE-SURFACE-POC-READABILITY-SUCCESSOR-ACT.md`](../.syzygy/governance/decisions/THREE-SURFACE-POC-READABILITY-SUCCESSOR-ACT.md) (2026-09-29) |
| [`polaris-project-wide-butlers-model`](changes/polaris-project-wide-butlers-model) | The project-wide Butlers slice of Polaris — one consented content class, behind the authority gate | **Signed off 2026-08-31, amended since by a chain of acts and version-tagged sign-offs.** Every byte is bound at an exact digest | [`POLARIS-PROJECT-WIDE-SPEC-SIGNOFF-ACT.md`](../.syzygy/governance/decisions/POLARIS-PROJECT-WIDE-SPEC-SIGNOFF-ACT.md) · [`PWB-READABILITY-SUCCESSOR-SIGNOFF-v1.0.md`](../.syzygy/governance/decisions/PWB-READABILITY-SUCCESSOR-SIGNOFF-v1.0.md) (2026-10-02) · [`PWB-TREE-FRAMING-AMENDMENT-SIGNOFF-v1.0.md`](../.syzygy/governance/decisions/PWB-TREE-FRAMING-AMENDMENT-SIGNOFF-v1.0.md) (2026-10-03) |
| [`polaris-manifesto-generation`](changes/polaris-manifesto-generation) | The generalized Polaris manifesto generator (base requirements) | **Adopted 2026-09-12.** Read only together with the understanding amendment below | [`POLARIS-GENERATOR-SPECIFICATION-ADOPTION-ACT.md`](../.syzygy/governance/decisions/POLARIS-GENERATOR-SPECIFICATION-ADOPTION-ACT.md) · [`POLARIS-GENERATOR-BASE-READABILITY-SUCCESSOR-ACT.md`](../.syzygy/governance/decisions/POLARIS-GENERATOR-BASE-READABILITY-SUCCESSOR-ACT.md) (2026-09-29) |
| [`polaris-manifesto-understanding-amendment`](changes/polaris-manifesto-understanding-amendment) | The overlay that modifies seven generator requirements and adds two | **Adopted 2026-09-13; requirement 004 replaced 2026-09-28** by the tree-form amendment ([`POLARIS-TREE-FORM-AMENDMENT-ADOPTION.md`](../.syzygy/governance/decisions/POLARIS-TREE-FORM-AMENDMENT-ADOPTION.md)) | [`POLARIS-UNDERSTANDING-SPECIFICATION-ADOPTION-ACT.md`](../.syzygy/governance/decisions/POLARIS-UNDERSTANDING-SPECIFICATION-ADOPTION-ACT.md) · [`POLARIS-UNDERSTANDING-READABILITY-SUCCESSOR-ACT.md`](../.syzygy/governance/decisions/POLARIS-UNDERSTANDING-READABILITY-SUCCESSOR-ACT.md) (2026-09-29) · [`POLARIS-UNDERSTANDING-DEPENDENCY-UNION-SUCCESSOR-ACT.md`](../.syzygy/governance/decisions/POLARIS-UNDERSTANDING-DEPENDENCY-UNION-SUCCESSOR-ACT.md) (2026-10-02, `GOVERNING-DEPENDENCIES.md` only) |
| [`polaris-non-governed-narrative-profile`](changes/polaris-non-governed-narrative-profile) | A candidate Polaris generator requirement for narrating an observed repository that has no Syzygy declarations | **Candidate — binds nothing; not one of the five in force.** Its delta sits in `proposed/`, not `specs/`; no owner act exists over it | None; review and owner packet: [`non-governed-narrative-profile`](../.syzygy/governance/contracts/candidates/non-governed-narrative-profile/) |
| [`polaris-dossier-local-agent-mode`](changes/polaris-dossier-local-agent-mode) | A candidate operator-agent authoring mode for the Polaris generator: the operator's own coding-agent session writes a dossier, Syzygy pins, checks and renders it | **Candidate — binds nothing; not one of the five in force.** Its delta sits in `proposed/`, not `specs/`; no owner act exists over it | None; review and owner packet: [`polaris-dossier-local-agent-mode`](../.syzygy/governance/contracts/candidates/polaris-dossier-local-agent-mode/) |

The PWB chain between its first and latest outcome, and every other bound
digest, is listed in
[`ACCEPTANCE-ACT-RECORD.md`](../.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md).
The 2026-10-02 reconciliation of all five is
[`docs/evidence/spec-readability-reconciliation-2026-10-02/`](../docs/evidence/spec-readability-reconciliation-2026-10-02/README.md),
and `scripts/check_spec_reconciliation.py --check` re-derives it.

**Read the act column, never a file's head.** Since the readability
successors no proposal carries a pre-adoption candidate banner (the POC's
carries no status line at all), but three `spec.md` files still open with
the candidate banner they were signed with: the POC's, the generator base's
and the understanding amendment's. The banner is not a
mistake anyone may repair in place, because the act bound the bytes that
carry it; only a signed successor can replace it.

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
