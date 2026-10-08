# Review — PR 403 project-documentation screening
Verdict: REVISE
Reviewed commit: 3e121a7130ee9694373f045a07c22db35458cb90
Reviewer: fresh-context

## Scope and method

- Subject: PR #403, head `3e121a7`, base `56c6c98`. Its commits are `be1e0f3d` (the code) and `3e121a7` (the mutant evidence record only). [Observed] `git diff --stat be1e0f3d 3e121a7` shows that one JSON file and nothing else.
- Changed files (8): the two screens, `polaris-generation-core/src/{public-source-classification.ts, .test.ts, index.ts}`, the two screen test files and `docs/evidence/project-documentation-screen-mutants-2026-10-08.json`. [Observed] No path under `.syzygy/**` or `openspec/**` and no `-RAW.md` is in the list (`gh pr diff 403 --name-only`).
- Governing text was read at the head commit: the policy's `publicSourceScope`, and the act records for policy v1 and v2, RFC5-14 and the Redis observation consent. To answer criterion 5 I also read `DOSSIER-LOCAL-AGENT-REDIS-AGENT-ANTHROPIC-ACT.md` and its artifact `.../dossier-local-agent-acts/instances/redis/AGENT-PROVIDER-STATEMENT-ANTHROPIC.md`, lines 20–60.
- Runs, in a scratch worktree at `3e121a7` after `npm ci`:
  - The three PR test files pass, 289/289 (177 core, 36 app, 76 dossier). [Observed]
  - Two throwaway probe tests ran against the real checkout records; they are quoted below and were deleted afterwards.
  - The sha256 of each pinned rule text, computed with Python from the policy at head, equals the module's `IMPLEMENTED_TEXTS`, all six. [Observed]
  - The policy file hashes to `98a87f81…`, the v2 act argument. The RFC-0005 module hashes to `a69a606c…`, the RFC5-14 act argument. [Observed]

## Findings

### F1 — High — the dossier's review packet now carries project-documentation text to a provider that no consent lists it for

- Location: `packages/polaris-dossier/src/screen.ts:65` together with its consumer `packages/polaris-dossier/src/review.ts:177-186,196-197`.
- Clauses violated:
  - The policy's `publicSourceScope.prerequisite.consentRule`: "a consent record that does not list project-documentation does not permit its egress, and no consent granted before the class existed is read as covering it (RFC5-14 as amended); this policy confers no consent".
  - `publicSourceScope.rawBodyHandling.rule`: "external egress only for content this scope classifies and only under a separate egress consent for the pair".
  - The v2 act, "What this act does not authorize": "a consent that does not list `project-documentation` still permits no egress of it (RFC5-14)".
  - The RFC5-14 act, Effect: "No existing consent gains the class, and no read, egress or implementation is authorized."
- What the code does:
  - [Observed] `review.ts` uses the dossier screen to decide which cited spans enter `packet.json` with `outcome: 'admitted'` and their `text`.
  - [Observed] The fidelity reviewer prompt (`review.ts:81`) tells the operator's agent session to "Judge the draft only from this packet … You are given nothing else and must use nothing else."
  - Before this PR only code-content bodies could be admitted. After it, README, docs and licenses bodies are admitted whenever the class act is in force. [Observed] `loadDossierScreen(REAL_ROOT, 2026-10-08)` returns `ok`, `projectDocumentation=true`.
- Why no consent covers it:
  - [Observed] The only Redis provider record lists "`governance-text`, `code-structure`, `code-content`, `evidence-content`, `derived-composites`" and not `project-documentation`.
  - [Observed] Its act predates the class.
  - [Observed] `grep -rn project-documentation .syzygy/governance/decisions` finds no consent or egress record that lists the class. The hits are the two acts, the sitting direction, the 2026-10-03 owner answers and the acceptance record.
  - [Observed] The provider gate checks only `contentClasses.length > 0` (`gate-sources.ts:293`, `preflight.ts:50`).
  - [Observed] The screen exposes admitted/excluded and no per-blob class, so nothing downstream can gate by class.
- Failing input: a Redis run whose draft cites `README.md` lines 1–5. `review-packet` writes those lines into `packet.json` as an admitted span. The review session, an Anthropic-backed Claude Code session, receives them under a consent that does not list the class.
- [Inferred] The provider statement says the agent "reads the clone without restriction", so the same bytes may reach the provider anyway through the authoring session. That is the agent's own read, though. The packet is content Syzygy selected, screened and handed over, which is what the consentRule governs. Whether a packet handed to a reviewer session counts as Syzygy's egress is an owner question that no act in scope answers.
- Fix:
  - Have the screen return the class it admitted each path under.
  - Admit a span into any agent-bound artifact only when that class is listed by the in-force provider statement or egress record for the pair.
  - Otherwise, ask the owner for a ruling or a statement successor that lists `project-documentation` before this ships.

### F2 — Medium — the any-repo reader's class prerequisite ignores `now` and withdrawal

- Location: `apps/three-surface-poc/src/polaris-generation/public-source-screening.ts:78-84,125`.
- Criterion 4: the class applies only while the acts it depends on are in force at `now`.
- Clause: `publicSourceScope.prerequisite.rule`: "the project-documentation rule classifies a blob only while the in-force RFC-0005 vocabulary lists project-documentation; a consumer that cannot confirm that treats every blob the rule names as indeterminate".
- What the code does: `classActConfirmed` checks only the record's form and digest. Its own docstring says it "neither sweeps the decisions tree for a withdrawal nor compares the act's instant with the clock".
- Failing inputs, observed in a probe through `PublicSourcePolicyActPort`:
  - Take the real class act record with Date, identity and Act instant rewritten to 2099-01-01. The result is `projectDocumentation=true`, and `screenPath('README.md')` is admitted.
  - A decisions file revoking the act is never read by this loader, so it cannot remove the class. [Inferred from the code; the port has no such input.]
- The dossier's `readClassActState` handles both correctly: it compares the instant with `now` and refuses on a naming file. That makes the two screens disagree on the same records.
- The parity test does not catch this. It feeds the dossier a boolean and the app a record that is already in force (`screen.test.ts` around lines 172 and 239).
- [Observed] The failure is currently masked. The app reader refuses the whole screen at head for an unrelated, pre-existing reason (F3), so it fails closed today. It turns into a live gap once F3 is repaired.
- Fix: decide the app's prerequisite with `readClassActState({ root, now })` or an equivalent that sees `now` and withdrawals, and add a parity case with a future-dated class act.

### F3 — Low (pre-existing; recorded because it hides F2) — the any-repo reader cannot load the policy now in force

- Location: `public-source-screening.ts:42-43,103-105`.
- [Observed] The probe `loadPublicSourceScreen(checkoutPolicyActPort(ROOT))` at head returned `Corpus read refused: public-source-policy: policy bytes do not hash to the act argument`.
- Cause: the loader reads the superseded v1 record. Its argument is `d42defca…`, and its `ACT_IDENTITY` regex does not match the v2 identity `…-SCOPE-V2-APPROVAL-…`. The v2 act says it "supersedes, for the `approve-policy` role only, the 2026-10-07 act recorded at `…PUBLIC-SOURCE-SCOPE-ACT.md`".
- Consequence: none of this PR's app-side code has run against the real records. Every app test builds a synthetic `actRecord(sha(policy))`. This is not introduced by the PR, but it means app-side criterion 4 is verified only by fixtures.

### F4 — Note — fold-only matching admits Unicode look-alikes of withheld words

- Location: `public-source-classification.ts`, `fold` and `hasExcludedWord`.
- Clause: "Matching compares a copy of the path with its ASCII letters A-Z folded to a-z and nothing else folded, normalized or decoded".
- [Observed in a probe] These paths are admitted as project-documentation:
  - `docs/ｄesign.md` (fullwidth d);
  - `docs/a\tb.md` (tab is not in `docTokenSeparators`);
  - `docs/rfc0001.md` (`rfc0001` is not the word `rfc`).
- This matches the text exactly, so it is not a defect. The policy's own `notMapped` says "The class is decided by these names alone". [Inferred] It is a residual worth stating in the screen's residuals comment, beside the literal-form detector residual. Detectors and the active-content scan still run on these bodies.

## Criteria

1. Path rules and parameters: met for the shared module. [Observed]
   - Every parameter is read from the policy bytes. The rule, the three path-rule texts, the disjointness statement and the prefix note are pinned by sha256 and equal the head policy.
   - Probes agree with the text on all of these cases:
     - `01-readme.md` matches, while `1-`, `001-`, `01_`, `01-01-` and fullwidth digits do not ("exactly the ASCII characters listed in digits");
     - `readme.md.md` and `readme.markdown` do not match ("one suffix");
     - `docs/.md` does not match ("longer than it");
     - `docs/a/design.md`, `docs/design-notes/a.md` and `docs/a.b.design.md` do not match ("no directory name after the first, and no file name without its extension");
     - `docs/requirements.txt`, `docs/requirements-dev.txt` and `docs/sub/CMakeLists.txt` do not match, and `docs/requirements.md` does (".txt" only);
     - `licenses/a/MIT.txt` (three segments) and `licenses/x.rst` do not match;
     - `/README.md`, `README.md/`, `docs//a.md`, `./README.md` and `docs\a.md` match nothing;
     - `docs/x.py` is code-content.
   - The "exactly one" check and "never code-content" are implemented (W1, W2).
2. Fail-closed choices where the text is silent: met. Malformed entries refuse. An entry that is not ASCII-lowercase refuses. A policy whose suffixes overlap `sourceExtensions` refuses. With the prefix non-optional, an unprefixed name matches nothing. A path matched by two rules falls through to code-content or indeterminate.
3. Detectors and active content unchanged: met. `screenBody` is byte-identical in both screens. The app test reads a docs body with a fenced credential and gets `secret-detector-match`, and a licenses body with `<script>` and gets `active-content`. [Observed]
4. Acts in force at `now`: met in the dossier (`readClassActState({root, now})`, `readPolicyActChain({root, now})`). Not met in the app (F2).
5. Act gap:
   - Reading is covered for Redis by the observation consent's Effect: "read-only reads of those commits' Git objects". The v2 policy act and the RFC5-14 act supply the classification. [Observed]
   - For other repositories the any-repo reader still needs each pair's own observation consent through its admission port. [Inferred; not re-verified here]
   - Carrying the newly admitted bodies to the provider through the review packet has no covering act (F1).
6. Tests:
   - Expected values are hard-coded literals: the live-rule `toEqual`, and path tables quoted from the rule text. The policy is read only as input. [Observed]
   - The parity test passes, but it does not cover temporal or withdrawal disagreement (F2).
   - The mutant record has `old`/`new` per mutant, subject commit `be1e0f3d` and per-file sha256. Its 74 of 74 are killed. It covers each path rule (R1–R4, D2–D7, L1–L3) and every parameter and list: P1–P15 over `digitCount`, `digits`, `separator`, `optional` and the ten lists. [Observed]
7. `.syzygy/**`, `openspec/**`, act-bound bytes and `-RAW.md`: untouched. [Observed]

## Required to clear

- F1: gate agent-bound spans by class against the in-force consent, or obtain an owner ruling.
- F2: give the app's prerequisite check `now` and withdrawal handling, with a parity case for it.
- F3 and F4 are not blocking.
