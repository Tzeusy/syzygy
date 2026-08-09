(part 1/3)

Reviewer: human-view (RD-10)
Date: 2026-08-09
Commit: 771965c
Files read:

- `C/rfcs/RFC-0007/README.md`, `narrative-contract.md`, `rendering-and-surface.md`
- `C/rfcs/RFC-0008/README.md`, `identity-authority-materialization.md`, `state-vocabulary-and-cost.md`, `accounting-reconciliation-and-release.md`
- `C/rfcs/RFC-0009/README.md`, `semantic-geography.md`, `visual-grammar-and-lenses.md`, `interaction-parity-and-release.md`
- Governing: `doctrine/vision.md`, `architecture.md`, `trust-and-evidence.md`, `v1.md`, `security.md`; `decisions/SURFACE-DECISION-RECORD.md`
- Reference (read to verify citations, not reviewed): `.syzygy/map/topology-candidates/` (all 11 files), `.syzygy/intent/OVERVIEW.md`, `C/CONTRACT-DEPENDENCY-INDEX.md`, and the cited clause bodies RFC2-24, RFC3-5/3-6, RFC4-23, RFC6-6, RFC6-24, RFC10-15
- Not read, per instruction: `C/round-2026-08d/`, `C/reviews/`, `C/history/`, `_bootstrap/`

---

## Answers to the review questions

1. **Fixed human entry (RFC7-39).** [Observed] The *path* is unambiguous; the *entry* is not — RFC7-39's front door and RFC7-6's primary narrative are two front doors with no stated relation, and the acceptance test (RFC7-30) enters the latter. Non-authority is enforced by clause for narrative-model units (RFC7-3, RFC7-33), but RFC7-39 never states that its file is one. **F2.**
2. **Root-repository discoverability (RFC7-40).** [Observed] Propose-only under VIS-5 is clean and correctly reasoned. The finding itself is not well-defined: a three-value domain that grows a fourth value inside the same clause, an Unknown with no RFC2-24 reason, and an input ("configured landing document") with no lawful configuration site under RFC3-5. **F9.**
3. **Polaris comprehension (VIS-3).** [Observed] Minimal default density is four registry vocabularies per capability, and the comprehension test contains no prompt that would fail a surface whose tier vocabulary is unreadable. **F10.**
4. **Trajectory truth.** [Observed] Conflation is guarded hard and well (RFC8-12, RFC8-15, RFC8-28, RFC8-30, RFC9-32, RFC9-46); an unstarted or failed item cannot render as its non-state. One structural flaw: the "two orthogonal fields" claim is false of the value `reconciled`. **F4.**
5. **Orrery semantics (VIS-7).** [Observed] Determinism and legend fidelity are the strongest work in the three packages. Two holes: residual-adjacency decidability is defeasible by lawful LOD/filter/narrowing (**F5**), and a mandatory aggregate-disclosed sibling state has no reserved treatment (**F6**).
6. **Accessibility.** [Observed] Polaris (RFC7-33/34) and Orrery (RFC9-46/48) are strong, including the reachability limb. RFC 0008 binds nothing: a sweep of all four RFC-0008 files for *keyboard | accessib | screen-reader | non-visual | colo(u)r* returns zero hits, and RFC8-28's separation rule omits the colour limb its RFC9-32 counterpart carries. **F3.**
7. **Topology alignment.** [Observed] No contradiction found. Two gaps: the topology bundle never places `.syzygy/intent/OVERVIEW.md`, and OVERVIEW.md's "four terminal answers" is a different quadruple from RFC8-28's. **F14.**
8. **Phase rules.** [Observed] Real in form, defective in reach: RFC7-38's coverage range stops at RFC7-37 (**F1**), and all three phase rules rest on an ungated "reviewed N/A judgment" (**F7**).

---

## Findings

### F1 — blocking — RFC7-38's coverage obligation does not reach RFC7-39 or RFC7-40

`rendering-and-surface.md` §3.13:

> **RFC7-38 — This contract schedules nothing.** … before implementation, every observable consequence of **RFC7-1…RFC7-37** must either **map to an approved OpenSpec requirement or scenario** … The surface-specification phase must produce, as a deliverable, a **clause-to-requirement coverage matrix** for this RFC — every clause mapped to requirement identities or to its reviewed N/A …
>
> *(RFC7-38 binds the whole package: RFC7-1…RFC7-37 spans both modules …)*

`README.md`, Phase boundary, repeats the bound: "its clause-to-requirement coverage matrix must cover **RFC7-1…RFC7-37 across both modules**". The module frontmatter records that the ordering is deliberate — "RFC7-38, the phase rule, is defined before RFC7-39/40 in file order — deliberate" — but the *range inside the clause* was not moved with them.

RFC7-39 and RFC7-40 are the two most plainly user-observable clauses in the package: a fixed entry path a human reader is sent to, and a per-repository rendered finding with a Proposal affordance. [Observed] The clause's general prohibition still reaches them, but the mechanism that discharges it does not: there is no obligation to map their consequences to an OpenSpec requirement and no matrix row in which their absence would show. The result is either that they cannot be implemented by the book at all, or — the realistic outcome — that they are implemented with no coverage and nothing detects it. This is exactly the failure RFC9-47(a) was written to prevent on the other surface; RFC 0007 has no equivalent self-maintenance clause, which is why the omission survived.

**Repair.** Amend RFC7-38's range in place to `RFC7-1…RFC7-37, RFC7-39, RFC7-40`, or restate it as "every clause of this RFC other than this one", and update the README Phase-boundary paragraph and the in-clause parenthetical in the same logical change. Do not fix this after the digest is bound (verification rule 10).

### F2 — major — two front doors, and the fixed one is untested and unattached to the narrative model

`rendering-and-surface.md` RFC7-39:

> For a governed project, `.syzygy/intent/OVERVIEW.md` is the **fixed, Syzygy-owned human entry point**: the one path a human reader is sent to first … and rendered as governed presentation under this contract's narrative rules.

`narrative-contract.md` RFC7-6:

> A governed project has at most one **primary narrative** — the front door the comprehension test (RFC7-30) enters.

`rendering-and-surface.md` RFC7-30:

> a fresh reader … **entering at the primary narrative (RFC7-6)** with navigation confined to Polaris …

[Observed] Nothing in the package states whether OVERVIEW.md *is* the primary narrative. A sweep for `primary narrative` and `OVERVIEW` across all three RFC-0007 files returns eight hits for the former and one for the latter, with no clause connecting them. Both horns are defective: if they differ, the path every human is sent to first is not the path the surface's only acceptance test walks; if they are the same, RFC7-6's "at most one" and RFC7-5's "Identifiers are opaque and label-independent" sit against a front door whose identity is a fixed path.

The second limb is sharper. RFC7-33's non-citability obligation is scoped by unit type: "Every **narrative-model unit (RFC7-5)** carries the **`non-citable` / `presentation-artifact`** attribute, required on **every** exported, embedded, or plain-text rendering". RFC7-39's "under this contract's narrative rules" is a blanket phrase; the same authors, facing the identical question one clause earlier, refused the blanket and enumerated — RFC7-36: "**Carry-over out of `.syzygy/intent/**`** — stated, not inferred … **These follow it:** RFC7-2 …; RFC7-7 …; RFC7-11 **and RFC7-11(a)** …; RFC7-33/34". RFC7-39 gets no such enumeration, so the one file external agents are most likely to fetch has no clause-level guarantee of the attribute whose omission RFC7-33 itself calls "unrecoverable at the consumer".

**Repair.** State in RFC7-39 whether the entry is the RFC7-6 primary narrative (and if so, that RFC7-30 enters it); and enumerate the carried obligations in RFC7-36's style rather than by blanket reference — at minimum RFC7-2, RFC7-5 membership, RFC7-7, RFC7-33/34.

### F3 — major — RFC 0008 binds no non-visual parity, and RFC8-28 permits a colour-only distinction between a gap and a Contradiction

Sweep, denominator all four RFC-0008 module files (`README.md`, `identity-authority-materialization.md`, `state-vocabulary-and-cost.md`, `accounting-reconciliation-and-release.md`), case-insensitive fixed-string search for *keyboard*, *accessib*, *screen reader*, *screen-reader*, *colour*, *color*, *non-visual*: **zero hits**. [Observed]

`accounting-reconciliation-and-release.md` RFC8-28:

> … **must never share a rendering**. Unqualified "reconciliation" means only the doctrinal sense … and the same reservation binds `unsatisfied` (a gap) against `contradiction-raised` (a Contradiction, owner adjudication only), which Trajectory **must never merge into one count or one badge** (RFC2-17; RFC4-6).

Its map counterpart closes the channel explicitly — `visual-grammar-and-lenses.md` RFC9-32: "**never share a mark, a mark's color, a count, or a legend entry**". [Inferred] Two differently-coloured badges do not "share" a rendering, a count, or a badge, so RFC8-28 as written is satisfied by a distinction only colour carries, on the surface where the reader learns whether a merged change is a gap (route: work) or a Contradiction (route: owner adjudication only, RFC1-21). Polaris binds RFC7-34 ("recoverable **without colour, position, or layout**") and Orrery binds RFC9-48; Trajectory binds neither, and no doctrine clause exempts it — trust-and-evidence.md's floor and VIS-1 do not distinguish surfaces.

**Repair.** Add the colour limb to RFC8-28 in RFC9-32's words, and add a non-visual parity clause to RFC 0008 (next free integer, RFC8-33) covering keyboard operability of the board/queue/drawer handoff and textual carriage of every normalized-state and chain-state value. Route the new obligation to a release check if RFC 0008 grows one.

(part 2/3)

### F4 — major — the "two orthogonal fields" claim is false of `reconciled`

`state-vocabulary-and-cost.md` RFC8-12:

> **The normalized state is one of two orthogonal fields.** … The **RFC2-18 chain state** (`merged`, `reconciliation-pending`, `reconciled@E`, `unsatisfied`, `contradiction-raised`, `Unknown(reason)`) is a **separate field with its own closed vocabulary** (RFC8-28), carried beside the normalized state on every rendering, filter, count, and machine answer, and **never folded into it** …

RFC8-13's derivation row for the eighth live state:

> | `reconciled` | `reconciled@E` per RFC2-18 | A reconciliation verdict claim, gate-backed Observed (RFC2-25), rendered with its evaluation identity | V0: never renders …

[Observed] The normalized value `reconciled` is *defined as* the chain value `reconciled@E`, so for that value the two fields are not orthogonal — one is a total function of the other. [Inferred] The consequence is operational, not cosmetic: RFC8-28's argument for carrying both fields is that normalized `merged` is compatible with three chain states, which is true of `merged` and false of `reconciled`; an implementer who reasons from that argument will drop the chain state wherever the normalized state is `reconciled`, and RFC8-28's own justification supplies the reasoning. Compounding it, two of the eight live values (`merged`, `reconciled`) collide in spelling with chain values that RFC6-14 requires be carried **verbatim** beside them on every machine answer, with no field-qualification rule anywhere in the package — the hazard RFC9-9 treats at length for `depends_on`/`depends-on`/`declared-dependency` and RFC1-25(b) closes with a twelve-pair invariant.

**Repair.** Either (a) state in RFC8-12 that normalized `reconciled` is a projection of the chain state and never substitutes for it, and add the field-qualification rule for machine answers; or (b) retire normalized `reconciled` in favour of the chain field alone (retire, never renumber). Whichever is chosen, the "orthogonal" wording must stop asserting more than the vocabulary supports.

### F5 — major — residual-adjacency decidability is defeasible by lawful LOD, filters, and performance narrowing

`semantic-geography.md` RFC9-9(a) part 2:

> **The residue must be reader-decidable, not merely disclaimed.** A nearness carries meaning only if it is **intra-district** — visible, because district boundary is a rendered reserved channel (RFC9-25) — or **accompanied by a rendered `declared-dependency` edge in honored state** — visible, because that edge renders on its own explicit channel with its state (RFC9-9(b)). … A reader can therefore decide which of the three readings applies to any given pair **from what is on the screen**, without access to the placement algorithm.

[Observed] Reading 1's discriminator is protected: RFC9-25 makes district boundary a reserved, lens-invariant channel. Reading 2's discriminator is not. `visual-grammar-and-lenses.md` RFC9-42: "Zoom and level-of-detail **may reduce geometric fidelity and label density freely**; they may never change a fact's epistemic state — only its aggregation." `semantic-geography.md` RFC9-13: "A filter that hides **entities** shows a persistent count of what it hid" — entities, not edges. `interaction-parity-and-release.md` RFC9-49 permits degradation "by narrowing an explicitly declared scope, rendered as narrowed". None of the three protects the `declared-dependency` edge channel, and RFC9-44 shows the package knows how to write that protection when it wants it: "no filter default, LOD step, lens, or profile may drop it."

[Inferred] So a lawful zoom-out, a lawful filter, or a lawful declared narrowing removes the only on-screen evidence distinguishing reading 2 from reading 3, and RFC9-9(a) part 1's third legend line — "residual adjacency — carries no meaning" — becomes false about nearness that *does* carry meaning. That is the VIS-7 legend-fidelity failure part 2 exists to prevent, reached without violating any clause. RFC9-47's gate list names the residual-adjacency line but only at full fidelity: "the position/proximity registry entry declares all three readings, and residual placement produces no enclosure, shared boundary, plinth or common ground plane that mimics declared containment." No check exercises a filtered or zoomed-out scene.

**Repair.** Add a limb to RFC9-9(a) part 2 protecting the `declared-dependency` edge channel and its honored/not-honored state from LOD reduction, filter defaults, and RFC9-49 narrowing wherever nearness is rendered — or, alternatively, require the third legend line to change to "undecidable at this fidelity" when the channel is suppressed. Route the resulting check into RFC9-47's list in the same logical change (RFC9-47(a) part 1).

### F6 — major — `editorial draft` is mandatory in aggregate disclosure and absent from the reserved palette

`visual-grammar-and-lenses.md` RFC9-43:

> **The disclosed composition is the full RFC9-46 equivalence tuple** — per-label, per-tier, per-Unknown-reason and per-freshness-state counts **and sibling surface states** … the sibling surface states being the three RFC2-25 places deliberately outside the registry (*dismissed by decision*, *unadopted draft*, *editorial draft*, per RFC6-14) …

RFC9-24, the reserved palette:

> **Contradicted** … ; **Dismissed by decision** … ; **Proposed/speculative** … ; **Unadopted draft** (proposed treatment + "unadopted" plate; anchors nothing).

[Observed] Sweep of all four RFC-0009 files for the fixed string `editorial`: **one hit**, RFC9-43 line 402. The state is minted at RFC7-20 ("`editorial-draft` is a **named RFC2-25 sibling surface state** — the third, alongside `dismissed-by-decision` and `unadopted-draft`") and required by RFC9-46's equivalence tuple, but RFC9-24 reserves no treatment for it. Under RFC9-26 — "**The registry is fail-closed: a channel with no registry entry must not render.** There is no hand-authored fallback legend and no default meaning" — the state either does not render (contradicting RFC9-43's mandatory composition and RFC9-46's tuple, a release-blocking table/scene disagreement under RFC6-22/23) or renders on an unreserved treatment, which is the unlegended-meaning violation VIS-7 forbids.

**Repair.** Add *editorial draft* to RFC9-24's reserved sibling-state list with a distinct reservation, in the same logical change as any RFC9-47 routing.

### F7 — major — the phase rules' escape hatch is an ungated authorization

Three clauses, one text. `rendering-and-surface.md` RFC7-38 / `accounting-reconciliation-and-release.md` RFC8-32 / `interaction-parity-and-release.md` RFC9-52:

> … must either **map to an approved OpenSpec requirement or scenario** in the governance root's `openspec/**` plane, or carry an **explicit, reviewed N/A judgment** recording why that consequence needs no requirement.

[Observed] None of the three names where the N/A judgment lives, who may review it, or under what provenance it is honored. [Inferred] An N/A judgment *removes an implementation obligation* — it is authorization-bearing by the corpus's own test, and the corpus gates every comparable artifact: RFC7-21 (draft adoption), RFC7-25 (review verdict), RFC7-31 (walkthrough judgment), RFC8-12 (derivation mapping), RFC9-18 (layout version registry), RFC9-26 (channel registry), RFC9-35 (promotion), RFC9-45 (judgment and release policy) all invoke RFC3-16(a), each with the same premise: `.syzygy/governance/**` is writable by the untrusted fleet-worker class (SEC-3, as RFC3-16(a) extends it to committed artifacts). The N/A judgment is the one authorization-bearing artifact in these three packages left ungated, and it is the one that turns "this clause needs a requirement" into "this clause needs nothing".

Secondary, same clauses: the binding sentence is over "every observable **consequence**" while the checkable deliverable is a "clause-to-requirement coverage matrix" — per clause. A clause with five observable consequences and one mapped requirement produces a complete-looking matrix. [Inferred]

**Repair.** In all three clauses, name the N/A judgment's home (`.syzygy/governance/decisions/`, per RFC3-15 and RFC7-25's own reasoning), require it to be honored only under RFC3-16(a), and state that a judgment whose provenance does not verify leaves the consequence unmapped rather than excused. Optionally state that the matrix rows are per observable consequence, not per clause.

### F8 — major — RFC7-11 degrades a claim to Unknown with no RFC2-24 reason, and the README still calls the defect Live after RFC 0002 discharged it

`narrative-contract.md` RFC7-11:

> When an anchor no longer resolves … the block renders the break **on the primary surface**: the anchored claim degrades to Unknown, the break is named (which anchor, which target; RFC6-5 outcome `unresolvable` or `retired`) …

`RFC-0006-cross-surface-selection-query-drawer.md` RFC6-6:

> **Outcomes are not Unknown reasons.** `not-applicable`, `retired`, `resolved-absent`, and `unresolvable` are **navigation outcomes**, not claim statuses: they must not be stamped with, or counted among, RFC2-24 Unknown reasons …

[Observed] RFC2-24 carries twelve closed reasons and RFC6-14 requires every machine answer carry the reason verbatim. RFC7-11 names an outcome and no reason, so the Unknown it mints has nothing to carry. The reason exists and was minted at this package's request — RFC2-24 #11 `reference-unresolvable`, "The source **was** captured and the governing declaration **does** exist, but a cited internal anchor no longer resolves … Repair the reference".

`RFC-0007/README.md` §5, defect 1, is titled "**RFC 0002 / RFC 0006 — dangling-anchor vocabulary. Live.**" and then reports its own discharge: "RFC 0002 has added it as reason #11 citing this finding". [Observed] Sweep for the fixed string `reference-unresolvable` across all three RFC-0007 files: **one hit**, README line 207 — the string appears in no clause. The loop is open at both ends: the clause never cites the reason, and the package still offers the owner a defect labelled Live whose upstream fix landed.

**Repair.** Cite reason #11 in RFC7-11 as the claim's Unknown reason (keeping the RFC6-5 outcome as the navigation fact it is), and re-status README §5 defect 1 from "Live" to discharged, noting that the owner may still strike #11 at RFC 0002's acceptance.

### F9 — major — RFC7-40's answer domain is stated closed at three values and then opened to four, with no reason vocabulary

`rendering-and-surface.md` RFC7-40:

> … the kernel answers: *does the repository's front door (its root README or **configured landing document**) link to the Syzygy project entry (RFC7-39)?* — **`yes / no / Unknown`**, per repository, at the producing evaluation. … The finding never implies that every observed repository can host a `.syzygy/` entry: for repositories without a governance root the finding renders the actual limitation — **not-applicable with the reason**, or Unknown where observation cannot establish it …

Three defects in one clause. [Observed]

1. **The domain contradicts itself.** Three values are set in bold as the answer set; a fourth (`not-applicable`) appears eleven lines later. Under RFC6-14 the value is carried verbatim on machine answers and under RFC6-22/23 a spelling disagreement between two renderings is release-blocking — the exact reasoning RFC8-12 gives for closing its vocabulary ("a value the contract never names can be neither carried verbatim on a machine answer nor checked for parity") and RFC9-9(b) gives for naming "a closed three-value categorical domain".
2. **The Unknown carries no reason.** Every comparable clause in the three packages names one — RFC9-20 (`missing-declaration`, RFC2-24 #1), RFC9-27 (`mapping-coverage-absent`, #5), RFC8-8 (#8), RFC9-30 (`unconsented-source-or-provider`). RFC7-40's Unknown names none, and the "reason" it does mention attaches to `not-applicable`, which is not an Unknown.
3. **"Configured landing document" has no lawful configuration site.** RFC3-5: "The declaration's top-level field set is **closed** at:" — eight fields, none of them a landing document — followed by "Additions to this field set require an amendment to this RFC." An input with no declared home is also unclassified as a snapshot input, which RFC2-2 makes fatal to a deterministic answer.

The unconsented-repository case, by contrast, is already answered upstream and only needs citing — RFC3-6: "An entry whose consent reference does not resolve to an in-force consent record is **not observed**: its content renders Unknown (`unconsented-source-or-provider`, RFC2-24 #6)".

**Repair.** State the domain once and closed (four values); require the RFC2-24 reason verbatim on Unknown and cite #6 for the unconsented branch via RFC3-6; and either drop "configured landing document" or route its declaration through an RFC3-5 amendment in the same logical change.

(part 3/3)

### F10 — major — the default reading path carries four registry vocabularies, and the comprehension test cannot detect that a reader could not read them

`narrative-contract.md` RFC7-16:

> Default density is minimal: per capability or major claim, one epistemic state — **its label with its RFC2-25 tier**, and its freshness — with its evaluation identity and a drawer/Trajectory handoff …
>
> **Tier is in the at-rest set for the same reason staleness is** … a `report-fact` Observed claim or an `asserted-by-worker` Inferred one, set in composed prose, reads as settled unless its tier renders beside it …

[Observed] The clause's reasoning is right, and the resulting minimum is four technical carriers on every capability at *minimal* density: an epistemic label, a tier drawn from RFC2-25's six-value registry (`gate-backed`, `report-fact`, `asserted-by-worker`, `reduced-fidelity`, `declared-only`, `suspended` — enumerated at RFC9-43), a freshness state, and an evaluation identity. No clause in the package obliges any of them to render with a plain-language gloss on the narrative surface.

RFC7-30's prompts are: "why the project exists; what it promises; what it refuses to be …; what its major capabilities are and how they fit; **where exactness lives** …; and **one thing the project does not currently know about itself**". [Inferred] None of these is failed by a reader who cannot distinguish `asserted-by-worker` from `gate-backed`. The last prompt is well-designed and catches the uniformly-confident surface; it does not catch the surface that is honest in a vocabulary the fresh reader cannot read. On a surface whose charter is "a cohesive visual argument" (SDR §2) and whose test is a cold-open walkthrough, that is the VIS-1 rank-2 obligation — "comprehension of the truth's presentation" — going unmeasured.

**Repair.** Add one prompt to RFC7-30 requiring the reader to state, in their own words, how strongly the surface claims to know one rendered fact and what would make it stronger; or add to RFC7-16 an obligation that registry vocabulary render with its plain-language meaning reachable at the point of display. The first is cheaper and is the one the test is shaped for.

### F11 — minor — a Wave-B clause is functionally conditional on an unaccepted Wave-D clause behind an open question, declared only as a citation

`semantic-geography.md` RFC9-8(a):

> … so it lives in the typed **workspace governance store** (RFC10-15), never in the workspace manifest … (Staged reference: until an accepted RFC 0010 mints the store, **no portfolio re-lay is lawful** — the machinery waits with the store, and the manifest never substitutes.) … Without this machinery, append-stability inherited from RFC9-15 leaves **no lawful way ever to re-lay the portfolio**.

[Observed] RFC10-15 exists (`RFC-0010/portfolio-and-cross-project-consent.md`) and its owning question is open — `RFC-0010/README.md`: "| q3 | Workspace governance store (RFC10-15) | **open** |". No RFC-0009 module declares `depends_on: RFC-0010`; module 1's frontmatter is `[RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0006]` and the package README's is `[RFC-0001…RFC-0008]`. `CONTRACT-DEPENDENCY-INDEX.md` accordingly records the relation under `cites`, the weakest of its three, beneath its own banner "**A citation is not a reliance.**" Here it is a reliance: a reader who loads RFC-0009 by the declared edges cannot evaluate the condition under which a portfolio re-lay becomes lawful.

The clause fails closed (no store, no re-lay), which is why this is minor rather than major. Separately and also minor: RFC-0007 and RFC-0009 declare `depends_on` on each other at both package and module level, so the declared load of either surface pulls the other entire.

**Repair.** Declare `depends_on: RFC-0010` on `semantic-geography.md` and regenerate the dependency index, or restate the staging in RFC9-8(a) without a forward clause citation ("until an owner-accepted typed workspace governance store exists").

### F12 — minor — the README's cross-module citation enumeration is inaccurate

`RFC-0007/README.md`, Clause map:

> **Twelve citation edges cross it, all resolvable by the lookup rule above:** module 1 → module 2 at RFC7-6→RFC7-30, RFC7-11/11(a)→RFC7-33, RFC7-14→RFC7-26, RFC7-17→RFC7-26/33, RFC7-20/25→RFC7-33; module 2 → module 1 at RFC7-26→RFC7-17, RFC7-27→RFC7-2, RFC7-29→RFC7-14/18/23, RFC7-30→RFC7-6, RFC7-31/32→RFC7-25, RFC7-33/34→RFC7-5/11/11(a)/13, RFC7-36→RFC7-2/3/7/11/11(a).

[Observed] Mechanical scan over all 41 clause bodies (26 in module 1, 15 in module 2, each body cut at the next `##` heading), matching `RFC7-<n>` and keeping only cross-range references: **10** distinct module-1 → module-2 edges and **21** distinct module-2 → module-1 edges, 31 in total. Edges present in the modules and absent from the README's list include RFC7-5→RFC7-28, RFC7-6→RFC7-31, RFC7-29→RFC7-2, RFC7-31→RFC7-3, RFC7-33→RFC7-3, RFC7-36→RFC7-5, and RFC7-38→RFC7-1.

The stated count is a derived measurement transcribed into contract prose inside the wave's digest set — the class of error the same README warns about two paragraphs earlier ("A measurement copied into contract prose goes stale the moment any module moves") and the class RFC-0009's README records going stale twice. Operational harm is nil, because the lookup rule resolves any `RFC7-n` without the list.

**Repair.** Delete the enumeration and the count; the lookup rule already discharges the navigation need. If it is kept, generate it.

### F13 — minor — the package's indices, scope maps and integration lists predate RFC7-39/40

[Observed] Sweep of all three RFC-0007 files for `RFC7-39` / `RFC7-40`: the only occurrences are the two clause definitions, RFC7-40's back-reference to RFC7-39, and four range-bookkeeping lines (`clauses:` frontmatter ×2, the clause-map table row, the two end-of-file footers). Consequently:

- `rendering-and-surface.md` §0 scope map ends at "the binding phase rule at the OpenSpec seam (RFC7-38)" and never mentions §3.14;
- the module's `governs:` frontmatter — `[reading-mode, proposed-scenario-rendering, curated-diagram, authority-boundary, comprehension-test, walkthrough-record, machine-parity, non-visual-recoverability, portfolio-narrative, subproject-navigation]` — carries no entry-point or discoverability term, and neither does the package README's;
- the module's `**Serves:** VIS-1, VIS-2, VIS-3, VIS-6, VIS-7; SEC-3, SEC-5` omits **VIS-5**, on which RFC7-40 expressly rests ("the repository front door lies outside the two writable namespaces (VIS-5)");
- module 2's §5 records no reliance for either clause, including RFC1-27, which RFC7-40 invokes for the Proposal;
- neither clause has a violation case, in a package that gives one to almost every other clause.

**Repair.** One pass updating scope map, `governs`, `tags`, `Serves`, §5 and the violation-case set, bundled with F1 (verification rule 10: batch, do not trickle). Consider giving RFC 0007 an RFC9-47(a)-style same-logical-change invariant; its absence is the proximate cause of both F1 and this finding.

### F14 — minor — topology silence on the fixed entry, and an OVERVIEW/RFC8-28 quadruple mismatch

[Observed] Sweep of all 11 files in `.syzygy/map/topology-candidates/` for `OVERVIEW`: zero hits. The bundle places the plane's directories — `02-project-workspace-repos.md`: "openspec/** + .syzygy/** plane<br/>(governance/, intent/, work/, map/, cache/, local/)" — and 04 enumerates the `governance/` categories file by file, but nothing in the bundle carries RFC7-39's per-project fixed path, though topology is the declared authority for intended placement. Not a contradiction; a silence between two candidates offered under separate acts.

Second: `.syzygy/intent/OVERVIEW.md` states "The terminal answers — reconciled-with-evidence, Unknown(reason), unsatisfied, contradiction-raised — are four different answers that never share a rendering." RFC8-28's four are "*reconciled at E with evidence* vs *merged, not yet evaluated* vs *evaluated and unsatisfied* vs *evaluated, contradiction raised*". [Inferred] These are two different partitions of the same six-value chain vocabulary, both presented as "the four", and the one the owner reads first is the one that drops *merged, not yet evaluated* — the state RFC8-29 makes the honest V0 answer for all merged work.

**Repair.** Route the OVERVIEW quadruple to the RFC8-28 wording at the overview's own act; add the RFC7-39 path to the topology bundle at its act. Neither belongs inside the Wave B digest set.

### F15 — minor — RFC9-48 misattributes a textual-label requirement to RFC9-27

`interaction-parity-and-release.md` RFC9-48:

> … **textual epistemic labels for every state (RFC9-27's two-carrier rule)** …

`visual-grammar-and-lenses.md` RFC9-27:

> No epistemic state is carried by color alone: each carries at least two of {surface treatment, plate/badge, label}.

[Observed] RFC9-27's rule is satisfied by *surface treatment + plate/badge*, neither of which is text; it is a colour-independence rule, not a textual-label rule. RFC9-48's own clause text independently binds textual labels, so nothing is lost in effect — but the parenthetical states that RFC9-27 requires something it does not, and RFC9-47's gate list repeats the attribution ("textual epistemic labels for every state").

**Repair.** Drop the parenthetical, or restate it as "(distinct from RFC9-27's two-carrier rule, which bars colour alone but permits two non-textual carriers)".

---

## Assessment

The three packages are, on the whole, unusually disciplined work: the Orrery determinism and legend-fidelity chain (RFC9-9/9(a)/9(b)/9-14/9-15(b)/9-16(d)), Trajectory's closure-fallacy and honest-absence apparatus (RFC8-12/13/15/28/29/30), and Polaris's citation/generation/time triad (RFC7-3, RFC7-20/21, RFC7-10/11(a)) each close their named failure with clauses a reviewer can actually fail an implementation against. The self-maintaining gate registry (RFC9-47(a)) is the best structural idea in the corpus.

What blocks the offer is narrow and mechanical: the two newest Polaris clauses were appended without moving the phase rule's range with them, so the surface's own OpenSpec boundary does not reach the entry point every human is sent to. That is a one-line clause amendment plus a hygiene pass, and it must land before a digest is bound rather than after. The major findings around it — the untested fixed entry, Trajectory's missing non-visual floor, the `reconciled` orthogonality slip, the ungated N/A judgment, and the two Orrery holes — are each repairable in place and none is structural.

VERDICT: REVISE
