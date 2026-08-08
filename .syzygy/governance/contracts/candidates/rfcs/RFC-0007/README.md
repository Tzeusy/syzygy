---
id: RFC-0007
title: Polaris (Intent Surface) — contract package index
status_source: owner-act-record
package: RFC-0007
modules: [narrative-contract, rendering-and-surface]
clauses: RFC7-1..RFC7-40 (sub-clauses RFC7-2(a)-(c), RFC7-9(a)-(c), RFC7-11(a); no gaps, no retired numbers, no merges)
implementation_boundary:
  kind: requires-openspec
  clause: RFC7-38
governs: [intent, narrative, section, claim-block, source-anchor, reading-order, citation-graph, curated-diagram, editorial-draft, portfolio-narrative]
applies_to: [polaris]
depends_on: [RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0009]
tags: [presentation, non-authoritative, progressive-disclosure, comprehension-test, machine-parity, editorial-draft, target-state-drift]
---

# RFC 0007 — Polaris (Intent Surface)

**Status:** Proposed foundational contract (self-declaration at authoring
time). Effective status is established solely by an owner-act record binding
each module file's exact content digest — as an owner-adopted bootstrap act
until the independent A1 correlation mechanism exists, and as a Syzygy-verified
effective act only after correlation (RFC3-16). Absent such a record, this
contract binds nothing.

**Date:** 2026-07-30 (amended through 2026-08-02; compacted and split into a
package at rev10). **Rationale, amendment history, alternatives, and answered
§8 questions:** `../../history/RFC-0007-history.md` (non-normative).

**Serves:** VIS-1…VIS-7; SEC-2, SEC-3, SEC-4, SEC-5. Implements **owner
rulings** SDR-13, SDR-14, SDR-15, SDR-16, SDR-17, SDR-18; honors SDR-27 for
non-visual parity and SDR-28/29/30 for portfolio rendering; resolves the
Polaris portion of SDR §5 question 10.

---

## Clause map and lookup rule

**Every clause identity appears in exactly one module.** One `RFC7-n`
namespace, no duplicated normative clauses, no renumbering.

| Module | File | Clauses |
|---|---|---|
| 1 — the curated narrative contract | `narrative-contract.md` | RFC7-1..RFC7-25, incl. RFC7-2(a)-(c), RFC7-9(a)-(c), RFC7-11(a) |
| 2 — rendering and surface | `rendering-and-surface.md` | RFC7-26..RFC7-40 |

Module sizes are deliberately **not stated here**. A measurement copied into
contract prose goes stale the moment any module moves, and moves this
package's content digest for a reason that has nothing to do with what the
package says. This artifact is governed by the applicable context-budget
policy; the current measurement lives in the generated budget report
`../../CONTEXT-BUDGET-REPORT.md`, which is regenerated, never transcribed.

**Lookup rule (deterministic).** For any citation `RFC7-n`, read `n` as an
integer: `n ≤ 25` → module 1; `n ≥ 26` → module 2. Every lettered sub-clause
lives with its parent — `RFC7-2(a)`–`(c)` and `RFC7-9(a)`–`(c)` and
`RFC7-11(a)` are all in module 1. The two ranges are contiguous and exhaustive
over RFC7-1…RFC7-40 with no gaps, so the rule never needs a search. Modules are
numbered for reading order only — citations name clauses, never modules.

**Reading order for a cold reader:** module 1 → module 2. Module 1 is
presupposed by module 2 (every clause there stands on RFC7-2 and RFC7-3);
module 2 is independently readable given module 1's two invariants and its
entity model.

**Where the seam falls.** Module 1 answers *may this sentence exist in curated
narrative, and what act does it take to put it there?* Module 2 answers *what
must the surface show, prove, and never blur?* No clause spans the seam. Twelve
citation edges cross it, all resolvable by the lookup rule above: module 1 →
module 2 at RFC7-6→RFC7-30, RFC7-11/11(a)→RFC7-33, RFC7-14→RFC7-26,
RFC7-17→RFC7-26/33, RFC7-20/25→RFC7-33; module 2 → module 1 at
RFC7-26→RFC7-17, RFC7-27→RFC7-2, RFC7-29→RFC7-14/18/23, RFC7-30→RFC7-6,
RFC7-31/32→RFC7-25, RFC7-33/34→RFC7-5/11/11(a)/13, RFC7-36→RFC7-2/3/7/11/11(a).

## Package reader map (non-normative)

*If this map and a clause disagree, the clause wins.*

Polaris is the **intent surface**: an argued, progressively disclosed account —
thesis → promises → architecture → capabilities → exact requirement text — with
evidence and work one step away. Two load-bearing invariants govern everything
in both modules:

- **every load-bearing narrative claim is anchored, marked non-normative, or
  epistemically labelled** — there is no fourth kind, and the check binds every
  act that produces narrative, not one path through it (module 1, RFC7-2);
- **nothing anywhere in Syzygy may cite a Polaris rendering as authority** —
  deleting everything under `.syzygy/intent/**` changes no truth, status, work,
  consent, or normative fact (module 1, RFC7-3).

The feared failure is not fabricated prose but a *faithful paragraph later
quoted instead of the rule*. Three mechanisms close the three doors to it:
**citation** is closed by RFC7-3; **generation** by the non-citable
`editorial-draft` state and its human adoption gate (RFC7-20/21); and **time**
by anchors that record their target's state at authorship, so a cited rule that
moved renders as drifted rather than as current (RFC7-10, RFC7-11(a)).

Two further obligations span the package: every distinction either module draws
is a **machine-readable attribute, recoverable without colour or layout, and
reachable without a pointing device** (module 2, RFC7-33/34) — a distinction
only pixels carry does not survive an endpoint response; and the surface's
acceptance test is a **cold-open comprehension walkthrough** whose last prompt
asks the reader to name one thing the project does not know about itself, so a
surface passable only by confident green fails (module 2, RFC7-30/31).

## Scope

This package is the semantic contract of the intent surface: "a cohesive visual
argument for what a project is, why it exists, what it promises, how it is
architected, and what its specifications require, progressively disclosing from
white-paper narrative into exact capabilities, requirements, contracts,
evidence, and work" [Observed: SDR §2 charter]. It defines the **curated
narrative model** (narrative, section, claim block, reading order, citation
graph) as a **governed presentation artifact** per SDR-13 — versioned,
attributed, revertible, human-readable, **non-authoritative**; claim blocks and
source anchors including the target-state component; the verbatim specification
leaf; the capability deep-dive band contract; generated editorial drafts and
their adoption gate; the authoring acts, gates, and materiality review; the two
reading modes and proposed-state rendering; the authority boundary; the
fresh-reader comprehension test; machine parity and non-visual recoverability;
and multi-project, subproject, and portfolio navigation. It is **semantics
only**: no renderer, layout, file format, or stack.

## 2. Doctrine grounding (non-normative)

[Observed] Doctrine gives Polaris identity and anti-thesis at once: Syzygy is
"not a documentation portal" — "a Syzygy from which no work is ever dispatched
has failed, regardless of how good its documents look" [vision.md] — yet the
intent surface must displace "the README-and-ad-hoc-investigation ritual as
the owner's instinctive first stop" [vision.md, Success]. The charter's
not-satisfied-by list binds (SDR §2). [Inferred] Two opposite failures must
both be designed against: the **document browser** (authority present, no
argument) and the **detached brochure** (argument present, prose unanchored —
and, worse, *cited*). **The dangerous artifact is not fabricated prose but a
faithful, correctly-derived paragraph later quoted instead of the rule** — a
second source of doctrine formed with nothing amended. This is the failure mode
RFC7-11(a), RFC7-12, and RFC7-14 cite.

[Observed] The owner resolved the research's central governance question
against its recommendation, and this package binds the rulings: SDR-13 — the
narrative is **a governed presentation artifact**, explicitly *not* the
recommended structure/prose split; SDR-14 — fresh-reader review is scoped to
material changes and release milestones; SDR-15 — generated prose is a
non-citable editorial draft until human adoption; SDR-16 — citation
granularity is the claim block; SDR-17 — status is minimal by default;
SDR-18 — Trajectory owns the drafting queue, Polaris the contextual
authoring/adoption experience.

## 4. Violation cases — package-spanning

*Cases 1–7, 12 and 14 are in module 1, cases 8, 9 and 11 in module 2.
Numbering is the stable package numbering; cases are distributed, never
renumbered. Cases 10, 13 and 15 span both modules and are held here: each
turns on a module-2 encoding or reachability obligation failing in a way that
defeats a module-1 invariant — RFC7-3's non-citability in case 13, and the
RFC7-2/RFC7-3 reading a machine consumer or non-visual reader is left with in
cases 10 and 15.*

10. *(RFC7-33/34, defeating RFC7-2/3)* Band structure carried only by
    background colours; a plain-text export losing the adopted/unadopted
    distinction.
13. *(RFC7-33 / RFC7-3)* An endpoint response or plain-text export carries a
    curated narrative's epistemic labels, resolvable anchors, and evaluation
    stamps but no `non-citable` / `presentation-artifact` attribute — and an
    external agent, unbound by RFC7-3, cites the paragraph in a work warrant.
15. *(RFC7-34/30, defeating RFC7-13's per-altitude obligation)* Every rendered
    unit is recoverable without colour or layout, and the disclosure path from
    thesis to verbatim leaf can only be traversed with a pointer — passing the
    comprehension test every time.

## 5. Integration — package-level

**Relies on RFC 0001:** the presentation profile (RFC1-7), which RFC7-5
requires and drafts rather than presumes; opaque identifiers (RFC1-10);
capability identity and no-silent-inference (RFC1-14); mapping-class
distinctness (RFC1-16); the badge rule (RFC1-19), which reaches both modules;
the plane rule (RFC1-22); the Claim entity and status routing (RFC1-5,
RFC1-24) the narrative claim-block type name must stay distinct from; Proposal
exclusivity (RFC1-27). **On RFC 0002:** the verbatim label + tier + reason +
freshness vocabulary (RFC2-10/24/25) — including `editorial-draft`, minted as
the third sibling surface state on this package's own reported distinction;
the inference-overlay discipline (RFC2-7); the admissibility floor made
operational (RFC2-12) behind RFC7-9; V0 reconciliation staging (RFC2-19); and
the revision-binding pattern (RFC2-11, RFC2-18), which RFC7-10's target-state
component **imitates and never extends** — RFC7-11(a) is a Polaris-local
rendering marker over a resolving anchor and mints no RFC2-24 Unknown reason.
**On RFC 0003:** `intent/` as a schema-versioned governed namespace (RFC3-18)
and its exclusion from cache (RFC3-20); spec anchors (RFC3-28) and the verbatim
identity scheme (RFC3-27); workspace-manifest boundaries (RFC3-10…14);
governance declarations (RFC3-17); the `kernel-recorded` record home (RFC3-15);
child-label pass-through (RFC3-32); local-state rules (RFC3-21); and the
**owner-act provenance predicate (RFC3-16(a))**, which gates three clauses
across both modules — draft adoption (RFC7-21), the review verdict (RFC7-25),
and the comprehension-test judgment (RFC7-31). **On RFC 0004:** the OpenSpec
adapter's verbatim read and anchor obligations (RFC4-10); the anti-duplication
invariant (RFC4-5). **On RFC 0005:** the egress choke point (RFC5-14/15) behind
RFC7-20; act attribution (RFC5-25) behind RFC7-7. **On RFC 0006:** selection
references, outcomes, URLs, label parity, the single drawer, the aggregation
contract, and scenario contexts — cited throughout, duplicated nowhere.

**Defects reported (not silently diverged from):**

1. **RFC 0002 / RFC 0006 — dangling-anchor vocabulary. Live.** RFC7-11's broken
   anchors land in RFC6-5's `unresolvable` outcome, but RFC2-24 has no Unknown
   reason whose resolution route is "repair the reference"; RFC 0006 already
   reported this, and Polaris is the most exposed surface. This package
   supports adding `reference-unresolvable` to RFC2-24; RFC 0002 has added it
   as reason #11 citing this finding, and the owner may still strike it at
   acceptance.
2. **RFC 0002 — RFC2-25 sibling surface states. Discharged, owner decision
   B10** (carried in RFC7-20; report narrative in history).
3. **RFC 0001 — RFC1-7 vs RFC1-22, personal view state. Resolved**; no RFC 0001
   change outstanding, RFC7-5 needs none (trail in history).

**Provides to RFC 0008 (Trajectory):** the SDR-18 seam obligations
(RFC7-22/24). **Provides to RFC 0009 (Orrery):** the curated-versus-computed
provenance attribute (RFC7-28) and the transclusion question (§7); RFC7-31 and
RFC9-45 state one verdict protocol.

## 6. Alternatives considered

Moved to history in full. Two remain load-bearing for interpreting live
clauses: the **structure/prose governance split** was rejected by the owner
(SDR-13), so materiality — not which half was touched — is the gate axis
(RFC7-25); and modelling **narrative edits as kernel Proposals** was rejected,
so RFC1-27's kind list needs no presentation kind. Four further rejected
alternatives (per-sentence badges; generated prose banned outright; a
portfolio meta-project; Polaris-local status vocabulary or rollups) are in
`../../history/RFC-0007-history.md` §6.

## 7. Deliberately deferred — package-level

Concrete `.syzygy/intent/**` schemas, file grammars, and anchor wire syntax →
implementation under accepted contracts (RFC3-18 versioning and migration
apply). Reader-controlled status density (SDR-17's "later") → post-acceptance
spec material; the minimal default binds now. Live transclusion of Orrery
scenes, and whose reproducibility obligations follow the embed → RFC 0009
coordination; until then, link-out. Blast-radius preview of proposed changes →
V1 gap-computation material (RFC2-19 staging); nothing in RFC7-26's proposed
mode computes deltas. Certificate rendering → post-V1 certificate RFC.
Portfolio-profile detail beyond RFC7-35/36 (cross-project saved selections,
workspace URLs) → RFC 0006's portfolio-profile deferral. Composite maturity
rendering → RFC 0002's deferral (RFC7-16); Polaris renders no composite number
until it is discharged. Link-integrity verification cadence for the citation
graph → quality policy; the obligation and its trust-floor consequence bind
here. **That cadence reaches only anchors that exist and break** (RFC7-11) and,
with RFC7-10's target-state component, anchors whose targets moved
(RFC7-11(a)); it never reaches a load-bearing claim that **never carried an
anchor at all**, which is caught only at the authoring act — which is why
RFC7-2's check binds every path to curated narrative rather than the
draft-adoption path alone.

## 8. Owner questions — package index

Numbering is stable across the package and immutable; each open question's full
text lives in the module owning its clause, and answered items' reasoning is in
`../../history/RFC-0007-history.md` §8.

| # | Subject | State | Lives in |
|---|---|---|---|
| q1 | Materiality authority (RFC7-25) | **answered — owner decision B6** (asymmetric declaration) | history §8; ruling in `narrative-contract.md` RFC7-25 |
| q2 | Primary-narrative cardinality (RFC7-6) | **open** | `narrative-contract.md` §8 |
| q3 | The editorial-draft surface state (§5 defect 2) | **answered — owner decision B10** (minted as a third sibling state) | history §8; ruling in `narrative-contract.md` RFC7-20 |
| q4 | Rejected-draft retention (RFC7-22) | **open** | `narrative-contract.md` §8 |
| q5 | Presentation-profile scope (RFC7-5/RFC7-6) | **answered — owner decision A4** (required; Polaris drafts a default for owner sign-off) | history §8; ruling in `narrative-contract.md` RFC7-5 |
| q6 | The verbatim leaf under a proposed reading (RFC7-14) | **answered — owner decision B5** (adopted text operative, delta adjacent) | history §8; ruling in `narrative-contract.md` RFC7-14 |
| q7 | The V0 disclosure enumeration (RFC7-13/RFC7-17) | **answered — owner decision B7** (obligations binding, counts are V0 defaults) | history §8; rulings in `narrative-contract.md` RFC7-13 and RFC7-17 |

**Also open, and not a §8 question:** OQ-010 — where a genuine cross-project
*fact* or Project-relationship entity would live. RFC7-36 binds the portfolio
narrative's discipline and settles nothing about it.

---

## Phase boundary

The phase rule **RFC7-38** binds the whole package: this contract fixes the
semantics of the intent surface and is not a specification of record from
which implementation work may be scheduled. The clause text is in
`rendering-and-surface.md` §3.13, and its clause-to-requirement coverage
matrix must cover **RFC7-1…RFC7-37 across both modules**, not the rendering
module alone.

---

*End of RFC 0007 package index. Clauses RFC7-1 … RFC7-40, with lettered
sub-clauses RFC7-2(a)–(c), RFC7-9(a)–(c) and RFC7-11(a), distributed across two
modules. No retired numbers, no merged numbers, no gaps in the range, and no
clause identity in more than one module.*
