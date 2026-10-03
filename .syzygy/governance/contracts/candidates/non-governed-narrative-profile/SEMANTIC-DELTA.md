# Semantic delta POLARIS-NGNP-1 — Non-governed narrative profile

> **Candidate — binds nothing.** A proposal in the form of
> `contracts/candidates/policy-candidates/SEMANTIC-DELTA-TEMPLATE.md`. An agent
> drafted it; adoption belongs to the owner.

**Artifact(s):**         `openspec/changes/polaris-non-governed-narrative-profile/proposed/polaris-generation/spec.md` (new); no existing file is edited
**Stable IDs affected:**  REQ-polaris-generation-032 (new). REQ-polaris-generation-004 (as amended by the tree-form adoption) is affected in effect, not in bytes: for a non-governed subject the new requirement displaces the text of 004 listed under "Displaced text" below, so 004 alone no longer states the rule for that class. REQ-polaris-generation-019 is relied on for the anchor form. Read against RFC1-14, RFC7-2, RFC7-6, RFC7-10, RFC7-13, RFC7-14, RFC7-15, RFC7-17, RFC7-19, RFC7-33. No RFC and no byte of 004 is edited.
**Change class:**         Normative
**Author:**               lane-d drafting agent (Claude Opus 5.5)
**Date:**                 2026-10-03

## Current meaning

Quoted from the effective requirement 004 (`openspec/changes/polaris-manifesto-understanding-amendment/specs/polaris-generation/spec.md`):

> The primary narrative SHALL use RFC7-13's default altitude order unless the owner rules otherwise; alternative named narratives remain subject to the same per-altitude and exact-leaf obligations.

> Capability deep dives SHALL preserve RFC7-17's three authority classes and default argument/contract/reality ordering.

> Catalog membership SHALL come from declared capabilities, with drafts unadopted and missing declarations explicit; empty bands SHALL retain an honest absence line.

Its scenarios, verbatim:

> #### Scenario: Primary altitudes and one-step source access
>
> - **WHEN** a primary narrative has no owner ruling changing its default altitude order
> - **THEN** it offers thesis/manifesto, architecture story, capability catalog, capability deep dive and verbatim specification leaf in that order, with each stopping depth independently honest
> - **AND** each anchored block reaches the owning artifact in one step regardless of browsing depth; a differently ordered additional narrative still meets each altitude obligation

> #### Scenario: Capability detail keeps three authority classes
>
> - **WHEN** a generated deep dive combines an explanation, requirements and current reality
> - **THEN** its default argument, contract and reality bands appear in that order with exactly one of the three authority classes declared per band in human and machine forms
> - **AND** reality facts come from the shared drawer, the contract band links exact owning text, and an empty band collapses to an honest absence line with the relevant Unknown reason instead of disappearing or leaving scaffold headings

> #### Scenario: Catalog membership comes from declarations
>
> - **WHEN** code names and a draft capability suggest functionality absent from adopted capability declarations
> - **THEN** the catalog preserves declared identities, visibly marks the draft unadopted and renders undeclared or unmapped coverage Unknown with its reason and route
> - **AND** the model cannot invent a declared capability from code, and a predominantly Unknown catalog remains a normal honest presentation

Quoted from the RFC clauses the profile reads against (`.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`; RFC7-33 in `RFC-0007/rendering-and-surface.md`; RFC1-14 in `RFC-0001-project-graph-identity-state-planes.md`). Each block is marked **whole** (the clause from its identifier to the next clause) or **excerpt**; no block is partial where it says whole. Four blocks (RFC7-2, RFC7-6, RFC7-13 and RFC7-14) are quoted as two blockquotes of one clause, and both paragraphs are present in each.

**RFC7-2, whole:**

> **RFC7-2 — Composition, never custody.** Every **load-bearing narrative
> claim** — a span of narrative content asserting a fact about the project
> (rules, behavior, structure, status, history, decisions) — is exactly one of:
>
> - **(a) anchored** — resolvable through its claim block's source anchors
>   (RFC7-9, RFC7-10) to the one artifact that owns the fact;
> - **(b) explicitly non-normative** — framing, motivation, analogy,
>   transition, or reader guidance, machine-marked as carrying no normative
>   force; or
> - **(c) epistemically labeled** — Observed with its evidence link, Inferred
>   with its inference provenance, or Unknown, per trust-and-evidence.md.
>
> There is no fourth kind: an unanchored, unlabeled, unmarked project-fact claim
> in curated narrative is a **defect**, not a style choice. Granularity is the
> claim block (SDR-16) — the obligation binds claims; the mechanism binds
> blocks.
>
> **The check binds the authoring act, not one path through it**: it is a
> property of **any act producing curated narrative** — a human typing prose,
> an agent repairing prose under VIS-3's authorship allowance, or a draft
> adoption — assessed per claim at the act. No authoring path reaches curated
> narrative without crossing it; RFC7-21 is one crossing point, not the only
> one (RFC7-23, RFC7-25).

**RFC7-6, whole (both paragraphs; the first speaks of a *governed* project):**

> **RFC7-6 — One primary narrative.** A governed project has at most one
> **primary narrative** — the front door the comprehension test (RFC7-30)
> enters. Additional named narratives are permitted under the same class and
> rules; none outranks another, because none is authoritative at all.
>
> **Thin, never absent.** On an undeclared or thin project the primary narrative
> may be **thin, or Syzygy-drafted and unadopted (RFC7-20), but never absent**: a
> predominantly-Unknown catalog under an honestly thin narrative is correct
> output (RFC7-15, RFC7-31) on v1.md's proving ground — "real, messy, already
> running, mostly undeclared" [Observed: v1.md]. Absence is not thinness; it is
> a missing front door, and it fails RFC7-30 rather than passing it trivially.

**RFC7-10, whole:**

> **RFC7-10 — Anchor form.** A source anchor is machine-readable and typed:
> **(target class, target identifier, optional fragment, target state)**, target
> class one of:
>
> - a **kernel entity reference** (selection reference per RFC6-1, optionally
>   evaluation-qualified);
> - a **doctrine rule or accepted-contract citation** (stable identifier
>   `VIS-n`/`SEC-n`/RFC clause, rendered per RFC6-20);
> - an **`openspec/**` anchor** (RFC3-28);
> - a **decision or policy identifier**; or
> - an **evidence artifact identifier** with integrity digest.
>
> No target class exists for narrative content, renderings, or editorial drafts
> (RFC7-3). Anchors embed durable identifiers, never labels, paths, or
> coordinates (RFC6-8/9).
>
> **The target-state component** records what the target said when the anchor
> was authored: for a declared or normative artifact (doctrine rule, accepted
> contract clause, `openspec/**` requirement or scenario, decision, policy,
> evidence artifact), its **revision**; for a kernel entity reference, the
> **evaluation identity** at which it was read together with the label + tier +
> reason the reference then carried (RFC6-14's vocabulary, verbatim). It is
> observed at the authoring act and **never rewritten by a later read**. It
> creates no new authority and no new epistemic state (`README.md` §5), and
> exists to enable RFC7-11(a).

**RFC7-13, whole (both paragraphs):**

> **RFC7-13 — Progressive disclosure: the obligation, and a V0 default path.**
> The binding content is the obligation **per altitude**: a narrative discloses
> progressively through named altitudes; **each altitude is a self-sufficient,
> honest read** — a reader who stops at any altitude has a true, coarser model,
> never a false one (VIS-1: simplify presentation, never content); every
> narrative descends to a **verbatim specification leaf** (RFC7-14), so
> exactness is reachable rather than summarized away. The path bounds
> *browsing*; a claim block's anchor is always **one step** from the owned
> artifact.
>
> The **V0 default ordering** is thesis/manifesto → architecture story →
> capability catalog → capability deep dive → verbatim specification leaf.
> Ordering and altitude count are a **V0 default, not a frozen foundational
> constraint** *(owner decision B7)*: another named narrative under RFC7-6 may
> order its altitudes differently for its audience, bound still by the
> per-altitude obligation and the verbatim-leaf terminus. The primary narrative
> uses the V0 default unless the owner rules otherwise.

**RFC7-14, whole (both paragraphs):**

> **RFC7-14 — The verbatim leaf.** Requirement and scenario text renders
> **verbatim from `openspec/**`** under the artifact contract's own identity
> scheme (RFC3-27, RFC4-10) — never paraphrased, reordered, or summarized in
> normative position. Polaris may present an ordering and annotate around
> requirement text; it may never store a reorganized copy [Observed:
> architecture.md, schema ownership]. The same holds for doctrine rule text.

> **Under a proposed-scenario reading (RFC7-26) the leaf renders the adopted
> text as operative**, with the proposal's delta **adjacent** — visually and
> queryably distinct (RFC6-24), never substituted for it, never interleaved so
> a reader cannot tell which text is which, never anchorable (RFC1-22). The leaf
> is the one place Polaris tells a reader the text before them *is* operative
> (RFC7-12); proposed text there would manufacture the most quotable unadopted
> text in the system. *(Owner decision B5; the rejected alternatives are in
> history.)*

**RFC7-15, whole (the "Thin, never absent" paragraph is RFC7-6's, quoted under RFC7-6 above):**

> **RFC7-15 — Capability catalog honesty.** The catalog projects **declared**
> capability identities (RFC1-14): nothing appears that no declared artifact
> asserts; drafted capabilities render unadopted; unmapped code renders Unknown,
> never silently inferred into a capability [Observed: v1.md]. A
> predominantly-Unknown catalog on an undeclared project is correct output,
> rendered as normal — not broken — with RFC2-24 reasons and resolution routes
> (`missing-declaration` foremost).

**RFC7-17, whole:**

> **RFC7-17 — Bands, machine-distinct; three authority classes, closed.** A deep
> dive composes named bands, each block declaring its band machine-readably
> (RFC7-33). The binding content is the **authority class per band**: every band
> falls in exactly one of three classes, no block straddles two, and no fourth
> class exists. The V0 composition is:
>
> - the **argument band** — authored, non-normative (RFC7-2 (b)): capability
>   thesis and outcome, why it exists (anchored to the motivating principle or
>   decision, never restating it), related capabilities;
> - the **contract band** — referenced, verbatim-reachable: requirement/scenario
>   identities and titles linking to the verbatim leaf, accepted contracts,
>   declared topology placement, active proposal deltas per RFC7-26;
> - the **reality band** — kernel-computed, VIS-2-governed: current status
>   (RFC7-16), implementation mappings with the four SDR-3 classes queryably
>   distinct (RFC1-16), evidence summaries, contradictions and open challenges
>   (first-class in the readable layer — prose must not resolve what
>   adjudication has not), open work, and intent history (adoptions,
>   amendments, dismissals — not a commit log).
>
> **Exactly these three bands, in this order, are the V0 default** *(owner
> decision B7)* — count and ordering are a V0 default, not a frozen constraint;
> the three authority classes are foundational and not negotiable at any V. A
> narrative composing its deep dive differently still assigns every band to one
> of the three classes and declares it machine-readably.

**RFC7-33, excerpt (its first paragraph; the clause continues with non-citability):**

> **RFC7-33 — Every distinction, machine-readable.** Every distinction this
> package draws — **`non-citable` / `presentation-artifact`** (below),
> claim-block kind (anchored / non-normative / labeled), the narrative
> claim-block **type name** (below), band membership and its authority class,
> curated-versus-computed provenance, adopted versus unadopted, editorial-draft
> state, proposal-context membership, review state, RFC7-11(a)'s
> **target-changed** state, label + tier + reason + freshness — is carried as a
> **machine-readable attribute on the rendered unit**, served identically
> through the machine-queryable endpoints (RFC6-13/14) and preserved in
> plain-text or exported renderings [Observed: agents are a first-class consumer
> from day one (vision.md); endpoints are V0-mandatory (v1.md)]. A distinction
> available only to pixels does not survive an endpoint response, a copy-paste
> into an agent prompt, or a reader who cannot see it.

**RFC1-14 and RFC7-19, each whole:**

> **RFC1-14.** **Capability** is the stable product-behavior identity: "a named
> unit of declared behavior that the project's own spec or shape documents
> assert exists, at the granularity a human would use to describe what the
> project does" [Observed: architecture.md, Definitions]. Capability identities
> come only from the project's own declared artifacts; a drafted (unadopted)
> capability renders as unadopted and **may not anchor the map** [Observed:
> v1.md]. Code mapping to no declared capability renders Unknown — never
> silently inferred into a capability.

> **RFC7-19 — Empty is honest.** A block with no content collapses to one honest
> line (what is absent, with its Unknown reason where a claim is implicated) —
> never an empty heading, never a hidden section, never scaffold headings
> manufacturing the document-browser failure over an undeclared capability.

**REQ-polaris-generation-019, excerpt (the sentence on anchors, and the scenario that refuses a path):**

> Canonical anchors SHALL use RFC7-10's target-specific identity, fragment and state representation, distinguishing artifact revision from kernel evaluation and verbatim label/tier/reason.

> #### Scenario: Canonical anchors reject presentation and unstable targets
>
> - **WHEN** a provider supplies a narrative/draft/rendering target, an unknown anchor class or a label/path in place of a durable target and fragment
> - **THEN** validation refuses each invalid anchor instead of coercing it into evidence
> - **AND** valid target-specific variants retain their owning identity and captured revision/state, and opaque presentation IDs are issued with recorded provenance independently of labels

[Inferred] The reason the profile is needed is not that these clauses have no object for an observed repository: they have a defined outcome there. RFC7-6 and RFC7-15 define a predominantly-Unknown catalog under an honestly thin narrative as correct output, and RFC7-19 defines the empty band as one honest line. The profile replaces that defined thin outcome with a defined fuller one; it does not fill a gap. The sentence "alternative named narratives remain subject to the same per-altitude and exact-leaf obligations" does not say what a leaf is where no `openspec/**` exists, and the leaf is, by RFC7-14, "the one place Polaris tells a reader the text before them *is* operative".

## Displaced text

For a non-governed subject only, the requirement displaces this text of REQ-polaris-generation-004 (as amended by the tree-form adoption). Each row quotes the text and says exactly how it is displaced; every other sentence and scenario of 004, and 002, 025 and 030, is unchanged.

| 004 text (quoted from the effective requirement) | How it is displaced for a non-governed subject |
|---|---|
| "Catalog membership SHALL come from declared capabilities, with drafts unadopted and missing declarations explicit" | Kept as a rule; "declared capabilities" is read as (a) states: a maintainer statement in a frozen form, not an adopted Syzygy declaration. A reading, not a replacement (O6) |
| Scenario "Catalog membership comes from declarations", keyed on "adopted capability declarations" | The same (a) reading applies to the scenario as to the clause above: "declared" means a maintainer statement in a frozen form; the code-derived limit the scenario states is kept (O6) |
| "Capability deep dives SHALL preserve RFC7-17's three authority classes and default argument/contract/reality ordering." | The three classes are preserved and each band is assigned to one; the reality-class band is not rendered, and its collapsed line declares the reality class (b) |
| "the contract band SHALL include accepted contract and declared topology-placement references alongside operative requirements/scenarios" | Replaced: the contract-class band holds only admitted maintainer reference spans; no accepted contract, topology or operative requirement exists for the subject |
| "the reality band SHALL retain the four SDR-3 implementation-mapping classes queryably distinct and intent-adoption/amendment/dismissal history, not substitute a commit log" | Not applied: no reality band is rendered, because no kernel evidence drawer exists (RFC7-18); implementation statements stay Inferred prose in the argument band |
| "empty bands SHALL retain an honest absence line" | Kept and extended: a band the profile does not render also gets its line, so a deep dive carries at most two |
| "Required headings, the altitude order, authority bands and verbatim exact-source text keep their structure; a generated summary above verbatim text is marked generated, never replaces that text or presents a paraphrase as it, and leaves the leaf as the owning text." | Kept for headings and altitude order. "Authority bands" is displaced as the rows above state. "Verbatim exact-source text" and "the leaf as the owning text" have no object, since no specification leaf exists; the anchor span of (c) is rendered verbatim, and a generated summary above it is marked generated and never replaces it |
| "Project-specific headings and composition SHALL preserve the existing primary altitude order, authority bands and required populations; missing content SHALL remain honestly absent or Unknown, not invented to fill a template." | Text unchanged, and read with the same displacement as the row above, so that the two sentences naming "authority bands" take one reading: the three authority classes are preserved, the reality-class band is a collapsed line, and a required population the subject does not have is the honest-absence case this sentence already requires [Inferred]. The owner may rule otherwise |
| "alternative named narratives remain subject to the same per-altitude and exact-leaf obligations" | The exact-leaf obligation is replaced by (c): one honest `missing-declaration` line at the leaf altitude and the RFC7-10 anchor as the terminus |
| Scenario "Primary altitudes and one-step source access", outcome "verbatim specification leaf in that order" | The leaf altitude is the honest line of (c); the one-step source access is the anchor |
| Scenario "Capability detail keeps three authority classes", outcomes "its default argument, contract and reality bands appear in that order" and "reality facts come from the shared drawer, the contract band links exact owning text" | No drawer and no owning contract text exist; the contract-class band links maintainer spans, and the reality class is declared by its collapsed line |
| Scenario "Capability bands preserve their actual content populations", outcome "contract exposes its accepted contracts, declared topology placement and operative requirements/scenarios; reality exposes the four distinct SDR-3 mapping classes and adoption/amendment/dismissal history" | The contract and reality populations are not exposed, because the subject has none of them; the missing contents keep the explicit absence or Unknown that the same scenario already requires |

## Proposed meaning

The whole text of the proposed requirement is in
`openspec/changes/polaris-non-governed-narrative-profile/proposed/polaris-generation/spec.md`
(requirement 032 and its twelve scenarios). Three readings, in short:

- **(a)** For an observed non-governed repository a capability is declared only where an admitted source the maintainers wrote, and that is not generated from code, states it in a form the run's frozen profile fixed before discovery, outside the producer. "Maintainer-written, not generated" is made observable by the profile's authored-documentation path classes and generated-file markers. Code, tests, comments, layout and generated reference text alone never declare.
- **(b)** The deep dive keeps the argument band, fills a contract-class band only from admitted reference spans, renders no reality band, and reports each absent band in its own honest line, so at most two lines per deep dive.
- **(c)** There is no verbatim specification leaf. The leaf altitude is one honest `missing-declaration` line, and the byte-exact admitted span is the anchor (RFC7-2 (a)) in RFC7-10's form (target class evidence artifact identifier with integrity digest; identifier the source's content-addressed object identifier; fragment the byte range; target state the admission revision), with repository and path as labels beside it and never inside it, and never called a specification, a leaf or operative.

**Why (a) is a reading of RFC1-14, not a departure from it.** RFC1-14 says capability identities "come only from the project's own declared artifacts" and that a capability is what "the project's own spec or shape documents assert exists". RFC7-15 says "nothing appears that no declared artifact asserts". The profile reads an observed repository's maintainer-written documentation, reference entries and manifests as that repository's "own spec or shape documents", because for a project without Syzygy declarations they are the only artifacts in which its maintainers assert what exists. [Inferred] This is an interpretation: RFC1-14's "spec or shape documents" may be read as requiring a specification, in which case (a) is an extension the owner would have to rule on (packet O6). The profile limits the reading with the same stricter rule the adopted scenario "Catalog membership comes from declarations" applies to code: no capability is invented from code, and generated reference text is code-derived, so it does not declare.

**Why (c) takes the anchor route (RFC7-2 (a)), not the leaf route.** RFC7-13 has every narrative descend to a verbatim specification leaf (RFC7-14), and RFC7-14's second paragraph makes the leaf the one place Polaris says the text before the reader is operative. A maintainer's README is not a specification, and the proposed requirement forbids calling it one; a span that is by its own words not a specification therefore cannot be the leaf. [Inferred] Two lawful routes exist: amend RFC7-13/14 so that a non-governed subject's leaf is its maintainer span (owner question O1, alternative), or, with no contract act, render the leaf altitude as one honest RFC7-19 line and make the span the RFC7-2 (a) anchor. The requirement is drafted on the second; round 1's first draft used the span as "the terminus" and was found to substitute for the leaf. The quote of RFC7-14 above is whole.

**Anchor form (RFC7-10).** The RFC7-10 quote above makes an anchor the typed tuple (target class, target identifier, optional fragment, target state), allows five target classes, and says anchors "embed durable identifiers, never labels, paths, or coordinates"; adopted REQ-polaris-generation-019 refuses "a label/path in place of a durable target and fragment". [Observed] The generator's `generationAnchorId` in `packages/polaris-generation-core/src/generation-source.ts` joins repository id, revision, path, object id and byte range into one string. It is a concatenation, not a digest, and it embeds a repository name and a path, so it is not itself an RFC7-10 anchor. [Inferred] Its object id and byte range map onto RFC7-10's target identifier and fragment, and its revision onto the target state, so a lawful anchor is a projection of those three with the repository and path shown beside it as labels. [Observed] The source record carries no hash-algorithm field: `generationAnchorId` and the record's object identifier are 40 or 64 hex characters, so the algorithm is recoverable from the identifier's length or must be added to the record (see the record-home Unknown in `design.md`). Whether an admitted source object of an observed repository is an "evidence artifact" for RFC7-10's last target class is a reading the owner decides (packet O7); if the owner reads it narrowly, (c) needs a different target class and RFC7-10 an amendment first.

## What explicitly does NOT change

- Requirements 001 to 031: every byte, for all projects, and every meaning and scenario for governed projects; for a non-governed subject only the text under "Displaced text" moves. A governed subject composed under the profile fails (scenario "Governed subject keeps governed readings").
- The primary altitude order and each altitude's independent honesty (004, RFC7-13). The altitude order for a dossier is not decided here.
- RFC7-13, RFC7-14 and RFC1-14: no clause is amended; the profile is drafted as a reading that needs no contract act, with the amendment route left to the owner (O1, O6).
- The three authority classes (RFC7-17): none merges, and no fourth appears. The reality class is not rendered, not redefined.
- The ban on invented motive and the Inferred-premises rule (002); the editorial-draft state and non-citability (RFC7-20).
- Admission: the profile is selected from the admitted project input and the admitted source classes that discovery exposes, by the one predicate in the requirement, and grants no read (020, 025, 030). Consent, egress and retention are untouched.
- "Advantages" framing and the page budget (gap analysis #18, #19): not addressed.

## Warrant

The owner's 2026-10-03 goal for a dossier of `redis/redis` and the gap analysis `docs/polaris-generation/REDIS-DOSSIER-GAP-ANALYSIS.md` section 2, items 1 to 3 and section 6 item 17 (a)-(c). RFC7-13 allows another named narrative bound by "the per-altitude obligation and the verbatim-leaf terminus", and RFC7-6 says a thin narrative over an undeclared project is correct; that latitude concerns ordering and altitude count, and the profile does not rest on it to excuse the leaf. The delta is a draft for the owner; it is not itself a ruling.

## Evidence or decision basis

`docs/polaris-generation/REDIS-DOSSIER-GAP-ANALYSIS.md` (Research note, binds nothing); `docs/polaris-generation/TARGETS.md`; the quoted requirement and RFC text above. No target repository body was read in drafting.

## Terms introduced / retired

Introduced: "non-governed narrative profile", "frozen declaration form", "contract-class band". Each is defined in the requirement's own text; none is entered in the term registry by this delta [Inferred: the registry is a candidate]. Retired: none.

## Downstream impact

Method and populations are in `IMPACT-LEDGER.md` (regexes published, counts computed by script at `9a6e8e31`). Summary [Observed]: requirement 004 is cited by identifier or continuation in 52 files and in 63 counting the prose short form, the title form and the range form (78 with the bare `REQ-004` form of sweep H); no byte-bound file needs editing for this candidate to exist. The candidate does need one existence-time edit outside the package, a row for its directory in `openspec/README.md`, which `scripts/check_spec_reconciliation.py --check` (R5) requires and which round 1 found missing; the row says the change is a candidate. Adoption touches the count sentence in `PROJECT-STATUS.md` (32 requirements, 194 scenarios), the recount and reconciliation tooling, the generated `DIRECTIVE-REGISTER.md` and the dependency-union script.

## Migration / supersession plan

Nothing is superseded. On adoption, one logical change (CC-REV-2): move the spec from `proposed/` to `specs/polaris-generation/`; generalize the recount script's base/overlay classification; update the status count; regenerate the register and union. The adopted change directories stay at their bound paths. No digest-bound artifact is touched by this candidate. If adoption instead edits requirement 004 in place, as the tree-form adoption did, that edit touches a bound file and needs its own regeneration and re-review cycle; this candidate avoids it by being additive.

## Review
**Required class:**  CC-REV-1 fresh context; CC-REV-4 as applicable to a spec delta
**Reviewer:**        fresh context per round; the round-1 and round-2 raws are retained in `reviews/`, and the round-3 raw is retained there with its dispositions
**Verdict:**         round 1 REVISE; round 2 REVISE; round 3 CONFIRM WITH EXCEPTIONS (notes only). The verdict of record is each raw's own `Verdict:` line
