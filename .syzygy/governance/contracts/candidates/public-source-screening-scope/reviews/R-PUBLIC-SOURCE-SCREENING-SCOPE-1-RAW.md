# R-PUBLIC-SOURCE-SCREENING-SCOPE — fresh-context review of the public-source screening scope package
Reviewed commit: 21fa1bc8224a058e60ad28229f2727dd6b328aab
Manifest SHA-256: 87a56aa65025c5e23fa18ede60432a2c55f982d823632892bebffd45a2b14c50
Verdict: REVISE

Reviewer: fresh-context agent, 2026-10-03. Worktree detached at the reviewed
commit, read-only. Artifact: every file of
`.syzygy/governance/contracts/candidates/public-source-screening-scope/` and
`scripts/build_public_source_screening_scope.py`. Subject: the secret
classification policy JSON at its bytes in the reviewed commit. No external
repository body was read and no model was called. Every digest below was
printed by `sha256sum` or the builder, never transcribed by hand.

## What was run

- `python3 scripts/build_public_source_screening_scope.py --check`:
  `public-source screening scope: current`, exit 0.
- `--selftest`: `selftest: 17 of 17 predicates held`, exit 0.
- `--manifest-digest` and `sha256sum` of the manifest file agree (the head
  above).
- Independent application: the patch applied with `patch` to a scratch copy of
  the policy hashes to the manifest row. Parsed as JSON, the only key added is
  `publicSourceScope`, the only key changed is `policyVersion`
  (`1.1.0-candidate.1` to `1.2.0-candidate.1`), and no key is removed.
  `publicSourceScope` sits directly after `scope`.
- `python3 scripts/check_governance.py` in the worktree: `31 OK, 21 WARN, 0 FAIL
  (52 checks)`.
- Sweep 1, re-run with the stated predicate over `git ls-tree -r -z` at
  `c540438d`: 1975 files, 52 hits, 14 under `apps/`, `packages/` or
  `scripts/`. These are the same 14 files the ledger names. At the reviewed
  commit the figures are 1982, 57 and 15 (the 15th is the new builder). The
  ledger dates its sweep to `c540438d`, so it reproduces.
- Sweep 2, re-run with the stated predicate at both commits: 15 files under
  `apps/` and `packages/`. The count reproduces, but the ledger's
  classification of those files does not (Finding 1).
- PR #120 interaction, simulated on `git archive` copies (reviewed commit;
  `origin/agent/tier4-dov25` at `0a8ef671`). In both orders the second patch
  fails to apply.
  - **#120 first:** with #120's patch applied, this builder's `--check` reports
    `STALE`. `--write` regenerates to `1.2.0-candidate.1` to
    `1.3.0-candidate.1`, and `--check` is then `current`.
  - **This package first:** with this package's patch applied, #120's
    `--check` fails with `patch does not apply`. Finding 3 covers what
    repairing that takes.
- Criterion 8, checked over all 6 package files: no file labels anything
  accepted or approved. The only hits for `approve`/`adopt` are act-type names,
  the proposed provenance-state label and the brief's own criterion. The four
  Markdown files contain 0 standalone 64-hex tokens.

## Criteria

1. **The diff is exactly the stated change: holds.** See What was run.
2. **Contradiction with inherited rules: does not hold.** See Findings 4 and 5.
3. **Loosenings stated and bounded: partly.** Network egress is bounded to two
   routes, storage to the run directory (Q3) and rendering to the local
   editorial draft (Q6), and logging and machine response stay `never`. All
   of these match Q3, Q6 and the egress template. Two problems remain: the
   active-content loosening for non-Markdown files is not stated as a
   loosening (Finding 4), and the classification narrows the owner's Q2/Q7
   answers without saying so (Finding 6).
4. **RFC5-14 soundness: partly.** Classes are assigned by rule, not asserted
   by the composer. `work-history` is never classified, and
   `project-documentation` is absent (the builder enforces both). The
   instruction-text rule is closed and sufficient for RFC5-15 part 2 at these
   bytes (Finding 9). The indeterminate case has two incompatible readings
   (Finding 5).
5. **Extension list labelled [Inferred]: holds.** SEMANTIC-DELTA.md:28 and
   OWNER-DECISION-PACKET.md Q3 label it.
6. **Read-gate consequence: holds in outcome.** The outcome is that the gate
   fails closed. The mechanism and the extent are misstated (Findings 1
   and 2).
7. **Sweeps honest: Sweep 1 holds.** Sweep 2's count holds, but its
   [Observed] reading is false (Finding 1).
8. **Authority: holds.**

## Findings

**Finding 1 — The impact ledger misses runtime and test copies of the policy version** (revise)
IMPACT-LEDGER.md:23-25 states "[Observed] Only `body-read-authority.ts` and
`governance-inputs.ts` check a policy field at run time … the rest read the
keys in tests or fixtures". Consequence 1 (IMPACT-LEDGER.md:31-33) says a
re-point of `governance-inputs.ts` and its act-record path is enough. Seven of
the 15 Sweep-2 files are not tests, and two of them carry the version at run
time:

- `packages/three-surface-poc-core/src/git-object-reader.ts:41-44` hard-codes
  `PWB_POLICY_IDENTITY.policyVersion: '1.1.0-candidate.1'`.
- `content-classification.ts:69` feeds that value into `PWB_SECRET_POLICY`,
  the version every exclusion record names.
- `git-object-reader.test.ts:547` and `content-classification.test.ts:550`
  assert those copies equal the JSON, and
  `content-classification.test.ts:255,286,406,474,488` hold the literal.
- `governance-inputs.ts:81` and `:102` (the act's `scopeAnchors`) also carry
  the version.

After the act, these tests fail and exclusions name a stale version until the
copies are bumped too. The Q2 continuation (OWNER-DECISION-PACKET.md:26-31)
asks the owner to authorize a re-point narrower than the one needed.
Violates: AGENTS.md verification rules 5 and 9; brief criteria 6 and 7.

**Finding 2 — The read-gate refusal is attributed to the version; the digest refuses first** (note)
SEMANTIC-DELTA.md:55-59 and IMPACT-LEDGER.md:31-33 attribute the refusal to
the version pin. In `body-read-authority.ts`, `exact-digest-wrong` (:444)
fires on any byte change before the policy-specific `policy-version-wrong`
check (:641) is reached. The current act record binds the old digest. Q2's
contrast (OWNER-DECISION-PACKET.md:30-31) implies that the alternative of not
bumping the version would only be mislabelled. In fact it would refuse reads
just the same. The cited precedent, the 2026-10-02 re-pin, changed the
policy's bytes without a version bump. The fail-closed outcome the package
states is correct. Violates: brief criterion 6 (accuracy of the stated
mechanism).

**Finding 3 — The PR #120 reconciliation is asymmetric and says it is not** (revise)
SEMANTIC-DELTA.md:48-51 says "Whichever act is performed second is
regenerated … with `--write` … the generator follows the new base version on
its own". OWNER-DECISION-PACKET.md:36-37 (Q4) recommends "whichever is ready
first". That is true only when this package is second.

#120's builder (`scripts/build_pwb_self_observation_acts.py:105-106` at
`0a8ef671`) hard-codes `POLICY_CURRENT_VERSION = "1.1.0-candidate.1"` and
`POLICY_PROPOSED_VERSION = "1.2.0-candidate.1"`. Its consent prose (:205)
names version `1.2.0-candidate.1`.

If this act lands first, #120 needs code edits to its builder and a changed
digest-bound consent record before `--write` can work. If #120 lands first,
this package needs only `--write` (simulated). Today both packages propose the
same label, `1.2.0-candidate.1`, for different bytes. Neither breaks the
other's performed state: each fails its own check closed until it is redone.

There is also an ambiguity once both land: `inheritedRules` ("every other rule
in this policy applies to this scope unchanged", patch :137) does not say
whether the sibling scope's rules are among them. Violates: brief criterion 1
(the stated reconciliation); the owner's Q4 is offered on an inaccurate
symmetry.

**Finding 4 — The non-Markdown active-content loosening conflicts with the inherited classificationSuccess and is not declared as a loosening** (revise)
`inheritedRules` (patch :137) re-reads `classificationOrder` and
`classificationSuccess` with two substitutions only: snapshot membership and
content-classification rules. That leaves the inherited condition "no
active-content form occurs outside a valid inert code context" in force for
every body. `activeContent.otherAdmittedFiles` (patch :113) says markup-like
bytes in non-Markdown files "are not an active-content match". The two
conflict.

Under the base rule, non-Markdown files with no inert context are withheld as
active content. The PR #215 outline (PUBLIC-SOURCE-POLICY-SCOPE-TEMPLATE.md
item 3) calls this "a change the act approves, not a carry-over".
SEMANTIC-DELTA.md:10-12 lists the scope's new authority as three items and
omits this one. SEMANTIC-DELTA.md:31 states the rule without marking it a
loosening.

"Markdown and any other prose that would be rendered as markup" (patch :112)
has no closed rule deciding which files that is (by extension or otherwise).
Violates: brief criteria 2 and 3; RFC5-14 "Classification is determinable".

**Finding 5 — The indeterminate blob has two incompatible readings** (revise)
Patch :93 makes every unclassified admitted blob "indeterminate: refused
egress and shown as such", which reads as admitted, stored and rendered
locally, with egress refused. Under `inheritedRules`' own reading, "the
content-classification rules above replace the PWB closed extraction class".
On that reading a blob with no class has an unknown extraction class, so
`classificationOrder` step 6 and `unclassifiableExclusion` exclude the whole
artifact, recorded hash-not-body and never stored or rendered (RFC5-16
"excluded, not indexed").

The readings decide whether README and LICENSE bodies may sit in the run
directory and appear in the draft. Inherited step 7 ("admit only parsed
project-shape facts") and classificationSuccess's "that extractor completes"
also have no stated reading for `code-content` bodies, which are admitted as
spans with no extractor. Violates: brief criteria 2 and 4; RFC5-14 (fails
closed); RFC5-16.

**Finding 6 — The scope narrows the owner's Q2/Q7 answers without disclosure** (revise)
`PUBLIC-REPO-ADMISSION-OWNER-ANSWERS-2026-10-03.md` (draft PR #215) records
these answers:

- Q2: "All but work-history".
- Q7: "T1 (requests) runs on code and specs only".
- Direction item 1: "The admission drafts follow the eight answers above".

The PR #215 outline (item 5) maps specification and design documents to
`governance-text` and committed reports to `evidence-content`. The scope
leaves `governanceTextPaths` and `evidenceContentPaths` empty (patch :91-92),
and the builder enforces the emptiness (`build_public_source_screening_scope.py:229-230`).
So specifications are indeterminate and refused egress. Narrowing is the safe
direction, but nothing in the delta, ledger or packet says the package departs
from Q2 and Q7 or why, and the packet asks no question about it. Violates:
brief References (owner answers Q2, Q7) and criterion 3; AGENTS.md "Preserve
the owner's trade-offs".

**Finding 7 — The "configuration" claim is overstated** (note)
SEMANTIC-DELTA.md:28 and patch :93 say configuration is indeterminate. The
extension rule (patch :57-84) classifies any configuration written in a
listed extension as `code-content`, for example `*.config.js`, `setup.py` or
`.sh`. Whether "ends with" is case-sensitive is unstated. Violates: brief
criterion 4 (the rule must determine the class the prose claims).

**Finding 8 — `networkEgress: false` beside two permitted routes** (note)
Patch :122-127 keeps `networkEgress: false` and carries the permission in
`networkEgressRoutes` and `routeRule`. SEMANTIC-DELTA.md:32 says egress is
"permitted for exactly two routes". A consumer that reads the boolean alone
fails closed, which is safe, but the representation and the delta's wording
differ. Violates: none; it is a legibility note.

**Finding 9 — The instruction-text rule is closed and sufficient at these bytes** (note)
`promptForStage(stage)` (`packages/polaris-generation-core/src/prompts.ts:29`)
takes no target input and imports nothing. `provider-draft.ts` imports only
`node:util` and a type. The two named symbols therefore produce only
Syzygy-authored text, and RFC5-15 part 2 can determine its class. The rule
binds symbols and code-declared version labels, not a digest. Whatever those
symbols later embed would be classed `code-content` by this rule, subject only
to RFC5-14's carry-forward. Violates: none; recorded for the next policy
version.
