# Exact predecessor requirement excerpts

[Observed] Review aid copied from the adopted CAP1 spec at baseline a9f671e9d69e1a20c89c7f6ed0c6d9e58a644c1d; the spec file is byte-identical at the rebased baseline 2d6a36328f638d3ce52605e88328c1ac7b4c9895 (BASELINE.json). Not a second authority; proposed full replacements are in specs/project-registration-and-honest-shape-visibility/spec.md.

### Requirement: CAP1-REQ-011 — Consent is a visible recorded fact, never an assumption

Group: Consent and coverage. Form: **invariant**.

Observation consent SHALL be a recorded, per-(project, repository)
consent record, and the consent state Syzygy serves SHALL derive only
from such records: their scope, attribution, and grant state render with
the coverage boundary. Absence of a resolvable in-force consent record
SHALL render as absence of consent — never as implied consent and never
as absence of the repository.

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

#### Scenario: Consent state joins to a record

- **WHEN** the coverage boundary is served for a repository whose
  consent record is in force
- **THEN** the served consent state cites that record's scope and grant
  state

```yaml
warrants:
  primary: RFC3-7
  doctrine: [SEC-4]
  contracts: [RFC3-7, RFC3-6, RFC1-3]
  policies: []
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-046 — Owning authority and effective status are exposed, stamp and record readable apart

Group: Why this answer and human/machine parity. Form: **state projection/query**.

For every answer resting on a governance artifact, Syzygy SHALL expose
the artifact's owning authority and governing revision, and SHALL
distinguish the artifact's self-declared lifecycle stamp (untrusted
content) from its effective status (derived from the owner-act record).
Where they disagree, the effective status governs and the disagreement
renders as a disclosed fact. An artifact with no owner-act record
renders effectively unadopted whatever its stamp claims.

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

#### Scenario: Stamp is not status

- **WHEN** an answer rests on an artifact self-declaring `accepted` with
  no owner-act record binding its digest
- **THEN** the fact set serves effective status unadopted, shows the
  stamp separately, and the answer treats the artifact as unadopted

```yaml
warrants:
  primary: RFC3-16
  doctrine: [VIS-4]
  contracts: [RFC3-16, "RFC3-16(a)", RFC6-13, RFC6-14]
  policies: []
  decisions: []
  topology: []
  parent_requirements: []
```
