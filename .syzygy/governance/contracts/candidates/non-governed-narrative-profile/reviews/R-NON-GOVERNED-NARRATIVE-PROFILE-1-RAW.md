# R-NON-GOVERNED-NARRATIVE-PROFILE-1 — independent review of the non-governed narrative profile
Reviewed commit: 9f4c943d4bc3a32529c8c0a323b651bc4c5156e9
Subject SHA-256: 73f858dc59484cf9e6e47a898f0d5c304bf460c906894989e57c0d8ae9659d19
Verdict: REVISE

## Scope and method

Fresh-context review (CC-REV-1) of the package named in
`.syzygy/governance/contracts/candidates/non-governed-narrative-profile/REVIEW-BRIEF.md`,
read in a detached worktree at the reviewed commit. Read: the nine package
files; RFC7-2, 7-6, 7-13, 7-14, 7-15, 7-17, 7-18, 7-19, 7-20 at their
defining clauses in `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`;
RFC1-14 (cited by RFC7-15) in
`.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`;
REQ-polaris-generation-002, 004, 025, 030 in the base and overlay specs;
`decisions/POLARIS-TREE-FORM-AMENDMENT-ADOPTION.md`; CC-SPEC-1…7 in
`SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`; AGENTS.md hard prohibitions
and verification rules. Every digest below was printed by `sha256sum`;
every count by a script run this session.

## Checks run and their results

- **Quotes (criterion 2).** [Observed] A Python script extracted every
  blockquote in `SEMANTIC-DELTA.md` (8 non-banner blocks) and tested each as
  an exact substring: blocks 1–6 occur byte-exact in the overlay spec, blocks
  7–8 (RFC7-14, RFC7-19) byte-exact in `narrative-contract.md`. 8 of 8 exact.
  The RFC7-14 quote is its first paragraph only; the omitted second paragraph
  is material (Finding 2). `design.md:13-14` fragments also occur exactly.
- **Bound bytes (criterion 3).** [Observed] `git diff --stat dbf8ed19 9f4c943d
  -- openspec/changes/polaris-manifesto-generation openspec/changes/polaris-manifesto-understanding-amendment`
  is empty. The commit adds 9 files and edits none. For each of the 9, its
  current sha256 appears in 0 tracked files (`git grep -l -F`), and its path
  appears in 0 tracked files outside the package. `python3 scripts/check_governance.py`
  at the reviewed commit: "31 OK, 21 WARN, 0 FAIL (52 checks)"; no line names
  either package directory.
- **Battery (not in the brief's list, found under criterion 8).**
  `python3 scripts/check_spec_reconciliation.py --check` FAILs at the
  reviewed commit and PASSes at `dbf8ed19` (Finding 1).
- **Recount tooling claim (criterion 8).** [Observed] Copied the tree
  (`git archive HEAD`) to a scratch directory, placed the proposed spec at
  `openspec/changes/polaris-non-governed-narrative-profile/specs/polaris-generation/spec.md`,
  ran `scripts/count_polaris_effective_scenarios.py`: "FAIL: expected exactly
  one base spec.md under openspec/changes/*/specs/polaris-generation/spec.md,
  found 2". The ledger's claim holds. Note the ADDED-only file is classified
  as a second *base*, not as an overlay, which the generalization must
  address. Unmodified, the script reports "TOTAL: 31 requirements, 182
  scenarios"; the subject has 8 `#### Scenario:` headings, so 190 is right.
- **Stable ID (criterion 7, CC-SPEC-3).** [Observed] Python `re`
  `(?:REQ-polaris-generation-|[Rr]equirement )(?:\d{3}\s*(?:/|,|, and| and|\.\.|–)\s*)*032\b`
  over all 1,973 paths of `git ls-tree -r dbf8ed19` (4 not UTF-8, skipped;
  1,969 searched): 0 hits. `REQ-polaris-generation-032` literal over the
  reviewed commit excluding the two package directories: 0 of 1,969
  decoded files. Unused.
- **Ledger sweeps (criterion 8).** [Observed] Re-running the four published
  regexes over `dbf8ed19` (1,969 decoded files) gives A 47, B 11, C 70,
  D 92 — the published counts. The per-row table reproduces when a raw
  review under `decisions/` is classed as a raw before as a decision record.
  `git grep -l -F REQ-polaris-generation-004 dbf8ed19` returns 47;
  `git grep -l -F -i "declared capabilit" dbf8ed19` returns 73. Both
  second-method figures reproduce. The B-versus-A claim does not
  (Finding 8).
- **Authority claims (criterion 9).** [Observed] 64-hex tokens across the
  nine files: 0. Every "accepted"/"adopted" occurrence (19 lines, read)
  refers to a genuinely adopted artifact or is negated. No file says a
  target-repository body was read; the delta says none was. Banner gaps:
  Finding 11.

## Answers to the acceptance criteria

1. **Class.** Normative is the right class: (a) changes what counts as a
   declaration, (b) removes a band and merges absence lines, (c) changes what
   the terminus quotes. Clarifying would be wrong. The stated reason is
   wrong in part (Finding 5): the current text does have an object for an
   undeclared project.
2. **Quotes.** Exact, 8 of 8 (above).
3. **Bound bytes.** None touched; adopted directories byte-identical. But
   the commit breaks a battery check (Finding 1).
4. **(a).** Code alone cannot declare, and the late-found-section scenario
   is a real constraint against post-hoc promotion. The freeze is weaker
   than claimed and a laundering path remains (Findings 3, 4).
5. **(b).** [Inferred] A lawful reading, not an exception: RFC7-17 makes
   band count a V0 default and binds only the class assignment, and an
   announced non-rendered band is not a hidden section. The merged
   "one line per deep dive" is underspecified (Finding 7).
6. **(c).** [Inferred] As drafted, an overlay is not enough: the profile's
   terminus is by its own words not a "verbatim specification leaf", and
   RFC7-14's second paragraph makes the leaf the place Polaris tells the
   reader the text is operative. A lawful no-amendment path exists. The
   owner decides O1 (Finding 2).
7. **CC-SPEC.** Form named and five parts present; ID unused; non-goals in
   the proposal and delta. Gaps: RFC1-14 unwarranted (Finding 3), profile
   selection predicate inconsistent (Finding 6), dependency list claimed
   generated (Finding 9), open questions not recorded in the spec
   (Finding 12).
8. **Ledger.** Counts reproduce; one second-method claim is false, the
   denominator is mislabelled, and two citer forms are missed (Finding 8).
   The openspec README impact is missing (Finding 1).
9. **Authority.** No adoption claim, no act digest, no body read. Two files
   carry no banner (Finding 11).
10. **Labels.** Mostly hold; exceptions in Findings 8 and 11.

## Findings

**Finding 1 — The commit fails a battery check; a default-path page is made false** (blocking)
`openspec/changes/polaris-non-governed-narrative-profile/` (new directory);
`openspec/README.md:20-23`;
`.syzygy/governance/contracts/candidates/non-governed-narrative-profile/SEMANTIC-DELTA.md:92`;
`IMPACT-LEDGER.md:74-85`. Violates CC-IMPACT-5/6 (edits required by the
change named with their actor) and AGENTS.md "Validation" (battery clean
before claiming).
[Observed] `python3 scripts/check_spec_reconciliation.py --check` at
`9f4c943d…` prints "FAIL  R5  default routes name the terminal records — 21
examined, 1 findings — 6 tracked change directories" with
"`openspec/README.md`: 0 rows for tracked change
`polaris-non-governed-narrative-profile`, expected 1", and "6 of 7
predicates without FAIL; FAIL". At `dbf8ed19` the same command prints "7 of
7 predicates without FAIL; PASS". The check is in `PROJECT-STATUS.md:399`'s
battery and in `.github/workflows/governance-docs.yml:231-232`.
`openspec/README.md:20-23` says "Every change lives under `changes/` … this
table does — one row per directory", which is now false. The delta's
"[Observed]: no byte-bound file needs editing for this candidate to exist"
is literally true (the README is not bound) but the ledger's "Edits
required" table names only adoption-time edits and misses this
existence-time one. Repair: add a candidate row to `openspec/README.md` in
the package (or hold the candidate outside `openspec/changes/`), name it in
the ledger, and re-run the battery.

**Finding 2 — (c) substitutes for the verbatim specification leaf; the O1 warrant misreads RFC7-13** (revise)
`proposed/polaris-generation/spec.md:15`, `:55`; `design.md:36-42`;
`OWNER-DECISION-PACKET.md:34-39`; `SEMANTIC-DELTA.md:45-50`, `:80`.
Violates RFC7-13 and RFC7-14 as read at their defining clauses (rule 8);
CC-SPEC-6.
RFC7-13 (`narrative-contract.md:306-312`): "every narrative descends to a
**verbatim specification leaf** (RFC7-14), so exactness is reachable rather
than summarized away." RFC7-14 (`:324-326`): "Requirement and scenario text
renders **verbatim from `openspec/**`**", and (`:335-336`): "The leaf is the
one place Polaris tells a reader the text before them *is* operative
(RFC7-12)". The subject's (c) requires the terminus to "NOT claim that the
text is a Syzygy specification or operative authority" and its scenario
says it "is not described as a specification". By its own words the
admitted span is therefore not a verbatim specification leaf, and putting
non-operative text in the one position that asserts operativeness is the
tension RFC7-14's second paragraph exists to prevent. The packet's
recommendation rests on "RFC7-13 binds another narrative to the verbatim
terminus, not to that directory"; but RFC7-13's own leaf cites RFC7-14, and
its "another named narrative" latitude (`:315-320`) concerns ordering and
altitude count, while this profile governs the *primary* narrative too
(spec line 9: "the generator SHALL compose the narrative"). The delta quotes
only RFC7-14's first paragraph, which omits the operative-ness sentence.
[Inferred] My reading: a spec overlay alone cannot make the admitted span
the leaf. Two lawful routes exist: (i) amend RFC7-13/14 first (packet's
alternative); or (ii) without amendment, render the leaf altitude for a
non-governed subject as one RFC7-19 honest line (no specification exists,
`missing-declaration`, per RFC7-6's "thin, never absent"), and specify the
byte-exact maintainer span as the one-step *anchor* terminus of RFC7-2 (a)
rather than as the leaf. Route (ii) keeps (c)'s substance and needs no
contract act. The owner decides O1; the package should state the reading
accurately and quote RFC7-14 whole.

**Finding 3 — "Declared" is redefined without its defining clause, RFC1-14** (revise)
`proposed/polaris-generation/spec.md:11`, `:78-85`; `SEMANTIC-DELTA.md:13-57`.
Violates CC-SPEC-2 rule 1 ("Every requirement names all material governing
warrants") and the NORMATIVE-CHANGE-WORKFLOW requirement to quote current
meaning.
RFC7-15 (`narrative-contract.md:340-342`) says the catalog "projects
**declared** capability identities (RFC1-14): nothing appears that no
declared artifact asserts". RFC1-14 (`RFC-0001-project-graph-identity-state-planes.md:360-366`)
defines Capability as "a named unit of declared behavior that the project's
own spec or shape documents assert exists" and "Capability identities come
only from the project's own declared artifacts". Reading (a) is a reading of
exactly these words — whether maintainer documentation, reference entries
and manifests are "the project's own spec or shape documents" — yet RFC1-14
is absent from the warrants block and the delta, and RFC7-15, the catalog
clause itself, is cited but not quoted in "Current meaning". [Inferred]
RFC1-14's "spec or shape documents" may well support (a); the package must
make that argument against the clause, not around it.

**Finding 4 — The declaration-form freeze leaves a laundering path and an undecidable predicate** (revise)
`proposed/polaris-generation/spec.md:11`, `:27-31`, `:71-74`. Violates the
adopted scenario "Catalog membership comes from declarations" ("the model
cannot invent a declared capability from code"); CC-SPEC-4 (oracle decidable
"without judgment").
(1) Eligible forms include "reference entries for commands, interfaces or
options, and machine-readable manifests that list them" from "an admitted
source authored in the observed repository". Nothing excludes reference
text *generated from code* and committed (API references from docstrings,
`--help` dumps, man pages or command tables emitted by a build step). Such a
file is a code-derived capability list in a declaration form, so a producer
can still promote code-derived capabilities into the catalog without
inventing anything. Require that a declaration source be maintainer-authored
rather than generated, and say how the oracle tells. (2) The spec does not
say who enumerates "the run's frozen profile" of forms; if the producer
writes it, freezing before discovery constrains little, because forms such as
"maintainer-written documentation that names the capability" are broad
enough to admit almost any README sentence. State that the form list is
fixed outside the producer (operator, owner or the evaluation harness), as
scenario line 31 already does for the oracle. (3) "maintainer-written" is
an authorship judgment the frozen oracle cannot settle mechanically; name
the observable that stands for it (path class, declared docs root,
non-generated marker).
The late-found-section scenario (lines 27-31) is a real constraint against
post-hoc promotion within a run.

**Finding 5 — "Modifies none" hides a change to requirement 004's effective meaning; the class reason is partly wrong** (revise)
`proposed/polaris-generation/spec.md:3`; `SEMANTIC-DELTA.md:8`, `:57`;
`proposal.md:31-32`. Violates NORMATIVE-CHANGE-WORKFLOW (affected IDs and
current meaning stated truthfully) and CC-SPEC-9 (a fresh reader can restate
the effective rule).
REQ-polaris-generation-004 today applies to every subject, governed or not.
Requirement 032 makes three of its readings inapplicable to a class of
subjects ("in place of the governed readings of the same three obligations
in REQ-polaris-generation-004"). That is a change to 004's effective meaning
for that class even though no 004 byte moves; "Stable IDs affected:
REQ-polaris-generation-032 (new)" should list 004 as affected, and a reader
of 004 alone is not told of the exception. The delta's reason, "As written,
these have no object for an observed repository", is [Inferred] and
contradicted by the clauses it reads against: RFC7-6 (`:166-168`) says that
on an undeclared project "a predominantly-Unknown catalog under an honestly
thin narrative is correct output", and RFC7-15 (`:343-345`) says such a
catalog "is correct output, rendered as normal — not broken". The current
rules have an object; they prescribe a thin outcome the proposal calls
"honest and useless" (`proposal.md:20-21`). Restate the reason as replacing
a defined thin outcome, and say so in the owner packet.

**Finding 6 — The profile-selection predicate differs between requirement and scenario, and its input is undefined** (revise)
`proposed/polaris-generation/spec.md:9`, `:59`, `:63-67`. Violates CC-SPEC-4
(reachable case; effective oracle) and CC-SPEC-9.
Line 9 defines non-governed as "no `openspec/**` specifications, adopted
capability declarations, declared topology or kernel evidence drawer"; line
59 makes a subject governed when it "has adopted Syzygy declarations,
specifications or a kernel evidence drawer" (no topology; "adopted Syzygy"
qualifies specifications). OpenSpec is a public tool: a repository using
`openspec/**` without any Syzygy adoption is governed under line 9 and
arguably not under line 59, and under neither is its catalog defined. The
selection input, "the admitted observation record of the subject" (line 9,
65), names a record and field that no parent requirement defines: Python
`re` "observation record", case-insensitive, over the base and overlay
specs returns 0 hits. Name the field or the existing record that carries
"governed", align the two predicates, and add the mixed case.

**Finding 7 — "One honest line per deep dive" is ambiguous and the combined case is untested** (note)
`proposed/polaris-generation/spec.md:13`, `:39-49`; `design.md:31-35`.
Against RFC7-19 and the adopted scenario "Capability detail keeps three
authority classes".
[Inferred] Answer to criterion 5: not rendering a reality band is lawful
under RFC7-17 (`:396-399`: count and ordering are "a V0 default, not a
frozen constraint … A narrative composing its deep dive differently still
assigns every band to one of the three classes"), and a band announced as
absent is not "a hidden section". But "Each band … SHALL be reported in
exactly one honest line per deep dive" reads either as "each band in one
line" or "all bands in one line"; `design.md:32` takes the second ("One
line per deep dive replaces up to three per-band lines"). RFC7-19 speaks per
block ("A block with no content collapses to one honest line"), and no
scenario covers a deep dive missing both its reality band and its
contract-class content. Also "up to three" is two at most, since the
argument band always applies. Pick one reading and add the combined
scenario.

**Finding 8 — Ledger: a false second-method claim, a mislabelled denominator, missed citer forms** (revise)
`IMPACT-LEDGER.md:8-9`, `:24-27`, `:29-32`. Violates verification rules 2
and 9 and CC-IMPACT-3.
(1) Lines 24-26: "its 11 files are in A or are continuation-only hits, and
no continuation-only hit was found outside A's list." [Observed] 5 of B's 11
files are not in A: `.syzygy/governance/decisions/POLARIS-UNDERSTANDING-SPECIFICATION-ADOPTION-ACT.md`,
`openspec/changes/polaris-manifesto-generation/ASSET-CONTRACT.md`,
`docs/design/POLARIS-M7-GENERATION-LOOP-FUNNEL.md`,
`docs/reviews/R-POLARIS-M7-GENERATION-LOOP-FUNNEL-RAW.md` and
`docs/reviews/R-POLARIS-M7-GENERATION-LOOP-FUNNEL-2-RAW.md`. The citer
population is A∪B = 52, never stated. (2) Line 9: "1,969 tracked files; a
file that did not decode as UTF-8 was skipped." [Observed] `git ls-tree -r
dbf8ed19` lists 1,973 paths; 4 do not decode; 1,969 is the searched
population, not the tracked one. (3) Missed forms: the prose short form,
`\b[Rr]equirements? (?:\d{3}(?:,| and|,? and| to)\s*)*004\b`, hits 7 files,
4 outside A∪B (`openspec/README.md`,
`openspec/changes/polaris-manifesto-generation/APPLICABILITY-DECISIONS.md`,
`docs/reviews/R-POLARIS-GENERATOR-FRESH-PRODUCT-2026-09-12-RAW.md`,
`docs/reviews/R-POLARIS-GENERATOR-PRODUCT-READINESS-2026-09-12-RAW.md`);
the title form `Understandable reading depths` hits 15, 4 outside A∪B,
including `scripts/check_spec_reconciliation.py`, which the ledger
disclosed as unswept [Unknown] (adequately labelled, but now measurable).
None of these changes the disposition; they change the claims.

**Finding 9 — The dependency list says "Generated" but no generator covers it; warrants incomplete** (note)
`GOVERNING-DEPENDENCIES.md:3-6`; `proposed/polaris-generation/spec.md:72`,
`:78-85`. CC-SPEC-2 rule 4 ("A hand-authored second list at specification
level is a defect"); CC-SPEC-2 rule 1.
The file says it is generated and, in the same sentence, that
`build_polaris_dependency_unions.py` "knows two changes"; whatever produced
it is not named, so it cannot be re-derived (its content does equal the
warrant block's union, checked by reading). The Observable relies on
"machine-readable band and authority-class declarations", which is RFC7-33
(`rendering-and-surface.md:205`), not warranted. `proposal.md:58-60` names
requirement 020 as a preserved admission parent; `parent_requirements`
omits it.

**Finding 10 — A preserved-obligation paraphrase that no parent states** (note)
`proposed/polaris-generation/spec.md:9`. CC-SPEC-9; RFC7-14's rule against
paraphrase in normative position, by analogy.
"the requirement that nothing cites or is cited as the observed project's
own statement" is listed as an obligation of 002, 004, 025 or 030.
[Observed] Python `re` `own statement|cited as`, case-insensitive, over the
base and overlay specs: 0 hits. The nearest text is 002's "Generated prose
SHALL NOT impersonate an author or present invented first-person statements
as quotations" and RFC7-20's "non-citable". Quote or cite the owning
sentence instead.

**Finding 11 — Two files carry no banner; an unlabelled claim about the target repository** (note)
`design.md:1-7`; `GOVERNING-DEPENDENCIES.md:1-6`; `proposal.md:18-21`.
Brief criterion 9 ("every banner must say it binds nothing"); AGENTS.md
epistemic discipline.
`design.md` and `GOVERNING-DEPENDENCIES.md` have no "binds nothing" banner
(the latter says "review routing, not authority"). `proposal.md:18-19`
states "An observed public repository such as `redis/redis` has none of
these" with no label, while the delta (`SEMANTIC-DELTA.md:84`) says no target
repository body was read. Label it [Inferred] or [Unknown] with its basis.

**Finding 12 — The spec does not record the open questions it believes it leaves open** (note)
`proposed/polaris-generation/spec.md` (whole file). CC-SPEC-6 ("the spec
records which open questions it believes it does not settle").
O1–O4 and the dossier altitude order (gap item 17d) are recorded only in
the packet and delta. Since (c) as drafted presumes O1's recommended answer
(Finding 2), the spec should name O1 as the question it is blocked on.

## Verdict rationale

Quotes are exact, no bound byte moves, the ID is free and the ledger's
counts reproduce. One blocking defect (the reconciliation battery fails
at the reviewed commit) and six revise findings (the terminus reading, the
missing RFC1-14 warrant, the laundering path, the hidden 004 effect, the
selection predicate, and the ledger's false claims) prevent confirmation.
