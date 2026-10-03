# R-EGRESS-V2-1 — egress record v2 confirmation
Reviewed commit: 860b0dea2d135fc032b61816540970315ebf012c
Manifest SHA-256: b66a3a5b11cf6527fa4b63b48fe320c08ab63ed27857b5c3306fe3a5099d04ac
Verdict: REVISE

Reviewer: fresh-context governance reviewer. No provider was called and no external repository body was read.
Worktree: detached at 860b0dea, `npm ci` run first. A second scratch worktree held origin/main (7fa33d32) with 860b0dea merged in, for N-6 only.
Paths below are relative to `.syzygy/governance/contracts/candidates/` unless they start with `scripts/` or `packages/`.
REC = `public-egress-v2/instances/egress-anthropic/EGRESS-CONSENT-ANTHROPIC.md`
TPL2 = `public-egress-v2/templates/EGRESS-CONSENT-TEMPLATE-V2.md`
TPL1 = `public-repo-admission/templates/EGRESS-CONSENT-TEMPLATE.md`
REC1 = `public-repo-admission/instances/egress-anthropic/EGRESS-CONSENT-ANTHROPIC.md`
SDK = `public-admission-registry-entries/proposed/POLARIS-PROVIDER-ROUTE-ANTHROPIC-AGENT-SDK-CANDIDATE.json`
MSG = `provider-route-messages-api-entry/proposed/POLARIS-PROVIDER-ROUTE-ANTHROPIC-MESSAGES-API-CANDIDATE.json`

## Digests (rule 3: computed by script, not transcribed)

- [Observed] `sha256sum public-egress-v2/PUBLIC-EGRESS-V2-MANIFEST.txt` gives b66a3a5b11cf6527fa4b63b48fe320c08ab63ed27857b5c3306fe3a5099d04ac. This equals `--manifest-digest` and the expected value.
- [Observed] Python `hashlib.sha256` over REC's bytes gives 5c729afe4ef26ea7d7aaf3cbef213bc25308a788a15c39439ec0607dc6cc156e. This equals the manifest row and `--digests`.
- [Observed] `git diff --stat HEAD origin/main -- .syzygy scripts/derive_generator_sent_text.mjs scripts/build_public_repo_admission.py` shows only this package's six files. The governing references (v1 package, #255 entry, #273 entry, #266 scope) at the head are byte-identical to main's.

## Builder runs (criterion 5)

[Observed] Each command was run at the head from the repository root:

- `--check`: "public egress v2: current", rc 0
- `--ready`: "public egress v2: ready", rc 0
- `--digests`: 5c729afe…, rc 0
- `--manifest-digest`: b66a3a5b…, rc 0
- `--selftest`: "selftest: 19 checks held", rc 0. The "unknown mode --bogus" line on stderr is the selftest's own expected refusal.

[Observed] Rule-6 mutations were made in the scratch worktree, and each was restored with `git checkout`:

| Mutant | Result |
|---|---|
| M1: the record field `Record version` in REC, candidate.1 changed to candidate.2 | `--check` fails: STALE REC, rc 1. `--manifest-digest` refuses: "refusing: stale", rc 1. |
| M1b: in REC's Retention field, the clause ", from the start of the run" deleted | `--check` fails: STALE REC, rc 1. |
| M2: a sent-text classification in `scripts/derive_generator_sent_text.mjs`, `'items[].excerpt': 'target-content'` changed to `'target-metadata'` | `--check` fails: STALE REC and manifest, rc 1. `--digests` refuses, rc 1. |
| M3: the `subsystems[].claims[].relevance` class removed from `DISCOVERY_INPUT_CLASS` | The derivation fails with "discovery-reduce: inputs field subsystems[].claims[].relevance has no class", and `--check` returns rc 1. |
| M4: the `ROUTE_TELEMETRY` override in v2.json loosened | `--check` fails: STALE, rc 1. |

[Observed] After the restore, `--check` reports "current" again and `git status` is clean.

[Observed] The selftest covers the following, and each was read in source (`scripts/build_public_egress_v2.py:178-301`):

- the readiness refusals: an empty stage list, an absent stage, a substring, and `all`;
- refusal of a same version, a class already present, a leftover placeholder and an unknown override;
- the two digest modes staying silent while not ready.

## Table (criterion 1)

- [Observed] A fresh `node scripts/derive_generator_sent_text.mjs --table` at the head equals REC1's table row for row.
- [Observed] A fresh `--table --discovery` equals REC's table, REC:73-114.
- [Observed] REC's table is REC1's 19 data rows unchanged, plus 21 added rows. Every added row's Stages cell is exactly `discovery-map` (9 rows) or `discovery-reduce` (12 rows). No v1 row is removed or reclassified, and no other stage appears.
- [Observed] Every row carries exactly one class. The envelope `inputs` of both discovery calls are rebuilt field by field in `packages/polaris-generation-core/src/discovery-provider.ts:105-117`, so the leaf set is closed.
- [Observed] Target content travels only as `items[].excerpt` (target-content). The map stage's validated replies travel as `claims[].claim` and `claims[].relevance` (composite).
- [Observed] Instruction text: the derivation asserts `envelope.system === promptForStage(stage).system` and that the schema equals `stageSchema(stage)` for both discovery stages (`scripts/derive_generator_sent_text.mjs:163-168`). The #266 rule names exactly those two symbols (`public-source-screening-scope/proposed/…patch`, `instructionTextRule.closedList`).
- [Observed] REC delegates instruction text to that rule (REC:55-58, REC:157-162) and does not restate it.
- [Observed] The refusal of out-of-table fields and route bytes stands at REC:129-130 and REC:160-162.

## Template diff, v1 to v2 (criterion 2)

[Observed] `diff TPL1 TPL2` produces exactly six hunks:

1. TPL2:1. The title changes from `{{PROVIDER}}` to `{{PROVIDER_ID}}, version 2`. **Preserves**; editorial.
2. TPL2:63-64. The derivation adds `--discovery` and the builder name changes. **Preserves.** The only widening it carries is the two stages in the generated table.
3. TPL2:70-71. "the last block of rows" becomes "the rows whose Where is `generate port`". **Preserves**; needed because the discovery rows now follow the port rows.
4. TPL2:77-84. "lists as fixed by the runtime" becomes "lists, whether the runtime or library fixes them or the entry pins them itself (model, effort, tool list, thinking, output ceiling) … follows whichever route entry the owner has in force". **Widens**, within the registry-entry delegation. The entry-pinned parameters become admissible. SDK:258 says this is exactly the reading a further version had to settle.
5. TPL2:86-107, the new section "Bytes each registered route entry lists". It **narrows**: route bytes are admitted only while the entry is in force, and with no entry in force none are. The per-route summary and the stripping sentence are informational.
6. TPL2:121-124. "adds no context of its own" becomes "adds no context beyond those listed bytes". **Widens**, within the delegation. Tools-off stays absolute.

[Observed] Changes in the filled fields (v2.json `fieldOverrides`, compared with REC1):

- PROVIDER: route-neutral. **Preserves**, by delegation.
- RETENTION: "the Agent SDK runtime's own state" becomes "any state the route's runtime or library keeps". **Preserves or narrows.**
- ROUTE_CONTEXT: **widens**, by delegation. See N-2.
- ROUTE_TELEMETRY: **preserves or narrows.**
- SUPERSEDES: new.
- CONTENT_CLASSES gains `project-documentation`. This is a **widening outside the two stages and the delegation**; see N-1.

No template widening falls outside the two stages and the delegation.

## Route neutrality (criterion 3)

- [Observed] RFC4-1 (`contracts/rfcs/RFC-0004/general-contract.md:69-75`): "Every external authority is reached through exactly one registered adapter per project".
- [Observed] `provider-route-messages-api-entry/SEMANTIC-DELTA.md:43-44`: the two entries share a role identity, "so the two cannot both sit in the registry".
- [Observed] Both routes therefore cannot be in force at once. REC:19 says "RFC4-1 admits one", and REC:134-135 admits no route byte with no entry in force. The text cannot be read to permit both routes, or a route with no entry in force.
- [Observed] Independence holds: REC:126-128 says "approving a route entry is a separate act (RFC4-1)", and the packet says the same at `public-egress-v2/OWNER-DECISION-PACKET.md:44-46`.
- Criterion 11 was checked item by item; see B-1 and N-3.

## Status (criterion 4)

- [Observed] REC:4-5 says "Candidate — binds nothing until the owner acts on this record's exact bytes".
- [Observed] REC:37 states conditional prospective supersession of 0.1.0-candidate.7, and says that with none in force it supersedes nothing.
- [Observed] Nothing is labelled accepted. A sweep for accepted, adopted and in force over the package's .md files returned only proposed or conditional uses.

## Governance check (criterion 7)

[Observed] `python3 scripts/check_governance.py` at the head ends with "32 OK, 21 WARN, 0 FAIL (53 checks)".

## Findings

**B-1 — The per-route summary misstates the Messages API route's pinned parameters ("the same pinned parameters"); criterion 11 fails.** (blocking)

The record line is REC:146-150, mirrored at TPL2:100-104: "**Messages API route** … the SDK library's fixed headers …, the headers the Node runtime fixes, and the same pinned parameters." The two entries do not pin the same parameters:

| Parameter | Agent SDK entry | Messages API entry |
|---|---|---|
| thinking | SDK:257 `"thinking": "off: thinking and context_management are absent …"` | MSG:370 `"thinking": "profile-set, one of two values only: off … or adaptive (exactly {\"type\":\"adaptive\"})"` |
| tools | SDK:255 `"tools": []` (the field is present and empty) | MSG:368 `"tools": "absent: the body has no tools field"` |

An owner who reads REC would conclude that thinking is off on both routes. That is false for route B.

These bytes become uneditable once an act binds them (AGENTS.md: "Never edit an artifact after an act has bound its digest"). The false sentence would then stand permanently. The entry would still govern, because REC:136 says the record "cites them and does not restate them", but the record as written is inaccurate.

Fix: name the difference, or drop "the same" and cite each entry's `routeFixedByThisEntry`.

**B-2 — The owner packet does not say in plain words what signing permits; criterion 6 fails.** (blocking)

`public-egress-v2/OWNER-DECISION-PACKET.md:11-49` lists the differences from v1 as a changelog: "gain `project-documentation`", "the discovery stages and fields, each with its one class". It never says what leaves the machine once the owner signs. The packet is missing three plain statements:

- Discovery sends bounded excerpts from many files of the two admitted public repositories to Anthropic before the pipeline chooses what to read. The excerpts are capped at 1,500 characters, with up to 40 map calls of up to 40 files each (`packages/polaris-generation-core/src/discovery.ts:37`). Discovery also sends the model's own claims about those files back in a second call.
- `project-documentation` would newly let README files, guides and design documents of those repositories leave. The current screening scope treats these as indeterminate and withholds them (`public-source-screening-scope/proposed/…patch`, `indeterminate`).
- Nothing about routes changes by signing.

The packet also has no "What you approve / what that permits" section and no owner phrase, though the phrase is reasonably deferred to the recorder.

**N-1 — `project-documentation` is a widening outside "the two stages and the registry delegation".** (note)

REC:30, built at `scripts/build_public_egress_v2.py:112`. The package declares it: packet item 2, brief criterion 1, builder docstring. It is gated on row 7 (packet:69-75). I treat it as declared scope rather than an undeclared widening.

If the dispatching lead's criterion 2 meant to exclude it, it is blocking. The subject description sent to this reviewer listed three changes and omitted the class.

**N-2 — ROUTE_CONTEXT turns v1's absolute context prohibitions into entry-overridable ones.** (note)

REC:171-174: "the route loads no instruction or memory files, user or project settings, MCP servers, hooks or environment summary … **beyond what the registered entry lists**". v1 (REC1:120-122) had no such qualifier.

Neither current entry lists any of these. SDK:317 lists the environment message as `absentByConstruction`, and MSG lists none. A future route entry, which is a separate owner act, could therefore admit memory files or an environment summary without a new egress version.

This is within the delegation the criteria allow, but it is the largest real loosening in v2. Keeping v1's absolute floor would cost nothing today.

**N-3 — The Agent SDK summary omits listed bytes, and the Messages API contrast implies one the Agent SDK route does not send.** (note)

REC:138-145 omits four bytes SDK lists:

- `stream: true` (SDK:251);
- `cache_control` ephemeral on the generator's parts and the prefix (SDK:244-248);
- the `?beta=true` endpoint query (SDK:242);
- `account_uuid` (empty) inside `metadata.user_id` (SDK:250).

REC:149-150 says route B "adds … no environment message". In a contrast list this implies that route A adds one, but SDK:317 says it is absent by construction. Because REC:136 defers to the entries, these omissions are not widenings. They are inaccuracies in bytes that will be bound.

**N-4 — The Scope's target-metadata bullet was not extended for the discovery fields.** (note)

REC:51-54 (TPL2:46-49, unchanged from v1) defines target-metadata as "the source ids, classification bases, exclusion flags and closed exclusion reasons … with no body". The new target-metadata rows go beyond that list:

- `subsystem` and `subsystems[].subsystem`: path prefixes (`discovery.ts:152`);
- `subsystems[].blobs`: a count;
- `items[].path` and `claims[].path`.

The paths are covered only by the trailing justification "a repository's paths are tree metadata (`code-structure`)". The counts are not named at all.

The #266 `classificationBasis` decides class by origin, so the class is code-structure and is permitted. The bullet still reads as a closed enumeration that the table exceeds. `blobId` is the source id's piece base (`discovery.ts:108-121`), not a content digest, so it is covered.

**N-5 — The meaning of `all` in the Stages column is undefined now that discovery stages exist.** (note)

REC:75-93 uses `all`, which the derivation emits for the six pipeline stages (`derive_generator_sent_text.mjs:190`). The `generate port` rows say `all`. REC:116-121 describes how the port carries `system` and `input`. Discovery envelopes are built "for what a generate port sends" (`discovery-provider.ts:4-5`), yet a reader cannot tell from REC whether the port rows cover the discovery stages.

**N-6 — The record cannot be checked or regenerated on current main.** (note)

[Observed] With origin/main (7fa33d32) and 860b0dea merged, `node scripts/derive_generator_sent_text.mjs --table` exits with "no generate call; pipeline outcome: … invalid-request". So do the v2 builder's `--check`, `--ready` and `--manifest-digest`, and so does v1's `build_public_repo_admission.py --check`.

The cause is that main's `validateReaderQuestions` (d8fd0516) rejects the derivation fixture's string reader questions. [Inferred] Once the fixture is repaired, the table probably keeps its rows, because `readerQuestions` is classed as a whole at the pipeline and discovery still takes strings. Any change to the table would still retire this review's digest (rule 10).

This breakage is on main and outside the PR, but it blocks the package's own readiness gate after rebase.

**N-7 — Stale or contradictory prose in the package.** (note)

- packet:7-9, packet:86-92 and REVIEW-BRIEF.md:5 say the record is not ready until #281 is on main. #281 merged on 2026-10-03 (18e83e6d is an ancestor of the head), and `--ready` passes.
- packet:33-35 says "the admitted repositories and content-class list are the first version's". This contradicts packet item 2 (packet:20) and REC:30.
- packet:46 says "row 2a", but packet:103 says "rows 2 and 3".
- packet:47 is an unwrapped long line.
- REVIEW-BRIEF.md:56-57 (criterion 7) asks whether retention and route context are "byte-identical to the first version's". They are deliberately not (v2.json overrides).
- REVIEW-BRIEF.md:24-26 prescribes the head order title, Verdict, Reviewed commit, Manifest. This raw follows the dispatcher's order (title, Reviewed commit, Manifest, Verdict), and a recorder must accept one or the other.

**N-8 — An out-of-order signing is not addressed.** (note)

REC:37 supersedes v1 only if an act over v1 is in force at v2's effective instant. If the owner performed v1's act after v2's, two records for the same (project, provider) pair would be in force, against RFC5-12's one record per pair. The packet says "signing both in order" (packet:79-80) but does not say that the reverse order is refused.

**N-9 — No check pins the template delta.** (note)

The builder docstring says TPL2 is "a copy of the first version's with the lines that name the Agent SDK route reworded" (`scripts/build_public_egress_v2.py:16-17`). Nothing checks that claim. A later edit to TPL2 that keeps `--check` green would pass silently, and only a review would catch it.
