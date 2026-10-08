# Review — PR 403 project-documentation screening, round 2
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: 189225c2c75da576777a3171270ec9409eae5cae
Reviewer: fresh-context

## Scope and method

- Subject: PR #403 at head `189225c2`. The merge base with `origin/main` is `56c6c98c`. Round 2 adds three commits on top of round 1's `3e121a71`:
  - `6acea701` retains the round-1 raw;
  - `fe4bb4ca` holds the code fix;
  - `189225c2` holds only the mutant record.
- [Observed] `git diff --name-status 56c6c98 189225c2` lists 24 paths. None is under `.syzygy/` or `openspec/`. The only `-RAW.md` is the added `docs/reviews/R-PR403-SCREEN-DOCS-1-RAW.md`.
- Governing text read at head:
  - the policy's `publicSourceScope`: `prerequisite`, `consentRule`, `rawBodyHandling`, `activeContent`, `accessBoundary` and `ingestBoundaries`;
  - the RFC5-14 class act record (`Act instant: 2026-10-07T17:48:25Z`);
  - the v2 policy act and the Redis observation act, as cited by round 1;
  - the Redis provider statement as `gate-sources.ts` parses it.
- Runs in a scratch worktree at `189225c2`, after `npm ci`. The worktree was removed afterwards.
  - The six PR test files pass, 387/387: class-gate 9, core classification 177, app screening 28, review 43, screen 90, render 40. [Observed]
  - Three throwaway probe tests, quoted below, were deleted with the worktree.
  - I re-ran mutant G5 myself. It was killed: 3 of 43 review tests failed. [Observed]
  - `python3 scripts/check_governance.py` reports "32 OK, 21 WARN, 0 FAIL (53 checks)". `check_docs_review_campaign_partition.py --check docs/README.md`, run from the worktree root, reports "partition PASS: denominator=379; assigned=379; … unmatched=0; overlaps=0". [Observed]

## Acceptance criteria

### 1. F1 and F2 fixed: met

F1 was checked with probes against the real checkout records at `now = 2026-10-08T12:00Z`. [Observed]

- `createPackageGateSources({root}).providerStatements.statementsFor('redis-redis')` returns exactly one record, `AGENT-PROVIDER-redis-redis-anthropic@0.1.0-candidate.1`. Its classes are `["governance-text","code-structure","code-content","evidence-content","derived-composites"]` and its act is `AGENT-PROVIDER-REDIS-ANTHROPIC-2026-10-07`. `statementContentClasses(…,'claude-code','anthropic',NOW)` returns that same list.
- `loadDossierScreen(ROOT, NOW)` with `unconsentedClass` gives these results:

  | Path | Class | Gate result (statement classes and `null`) |
  |---|---|---|
  | `README.md` | `project-documentation` | `project-documentation`, so withheld |
  | `docs/index.md` | `project-documentation` | `project-documentation`, so withheld |
  | `LICENSE.txt` | `project-documentation` | `project-documentation`, so withheld |
  | `licenses/MIT.txt` | `project-documentation` | `project-documentation`, so withheld |
  | `src/server.c` | `code-content` | `undefined`, so passes |
  | `tests/unit/type/list.tcl` | `code-content` | `undefined`, so passes |
  | `redis.conf` | `unknown-extraction-class` | `unclassified` |

- So the round-1 failing input, a Redis draft citing `README.md` lines 1–5, now yields a packet span with `outcome: 'class-not-consented'` and `missingClass: 'project-documentation'`, and no `text`. `review.test.ts` asserts exactly this with the real Redis class list (lines 604–612). Mutant G5, which removes the check, fails it. [Observed]

F2 was checked with probes through the app's own `checkoutPolicyActPort(root, () => now)`. [Observed]

- On the real tree, `classActInForce` is `false` at the act instant minus 1 s and `true` at plus 1 s. The dossier's `readClassActState` agrees: `absent` before the instant.
- I copied the real `.syzygy/` tree and added a decisions file reading "Withdraws `RFC5-PROJECT-DOCUMENTATION-AMEND-2026-10-07`." `classActInForce` went from `true` to `false`.
- The new parity case (`screen.test.ts`, "decides the class prerequisite as the app does from the same records at now") covers five cases with both screens: in force, absent, dated after now, withdrawn, and binding other module bytes.

### 2. Gate coverage of every agent-bound artifact: met for Syzygy-read bytes, with exception E1

Consumers of the screen:
- [Observed] `grep -rln -F` for `screenPath|screenBody|loadDossierScreen|DossierScreen` over `apps/`, `packages/` and `scripts/` (excluding `node_modules` and `dist`) finds 16 files. Five of them are non-test production modules: `check.ts`, `close.ts`, `render.ts`, `review.ts` and the app's `public-source-screening.ts`. `index.ts` re-exports, and `class-gate.ts` mentions them only in its doc comment.
- [Observed] `readScreenedRepoCorpus` and `loadPublicSourceScreen` have no caller outside their own test and `screen.test.ts`. The app screen therefore hands nothing to any agent or provider today, as its header says.
- [Observed] The only importer of `@syzygy/polaris-dossier` outside the package is `apps/syzygy/src/main.ts:253`, which calls `runDossierCli`.

Agent-bound artifacts:

| Artifact | Carries Syzygy-read repository bytes? | Gated? |
|---|---|---|
| Authoring brief (`brief.ts`) | No. Its docstring at line 21 says "It reads no blob of the subject". The file imports no screen and no blob reader. [Observed] | n/a |
| Inventory brief and prompt (`session-handover.ts`, `inventory.ts`) | No. `inventory.ts` is not among the blob-reading modules, and the prompt is fixed text. [Observed] | n/a |
| Fidelity packet `spans` (`review.ts:198-211`) | Yes | Yes. Probe and G5–G7. [Observed] |
| Rendered site, carried whole by the design packet (`render.ts:260-268` and onward; `review.ts:281`) | Yes | Yes. Withheld paths are dropped from `admitted`, so from source pages, quotations and citation source ids. `render.test.ts` asserts that no page contains the withheld sentence. G8–G12. [Observed] |
| Check findings returned to the authoring session (`check.ts`) | No. Findings carry fixed texts, line counts and byte ranges, with no body text (lines 598–634). [Observed] | n/a |
| `close.ts` | No blob read. [Observed: no blob-reader import] | n/a |
| Fidelity packet `draft` and `inventory` documents | Agent-authored text, which can include verbatim quotations of a withheld body | No. See E1 |

The population is 4 dossier production consumers and 1 app module with 0 production callers, giving 6 agent-bound artifacts. Five of the six are clear. The sixth, the draft and inventory carried in the fidelity packet, is E1.

### 3. A withheld span is typed and named: met

- Fidelity packet: the span variant `outcome: 'class-not-consented'` with `missingClass`, in the type at `review.ts:77` and the value at `review.ts:204`. It is counted under `excluded` in the report.
- Site:
  - the block is `unknown` / `excluded-content`, and its basis names the class and whether a statement exists;
  - the discovery row reads "admitted by screening as project-documentation; withheld from every agent-bound artifact: … (class-not-consented)";
  - the source row is kept with `exclusion.reason: 'body-not-retained-for-generation'`.
- `render.test.ts` asserts every one of these. [Observed]
- See N3 on the source row's reason.

### 4. Local quotation verification is not egress: met by the clauses below

- `publicSourceScope.purpose`: "read their Git snapshot objects, screen them under this policy and classify them into RFC5-14 classes".
- `ingestBoundaries`: `["observation","model","run-directory","human-html"]`.
- `rawBodyHandling`: `"storage": "run-directory-only"`, `"machineResponse": "never"`, `"externalEgress": "classified-content-under-an-effective-egress-consent"`, and the rule "storage is permitted only inside a run directory …; external egress only for content this scope classifies and only under a separate egress consent for the pair".
- `prerequisite.consentRule` restricts "egress" only: "a consent record that does not list project-documentation does not permit its egress".

[Inferred] No clause says in words that in-process verification is not egress. Reading and classifying is the scope's stated purpose, though, and the consent restriction is phrased over egress and "external egress". Verification inside the observation and model boundaries, with byte ranges and no body stored in the run directory, is therefore not egress under these clauses.

What leaves to the authoring session is the verification outcome: the fixed `QUOTE_FAILURE` texts in `check.ts:619`. That is one bit per quotation the agent itself wrote from a clone it already reads. [Inferred] It is not a carriage of the body.

### 5. Round-1 criteria 1–7 still hold: met

- [Observed] `git diff --stat 3e121a71 189225c2` does not touch `public-source-classification.ts` or its test, so the round-1 probes of criteria 1–2 stand.
- `screenBody` is unchanged in both screens (criterion 3).
- Criterion 4 is now met in the app (above).
- The parity test now also compares `contentClass`.
- Criterion 7 is re-checked below.

### 6. The mutant record covers the gate, temporal and withdrawal: met

- [Observed] `docs/evidence/project-documentation-screen-mutants-2026-10-08.json` reports 90 of 90 killed at subject `fe4bb4ca34e18038b8387f074b4951aa6e035607`, with `old`/`new` per mutant and per-file sha256.
- I recomputed the sha256 of seven subject files at head: `class-gate.ts`, `review.ts`, `render.ts`, `screen.ts`, the app's `public-source-screening.ts`, `polaris-generation-consent/src/package-reader.ts` and `review.test.ts`. All seven equal the record. [Observed]
- Coverage by mutant:
  - the gate: G1–G4 in `class-gate.ts`, G5–G7 in the fidelity packet, G8–G12 in the site, G13–G15 for statement classes carried through reverify, `gate-sources` and `openRun`;
  - temporal: C2, the class act instant after `now`, and A2, the app clock pinned to `MAX_SAFE_INTEGER`;
  - withdrawal: C1, the withdrawal sweep removed;
  - refused or absent states: A3 and A4.

### 7. Governed and act-bound bytes untouched; round-1 raw verbatim: met

- [Observed] There are no `.syzygy/**` or `openspec/**` paths in the diff.
- [Observed] `cmp docs/reviews/R-PR403-SCREEN-DOCS-1-RAW.md <scratchpad>/R-PR403-SCREEN-DOCS-1-RAW.md` produced no output and exited 0, so the files are byte-identical.
- No other `-RAW.md` was added or modified.

## Findings

### E1 — Low — the fidelity packet's `draft` carries a withheld project-documentation quotation verbatim

- Location: `packages/polaris-dossier/src/review.ts:152-153,219`, which carries `draft.document` as the draft minus `discovery`. The gate's own population statement is at `packages/polaris-dossier/src/class-gate.ts:13-17`.
- Clause: the policy's `prerequisite.consentRule`, "a consent record that does not list project-documentation does not permit its egress"; also `class-gate.ts:8-11`, "a span enters the fidelity packet … only when the class … is listed".
- Failing input [Observed in a probe over the `review.test.ts` fixture]:
  - Draft block `p2` reads `The project states: "Snapshots are written periodically."` and cites `docs/notes.txt` line 2.
  - Run it under the real Redis class list, which lacks `project-documentation`. The span is correctly `class-not-consented` with no `text`.
  - Yet `packet.json` contains `Snapshots are written periodically.` once, under the top-level key `draft`. The same holds for a non-governed run.
  - `check` has already verified this quotation byte-for-byte against the withheld body, so the review session receives exact project-documentation bytes. The render path treats such a quotation as Syzygy's located bytes and withholds it.
- Why Low and not blocking:
  - [Inferred] The draft is authored by the agent, which the provider statement describes as reading the clone itself. The criterion governs "Syzygy-selected repository bytes", and the draft is not Syzygy-selected.
  - [Inferred] This carriage predates the PR. Before it, a README quotation sat in the draft just the same, and the class then was `unknown-extraction-class`.
  - Round 1 already left open, as an owner question, whether a reviewer packet is Syzygy's egress.
- Repair, either of:
  - (a) state this residual in `class-gate.ts`'s population paragraph ("the packet's draft and inventory are agent-authored and may quote a withheld body verbatim; the gate covers Syzygy-read spans only") and in the review packet disclosures;
  - (b) replace verified quotations of class-withheld spans in `draftView` with a withheld marker, as `render.ts` does.

  (a) suffices for this PR.

### N2 — Note (pre-existing round-1 F3, still present) — the app loader refuses the real records

- Location: `apps/three-surface-poc/src/polaris-generation/public-source-screening.ts:51-53,97-104`.
- [Observed] `loadPublicSourceScreen(checkoutPolicyActPort(ROOT, () => now))` at head returns "Corpus read refused: public-source-policy: policy bytes do not hash to the act argument". The loader still reads only the superseded v1 act record.
- So the app's new prerequisite and `contentClass` run only against fixtures (the parity root writes a v1-form policy act). It fails closed, and [Observed] the app reader has no production caller.

### N3 — Note — the generation source row for a class-withheld body names no class

- Location: `packages/polaris-dossier/src/render.ts:286-288`.
- A withheld body's source row reuses the closed reason `body-not-retained-for-generation`, a member of `GENERATION_EXCLUSION_REASONS`. Only the discovery row and the block basis name the class.
- This satisfies criterion 3, since the class is named on the page, but a reader of the sources table alone sees a reason that does not say why. The comment at lines 285–286 says so.

### N4 — Note — the rendered human view also withholds project-documentation quotations

- `rawBodyHandling.rendering` permits "quoted-context-encoded-spans-in-editorial-draft" locally. Because the same site is the design packet, `render.ts` withholds the quotations from the human view too.
- This fails closed and is not a defect. It means a Redis dossier shows no README quotation to its human reader until a statement lists the class.

## Required to clear

- Nothing blocking.
- Recommended: E1 (a), stating the residual.
- N2–N4 are recorded for the next pass.
