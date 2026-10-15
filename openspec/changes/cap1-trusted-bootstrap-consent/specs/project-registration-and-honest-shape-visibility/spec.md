# CAP1 consent provenance amendment

## MODIFIED Requirements

### Requirement: CAP1-REQ-011 — Consent is a visible recorded fact, never an assumption

Observation consent SHALL be a recorded, per-(project, repository) consent record, and the consent state Syzygy serves SHALL derive only from such records: their scope, attribution, and grant state render with the coverage boundary. Absence of a resolvable in-force consent record SHALL render as absence of consent — never as implied consent and never as absence of the repository. For repository observation consent only, CAP1 SHALL evaluate the exact consent artifact and its effective owner act under RFC3-16(a/b/c) before reading the dependent repository content. A human act explicitly selecting state (1), with all nine bindings and explicit absence of the A1 audit identity, SHALL admit its in-force, scope-matched consent without an independent provider; state (2) SHALL require successful independent correlation. Absence, malformed binding, digest/identity/project/act-type/scope mismatch, missing attribution or instant, future-dated, stale under an applicable declared bound, expired, superseded, revoked, or known non-human act state SHALL refuse the dependent observation, render authorization Unknown and route the contradiction to the owner. An omitted audit-identity field is invalid; explicit absence is permitted only for state (1). Failed or unavailable state-(2) correlation SHALL NOT create state (1). Bootstrap is an explicit human trust choice, never a default, inferred permission or proof of attendance; accepting a forged record remains unauthorized. Valid withdrawal defeats a grant for the same pair; invalid or unresolvable referenced withdrawal evidence SHALL leave the pair refused rather than revive a grant. Consent records, bindings, provenance result and refusal reasons SHALL be captured for the producing evaluation; identical captured inputs and as-of produce the same decision, and subsequent source changes SHALL NOT alter that evaluation.

ID: CAP1-REQ-011
Source: RFC3-16(a), RFC3-16(b), RFC3-16(c), RFC3-7, RFC3-30; VIS-2, VIS-4, SEC-4
Scope: v1-mandatory

#### Scenario: Consent state joins to a record

- **WHEN** the coverage boundary is served for a repository whose
  consent record is in force
- **THEN** the served consent state cites that record's scope and grant
  state

#### Scenario: Explicit bootstrap consent without an audit provider

- **WHEN** the owner has explicitly performed a state-(1) consent act for the exact project/repository/artifact digest, all nine bindings are present with audit identity explicitly absent, and the act is current and in scope
- **THEN** the consent gate admits only that observation scope without requiring an A1 provider

#### Scenario: Correlated consent

- **WHEN** a consent act claims state (2) and its independently kept audit record successfully correlates all required bindings
- **THEN** the consent gate admits only its current exact scope and retains the correlation basis

#### Scenario: Invalid binding refuses observation

- **WHEN** each of missing record, malformed binding, omitted audit field, digest mismatch, wrong artifact identity, wrong project, wrong act type, wrong scope, missing owner, missing instant, future instant, applicable-staleness breach, declared expiry, supersession, revocation and known non-human act is supplied as a separate invalid case
- **THEN** the dependent repository content is not read, authorization is Unknown, and its specific failure and owner contradiction route are available

#### Scenario: Failed correlation does not downgrade

- **WHEN** a state-(2) record has missing, unavailable, mismatched or indeterminate correlation, evaluated separately
- **THEN** observation remains refused and no bootstrap fallback or automatic retry grants consent

#### Scenario: Observable machine-only submission is refused

- **WHEN** the controlled input supplies a consent-shaped artifact plus only a machine-submission record or caller verification flag, with no referenced owner-act record, or a separate case whose declared actor class is non-human
- **THEN** it grants no consent and the diagnostic distinguishes missing owner-act evidence from recognized non-human evidence

#### Scenario: Withdrawal and unresolved withdrawal remain fail closed

- **WHEN** an in-force grant and a referenced withdrawal concern the same pair, with the withdrawal valid, malformed or unresolvable in separate cases
- **THEN** the pair remains refused and the withdrawal result is retained; input order does not revive the grant

#### Scenario: Captured decision is immutable

- **WHEN** two evaluations use identical captured consent/act inputs and as-of while the underlying files change after capture
- **THEN** both decisions are identical and consume no post-capture authority bytes; new authority state requires a new capture

Group: Consent and coverage. Form: **invariant**.

- **Case** (scope of quantification): every (project, repository) pair
  the declaration names; counterexample schema: a repository rendered as
  observed whose consent reference resolves to no in-force consent
  record; sweep: for each declared pair, join the served coverage state
  to the consent records at the snapshot — denominator: the declared
  pair count.
- **Observable**: consent state per repository in the coverage answer
  and the "Why this answer?" fact set.
- **Oracle**: every pair served as observed joins to an in-force consent
  record; every pair without one is served as unconsented. Bounded by
  the declared pair count.
- **Oracle independence**: the consent records are governance-plane
  artifacts the checker can read directly; the oracle never consults
  Syzygy's consent logic.
- **Falsifier**: a repository observed (any content served) with no
  in-force consent record, or consent state served that no record
  supports.

- **Bootstrap oracle boundary**: the controlled negative case removes the referenced owner-act record or supplies a declared non-human actor; an independent fixture manifest specifies that input difference and the expected refusal/read count. The positive fixture declares a simulated human-performed act for testing only. Byte-identical forgeries are not a mechanically distinguishable fixture; actual human attendance remains the owner-trust premise of RFC3-16(a), and unauthorized forgery remains a trust-floor violation, never a claimed detection guarantee.

- **Additional case and oracle**: each added scenario above is a separate controlled case; expected admission, read/refusal and provenance tuples are specified independently of the implementation. Compare both emitted channels and intercepted content reads against those literals. The case denominator is the enumerated scenario/input-variant matrix, never the implementation's accepted subset. Any difference falsifies the added limb.

```yaml
warrants:
  primary: "RFC3-16(a)"
  doctrine: [VIS-2, VIS-4, SEC-4]
  contracts: [RFC1-3, RFC3-6, RFC3-7, RFC3-16, "RFC3-16(a)", "RFC3-16(b)", "RFC3-16(c)", RFC3-30, RFC6-13, RFC6-14, RFC7-33]
  policies: []
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-046 — Owning authority and effective status are exposed, stamp and record readable apart

For every answer resting on a governance artifact, Syzygy SHALL expose the artifact's owning authority and governing revision, and SHALL distinguish the artifact's self-declared lifecycle stamp (untrusted content) from its effective status (derived from the owner-act record). Where they disagree, the effective status governs and the disagreement renders as a disclosed fact. An artifact with no owner-act record renders effectively unadopted whatever its stamp claims. For the repository-observation consent decision defined by CAP1-REQ-011, both the human fact set and machine answer SHALL expose the consent artifact identity and digest, owner-act basis, provenance state and evaluation identity, or the precise refusal reason with authorization Unknown. Effective state (1) SHALL be labelled exactly owner-adopted (bootstrap, uncorrelated), with A1 identity explicitly absent; only successfully correlated state (2) SHALL be labelled Syzygy-verified. A recorded act, a correlation result and success of an authorized effect SHALL remain distinct. The provenance explanation SHALL be readable without colour, position or hover and reachable through the existing keyboard-accessible explanation path. The primary Unknown reason remains unconsented-source-or-provider with a specific consent diagnostic; valid bootstrap admission SHALL NOT be presented as an error merely because A1 is absent. Later successful correlation SHALL affect only a newly identified evaluation and SHALL NOT rewrite prior provenance or imply successful execution. These added valid/invalid-state obligations apply to consent only, not a general authority-input subsystem.

ID: CAP1-REQ-046
Source: RFC3-16(a), RFC3-16(b), RFC3-16(c), RFC3-7, RFC3-30; VIS-2, VIS-4, SEC-4
Scope: v1-mandatory

#### Scenario: Stamp is not status

- **WHEN** an answer rests on an artifact self-declaring `accepted` with
  no owner-act record binding its digest
- **THEN** the fact set serves effective status unadopted, shows the
  stamp separately, and the answer treats the artifact as unadopted

#### Scenario: Bootstrap disclosure agrees across channels

- **WHEN** an explicitly owner-performed valid state-(1) consent admits observation
- **THEN** the human and machine answers show owner-adopted (bootstrap, uncorrelated), explicit absent A1 identity and the same exact act/artifact/evaluation basis, without claiming independent verification or successful effects

#### Scenario: Invalid consent has an accessible explanation

- **WHEN** a CAP1-REQ-011 invalid or absent act refuses observation
- **THEN** both channels show authorization Unknown, unconsented-source-or-provider and the same specific diagnostic; keyboard users can reach the explanation without relying on hover or colour

#### Scenario: New correlation cannot rewrite old evidence

- **WHEN** a previously bootstrap consent later gains successful independent correlation in a newly captured evaluation
- **THEN** the new answer may report Syzygy-verified, while the prior evaluation retains bootstrap provenance and neither reports effect success from correlation alone

Group: Why this answer and human/machine parity. Form: **state projection/query**.

- **Case**: a checker presents an artifact whose stamp says `accepted`
  with no owner-act record, and queries an answer resting on it.
- **Observable**: the served effective status, the stamp, and the
  disclosed disagreement.
- **Oracle**: the served effective status is unadopted; both values are
  separately readable in the fact set. Bounded: one artifact, one fact
  set.
- **Oracle independence**: the fixture controls the stamp and the
  absence of a record; the rule is RFC3-16's.
- **Falsifier**: a stamped-but-unrecorded artifact served as effectively
  accepted, or stamp and effective status merged into one
  indistinguishable field.

- **Additional case and oracle**: each added scenario above is a separate controlled case; expected admission, read/refusal and provenance tuples are specified independently of the implementation. Compare both emitted channels and intercepted content reads against those literals. The case denominator is the enumerated scenario/input-variant matrix, never the implementation's accepted subset. Any difference falsifies the added limb.

```yaml
warrants:
  primary: "RFC3-16(a)"
  doctrine: [VIS-2, VIS-4, SEC-4]
  contracts: [RFC1-3, RFC3-6, RFC3-7, RFC3-16, "RFC3-16(a)", "RFC3-16(b)", "RFC3-16(c)", RFC3-30, RFC6-13, RFC6-14, RFC7-33]
  policies: []
  decisions: []
  topology: []
  parent_requirements: []
```
