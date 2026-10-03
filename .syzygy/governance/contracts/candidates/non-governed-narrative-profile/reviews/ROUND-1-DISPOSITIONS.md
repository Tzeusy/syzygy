> **Candidate — binds nothing.** Dispositions of the round-1 findings on this
> package. It is not a review, carries no verdict and confirms nothing; a
> later round decides whether each disposition is true of the bytes it names.

# Round-1 dispositions — non-governed narrative profile

Reviewed record: `reviews/R-NON-GOVERNED-NARRATIVE-PROFILE-1-RAW.md`
(verdict of record: REVISE; reviewed commit 9f4c943d4bc3a32529c8c0a323b651bc4c5156e9).
The raw is retained verbatim and not edited. Its head carries the subject
digest of `proposed/polaris-generation/spec.md` at the reviewed commit, which
this round's repairs retire (rule 10).

Every count below was re-derived by script from the repaired bytes or the
named commit, not copied from the raw.

| # | Class | Disposition | Where |
|---|---|---|---|
| 1 | blocking | Repaired: row added, ledger names it, R5 passes | `openspec/README.md`; `IMPACT-LEDGER.md` |
| 2 | revise | Repaired by the reviewer's route (ii); O1 restated | spec (c); delta; packet O1 |
| 3 | revise | Repaired: RFC1-14, RFC7-15 and RFC7-33 warranted and quoted | spec warrants; delta |
| 4 | revise | Repaired in three parts | spec (a) and two scenarios |
| 5 | revise | Repaired: 004 listed as affected, reason restated | spec preamble; delta; proposal; packet |
| 6 | revise | Repaired: one predicate, input named, mixed case added | spec; scenarios |
| 7 | note | Accepted: per-band lines, combined scenario added | spec (b); scenario |
| 8 | revise | Repaired: re-derived, withdrawn claim named, forms added | `IMPACT-LEDGER.md` |
| 9 | note | Accepted: "generated" withdrawn, warrants extended | `GOVERNING-DEPENDENCIES.md`; spec |
| 10 | note | Accepted: paraphrase replaced by a quoted obligation | spec |
| 11 | note | Accepted | `design.md`; `GOVERNING-DEPENDENCIES.md`; `proposal.md` |
| 12 | note | Accepted: open questions recorded in the spec | spec |

## Finding 1 — the reconciliation battery

Reproduced: `scripts/check_spec_reconciliation.py --check` failed predicate R5
for want of a row. The directory has a row in `openspec/README.md` now, worded
as a candidate no act binds and not as one of the five in force; the table's
lead sentence says a sixth row is such a candidate. The first draft of the row
named the new requirement identifier and made predicate R4 fail (the
identifier resolves to no adopted requirement); the identifier was removed
from the row. The command now ends "7 of 7 predicates without FAIL; PASS".
The ledger's "Edits required" table names this existence-time edit and its
actor. `openspec/README.md` is not act-bound by any manifest I grepped; the
reviewer said the same, and I did not re-hash it against every manifest.

## Finding 2 — the leaf

Taken as the reviewer's route (ii). The requirement no longer calls the span
the leaf: (c) renders the leaf altitude as one honest `missing-declaration`
line and makes the byte-exact span the RFC7-2 (a) anchor, never labelled a
leaf, specification or operative. The scenario "Verbatim terminus is the
admitted span" is replaced by "Anchor terminus without a specification leaf".
The delta quotes RFC7-14 and RFC7-13 whole (the extraction script copied each
paragraph from the module, not from memory) and gives the reading with its
[Inferred] label. Packet O1 now states the question as "leaf or anchor", keeps
the amendment route as the alternative, and records that round 1 found the
earlier wording unlawful. The owner still decides.

## Finding 3 — RFC1-14

Accepted. RFC1-14, RFC7-15 and RFC7-33 are in the warrants block and
quoted whole in the delta, with the argument that the profile reads an
observed repository's maintainer documentation as "the project's own spec or
shape documents". That reading is labelled [Inferred] and is put to the owner
as a new question, O6, with the amendment alternative.

## Finding 4 — the declaration forms

All three parts accepted. (1) Reference text generated from code is excluded,
with a scenario "Generated reference is not a declaration". (2) The frozen
profile is fixed by the operator, the owner or the evaluation harness outside
the producer, with a scenario "Frozen forms are not the producer's". (3)
"Maintainer-written" is made observable by a path class the frozen profile
declares as authored documentation and by generated-file markers the profile
lists; a source the profile cannot place on either side is not a declaration
source. This is a mechanical stand-in for an authorship judgment, and the
design note says so.

## Finding 5 — "modifies none"

Accepted. The preamble, the delta's affected-IDs line and the proposal now say
004 changes in effect, not in bytes. The reason is restated: RFC7-6 and
RFC7-15 define a thin, predominantly Unknown outcome as correct, so the
current text has an object and the proposal replaces a defined outcome. The
packet says so in plain terms.

## Finding 6 — the selection predicate

Accepted. One predicate (no `openspec/**` specification, no adopted capability
declaration, no declared topology, no kernel evidence drawer in the admitted
source inventory) is used in the requirement and the scenario. The input is
the admitted project input (REQ-001) and the source classes discovery exposes
(REQ-030), both of which exist in the adopted text; the earlier phrase
"admitted observation record" was removed. A repository that has only
`openspec/**` specifications is governed under this predicate and takes the
governed readings, since the verbatim leaf then exists; a scenario "Partly
governed subject" says so.

## Finding 7 — one line per deep dive

Accepted. RFC7-19 speaks per block, so each absent band gets its own line, at
most two per deep dive (the argument band always applies); the design note's
"up to three" is gone. The combined case has a scenario.

## Finding 8 — the ledger

Accepted in all three parts, re-derived by script. (1) The claim that B's
files are in A is withdrawn: 5 of 11 are not; A or B is 52. (2) The
denominator is stated as 1,988 paths, 4 skipped, 1,984 searched at the new base
(1,973, 4, 1,969 at round 1's), and the round-1 wording that called 1,969
"tracked" is corrected. (3) The short form and the title form are added as
sweeps E and F (7 and 15 files, 8 outside A or B), including the reconciliation
checker, and the "[Unknown]" on the title form is replaced by the measurement.
A, B, C, D and the per-row table reproduce at both commits; the row rule
(raw before decision) is now stated. Counts changed only by the new sweeps and
the new total 60.

## Finding 9 — the dependency list

Accepted. The file no longer says it is generated: it says it was copied by
hand from the one warrants block, that no script covers it, and that a
covering script or deletion is needed before adoption, which is what CC-SPEC-2
rule 4 requires of a second list. RFC7-33 is warranted (it carries the
machine-readable distinctions the Observable relies on) and requirement 020 is
now in `parent_requirements`, together with 001, which the new selection
sentence cites.

## Finding 10 — the paraphrased obligation

Accepted. The sentence no parent states is replaced by the quoted sentence of
REQ-002 about impersonation and invented first-person quotation.

## Finding 11 — banners and labels

Accepted. `design.md` and `GOVERNING-DEPENDENCIES.md` carry a "binds nothing"
banner; the `redis/redis` sentence in `proposal.md` is labelled [Inferred]
with its basis (public description; no body read).

## Finding 12 — open questions

Accepted. The requirement records what it does not settle (O1, the dossier
altitude order, "advantages", the page budget, and the glossary question O5).

## The glossary question (asked by the lead, not a finding)

Decided: deferred, recorded as packet O5, not added. Reasons: the adopted
requirements already forbid an unestablished glossary definition; the
provider draft schema has no glossary field (relayed from lane-e's PR 265, not
re-read here), so a requirement would need a schema change that no act
authorizes; the glossary would apply to governed subjects too, which is a
different category from the three readings in this change; and adding it now
would restart the review of a package that has just taken seven substantive
repairs. The packet records the shape an additive requirement would take.
