> **Approved** — owner decision D2 (2026-08-01), amendment B21 applied where noted. **This directory (`.syzygy/governance/policies/craft-and-care/`) is the canonical home of these policies.** The bootstrap-phase copy is preserved separately as historical review evidence. Binding force on implementation work begins with the owner's digest-bound acceptance of the foundational design contracts (the act defined in the active acceptance record; the policies cite RFC clauses that bind nothing until then).

# Observability and operations

Syzygy's observation is deterministic, its inference stays visibly separate,
its failures leave labelled, durable traces, re-running it is safe, and its
own status meets the evidence bar it renders — because the observer *is*
the product.

- **Baseline, applied by reference:**
  - canonical bias 3: bias toward observability — failure paths diagnosable
    with structured context;
  - canonical bias 6: fail-fast over silent fallback.
- **Why Syzygy sharpens them:** an operational failure that hides itself
  doesn't just complicate debugging — it makes the product lie.

## CC-OBS-1 — Observation is deterministic; freshness is identity-bearing

The deterministic layer of an observation record is a pure function of the
identified evaluation (source snapshot + as-of instant), and its logical
freshness state is part of that identity [Observed — VIS-7; architecture.md
temporal model].

- **The identity test:**
  - identical across runs, byte-comparable;
  - **logical freshness state (fresh, stale, broken, superseded) is inside
    the identity test**;
  - only display formatting (localized timestamps, relative-age strings) is
    excluded, and extending that exclusion is a doctrine amendment.
- **Engineering consequences:**
  - no ambient inputs: wall-clock reads, environment lookups,
    unsnapshotted files, or network state may not influence deterministic
    claims — a source not captured in the snapshot renders unavailable or
    Unknown instead;
  - all time-sensitive judgments (currency, staleness, dismissal expiry)
    are computed at the evaluation's as-of instant, passed explicitly;
  - time may only degrade a claim through a new identified evaluation,
    never establish or improve one.
- *Violation:* a staleness check that calls the system clock at render time,
  so the same observation record flips from fresh to stale between two page
  loads with no new evaluation.

## CC-OBS-2 — Inference is never rendered as observed fact

Deterministic facts and inferences are computed and stored in distinct
layers, and inferred structure is never rendered as observed fact.

- **The inferred layer** [Observed — trust-and-evidence.md]:
  - is a separate artifact recording model, version, and inputs;
  - is excluded from the VIS-7 identity test;
  - holds challenge authority only — it may conservatively suspend a claim
    to Unknown (with its provenance rendered), never establish or raise
    one.
- **Rendering may blend layers only when** inferred structure stays
  visually distinct and provenance is available at the point of
  consumption.
- **A worker's assertion** is a report fact, not the asserted fact (SDR-9;
  the full rendering-tier policy is CC-PROV-4).
- *Violation:* an inferred capability-to-code mapping drawn with the same edge
  style as a declared mapping, "because it's probably right."

## CC-OBS-3 — Degradation is labelled; fidelity is never invented

Adapters and observers degrade **explicitly**: stale, coarse, or unknown
data is labelled as such, never passed off as current or fine-grained.

- **A broken observer** degrades to its last-good observation record,
  clearly marked stale/broken on the primary surface — it never fails
  invisibly [Observed — trust-and-evidence.md, staleness].
- **Where a source offers only coarse data**, the surface renders **reduced
  fidelity explicitly** rather than fabricating fine-grained certainty.
  - E.g. PR-level data is rendered as PR-level, never dressed as
    event-level (SDR-33).
  - Adapters degrade with labeled staleness [Observed — FD-020 E7-b].
- **Every degradation state carries a reason** from the closed
  unknown-reason vocabulary (RFC 0002 material).
  - "Unknown" without a reason class is a finding once that vocabulary
    exists.
- *Violation:* an adapter that, unable to reach CI, re-renders yesterday's
  check results with today's evaluation — silently, as current.

## CC-OBS-4 — Operational failures leave durable, identified traces

Every observer, adapter, or pipeline failure produces a durable, identified
failure record with enough structured context to narrow plausible causes —
not merely "sync failed."

- **Structured context:** source, operation, evaluation identity, error
  class.
- **Failure records are evidence-grade:** they carry source, capture time,
  scope, and provenance like any other evidence artifact [Observed —
  trust-and-evidence.md, evidence definition].
- **Fail-fast is the default.** Graceful degradation exists only where
  CC-OBS-3 explicitly labels it.
- *Violation:* a scheduled observation pass that catches all exceptions, logs
  `refresh failed` to a rotating debug log, and leaves the surface rendering
  the previous pass unmarked.

## CC-OBS-5 — Authoritative effects are idempotent

A pass over an unchanged, no-gap source snapshot — at any as-of instant —
must not mutate authoritative artifacts, create or reprioritize work, or
establish or improve any status claim [Observed — architecture.md,
idempotence invariant, constitutional].

- **Operational jobs** (sync passes, refreshes, re-evaluations) are
  engineered and tested to this invariant; re-running is always safe.
- **Derived conveniences** (cache reuse, zero-token sync, byte-identical
  inference output) are engineering goals sacrificial under VIS-1, rank 5 —
  never bought with rank-1 truth.
- *Violation:* re-running an unchanged sync pass bumps every work item's
  "last-touched" ordering, silently reprioritizing the queue.

## CC-OBS-6 — Syzygy's own operations meet the evidence bar it renders

Operational claims about Syzygy itself — "the nightly evaluation ran," "the
index is current" — follow the same rules as claims about governed
projects: current evidence or Unknown. [Inferred — doctrine states the trust
floor for Syzygy's surfaces; extending it to self-status is this cluster's
addition.]

- **Health/status endpoints** render evaluation identity and freshness, not
  a bare `ok`.
- *Violation:* a `/health` endpoint hardcoded to return `ok` while the
  observation pipeline has been failing for a week.
