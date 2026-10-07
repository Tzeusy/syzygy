# R-ARBITRARY-PUBLIC-REPO-3
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: b7a7758c22eb0e546a399340b3e2f3e827e137ee
Subject: openspec/changes/polaris-dossier-arbitrary-public-repo/

Reviewer: fresh-context reviewer (Claude Opus 5.5), 2026-10-08. Read-only.
Round 3, the last round. Bytes were read with `git archive b7a7758c…` of the
change directory, `openspec/README.md`, both earlier raws, the four installed
`polaris-generation` spec files, doctrine, the RFC modules and the cited act
records. Ledger sweeps were re-run over `git archive 3409ef5a`. No external or
target repository content was fetched. The network was used only for `git
fetch` of the branch and `gh pr view 392`. Scratch scripts: `r3_check.py`
(counts, predecessor quotes, AMENDMENTS quotes, act types), `r3_ledger.py`
(sweeps A–F) and `r3_sweep.py` (overclaim phrases, history passages, 039
references).

Line anchors refer to the files at `b7a7758c`. `spec.md` means
`proposed/polaris-generation/spec.md`. Its requirement paragraphs are single
long lines, so a line anchor names a paragraph.

## Confirmations (no finding)

- [Observed] **Counts** (`r3_check.py`). There are 3 requirements:
  037 has 21 scenarios, 038 has 10 and 039 has 4, for 35 in all. A
  line-start count also gives 35. Without 039 the figures are 2 requirements
  and 31 scenarios. These equal `IMPACT-LEDGER.md:95`. If Q2 is answered no,
  one more scenario goes ("Ancestor commits read with history admitted"),
  which is 34, or 30 without 039. The ledger says "one scenario fewer"
  (`:103-106`).
- [Observed] **Ledger sweeps A–F** (`r3_ledger.py`) re-derived over
  `3409ef5a`: 2,569 paths, 4 non-UTF-8 skipped, 2,565 searched.
  - A: 37 = 6/1/2/9/0/19/0.
  - B: 181 = 33/10/24/54/10/40/10.
  - C: 77 = 7/5/3/20/4/37/1.
  - D: 19 = 1/0/3/4/2/7/2.
  - E: 34 = 7/0/0/7/3/16/1.
  - F: 0.

  Every cell equals `IMPACT-LEDGER.md:20-25`. A second method,
  `git grep -l -F` for the three identifiers at the current `origin/main`,
  returns no file.
- [Observed] **Predecessor quotes in `spec.md`.** All 13 distinct quoted
  predecessor spans occur verbatim, after whitespace normalisation, in the
  four installed spec files. They are:
  - from 033: three sentences and the falsifier arm;
  - from 025: one sentence;
  - from 032: the drawer clause and the two sentences of (a);
  - from 034: two spans;
  - from 002: two spans.

  The four remaining quoted strings are the change's own markers and scenario
  titles.
- [Observed] **Rule 8, REQ-032.** The two REQ-032 sentences that
  `spec.md:192` names are exact. The first is "A source counts as
  maintainer-written and not generated only when it lies under a path class
  the frozen profile declares as authored documentation or manifest, … is
  reported as a source the profile did not cover". The second is "The frozen
  profile, its declaration forms and its path and marker rules SHALL be fixed
  … and recorded before discovery began". Both are in REQ-032 (a), at
  `polaris-non-governed-narrative-profile/specs/polaris-generation/spec.md:11`.
  The citation "REQ-polaris-generation-032 (a)" at `spec.md:184` resolves.
- [Observed] **AMENDMENTS "Current meaning" blocks.** All 11 of 11 are exact
  against `architecture.md`, RFC-0001, RFC-0003 `manifests-and-namespace.md`
  and RFC-0005 `consent-egress-secrets.md`.
  - The A3 change to RFC3-7's opening quotes `manifests-and-namespace.md:256-258`
    exactly: "**RFC3-7.** **Consent records** are governance acts stored in
    `.syzygy/governance/decisions/`, referenced — never embedded — from the
    declaration. Two kinds:".
  - Its proposed replacement keeps that prefix byte for byte and appends the
    standing-record clause (`AMENDMENTS.md:357-361`).
- [Observed] **Act types.** `DOSSIER-LOCAL-AGENT-D9-IN-FORCE-ACT.md` reads
  "Act type: `bind-exact-bytes`", which A1b names (`AMENDMENTS.md:57`).
  `PUBLIC-REPO-ADMISSION-REDIS-OBSERVATION-ACT.md` reads "Act type:
  `consent-observation`", which A5 names (`AMENDMENTS.md:61`).
  `PWB-BUTLERS-OBSERVATION-CONSENT-ACT.md` carries the same type.
- [Observed] **Q6 "no" strike.** No passage of 037 or 038 names REQ-039.
  `r3_sweep.py` finds "039" in `spec.md` only at `:3` (the intro) and inside
  039 itself. `GOVERNING-DEPENDENCIES.md` equals the union of the three
  warrants blocks. Its `REQ-polaris-generation-038` parent entry comes from
  039 only and goes away at regeneration, as `proposal.md:139-141` says.
- [Observed] **VIS-4.** Every file carries a candidate banner. The packet
  says "Nothing here is decided" (`OWNER-PACKET.md:4`). Q0–Q8 each carry a
  recommendation, and Q1 and Q3 recommend per part. PR #392 is still `OPEN`,
  and the packet now says "Once open PR #392 merges" (`:85`) and "would
  enforce" (`:93`).
- [Observed] `openspec/README.md:42`: the row says "Candidate, drafted
  2026-10-08; no act binds it".

## Round-2 findings

| R2 | Status | Evidence at `b7a7758c` |
|---|---|---|
| B1 exclusion bypass, absolute guarantee | **Resolved** | No provenance is claimed: "Syzygy makes no network request, so it cannot establish which repository a clone came from: that a run's repository is not one of these rests on the operator's declaration, and is Inferred" (`spec.md:13`). (a) The fold now handles the scheme including the scp form, user information, port, `www.`, trailing `/` and `.git`, and case-folds "the host and the whole path"; "an over-match only refuses" (`:16`). (b) "the declared URL is never checked against the clone" (`:19`). (c) A filesystem-locator comparison has been added (`:16`). (d) Two residuals are named on every page (`:19`), with the Redis example. The packet states both: "If you give a different URL and a new name, nothing offline can tell … Butlers' consent names only a local folder, so a copy of it elsewhere under a new name also goes ahead" (`OWNER-PACKET.md:87`). The phrase "cannot come back under a new name" is gone [Observed, `r3_sweep.py`, no hit in any file of the change]. (e) A1 (`AMENDMENTS.md:123-126`), A3 (`:350-353`) and A4 (`:449-450`) each say the exclusion rests on the operator's declaration. (f) The population is defined by state (`spec.md:13`); see note 5 for location. (g) New scenario "Consented repository at an unconsented commit under its own URL" (`:71-75`). The proposal (`:96-100`) and ledger (`:56-60`) no longer say "never reaches". |
| B2 vendored class undefined | **Resolved**, with notes 4 and 5 | `spec.md:184` defines the third-party path class concretely: (i) ten directory segments, case-folded, at any depth; (ii) submodule paths; (iii) `.gitattributes` `linguist-vendored`; (iv) an optional profile rule. A root `README.md` has no directory segment, so it is outside (i). Everything outside the class is a maintainer source, and the text says so: "source code and its comments, tests, and every source that REQ-polaris-generation-032 counts as authored documentation or manifest and that lies outside the class remain maintainer sources". `:192` names both REQ-032 sentences and reads them exactly (see the confirmation above). Runs with no profile, governed runs included, apply (i)–(iii) (`:192`). There are new scenarios "Bundled dependency text is not maintainer-stated" (`:204-208`) and a `src/` source comment (`:200`). |
| B3 trailers leak identities | **Resolved**, with note 3 | `spec.md:23` names eight trailers and says "ignoring case and leading whitespace". Lines with an e-mail address pattern are withheld and recorded hash-not-body. The free-prose residual is disclosed. The scenario at `:115-117` uses `signed-off-by:` and `Co-Authored-By:`, which exercises case. The falsifier covers "a message line the identity screen withholds" (`:167`). The packet's Q2 matches the spec (`OWNER-PACKET.md:102-106`). |
| N4 Q2 "no" leaves the reread | **Partly** | Q2 now says "the history text is deleted from the spec and from the RFC 0005 amendment before you sign" (`OWNER-PACKET.md:108-110`). The A4 clause is bracketed (`AMENDMENTS.md:451-453`) and the intro lists the passages (`spec.md:3`). The strike list does not reach every passage, and the marker invariant it states is false. See new note 1. |
| N5 local commits overclaim | **Resolved** in spec and design; packet residual in note 1 | `spec.md:21`: "A clone that still holds the public parent of a locally made commit is therefore refused. A local commit in a clone re-shallowed to that commit alone … cannot be told apart from a published one without a network request". The rule is conditioned on history not being admitted, and `:23` says history lifts it. #392 is now written as conditional. Packet Q2 does not mention that history lifts the shape refusal (note 1). |
| N6 A1 act form, A5 type | **Resolved** | A1b `bind-exact-bytes` is in `AMENDMENTS.md:57`, the Q0 table (`OWNER-PACKET.md:59`), Q8 (`:177`), the ledger (`:88`), `tasks.md:20` and design slice 1. A5 is `consent-observation` (`AMENDMENTS.md:61`). Both are verified against the act records above. |
| N7 039 dangling refs, `v1-reserved` | **Resolved** | 038 keys on ruling 10b itself (`spec.md:188`), not on 039. 039's `Scope:` is stated in words (`:285`). The string `v1-reserved` is absent from the change [Observed, `r3_sweep.py`]. |
| N8 RFC3-7 reference | **Resolved** | The A3 proposed opening says the standing record is "referenced from the observing Project's declaration in the same way" (`AMENDMENTS.md:357-361`). The text also discloses that no declaration is tracked and that REQ-037 does not wait for one (`:363-366`; `design.md:256-263`). |
| N9 direction gloss | **Resolved** | `AMENDMENTS.md:153-157` marks the gloss "[Inferred]" and says the direction "does not say it". `design.md:60-64` and `proposal.md:12-15` agree. Q0 says the alternative "also meets your recorded direction as written" (`OWNER-PACKET.md:74-77`). |

**Round 1, regression check.** No round-1 resolution has regressed
[Observed].
- B1: amendment, not reading (`spec.md:3`, `AMENDMENTS.md:10`,
  `OWNER-PACKET.md:34-35`).
- B3: Redis keeps its basis (`spec.md:3`, scenario `:155-159`).
- B4: history is off by default and the 033 reread is named (`:21`, `:23`).
- B5: the verdict classifies every Inferred block (`:190`).
- N8: governed attribution (`design.md:140-161`).
- N9: execution refused by default (`spec.md:25`).
- N10: installed registry copy (`design.md:269-276`).
- N11: marking and backstop (`spec.md:279`).
- N12: the drawer statement is labelled Inferred (`:27`).

## New findings

### 1. A Q2 "no" does not cleanly strike history; the stated marker invariant is false, and the standing record's history field stays load-bearing (note)

**Anchors.**
- `spec.md:3`: "Every passage that admits history names 'the history option
  (packet Q2)' or opens 'History option (packet Q2)' … If the owner answers
  no, each of them is struck before sign-off".
- `OWNER-PACKET.md:108-110`: "the history text is deleted … so a later edit
  of the standing permission alone could not switch history on."

**Analysis [Observed, `r3_sweep.py`].** The sweep found these passages that
depend on history and do not carry the marker:
- the conditional "Where the standing record does not admit history"
  (`spec.md:21`);
- the WHEN clauses of "Local commit on top of a public commit" (`:103`) and
  "Ancestor read without history admitted" (`:109`);
- the disclosure "whether history is admitted, and, where it is, that
  author, committer, signature and identity-screened message lines are
  withheld" (`:29`);
- the Case arms "history … fields" and "ancestor commits with … identity
  trailers" (`:163`);
- the falsifier arms "reachable ancestor", "or an ancestor tree or blob is
  read where it is" and "a message line the identity screen withholds"
  (`:167`);
- 038's Case "with history admitted and not admitted" (`:260`).

The intro covers the falsifier arms only by the description "the history
arms of its falsifier". It does not say whether the guard arms (for example
"an ancestor commit is read where history is not admitted") are struck or
kept. The scenario at `:115` carries "(history option, packet Q2)", which is
not the exact string the intro gives.

**Consequence [Inferred].** A strike that follows the marker leaves two
problems:
- "the identity screen" is referenced at `:29` and `:167`, but is defined
  only in the struck paragraph.
- The standing record's history field (`design.md:50`) still decides
  `:21`'s one-commit clone shape. A later standing-record version that
  "admits history" would then lift the local-commit refusal with no spec
  change. Ancestor reads stay barred, because 033's sentence is no longer
  reread. So the packet's sentence holds for reads but not for the shape
  check.

Separately, the Q2 option text does not tell the owner that a yes also lifts
the local-commit shape refusal (`spec.md:23`: "a local commit on top of a
public one is no longer refused by shape").

**Repair.**
- Under Q2 "no", make `:21`, `:103` and `:109` unconditional.
- Mark every passage above with the exact marker. Alternatively, list each
  one by line in the intro and in `tasks.md:18`, saying which guard arms
  stay.
- Strike the standing record's history field from `design.md` §1.
- Add one line to Q2's option: "a commit you made on top of a public one is
  then no longer refused by shape."

### 2. The pinned commit's own author, committer and signature lines are withheld only under the history option (note)

**Anchor.** `spec.md:23` sits inside the struck paragraph: "Syzygy SHALL
withhold the author and committer lines of every commit object, and any
signature it carries, before classification."

**Clause.** The admission scope includes "the pinned commit's commit object"
(`:11`). REQ-033 says nothing about author or committer lines [Observed: 0
hits for "committer" in `polaris-dossier-local-agent-mode/.../spec.md`].

**Analysis [Inferred].** Under the recommended Q2 "no", 037 has no rule for
the identity lines of the one commit object every standing run reads. The
falsifier arm "an author, committer or signature line … is stored, rendered"
(`:167`) is struck or kept depending on how "history arms" is read. Commit
messages are uncitable without history (`:190`), so the practical exposure
is small. Redis runs have the same gap today.

**Repair.** Move the author, committer and signature withholding out of the
history paragraph, so it applies to the pinned commit of every standing run.
Alternatively, state that the pinned commit object's header lines are never
stored, rendered or quoted. Keep that falsifier arm outside the strike list.

### 3. The identity screen's e-mail pattern is unpublished and its trailer list is closed (note)

**Anchor.** `spec.md:23`: "withholds every line which contains an e-mail
address pattern or begins, ignoring case and leading whitespace, with one of
the trailers `Signed-off-by:`, … or `Cc:`".

**Analysis [Inferred, general knowledge].**
- "An e-mail address pattern" is not a predicate. Implementations will
  differ on `<user@localhost>`, obfuscated forms and bare `@handle`. This is
  the class AGENTS.md's run-form lesson warns about: publish the regex.
- Common identity trailers outside the list pass when they carry a name
  without an address. Examples are `Helped-by:`, `Approved-by:`,
  `Requested-by:`, `Bisected-by:` and `Authored-by:`. A trailer is not "free
  prose", so the disclosed residual does not cover these.
- A folded trailer's continuation line, indented under the trailer, is not
  withheld.
- A hash-not-body record of a low-entropy line such as `Signed-off-by: Name
  <addr>` can be confirmed by guessing. Whether that is acceptable is part
  of the privacy question the spec already defers.

**Repair.**
- Publish the pattern (for example `[^\s<>@]+@[^\s<>@]+`) and state that an
  over-match only withholds.
- Add a generic arm `^\s*[A-Za-z][A-Za-z0-9-]*-by:`, ignoring case, beside
  the named list.
- Withhold continuation lines of a withheld trailer.
- Note the hash-linkability point in Q2's privacy sentence.

### 4. REQ-038 says the class "withdraws no maintainer-stated advantage except one quoted from third-party text", and the packet says "no advantage you have today is lost"; neither is established (note)

**Anchors.**
- `spec.md:184`: "so this rule withdraws no maintainer-stated advantage
  except one quoted from third-party text".
- `OWNER-PACKET.md:136-137`: "so no advantage you have today is lost".

**Analysis.**
- [Inferred] The class is defined by path, and the same paragraph calls it a
  heuristic. Text the maintainers wrote under a class segment loses
  maintainer-stated status. Examples are a project's own `deps/README` about
  how it vendors, or an `external/` or `extern/` module of its own code. So
  the rule withdraws any advantage quoted from inside the class, whoever
  wrote it.
- [Unknown] Whether any advantage in the existing Redis dossier quotes a
  path inside the class was not checked. That would need reading the
  dossier, which this review did not do.

**Repair.**
- Reword `:184` to "withdraws maintainer-stated status only from text inside
  the class, which may include maintainer-written text there; that
  over-exclusion is the heuristic's cost".
- In Q4, either verify the Redis dossier's advantage anchors against the
  class and cite the check, or say "[Unknown] whether any current Redis
  advantage quotes such a path".

### 5. Three predicates are not yet testable as written: `.gitattributes` semantics, path normalisation, and where the compared records live (note)

**Anchors.**
- `spec.md:184` (iii): "every path that a `.gitattributes` file at the
  pinned revision marks with the attribute `linguist-vendored`".
- `:16`: "after both are made absolute and normalised".
- `:13`: "every observation consent record Syzygy holds, whether performed,
  withdrawn, revoked, or prepared and never performed".

**Analysis [Inferred].**
- Git attributes can be set, unset (`-linguist-vendored`) or given a value
  (`linguist-vendored=false`). They can also be overridden by deeper
  `.gitattributes` files and by macros. "Marks with the attribute" does not
  say which of these count.
- "Normalised" for a filesystem path does not say whether it is lexical or
  resolves symbolic links. That decides whether a symlinked Butlers checkout
  matches.
- The population is defined by state, not by location. The Redis consent
  instance is under `contracts/candidates/public-repo-admission/instances/`.
  Butlers' consent is in `decisions/`. Prepared packets can live anywhere. A
  gate and its oracle need the same enumeration.

**Repair.**
- Say "set to true by git's attribute resolution at the pinned tree (unset
  or `false` does not count)".
- Say "lexically normalised; symbolic links are resolved" (or not).
- Name the directories or the registry from which compared records are
  enumerated, and make the oracle use the same list.

### 6. Q6 does not say that 038 already admits reconstructed advantages once 10b is reversed, even with 039 struck (note)

**Anchors.**
- `spec.md:188`: "a block of the advantage kind with a `reconstructed`
  basis fails the check while that ruling stands unreversed".
- `OWNER-PACKET.md:156-165`: Q6 describes only 039 under "Yes", and
  "Revisit after the first run" under "No".

**Analysis [Inferred].** If the owner answers no and later reverses 10b by a
plain direction, 038 starts admitting reconstructed advantages with no new
spec version. They are still subject to `:186`'s named-project rule. This is
the owner's own act, so VIS-4 holds. But the packet presents the reversal's
effect as 039 alone.

**Repair.** Add one sentence to Q6: "Reversing 10b later, by itself, would
also let 038 reconstruct advantages (not comparisons with named projects);
039 only adds outside-source comparisons."

### 7. Small accuracy items (note)

- `OWNER-PACKET.md:31-32` says "written into doctrine … and into four
  accepted contracts". The change amends three contract modules (RFC 0001,
  0003, 0005) and seven clauses. The Q0 table lists three contract rows.
  `AMENDMENTS.md:11` says "four accepted contract clauses say that every
  observed repository has its own consent record, and that a repository's
  identity lives in a project declaration". Four fits the consent half
  (RFC1-3, RFC3-7, RFC3-30, RFC5-12), but the sentence also claims the
  identity half, which is RFC1-2, RFC1-4 and RFC3-6. Repair: say "three
  accepted contracts (seven clauses)".
- `IMPACT-LEDGER.md:54-55` and `:87` still describe only "the round 1 raw".
  This change also retains `R-ARBITRARY-PUBLIC-REPO-2-RAW.md` and updated its
  `docs/README.md` row. Repair: say "the round 1 and round 2 raws".

## Acceptance criteria

1. **Round-2 findings: met except N4 (partly).** B1, B2, B3, N5, N6, N7, N8
   and N9 are resolved, with notes 3–5 refining B2 and B3. N4 is partly met
   (note 1). No round-1 resolution regressed.
2. **No offline guarantee claimed: met.** Provenance is never claimed. Both
   residuals are stated in the spec (`:19`), the design (`:92-100`), A1, A3,
   A4 and the packet (`:87`). Note 4 is a different overclaim, about path
   classes, not provenance.
3. **Vendored class: met, with notes.** It is concrete and the REQ-032
   quotes are exact. The root README and REQ-032 authored documentation
   outside the class stay maintainer-stated. The "withdraws no … except
   third-party" sentence overclaims (note 4), and (iii)'s semantics need
   pinning (note 5).
4. **Identity screen: partly met.** The trailers, case handling,
   leading-whitespace handling and the withheld lines are precise. The
   e-mail pattern is not published (note 3).
5. **Clean strikes: Q6 met; Q2 partly met** (note 1).
6. **A1b, A5, RFC3-7: met.**
7. **Counts: met.** 3 requirements; 21 + 10 + 4 = 35 scenarios, or 31
   without 039. Ledger sweeps A–F were re-derived exactly.
8. **Owner packet: met, with notes 1, 4, 6 and 7.** It is readable, gives a
   recommendation on every question and decides nothing.

Every remaining finding is a note.
