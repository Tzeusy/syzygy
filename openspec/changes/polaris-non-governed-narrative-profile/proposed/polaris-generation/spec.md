# Polaris non-governed narrative profile

Candidate exact behavioral delta; not yet adopted, binds nothing. This change applies to the existing polaris-generation capability. It adds one requirement. It edits no byte of any predecessor requirement or scenario, in the base change or in the understanding amendment as amended by the tree-form adoption, but for a non-governed subject it displaces the text of REQ-polaris-generation-004 that the requirement names, so that requirement's effective meaning changes for that class of subject and 004 is read together with this one. For a governed subject every predecessor requirement and scenario keeps its bytes and its meaning.

## ADDED Requirements

### Requirement: Non-governed narrative profile

When the subject is not governed, the generator SHALL compose the narrative under this profile in place of the governed readings of REQ-polaris-generation-004 that (a) to (c) below name and the list after (c) displaces. A subject is governed when any one of four conditions holds: the admitted project input (REQ-polaris-generation-001) records that a kernel evidence drawer exists for the subject; or its admitted source inventory, as the source classes that discovery exposes before it claims coverage (REQ-polaris-generation-030) show it, holds an `openspec/**` specification, an adopted capability declaration or declared topology. A subject is non-governed only when the admitted project input states that no kernel evidence drawer exists for it and the admitted inventory holds none of the other three. The profile SHALL be selected from those two admitted inputs, never from the generator's own reading of the repository to grant itself that reading; where the admitted project input does not state whether a drawer exists, the profile SHALL NOT be selected and the run is refused or limited. A governed subject SHALL NOT be composed under this profile, including a governed subject whose `openspec/**` lies outside its admission; it takes the governed readings of REQ-polaris-generation-004, including an honest absence line for each band it cannot fill. For a non-governed subject the profile displaces exactly this text of REQ-polaris-generation-004, quoted in the semantic delta: the clause "Catalog membership SHALL come from declared capabilities", read as (a) states; the clause "Capability deep dives SHALL preserve RFC7-17's three authority classes and default argument/contract/reality ordering", whose reality-class band is not rendered as (b) states; the contract-band and reality-band clauses of the sentence that begins "The argument band SHALL include" (its argument-band clause is unchanged); the clause "empty bands SHALL retain an honest absence line", which also covers a band the profile does not render; the words about authority bands, verbatim exact-source text and "the leaf as the owning text" in the sentence that begins "Required headings, the altitude order", and the clause "alternative named narratives remain subject to the same per-altitude and exact-leaf obligations", which have no verbatim specification leaf to apply to and are replaced by (c); and the scenarios "Primary altitudes and one-step source access", "Capability detail keeps three authority classes" and "Capability bands preserve their actual content populations", in their leaf, contract-band and reality-band outcomes. Every other sentence and scenario of REQ-polaris-generation-004, and every obligation of REQ-polaris-generation-002, 025 and 030, is unchanged, including the primary altitude order, the per-altitude honesty of each stopping depth, the editorial-draft state, the prohibition on inventing motive, and the rule that generated prose SHALL NOT impersonate an author or present invented first-person statements as quotations (REQ-polaris-generation-002).

(a) A capability is declared for the subject only where an admitted source that the maintainers of the observed repository wrote, and that is not generated from code, states it in a declaration form that the run's frozen profile enumerated before discovery began. The frozen profile, its declaration forms and its path and marker rules SHALL be fixed by the operator, the owner or the evaluation harness outside the producer that drafts the catalog, and recorded before discovery began. Eligible forms are maintainer-written documentation that names the capability, reference entries for commands, interfaces or options, and machine-readable manifests that list them. A source counts as maintainer-written and not generated only when it lies under a path class the frozen profile declares as authored documentation or manifest, and carries none of the generated-file markers the frozen profile lists (a generated-file header, a build-output location or a code-extraction marker); a source the frozen profile cannot place on either side is not a declaration source and is reported as a source the profile did not cover. A code identifier, test name, comment, file name or directory layout alone SHALL NOT declare a capability, nor SHALL reference text generated from code; a capability suggested only by such material MAY appear as an unadopted, Inferred draft entry that exposes its admitted premises. Each declared capability SHALL retain the anchor of (c) for its source, with the repository and path shown beside it as labels, and the catalog SHALL keep declared, unadopted-draft and Unknown coverage visibly distinct. A declaration is the maintainers' statement of what the project offers; it SHALL NOT be presented as verified behavior, as adopted Syzygy capability intent, or as endorsed by the maintainers.

(b) A capability deep dive SHALL keep its argument band. It SHALL render a contract-class band only from admitted maintainer reference spans for that capability, and SHALL NOT render a reality-class band with content, a heading or scaffold, because no kernel-computed evidence drawer exists for the subject and implementation statements remain Inferred prose in the argument band with their premises. Each band the profile does not render, and each applicable band that has no admitted content for that capability, SHALL be reported in its own honest line (REQ-polaris-generation-004, RFC7-19), so that a deep dive carries at most two such lines; each line names the band, why it is absent and the Unknown reason where a claim is implicated. Each such line is a collapsed block (RFC7-19) that declares, machine-readably (RFC7-33), the band it reports on and that band's authority class (the contract class or the reality class), so that every band is assigned to one of the three classes (RFC7-17); a collapsed block is not a rendered band. The deep dive SHALL NOT carry an empty heading, a hidden section or scaffold headings for a band it does not render, and it SHALL NOT convert the absence into a claim that the capability has no contract or no behavior.

(c) A subject with no specification has no verbatim specification leaf (RFC7-14) to descend to. The leaf altitude for a non-governed subject SHALL be one honest line stating that no specification exists for the subject, with the Unknown reason `missing-declaration`, and SHALL NOT be filled with any text presented as a specification or as operative. The exact-source terminus of a load-bearing claim block SHALL be its anchor (RFC7-2 (a)) in RFC7-10's form: the target class is an evidence artifact identifier with integrity digest, whose identifier is the admitted source's content-addressed object identifier with its hash algorithm named; the optional fragment is the byte range of the span; the target state is the revision at which the source was admitted. The anchor SHALL embed no repository name, path or label as its identity (RFC7-10, REQ-polaris-generation-019); the repository and path appear beside it as presentation labels, and the byte-exact admitted span is rendered verbatim and distinct from any generated text, reachable in one step. The anchor SHALL NOT be paraphrased, reordered or summarized in the position it occupies, SHALL NOT carry a Syzygy requirement identity, and SHALL NOT be labelled a specification, a leaf or operative text. A source that could not be admitted or quoted SHALL leave the claim Unknown with its reason and route rather than receive a substitute.

This requirement does not settle, and is blocked on only as stated: whether the owner reads RFC7-13 and RFC7-14 so that the maintainer span may be the leaf itself, which would need those clauses amended first (owner question O1, where (c) as written is the route that needs no amendment); whether an admitted source of an observed repository is an "evidence artifact" for RFC7-10's target class (owner question O7); whether maintainer documentation is the project's own "spec or shape documents" in RFC1-14's sense, on which (a) and the scenario "Partly governed subject" rest (owner question O6); whether the admitted project input record can carry the drawer statement and the run's frozen profile needs a new record or schema (an implementation question, Unknown today); the dossier's altitude order; the reading of "advantages"; the reader-facing page budget; and whether a model-authored glossary anchored to admitted spans belongs in this profile (owner question O5, deferred; the existing requirements already forbid an unestablished glossary definition).

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
- **THEN** it shows an argument band, a contract-class band quoting those spans, and one collapsed block stating, with the reality class declared, that no reality band exists for this subject and why
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
- **THEN** the byte-exact admitted span appears distinct from generated text, one step from the claim block, with an anchor of target class evidence artifact identifier (the source's object identifier and hash algorithm), a byte-range fragment and the admission revision as target state, and with the repository and path shown beside it as labels
- **AND** the anchor embeds no path or label as its identity, the span carries no Syzygy requirement identity and is not described as a specification, a leaf or operative text, and the leaf altitude is one honest line with the Unknown reason `missing-declaration`

#### Scenario: Governed subject keeps governed readings

- **WHEN** any one of the four conditions that make a subject governed holds, including a project input that records an evidence drawer while the subject's `openspec/**` lies outside its admission
- **THEN** the generator composes under the governed readings of REQ-polaris-generation-004, including the `openspec/**` verbatim leaf where it was admitted and the full three bands
- **AND** selecting this profile for it fails the evaluation

#### Scenario: Partly governed subject

- **WHEN** the admitted inventory of an observed repository holds `openspec/**` specifications and nothing else of the three inventory conditions, and the project input records no evidence drawer
- **THEN** the generator composes under the governed readings, the `openspec/**` text is the verbatim leaf, and the reality band collapses to its honest absence line with the Unknown reason
- **AND** selecting this profile for it fails the evaluation

#### Scenario: Profile selected from the admitted record

- **WHEN** a run on an unfamiliar repository would need to read the repository to decide whether it is governed, or its project input does not state whether an evidence drawer exists
- **THEN** the profile is determined from the admitted project input and the admitted source classes that discovery exposes, or the run is refused or limited and the profile is not selected
- **AND** the generator does not read beyond its admission to choose its own composition rules

Form: event-response.

- **Case:** Run the named scenarios using independently prepared non-governed, partly governed and governed source snapshots, frozen declaration forms with their path classes and markers, and controlled admission records.
- **Observable:** Inspect the catalog entries, deep-dive bands and absence lines, anchor blocks with their identities and digests, the leaf-altitude line, the recorded frozen profile, and the machine-readable band and authority-class declarations (RFC7-33) in the generated draft.
- **Oracle:** Frozen source-derived expectations of which statements are maintainer declarations, which bands apply and what each span says, prepared outside the generator; producer catalog flags and prose are not expected truth.
- **Oracle independence:** Derive the declared-capability expectation from the owning sources and the frozen forms before the generated draft is seen.
- **Falsifier:** A capability is declared from code alone or from generated reference text, the producer alters the frozen profile, a declaration appears as verified or adopted, a reality band with content, or a scaffold or empty heading for either absent band, appears for a non-governed subject, an absence line declares no band or class, an absence line asserts that no contract exists, an anchor embeds a path or label as its identity, is paraphrased or is labelled a specification, a leaf or operative, or a governed or partly governed subject is composed under this profile.

```yaml
warrants:
  primary: RFC7-13
  doctrine: [VIS-1, VIS-2, VIS-3, VIS-4, SEC-2]
  contracts: [RFC1-14, RFC7-2, RFC7-6, RFC7-10, RFC7-13, RFC7-14, RFC7-15, RFC7-17, RFC7-18, RFC7-19, RFC7-20, RFC7-33]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: []
  topology: []
  parent_requirements: [REQ-polaris-generation-001, REQ-polaris-generation-002, REQ-polaris-generation-004, REQ-polaris-generation-019, REQ-polaris-generation-020, REQ-polaris-generation-025, REQ-polaris-generation-030]
```
