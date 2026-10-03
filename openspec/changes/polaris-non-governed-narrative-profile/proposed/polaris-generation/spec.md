# Polaris non-governed narrative profile

Candidate exact behavioral delta; not yet adopted, binds nothing. This change applies to the existing polaris-generation capability. It adds one requirement. It edits no byte of any predecessor requirement or scenario, in the base change or in the understanding amendment as amended by the tree-form adoption, but for a non-governed subject it displaces three readings of REQ-polaris-generation-004, so that requirement's effective meaning changes for that class of subject and 004 is read together with this one. For a governed subject every predecessor requirement and scenario keeps its bytes and its meaning.

## ADDED Requirements

### Requirement: Non-governed narrative profile

When the subject is an observed repository that governs itself by no Syzygy declarations (its admitted source inventory holds no `openspec/**` specification, no adopted capability declaration, no declared topology and no kernel evidence drawer), the generator SHALL compose the narrative under this profile in place of the governed readings of the three obligations of REQ-polaris-generation-004 that (a) to (c) below name. The profile SHALL be selected from the admitted project input (REQ-polaris-generation-001) and the admitted source classes that discovery exposes before it claims coverage (REQ-polaris-generation-030), never from the generator's own reading of the repository to grant itself that reading. A subject whose admitted inventory holds any one of the four SHALL NOT be composed under this profile; it takes the governed readings of REQ-polaris-generation-004, including an honest absence line for each band it cannot fill. The profile changes only the three readings below; every other obligation of REQ-polaris-generation-002, 004, 025 and 030 is unchanged, including the primary altitude order, the per-altitude honesty of each stopping depth, the editorial-draft state, the prohibition on inventing motive, and the rule that generated prose SHALL NOT impersonate an author or present invented first-person statements as quotations (REQ-polaris-generation-002).

(a) A capability is declared for the subject only where an admitted source that the maintainers of the observed repository wrote, and that is not generated from code, states it in a declaration form that the run's frozen profile enumerated before discovery began. The frozen profile, its declaration forms and its path and marker rules SHALL be fixed by the operator, the owner or the evaluation harness outside the producer that drafts the catalog, and recorded before discovery began. Eligible forms are maintainer-written documentation that names the capability, reference entries for commands, interfaces or options, and machine-readable manifests that list them. A source counts as maintainer-written and not generated only when it lies under a path class the frozen profile declares as authored documentation or manifest, and carries none of the generated-file markers the frozen profile lists (a generated-file header, a build-output location or a code-extraction marker); a source the frozen profile cannot place on either side is not a declaration source and is reported as a source the profile did not cover. A code identifier, test name, comment, file name or directory layout alone SHALL NOT declare a capability, nor SHALL reference text generated from code; a capability suggested only by such material MAY appear as an unadopted, Inferred draft entry that exposes its admitted premises. Each declared capability SHALL retain its source path, revision and span, and the catalog SHALL keep declared, unadopted-draft and Unknown coverage visibly distinct. A declaration is the maintainers' statement of what the project offers; it SHALL NOT be presented as verified behavior, as adopted Syzygy capability intent, or as endorsed by the maintainers.

(b) A capability deep dive SHALL keep its argument band. It SHALL render a contract-class band only from admitted maintainer reference spans for that capability, and SHALL NOT render a reality-class band, because no kernel-computed evidence drawer exists for the subject and implementation statements remain Inferred prose in the argument band with their premises. Each band the profile does not render, and each applicable band that has no admitted content for that capability, SHALL be reported in its own honest line (REQ-polaris-generation-004, RFC7-19), so that a deep dive carries at most two such lines; each line names the band, why it is absent and the Unknown reason where a claim is implicated. The deep dive SHALL NOT carry an empty heading, a hidden section or scaffold headings for a band it does not render, and it SHALL NOT convert the absence into a claim that the capability has no contract or no behavior.

(c) A subject with no specification has no verbatim specification leaf (RFC7-14) to descend to. The leaf altitude for a non-governed subject SHALL be one honest line stating that no specification exists for the subject, with the Unknown reason `missing-declaration`, and SHALL NOT be filled with any text presented as a specification or as operative. The exact-source terminus of a load-bearing claim block SHALL be its anchor (RFC7-2 (a)): the byte-exact admitted span, rendered verbatim and distinct from any generated text, under the identity of repository, revision, path and span with the source digest, reachable in one step. The anchor SHALL NOT be paraphrased, reordered or summarized in the position it occupies, SHALL NOT carry a Syzygy requirement identity, and SHALL NOT be labelled a specification, a leaf or operative text. A source that could not be admitted or quoted SHALL leave the claim Unknown with its reason and route rather than receive a substitute.

This requirement does not settle, and is blocked on only as stated: whether the owner reads RFC7-13 and RFC7-14 so that the maintainer span may be the leaf itself, which would need those clauses amended first (owner question O1, where (c) as written is the route that needs no amendment); the dossier's altitude order; the reading of "advantages"; the reader-facing page budget; and whether a model-authored glossary anchored to admitted spans belongs in this profile (owner question O5, deferred; the existing requirements already forbid an unestablished glossary definition).

ID: REQ-polaris-generation-032
Source: RFC7-13; governing warrants below.
Scope: v1-mandatory

#### Scenario: Maintainer-declared capability

- **WHEN** an admitted reference document of the observed repository lists a command, lies under a path class the frozen profile declares as authored documentation, and a frozen declaration form covers reference entries
- **THEN** the catalog lists that command as declared by the maintainers, with its path, revision and span, and not as verified behavior
- **AND** a capability that only a source file's function names suggest appears as an unadopted Inferred draft with its premises, or as Unknown, and never as declared

#### Scenario: Generated reference is not a declaration

- **WHEN** a committed command table or API reference carries a generated-file marker the frozen profile lists, or lies outside every authored-documentation path class
- **THEN** it is not a declaration source and the capabilities it lists are not declared by it
- **AND** the source is reported as one the profile did not cover, and the catalog shows those capabilities as drafts or Unknown

#### Scenario: Declaration form fixed before discovery

- **WHEN** a documentation section that would qualify as a declaration is found only after discovery and no frozen form covers it
- **THEN** the section is reported as a source the profile did not cover and is not promoted to a declaration in that run
- **AND** the run's independent oracle, prepared before drafting, is not changed by what the producer found

#### Scenario: Frozen forms are not the producer's

- **WHEN** the producer that drafts the catalog proposes or alters a declaration form, path class or marker after the frozen profile was recorded
- **THEN** the proposed form is not applied in that run and the departure is reported
- **AND** the catalog is judged against the recorded frozen profile only

#### Scenario: Predominantly Unknown catalog remains honest

- **WHEN** the admitted sources declare few of the capabilities the code appears to implement
- **THEN** the catalog shows the few declared entries and renders the rest as drafts or Unknown with their reasons
- **AND** it does not raise drafts to declared entries to fill the catalog

#### Scenario: Deep dive without governed bands

- **WHEN** a deep dive is composed for a declared capability of a non-governed repository with admitted reference spans
- **THEN** it shows an argument band, a contract-class band quoting those spans, and one line stating that no reality band exists for this subject and why
- **AND** it shows no empty reality heading and no scaffold, and implementation relationships it states are Inferred with admitted premises

#### Scenario: Applicable band with no content

- **WHEN** a declared capability has no admitted reference span for its contract-class band
- **THEN** the deep dive reports in one line that the contract-class band is Unknown for it, with the reason and the route to the sources that were admitted
- **AND** the line does not state or imply that the capability has no documented contract

#### Scenario: Neither contract band nor reality band

- **WHEN** a declared capability has no admitted reference span and the subject has no evidence drawer
- **THEN** the deep dive keeps its argument band and carries exactly two lines, one for the contract-class band and one for the reality band, each naming the band and its reason
- **AND** neither line states that the capability has no contract or no behavior, and no heading stands over either absent band

#### Scenario: Anchor terminus without a specification leaf

- **WHEN** a reader follows a load-bearing claim of a non-governed narrative to its exact source
- **THEN** the byte-exact admitted span appears under repository, revision, path and span with its digest, distinct from generated text, one step from the claim block
- **AND** the span carries no Syzygy requirement identity and is not described as a specification, a leaf or operative text, and the leaf altitude is one honest line with the Unknown reason `missing-declaration`

#### Scenario: Governed subject keeps governed readings

- **WHEN** the subject has adopted Syzygy declarations, specifications or a kernel evidence drawer
- **THEN** the generator composes under the governed readings of REQ-polaris-generation-004, including the `openspec/**` verbatim leaf and the full three bands
- **AND** selecting this profile for it fails the evaluation

#### Scenario: Partly governed subject

- **WHEN** the admitted inventory of an observed repository holds `openspec/**` specifications and nothing else of the four, so that no evidence drawer exists
- **THEN** the generator composes under the governed readings, the `openspec/**` text is the verbatim leaf, and the reality band collapses to its honest absence line with the Unknown reason
- **AND** selecting this profile for it fails the evaluation

#### Scenario: Profile selected from the admitted record

- **WHEN** a run on an unfamiliar repository would need to read the repository to decide whether it is governed
- **THEN** the profile is determined from the admitted project input and the admitted source classes that discovery exposes, or the run is refused or limited
- **AND** the generator does not read beyond its admission to choose its own composition rules

Form: event-response.

- **Case:** Run the named scenarios using independently prepared non-governed, partly governed and governed source snapshots, frozen declaration forms with their path classes and markers, and controlled admission records.
- **Observable:** Inspect the catalog entries, deep-dive bands and absence lines, anchor blocks with their identities and digests, the leaf-altitude line, the recorded frozen profile, and the machine-readable band and authority-class declarations (RFC7-33) in the generated draft.
- **Oracle:** Frozen source-derived expectations of which statements are maintainer declarations, which bands apply and what each span says, prepared outside the generator; producer catalog flags and prose are not expected truth.
- **Oracle independence:** Derive the declared-capability expectation from the owning sources and the frozen forms before the generated draft is seen.
- **Falsifier:** A capability is declared from code alone or from generated reference text, the producer alters the frozen profile, a declaration appears as verified or adopted, a reality band or scaffold heading appears for a non-governed subject, an absence line asserts that no contract exists, an anchor is paraphrased or labelled a specification, a leaf or operative, or a governed or partly governed subject is composed under this profile.

```yaml
warrants:
  primary: RFC7-13
  doctrine: [VIS-1, VIS-2, VIS-3, VIS-4, SEC-2]
  contracts: [RFC1-14, RFC7-2, RFC7-6, RFC7-13, RFC7-14, RFC7-15, RFC7-17, RFC7-18, RFC7-19, RFC7-20, RFC7-33]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: []
  topology: []
  parent_requirements: [REQ-polaris-generation-001, REQ-polaris-generation-002, REQ-polaris-generation-004, REQ-polaris-generation-020, REQ-polaris-generation-025, REQ-polaris-generation-030]
```
