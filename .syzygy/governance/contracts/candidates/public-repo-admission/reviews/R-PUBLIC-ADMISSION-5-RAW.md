# R-PUBLIC-ADMISSION-5 — public-repository admission package
Reviewed commit: a445e25307db2fa2026540834f6a1ae5ccae2918
Manifest SHA-256: ccb422ca85708a9649b19c5688488a7cbcd9e6408f862f2c687d6c794b0f120a
Verdict: REVISE

Reviewer: fresh-context subagent, 2026-10-03. Worktree detached at the
reviewed commit (`git log -1` printed it before anything else was read); used
read-only, then removed.

Scope read: every file under
`.syzygy/governance/contracts/candidates/public-repo-admission/` except
`reviews/` (packet, brief, manifest, three templates, three instance
directories each with `params.json` and one record),
`scripts/build_public_repo_admission.py`, and
`.syzygy/governance/decisions/PUBLIC-REPO-ADMISSION-OWNER-ANSWERS-2026-10-03.md`.
R1–R4 raws read for their findings only. Governing references read: SEC-2,
SEC-3 (`doctrine/security.md`:42, :61); RFC5-12 to RFC5-16
(`rfcs/RFC-0005/consent-egress-secrets.md`:95–260); RFC3-16 (head of the
clause, :112) and the state-(1) label (:221); RFC3-30 quote (:528);
RFC4-1 (`general-contract.md`:74) and RFC-0004 "honored **only under
RFC3-16(a)**" (:39); REQ-polaris-generation-025 (spec :1400); the re-pin act's
Ceremony section; the Scope A direction; `TARGETS.md` lines 37–39 and 60–64.
To test criterion 1 (R4 finding 3) I also read the generator source the
egress record names: `packages/polaris-generation-core/src/prompts.ts`,
`provider-draft.ts` and `pipeline.ts`. No hosting service contacted; no
target repository body read.

## Verified [Observed]

- `python3 scripts/build_public_repo_admission.py --check`: "public-repo
  admission instances: current", rc 0. `--selftest`: "selftest: 7 of 7
  mutants caught (banner kept, unfilled field, placeholder in value, missing
  banner, stale instance, orphan record, stale manifest)", rc 0. `--digests`
  rc 0, three rows. `--manifest-digest`:
  `ccb422ca85708a9649b19c5688488a7cbcd9e6408f862f2c687d6c794b0f120a`, rc 0,
  equal to `sha256sum PUBLIC-REPO-ADMISSION-MANIFEST.txt`. `--bogus`: "unknown
  mode --bogus", rc 2.
- Each of the three manifest rows equals `sha256sum` of its record, and equals
  the `--digests` line for it. Row population: 3 rows; `find instances -name
  '*.md'` returns 3 files, the same three paths. Header "3 records" is right.
- 64-hex sweep over the 13 package files outside `reviews/` plus the
  direction: Python `(?<![0-9a-fA-F])[0-9a-fA-F]{64}(?![0-9a-fA-F])` finds 3,
  all in the manifest `.txt`; 0 in every `.md`. `grep -rnoE
  '\b[0-9a-f]{64}\b' --include=*.md` agrees (0).
- Redis pins (text compare): `8.10.2` `498ecd0d…` = `TARGETS.md`:38;
  `7.2.4` `d2c8a4b9…`, `7.4.0` `c9d29f6a…`, `8.0.0` `e91a340e…` =
  `TARGETS.md`:62–64. requests `v2.34.2` `6e83187b…` = `TARGETS.md`:37.
  All five 40-hex strings match character for character.
- Egress scope lists exactly `(project:syzygy, repository:psf-requests)` and
  `(project:syzygy, repository:redis-redis)`; the two observation subjects are
  exactly those pairs. No third pair.
- RFC5-12's required fields (class, subject, scope, granting principal, grant
  instant, revocation state) are present in all three records.
- Packet quotes of RFC3-30, RFC4-1, RFC-0004 and REQ-025 match their clauses.
- No file labels the package or a record accepted, adopted, approved or
  signed off. Every hit for those words is a reference to some other artifact,
  the state-(1) label `owner-adopted (bootstrap, uncorrelated)`, or a negation.
  Every Markdown banner says the file binds nothing; the manifest header says
  the same. No sentence says a requests or Redis body was read; packet line 8
  says none was.
- README/LICENSE/`project-documentation` sweep: no record or packet sentence
  promises their egress. Outline item 5 (`PUBLIC-SOURCE-POLICY-SCOPE-TEMPLATE.md`:62–63)
  sends them to "indeterminate, refused egress". Packet 93–95 defers the class
  to a later version. Q7 (195–198) states the cost: T2's licence-history proof
  cannot run until (a) is in force.

## Criterion results

1. **R4 repairs.**
   - F1 (blocking, transcript elsewhere): repaired. The egress record (:31)
     says the runtime's state and transcript "are written only inside a run
     directory … from the start of the run. A run whose runtime cannot be
     configured to keep its state and transcript inside that directory does
     not start."
   - F2 (garbled Q3): repaired (packet :126–128).
   - F3 (prompt text has no class): not repaired; see Finding 1.
   - F4 (runtime context, telemetry): repaired (:62–72).
   - F5 (which terms): partly repaired; see Finding 2.
   - F6: no change was asked for.
   - R1–R3 blocking findings (R1 F1–F4, R2 F1–F2, R3 F1): I checked each
     against the current bytes. None regressed with the egress move.
2. **Owner answers.** Q1 (title, :19), Q2 (five classes, no `work-history`),
   Q3 (:31), Q4 (subjects) and Q5 (state (1) on each record) are followed. Q7:
   the class is absent. Q6 has no carrier in any record; see Finding 5.
   Direction item 2's tools-off condition is at :62–64.
3. **Scope equals admitted observations:** yes. The record is consistent with
   REQ-025: it requires an in-force observation consent but grants no read,
   and each observation record (:61 / :58) excludes egress.
4. **Redis revisions equal the pins:** yes, by text. The fetch-alone scope
   holds for four revisions: each `git fetch --depth=1 <upstream> <commit>`
   transfers one commit with no ancestors, and listing a revision admits it
   even if it is an ancestor of another listed one. See Finding 4 on "commit
   object id".
5. **Q7 position:** coherent (above).
6. **Manifest:** rows and population verified (above). Two kinds of claim no
   mutant covers; see Finding 3.
7. **Signing path:** the Scope A direction (:30–34) names "the PWB
   specification deltas, the observer registry entry and the contract
   successors queued behind them"; consents are not named. The packet says so
   and labels its conclusion [Inferred] (:169–172), which is right. Its
   account of the re-pin Ceremony matches act lines 30–57 (no digest in the
   packet; option names the acts "at the manifest rows"; the recorder refuses
   another argument; state (1)).
8. **Authority claims:** none found (above).
9. **Packet self-accuracy:** two inaccuracies; see Findings 2 and 6.

## Findings

**Finding 1 — the generator's instruction text is admitted under a path that omits the response schemas, and no classification policy classifies it** (blocking)

`instances/egress-anthropic/EGRESS-CONSENT-ANTHROPIC.md:46–51` (template
:42–47): "together with the generator's own instruction text — its stage
prompts and response schemas, authored in Syzygy's repository at
`packages/polaris-generation-core/src/prompts.ts` and classified
`code-content` of `project:syzygy` — which every request carries. Every other
source of `project:syzygy` content is outside this consent, including … the
rest of Syzygy's own repository … and stays unsent."

[Observed] The response schemas are not authored in `prompts.ts`.
`prompts.ts` exports only `GenerationStage` and `promptForStage` (:1, :29).
The schemas are `stageSchema` in `provider-draft.ts` (:64–70), wired as the
`responseSchema` port (`apps/three-surface-poc/src/polaris-generation/self-corpus.ts:135`,
`pipeline-demo.ts:98`). `pipeline.ts:258` puts them in every request envelope
(`responseSchema: schema.schema`). By the record's own words,
`provider-draft.ts` is "the rest of Syzygy's own repository" and "stays
unsent". So the record forbids content it says every request carries.

The record also conflicts with its own first condition (:55–57): "Only
content screened under `project:syzygy`'s effective public-source screening
scope may be sent." That scope covers admitted public repositories only
(outline item 1). Syzygy's own prompt source is not in one. Outline item 5
classifies target content only.

So the classification of the prompt text rests on the consent record's own
assertion, not on a classification policy.
- **RFC5-15**, part 2: "the content's class is **determinable and within the
  consented set** under a classification policy carrying an effective owner
  act under RFC3-16(a)".
- **REQ-polaris-generation-025** (:1400): "Content classification SHALL use
  RFC5-14's closed vocabulary and the effective declared policy".
- **RFC5-14**: class is "never an attribute the composing step asserts about
  its own output".

Under RFC5-15, every request would fail closed. Alternatively, an
implementation would send text the record says stays unsent. The owner would
be signing either an unusable consent or a self-contradicting one. This is
the third round on the same item: R3 F5 and R4 F3 ("Name those paths, or the
rule that selects them, in the record or in outline item 5").

Repair:
- Name every source of carried instruction text by path (at least
  `prompts.ts` and `provider-draft.ts`'s schemas), or the rule that selects
  it.
- Put the classification of that text in the policy extension (outline item
  5, or a sibling rule), not in the consent.
- Make the first condition admit it, or carve it out explicitly.

**Finding 2 — "the terms of the signed-in account" still names no terms, and the R4 disposition says it does** (note)

`EGRESS-CONSENT-ANTHROPIC.md:31`: "Anthropic's own retention is as the terms
of the signed-in account state, disclosed rather than promised." R4 F5 asked
for the account type, the terms document governing it, and the training-use
setting recorded as a disclosed fact at offering. The record now names the
account ("the owner's existing Claude account", :1, :19). It names no account
type, no terms document and no training-use setting. Retention under a
consumer subscription can depend on that setting [Inferred]. The packet's R4
row 5 (:272) says "The record names the owner's signed-in Claude account and
its terms". That overstates the bytes: the terms are not named.

Governing: brief criterion 9; packet Q3 (the kit's retention field).
Repair: either name the account type and terms document, with the training
setting disclosed at offering, or reword the R4 row 5 disposition to say what
was done.

**Finding 3 — builder claims no selftest mutant covers** (note)

`scripts/build_public_repo_admission.py`:
- (a) The `--check` docstring (:10–11) says it fails when "an instance
  directory holds a record nothing produces". `stale()` (:137) looks only in
  directories that already produce a record (`{p.parent for p in
  produced}`). [Observed, scratch copy of the package, no tracked file
  touched] I added `instances/sentry/OBSERVATION-CONSENT.md` with no
  `params.json`, then again with `{"common": {}}`. In both runs `stale()`
  did not report the `.md`.
- (b) "banner kept" (:79–81) is an assertion on the good render, not a mutant.
  "7 of 7 mutants" is six mutants and one positive check.
- (c) No mutant covers the `--digests` / `--manifest-digest` refusal while
  stale (:160–169), or unknown-mode rc 2. I ran the latter by hand.
- (d) The stale-manifest mutant (`replace("1", "2", 1)`, :121) edits the
  header count, not a digest row. Whole-file comparison catches both, so this
  is coverage wording only.

Governing: AGENTS.md verification rule 6; brief criterion 6.
Repair: report `.md` files under every `instances/*/`. Add mutants for the
two refusals. Count the banner check separately.

**Finding 4 — "full commit object id" for the Redis trio rests on a column headed "Tag target"** (note)

`instances/redis/OBSERVATION-CONSENT.md:21`: "Admitted revisions (each a full
commit object id; a tag name is a label only)". `TARGETS.md`:61 heads the
licence-history column "Tag target". The same file (:44–45) distinguishes an
annotated tag object from its peeled commit for another target. Nothing in
the reviewed bytes says the three licence-history ids are peeled commits.
Whether they are commits or tag objects is [Unknown] to this review, which
compared text only, as the brief requires. If any is an annotated-tag object,
the grant (`git fetch --depth=1 <upstream> <commit>`, "each admitted
revision's commit object") names a non-commit.

Governing: brief criterion 4. Repair: record in `TARGETS.md` or the packet
how each id was established as a commit (e.g. peeled `^{}`), as R4 did for
requests.

**Finding 5 — the Q6 answer has no carrier** (note)

The direction (:34) answers Q6 "Local only, editorial draft". No record
states a serving limit. The egress record's own condition (:73–75) covers
labelling, not where drafts are served. Outline item 4 permits rendering "in
a generated editorial draft and its source routes" without saying local only.
The packet does not say which future record carries Q6 (registry entry,
policy extension or implementation gate).

Governing: brief criterion 2. Repair: name the carrier, or add "local only,
never published" to outline item 4's rendering line.

**Finding 6 — the packet's review section still says the round-3 repair is unreviewed and that no fifth round is dispatched unasked** (note)

`OWNER-DECISION-PACKET.md:214–217`: "after a third REVISE the drafter
repairs, dispatches no further round, and asks the owner. The round-3 repair
below is therefore unreviewed". Round 4 has since reviewed that repair.

:262–264 says "per the owner's choice the drafter reports rather than
dispatching a fifth round unasked". This round 5 exists (brief :1–6), but
the packet does not say who asked for it. Lines 275–278 then describe round 5
as pending.

These are stale sentences. They are not dated at the sentence (AGENTS.md
"Governance prose": mark staleness at the stale sentence). Also, :91–92
calls the egress record "the next version of the single … record", while
the record says it "supersedes no earlier consent". No earlier consent
exists; "next version" means the next candidate draft and should say so.

Governing: brief criterion 9. Repair: date or qualify the two sentences, name
who asked for round 5, and say "candidate draft" at :91.

## Summary

One blocking finding (1). It sits in the bytes of the egress record, an act
argument, and repeats R3 F5 and R4 F3. Five notes. Manifest, digests, pins,
scope population, owner answers Q1–Q5 and Q7, the authority sweep and the
signing-path reasoning all check out.
