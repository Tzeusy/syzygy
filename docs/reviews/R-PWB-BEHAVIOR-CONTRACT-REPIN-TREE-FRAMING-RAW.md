# Independent review — PWB behaviour-contract re-pin to the tree-framing sign-off (round 1)
Reviewed commit: 54f8b30837536e3bf90d445fe0048f0316fee41b
Manifest SHA-256: 9214191663ea076b331acad63f6d2b1789ed1bbf5a8a17c5acf406213b36a227
Verdict: REVISE

Reviewer context: fresh context, review tree detached at the commit above, own scratch clones under the session scratchpad (`m6`, `c3`, `base`, `reh`, `reh2`), no edits to the review tree, no commits. The manifest digest above was computed with `sha256sum` on the FILE `PWB-EFFECT-REPIN-MANIFEST.txt` at that commit. `python3 scripts/build_pwb_behavior_contract_repin_tree_framing.py --manifest-digest` printed the same value.

## Findings

**Finding 1 — the Signing path misstates the condition in the Scope A direction's "What this does not do" sentence and treats it as still in force** (revise)

`OWNER-DECISION-PACKET.md`, "Signing path", registry paragraph: "The Scope A direction's own "What this does not do" section also says the existing phrase-and-digest acts "remain the only way to perform the queued packages" until that contract change lands."

The direction (`decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`, "What this does not do") reads: "The replacement mechanism and the removal of the digest machinery for the covered artifacts travel as one governed change after this record. Until that change lands, the existing phrase-and-digest acts remain the only way to perform the queued packages." "That change" is the governed change that implements the replacement mechanism. It is not a contract change. Nothing earlier in the packet's paragraph is a "contract change" either. The nearest phrase, "a separate contract-reading decision", comes after the sentence.

[Observed] Commit `842b624f` (2026-10-02), "version-tagged sign-off recorder and wiring (Scope A)", says it "Implements OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02". The recorder it added, `scripts/record_versioned_signoff.py`, has since recorded the very sign-off this package pins to (`pwb-tree-framing-amendment-v1.0`). [Inferred] At least part of "that change" has landed. Whether it covers the registry entry is a separate question. The commit names "the RFC-0007 scoped-values successor and lane B" and never mentions the registry. The packet does not say that the condition is partly met, and it presents the bar as current.

The sentence is also at odds with the packet's next paragraph, which says "The Scope A path stays open to the owner". If digest acts "remain the only way", that path is not open. This paragraph is what the owner reads to answer open question 1, so the misstatement bears on a decision. The main reason the packet gives still holds: the gate code plus the RFC3-16(a)/(b) quotation (see criterion 8). The fix is to quote the condition as the direction words it, say what has landed (`842b624f`, the recorder) and what has not (the gate never learned to read a tag record for the registry role), or drop the sentence.

**Finding 2 — three builder predicates survive their own removal** (note)

Rule-6 run in scratch clone `c3`: each predicate was replaced with `if False` (one at a time, original restored between runs), then `--selftest` was run.

- `if _count_contracts(new) != 1:` → `35 fixtures, 0 failing` (survived).
- `if read(root, subject.path) != body:` (post-act "the act is performed but the subject is not the proposed bytes") → `35 fixtures, 0 failing` (survived). [Inferred] This predicate is unreachable by construction. `base_bytes` reverse-applies the patch to the live subject and `check` forward-applies it again, so `body` equals the live bytes whenever the reverse apply succeeds. The docstring's "so the tree carries exactly the proposed bytes" rests on the reverse apply plus the predecessor-digest test, not on this line.
- In `apply()`, `if findings:` → `if False:` ("refusing to apply: the package does not verify") → `35 fixtures, 0 failing` (survived). The only `apply` refusal under test is the missing `--at-adoption` case. The adoption step that the packet and the delta describe ("applies its own patch through ... `--apply <subject> --at-adoption`") depends on that refusal, and no fixture shows it.

Every other predicate was killed: keys, id, signed row, signedBy, Tag line, changes-nothing, restored-equality, two-line count, stale pin, row order, exact regeneration, `proposed/` population and base hash, each with 1 to 4 failing fixtures. All 35 fixtures are mutations the package really would be wrong about. No fixture is vacuous. The R6 case covers the wrong-pin case independently (criterion 6).

**Finding 3 — the impact ledger's `governance-inputs.test.ts` row names one failing case, but five others fail in a rehearsal** (note)

The ledger row reads: "`apps/three-surface-poc/src/governance-inputs.test.ts`, real-tree case | ... | [Inferred] **Fails** until the gate is re-pointed; read from the test, not run against the rehearsal". I ran `npm ci --offline` in scratch clone `reh2`, then `--apply both --at-adoption` and the two placeholder records, then `npx vitest run apps/three-surface-poc/src/governance-inputs.test.ts`. Five **hermetic** cases fail, because they build their fixtures from the live artifact and record bytes:

- "loads the three artifacts and act records and resolves every recording tag"
- "detects a later decision record that revokes or supersedes an act identity" (`registry:exact-digest-wrong`, expected `registry:superseded`)
- "detects a later amendment-form record that supersedes an act by its record path" (`policy:exact-digest-wrong`)
- "the current policy and registry acts name the records they supersede…" (`policy:exact-digest-wrong`, expected `supersession-target-wrong`)
- "direction C: the gate admits under the 2026-10-02 re-pin acts…"

The real-tree case passed in that run, because it reads `HEAD` (`governanceRevision = git rev-parse HEAD`) and the rehearsal was not committed. [Inferred] From line 393 (`expect(record.text).toContain(\`Exact digest (SHA-256): …\`)`), it will fail once the act change is committed, as the ledger says. Across `packages/three-surface-poc-core` and `apps/three-surface-poc`, 1,478 tests passed and 5 failed, all in this one file. The two unhandled errors were vitest worker RPC timeouts under load and are unrelated. At-adoption step 4 ("Direction C's implementation re-point, with its tests") already covers all six cases, so no decision changes. The row understates the work.

**Finding 4 — the reason given for Normative does not use the template's test** (note)

The class is right (see criterion 1). The delta's reason, though, says "No reader is put out of compliance by it, but the governed object changes". The template's test for Normative is "Someone who complied before may not comply now, or the reverse" (`SEMANTIC-DELTA-TEMPLATE.md`, "Change classes"). Read literally, the stated reason answers that test with "no". The stronger reason, which fits the template, is that the declared governing contract now includes seven PWB-REQ-014 tree-framing scenarios. An observer that conformed to the readability-successor `spec.md` may not conform to the one now pinned.

**Finding 5 — open question 2 understates what a version-label bump would touch** (note)

The packet says a bump "would change both arguments, the gate's scope anchors and two tests that read `policyVersion` from the file. Direction C would then also cover the anchors." Those two tests do exist (`content-classification.test.ts:550`, `git-object-reader.test.ts:547`). A bump would also reach implementation constants that are not scope anchors: `packages/three-surface-poc-core/src/git-object-reader.ts:43` (`policyVersion: '1.1.0-candidate.1'`), `packages/three-surface-poc-core/src/project-shape-observation.ts:50` (`observerVersion: '1.2.0-candidate.1'`) and the gate's `policyVersion` expectation at `apps/three-surface-poc/src/governance-inputs.ts:81`. Hard-coded literals in `content-classification.test.ts`, `project-shape-model.test.ts` and `project-shape-observation.test.ts` would also need changing. A direction C limited to "anchors" would not cover the core constants. The drafted answer is "no bump", so this matters only if the owner chooses otherwise. The 2026-10-02 packet carried the same sentence.

**Finding 6 — RFC3-16(b) item 3's full wording is not quoted where open question 1 turns on it** (note)

The packet says the gate "would stay closed until the owner decided whether a tag on a commit satisfies RFC3-16(b) item 3". Item 3 reads "the **exact content or revision digest** of the artifact as acted on". The words "or revision" are what such an owner decision would be about, and the packet does not quote them. The packet's own quotations from RFC3-16(a) are accurate.

**Finding 7 — the Recording section does not say which review-campaign row this raw joins** (note)

Under the brief's name, `R-PWB-BEHAVIOR-CONTRACT-REPIN-TREE-FRAMING-RAW.md` matches the existing `registry-currency` campaign ("P-69/P-72 registry gate", pattern `R-PWB-(?:REGISTRY-CURRENCY|BEHAVIOR-CONTRACT-REPIN)-.*\.md`, `scripts/check_docs_review_campaign_partition.py:189`). It does not match the `tree-framing` campaign (`R-PWB-TREE-FRAMING-.*\.md`). Storing it therefore changes that row's count (5) and its last verdict of record in `docs/README.md`, in the same commit as the raw. This is integration work at recording time, outside the reviewed bytes.

## Criteria

### 1. Is the change class right?

Yes, Normative. `SEMANTIC-DELTA-TEMPLATE.md` defines Clarifying as "The obligation is unchanged; its statement is made harder to misread." That does not fit. The field's referent changes from the `spec.md` signed as `pwb-readability-successor-v1.0` to the one signed as `pwb-tree-framing-amendment-v1.0`, and the delta says the latter adds seven PWB-REQ-014 scenarios. The governed obligation is wider, which is Normative under the template ("An obligation is added, removed, narrowed, or widened"). The prior re-pin chose the same class (`pwb-behavior-contract-repin/SEMANTIC-DELTA.md` line 20). The reason given is weaker than it should be (Finding 4), but the class does not depend on it.

### 2. Are the subjects untouched?

Yes. At the reviewed commit, `sha256sum` gives:
- registry `ad9cd6769bffbb1a3ef94625c73226dec133fb7c9f1e0bc40186b09b15e165fa`, equal to `PWB-OBSERVER-REGISTRY-BEHAVIOR-CONTRACT-REPIN-ACT.md:15` `Exact digest (SHA-256)`;
- policy `66cd41ee626efb11d666d19c0cd42c6d001ec4482837b71475c42f661f1d936c`, equal to `PWB-SECRET-CLASSIFICATION-POLICY-BEHAVIOR-CONTRACT-REPIN-ACT.md:15`.

`git diff --name-status dbf8ed19 54f8b308` lists 11 paths: seven added package files, the new builder, and three modified files (`PENDING-OWNER-DECISIONS.md` one row, `PROJECT-STATUS.md` one row, `check_spec_reconciliation.py`). No subject, act record, aggregate record or prior manifest is in the list. The only proposed change to either subject is the two patches.

### 3. Does the patch change exactly what the delta says?

Yes. In scratch clone `c3`, `git apply --check` and then `git apply` of both patches gave `--numstat` `2 2` for each subject. A recursive JSON-path diff between `HEAD:` and the applied bytes returns exactly `/entries/0/governingBehaviorContract/{signedBy,version}` for the registry and `/governingBehaviorContract/{signedBy,version}` for the policy. `id` is unchanged. The applied bytes hash to the manifest rows (`f9441339…` registry, `97b43474…` policy).

### 4. Is the pin right?

Yes. Python sha256 of the current `spec.md` gives `d0ac6ba20501798e715aae42e16fbc7555fc8d4d60f9f16e01f376fb75349c4a`. The single `spec.md` row of `pwb-tree-framing-amendment/PWB-TREE-FRAMING-AMENDMENT-MANIFEST.txt` is the same value, and both patches pin `sha256:` plus that value. `git cat-file -t pwb-tree-framing-amendment-v1.0` gives `tag`, an ancestor of the reviewed commit, and `git show pwb-tree-framing-amendment-v1.0:<spec path> | sha256sum` gives the same digest. No later commit touches `spec.md`. `signedBy` names that tag and `decisions/PWB-TREE-FRAMING-AMENDMENT-SIGNOFF-v1.0.md`, whose line `Tag: pwb-tree-framing-amendment-v1.0` names it, as does the tag's tree. The builder checks the record's Tag line and the manifest row. It does not check the git tag itself, which I checked here.

### 5. Does the package verify, and does its verification mean anything?

`--check`: rc 0, "manifest matches its 2 proposed subjects (pin = the pwb-tree-framing-amendment-v1.0 spec.md row); registry: patch applies to the act-in-force bytes, policy: patch applies to the act-in-force bytes". `--selftest`: "35 fixtures, 0 failing". Each mutation is a real way the package could be wrong: subject drift, a wrong predecessor digest, corrupt context, a superseded or unsigned pin, a wrong tag, a changed id, an extra key, an outside field, a whitespace-only line, a version-only patch, the signing record missing or naming another tag, the spec row missing, a stale `spec.md`, manifest digest/path/missing, `proposed/` population, records without application, post-act drift, and the replay arms. Claims no mutant covers: the contract-count predicate, the post-act "subject is not the proposed bytes" predicate, and `apply()`'s refusal when the check fails (Finding 2). Also confirmed in rehearsal clone `reh`: post-act, `--check` gives "registry: performed, subject = proposed bytes, policy: performed, subject = proposed bytes" and `--selftest` gives 35/0.

### 6. Does the R6 case prove what it says?

Yes. On the tree, `check_spec_reconciliation.py --check` reports R1–R5 and R7 OK, `WARN R6 … 2 examined, 2 findings`, each naming `0d50f8f4…` against `d0ac6ba2…` and `(syzygy-2g0d)`, then "7 of 7 predicates without FAIL". `--selftest` gives "40 of 40 mutants killed", including `pins-after-repin-acts R6=0|R2,R3,R4 (failed: R2, R3, R4)` and `pins-after-tree-framing-repin-acts R6=0 (failed: )`.

Rule 6, in scratch clone `m6`:
(a) The policy patch's `+    "version": "sha256:d0ac6ba2…"` changed to `sha256:` followed by `ab`×32: the selftest prints `SURVIVED pins-after-tree-framing-repin-acts` and `SELFTEST FAIL`.
(b) The registry patch's plus line changed to the superseded `sha256:0d50f8f4…`: same result. The builder's `--check` fails on (b) with the signed-row, two-line, stale-pin and regeneration findings.

In both runs `pins-after-repin-acts` was still killed. R6 examined both pins: `check_pins` adds a finding for any subject that has no contract, so `R6=0` cannot pass with only one pin examined.

### 7. Is the read-gate consequence stated correctly?

Yes. `governance-inputs.ts:56-60` `PWB_ACT_RECORDS` names the two 2026-10-02 records the packet names. `body-read-authority.ts:443-444` returns `exact-digest-wrong` when the record's digest is not the artifact's. `:531-532` returns `superseded` when the lifecycle scan (`governance-inputs.ts` `lifecycleFor`, matching by act identity or record path) finds a superseding record. `:736` sets `admits = valid.length === AUTHORITY_KINDS.length`. Observed in `reh2`: after the apply, the hermetic tests report `registry:exact-digest-wrong` and `policy:exact-digest-wrong` (Finding 3).

Direction C is enough and no wider than needed. The gate's role-specific expectations are the record pointers, `actIdentity`, `recordingTag` and the `supersession` target (`PWB_SUPERSEDED_ACT_RECORDS`). C permits exactly those plus tests. The `scopeAnchors`, `policyVersion`, `governingActInstant` (`2026-09-02`, which predates the new acts) and consent are unchanged and need not move. `governingBehaviorContract` is read by no code (criterion 9).

### 8. Is the signing-path reasoning sound?

The policy is outside Scope A. Item 1 of the direction lists "the PWB specification deltas, the observer registry entry and the contract successors queued behind them", and a secret-classification policy is none of these. The packet quotes that list exactly. The RFC3-16 quotations are accurate at their defining clause (`governance-homes-and-owner-acts.md:215-220`): "Such an artifact is honored only through an **effective owner act**", and "bound to the artifact's exact digest under RFC3-16(b)". They match the gate code: `git-ref-only` ("only a Git commit/tag attests") and `specification-signoff-only` are invalid record kinds, and `exact-digest-*` enforces item 3. The counterfactual "no lawful re-point would exist" is labelled `[Inferred]`, which is right for a counterfactual. The added sentence paraphrasing the Scope A "What this does not do" section is not accurate (Finding 1), and item 3's own wording is not quoted (Finding 6).

### 9. Are the impact ledger's sweeps and rehearsal honest?

At `dbf8ed1911aa193b0db7cfebdf8d4338c7500ba0`, `git ls-tree -r` gives 1,973 files. Sweep 1 (`git grep -l -F governingBehaviorContract`) gives 32 files, and a second method (Python byte search over every blob in that population) also gives 32. The ten classes sum to 32 as stated (2+1+2+1+1+6+3+6+1+9), and every file falls in the class the ledger gives. `-- packages apps` returns one line, the `governance-inputs.ts:54` comment.

Sweep 2 gives registry 26 and policy 20 by both methods. The evidence and pursuit JSON split is 14 and 6. Every implementation or tooling file in sweep 2 appears in the reader table. I also swept the gate loader's importers (`PWB_AUTHORITY_ARTIFACTS|PWB_ACT_RECORDS|PWB_SUPERSEDED_ACT_RECORDS|loadBodyReadAuthorityInputs` over apps, packages and scripts): `git-blob-batch.test.ts` (only compares single and batched loads at `HEAD`), `production-reobserve.ts` (production consumer, covered by "Read gate") and `project-shape-discovery.live.test.ts` (skipped unless `SYZYGY_POC_BUTLERS_REPO` is set; expects `admits` true, so it is restored by C). None changes a conclusion.

Rehearsal, repeated in clone `reh` (`--apply both --at-adoption`, two `# placeholder` records at the offered paths, uncommitted), running the full PROJECT-STATUS battery plus this package's builder check and selftest. The unmodified clone `base` passed all 70 commands. In `reh`, exactly these failed:
- `check_governance.py`: `FAIL CG-7e … 68 files examined, 11 findings` (ledger: 11);
- `build_pwb_registry_currency_briefing_amendment.py` `--check` and `--selftest`, and `record_pwb_registry_currency_amendment.py --check`;
- `build_pwb_behavior_contract_repin.py` `--check` and `--selftest`;
- `record_pwb_behavior_contract_repin_acts.py --check policy` and `--check registry`;
- `check_spec_reconciliation.py --selftest` (`ValueError … does not reverse-apply`, inside `build_pwb_behavior_contract_repin.py`).

These passed: `record_pwb_behavior_contract_repin_acts.py --selftest` (38/0), `record_pwb_registry_currency_amendment.py --selftest` (16/0), `build_pwb_truth_policy_amendment.py --check`, `check_polaris_response_ceiling_reading.py --check` (`OK`), and `check_spec_reconciliation.py --check` (R1–R7 OK, `R6 … 2 examined, 0 findings`). Every stated result is confirmed. The one TypeScript row is understated (Finding 3).

### 10. Is the at-adoption list complete?

Every failure in the rehearsal maps to a step. CG-7e maps to step 2. The 2026-10-02 and 2026-09-30 builders and recorders map to step 3, which also names the `pins-after-repin-acts` dependency of the R6 selftest. `governance-inputs.test.ts` maps to step 4. R6 maps to step 5. The battery lines for this package's builder (not yet in the battery), the workflow and the CG-26 sentence map to step 6. The phrases are unchanged from the 2026-10-02 acts (`APPROVE POLARIS BUTLERS SECRET-CLASSIFICATION POLICY`, `ADOPT POLARIS BUTLERS PROJECT-SHAPE OBSERVER REGISTRY ENTRY`, the same `phrasePrefix` in `governance-inputs.ts`). The packet carries no phrase-linked digest, so not registering at drafting is consistent with the 2026-10-02 draft. I found no missing battery line, registration or reader. A recording-time item outside the acts is in Finding 7.

### 11. Does the package avoid quoting any act argument?

Yes. A Python sweep for standalone 64-hex tokens over all 7 package files gives 0 in each of the four Markdown files. The non-Markdown files hold 2 each: the manifest's two rows, and in each patch the old and new `version` pins (spec digests, not act arguments). No Markdown file carries a 12-to-63-hex run either.

### 12. Does the package claim any authority it lacks?

No. All four Markdown files open with "**Candidate — binds nothing.**", and the manifest header says "Candidate; this file and its rows bind nothing by themselves." A case-folded sweep for `accepted|adopted|approved|signed off|sign-off|performed` finds only factual uses: "accepted RFC 0003", "accepted contracts", the existing tree-framing "sign-off", "performed package/records" naming history, and the brief's criterion 12 wording. The `PROJECT-STATUS.md` row and register row P-90 say "Candidate … not yet reviewed; binds nothing" and "Not yet reviewed, so not yet offered".
