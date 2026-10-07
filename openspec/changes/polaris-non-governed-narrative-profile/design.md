# Reading governed narrative obligations for an observed repository

> **Candidate — binds nothing.** Explains the placement of the candidate
> requirement in `specs/polaris-generation/spec.md`; not adopted.

**A non-governed subject keeps every altitude and every honesty obligation;
it changes only what counts as a declaration, which bands exist and what the
exact-source terminus quotes.** This file explains the placement. Observable
commitments live in `specs/polaris-generation/spec.md`. Source doctrine,
accepted contracts and the adopted requirements remain controlling.

## The problem in three places

| Governed obligation | Quoted from | What the profile replaces, and why |
|---|---|---|
| Catalog membership "SHALL come from declared capabilities" | REQ-polaris-generation-004 | The adopted text defines a thin, predominantly Unknown catalog as correct output (RFC7-15), so the outcome is defined; the profile replaces it with a fuller one in which a maintainer statement in a frozen form declares. |
| Deep dives keep argument, contract and reality bands; empty bands "retain an honest absence line" | REQ-polaris-generation-004; RFC7-17, RFC7-19 | The contract band names accepted contracts and topology, and the reality band is computed by the kernel's evidence drawer (RFC7-18); a non-governed subject has neither. The profile fills the contract-class band from maintainer reference spans and renders no reality band. |
| Every narrative descends to a verbatim specification leaf, rendered "verbatim from `openspec/**`" | RFC7-13, RFC7-14 | A non-governed subject has no `openspec/**` and no specification, so the verbatim leaf has no text to quote. The profile replaces the leaf altitude with one honest line. |

## Decisions in this change

1. **Declared means maintainer-stated in an admitted source, by a form fixed
   in advance and outside the producer.** The run's frozen profile lists
   eligible forms, authored-documentation path classes and generated-file
   markers before discovery; the operator, owner or evaluation harness fixes
   it, not the producer. This keeps the catalog out of the producer's hands:
   the independent oracle can be written from the sources and the forms before
   a draft exists (requirement 014's independence). A late-found section is
   reported, not promoted. A committed reference generated from code is not a
   declaration, or a producer could launder a code-derived list through a
   declaration form; path class and marker stand for "maintainer-written"
   because an authorship judgment cannot be settled mechanically. Code-only
   suggestions stay unadopted Inferred drafts, which the adopted scenario
   "Catalog membership comes from declarations" already requires. The reading
   of RFC1-14 ("the project's own spec or shape documents") is argued in the
   semantic delta, not assumed.
2. **Bands: render what exists, say once per band what does not.** The
   argument band always applies. The contract-class band is referenced
   material, so maintainer reference spans can fill it honestly. The reality
   band is kernel-computed by definition (RFC7-17, RFC7-18), so the profile
   does not render one, and implementation statements stay Inferred in the
   argument band. RFC7-19 speaks per block ("A block with no content collapses
   to one honest line"), so each absent band gets its own line: at most two
   per deep dive, since the argument band always applies. Not rendering a band
   is lawful under RFC7-17, which makes count and ordering a V0 default and
   binds the class assignment, not the number of bands [Inferred]. The line
   must never say "no contract exists", because absence of an admitted span is
   Unknown, not negative.
3. **No leaf; the anchor is the terminus.** RFC7-13 has every narrative descend
   to a verbatim specification leaf, and RFC7-14 makes the leaf "the one place
   Polaris tells a reader the text before them *is* operative". A maintainer's
   README is not a specification, so putting it in the leaf position would
   assert operativeness it does not have. The profile therefore renders the
   leaf altitude as one honest line (RFC7-19, reason `missing-declaration`)
   and makes the byte-exact admitted span the anchor of RFC7-2 (a), reachable
   in one step and never called a leaf or specification [Inferred]. This needs
   no contract amendment, provided the anchor has RFC7-10's form: a target
   class, a target identifier, a fragment and a target state, with no path or
   label inside it. The profile takes the source's content-addressed object
   identifier as the identifier, the byte range as the fragment and the
   admission revision as the state. [Observed] The generator's
   `generationAnchorId` joins repository id, revision, path, object id and
   range into one string, so it is not that anchor; an implementation projects
   the three fields and shows repository and path as labels. Whether a source
   object of an observed repository is an "evidence artifact" in RFC7-10's
   sense is packet O7. Whether the owner would rather read RFC7-13/14 so
   that the span is the leaf itself is put as packet O1; that reading would
   need those clauses amended first.

## Known residuals

- **Laundering through an unmarked generated file.** Path class and marker are
  necessary conditions for "maintainer-written and not generated", not
  sufficient ones. A reference generated from code and committed without any
  marker the frozen profile lists, under an authored-documentation path,
  passes the observable while (a) forbids it. On prepared snapshots the
  oracle decides it, because the snapshot's authorship is known; in
  production only the frozen profile's marker list stands between the two, so
  the profile is as good as that list. The spec states no stronger guarantee.
- **Record homes are Unknown.** The frozen profile is a new run-control
  record, and the selection predicate needs the project input to state
  whether an evidence drawer exists. [Unknown] whether the interchange
  records of REQ-polaris-generation-019 can carry either without a schema
  change; if not, the change is an implementation path that no act authorizes
  here, as for the glossary (packet O5). It is listed in `tasks.md`.

## What stays unchanged

Primary altitude order (RFC7-13's default, with the owner free to rule
otherwise), the editorial-draft state (RFC7-20), the one-step anchor rule,
glossary and diagram obligations, REQ-002's ban on invented motive, and
admission and consent. The profile adds no read, egress or write.

## Placement

One added requirement in the existing `polaris-generation` capability. The
change is held in `proposed/` until adoption (see the proposal). The
semantic delta, impact ledger, review brief and owner packet are in
`.syzygy/governance/contracts/candidates/non-governed-narrative-profile/`.
