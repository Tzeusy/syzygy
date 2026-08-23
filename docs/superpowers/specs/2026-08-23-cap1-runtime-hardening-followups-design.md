# Capability 1 runtime-hardening follow-ups — design

**Status:** The conversation-level design is approved; this written record is
pending user review before implementation planning.

**Baseline:** `main` at `0cbb8f9e0eabf7e89d023c2fe7f559465f77b2b0`; the
baseline unit suite passed 53 files / 408 tests in an isolated worktree.

## Purpose and authority

[Observed] The owner’s 2026-08-21 authorization permits Capability 1
implementation, tests, developer tooling, and a bounded Beads backlog. The
adopted Capability 1 specification remains the behavioral authority. This
design is implementation guidance only; it neither amends the adopted
specification nor changes accepted contracts.

No further owner act is needed while the work remains within that authorization.
Any spec/contract amendment, security or retention posture change, normative
data-contract change, resource-envelope breach, or scope expansion returns to
the act's escalation path.

The work addresses the lawful portions of `syzygy-ydr` and `syzygy-h84` that
remain after the completed runtime epic. It improves the faithfulness of
runtime evaluation and the strength of its independent checks without claiming
that the broader governance backlog is executable.

## Scope and non-goals

The implementation sequence has three phases:

1. Runtime input and parity-oracle hardening.
2. Consent and coverage truth.
3. Served discoverability facts.

The following are explicitly out of scope:

- Any edit under `openspec/**` or `.syzygy/**`, including generated governance
  views and accepted contract artifacts.
- Rendering an unresolvable consent reference as reason #11. Accepted RFC3-6
  assigns that condition to reason #6; changing it needs the governed
  amendment path.
- Inventing an authority-exposure source, proposal source, Markdown dialect,
  retention model, or persistent last-good observation contract.
- Updating status pages to declare completion before the corresponding
  behavior and evidence exist.
- The stale or governance-only portions of the remaining open queue.

## Delivery topology

`syzygy-h84` remains the provenance record for the runtime follow-ups and
`syzygy-ydr` remains the provenance record for consent findings. Before code
starts, the coordinator will shape focused child Beads with complete dispatch
packets and explicit dependencies; no worker receives either current aggregate
record unchanged.

The envelope permits two to three workstreams, but these phases are serialized
where they share `coverage.ts`, `pipeline.ts`, evaluation facts, or exact-head
review surfaces. Each child has one accountable implementation worker and an
independent exact-head review when its risk tier requires it.

## Phase 1 — runtime input and parity-oracle hardening

### Outcome

The local daemon's actual credential check is protected by transport-level
regressions, and the independent parity oracle compares the complete fact
sequence or multiset rather than collapsing duplicate fact names in a `Map`.

[Observed] The dangling state-directory finding is already satisfied on the
baseline: startup returns the existing `invalid` arm with a named
governed-plane refusal, and the system test proves a nonzero exit and no
writes. It is therefore not a child outcome in this design.

### Focused child outcomes

1. **Credential transport regression proof.** Prove that whitespace-only and
   malformed presented bearer credentials are rejected by the daemon’s actual
   constant-time credential check. This is a test-debt correction, not a
   widening of the core `admitClient` stub.
2. **Parity oracle hardening.** Replace name-keyed comparison with a
   positional or multiset comparison that preserves duplicate facts and proves
   the prior Map-collapse false negative is detected.

### Surface and evidence

Likely surfaces are `packages/cap1-daemon/src/credentials.*`,
`packages/cap1-core/src/parity.ts`, and the requirement-keyed parity tests.
Each child gets a falsifier before its fix, focused tests during iteration, and
the shared unit/type/system gates before review. Phase 1 owns the credential
admission regression for `CAP1-REQ-015` and comparator hardening for
`CAP1-REQ-041`, `043`, and `045`; later phases consume that comparator rather
than modifying it.

## Phase 2 — consent and coverage truth

### Outcome

Every declared per-repository consent reference participates in runtime
resolution; coverage results preserve the consent or withdrawal provenance
needed to explain capture-failed, stale, withdrawn, and unavailable outcomes;
and the rendered human and machine channels agree.

### Design

1. Form the de-duplicated referenced-record input from both the declaration’s
   top-level consent references and each repository entry’s consent reference.
   A missing referenced record follows the existing reason #6 behavior and
   never becomes reason #11. Duplicate references load one record while every
   declared repository still receives one coverage result.
2. Carry the resolved consent or withdrawal record identity through the
   coverage result rather than retaining only an abstract basis. Render that
   provenance in both served channels. Existing fail-closed precedence remains:
   a withdrawal defeats an in-force grant for the same project/repository pair.
3. Distinguish observer failure from source-unreachable only where the current
   specification and accepted rendering vocabulary already define the two
   states. First create fixtures for the six operational rows below, which
   cover the specification's four condition categories. If
   degrade-to-last-good cannot use an already-supported observation input,
   stop before adding persistence, retry, or storage semantics and return that
   boundary to the governed change path.
4. Document the current `<decisionsDir>/<reference>.yaml` loader convention as
   implementation documentation only; it does not become a new normative
   conformance rule.

The required phase matrix is:

| Input condition | Coverage result | Required provenance and rendered outcome |
|---|---|---|
| In-force record and captured repository | `observed` | Record ID, scope, attribution, and `in-force` grant state appear in the coverage facts and both channels. |
| Missing or unresolvable reference | `unconsented`, reason #6 | The repository remains visible; the result identifies absence of resolvable consent and never reclassifies it as reason #11. |
| Withdrawn record for the declared pair | `unconsented`, reason #6 | Withdrawal defeats any in-force grant; the withdrawal record is visible as the consent basis in both channels. |
| In-force consent and source unreadable at snapshot, with no observer/adapter error | `capture-failed`, reason #10 | The coverage result preserves the in-force consent citation while rendering source-unreachable as Unknown. |
| In-force consent and stale observation | `stale`, reason #4 | The coverage result preserves the in-force consent citation and renders stale evidence distinctly. |
| Observer/adapter error while attempting a source that was otherwise reachable | **Observer failed**, the existing RFC2-23 degradation state | This row takes precedence over source-unreachable. Both channels visibly identify the accepted degradation state; affected new claims are Unknown with reason #10. RFC2-23 requires the existing last-good observation record to render stale/broken. If planning cannot identify an already-authorized input for that record, this row stops before inventing persistence, retry, or storage semantics. |

### Surface and evidence

This phase is a high-risk vertical slice across declaration, consent, coverage,
loader, pipeline, observation, and human/machine rendering modules. It is one
serialized coverage ownership lane, with requirement tests for
`CAP1-REQ-011`–`015`, targeted daemon tests, dual-channel assertions, and a
system test. It owns the coverage limbs of `CAP1-REQ-015`; Phase 1 owns that
requirement's credential-admission regression. It needs independent exact-head
review.

## Phase 3 — served discoverability facts

### Outcome

Discoverability findings produced from repository evidence become part of the
same `ProjectEvaluation` that supplies the seven shape answers, and appear
identically in the machine and human channels with their evidence and
disclosure status intact.

### Design

1. Treat a raw README substring as insufficient evidence that an entry link
   exists. The behavior matrix is: a parsed Markdown link to the fixed entry
   is `yes`; readable plain text mentioning the path but containing no such
   link is `no`; a missing or unreadable root README is `Unknown`; and a
   repository with no governance root is `not-applicable`. The parser must not
   establish a new canonical Markdown dialect; if those cases cannot be
   distinguished without one, stop and return to the governing change path.
   For this Capability 1 slice, the fixed entry target is exactly
   `.syzygy/intent/OVERVIEW.md`; a passing `yes` fixture uses a parsed Markdown
   link whose destination equals that path, rather than a raw-text occurrence.
2. Thread the resulting discoverability findings through evaluation and both
   renderers, preserving `Unknown`/absence disclosure rather than inventing a
   success state.
3. Preserve current explicit absence for authority exposure and proposals until
   an authoritative input exists. Proposal carriage becomes a later local
   implementation task only once evaluation produces real proposals.

### Surface and evidence

Likely surfaces are observation, pipeline, fact model, human route, machine
route, and parity/conformance tests for `CAP1-REQ-040`, `041`, `046`, and
`050`–`053`. The implementation must demonstrate browser-equivalent and
machine-route parity at the real serving seam. Phase 3 owns the served-fact
work for `CAP1-REQ-040`, `046`, and `050`–`053`; it consumes the comparator
hardened in Phase 1 rather than changing that comparator again.

## Review, verification, and closeout

Every child begins with a behavior-executing falsifier and ends with its named
targeted checks, `npm run typecheck`, `npm test`, and `npm run test:system`.
The planning record must name the exact test IDs, but the expected minimum is:

- Phase 1: credential/admission tests plus `CAP1-REQ-015`, parity tests plus
  `CAP1-REQ-041`, `043`, and `045`, and the duplicate-name falsifier.
- Phase 2: `CAP1-REQ-011`–`015`, consent-loading/pipeline/observation/route
  tests, the six-case matrix fixtures covering four specification conditions,
  and dual-channel serving tests.
- Phase 3: `CAP1-REQ-040`, `041`, `046`, and `050`–`053`, plus pipeline and
  both route tests proving one finding per declared repository.

Phase 1 and Phase 2 are high-risk and require independent exact-head review;
Phase 3 is standard-risk unless implementation introduces a new trust boundary,
in which case it escalates to high-risk review. Workers declare their tested
bytes FROZEN; the coordinator re-verifies staged bytes before commit or merge.
A Bead closes only after its reviewed change reaches `main`.

After all behavior packets land, a final truthful-status packet may update the
root status/workflow language using fresh evidence. Root-only selftest-fixture
hygiene from `syzygy-e84` is a separate maintenance design; its governed-plane
portion remains held.

## Approval checkpoint

The conversation approved the design direction, but this written record still
requires the user's review. After that review, the next step is a detailed
implementation plan and then packet-complete Bead shaping under the existing
2026-08-21 authorization. No implementation or Beads lifecycle mutation is
authorized by this document alone.
