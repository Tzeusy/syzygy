# Owner decision packet — three acts for a test-only self-observation

> **Candidate — binds nothing.** Prepared by an agent under the owner's
> 2026-09-21 ruling on P-74 question 3, in
> `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`.
> That ruling authorizes drafting and nothing more. Effect would come only
> from three separate owner acts, each dated and each over its own exact
> bytes. Silence, a commit, a review, a merged pull request or a passing
> check performs no act. No act record is written here.

## What this package is, in one paragraph

M8 slice 6 wants to run the project-shape pipeline against this repository
itself, inside one test, to show the pipeline works on a project other than
Butlers. Today nothing permits that. Your P-74 answer to question 3 chose
"three acts scoped to a test-only self-observation (consent record, second
registry entry, secret-policy extension) before slice 6 runs". The
record's own reading of that row adds that each act is separate and dated.
This directory drafts those three:

1. **A consent record** for Syzygy observing its own repository, test-only.
2. **A second registry entry** declaring the observer for that pair. It
   serves nothing, caches nothing and logs nothing.
3. **An extension to the secret-classification policy** that adds a
   screening scope for that pair.

`SEMANTIC-DELTA.md` says what each act changes. `IMPACT-LEDGER.md` says
what depends on each, with the sweeps that found them. `REVIEW-BRIEF.md`
says what an independent reviewer should be given. Rounds 1 and 2 of
review returned REVISE; this is the round-2 repair, not yet reviewed. The
"Review record" at the end says what changed for each finding.

## What each act would allow, in plain words

With all three acts, one test may read at most six of this repository's
own committed files, at one fixed revision: the doctrine index
`.syzygy/governance/doctrine/README.md` and the five doctrine files it
links to. Those reads are screened by the same secret rules as Butlers,
and the test builds the page in memory to check it. Nothing is served,
cached, logged or saved. The test's own checks compare only digests,
counts, identities and reasons, so a failing test prints no observed text.
Any one act without the other two allows nothing, because a read needs all
three to be valid.

The consent names the exact observer and policy versions it covers. A later
version of either needs a new consent act, so a later registry entry or
policy can never widen what was consented.

None of the three acts authorizes code. Open question 4 asks whether writing
the test needs a separate owner direction.

## The three acts

### Act 1 — consent

- **Act type:** `consent-observation`, in the shape of the 2026-09-02
  Butlers consent act.
- **Subject:** the drafted record under `proposed/`. At adoption, its bytes
  are copied unchanged beside the Butlers consent record in
  `.syzygy/governance/decisions/`. The file name ends
  `SYZYGY-SELF-PROJECT-SHAPE-OBSERVATION-CONSENT.md`.
- **Phrase and argument:**

```text
CONSENT TO SYZYGY SELF PROJECT-SHAPE OBSERVATION: 2901eccbc92cfcec8aaae0ec5817dd70a74d333bb3af321c81e094fc47c022e4
```

The phrase is new. The Butlers phrase names Butlers, and reusing it would
make one label name two subjects.

### Act 2 — second registry entry

- **Act type:** `adopt-registry-entry`.
- **Subject:** the drafted entry under `proposed/`. At adoption, its bytes
  are copied unchanged beside the Butlers entry in
  `.syzygy/governance/declarations/adapter-registry/`. The file name ends
  `POLARIS-SYZYGY-SELF-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`.
- **Phrase and argument:**

```text
ADOPT POLARIS SYZYGY SELF PROJECT-SHAPE OBSERVER REGISTRY ENTRY: 6b3d0b9992cc4c1e6217013a62c3fc6d32e3077559895553f5234e287c423fce
```

This argument goes stale whenever the PWB specification changes, because
the entry pins the specification's digest (see "Landing order").

### Act 3 — policy extension

- **Act type:** `approve-policy`. This is a superseding act over the same
  policy file that the 2026-09-05 policy amendment act bound.
- **Phrase:** unchanged — `APPROVE POLARIS BUTLERS SECRET-CLASSIFICATION
  POLICY`, followed by the SHA-256 of the policy after the patch.
- **The argument is deliberately not offered here.** The bytes it would hash
  exist only when the patch under `proposed/` is applied to the policy's
  current bytes. The policy's current bytes stay unchanged, so the act in
  force stays unbroken. Writing that digest next to the phrase in Markdown
  would put a third digest in the tree: neither the file's current hash nor
  any performed act's argument. The digest is kept in
  `SELF-OBSERVATION-POLICY-EXTENSION-MANIFEST.txt`, where
  `scripts/build_pwb_self_observation_acts.py --check` re-derives it. Read it
  there. At the act, the recorder checks the phrase against the bytes
  present then.

## Why two acts are registered in `check_governance.py` and one is not

- **Acts 1 and 2 are registered now.**
  - Their phrases are new, and their subjects are the drafted files, which
    exist in this directory.
  - The governance check therefore compares each digest quoted above with
    the drafted file's real hash. It fails if either drifts.
  - Both registrations switch on only while the drafted file exists.
  - At adoption, each subject path moves to its installed path.
- **Act 3 is not registered, for the same three reasons the `.18` registry
  packet gives:**
  1. Its label is already registered, with this subject.
  2. A new amendment row needs the new act record's path and the digest
     actually used at the act. Neither exists before the act.
  3. Registering the manifest would compare the post-patch digest with the
     file's current hash. That comparison must fail while this is a
     candidate.

  The change that performs act 3 must therefore register this package's
  policy manifest in `check_governance.py`, write act 3's record and add
  its amendment row, all in the same commit (see "Nothing in this package
  forces another package to regenerate").

## Landing order and which manifests move

The only landing order the owner has set is `.21 → .30 → .22 → lane B`
(`POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md` §6). That
ruling does not place `.20`, `.18`, `dov.24`, `dov.29` or N8, and nothing
here assumes a place for them.

| This package's manifest | Changes when | Why |
|---|---|---|
| consent | only if the consent text changes | [Observed] it depends on nothing else in the tree |
| registry entry | after **every** act that changes the PWB specification: `.21`, `.30`, `.22`, lane B, `.20`, and `dov.29` | [Observed] the entry pins the specification's digest; the builder fails until it is regenerated |
| registry entry | after `dov.24`'s act | [Inferred] `dov.24` adds source-grammar fields to the Butlers entry, and the self entry should carry the same field set |
| registry entry | after N8's profile vocabulary lands | [Inferred] N8 lets a profile declare container shapes; the self entry would then declare this repository's |
| policy extension | only if the policy file changes | [Observed] no other candidate package's `proposed/` patch touches the policy (swept by the builder on every `--check`) |

`.18` changes only the Butlers entry. It shares no bytes with this package,
so its act moves no manifest here [Observed]. Its sub-question on whether
the self entry should also carry a briefing ceiling is open question 7.

**Proposed order (the owner's to set):**

- Act 1, any time.
- Act 3, together with the code change that moves the policy version and
  the policy act's identity (see "What happens to Butlers").
- Act 2, last: after `dov.24` and after the last PWB specification act the
  owner wants in force before slice 6. Regenerate its manifest with
  `--write` just before performing it, and update the digest quoted above.

The tooling allows any order. `--check` passes before, between and after
the three adoptions, and `--apply` refuses only an act that is already
applied. The self-test runs all six orders.

**Nothing in this package forces another package to regenerate.**
[Observed] No other candidate hashes the two new files. Act 3 moves the
policy's bytes, which has two consequences:

- `scripts/build_pwb_truth_policy_amendment.py --check` goes red at
  adoption. That builder hashes the policy's current bytes. On 2026-09-23,
  asked about that builder in the `.18` package, you answered "Retire it in
  the adoption change (Recommended)"
  (`POLARIS-GATE-PACKAGE-OPEN-QUESTIONS-2026-09-23-DECISION.md` §2,
  question 4). If `.18` lands first and retires it, nothing more is needed
  here. If act 3 lands first, the proposal is that act 3's adoption change
  retires it the same way. That answer was given for `.18`, so this is a
  proposal for you to confirm, not a ruling [Inferred].
- `scripts/check_governance.py` also goes red at adoption [Observed in a
  scratch clone, round-2 review]: CG-7e reports 5 findings. This package's
  policy manifest is in neither act-copy registry, and the truth-policy
  packet, its manifest, `ACCEPTANCE-ACT-RECORD.md` and the 2026-09-05
  policy amendment act record no longer contain the policy's current
  argument. The adoption change clears these by registering the manifest
  and recording act 3, as above.

## What happens to Butlers when act 3 is applied

Act 3 changes the policy file Butlers reads depend on, and it supersedes
the policy act the code names. `IMPACT-LEDGER.md` sweep 2 lists every site.
In short:

- [Observed] 10 lines in 4 files hard-code the policy version
  `1.1.0-candidate.1`: two in `apps/three-surface-poc/src/governance-inputs.ts`
  (the version and the policy's scope anchors), one in
  `packages/three-surface-poc-core/src/git-object-reader.ts`
  (`PWB_POLICY_IDENTITY`, which `content-classification.ts` reuses), five in
  `content-classification.test.ts` and two in `project-shape-model.test.ts`.
- [Observed] The same code also names the policy act in force: its act
  identity, recording tag and act-record path, and the earlier act it
  superseded. After act 3 all of these name the new act.

[Inferred] If the policy file moves before the code does, the Butlers
body-read authority fails closed and the Butlers page reads Unknown until
the code catches up. The tests that compare the code with the policy file
would also fail. This fails safe, but it is visible. That is why act 3
should land in the same change that moves all of those sites together.

## Open questions for the owner

Every value below is drafted as a **proposal**. None is decided. Changing
any of them changes an argument, so each belongs before the act, not after
it.

1. **Who writes the consent's words?** The Butlers consent record quotes a
   statement the owner actually made. No such statement exists for this
   pair, and an agent may not write one. The draft says instead: "If the
   owner performs the act over this record's exact digest, the act itself is
   the grant." *Proposal:* accept that. *Alternative:* the owner supplies a
   sentence to quote. That changes act 1's argument.
2. **Extend the one policy — already ruled, stated here for its
   consequence.** The option you chose on P-74 question 3 read "an
   extension of the existing secret-classification policy to the observing
   project's own tree". So act 3 patches the one policy file, and the
   Butlers window described above follows from that choice. Nothing to
   decide here unless you want to reopen the ruling.
3. **Which file starts the self-observation?** *Proposal:*
   `.syzygy/governance/doctrine/README.md`. This repository has no catalog,
   no root summary and no precedence table in the grammar the observer
   reads, so the draft declares none. Every claim that depends on one reads
   Unknown. *Alternative:* the owner authors such a table for this
   repository. That is an intent change, outside this package.
4. **Does slice 6's code need its own permission?** Line 73 of the PWB
   implementation act says "No second repository". The P-74 row's
   reading says "Slices 1, 3, 4, 6 (design) and 7 under the PWB
   implementation act as continued 2026-09-05".
   The three acts do not amend that act, and its "No second repository"
   line governs *running* the test, not only writing it. Whether the three
   acts, together with that row, are enough to write and run the test is
   unclear [Unknown]. *Proposal:* a plain owner continuation direction
   naming slice 6, and saying the test may run. It binds no digest and needs
   no packet.
5. **Provenance state.** *Proposal:* state (1), owner-adopted bootstrap,
   uncorrelated, with the A1 audit record recorded as absent. This is the
   same as all three Butlers acts. It stays visible as uncorrelated and is
   never "independently verified".
6. **Should the self entry pin the PWB specification's digest?** The
   Butlers entry does, so the draft does too. The cost is that act 2's
   argument moves with every specification act. *Proposal:* pin it, and
   perform act 2 last.
7. **Should the self entry copy `.18`'s currency bounds and briefing
   ceiling, and `dov.24`'s grammar fields?** *Proposal:*
   - Copy `dov.24`'s fields once its act lands.
   - Do not copy the briefing ceiling, because nothing is served.
   - Leave the currency bounds for the owner. With no bound, currency reads
     Unknown, which is safe.
8. **Should act 3 also refresh the policy's own pinned specification
   digest?** The policy pins the PWB specification's digest too, so every
   specification act leaves it stale. No package is assigned to refresh it.
   *Proposal:* no. Keep act 3 to the one scope it was ruled for. The
   refresh gets its own act. *Cost:* the consent pins policy version
   `1.2.0-candidate.1`, so any later policy act that bumps the version,
   this refresh included, leaves the self consent not covering the new
   version. Slice 6 cannot run again until a new consent act, even when
   the bump was for a Butlers-only reason [Inferred].
9. **Names and versions.** *Proposal:*
   - record ID `PWB-SELF-CONSENT-2026-09-26`;
   - observer `polaris-syzygy-self-project-shape`, version
     `1.0.0-candidate.1`;
   - policy version `1.2.0-candidate.1`;
   - discovery version `pwb-self-discovery-v1-candidate.1`.

   The record ID embeds the date the record was drafted, not the date of any
   statement or act. If you would rather it carry the act date, it changes
   at the act, and so does act 1's argument.
10. **Which rule decides whether the self pair may be read?** No approved
    requirement names this pair. PWB-REQ-005 says "The consent subject SHALL
    be exactly `(observing Syzygy project, configured Butlers
    repository)`", and the M8 portability funnel says "No approved
    requirement names a self-observation". The ruling forbids editing
    PWB-REQ-005. A sibling answer bears on this: your P-76 answer to
    question 2 was "an observing project reading its own tree, recorded
    here, needs no consent record, registry entry or act". That covers M7
    slice 3, which reads Syzygy's own governed corpus, the same doctrine
    files slice 6 would read. P-74 question 3 is the answer specific to
    slice 6, so the two do not conflict [Inferred], but they place different
    gates on reading the same files. *Proposal:* slice 6 applies
    PWB-REQ-005's gate to the self pair by analogy, and says so in the test.
    *Alternative:* the test runs with no specified gate beyond the three
    acts. *Alternative:* a separate specification change names the self pair
    first.
11. **Which checkouts count as `repository:syzygy`?** The consent resolves
    the locator from whatever checkout runs the test. That could be a fork,
    a pull-request branch in hosted CI, or an old worktree. *Proposal:* any
    checkout of this repository whose fixture revision is a commit on
    `main`, including hosted CI runs of this repository's own workflows,
    and no fork. *Alternative:* the consent pins the fixture's revision,
    which changes act 1's argument whenever the fixture moves.

## What is not in this package

- No act record, recorder script or acceptance-record row. Those land with
  each act.
- No code. The authority lookup N8 slice 4 added is keyed by observing
  project, and both pairs share `project:syzygy` [Observed]. Slice 6's
  implementation has to key it by the pair instead [Inferred]. The drafted
  policy scope and registry entry both say authority for this pair "is
  never inherited from another pair, including through expectations keyed
  only by the observing project".
- No change to the PROJECT-STATUS battery, the hosted workflow or its count
  sentence. Those are registered once, at merge time.

## How to verify this package before acting

All read-only:

```sh
python3 scripts/build_pwb_self_observation_acts.py --check
python3 scripts/build_pwb_self_observation_acts.py --selftest
python3 scripts/build_pwb_self_observation_acts.py --diff
python3 scripts/check_governance.py
```

`--check` re-derives all three manifests. It also checks:

- that the drafted files and the patched policy say what this packet says;
- that the consent's grant paragraph is exactly the closed six-file grant,
  and that the policy scope and registry entry name the same six paths and
  the same versions;
- that the patch still applies to the policy (act 3 pending), or that the
  policy already holds the patched bytes (installed);
- that each install target is free (pending) or holds exactly the drafted
  bytes (installed);
- that no other candidate patches, or drafts a file with the same name as,
  any of the three targets;
- that the two digests above are current.

`--selftest` breaks each check in turn and requires each break to fail. It
also replaces each check `--check` calls with one that always reports a
problem, and requires `--check` to report it. Then it applies the three acts
in all six orders in a scratch copy, and requires `--check` to pass after
each act and a repeated act to be refused. It also requires `--apply` to
install nothing over a package that does not verify. "Installed" means only
that the bytes are in place; only your act makes an act performed. The
count it prints is the number of those cases. `--diff` prints the policy
change in full.


## Review record

Round 1: **REVISE**, over commit `5323721`, retained verbatim at
`docs/reviews/R-DOV25-SELF-OBSERVATION-ACTS-RAW.md`. That commit is
pre-rebase: the branch was rebased onto `main` afterwards, to `6eb406d`, with
no change to this package, and the repair below was made on `6eb406d`. The
branch was then rebased again, onto `66114ac`, before round 2 read it at
`35e497b` (parent `2f11704`); `6eb406d` is on no remote ref. Every
repair changes bytes the review read, so the round-1 verdict covers none of
the current bytes (verification rule 10). Both new-file digests above
changed. No confirmation review has been run.

| Finding | Severity | Disposition |
|---|---|---|
| F1 — `--apply` of the first act blocks the other two; `IMPACT-LEDGER.md` "not changed" claim was unrun | revise | **Repaired.** Every check now takes the tree root. An install target holding exactly the drafted bytes is *adopted*; only different bytes fail. The policy is *pending* if the patch applies forward and *adopted* if it reverses cleanly. `--apply` refuses only an already-adopted act. `--selftest` applies the three acts in all six orders in a scratch copy and requires `--check` to pass after each. The ledger claim is now [Observed] from a run: after the three applies in a full worktree copy, `git status --porcelain` listed exactly the three target paths. |
| F2 — package claimed PWB-REQ-005 governs the self pair; inherited "signed PWB grammar" steps had no self reading | revise | **Repaired.** `SEMANTIC-DELTA.md` now says no approved requirement names the self pair, quoting PWB-REQ-005 and the funnel, and that slice 6 would apply the gate by analogy [Inferred]. `inheritedRules` now says how the signed-grammar rules read under this scope; a builder predicate requires that sentence. New open question 10 asks the owner which rule decides admission. |
| F3 — consented population not closed; consent scope floated with later versions | revise | **Repaired.** The consent names the closed population (the doctrine index and at most the five files it links to, nothing else even if linked), pins observer `1.0.0-candidate.1` and policy `1.2.0-candidate.1`, and says a later version of either needs a new consent act. The policy scope gains `phaseBPaths`; the registry entry gains `sourcePopulation`. The builder requires all three to name the same six paths and the consent to carry both pins. |
| F4 — "never logged, written to disk" not met by default test output | revise | **Repaired.** The consent, the registry entry's `surfaceExposure.rule` and the policy's `ingestBoundaryRule` each say assertions compare only digests, counts, identities and closed reasons, and no assertion message, snapshot, reporter output or test log carries an observed body or rendered text. The consent's exclusions name test-runner output, snapshots and CI logs. A builder predicate requires the sentence in all three. |
| F5 — locator unbound; no owner question | note | **Routed to the owner** as open question 11, with a proposal. |
| F6 — Q2 reopened a ruled choice; Q4 imprecise; Q9 record-ID date; two gates missing | note | **Repaired.** Q2 is restated as a consequence of the ruling, quoting the chosen option. Q4 says the act's "No second repository" line governs running the test and the three acts do not amend it. Q9 notes the record ID carries the drafting date. Questions 10 and 11 added. |
| F7 — sweep 2 missed a line; Butlers authority chain beyond the version not named | note | **Repaired.** Sweep 2 is re-run by fixed string at `6eb406d` over the 348 tracked files under `apps/`, `packages/` and `scripts/`: 21 lines, classified in a table as 10 policy-version lines in 4 files, 6 observer-version lines and 5 script lines. It now lists the act identity, recording tag, act-record paths, supersession target and act instant the policy object names. "What happens to Butlers" above says the same. |
| F8 — several `check()` predicates had no mutant; no call-site mutants | note | **Repaired.** Added mutants for database and network access, log, stored evaluation, walkthrough record, non-object resource limits, an empty seed list, all five scope sentences, and two Status lines, plus mutants for every new predicate. Each of the eight finders `check()` calls is replaced in turn with one returning a sentinel, and `check()` must surface it. The count went from 44 to 118; 36 of those are the adoption-order steps. |
| F9 — registry reused Butlers discovery and implementation identities | note | **Repaired.** The self entry has its own `discoveryVersion`, `pwb-self-discovery-v1-candidate.1`, and names no `implementationId` or `implementationVersion` until slice 6 does; its `implementation` sentence says so. The builder fails on a shared discovery version or a named implementation. |
| F10 — `selfReferenceRule` left the file/copy distinction and part of the population implicit; no registry counterpart | note | **Repaired.** The rule now reads as the review suggested: no object read as an observed Git blob, naming manifests, packets and the acceptance-act record, is an authority input, and authority for this pair is never inherited from another pair, including through expectations keyed only by the observing project. The registry entry carries the same rule. A builder predicate requires it in both. |
| F11 — composition sweep saw only patches | note | **Repaired.** It now reads every file under every other package's `proposed/`, and fails on a patch targeting any of the three files or any file sharing a target's name. A selftest mutant drafts a whole registry file in a sibling. At `6eb406d` the other packages hold 21 `proposed/` files in 7 packages, all patches, none colliding. |

Round 2: **REVISE**, over commit `35e497b`, retained verbatim at
`docs/reviews/R-DOV25-SELF-OBSERVATION-ACTS-2-RAW.md`. The round-2 repair
below was made after rebasing onto `08d4d02`. It changes the consent
draft, so act 1's argument above changed again; the registry and policy
arguments did not. The round-2 verdict covers none of the current bytes
(verification rule 10). No confirmation review has been run.

| Finding | Severity | Disposition |
|---|---|---|
| N1 — "retires or rebases" presented as the owner's ruling | revise | **Repaired.** The packet and the ledger now quote the owner's answer cell, "Retire it in the adoption change (Recommended)", and say it was given for `.18`. The rebase branch is gone. Applying the same handling to act 3's adoption change is marked a proposal [Inferred]. A sweep of the whole package for owner-attributed sentences found four more that quoted the P-74 row's "What it means" column as the owner's words: the packet's opening paragraph, two sentences of `SEMANTIC-DELTA.md`, and the consent draft ("separate, dated"). Each now quotes the answer cell, or names the column as the record's reading. |
| N2 — `--check` did not enforce a closed consent population | revise | **Repaired in the builder.** `consent_findings` now requires the consent's grant paragraph, from "## Scope" to the version pins, to equal one exact closed-grant text, whitespace-normalized. The reviewer's four widening mutants (another path, "closed … at most six" dropped, links followed, the working tree added) are selftest cases, and each fails. The packet's `--check` list now says what is checked. |
| N3 — `6eb406d` unreachable; sweep 2 reads 22 at the head | note | **Repaired.** The review record above names both rebases. The ledger keeps the `6eb406d` table, adds the 22-line re-run at the round-2 head with the builder's third line named, and states which tree the 1,552 figure counted. |
| N4 — sweep 3 and 4 denominators were one level deep | note | **Repaired.** Both now give the recursive counts (22 patches in 8 packages; 21 sibling files in 7) and name the nested RFC-0007 patch. The 20→21 change is explained by the glob, not by growth. |
| N5 — four selftest survivors (M1, M2, M6, M8) | note | **Repaired.** New cases: a nested sibling patch (kills M1); `--apply` over a package with a corrupted manifest must install nothing (kills M2); the policy checked against a tree with no doctrine README (isolates and kills M6). The "names no phase-A seed" predicate was redundant with population equality and is removed (M8); the empty-list mutant stays and is killed by equality. Each of the three mutants and a mutant disabling the grant check was run against a copy of the builder and failed `--selftest`. Count 118 → 125. |
| N6 — `check_governance.py` goes red at `--apply policy` | note | **Repaired.** The packet names the CG-7e state and says act 3's adoption change registers the policy manifest and records the act in the same commit. |
| N7 — P-76 Q2 not mentioned | note | **Repaired.** Open question 10 quotes the P-76 question 2 answer cell and says how it sits beside P-74 question 3 [Inferred]. |
| N8 — cost of the consent's policy-version pin | note | **Repaired.** Open question 8 states it. |
| N9 — Q4 quote not byte-exact | note | **Repaired.** The quote is now exact, capital included, runs to the end of the sentence, and says it is the row's reading. |
| N10 — builder state word "adopted" | note | **Repaired.** The builder's states are now `pending` and `installed`; the packet says only the owner's act makes an act performed. |
