# Feature request M1 — Polaris page size: state page-invariant facts once

> **Candidate — binds nothing.** This is the feature-request funnel for the
> first move released from the 2026-09-13 vision pursuit. It proposes; the
> owner disposes (VIS-4). Nothing here authorizes implementation, and no bead
> becomes runnable by this file. Bead: `syzygy-dov.1`. Dossier:
> `docs/pursuits/2026-09-13-vision-pursuit.md`, section M1. The pending
> decision that carries the owner's three questions is P-67 in
> `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`.

Date: 2026-09-13. Author: the pursuit session (Claude), for the owner.

Size: **medium** for lane A (several renderer components, observable markup
changes, no spec text touched); **large** for lane B (it amends three signed
PWB requirements and therefore needs an independent spec review before any
owner act).

Baseline: Syzygy `5bb79cc` (main). The retained captures were taken at
`f4589e2`; `git diff --stat f4589e2..5bb79cc` over the four renderer files
named below is empty, so every measurement still describes the current code
[Observed]. Butlers: the rendered capture is from the 2026-09-10 evaluation
at Butlers revision 66ed58f; the 503 breach was captured at Butlers head
7c8743f63 (2026-09-12).

## The three questions for the owner

Batched, each with the recommended answer first. Everything else in this
file is the evidence behind them.

| # | Question | Recommended |
|---|---|---|
| Q1 | Authorize **lane A**, an implementation-only trim in the exact shape of the P-63 ruling: (a) stop embedding the narrative JSON in the human page, since the identical payload is already served at the authenticated presentation route; (b) render statement-less item classes as a compact list instead of a three-column claim table. Run under the existing bead `syzygy-dov.1`, so no new POC bead is filed and P-52 is not touched. | **Yes.** Expected saving about 760 KB on the 2,090,025-byte capture [Inferred from the measurements below]; the page returns to roughly 1.3 MB with about 790 KB of headroom. |
| Q2 | Have the **lane B** semantic delta drafted for a PWB behavior amendment act: let a page-invariant tuple field (evaluation identity), an identical tuple shared by every row of one table, and the two presentation flags be stated **once at an enclosing scope with a stated inheritance rule**, with the parity comparator expanding the scope back to one tuple per claim. | **Yes, after lane A is measured.** Lane B is the structural fix (it lowers the per-item slope by roughly a third), but it changes signed text, and lane A alone clears the ceiling. Draft it once the lane A measurement is retained, so the packet quotes real numbers. |
| Q3 | Accept that the M1 outcome is a **smaller slope and a removed constant, not a sublinear page**. Under PWB-REQ-011 (complete catalogs), PWB-REQ-020 (exact multiplicity) and PWB-REQ-021 (whole-project cold open on one page) every declared item renders once, so the served page is at least linear in the item count. True sublinearity means catalogs on their own routes, which is a different spec question. | **Accept.** Record the honest target: page bytes at Butlers head under 1.4 MB on both host forms, per-item marginal cost under 1,000 bytes after lane B. Re-open the route question only if Butlers growth threatens the ceiling again. |

## Gate 0 — Baseline

| Pillar | Present | Constrains this request |
|---|---|---|
| Doctrine (heart-and-soul) | Yes, adopted: VIS-1…7, SEC-1…5 | VIS-1 rank order and its "simplify presentation, never content" rule; VIS-2 |
| Decisions (legends-and-lore) | Yes | P-63 ruling and its constraints; PWB-STATE1 and 2026-09-05 amendment precedents; P-52 (POC item cap) |
| Specification (openspec) | Yes, signed: `openspec/changes/polaris-project-wide-butlers-model/` (digest-bound, uneditable) | PWB-REQ-007, 011, 014, 016, 020, 021 |
| Topology (lay-and-land) | Candidate bundle only | None beyond app-versus-core placement |
| Craft (craft-and-care) | Yes, owner-approved | CC-TEST-5/6 oracles, rule-6 mutation evidence, retained evidence, independent raw review |

## Gate 1 — Motif

**Problem.** At Butlers head 7c8743f63 the human page `/polaris` measures
2,132,656 encoded bytes against the declared ceiling of 2,097,152, so the
daemon answers HTTP 503 with a JSON body saying `served: nothing`; no ledger,
log line or status record sees it [Observed: capture `polaris.html`, 838
bytes, the 503 body; `apps/three-surface-poc/src/routes.ts` lines 99 to 151].
The owner's loopback daemon still serves a 2,090,025-byte page because its
evaluation predates the last Butlers commits. Last time this happened it was
caught 44 KB before the line and answered by the P-63 trim; the 479 KB that
trim bought has been consumed by Butlers growth and the merged repairs in
six days.

**Who.** The owner, whose RFC7-30 cold-open walkthrough (`syzygy-1z3.22`) is
gated on a page that serves; every agent that reads Polaris through the
human channel; the next Butlers contributor whose commit tips the page over.

**Success, falsifiable.**

1. `/polaris` at Butlers head serves on both host forms (direct and with the
   tailnet `Host` header) with at least 600 KB of headroom under the ceiling.
2. The per-item marginal cost, measured as the byte difference between two
   evaluations differing by one catalog item, is under 1,000 bytes after
   lane B (today about 2,600 bytes: one table row of 1,300 to 1,650 bytes
   plus one narrative block of about 745 bytes, both linear in items).
3. Every invariant the P-63 evidence file records is unchanged before and
   after: claim id set, the 19-member Unknown set, tuple multiset per claim,
   item and source populations, fragment targets with zero dangling, and the
   mount-prefixed link count.

**Motif.** *A fact that holds for the whole page, or for a whole table, is
stated once, at the scope it holds for, and every consumer can expand it
back.* This is the same motif VIS-1 uses for its own example ("Unknown ×40")
and that the page already applies one level up in `reasonCountsBlock`.

**The honest correction (Q3).** The dossier asked for a "sublinear" page.
The signed specification does not allow it: PWB-REQ-011 requires complete
catalogs, PWB-REQ-020 requires the human fact multiset to equal the machine
one with multiplicity, and PWB-REQ-021's cold open is one page. The
walkthrough preflight enforces this by counting every reconciled item
exactly once in the served HTML (`walkthrough-preflight.ts` line 151). So
the request is restated as: remove the one constant that is not a fact
(625 KB of duplicated JSON) and lower the per-item slope. Moving catalogs to
their own routes would be the sublinear answer and is out of scope here; it
needs its own funnel against PWB-REQ-011 and PWB-REQ-021.

## Measurements on the retained capture

All from `polaris-7478.html` (2,090,025 bytes, Butlers 66ed58f, Syzygy
`f4589e2`), computed by a Python sweep this session [Observed].

| Component | Count | Bytes | Share |
|---|---|---|---|
| Narrative JSON script (one element, before the first visible heading) | 1 | 625,340 | 29.9% |
| Claim-tuple spans | 699 | 409,829 | 19.6% |
| of which `data-evaluation-id` attributes, all one value | 699 | 49,629 | 2.4% |
| Presentation-flag pairs (`data-presentation-artifact`, `data-non-citable`) | 2,615 each | 115,060 | 5.5% |
| Item rows, all classes | 402 | 604,136 | 28.9% |

Per class, table bytes and bytes per row: catalog-entry 93,090 over 65 rows
(1,432); topology-component 116,843 over 152 (768); baseline-spec 305,132
over 185 (1,649); design-contract 40,487 over 32 (1,265); success-criterion
18,561 over 13 (1,427); principle 15,709 over 7 (2,244); craft-policy 10,175
over 7 (1,453); roster-identity 8,035 over 6 (1,339).

Two facts drive the design. The narrative script is byte-for-byte the
payload the daemon already serves at the authenticated presentation route
from the same render (`routes.ts` line 165 onward), and no client script
reads the in-page copy: its only consumers are four test files [Observed:
sweep of `apps/three-surface-poc/src` for the script id]. And 230 of the 295
catalog-side rows in four classes render a "declared" statement that is
byte-identical to the key in the first column, because those extractors
capture no statement (`project-shape-extraction.ts` lines 491 to 497).

## Gate 2 — Doctrine

**Aligned.** VIS-1: "Comprehension is achieved by simplifying
*presentation*, never *content*: an honest view may aggregate, defer, or
progressively disclose Unknowns, but may never substitute a confident state
for an Unknown one." Both lanes remove markup, never a claim, an Unknown, a
tuple field or a route. VIS-2: a page that cannot be served renders no
truth; today the breach renders nothing and reports nothing.

**Conflict check.** VIS-1 rank 1 (truth and observation determinism) is not
spent: the fact model, the machine answer and the narrative payload are
untouched. RFC7-16's "one epistemic state per major claim, with its
evaluation identity" is satisfied by inheritance under lane B; RFC6-22
defines equivalence "over semantics and query results, never over pixels",
which is exactly the reading lane B asks the comparator to take.

## Gate 3 — Topology

Lives in `apps/three-surface-poc/src/` only: the renderer (`polaris.ts`,
functions `claimTuple`, `itemRow`, `classBlock`), the narrative module
(`polaris-narrative.ts`, `narrativeScript` and `parseNarrativeScript`), and
the sweeps and tests that read the human page (`polaris-parity-sweep.test.ts`,
`walkthrough-preflight.ts`, `polaris-epistemic-tuples.test.ts`, the four
narrative-reading tests). The core package, the observation pipeline, the
registry ceiling and `routes.ts` are not touched. Lane A changes no
contract. Lane B changes the human-channel convention that PWB-REQ-007,
PWB-REQ-014 and PWB-REQ-020 describe, and nothing in the machine channel.

## Gate 4 — Design sketch

### Lane A (implementation-only; the P-63 shape)

1. **Narrative JSON off the page.** `narrativeScript` is no longer embedded
   in the human page. The payload stays in the render result and at the
   authenticated presentation route, unchanged. The four tests that call
   `parseNarrativeScript` on page HTML read the route body instead. The
   no-JS path is unaffected because nothing on the page reads the script.
   Saving: 625,340 bytes on the capture, and every future narrative block
   (about 745 bytes per item) leaves the page's slope.
2. **Compact list for statement-less classes.** When no item of a class
   carries a statement, `classBlock` renders a `<ul>` region instead of the
   three-column table: one `<li data-polaris-item="…">` per item holding the
   key, the support citation, the exact-text link where one exists, and the
   unchanged `claimTuple` span. The region keeps its role on the region div
   (never hoisted onto the list, per the guardrail on where a trimmed byte
   may not come from). The parity sweep's `classes-with-item-tables` family
   learns the list form as a second admitted container so a class cannot
   silently drop to zero rows. Saving: about 130 to 150 KB on the capture
   [Inferred: 185 baseline-spec rows at about 750 bytes saved each]; more
   as the class grows.

Trade-offs rejected: raising the ceiling (P-63 arm B, a registry act that
buys time and no structure); shortening the 40-character revision and the
source prefix inside anchors (PWB-REQ-014 makes them durable identity);
moving the baseline-spec section to its own route (allowed by the P-63
constraints for that one class, but it removes a reading level rather than
markup, and lane A does not need it).

### Lane B (spec amendment; the 2026-09-05 shape)

An **enclosing scope** is any element carrying `data-claim-scope`. Three
things may be stated on a scope instead of on each leaf beneath it:

- `data-evaluation-id`, when every claim under the scope shares it;
- the full epistemic tuple (`data-epistemic-label`, tier, primary and
  secondary reasons, freshness, challenge state), when every row of one
  item table shares it, rendered once beside the table caption as
  "N of N items: Observed · report-fact · fresh · unchallenged", with the
  per-row span kept only for rows whose tuple differs;
- `data-presentation-artifact` and `data-non-citable`, on the section that
  contains only presentation units.

The **inheritance rule**, stated once in the page's claim-states lede and in
the machine form: a leaf marker's value for a field is the nearest ancestor
scope's value when the leaf does not carry the field itself. The parity
comparator (`leafMarkers` in the sweep) expands scopes before comparing, so
the human multiset it reports still has one tuple per claim and PWB-REQ-020's
"collapsed" falsifier still fires when a scope hides a differing row. A
build-time assertion fails the render if one page carries two distinct
evaluation ids, so the hoist cannot go stale silently.

Saving on the capture: about 49.6 KB (evaluation id), about 300 KB (tuples
of the rows whose tuple equals the table's), about 100 KB (flags); together
roughly 450 KB and about a third of the per-item slope.

Trade-offs rejected: an inheritance rule known only to the renderer (the
comparator must import no rendering code, PWB-REQ-020); dropping fields the
reader "does not need" (PWB-REQ-007's complete tuple).

### Design bar for the human surface

No new interaction is introduced. The contract inputs carried into
acceptance are the existing ones: PWB-REQ-016 (comprehension without vision
or a pointing device), every fragment target reachable and outside
`<details>`, keyboard paths complete, direct and tailnet parity, the no-JS
path complete, and the glossary still describing every tuple span
(`walkthrough-preflight.ts` line 222).

## Gate 5 — Specification

**Lane A: no spec delta.** Every observable obligation stays satisfied by
the same markup semantics: each item still renders once with its complete
tuple, its citation and its exact-text route; the narrative payload is
still served, marked non-citable, from the same evaluation. The change is
where bytes are, not what is stated. This is the same judgment the P-63
ruling made ("implementation-only trim").

**Lane B: semantic delta, drafted below in the project's own form** (the
`SEMANTIC-DELTA-TEMPLATE.md` fields), because the PWB specification is
digest-bound and its two prior amendments travelled as a
`contracts/candidates/` package plus an owner act, not as edits to the
change directory. This draft is the proposal text for that package; it is
not the package and it binds nothing.

### Draft semantic delta — scoped epistemic attributes on the human channel

**Artifacts:** the signed PWB behavior package (successor of
`contracts/candidates/pwb-truth-policy-amendment/`), restating
`openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md`.
**Stable IDs affected:** PWB-REQ-007, PWB-REQ-014, PWB-REQ-020. None
minted, retired or renumbered.
**Change class:** Normative (it admits a human-channel encoding the current
text forbids by its literal wording).
**Author / date:** pursuit session, 2026-09-13 (draft only).

**Current meaning, quoted.**

- PWB-REQ-007: "Every project entity and project-fact claim SHALL have a
  stable semantic Claim identity plus an evaluation instance, be
  challengeable with resolvable support, and carry the closed label, tier,
  exactly one primary reason, zero or more closed secondary reasons,
  freshness, challenge state and evaluation identity that govern it."
  Observable: "human and machine views expose identical complete tuples".
- PWB-REQ-014: "Every owner-visible narrative unit SHALL carry
  `presentation-artifact` and `non-citable` attributes and exactly one claim
  role".
- PWB-REQ-020: "…SHALL be recoverable from the same evaluation in the
  machine answer, preserving multiplicity and exact provenance state."
  Falsifier: "one fact … is missing, duplicated, changed, collapsed or
  associated with a different evaluation in either channel."

**Proposed meaning.** Add one sentence to each:

- PWB-REQ-007: "A tuple field whose value is identical for every claim
  under one enclosing scope MAY be carried once on that scope; the claim
  still carries it by the stated inheritance rule, and a claim whose value
  differs from its scope SHALL carry the field itself."
- PWB-REQ-014: "The two attributes MAY be carried by an enclosing scope
  that contains only presentation units; a unit under such a scope carries
  them by the stated inheritance rule."
- PWB-REQ-020: "Recoverability is judged after scope expansion under the
  stated inheritance rule; the comparator SHALL expand scopes itself and
  SHALL still fail when a scope's value hides a differing member."

**What explicitly does not change.** The machine answer and the narrative
machine form (they never carried scopes). The vocabulary of every field.
The one-tuple-per-claim multiset the comparator reports. The requirement
that Unknown never folds into a total (a scope with any differing member
renders that member's own tuple). RFC7-16's per-claim evaluation identity
(it is inherited, not dropped). PWB-REQ-011, 016 and 021.

**Warrant.** VIS-1's own example of honest simplification; RFC6-22's
equivalence "over semantics and query results, never over pixels"; the
P0-CEILING breach at Butlers head, which VIS-2 turns into a page that
renders no truth.

**Downstream impact** (sweep to be run when the package is drafted, not
asserted here): the parity sweep, the walkthrough preflight, the epistemic
tuples test, the mutation sweep's tuple mutants, the P-63 evidence file's
`claimTuples` invariant, and the PWB implementation plan's PWB-REQ-020
section.

**Review required.** Fresh-context spec review (large size), then the
owner act in the 2026-09-05 shape.

## Gate 6 — Engineering bar

Acceptance for lane A, reusing the P-63 bead's criteria:

1. Retained before-and-after measurement, direct and tailnet host forms, at
   a named Syzygy commit and Butlers revision, in `docs/evidence/`, from a
   private daemon on port 0 with its own state directory, never the loopback
   daemon on 7478, on a committed clean tree.
2. Every P-63 invariant equal before and after (listed under success
   criterion 3), computed by the same script, not transcribed.
3. Preflight populations, PWB-REQ-020 parity with both denominators,
   keyboard, no-JS and browser tests, the app suite twice and the full
   suite pass; typecheck clean after `tsc -b` on the core package.
4. Rule-6 mutation evidence for the two new guard branches: the list-form
   container in `classes-with-item-tables`, and the route-read narrative
   tests (mutate the route body and confirm each test fails).
5. Independent review in the improvement-cycle shape, raw retained as
   `…-RAW.md`, before close. The 2026-09-07 trim record stays as history.

Lane B adds: the comparator's scope expansion gets its own mutants (a scope
value that hides a differing member must fail), the build-time
two-evaluation-ids assertion gets one, and the human-channel inheritance
rule is written in the claim-states lede and the machine form before any
attribute moves.

## Funnel summary

```
## Feature Request: M1 — Polaris page size: state page-invariant facts once
Size: medium (lane A) / large (lane B)
Baseline: Syzygy 5bb79cc; captures f4589e2 (renderer unchanged); Butlers 66ed58f rendered, 7c8743f63 breach
- G1 Motif: 503 at the ceiling serving nothing → state whole-page and whole-table facts once [Observed: capture, routes.ts]
- G2 Doctrine: aligned — VIS-1 "simplify presentation, never content"; VIS-2
- G3 Topology: apps/three-surface-poc renderer, narrative module, sweeps; no core, route or registry change; lane B changes the human-channel convention of PWB-REQ-007/014/020
- G4 Design: lane A (narrative off page, compact list); lane B (scoped attributes + comparator expansion); route-per-catalog rejected as out of scope
- G5 Spec: lane A none; lane B draft semantic delta above (3 MODIFIED, 0 ADDED); out of scope: catalog routes, ceiling raise, anchor identity shortening
- G6 Bar: P-63 acceptance criteria 1–5 reused; rule-6 mutants for each new guard branch
Open questions: Q1, Q2, Q3 above (P-67)
Sign-off: pending — the owner's, by ruling P-67
Recommended handoff: Q1 yes → execute lane A under syzygy-dov.1 in the P-63 shape; Q2 → draft the lane B package after the lane A measurement; Q3 → record the restated target in the bead
```
