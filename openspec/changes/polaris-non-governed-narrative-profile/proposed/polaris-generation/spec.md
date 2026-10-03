# Polaris non-governed narrative profile

Candidate exact behavioral delta; not yet adopted, binds nothing. This change applies to the existing polaris-generation capability. It adds one requirement and modifies none: every predecessor requirement and scenario, in the base change and in the understanding amendment as amended by the tree-form adoption, keeps its bytes and its meaning for governed projects.

## ADDED Requirements

### Requirement: Non-governed narrative profile

When the subject is an observed repository that governs itself by no Syzygy declarations (no `openspec/**` specifications, adopted capability declarations, declared topology or kernel evidence drawer), the generator SHALL compose the narrative under this profile in place of the governed readings of the same three obligations in REQ-polaris-generation-004. The profile SHALL be selected from the admitted observation record of the subject, never from the generator's own inspection of the repository to grant itself that reading, and a governed subject SHALL NOT be composed under it. The profile changes only the three readings below; every other obligation of REQ-polaris-generation-002, 004, 025 and 030, including the primary altitude order, the per-altitude honesty of each stopping depth, the editorial-draft state, the prohibition on inventing motive, and the requirement that nothing cites or is cited as the observed project's own statement, is unchanged.

(a) A capability is declared for the subject only where an admitted source authored in the observed repository states it, in a declaration form that the run's frozen profile enumerated before discovery began. Eligible forms are maintainer-written documentation that names the capability, reference entries for commands, interfaces or options, and machine-readable manifests that list them. A code identifier, test name, comment, file name or directory layout alone SHALL NOT declare a capability; a capability suggested only by such material MAY appear as an unadopted, Inferred draft entry that exposes its admitted premises. Each declared capability SHALL retain its source path, revision and span, and the catalog SHALL keep declared, unadopted-draft and Unknown coverage visibly distinct. A declaration is the maintainers' statement of what the project offers; it SHALL NOT be presented as verified behavior, as adopted Syzygy capability intent, or as endorsed by the maintainers.

(b) A capability deep dive SHALL keep its argument band. It SHALL render a contract-class band only from admitted maintainer reference spans for that capability, and SHALL NOT render a reality-class band, because no kernel-computed evidence drawer exists for the subject and implementation statements remain Inferred prose in the argument band with their premises. Each band the profile does not render, and each applicable band that has no admitted content for that capability, SHALL be reported in exactly one honest line per deep dive that names the band, why it is absent and the Unknown reason where a claim is implicated. The deep dive SHALL NOT carry an empty heading, a hidden section or scaffold headings for a band it does not render, and it SHALL NOT convert the absence into a claim that the capability has no contract or no behavior.

(c) The exact-source terminus SHALL be the admitted source span: the byte-exact text of the span, rendered verbatim and distinct from any generated text, under the identity of repository, revision, path and span with the source digest. The terminus SHALL NOT be paraphrased, reordered or summarized in the position it occupies, and it SHALL NOT claim that the text is a Syzygy specification or operative authority. A block that makes a load-bearing claim SHALL reach its terminus in one step, as for governed projects, and a source that could not be admitted or quoted SHALL leave the claim Unknown with its reason and route rather than receive a substitute.

ID: REQ-polaris-generation-032
Source: RFC7-13; governing warrants below.
Scope: v1-mandatory

#### Scenario: Maintainer-declared capability

- **WHEN** an admitted reference document of the observed repository lists a command and a frozen declaration form covers reference entries
- **THEN** the catalog lists that command as declared by the maintainers, with its path, revision and span, and not as verified behavior
- **AND** a capability that only a source file's function names suggest appears as an unadopted Inferred draft with its premises, or as Unknown, and never as declared

#### Scenario: Declaration form fixed before discovery

- **WHEN** a documentation section that would qualify as a declaration is found only after discovery and no frozen form covers it
- **THEN** the section is reported as a source the profile did not cover and is not promoted to a declaration in that run
- **AND** the run's independent oracle, prepared before drafting, is not changed by what the producer found

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

#### Scenario: Verbatim terminus is the admitted span

- **WHEN** a reader follows a load-bearing claim to its exact source
- **THEN** the byte-exact admitted span appears under repository, revision, path and span with its digest, distinct from generated text
- **AND** the terminus carries no Syzygy requirement identity and is not described as a specification

#### Scenario: Governed subject keeps governed readings

- **WHEN** the subject has adopted Syzygy declarations, specifications or a kernel evidence drawer
- **THEN** the generator composes under the governed readings of REQ-polaris-generation-004, including the `openspec/**` verbatim leaf and the full three bands
- **AND** selecting this profile for it fails the evaluation

#### Scenario: Profile selected from the observation record

- **WHEN** a run on an unfamiliar repository would need to read the repository to decide whether it is governed
- **THEN** the profile is determined from the admitted observation record and the registered source population, or the run is refused or limited
- **AND** the generator does not read beyond its admission to choose its own composition rules

Form: event-response.

- **Case:** Run the named scenarios using independently prepared non-governed and governed source snapshots, frozen declaration forms and controlled admission records.
- **Observable:** Inspect the catalog entries, deep-dive bands and absence lines, terminus blocks with their identities and digests, and the machine-readable band and authority-class declarations in the generated draft.
- **Oracle:** Frozen source-derived expectations of which statements are maintainer declarations, which bands apply and what each span says, prepared outside the generator; producer catalog flags and prose are not expected truth.
- **Oracle independence:** Derive the declared-capability expectation from the owning sources and the frozen forms before the generated draft is seen.
- **Falsifier:** A capability is declared from code alone, a declaration appears as verified or adopted, a reality band or scaffold heading appears for a non-governed subject, an absence line asserts that no contract exists, a terminus is paraphrased or labelled a specification, or a governed subject is composed under this profile.

```yaml
warrants:
  primary: RFC7-13
  doctrine: [VIS-1, VIS-2, VIS-3, VIS-4, SEC-2]
  contracts: [RFC7-2, RFC7-6, RFC7-13, RFC7-14, RFC7-15, RFC7-17, RFC7-18, RFC7-19, RFC7-20]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: []
  topology: []
  parent_requirements: [REQ-polaris-generation-002, REQ-polaris-generation-004, REQ-polaris-generation-025, REQ-polaris-generation-030]
```
