# R-ARBITRARY-PUBLIC-REPO-2
Verdict: REVISE
Reviewed commit: 9d8a9b12c9c33636fd65e58ac63f5539aa0b371b
Subject: openspec/changes/polaris-dossier-arbitrary-public-repo/

Reviewer: fresh-context reviewer (Claude Opus 5.5), 2026-10-08. Read-only.
Bytes read with `git archive 9d8a9b12…` of the change directory, the round-1
raw and `openspec/README.md`. Governing texts read at `origin/main`
`3409ef5ae9f7dcbadbb248d4df1c295dc43a5b0b`, the base the change cites. The
branch's merge base with the current `origin/main` is `1de12311`, which is one
commit past `3409ef5a`. That commit adds only
`decisions/ARBITRARY-PUBLIC-REPO-DOSSIER-DIRECTION.md` [Observed:
`git show --stat`], so every cited line is unchanged. No external or target
repository content was fetched. Scratch scripts: `r2_quotes.py`,
`r2_predq.py`, `r2_sweep.py`, `r2_bound.py`, `r2_ledger.py`.

## Confirmations (no finding)

- [Observed] Every "Current meaning" quotation in `AMENDMENTS.md` matches
  the base bytes after whitespace normalisation: 11 of 11 blocks across
  A1–A4. Line ranges were printed and checked: `architecture.md:26-27`,
  `:62-64`; RFC-0001 `:169-176`, `:178-181`, `:188-191`; RFC-0003
  `:249-254`, `:256-264`, `:274-275`, `:519-521`; RFC-0005 `:99-101`,
  `:111-112`.
- [Observed] All 11 quoted predecessor spans in `spec.md` occur verbatim in
  the four installed `polaris-generation` spec files (033's three sentences
  and its falsifier arm, 025, 032, 034 ×2, 002 ×2). `design.md`'s SEC-3
  quotes match `security.md:95-99`. Its S3-review quote matches
  `R-POLARIS-DOSSIER-S3-GATES-2-RAW.md:54`. Its registry quote matches the
  installed JSON `:58`.
- [Observed] Counts were re-derived by script. The spec has 3 requirements:
  037 has 18 scenarios, 038 has 10 and 039 has 4, for 32 in all and 28
  without 039. A second method (line-start count) also gives 32. Ledger
  sweeps A–F were re-run over `git ls-tree -r -z 3409ef5a`: 2,569 paths, 4
  skipped as non-UTF-8, 2,565 searched. Every total and class cell equals
  `IMPACT-LEDGER.md:20-25`. `REQ-polaris-generation-03[789]` returns no file
  at `3409ef5a`, and none at the current `origin/main` `1de12311`.
- [Observed] The digest-citer table (`IMPACT-LEDGER.md:38-45`) and the
  "Collisions" list (`AMENDMENTS.md:67-86`) were re-derived by hashing each
  target and searching all 2,565 decodable files:
  - `architecture.md` is cited only by D7's and D8's `OWNER-DECISION-PACKET.md`
    and `SEMANTIC-DELTA.md` (4 files).
  - RFC-0001 and RFC-0003 are each cited by the same 2 manifests.
  - RFC-0005 is cited by the 6 files listed.
  - The installed registry JSON is cited by the 3 files listed.
  - D9's log row queues "(c), an RFC 0005 amendment" for RFC5-12
    (`DOCTRINE-AMENDMENT-LOG.md:12`), as stated.
  - A sweep of non-raw `.syzygy/` and `openspec/` files for an amendment of
    RFC5-12, RFC1-2/3/4 or RFC3-6/7/30 finds only the D9 package. No other
    collision is missing from the tracked tree. Open PRs on other branches:
    [Unknown].
- [Observed] Nothing is presented as performed or decided. Every file
  carries a candidate banner. `OWNER-PACKET.md:3-5` reads "Nothing here is
  decided, and no act is offered until a fresh-context review confirms these
  bytes". Each of Q0–Q8 carries a recommendation.
- The direction says "the code and its history"; history is off by default.
  [Inferred] This is disclosed honestly and is not a defect.
  - `proposal.md:29-32`: "This draft keeps history off by default and
    offers it as packet Q2, because reading history changes REQ-033's
    one-commit rule; that trade-off is the owner's".
  - `OWNER-PACKET.md:90-92`: "this recommendation departs from that for now,
    and saying yes here restores it".
  - The direction's own words are permissive ("the dossier *may* reconstruct
    it from the code and its history", direction `:40-41`). Recommending the
    narrower default and naming the departure is within VIS-4.
  - Finding 4 covers what "no" leaves behind.

## Round-1 findings

| R1 | Status | Evidence at `9d8a9b12` |
|---|---|---|
| B1 Q0 reading is an amendment | **Resolved** | `spec.md:3`: "REQ-polaris-generation-037 is an amendment in substance of adopted doctrine and of accepted contracts, not a reading of them. It admits no run until a doctrine amendment … and a contract amendment of RFC1-2, RFC1-3, RFC1-4, RFC3-6, RFC3-7, RFC3-30 and RFC5-12 … are in force". `AMENDMENTS.md:10` reads "**Plainly: REQ-polaris-generation-037 is an amendment, not a reading.**" `OWNER-PACKET.md:34-35` reads "The first draft suggested you could simply rule that it did; the review showed that it does not, and that suggestion is withdrawn." The clause table now carries RFC1-2/3/4, RFC3-6/7/30 (`design.md:23-28`). Warrants gain RFC3-6, RFC3-7 (`spec.md:156`). |
| B2 identity laundering | **Partly** | Commit and URL predicates were added (`spec.md:16-17`), with scenarios `:54-82` and a residual (`:20`). The URL is still an unverified label, and the normalisation leaves same-host spellings. Redis outside its four revisions and Butlers at any revision are reachable under a new identity. The packet tells the owner "a withdrawn repository cannot come back under a new name" (`OWNER-PACKET.md:83`). See new finding 1. |
| B3 Redis "untouched" | **Resolved** | `spec.md:3`: "keeps its admission basis, consent, statements, pinned revisions … except that REQ-polaris-generation-038 applies to every operator-agent run; whether it should apply to Redis's runs is an owner question". The falsifier is narrowed to "Redis's admission basis, consent, statements or pinned revisions change" (`:150`). See also `proposal.md:91-96`, `OWNER-PACKET.md:37-41` and Q5 (`:128-135`). |
| B4 history vs REQ-033 | **Resolved**, with residuals | History is off by default (`spec.md:22`). When admitted, `:24` names 033's two sentences and its falsifier arm and gives their reading. It admits commit objects only ("it SHALL NOT read an ancestor's tree or blob") and withholds author, committer and signature lines hash-not-body. The packet calls it a change: "This changes REQ-033's rule" (`OWNER-PACKET.md:95-96`). Residuals: new findings 3 and 4. |
| B5 unmarked motive claims | **Resolved** | `spec.md:173`: "The fidelity verdict … SHALL classify every Inferred block of the draft, marked or not … A block it classifies as one of the four kinds that carries no basis … is a blocking finding whose deficient subject is the marking." The attribution bar now covers "No block, of any kind or basis, marked or unmarked" (`:169`). Scenario "Unmarked motivation" is at `:199-203`; falsifier arm at `:247`. |
| N6 vendored text as maintainer-stated | **Partly** | `spec.md:167` excludes "a path the run's frozen profile classes as vendored or third-party" and labels authorship "Inferred … from its location". No predecessor defines such a path class. See new finding 2. |
| N7 Q1c "Excluded" unchecked | **Partly** | The publication declaration was added (`spec.md:9`, `:30`), and Q1a now says "You declare … that the commit is published there". Q1c still overclaims ("refused automatically"). See new finding 5. |
| N8 governed predicate attribution | **Resolved** | `design.md:119-137` cites `governed.ts:6-8` and S3 raw `:54`, carries the residual list and restates the premise for third-party trees. `spec.md:28` requires the residual to be disclosed. Packet Q3 (`:108-114`) explains it. |
| N9 D9 cost for unknown code | **Resolved** | `spec.md:26` refuses an execution choice unless the standing record permits it. Packet Q1f (`:84`) quotes "and can change any file the owner can"; nothing contains it. |
| N10 installed registry entry | **Resolved** | `design.md:217-224` names the installed copy and the reader (`package-reader.ts:773`). Ledger: `IMPACT-LEDGER.md:45`, `:90`. |
| N11 REQ-039 scope and marking | **Resolved**, minor residual | `spec.md:262`: "Syzygy can detect such a block only from the agent's marking; the fidelity review is the backstop". Scope is `v1-reserved`. See new finding 7. |
| N12 drawer statement unlabelled | **Resolved** | `spec.md:28`: "That statement is the owner's, made in advance for every such repository … its truth for a given repository is Inferred from the exclusions above, and the page SHALL label it so." |

## New findings

### 1. The exclusions can still be bypassed for both repositories that have their own consent, and the packet and amendment texts state the guarantee as absolute (blocking)

**Anchors.**

- `spec.md:16-17`: the exclusion predicates.
- `spec.md:20`: the residual, "for example another commit of a repository
  whose per-repository consent was withdrawn, reached through a mirror URL".
- `OWNER-PACKET.md:83`: "Matched by name, by commit and by URL, so a
  withdrawn repository cannot come back under a new name." / "Some cases
  slip through: a later commit of a withdrawn repository, reached through a
  different mirror."
- `design.md:83-88`.
- `proposal.md:91-93`: "the standing consent never applies to it".
- `IMPACT-LEDGER.md:56-58`: "the standing route never reaches it".
- `AMENDMENTS.md:121-122`: A1, "never covers a repository that has its own
  record".
- `AMENDMENTS.md:341-342`: A3, "A repository with its own observation
  consent record, in any state, is never reached by a standing one".

**Clauses.**

- The Redis act's Effect (`PUBLIC-REPO-ADMISSION-REDIS-OBSERVATION-ACT.md:65`):
  "observation consent … at the four admitted revisions it lists". The
  owner's selection was "Syzygy may read the Git objects of the four
  consented Redis commits and nothing else of Redis" (`:45`).
- RFC5-13: "Consent revocation is prospective".
- VIS-4: owner decisions rest on the packet.

**Analysis, [Observed] from the records.**

- The Redis consent record
  (`contracts/candidates/public-repo-admission/instances/redis/OBSERVATION-CONSENT.md`)
  carries `Upstream: https://github.com/redis/redis` (`:19`) and four
  revisions (`:25-28`).
- The Butlers consent (`decisions/BUTLERS-PROJECT-SHAPE-OBSERVATION-CONSENT.md`)
  has subject `repository:butlers-configured-poc` (`:15`), a filesystem
  locator `/home/tze/GitHub/butlers` (`:17`), and no revision or upstream
  URL.

**Analysis, [Inferred] from the spec text.** Six routes reach a repository
that has its own record:

- **The URL is a label.** Syzygy never compares it with the clone, so the URL
  predicate only catches an operator who declares the true URL.
- **The normalisation leaves same-host spellings unfolded.**
  `https://github.com/Redis/redis` is one example (GitHub paths are
  case-insensitive [Inferred, general knowledge]). `https://www.github.com/redis/redis`
  is another. An `http`/`https` pair differs only by scheme.
- **The commit predicate matches only named revisions and their direct
  children.** Any other Redis commit (a fifth tag, `unstable` HEAD) under any
  identity other than `redis-redis` is therefore admitted under the standing
  route. Redis's act scopes that read out.
- **Butlers has no content anchor.** Its record names neither revisions nor
  an upstream, so a Butlers clone under any new identity and any URL passes
  every content predicate.
  - The governed-tree test may still refuse it, if the pinned tree holds an
    `openspec` or `.syzygy` segment [Inferred].
- **The identity predicate is likely structurally vacuous for legacy
  records.** The standing record "fixes" an identity form, and the design's
  candidate is `repository:<host>-<owner>-<name>` (`design.md:214-216`).
  Neither `redis-redis` nor `butlers-configured-poc` has that form. An
  operator who follows the standing form never matches either. So
  `design.md:87-88`'s "the identity check would still catch `redis-redis` if
  declared" holds only for an operator who chooses the legacy spelling.
- **The population is undefined.** "Any per-repository observation consent
  record" does not say whether it means performed act records only, or also
  instance files, candidates and declined packets.

**What the change says about this.** The spec's generic residual sentence
(`:20`) formally covers these cases. But the packet, which is what the owner
signs from, names only "a later commit of a withdrawn repository, reached
through a different mirror". It opens the same cell with an absolute ("cannot
come back under a new name"). The A1 and A3 texts would write the absolute
into doctrine and contract. The most realistic leak is an in-force,
narrowly-scoped consent (Redis) read at another commit through an ordinary
URL variant. That case is not a withdrawn repository, and not a different
mirror.

**Repair.**

- (a) Make the URL fold fail-closed:
  - compare host and path case-insensitively;
  - strip `www.`;
  - treat `http`, `https`, `ssh://` and scp-form spellings of one host and
    path as equal;
  - over-matching only refuses.
- (b) Say in `spec.md:20`, `design.md` §2 and Q1e that the URL is never
  checked against the clone.
- (c) Give records that carry no content anchor one:
  - require the standing record's exclusion list to carry each existing
    consented repository's URL and identity (Redis, Butlers); or
  - add a tree-level check. Compare the pinned root tree and its top-level
    blob ids against the trees Syzygy has recorded for consented revisions.
- (d) Rewrite Q1e and the design residual to name both cases:
  - the in-force-narrow case: a Redis commit other than its four;
  - the no-anchor case: Butlers at any commit.

  Strike "cannot come back under a new name".
- (e) In A1/A3/A4 or the packet, state that a run reaching a repository with
  its own record is an unconsented read that Syzygy detects only through the
  predicates above, and otherwise rests on the operator's declaration
  (Inferred).
- (f) Define the population of consent records compared.
- (g) Add a scenario: "Consented repository at an unconsented commit under a
  new identity".

### 2. REQ-038 keys maintainer authorship on a "vendored or third-party" path class that no frozen profile defines; read literally, nothing is maintainer-stated (blocking)

**Anchors.**

- `spec.md:167`: "does not lie under a path the run's frozen profile classes
  as vendored or third-party … Text under a vendored or third-party path, and
  text the frozen profile cannot place on either side, is not
  maintainer-stated".
- `spec.md:175`: "this requirement reads exactly this predecessor text: in
  REQ-polaris-generation-034 … in REQ-polaris-generation-035 … and in
  REQ-polaris-generation-002". REQ-032 is not listed.

**Clause** (REQ-032, `polaris-non-governed-narrative-profile/specs/polaris-generation/spec.md:11`,
[Observed]): "A source counts as maintainer-written and not generated only
when it lies under a path class the frozen profile declares as authored
documentation or manifest, and carries none of the generated-file markers the
frozen profile lists … a source the frozen profile cannot place on either
side is not a declaration source". The frozen profile's path classes are
authored documentation and manifest. It has no vendored or third-party class.

**Analysis [Inferred].**

- 038 relies on a profile field that does not exist, and it does not name the
  REQ-032 sentence it would extend.
- "Either side" is borrowed from REQ-032, where the sides are authored and
  not authored. Under that reading, a source comment in `src/` lies in no
  authored-documentation class. It is "unplaced", and so not
  maintainer-stated.
  - This contradicts 038's own scenario "Maintainer text anchors the
    motivation" (`:183`, "a design note or source comment").
- A governed run is composed under REQ-004, not the non-governed profile, and
  may record no frozen profile at all. There, every source is unplaced.
- Ruling 10b keeps advantages maintainer-stated only (`:171`). A literal
  implementation therefore drops every advantage. That includes Redis's if
  Q5 is answered yes, which is a regression the packet does not mention.

**Repair.**

- Add the vendored or third-party path class as a new field of the frozen
  profile. Name and read REQ-032's sentence "The frozen profile, its
  declaration forms and its path and marker rules SHALL be fixed … before
  discovery began" in `:175`.
- Say who fixes the class for governed runs, and for runs with no recorded
  profile.
- Replace "cannot place on either side" with a two-sided definition (inside a
  vendored or third-party class, or outside it).
- Add a scenario for a source comment outside every documentation class.

### 3. With history admitted, commit-message trailers carry the identities the spec and packet say are withheld (blocking)

**Anchors.**

- `spec.md:24`: "Syzygy SHALL withhold the author and committer lines of
  every commit object … Only the message text of an ancestor commit is
  classified, screened and available for citation".
- `spec.md:100`: "no author or committer name or address is stored,
  rendered, quoted or placed in a review packet".
- `OWNER-PACKET.md:96-98`: "Author and committer names and email addresses
  would be withheld and never shown, since showing them is a privacy question
  of its own."

**Clause.** VIS-4 keeps privacy posture human-gated. AGENTS.md lists the
security/privacy/retention posture as an escalation trigger.

**Analysis [Inferred, general knowledge].** Many public projects carry
`Signed-off-by: Name <address>`, `Co-authored-by:`, `Reported-by:` and
similar trailers in the message body. Under `:24` that body is "available
for citation", and SEC-5 secret screening does not treat an e-mail address as
a secret. So the author identities the packet promises are "never shown" can
be quoted and rendered. The falsifier (`:150`) tests only "an author,
committer or signature line".

**Repair.**

- Withhold message trailer lines (`^[A-Za-z-]+-by:` and `Co-authored-by:`)
  and any e-mail address in the message text, hash-not-body.
- Extend the scenario at `:96-100` and the falsifier to cover them.
- Or correct Q2 to say that names in message text remain visible, as part of
  the privacy question.

### 4. Answering Q2 "no" still adopts the REQ-033 reread, and the packet does not say so (note)

**Anchors.**

- `spec.md:24`: the history paragraph sits inside REQ-037, conditioned only
  on "where the standing record admits history".
- `AMENDMENTS.md:425-426`: A4, "only where it says so, that commit's
  ancestor commit objects".
- `IMPACT-LEDGER.md:101-103` and `tasks.md:14-15`: "stay as the disabled
  option or are struck, at the owner's choice".
- `OWNER-PACKET.md:86-98`: Q2 offers no such sub-choice.

**Analysis [Inferred].** If the owner answers "no" and the history text is
kept, the spec still adopts the reread of 033's "at the pinned revision" and
its falsifier arm. A4 still puts history into RFC5-12. A later version of
the standing record, which is a consent act rather than a spec or contract
amendment, would then switch history on.

**Repair.** Add the sub-choice to Q2: strike, or keep dormant. Say that
"strike" also removes A4's history clause. Say that "dormant" means a new
standing-record version alone can enable it.

### 5. Local commits: "refused automatically" overclaims (note)

**Anchors.**

- `spec.md:22`: "A commit made locally on top of a fetched public commit is
  therefore refused."
- `OWNER-PACKET.md:81`: Q1c, "a commit you made on top of it is refused
  automatically".
- `OWNER-PACKET.md:89`: "as the one-commit clone check (open PR #392)
  enforces".

**Analysis.**

- [Inferred] A depth-1 clone of the operator's own local repository yields a
  single commit whose shallow boundary is that commit. It satisfies every
  clone-shape rule. `design.md:103-106` says so correctly ("a shallow commit
  whose parents were never fetched").
- With history admitted, the shape check admits ancestors, so a local commit
  on top is not refused at all.
- [Observed] PR #392 is `OPEN` (`gh pr view 392`), so "enforces" describes
  unmerged code.

**Repair.** Reword `:22` and Q1c to "a clone that still holds the public
parent is refused; a re-shallowed local commit rests on your publication
declaration". Condition the sentence on history not being admitted. Write
"would enforce" for #392.

### 6. The A1 act form omits the exact-bytes binding that REQ-037's RFC3-16 check needs; A5's act type is unnamed (note)

**Anchors.**

- `AMENDMENTS.md:56`: A1's act is "a new row of
  `decisions/DOCTRINE-AMENDMENT-LOG.md` … adopted in the owner's words",
  with D9 as precedent.
- `spec.md:9`: the amendments must be in force "each established from the
  record of the owner act that makes it effective (RFC3-16), never from a
  status word".
- `AMENDMENTS.md:60`: A5 is "A digest-bound consent act".

**Analysis.**

- [Observed] D9's log-row adoption alone was not what REQ-033's gate reads.
  The gate reads a separate act: `DOSSIER-LOCAL-AGENT-D9-IN-FORCE-ACT.md`,
  act type `bind-exact-bytes`, which binds "the exact whole-file bytes of
  `security.md` and `v1.md`".
- [Inferred] A1 as drafted gives REQ-037 no digest-bound record to check, so
  either an A1b in-force act is missing from the table, Q0 and Q8, or the
  spec must say how a log row satisfies RFC3-16.
- The Redis precedent's act type is `consent-observation`, but A5 does not
  name it.

**Repair.** Add the in-force binding act (or the alternative) to A1, Q0's
table and Q8's order. Name `consent-observation` for A5.

### 7. REQ-039 striking leaves dangling references, and `v1-reserved` is new to the repo (note)

**Anchors.**

- `spec.md:169`: "or REQ-polaris-generation-039 is in force".
- `spec.md:171`: "unless the owner has reversed that ruling and
  REQ-polaris-generation-039 is in force".
- `tasks.md:12-13`: strikes only 039.
- `spec.md:268`: `Scope: v1-reserved`.

**Analysis.**

- [Observed] All 43 `Scope:` lines in `openspec/` read `v1-mandatory`.
  `v1-reserved` is cited only to an external skill file
  (`design.md:202-203`).
- The meaning "implementation may stub" sits oddly with a requirement that,
  once in force, gates readiness.

**Repair.** Say that striking 039 also strikes the two 038 clauses. Either
state the conditional scope in words, or cite where the repo defines
`v1-reserved`.

### 8. RFC3-7's "referenced — never embedded — from the declaration" is left unaddressed for the standing record (note)

**Anchors.**

- `AMENDMENTS.md:357-358`: "Consent records are governance acts in
  `decisions/`" is listed as unchanged.
- RFC3-7 at `manifests-and-namespace.md:256-258` [Observed]: "**Consent
  records** are governance acts stored in `.syzygy/governance/decisions/`,
  referenced — never embedded — from the declaration."

**Analysis [Inferred].** A3 says a standing-only repository "has no
repository entry", but it never says what references the standing record.
The pre-existing gap means no project declaration is tracked at all
(`AMENDMENTS.md:39-42`).

**Repair.** In A3, either say the standing record is referenced from
`project:syzygy`'s declaration (and disclose that none exists today), or
amend that clause too.

### 9. "Without per-repository acts" is attributed to the direction, which does not say it (note)

**Anchors.**

- `AMENDMENTS.md:144-148`: "which directs a draft for 'any arbitrary git
  repository' without per-repository acts".
- `design.md:60`: "a per-repository act signed quickly (rejected: the owner
  asked for none)".

**Clause** ([Observed], direction `:35-38`): "without a per-repository code
change or review round".

**Analysis [Inferred].** The owner was reacting to a list that included "its
own consent act", so removing acts may be what the owner wants. But that is
the lead's reading, not the recorded direction. Q0's alternative ("make
signing one faster") meets the recorded words literally.

**Repair.** Label the gloss Inferred in A1's warrant and in `design.md:60`.
Note in Q0 that the alternative satisfies direction item 1 as written.

## Acceptance criteria

1. **Round-1 findings: met except B2 (partly), N6 (partly) and N7 (partly).**
   B1, B3, B4, B5 and N8–N12 are resolved.
2. **AMENDMENTS deltas: partly met.** Every quote is exact (11/11), the
   proposed text is complete, and the collisions are accurate with none
   missing in the tracked tree. A1's act form is incomplete and A5's act
   type is unnamed (finding 6). RFC3-7's opening is unaddressed (finding 8).
3. **Exclusion paths: not met.** Same-host URL variants and unanchored
   records bypass them, and the packet misstates the residual (finding 1).
4. **No new defect: not met.**
   - New in the repair: the undefined vendored path class (finding 2) and
     the trailer leak (finding 3).
   - The history-versus-direction tension is honestly disclosed and is not a
     defect. What a Q2 "no" leaves adopted is undisclosed (finding 4).
5. **Owner packet: partly met.**
   - It is readable, recommends on every question and decides nothing.
   - Q1c, Q1e and Q2 overstate (findings 1, 3 and 5).
6. **Counts and ledger: met.** 3 requirements, 32 scenarios and 28 without
   039; sweeps A–F and the citer table were re-derived exactly.
