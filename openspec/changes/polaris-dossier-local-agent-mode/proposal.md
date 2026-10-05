# Polaris dossier local-agent mode

> **Candidate — binds nothing.** Drafted 2026-10-05 under the owner direction
> `POLARIS-DOSSIER-LOCAL-AGENT-MODE-2026-10-05`, recorded in
> `POLARIS-DOSSIER-LOCAL-AGENT-MODE-DIRECTION.md` in the decisions home (it
> lands by PR #351 and is not on `main` at this change's base), which
> authorizes drafting and review only. It is not adopted, performs no
> act, and grants no read, egress, write or execution. Effect comes only from
> the owner's sign-off of the exact reviewed bytes (VIS-4).

**A Polaris dossier can be written by the operator's own Claude Code or Codex
session over a local clone, while Syzygy checks every quotation against the
pinned Git objects, runs a fresh-context review step and renders the pages,
and makes no provider call itself.** This change adds that operator-agent mode
to the `polaris-generation` capability, beside the provider mode the adopted
requirements describe.

## Why

On 2026-10-05 the owner wrote that dossier generation "should be purely done
by a human using claude-code or codex, a provided syzygy binary, and the
target codebase cloned locally", with no API key, and then directed the mode. The adopted generator requirements
assume the opposite: Syzygy calls the model through a registered provider
route, under stage budgets it enforces, with provider receipts for usage, an
independent inventory and review that Syzygy dispatches, and a discovery
account Syzygy produces from its own reads. Those requirements cannot be met
literally when the model runs in the operator's session, and meeting them by
pretence (receipts Syzygy never saw, a "registered route" that is the
operator's terminal) would break VIS-2. The direction routes the change
through one reviewed CC-REV-2 delta.

## What changes

- **Added:** four requirements, 033 to 036, in the existing
  `polaris-generation` capability:
  - 033 Operator-agent authoring mode: mode selection, clone pinning to a
    consented revision, Git-object reads only, no provider call, the
    operator's declared limits, unobserved agent usage, and the disclosure.
  - 034 Agent brief and mechanically checked draft: the brief, the labelling
    and quotation rules, the draft schema, the quote, path and label checks
    with repair findings, and rendering.
  - 035 Fresh-context review in the operator-agent mode: inventory and review
    contexts, the review packet, verdict validation, and what independence
    can and cannot be shown.
  - 036 Self-reported discovery and in-session clarification.
- **Modified in effect, not in bytes:** for an operator-agent run the new
  requirements displace or read named text of REQ-polaris-generation-005,
  006, 017, 018, 030 and 031, and of the base change's `INTERFACES.md`
  (Provider bullet; "Budget and retry decisions"). Each displaced sentence is
  quoted in the semantic delta. For a provider-mode run nothing changes.
- **Not displaced, and put to the owner:** the draft-layer consent sentence of
  REQ-polaris-generation-001 and the consent condition of RFC7-20, an accepted
  contract this change cannot amend. Until the owner rules (owner question
  O1), an operator-agent draft layer renders Unknown
  (`unconsented-source-or-provider`) exactly as 001 requires.
- **Parked, not withdrawn:** the provider mode and its route, egress and
  adapter packages, per the direction's item 4.

## Capabilities

- **Modified:** `polaris-generation`, by four added requirements.
- **New:** none. The mode is a way of running the same generator, in the way
  requirements 030 and 031 extended it.

## Amendment relation

- It amends the composition of `openspec/changes/polaris-manifesto-generation/`
  and `openspec/changes/polaris-manifesto-understanding-amendment/`, as
  amended by the tree-form adoption. No byte of either is edited.
- It is independent of the candidate
  `openspec/changes/polaris-non-governed-narrative-profile/` (requirement 032)
  and overlaps it nowhere: 032 says how a non-governed subject's narrative is
  composed, this change says who authors it and how Syzygy checks it. A Redis
  dossier needs both. The numbers 033 to 036 follow 032; if 032 is never
  adopted the gap stays, because identifiers are never renumbered.
- **The candidate delta is held in `proposed/`, not `specs/`,** for the reason
  the profile change gives: `scripts/count_polaris_effective_scenarios.py`
  requires exactly one base and one overlay. Placing it in `specs/` is a step
  of adoption, taken with that script's generalization (`tasks.md`).
- Never archive or sync this as an unrelated competing change.

## Scope and preserved boundaries

- **Syzygy's own reads keep every gate.** Observation consent, the observer
  registry entry, and the classification and screening policy acts apply to
  every Git object Syzygy reads, unchanged (direction item 3).
- **Who sends is the ruling, not whether consent is needed.** The agent's
  sends to its provider are the operator's own act (direction item 2). Every
  transmission Syzygy itself makes still traverses the egress check of
  REQ-polaris-generation-025; in this mode Syzygy makes none.
- **Unobservable things stay Inferred or unrecorded.** What the agent read,
  how much it spent and whether its review contexts were fresh are
  operator-declared or self-reported, and the page says so. Only Syzygy's own
  reads, checks and steps are Observed.
- **Governed subjects stay in the provider mode** until the owner rules
  otherwise (owner question O2).
- **No new permission.** This is not permission to read, egress, write,
  execute observed code, deploy, release or adopt intent.

## Impact

- **Generation core:** a local-agent draft schema and adapter onto the
  existing quote check, schema validation, review validation and dossier
  evaluation.
- **App:** a `syzygy dossier` command family (design only: `design.md`), the
  consent reader of PR #263 (open, not on main), Git-object reads by
  identifier, and the existing dossier renderer.
- **Agent harness:** a thin Claude Code skill and Codex instructions that
  drive the loop (text in `design.md`; not installed by this change).
- **Authority unchanged.** The generator's authority remains what its
  performed acts say. Implementation that depends on this change waits for
  the owner's sign-off (direction item 5).
