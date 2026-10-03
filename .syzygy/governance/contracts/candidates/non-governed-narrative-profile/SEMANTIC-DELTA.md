# Semantic delta POLARIS-NGNP-1 — Non-governed narrative profile

> **Candidate — binds nothing.** A proposal in the form of
> `contracts/candidates/policy-candidates/SEMANTIC-DELTA-TEMPLATE.md`. An agent
> drafted it; adoption belongs to the owner.

**Artifact(s):**         `openspec/changes/polaris-non-governed-narrative-profile/proposed/polaris-generation/spec.md` (new); no existing file is edited
**Stable IDs affected:**  REQ-polaris-generation-032 (new). REQ-polaris-generation-004 (as amended by the tree-form adoption) is affected in effect, not in bytes: for a non-governed subject the new requirement displaces three of 004's readings, so 004 alone no longer states the rule for that class. Read against RFC1-14, RFC7-2, RFC7-6, RFC7-13, RFC7-14, RFC7-15, RFC7-17, RFC7-19. No RFC and no byte of 004 is edited.
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

Quoted from the RFC clauses the profile reads against (`.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`, and RFC1-14 in `RFC-0001-project-graph-identity-state-planes.md`), each whole:

> **RFC7-13 — Progressive disclosure: the obligation, and a V0 default path.**
> The binding content is the obligation **per altitude**: a narrative discloses
> progressively through named altitudes; **each altitude is a self-sufficient,
> honest read** — a reader who stops at any altitude has a true, coarser model,
> never a false one (VIS-1: simplify presentation, never content); every
> narrative descends to a **verbatim specification leaf** (RFC7-14), so
> exactness is reachable rather than summarized away. The path bounds
> *browsing*; a claim block's anchor is always **one step** from the owned
> artifact.

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

> **RFC7-15 — Capability catalog honesty.** The catalog projects **declared**
> capability identities (RFC1-14): nothing appears that no declared artifact
> asserts; drafted capabilities render unadopted; unmapped code renders Unknown,
> never silently inferred into a capability [Observed: v1.md]. A
> predominantly-Unknown catalog on an undeclared project is correct output,
> rendered as normal — not broken — with RFC2-24 reasons and resolution routes
> (`missing-declaration` foremost).

> **Thin, never absent.** On an undeclared or thin project the primary narrative
> may be **thin, or Syzygy-drafted and unadopted (RFC7-20), but never absent**: a
> predominantly-Unknown catalog under an honestly thin narrative is correct
> output (RFC7-15, RFC7-31) on v1.md's proving ground — "real, messy, already
> running, mostly undeclared" [Observed: v1.md]. Absence is not thinness; it is
> a missing front door, and it fails RFC7-30 rather than passing it trivially.

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

[Inferred] These clauses and the requirement have no object for an observed repository with no Syzygy declarations, no `openspec/**` and no kernel evidence drawer *in the sense the proposal needs*: they do have a defined outcome. RFC7-6 and RFC7-15 define a predominantly-Unknown catalog under an honestly thin narrative as correct output, and RFC7-19 defines the empty band as one honest line. The proposal replaces that defined thin outcome with a defined fuller one; it does not fill a gap. The sentence "alternative named narratives remain subject to the same per-altitude and exact-leaf obligations" does not say what a leaf is where no `openspec/**` exists, and the leaf is, by RFC7-14, "the one place Polaris tells a reader the text before them *is* operative".

## Proposed meaning

The whole text of the proposed requirement is in
`openspec/changes/polaris-non-governed-narrative-profile/proposed/polaris-generation/spec.md`
(requirement 032 and its twelve scenarios). Three readings, in short:

- **(a)** For an observed non-governed repository a capability is declared only where an admitted source the maintainers wrote, and that is not generated from code, states it in a form the run's frozen profile fixed before discovery, outside the producer. "Maintainer-written, not generated" is made observable by the profile's authored-documentation path classes and generated-file markers. Code, tests, comments, layout and generated reference text alone never declare.
- **(b)** The deep dive keeps the argument band, fills a contract-class band only from admitted reference spans, renders no reality band, and reports each absent band in its own honest line, so at most two lines per deep dive.
- **(c)** There is no verbatim specification leaf. The leaf altitude is one honest `missing-declaration` line, and the byte-exact admitted span is the anchor (RFC7-2 (a)) under repository, revision, path, span and digest, never called a specification, a leaf or operative.

**Why (a) is a reading of RFC1-14, not a departure from it.** RFC1-14 says capability identities "come only from the project's own declared artifacts" and that a capability is what "the project's own spec or shape documents assert exists". RFC7-15 says "nothing appears that no declared artifact asserts". The profile reads an observed repository's maintainer-written documentation, reference entries and manifests as that repository's "own spec or shape documents", because for a project without Syzygy declarations they are the only artifacts in which its maintainers assert what exists. [Inferred] This is an interpretation: RFC1-14's "spec or shape documents" may be read as requiring a specification, in which case (a) is an extension the owner would have to rule on (packet O6). The profile limits the reading with the same stricter rule the adopted scenario "Catalog membership comes from declarations" applies to code: no capability is invented from code, and generated reference text is code-derived, so it does not declare.

**Why (c) takes the anchor route (RFC7-2 (a)), not the leaf route.** RFC7-13 has every narrative descend to a verbatim specification leaf (RFC7-14), and RFC7-14's second paragraph makes the leaf the one place Polaris says the text before the reader is operative. A maintainer's README is not a specification, and the proposed requirement forbids calling it one; a span that is by its own words not a specification therefore cannot be the leaf. [Inferred] Two lawful routes exist: amend RFC7-13/14 so that a non-governed subject's leaf is its maintainer span (owner question O1, alternative), or, with no contract act, render the leaf altitude as one honest RFC7-19 line and make the span the RFC7-2 (a) anchor. The requirement is drafted on the second; round 1's first draft used the span as "the terminus" and was found to substitute for the leaf. The quote of RFC7-14 above is whole.

## What explicitly does NOT change

- Requirements 001 to 031: every byte, meaning and scenario, for governed projects. A governed subject composed under the profile fails (scenario "Governed subject keeps governed readings").
- The primary altitude order and each altitude's independent honesty (004, RFC7-13). The altitude order for a dossier is not decided here.
- RFC7-13, RFC7-14 and RFC1-14: no clause is amended; the profile is drafted as a reading that needs no contract act, with the amendment route left to the owner (O1, O6).
- The three authority classes (RFC7-17): none merges, and no fourth appears. The reality class is not rendered, not redefined.
- The ban on invented motive and the Inferred-premises rule (002); the editorial-draft state and non-citability (RFC7-20).
- Admission: the profile is chosen from the admitted observation record and grants no read (020, 025, 030). Consent, egress and retention are untouched.
- "Advantages" framing and the page budget (gap analysis #18, #19): not addressed.

## Warrant

The owner's 2026-10-03 goal for a dossier of `redis/redis` and the gap analysis `docs/polaris-generation/REDIS-DOSSIER-GAP-ANALYSIS.md` section 2, items 1 to 3 and section 6 item 17 (a)-(c). RFC7-13 allows another named narrative bound by "the per-altitude obligation and the verbatim-leaf terminus", and RFC7-6 says a thin narrative over an undeclared project is correct; that latitude concerns ordering and altitude count, and the profile does not rest on it to excuse the leaf. The delta is a draft for the owner; it is not itself a ruling.

## Evidence or decision basis

`docs/polaris-generation/REDIS-DOSSIER-GAP-ANALYSIS.md` (Research note, binds nothing); `docs/polaris-generation/TARGETS.md`; the quoted requirement and RFC text above. No target repository body was read in drafting.

## Terms introduced / retired

Introduced: "non-governed narrative profile", "frozen declaration form", "contract-class band". Each is defined in the requirement's own text; none is entered in the term registry by this delta [Inferred: the registry is a candidate]. Retired: none.

## Downstream impact

Method and populations are in `IMPACT-LEDGER.md` (regexes published, counts computed by script at `9a6e8e31`). Summary [Observed]: requirement 004 is cited by identifier or continuation in 52 files and in 60 counting the prose short form and the title form; no byte-bound file needs editing for this candidate to exist. The candidate does need one existence-time edit outside the package, a row for its directory in `openspec/README.md`, which `scripts/check_spec_reconciliation.py --check` (R5) requires and which round 1 found missing; the row says the change is a candidate. Adoption touches the count sentence in `PROJECT-STATUS.md` (32 requirements, 194 scenarios), the recount and reconciliation tooling, the generated `DIRECTIVE-REGISTER.md` and the dependency-union script.

## Migration / supersession plan

Nothing is superseded. On adoption, one logical change (CC-REV-2): move the spec from `proposed/` to `specs/polaris-generation/`; generalize the recount script's base/overlay classification; update the status count; regenerate the register and union. The adopted change directories stay at their bound paths. No digest-bound artifact is touched by this candidate. If adoption instead edits requirement 004 in place, as the tree-form adoption did, that edit touches a bound file and needs its own regeneration and re-review cycle; this candidate avoids it by being additive.

## Review
**Required class:**  CC-REV-1 fresh context; CC-REV-4 as applicable to a spec delta
**Reviewer:**        not yet assigned; must not share the drafting session
**Verdict:**         none — no review has been run
