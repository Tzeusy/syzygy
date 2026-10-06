Title: R-POLARIS-DOSSIER-S3-GATES-2
Reviewed commit: ec0a676b0918e820f03e6da76e950fe3a43abd94
Verdict: REVISE

Scope: PR #379, the repair of R-POLARIS-DOSSIER-S3-GATES-1 (REVISE over 8df5be2a). It covers `reverifyPinnedRevision`, the governed predicate, the recorded clone, the brief's live label, `consentAbsenceFor` / `notInForceRecords`, and the rule-6 record `docs/evidence/polaris-dossier-s3r-reverify-mutants-2026-10-07.json`. Governing text: REQ-polaris-generation-033, in openspec/changes/polaris-dossier-local-agent-mode/specs/polaris-generation/spec.md. The sentences used are at line 11 (governed predicate; "its withdrawal SHALL refuse further steps of any run that relies on it"), line 13 (pinned-revision re-verification and the read rules), line 25 (re-derive or label Inferred) and line 399 (start gates pass before any object is read for a check). Paths below are relative to the repository root.

Verification, in a scratch worktree at ec0a676b (`npm ci`, `tsc -b packages/polaris-dossier` clean):
- `vitest run packages/polaris-dossier packages/polaris-generation-consent`: 15 files, 560 tests passed, 0 failed. [Observed]
- I added probe tests to the scratch worktree only, as a copy of start-gates.test.ts with three extra cases, and never committed them. Results are under findings 1, 4 and 6. [Observed]
- Mutant record: the subject commit 0fce6f85 is an ancestor of ec0a676b, and the only commit between them is the evidence commit. All 6 recorded subject files hash to their recorded sha256 at ec0a676b (6 same, 0 differ). Each of the 19 entries' `old` fragment occurs exactly once in its file. I re-applied G3, G6, L3 and K1 at ec0a676b. All four were killed, with 2, 1, 2 and 1 failing tests, which equals the recorded `failedTests`. [Observed]

## Round-1 findings: confirmed or refuted

1. (note) [Observed] Round-1 finding 1 (blocking) is repaired.
   - The guard now lists the pinned tree from the recorded clone through the re-hashing reader. It recomputes `governedSubject` from the live project input and refuses `governed-changed` on any mismatch. It requires a live statement whenever `statementRequired`, whatever the record says (packages/polaris-dossier/src/reverify.ts:103-128).
   - Route (a), the pin moved from A to C, now refuses `['governed-changed','statement']`. With a statement in force it refuses `['governed-changed','statement-changed']` (start-gates.test.ts:467-477).
   - Route (b), the record downgraded, refuses both before and after withdrawal (start-gates.test.ts:480-486).
   - A drawer recorded after start refuses (start-gates.test.ts:488-491).
   - Mutants G1, G2, G4 and G5 remove each part of this, and each is killed.
   - One residual route remains, through a field the repair still takes from run.json; see finding 6.

2. (note) [Observed] Round-1 finding 2 (revise) is repaired for S3 and S5. The guard returns `revision.label` and `revision.consentRecord` from the live consent (reverify.ts:130-136), and the brief renders that label (brief.ts:71 via `revisionLabel`, brief.ts:210). A forged label and consent record in run.json are ignored, and a relabelled consent shows its new label (start-gates.test.ts:390-398). Mutants L1–L3 are killed. A pin moved between two non-governed consented revisions still passes and shows the new revision's live label (start-gates.test.ts:493-498). This is the bounded harm round 1 accepted once finding 1 was fixed. [Unknown] whether the S6, S8 and S9 beads (syzygy-qkea.7, .9, .10) state that their renders take the label and consent record from the guard result. syzygy-qkea.23's description names the rule, but the PR says only that those branches rebase onto this one.

3. (note) [Observed] Round-1 finding 3 (revise) is repaired. Every refusal carries `{code, reason}` over nine codes (reverify.ts:26-30), and `reasons` is derived from `refusals` (reverify.ts:71-72, tested at start-gates.test.ts:436). C1 is killed. The brief forwards `refusals` (brief.ts:194). The brief does not forward the guard's `objectRead` or its disclosures; see finding 8.

## Attack on the new guard

4. (note) [Observed] The recorded clone path cannot be used to make the recomputed kind match a false recorded kind, short of a SHA-1 collision.
   - `run.json`'s `subject.clone.path` is agent-writable. Its only validation is that it is absolute and normalised (run-record.ts:149-150).
   - Every object, though, is reached by identifier from the pinned commit and re-hashed (git-object-reader.ts:308-312). Alternates are detected and never followed (git-object-reader.ts:287-288, 324). So any store yields the tree that the consented commit identifier fixes, or a refusal.
   - Probe: I pointed the path at a fresh clone of the same origin checked out at another commit. It passed with the same decision. I pointed it at an empty `.git` directory, and it refused `listing` with "… is in neither a loose object nor a pack of this clone".
   - Residual [Inferred]: the path may name a non-consented repository's store, for example another checkout on the host. The reader then opens that store's pack indexes and inflates whatever objects the lookup or an ofs-delta chain reaches before it re-hashes them. No such byte reaches a decision or an output, but it is a read of an unconsented store. Consider refusing a recorded path whose real path differs from the one recorded, or whose `.git` lies inside the state root. Mainly, disclose that the clone location is Inferred and is chosen by whoever last wrote run.json (the module comment says this at run-record.ts:21-24; the guard's disclosure does not).

5. (note) [Observed] No object is read before the consent, registry and policy gates pass. The early return at reverify.ts:101 precedes the reader at :105, and G6 is killed. However, the per-project statement gate is decided only after the listing, by construction, because whether a statement is needed depends on the listing. A guard for a governed run whose statement was withdrawn therefore reads the commit and its trees, though no blob, before it refuses (probe and start-gates.test.ts:472: `opened` is `[C]` on a refusing run). This matches init's order (start-gates.test.ts:280-282, "after listing the pinned tree"). [Inferred] It is consistent with spec line 399, which names the start gates (consent, registry, policy: line 13 and the scenario at line 43) as what must pass before a read for a check. A tree listing to decide the predicate is not a check's content read. Still, spec line 13 requires every object to be "classified and screened … before its content is used in a check", and tree entries are used here unscreened. Round 1 did not raise this, and it predates the PR (init did the same). Record it as a disclosed property rather than a defect.

6. (revise) [Observed] A run whose statement is withdrawn can be rebound to another in-force statement by editing two run.json fields, and the guard's own disclosure says this cannot happen.
   - The guard chooses the statement with `providerStatementGate(…, declared.agentProvider, now)` (reverify.ts:120), and `declared.agentProvider` is read from run.json.
   - Probe: init a governed run at B relying on `STATEMENT-REDIS-ANTHROPIC@1`. Edit run.json to `declared.agentProvider: "openai"` and `subject.providerStatement: "STATEMENT-REDIS-OPENAI@1"`. Withdraw the Anthropic statement, with an OpenAI statement for the same repository in force. The result is `{"ok":true,"providerStatement":"STATEMENT-REDIS-OPENAI@1"}`. The agent sessions are still the operator's Anthropic tool. 033: "its withdrawal SHALL refuse further steps of any run that relies on it."
   - The operator's provider is a declaration, not re-derivable, so spec line 25 allows it to be shown as Inferred ("the citation of a per-project statement"). The mechanism cannot be fully closed under the stated threat model, and it needs a second owner act (another provider's statement for the same repository) to exploit.
   - What is wrong at this commit is the claim. The guard's disclosure says "whether that commit is consented, whether the subject is governed and which statement covers it were decided again at this step from the records in force now" (reverify.ts:66), and the module comment says "nothing the guard decides rests on what it says beyond which revision, repository and clone to look at" (reverify.ts:13-14). Both are false for the provider and therefore for the statement.
   - Repair: name the declared provider (and the statement citation it selects) as read from the run record, and so Inferred, in the disclosure and the comment. Add the probe above as a test that pins the disclosed behaviour, or make it refuse if a mechanism is chosen. One option: refuse when the run record's provider differs from the provider named in `brief.json`, once one exists. That file is also within reach, so it raises the edit count rather than closing the route.
   - Coordinate with #377, which changes `providerStatementGate`'s arguments at this same line (PR body).

7. (note) [Observed] No label shown by S3 or S5 comes from run.json where a live record exists, apart from finding 6's provider.
   - Brief: it shows the repository URL and id from run.json (brief.ts:70). The `consent-ids` check binds that URL to exactly the recorded id under the live consent, so the shown pair is live-equivalent. The label is live. The governed kind and the statement are not rendered.
   - `status` still shows the recorded subject, including `pinnedRevision.label`, under its top-level Inferred label, which is correct.

## Governed predicate

8. (note) [Observed] The stricter predicate gives no false refusal on ordinary trees, gives fail-closed over-counts, and leaves some gaps. The predicate is NFKC, then `toUpperCase().toLowerCase()`, then trailing `[. ]+` stripped per segment (governed.ts:34). I probed it directly over the built `dist/governed.js`.
   - Ordinary paths stay non-governed: `src/server.c`, `docs/OpenSpec.md`, `tests/openspec_test.c`, `deps/openspec-lite/x.c`, `.syzygyrc`, `syzygy/x` and `.github/workflows/ci.yml`. [Observed]
   - Over-counts, which fail closed by requiring a statement: any entry whose segment is `openspec` counts, a file as much as a directory, at any depth. `bin/openspec`, `node_modules/openspec/index.js` (a vendored package of that name) and a file `docs/.syzygy` all read as governed. [Inferred] None is expected in an ordinary C repository such as the redis target. A JavaScript repository that vendors or ships an `openspec` package would need a statement, which is safe but surprising. The disclosure should say "an entry named", not "under an openspec/ directory" (governed.ts:40-41 reasons).
   - Folded correctly: `OPENSPEC`, `openſpec`, fullwidth `ｏpenspec`, fullwidth-dot `．syzygy`, `openspec.`, `openspec . `, `openspec` + U+00A0, and `.syzygy` + U+3000 (NFKC maps both to a space). [Observed]
   - Gaps, still non-governed: default-ignorable code points inside the segment (U+200C, U+200D, U+200B, U+FEFF, U+00AD). Git's `core.protectHFS` treats several of these as ignorable on HFS+. Also a trailing tab, the NTFS stream form `openspec::$INDEX_ALLOCATION`, and the 8.3 short name `OPENSP~1`. [Inferred] These matter only for a tree built to look non-governed while a case-insensitive or ignorable-folding filesystem would resolve the segment to `openspec` or `.syzygy`. The project the statement protects has no motive to hide its own governance tree, so this is a disclosure item. The comment's "never less strict than a root-only, exact-case match" remains true.
   - P1 and P2 kill the fold and the strip. No mutant or test covers an ignorable code point.

9. (note) [Observed] Over-refusal on a better-known subject. A run started `unstated` (project input silent, statement in force) refuses `governed-changed` once a project input is admitted stating no drawer and the tree is non-governed (probe: `["governed-changed"]`). This is fail-closed and arguably right, since the run's recorded basis changed, but the reason text reads as an alarm for a change that only removed a requirement. Consider a distinct code, or say in the reason that the run must be re-initialised.

## Other

10. (note) [Observed] Docstrings are stale after the repair.
   - brief.ts:20-21 still says the brief "reads no object of the subject". It now lists the pinned tree's commit and trees through the guard (brief.ts:193). The `renderBrief` doc ("everything in it … comes from the run record and the doctrine file", brief.ts:57) no longer holds for the label.
   - The brief refusal at brief.ts:194 forwards the guard's `refusals` but not its `objectRead` or its disclosures. A `listing` refusal therefore loses its structured object-read detail in the brief's machine form. S9's renders should forward both.

11. (note) [Observed] The consent-absence reasons (round-1 note 4) are reporting only and grant nothing. `consentAbsenceFor` is consulted only after `repositoryIdsFor` returned no id (reverify.ts:91, init.ts:87, preflight.ts:41). Five literal-string tests cover it (digest-bound-act.test.ts, `consentAbsenceFor`), and K1–K3 are killed.
   - Its records are re-read separately from `repositoryIdsFor`, so a record changed between the two reads can produce a reason such as "… is in force" beside an empty id list. That fails closed, but the text is self-contradictory. [Inferred]
   - A withdrawal in an undefined form lands under "could not be read (invalid-records)", which is tested at start-gates.test.ts:440-441.

12. (note) [Observed] The rule-6 record is sound.
   - Each mutant stores `id`, `file`, `old`, `new`, `tests`, `outcome`, `failedTests`, `totalTests` and a `note`.
   - The record names the subject commit, the per-file sha256, the runner path and sha256, and the run instant. The no-op control survived.
   - The record has one `project` field, `@syzygy/polaris-dossier`, but K1–K3 ran the consent package's tests (58 and 36 tests). Either the runner resolved the project per file, or the field misdescribes the command. My re-run of K1 by file path was killed with 1 failure, as recorded. [Inferred: the field is descriptive only]
   - No mutant covers `declared.agentProvider` (finding 6), the `listing` refusal arm, or the init realpath of the clone.

13. (note) [Observed] The tests use hard-coded literals for every expected reason, code, label, consent record and disclosure, for example start-gates.test.ts:361-365, 413, 449, 456, 474 and the status.test.ts clone cases. Commits come from the fixture repository. No expected value is imported from the module under test. brief.test.ts imports `NO_PROVIDER_STATEMENTS`, a fixture input rather than an expected value, and its fixture reader stands in for a clone (brief.test.ts:72).
