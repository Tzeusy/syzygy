# Capability 1 specification-outline exercise 2 — round 2026-08i

> **An exercise, not a specification.** This file tests **chartered
> feasibility** — could a spec author, starting from the charter and the
> reviewed CC-SPEC standard, produce a lawful specification without
> running out of authority? It authors no requirement, creates no
> `openspec/` content, decides nothing, and is superseded by any real
> specification the owner later authorizes. Authoring remains forbidden
> until the owner's launch decision.
>
> **Provenance, disclosed:** authored 2026-08-17 by the convergence-pass
> lead session — **not blind**, unlike the round-2026-08f exercise
> (RD-60, administered 2026-08-11 to a fresh-context agent and graded).
> This pass's structure is `[Inferred]` from the sources below; the
> feasibility comparison against RD-60's blockers is `[Observed]` from
> the cited records.
>
> Sources, at their current digests:
> - `../CAPABILITY-1-CHARTER.yaml` — sha256
>   `aa71b9b2c0d82158f96ecc175d226ff00ea9b36f1cfbd6e832111cbf50934f58`
>   (the one source; views regenerated drift-free this session)
> - `../policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`
>   (CC-SPEC-1…11) — the RD-70-confirmed bytes, act 6's argument
> - `../round-2026-08f/CAPABILITY-1-SPEC-OUTLINE-EXERCISE-RAW.md` (RD-60)
>   — the predecessor, for the delta section only

## 1. The capability, in the charter's one sentence

> A project can be registered and its shape read honestly — every facet
> answered on its own, every Unknown carrying its reason and its owning
> authority, and the same facts reaching a human and a machine — without
> any claim the evidence does not support.

Discharges **CC-SPEC-1** (one coherent capability, in/out named): the
sentence is the capability; the charter's `non_goals` list is the "out";
SDR-37's granularity rule is satisfied — one change, one capability, one
acceptance decision.

## 2. The outline — sections, and the CC-SPEC clause each would discharge

| § | Section (heading only — no requirement text) | Charter row(s) | Discharges |
|---|---|---|---|
| S0 | Scope statement: the sentence above; in-scope facets; the non-goals verbatim; the deferred-semantics table (Mission-ready renders `not evaluated / deferred / Unknown`) | header, `non_goals`, `deferred_semantics` | CC-SPEC-1, CC-SPEC-5 |
| S1 | Facet vocabulary — authored **here**, per SDR-36 (site a2): the facet names, definitions, constituent facts, and evaluation semantics this spec owns | `deferred_semantics` "facet vocabulary" | CC-SPEC-1 (scope), CC-SPEC-6 (the ruling is recorded, not silently selected) |
| S2 | Registration: declaration parse/validate; invalid ⇒ named failure, never partial registration | 1.1 | CC-SPEC-2, -3, -4 per requirement |
| S3 | Consent and coverage: boundary renders as fact, not silence | 1.2 | CC-SPEC-2, -3, -4 |
| S4 | Human entry at the declared entry path (P-38 ruled: as drafted) | 1.3 | CC-SPEC-2, -3, -4 |
| S5 | Shape facets answered independently — no rollup, no composite badge; uncomputed reconciliation renders Unknown (P-31/SDR-34: RFC2-19(a) as written) | 1.4 | CC-SPEC-2, -3, -4 |
| S6 | Owning authority + Unknown reason on every answer, identically human and machine (P-36/SDR-35 Unknown-vs-gap boundary as ruled) | 1.5 | CC-SPEC-2, -3, -4 |
| S7 | Discoverability in the closed four-value domain; propose the link, never write it | 1.6 | CC-SPEC-2, -3, -4 |
| S8 | Acceptance forms: the named falsifiable form for every requirement above; the parity oracle domain is RFC6-23's enumeration | all | CC-SPEC-4 |
| S9 | Coverage matrix (deliverable, per §3 below) | all | CC-SPEC-8 |
| S10 | Completeness table: population = the S0 scope statement's declared obligations, each `covered` / `lawfully out of scope` / `Unknown, unresolved`, summing; non-author confirmer | all | CC-SPEC-11 |
| S11 | Unknowns and open questions carried on the surface (see §4 residue) | — | CC-SPEC-5, CC-SPEC-6 |
| S12 | Adoption record: the exact digests of the accepted waves and the craft acts this spec is judged under | — | CC-SPEC-10 |

No section names a stack, schema, or mechanism — registration and
rendering are specified behaviorally, so **CC-SPEC-7** is discharged by
omission, checked at review. **CC-SPEC-9** (fresh-reader restatement) is
a property of the finished text, testable only then.

## 3. The coverage matrix the specification would face

Population `[Observed]` from the charter (self-checked at generation):
**29 governing clauses across 6 behavior rows**, resolving into Wave A
modules (RFC-0001, -0002, -0003, -0005, -0006) and Wave B modules
(RFC-0007, -0008) — no deferred-wave module, enforced by generation.

Under the repaired **CC-SPEC-8**, the matrix's unit is the contract's:
**rows are per observable consequence, not per clause** — so the row
count exceeds 29 and is knowable only at authoring, when each clause's
observable consequences are enumerated. Any N/A row requires a recorded
**owner** judgment homed in `decisions/`, verifiable under RFC3-16(a);
the author's or a reviewer's say-so discharges nothing. Given every
charter clause was added as a verified *reliance* (rule 5), the expected
N/A count for chartered clauses is zero `[Inferred]`; N/A pressure will
come from the phase-rule clauses' own modules when applicability is
tested clause-by-clause against S0.

## 4. Delta against the round-2026-08f exercise (RD-60)

RD-60's §3 listed **13 blockers**. Their state today `[Observed]`:

| RD-60 blocker | State 2026-08-17 |
|---|---|
| P-37 facet vocabulary (its "single largest hole") | **Ruled** (SDR-36): this spec owns the vocabulary — S1 exists because of it; the *text* still needs authoring |
| P-36 Unknown vs gap | **Ruled** (SDR-35) |
| P-38 human entry | **Ruled** (as drafted) |
| P-40 granularity | **Ruled** (SDR-37); CC-SPEC-1 re-grounded on it |
| P-39 OpenSpec form/version | **Ruled** — pinned 1.9.0 (`GOVERNANCE-SUBSTRATE-LOCK.yaml`) |
| P-41 + P-42 acceptance standard | **Offer open** — review cycle closed (RD-69→RD-70), acts 6/7 minted; the act itself is the owner's |
| P-33 Wave A install shape | **Ruled** (shape M, zero bytes moved — the RD-60 worry "bytes regenerated before any act" did not materialize) |
| P-31 merged-but-unreconciled | **Ruled** (SDR-34) |
| P-35 / P-34 operating constraints, launch gate | **Both ruled** (P-34 arm (a): v2.4 approved, two residuals disclosed) |
| RFC-0003 §7 q1 (monorepo subprojects) | **Still open in the clause bytes** — S2 carries it as a disclosed Unknown (CC-SPEC-6 route if a requirement would silently select an answer) |
| RFC-0001 §8 q1–q3, RFC-0003 §7 q2 | **Still open in the clause bytes** — S11 residue |
| A1 correlation mechanism (RFC3-16 "owner-adopted bootstrap") | **Still true** — S12 records adoption at digests; correlation stays out of scope for Capability 1 |
| The owner's launch decision | **Unmade — authoring remains forbidden.** |

Net: **9 of 13 blockers ruled away; 4 remain**, of which three are
open-in-the-contract questions the spec can carry as disclosed Unknowns
and one — the launch decision — is the gate this whole pass exists to
tee up. RD-60's two biggest *reading* gaps (RFC-0006 unrouted;
RFC3-16(a) unread) are closed structurally: both are now chartered
governing clauses, so the router loads them for the authoring task.

## 5. Feasibility statement

`[Inferred]` **Chartered feasibility holds.** Every S-section traces to
a charter row or a ruled decision; every CC-SPEC-1…11 obligation has a
section that would discharge it; no section requires an unruled decision,
a deferred-wave clause, or an authority that does not exist. The
remaining prerequisites are exactly the acts already queued — Waves A and
B, acts 6 and 7 — plus the formal administration and the owner's launch
decision. What this exercise cannot show: that the requirement *text*
survives CC-SPEC-4/9 review — only authoring shows that, and authoring
waits for the owner.
