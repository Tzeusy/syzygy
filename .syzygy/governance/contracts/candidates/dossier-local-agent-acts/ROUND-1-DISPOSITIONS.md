# Round 1 dispositions — local-agent dossier sitting

Reviewed record: .syzygy/governance/contracts/candidates/dossier-local-agent-acts/reviews/R-DOSSIER-LOCAL-AGENT-SITTING-1-RAW.md

Verdict of record (the raw's own `Verdict:` line): REVISE. Seven findings:
two revise, five notes. Every finding is repaired in the commit that adds
this record; round 2 reads the repaired bytes. The raw is stored verbatim
(CC-REV-6).

### 1 — revise: the tag sign-off record of the registry entry lacked RFC3-16(b) items

Repaired (option A). `scripts/record_versioned_signoff.py`: for a package
that installs a registry entry the record now carries `Recorded at (UTC)`
(item 6, taken by `--instant` or now, and required to fall on the
sign-off's date), `Act type: adopt-registry-entry` (item 4, the type every
earlier registry act used), the project identity, the installed entry and
its SHA-256 (item 3), the scope (item 7), the supersession line (item 8), the
state-(1) provenance and `A1 audit-record identity … explicitly absent`
(item 9). `--check` reads the instant back from the record and regenerates
it exactly. Two new fixtures: the rendered lines, and a record-then-check run
that refuses an off-date instant and fails its check after an edit to the
installed entry. The seven earlier sign-off records still regenerate exactly
(their packages install no entry, so they render none of these lines). The
packet's row-2 section and `SEMANTIC-DELTA.md` say what the record carries.

### 2 — revise: the entry called the reader "implemented" for behaviour it does not perform

Repaired (options A and B together). The entry now says "partly
implemented" and carries `implementationCoverage`: `reader` lists what the
reader file does; `awaitingGate` lists the four source limits, screening,
the fact records (source reference included), the failure-state mapping and
the state-directory writes, which belong to the dossier gate that is not yet
written. The builder refuses an entry that omits any of the eight
declarations the round named from `awaitingGate`, or lists one on both sides
(three new mutants). The packet's row 2 has a paragraph "What is built and
what is not", which tells the owner that signing now approves declarations
no code yet performs, and gives the alternative of signing after the gate
lands. Its list of what a real run still needs names the gate's share.

### 3 — note: an edit to a bound file blocks every act before the sitting

Repaired in the packet's cost paragraph. Before the sitting, any such edit
regenerates a record, so the manifest changes, and the review is retired for
every row and for the entry's sign-off. After an act is recorded, the edit
affects only the record it touches. The recorder stays fail-closed as it is.

### 4 — note: the stretch in "enough to adopt" was not named

Repaired. Rows 4–5 now say that doctrine has always been adopted without a
digest act, that RFC3-16 read literally calls such an artifact unadopted,
and they name both readings a reviewer may contest. The first is that the
acts only bind already-adopted text to bytes, rather than making it
effective. The second is that an act over a record listing the files'
digests binds those files indirectly.

### 5 — note: row 5 adds the record the owner's choice was described as not needing

Repaired. The row-5 bullet quotes the option's "No extra record", says that
R3-F8 later required an act, and says that declining keeps the original
choice at the stated cost.

### 6 — note: a miscount and ambiguities in the packet

Repaired:

- "four of those" now reads "none of the five".
- The classes are attributed to the first Anthropic egress record by path.
  The packet also notes that the second version adds a class that is not yet
  in the vocabulary.
- Row 2 explains why the entry is version 2.0.0-candidate.1 while the
  package sign-off is 1.0.
- Table row 3 states the tree condition.

### 7 — note: the semantic delta left out three changes

Repaired:

- New rows for `signedBy`, for `revisionNotAdmitted.executionFact` and its
  `note`, and for `authorizationModeDerivation`.
- The classification-policy gap the round found is closed in the entry
  itself. It gets a `classification-policy` input class, mapped to RFC2-1
  items 7 and 11, and two `admissionFailureMapping` keys that mirror the
  screening scope. The builder refuses either omission.
- The delta now states its own predicate. A recursive key diff over the two
  entries finds 44 changed, added or removed keys, and the last segment of
  each appears literally on the page.
