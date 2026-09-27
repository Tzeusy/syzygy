# R-DOV25 — independent review of the three test-only self-observation act packets (PR #120)

- Reviewed commit: `53237210ec4d81c91a9216ff758c0cbf0c618e60` (`origin/agent/tier4-dov25`), merge base `3ee61c7`
- Also checked: a local merge of that head onto `origin/main` `23b486c`
- Package: `.syzygy/governance/contracts/candidates/pwb-self-observation-acts/`, `scripts/build_pwb_self_observation_acts.py`, `scripts/check_governance.py` (diff)
- Reviewer: fresh-context agent, read-only. Nothing was edited in the repository or on the branch. Mutations ran only in throwaway copies under the scratchpad.
- Date: 2026-09-27

## Commands run and outputs read

| Command (tree) | Result |
|---|---|
| `build_pwb_self_observation_acts.py --check` (PR head) | exit 0; "3 manifests match their 3 proposed artifacts"; digests e72382b6…, 2218911c…, d93a7754… |
| `--check` (PR merged onto `origin/main`) | exit 0, same digests |
| `--selftest` (PR head) | exit 0; "selftest: 44 predicates". I recounted the `expect`/`count` sites: 5 + 12 + 12 + 15 = 44 |
| `check_governance.py` (PR head / base / merged) | `32 OK, 20 WARN, 0 FAIL (52 checks)` on all three. I diffed base against head: the only changes are the file-count denominators, CG-7d gaining the two new subjects (1 quotation each, 0 findings), and CG-7e registering the packet and two manifests |
| `check_governance.py --selftest` (PR head) | `268 fixtures, 0 failing` |
| Rule 6 on the registration (copy): append one byte to the proposed consent | CG-7d FAIL at `OWNER-DECISION-PACKET.md:54`; CG-7e FAIL on the packet and `SELF-OBSERVATION-CONSENT-MANIFEST.txt`; `31 OK, 19 WARN, 2 FAIL`. The registration bites |
| Rule 6 on `--apply` (copy): `--apply consent --at-adoption`, then `--apply policy`, then `--apply registry` | the first succeeds; **both later ones refuse** (see F1) |
| Re-derivation of the impact ledger's sweeps at `3ee61c7` (`git grep -F` / `-nE`) | S1 38 ✓ (docs 14 ✓); S2 10 lines ✓ as a regex count, but it understates the population (F7); S3 19 ✓; five spec-patching packages ✓ (the five listed); 20 foreign patches in 7 directories ✓; S5 2 ✓; S6 2 ✓ |
| Digest sweep on PR head for e72382b69ff4 / 2218911c7b04 / d93a7754089f | found only in this package's packet and manifests; "no other candidate hashes the two new files" ✓ |

Clauses I checked at source: P-74 row (ruling file line 64) ✓; PWB implementation act line 73 ("No second repository…") ✓; RFC1-3 (RFC-0001 lines 130–133) ✓; the PWB-REQ-005 excerpt (spec lines 206–210) ✓; the policy's current bytes `d148f036…`, bound by `PWB-SECRET-CLASSIFICATION-POLICY-AMENDMENT-ACT.md:15/36` and the acceptance record line 281 ✓; the version sites `governance-inputs.ts:72` and `git-object-reader.ts:43` ✓.

What holds: the three acts have separate subjects, phrases and manifests. Act 3's reuse of the performed label is justified and is registered correctly as not-yet-a-chain-link. The consent quotes no owner words, and a check backs that. The Butlers consent, the Butlers registry entry and the spec are byte-untouched. The policy builder asserts that every key other than `policyVersion` and `selfObservationScope` is equal. The CG-7d/7e registration is existence-gated and mutation-tested. VIS-4 is respected: every artifact is banner-marked candidate, and no act, record or acceptance row is written.

## Findings

### F1 — revise — `--apply` cannot perform three separate acts: the first adoption blocks the other two, and `--check` goes permanently red

Evidence:
- `scripts/build_pwb_self_observation_acts.py:269-272`, `new_target_findings`: "install target already exists", for both the consent and the registry target.
- `:596-601`, `apply()`: "findings = check() / if findings: print("refusing to apply…")".
- `policy_proposed()` (`:115-131`) re-applies the patch to whatever bytes are current, so once act 3 is applied it fails ("does not apply to the current bytes").
- The packet's order is `OWNER-DECISION-PACKET.md:130-132`: "Act 1, any time. / Act 3, together with the code change … / Act 2, last".
- I observed this in a copy. After `--apply consent --at-adoption`, both `--apply policy --at-adoption` and `--apply registry --at-adoption` print `refusing to apply: the package does not verify / install target already exists: .syzygy/governance/decisions/SYZYGY-SELF-PROJECT-SHAPE-OBSERVATION-CONSENT.md` and exit 1.

The ruling requires "three acts … each separate and dated". The tooling makes the second and third adoption impossible without editing the builder, and editing it at act time is the kind of unreviewed adoption-time change the packet otherwise avoids. The same defect makes `IMPACT-LEDGER.md:134` false as labelled: "[Observed] These are byte-identical before and after `--apply` of all three acts". `--apply` of all three cannot have been run, so the claim is at best [Inferred] from what `apply()` writes.

Fix:
- Make `check()`/`apply()` per-act and state-aware. An installed target that is byte-equal to its proposed file is "adopted", not "occupied". A policy whose current hash equals the manifest row is "adopted", not "patch fails".
- Add selftest mutants for each adoption order the packet allows.
- Relabel IMPACT-LEDGER:134 [Inferred], or run the three applies and cite the run.

### F2 — revise — the package claims PWB-REQ-005 governs the self pair, and inherits Butlers-bound "signed PWB grammar" steps; neither holds as written (rule 8)

Evidence:
- `SEMANTIC-DELTA.md:22-23`: "The three artifacts are the inputs PWB-REQ-005 names, for a second pair".
- PWB-REQ-005 itself (spec line 257–258): "The consent subject SHALL be exactly `(observing Syzygy project, configured Butlers repository)`". PWB-REQ-001 (line 73) opens "WHEN the POC observes Butlers".
- REQ-004 (lines 491–512) closes admission to "the nine literal V1 catalog headings", `Key Architectural Facts` and the exact `Precedence Order When Layers Disagree` table.
- The funnel the ruling adopted says the opposite of the delta: `docs/design/POLARIS-M8-PORTABILITY-FUNNEL.md` Gate row for slice 6, "No approved requirement names a self-observation".
- The policy patch's `inheritedRules` (patch line 30) carries over "phase-B manifest rule … classification order, classification success" unchanged. Those rules read, in the base policy:
  - phaseB `manifestRule`: "manifest must validate against the signed PWB source grammar";
  - `classificationOrder[0]`: "verify exact Git-object membership … against the signed PWB grammar";
  - `classificationSuccess`: "its extraction class is in the signed PWB closed set".

[Inferred] Under the self scope, "the signed PWB grammar" is the Butlers grammar. Every self source then fails membership, or else an implementer silently substitutes the unsigned registry profile for "signed grammar". Either way, brief question 2 ("really carry every screening rule over … with no gap") has a gap. The self pair's admission gate is also governed by no signed requirement: REQ-005's 195-case population is defined for the Butlers subject, and the ruling forbids editing it.

Fix:
- Replace SEMANTIC-DELTA:22-23 with an accurate statement: no approved requirement names the self pair, and slice 6 would apply REQ-005's gate by analogy, [Inferred].
- In `inheritedRules`, say explicitly how "signed PWB grammar / closed set" reads under the self scope. For example: "the PWB grammar's extraction classes and fixed literals apply unchanged; a self source matching no signed literal is excluded as unknown extraction class".
- Add an open question asking the owner whether REQ-005's gate applies to the self pair by analogy, or whether the test runs with no specified gate.

### F3 — revise — the consented source population is not closed, and the consent's scope floats with later, unpinned versions of the other two artifacts

Evidence:
- Consent, `proposed/SYZYGY-SELF-PROJECT-SHAPE-OBSERVATION-CONSENT.md:43-47`: "reads of exact Git objects … selected by the observation the second adapter-registry entry for this pair declares (observer `polaris-syzygy-self-project-shape`) and screened by the secret-classification policy's self-observation scope". There is no version or digest.
- Compare the Butlers consent (`BUTLERS-PROJECT-SHAPE-OBSERVATION-CONSENT.md:35-41`), which pins "specification digest `2e453a6e…`" and "that specification's closed source population".
- Policy patch line 29, `derivedSeedRule`: "read only the further indexes the second adapter-registry entry's profile for this pair declares".
- The entry declares none: `fixedCatalogKeys: []`, `rootSummary: null`, `precedence: null`, and no index list anywhere in the entry.
- Nothing in the three artifacts says what the phase-B manifest contains for this pair.

So the population is either {`doctrine/README.md`} or undefined. Worse, a later superseding registry entry, one that declares more indexes, would widen what the consent covers with no new consent act. The Butlers consent was pinned precisely to prevent that.

Fix:
- Pin the consent's scope to the observer ID and version, and to the policy's `1.2.0-candidate.1` self scope, adding "a later version of either needs a new consent act".
- Or state the closed population in the consent itself, for example: "phase A: `.syzygy/governance/doctrine/README.md`; phase B: only the files that index links to under `.syzygy/governance/doctrine/`".
- Make the registry entry declare the same population explicitly, rather than "none".

### F4 — revise — "never … logged, written to disk" is not met by the default test toolchain, and nothing in the drafts constrains it (brief question 1)

Evidence:
- Consent `:49-52`: "they are never served, cached, logged, written to disk or written to a walkthrough record".
- Registry `surfaceExposure.rule`: "never served, cached, logged or written anywhere".
- Policy patch line 25, `ingestBoundaryRule`: the same.

[Inferred] A failing Vitest assertion over the in-memory page or machine answer prints expected and received values to stdout, and those reach CI logs, which are a stored surface in SEC-5's terms ("any Syzygy surface, store, or endpoint"). A snapshot assertion writes to disk. The consent makes a promise that the most natural implementation breaks on its first red run. The body would be screened, but the record would still be false.

Fix: before act 1's digest is fixed, add one bounding sentence to the consent, and mirror it in `surfaceExposure`: "assertions compare only digests, counts, identities and closed reasons; no assertion message, snapshot or reporter output carries an observed body or rendered text". Alternatively, name test-runner output as a log boundary and forbid it explicitly.

### F5 — note — the locator is unbound, and the registry's input class expects an approved locator; this is a missing owner question

Evidence:
- Consent `:17-19`: "the root of the Syzygy checkout that runs the conformance test, resolved from that checkout's own Git metadata at test time".
- Registry `inputClasses`: `repository-locator-mapping` / "opaque-repository-id-plus-normalized-approved-locator".
- AGENTS notes: "The daemon serves only the registered locator (`git-observation.ts` refuses any other `--repo`)".

[Inferred] Any checkout satisfies this: a fork, a PR branch in hosted CI, a stale worktree. None of them is `repository:syzygy` by identity, and the revision is named by fixture code, which is bytes no act binds.

Fix: add a tenth open question, "which checkouts and runners count as `repository:syzygy`, and does a hosted CI run fall inside the consent?", or bind the fixture's revision in the consent.

### F6 — note — open question 2 reopens a choice the ruling already made

Evidence:
- `OWNER-DECISION-PACKET.md:181-182`: "The ruling says "secret-policy extension", which this package reads as a patch to the one policy [Inferred]".
- The recommended arm the owner took verbatim (funnel Q3, line 45) reads: "an extension of the existing secret-classification policy to the observing project's own tree".

So arm A is [Observed] in the adopted text, and the separate-file alternative lies outside the ruling. Of the nine questions:

| Question | Assessment |
|---|---|
| Q1 (who writes the consent's words) | a genuine VIS-4 gate |
| Q2 (extend or separate policy) | not open: the ruling chose extension |
| Q3 (seed file) | genuine; it moves the argument |
| Q4 (does slice 6's code need permission) | genuine. It should also say that the implementation act's line-73 exclusion ("No second repository") governs *running* the test, not only writing it; the three acts do not amend that act |
| Q5 (provenance state) | genuine, though the act itself makes this selection |
| Q6 (pin the spec digest) | genuine |
| Q7 (copy `.18`/`dov.24` fields) | genuine |
| Q8 (refresh the policy's spec pin) | genuine |
| Q9 (names and versions) | only nominally a gate. Note that the record ID `PWB-SELF-CONSENT-2026-09-26` embeds the drafting date, not a statement or act date |

Two gates are missing: F2's (which specification governs the self gate) and F5's (locator).

Fix:
- Restate Q2 as a consequence, not a choice: "extension, as ruled; the Butlers window follows".
- Tighten Q4 as described.
- Add the two missing questions.

### F7 — note — act 3's Butlers consequences are understated: the ledger's sweep 2 misses a line, and the authority chain moves beyond the version

Evidence:
- `IMPACT-LEDGER.md:46-50`: "That leaves 9 policy-version lines in 4 files … `governance-inputs.ts`: 1 line, plus the policy scope anchor".
- A fixed-string sweep for `1.1.0-candidate.1` at `3ee61c7` also finds `governance-inputs.ts:93`: `scopeAnchors: ['polaris-butlers-project-shape-secrets', '1.1.0-candidate.1', 'project:syzygy']`. That is a tenth policy-version line, which the ledger names only in prose.
- More material: act 3 is a superseding approve-policy act over the policy Butlers reads depend on. `governance-inputs.ts:87-95` also hard-codes the Butlers policy authority's `actIdentity: 'PWB-SECRET-CLASSIFICATION-POLICY-APPROVAL-AMENDMENT-2026-09-05'`, `recordingTag`, the `supersession` target, and plausibly `governingActInstant`.

[Inferred] All of these must move in act 3's adoption change, or the Butlers limb fails closed on REQ-005's "act-record identity … wrong but present" cases. The packet (`:137-167` region, "What happens to Butlers") names only the version.

Fix: extend the ledger and the packet section to cover the full Butlers policy-authority tuple, and give the sweep-2 count by fixed string with a stated denominator.

### F8 — note — the selftest leaves several `check()` predicates with no mutant (brief question 6)

Evidence: the predicates run in `check()` against the mutants built in `selftest()` (`:397-574`).

No mutant exists for:
- `typedAuthority.databaseAccess`/`networkAccess` non-empty (`:211-213`; only `writeSurface` is mutated);
- `surfaceExposure.log`/`storedEvaluation`/`walkthroughRecord` (`:220-222`; only `cache` is mutated);
- `resourceLimits` not being an object (`:225-227`);
- an empty `phaseASeedPaths` (`:166-167`);
- four of the five empty-sentence keys, including `inheritedRules` (`:173-176`; only `selfReferenceRule` is mutated);
- a consent with two `Status:` lines.

In addition, every mutant calls the predicate function directly. Nothing proves `check()` still calls `composition_findings` or `packet_findings`, so deleting one of those lines from `check()` would leave `--selftest` green. "The count it prints is the number of checks covered" (packet `:255`) therefore overstates coverage of `check()`.

Fix: add the listed mutants, plus one mutant per `check()` call site, for example by monkeypatching each finder to return a sentinel and asserting that `check()` surfaces it.

### F9 — note — the registry entry reuses Butlers identities that denote a different discovery algorithm and implementation

Evidence:
- Registry `:11`: `"discoveryVersion": "pwb-discovery-v2-candidate.1"`. This is identical to the Butlers entry, but the self discovery has a different seed, no pillars and no roster enumeration.
- `:14`: `"implementationId": "three-surface-poc-core/project-shape-observer"`, `"implementationVersion": "1.0.0"`, beside `:34`: `"implementation": "none yet"`.

PWB-REQ-001 binds "source-discovery version and observer/parser version as deterministic evaluation inputs". Sharing the discovery version makes two different algorithms indistinguishable in the evaluation identity.

Fix: give the self discovery its own version identity, and either state that the self observation reuses the existing observer module or leave `implementationId` absent until slice 6 names it.

### F10 — note — `selfReferenceRule` is directionally right but leaves the file/copy distinction and part of the population implicit (brief question 3)

Evidence: policy patch line 31: "this policy, every registry entry, consent record and act record in this repository are observed text under this scope and never an authority input to the same evaluation; authority inputs are read only through the governance-inputs path".

The same file is both observed text and an authority input. The rule means the Git-blob copy at the fixture revision, but it does not say so. The enumeration also omits the digest-carrying manifests, the owner packets and `ACCEPTANCE-ACT-RECORD.md`, unless "act record" is read to cover it. The rule lives only in the policy; the registry entry has no counterpart. The real risk the ledger found (sweep 6: `PWB_AUTHORITY_EXPECTATIONS_BY_PROJECT` keyed by observing project) would make the self pair resolve the Butlers authorities. That risk is correctly disclosed as [Inferred], but no drafted artifact forbids it.

Fix:
- Reword the rule to: "no object read as an observed Git blob under this scope — including any policy, registry entry, consent, act record, manifest, packet or the acceptance record — is an authority input; authority for this pair is evaluated only for the pair `(project:syzygy, repository:syzygy)`, never inherited from another pair".
- Mirror the rule in the registry entry.

### F11 — note — the composition sweep sees only patches

Evidence: `composition_findings` (`:275-286`) reads only `*/proposed/*.patch` `+++ b/` targets. Another package that drafts a whole file for either install path, the way this package does, would not be detected. `new_target_findings` catches that only after installation.

Fix: also compare the basenames of every sibling's `proposed/` population against the two install targets.

## Answers to the brief's seven questions, in short

1. Nothing wider is permitted in intent. However, the population is not closed (F3) and "never logged" is not bounded (F4).
2. Butlers rules are byte-identical, and the builder checks that. `inheritedRules` has the signed-grammar gap (F2).
3. `selfReferenceRule` is not enough on its own terms (F10).
4. Yes: no words are drafted into the owner's mouth, and a check backs that.
5. The landing-order table is correct against the tree for the five spec packages and `.18`. The Butlers consequences are understated (F7), and the separate-adoption order cannot be executed with the shipped tooling (F1).
6. The mutants are distinct, but several predicates and every `check()` call site have none (F8).
7. The [Observed] sweeps re-derive at their stated base, except IMPACT-LEDGER:134 (F1) and sweep 2's population (F7).

No rule 1–10 violation in the tooling registration. Rule 5/8 applies to F2, rule 6 to F1 and F8, and rule 9 to F7.

Verdict: REVISE
