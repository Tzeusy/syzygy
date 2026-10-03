# R-NON-GOVERNED-NARRATIVE-PROFILE-2 — independent review of the non-governed narrative profile, round 2
Reviewed commit: fb73786340542624bba9bf38367726b58acbc7b6
Subject SHA-256: 603c840b58bbf153653e539a3d4957791f5213d69185a1528d37579f5604231b
Verdict: REVISE

## Scope and method

Fresh-context review (CC-REV-1) of the package named in
`.syzygy/governance/contracts/candidates/non-governed-narrative-profile/REVIEW-BRIEF.md`,
round 2. I read it in a detached worktree at the reviewed commit and modified nothing.
I read the five files under `openspec/changes/polaris-non-governed-narrative-profile/`,
the package's four files and the two files in its `reviews/` directory, and
`openspec/README.md` (the one file the change edits outside both
directories). I read these clauses where they are defined: RFC7-2, RFC7-6, RFC7-9, RFC7-10, RFC7-12, RFC7-13,
RFC7-14, RFC7-15, RFC7-17, RFC7-18, RFC7-19 and RFC7-20 in
`.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`, RFC7-33
in `RFC-0007/rendering-and-surface.md:205`, RFC1-14 in
`RFC-0001-project-graph-identity-state-planes.md:361-368`, and RFC2-24 in
`RFC-0002/rendering-vocabularies.md:103`. Each location came from
`DIRECTIVE-REGISTER.md`. I also read the effective REQ-polaris-generation-001,
002, 004, 019, 020 and 030 in the base and overlay specs,
`decisions/POLARIS-TREE-FORM-AMENDMENT-ADOPTION.md`, CC-SPEC-2, 4, 6, 8 and 9,
CC-REV-2 (`review-and-documentation.md:71`), and the hard prohibitions and
verification rules in AGENTS.md. `sha256sum` printed every digest, and a
script run this session produced every count.

## Checks run and their results

- **Battery.** [Observed] `python3 scripts/check_spec_reconciliation.py --check`
  at `fb737863` ends "7 of 7 predicates without FAIL; PASS", with
  "R5 default routes name the terminal records — 21 examined, 0 findings — 6
  tracked change directories". `python3 scripts/check_governance.py` prints
  "31 OK, 21 WARN, 0 FAIL (52 checks)" at `fb737863`, the same as at
  `9a6e8e31`. Diffing the two outputs with counts masked leaves exactly one
  new line, a CG-1f frozen-lane WARN. In it the round-1 raw cites
  `openspec/changes/polaris-non-governed-narrative-profile/specs/polaris-generation/spec.md`.
  That is a raw quoting a scratch path. CG-1f classifies it and does not
  fail it.
- **Bound bytes (criterion 3).** [Observed] `git diff --quiet 9a6e8e31 HEAD
  -- openspec/changes/polaris-manifesto-generation openspec/changes/polaris-manifesto-understanding-amendment`
  returns 0, so both adopted directories are byte-identical. The change
  touches 12 files: it adds 11 and edits only `openspec/README.md`. I ran
  `git grep -l -F` for each file's current sha256 and got 0 tracked files for
  each of the 12. `openspec/README.md` hashes at `9a6e8e31` and at HEAD
  likewise appear in 0 tracked files. No `*-MANIFEST.txt` names the
  `openspec/README.md` path, nor does `ACCEPTANCE-ACT-RECORD.md` or
  `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`. No act binds any byte
  the change touches.
- **Quotes (criterion 2).** [Observed] A Python script extracted the 14
  blockquotes in `SEMANTIC-DELTA.md`. Apart from the banner, each of the 13 is
  an exact substring of its source. Blocks 1–6 occur in both the base and the
  overlay spec. Blocks 7–11 and 13 occur in `narrative-contract.md` and
  block 12 in RFC-0001. 13 of 13 are exact. Some quotes are partial where the
  delta says "whole", and several clauses the change rests on are not quoted
  (Finding 4). REQ-002's quoted sentence ("Generated prose SHALL NOT
  impersonate…") occurs exactly in both specs, so the round-1 Finding 10
  repair holds.
- **Stable ID (criterion 7).** [Observed] Python `re`
  `REQ-polaris-generation-032|REQ-polaris-generation-(?:\d{3}\s*(?:/|,|, and| and|\.\.|–)\s*)+032\b`
  ran over `git ls-files` at `fb737863`. There are 1,999 tracked paths; 4 did not
  decode and were skipped, so 1,995 were searched. It hit 5 files, all inside
  the two package directories. The identifier is unused elsewhere.
- **Ledger sweeps (criterion 8).** [Observed] My own script ran the six
  published regexes (Python, the flags as published) over `git ls-tree -r -z`
  at `9a6e8e31`, excluding the two package prefixes. It searched 1,988 paths,
  skipped 4 and so searched 1,984. Counts: A 47, B 11, C 70, D 92, E 7, F 15.
  A∩B is 6, B∖A is 5 and A∪B is 52. E∖(A∪B) is 4 files and F∖(A∪B) is 4
  files, with no overlap between them, and A∪B∪E∪F is 60. The eight named
  files match the ledger's list. With the ledger's stated first-match path
  rule, the per-row table reproduces cell for cell:
  decisions 6/2/1/0/0/0, evidence 19/3/10/14/2/10, raw 4/2/12/14/2/1,
  `.syzygy` 5/0/26/38/0/0, openspec 5/1/13/13/2/2, code 3/1/4/4/0/1,
  other 5/2/4/9/1/1. At `dbf8ed19` the script searched 1,973 paths, skipped
  4, searched 1,969, and gave the same six counts, the same A∩B and A∪B, the
  same eight extra files and 60. I differ from the ledger nowhere. The
  second-method claims are true as narrowed: per the round-1 raw,
  `git grep -l -F REQ-polaris-generation-004` gives 47, and the
  `declared capabilit` count of 73 confirms only D's first alternative, which
  the ledger now says. Missed citer form: Finding 9.
- **Recount tooling (criterion 8).** [Observed] I extracted the commit with
  `git archive` into a scratch tree. Unmodified, `count_polaris_effective_scenarios.py`
  ends "PROJECT-STATUS.md asserts: 31 requirements, 182 scenarios". With the
  spec copied to
  `openspec/changes/polaris-non-governed-narrative-profile/specs/polaris-generation/spec.md`
  it prints "FAIL: expected exactly one base spec.md under
  openspec/changes/*/specs/polaris-generation/spec.md, found 2". The claimed
  failure holds. The subject has 12 `#### Scenario:` headings, so 194 is right.
- **Authority (criterion 9).** [Observed] 64-hex tokens: 0 in each of the
  ten non-raw package files. The round-1 raw has 1 (its own head), which
  CG-15 exempts as a raw. Every package file opens with "binds nothing" in
  its first 600 bytes except `tasks.md` (Finding 12) and the raw. The
  `openspec/README.md` row reads "Candidate — binds nothing; not one of the
  five in force". No file says a target repository body was read.
  `proposal.md:18-21` labels its `redis/redis` sentence [Inferred].
- **Glossary relay (criterion 11).** [Observed] A
  `git grep -n -i glossar -- packages/polaris-generation-core/src` hit only
  `prompts.ts` (prompt text); no schema module carries a glossary field. That
  supports the relayed lane-e statement, which the package itself did not
  re-read.

## Answers to the acceptance criteria

1. **Class.** Normative is right. (a) changes what counts as a declaration,
   (c) changes what the exact-source terminus is, and 004's effective
   meaning changes for a class of subject. Clarifying would be wrong. The
   reason is now restated correctly in the delta's paragraph and the
   proposal. Two stale sentences still carry the old reason (Finding 7).
2. **Quotes.** 13 of 13 are exact. "Each whole" is false for RFC7-13 and for
   the unlabelled RFC7-6 paragraph, and RFC7-2, RFC7-17 and RFC7-33 are
   relied on but not quoted (Finding 4).
3. **Bound bytes.** The change touches none, and the battery passes.
4. **(a).** [Inferred] Code alone cannot declare. Generated reference text
   is excluded by name. The form list, path classes and markers are fixed
   outside the producer before discovery. The late-found-section and
   producer-alteration scenarios are real constraints, not formalities.
   Path class and marker are necessary conditions, so the evaluation oracle
   is decidable on prepared snapshots. A residual laundering path remains: a
   code-generated file that carries no listed marker and sits under an
   authored-documentation path passes the observable while violating the
   prohibition. The spec does not state this residual, and the design note
   does not disclose it (Finding 10). Whether maintainer documentation
   counts as "the project's own spec or shape documents" is packet O6, an
   open owner question with no signed bytes assuming it, so it does not
   block.
5. **(b).** [Inferred] Not rendering a reality band is a lawful reading,
   not an exception. RFC7-17 (`:395-399`) says "count and ordering are a V0
   default, not a frozen constraint … A narrative composing its deep dive
   differently still assigns every band to one of the three classes and
   declares it machine-readably". An absence announced in its own line is
   not "a hidden section" (RFC7-19, `:409-412`). Per-band lines, at most two
   per deep dive, now follow RFC7-19's per-block wording. The spec does not
   say which band and class the absence line itself declares machine-readably
   (Finding 5). That is O2's subject matter only in part, and it does not
   block.
6. **(c).** [Inferred] The round-2 route is lawful without an amendment to
   RFC7-13 or RFC7-14, as a leaf/anchor question. RFC7-19 governs every
   block with no content. The adopted tree-form 004 already requires that
   "missing content SHALL remain honestly absent or Unknown". The
   exactness RFC7-13 protects ("so exactness is reachable rather than
   summarized away") is carried by the one-step anchor. RFC7-14 is quoted
   whole (both paragraphs, `:324-338`). The residual is that RFC7-13's
   "every narrative descends to a **verbatim specification leaf**", read
   literally, is not met. An undeclared governed project already faces that
   under the current text, and the owner decides it as O1, so it does not
   block. Separate from O1 and not posed by the packet: the anchor's own form
   does not meet RFC7-10 or adopted REQ-019 as written (Finding 1).
7. **CC-SPEC.** The form is named (event-response), and the case,
   observable, oracle, independence and falsifier are all present. The ID is
   unused (1,995 searched). Non-goals are explicit. Gaps: one warrant is
   missing (RFC7-10, REQ-019; Finding 1); the profile-selection predicate
   still has two forms (Finding 3); "every other obligation is unchanged" is
   false (Finding 2); O6 is not recorded in the spec (Finding 8); and the
   oracle cannot tell which band an absence line declares (Finding 5).
8. **Ledger.** Every count reproduces at both commits, and I differ nowhere.
   One citer form, the hyphen range, is missed (Finding 9).
9. **Authority.** No adoption claim, no act digest, no body read.
   `tasks.md` carries no "binds nothing" sentence (Finding 12).
10. **Labels.** They mostly hold. Exceptions: the unlabelled "No capability
    declarations exist" (`design.md:16`, Finding 7) and the delta's [Inferred]
    paragraph, which contradicts itself (Finding 7).
11. **Round-1 repairs.** Findings 1, 7 (in the spec), 8, 9, 10, 11 and 12
    are true of the current bytes. Finding 2 is repaired in the spec, but
    the disposition's "quotes … RFC7-13 whole" is false (Finding 4). Finding 3's
    disposition says RFC7-33 is "quoted whole in the delta", but the delta
    does not quote RFC7-33 at all (Finding 4). Finding 5 is repaired in the
    preamble, delta, proposal and packet, but `design.md` keeps the old
    reason (Finding 7). Finding 6's "one predicate … is used in the
    requirement and the scenario" is false for the scenario "Governed
    subject keeps governed readings", and the delta keeps the removed phrase
    "admitted observation record" (Finding 3). Finding 7's repair is not
    carried into the packet or the task list (Finding 6). Repairs that
    introduced a new defect: route (ii) moved the terminus onto the anchor
    and so brought in RFC7-10, which no one checked (Finding 1); and the new
    "every other obligation … unchanged" sentence (Finding 2). Copied
    counts: none, since every ledger figure re-derives. **Glossary (O5):**
    the deferral is justified by its sources. The scenario "No supported
    optional asset" (overlay `:91-95`) makes an unestablished glossary
    definition an omission with a disclosed gap. 004 already governs
    glossaries for every subject ("Glossaries SHALL explain concepts where
    needed for comprehension"), so a glossary rule is a different category
    from the three non-governed readings. The schema statement is relayed in
    the package, but my grep supports it.

## Findings

**Finding 1 — The anchor form of (c) is unwarranted and, as written, conflicts with RFC7-10 and adopted REQ-019** (revise)
`openspec/changes/polaris-non-governed-narrative-profile/proposed/polaris-generation/spec.md:15`,
`:73-75`, `:103-112`; `SEMANTIC-DELTA.md:110`, `:114`. Violates CC-SPEC-2
("Every requirement names all material governing warrants") and rule 8.
(c) makes "the exact-source terminus of a load-bearing claim block … its
anchor (RFC7-2 (a))". The anchor's identity is "repository, revision, path
and span with the source digest". RFC7-2 (a) (`narrative-contract.md:91-92`)
defines an anchored claim as "resolvable through its claim block's source
anchors (RFC7-9, RFC7-10) to the one artifact that owns the fact". RFC7-10
(`:217-231`) says "A source anchor is machine-readable and typed: **(target
class, target identifier, optional fragment, target state)**". It allows
five target classes: kernel entity, doctrine/contract citation,
`openspec/**` anchor, decision/policy identifier, "an **evidence artifact
identifier** with integrity digest". It also says "Anchors embed durable
identifiers, never labels, paths, or coordinates (RFC6-8/9)". Adopted
REQ-polaris-generation-019 (overlay `:508`) says "Canonical anchors SHALL
use RFC7-10's target-specific identity, fragment and state representation".
Its scenario "Canonical anchors reject presentation and unstable targets"
(`:550-554`) refuses "a label/path in place of a durable target and
fragment". (c) names a path and a span as the anchor's identity. It names no
target class, and RFC7-10 and REQ-019 are absent from `warrants` and from
`parent_requirements`. The delta quotes neither RFC7-2 nor RFC7-10.
[Inferred] A lawful form probably exists: an admitted source span as an
evidence artifact identifier with integrity digest, with path and span as
the fragment or the target state. The requirement must say so and warrant
it. As written, a fresh implementer following (c) builds an anchor that
REQ-019's validation must refuse. This is not O1, which asks whether the
span is the leaf or the anchor. The packet poses no question about the
anchor's form. Round 1's route (ii), which this round adopted, carried the
gap in.

**Finding 2 — "Every other obligation of … 004 is unchanged" is false; the current meaning omits the 004 text that (b) and (c) displace** (revise)
`proposed/polaris-generation/spec.md:9`; `SEMANTIC-DELTA.md:13-23`;
`design.md:61-66`. Violates NORMATIVE-CHANGE-WORKFLOW (current meaning
stated), CC-SPEC-9 and brief criterion 2.
The effective 004 (overlay `:78`) also says "the contract band SHALL include
accepted contract and declared topology-placement references alongside
operative requirements/scenarios; the reality band SHALL retain the four
SDR-3 implementation-mapping classes queryably distinct". It says "Required
headings, the altitude order, authority bands and verbatim exact-source text
keep their structure; … leaves the leaf as the owning text". Its scenario
"Capability bands preserve their actual content populations" (`:127-131`)
says "contract exposes its accepted contracts, declared topology placement
and operative requirements/scenarios; reality exposes the four distinct
SDR-3 mapping classes". (b) fills the contract-class band "only from
admitted maintainer reference spans" and renders no reality band. (c)
replaces the leaf with a line. Those are readings of these sentences too,
yet the spec says "The profile changes only the three readings below; every
other obligation of REQ-polaris-generation-002, 004, 025 and 030 is
unchanged". The delta quotes three sentences and three scenarios of 004 and
omits these. [Inferred] Some of the displacement could be read as the
honest-absence clause doing its work. A contract band whose population is
maintainer prose, where 004 names operative requirements, is a substitution,
not an absence. Name these sentences and the scenario as displaced for a
non-governed subject, quote them, and remove "every other obligation … is
unchanged" or narrow it.

**Finding 3 — The selection predicate still has two forms; the round-1 Finding 6 disposition is false for one scenario** (revise)
`proposed/polaris-generation/spec.md:9`, `:77-81`, `:83-87`;
`SEMANTIC-DELTA.md:123`; `reviews/ROUND-1-DISPOSITIONS.md:87-95`. Violates
CC-SPEC-4 (oracle "without judgment") and CC-SPEC-9.
The requirement keys on the *admitted inventory*: "its admitted source
inventory holds no `openspec/**` specification, no adopted capability
declaration, no declared topology and no kernel evidence drawer". The
scenario "Governed subject keeps governed readings" keys on the *subject*,
with the round-1 wording: "the subject has adopted Syzygy declarations,
specifications or a kernel evidence drawer". It omits topology, and
"adopted Syzygy" qualifies specifications. The two diverge on (i) a subject
whose only governance artifact is declared topology, and (ii) a governed
subject whose `openspec/**` lies outside its admission. Line 9 selects the
profile for (ii), while the scenario's "selecting this profile for it fails
the evaluation" makes the same run fail. The disposition says "One
predicate … is used in the requirement and the scenario". That is true of
"Partly governed subject" and false of this one. Also, "kernel evidence
drawer" is Syzygy kernel state, not something an admitted source inventory
of an observed repository can hold. The predicate needs a named input for
it, such as the subject's kernel registration. `SEMANTIC-DELTA.md:123` still
says "the profile is chosen from the admitted observation record". The
disposition says the spec removed that phrase as undefined, and it survives
in the delta. Align the governed scenario to line 9's predicate, decide case
(ii) explicitly, and name where the drawer fact comes from.

**Finding 4 — "Each whole" is false for two quotes, and three relied-on clauses are unquoted; two dispositions say otherwise** (revise)
`SEMANTIC-DELTA.md:43`, `:45-53`, `:79-84`, `:114`;
`reviews/ROUND-1-DISPOSITIONS.md:51-52`, `:59-61`. Violates rule 8 ("Anchor
a contract claim to a defined clause and quote it") and NORMATIVE-CHANGE-WORKFLOW.
The delta introduces its RFC quotes as "each whole". The RFC7-13 quote is
its first paragraph (`narrative-contract.md:306-314`). The second paragraph
(`:316-322`) is omitted, though the delta's Warrant section (`:128`) relies
on it: "another named narrative under RFC7-6 may order its altitudes
differently … bound still by the per-altitude obligation and the
verbatim-leaf terminus". The "Thin, never absent" block is RFC7-6's second
paragraph (`:165-170`). It carries no clause identifier and omits RFC7-6's
first paragraph ("A governed project has at most one **primary
narrative**"). That sentence is itself material, because RFC7-6 speaks of a
*governed* project and this profile is for a non-governed one. RFC7-2 (the
anchor route of (c)), RFC7-17 (the class rule criterion 5 turns on) and
RFC7-33 (warranted and used by the Observable) are not quoted anywhere in
the delta. The round-1 disposition says "The delta quotes RFC7-14 and RFC7-13
whole". That is true of RFC7-14 and false of RFC7-13. It also says
"RFC1-14, RFC7-15 and RFC7-33 are … quoted whole in the delta", which is
false of RFC7-33. Quote each clause the change rests on, whole or marked as
an excerpt, and correct the two disposition sentences in a successor record,
never in the retained one.

**Finding 5 — The band membership of an absence line is unspecified, so the reality-band falsifier needs judgment** (note)
`proposed/polaris-generation/spec.md:13`, `:53-57`, `:65-69`, `:98`, `:101`.
Against RFC7-17 ("each block declaring its band machine-readably (RFC7-33)")
and CC-SPEC-4.
(b) "SHALL NOT render a reality-class band", yet requires a line reporting
it. The Observable inspects "the machine-readable band and authority-class
declarations (RFC7-33)". The spec does not say whether the absence line
declares itself a reality-band block (a collapsed band, as 004's governed
reading would have it), belongs to the argument band, or carries no band.
The Falsifier "a reality band … appears for a non-governed subject" decides
differently under each. State the line's machine band and class, or say it
declares none and why RFC7-17 permits that.

**Finding 6 — The round-1 Finding 7 repair is not carried into the packet or the task list** (note)
`OWNER-DECISION-PACKET.md:27-29`, `:52-57`;
`openspec/changes/polaris-non-governed-narrative-profile/tasks.md:26-28`.
Against CC-SPEC-9 and CC-REV-2 consistency.
The packet says "One line says what is absent and why", and the task list
says "one absence line". The spec now requires a line per absent band, at
most two. The O2 "Alternative" ("require the reality band to appear as a
single Unknown line only, which is what the package already does") restates
the recommendation, so the owner is offered no real alternative. Either
state a distinct alternative or drop it.

**Finding 7 — The withdrawn "no object" reason survives in two places** (note)
`SEMANTIC-DELTA.md:100`; `design.md:14`, `:16`. Against round-1 Finding 5's
disposition and AGENTS.md epistemic discipline.
The delta's [Inferred] paragraph opens "These clauses and the requirement
have no object for an observed repository … *in the sense the proposal
needs*: they do have a defined outcome". It asserts and denies in one
sentence. `design.md`'s table header is still "Why it has no object for an
observed repository", and its row "No capability declarations exist." is an
unlabelled claim about any observed repository. The corrected reason is
that a thin, defined outcome is replaced. Use that reason in both files.

**Finding 8 — The spec does not record O6, on which (a) rests** (note)
`proposed/polaris-generation/spec.md:17`. CC-SPEC-6 ("the spec records which
open questions it believes it does not settle").
The "does not settle" paragraph names O1, the dossier altitude order,
"advantages", the page budget and O5. (a) is drafted on O6's recommended
answer (maintainer documentation as RFC1-14's "the project's own spec or
shape documents"; `SEMANTIC-DELTA.md:112`), and O6 is absent from the spec.
O6 is an open owner question and does not block. The spec should name it as
O1 is named.

**Finding 9 — The ledger misses the hyphen-range citer form** (note)
`IMPACT-LEDGER.md:17-24`, `:49-50`. Rule 9 (an absence claim's denominator
covers the forms an identifier occurs in).
The B and E regexes accept `/ , and .. –` and ` to` only as separators
*ending* at 004. A range that spans 004 with a hyphen-minus is missed. Python
`re` `(?:REQ-polaris-generation-|[Rr]equirements? )(\d{3})\s*(?:\.\.\.?|–|—|-| to | through )\s*(?:REQ-polaris-generation-)?(\d{3})\b`,
filtered to ranges with start < 4 ≤ end, ran at `9a6e8e31` and hit 9 files.
4 of them fall outside A∪B∪E∪F. Three of the four concern this capability:
`openspec/changes/polaris-manifesto-generation/EXECUTION-PHASES.md:18`
("Requirements 001-012, 014-019 and 025"),
`docs/reviews/R-POLARIS-M6-GENERATOR-HONESTY-FUNNEL-RAW.md` and
`docs/reviews/R-POLARIS-M6-GENERATOR-HONESTY-FUNNEL-2-RAW.md`. The fourth
is the CAP1 spec's own numbering. All three are bound or raw, so the
disposition does not change. The citer population is 63, not 60, and the
ledger's "[Unknown]" sentence covers "a name other than these six forms",
which a range of the same name is not.

**Finding 10 — The residual laundering path and the frozen profile's record home are undisclosed** (note)
`proposed/polaris-generation/spec.md:11`; `design.md:22-36`;
`OWNER-DECISION-PACKET.md:78-94`. Against the adopted scenario "Catalog
membership comes from declarations" and REQ-019 ("Generator records SHALL
use explicit class/version and typed variants with separate ownership for
requests, inventories, controls…").
(1) Path class and marker are necessary conditions for "maintainer-written
and not generated". They are not sufficient: a code-generated reference
committed without a listed marker under an authored-documentation path
passes the observable while (a) forbids it. The oracle holds on prepared
snapshots. In production it is the frozen profile's marker list that
decides. Say so in `design.md` as a known residual. (2) The frozen profile
is a new run control record. O5's reasoning, that a glossary would need a
schema change no act authorizes, applies equally here. The package does not
say which REQ-019 record carries the frozen profile or whether the
implementation needs a schema change. `tasks.md:22-23` lists it as
implementation work.

**Finding 11 — "Partly governed subject" makes an outside repository's OpenSpec text the operative leaf** (note)
`proposed/polaris-generation/spec.md:83-87`. Against RFC7-14
(`narrative-contract.md:334-336`, "The leaf is the one place Polaris tells a
reader the text before them *is* operative").
[Inferred] For an observed repository that uses `openspec/**` with no
Syzygy adoption, the scenario requires "the `openspec/**` text is the
verbatim leaf", which RFC7-14 makes the place where Polaris calls text
operative. That may well be the governed reading's present effect. Stating
it as a binding scenario rests on the same RFC1-14 reading as O6 (a
project's own spec counts for Syzygy's purposes). It belongs beside O6 in
the packet, and needs no change to the bytes unless the owner rules O6 the
other way.

**Finding 12 — `tasks.md` carries no "binds nothing" banner** (note)
`openspec/changes/polaris-non-governed-narrative-profile/tasks.md:3-5`. Brief
criterion 9 ("every banner must say it binds nothing").
The head reads "Candidate checklist; unchecked obligations are unperformed.
This is not a dispatch plan, an adoption record or permission to implement".
That is true in substance but lacks the sentence the criterion names.

## Verdict rationale

Since round 1, the battery passes. No bound byte moves. The ID is free. All
13 quotes are byte-exact. Every ledger count re-derives at both commits, and
I differ from it nowhere. Round-1 Findings 1 and 8 to 12 are resolved, and
round-1 Findings 2 to 7 are resolved in substance in the spec. Four revise
findings prevent confirmation:

- (c)'s anchor names no RFC7-10 target class and is built from path and
  span, which RFC7-10 and adopted REQ-019 refuse.
- The spec says every other 004 obligation is unchanged when (b) and (c)
  displace 004's band-population and leaf sentences.
- The selection predicate still has two forms.
- Two round-1 dispositions claim quotes the delta does not carry.

O1, O2, O5 and O6 are open owner questions with no signed bytes assuming an
answer. They block nothing here.
