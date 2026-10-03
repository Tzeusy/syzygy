# R-PUBLIC-SOURCE-SCREENING-SCOPE-2 — fresh-context round-2 review of the public-source screening scope package
Reviewed commit: 076ffdc95b9e4585bb3441933d00c1601e0a0bc9
Manifest SHA-256: c8b3700d380d4f9934cc6fd0259047eaa9804e85988b7d44c50d751cfd2a098d
Verdict: REVISE

Reviewer: fresh-context agent, 2026-10-03. Scratch worktree detached at the
reviewed commit, read-only; simulations ran on a `git archive` copy and a
`git clone --shared` scratch clone, never on a tracked file. No external
repository was read and no model was called. Other branches of this
repository were read by ref: PR #120 at `0a8ef671`, PR #215 at `b17207ce`,
PR #259 at `37d496ce`, PR #260 at `b76c5c4f`. The manifest digest in the head
was printed by `--manifest-digest` and by `sha256sum` (they agree), and
written into this file by script.

## What was run

- `python3 scripts/build_public_source_screening_scope.py --check`:
  `public-source screening scope: current`, exit 0.
- `--selftest`: `selftest: 22 of 22 predicates held`, exit 0 (22 lines `ok`).
- Independent application: the patch applied with `patch` to a scratch copy
  of the policy hashes, by `sha256sum`, to exactly the manifest row. Parsed as
  JSON, the only key added is `publicSourceScope` (directly after `scope`),
  the only key changed is `policyVersion` (`1.1.0-candidate.1` to
  `1.2.0-public-source-candidate.1`), no key removed. The new label passes
  `SEMVER` in `body-read-authority.ts:338`.
- `python3 scripts/check_governance.py` at the reviewed commit:
  `31 OK, 21 WARN, 0 FAIL (52 checks)`.
- Sweep 1 (`git grep -l -F` for the policy basename): at `c540438d` 1975 files,
  52 hits, 14 under `apps/`, `packages/`, `scripts/` (the ledger's 14, same
  names); at the reviewed commit 1983, 57, 15. Re-run a second way (Python
  `re.search` over `git show` of every `git ls-tree -r -z` path): same figures.
- Sweep 2 (`policyVersion|accessBoundary|sourceAdmission|rawBodyHandling`
  under `apps/` and `packages/`): 15 files at both commits, by both methods.
- Version-literal sweep (`grep -F 1.1.0-candidate.1` over tracked files under
  `apps/`, `packages/`, `scripts/`): 8 files at both `c540438d` and the
  reviewed commit (5 under apps/packages, 3 under scripts).
- Simulated act (scratch clone at the reviewed commit, patched policy
  committed): `record_pwb_behavior_contract_repin_acts.py --check policy …
  --date 2026-10-02` fails ("policy subject hashes to …, not the owner
  argument"); `build_pwb_behavior_contract_repin.py --check` fails ("the tree
  with the patch reversed hashes to …, not the argument …");
  `check_governance.py` gives `30 OK, 21 WARN, 1 FAIL` — CG-7e with 6
  findings.
- PR #120 first (scratch clone; #120's policy patch from `0a8ef671` applied):
  this builder's `--check` reports `STALE`; after `--write` it is `current`
  and the proposed version is `1.3.0-public-source-candidate.1`. Holds as the
  delta states.
- Criterion 8: the four package Markdown files carry 0 standalone 64-hex
  tokens; `reviews/R-PUBLIC-SOURCE-SCREENING-SCOPE-1-RAW.md` carries 1 (its
  own head). No file labels anything accepted or approved; hits for
  `approve`/`adopt` are act-type names, the provenance-state label and the
  brief's criterion.

## Criteria

1. **Diff exactly the stated change: holds.**
2. **No contradiction with inherited base rules: holds.** `inheritedRules`
   (patch :154) now gives one reading of `classificationOrder` steps 1, 5, 6
   and 7 and of `classificationSuccess`; active content is unchanged
   (patch :129); indeterminate has one fail-closed reading (patch :93). The
   cross-package contradiction in Finding 2 is with the egress template, not
   a base rule.
3. **Loosenings stated and bounded: holds** against Q3 (run directory) and Q6
   (local editorial draft): storage, rendering, two network routes, logging and
   machine response `never`. The scope permits *less* than the egress template
   needs (Finding 2), not more.
4. **RFC5-14 soundness: partly.** Classes are by rule; `work-history` never;
   `project-documentation` absent; indeterminate fails closed;
   `classificationBasis` (patch :110) matches RFC5-14 "a property of what
   enters the choke point, tracked from where the content originated". The
   instruction-text rule is closed and sufficient: [Observed] `prompts.ts`
   has no import, `provider-draft.ts` imports only `node:util` and a type,
   and the template's `envelope-control` fields (`promptVersion`,
   `responseSchemaVersion`) are produced by the two named symbols
   (`prompts.ts:31`, `provider-draft.ts:68`, used at `pipeline.ts:258`). The
   scope does not classify the target-metadata the template sends
   (Finding 2), and the run-profile condition is not satisfiable by current
   code (Finding 6).
5. **Extension list labelled [Inferred]: holds** (delta :32, packet Q3, patch
   comment in the builder :59).
6. **Read-gate consequence: holds.** [Observed] `exact-digest-wrong`
   (`body-read-authority.ts:444`) precedes `policy-version-wrong` (:641).
7. **Sweeps honest: hold** in their counts; one sentence of the version
   predicate miscounts (Finding 4).
8. **Authority: holds**, with the literal-wording note in Finding 8.
9. **Round-1 repairs:**
   - F1 (pins): partly — the table grew but is still incomplete (Finding 1).
   - F2 (digest first): resolved (delta :82-89, ledger :50-51).
   - F3 (asymmetry): resolved in the delta (:62-78) and packet Q4; distinct
     label holds; the builder docstring still states the old symmetry
     (Finding 3); the reverse sibling direction stays open (Finding 5).
   - F4 (active content): resolved — no loosening, builder predicate "active
     content loosened is caught".
   - F5 (indeterminate): resolved — one reading, enforced by "indeterminate
     reading dropped is caught"; a stale builder comment remains (Finding 3).
   - F6 (Q2/Q7 narrowing): resolved — delta :51-60 and packet Q5.
   - F7 (configuration, case): resolved — patch :57, delta :32, packet Q3.
   - F8 (networkEgress wording): resolved — delta :39.
   - F9: unchanged and still true at these bytes.
   - New in this round: `classificationBasis`, `runProfileRule`,
     `exclusionMetadata`. The last introduced a defect (Finding 2).

## Findings

**Finding 1 — The pin table and the Q2 continuation still omit pins that break on the act** (revise)
IMPACT-LEDGER.md:34-35 says the table is "Re-derived … Every one needs
re-pointing in the same change as the act", and OWNER-DECISION-PACKET.md:26-34
(Q2) asks the owner to widen the continuation to exactly that list. A fresh
sweep finds pins the table does not name:
- run-time act identity in `apps/three-surface-poc/src/governance-inputs.ts`:
  `actIdentity` (:98), `recordingTag` (:101, a signed git tag), the
  superseded-record pointer `PWB_SUPERSEDED_ACT_RECORDS.policy` (:63) that
  `supersession` (:104) targets; and their assertions in
  `governance-inputs.test.ts` (:167, :306, :308). The table's
  `governance-inputs.test.ts:311` row covers only the scope anchor;
- governance tooling bound to the current policy digest, which the simulated
  act turns red: `PROJECT-STATUS.md:376` and `:378` and
  `.github/workflows/governance-docs.yml:155` and `:161`
  (`build_pwb_behavior_contract_repin.py --check` and
  `record_pwb_behavior_contract_repin_acts.py --check policy …`, both fail),
  and `scripts/check_governance.py`'s act-subject chain for
  `APPROVE POLARIS BUTLERS SECRET-CLASSIFICATION POLICY` (:1633-1683) and
  ACT_DIGEST_COPY_FILES rows, without which CG-7e fails with 6 findings
  (simulated). A superseded recorder failing `--check` is by design, so these
  lines must be replaced in the recording change, which the owner's
  continuation must cover.
The ledger's heading is "Pins that carry the policy version or digest"; the
battery and workflow lines carry the digest literally and are absent.
Violates: brief criteria 6 and 9 ("is it complete?"); AGENTS.md verification
rules 2 and 9 (a completeness claim needs a sweep with a denominator).

**Finding 2 — `exclusionMetadata` conflicts with the egress template's target-metadata, and no rule classes what every inventory and plan request carries** (revise)
Patch :111 makes the list exhaustive: "the metadata of an excluded source that
may leave the host is its content digest, its policy id and version and one
exclusion reason". The egress template the brief names
(`public-repo-admission/templates/EGRESS-CONSENT-TEMPLATE.md:46-49` at PR #215
`b17207ce`) sends "the source ids, classification bases, exclusion flags and
closed exclusion reasons of the same pairs' sources … Excluded sources'
metadata may leave". The pipeline does exactly that today: `sourcePopulation`
(`packages/polaris-generation-core/src/pipeline.ts:237-238`) carries
`sourceId`, `classificationBasis`, `excluded` and `reason` for every source,
excluded or not, and is sent at the inventory and plan stages (:393-394).
Under this scope (patch :110 says a field-level table confers no class) the
`code-structure` rule (patch :53) covers paths, object ids and sizes only, and
no other rule covers a classification basis or an exclusion flag. [Inferred]
Those fields have no determinable class, so RFC5-14 refuses the request; and
since README, LICENSE and every non-listed extension are excluded (patch
:93), every real target has excluded sources, so every inventory request of a
T1 run is refused. It fails closed, but the two drafts cannot run together,
and the list carries content digest and policy id/version, which the pipeline
does not send, while omitting the four fields it does. The admission round-7
disposition 4 carried "reason must come from a closed list" here; it did not
ask for an exhaustive field list. No owner question in this packet or in
PR #260 (`OWNER-SITTING-PACKET.md` at `b76c5c4f`) presents the choice, and the
signed bytes assume an answer. Also note: the template (:50-53) relies on "the
generator-authored-request-text rule of … the public-source screening scope";
no rule of that name exists here (the rules are `instructionTextRule` and
`runProfileRule`). Violates: brief criterion 4 (sufficiency for RFC5-15 part
2), criterion 9 (a repair introduced a defect); RFC5-14 "Classification is
determinable".

**Finding 3 — The builder still states two round-1 readings the repair retired** (note)
`scripts/build_public_source_screening_scope.py:14-18` says "whichever act
lands second reruns `--write` against the other's performed bytes, and the
next minor follows automatically" — the symmetric reconciliation round-1 F3
found false for this-package-first. `:59-60` says a file outside the list is
"indeterminate and refused egress", the reading round-1 F5 retired (patch :93
excludes it from reading as well). Neither is a manifest row. Violates: brief
criterion 9 (round-1 F3, F5 repairs carried into every artifact file).

**Finding 4 — The version-literal sentence miscounts the scripts and misnames one** (note)
IMPACT-LEDGER.md:45-48: "8 files. Three recorders and one builder in
`scripts/` also carry it". The 8 files are 5 under apps/packages and 3 under
scripts: two recorders (`record_pwb_behavior_contract_repin_acts.py`,
`record_pwb_effect_amendment_acts.py`) and one builder
(`build_pwb_registry_currency_briefing_amendment.py:54`), and that builder's
`CURRENT_VERSION` is the registry's version, not the policy's. IMPACT-LEDGER.md:23-25
also says `git-object-reader.ts` "check[s]" a field; it carries a copy.
Violates: AGENTS.md verification rule 3 (totals are computed).

**Finding 5 — Sibling separation is one-directional** (note)
`inheritedRules` (patch :154) says sibling scope rules do not govern this
scope, but nothing says this scope's rules govern only the repositories it
admits. PR #120's `selfObservationScope.inheritedRules` (its patch :37 at
`0a8ef671`) reads "every other rule in this policy applies to this scope
unchanged: the access boundary, … raw-body handling". Once both are performed,
in either order, a reader can ask whether `publicSourceScope.accessBoundary`'s
routes or its run-directory `rawBodyHandling` reach the self-observation
scope. The nesting and `observedRepositories` (patch :14) make the narrow
reading likely [Inferred]; one clause here would close it. PR #120's contents
are out of scope; this scope's own bytes are not. Violates: none; legibility
of a loosening boundary.

**Finding 6 — The run-profile condition names a carrier no request has** (note)
Patch :125 classifies questions and assets only "at the profile id a request
names (dossier-v1 at drafting)". [Observed] At the reviewed commit
`dossier-profile.ts` does not exist (it is on PR #259, `agent/dossier-engine-4`
at `37d496ce`, and two later branches); no request type names a profile id at
the base or on PR #259, whose `repo-corpus.ts:51` selects by config
`profile: "dossier"`, not `dossier-v1`. The [Observed] claims about the base
(readerQuestions `unknown`, `pipeline.ts:27`; only requestedAssets validated,
:191; forwarded unchanged, :239) hold. The effect fails closed — nothing is
classified until a request carries the id — and the packet presents the typed
validation as not assumed. Not blocking; the condition's carrier should be
named when PR #259 lands. Violates: none at these bytes.

**Finding 7 — Q6's measured-later consequence understates two listed extensions and a second exclusion path** (note)
Patch :129-130 and packet Q6 (OWNER-DECISION-PACKET.md:57-61) disclose that
markup-like bytes outside an inert context are withheld. [Inferred] from the
base `activeContentClassification`: `.jsx` and `.tsx` (patch :71, :83) contain
`html-element` forms by construction, so the list proposes classes for files
the scan will nearly always withhold; and an unmatched backtick run
(`unclosed-inline-span`, a `notInert` form, with `malformedContextAction`
exclude-whole-artifact) excludes shell scripts with command substitution, Go
raw strings or JS template literals of odd backtick count, independent of
markup. Q6 is an open owner question with measure-first as its recommendation;
the signed bytes take the recommended answer, which is the question. Not
blocking. Violates: none; disclosure precision for Q3 and Q6.

**Finding 8 — Criterion 8's wording catches the package's own retained raws** (note)
REVIEW-BRIEF.md:49-50 forbids any 64-hex digest "in any Markdown file of the
package", while :69-79 require each raw in `reviews/` to carry the manifest
digest in its head; the round-1 raw does (1 token), as this one will. Raw
output is CC-REV-6 material and exempt in substance. Violates: none; the
criterion should scope out `reviews/`.

## Verdict

REVISE: Findings 1 and 2 are revise. Findings 3 to 8 are notes.
