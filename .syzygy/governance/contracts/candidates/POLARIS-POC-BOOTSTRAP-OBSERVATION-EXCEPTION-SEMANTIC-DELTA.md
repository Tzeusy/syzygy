> **Candidate — binds nothing.** This proposes one temporary exception for
> the named, non-release Polaris POC. It edits no accepted contract or signed
> OpenSpec byte. No Butlers body read or implementation is authorized by this
> file.
>
> **⛔ REVISE — NOT OFFERED.** Independent security review at SHA-256
> `da14c86b651e263e144975bfedcc59b800d5dc0600de7280a071403e6e07fa8a`
> found that this amendment is itself authorization-for-effect and therefore
> cannot make itself machine-effective from a state-(1) act. The same-tree
> exception preserves the RFC4-7/RFC5-16 forgery threat it claims to bound.
> The reviewed body is retained as diagnostic evidence; do not sign or apply
> it. See `docs/reviews/R-POLARIS-POC-EXCEPTION-SECURITY-RAW.md`.

# Semantic delta PWB-EX-1 — bootstrap observation for the Polaris POC

**Artifacts:** `.syzygy/governance/contracts/rfcs/RFC-0003/governance-homes-and-owner-acts.md`; `.syzygy/governance/contracts/rfcs/RFC-0004/general-contract.md`; `.syzygy/governance/contracts/rfcs/RFC-0005/consent-egress-secrets.md`; `openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md`

**Stable IDs affected:** `RFC3-16(a)`, `RFC3-16(c)`, `RFC4-7`, `RFC5-16`, `PWB-REQ-005`; no ID is renumbered and no new RFC clause is minted

**Change class:** Normative — it permits a body read that the current clauses prohibit

**Author:** OpenAI Codex, drafting only

**Date:** 2026-08-31

**Baseline:** commit `8fb605316737a8505791d43df7212833d8c513ee`

## Current meaning

### RFC3-16(a)

Current subject digest: `bc08a888f3ea716047c021d5bf76b92045671d8ce20b043026fcbd9c7d4cdb77`.

The effect rule currently says exactly:

> **Effect when the predicate fails.** An authorization present in the tree
> without verifiable owner-act provenance is **never silently honored and never
> silently deleted**. Its **dependent effect is blocked** — the egress is
> refused, the run does not launch, the adapter write does not proceed, the
> adoption does not bind, the policy does not widen anything — the
> **authorization itself renders Unknown**, and the condition **mints a
> contradiction routed to owner adjudication**: exactly the posture RFC3-3
> takes for an inoperative write-expanding field and RFC3-9 takes for a
> governance artifact Syzygy did not author. Blocking is not deletion: the
> artifact and its unverifiable state both remain rendered.

Therefore an uncorrelated consent, policy or registry entry authorizes no
observation effect.

### RFC3-16(c)

The final consequence currently says exactly:

> - Nothing here weakens RFC3-16(a): an authorization-bearing artifact resting
>   on a state-(1) record has not satisfied the predicate, and RFC3-16(a)'s
>   *Effect when the predicate fails* governs its dependent effects. The
>   constraint half of the same split — a state-(1) artifact consumed as a
>   constraint binds at full strength — is stated in RFC3-16(b)'s *Bootstrap
>   correlation* paragraph; the two halves are one rule read from either end.

The two provenance states are closed, and state (1) never authorizes an
effect.

### RFC4-7

Current subject digest: `2b5072a2b718e4609b279b130ef39daeb49fc6079c8da9c01e14aa12021149d4`.

The registry gate currently says exactly:

> **RFC4-7 — The registry.** A per-project, versioned **adapter registry** lives
> in the governance plane (`.syzygy/governance/`; physical schema: RFC 0003).
> One entry per registered observer/adapter, holding the RFC4-2 declaration set
> plus the entry's own adoption status. The registry is a snapshot input; an
> output attributed to an adapter absent from the snapshot's registry state is
> inadmissible as a deterministic fact and renders Unknown
> (`source-uncaptured-or-unreachable`). An entry's **adoption status is not
> self-authenticating** (RFC3-16): admitting an adapter is what makes its output
> a deterministic fact at all, so an entry is honored **only under RFC3-16(a)** —
> an entry an untrusted writer could mint would register an arbitrary adapter
> and launder whatever it emits into the deterministic base graph, which no
> downstream tier or freshness check inspects. An entry whose owner-act
> provenance does not verify admits nothing: outputs attributed to it render
> Unknown exactly as if the adapter were unregistered.

An uncorrelated project-shape adapter entry therefore admits no facts.

### RFC5-16

Current subject digest: `cdbeb638bbdd47fada153dad6d9334803c3c54e45408fb54b39c5c9d4fb59f69`.

The policy gate currently ends exactly:

> The policy version is a snapshot input (RFC2-1 item 7), so what was screened
> is part of every evaluation's identity — and the policy is honored **only
> under RFC3-16(a)**: it is an owner-approved declaration whose effect is to
> widen what Syzygy may take in, so a permissive version an untrusted writer
> could mint would admit at every ingest boundary exactly the content SEC-5
> requires excluded, and the exclusion counts would render honest about a
> screen that never screened. An unverifiable policy does not fail open: the
> ingest is blocked on RFC3-16(a)'s effect rule, never performed under the
> unverified policy.

An uncorrelated secret policy therefore blocks ingest even when it is strict.

### PWB-REQ-005

Current subject digest: `07392c115e3a63bb3aceb259362a70e0d1ee11d6ba2621492fd03cf1893aca61`.

The requirement currently says exactly:

> The POC SHALL NOT read any Butlers project-shape body until an exact
> per-repository observation-consent record, a concrete secret-classification
> policy and the project-shape observer's registered adapter entry all have
> verifiable owner-act provenance. Their identities and versions SHALL be
> evaluation inputs. Absence, mismatch, staleness or unverifiable provenance
> SHALL produce zero body reads and a project-model Unknown.
> The consent subject SHALL be the exact `(observing Syzygy project, configured
> Butlers repository)` pair; a consent for another project, repository or content
> class SHALL not match.
> The observer registry entry SHALL live in Syzygy's governance plane, name that
> same project/repository pair and declare the observer's read-only authority and
> empty write surface.

Its oracle permits reads only for an independently verified triple.

## Proposed meaning

### Add one closed exception to RFC3-16(a) and RFC3-16(c)

Append this sentence to RFC3-16(a)'s effect rule:

> The only exception is `PWB-BOOTSTRAP-OBS-1` in RFC3-16(c): it is closed to
> the exact named project, repository, artifacts, effect, expiry and POC, and
> no other gate may infer or generalize it.

Append this text to RFC3-16(c), without creating a third provenance state:

> **`PWB-BOOTSTRAP-OBS-1` — named non-release observation exception.** Until
> `2026-09-30T00:00:00Z`, the one `polaris-project-wide-butlers-model` POC may
> honor state-(1) owner acts for exactly these authorization artifacts:
> observation consent for `(project:syzygy,
> repository:butlers-configured-poc)`, secret policy
> `polaris-butlers-project-shape-secrets`, and adapter entry
> `polaris-butlers-project-shape`. Each act must bind RFC3-16(b) items 1–8,
> including the exact artifact digest, and must disclose item 9 as absent. The
> contract-amendment act and the three artifact acts must be recorded together;
> absence or mismatch of any one leaves the normal effect rule unchanged.
>
> This exception permits only deterministic, read-only observation of exact Git
> objects selected by the signed PWB source grammar. The adapter has no write,
> database, credential-API, process-environment, observed-code-execution or
> network authority. The owner-approved policy still runs before every ingest
> and fails closed. Only the exact exception and artifact acts select this
> authorization mode; no command-line flag, path, environment value or runtime
> default may widen it.
>
> Every admitted machine fact carries the exception identity, provenance state
> and expiry. Polaris shows one persistent project-account notice — **“POC
> exception — owner-adopted bootstrap, not independently verified — expires
> 30 Sep 2026.”** — and makes the same metadata reachable from each claim
> without repeating the sentence beside every item. Expiry is judged at the
> evaluation's identified as-of instant, never by an ambient wall clock. The
> exception does not make state (1)
> independently verified, does not satisfy a release, conformance, certificate,
> egress, write, execution or second-project gate, and does not authorize an
> inferred positive claim. At expiry or revocation, the next evaluation performs
> zero new body reads; prior records remain immutable and visibly withdrawn or
> stale. This exception does not retroactively authorize any earlier read.

The normal A1 mechanism and the two-state model remain the only behavior
outside this exact exception.

The amended contract is consumed as a constraint, so its state-(1) acceptance
continues to bind under RFC3-16(b)'s existing constraint/effect split. The
consent, policy and registry are the only authorization-for-effect artifacts
this exception permits in state (1).

### Amend RFC4-7 only for the named adapter

Append:

> Under `PWB-BOOTSTRAP-OBS-1` only, the exact state-(1)
> `polaris-butlers-project-shape` entry may admit deterministic facts solely to
> the named PWB evaluation. Every emitted fact carries the entry digest,
> exception identity, uncorrelated provenance state and expiry. Those facts
> are inadmissible to every other evaluation, project, release or certificate.
> Missing, changed, expired or revoked entry state follows the normal rule and
> admits nothing.

### Amend RFC5-16 only for the named policy

Append:

> Under `PWB-BOOTSTRAP-OBS-1` only, the exact state-(1)
> `polaris-butlers-project-shape-secrets` policy may screen the named PWB ingest.
> Its identity, version, digest, uncorrelated provenance state and expiry are
> snapshot inputs. Every existing fail-closed rule in RFC5-16 and RFC5-17 still
> applies. Missing, changed, expired or revoked policy state blocks ingest.

### Replace PWB-REQ-005 with this behavior

Keep the requirement title and ID. Replace its normative body with:

> The POC SHALL perform zero Butlers project-shape body reads unless either:
> (a) the exact observation-consent record, secret-classification policy and
> registered adapter entry all have independently verifiable owner-act
> provenance; or (b) every condition of `PWB-BOOTSTRAP-OBS-1` is satisfied for
> this exact POC evaluation. Their identities, versions, digests, provenance
> states and the selected authorization mode SHALL be evaluation inputs.
>
> The consent subject SHALL be exactly `(project:syzygy,
> repository:butlers-configured-poc)`. The adapter entry SHALL live in Syzygy's
> governance plane and declare read-only Git authority with an empty write
> surface. The bootstrap exception SHALL additionally require its exact expiry,
> three state-(1) acts and visible unverified label.
> Absence, mismatch, staleness, expiry, revocation or invalid provenance for the
> selected mode SHALL produce zero body reads and a project-model Unknown.

Add these observable scenarios while retaining the existing missing-consent
scenario:

> #### Scenario: Exact bootstrap exception permits bounded observation
>
> - **WHEN** the exact state-(1) consent, policy and registry acts match the
>   named project, repository, artifact digests and unexpired exception
> - **THEN** the project-shape adapter may read only manifest-selected exact Git
>   objects through its empty-write authority
> - **AND** Polaris shows the exact project-account notice, each claim exposes
>   the same metadata on demand, and `/api/poc` carries it on every admitted
>   project-shape fact
>
> #### Scenario: Missing or expired exception remains zero-read
>
> - **WHEN** the normal verified triple is absent and any bootstrap condition,
>   flag, digest or expiry check fails
> - **THEN** the project-shape adapter performs zero body reads
> - **AND** the project model reports Unknown with the exact failed gate

The independent oracle must enumerate both modes, inject the body-read spy,
and prove that the exception admits only the exact named tuple before expiry.

## What explicitly does NOT change

- SEC-2 and SEC-5 remain binding. No secret may enter a model, cache, log,
  human surface, machine response or record.
- PWB's closed source grammar, exact-Git-object rule, traversal/symlink/
  submodule refusals, active-content refusal and resource limits do not move.
- The adapter has no Butlers write, database, credential API, process
  environment, execution, network or second-repository authority.
- RFC3-16(c) still has exactly two provenance states. The exception is visibly
  state (1), never “verified,” and never a reusable third state.
- A1 remains the only general mechanism. No other consent, policy, adapter,
  project, effect or runtime may cite this exception.
- The POC remains non-release. No compliance, alignment, convergence or
  security-success claim follows from using the exception.
- The owner has not approved the current consent, policy, registry or this
  delta. Their presence and this draft authorize nothing.
- The previously recorded read-boundary incident remains unauthorized and is
  not converted into evidence by a later act.

## Warrant

The owner explicitly granted Butlers observation and prohibited secret reads
in the Polaris walkthrough. The signed PWB change cannot honor that direction
without the A1 audit mechanism, and the A1 mechanism is not implemented. This
delta makes the alternative exact enough to accept or reject; it does not infer
the owner's choice.

The product warrant remains the owner finding recorded in
`docs/reviews/R-POC-OWNER-WALKTHROUGH-POLARIS.md`: Polaris currently explains
one WhatsApp slice rather than Butlers. The exception is useful only insofar as
it unblocks the signed project-wide observation behavior.

## Evidence or decision basis

- `.syzygy/governance/decisions/POLARIS-PROJECT-WIDE-SPEC-SIGNOFF-ACT.md`
  freezes the current PWB behavior and names the three unsatisfied authorities.
- `.syzygy/governance/decisions/BUTLERS-PROJECT-SHAPE-OBSERVATION-CONSENT.md`
  preserves the owner's direct statement but truthfully reports no effective
  act.
- `docs/reviews/R-POLARIS-OBSERVATION-GATE-CONFIRMATION-RAW.md` confirms the
  three candidate artifact shapes and the remaining A1 blocker.
- `docs/reviews/R-POLARIS-PRECONDITION-READ-BOUNDARY-INCIDENT.md` shows why an
  exception must be explicit and non-retroactive.

## Terms introduced / retired

- Introduced locally: `PWB-BOOTSTRAP-OBS-1`, a closed exception identity.
- Introduced as an evaluation value: `bootstrap-exception` authorization mode.
- Owner-visible copy: “POC exception — owner-adopted bootstrap, not
  independently verified — expires 30 Sep 2026.”
- No kernel epistemic label, tier, Unknown reason or degradation state is added
  or retired.

## Downstream impact

Method: exact fixed-string sweeps with both `rg -F` and `git grep -F` at
baseline `8fb6053`; both methods returned the same tracked-file counts.

| Identifier | Tracked files containing it | Direct active-contract files | PWB files |
|---|---:|---:|---:|
| `RFC3-16(a)` | 187 | 26 | 3 |
| `RFC3-16(c)` | 43 | 3 | 2 |
| `RFC4-7` | 32 | 3 | 5 |
| `RFC5-16` | 37 | 5 | 4 |
| `PWB-REQ-005` | 20 | 0 | 9 |

The counts are reference populations, not claims that every file requires an
edit. The same-logical-change audit must disposition every member.

Known direct propagation if the owner chooses this delta:

1. Amend the three installed Wave-A contract modules and their candidate-tree
   counterparts at the same exact text.
2. Update the RFC 0003/0004/0005 package summaries whose “only verified” prose
   would otherwise become false.
3. Regenerate Wave-A and active manifests, contract index, dependency index,
   budget report and any router/context outputs whose digests or word counts
   move; obtain a fresh digest-binding review and owner acceptance act.
4. Amend PWB proposal, design, PWB-REQ-005, tasks, capability coverage,
   contract coverage, repair delta, dependency union and affected matrices as
   one frozen candidate; obtain a fresh sign-off act superseding the eleven
   current digests.
5. Re-review the exact affected consequence rows in the signed
   `project-registration-and-honest-shape-visibility` and
   `three-surface-poc-experience` changes. Their signed bytes remain untouched
   unless the review proves an assertion became false; any required edit uses
   its own digest-bound amendment act in the same logical change.
6. Finalize the consent candidate so its self-declared lifecycle is compatible
   with a future act, then bind the exact consent, policy and registry digests
   in the ordered owner ceremony the amended clauses require.
7. Update `PROJECT-STATUS.md`, the Bead and PWB task 1.5 only after the complete
   transaction verifies. Historical act and incident records remain append-only.

This is not a one-file PWB correction. It is a bounded but foundational
security-contract amendment.

## Migration / supersession plan

No accepted or signed byte changes before owner authorization. If authorized:

1. freeze the exact proposed contract/spec text and finalize the three
   authority candidates;
2. run fresh security and contract-coverage review on those exact bytes;
3. prepare regenerated manifests and every invalidated signed artifact without
   installing them;
4. present one ordered owner packet: accept the amended Wave-A contract bytes,
   sign the amended PWB suite, then consent/approve/adopt the three exact gate
   artifacts under the now-binding exception;
5. install and commit the whole transaction without an intermediate mainline
   state in which contracts and PWB disagree;
6. add zero-read authority tests and visible exception parity before any live
   Butlers body read; and
7. at expiry or revocation, default to the normal verified triple or Unknown.

Rollback before implementation is deletion of this unadopted candidate.
Rollback after adoption is a new owner act that revokes the exception and
restores zero-read behavior; prior records remain visible and stale.

## Review

**Required class:** CC-REV-1 authority boundary, deterministic observation,
security and public interface; CC-REV-4 material normative amendment

**Reviewer:** pending fresh-context review

**Verdict:** pending
