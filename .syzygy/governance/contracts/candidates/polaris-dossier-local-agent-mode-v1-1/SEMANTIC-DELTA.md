> **Candidate — binds nothing.** This semantic delta is drafted under bead
> `syzygy-qkea.1` and CC-REV-2. It performs no act, amends no signed byte and
> authorizes no implementation. Version 1.0 of
> `polaris-dossier-local-agent-mode` stays in force until the owner signs off
> version 1.1 after a fresh independent review of these exact bytes.

# Semantic delta DOSSIER-LOCAL-AGENT-1.1 — the round-3 notes made normative

Version 1.1 writes into the signed specification what the v1.0 sign-off
carried as implementation obligations and "later amendment" lines: D9's
credential condition becomes a keeping obligation checked at every step, the
host and attendance declaration gets a named source, the non-permitting brief
states SEC-3's rule to the agent in words it can follow, and the records
Syzygy reads for its gates are disclosed as within the sessions' reach. One
further change, D9's note N6, is drafted as a separate hunk that goes in only
if the owner accepts it.

**Artifact(s):** the signed change
`openspec/changes/polaris-dossier-local-agent-mode/`, at its v1.0 bytes on
`main` (`55daf6ce`, tag `polaris-dossier-local-agent-mode-v1.0`). Three files
move, by the patches under `proposed/`:

- `specs/polaris-generation/spec.md` (`spec.md.patch`);
- `design.md` (`design.md.patch`);
- `proposal.md` (`proposal.md.patch`).

`GOVERNING-DEPENDENCIES.md` is regenerated on install
(`check_spec_reconciliation.py --regenerate`), and gains one contract row,
RFC5-12. `tasks.md` is unchanged. The optional hunk,
`spec.md.n6-optional.patch`, applies on top of `spec.md.patch` and touches
only `spec.md`.

**Stable IDs affected:** REQ-polaris-generation-033, amended in place
(requirement text, three scenarios edited, three scenarios added, the
falsifier, the case and the warrant block). REQ-polaris-generation-034,
amended in place (one clause of its first paragraph). REQ-polaris-generation-035
and 036 are unchanged. No identifier is minted, retired, renamed or
renumbered, and no requirement title changes.

**Change class:** **Normative.** An implementation that conforms to v1.0 may
check credentials only at `check` and `close`, issue a permitting brief on
`operatorIsOwner` alone, quote SEC-3's adopted head sentence as the whole of a
non-permitting brief's rule, and restate D9's cost in its own words. Each of
those fails v1.1.

**Author:** agent drafting for bead `syzygy-qkea.1` (lane-doctrine).

**Date:** 2026-10-06, drafted over v1.0 as signed at `55daf6ce`, after D9's
adoption at `cf2a894b`.

## Sources

Every item below comes from one of two records, and each says which:

- the v1.0 notes record,
  `.syzygy/governance/contracts/candidates/POLARIS-DOSSIER-LOCAL-AGENT-MODE-REVIEW-NOTES.md`,
  for round-3 findings 1 to 9 of
  `docs/reviews/R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-3-RAW.md` ("R3-F*n*");
- D9's notes record,
  `.syzygy/governance/contracts/candidates/DOCTRINE-AMENDMENT-D9-REVIEW-NOTES.md`,
  for its notes N5 and N6.

The owner adopted D9 on 2026-10-06 with its credential condition kept
(Q3 (b); `.syzygy/governance/decisions/DOCTRINE-AMENDMENT-LOG.md`, row D9).
SEC-3 as adopted is the reference text for every SEC-3 quotation below.

## Current meaning

At v1.0, REQ-polaris-generation-033:

- checks adapter credentials "before it issues a brief that permits execution,
  at every later check and at close", reading "every credential that
  Syzygy's configuration holds for its typed adapters", and holds Syzygy to no
  keeping obligation;
- names no source for the conditions "the authoring session is one the owner
  started on the owner's own host and attends", beyond the attendance
  sentence "whether the owner attended is the operator's declaration,
  labelled Inferred";
- has the run record carry "the cost D9 states" as a restatement that omits
  "Observed code it runs can reach them" and "Nothing contains it, so it
  gives none of a profile's guarantees";
- says the agent's per-run choice can be entered by no one but the operator
  only implicitly ("Syzygy cannot observe who ran the command");
- has a non-permitting brief "quote SEC-3's rule that observed-project code
  runs only inside an explicit, opt-in execution profile", a sentence SEC-3
  no longer contains: as adopted, its head reads "Syzygy runs observed-project
  code only inside an explicit, opt-in execution profile";
- does not distinguish the per-run choice from an execution consent;
- establishes that a consent, policy act or ruling is "in force" without
  saying how, and discloses nothing about the records it reads for its gates
  being within the sessions' reach;
- says nothing of the skill and Codex texts beyond "The skill and agent texts
  SHALL tell the agent never to run that command."

Its scenario "Governed subject without a per-project provider statement"
reads "an adopted capability declaration", while the requirement counts every
`.syzygy/` path "adopted or not".

## Proposed meaning

Each item names its source, then what the text does.

1. **R3-F1, the credential condition.** "Syzygy SHALL NOT, from the issue of
   a brief that permits execution, hold or write a typed-adapter credential
   where the operator's user can read it". The read runs "before it issues
   such a brief and at every later step it takes for the run (each check,
   inventory check, review check and render, and close)", over "every
   credential that Syzygy holds for its typed adapters". The list comes from
   "a source the disclosure names", which is disclosed as within the agent
   sessions' write reach. Readability "between checks, after close, through
   privilege escalation or by another route is Inferred and disclosed". The
   scenario "Adapter credential readable" and the falsifier follow.
   The keeping obligation has no end: it holds from the first permitting
   brief on. That matches the recommended answer to D9's note N2 ("once
   Syzygy holds one, it is kept from your user account permanently"); if the
   owner rules N2 otherwise, this sentence needs a new version.
2. **R3-F2, the declaration.** The command that records the choice "SHALL
   record the operator's declaration that the owner started the authoring
   session on the owner's own host and attends it; Syzygy SHALL issue no
   permitting brief without that declaration". It is Inferred, attributed to
   the operator, disclosed beside the choice, added to the record rule's
   Inferred list and named in the run record. Two scenarios are added,
   "Permitting brief without the host and attendance declaration" and
   "Permitting brief carries its lapse statement", and the falsifier gains
   the two arms the finding asked for.
3. **R3-F3, D9's cost.** The run record carries "the cost D9 states, quoted
   verbatim from SEC-3's bullet "What the permitted case costs" as adopted in
   `security.md`, never restated or abridged". The restatement is deleted.
4. **R3-F4, who can enter the choice.** "the authoring agent, which runs the
   neighbouring commands, could run that command itself or write its record
   into the state directory, and only the skill and agent texts forbid it."
   This is a disclosure, not a new mechanism: the stronger design the finding
   mentions (a typed confirmation from a controlling terminal) may exclude
   the `!` launch form 033 admits, and is not proposed.
5. **R3-F5, the non-permitting brief.** It "SHALL quote SEC-3's head sentence
   as adopted, cite SEC-3, and state the rule as it applies to the agent, in
   its own words: do not build or run the observed project outside an
   explicit, opt-in execution profile". The inventory brief, packets and
   session prompts carry the rule "in that form"; 034's brief clause and two
   scenarios follow.
6. **R3-F7, not an execution consent.** "The choice SHALL NOT be read, stored
   or reported as an execution consent (RFC5-12; the base change's
   `SOURCE-POLICY.md`: "Execution consent is per project for an exact
   approved execution-profile version."), and it approves no execution
   profile." RFC5-12 joins 033's contract warrants.
7. **R3-F8, the gate inputs.** "Syzygy SHALL establish that the observation
   consent, the registry entry, each policy act, any per-project statement,
   D9 and the owner's reading of RFC7-20 are in force from the record of the
   owner's act that makes each effective (RFC3-16: "Effective status is read
   from the owner-act record, not from the stamp"), never from a status word
   or a file's presence." The disclosure list gains "that the records Syzygy
   read for its gates …, and where execution was permitted the source of the
   credential list, lie within the agent sessions' write reach". The scenario
   "Gate records established from owner acts" says what "not in force" does
   for each input: a missing consent, registry entry, policy act or statement
   refuses its step; D9 not in force gives a non-permitting brief; the
   RFC7-20 reading not in force renders an operator-computed draft layer
   Unknown.
8. **R3-F9, editorial residues.** The scenario reads "a capability
   declaration or declared topology, or any `.syzygy/` path, adopted or not";
   the proposal's "Modified in effect" list adds 021, `OWNER-FLOW.md` and
   `SECURITY-CONTRACT.md`, with the sections 033 names; the skill's
   description reads "for any repository the operator holds the consents
   for".
9. **D9-N5, the skill sentence.** "The `/polaris-dossier` skill and the Codex
   instructions SHALL NOT grant execution themselves: they SHALL only defer
   to the execution rule in the run's `brief.md`, and absent that brief SHALL
   state that the observed project is not to be built or run outside an
   explicit, opt-in execution profile."
10. **E1, banners now false.** The spec's head paragraph, `design.md`'s and
    `proposal.md`'s banners said "Candidate — binds nothing", "not adopted",
    and that D9 "is not adopted". After the v1.0 sign-off and D9's adoption
    each is false in bytes no one may edit outside a new version. Version 1.1
    states the version, the v1.0 sign-off and D9's adoption, and that these
    bytes bind only by the v1.1 sign-off. This item is not in the notes
    records; it is drafted here because v1.1 is the only lawful place to
    correct those sentences, and the owner may drop it without touching any
    other item.
11. **Optional: D9-N6, reported commands outside the named scope.** Only in
    `spec.md.n6-optional.patch`, and only if the owner accepts N6. Where
    execution was permitted, each reported command carries its reported
    working directory and the agent's statement of whether it falls within
    the choice's scope; Syzygy flags, as an Inferred finding disclosed beside
    the command, every command reported outside the clone, with no working
    directory, or stated by the agent to fall outside the scope. "A flag
    refuses no step and hides no command." One scenario and one falsifier arm
    are added. Whether a command "builds or runs the observed project" is not
    mechanically decidable from a self-reported command line, so the flag
    rests on two observable proxies and the agent's own statement; it can
    miss an out-of-scope command run inside the clone that the agent calls
    in scope.

### Not carried

- **R3-F6** (the RFC5-24 line): drafted only for the case where the owner
  declined D9's Q3 (b). The owner kept Q3 (b), so it drops out.
- The three package-prose residues of R3-F9 (the v1.0 impact ledger's "No
  overlap" line, the v1.0 delta's "retained by the lead", the v1.0 packet's
  credential-check timing) sit in the v1.0 candidate package, whose bytes the
  v1.0 sign-off read. They are corrected here, not edited there:
  - the governed predicate *is* an overlap with REQ-polaris-generation-032,
    which the proposal and 033 record;
  - the second review raw is on `main` at
    `docs/reviews/R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-2-RAW.md`;
  - at v1.0 the credential read ran before the brief, at every check and at
    close; under v1.1 it runs at every step.
- R3-F8's and R3-F1's implementation obligations stand as written in the
  notes record; this delta makes their normative halves binding and changes
  neither obligation.

## What explicitly does NOT change

- REQ-polaris-generation-035 and 036, every adopted requirement 001–032, and
  the base and understanding changes.
- The permitted case's conditions (D9 in force; the operator is the owner,
  attending a session the owner started on the owner's host; a per-run
  choice recorded before the brief; the credential condition): v1.1 names
  the source of one declaration and the steps of one check, and adds none.
- RFC7-20 and SEC-2 as read under the owner's rulings; the round-1, round-2
  and round-3 items carried to the owner at v1.0 are not reopened.
- The `!` launch form for inventory and review sessions.
- No doctrine, contract or policy text, and no implementation code.

## Warrant

- **D9 as adopted** (SEC-3's conditions list and its "What the permitted case
  costs" bullet) for items 1, 3 and 9.
- **SEC-3** for item 5; **RFC5-12** and the base change's `SOURCE-POLICY.md`
  for item 6; **RFC3-16** for item 7.
- **VIS-1, VIS-2** for the disclosures in items 1, 2, 4 and 7: a value Syzygy
  cannot observe is Inferred and said so.
- **CC-REV-2** (an amendment of a signed specification travels as a new
  version with its own review) and the owner's direction
  `OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02`, as extended to
  Polaris generator deltas by the v1.0 selection.

## Evidence or decision basis

- R3 findings 1–9, verbatim in the raw named above; their dispositions in
  the v1.0 notes record ("The other round-3 notes").
- D9 notes N5 and N6, and the owner's adoption with Q3 (b).
- [Observed, this session at `55daf6ce`] the post-apply bytes validate under
  `openspec validate polaris-dossier-local-agent-mode --strict` (OpenSpec
  1.9.0) with and without the N6 hunk; the effective Polaris composition is
  35 requirements and 230 scenarios (231 with N6), against 35 and 227 at
  v1.0 (`scripts/count_polaris_effective_scenarios.py`).

## Terms introduced / retired

- **The operator's declaration** (that the owner started the authoring
  session on the owner's own host and attends it): introduced, as a value
  the dedicated command records.
- **The agent-directed statement** of SEC-3's rule: introduced, as the form a
  non-permitting brief carries.
- Nothing retired.

## Downstream impact

See `IMPACT-LEDGER.md`. In short: three files of one change move, one
generated file is regenerated, the reconciliation census is regenerated, no
implementation code cites the changed text yet, and the implementation
slices written against v1.0 gain obligations that they already carry as
implementation obligations from the notes record.

## Migration / supersession plan

- The v1.1 sign-off is recorded the way v1.0 was: the recorder applies the
  three patches (and the N6 hunk if accepted) through a builder, writes a
  v1.1 record and aggregate block, and `--regenerate` refreshes the union and
  the census. v1.0's record is never edited.
- **Prerequisites that do not exist yet** (scripts, outside this package):
  a builder for this package's patches and its entry in
  `record_versioned_signoff.py`'s `real_packages()`; the reconciliation's
  handling of a second version-tagged record for an installed Polaris
  addition (today `check_spec_reconciliation.py` treats a signed addition's
  records by package and version, and v1.0's applied-tree check reads the
  v1.0 bytes, which v1.1 replaces). The PWB successor chain is the precedent.
- The implementation slices keep the v1.0 tests; once v1.1 is signed, the
  tests that pin R3-F1, F2, F3, F5, F7, F8 and N5 obligations become
  conformance tests of normative text.

## Review

Fresh-context review rounds on the default model, at most three, under
`REVIEW-BRIEF.md`. Raws are stored verbatim under `docs/reviews/` as
`R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-V1-1-<n>-RAW.md`.
