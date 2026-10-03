# Semantic delta POLARIS-NGNP-1 — Non-governed narrative profile

> **Candidate — binds nothing.** A proposal in the form of
> `contracts/candidates/policy-candidates/SEMANTIC-DELTA-TEMPLATE.md`. An agent
> drafted it; adoption belongs to the owner.

**Artifact(s):**         `openspec/changes/polaris-non-governed-narrative-profile/proposed/polaris-generation/spec.md` (new); no existing file is edited
**Stable IDs affected:**  REQ-polaris-generation-032 (new). Read against REQ-polaris-generation-004 (as amended by the tree-form adoption), RFC7-13, RFC7-14, RFC7-17, RFC7-19. Neither RFC nor requirement 004 is edited.
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

Quoted from RFC7-14 and RFC7-19 (`.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`):

> **RFC7-14 — The verbatim leaf.** Requirement and scenario text renders
> **verbatim from `openspec/**`** under the artifact contract's own identity
> scheme (RFC3-27, RFC4-10) — never paraphrased, reordered, or summarized in
> normative position. Polaris may present an ordering and annotate around
> requirement text; it may never store a reorganized copy [Observed:
> architecture.md, schema ownership]. The same holds for doctrine rule text.

> **RFC7-19 — Empty is honest.** A block with no content collapses to one honest
> line (what is absent, with its Unknown reason where a claim is implicated) —
> never an empty heading, never a hidden section, never scaffold headings
> manufacturing the document-browser failure over an undeclared capability.

[Inferred] As written, these have no object for an observed repository with no Syzygy declarations, no `openspec/**` and no kernel evidence drawer. The sentence "alternative named narratives remain subject to the same per-altitude and exact-leaf obligations" does not say what a leaf is where no `openspec/**` exists.

## Proposed meaning

The whole text of the proposed requirement is in
`openspec/changes/polaris-non-governed-narrative-profile/proposed/polaris-generation/spec.md`
(requirement 032 and its eight scenarios). Three readings, in short:

- **(a)** For an observed non-governed repository a capability is declared only where an admitted maintainer-authored source states it in a form the run's frozen profile fixed before discovery. Code, tests, comments and layout alone never declare.
- **(b)** The deep dive keeps the argument band, fills a contract-class band only from admitted reference spans, renders no reality band, and reports every absent band in one line per deep dive.
- **(c)** The terminus is the byte-exact admitted span under repository, revision, path, span and digest, never called a specification.

## What explicitly does NOT change

- Requirements 001 to 031: every byte, meaning and scenario, for governed projects. A governed subject composed under the profile fails (scenario "Governed subject keeps governed readings").
- The primary altitude order and each altitude's independent honesty (004, RFC7-13). The altitude order for a dossier is not decided here.
- The three authority classes (RFC7-17): none merges, and no fourth appears. The reality class is not rendered, not redefined.
- The ban on invented motive and the Inferred-premises rule (002); the editorial-draft state and non-citability (RFC7-20).
- Admission: the profile is chosen from the admitted observation record and grants no read (020, 025, 030). Consent, egress and retention are untouched.
- "Advantages" framing and the page budget (gap analysis #18, #19): not addressed.

## Warrant

The owner's 2026-10-03 goal for a dossier of `redis/redis` and the gap analysis `docs/polaris-generation/REDIS-DOSSIER-GAP-ANALYSIS.md` section 2, items 1 to 3 and section 6 item 17 (a)-(c). RFC7-13 allows another named narrative bound by "the per-altitude obligation and the verbatim-leaf terminus", and RFC7-6 says a thin narrative over an undeclared project is correct. The delta is a draft for the owner; it is not itself a ruling.

## Evidence or decision basis

`docs/polaris-generation/REDIS-DOSSIER-GAP-ANALYSIS.md` (Research note, binds nothing); `docs/polaris-generation/TARGETS.md`; the quoted requirement and RFC text above. No target repository body was read in drafting.

## Terms introduced / retired

Introduced: "non-governed narrative profile", "frozen declaration form", "contract-class band". Each is defined in the requirement's own text; none is entered in the term registry by this delta [Inferred: the registry is a candidate]. Retired: none.

## Downstream impact

Method and populations are in `IMPACT-LEDGER.md` (regexes published, counts computed). Summary [Observed]: no byte-bound file needs editing for this candidate to exist; adoption touches the count sentence in `PROJECT-STATUS.md`, the recount and reconciliation tooling, the generated `DIRECTIVE-REGISTER.md` and the dependency-union script.

## Migration / supersession plan

Nothing is superseded. On adoption, one logical change (CC-REV-2): move the spec from `proposed/` to `specs/polaris-generation/`; generalize the recount script's base/overlay classification; update the status count; regenerate the register and union. The adopted change directories stay at their bound paths. No digest-bound artifact is touched by this candidate. If adoption instead edits requirement 004 in place, as the tree-form adoption did, that edit touches a bound file and needs its own regeneration and re-review cycle; this candidate avoids it by being additive.

## Review
**Required class:**  CC-REV-1 fresh context; CC-REV-4 as applicable to a spec delta
**Reviewer:**        not yet assigned; must not share the drafting session
**Verdict:**         none — no review has been run
