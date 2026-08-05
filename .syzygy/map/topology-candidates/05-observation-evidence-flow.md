# 05 — Observation and Evidence Flow

> **Reviewed draft — grounded in proposed foundational contracts (currency note, not an ordering precondition: this bundle's own gate is §2 act 3 of the acceptance record and does not wait on the RFC act).** Reviewed fresh-context (reviews 5–7, dispositions recorded); updated at the rev7 rework for the corrected contracts (D1 historical scope, five governance categories, walkthrough three-way split, captured external confirmation, `Base` scenario context). Becomes canonical only by its **own owner act** — `ACCEPT TOPOLOGY: <bundle-manifest-digest>`, binding the exact digest of every file in the bundle — never implicitly on the RFC gate (RFC3-16: this stamp is a self-declaration; effective status lives in the owner-act record).
>
> Rendering: Mermaid is the durable, renderable fallback chosen for this phase; an Excalidraw + SVG upgrade is a tracked follow-up.

## What this shows

The deterministic path from sources to rendered claims — capture, snapshot,
evaluation, immutable record, claims — and, deliberately separate, the
inference overlay path that can only challenge, never establish. Solid
arrows are the deterministic layer; dashed arrows are the inferred layer.

```mermaid
flowchart TB
    subgraph Sources["Sources — each consented (SEC-4), each identified in the snapshot (RFC2-1)"]
        Repos["Repositories: governance plane,<br/>spec structure, code"]
        Reports["Test / CI / verification reports<br/>(each names the revision it describes)"]
        Runtime["Runtime datasets + declared window"]
        WorkX["Scheduler export + capture instant"]
    end

    subgraph Det["Deterministic path [target] — VIS-7 identity test applies"]
        Obs["Observers / adapters —<br/>registered identity + version (RFC4-2/7);<br/>secret screening at every ingest, fail-closed (SEC-5; RFC5-16);<br/>failure degrades to last-good, marked stale/broken (RFC4-4)"]
        Snap["Source snapshot —<br/>closed rule: uncaptured input = uninfluential;<br/>affected claims render Unknown (RFC2-1/2)"]
        Ev["Identified evaluation =<br/>(snapshot, as-of instant) (RFC2-3);<br/>later evaluation over same snapshot may only degrade (RFC2-4)"]
        Rec["Observation record — immutable,<br/>deterministic facts only, VIS-6 exception (b) (RFC2-6)"]
        Claims["Claim instances —<br/>label (Observed/Inferred/Unknown)<br/>+ tier (6, closed) + Unknown reason (11, closed)<br/>+ freshness (RFC2-24/25)"]
    end

    subgraph Inf["Inference overlay — separate challenge-only path [target] (trust-and-evidence.md seam)"]
        Overlay["Inference overlay — separate artifact:<br/>model + version + exact inputs recorded;<br/>computed only under egress consent (SEC-2; RFC2-7)"]
        Chal["Admitted challenge —<br/>one exact claim, falsifiable concern,<br/>provenance, individually resolvable (RFC2-12/13)"]
    end

    Surfaces["Surfaces + machine endpoints —<br/>render label + tier + reason verbatim (RFC6-14)"]

    Repos -->|"captured: capture instant + capturing observer identity/version (RFC4-3)"| Obs
    Reports -->|"captured; revision-bound (RFC2-11)"| Obs
    Runtime -->|"ingested with window"| Obs
    WorkX -->|"captured before retention horizon (RFC4-16)"| Obs
    Obs -->|"identified inputs, by version or hash"| Snap
    Snap -->|"plus explicit as-of instant — never ambient clock"| Ev
    Ev -->|"produces exactly one record per evaluation"| Rec
    Rec -->|"supports — the ONLY path from evidence to positive status (RFC1-24)"| Claims
    Claims -->|"one drawer fact set per selection (RFC6-18)"| Surfaces

    Snap -.->|"consented inputs only; absent consent overlay is NOT computed → Unknown (RFC2-7)"| Overlay
    Overlay -.->|"submits challenges; may propose, visually distinct, never anchors the map (RFC2-8)"| Chal
    Chal -.->|"conservative suspension: claim renders Unknown (challenge-suspended), deterministic basis stays visible (RFC2-8/14)"| Claims
```

## Authority boundaries

- **The seam is structural** [Observed: trust-and-evidence.md]: observation
  records contain deterministic facts only; overlays are separate,
  separately versioned artifacts excluded from the VIS-7 identity test. An
  LLM assertion is Inferred, never Observed.
- **Challenge authority only** [Observed: RFC2-8]: an overlay never
  establishes, raises, or independently satisfies a positive status claim.
  Only `gate-backed` Observed evidence turns anything green (RFC2-25).
- **Time is an input** [Observed: architecture.md]: no status changes
  without a new identified evaluation; the wall clock never flips a badge.
- **Failure is rendered** [Observed: RFC2-23]: broken observers, unreachable
  sources, withdrawn consent, partial snapshots, excluded secrets, and
  missing quantities each have a defined rendering — Unknown with reason,
  never silence, never zero.

## [target] vs already true

- **[target]:** the entire pipeline — no observer, snapshot, evaluation, or
  overlay machinery exists.
- **[Observed] today:** the semantics are fixed by adopted doctrine
  (snapshot closed rule, temporal rule, seam) and drafted in RFC 0002/0004;
  the twelve Unknown reasons and six tiers are RFC-draft vocabulary, not yet
  accepted.
- **[Inferred]:** initial capture fidelity will be constrained by the
  substrate's forgetfulness (squash-merge history loss, `bd gc` horizons) —
  RFC 0004 renders that as labeled reduced fidelity rather than invented
  precision (RFC4-16/24).
