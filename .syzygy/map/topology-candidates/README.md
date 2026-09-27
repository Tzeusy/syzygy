# Syzygy Topology — Lay and Land (candidate bundle, draft)

> **Reviewed draft — grounded in candidate foundational contracts (currency note, not an ordering precondition: this bundle's own gate is §2 act 3 of the acceptance record and does not wait on the RFC act).** Reviewed fresh-context (reviews 5–7, dispositions recorded); updated at the rev7 rework for the corrected contracts (D1 historical scope, five governance categories, walkthrough three-way split, captured external confirmation, `Base` scenario context). Becomes canonical only by its **own owner act** — `ACCEPT TOPOLOGY: <bundle-manifest-digest>`, binding the exact digest of every file in the bundle — never implicitly on the RFC gate (RFC3-16: this stamp is a self-declaration; effective status lives in the owner-act record).

> Restyled 2026-09-28 for readability (no change of meaning); reviews 5–7 reviewed the prior bytes, and this restyle's review is recorded in [the topology restyle packet](../../governance/decisions/TOPOLOGY-TREE-RESTYLE.md).

Eight focused diagram documents draw the initial canonical topology of
Syzygy. Where a diagram and an RFC disagree, the RFC governs, including for
vocabulary.

- **Drawn from:** adopted doctrine (`.syzygy/governance/doctrine/`), the
  Surface Decision Record (SDR-1..33), and RFC drafts 0001–0006.

**Currency caveat.** These diagrams were drawn while the whole RFC set was
still in flight, and they lag it in both directions, so the RFC governs
wherever the two disagree.

- **Surface content predates its RFCs.** Surface-level content
  (Polaris/Trajectory/Orrery internals) is grounded in the SDR charter, not
  in RFCs 0007–0009, which did not yet exist.
- **The RFCs drawn from kept moving.** RFCs 0001–0006 continued to be
  amended after these were drawn: closed vocabularies grew and clause
  wording tightened.
- **Review 07 swept the cluster** against the current RFC text and repaired
  the drifts it found.
  - The repairs are in these files' bytes, which the bundle manifest binds.
  - Its fix report, `07-topology-FIX-REPORT.md`, was a founder-local process
    record under a `reviews/` tree that did not travel into the tracked
    repository.

## Index

Each file answers one question.

| File | Question it answers |
|---|---|
| [01-system-context.md](01-system-context.md) | Who and what surrounds Syzygy, and across which trust boundaries? |
| [02-project-workspace-repos.md](02-project-workspace-repos.md) | How do workspace, Projects, governance roots, observed-source repos, and consents compose? |
| [03-kernel-and-surfaces.md](03-kernel-and-surfaces.md) | What is the one kernel, and how do the three surfaces and the machine plane project from it? |
| [04-authority-write-boundaries.md](04-authority-write-boundaries.md) | Exactly where may Syzygy write, and how does every other effect reach its typed authority? |
| [05-observation-evidence-flow.md](05-observation-evidence-flow.md) | How do sources become snapshots, evaluations, records, and claims — and why can inference only challenge? |
| [06-intent-to-reconciliation-flow.md](06-intent-to-reconciliation-flow.md) | How does adopted intent become dispatched work, and how is merged work reconciled against the intent that warranted it? |
| [07-client-trust-boundaries.md](07-client-trust-boundaries.md) | Who may connect, over which exposure modes, and where do the consent gates sit? |
| [08-adapter-external-systems.md](08-adapter-external-systems.md) | What does each adapter mediate, with what authority, trust direction, and degraded modes? |

## Labelling convention

Every substantive prose claim carries a label, and effectively all runtime
behavior is **[target]**; draft-RFC citations bind nothing until their acts.

- **Labels.** Every substantive prose claim is labelled **[Observed]** (with
  source), **[Inferred]**, or **[target]**.
- **[target]** marks target-state elements: things these diagrams commit to
  as intended shape but which do not exist.
  - No application code, process, or database technology exists or is
    selected (pre-implementation bootstrap).
  - Since Syzygy is unimplemented, effectively **all runtime behavior in
    every diagram is [target]**.
  - Each file's closing section says precisely what is target versus already
    true: adopted doctrine, recorded decisions, the existing
    `.syzygy/governance/` plane, and the existing substrate tools.
- **Draft-RFC clause citations** (RFC1-n … RFC6-n) cite candidate contracts
  that bind nothing until the owner performs the digest-bound acceptance
  acts defined in the active acceptance record (the wave acts).
  - This file quotes no acceptance phrase, so a phrase retirement cannot
    silently invalidate this sentence — the record governs.

## Rendering note

Mermaid is the source of truth for these drawings until each gets its
tracked Excalidraw upgrade.

- Mermaid fenced blocks were chosen as the durable, renderable fallback
  (rendered natively by GitHub and most viewers).
- An **Excalidraw + exported SVG upgrade is a tracked follow-up** for each
  diagram.
