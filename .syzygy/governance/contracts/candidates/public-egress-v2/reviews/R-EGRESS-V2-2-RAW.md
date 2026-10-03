# R-EGRESS-V2-2 — egress record v2 confirmation, round 2
Reviewed commit: d2f9ab90b530c00e4c96d5f1a4e6ccff4c78f5b5
Manifest SHA-256: 6a9e3c94336677ce35759394109f6a3e3ed85f3b315e7b083cf28a0b61de5675
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer: fresh-context governance reviewer. No provider was called and no external repository body was read. Nothing was pushed, commented or edited in tracked files.
Worktree: detached at d2f9ab90, `npm ci` first. A second scratch worktree held origin/main (bf12c5af) with d2f9ab90 merged in (merge commit 141b1f78), for N-6 only. Both were removed.
Paths are relative to `.syzygy/governance/contracts/candidates/` unless they start with `scripts/`, `packages/` or `.github/`.
REC = `public-egress-v2/instances/egress-anthropic/EGRESS-CONSENT-ANTHROPIC.md`; TPL2 = `public-egress-v2/templates/EGRESS-CONSENT-TEMPLATE-V2.md`; TPL1 / REC1 = the `public-repo-admission/` template and record; PKT = `public-egress-v2/OWNER-DECISION-PACKET.md`; SDK = `public-admission-registry-entries/proposed/POLARIS-PROVIDER-ROUTE-ANTHROPIC-AGENT-SDK-CANDIDATE.json`; MSG = `provider-route-messages-api-entry/proposed/POLARIS-PROVIDER-ROUTE-ANTHROPIC-MESSAGES-API-CANDIDATE.json`.

## Digests (rule 3, scripted)

- [Observed] `sha256sum public-egress-v2/PUBLIC-EGRESS-V2-MANIFEST.txt` = 6a9e3c94336677ce35759394109f6a3e3ed85f3b315e7b083cf28a0b61de5675, equal to `--manifest-digest` at the head and on the merge with main.
- [Observed] Python `hashlib.sha256` over REC's bytes = d0b895062f245d58b541c58e75b09e976bf307b52b7ac5c3644feceb64e1a86f, equal to the manifest row and `--digests`.
- [Observed] The dispatch brief gave d0b89506… as the "expected manifest FILE" digest. That value is the record digest (the manifest's row), not the file digest. The head above carries the file digest, as the brief's own words and REVIEW-BRIEF.md:25-27 require.
- [Observed] REC1 hashes to cbae0a84…, equal to the pin at `scripts/record_public_repo_admission_acts.py:79`; v1 bytes are unchanged on the branch.

## Runs (criterion 8)

- [Observed] `build_public_egress_v2.py --check` → "public egress v2: current" rc 0; `--ready` → "ready" rc 0; `--digests`/`--manifest-digest` rc 0 (values above); `--selftest` → "selftest: 22 checks held" rc 0 (the "unknown mode --bogus" stderr line is the selftest's own expected refusal, line 346).
- [Observed] `build_public_repo_admission.py --check` → "public-repo admission instances: current" rc 0.
- [Observed] `record_public_repo_admission_acts.py --selftest` → "35 of 35 predicates held" rc 0.
- [Observed] `python3 scripts/check_governance.py` → "32 OK, 21 WARN, 0 FAIL (53 checks)".
- Rule-6 mutants (each restored with `git checkout`; `--check` current again after):
  - M1 record field: REC `Record version` candidate.1 → candidate.2: `--check` STALE REC rc 1; `--digests` "refusing: stale" rc 1.
  - M2 classification: `scripts/derive_generator_sent_text.mjs:154` `'items[].excerpt': 'target-content'` → `'target-metadata'`: `--check` STALE REC and manifest, rc 1.
  - M3 template, same line count: TPL2 "with no entry in force, no route byte is permitted" → "any route byte is permitted": `--check` STALE before `--write` (rc 1); after `--write`, `--check` "current" rc 0 and `--ready` "ready". See N-3.
  - M4 v1 recorder wiring: `if superseded_by_later_version(...)` in `do_record` disabled: selftest still "35 of 35" rc 0. See N-4.
  - M5 v1 recorder predicate: key `egress-anthropic` → `egress-anthropicX`: selftest "34 of 35", the new predicate FAILs.
  - M6 derive leaf list: drop `topics` from `READER_QUESTION_LEAVES`: exit 2, "readerQuestions[] leaf topics has no class".
  - M7 derive fixture gains an extra reader-question key: the pipeline's own validator stops first (exit 1, "invalid-request"); the leaf check is defence in depth behind it.
- [Observed] node-ci: `.github/workflows/node-ci.yml:91-95` adds both `--check` steps after `npm ci`/build/typecheck, with no `if:` guard. PR run 37143565400 at d2f9ab90 logs "public-repo admission instances: current" and "public egress v2: current" in those steps (output read, not exit code).

## Criterion 1 — round-1 dispositions against the bytes

- **B-1 repaired.** [Observed] REC:163-168 no longer says "the same". Item by item against `requestBytes`:
  - model / effort / ceiling "as each entry pins them": SDK `routeFixedByThisEntry` model claude-opus-5-5, effort high, maxTokensCeiling 64000; MSG identical values. Holds.
  - tools: REC:164-166 "Agent SDK route sends an empty `tools` list and the Messages API route sends no `tools` field" = SDK `"tools": []` / MSG `"tools": "absent: the body has no tools field"`. Holds.
  - thinking: REC:166-168 off vs off-or-exactly-adaptive = SDK `"thinking": "off: …"` / MSG `"profile-set, one of two values only: off … or adaptive (exactly {\"type\":\"adaptive\"})"`. Holds.
  - endpoint: REC:149 `POST /v1/messages?beta=true`, streamed = SDK `endpoint`, `runtimeFixed` "stream: true"; REC:159 no query string, streamed = MSG `endpoint`, `sdkFixed` "stream: true". Holds.
  - Agent SDK additions REC:150-153: system prefix (SDK `runtimeFixed` system[0]), empty system message (messages[1]), `metadata.user_id` with device id, session id and empty `account_uuid`, `cache_control` on generator parts (SDK `generatorBuilt`). Holds, with the omission in N-5.
  - headers: three machine-identifying headers in both closed sets (SDK and MSG `machineFingerprint`). Holds.
  - probe: REC:155-156 vs SDK `probe`; REC:162 "no probe" vs MSG `probe: "none"`. Holds.
  - absent by construction REC:156-157 vs SDK `absentByConstruction` (environment message, billing header, safeguards, any tool). Holds.
  - MSG absences REC:161-162 vs MSG `absentByConstruction` and `runtimeFixed`. Holds.
  - stripping REC:169-171: off by default, owner option (SDK packet O4, MSG packet O2). Holds.
- **B-2 repaired**, with N-1. PKT:11-34 now says in plain words what leaves: excerpts of the two repositories before selection, the reduce call's claims, the metadata, README/guide files under the new class, that the route does not change, and what never leaves. Caps 1,500 / 40 / 40 equal `DEFAULT_DISCOVERY_BUDGET` at `packages/polaris-generation-core/src/discovery.ts:36-37`. The repositories and commit counts (one for psf/requests, four for redis) match `public-repo-admission/instances/{requests,redis}/OBSERVATION-CONSENT.md:25-28`.
- **N-1** accepted as declared: REC:30, PKT:23-27, PKT:45-46.
- **N-2 repaired.** REC:188-191 (from `v2.json` ROUTE_CONTEXT): "the route loads no instruction or memory files, user or project settings, MCP servers, hooks or environment summary (working directory, Git status); a route entry may narrow this and can never override it". This is v1's REC1:120-121 list unchanged, with the "beyond what the registered entry lists" qualifier of round 1 gone.
- **N-3** repaired with B-1 (stream, `cache_control`, `?beta=true`, empty account id, environment message absent).
- **N-4 repaired.** REC:52-57 names subsystem names, blob counts, blob ids and paths; REC:46 names the excerpts.
- **N-5 repaired.** REC:135-139 defines `all`, and labels the discovery-port statement [Inferred].
- **N-6 repaired, re-derived.** [Observed] On origin/main bf12c5af as it stands, main's own `derive_generator_sent_text.mjs --table` exits 1 ("no generate call … invalid-request"), and v1's `--check` raises. On main + d2f9ab90, both `--check`s report current and REC1 still hashes to cbae0a84. So v1's table bytes are unchanged and the fix is required for main. The guard is at `scripts/derive_generator_sent_text.mjs:49-54` (M6).
- **N-7 repaired.** PKT:7-9 no longer gates on #281; PKT:45-46 reconciles the class list; PKT:135 says "rows 2a to 3b"; REVIEW-BRIEF.md:58-61 says retention and route context differ deliberately; REVIEW-BRIEF.md:25-27 head order matches.
- **N-8 repaired.** `scripts/record_public_repo_admission_acts.py:426-442` refuses `egress-anthropic` once `.syzygy/governance/decisions/PUBLIC-EGRESS-V2-ANTHROPIC-ACT.md` exists. [Observed] A direct probe of `do_record` on a scratch tree holding that file returned 1 with "FAILED (nothing written)", and wrote nothing else. Selftest predicate at :636-644 (M5). The packet says the same at PKT:116-120. See N-4.
- **N-9 partly repaired.** See N-3.

## Criteria 2-5 — summary

- Template diff TPL1→TPL2: [Observed] `diff` gives 8 hunks, 13 removed and 60 added lines, equal to `v2.json` `templateDelta`. Each hunk is one of: the title; the discovery excerpt and metadata scope (stages); the derivation command and builder name; the port-row wording; "beyond these fields" (delegation); the new `all` paragraph and per-route section (narrowing plus information); and model-sees-only (delegation). No other widening. The field overrides: PROVIDER (delegation), RETENTION ("runtime"→"route's runtime or library": restatement), ROUTE_CONTEXT (absolute ban kept; "working directory, if it has one" is delegation), ROUTE_TELEMETRY ("no telemetry … is sent; a route that cannot disable them does not start": equal or stronger). The class is added by the builder at `scripts/build_public_egress_v2.py:132`.
- Route neutrality: REC:19 "the one registered … (the Agent SDK entry or the Messages API entry, whichever the adapter registry holds; RFC4-1 admits one)"; REC:143-144 "A route's bytes are permitted only while that route's registry entry is in force; with no entry in force, no route byte is permitted." Neither both routes at once nor a route with no entry is permitted.
- Status: REC:4-5 "Candidate — binds nothing until the owner acts on this record's exact bytes"; REC:37 conditional prospective supersession; PKT:109-120 states both lawful orders and the refused one. Nothing is labelled accepted (VIS-4).
- Instruction text: `scripts/derive_generator_sent_text.mjs:170-175` asserts the discovery `system` and schema equal `promptForStage`/`stageSchema` output; REC:58-61 delegates to the #266 rule.

## Findings

**N-1 — The packet presents the discovery caps as limits that signing carries; they are code defaults that neither the record nor any check binds.** (note; fix before the packet is offered)
PKT:18-20 says "Each excerpt is capped at 1,500 characters; one map call covers up to 40 files; up to 40 map calls run". [Observed] These are `DEFAULT_DISCOVERY_BUDGET` (`discovery.ts:36-37`). `discoverAndSelect` takes the budget as a parameter, and validation (`discovery.ts:180-182`) bounds `maxExcerptChars` and `maxMapCalls` only below (≥ 0), with no upper bound. REC states no cap. No production caller passes a budget yet: `git grep discoverAndSelect` finds only `discovery.ts`, its test and `index.ts`. A run with a larger budget is therefore within the consent. The packet also calls the reduce payload "short claims", which can be up to `maxReduceClaims` 400 claims of `maxClaimChars` 400 characters each (`discovery.ts:37`).
Suggested words: "with the default budget …; the record itself sets no cap."

**N-2 — The dispatch brief's expected manifest digest is the record digest.** (note) See Digests. The head carries the computed file digest, 6a9e3c94…. A recorder that binds this raw must expect the file digest (REVIEW-BRIEF.md:25-27).

**N-3 — The template pin is count-only; a same-count semantic edit plus `--write` passes `--check`.** (note)
`scripts/build_public_egress_v2.py:93-110,191-194` compares only (hunks, removed, added). Mutant M3 inverted the no-entry sentence, then `--write`, `--check` "current" and `--ready` "ready". Rule 10 still guards the bytes, because the record digest changes and any review bound to it is retired, but the pin does not catch "the template moves" in general. Pinning the TPL2 sha256, or the diff text, in `v2.json` would close it.

**N-4 — The v1 recorder's selftest covers the predicate, not its call site.** (note)
M4 disabled the refusal in `do_record` (`scripts/record_public_repo_admission_acts.py:437`), and the selftest still held 35 of 35. The refusal works today: the direct probe refused. Separately, the guard keys on a filename that no file at the subject commit produces. [Observed] The row-8 recorder is absent from every origin ref. A local unpushed branch `tmp-v2` (e1e5c3c8, outside this subject) has `scripts/record_public_egress_v2_act.py:124` `DECISIONS / f"PUBLIC-EGRESS-V2-{self.stem}-ACT.md"`, whose stem was not checked. When that recorder lands, assert the coupling in one test. Also, `import tempfile` was placed above `selftest()`'s docstring (:495), so the function lost its docstring.

**N-5 — The Agent SDK summary omits `cache_control` on the fixed system prefix.** (note)
REC:150-153 says `cache_control` sits "on the generator's system prompt and input". SDK `runtimeFixed` also lists "system[0]: … (cache_control ephemeral)". REC:146 says the entries govern, so this is not a widening, but these bytes will be bound once the act is performed. If repaired, write "on the prefix and on the generator's system prompt and input".

**N-6 — Delegation reaches any successor entry in the same role.** (note)
REC:19 names "the Agent SDK entry or the Messages API entry" by kind, not by digest or pinned version. A later owner-approved entry, such as a version bump with new header literals, carries its bytes into this consent without a new egress version. This is the declared registry delegation, and the absolute ban (REC:188-191) bounds it. Recorded so that the owner sees it.
