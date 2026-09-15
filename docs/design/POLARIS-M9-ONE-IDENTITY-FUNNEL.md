# Feature request M9 — One identity, one epistemic shape, one vocabulary across the surfaces

> **Candidate — binds nothing.** Bead `syzygy-dov.9`, move M9 of the
> 2026-09-13 vision pursuit. **The pursuit record set**, defined once: the
> dossier `docs/pursuits/2026-09-13-vision-pursuit.md`, and the machine
> records `docs/pursuits/2026-09-13-vision-pursuit-data.json` and its
> `-harvest.json` twin. "The dossier" below always means the `.md`; a
> figure quoted from the machine records is cited to them by name
> [corrected 2026-09-15 per review 1, F6: four quotations were attributed
> to the dossier and occur only in the two JSON records].
> written in the shape of `docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md` and its
> siblings. Planning only: nothing here authorizes implementation, and this
> packet rules no slice authorized or unauthorized. Each owner question below
> names the lawful arms the owner may take; naming an arm is not a ruling that
> a slice is authorized. The owner disposes.

Date: 2026-09-15. Author: a funnel session (Claude), for the owner.

Size: **small** (slices 1, 2 and 8) / **medium** (slices 3, 6 and 7) /
**large** (slices 4 and 5).

Baseline: Syzygy `a9f671e` (main), read in the worktree on branch
`agent/syzygy-dov.9`. The subject is the three-surface POC's rendered and
served identity — the four pages, the shared model, and the vocabularies they
encode — not the manifesto generator.

**Line-number convention, stated once.** Every line number in this packet is
1-based and names the line on which the cited text *begins*, read at
`a9f671e` in this worktree this session. Where a sentence wraps across two
lines, both are given.

## The six questions for the owner

Batched, each with the recommended answer first. Everything below is the
evidence behind them. Q1 and Q2 are the packet's central questions; Q6 is the
only one that could stop slices 1 and 2, which are otherwise the cheapest
work here.

| # | Question | Recommended |
|---|---|---|
| Q1 | **Is the spec delta for slices 3–8 one CC-REV-2 amendment package against the three-surface-poc-experience specification alone, or one package spanning that specification and the project-wide Polaris (PWB) specification together?** The two specifications are separately signed and separately digest-bound: `THREE-SURFACE-POC-SPEC-SIGNOFF-ACT.md` line 39 says of its six signed artifacts, verbatim, "An edit to any of these breaks this act's digests; changes route through CC-REV-2's amendment path"; `POLARIS-PROJECT-WIDE-SPEC-SIGNOFF-ACT.md` line 31 says of its eleven, "An edit to any listed artifact breaks this act's digest binding and must use the amendment path". Lane B's package already occupies the PWB side: its manifest names all eleven PWB artifacts and declares, verbatim, "All rows take effect together or none do" (the file PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt under `.syzygy/governance/contracts/candidates/`, in its lane-B package directory pwb-scoped-attributes-amendment; named without a code span because it exists only on lane B's branch and CG-1b requires every code-span path to resolve in this worktree, and read there read-only this session). Two unperformed manifests proposing different bytes for the same eleven files cannot both be adopted. | **One package against the three-surface-poc-experience specification only, sequenced to start after lane B's PWB manifest is disposed of.** Every consequence M9 renders is a three-surface consequence: the cross-surface link, the state label, the join key, the entity/relationship epistemic tuple, the relation vocabulary. None of them changes what a *project-shape* claim carries, which is the PWB plane. **The counter-argument, and it is real:** Q2's recommended answer says PWB-REQ-007 does not reach the POC's nine entities and nine relationships; if the owner reads it the other way, the unified tuple is an implementation of a PWB requirement and the delta belongs on the PWB side, where it would collide with lane B head-on. **Second lawful arm:** one package spanning both specifications, drafted only after lane B lands or is withdrawn. **Third lawful arm, for the structural slices only:** a reviewed N/A judgment package, which is RFC2-26's own second route and a materially cheaper owner act than a CC-REV-2 amendment. The clause reads, verbatim at `.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md` line 201: "Before implementation, every observable consequence either maps to an approved OpenSpec requirement and scenario in the governance root's `openspec/**` plane, or carries a reviewed N/A judgment proving it purely structural with no independently testable behavior"; its home and gate are at line 206: "A reviewed N/A judgment is a recorded owner judgment homed in `decisions/` (RFC3-15), and the judgment is honored only through an effective owner act under RFC3-16(a)". Reachability per slice, this packet's reading and not a ruling [Inferred]: **slice 6a reachable** — a data attribute carrying an id the page already renders elsewhere changes no rendered claim; **slice 8 arguable and put rather than assumed** — the kind strings *are* rendered in the exact tables (`exact-tables.ts` lines 28 and 41), so a rename is observable even though no truth moves; **slices 1, 2, 4a, 4b, 5, 6b and 7 not reachable** — each adds independently testable behaviour, which is what the clause's "purely structural" excludes [added 2026-09-15 per review 1, F14, which found this arm named only in a Gate 5 row]. **Default if unanswered: no delta is drafted**; slices 3–8 hold and slices 1 and 2 are unaffected. |
| Q2 | **Does PWB-REQ-007's "Every project entity and project-fact claim" reach the POC's nine `entities[]` and nine `relationships[]`, or only the project-shape plane?** The requirement text (`openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md` line 443) reads, verbatim: "Every project entity and project-fact claim SHALL have a stable semantic Claim identity plus an evaluation instance, be challengeable with resolvable support, and carry the closed label, tier, exactly one primary reason, zero or more closed secondary reasons, freshness, challenge state and evaluation identity that govern it." Measured this session over the retained machine capture: **1,167** epistemic-labelled objects, of which **1,137** carry a tier and **30** do not; of those 30, **18** are the nine entities and nine relationships (`{basis,label}` ×9, `{label,reason}` ×9) and **12** are Unknown project-shape claims whose absent tier is optional in the type [Observed; census and predicate in the evidence record]. | **Only the project-shape plane.** That specification's Purpose paragraph (line 5) defines its subject as "the full declared shape of the configured Butlers project", and its reader definitions (lines 15–26) close "declared item" at nine classes, none of which is a capability, intent, work item, code region, test definition, test evidence or runtime — the kinds the nine POC entities carry (`packages/three-surface-poc-core/src/model.ts` lines 64–73). So PWB-REQ-007 governs project-shape claims, and the POC entity graph is governed by the three-surface specification, which sets no tuple requirement on it [Inferred — a reading of the requirement's scope, which is what this question puts to the owner]. **The counter-argument is strong:** the nine entities are rendered on Polaris beside 713 claims that *do* carry the full tuple, in one page and one payload, and a reader cannot see which plane a claim belongs to; if PWB-REQ-007 does reach them, the served payload is in breach today and slice 4 is a repair owed rather than an enhancement offered. **Second lawful arm:** rule that it reaches them — which makes slice 4 conformance to an adopted requirement, moves the delta to the PWB side (Q1's second arm), and makes the current payload a disclosed breach that must be recorded. **Default if unanswered: slice 4 holds.** |
| Q3 | **Are the POC's eight relation kinds inside RFC1-26's closure, and if so, is `CONTRACT-COVERAGE.md` line 89 a defect of the matrix or a satisfaction of the clause?** RFC1-26 reads, verbatim, at `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md` lines 636–642: "Every rendered internal edge must resolve to its identified target (trust floor); an edge the kernel cannot resolve is not emitted. Relations not in this table do not exist at V0; profiles may add relations under their governing RFCs but may not re-type these. **A relation may be added to this table only by amendment carrying an owner decision** (RFC1-25(a) records the two such amendments to date); no drafter, reviewer, adapter, or profile may widen the core vocabulary by prose." The POC emits eight kinds; **one**, `contains`, is in RFC1-25's table; seven are not [Observed, intersection computed this session]. `openspec/changes/three-surface-poc-experience/CONTRACT-COVERAGE.md` line 89 records the consequence "Relations outside the closed table don't exist; no prose-widening" as **covered** by POC-REQ-052 — a requirement whose own text (spec line 855) is scoped to Orrery and forbids rendering "an edge, adjacency, grouping, or emphasis encoding a relationship the shared model does not hold", which is anti-fabrication, not vocabulary closure. | **The seven are outside the closed table, and line 89's mapping does not carry the closure consequence — but the matrix row is act-bound and may not be edited, so the honest route is a new requirement in slice 3's delta plus an explicit disclosure, not a correction at the site.** RFC2-26's own second paragraph says "a complete-looking matrix over under-enumerated consequences is a defect of the matrix", so the clause anticipates exactly this shape. **The counter-argument:** the POC is a bounded non-release proof of concept that builds no kernel and claims no V0 graph; an owner may reasonably read RFC1-26's "rendered internal edge" as governing the kernel's project graph, not a POC's local rendering vocabulary, in which case nothing is out of vocabulary and slice 8 is cosmetic. **Second lawful arm:** rule the POC's kinds a surface-local vocabulary outside RFC1-26, and land slice 8 as a naming convenience with no contract claim. **Third lawful arm:** Q1's reviewed N/A judgment package under `decisions/`, which reaches slice 8 on the reading that a rename with no rendered-truth change is purely structural — arguable rather than clear, because the kinds are rendered (`exact-tables.ts` lines 28 and 41) [added 2026-09-15 per review 1, F14]. **Default if unanswered: slice 8 lands neither the renames nor the flag**, and the divergence stays recorded here. |
| Q4 | **If and when an agent asserts something, may the POC construct `Inferred`?** [recast 2026-09-15 per review 1, F13; superseded wording: "Should the POC be able to construct `Inferred` at all?" — on the recommended arm this packet's own act table says no trigger is reached, so the genuine gate is the constructible limb, not the typing decision.] Doctrine reserves the label for agent output: `.syzygy/governance/doctrine/trust-and-evidence.md` line 16 says, verbatim, "An LLM assertion is **Inferred, never Observed**", and the shipped legend already says so in two sentences (`apps/three-surface-poc/src/polaris-copy.ts` lines 35 and 41). Measured this session: `Inferred` appears in **0 of 27** non-test modules under `packages/three-surface-poc-core/src` and in **1 of 45** under `apps/three-surface-poc/src`, that one being the legend file; the two production claim constructors are `observedClaim` and `unknownClaim` (`packages/three-surface-poc-core/src/project-shape-model.ts` lines 184 and 188). Note that the shared tuple type **already carries** an Inferred arm (`packages/cap1-core/src/epistemic.ts` line 52); what is missing is a constructor and, on the POC's own two-member union, the arm itself. | **Yes, but only as the typed landing zone with no production constructor until an agent actually asserts something.** VIS-2's bar is that absence of evidence renders Unknown; an Inferred arm that nothing can construct is honest, and an arm that a renderer can construct from a non-agent source is the failure VIS-2 names. Add the arm, add the exclusion battery, and leave the constructor to whatever first produces an agent assertion. **The counter-argument:** a typed-but-unreachable arm is dead code with a test suite, and the honest render of "no agent has asserted anything here" is already Unknown with a reason — so the arm buys a vocabulary completeness claim and no observable truth. **Second lawful arm:** leave `PocEpistemic` two-membered, unify only the shape, and record that 2 of 3 doctrine labels remain unreachable. **On the recommended arm no owner act is reached**: Gate 3's act table records that "A typed-but-unconstructible arm reaches no trigger", so the typed arm proceeds under the improvement-cycles direction's recorded-finding limb like slices 1, 2 and 7, and what is put to the owner here is the *constructible* limb — which is why Q4 stays in the batch as a question rather than being decided inside the implementation plane [added 2026-09-15 per review 1, F13]. **The recommended answer did not change.** **Default if unanswered: the shape unifies without the Inferred arm** (slice 4a only; slice 4b holds). |
| Q5 | **Which of M9's byte-adding slices may draw on the page's measured headroom, and in what order, given that a ceiling breach serves nothing?** Measured this session on the retained lane-A capture at `a9f671e`: `/polaris` is **1,478,637** bytes direct and **1,484,487** through the tailnet mount, against a declared `maxHumanResponseBytes` of **2,097,152** (`.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json` line 270) — **618,515** bytes of headroom direct, **612,665** through the mount. The page already spends **418,122** bytes, 28.3% of itself, on 713 claim-tuple spans averaging **586.4** bytes each. The break-even for a per-item ribbon over the 415 declared items is **1,490** bytes per item. A ribbon whose three slots reuse the existing tuple markup costs at least 1,758 bytes per item and **does not fit**; a minimal three-anchor ribbon at roughly 300 bytes per item costs about 124,500 and does. | **Spend the headroom in this order: slice 1 (about 2 KB), slice 2 (under 1 KB), slice 6's identity attributes (about 12 KB on Trajectory, under 1 KB on Orrery), slice 4's eighteen tuples (about 10.5 KB on Polaris), and slice 5's ribbon last and only at the one-capability scale (about 1 KB), never at catalog fan-out until measured again.** **The counter-argument:** that headroom is not free — `AGENTS.md` records the P-63 trim's remaining margin as earmarked for the P-60/P-61 Butlers repairs at 418–443 KB, and those repairs land on a real Butlers commit this packet cannot schedule; spending 25 KB here narrows a margin someone else is counting on. **Second lawful arm:** land only slices 1, 2 and 8 (no measurable byte growth beyond about 3 KB) until the Butlers repairs are on main and the page is re-measured. **Default if unanswered: slices 1, 2 and 8 proceed on their own gates; every byte-adding slice holds.** |
| Q6 | **Do slices 1 and 2 need an owner direction naming them?** No requirement in the signed three-surface specification names either consequence: over its **24** requirements and **24** scenarios, swept this session, none requires a link from a claim on one surface to the same subject on another, and none requires a surface to name which of the three states it holds. The improvement-cycles direction says, verbatim (`.syzygy/governance/decisions/THREE-SURFACE-POC-IMPROVEMENT-CYCLES-DIRECTION.md` lines 55–56): "Improvement-cycle work must trace to POC-REQ-001..061 or to a recorded review finding." | **No — they trace to recorded review findings, which is the direction's own second limb.** The pursuit produced exactly what that direction defines a cycle's first step to be — "a review/audit of the runnable POC in fresh context producing evidence-cited findings" (line 34) — and L6-F2 and L6-F7 are those findings, each carrying capture-level evidence re-derived in this packet. **The counter-argument:** the direction's cycle structure also says a cycle's repairs are "derived only from recorded findings" and that "the agent reports each completed cycle to the owner before starting the next" (line 41) — the first quotation begins at line 36, not 41 [corrected 2026-09-15 per review 1, F15(2), which found two quotations sharing one cite]; if the owner reads the pursuit as a *new* cycle rather than a continuation, its report is owed before any repair lands. **Second lawful arm:** treat the pursuit as cycle *n*'s review, report it, and land slices 1 and 2 as cycle *n*'s repairs after that report. **Default if unanswered: slices 1 and 2 are filed but not landed**, because the report is cheap and the ordering is the owner's.  |

### Decided in this packet, not put to the owner

**The dossier's prerequisite line survives in one half and fails in the
other.** It reads: "None for links and naming; spec amendment for the shared
identity and the ribbon (the cross-surface identity system is a declared
deferral in the POC spec)."

- *"None for links and naming"* **survives**, subject to Q6. Neither slice 1
  nor slice 2 edits a bound byte, and both trace to recorded findings.
- *"Spec amendment for the shared identity and the ribbon"* **survives and
  widens**: the epistemic tuple (slice 4) and the relation names (slice 8)
  need the same delta, which the dossier's own slice 3 already says even
  though its prerequisite sentence does not.
- *"The cross-surface identity system is a declared deferral in the POC
  spec"* **does not survive as written**, and the correction makes the
  amendment easier to justify rather than harder. The three clauses in
  question sit in **Part B2**, whose heading reads "clauses believed not
  applicable (author's reading, non-binding)" (line 232) and whose preamble
  says, verbatim (lines 238–241): "**A belief is not a reviewed N/A**; until
  the owner records N/A judgments in `decisions/`, these clauses'
  consequences also render Unknown pending owner-reviewed N/A. The per-clause
  readings are listed so the owner can review or contest each one directly."
  The signing act says the same thing in its own words: "This act **mints no
  per-clause N/A judgment**; every uncovered consequence continues to render
  'Unknown pending owner-reviewed N/A' exactly as the matrix states"
  (`.syzygy/governance/decisions/THREE-SURFACE-POC-SPEC-SIGNOFF-ACT.md`
  lines 32–34). So there is **no owner deferral to reopen**. What exists is
  an author's belief, an uncovered consequence rendering Unknown, and a
  specification that says nothing about cross-surface identity either way.

**M9's slice list is three slices short of its own What bullet.** The
dossier's What bullet names seven agent moves and its Slices list gives five.
L6-M7 (moving Polaris's observed band) appears in the What and in no slice;
L6-M5's *implementation* half and L5-M8's *implementation* half each have
their spec side folded into slice 3 and no slice of their own. They are
carried below as slices 6, 7 and 8 with their mappings done, so the gap is
recorded rather than dropped. The mapping is:

| Dossier slice | This packet | Agent move |
|---|---|---|
| 1 Links | Slice 1 | L6-M2 |
| 2 State labels | Slice 2 | L6-M3 |
| 3 Spec delta | Slice 3 | L6-M5 (spec), L5-M2 (spec), L5-M8 (spec) |
| 4 Shape unification | Slice 4a, 4b | L5-M2 |
| 5 Ribbon | Slice 5 | L6-M6 |
| — (in the What only) | Slice 6 | L6-M5 (implementation) |
| — (in the What only) | Slice 7 | L6-M7 |
| — (in the What only) | Slice 8 | L5-M8 (implementation) |

**Slice ordering inside M9 is a stated decision, not a question.** The
2026-08-29 POC mode direction sets work-in-progress **one** for POC
shared-model changes, restated in the improvement-cycles direction (line 50).
Slices 2, 4, 6 and 8 all change the shared model file
`packages/three-surface-poc-core/src/model.ts`.
They therefore land one at a time, in the order slice 2 → slice 6 → slice 4 →
slice 8, whatever the owner rules elsewhere. That is the existing bound
applied, not a new judgment.

**A near-miss in this packet's own measurement, recorded rather than hidden.**
A first pass at the identity census reported that every entity and
relationship id is minted twice on Orrery and on the home page, and that nine
fragment links per page therefore resolve to a non-unique target — a VIS-7
violation. It was false. The predicate `\bid="` matches inside
`data-entity-id="` and `data-relationship-id="` because `-` to `i` is a word
boundary. Re-run with `\sid="`, all four pages have **zero** duplicated ids
and **zero** fragment links whose target is not exactly one element
(Polaris 350 ids / 699 fragment hrefs, Trajectory 311 / 311, home 24 / 36,
Orrery 23 / 19, on the post-lane-A and 2026-09-10 captures respectively)
[Observed, both predicates run this session; verification rule 1]. No finding
in this packet rests on the discarded figure.

## Gate 0 — Baseline

| Pillar | Present | Constrains this request |
|---|---|---|
| Doctrine | `.syzygy/governance/doctrine/vision.md`, `trust-and-evidence.md` | VIS-1, VIS-2, VIS-3, VIS-4, VIS-5, VIS-7 |
| Decisions | `.syzygy/governance/decisions/THREE-SURFACE-POC-SPEC-SIGNOFF-ACT.md`, `THREE-SURFACE-POC-IMPROVEMENT-CYCLES-DIRECTION.md`, `THREE-SURFACE-POC-MODE-DIRECTION.md`, `POLARIS-PROJECT-WIDE-SPEC-SIGNOFF-ACT.md`, `PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md`, `PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md` | quoted per slice in Gate 3 |
| Specification | `openspec/changes/three-surface-poc-experience/specs/three-surface-poc-experience/spec.md` | **24 requirements, 24 scenarios** [Observed, counted this session under the predicates `^### Requirement:` and `^#### Scenario:`] |
| Second specification | `openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md` | PWB-REQ-007 and PWB-REQ-020; reached only on Q2's second arm |
| Coverage matrices | `openspec/changes/three-surface-poc-experience/CONTRACT-COVERAGE.md` | signed; Part B2's beliefs bind nothing and render Unknown |
| Contracts | RFC-0001 §3.7 (RFC1-24 … RFC1-26), RFC-0002's RFC2-24 and RFC2-26 | Wave A **ACCEPTED**, act performed 2026-08-17 (`PROJECT-STATUS.md` line 147) |
| Registry | `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json` | `maxHumanResponseBytes` 2,097,152 (line 270); a breach serves nothing |
| Policies | `.syzygy/governance/policies/craft-and-care/review-and-documentation.md` | CC-REV-2, the amendment path slice 3 uses |

**What binds, and what only looks like it binds.** Six
three-surface-poc-experience artifacts are digest-bound by the sign-off act
(its table at lines 42–49; the digests are not reproduced here, per CG-15 —
the record is cited by path). `tasks.md` is deliberately **not** in that set:
the act says so at lines 51–53. Eleven PWB artifacts are digest-bound by the
project-wide sign-off act (table at lines 34–46). No slice below edits any of
those seventeen files outside slice 3, which is by construction an amendment
through CC-REV-2 and therefore the lawful path rather than an edit.

**Two banners a reader must not trust.** `CONTRACT-COVERAGE.md`'s head opens
"**Candidate.** Ships with the candidate specification and binds nothing
until owner sign-off" (line 3) over bytes the 2026-08-30 act signed;
`openspec/changes/three-surface-poc-experience/proposal.md` carries the same
class of stale opening. Per `AGENTS.md`, read the act record, never the
package banner. Neither may be corrected: the act bound the bytes that say
it.

**What the PWB implementation authorization does not authorize.** Its line 76
reads, verbatim: "No edit to any act-bound artifact: the eleven signed PWB
artifacts, the three effect-act subjects, the six signed
`three-surface-poc-experience` artifacts, or the seven adopted Capability 1
artifacts. Spec changes route through CC-REV-2's amendment path and a new
owner act." Its escalation triggers (lines 88–94) stop implementation before
"a change to doctrine or an accepted contract; an amendment to the signed PWB
specification; … or any scope beyond the signed change." Slice 3 is an
amendment by construction and therefore crosses a trigger by design; Q1 asks
which specification it crosses it for.

## Gate 1 — Motif

**Eleven attribute names carry an entity identity across the four served
pages, and not one of them appears on more than two of them.** [Corrected
2026-09-15 per review 1, F4, from "Ten": the per-page counts 3 / 8 / 2 / 0
were right and their union is 3 + 8 = 11, because Orrery's two are already
home's. Recomputed this session.] Measured this session
over the four captures, with the nine ids of `model.entities` as the
denominator and "an attribute whose value is exactly one of the nine" as the
predicate:

| Page | Attribute names carrying an entity id | Count |
|---|---|---:|
| home | `id`, `data-entity-id`, `data-surface-entity` | 3 |
| Polaris | `data-polaris-section`, `data-claim-provenance`, `data-unknown-disclosure`, `data-argument-ref`, `data-capability-deep-dive`, `data-depth-dive`, `data-depth-source`, `data-proposal-capability` | 8 |
| Orrery | `id`, `data-entity-id` | 2 |
| Trajectory | none | 0 |

Polaris — the surface that carries the capability argument — mints **no**
`id` and **no** `data-entity-id` for any of the nine. Trajectory names none of
the nine in any attribute at all. The one attribute that *is* an identity by
design, `data-claim-id`, occurs **699** times on the 2026-09-10 Polaris
capture and **713** on the post-lane-A capture, and **0** times on the other
three pages — and **0** of its values is an entity id: all of them lie in the
`claim:` namespace of the project-shape plane. So the attribute the product
uses to say "this element is that subject" exists on one plane of one page.

**Zero of 1,439 rendered hrefs cross a surface at claim level.** Re-derived
this session over the four captures: home 40, Polaris 1,061, Trajectory 315,
Orrery 23. Classified by predicate — a leading `#` is a fragment; a leading
`/polaris/source` is a source route; one of `/`, `/polaris`, `/trajectory`,
`/orrery` exactly is a surface root; a match of
`^/(polaris|trajectory|orrery)#` is a claim-level cross-surface link — the
totals are 1,051 fragments, 372 source routes, **16** surface roots (exactly
four per page, all sixteen inside the single `<nav class="site-nav">` block
that `apps/three-surface-poc/src/page-shell.ts` line 23 emits) and **0**
claim-level cross-surface links.

**And the sweep that would catch a broken one is blind to the shape.** The
existing dangling-link check
(`apps/three-surface-poc/src/polaris-reachability.test.ts` line 189)
extracts its population with `/\shref="#([^"]+)"/g` (line 101) — a
predicate that matches fragment links and nothing else. A cross-surface
href of the form
`/orrery#capability:whatsapp-transport-identity` is invisible to it. Slice 1
therefore cannot land its links without extending that sweep, or it ships
exactly the class of defect VIS-7 names as a violation, unchecked.

**The three-state model is never named on a surface.** Sweeping the four
captures case-insensitively: *desired* occurs **1** time in total, in the home
page's caveat sentence, quoted whole from
`apps/three-surface-poc/src/routes.ts` line 80: "POC, not product status.
Desired, execution, and observed state remain distinct. Merge is not
verification. Missing evidence is rendered Unknown." [restored 2026-09-15 per
review 1, F17, which found the last two sentences dropped with no elision
mark]; *execution state* occurs **0** times; *observed state* occurs **1**
time,
in that same sentence; *three-state* and *three state* occur **0** times
anywhere. The three home panels are distinguished by their question strings
alone, and `PocSurface` (`packages/three-surface-poc-core/src/model.ts` lines
90–96) carries `id`, `title`, `question` and two id lists — and no state.

**Two epistemic types, five arms, four shapes in one payload — and the
thinner of the two governs the graph the product exists to render.** The POC's
own union is two-membered (`model.ts` lines 44–46):

```
export type PocEpistemic =
  | { readonly label: 'Observed'; readonly basis: string }
  | { readonly label: 'Unknown'; readonly reason: string };
```

The shared tuple is three-membered, with an Inferred arm already typed
(`packages/cap1-core/src/epistemic.ts` lines 50–67), and the project-shape
claim wraps it with a stable identity, resolution routes, a challenge state
and support (`packages/three-surface-poc-core/src/project-shape-model.ts`
lines 120–131). `PocEntity.epistemic` and `PocRelationship.epistemic`
(`model.ts` lines 76 and 86) take the two-member union; so do all nine
relationships, including the four edges of the intent → work → code →
evidence → runtime chain [corrected 2026-09-15 per review 1, F20, from
"five edges"; the chain holds four, and the fifth Unknown relationship is
`coverage-unknown`, capability → `region:unmapped-code`, which is not on it].

**And the relation vocabulary is a near-homograph of a closed contract set.**
The POC emits eight kinds — `contains`, `governed-by`, `mapped-to`,
`materializes-as`, `changes`, `verified-by`, `satisfies-at-runtime`,
`coverage-unknown` — over nine relationships. RFC1-25's table closes the V0
vocabulary at **26** data rows carrying **30** backticked relation tokens.
The intersection is **{`contains`}**: 1 of 8. `materializes-as` versus
`materializes`, `verified-by` versus `verifies`, `governed-by` versus
`governs` are each one morpheme apart. `PocRelationship.kind` is declared
`string` (`model.ts` line 82), so nothing in the type system notices.

**Success criteria, per slice.** Slice 1: a reader on any surface can reach
the same subject on another surface by following a link, and a broken one
fails a check. Slice 2: each of the four pages names which of the three
states it holds, and the legend names all three. Slice 3: a specification
exists that says what a cross-surface identity is. Slice 4: one epistemic
record shape across the payload, with the third label reachable or honestly
absent. Slice 5: the owner sees, per claim, what is meant, what is moving and
what exists — with Unknown and a route in the empty slots. Slice 6: the same
subject carries the same identity attribute on every page that names it.
Slice 7: each surface holds the state it owns and links for the rest. Slice 8:
every emitted relation kind is either RFC1-25's name or explicitly flagged as
outside it. None of these turns anything green; four of them make an absence
visible that is currently invisible.

**What M9 is not.** It is not a change to project-shape observation, not a
Butlers read, not a widening of any content class, not a provider
integration, and not a claim that the three-state propagation exists. At
today's evaluation the honest render of slice 5's ribbon is two Unknowns for
414 of 415 items, and that is the point.

## Measurements at `a9f671e`

Every figure below was taken this session, in the worktree at `a9f671e` or
over the retained captures named beside it. Method, predicate, denominator
and raw output for each are in the evidence record beside this packet.

### Href census over the four captures

Captures: `home.html`, `polaris-7478.html`, `trajectory-7478.html`,
`orrery-7478.html` under the retained capture directory. Predicate: every
`href="…"` occurrence.

**The four-page capture mixes two evaluations, and each served figure is
named to its own.** [Corrected 2026-09-15 per review 1, F1; superseded
wording: "provenance 2026-09-10 loopback daemon" — false for two of the
five files, unsupported for two more, and true only of
`polaris-7478.html`.] Read this session out of the captures' own embedded
evaluation blocks and the retained run script and daemon log in the same
directory:

| Capture file | Daemon | Evaluation | as-of |
|---|---|---|---|
| `polaris-7478.html` | owner's loopback daemon on 7478 | Butlers `66ed58f` / observer `a121591` | 2026-09-10T01:50:48.470Z [Observed, from the file] |
| `trajectory-7478.html` | [Inferred] the same loopback daemon | [Unknown] from the bytes | [Unknown] from the bytes |
| `orrery-7478.html` | [Inferred] the same loopback daemon | [Unknown] from the bytes | [Unknown] from the bytes |
| `home.html` | a **private** daemon, `--port 0 --state-dir …`, served on `127.0.0.1:41215` | Butlers `7c8743f` / observer `f4589e2` | 2026-09-13T02:03:33.040Z [Observed, from the file] |
| `api-poc.json` | the same private daemon | Butlers `7c8743f` / observer `f4589e2` | 2026-09-13T02:03:33.040Z [Observed, from the file] |

`trajectory-7478.html` and `orrery-7478.html` embed no snapshot label at
all, so their provenance is **[Unknown] from the bytes**; it is asserted
only **[Inferred]** from the capture directory's own retained run script
and daemon log, which show that the run those two `-7478` files did *not*
come from wrote `home.html`, `api-poc.json` and an un-suffixed
`trajectory.html` and `orrery.html` from the private daemon, and that the
same run's `polaris.html` is an 838-byte `response-limit-breached` body —
which is why a `-7478` Polaris page had to be substituted.

**Which figures depend on which.** The href census, the identity-attribute
census, the three-state word sweep, the `data-claim-id` 2026-09-10 column
and the `/trajectory`, `/orrery` and home ceiling rows are all taken over
the four-page set and therefore mix the two evaluations. The epistemic
census (1,167 / 1,137 / 30 / 18) and every figure derived from it come
from `api-poc.json` alone — the private daemon's 2026-09-13 evaluation,
two Butlers revisions and three days from the `-7478` pages beside it. The
post-lane-A Polaris figures, the 713 claim-tuple spans and the reality-band
decomposition come from the lane-A capture, named at use. **The arithmetic
does not move**: the whole epistemic census was recomputed this session
over *both* retained `api-poc.json` files — the four-page one and the
lane-A one — and they agree in every cell (1,167 labelled objects; 1,137
with a tier, 30 without, of which 18 are the nine entities and nine
relationships; Observed 1,146 / Unknown 21 / Inferred 0; tier `report-fact`
1,137 and 0 of the other five; freshness `fresh` 1,149 and 0 of the other
three; challenge `unchallenged` 1,149; Unknown primary reason
`excluded-content` 12 and 0 of the other eleven) [Observed, both files
walked this session with the same predicate]. The defect was the stated
provenance, not a number.

| Page | hrefs | fragment | source route | surface root | claim-level cross-surface |
|---|---:|---:|---:|---:|---:|
| home | 40 | 36 | 0 | 4 | **0** |
| Polaris | 1,061 | 685 | 372 | 4 | **0** |
| Trajectory | 315 | 311 | 0 | 4 | **0** |
| Orrery | 23 | 19 | 0 | 4 | **0** |
| **total** | **1,439** | **1,051** | **372** | **16** | **0** |

All sixteen surface-root hrefs sit inside the one `<nav class="site-nav">`
block each page carries; the count of nav blocks per page is 1 and the count
of hrefs inside it is 4, on all four pages. On the post-lane-A Polaris
capture the totals are 1,089 hrefs and still **0** claim-level cross-surface
links.

### `data-claim-id` and the identity attributes

| Page | `data-claim-id` | distinct | values naming an entity id |
|---|---:|---:|---:|
| Polaris (2026-09-10) | 699 | 689 | **0** |
| Polaris (post-lane-A) | 713 | 703 | **0** |
| home | 0 | 0 | 0 |
| Trajectory | 0 | 0 | 0 |
| Orrery | 0 | 0 | 0 |

The 699 and 713 counts exceed their distinct counts by 10 exactly, which is
the per-tuple repetition `AGENTS.md` records for PWB-REQ-020 parity: a claim
may render more than once, so `tuples === distinct ids` is a false invariant
and is not asserted here.

### The three states, as words on the pages

Case-insensitive sweep over the four captures, denominator the four files:

| Term | home | Polaris | Trajectory | Orrery |
|---|---:|---:|---:|---:|
| desired | **1** | 0 | 0 | 0 |
| execution state | 0 | 0 | 0 | 0 |
| observed state | **1** | 0 | 0 | 0 |
| three-state / three state | 0 | 0 | 0 | 0 |

Both home occurrences are the same sentence, emitted at
`apps/three-surface-poc/src/routes.ts` line 80.

### The epistemic shapes in the payload

Over the retained `api-poc.json` capture, walking every object carrying a
`label` whose value is one of the three doctrine labels:

| Key signature | Count | Where |
|---|---:|---|
| `{freshness, label, tier}` | 1,137 | project-shape facts, items, sources, account, classes |
| `{freshness, label, reasons}` | 12 | project-shape Unknown claims |
| `{basis, label}` | 9 | 5 entities, 4 relationships |
| `{label, reason}` | 9 | 4 entities, 5 relationships |
| **total** | **1,167** | |

Labels: Observed 1,146, Unknown 21, **Inferred 0**. Tiers: `report-fact`
1,137, every other tier 0 of 6. Unknown primary reasons: `excluded-content`
12, every other reason 0 of 12. Freshness: `fresh` 1,149, 0 of the rest.
Challenge: `unchallenged` 1,149.

**The dossier's "three epistemic record shapes" is not reproducible under any
of the three predicates this packet can construct.** Declared TypeScript
types: **2**. Declared arms across those types: **5** (2 + 3). Key signatures
actually emitted: **4**. The load-bearing part of the finding — that the
weaker shape governs the whole propagation graph — stands unchanged: all
eighteen entity and relationship claims carry the two-member union, and the
**four** edges of intent → work → code → evidence → runtime are among them:
`materializes-as`, `changes`, `verified-by` and `satisfies-at-runtime`. The
fifth Unknown relationship is `coverage-unknown`, capability →
`region:unmapped-code`, which is not on the chain [corrected 2026-09-15 per
review 1, F20, from "the five edges"; all nine relationships read from the
machine capture this session].

The machine records' parenthetical "30 of them (all 9 entities, all 9
relationships and their kin) carry NO tier field at all"
(`docs/pursuits/2026-09-13-vision-pursuit-data.json` line 4296 and the
`-harvest.json` twin's line 3889; it does not occur in the dossier `.md`
[Observed, `grep -rn -F` over every tracked file under `docs/`, `.syzygy/`
and `openspec/` this session — corrected 2026-09-15 per review 1, F6]) is
right on the 30 and loose on the composition: 18 of the 30 are the entities
and relationships; the other 12 are
Unknown project-shape claims whose tier is optional in the type
(`project-shape-model.ts` line 188 takes `tier` as an optional parameter), so
their missing tier is a type-lawful absence and not the same defect.

### `Inferred` across the POC source

Denominators: 27 non-test modules under `packages/three-surface-poc-core/src`,
45 under `apps/three-surface-poc/src`, 21 under `packages/cap1-core/src`.
Predicate: the word `Inferred` on a whole-word boundary.

| Tree | non-test hits | files |
|---|---:|---|
| `packages/three-surface-poc-core/src` | **0** | none |
| `apps/three-surface-poc/src` | 2 | `polaris-copy.ts` only, lines 35 and 41 |
| `packages/cap1-core/src` | 2 | `vocabulary.ts` line 65, `epistemic.ts` line 36 |

Both cap1-core hits are the vocabulary declaration and its tuple-position
binding, not a constructor. The dossier cites `vocabulary.ts` lines 64–65 for
`EPISTEMIC_LABELS`; the declaration begins on **line 65**, with lines 63–64
carrying its comment.

### The eight edge kinds against RFC1-25

RFC1-25 is defined at
`.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`
line 463 per `DIRECTIVE-REGISTER.md` line 226. Its opening sentence reads,
verbatim:

> **RFC1-25.** The V0 relation vocabulary is **closed** at the following set.

Its table runs from the header at line 494 to the last data row at line 521:
**26 data rows**, carrying **30** backticked relation tokens in the first
column — `contains`, `part_of`, `declares`, `refines`, `governs`,
`motivates`, `implements`, `structurally_related`, `calls`, `exposes`,
`accesses(mode)`, `realizes`, `covers`, `verifies`, `depends_on`,
`declared-dependency`, `placed_in`, `proposes_change_to`, `materializes`,
`addresses`, `supports`, `challenges`, `dismisses`, `adjudicates`, `cites`,
`scoped_to`, `produced_by`, `identified_in`, `supersedes`, `succeeds`.

**The machine records' "25-row table" undercounts by one and their
enumeration omits **four** of the thirty tokens: `calls`, `exposes`,
`accesses(mode)` and `succeeds`.** Predicate: the set difference between
the thirty backticked first-column tokens of RFC1-25's table (header 494,
last data row 521) and the twenty-five comma-separated entries of the
enumeration at `docs/pursuits/2026-09-13-vision-pursuit-data.json` line
4360, split on `/` to give twenty-six tokens; denominator thirty, computed
this session [Observed]. The `-harvest.json` twin carries the same string
at its line 3953. [Corrected 2026-09-15 per review 1, F7; superseded
wording: "The dossier's '25-row table' undercounts by one and its
enumeration omits `succeeds` (line 521, the split/merge continuity edge)"
— which was itself a spot check where rule 9 wants a set difference, and
cited the dossier `.md`, where the string does not occur.] The
load-bearing figure is unaffected: the intersection with the POC's eight
kinds is still
**{`contains`}**, 1 of 8.

| POC kind | count | RFC1-25 counterpart | in the set |
|---|---:|---|---|
| `contains` | 1 | `contains` / `part_of` | **yes** |
| `governed-by` | 1 | `governs` (direction reversed) | no |
| `mapped-to` | 2 | `implements` or `covers`, per endpoint | no |
| `materializes-as` | 1 | `materializes` | no |
| `changes` | 1 | none | no |
| `verified-by` | 1 | `verifies` (direction reversed) | no |
| `satisfies-at-runtime` | 1 | none | no |
| `coverage-unknown` | 1 | none | no |

### Page sizes against the declared ceiling

Every row names the daemon and evaluation it was served from; no new
measurement was taken for this packet and no daemon was started [row labels
added 2026-09-15 per review 1, F3, which found the table silent on which
row came from which daemon].

| Artefact | Daemon and evaluation | bytes | ceiling | headroom |
|---|---|---:|---:|---:|
| `/polaris` direct, post-lane-A | lane-A private daemon, Butlers `2e3bac9` | 1,478,637 | 2,097,152 | 618,515 |
| `/polaris` through the tailnet mount | the same | 1,484,487 | 2,097,152 | 612,665 |
| `/polaris` pre-lane-A (`polaris-7478.html`) | loopback daemon on 7478, Butlers `66ed58f` | 2,090,025 | 2,097,152 | **7,127** |
| `/polaris` pre-lane-A, private daemon (`polaris.html`) | private daemon, Butlers `7c8743f` | **2,132,656 observed against 2,097,152 declared — a breach; 838 bytes of `response-limit-breached` body served** | 2,097,152 | **none; over by 35,504** |
| `/trajectory` (`trajectory-7478.html`) | loopback daemon on 7478 [Inferred]; evaluation [Unknown] from the bytes | 254,168 | 2,097,152 | 1,842,984 |
| `/orrery` (`orrery-7478.html`) | the same | 37,048 | 2,097,152 | 2,060,104 |
| home (2026-09-13) | private daemon, Butlers `7c8743f` | 38,706 | 2,097,152 | 2,058,446 |
| `/api/poc` post-lane-A | lane-A private daemon | 5,520,314 | 8,388,608 | 2,868,294 |

**The 618,515-byte headroom is one evaluation's figure, and the same page
breached the ceiling on a different Butlers revision three days later.**
The two pre-lane-A rows are the whole argument for reading it that way: at
Butlers `66ed58f` `/polaris` sat **7,127** bytes under the ceiling, and at
Butlers `7c8743f` it served nothing at all — HTTP 503 with
`served: "nothing"`, `failure: "response-limit-breached"`, readiness false,
and no ledger line, exactly as `AGENTS.md` records. The lane-A trim is what
bought the 618,515, and a Butlers commit nobody here schedules can spend it
again [Observed, both byte counts and the breach body's own `observed` and
`declared` fields read off the retained captures this session; two of the
three pre-lane-A figures appear nowhere in the first draft].

Claim-tuple spans on the post-lane-A Polaris page: **713** occurrences,
**418,122** bytes, mean **586.4**, min 559, max 661 — 28.3% of the page.

### The Polaris observed band, decomposed

Predicate for the band: the `<section class="band" … data-band="reality">`
element through its depth-matched closing tag. Identical on both Polaris
captures. **One predicate for every part row: delete the element, its own
tags included, and count the bytes that leave the page.** That is the only
predicate under which a part figure is a recovery figure, and it is applied
to all four [restated 2026-09-15 per review 1, F8; in the first draft two
of the four part rows carried no stated predicate and the four were
measured on inconsistent conventions — inner text for one, an inner list
for another. Every figure below was re-measured this session on both
Polaris captures, which agree to the byte].

| Part | predicate | bytes |
|---|---|---:|
| whole reality band | the `data-band="reality"` section, tags included | **14,820** |
| 11 headings | each `<h1>`–`<h6>` element, tags included | 2,130 |
| 9 entity detail spans | each `<span data-claim-provenance="…">` element, tags included | **1,534** (905 as inner text alone — the first draft's figure) |
| 9 provenance citation spans | each `<span class="citation">` element, tags included | 4,309 (unchanged; the first draft already measured this one with tags) |
| the relationship section | the whole `<section class="relationships">`, tags included — h3 189 + lede 243 + wrapper 171 + the list | **5,680** (5,077 for the inner `<ul>` alone — the first draft's figure) |

**The machine records' 14,804 is 16 bytes low and their "~12 KB recovered,
2.8% of the P-63 trim" overstates the saving**
(`docs/pursuits/2026-09-13-vision-pursuit-data.json` and the
`-harvest.json` twin carry both strings; neither occurs in the dossier
`.md` [Observed, `grep -rn -F` over every tracked file under `docs/`,
`.syzygy/` and `openspec/` this session — cite corrected 2026-09-15 per
review 1, F6]). Under the one stated predicate, dropping the details and
citations recovers **5,843** bytes; also moving the relationship section to
Orrery brings the total to **11,523**, which is 1.3% and 2.6% of the P-63
trim's 434,960 bytes respectively [corrected 2026-09-15 per review 1, F8;
superseded figures 5,214 and 10,291, which mixed inner-text and inner-list
measurements into a tags-included total and understated both recoveries].
And slice 7 as the machine records frame it *adds* a claim tuple per
entity: nine tuples at the measured mean is **5,278** bytes, so the net is
a saving of between **565** and **6,245** bytes depending on whether the
relationship section moves [derived 2026-09-15 from the corrected part
figures; superseded: "the net saving is between −64 and +5,013 bytes"].
Slice 7 is a coherence move with no reliable byte dividend, and it is argued
that way below.

### Line numbers re-verified at `a9f671e`

The dossier's evidence lines were read at `f4589e2`; the lane-A trim
(`2ef68f5`) moved several. Re-verified this session:

| Dossier citation | At `a9f671e` |
|---|---|
| `polaris.ts` 256–295 | exact enough: `codeStructureSection` 255–274, `workItemsSection` 276–295 |
| `polaris.ts` 1156–1171 (reality band) | **stale**: at 1156–1171 sit the tail of `argumentBand` and `contractBand`; `realityBand` begins at **1173** |
| `model.ts` 43–45 | **off by one**: `PocEpistemic` is declared at 44–46 |
| `vocabulary.ts` 64–65 | **off by one**: `EPISTEMIC_LABELS` is at 65 |
| `trajectory.ts` 137–192 | exact: `renderTrajectoryPage` opens at 136 and its eyebrow is at 192 |
| `orrery.ts` 157 | exact: the eyebrow string |
| `polaris-copy.ts` 35, 41 | exact: both legend sentences |
| RFC-0001 line 463 | exact: RFC1-25's opening sentence |
| `CONTRACT-COVERAGE.md` 358–360, 371 | 358 and 360 are RFC6-1 and RFC6-3 as cited; **371 is RFC6-24**, not RFC6-12 — RFC6-12 is at **369** |

## Gate 2 — Doctrine

**VIS-1 — Comprehensible truth first.** Quoted at the clause,
`.syzygy/governance/doctrine/vision.md` lines 82–94: "The full ordering,
highest first: (1) truth and observation determinism; (2) comprehension of
the truth's presentation; (3) momentum (delivery speed); (4) breadth of scope
and fidelity of presentation; (5) reproducibility of derived convenience…
Comprehension is achieved by simplifying *presentation*, never *content*."
Slices 1, 2 and 7 are rank-2 work: nothing new is observed, and what is
already true becomes reachable and nameable. Slices 4, 6 and 8 are rank-1
work: they change what the model asserts about itself. When the two compete
for the same headroom, VIS-1's ordering says the rank-1 slices win, which is
why Q5's recommended order puts slice 4 ahead of slice 5.

**VIS-2 — No evidence means Unknown, not success.** Lines 96–106: "No surface
may declare a project aligned, converged, or genome-complete — nor turn
anything green — without current evidence… Until a claim class declares its
currency bound, its evidence is not current and the claim renders Unknown."
Slice 5 is this rule made per-claim: at the current evaluation its honest
render is two Unknowns with routes for 414 of 415 items, and the missing
propagation becomes visible instead of absent. Slice 4b is this rule applied
to the label doctrine reserves for agents: an Inferred claim may never raise a
positive claim and must be excluded from every Observed denominator, and
absence of evidence still renders Unknown, never Inferred.

**VIS-3 — Human interpretability.** Lines 108–120 (corrected 2026-09-15 per
review 1, F19, from 108–121): "Every normative artifact —
spec, doctrine, contract — must remain digestible by a human unfamiliar with
the project." Slice 3 writes normative text and is therefore directly bound by
this; slice 2's state labels are a surface change and are argued from VIS-1's
rank-2 comprehension ordering instead, not from VIS-3 [Inferred — a reading of
VIS-3's scope, stated rather than resolved; the dossier tags VIS-3 for the
state labels without this qualification].

**VIS-4 — Humans steer the vision; agents shape within it.** Lines 122–139
(corrected 2026-09-15 per review 1, F19, from 122–140):
"Shape-defining deltas — heart-and-soul doctrine, craft-and-care standards,
topology, and RFC acceptance — require owner sign-off, every time; Syzygy and
its agents may draft them, never adopt them." This packet drafts and adopts
nothing. Slice 3 is drafted as a CC-REV-2 delta for the owner to sign or not.

**VIS-5 — Syzygy never writes code; direct writes are confined to two
namespaces.** Every implementation slice writes into `apps/**` or
`packages/**`, which the PWB continuation act names as "the same ordinary
implementation plane (`apps/**`, `packages/**`, tooling, root manifests;
never `openspec/**` or `.syzygy/**`)" (lines 112–113). Slice 3 writes into
`.syzygy/governance/contracts/candidates/`, which is the amendment-package
home, not an installed authority.

**VIS-7 — The observatory itself must be trustworthy.** Lines 183–193: "every
rendered internal project-entity link resolves to its identified target (the
normative link rule, exactly as stated in trust-and-evidence.md floor bullet
2); every encoding means what its legend says; no secret material appears in
any surface or store… *Violation:* a dangling internal link". Slice 1 adds
rendered internal project-entity links, so it takes on this obligation in
full — and the existing sweep cannot see the link shape it adds, which is why
slice 1's oracle is not optional. Slice 8 is the second limb: an encoding
whose name is one morpheme from a contract relation means something other than
what a reader joining by name will take it to mean.

**RFC2-24's closed twelve.** If slice 5's Unknown slots render a reason, that
reason must be one of RFC2-24's twelve verbatim — the project-shape model
already throws rather than mint one (`project-shape-model.ts` lines 142–148:
"anything else would be a minted reason, which RFC2-24 forbids — so it is a
thrown invariant, never a rendered word"). Slice 5 must reuse that closed set
or carry no reason at all; it may not invent "no work item names this claim"
as a twelfth-plus-one.

## Gate 3 — Topology

| Slice | Lives in | Governed artifact touched |
|---|---|---|
| 1 Cross-surface links | `apps/three-surface-poc/src/polaris.ts`, `trajectory.ts`, `orrery.ts`, `materialize-action.ts`, `page-shell.ts`; `polaris-reachability.test.ts`, `surface-routes.test.ts` | none |
| 2 State labels | `packages/three-surface-poc-core/src/model.ts` (`PocSurface` gains a state), `apps/three-surface-poc/src/routes.ts`, `page-shell.ts`, `polaris-copy.ts`, `polaris.ts`, `trajectory.ts`, `orrery.ts`; `cross-cutting.test.ts` | none |
| 3 The amendment package | a new directory under `.syzygy/governance/contracts/candidates/`, with a semantic delta, a manifest and `proposed/*.patch` files — **the signed spec is never edited in place** | **the six signed three-surface artifacts, by amendment only** |
| 4a Shape unification | `packages/three-surface-poc-core/src/model.ts`, `project-shape-model.ts`; `apps/three-surface-poc/src/exact-tables.ts`, `polaris.ts`, `routes.ts` | none |
| 4b The Inferred arm | `packages/cap1-core/src/epistemic.ts` (constructor and exclusion rules), `packages/three-surface-poc-core/src/model.ts`; `polaris-epistemic-tuples.test.ts` | none |
| 5 The tri-state ribbon | `apps/three-surface-poc/src/polaris.ts`, `polaris-copy.ts` | none |
| 6 One claim identity | `apps/three-surface-poc/src/trajectory.ts`, `orrery.ts`, `exact-tables.ts`, `routes.ts`, `materialize-action.ts`, and `packages/three-surface-poc-core/src/model.ts` for slice 6b, which makes the artifact identity the canonical join key and therefore has to carry that identity and its aliases on the model rather than derive it in three renderers [corrected 2026-09-15 per review 1, F10; superseded row omitted `model.ts`, contradicting this packet's own "slices 2, 4, 6 and 8 all change the shared model file" and the four-slice work-in-progress queue that rests on it. The Gate 3 row was the error; the queue stands] | none |
| 7 The observed band moves | `apps/three-surface-poc/src/polaris.ts`, `orrery.ts` | none |
| 8 RFC1-25 names | `packages/three-surface-poc-core/src/model.ts` (the `kind` union and a flag) | none |

Boundaries crossed: slice 3 only, and by the amendment path rather than by
editing. Every other file above is in the implementation plane.

Not touched by any slice: the project-shape observation pipeline
(`body-read-authority.ts` through `project-shape-model.ts`'s extraction and
coverage stages), which no slice reads differently; the walkthrough readiness
and judgment seams, which stay four distinct states; the verbatim route; the
source-route identity, which slice 6 *reads* as its join key and does not
change.

### The authorizing act, per slice

| Slice | Owner act needed | Named act and the limiting sentence |
|---|---|---|
| 1 Links | **No**, subject to Q6 | `THREE-SURFACE-POC-IMPROVEMENT-CYCLES-DIRECTION.md` lines 55–56: "Improvement-cycle work must trace to POC-REQ-001..061 or to a recorded review finding." Traces to L6-F2, a recorded finding. The limiting sentence is the same record's lines 46–54, which retain "one configured Butlers repository only; no production release, deployment, or broad remote access… the signed `three-surface-poc-experience` artifacts stay frozen at their act digests (spec changes route through CC-REV-2)". Slice 1 crosses none of those |
| 2 State labels | **No**, subject to Q6 | Same direction, same limb; traces to L6-F7 |
| 3 Amendment package | **Yes — a new owner act, by construction** | The sign-off act's line 39 routes any change to these bytes through CC-REV-2; the PWB implementation act adds "and a new owner act" at line 79 (the sentence carrying it begins at 78) [corrected 2026-09-15 per review 1, F15(3)]. Drafting the package needs no act; adopting it needs one |
| 4a Shape unification | **No on Q2's recommended arm; the amendment on its second arm** | Same improvement-cycles direction, tracing to L5-F4. On Q2's second arm this becomes conformance to PWB-REQ-007 under `PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md`, whose point 3 keeps scope "otherwise unchanged from 2026-09-02" (line 110) |
| 4b The Inferred arm | **Yes if Q4 is ruled the first way and the arm becomes constructible** — the label doctrine reserves for agents is a truth-posture change | Same direction; the escalation trigger reached is the PWB act's "any scope beyond the signed change" (line 93). A typed-but-unconstructible arm reaches no trigger |
| 5 The ribbon | **Yes — slice 3's act** | The ribbon renders a per-claim cross-surface state, which is precisely what no requirement names. It rides slice 3's adoption or it does not land |
| 6 One claim identity | **Yes — slice 3's act** for the join key; **no** for the attribute alone | Landing `data-claim-id` on Trajectory and Orrery with today's ids changes no truth. Making the artifact identity the canonical join key changes what an id *means*, which is slice 3's subject |
| 7 The band moves | **No** | Same improvement-cycles direction, tracing to L6-M7's own evidence. No requirement forbids it and PWB-REQ-020 parity is preserved by construction (below) |
| 8 RFC1-25 names | **Yes if Q3 is ruled the first way** | On the first reading the closure is a contract obligation the specification does not carry, so the requirement is slice 3's. On the second reading it is a naming convenience needing no act |

**What landing slices 4, 6 and 8 retires — and what is already retired.**
All three rewrite `packages/three-surface-poc-core/src/model.ts`, which is a
`subjects` digest row of
`docs/evidence/pwb-p3-8-reachability-mutation-run-2026-09-04.json` alongside
`apps/three-surface-poc/src/polaris.ts`. Checked this session: **neither
recorded digest equals its file's current bytes**, so that record's binding to
these exact bytes was already retired by the intervening work, and slices 4, 6
and 8 retire nothing that is still live there [Observed, `sha256sum` compared
against the record's own rows; neither value is reproduced here, per CG-15 —
the record is cited by path]. That is verification rule 10 working rather than
failing. No *act* binds any slice-touched implementation file. Two other
mutation-run records name `model.ts` as a mutation target without a digest row
(`docs/evidence/pwb-c5-readiness-verbatim-mutation-run-2026-09-05.json`,
`docs/evidence/pwb-c7-fresh-demo-readiness-mutation-run-2026-09-05.json`);
their mutants must still be re-run, because a mutant that no longer applies
scores as survived.

All eight slices run under `syzygy-dov.9`, the pursuit bead; no new POC bead
is filed by this packet.

## Gate 4 — Design sketch, per slice

### Slice 1 — The links whose addresses already exist (small; no act per Q6)

**The five links.** On Polaris: the `region:work-items` count links to
`/trajectory`; the `region:code-structure` count links to `/orrery`; each
reality-band entity links to `/orrery#<entityId>`. On Trajectory: the
materialize packet's governing intent links to
`/polaris#polaris-deep-dive-<capabilitySlug>`. On Orrery: each mapped
region's capability id links to its Polaris deep dive. Every href is built
through the existing `withMountPrefix` helper, the same one
`apps/three-surface-poc/src/page-shell.ts` line 20 already uses for the nav,
so the tailnet mount rewrites them for free.

**The oracle, and why the existing one will not do.** POC-REQ-053's oracle
reads, verbatim at spec lines 903–904: "**Oracle**: HTTP/anchor
resolution per enumerated element; zero dangling links over the exhausted
population decides." [corrected 2026-09-15 per review 1, F11; superseded
wording put the clause inside quotation marks as "resolution per
enumerated element over the exhausted population; zero dangling links over
the exhausted population decides" (spec lines 899–908), which dropped two
words and relocated a phrase with no elision mark.] Reuse it, but the sweep
must run over a *served* population, not a rendered string: the target lives
on a different page.
`surface-routes.test.ts` already stands up a real daemon and follows nav links
through both the direct and the tailnet-`Host` paths (its cases at lines 38
and 123), so the cross-surface sweep belongs there: enumerate every href
matching `^/(polaris|trajectory|orrery)(#|$)`, GET the target page, assert
the fragment resolves to exactly one `\sid="…"` on it, and report the
denominator.

**Rule-6 mutants.** (a) Point one cross-surface link at an id that exists on
no page; confirm the *existing* Polaris reachability sweep still passes —
establishing that it is blind — and that the new sweep fails naming the link.
(b) Remove `withMountPrefix` from one of the five; confirm the tailnet-`Host`
case fails while the direct case passes, so the mount limb is genuinely
tested. (c) Delete one link entirely; confirm the denominator drops and the
test fails on the count, not only on resolution — a sweep that only checks
what it finds cannot notice an absence.

**Byte cost.** Five link classes over the current population: 2 region counts
+ 9 reality-band entities on Polaris, 1 on Trajectory, 1 on Orrery = 13 links
at roughly 60–75 bytes of added markup each, plus 15 bytes per link under the
mount prefix. Under 2 KB on the largest page.

### Slice 2 — The three states named where they live (small; no act per Q6)

`PocSurface` gains `state: 'desired' | 'execution' | 'observed'`, set once in
the model beside the existing `question`. Each surface's eyebrow becomes
"Polaris · desired state · what this project is meant to be" and its two
siblings; the home page's three panels take the state name as a label above
the existing question string; the shared legend gains one line mapping the
three surface names to the three states. Roughly 500 bytes across four pages.

**Why the field and not four string literals.** Putting the state in
`PocSurface` means no surface can omit it and no surface can disagree with the
legend — the legend is generated from the same table. Four literals in four
renderers is the shape that lets one drift.

**Oracle.** In `cross-cutting.test.ts`, which already renders all four pages
from one fixture (its imports at lines 4–9): assert each of the four pages
names its own state exactly once and that the legend names all three. Match a
distinctive full phrase, never the bare word — `AGENTS.md` records that a
short label is "reached" by coincidence, and *desired* is exactly that kind of
word in a page that also contains the caveat sentence.

**Rule-6 mutants.** (a) Remove one surface's state from the model; the
per-page assertion fails. (b) Change the legend's spelling of one state; the
legend-to-page comparison fails. (c) Swap Trajectory's and Orrery's states;
each page's own assertion fails, proving the check is per surface and not a
page-wide substring.

### Slice 3 — One amendment package (medium; the owner act, per Q1)

A CC-REV-2 semantic delta against the three-surface-poc-experience
specification, drafted as a candidate package with `proposed/*.patch` files
and a manifest over the proposed bytes — never as an edit in place. Its
content, in one package because one join key is built and not two:

1. **POC-REQ-054 — one claim identity across surfaces.** Modelled on
   POC-REQ-053's oracle shape: enumerate every element on any surface that
   names a subject present on another, and resolve each. Declares the
   canonical join key. Names, in its coverage rows, the RFC6-1, RFC6-3 and
   RFC6-12 consequences it moves out of "Unknown pending owner-reviewed N/A".
2. **An amendment to POC-REQ-060** extending "SHALL encode epistemic states
   (Observed, Unknown, and their reasons) identically wherever they appear"
   (spec lines 931–934) to the *record shape*, not the encoding alone, and to
   all three labels rather than the two its text enumerates.
3. **POC-REQ-055 — the relation vocabulary is declared.** Every emitted kind
   is either an RFC1-25 name or carries an explicit out-of-vocabulary flag
   with a reason. This is the requirement `CONTRACT-COVERAGE.md` line 89
   points at POC-REQ-052 for and POC-REQ-052's text does not carry.
4. **A scenario for the ribbon** if slice 5 is to be lawful under RFC2-26 —
   see Gate 5.

**What it may not do.** It may not edit `CONTRACT-COVERAGE.md` line 89 to say
the mapping was wrong: that file's bytes are signed, and a superseding matrix
row belongs in the amendment's own proposed coverage, with the predecessor
row preserved. It may not restate a clause normatively — the matrix's
own head banner says "the clause text is the authority, and nothing here
restates a clause normatively"
(`openspec/changes/three-surface-poc-experience/CONTRACT-COVERAGE.md`
lines 7–8) [corrected 2026-09-15 per review 1, F15(5); superseded wording
attributed those bytes to CC-SPEC-8, whose own clause at
`.syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`
line 229 per `DIRECTIVE-REGISTER.md` line 129 carries the per-consequence
row unit and the applicability test, not that sentence].

**Oracle.** The package's own manifest `--check`, plus a fresh-context
independent review per CC-REV-6, plus the amendment tooling's both-location
probe that `AGENTS.md` records as a guardrail.

### Slice 4a — One epistemic record shape, no behaviour change (large; no act per Q2)

Replace `PocEpistemic` on `PocEntity.epistemic` and
`PocRelationship.epistemic` with the `ProjectShapeClaim` shape — `claimId`,
`evaluationId`, the cap1-core tuple, `resolutionRoutes`, `challenge`,
`support`. The existing `basis` prose becomes the claim's support and the
existing `reason` prose maps to a closed RFC2-24 reason plus its route; where
no closed reason fits, the migration stops rather than mints one, and that
stop is the finding.

**The acceptance bar is byte-identity.** `/api/poc` entity and relationship
tuples must be supersets of today's, and the four human pages must be
byte-identical before and after — because slice 4a is a shape change and not
a render change. If a page moves by one byte, either the renderer was reading
the shape or the migration changed a value; both are worth stopping for.

**Rule-6 mutants.** (a) Drop `tier` from one migrated entity; the conformance
expectation, a hard-coded literal, fails. (b) Map one Unknown reason to a
string outside RFC2-24's twelve; `closedReason` throws, and the test asserts
the throw rather than a rendered word. (c) Change one entity's `basis` text;
the byte-identity assertion fails, proving it is live.

### Slice 4b — The Inferred arm and its exclusion battery (large; act per Q4)

Add the third arm to the POC union and, on Q4's recommended answer, leave it
without a production constructor:

```
| { readonly label: 'Inferred'; readonly tier: 'asserted-by-worker';
    readonly assertedBy: { actor: string; runIdentity: string; at: string };
    readonly premises: readonly string[];
    readonly challenge: ChallengeState;
    readonly freshness: FreshnessState;
    readonly resolutionRoutes: readonly ResolutionRoute[] }
```

**Three invariants, each with its own counterexample.** An Inferred claim (i)
never appears in any Observed count, (ii) never clears an Unknown, (iii)
renders distinctly rather than as the same grey. The third needs slice 2's
legend line and the declared encoding table to carry it, or the claim renders
identically to an Observed one and the arm is a lie in CSS.

**Rule-6 mutants.** (a) Include one Inferred claim in an Observed denominator;
the exclusion assertion fails. (b) Construct an Inferred claim with an empty
`premises` list; the constructor refuses. (c) Render an Inferred claim with
the Observed encoding; the legend-to-encoding comparison in
`cross-cutting.test.ts` fails.

### Slice 5 — The per-claim tri-state ribbon (large; slice 3's act)

Beside each Polaris claim, three slots with the declared encoding: *desired*
(this claim, always Observed here), *execution* (the work items whose external
reference names this claim; Unknown with a named route when none), *observed*
(the code region or file the claim maps to; Unknown with a named route when
unmapped). Each populated slot links to the owning surface at the claim's own
fragment. Never a score, never a verdict, never a completeness percentage.

**Scale it from one, not to all.** Render the ribbon for the **one**
capability deep dive first — three slots, two of them Unknown with routes —
and put it in front of the owner before generalizing. Q5's measurement is why:
the break-even for a catalog-wide ribbon is 1,490 bytes per item against
618,515 bytes of headroom, and a ribbon that reuses the existing 586-byte
tuple markup three times over costs 1,758 and does not fit.

**Machine parity.** The same three slots in `/api/poc` per claim, with the
same Unknown reasons, or PWB-REQ-020 parity breaks. That parity is **per
tuple, not per id**: a claim may render more than once, so the check compares
every rendered tuple against its machine claim by id and compares both id
sets.

**Rule-6 mutants.** (a) Populate an execution slot from a work item that does
not name the claim; the join assertion fails. (b) Render an empty slot as
absent rather than Unknown; the VIS-2 assertion fails on the count of rendered
slots against three times the population. (c) Render the ribbon on the human
page only; the parity sweep fails on the machine side.

### Slice 6 — One claim identity, landed (medium; act for the key, not the attribute)

Two separable halves.

**(a) The attribute, no act.** Put `data-claim-id` on Trajectory work-item
cards and Orrery entity rows, carrying today's ids. Trajectory's **310**
rendered cards at roughly 40 bytes each [corrected 2026-09-15 per review 1,
F9;
superseded figure 299 was the `class="wi-card"` count of the private-daemon
Trajectory capture, which this packet's record does not name — 310 is the
count on `trajectory-7478.html`, the capture every other Trajectory figure
here comes from] is about 12 KB against 1.8 MB of headroom;
Orrery's nine rows are under 1 KB. Nothing's meaning changes; the attribute
that says "this element is that subject" simply becomes the same word on every
page, and the sweep in slice 1 gains a machine-checkable population.

**(b) The key, slice 3's act.** Make the artifact identity the source route
already mints — `repository:<repo>@<rev>:<path>#<objectId>` — the canonical
join key, so one artifact resolves to one string instead of a change id on
Polaris, a prose sentence on Trajectory and an entity id plus digest on
Orrery. Derive fragment ids from that identity, keeping the old ids as aliases
for one release so no link breaks.

**Rule-6 mutants.** (a) Give one Trajectory card the wrong claim id; the
cross-surface resolution sweep fails. (b) Remove the alias for one renamed
fragment id; the reachability sweep fails on a dangling link. (c) Mint a join
key from a path rather than the artifact identity; the oracle, which reads the
route table from the served source route and not from the renderer, fails on
the mismatch.

### Slice 7 — The observed band moves to the surface that owns it (medium; no act)

Replace the reality band's per-entity provenance dump with, per entity, its
title, its claim tuple and a link to `/orrery#<entityId>` — the exact-table
row that already renders the same facts. Keep the epistemic state on Polaris;
move the provenance list to Orrery, which already serves it through
`exactTablesSection`.

**Be honest about the size.** Measured above under one stated predicate:
the recoverable bytes are **5,843** (details and citations) or **11,523**
(also moving the relationship section), and the added claim tuples cost
5,278. The net is a saving of between **565** and **6,245** bytes [corrected
2026-09-15 per review 1, F8; superseded: "the recoverable bytes are 5,214
(details and citations) or 10,291 (also moving the relationship list) … The
net is between −64 and +5,013 bytes"]. This
is a coherence move — it removes the third markup vocabulary slice 6 would
otherwise have to reconcile — and **not** a ceiling answer. Anyone who lands
it expecting 12 KB back will be disappointed: the honest ceiling on the whole
move, relationship section included, is a net 6,245 bytes against 618,515 of
headroom.

**Rule-6 mutants.** (a) Drop one entity's claim tuple while keeping its link;
the per-tuple parity sweep fails. (b) Point one entity's link at Orrery's
relationship row rather than its entity row; the cross-surface resolution
sweep fails on the id mismatch. (c) Remove the provenance from Orrery as well
as Polaris; the PWB-REQ-020 parity sweep fails because the machine answer
still carries it.

### Slice 8 — RFC1-25's names, and a flag for the three outside (small; act per Q3)

Rename `materializes-as` → `materializes`, `verified-by` → `verifies`,
`governed-by` → `governs`, and give `mapped-to` its RFC1-25 counterpart —
`implements` or `covers`, per endpoint, since RFC1-25's rows type them
differently. The three with no counterpart — `changes`,
`satisfies-at-runtime`, `coverage-unknown` — keep their names and gain an
explicit `outsideClosedVocabulary: { reason: string }` rather than a
plausible-looking name. `PocRelationship.kind` narrows from `string` to a
union, so a new kind is a compile error rather than a silent addition.

**Directions matter and are not free.** `governed-by` reverses `governs`;
`verified-by` reverses `verifies`. Renaming without swapping the endpoints
produces an edge that is in the vocabulary and backwards, which is worse than
one that is out of it and honest. Each rename carries an endpoint swap and a
test that asserts the direction.

**Rule-6 mutants.** (a) Rename without swapping endpoints; the direction
assertion fails. (b) Add a ninth kind with no flag; the "every kind is in
RFC1-25's set or flagged" test fails, denominator reported. (c) Flag a kind
that *is* in RFC1-25's set; the same test fails from the other side.

### Design bar for the human surface

Slice 2's eyebrows and slice 5's ribbon are the only visible additions. Both
must carry their meaning in text, not position or colour: POC-REQ-061 requires
legends "whose text matches every visual encoding in use" (spec lines
972–973), and RFC7-34's recoverability rule is already the POC's bar. The
ribbon's three slots are a list with three labelled items, not a traffic
light. No fragment target may sit inside a `<details>` — `AGENTS.md` records
why.

## Gate 5 — Specification

The specification in force for the three surfaces is
`openspec/changes/three-surface-poc-experience/specs/three-surface-poc-experience/spec.md`
as signed 2026-08-30: **24 requirements and 24 scenarios**, counted this
session, one scenario per requirement. There is no amendment overlay for it;
`AGENTS.md`'s composition rule concerns the Polaris *generator* specification
and does not reach this one [Observed: `ls -d openspec/changes/*/` returns
**six** directories, of which `archive/` holds only a `README.md` and is
excluded;
none of the remaining five is a three-surface amendment. Corrected
2026-09-15 per review 1, F21, which found the exclusion unstated].

### Does the cross-surface identity need a delta? (Q1)

**Yes, and the reason is a silence rather than a prohibition.** Swept this
session over all 24 requirements: none names a link from one surface to
another, none names a shared identity, none constrains the relation
vocabulary by name, and POC-REQ-060 — the only cross-surface requirement —
governs *encoding*, not record shape, and enumerates only two of the three
labels. Its text (spec lines 931–934) reads, verbatim:

> The three surfaces SHALL draw from one declared set of design tokens, and
> SHALL encode epistemic states (Observed, Unknown, and their reasons)
> identically wherever they appear. Scope of quantification: every epistemic
> encoding across the three surfaces.

Its scenario, "Unknown looks the same everywhere" (lines 948–953), reads:

> - **WHEN** the same Unknown relationship appears on Polaris, Trajectory,
>   and Orrery
> - **THEN** all three render it with the declared Unknown encoding from the
>   shared token set

That scenario is the nearest thing the specification has to a cross-surface
identity requirement, and it presumes the sameness it does not require: it
says "the same Unknown relationship" without saying how a reader or a machine
establishes that two renderings are the same relationship. That is precisely
the gap slice 3 closes.

**And there is no deferral standing in the way.** The three RFC6 clauses the
dossier calls a deferral are Part B2 beliefs; the matrix's own preamble and
the signing act both say they render Unknown pending owner-reviewed N/A, never
covered. Adding POC-REQ-054 moves three consequences from Unknown to covered,
which is a strict improvement in the matrix's own terms, not a reopening of a
settled question.

### The RFC2-26 test, run over all eight slice rows

RFC-0002 is an accepted design contract in force (`PROJECT-STATUS.md` line
147, Wave A, act performed 2026-08-17). Its phase rule is quoted verbatim at
the defined clause,
`.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md` lines
196–221 per `DIRECTIVE-REGISTER.md` line 260, under the `###` heading
"Authority boundary at the OpenSpec seam (binding phase rule)" at line 194 —
**the whole clause, both paragraphs**, rewrapped only to this packet's column
bar:

> **RFC2-26.** This contract schedules nothing: **it is not a specification of
> record from which implementation work may be scheduled**. No implementation
> work for user-observable consequences of this contract — evaluation and
> snapshot displays, claim and challenge rendering, Unknown-reason and
> rendering-tier presentation, reconciliation-chain and gap surfaces, API
> answers over epistemic state — may be scheduled solely from this RFC. Before
> implementation, every observable consequence either maps to an approved
> OpenSpec requirement and scenario in the governance root's `openspec/**`
> plane, or carries a reviewed N/A judgment proving it purely structural with
> no independently testable behavior. **The reviewed N/A judgment's home and
> gate.** A reviewed N/A judgment is a recorded owner judgment homed in
> `decisions/` (RFC3-15), and the judgment is honored only through an
> effective owner act under RFC3-16(a), in state (1) or state (2), with that
> state rendered; absent or invalid acts map nothing and leave the consequence
> unmapped and Unknown, never covered (RFC3-16(a)'s effect rule; VIS-2).
>
> **Rows are per observable consequence, not per clause.** A clause with five
> observable consequences and one mapped requirement is not covered; the
> matrix discloses the consequences it enumerates for each clause, so a
> complete-looking matrix over under-enumerated consequences is a defect of
> the matrix. At surface specification a clause-to-requirement coverage matrix
> over RFC2-1..RFC2-26 is produced — **that matrix is review material, never
> authority**. This clause creates no OpenSpec content now (none may exist
> during bootstrap). This clause binds the whole RFC 0002 package, not this
> module alone. (Shape-parallel with RFC6-28, RFC7-38, RFC8-32, RFC9-52,
> RFC10-16, RFC11-12.)

**The denominator is eight**: the eight slice rows of Gate 3's act table
[Observed, counted this session over that table]. Every requirement and
scenario cited below was read at source this session.

| Slice | RFC2-26 consequence class | Approved requirement **and** scenario | Limb 1 |
|---|---|---|---|
| 1 Links | **None enumerated with confidence.** A link between two surfaces is navigation, not "claim and challenge rendering" or an "API answer over epistemic state"; but it is arguably part of a "reconciliation-chain and gap surface" once it carries a claim's identity [Inferred — this packet does not decide it] | **None.** No requirement names a cross-surface link. The nearest are POC-REQ-053 ("Every entity Orrery renders SHALL link to the same entity route the exact tables serve", line 894) with scenario "Spatial and exact agree" (lines 910–914), whose scope is "all interactive entity elements on the surface" — one surface, not two | **Requirement absent.** Put to the owner under RFC2-26 in Q6. This packet does not call slice 1 lawful or unlawful. Two repair routes: a requirement and scenario added through slice 3's delta, or the reviewed N/A route the clause itself names — which this packet reads as probably unreachable here, because an added link is independently testable and not "purely structural" [Inferred] |
| 2 State labels | **None enumerated.** Three words in four eyebrows and one legend line; nothing rendered about a claim, nothing queried | **None**, and the nearest, POC-REQ-060, is about encoding rather than naming | n/a on this packet's reading. The clause is not engaged. Q6 still governs, on the direction rather than on RFC2-26 |
| 3 Amendment package | **n/a.** Drafting specification text is not implementation work | n/a | n/a. The gate here is CC-REV-2 and a new owner act, not RFC2-26 |
| 4a Shape unification | "API answers over epistemic state" (the tuple *is* the epistemic state in the machine answer) | **POC-REQ-060**, line 927, scenario "Unknown looks the same everywhere", lines 948–953 — **and the fit is partial**: POC-REQ-060 requires identical *encoding*, and slice 4a changes the *record*. On Q2's second arm the closer requirement is **PWB-REQ-007**, line 439, scenario "Missing current evidence remains explicit Unknown", lines 470–474, whose THEN reads "its claim renders Unknown with the exact primary reason and route / **AND** its tier, freshness and evaluation identity remain visible" | **Requirement available, fit contested.** Which requirement applies is Q2; this packet rules neither. On Q2's recommended answer the mapping is POC-REQ-060 stretched beyond its text, which is why slice 3's amendment to it is in the package |
| 4b Inferred arm | "claim and challenge rendering"; "Unknown-reason and rendering-tier presentation" (`asserted-by-worker` is one of RFC2-25's six tiers) | **None.** POC-REQ-060's text enumerates "Observed, Unknown, and their reasons" and no requirement in the specification names Inferred at all [Observed, swept this session over all 24] | **Requirement absent.** Q4's first arm needs slice 3's amendment; Q4's second arm leaves the arm unconstructed and enumerates no consequence |
| 5 The ribbon | "claim and challenge rendering"; "reconciliation-chain and gap surfaces"; "API answers over epistemic state" — three of the six classes the clause lists | **None.** This is the clearest absence in the table: a per-claim three-state display is exactly a reconciliation-chain surface and no requirement names one | **Requirement absent.** Slice 5 rides slice 3's delta or it does not land. Stated plainly rather than argued around |
| 6a Identity attribute | **None enumerated.** A data attribute carrying an id the page already renders elsewhere changes no rendered claim | n/a | n/a on the attribute alone |
| 6b The join key | "API answers over epistemic state" (the key is what a machine consumer joins on) | **None**; POC-REQ-053's oracle is the *shape* to reuse, not a mapping | **Requirement absent.** Slice 3's POC-REQ-054 is the repair route |
| 7 The band moves | "claim and challenge rendering" (the provenance list is claim rendering, moved) | **POC-REQ-031**, "Every positive Polaris claim carries resolvable provenance", line 537, with its scenario — the requirement slice 7 must not break rather than the one it implements. Also **POC-REQ-053**, line 890, for the Orrery side of the link | **Available as a constraint, absent as a warrant.** Slice 7 is scheduled from a recorded finding under the improvement-cycles direction, and POC-REQ-031 is the bar it must still clear afterwards: "resolvable" must survive the move to a link |
| 8 RFC1-25 names | "claim and challenge rendering" if a kind is rendered; the kinds *are* rendered, in the exact tables (`exact-tables.ts` lines 28 and 41) | **POC-REQ-052**, line 851, scenario "No proximity-invented edges", lines 872–877 — **but read what it says**: "no legend-declared relationship encoding connects them, and every rendered edge resolves to a model relationship". That is anti-fabrication. Nothing in it constrains the *name* a held relationship is rendered under | **Requirement partial.** The coverage matrix claims otherwise at line 89; this packet reads that as an under-enumerated row, which RFC2-26's second paragraph calls "a defect of the matrix" — and the matrix is signed and may not be corrected at the site. Q3 puts the reading to the owner |

**What the test establishes and what it does not.** It establishes
[Observed] that **on Q2's recommended arm, no slice of M9 maps to an
approved requirement-and-scenario pair that names its consequence**; that
slice 4a's nearest requirement is a stretch of POC-REQ-060 on that reading
and PWB-REQ-007 on the other — and that on Q2's second arm slice 4a
*does* map, to PWB-REQ-007's text and its own scenario, so the blanket form
of the claim holds only on the recommended arm [qualified 2026-09-15 per
review 1, F12; superseded wording: "no slice of M9 maps to an approved
requirement-and-scenario pair that **squarely** names its consequence …
and a **squarely-fitting** PWB-REQ-007 on the other" — the same sentence
contradicted its own [Observed] label, and "squarely" is a judgment about
fit, not an observation. The per-row table carries the nuance]; that slices
4b, 5, 6b and 8 have no requirement at all; and that
slices 1, 2, 3, 6a and 7 enumerate either no RFC-0002 consequence or one this
packet declines to rule on. It does **not** establish that any slice is
lawful. That is Q1, Q3, Q4 and Q6's, and RFC2-26's own scope sentence — "This
clause binds the whole RFC 0002 package, not this module alone" (line 219;
corrected 2026-09-15 per review 1, F15(4), from 220) —
is a reading the owner may take more or less broadly than this packet has.

### New WHEN/THEN scenarios, for the beads' acceptance contract, not the spec

These are acceptance criteria for the implementing beads. They are **not**
proposed spec text; slice 3's package is where proposed spec text would live.

**S1 (slice 1).** WHEN a reader on Polaris follows the work-items region
count, THEN the response is Trajectory's page, AND the same link under a
tailnet `Host` header carries the mount prefix.

**S2 (slice 1).** WHEN any cross-surface link names a fragment, THEN that
fragment resolves to exactly one element on the target page, AND the sweep
reports its denominator and fails if the denominator shrinks.

**S3 (slice 2).** WHEN any of the four pages is served, THEN it names its own
state exactly once as a distinctive phrase, AND the legend names all three.

**S4 (slice 4a).** WHEN the shape migration lands, THEN every entity and
relationship tuple in the machine answer is a superset of its predecessor,
AND all four human pages are byte-identical to their pre-migration bytes.

**S5 (slice 4b).** WHEN an Inferred claim exists, THEN it appears in no
Observed denominator and clears no Unknown, AND it renders with an encoding
the legend distinguishes from Observed.

**S6 (slice 5).** WHEN a claim has no work item naming it and no mapped code
region, THEN its ribbon renders two Unknown slots each with a route, AND
neither slot is absent, blank, or styled as Observed.

**S7 (slice 5).** WHEN the ribbon renders on the human page, THEN the machine
answer carries the same three slots for the same claim id, AND the parity
check compares every rendered tuple against its machine claim by id and both
id sets, never tuple count against distinct-id count.

**S8 (slice 6).** WHEN a subject appears on two surfaces, THEN both carry the
same `data-claim-id` value, AND a sweep over the union of the four pages
reports how many subjects appear on more than one surface as its denominator.

**S9 (slice 7).** WHEN the reality band renders after the move, THEN every
entity still carries a resolvable provenance route, AND the byte delta is
recorded in the bead against the measurements in this packet.

**S10 (slice 8).** WHEN a relationship kind is emitted, THEN it is either one
of RFC1-25's thirty relation tokens or carries `outsideClosedVocabulary` with
a reason, AND the test reports eight as its denominator.

## Collision and sequencing

**Two predicates, both reported, because they disagree.** Predicate A: every
code span in the sibling packet that names an implementation-plane path
(`apps/`, `packages/`, `scripts/`, `docs/polaris-generation/`, or
`package.json`) and resolves to a file in that sibling's own worktree.
Predicate B: the same, restricted to the sibling's "Gate 3 — Topology"
section — that is, the files each sibling *proposes touching* rather than
merely cites. Both are intersected with M9's **eleven-file** candidate
surface, listed in Gate 3 [corrected 2026-09-15 per review 1, F5, from
"ten-file":
`apps/three-surface-poc/src/exact-tables.ts` appears in Gate 3's slice 4a and
slice 6 rows and was missing from the intersection surface. Gate 3 names
eleven distinct implementation files and four test files; the four test files
remain out of the surface, which is the packet's stated choice. The omission
was not neutral — `exact-tables.ts` is where `data-entity-id` is emitted
today, so it is the file slice 6a needs]. Fenced code blocks are stripped
before extraction.

| Sibling | Head read this session | A: resolving spans | A ∩ M9 | B: Gate-3 spans | B ∩ M9 |
|---|---|---:|---:|---:|---:|
| M1 (lane A, on main) | `a9f671e` | 1 | 1 | 0 | **0** |
| M2, PR #36, P-69 | `f2f37dd` | 11 | 4 | 7 | **4** |
| M3, PR #37, P-70 | `6574600` | 13 | 4 | 9 | **2** |
| M4, PR #38, P-71 | `63b8e33` | 22 | **9** | 13 | **8** |
| M5, PR #39, P-72 | `ba9ca61` | 9 | 3 | 5 | **3** |
| M6, PR #40, P-73 | `83c9f60` | 13 | 0 | 9 | **0** |
| lane B, PR #35, P-68 | `4090f98` | 1 | 0 | n/a | **0** |

**M9 is the collision-heavy packet, and pretending otherwise would be the
useful lie.** M6's sibling intersections were zero across the board; M9's are
not. Under predicate B:

- **M4 (P-71) shares eight of M9's eleven files**: `polaris.ts`,
  `routes.ts`, `trajectory.ts`, `orrery.ts`, `polaris-copy.ts`,
  `exact-tables.ts`, `model.ts` and `project-shape-model.ts`. That is M9's
  entire surface bar `page-shell.ts`, `materialize-action.ts` and
  `epistemic.ts` — the residue sentence was exactly right and the count was
  one low [corrected 2026-09-15 per review 1, F5, from "seven of M9's ten
  files"; recomputed at `63b8e33` this session, A 22 / A ∩ 9 / B 13 /
  B ∩ 8 on the eleven-file surface]. `exact-tables.ts` is the added
  intersection and the one most likely to bite, because slice 6a needs it.
- **M2 (P-69) shares four**: `polaris-copy.ts`, `routes.ts`, `model.ts`,
  `project-shape-model.ts`. It does **not** touch `polaris.ts` — the string
  `apps/three-surface-poc/src/polaris.ts` occurs **0** times in its whole
  packet [Observed, counted this session]. The dossier-level framing that M2,
  M3 and M4 "each touch `apps/three-surface-poc/src/polaris.ts` and the
  legend" is right about the legend for all three and right about
  `polaris.ts` for M3 and M4 only.
- **M3 (P-70) shares two**: `polaris.ts` and `polaris-copy.ts`.
- **M5 (P-72) shares three**: `polaris.ts`, `routes.ts`, `model.ts`.
- **M6 and lane B share nothing** with M9's surface.

**The exact collisions, named.**

1. `apps/three-surface-poc/src/polaris-copy.ts` — the legend — is claimed by
   M2, M3, M4 and M9's slice 2. Four packets proposing legend lines is one
   legend rewritten four times or once. **M9's slice 2 takes its legend line
   last**, after whichever of the three lands, and the line is additive.
2. `packages/three-surface-poc-core/src/model.ts` is claimed by M2, M4, M5,
   **M8** and M9's slices 2, 4, 6 and 8. This is the POC shared model, and
   the 2026-08-29 direction's work-in-progress limit of **one** for
   shared-model changes applies across packets, not only within one.
   **M9's four model-touching slices queue behind M2, M4, M5 and M8's model
   work and behind each other** [M8 added 2026-09-15 per review 1, F2; its
   Gate 3 slice 7 row names the shared model and a new seed module beside
   it, read read-only in `m8wt` at `4b2e8cb`].
3. `apps/three-surface-poc/src/polaris.ts` is claimed by M3, M4, M5 and M9's
   slices 1, 5 and 7. It is a 1,200-line renderer; three packets editing it
   concurrently is a merge problem, not a governance one, but it is the
   reason slice 5 should not be attempted before M4 lands.
4. `.syzygy/governance/contracts/candidates/` — **lane B's PWB manifest is
   the one collision that is not about files at all.** Lane B's manifest binds
   all eleven PWB artifacts and declares that all rows take effect together or
   none do. On Q1's second arm M9's slice 3 would propose different bytes for
   the same `specs/polaris-project-wide-butlers-model/spec.md`, and the two
   packages become mutually exclusive: adopting either retires the other's
   manifest. On Q1's recommended arm — a three-surface-only delta — there is
   **no** intersection, because the six signed three-surface artifacts appear
   in no row of lane B's manifest [Observed, the manifest's eleven rows read
   this session; the digests are not reproduced here].

**The shared governance file.** All six sibling packets add a row to
`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`: P-68 (lane B),
P-69 (M2), P-70 (M3), P-71 (M4), P-72 (M5), P-73 (M6), each present only in
its own worktree's register [Observed, counted this session with the
predicate `^\| P-` over the seven registers; the M9 worktree's register ends
at P-53 and carries none of the six — superseded 2026-09-15: M8's register
now carries P-74 and this one carries P-75, and the sibling count that the
sentence above states as six is the count of registers carrying a row at the
first draft, not today]. **This packet registers as P-75**, added on this
branch in the same pass as these review-1 repairs, which is the sequence the
sibling packets settled on
[assigned 2026-09-15; superseded forecast: "This packet writes no register
row: M9's six questions would register as P-74 after review 1". Review 1, F16
was right that a literal forecast was unsafe — M8 took P-74 at its own
close-out, and M7's row will land after its own review. Recounted this
session with the predicate `^| P-` over each worktree's register: `laneb`
P-68, `m2wt` P-69, `m3wt` P-70, `m4wt` P-71, `m5wt` P-72, `m6wt` P-73,
`m8wt` P-74, `m7wt` none beyond P-53].

**The two other P2 packets drafted in parallel with this one — M7 and M8 —
are not disjoint from M9, and M8 is the second-heaviest collision in this
table.** [Corrected 2026-09-15 per review 1, F2; superseded wording: "They
are disjoint from M9 by design, on the orchestrator's assignment; M9's
surface is the four rendered pages, the shared POC model and the cap1-core
epistemic tuple, and any overlap would show up as a conflict at merge
rather than as a governance collision." That was an unlabelled substantive
claim and the sibling worktrees falsify it.] Recomputed this session under
the same predicates and the eleven-file surface, reading each sibling
read-only at the head named:

| Sibling | Head read this session | B: Gate-3 spans | B ∩ M9 |
|---|---|---:|---:|
| M7 (`m7wt`) | `0c4b4a9` | 11 | **1** |
| M8 (`m8wt`) | `4b2e8cb` | 20 | **7** |

M7's one is `apps/three-surface-poc/src/routes.ts`. M8's seven are
`apps/three-surface-poc/src/orrery.ts`, `polaris-copy.ts`, `polaris.ts`,
`routes.ts`, `trajectory.ts`,
`packages/three-surface-poc-core/src/model.ts` and `project-shape-model.ts`
— a larger intersection than every sibling except M4, and it includes the
POC shared model [Observed, both recomputed this session]. At `8035c8f`,
the head review 1 read, M8's figures were 19 and **6** (without
`project-shape-model.ts`); M8's own review-1 close-out moved them to 20 and
7, so the collision grew rather than shrank [Observed, both revisions
measured this session by `git show` into the same predicate].

**Question-level collisions, which intersecting files does not catch.**
[Added 2026-09-15 per review 1, F18.] Four sibling owner questions sit over
clauses or rules M9's own questions presuppose. Each is quoted by
identifier and subject only; **none is re-asked here**, and this packet
rules none of them.

| Sibling question | Subject | Which M9 question presupposes it |
|---|---|---|
| **M3 Q1** (`m3wt` at `6574600`) | whether POC-REQ-060's "epistemic encoding" reaches only the two declared badge spans, or Polaris's present rendering is a non-conformance | M9's **slice 3** proposes amending POC-REQ-060 to reach the *record shape*; the amendment presupposes an answer on the same clause. Named in **Q1** |
| **M2 Q1** (`m2wt` at `f2f37dd`) | whether the PWB model's "the evaluation itself is the currency" argument satisfies RFC2-9, or each claim class must declare a currency bound | over PWB-REQ-007's currency limb, the same requirement M9's **Q2** reads for *scope*. Three open questions now sit over one requirement |
| **M2 Q6** (`m2wt` at `f2f37dd`) | sequencing M2's spec work against lane B's package, which "rewrites the same clause region of PWB-REQ-007" | the same sequencing M9's **Q1** recommends for its own delta |
| **M8 Q7** (`m8wt` at `4b2e8cb`) | whether rewriting the shared `PocModel` type triggers the owner's improvement-cycle ceremony — work-in-progress one, review → repair → confirm → owner report | M9's **Q6** puts the same direction's second limb to the owner, and M9's stated slice ordering rests on the same work-in-progress rule |

**M8 Q7 and M9 Q6 are overlapping ceremony questions and should be ruled
together.** They differ in what they ask: M8 Q7 asks whether one
shared-model rewrite triggers the full cycle ceremony; M9 Q6 asks whether
the pursuit that produced both packets is a continuation of an open cycle
or a new one owing a report first. M9 proposes that the owner answer Q6
first — it is the wider question, and its answer sets whether any cycle
report is owed at all — and then read M8 Q7 as the per-change application
of the same rule. If Q6 is answered as recommended (a continuation), M8 Q7
is a work-in-progress-slot question rather than a report question; if Q6 is
answered the other way, both packets' shared-model work waits on the same
report [Inferred — a sequencing proposal, not a ruling; M8's question is
not re-asked here and stands as its own row P-74 on `agent/syzygy-dov.8`].

**Sequencing inside M9.** Slice 1 is independent of everything and may land
first. Slice 2 is independent of slice 1 and is the first of the four
model-touching slices, so it takes the shared-model slot first. Slice 3 gates
slices 5, 6b and 8 and, on Q2's second arm, slice 4 as well. Slice 6a is
independent and may land any time. Slice 4a must precede 4b. Slice 7 depends
on slice 1's Polaris → Orrery entity links landing first, because it replaces
a provenance list with one of them. Slice 5 is last: it is the largest, the
most gated, and the only one whose byte cost can breach the ceiling.

**Not verifiable this session.** [Unknown] Whether the sibling branches'
actual diffs stay inside the paths their Gate 3 sections name, until they
land. [Unknown] Which arm the owner takes on Q1, and therefore whether lane B
and M9's delta are compatible. [Unknown] Whether the P-60/P-61 Butlers repairs
land before or after any byte-adding M9 slice, and therefore what headroom is
actually available at the time. [Unknown] Whether M7's and M8's branches will
still name the paths their Gate 3 sections name when they land — their
intersections are measured above at the heads named there, not forecast
[superseded 2026-09-15 per review 1, F2: "[Unknown] The content of the two
parallel P2 packets", which is no longer true — both were read read-only this
session].

## Gate 6 — Engineering bar

1. **Every count in this packet carries its predicate and its denominator**,
   and every one was taken this session — in the worktree at `a9f671e` for
   source figures, and over the named retained captures for served figures,
   each named to the evaluation it was actually served from, per the
   provenance table in the href-census section [rewritten 2026-09-15 per
   review 1, F1; superseded wording ended "with the capture's own
   provenance stated", which was false for two of the five files, and per
   review 1, F8, two of the four reality-band part rows carried no stated
   predicate at all — both repaired at their sites].
2. **Two methods for the load-bearing zeros.** "Zero claim-level cross-surface
   links" is established both by the href classification and by the
   independent observation that all sixteen surface-root hrefs sit inside the
   single `site-nav` block each page emits, which the renderer confirms at
   `page-shell.ts` line 23. "Zero `Inferred` in production modules" is
   established by a whole-word sweep with its file denominators and by reading
   the only two claim constructors at source.
3. **A false finding was caught by the second method and is recorded, not
   hidden** — the duplicate-id artefact in "Decided in this packet" above.
   Verification rule 1: `\b` before `id="` matches inside
   `data-entity-id="`. No claim here rests on it.
4. **Rule-6 mutants are specified per slice and per guard branch**, three
   apiece, each naming the predicate to mutate and the check that must then
   fail. Slice 1's mutant (a) is the important one: it asserts that the
   *existing* sweep passes, which is how a blind check is proved blind rather
   than assumed sound.
5. **Conformance expected values are literals in the tests**, never imported
   from the module under test.
6. **The copy-oracle caution is applied.** Slice 2's assertion matches a
   distinctive full phrase, because *desired* is a short word that already
   occurs once on the home page in a different role — a substring check would
   pass on the caveat sentence and prove nothing.
7. **The parity caution is applied.** Slice 5's and slice 7's checks compare
   every rendered tuple against its machine claim by id and compare both id
   sets; `tuples === distinct ids` is a false invariant on this page, as the
   699-against-689 and 713-against-703 measurements above show directly.
8. **No act-bound byte is proposed for edit.** The six signed three-surface
   artifacts and the eleven signed PWB artifacts were each checked against
   Gate 3's slice-touched paths; the intersection is empty. Slice 3 changes
   signed bytes only through the CC-REV-2 amendment path, which is the route
   both sign-off acts name. Three slice-touched implementation files are
   digest rows of evidence records rather than acts; Gate 3 records the
   re-run obligation.
9. **No observed-repository path is backticked** anywhere in this file, and no
   act argument, manifest digest or signed digest is reproduced — the four
   digest-bearing records consulted are cited by path, per CG-7e and CG-15.
10. **Independent review.** This packet has had **one**, verdict **REVISE**,
    retained verbatim and dispositioned in "Review 1 and repairs
    (2026-09-15)" below [superseded 2026-09-15: "This packet has had
    **none**. It is a first draft."]. Verification rule 10: review 1 binds
    the bytes it names and not these, so **these repairs are uncovered
    until a second fresh-context review confirms them**, and each raw is
    its own `-RAW.md` file, never an overwrite.
11. **Conventions this packet was checked against, this session**, over its
    final bytes. **The line convention, stated once:** a line is a
    newline-separated segment of the file as split on `\n`, and the empty
    segment after a trailing newline is not counted; "non-fence" excludes
    every line inside a fenced block and the fence lines themselves. Every
    non-fence line has an even backtick count, so no code span is broken
    across a line break: **0** of the non-fence lines, over the denominator
    re-derived in the review-1 section below [convention added
    2026-09-15 per review 1, F19, which reproduced 1,205 under the strict
    count and 1,206 with the trailing segment; the denominator is re-derived
    for the current bytes rather than carried forward, because the first
    draft's 1,206 is not true of a file this pass has rewritten].
    The over-78-column count outside tables, block quotes, headings and
    fences is likewise re-derived for the current bytes and reported in the
    review-1 section below, each such line being a single unbreakable
    code-span path. Of **295** distinct code spans, **68** contain a `/` and
    **22** of those do not resolve as a path in this worktree; each is
    enumerated and none is a path to a file that should exist here [recounted
    2026-09-15 over the repaired bytes; superseded first-draft figures: 233
    distinct spans, 19 non-resolving. The three additions are
    `agent/syzygy-dov.8`, `archive/` and the directory-listing command that
    finding F21 required]: five write-root or package globs (`.syzygy/**`,
    `openspec/**`, `apps/**`, `packages/**`, `proposed/*.patch`), seven served
    route strings and fragment forms (`/polaris`, `/trajectory`, `/orrery`,
    `/api/poc`, `/polaris/source`, `/orrery#<entityId>`,
    `/polaris#polaris-deep-dive-<capabilitySlug>`), one further route example
    (`/orrery#capability:whatsapp-transport-identity`), three regular
    expressions (`/\shref="#([^"]+)"/g`, `^/(polaris|trajectory|orrery)#`,
    `^/(polaris|trajectory|orrery)(#|$)`), two branch names
    (`agent/syzygy-dov.9`, `agent/syzygy-dov.8`), RFC2-26's own bare
    `decisions/`, one directory named relative to its parent (`archive/`, a
    child of `openspec/changes/`), one shell command
    (`ls -d openspec/changes/*/`), and one path written relative to its change
    directory (`specs/polaris-project-wide-butlers-model/spec.md`), which is
    given in full elsewhere in this file. Lane B's amendment manifest is named
    without a code span because it exists only on lane B's branch. The
    retained capture files are named by bare filename, as the first draft
    names them, so no scratchpad path is written as a code span.
12. **`scripts/check_governance.py` was run in this worktree** after both
    files were written; its last line is recorded in the evidence record and
    reported with this packet.

## Review 1 and repairs (2026-09-15)

An independent fresh-context review of this packet (read-only; only the
artifact, its governing references and the acceptance criteria) is retained
verbatim at `docs/reviews/R-POLARIS-M9-ONE-IDENTITY-FUNNEL-RAW.md` (42309
bytes, sha256
`fa280ab0544e8211ed9c8a38982ad073735590e3d61750398e65a795dd67b82e`, computed
by `wc -c` and `sha256sum` this session, never transcribed). It reviewed this
packet at 93626 bytes, sha256
`ae0ec92c4c7f858e85160704b799c21c39b34e86cb9fe7d2b685169e21c09e26`, and the
evidence record at 30164 bytes, sha256
`38ef8d5ef25a550a8d511d5fcbe9954ffdf96e4662d942bbb0b0d647dd5be54a`, both
tracked at commit `206d775` (measured here by `git show 206d775:<path>` piped
to `wc -c` and `sha256sum`). Its verdict word, copied exactly: **REVISE**.
Counts as the raw states them: **2 blocking, 16 non-blocking, 3 editorial**,
numbered F1-F21.

**Its six-question table, in one line:** scope truthful for Q1, Q2, Q3, Q5
and Q6 and **partly** for Q4; a genuine human gate for Q1, Q2, Q3 and Q6,
**only on one limb** for Q4 and **borderline** for Q5; the recommendation
follows from the evidence for all six; all lawful arms named for Q2, Q4, Q5
and Q6 and **not** for Q1 and Q3.

Every one of the twenty-one findings was re-derived against source before
being applied — none was assumed correct. The five capture files' embedded
evaluation blocks were read directly and the capture directory's own retained
run script and daemon log with them; the epistemic census was recomputed in
full over *both* retained `api-poc.json` files; the M7 and M8 intersections
were recomputed under this packet's own predicate B at each sibling's current
head and, for M8, at the head review 1 read as well; the attribute-name union,
the `wi-card` counts on both Trajectory captures, the four reality-band parts
on both Polaris captures, the RFC1-25 set difference, the nine relationships,
the register rows across nine worktrees, the `openspec/changes/` directory
listing and every one of the five miscited clauses were each re-run or re-read
at source. Every edit in this pass was made after that review, so by
verification rule 10 the review binds the bytes it names and not these:
**these repairs are uncovered until a second fresh-context review confirms
them**, and its raw would be a second `-RAW.md` file, never an overwrite.
Superseded wording is marked in place and dated, never deleted.

| Finding | Severity | Disposition |
|---|---|---|
| F1 the four-page capture's stated provenance is false for two of its five files | blocking | **CONFIRMED.** Read this session out of the files themselves: `polaris-7478.html` carries Butlers `66ed58f` / observer `a121591` and as-of 2026-09-10T01:50:48.470Z; `home.html` and `api-poc.json` carry Butlers `7c8743f` / observer `f4589e2` and as-of 2026-09-13T02:03:33.040Z; `trajectory-7478.html` and `orrery-7478.html` embed no snapshot label at all. The retained run script and daemon log show the private daemon on `127.0.0.1:41215` at the `7c8743f` revision, and the same run's Polaris output is an 838-byte `response-limit-breached` body. **The arithmetic does not move:** the whole census recomputed over both retained `api-poc.json` files agrees in every cell — 1,167 / 1,137 with tier / 30 without / 18 of them the nine entities and nine relationships; Observed 1,146, Unknown 21, Inferred 0; tier `report-fact` 1,137 and 0 of the other five; freshness `fresh` 1,149 and 0 of the other three; challenge `unchallenged` 1,149; Unknown primary reason `excluded-content` 12 and 0 of the other eleven. A provenance table now names each file's daemon, evaluation and as-of at the href census, with Trajectory's and Orrery's labelled [Unknown] from the bytes and [Inferred] from the log; the packet says which figures depend on which evaluation; Gate 6 bullet 1 is narrowed; the record's `captures_used` is marked false in place and corrected keys appended |
| F2 the disjointness claim about M7 and M8 is false | blocking | **CONFIRMED**, and larger than the review measured. Recomputed under predicate B on the eleven-file surface: M7 at `0c4b4a9` 11 Gate-3 spans, **1** shared (`routes.ts`); M8 at `4b2e8cb` 20 spans, **7** shared, including `model.ts` and `project-shape-model.ts`. At `8035c8f`, the head review 1 read, M8 was 19 and **6** — M8's own close-out grew the collision. The disjointness assertion is replaced by the measured rows with the superseded sentence kept and dated; M8 is added to collision item 2's shared-model queue; and a question-level collision table now discloses M8 Q7 against M9 Q6, with a stated proposal that the owner rule Q6 first as the wider question and read M8 Q7 as its per-change application. M8's question is not re-asked |
| F3 two ceiling rows are 7478-daemon measurements and the pre-lane-A Polaris observations are omitted | non-blocking | **CONFIRMED.** `polaris-7478.html` is **2,090,025** bytes — 7,127 under the ceiling — and the same directory's `polaris.html` is a 503 body recording `observed` **2,132,656** against `declared` **2,097,152** at Butlers `7c8743f`. Both recomputed this session, read-only; no daemon was started. The ceiling table gains a daemon-and-evaluation column and both rows, and the packet now says the 618,515 headroom is one evaluation's figure |
| F4 the attribute-name union is eleven, not ten | non-blocking | **CONFIRMED.** Recomputed over the four captures with the nine `model.entities` ids as the denominator: home 3, Polaris 8, Orrery 2, Trajectory 0; union **11**, because Orrery's two (`id`, `data-entity-id`) are already home's. Corrected in Gate 1, in the funnel summary and in the record |
| F5 the collision surface omits `exact-tables.ts`, and M4 shares eight | non-blocking | **CONFIRMED.** Gate 3 names **eleven** distinct implementation files (plus four test files, deliberately out of the surface); `apps/three-surface-poc/src/exact-tables.ts` is in the slice 4a and slice 6 rows. Recomputed at `63b8e33`: M4 A 22 / A ∩ **9** / B 13 / B ∩ **8**. Every other sibling row is unchanged under the wider surface, re-run this session. The surface, the M4 bullet, the table cell and the record are all corrected |
| F6 four quotations are attributed to the dossier and occur only in the machine records | non-blocking | **CONFIRMED.** `grep -rn -F` over every tracked file under `docs/`, `.syzygy/` and `openspec/`: all four strings occur in `docs/pursuits/2026-09-13-vision-pursuit-data.json` **and** its `-harvest.json` twin (and in this packet and its record), and **0** times in `docs/pursuits/2026-09-13-vision-pursuit.md`. The pursuit *record set* is defined at the head, each quotation is cited to the JSON record and line, and the dossier is not edited |
| F7 the enumeration omits four RFC1-25 tokens, not one | non-blocking | **CONFIRMED.** Set difference computed this session: RFC1-25's table (header 494, last data row 521) carries 26 data rows and **30** backticked first-column tokens; the enumeration at `docs/pursuits/2026-09-13-vision-pursuit-data.json` line 4360 lists 25 comma-separated entries covering 26 tokens; the omissions are `calls`, `exposes`, `accesses(mode)` and `succeeds`. Restated with the set difference as the predicate. The 1-of-8 intersection is unaffected and re-derives |
| F8 two of the four band part rows carry no predicate and the four use inconsistent conventions | non-blocking | **CONFIRMED** to the byte. Re-measured on both Polaris captures under one predicate — delete the element, its own tags included: band 14,820; 11 headings 2,130; 9 detail spans **1,534** (905 inner text); 9 citation spans 4,309; relationship **section** **5,680** (5,077 for the inner `<ul>`). Recoveries restated at **5,843** and **11,523**, 1.3% and 2.6% of the P-63 trim, and slice 7's derived net restated as a saving of **565** to **6,245** bytes. The conclusion is unchanged: no reliable byte dividend |
| F9 slice 6a's 299 comes from a capture the record does not name | non-blocking | **CONFIRMED.** `class="wi-card"` counted this session: **310** in `trajectory-7478.html`, 299 in `trajectory.html`. Corrected to 310, the figure from the named capture, which is where every other Trajectory figure in this packet comes from |
| F10 slice 6's model.ts membership is self-contradictory | non-blocking | **CONFIRMED**, and resolved the way the review reads it. Slice 6b makes the artifact identity the canonical join key and derives fragment ids from it while keeping the old ids as aliases — an identity and an alias list that have to live on the model rather than be re-derived in three renderers. Gate 3's slice 6 row was the error; `model.ts` is added to it with the superseded omission marked, and the four-slice work-in-progress queue stands |
| F11 POC-REQ-053's oracle is quoted inside quotation marks and is not verbatim | non-blocking | **CONFIRMED.** The clause sits at spec lines **903-904** and reads "**Oracle**: HTTP/anchor resolution per enumerated element; zero dangling links over the exhausted population decides." Quoted as written, at its own lines, with the superseded paraphrase kept and marked |
| F12 an [Observed] label on a claim the same sentence contradicts | non-blocking | **CONFIRMED.** The blanket claim is qualified to Q2's recommended arm, "squarely" is dropped from the [Observed] clause, and the sentence now says plainly that on Q2's second arm slice 4a does map. Mirrored in the funnel summary |
| F13 Q4's framing overstates the gate | non-blocking | **CONFIRMED.** Gate 3's act row already says "A typed-but-unconstructible arm reaches no trigger", so on the recommended arm Q4 is a typing decision inside the implementation plane. Q4 is recast as "If and when an agent asserts something, may the POC construct `Inferred`?", the recommended arm is stated to proceed under the improvement-cycles direction without a new act, and Q4 stays in the batch as a put question. **Q4's recommended answer did not change** — it is still "add the arm as a typed landing zone with no production constructor" |
| F14 a lawful arm is named once and then dropped | non-blocking | **CONFIRMED.** RFC2-26's reviewed-N/A route is added as a third lawful arm of Q1, and of Q3 where it reaches slice 8, quoted at its own lines (the route at line 201, its home and gate at line 206) with per-slice reachability stated as this packet's reading and labelled [Inferred]: slice 6a reachable, slice 8 arguable and put rather than assumed, the other seven not reachable because each adds independently testable behaviour. **Q1's recommended answer did not change** — it is still one package against the three-surface specification alone; the arm is added to the arms the owner may take, which is what the question asks |
| F15 five citation slips | non-blocking | **CONFIRMED**, all five, each checked at source this session. (1) `.syzygy/governance/doctrine/trust-and-evidence.md` line 16, now quoted verbatim in Q4. (2) Q6's two quotations split: line 41 for the report sentence, line 36 for "derived only from recorded findings". (3) The PWB implementation act's "and a new owner act" begins at line **79**; the sentence carrying it begins at 78. (4) RFC2-26's scope sentence begins at line **219**. (5) The "clause text is the authority" sentence is `CONTRACT-COVERAGE.md`'s own head banner at lines 7-8, not CC-SPEC-8's text — CC-SPEC-8 is at `SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` line 229 per `DIRECTIVE-REGISTER.md` line 129 and carries the per-consequence row unit and the applicability test instead. Cited as the matrix's own banner |
| F16 the P-number forecast overlooks two peers | non-blocking | **CONFIRMED**, and the assignment is now settled rather than forecast. Recounted this session with the predicate `^\| P-` over each worktree's register: `laneb` P-68, `m2wt` P-69, `m3wt` P-70, `m4wt` P-71, `m5wt` P-72, `m6wt` P-73, **`m8wt` P-74** (taken at its own review-1 close-out), `m7wt` none beyond P-53. **This packet registers as P-75**; both sentences are corrected and the superseded forecast kept and dated |
| F17 an unmarked elision in the home-page caveat | non-blocking | **CONFIRMED.** `apps/three-surface-poc/src/routes.ts` line 80 continues "Merge is not verification. Missing evidence is rendered Unknown." The line is now quoted whole |
| F18 the collision section intersects files and never questions | non-blocking | **CONFIRMED.** A question-level collision table is added naming M3 Q1 (POC-REQ-060's reach), M2 Q1 and Q6 (PWB-REQ-007's currency limb and its sequencing against lane B), and M8 Q7 (shared-model ceremony), each read read-only in its own worktree at the head named, with the M9 question that presupposes it. None is re-asked and none is ruled here |
| F19 two clause extents overrun by one line; the 1,206 denominator is convention-dependent | editorial | **CONFIRMED.** VIS-3 ends at line **120** and VIS-4 at **139**, both read at source; corrected. The line convention is now stated once (split on `\n`, trailing empty segment not counted, fence lines and fenced content excluded) and the non-fence denominator is re-derived for the current bytes rather than carried forward |
| F20 the intent-to-runtime chain holds four edges, not five | editorial | **CONFIRMED.** All nine relationships read from the machine capture this session: the chain is `materializes-as`, `changes`, `verified-by`, `satisfies-at-runtime`; the fifth Unknown relationship is `coverage-unknown`, capability → `region:unmapped-code`, which is not on the chain. Corrected at both sites. The load-bearing part — all eighteen entity and relationship claims carrying the two-member union — is unchanged |
| F21 an [Observed] absence claim with an unstated exclusion | editorial | **CONFIRMED.** `ls -d openspec/changes/*/` returns **six**; `archive/` holds only a `README.md`. The exclusion is now stated and the conclusion is unchanged |

**Recommended answers changed by this review: none.** Q4's framing changed
and Q1 gained a third lawful arm, and both are called out because they are
the two the review pressed hardest — but **Q4 still recommends** adding the
Inferred arm as a typed landing zone with no production constructor, and
**Q1 still recommends** one CC-REV-2 package against the
three-surface-poc-experience specification alone, sequenced after lane B's
PWB manifest is disposed of. Q2, Q3, Q5 and Q6 recommend what they
recommended before. No default-if-unanswered moved.

**Register.** These six questions are registered as **P-75** in
`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` on this branch, in
the same pass as these repairs — the sequence the sibling packets settled on.
P-68 (lane B), P-69 (M2), P-70 (M3), P-71 (M4), P-72 (M5), P-73 (M6) and
P-74 (M8) each live only on their own branch; M7 carries no row yet.

**Conventions after these repairs**, re-derived over the final bytes this
session, last of all: **8** lines exceed 78 columns outside fenced
blocks and table rows (predicate: lines outside fenced blocks whose first
non-space character is not a pipe, length > 78; denominator: all
1,580 lines of this file); **0** non-fence lines carry an odd backtick
count, over **1,552** non-fence lines. The eight are enumerated: this file's
title line, the four `###` slice headings that name their size and act, and
three single unbreakable code-span paths (RFC-0001's module, the
specification-acceptance policy candidate, and the three-surface spec) — none
is a prose line that could be rewrapped, and every prose line this pass wrote
or touched is within the bar.

## Funnel summary

```
## Feature Request: M9 - One identity, one epistemic shape, one vocabulary across the surfaces
Size: small (slices 1, 2, 8) / medium (slices 3, 6, 7) / large (slices 4, 5)
Baseline: Syzygy a9f671e; served figures from the retained four-page capture and the post-lane-A Polaris capture, each named at use. The four-page capture MIXES TWO EVALUATIONS and each figure is named to its own: polaris-7478.html from the loopback daemon at Butlers 66ed58f, as-of 2026-09-10; home.html and api-poc.json from a private daemon at Butlers 7c8743f, as-of 2026-09-13; trajectory-7478.html and orrery-7478.html carry no snapshot label, so [Unknown] from the bytes and [Inferred] from the capture directory's own log (corrected 2026-09-15 per review 1, F1; superseded: "the 2026-09-10 four-page capture"). The dossier audited at f4589e2, before the lane-A trim moved several cited lines
- G1 Motif: eleven attribute names carry an entity identity across the four pages and none appears on more than two of them (corrected 2026-09-15 per review 1, F4, from ten; per-page 3/8/2/0, union 3 + 8 because Orrery's two are home's) - Polaris uses eight and mints no id for any of the nine entities, Trajectory names none of them at all; data-claim-id occurs 699/713 times on Polaris and 0 on the other three, and 0 of its values is an entity id; 0 of 1,439 rendered hrefs cross a surface at claim level and all 16 surface-root hrefs sit in the one site-nav block; the word "desired" occurs once across all four pages, in a caveat; two epistemic types with five arms emit four key-signatures in one payload and the two-member one governs all eighteen entity and relationship claims; 1 of the POC's 8 relation kinds is in RFC1-25's closed 26-row table [Observed, every figure measured this session with predicate and denominator stated]
- G2 Doctrine: VIS-1's ordering putting the rank-1 shape slices ahead of the rank-2 comprehension slices; VIS-2 at the ribbon and the Inferred arm; VIS-7's normative link rule, which slice 1 takes on in full and the existing sweep cannot see; VIS-4 (this packet drafts and adopts nothing); VIS-5 (implementation plane only); RFC2-24's closed twelve as a boundary the ribbon may not cross
- G3 Topology: apps/three-surface-poc/src + packages/three-surface-poc-core/src + packages/cap1-core/src; one slice (3) is an amendment package under contracts/candidates and edits no signed byte in place; four slices touch the POC shared model and therefore queue at work-in-progress one
- G4 Design: five cross-surface links through the existing mount-prefix helper with a served-population oracle; a state field on PocSurface so no surface can omit its state; one CC-REV-2 package carrying the join key, the tuple and the relation vocabulary together so one key is built and not two; shape unification whose acceptance bar is byte-identical pages; a typed Inferred arm with three exclusion counterexamples; a three-slot ribbon rendered for one capability first; data-claim-id landed on the two surfaces that lack it; the observed band replaced by a link; RFC1-25 names with endpoint swaps and an explicit out-of-vocabulary flag
- G5 Spec: on Q2's recommended arm no slice of M9 maps to an approved requirement-and-scenario pair that names its consequence (qualified 2026-09-15 per review 1, F12; superseded: "no slice of M9 maps to an approved requirement-and-scenario pair that squarely names its consequence" - on Q2's second arm slice 4a does map), over a denominator of 24 requirements and 24 scenarios. RFC2-26 run over all eight slice rows (denominator 8): slices 4b, 5, 6b and 8 have no requirement at all; slice 4a's nearest is POC-REQ-060 stretched beyond its text on one reading of Q2 and PWB-REQ-007 squarely on the other; slices 1, 2, 3, 6a and 7 enumerate either no RFC-0002 consequence or one this packet declines to rule. The cross-surface identity is NOT a binding deferral: RFC6-1/6-3/6-12 sit in CONTRACT-COVERAGE.md Part B2, "clauses believed not applicable (author's reading, non-binding)", and the sign-off act mints no per-clause N/A, so they render Unknown pending owner-reviewed N/A - there is nothing to reopen
- G6 Bar: every count with predicate and denominator, each served figure named to the evaluation it came from; two methods for each load-bearing zero; one false finding caught by the second method and recorded rather than deleted; three rule-6 mutants per slice including one that proves the existing sweep blind; no act-bound byte proposed for edit; ONE independent review, verdict REVISE (2 blocking, 16 non-blocking, 3 editorial), all 21 findings re-derived before applying and dispositioned below - THESE REPAIRS ARE UNCOVERED UNTIL A SECOND REVIEW CONFIRMS THEM (superseded 2026-09-15: "NO independent review yet - this is a first draft")
Acts: slices 1, 2 and 7 ride THREE-SURFACE-POC-IMPROVEMENT-CYCLES-DIRECTION.md's second limb ("or to a recorded review finding", line 56), subject to Q6; slice 3 needs a new owner act by construction, per both sign-off acts' amendment sentences; slices 5, 6b and 8 ride slice 3's act; slice 4's act depends on Q2's reading of PWB-REQ-007's scope; slice 4b needs an act if the Inferred arm becomes constructible
Open questions: Q1-Q6 above, registered as P-75 in PENDING-OWNER-DECISIONS.md on this branch, batched with the review-1 repairs as the sibling packets' P-68 through P-74 rows were (assigned 2026-09-15; superseded: "NOT registered in PENDING-OWNER-DECISIONS.md - this packet writes two files and no register row; the row would be P-74 after review 1" - M8 took P-74 at its own close-out and M7's row lands after its own review)
Sign-off: pending - the owner's
Recommended handoff: land slice 1, then slice 2, then slice 6a - none needs a schema decision and together they cost under 15 KB; rule Q1 and draft slice 3; hold every other slice behind it
```

## Recommended handoff

**If Q6 is answered as recommended:** file no new bead. Build slice 1 first,
under `syzygy-dov.9`. It is the cheapest slice, it is the one the dossier
itself names as the prerequisite experiment for the ribbon — if the owner does
not use these links, slice 5 is not worth its amendment — and it carries the
only defect in this packet that is already a VIS-7 exposure waiting to happen:
the sweep that would catch a broken cross-surface link cannot see one. Then
slice 2, then slice 6a. Together they cost under 15 KB of a 618 KB headroom
and change no truth.

**If Q6 is answered the other way** — that the pursuit is a new cycle whose
report is owed first — then report the cycle and land the same three slices
after. Nothing about the design changes; only the order does.

**If Q1 is answered as recommended:** draft slice 3 as a
three-surface-only CC-REV-2 package and sequence it to start after lane B's
PWB manifest is disposed of, so that two unperformed manifests are never open
over the same eleven files. If the owner takes the second arm — one package
spanning both specifications — then M9's delta and lane B's are one change,
not two, and lane B's package must be reopened rather than raced.

**If Q2 is answered the other way** — that PWB-REQ-007 reaches the POC's nine
entities and nine relationships — then two things follow that the owner should
see together. Slice 4 becomes conformance to an adopted requirement rather
than an enhancement, which makes it *more* urgent, not less. And the served
payload is in breach today, on 18 of 1,167 epistemic-labelled objects, which
is a disclosure owed before the next evaluation is presented as sound. This
packet does not make that finding, because it reads the requirement's scope
the other way; but the reading is the owner's and the consequence should not
be discovered later.

**If Q3 is answered as recommended:** slice 8 lands the renames with their
endpoint swaps and the out-of-vocabulary flag, and slice 3 carries
POC-REQ-055. The thing to write down in the bead is the part that cannot be
repaired: `CONTRACT-COVERAGE.md` line 89 will continue to say the closure
consequence is covered by POC-REQ-052, because those bytes are signed. The
amendment's own coverage rows are where the successor reading lives, with the
predecessor row preserved. If the owner takes the second arm — that the POC's
kinds are a surface-local vocabulary outside RFC1-26 — then slice 8 is a
naming convenience, worth doing for readers and carrying no contract claim,
and the bead should say so rather than let a reader infer a compliance that
was never asserted.

**If Q4 is answered as recommended:** slice 4b adds the arm and the exclusion
battery and stops there. The bead records, in its close reason, that 2 of the
3 doctrine labels and 5 of the 6 rendering tiers remain unreachable in
production — so the next person to open this does not read a typed arm as a
constructed one. If the owner takes the second arm, the same sentence is owed
with one fewer label.

**If Q5 is answered as recommended:** the byte-adding slices land in the
stated order and each bead records its measured delta against the figures in
this packet, re-measured on a committed clean tree per `AGENTS.md`'s
measurement rule. The slice to watch is 5: the catalog-wide ribbon does not
fit today, and the honest thing to do at the fan-out step is to measure again
and say so, not to trim something else to make room. If the owner takes the
second arm — nothing byte-adding until the Butlers repairs land — then slices
1, 2 and 8 proceed and the rest wait on a Butlers commit this packet cannot
schedule.
