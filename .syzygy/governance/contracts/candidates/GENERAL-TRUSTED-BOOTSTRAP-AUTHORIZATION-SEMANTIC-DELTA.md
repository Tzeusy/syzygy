> **SATISFIED 2026-09-01 — amendment transaction performed.** The owner
> performed the exact indivisible transaction recorded at
> `.syzygy/governance/decisions/GENERAL-TRUSTED-BOOTSTRAP-AUTHORIZATION-ACT.md`.
> This routing artifact remains non-bound history and grants no effect-specific
> authority beyond the five recorded transaction rows.

# Semantic delta GBA-1 — state-(1) owner acts may take effect

**Artifacts:** accepted RFC 0001–0009 modules that hard-code A1-only owner-act effects; candidate RFC 0010 mission modules; affected package summaries, manifests, indexes and signed coverage artifacts

**Stable IDs affected:** `RFC3-2`, `RFC3-15`, `RFC3-16(a)`, `RFC3-16(b)`, `RFC3-16(c)`, `RFC2-9`, `RFC2-13`, `RFC4-7`, `RFC4-12`, `RFC4-13(b)`, `RFC4-23`, `RFC4-26`, `RFC5-15`, `RFC5-16`, `RFC5-18(c)`, `RFC7-21`, `RFC7-25`, `RFC7-31`, `RFC8-16`, `RFC9-8(a)`, `RFC9-18`, `RFC9-26`, `RFC9-45`, phase rules `RFC1-33`, `RFC2-26`, `RFC3-33`, `RFC4-30`, `RFC5-27`, `RFC6-28`, `RFC7-38`, `RFC8-32`, `RFC9-52`; candidate `RFC10-4`, `RFC10-9`, `RFC10-21`, `RFC10-24`; policy `CC-SPEC-8`; no ID is added, retired or renumbered

**Change class:** Normative — a real human state-(1) act can authorize effects that currently require state (2)

**Author:** OpenAI Codex, drafting only

**Date:** 2026-08-31

**Baseline:** commit `20e5b6e`

## Current meaning

RFC3-16(a) currently says exactly:

> Such an artifact is honored **only when its owner-act provenance is
> independently verifiable to Syzygy by a mechanism the governed tree cannot
> forge**.

RFC3-16(b)'s bootstrap-correlation paragraph currently splits constraints from
authorizations:

> an artifact consumed as a **constraint** binds at full strength ... while an
> artifact consumed as an **authorization for an effect** ... has not satisfied
> the RFC3-16(a) predicate on a state-(1) record alone

RFC3-16(a)'s failure rule currently says an unverified authorization blocks its
effect, renders Unknown and mints a contradiction. RFC3-16(c)'s final
consequence repeats that a state-(1) authorization cannot take effect.

Direct consumers turn that general rule into effect-specific blocks. The
load-bearing current phrases include:

| Clause | Current A1-only consequence |
|---|---|
| `RFC2-9` | a currency-bound declaration without verifiable owner-act provenance does not unblock its claim class |
| `RFC2-13` | an unverifiable challenge resolution or sweep policy cannot resolve/suspend claims |
| `RFC3-2/15` | kernel sweep-resolution records require a provenance-verified policy |
| `RFC4-7` | an adapter entry whose owner-act provenance does not verify admits nothing |
| `RFC4-12` | code observation requires a secret policy whose owner-act provenance verifies |
| `RFC4-13(b)` | a governed checker definition is honored only with verifiable owner-act/governance provenance |
| `RFC4-26` | marker-sourced declarations require a verifiable marker-adoption owner act |
| `RFC5-15` | classification policy and egress consent provenance must verify before transmission |
| `RFC5-16` | an unverifiable secret policy blocks ingest |
| `RFC5-18(c)` | an execution approval without verifiable provenance blocks launch and mints a contradiction |
| `RFC7-21` | adoption whose owner-act provenance does not verify leaves the draft unadopted |
| `RFC7-25` | an unverifiable review pass does not clear the adoption freeze |
| `RFC7-31` | an unverifiable walkthrough judgment is `verdict-unlawful` and leaves the test Unknown |
| `RFC9-18` | an unverified layout registry entry establishes no version |
| `RFC9-26` | an unverified channel entry is treated as absent |
| `RFC9-45` | unverified release policy, waiver or judgment cannot clear the walkthrough/release gate |
| Phase rules | reviewed N/A judgments map nothing unless owner-act provenance verifies |
| `RFC9-8(a)` | a portfolio registry entry whose provenance does not verify is treated as absent |
| Candidate `RFC10-4/9/21` | mission, envelope and cross-project consent effects require verified/A1 provenance |
| Candidate `RFC10-24` | mission operation remains blocked until D3 or an owner doctrine-interpretation ruling |

The A1 correlation identity is RFC3-16(b) item 9. State (1) is rendered as a
human/social fact, but is not currently effectual.

## Proposed meaning

### RFC3-16(a) — effect requires a valid owner act, not state (2)

Replace the first sentence of **The predicate** with:

> An authorization-bearing artifact is honored only through an **effective
> owner act**. An effective owner act is an actual human owner act whose record
> is current, attributable, scope-matched and bound to the artifact's exact
> digest under RFC3-16(b). Its provenance may be state (1),
> `owner-adopted (bootstrap, uncorrelated)`, or state (2), `Syzygy-verified`.
> Independent correlation distinguishes those states; it is not what makes the
> human act effective.

Immediately follow it with:

> **Trust premise.** State (1) relies on the owner's trust in the recorded tree
> and does not prove the tree could not forge the record. A well-formed file,
> stored owner name, machine submission or agent assertion is never by itself
> an owner act. A machine may prepare an act for owner attendance; it may not
> mint, impersonate, approve, widen, revoke or reinterpret one. If an
> implementation accepts a forged record as an act, the resulting effect is
> unauthorized and is a trust-floor violation, not authority granted by this
> clause.

Replace **Effect when the predicate fails** with:

> **Effect when the owner-act gate fails.** Missing, digest-mismatched,
> wrong-scope, stale, expired, superseded, revoked, unattributed or non-human
> act state blocks the dependent effect, renders the authorization Unknown and
> mints a contradiction routed to owner adjudication. Absence of A1 correlation
> alone does none of those: a valid state-(1) act takes effect and remains
> visibly uncorrelated. Failed or indeterminate correlation of a record claiming
> state (2) never silently downgrades it to state (1); trusted-bootstrap must be
> the explicit state of the human act.

The non-exhaustive example list and consuming-gate list remain. Every consumer
continues to cite RFC3-16(a), now checking act effectiveness and provenance
state separately.

### RFC3-16(b) — items 1–8 bind every act; item 9 distinguishes state (2)

Replace the introduction “A verifiable owner act binds” with:

> Every owner act, in either provenance state, binds at minimum all of:

Keep items 1–8. Replace item 9 with:

> 9. the **A1 audit-record identity or its explicit absence**. State (2) binds
>    the independently kept audit identity and successful correlation. State
>    (1) records that no external correlation identity exists. Omitting the
>    field is invalid; explicit absence is not independent verification.

Replace the bootstrap-correlation effect split with:

> A state-(1) act satisfying items 1–8 and explicitly recording item 9 absent
> is effective under RFC3-16(a). Correlation upgrades its provenance to state
> (2) without editing the artifact or retroactively changing the act's prior
> effects. A git commit/tag or tree record alone still proves neither human
> attendance nor state (2); the project deliberately trusts a recorded
> state-(1) act only because the owner chose that trust model. State (1)
> remains available after an A1 mechanism exists, but only when the human owner
> explicitly chooses trusted-bootstrap provenance in the act itself. A failed,
> unavailable or indeterminate A1 attempt never creates state (1) and never
> changes a record claiming state (2) into state (1).

### RFC3-16(c) — two effective states, one verification claim

Keep exactly two provenance states. Amend state (1) to say:

> **(1) Owner-adopted (bootstrap, uncorrelated).** This is a real human/social
> governance act, preserved as the exact owner phrase, exact content digest,
> act record and recording commit/tag. It may be performed before or after an
> A1 mechanism exists; after A1 exists, the act must explicitly select state
> (1). It is effective only for its exact act type and scope. It remains
> forgeable from the governed tree's perspective and never supports the claim
> “independently verified.”

Amend state (2) to cover both direct and later correlation:

> **(2) Syzygy-verified (effective act).** An owner act either performed
> through the independent A1 ceremony and audit mechanism, or first recorded
> in state (1) and later correlated through that mechanism. Both paths bind
> RFC3-16(b)'s nine items. Only this state supports the claim “independently
> verified.”

Replace the final non-effect consequence with:

> Both valid provenance states may carry an effective owner act. Surfaces and
> APIs always expose the exact state and authorization basis. Correlation may
> upgrade state (1) to state (2) through a new evaluation; it never changes the
> historical fact that earlier effects ran under owner-trusted, uncorrelated
> provenance.

No third provenance state is added. `owner-trusted` is presentation of state
(1), not a new label.

## Direct consumer amendments

Every consumer retains its effect-specific gates. Only its A1-only clause is
replaced.

### RFC2-9 and RFC2-13

- Currency-bound declarations, authorization-bearing latency/resolution/sweep
  policies, and actual human resolution decisions require an effective owner
  act under RFC3-16(a). State (1) is effective and disclosed; state (2) is
  independently verified. No act or invalid act retains the existing
  Unknown/suspension behavior.
- Kernel-recorded admission, rejection and deterministic sweep-resolution
  facts remain kernel facts, never owner acts or adoptable artifacts. They
  carry the authorization provenance of the policy under which they were
  produced without inheriting owner-act status themselves.
- Evidence-origin verification and inference provenance do not change. An
  unverifiable evidence artifact is not converted into an owner act.

### RFC4-7 and RFC4-13(b)

- Registry/checker definitions require effective exact-digest owner adoption.
  State (1) entries/definitions may admit outputs or certify only within their
  declared authority/applicability; state remains visible on every emitted
  fact/result.
- Missing or invalid adoption still admits nothing. Checker authorship/
  certification separation, declared satisfaction semantics and the
  `return PASS` falsifier remain unchanged.

### RFC3-2, RFC3-15, RFC4-12 and RFC4-26

- Kernel resolution records remain kernel facts. Their authority comes from
  checking that the pre-declared resolving policy has an effective owner act
  under RFC3-16(a), with its exact state carried into the record; the record
  never authorizes itself.
- The code-structure observer continues to use only the observing project's
  own secret policy. That policy must have an effective owner act; every SEC-5
  exclusion and fail-closed ingest rule remains unchanged.
- A marker-adoption policy requires an effective exact-digest owner act in
  either state. Markers remain untrusted code-tree text and anchor nothing
  without that separately adopted policy.

### RFC4-23 and RFC8-16

- The worker-liveness staleness bound remains an authorization-bearing policy
  under RFC3-16(a). A valid state-(1) or state-(2) act makes it effective and
  its exact provenance state renders; a missing or invalid act leaves the
  bound undeclared and `active` unrenderable.
- The act warrants use of the bound. It is never evidence that a worker is
  alive, that a progress signal occurred, or that any work succeeded.

### RFC5-15, RFC5-16 and RFC5-18(c)

- Egress still requires in-force per-provider consent, determinable consented
  content classes, one choke point and audit record. Classification policy and
  consent require effective owner acts; state (1) is accepted and disclosed.
- Secret policy requires effective exact-digest owner approval in either state.
  All-sink fail-closed screening and SEC-5 remain unchanged.
- Execution still requires every RFC5-18 limb. Only limb (c)'s provenance
  result changes: a valid state-(1) profile approval may launch; every profile,
  authentication, isolation, capture and destructive-operation gate remains.

### RFC7-21, RFC7-25 and RFC7-31

- Adoption, materiality/review verdicts and walkthrough judgments require real
  human owner acts effective under RFC3-16(a). State (1) may adopt/clear/judge
  while remaining visibly uncorrelated.
- Per-claim attestation, attribution, reasoning, review scope/freshness, owner
  classification, nonvisual execution record and `verdict-unlawful` behavior
  for invalid acts remain unchanged. Agents still cannot adopt their own prose.

### RFC9-8(a), RFC9-18, RFC9-26 and RFC9-45

- Portfolio/layout/channel registries and release policies/waivers/judgments
  require effective exact-digest owner acts in either state. State (1) changes
  no legend, layout, walkthrough, trust-floor or release requirement besides
  the A1-only provenance result.
- Missing/invalid entries remain absent; unlawful verdicts remain fail-closed.
  RFC9-45 remains a walkthrough/release-policy gate, not a generic deployment
  or recovery contract. This amendment creates no deployment or recovery
  authority; those effects remain unavailable until separately contracted,
  specified and authorized.

### The nine accepted phase rules

In RFC1-33, RFC2-26, RFC3-33, RFC4-30, RFC5-27, RFC6-28, RFC7-38, RFC8-32 and
RFC9-52, replace the standard consequence:

> the judgment is honored only where its owner-act provenance is verifiable;
> where it does not verify, the judgment maps nothing

with:

> the judgment is honored only through an effective owner act under RFC3-16(a),
> in state (1) or state (2), with that state rendered; absent or invalid acts
> map nothing and leave the consequence unmapped and Unknown

Every reviewed-N/A home, per-consequence review rule and coverage obligation
remains unchanged.

### Candidate RFC 0010

- `RFC10-4`: a mission requires an effective exact initiating owner act; state
  (1) is permitted and visible, but a machine-submitted record is not an act.
- `RFC10-9`: remove “always an A1-mechanism act” and state-(1) blocking. Mission
  approval and every envelope amendment require an effective owner act in
  either state. Parent/envelope bounds, no self-widening and every other gate
  remain.
- `RFC10-21`: each embedded project's egress consent requires an effective act
  in either state; missing/invalid consent still fails closed.
- `RFC10-24`: record that
  `BOUNDED-MISSION-DOCTRINE-INTERPRETATION-2026-08-31` satisfies the owner-ruling
  alternative. Operation remains impossible until RFC 0010 is accepted, its
  required OpenSpec behavior is signed and every mission gate passes.

RFC 0010 remains candidate and binds nothing. This delta neither accepts it nor
starts a mission.

## What explicitly does NOT change

- Humans remain the only owners. Machines cannot manufacture owner authority.
- Every effect-specific consent, profile, envelope, authentication, scope,
  budget, write-boundary, recovery, stop, evidence and audit gate remains
  conjunctive.
- Observation/write consent remains per repository; egress remains per
  project/provider/content-class set; execution remains profile-bound; writes
  remain attributed, atomic and revertable.
- SEC-5 and the VIS-7 trust floor remain outcome-binding.
- State (1) is never independently verified. State (2) still requires A1.
- An effective owner act is a warrant, never evidence that an effect succeeded,
  a claim is true, completion occurred, effects were applied, recovery worked
  or a release gate passed. A1 correlation and RFC5-25 audit evidence establish
  provenance or occurrence only; they do not establish substantive success.
- RFC5-25 audit evidence remains required for effects even when it is not an A1
  correlation record.
- No current deployment, release, write, egress, execution or mission is
  authorized by this amendment transaction.
- No generic accepted recovery-effect contract is invented. Candidate RFC10
  recovery clauses remain candidate until accepted.
- The superseded read-only transaction and phrase remain never-effective
  historical evidence.

## Warrant

- `GENERAL-TRUSTED-BOOTSTRAP-AUTHORIZATION-DIR-2026-08-31` directs that exact
  owner bootstrap acts may satisfy every existing effect-specific gate without
  external correlation.
- `BOUNDED-MISSION-DOCTRINE-INTERPRETATION-2026-08-31` rules that exact
  owner-approved bounded missions are human-triggered under existing doctrine.

The owner expressly accepts same-tree forgery risk as a trust assumption. The
amendment must expose, not claim to eliminate, that risk.

## Evidence or decision basis

- `.syzygy/governance/decisions/GENERAL-TRUSTED-BOOTSTRAP-AUTHORIZATION-DIRECTION.md`
- `.syzygy/governance/decisions/BOUNDED-MISSION-DOCTRINE-INTERPRETATION-ACT.md`
- `docs/reviews/R-POLARIS-POC-EXCEPTION-SECURITY-RAW.md` records the risk now
  knowingly accepted rather than hidden.
- The retired `agent/syzygy-1z3-trusted-bootstrap` transaction demonstrates the
  exact-digest, act-semantics and full-impact-ledger controls to retain.

## Terms introduced / retired

- **effective owner act** — a real human owner act satisfying RFC3-16(b) and
  current/scope/lifecycle checks, in either provenance state.
- **owner-trusted** — presentation of effective state (1), never a provenance
  state or synonym for verified.
- Retired behavior: A1 correlation as the universal precondition for effect.
- Retained behavior: A1 correlation as the sole precondition for the claim
  `Syzygy-verified`.

## Downstream impact

Baseline fixed-string populations at `20e5b6e`: 191 files cite `RFC3-16(a)`,
45 cite `RFC3-16(c)`, 37 contain “provenance does not verify”, 6 contain
“unverifiable provenance”, 19 contain “verifiable owner-act provenance”, 22
contain `state-(1)`, and 6 contain “A1-mechanism act”. A generated impact
ledger must union and classify every member as edit, re-review or no impact.

Direct edits include installed and candidate-mirror modules for every accepted
clause named above, including every additional explicit A1-only phrase in those
clauses; candidate RFC10 modules; affected package summaries;
Wave-A/B manifests as applicable; active manifest, indexes, context budgets and
task router; governance checks whose assertions hard-code A1-only effect;
signed OpenSpec coverage/spec artifacts whose consequence text or behavior is
invalidated; and current-state pointers after the act.

Pure citations saying “honored under RFC3-16(a)” may remain if they delegate
without restating A1-only behavior, but each still receives a ledger
disposition. Historical acts/reviews remain append-only.

## Migration / supersession plan

1. Build a fresh generalized candidate transaction from `20e5b6e`; do not
   broaden or revive the retired Polaris manifest.
2. Apply exact central and direct-consumer amendments to installed/candidate
   contract mirrors; regenerate all derived artifacts.
3. Update candidate RFC10 and record RFC10-24's doctrine-ruling satisfaction,
   without accepting or operating RFC10.
4. Reconcile signed specs/coverage artifacts under CC-REV-2. A lower-level spec
   may remain stricter, but no matrix may misstate the amended contract.
5. Generate and bind a complete impact ledger and exact act-semantics artifact.
6. Obtain fresh-context security, doctrine, contract and public-interface
   review on frozen bytes.
7. Present one exact-digest owner transaction for the generalized contract
   amendment. It performs no effect-specific act.
8. After acceptance, amend PWB to consume the shared rule; finalize and obtain
   separate consent/policy/registry acts; then resume Polaris implementation.

Rollback before adoption is deletion of this candidate. After adoption, a new
owner amendment restores A1-only effectiveness; prior effect/audit records
remain immutable and disclose the provenance state used.

## Review routing

**Required class:** CC-REV-1 authority boundary, security, deterministic
observation, public interface and execution; CC-REV-4 material amendment

**Reviewer:** independent fresh-context security and contract review. Raw
passes and their exact verdicts are stored in `docs/reviews/`; this candidate
does not carry a desired verdict for a future reviewer.
