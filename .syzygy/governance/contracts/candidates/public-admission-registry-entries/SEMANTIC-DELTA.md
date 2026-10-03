# Semantic delta — public-admission registry entries (provider route and Git-hosting source acquisition)

> **Candidate — binds nothing.** Drafted by an agent for bead `syzygy-mea`.
> Effect over either entry would come only from that entry's own owner act.
> No review has been run against these bytes.

**Artifact(s):** two new whole files under `proposed/` in this directory:
`POLARIS-PROVIDER-ROUTE-ANTHROPIC-AGENT-SDK-CANDIDATE.json` and
`POLARIS-PUBLIC-GIT-SOURCE-ACQUISITION-CANDIDATE.json`. Neither exists in the
installed home `.syzygy/governance/declarations/adapter-registry/`, and this
package installs nothing there.

**Stable IDs affected:** none minted, renamed or retired. The entries answer
REQ-polaris-generation-017 and 018 (Source: RFC4-2) and cite RFC4-1, RFC4-2,
RFC4-3, RFC3-16(a), RFC5-15 and RFC5-16.

**Change class:** Normative (it creates registry entries; an entry is honored
only under an owner act, RFC4-7).

**Author:** Claude agent session, 2026-10-03.

## Current meaning

[Observed] The installed registry holds one entry, the Butlers project-shape
observer, which declares `networkAccess: []` and a read-only Git object
surface. No entry registers a provider route or any source acquisition other
than that one. [Observed] The generator's only `generate` port is a scripted
responder, and the only real-input reader is the Syzygy self-corpus (gap G1
and G2 in `docs/polaris-generation/TRACKER.md`). Under REQ-polaris-generation-017
an unregistered route "cannot establish a deterministic fact and new effects
using that unregistered authority are refused".

## Proposed meaning

Two entries, each a separate registry event.

1. **Provider execution route** (`polaris-provider-route-anthropic-agent-sdk`).
   The one registered adapter through which `project:syzygy` reaches the
   provider Anthropic, via the Claude Agent SDK runtime (RFC4-1: one adapter
   per external authority per project; the packet's item 2). Determinism
   class `capture`. Typed question: "What did the provider return for this
   exact request?" Write surface empty; the only local write is the run
   directory. Its `routeConditions` restate the egress record's conditions
   (no tools, no ambient context, telemetry off, state inside the run
   directory, acceptance by captured request, no fallback) as declarations
   the implementation must enforce. The egress record, not this entry, is the
   authority for them; the entry cannot widen them.
2. **Public Git-hosting source acquisition**
   (`polaris-public-git-source-acquisition`). One shared adapter for every
   `(project:syzygy, repository)` pair that has its own in-force observation
   consent (the packet's item 5 left "per target or one shared adapter"
   undecided; this delta proposes one shared adapter and the owner decides,
   question O1 of the packet). The fetch reaches the hosting service, which
   RFC4-1 treats as an external authority, so network access is declared and
   limited to one shallow fetch of exactly one admitted commit per fetch.
   Reads go through Git object access in the run-directory repository; no
   working tree, no execution, no ancestor history. Determinism class
   `capture` for the fetch; tree listing and span derivation over the
   identified capture are derivation-deterministic. Resource limits are
   [Inferred] proposals for the owner (question O2), because no target body
   has been read to measure them.

Both entries set `implementationVersion` to `null`: [Unknown] until the
implementation exists (RFC4-3 admits no output from an entry whose
implementation identity and version are not in the snapshot). A signed entry
therefore enables nothing until code lands and the generator's consent-backed
ports (gap G3) consult it.

## What the entries do not do

They grant no read, egress, write, execution or release. The provider entry
does not replace the egress consent (REQ-polaris-generation-025: consents stay
separately revocable and imply nothing). The acquisition entry does not
replace the observation consent, and it depends on a public-source screening
scope that is drafted separately and not yet in force: with no effective
scope, `missingScreeningScope` maps to `missing-declaration` and nothing is
read.

## Epistemic labels

- [Observed] Field shapes follow the installed Butlers entry; the
  `contractVersion` value is copied from it and the builder re-checks the
  copy against the live file.
- [Inferred] The authority type names `model-provider` and
  `hosting-and-version-control` are the drafter's; RFC4-1 lists examples only.
- [Inferred] The degradation-state mappings reuse the Butlers entry's
  five states; `usageOrDispatchUncertain` mapped to Partial snapshot is a
  judgement the reviewer should test.
- [Unknown] Whether the Agent SDK on the owner's login can meet the route
  conditions (gap #21); the entry says so in its own `unknowns` list.
