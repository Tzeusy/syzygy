# R-NON-GOVERNED-NARRATIVE-PROFILE-3 — independent review of the non-governed narrative profile, round 3
Reviewed commit: d867a535107cf58acdb7cbba814345cc49667dcd
Subject SHA-256: 3b2abfe9221c6aba641c86a23819a3fce5bb0e15617170e7aa7351fc479cb9b3
Verdict: CONFIRM WITH EXCEPTIONS

## Scope and method

This is a fresh-context review (CC-REV-1) of round 3, run against
`.syzygy/governance/contracts/candidates/non-governed-narrative-profile/REVIEW-BRIEF.md`.
I read the change in a detached worktree at the reviewed commit and modified
no tracked file. The merge base with `origin/main` is `b97b77ed`. The branch
adds 13 files and modifies one, `openspec/README.md`.

I read every file named under "What the reviewer is given". That covers the
five files under `openspec/changes/polaris-non-governed-narrative-profile/`,
the four package files, both earlier raws and both disposition records. I
also read each governing clause where it is defined:

- RFC7-2 `narrative-contract.md:87`, RFC7-6 `:160`, RFC7-10 `:217`, RFC7-13 `:306`,
  RFC7-14 `:324`, RFC7-15 `:340`, RFC7-17 `:376`, RFC7-18 `:401` and RFC7-19 `:409`.
- RFC7-33 in `rendering-and-surface.md:205`.
- RFC1-14 in `RFC-0001-project-graph-identity-state-planes.md:361`.
- RFC6-8 and RFC6-9 in `RFC-0006-cross-surface-selection-query-drawer.md:230` and following,
  for the meaning of "coordinates".
- The effective REQ-polaris-generation-004 (overlay `:76-131`) and 019 (overlay `:506` and following).

`sha256sum` printed every digest. A script run in this session produced every
count. I used Python `re` or `grep -F` for every load-bearing match. One
`grep -o -E` attempt hit ugrep's complexity limit; I discarded it and re-ran
the match in Python (rule 1).

## Checks run and their results

- **Battery.** [Observed] At `d867a535`, `python3 scripts/check_governance.py`
  prints "31 OK, 21 WARN, 0 FAIL (52 checks)", the same as at `9a6e8e31`. The
  package appears only in two CG-1f frozen-lane WARN lines, which are the two
  retained raws quoting the scratch path `…/specs/polaris-generation/spec.md`.
  `python3 scripts/check_spec_reconciliation.py --check` ends "7 of 7
  predicates without FAIL; PASS".
- **Bound bytes (criterion 3).** [Observed] `git diff --quiet b97b77ed HEAD --
  openspec/changes/polaris-manifesto-generation
  openspec/changes/polaris-manifesto-understanding-amendment` exits 0. I ran
  `git grep -l -F <sha256>` at HEAD for each of the 14 touched files' current
  digests and for the base digest of `openspec/README.md`. Every one returned
  0 tracked files. No `*-MANIFEST.txt`, `ACCEPTANCE-ACT-RECORD.md` or
  `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` names `openspec/README.md`.
  The added README row reads "Candidate — binds nothing; not one of the five
  in force". No act binds any byte the change touches.
- **Quotes (criteria 2 and 14).** [Observed] A Python script extracted the 20
  blockquotes in `SEMANTIC-DELTA.md`. The first is the banner and quotes no
  source. All 19 others are exact substrings of their sources. Blocks at
  `:17`, `:19`, `:21`, `:25`, `:31`, `:37`, `:222` and `:224` occur in both the
  base and the overlay spec. The RFC blocks occur in their defining modules.
  For each block the delta marks whole, I sliced the clause from its bold
  identifier to the next bold clause identifier or heading. I compared the
  two after collapsing whitespace. RFC7-2, RFC7-6, RFC7-10, RFC7-13, RFC7-14
  (its two blocks joined), RFC7-17, RFC7-19 and RFC1-14 are equal to their
  clauses, at 1279, 749, 1330, 1097, 978, 1519, 301 and 558 characters. The
  RFC7-15 block is equal to its whole clause (477/477) although the delta
  labels it "first paragraph" (Finding 1). RFC7-33 is 934 of 2,362
  characters and is correctly labelled an excerpt. No "whole" block is partial.
- **Displaced text (criterion 12).** [Observed] Every quoted fragment in the
  ten table rows (`SEMANTIC-DELTA.md:238-247`) is an exact substring of the
  effective requirement 004 (overlay `:76-131`): 13 fragments, 13 hits. The
  same holds for every quoted fragment in spec `:9`: 10 fragments, 10 hits.
  The completeness check is Finding 3.
- **Stable ID (criterion 7).** [Observed] The Python `re` sweep was
  `REQ-polaris-generation-032`, the continuation form, the prose short form
  and a bare `REQ-032`. It ran over `git ls-files` at HEAD: 2,003 paths, 4
  undecodable and skipped, 1,999 searched, 11 hits. Eight hits lie in the two
  change directories. The other three use bare `REQ-032` for the Capability 1
  requirement: `round-2026-08k/reviews/RS-2-TESTABILITY-RAW.md`,
  `RS-4-CONFIRMING-RAW.md` and `packages/cap1-conformance/src/req-032.conformance.test.ts`.
  `REQ-polaris-generation-032` is unused outside this change.
- **Ledger sweeps (criterion 8).** [Observed] My own script ran the seven
  published regexes over `git ls-tree -r -z` at `9a6e8e31`, excluding the two
  package prefixes. It covered 1,988 paths, skipped 4 and searched 1,984. The
  counts were A 47, B 11, C 70, D 92, E 7, F 15 and G 9. A∩B is 6, B∖A is 5
  and A∪B is 52. E∖(A∪B) is 4 files and F∖(A∪B) is 4 files, and A∪B∪E∪F is
  60. G∖(A∪B∪E∪F) is 4 files:
  - `EXECUTION-PHASES.md:18`;
  - the M6 funnel raws at lines 128 and 122;
  - the Capability 1 spec at line 830.

  The per-row table reproduces cell for cell: decisions 6/2/1/0/0/0, evidence
  19/3/10/14/2/10, raw 4/2/12/14/2/1, `.syzygy` 5/0/26/38/0/0, openspec
  5/1/13/13/2/2, code 3/1/4/4/0/1 and other 5/2/4/9/1/1. The eight named
  extra files match. My counts differ from the ledger's nowhere.

  For the second method, `git grep -l -F 'REQ-polaris-generation-004'` gives
  47 and `git grep -l -F -i 'declared capabilit'` gives 73, which is true as
  the ledger narrows it. The regexes miss one citer form (Finding 2).
- **Recount tooling (criterion 8).** [Observed] I extracted the commit with
  `git archive` into a scratch tree. Unmodified, the count script prints
  "PROJECT-STATUS.md asserts: 31 requirements, 182 scenarios". With the spec
  copied to `…/polaris-non-governed-narrative-profile/specs/polaris-generation/spec.md`,
  it prints "FAIL: expected exactly one base spec.md … found 2". The claimed
  failure holds. The subject has 12 `#### Scenario:` headings, so 194 is right.
- **Authority (criterion 9).** [Observed] I counted standalone 64-hex tokens.
  There are 0 in each of the 11 non-raw files across both directories, and 1
  in each raw (its own head, which CG-15 exempts). Every non-raw file says
  "binds nothing" at its head, including `tasks.md:3` (the round-2 Finding 12
  repair). No file labels the change accepted or adopted, and no file says a
  target repository body was read.
- **`generationAnchorId` (criterion 6).** [Observed]
  `packages/polaris-generation-core/src/generation-source.ts:42-48` builds
  `${repositoryId}@${revision}:${path}#${objectId}` plus `:${start}-${end}`.
  The delta's account (`SEMANTIC-DELTA.md:263`) and `design.md:61-63` say it
  "joins repository id, revision, path, object id and byte range … a
  concatenation, not a digest". That is accurate. `gitBlobObjectId` (`:50-53`)
  produces a git blob id under `sha1` or `sha256`. The source record has no
  algorithm field (Finding 6).

## Answers to the acceptance criteria

1. **Class.** Normative is right. (a) changes what counts as a declaration,
   (c) changes the exact-source terminus, and 004's effective meaning changes
   for a class of subject. The stated reason (`SEMANTIC-DELTA.md:230`) no
   longer contradicts itself.
2. **Quotes.** 19 of 19 source quotes are exact, and each whole block is the
   whole clause. One label is wrong (Finding 1).
3. **Bound bytes.** The change touches none, and the battery passes.
4. **(a).** [Inferred] (a) stays inside the adopted rule. Code, tests,
   comments, layout and generated reference text cannot declare. Forms, path
   classes and markers are fixed outside the producer before discovery. The
   late-found and producer-alteration scenarios are real constraints. The
   unmarked-generated-file laundering path remains. It is now stated as a
   known residual (`design.md:72-79`), and the spec claims no stronger
   guarantee.
5. **(b).** [Inferred] Not rendering a reality band is a lawful reading, not
   an exception. RFC7-17 (`:395-399`) reads: "count and ordering are a V0
   default, not a frozen constraint … A narrative composing its deep dive
   differently still assigns every band to one of the three classes and
   declares it machine-readably". Spec `:13` makes each absence line "a
   collapsed block (RFC7-19) that declares, machine-readably (RFC7-33), the
   band it reports on and that band's authority class". That is RFC7-19's
   collapse ("A block with no content collapses to one honest line"). The
   reality band is assigned to its class and is not hidden. "At most two"
   lines, one per absent band, is a lawful per-block reading of RFC7-19.
6. **(c).** The anchor repair uses a target class that RFC7-10 defines. The
   clause reads, `narrative-contract.md:217-219` and `:227`: "A source anchor is
   machine-readable and typed: **(target class, target identifier, optional
   fragment, target state)**, target class one of: … an **evidence artifact
   identifier** with integrity digest." Its target-state paragraph (`:233-236`)
   gives, for an "evidence artifact, its **revision**". The spec fills the
   tuple accordingly: class evidence artifact identifier, identifier the
   content-addressed object id with its algorithm, fragment the byte range,
   state the admission revision. RFC7-10's ban, "Anchors embed durable
   identifiers, never labels, paths, or coordinates (RFC6-8/9)", is met. RFC6-9
   uses "coordinates" for map layout ("re-laying-out the map changes **no URL**"),
   and the byte range sits in RFC7-10's own "optional fragment" slot.
   RFC1-14's object table (RFC-0001 `:214`) gives an Evidence artifact
   "identifier + integrity digest". That supports the reading, and O7 leaves
   the scope question to the owner.

   REQ-019's scenario "Canonical anchors reject presentation and unstable
   targets" refuses "a label/path in place of a durable target and fragment".
   (c) supplies a durable target and fragment and keeps path and repository as
   labels, so it passes. [Inferred] The leaf route is lawful without amending
   RFC7-13 or RFC7-14 only under the reading that RFC7-19's honest line
   discharges RFC7-13's "every narrative descends to a **verbatim
   specification leaf**" where no specification exists. Read literally, that
   clause is not met. The packet puts this to the owner as O1, so it does not
   block. The delta's account of `generationAnchorId` matches the code, with
   one gap (Finding 6).
7. **CC-SPEC.** The form is named (event-response). Case, observable, oracle,
   independence and falsifier are present. The warrants include RFC7-10 and
   REQ-019, and `GOVERNING-DEPENDENCIES.md` equals the warrants block, with 12
   contracts and 7 parent requirements. The ID is unused across 1,999 searched
   paths. Non-goals and open questions (O1, O5, O6 and O7, plus the record
   home) are recorded at spec `:17`. One wording ambiguity remains in a
   scenario (Finding 4).
8. **Ledger.** Every count reproduces, and the 63 is right over the seven
   published forms. One citer form is missed (Finding 2).
9. **Authority.** No adoption claim, no act digest and no body read. Two
   sentences still say no review has run (Finding 5).
10. **Labels.** They hold, except the stale review-status sentences
    (Finding 5).
11. **Repairs.** I checked round 1, findings 1–12. Every disposition is true of
    the current bytes as corrected by round 2. The round-1 F6 sentence and its
    predicate parenthetical are withdrawn by `ROUND-2-DISPOSITIONS.md:61-65`.

    I checked round 2, findings 1–12. Findings 1, 3 and 5–12 are true of the
    bytes:
    - F1: the anchor is in RFC7-10's form and warranted.
    - F3: one four-condition predicate, case (ii) decided at spec `:79`, and
      the phrase "admitted observation record" is absent from the package (0
      hits).
    - F5: spec `:13` and the falsifier `:101`.
    - F6: packet `:27-30`, `tasks.md:31-34` and a distinct O2 alternative at
      `:55-59`.
    - F7: delta `:230` and the `design.md` table header at `:14`.
    - F8: spec `:17`.
    - F9: ledger sweep G.
    - F10: `design.md` "Known residuals".
    - F11: packet `:120-124`.
    - F12: `tasks.md:3`.

    F2 is repaired in substance, but its disposition says the delta "no longer
    say[s] 'three readings'", which is false (Finding 7). Two sentences, one in
    F4's disposition and one in the delta itself, misdescribe the quotes
    (Finding 1).

    New defects from repairs: Finding 1 (the RFC7-15 label written in the
    round-3 repair) and Finding 4. The F2 repair's list stops one sentence
    short (Finding 3).

    Copied counts: none of the ledger figures. The disposition's "All 20
    blockquotes are exact substrings" counts the banner, so 19 is the figure
    (Finding 1).

    The glossary deferral (O5) is justified by its sources. The scenario "No
    supported optional asset" appears verbatim in both the base (`:201`) and
    the overlay (`:93`). 004 governs glossaries for every subject ("Glossaries
    SHALL explain concepts where needed for comprehension"). `glossar` occurs
    in `packages/polaris-generation-core/src` only in `prompts.ts`, so no
    schema field exists.
12. **Displaced text.** Every listed fragment is exact and changes in effect.
    One sentence, and the leading outcome of one listed scenario, are not
    named (Finding 3).
13. **One selection predicate.** The requirement, "Governed subject keeps
    governed readings", "Profile selected from the admitted record" and the
    delta (`:272`) use one predicate. Case (ii) is decided as governed.
    "Partly governed subject" uses a wording that a silent project input also
    satisfies (Finding 4).
14. **Quote labels.** No "whole" block is partial. One block is labelled as
    partial when it is whole, and one framing sentence is false (Finding 1).

## Findings

**Finding 1 — The RFC7-15 block is labelled a first paragraph when it is the whole clause, and a phantom second paragraph is attributed to it** (note)

Evidence:
- `SEMANTIC-DELTA.md:151` heads the block "RFC7-15, first paragraph (the
  clause's second paragraph, "Thin, never absent", is quoted under RFC7-6
  above)".
- RFC7-15 (`narrative-contract.md:340-346`) is one paragraph. RFC7-16 begins
  at `:348`.
- "**Thin, never absent.**" is RFC7-6's second paragraph (`:165-170`), and the
  delta correctly quotes it there at `:78-83`.
- `SEMANTIC-DELTA.md:43` says "RFC7-14 is the only block that is two quoted
  paragraphs of one clause". The RFC7-2, RFC7-6 and RFC7-13 blocks each carry
  two paragraphs too.
- `ROUND-2-DISPOSITIONS.md:68-71` says RFC7-15 is quoted whole and that "All
  20 blockquotes are exact substrings of their sources". Block 1 is the
  banner, so 19 quotes are exact.

This is against rule 8 ("Anchor a contract claim to a defined clause") and
brief criterion 14. The quoted bytes are right. The label misattributes RFC7-6
text to RFC7-15, so the delta and its own disposition contradict each other.
Mark the block whole, drop the parenthetical, and say what the `:43` sentence
means (two blockquotes, not two paragraphs).

**Finding 2 — The ledger's sweeps miss the bare `REQ-004` short form; 15 more files cite requirement 004** (note)

Evidence: `IMPACT-LEDGER.md:169-177`, `:196`, `:215-217`. This is against
rule 9 (the denominator covers the forms an identifier occurs in) and brief
criterion 8 ("Name any citer form the regexes miss").

[Observed] The Python `re` pattern was
`(?<![A-Za-z0-9-])REQ-(?:\d{3}\s*(?:/|,|, and| and|\.\.|–)\s*)*004\b`. It ran
over the same 1,984 searched paths at `9a6e8e31` and hit 28 files. Of these,
16 lie outside A∪B∪E∪F∪G. One is not a citer: in
`three-surface-poc-readability-successor/proposed/design.md.patch:88`,
`REQ-004` is a POC requirement. The other 15 cite polaris-generation 004:
- the four `POLARIS-TREE-FORM-AMENDMENT-REVIEW-{1..4}-RAW.md`;
- `docs/design/POLARIS-GENERATOR-RFC7-COVERAGE-V2.md:13` ("REQ-004 establishes
  the band class/order") and `-V3.md:5`;
- four files under `docs/evidence/polaris-understanding-reconciliation-2026-09-28/`
  (`README.md:18`, `REVIEW-RAW.md:13`, `REVIEW-1-RAW.md:15`, `HISTORY-REVIEW-13-RAW.md:57`);
- `docs/evidence/spec-readability-reconciliation-2026-10-02/README.md:69`;
- `docs/polaris-generation/REDIS-DOSSIER-GAP-ANALYSIS.md:96`
  ("REQ-002/004/006/…");
- `docs/polaris-generation/TRACKER.md:173`;
- the two `docs/pursuits/2026-09-22-vision-pursuit-*.json` files.

The citer population is therefore 78 (63 + 15). The ledger's [Unknown]
sentence (`:215-217`) does disclose that other forms are uncovered. Most of
the 15 are raws or evidence. Two design notes and `TRACKER.md` are unbound
docs that read 004's band rule, so they belong in the disposition with an
explicit "no edit" or "optional" call. Add the sweep and its regex in full.

**Finding 3 — One more 004 sentence carries "authority bands" and is not named as displaced, and one listed scenario is quoted short of its displaced outcome** (note)

Evidence: spec `:9` ("Every other sentence and scenario of
REQ-polaris-generation-004 … is unchanged"); `SEMANTIC-DELTA.md:234`, `:243`,
`:246`; overlay `:78`. This is against brief criterion 12 and CC-SPEC-9.

[Observed] The effective 004 says: "Project-specific headings and
composition SHALL preserve the existing primary altitude order, authority
bands and required populations; missing content SHALL remain honestly absent
or Unknown, not invented to fill a template." `grep -F` and a Python
substring check over all 13 tracked files of the change find neither
"Project-specific headings" nor "required populations".

The package treats the identical words "authority bands" in the tree-form
sentence as displaced (`:243`, "'Authority bands' is displaced as the rows
above state"). Here it leaves them, and "required populations", under
"unchanged". [Inferred] The sentence can be read as unchanged, because its own
clause keeps missing populations honestly absent. Either reading is
defensible, but the package must take the same one for both sentences.

Likewise, the row for "Capability detail keeps three authority classes"
(`:246`) quotes only its AND outcome. The THEN outcome, "its default argument,
contract and reality bands appear in that order", is also displaced, because
no reality band appears. Spec `:9`'s generic "reality-band outcomes" covers
it, so this is a quote-coverage gap only.

The adopted scenario "Catalog membership comes from declarations" keys on
"adopted capability declarations". Its effect also turns on (a)'s reading of
"declared". Row `:238` covers that reading for the clause and not for the
scenario, which is the same O6 question.

Name the sentence (or say why it is unchanged), extend the `:246` quote, and
note the scenario beside row 1.

**Finding 4 — "Partly governed subject" says the project input "records no evidence drawer", which a silent input also satisfies** (note)

Evidence: spec `:85` against spec `:9`. This is against CC-SPEC-4 and brief
criterion 13.

Line 9 separates three input states. In the first, the input records that a
drawer exists. In the second, it "states that no kernel evidence drawer
exists". In the third, it "does not state whether a drawer exists", and then
"the profile SHALL NOT be selected and the run is refused or limited". The
scenario's WHEN, "the project input records no evidence drawer", is true of
both the second and the third state. Its THEN, "composes under the governed
readings", is right for both: the subject is governed by its `openspec/**`
either way, and the profile is not selected. Line 9's "refused or limited"
for a silent input does not say whether it applies to a subject already
governed by its inventory. An oracle writer could therefore expect "refused
or limited" where the scenario expects governed composition. [Inferred] The
fix is one phrase: "states that no evidence drawer exists". Alternatively,
line 9 could say that the refusal applies only when the inventory conditions
are also unmet.

**Finding 5 — Two sentences still say no review has been run** (note)

Evidence: `SEMANTIC-DELTA.md:297-298` ("**Reviewer:** not yet assigned …
**Verdict:** none — no review has been run") and `OWNER-DECISION-PACKET.md:151-152`
("Fresh-context review before any offering … None has been run."). This is
against AGENTS.md's epistemic discipline and the "mark staleness at the stale
sentence" lesson.

At the reviewed commit, `reviews/` holds two REVISE raws, and the brief
(`:5`) says so. Both sentences are false of the bytes they ship with. Name the
rounds and their verdicts of record, or point to `reviews/`.

**Finding 6 — The delta's projection of `generationAnchorId` omits the hash algorithm that (c) requires named** (note)

Evidence: spec `:15` ("content-addressed object identifier with its hash
algorithm named"); `SEMANTIC-DELTA.md:263` ("a lawful anchor is a projection
of those three"); `design.md:63`; `tasks.md:35-38` ("object identifier and
algorithm … projected from the generator's source fields");
`generation-source.ts:40`, `:50-53`.

[Observed] The source record carries `objectId` as 40 or 64 hex
(`hexObjectId`) and no algorithm field. `gitBlobObjectId` takes `sha1` or
`sha256`. The algorithm is recoverable only from the id's length. The three
projected fields do not supply a named algorithm, and "projected from the
generator's source fields" overstates what the fields hold. Say that the
algorithm is derived from the id's length or must be added to the record, and
put it beside the record-home Unknown (`design.md:80-85`).

**Finding 7 — The round-2 Finding 2 disposition says the delta no longer says "three readings"; it does** (note)

Evidence: `ROUND-2-DISPOSITIONS.md:48` ("The preamble, proposal and delta no
longer say 'three readings'") against `SEMANTIC-DELTA.md:253` ("Three
readings, in short:"). The packet also says "the three readings here" at
`OWNER-DECISION-PACKET.md:88`. This is against brief criterion 11.

The surviving uses introduce (a)–(c) and do not reassert the withdrawn "the
profile changes only the three readings" claim, so the substance is
repaired. The disposition's sentence is literally false of the bytes. Correct
it in the next disposition record, not in this one.

## Verdict rationale

The round-2 revise findings are repaired in the bytes. (c)'s anchor now fills
RFC7-10's typed tuple with a target class the clause defines ("an **evidence
artifact identifier** with integrity digest"), keeps path and repository as
labels, and meets REQ-019's refusal scenario. 004's displaced text is listed
and quoted exactly. The selection predicate has one form, and case (ii) is
decided. Every quote the delta calls whole is the whole clause.

Every count in the ledger re-derives at `9a6e8e31`. The battery passes, no
bound byte moves, and the ID is free. The seven findings are notes: a
mislabelled quote, an unswept citer form, an incomplete but recoverable
displaced-text list, one ambiguous scenario phrase, two stale review-status
sentences, an unstated algorithm source and one false disposition sentence.
None changes what an implementer must build or what the owner is asked. O1,
O6 and O7 remain the owner's and block nothing here.
