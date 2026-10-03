# Semantic delta — public-admission registry entries (provider route and Git-hosting source acquisition)

> **Candidate — binds nothing.** Drafted by an agent for bead `syzygy-mea`.
> Effect over either entry would come only from that entry's own owner act.
> Rounds 1, 2 and 3 returned REVISE (raws retained under `reviews/`); this is
> the round-4 text. No review has run against these bytes.

**Artifact(s):** two new whole files under `proposed/` in this directory:
`POLARIS-PROVIDER-ROUTE-ANTHROPIC-AGENT-SDK-CANDIDATE.json` and
`POLARIS-PUBLIC-GIT-SOURCE-ACQUISITION-CANDIDATE.json`. Neither exists in the
installed home `.syzygy/governance/declarations/adapter-registry/`, and this
package installs nothing there.

**Stable IDs affected:** none minted, renamed or retired. The entries answer
REQ-polaris-generation-017 (Source: RFC4-2) and 018 (Source: RFC4-19) and
cite RFC4-1, RFC4-2, RFC4-3, RFC3-16(a), RFC5-15 and RFC5-16.

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
   exact request?" It is one entry for one route; PR #264's Messages API route
   would be a substitute that replaces it under a new act (RFC4-1), never a
   second route beside it. The entry pins the Agent SDK 0.3.288 and bundled
   CLI 2.1.288 and states that the request is the generator's two parts
   (stage system prompt, stage input envelope) plus bytes the runtime adds,
   which the entry lists inline in `requestBytes` (runtime-fixed bytes, the
   pinned model, no tools, effort and a max_tokens ceiling, headers, the probe);
   `PROVIDER-EGRESS-BYTES.md` (PR #258) is provenance only. Write surface empty,
   argued: the dispatch is an effect and the egress consent is its explicit
   authority. Its `routeConditions` restate the egress record's conditions and
   name the record, with one divergence: the record says the route "adds no
   context of its own", and the runtime envelope does, so accepting it (packet
   O4) needs an egress record version that admits the listed bytes. The
   acceptance check is generator-built parts byte for byte plus `requestBytes`
   for everything else; any byte in neither fails. The egress record, not this
   entry, is the authority; the entry cannot widen it.
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

Both entries set `implementationVersion` to `null` and leave the governing
contract version Unknown. RFC4-3 admits no output from such an entry, and
filling either field changes the bytes, the manifest row and the act argument
(rule 10). So these rows are not the bytes that could ever admit output: signing
them would register the declared boundary and nothing more, and each usable
entry is a later observer version that carries the implementation version,
is reviewed afresh and is signed by its own act. Code landing alone does
not enable anything, and the generator's consent-backed ports (gap G3) must
consult the later entry.

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
- [Inferred] The degradation-state mappings use RFC2-23's six states.
  Round 1 found uncertain usage mis-mapped to Partial snapshot: absent tokens
  are Missing quantity, uncertain dispatch is an execution fact routed by the
  claim-reason predicate, a non-admitted revision is refused before fetch with
  reason 6, and a runtime that cannot meet the route conditions is reason 12
  `execution-blocked`. Absent consent is a refused effect, never a withdrawal.
- [Unknown] Whether the Agent SDK on the owner's login or key can meet the route
  conditions (gap #21), whether the real API accepts the runtime's empty system
  message, traffic beyond the captured paths, and credential writes outside the
  run directory; the entry says so in its own `unknowns` list.
- [Inferred] The RFC2-1 snapshot-input mapping is stated in each entry as the
  drafter's; the installed Butlers entry has none, so that gap is inherited.
