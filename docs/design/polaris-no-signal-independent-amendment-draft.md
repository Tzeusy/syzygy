# Semantic delta — activity assessment without a captured signal

**Candidate — binds nothing.** Prepared for independent review. No accepted
contract bytes, mapping, owner act or historical evaluation are changed.

**Artifact:** `.syzygy/governance/contracts/rfcs/RFC-0008/state-vocabulary-and-cost.md`
**Stable ID affected:** RFC8-13, activity-undetermined row.
**Change class:** Normative — adds a previously undefined absence case.
**Author:** Codex, as proposal drafter only.
**Date:** 2026-09-09.

## Current meaning

Exact affected row from the accepted module:

```markdown
| `activity-undetermined` | Claimed, but no staleness bound is declared, so no signal can count as current | A claim fact exists and RFC4-23's staleness bound is undeclared — RFC2-9's mechanics applied to liveness | `active` is **unrenderable** until the bound is declared (RFC8-16). The claim fact and its instant still render; resolution is a governance act — declare the bound — not fresh evidence |
```

The owning module's current digest is recorded in the companion impact inventory.
The rest of RFC8-13 remains unchanged by this proposed replacement.

## Proposed meaning

Replace that row only, subject to the owning adoption process:

```markdown
| `activity-undetermined` | Claimed; activity assessment lacks an effective staleness bound or an admissible last-progress-signal observation | The declared normalization selects activity assessment for a claim fact, and either RFC4-23's bound is absent or ineffective, or the bound is effective but the answering snapshot contains no admissible last-progress-signal observation. An independently satisfied predicate for another normalized state is not overridden | The claim fact and its actual instant remain visible. Disclose which prerequisite is missing: bound, signal, or both. An otherwise permitted captured qualifying event remains disclosed when the bound is missing: inability to establish its currentness does not make the event itself missing. A missing bound routes to its effective declaration; a missing signal routes to capture or recovery of admissible progress evidence, never fabrication of a timestamp or an assertion that no progress ever occurred. A present admissible signal older than the effective bound remains `stale-or-dead`; a qualifying current signal retains the existing `active` predicate. This is state-local absence, not a new RFC2-24 reason; raw substrate state and the answering evaluation remain visible |
```

This does not claim that the current contract already permits the new branch.
Another existing state remains usable only when its own predicate is satisfied.

## Preserved neighboring obligations

- The thirteen normalized values and six chain values stay unchanged and separate.
- Qualifying progress signals remain exclusively those in RFC4-23. Provider
  requests, responses, draft saves, heartbeats, locks and worktree presence gain
  no worker-liveness authority.
- No positive liveness or dispatch authority is granted by the new absence case.
- Missing/ineffective bounds retain their current behavior; a real old signal
  retains stale-or-dead and its actual instant; a qualifying current signal
  retains the current active predicate.
- State-local absence remains separate from claim labels/tiers/Unknown reasons.
- Snapshot identity, effective mapping/bound acts, immutable history, raw-state
  visibility and paired chain-field obligations continue to apply.

## Warrant

The generator's requested operation exposes a claimed-work case that need not
produce branch, commit or PR progress. The bounded clause analysis and local
mapping search did not establish an effective predicate answering that case.
This authorizes preparation of a remedy for review, not its adoption or use.

## Evidence and decision basis

See `docs/design/polaris-generator-no-progress-signal-decision-2026-09-09.md`
and `docs/evidence/polaris-generator-no-signal-mapping-search-2026-09-09.json`.
Both are candidate analysis, not independent project truth or an effective act.
The mapping search is bounded; an effective existing mapping must be considered
if subsequently supplied. No global absence claim is made.

## Terms

No normalized value, claim-reason code or kernel entity is introduced or retired.
The explanation of unavailable prerequisites is state-local display/query detail,
not a new global reason taxonomy. Its representation requires the normal schema
review; names in this proposal do not mint a new registry vocabulary.

## Downstream impact

The companion `docs/evidence/polaris-generator-no-signal-delta-impact-2026-09-09.json`
records source bindings and a reproducible candidate impact search. It is an
inventory for semantic review, not a claim that every textual hit must be edited.
Current/unbound consumers must be checked for an assumption that this value means
only a missing bound. Historical/raw evidence stays unchanged. The feature's
WORK-STATE-CONTRACT and REQ028 still describe this as unresolved until the
companion change and required feature gates are complete.

## Migration and supersession

Do not edit the digest-bound accepted module in place during drafting. Prepare
and review the exact replacement, affected-ID/consumer dispositions, versioned
normalization definition and owning amendment/manifest transaction together.
Only the owner may bind the resulting semantic change. Retain old source bytes,
acts, manifests and evaluation inputs; do not reinterpret earlier evaluations
under a newer mapping or contract version. New evaluations must identify the
amended contract and effective mapping version. Generator specification wording
and any current consumer explanations must be updated in the same logical
adoption change, rather than silently relying on this draft.

## Review criteria

1. Distinguish no bound, no captured signal, both absent, stale real signal and
   current qualifying signal, without inventing a time or erasing another valid
   state predicate.
2. Keep genuine generation-stage evidence separate from worker liveness.
3. Preserve raw/chain fields and historical replay under their recorded versions.
4. Confirm downstream explanations/routes and amendment scope before an owner
   package is offered; no implementation may use the proposed branch early.

**Required class:** Independent normative-change review under the owning craft
and contract process.
**Reviewer:** Pending fresh-context review.
**Verdict:** Pending; no adoption or implementation authority.
