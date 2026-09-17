# Feature request M14 — Provenance depth: a digest a reader can reach, a citation that lands on its one requirement, and a catalog item that is more than a marker

> **Candidate — binds nothing.** Bead `syzygy-dov.14`, move M14 of the
> 2026-09-13 vision pursuit (`docs/pursuits/2026-09-13-vision-pursuit.md`,
> section "### M14"), written in the shape of
> `docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md` and its siblings, and
> structurally beside the M13 navigation-scale funnel packet on its branch.
> Planning only: nothing here authorizes implementation. This packet names
> lawful arms for the owner to take; it rules no slice authorized or
> unauthorized, and the owner disposes.
>
> **Review 1 landed 2026-09-17 — CONFIRM WITH EXCEPTIONS (0 blocking, 1
> non-blocking F1, 1 editorial F2), both applied.** [superseded 2026-09-17
> after review 1: "First draft — NO independent review yet. Where the M13
> packet records two fresh-context reviews, this packet records none."] By
> verification rule 10 review 1 binds the reviewed `7d764fc` bytes; the F1
> and F2 repairs and this re-tensing post-date them, so they are themselves
> uncovered until a second independent review confirms them. The load-bearing
> headline was also reproduced this session by two independent methods
> (verification rule 2). See "## Review 1 and repairs (2026-09-17)" below.

Date: 2026-09-17. Author: a funnel session (Claude), for the owner.

Size: **small** (slices 3 and 4) / **medium** (slices 1 and 2) / **large**
(slice 5, and only its amendment-drafting question is asked here).

Baseline: Syzygy `a9f671e` (main). The subject is the rendered Polaris human
page, the renderer that emits it, and the two render-time seams beside the
shape.

**Line-count convention, stated once.** A "line N" below is the one-based
index into the split-on-newline segments of the file at `a9f671e` — the
number `sed -n 'Np'` prints. A byte count is the UTF-8 length.

**Capture convention, stated once.** Two captures are read. The **post-trim**
capture is the retained lane A "after" capture, `polaris-direct.html`
(1,478,637 bytes) and `polaris-tailnet.html`
(1,484,487 bytes), served at Syzygy `2ef68f5` against Butlers revision
`2e3bac97790b4bd8906dcac63eadb5642a0bb1ac` and recorded in
`docs/evidence/pwb-m1-polaris-lane-a-measurement-2026-09-13.json`; its
machine sibling is `api-poc.json` (5,520,314 bytes). The **pre-trim** capture
is the earlier `polaris-7478.html` the dossier audited (2,090,025 UTF-8 bytes
as it sits on disk). Every figure below names which capture it is measured on
and gives that capture's byte count as its denominator. No daemon was started
this session and the loopback daemon on port 7478 was never contacted.

## The five questions for the owner

Batched, recommended answer first. Everything below is the evidence behind
them. Q1 is the packet's central question: it is the one slice that changes
what the page *serves* rather than how it is labelled, and it is the reason
the move exists — a digest with no route to its bytes is not provenance
(VIS-3, VIS-7).

| # | Question | Recommended |
|---|---|---|
| Q1 | **[S5-M2] May the exact-source route be extended to the body-classified non-baseline sources — dropping the class gate for the 77 that carry a classified blob, and keeping the 9 withheld sources digest-only?** Measured this session on the post-trim capture: **86** of **278** source rows (**31%**) render a content digest with no exact-source route, because `apps/three-surface-poc/src/verbatim-route.ts` lines 78–79 refuse the route to every source whose rule is not `baseline-spec-tree` (refusal `unconsented-source-or-provider`, "the exact-requirement route applies to baseline specs only"). Of the 86, the machine answer `projectShape.sources` in `api-poc.json` classifies **77** as a blob anchor the pipeline read and admitted — pillar-index 5, pillar-named-file 53, root-index 1, roster-tree 18 — and **9** as excluded, kept digest-only by the route's own fail-closed refusal at line 87 (`excluded-content`) — pillar-named-file 1, roster-tree 8, of which 8 are `unclassifiable-excluded` (frontend.md and seven butler.toml, the active-content / "TOML has no inert context" files) and 1 is an `excluded-artifact` (roster/qa/MANIFESTO.md, a markdown manifesto), all outcome=excluded [superseded 2026-09-17 after review 1 F1: "withheld active content"]. There are no tree or missing-at-revision anchors in this capture. A caveat the slice cannot skip: the route's leaf renderer runs `selectRequirementSections` (`apps/three-surface-poc/src/capability-detail.ts` lines 256–260) and refuses a body with no requirement heading, so dropping the gate alone would refuse the 77 with `reference-unresolvable`; S5-M2 also needs a whole-body render mode for the non-baseline classes, which is new content-presentation behavior the signed change does not describe. | **Yes for the 77, never for the 9 — and add the body render mode, do not merely delete the gate.** The 9 withheld sources are the AGENTS.md known gap — seven butler.toml with no inert context, one named markdown file (frontend.md, also `unclassifiable-excluded`), and one `excluded-artifact` markdown manifesto (roster/qa/MANIFESTO.md) [superseded 2026-09-17 after review 1 F1: "roster identity files and one named file have no inert context"] — and the route's excluded-content refusal is the fail-closed polarity doctrine wants; it must stay. **Every lawful arm:** (a) *no change* — the 86 keep a routeless digest; (b) *the recommended arm* — drop the class gate for the 77 body-classified sources and add a whole-body render mode, the 9 withheld staying digest-only by the existing refusal; (c) *route-metadata only* — for the 77, render the anchor's revision-bound identity and classification reason as reachable text without serving the body, half the value, no new render mode. **Counter-argument, and it is the strong one:** arm (b) adds a rendering mode the specification never contemplated, so Q5's escalation reading (Gate 3) reaches it too — an owner who reads "any scope beyond the signed change" strictly will want arm (b) ruled, not inherited. **Default if unanswered: the gate stays, the 86 keep a routeless digest, no route work ships.** |
| Q2 | **[S5-M3] May the exact-source route take a requirement selector parameter and a scroll anchor, so a citation lands on the one requirement it names rather than the whole spec?** Today the route serves every requirement section of the baseline spec, joined (`selectRequirementSections`, `apps/three-surface-poc/src/capability-detail.ts` lines 256–260). A citation names one requirement; the reader is dropped at the top of all of them. The route's identity is carried entirely by the href — `sourceRouteHref(mountPrefix, identity)` at `apps/three-surface-poc/src/polaris-source.ts` lines 41–43 appends `?identity=`, and `sourceRouteIdentities(html)` at lines 49–58 reads it back, "the one carrier of the identity; no attribute restates it." | **Yes, add a scroll anchor, and keep the whole spec served — arm (a).** A scroll anchor lands the reader on the named requirement without narrowing what the route returns, so PWB-REQ-011's coarser-account invariant is untouched. **Second lawful arm:** (b) a selector that serves only the named requirement — smaller payload, but it removes a stopping point the depth invariant arguably counts, and it multiplies the route identities PWB-REQ-011's depth sweep must enumerate. **Counter-argument:** the same 192 baseline identities already render twice (catalog group and evidence group), so a per-tuple PWB-REQ-020 parity check, not a per-id one, must cover the new parameter, or a divergence hides behind an unchanged id. **Default if unanswered: no selector and no anchor; the route serves the whole spec as today.** |
| Q3 | **[S5-M4] May one legend sentence be added beside the sources table, decoding the source-identity grammar a reader now has to infer?** The 278 source rows render a rule token, an anchor kind, a classification outcome and — for the 86 non-baseline rows — a truncated content digest, with no key on the page saying what those fields mean. | **Yes — one copy-table sentence, `POLARIS_COPY` being implementation, not a governed artifact.** It is the cheapest slice in the move and it removes an inference the reader should not have to make. **Counter-argument:** any legend is prose that can drift from the grammar it describes; the sentence must be derived from the same rule set the manifest declares (`SOURCE_RULES` at `packages/three-surface-poc-core/src/project-shape-manifest.ts` line 71), not hand-written beside it. **Second lawful arm:** render the legend from the rule set programmatically rather than as a copy string, so it cannot drift. **Default if unanswered: no legend ships.** |
| Q4 | **[S4-M4] May a reconciliation line be rendered beside the catalog, relating the sources, the extraction classes and the items — derived from the machine answer?** The machine answer `projectShape.items` carries **415** items across **9** classes; the page renders **417** bare `data-polaris-item` markers; the catalog's eight classes sum to **409** (the M13 figure, which is 415 minus the 6 project-account-section items that render in the account section, not the catalog). A reader is given none of these three numbers, nor the 278-sources-to-415-items derivation, nor their relationship. | **Yes — one line, derived from `projectShape`, labelled `[Observed]` for the machine figures and `[Inferred]` for any sum.** It renders the reconciliation the page currently withholds. **Counter-argument:** the 417-versus-415 delta is `[Unknown]` from the HTML alone — the render predicate (per-class bounding versus bare occurrence) changes the number — so the line must state its predicate, or it manufactures a false exactness. **Second lawful arm:** render only the authoritative `projectShape.items` total and per-class counts, and omit the bare-marker count until its predicate is settled. **Default if unanswered: no reconciliation line ships.** |
| Q5 | **[S4-M3] May a CC-REV-2 semantic delta to PWB-REQ-015's band semantics be *drafted* — not implemented — so catalog items can route into per-item depth pages instead of the single hard-coded capability deep dive?** Today `deriveCapabilityDeepDives` (`apps/three-surface-poc/src/capability-detail.ts` lines 96–119) returns one deep dive per `capability` entity, and the model carries exactly **1** capability entity, so there is one hard-coded capability depth page. PWB-REQ-015 (`openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md` line 816) fixes that page's authority-band semantics; generalizing depth pages to non-capability catalog items needs those band semantics amended. | **Authorize the *drafting* only — a CC-REV-2 semantic delta binds nothing (VIS-4), and implementation waits on the signed amendment and a fresh implementation authorization.** Drafting lets the owner see the exact band-semantics change before deciding anything. **This is the one slice that trips an escalation trigger:** the continuation act (Gate 3) stops work for "a further amendment to the signed PWB specification beyond the 2026-09-05 package," so even the recommended arm is drafting, never building. **Second lawful arm:** rule that the single capability deep dive is sufficient for the bounded POC and record per-item depth as an accepted, permanent gap. **Default if unanswered: no amendment is drafted; the single capability depth page stands.** |

### Decided in this packet, not put to the owner

**The dossier's headline is re-derived on the retained capture and both
figures are published.** The dossier states 86 of 271 (32%) over its pre-trim
capture. Re-derived this session: **86 of 278 (31%)** on the retained
post-trim capture, and **86 of 271 (32%)** reproduced exactly on the pre-trim
capture. The figure that moved is the denominator (271 → 278, +7) and the
route-reachable baseline-spec count (185 → 192, +7); the 86 digest-only rows
are **unchanged** in count and composition on both captures. The predicate is
stated at each figure and the denominator is the capture's own source-row
count. Neither number is green and neither is the whole story: 31% of the
page's sources still carry a digest a reader cannot verify against anything,
which is the move's motive.

**The 86 is two populations, not one, and only 77 are the slice's subject.**
The dossier reads the 86 as a single "digest-only" class to be routed. Split
this session against the machine answer: **77** carry a classified blob and
are route-able once a body render mode exists; **9** are excluded — eight
active-content sources (seven butler.toml and frontend.md) plus one
excluded-artifact markdown manifesto (roster/qa/MANIFESTO.md) [superseded
2026-09-17 after review 1 F1: "9 are withheld active content"] — the route
must keep digest-only, and its fail-closed refusal already does. Collapsing
the two would propose serving withheld content, which the recommendation
explicitly does not.

**The item reconciliation is genuinely unstated, and stating it honestly is
the slice — not resolving every off-by-two.** The authoritative figure is
`projectShape.items` = **415** across nine classes. The page's **417** bare
markers and the catalog's **409** eight-class sum are true of different
predicates, and the 417-versus-415 delta of two is `[Unknown]` from the HTML
alone. S4-M4 renders the relationship the reader is missing; it does not claim
a single number where the predicates disagree.

**S5-M4's legend is ordinary implementation and is stated here as a decision,
not asked — except for its drift risk, which is Q3's second arm.** A copy
sentence beside a table is engineering inside the existing act. The only thing
worth an owner's eye is whether it is a hand-written string (which can drift)
or derived from the rule set (which cannot), and that is the arm Q3 offers.

## Gate 0 — Baseline

| Pillar | Present | Constrains this request |
|---|---|---|
| Doctrine | `.syzygy/governance/doctrine/vision.md`, `security.md` | VIS-2 (no-evidence → Unknown), VIS-3 and VIS-7 (a claim reaches its evidence); no SEC rule is newly engaged — the 9 withheld sources stay withheld, so no new read and no egress |
| Decisions | `PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md` (2026-09-02), `PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md` (2026-09-05), `THREE-SURFACE-POC-SPEC-SIGNOFF-ACT.md`, `PWB-TRUTH-READINESS-AMENDMENT-ACT.md` (2026-09-05) | the first two are the implementation grant and its continuation, quoted in Q5 and Gate 3; the fourth binds the eleven PWB artifacts, one of which is PWB-REQ-015's home |
| Specification | `openspec/changes/three-surface-poc-experience/…/spec.md` and `openspec/changes/polaris-project-wide-butlers-model/…/spec.md` | PWB-REQ-011 (exact-source route and its depth invariant), PWB-REQ-015 (capability-detail band semantics, the Q5 subject), PWB-REQ-020 (per-tuple parity), PWB-REQ-001/003/007 (the source record's content); POC-REQ-021/022/030/061 |
| Amendment overlay | **None as a separate directory.** The PWB 2026-09-05 amendment was performed **in place**; every PWB citation below is to the current, amended bytes, and each is a bound byte no slice may edit | Q5 is the one slice that would amend a bound byte, which is why it asks for drafting authorization, not implementation |
| Contracts | RFC-0002 (RFC2-26 phase rule), RFC-0007 (RFC7-34 non-visual recoverability), RFC-0009 (RFC9-13 personal presentation state) | RFC2-26 run in Gate 5; RFC7-34's recoverability limb, which Q1's route serves; RFC9-13, not engaged because no slice adds stored presentation state |
| Policies | `policy-candidates/` (CC-SPEC, CC-IMPACT, in force despite the directory name); CC-REV-2 | CC-REV-2 is the amendment path Q5 asks to *draft* down |

**Two bound-byte constraints this packet obeys.** (a) PWB-REQ-015's home is a
row of the 2026-09-05 manifest, so **no slice edits it**; Q5 asks only to
draft a CC-REV-2 delta against it, which the owner then disposes. (b) The 9
withheld sources stay withheld: no slice proposes reading a content class the
PWB-REQ-005 evaluation excludes, and Q1's recommendation keeps the route's
excluded-content refusal exactly as it is.

## Gate 1 — Motif

The move is one sentence of doctrine made mechanical: **a digest a reader
cannot reach is not provenance.** The page today renders, for 86 of its 278
sources, a truncated content digest in a `data-parity-field` code element and
nothing a reader can open to check that digest against a body. For the 192
baseline sources it renders the opposite — a no-body epistemic disclosure plus
an exact-source route. The five
slices close the gap from both ends: Q1 gives the 77 body-classified sources
the route the 192 already have; Q2 makes that route land where the citation
points; Q3 tells the reader what the identity fields mean; Q4 reconciles the
counts the reader is asked to trust; Q5 asks whether a catalog item may be as
deep as the one capability already is.

The motif is VIS-3 and VIS-7, not a new idea: every claim reaches its
evidence, and the reader is never asked to trust a figure they cannot check.
The 9 withheld sources are the motif's honest boundary — provenance depth
stops where consent does, and the fail-closed refusal is where it stops.

## Measurements

Each figure names its capture and its denominator. Method is Python `re`
throughout (verification rule 1); the headline is confirmed by a second method
(verification rule 2).

### 1. The routeless-digest headline, both captures

Post-trim (`polaris-direct.html`, 1,478,637 bytes): **278** source rows
(`<tr id="polaris-source-…">`), **278** rule tokens (`<b>Rule:</b>`). Per
rule: root-index 1, pillar-index 5, pillar-named-file 54, baseline-spec-tree
192, roster-tree 26. Non-baseline (digest-only) = 1 + 5 + 54 + 26 = **86**;
86 / 278 = 30.9%, published as **31%**. Route links (`/polaris/source?`):
**386** hrefs over **192** distinct identities (each baseline identity renders
twice), **0** of them non-baseline.

Pre-trim (`polaris-7478.html`, 2,090,025 bytes): **271** source rows; per
rule root-index 1, pillar-index 5, pillar-named-file 54, baseline-spec-tree
185, roster-tree 26; non-baseline = **86**; 86 / 271 = 31.7%, the dossier's
**32%**.

Figure that moved: denominator 271 → 278 (+7), baseline-spec-tree 185 → 192
(+7 now route-reachable), the 86 unchanged. **Second method:** a `Counter`
over the per-rule literal tokens sums to the same per-rule tally and the same
86 on each capture, and the machine `projectShape.sources` anchor/outcome
walk yields the same 86 (77 + 9) — verification rule 2.

### 2. The 86 split into route-able and withheld

From `projectShape.sources` (278 entries), tallied by (anchor.kind,
record.outcome): baseline-spec-tree is 192 blob+classified, all already
routed. The 86 non-baseline are **77** blob+classified (pillar-index 5,
pillar-named-file 53, root-index 1, roster-tree 18) and **9** blob+excluded
(pillar-named-file 1, roster-tree 8). No tree or missing-at-revision anchors
appear in this capture. The 9 excluded are eight active-content sources
(seven butler.toml and frontend.md, `unclassifiable-excluded`) plus one
`excluded-artifact` markdown manifesto (roster/qa/MANIFESTO.md) [superseded
2026-09-17 after review 1 F1: "withheld active content"]; the route already
refuses them at `apps/three-surface-poc/src/verbatim-route.ts` line 87 with
`excluded-content`, fail-closed.

### 3. The item reconciliation

`projectShape.items` length **415**, per class: baseline-spec 192,
topology-component 87, catalog-entry 65, design-contract 32, success-criterion
13, principle 7, craft-policy 7, roster-identity 6, project-account-section 6
(nine classes, sum 415). The page renders **417** bare `data-polaris-item`
occurrences. The catalog's eight classes sum to **409** — 415 minus the 6
project-account-section items, which render in the account section, not the
catalog (this is the M13 figure, reproduced). The 417 − 415 delta of **2** is
`[Unknown]` from the HTML alone; the render predicate changes it, which is
what S4-M4 exists to render honestly.

### 4. The single capability deep dive

`deriveCapabilityDeepDives(model)`
(`apps/three-surface-poc/src/capability-detail.ts` lines 96–119) filters
`entity.kind === 'capability'` and returns one dive each. The model carries
**9** entities, one of each kind, so exactly **1** is
a capability and there is **1** hard-coded capability depth page. S4-M3 would
route the 65 catalog-entry items (or a chosen class) into per-item depth
pages, which is the band-semantics generalization Q5 asks to draft.

## Gate 2 — Doctrine

- **VIS-2 (no-evidence → Unknown, never zero, never green).** Q4's
  reconciliation line labels the machine figures `[Observed]`, any sum
  `[Inferred]`, and the 417-versus-415 delta `[Unknown]`. The headline
  publishes 31% and 32% as `[Observed]` on their named captures, never a
  single smoothed figure.
- **VIS-3 / VIS-7 (a claim reaches its evidence).** Q1 is this doctrine made
  mechanical for the 77; the 9 withheld sources are its honest boundary and
  render Unknown-with-reason, not a false route.
- **RFC7-34 (non-visual recoverability).** The exact-source route is the
  non-visual recovery path for a source's bytes; extending it to the 77
  widens what a screen-reader user can recover, and the scroll anchor of Q2's
  recommended arm must be an `id` the reader can reach, never a target buried
  inside a closed `<details>` (the AGENTS.md fragment-target lesson).
- **RFC9-13 (personal presentation state).** Not engaged: no slice stores or
  restores any camera, filter or selection. Q4's line is derived per render
  and caches nothing, like the route beside it.
- **Fail-closed polarity.** The 9 withheld sources: withholding defeats the
  route, and the refusal is the correct default. No slice relaxes it.

## Gate 3 — Topology and the acts

The authorizing acts are the implementation grant
(`PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md`, 2026-09-02, point 1) and its
continuation (`PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md`,
2026-09-05, point 3). The continuation's escalation-trigger paragraph is the
sentence each slice is tested against — it stops work before, among other
triggers, "a further amendment to the signed PWB specification beyond the
2026-09-05 package" and "any scope beyond the signed change." Each slice
against that sentence:

| Slice | Trigger test | Reading |
|---|---|---|
| Q1 / S5-M2 | a new content-presentation mode (serving non-baseline bodies) the exact-source scenario does not describe | reaches "any scope beyond the signed change"; put to the owner in Q1, and its band-adjacent cousin in Q5 |
| Q2 / S5-M3 | scroll anchor (arm a) serves the same bytes; selector (arm b) narrows the response and touches PWB-REQ-011 route shape | arm (a) trips nothing; arm (b) is a route-shape change the owner should rule |
| Q3 / S5-M4 | a copy-table legend sentence | implementation inside the act; no trigger |
| Q4 / S4-M4 | a derived reconciliation line the parity sweep must cover | implementation inside the act; no trigger |
| Q5 / S4-M3 | amends PWB-REQ-015's band semantics | **trips "a further amendment to the signed PWB specification"** — Q5 authorizes drafting only, which binds nothing (VIS-4) |

There is no PWB overlay change directory; the 2026-09-05 amendment replaced
the spec bytes in place and they are bound. That is why Q5's lawful path is a
CC-REV-2 semantic delta the owner disposes, never an in-place edit.

## Gate 4 — Design sketch, per slice

**Slice 1 (S5-M2).** Two changes, both in the app seam, none in the bound
spec. (a) Replace the unconditional class gate at
`apps/three-surface-poc/src/verbatim-route.ts` lines 78–79 with a branch that
admits a source whose anchor is a classified blob and whose rule is any of the
five, while the line-87 `excluded-content` refusal stays untouched for the 9.
(b) Add a whole-body render mode to the leaf renderer so a non-baseline body,
which carries no requirement heading, renders in full instead of failing
`selectRequirementSections` with `reference-unresolvable`
(`apps/three-surface-poc/src/capability-detail.ts` lines 256–260). The route
still runs the secret detectors and active-content scan on the transient body
(Phase B), so a body that classifies as active is refused at render,
fail-closed.

**Slice 2 (S5-M3).** Add a scroll anchor (arm a) to the leaf renderer so each
requirement section carries an `id` the citation's identity can target, the
route still serving every section. The href stays the single carrier of the
source identity (`sourceRouteHref` / `sourceRouteIdentities`,
`apps/three-surface-poc/src/polaris-source.ts` lines 41–58); the anchor is a
fragment on top of the unchanged identity, so PWB-REQ-020 parity — checked per
tuple, not per id — still reads the same identity back. Arm (b), a selector
that narrows the response, is the route-shape change Q2 flags.

**Slice 3 (S5-M4).** One sentence beside the sources table decoding the
identity grammar: rule (one of the five `SOURCE_RULES`), anchor kind, outcome,
and the digest field. Recommended derived from the rule set at
`packages/three-surface-poc-core/src/project-shape-manifest.ts` line 71 so it
cannot drift; the copy-string arm is the cheaper, driftable alternative.

**Slice 4 (S4-M4).** One reconciliation line beside the catalog, derived from
`projectShape`: the sources count (278), the item total (415), the nine class
counts, and — if published — the bare-marker count (417) with its predicate
stated and the delta labelled `[Unknown]`. No new model field; the line reads
the existing `projectShape.items`.

**Slice 5 (S4-M3).** Not designed here — only its question is asked. The
drafting Q5 authorizes would produce a CC-REV-2 semantic delta to PWB-REQ-015
(`…/spec.md` line 816) generalizing the deep-dive band semantics
(argument / contract / reality bands) from the one capability entity to
per-item catalog depth pages, plus the blast-radius statement CC-IMPACT
requires and a fresh-context review. The delta binds nothing; implementation
waits on the owner's sign-off and a fresh implementation authorization.

## Gate 5 — Specification and the RFC2-26 test

RFC2-26 bars scheduling implementation work for user-observable consequences
**of RFC-0002** from that RFC alone. Each slice is scheduled from an approved
OpenSpec requirement with a scenario, not from RFC-0002:

- Slice 1 from PWB-REQ-011 (the exact-source route) and PWB-REQ-007 (complete
  epistemic state) — extending the route to more sources serves both.
- Slice 2 from PWB-REQ-011 (the depth invariant the scroll arm preserves).
- Slice 3 from PWB-REQ-012's owner-visible-string roles (the legend is a
  `scope-instruction`-class string) — an engineering decision inside the act.
- Slice 4 from PWB-REQ-007 and PWB-REQ-016 (the honest count and its render).
- Slice 5 from PWB-REQ-015 itself, which is why it is an amendment and not an
  implementation — the requirement's own band semantics are the subject.

Each slice's oracle is a hand-typed sweep or a per-tuple parity check, not a
generator that quotes prose (the rule-1-and-8 discipline). The load-bearing
one is slice 1's: the route's output for each of the 77 must be checked
against the transient body it served, and the 9 must still refuse, mutation-
tested per predicate (verification rule 6) before the slice is called green.

## Collision and sequencing

| Slice | Touches | Collides with |
|---|---|---|
| 1 S5-M2 | `verbatim-route.ts`, `capability-detail.ts` leaf | 2 (same leaf renderer) |
| 2 S5-M3 | `capability-detail.ts` leaf, anchor ids | 1 (same leaf renderer) |
| 3 S5-M4 | `polaris-copy.ts` or a derived legend | none |
| 4 S4-M4 | catalog render, reads `projectShape.items` | none |
| 5 S4-M3 | PWB-REQ-015 (drafting only) | none until built; then 1 and 2's leaf |

Slices 1 and 2 both change the leaf renderer and should land together or in
order (1 then 2), so the whole-body mode and the scroll anchor are designed
against one leaf, not two. Slices 3 and 4 are independent and may land any
time under the acts in force. Slice 5 is drafting only; nothing it produces
is scheduled until the owner signs the amendment and authorizes implementation
afresh.

## Gate 6 — Engineering bar and the first-draft posture

- **Self-referential figures, computed at a fixed point.** This file is
  **494** lines, **467** of them outside fenced code blocks. Over the
  non-fenced prose lines whose first non-space character is not `|`, `>` or
  `#`, **0** exceed 78 columns — every code span and long identifier was
  wrapped at a space between spans, never broken across a line, so there is
  no disclosed over-width exception. The odd-backtick-non-fence-line
  count is **0** — no code span is broken across a line break. These numbers
  are the same ones the evidence record carries, computed against the bytes
  this file ends in.
- **No self-referential figure was transcribed.** Each was scripted over the
  finished bytes and iterated to convergence after the last edit
  (verification rule 3).
- **Review 1 landed 2026-09-17, CONFIRM WITH EXCEPTIONS (0 blocking, 1
  non-blocking F1, 1 editorial F2); both applied** [superseded 2026-09-17
  after review 1: "First draft — no review"]. By verification rule 10 review
  1 binds the reviewed `7d764fc` bytes; the F1 and F2 repairs and this
  re-tensing post-date them, so they are themselves uncovered until a second
  independent review confirms them. The headline (86 of 278; 86 of 271; the
  77 + 9 split) was reproduced this session by Python `re` over the source
  rows, by a per-rule `Counter`, and by the machine `projectShape.sources`
  tally — verification rule 2, a second method — and now by review 1's
  independent re-derivation as well. Where the M13 packet records two
  fresh-context reviews, this packet records **one**, and the register row
  P-81 says so.
- **What a review must re-derive.** The two captures' 86; the 77 + 9 split
  against `projectShape.sources`; the 415 / 417 / 409 item figures and their
  predicates; that the class gate and the excluded-content refusal are the
  two lines they are quoted as; and that Q5's subject is PWB-REQ-015's band
  semantics and nothing broader.

## Review 1 and repairs (2026-09-17)

An independent fresh-context review of this packet (read-only; only the
artifact, its governing references and the acceptance criteria) is retained
verbatim at `docs/reviews/R-POLARIS-M14-PROVENANCE-DEPTH-FUNNEL-1-RAW.md`
(**9415** bytes, sha256
`a3858514d22cf758f1d1fb16f5c3a4116ce8110445e51b9a9f266dfa4b600a81`, both
computed this session with `wc -c` and `sha256sum`, never transcribed). It
reviewed commit `7d764fc`, at which the three files it measured hashed as
follows — file-content sha256 (not truncated signed digests), recomputed this
session with `git show 7d764fc:<path>` piped to `wc -c` and `sha256sum`:

| File reviewed at `7d764fc` | Bytes | sha256 |
|---|---:|---|
| `docs/design/POLARIS-M14-PROVENANCE-DEPTH-FUNNEL.md` | 31659 | `0ed3940533bfb368170ba5a4226e40273e646dcb442da0f7349d633e025cb3e3` |
| `docs/evidence/polaris-m14-provenance-depth-funnel-2026-09-17.json` | 13943 | `1a16d30552f04f6e08f149790f487e22d9ccb5e344fd134278e87e5903adcafe` |
| `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` | 29287 | `ba741cc157371f9e966e1e7b93c5278b19ff7c8ad55cb746558285c5ef20598b` |

All three match the raw's own frozen-bytes block exactly.

Its verdict word, copied exactly: **CONFIRM WITH EXCEPTIONS**. Its counts:
**0 blocking, 1 non-blocking (F1), 1 editorial (F2)** — no blocking finding.

**Every load-bearing figure reproduced exactly, by at least two independent
methods (verification rule 2).** The review re-derived the headline
distribution on both captures — 278 source rows and 86 non-baseline (30.9%)
on the post-trim capture, 271 and 86 (31.7%) on the pre-trim, the per-rule
tally and the 185→192 / 271→278 figures that moved, the 86 unchanged in count
and composition — confirmed against the machine `projectShape.sources` rule
tally and the 192 distinct route identities; the 386 route hrefs over 192
distinct baseline identities and 0 non-baseline; the 77 + 9 split against
`projectShape.sources` (all 278 anchors blob, 0 tree, 0 missing-at-revision,
all 9 excluded carrying `record.outcome == 'excluded'`); the item figures
`projectShape.items` 415 across nine classes, 417 page markers and the catalog
eight-class 409, the 417−415 delta of two labelled `[Unknown]` from the HTML;
Q5's one `capability` entity of nine and its one hard-coded deep dive; and
every source citation at `a9f671e` (`verbatim-route.ts` 78–79 and 87,
`capability-detail.ts` 96–119 and 256–260, `polaris-source.ts` 41–58,
`project-shape-manifest.ts` 71, `spec.md` 816). It confirmed the packet
planning-only — the diff is the packet, its evidence record and a two-line
register addition, no implementation code and no act-bound byte edited — and
the P-81 row a faithful one-line rendering. It raised two exceptions, both
re-derived against source before being applied.

**F1 — non-blocking. The composition of the 9 withheld sources was glossed
imprecisely.** The packet (Q1 and Measurement 2) and the evidence record
characterized all 9 uniformly as "withheld active content" whose "TOML has no
inert context." Re-derived against `projectShape.sources`: 8 of the 9 carry
redactionClass `unclassifiable-excluded` — frontend.md (rule
pillar-named-file) and seven butler.toml (rule roster-tree) — while the ninth,
roster/qa/MANIFESTO.md (rule roster-tree), carries `excluded-artifact`: a
markdown manifesto, not a TOML file and not an identity file. The load-bearing
partition is unaffected — all 9 carry `record.outcome == 'excluded'` and the
line-87 refusal keeps every one digest-only regardless of sub-class, so the
77/9 split, the pillar-named-file 1 / roster-tree 8 rule split, every count
and every recommendation stand. Repaired: the gloss is qualified at Q1's
composition sentence and its answer, at Measurement 2 and at the evidence
record's `meaning` key, each superseded phrase kept in a dated bracket.

**F2 — editorial. A line-range disagreement inside the evidence record.** The
evidence key `route_leaf_caveat` cited `capability-detail.ts:256-259` while
the packet (Q1 and Q2) and the evidence key `leaf_renderer` cite `256-260`
for the same `selectRequirementSections` block — the call at line 256 through
the render at line 260. Repaired: `route_leaf_caveat` is aligned to `256-260`,
the superseded `256-259` kept in a dated bracket.

**Rule 10.** Review 1 binds the bytes it named — the three digests in the
table above, at commit `7d764fc` — and not these. The F1 and F2 repairs, this
section and the re-tensed posture above and in the register all post-date
`7d764fc`, so by verification rule 10 they are themselves uncovered until a
second independent fresh-context review, bound to the post-repair bytes,
confirms them. What these edits add is review 1's own confirmation and two
applied exceptions; they move no recommendation, arm or default, and Q1–Q5 are
byte-identical to `7d764fc`.

**Figures re-derived last of all, after every edit in this pass**, over the
bytes this paragraph is part of and iterated to a fixed point. Over-width
lines under the predicate "lines outside fenced code blocks whose first
non-space character is not `|`, `>` or `#`, longer than 78 columns",
denominator every line of this file: **0**. Non-fence lines with an odd
backtick count: **0** of **467**, so no code span is broken across a line
break. Total lines **494**, non-fence lines **467**. These are the same
numbers the evidence record's `packet_measured_after_review1` block carries.

## Funnel summary

```
Move M14 — Provenance depth              review 1 2026-09-17: CONFIRM w/ EXC
-------------------------------------------------------------------------
Motif      a digest a reader cannot reach is not provenance (VIS-3, VIS-7)
Headline   86 of 278 sources (31%) route-less on the post-trim capture
           86 of 271 (32%) on the dossier's pre-trim capture; 86 unchanged
Split      77 body-classified (route-able) + 9 withheld (stay digest-only)
Items      projectShape.items 415 / page markers 417 / catalog 8-class 409

Q1 S5-M2   extend the route to the 77, add a body render mode      medium
           default: gate stays, 86 stay route-less, nothing ships
Q2 S5-M3   scroll anchor to the named requirement, whole spec served medium
           default: no anchor; the route serves the whole spec
Q3 S5-M4   one legend sentence decoding the identity grammar        small
           default: no legend ships
Q4 S4-M4   one reconciliation line beside the catalog              small
           default: no reconciliation line ships
Q5 S4-M3   DRAFT a CC-REV-2 delta to PWB-REQ-015 band semantics    large
           default: no amendment drafted; one capability page stands

Acts       Q1 reaches the scope trigger; Q5 trips the spec-amendment
           trigger and asks for drafting only (binds nothing, VIS-4)
Review     Review 1 (2026-09-17): CONFIRM WITH EXCEPTIONS, 0 blk / 1 nonblk
           F1 / 1 ed F2; both applied. Rule 10: the repairs are uncovered
           until a second independent review confirms them.
Register   P-81, first-draft posture, added to PENDING-OWNER-DECISIONS.md
```

## Recommended handoff

1. **Commission the second fresh-context review** [superseded 2026-09-17
   after review 1: "Commission the fresh-context review this packet does not
   have. It is the first-draft gap by design"]. Review 1 (2026-09-17, CONFIRM
   WITH EXCEPTIONS) has landed and its F1/F2 repairs are applied, but by rule
   10 those repairs are uncovered until a second review, bound to the
   post-repair bytes, confirms them. Give the reviewer only this packet, its
   evidence record, the named source files at `a9f671e`, and the acceptance
   criteria.
2. **Put Q1–Q5 to the owner as one batch.** Each carries a recommended
   answer, its lawful arms and a stated default of "nothing happens." Slices
   3 and 4 may proceed under the acts in force once ruled; slices 1 and 2
   land together; slice 5 is drafting only.
3. **Do not build slice 5 on this packet.** Q5 authorizes drafting a CC-REV-2
   delta and nothing more; implementation waits on the owner's signature and
   a fresh implementation authorization.
4. **Keep the 9 withheld sources withheld.** No arm of any slice proposes
   reading them; Q1's recommendation keeps the excluded-content refusal
   exactly as it is, which is the fail-closed boundary of the whole move.
