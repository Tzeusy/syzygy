# 06 — Intent to Reconciliation Flow

> **Reviewed draft — grounded in proposed foundational contracts (currency note, not an ordering precondition: this bundle's own gate is §2 act 3 of the acceptance record and does not wait on the RFC act).** Reviewed fresh-context (reviews 5–7, dispositions recorded); updated at the rev7 rework for the corrected contracts (D1 historical scope, five governance categories, walkthrough three-way split, captured external confirmation, `Base` scenario context). Becomes canonical only by its **own owner act** — `ACCEPT TOPOLOGY: <bundle-manifest-digest>`, binding the exact digest of every file in the bundle — never implicitly on the RFC gate (RFC3-16: this stamp is a self-declaration; effective status lives in the owner-act record).
>
> Rendering: Mermaid is the durable, renderable fallback chosen for this phase; an Excalidraw + SVG upgrade is a tracked follow-up.

## What this shows

The full loop from adopted intent to a reconciliation verdict, with every
human-triggered gate marked (hexagons), the one-way materialization door,
and the post-merge reconciliation chain (RFC2-18) — with its four
separately-named, separately-routed outcomes — that no substrate provides
today. The whole loop is human-triggered; nothing here runs autonomously.

```mermaid
flowchart TB
    Intent["Adopted intent — openspec/** requirements,<br/>governance artifacts (desired plane)"]
    Observed["Observed state — at an identified evaluation"]
    Delta["V0: absence surfaced, rendered Unknown [target]<br/>V1: gap computed as navigable object [target]<br/>(v1.md V0/V1 boundary)"]
    Confirm{{"Confirmation act — Decision or declared Policy:<br/>a derived gap is never its own work warrant (RFC1-21)"}}
    Prop["Proposal, kind: execution intent —<br/>carries exclusivity group (RFC1-27)"]
    Approve{{"OWNER approval Decision (VIS-4) —<br/>proposal enters state approved"}}
    Plan["Approved plan item —<br/>lives in .syzygy/work/** until materialized<br/>(RFC1-28; SDR-7)"]
    Mat["Materialization — ONE-WAY door:<br/>immutable record maps proposal → work-item set,<br/>pins the warranted intent revision (RFC1-29; RFC3-19)"]
    WI["Scheduler work items —<br/>Beads authoritative for lifecycle from here (SDR-7)"]
    Exec["Worker execution — outside Syzygy's body;<br/>captured as Execution Records, evidence about work,<br/>never proof intent is satisfied (SDR-8; RFC1-22)"]
    Merge["Merge fact — from the VCS adapter only,<br/>never inferred from scheduler closure (RFC2-20)"]
    Pending["reconciliation-pending —<br/>the honest default state of all merged work (RFC2-18)"]
    Trigger{{"HUMAN-TRIGGERED propagate / observation pass —<br/>reconciliation never runs on merge events (RFC2-19)"}}
    RecEval["Reconciliation evaluation [target, V1 computes; V0 renders absence] —<br/>snapshot includes post-merge revisions + pinned intent revision<br/>+ claimed verification evidence (RFC2-18)"]
    Rc["reconciled@E —<br/>requires gate-backed Observed evidence"]
    Uns["unsatisfied —<br/>warranted intent not satisfied, nothing co-unsatisfiable:<br/>by definition a gap (RFC2-18)"]
    Cdr["contradiction-raised —<br/>co-unsatisfiable authoritative claims: mints a Contradiction,<br/>conclusion renders Unknown (contradicted-pending-adjudication)<br/>(RFC2-15/18)"]
    Unk["Unknown(reason) —<br/>could not decide; reason from RFC2-24"]
    Owner{{"OWNER — adjudicates Contradictions (RFC1-25)<br/>and receives spec-indictments:<br/>the loop's one upward arrow (architecture.md)"}}

    Intent -->|"compared against"| Delta
    Observed -->|"compared against"| Delta
    Delta -->|"motivates work only through"| Confirm
    Confirm -->|"warrants authorship of"| Prop
    Prop -->|"adoption gate"| Approve
    Approve -->|"same entity, same identity; approval mints nothing new"| Plan
    Plan -->|"deliberate act"| Mat
    Mat -->|"creates, via typed Beads adapter"| WI
    WI -->|"dispatched to actuator toolchain"| Exec
    Exec -->|"change reaches integration branch"| Merge
    Merge -->|"attaches automatically + deterministically"| Pending
    Pending -->|"evaluated only inside"| Trigger
    Trigger -->|"runs"| RecEval
    RecEval -->|"verdict"| Rc
    RecEval -->|"verdict"| Uns
    RecEval -->|"verdict"| Cdr
    RecEval -->|"verdict"| Unk
    Uns -->|"opens a gap — which re-enters the loop only through the confirmation act (RFC1-21)"| Delta
    Uns -->|"or routes upward as a spec-indictment"| Owner
    Cdr -->|"only lawful exit: an adjudicates Decision (RFC1-25) — never precedence, never auto-scheduled, and NEVER a gap opened on its behalf (RFC2-17/18)"| Owner
```

## Authority boundaries and gates

- **Human gates (hexagons):** gap confirmation, proposal approval, the
  propagate/observation trigger, the owner's adjudication of Contradictions,
  and the owner's handling of spec-indictments — two distinct owner acts, not
  one. Autonomy beyond VIS-4's bounds is licensed only through the mechanism
  VIS-4 names.
- **The two negative outcomes never merge** [Observed: RFC2-17/18]:
  `unsatisfied` means the warranted intent revision is not satisfied and
  nothing is co-unsatisfiable — that is a **gap**, so it opens one or routes
  upward as a spec-indictment. `contradiction-raised` means the evaluation
  found co-unsatisfiable authoritative claims — a **Contradiction** is minted,
  the conclusion renders Unknown (reason #8, `suspended` tier), and its only
  lawful exit is an `adjudicates` Decision: never resolved by precedence,
  never auto-scheduled into work, and specifically **never routed into work
  through a gap opened on its behalf** (RFC1-21). The two are separately
  named, separately counted, and separately routed; no surface, aggregate,
  endpoint, count, or UI string may merge them (RFC2-17).
- **Sequenced authority, no duplication** [Observed: RFC1-29]: before
  materialization the approved Proposal in `.syzygy/work/**` answers "what
  is the state of this planned work"; after it, the scheduler through its
  typed adapter. The materialization record is immutable — later scheduler
  divergence is a fact about the scheduler, never grounds to rewrite it.
- **Execution never proves intent** [Observed: vision.md thesis; RFC1-22]:
  merged and closed are execution states; the reconciliation verdict binds
  to the *warranted* intent revision, so post-merge intent drift surfaces
  as a new gap, not retroactive failure (RFC2-18).
- **The closure fallacy is forbidden** [Observed: RFC2-20]: scheduler
  closure never implies reconciled; scheduler-internal "reconciliation"
  (state repair) never shares a field or count with this chain (RFC2-17).

## [target] vs already true

- **[target]:** the entire flow. V0 targets: absence surfacing, the
  propagation proof-of-concept slice (one spec delta → one dispatched work
  item), and honest "reconciliation evidence absent / Unknown" rendering
  for merged work (SDR-12). V1 targets: gap computation and the computed
  reconciliation evaluation.
- **[Observed] today:** the reconciliation evaluation exists nowhere in any
  substrate — no object, no field, no convention (RFC 0002 Summary); the
  chain is created by these drafts.
- **[Inferred]:** the wall of reconciliation-pending Unknowns on a
  fleet-built project will be V0's most visible honest output; doctrine
  classifies it as correct, not a defect (RFC2-19).
