> **Candidate — binds nothing.** Dispositions of the round-2 findings on this
> package, and corrections to three sentences of the round-1 dispositions. It
> is not a review, carries no verdict and confirms nothing; a later round
> decides whether each disposition is true of the bytes it names. The
> round-1 record is retained and not edited (CC-REV-6); the corrections are
> made here.

# Round-2 dispositions — non-governed narrative profile

Reviewed record: .syzygy/governance/contracts/candidates/non-governed-narrative-profile/reviews/R-NON-GOVERNED-NARRATIVE-PROFILE-2-RAW.md

Revise-severity findings: 4

The raw's verdict of record is REVISE (findings 1 to 4 revise, 5 to 12 note;
reviewed commit fb73786340542624bba9bf38367726b58acbc7b6). The raw is
retained verbatim and not edited. Its head carries the subject digest of the
spec at the reviewed commit, which this round's repairs retire (rule 10).
Every count below was re-derived by script from the repaired bytes or the
named commit, not copied from the raw.

**Finding 1 — the anchor form (revise).** Repaired. (c) now has RFC7-10's
form: target class evidence artifact identifier with integrity digest,
identifier the source's content-addressed object identifier with its hash
algorithm named, fragment the byte range, target state the admission revision,
and no repository, path or label inside the anchor. RFC7-10 and
REQ-polaris-generation-019 are in the warrants and the dependency union, and
the delta quotes RFC7-10 whole and the REQ-019 sentence and scenario as an
excerpt. On the lead's question whether `generationAnchorId` maps: [Observed]
it does not as written. The function in
`packages/polaris-generation-core/src/generation-source.ts` joins repository
id, revision, path, object id and byte range with `@`, `:`, `#` and `-`; it is
a concatenation, not a digest, and embeds a repository name and a path. Its
object id and byte range are the identifier and fragment, and its revision is
the state, so an implementation projects those three; the task list says not
to use the string. Whether an observed repository's source object is an
"evidence artifact" is a reading, put to the owner as new packet question O7.

**Finding 2 — "every other obligation … is unchanged" (revise).** Repaired.
The sentence is replaced by a list of the displaced text in the requirement
and a "Displaced text" table in the delta that quotes each sentence or
scenario of REQ-polaris-generation-004 and says how it is displaced: the
band-content sentence (contract-band and reality-band clauses), the scenario
"Capability bands preserve their actual content populations", the tree-form
sentence's words on authority bands, verbatim exact-source text and "the leaf
as the owning text", the "exact-leaf" clause, and the leaf, contract-band and
reality-band outcomes of two further scenarios. Ten rows; every quoted
fragment was re-extracted from the effective requirement and is an exact
substring. The preamble, proposal and delta no longer say "three readings".

**Finding 3 — one selection predicate (revise).** Repaired. The requirement
defines "governed" once, by four conditions: the admitted project input records
a kernel evidence drawer, or the admitted inventory holds an `openspec/**`
specification, an adopted capability declaration or declared topology. The
drawer fact comes from the admitted project input (REQ-polaris-generation-001),
which must state it; if it does not, the profile is not selected and the run
is refused or limited. Case (ii), a governed subject whose `openspec/**` lies
outside its admission, is decided: it is governed if its project input records
a drawer, and the scenario "Governed subject keeps governed readings" says so.
"Partly governed subject" and "Profile selected from the admitted record" use
the same predicate. The delta's phrase "admitted observation record" is
replaced. **Correction to the round-1 record:** its Finding 6 disposition says
"One predicate … is used in the requirement and the scenario". That was true of
"Partly governed subject" and false of "Governed subject keeps governed
readings", which kept the round-1 wording and omitted topology, and the
delta kept the removed phrase. The sentence is withdrawn; this one replaces it.

**Finding 4 — quotes (revise).** Repaired. Every block in the delta is marked
whole or excerpt, and each was re-extracted by script from its clause: RFC7-2,
RFC7-6 (both paragraphs), RFC7-10, RFC7-13 (both paragraphs), RFC7-14 (both
paragraphs), RFC7-15, RFC7-17, RFC1-14 and RFC7-19 are whole; RFC7-33 and
REQ-polaris-generation-019 are labelled excerpts. All 20 blockquotes are exact
substrings of their sources. **Corrections to the round-1 record:** its
Finding 3 disposition says the delta quotes "RFC7-14 and RFC7-13 whole" (true
of RFC7-14, false of RFC7-13, whose second paragraph was missing) and that
"RFC1-14, RFC7-15 and RFC7-33" are "quoted whole in the delta" (false of
RFC7-33, which the delta did not quote). Both sentences are withdrawn.

**Finding 5 — the band an absence line declares (note).** Accepted. Each
absence line is a collapsed block (RFC7-19) that declares, machine-readably
(RFC7-33), the band it reports on and that band's authority class; a collapsed
block is not a rendered band. The reality-band prohibition and falsifier now
speak of a reality band with content, a heading or scaffold, and add a line
that declares no band or class.

**Finding 6 — packet and task list (note).** Accepted. The packet and
`tasks.md` say a line for each band not rendered, at most two. The O2
alternative is now a distinct option: populate a reality-class band from
non-kernel sources, which contradicts RFC7-18 and needs its amendment first.

**Finding 7 — the withdrawn reason (note).** Accepted. The delta's [Inferred]
paragraph states the corrected reason (a defined thin outcome is replaced) and
no longer contradicts itself; `design.md`'s table header and rows say what is
replaced and why, and the unlabelled "No capability declarations exist" is gone.

**Finding 8 — O6 in the spec (note).** Accepted. The "does not settle"
paragraph names O6, and O7 and the record-home question beside O1.

**Finding 9 — the range citer form (note).** Accepted. Sweep G is added with
its regex published in full. Re-derived by the ledger's own script at
`9a6e8e31` (1,988 paths, 4 skipped, 1,984 searched): G hits 9 files, 5 already
in A, B, E or F and 4 outside; reading the 4 lines, three range over this
capability's numbers and one ("requirements 001–006") belongs to the
Capability 1 specification. The citer population is 63 (60 + 3), as the
reviewer found, and the ledger and delta say so.

**Finding 10 — residual and record home (note).** Accepted. `design.md` gains
a "Known residuals" section: the laundering path through an unmarked generated
file under an authored path, stated as a limit of the frozen marker list, and
the Unknown whether the REQ-019 records can carry the frozen profile and the
drawer statement without a schema change. The packet has an implementation
note and `tasks.md` lists the decision first.

**Finding 11 — outside `openspec/**` as the leaf (note).** Accepted as a
packet entry beside O6; no spec byte changes. The scenario rests on O6's
reading of RFC1-14.

**Finding 12 — `tasks.md` banner (note).** Accepted. It opens with "Candidate
— binds nothing."
