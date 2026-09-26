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
Butlers. Today nothing permits that. The P-74 ruling chose to permit it
with three separate owner acts, and said "slice 6 runs only after the three
acts exist, each separate and dated". This directory drafts those three:

1. **A consent record** for Syzygy observing its own repository, test-only.
2. **A second registry entry** declaring the observer for that pair. It
   serves nothing, caches nothing and logs nothing.
3. **An extension to the secret-classification policy** that adds a
   screening scope for that pair.

`SEMANTIC-DELTA.md` says what each act changes. `IMPACT-LEDGER.md` says
what depends on each, with the sweeps that found them. `REVIEW-BRIEF.md`
says what an independent reviewer should be given. Nothing here has been
reviewed.

## What each act would allow, in plain words

With all three acts, one test may read this repository's own committed files
at one fixed revision. Those reads are screened by the same secret rules as
Butlers, and the test builds the page in memory to check it. Nothing is
served, cached, logged or saved. Any one act without the other two allows
nothing, because a read needs all three to be valid.

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
CONSENT TO SYZYGY SELF PROJECT-SHAPE OBSERVATION: e72382b69ff4bff1596b05afb5b3553d3329d743e192b2ce65caf2fa46a729d6
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
ADOPT POLARIS SYZYGY SELF PROJECT-SHAPE OBSERVER REGISTRY ENTRY: 2218911c7b04bd1b5084d3c2a5e8da22735039cd9cb7e4d800b70e276f4fb912
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

## Landing order and which manifests move

The queue this package must fit is `.21 → .30 → .22 → lane B`, then `.20`
and `.18`, with `dov.24` and N8 alongside.

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
- Act 3, together with the code change that updates the policy version.
- Act 2, last: after `dov.24` and after the last PWB specification act the
  owner wants in force before slice 6. Regenerate its manifest with
  `--write` just before performing it, and update the digest quoted above.

**Nothing in this package forces another package to regenerate.**
[Observed] No other candidate hashes the two new files. Act 3 moves the
policy's bytes, which has two consequences:

- `scripts/build_pwb_truth_policy_amendment.py --check` goes red at
  adoption. That builder hashes the policy's current bytes.
- On 2026-09-23 the owner ruled that the change applying `.18` "retires or
  rebases" that check. If `.18` lands first and retires the check, nothing
  more is needed. If it rebases the check, act 3's adoption change must
  rebase the policy row the same way.

## What happens to Butlers when act 3 is applied

[Observed] Two source sites hard-code the policy version
`1.1.0-candidate.1`:

- the expectations in `apps/three-surface-poc/src/governance-inputs.ts`
  (line 72, and the policy's scope anchors);
- `PWB_POLICY_IDENTITY` in
  `packages/three-surface-poc-core/src/git-object-reader.ts` (line 43),
  which `PWB_SECRET_POLICY` in `content-classification.ts` reuses.

Two test files assert the same value:
`content-classification.test.ts` (five places) and
`project-shape-model.test.ts` (two places).

[Inferred] If the policy file moves before those do, the Butlers body-read
authority fails closed and the Butlers page reads Unknown until they catch
up. The tests that compare the hard-coded copy with the policy file would
also fail. This fails safe, but it is visible. That is why act 3 should land in
the same change that updates those sites, and why open question 2 offers a
separate policy file instead.

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
2. **Extend the Butlers policy, or write a second policy file?** The ruling
   says "secret-policy extension", which this package reads as a patch to
   the one policy [Inferred]. The cost is the Butlers window described
   above. A separate file for the self pair would leave Butlers untouched,
   but would need a new phrase and a new subject. *Proposal:* extend (arm
   A), landing with the version-site update.
3. **Which file starts the self-observation?** *Proposal:*
   `.syzygy/governance/doctrine/README.md`. This repository has no catalog,
   no root summary and no precedence table in the grammar the observer
   reads, so the draft declares none. Every claim that depends on one reads
   Unknown. *Alternative:* the owner authors such a table for this
   repository. That is an intent change, outside this package.
4. **Does slice 6's code need its own permission?** Line 73 of the PWB
   implementation act says "No second repository". The P-74 row puts
   "slices 1, 3, 4, 6 (design) and 7 under the PWB implementation act".
   Whether the three acts, together with that row, are enough to write and
   run the test is unclear [Unknown]. *Proposal:* a plain owner continuation
   direction naming slice 6. It binds no digest and needs no packet.
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
   refresh gets its own act.
9. **Names and versions.** *Proposal:*
   - record ID `PWB-SELF-CONSENT-2026-09-26`;
   - observer `polaris-syzygy-self-project-shape`, version
     `1.0.0-candidate.1`;
   - policy version `1.2.0-candidate.1`.

## What is not in this package

- No act record, recorder script or acceptance-record row. Those land with
  each act.
- No code. The authority lookup N8 slice 4 added is keyed by observing
  project, and both pairs share `project:syzygy` [Observed]. Slice 6's
  implementation has to key it by the pair instead [Inferred].
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
- that the patch still applies to the bound policy bytes;
- that the two install targets are still free;
- that no other candidate patches the same files;
- that the two digests above are current.

`--selftest` breaks each check in turn and requires each break to fail. The
count it prints is the number of checks covered. `--diff` prints the policy
change in full.
