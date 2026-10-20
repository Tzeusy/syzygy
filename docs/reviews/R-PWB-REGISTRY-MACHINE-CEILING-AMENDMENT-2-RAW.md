# Review — P-114 PWB registry machine-ceiling amendment, round 2
Reviewed commit: 7d7c3a3e8a68764f987aabd80d09d9c5963d7475
Manifest SHA-256: 5396c8912cd329ba4d4413245e69c1d6fb81536713115e7ca32506e7b1768ac1
Verdict: CONFIRM WITH EXCEPTIONS


[Observed] This is an independent confirmation review of the repaired bytes at the commit above. The brief still says Round 1; this raw is Round 2. The scope is the package named by `REVIEW-BRIEF.md`, its builder, the live-size evidence record, the installed subject and the listed governing references. The predecessor raw and `ROUND-1-DISPOSITIONS.md` were read to assess closure, not as authority for the repaired artifact.

[Inferred] The normative proposal is coherent: change exactly one declared output limit, keep the input/read/security envelope intact, and require the owner to sign the entry and authorize the narrow implementation together. No blocking or revise finding remains. The three findings below are notes; they do not require an edit to these reviewed package bytes.

## Findings

**Finding 1 — Present the refusal as the measured incident, not the current runtime state** (note)

[Observed] `OWNER-DECISION-PACKET.md:11` opens “Since 2026-10-20 ... is refused”, while lines 19–20 say the P-100 implementation was reverted to bring the answer back under the ceiling. The evidence record measures the pre-revert commits `8340fa220ba1bb0ed0a1e6da9f401e72791c53dc` and `0ba7200067769a5307e609cef309c63296e003e6`. The reviewed head already contains the revert commit `7dfe709a`.

[Unknown] This review establishes no current `/api/poc` response, live listener or post-revert size. The lead reported newer measurements while this review was running; I did not use those reports as observed runtime evidence or as a different artifact subject.

[Inferred] The owner-facing presentation should identify the 8,497,943-byte 503 as the motivating incident and the 72-day figure as extrapolation from that incident's five-day rate. The packet already discloses the revert, so this does not change the bounded capacity question or the one-value recommendation. Preserve current framing beside the offered decision; a confirmation here is not confirmation that the endpoint is still refused. VIS-1 requires “Comprehensible truth first”; CC-REV-5 requires provenance “where the claim is read”.

**Finding 2 — The builder's static checks do not prove the runtime constant or gate is valid** (note)

[Observed] The repaired scanner closes the specific Round-1 comment, quote-style, identity, tag and supersession cases. Its remaining boundary is visible at `scripts/build_pwb_registry_machine_ceiling_amendment.py:235` and lines 252–265:

- An unapplied fixture whose constant is `maxMachineResponseBytes: 8388608 * 2,` verifies. The numeric regex reads the leading integer; JavaScript evaluates the expression to 16 MiB.
- An unapplied fixture that changes only `PWB_SUPERSEDED_ACT_RECORDS.registry` from the currency-briefing record to act B verifies. The unapplied branch does not compare the extracted supersession target.
- An applied fixture with an empty current record path and empty act identity verifies when the required tag and supersession target are present. The applied predicates require one string different from act B, not an effective new record.

The exact mutations and returned findings are retained in `independent-probes.json`. These are limits of the builder's static guard, not observed authorization bypasses. [Observed] The independent registry-parity test compares the evaluated `PWB_RESOURCE_LIMITS` object with the entry (`project-shape-observation.test.ts:778–789`), while the actual authority evaluator rejects missing records and wrong supersession targets (`body-read-authority.ts:405` and lines 481–494). PWB-REQ-005 forbids reads until the three exact authorities carry effective owner acts.

[Inferred] Keep the builder, parity test, dedicated recorder checks and full authority evaluation as distinct sign-off verification gates. A clean builder result alone must not be reported as proof that the new act exists or that reads are admitted. This note does not ask for a TypeScript parser or further package repair; it bounds the check's evidentiary meaning, consistent with engineering-bar bias 8 and VIS-2.

**Finding 3 — A2 omits three unaffected readers of `contractVersion`** (note)

[Observed] A direct source-path sweep also finds these readers of the installed entry:

- `scripts/build_public_git_source_acquisition_local_agent.py:206`;
- `scripts/build_public_admission_registry_entries.py:303`;
- `scripts/build_provider_route_messages_api_entry.py:426`.

Each parses the entry and consumes only `entries[0].contractVersion`. They are absent from `IMPACT-LEDGER.md` A2. [Observed] The independent patch comparison leaves that field byte-identical. [Inferred] They need no successor, new authorization or amendment for P-114. Record them as unaffected consumers in the sibling disposition if describing A2 as a complete reader inventory. This does not add any required edit to ask 2 or invalidate its bounded implementation inventory. CC-REV-2 requires updating invalidated authoritative artifacts in the same logical change; these readers are not invalidated by this value-only change.

## Owner-decision packet checks

**Problem scope: Pass.** [Inferred] The governing 2026-10-15 direction asks for the 16 MiB registry amendment first, then a separate serve-once amendment. This package confines itself to that capacity question. The input ceiling, human and briefing ceilings, consented content class, write surface, egress and execution prohibitions remain unchanged. Finding 1 limits the runtime framing; it does not widen or defeat the problem scope.

**Recommendation: Pass.** [Inferred] Doubling this one output ceiling is a defensible bounded step for the stated one-owner POC. The rate and headroom are explicitly extrapolations, serialization time is Unknown, the version-number departure and contrary precedents are disclosed, and owner sign-off remains necessary. PWB-REQ-006 requires that final human HTML and machine JSON “each have an explicit byte ceiling”; it does not mandate 8 MiB. Its bounded typed failure remains unchanged above the proposed ceiling. This preserves VIS-1's complete content and VIS-4's owner decision boundary.

[Observed] Ask 2 is necessary: `routes.ts:233` and `:255` consume the code limit, not the entry's JSON value; the read gate binds the entry's exact digest. The implementation direction of 2026-10-15 enumerates its covered amendments and does not name this entry. The repaired ask explicitly covers the constant, four gate pointers, affected tests, four named builder/recorder successors, dedicated recording machinery, governance registration and battery/workflow integration. Its successor allowance names only this package's row. The two answers must occur together; neither a lone signature nor a lone authorization records or builds anything. This is consistent with VIS-4 and the supplied Scope-A direction.

[Inferred] The review classes touched are authority boundaries, public interface and deterministic observation identity. The sign-off, evidence/inference and security floors remain in force; no new read, egress, execution or write permission is cleared by this review.

## Confirmation answers and retained verification

1. **One value.** [Observed] My independent `git apply` in a temporary fixture produces exactly the bytes obtained by replacing the one old literal. Exactly line 271 changes; parsed JSON becomes identical again after restoring only `entries[0].resourceLimits.maxMachineResponseBytes`. The proposed bytes hash to the one manifest row. The installed subject's hash equals act B's exact digest. The manifest file hash was independently computed with SHA-256 and equals `--manifest-digest`.
2. **Honest basis.** [Observed] The retained records and arithmetic agree: growth 570,510 bytes over five days, 114,102 bytes/day; the incident exceeds 8 MiB by 109,335 bytes; 16 MiB leaves 8,279,273 bytes, about 72.56 days at that rate. P-100's recorded cost is 2,554,038 bytes. [Inferred] The repaired attribution correctly keeps equal measurements Observed and the work-item explanation Inferred; it carries the disagreeing 394/261 item-equivalent estimates. Runtime performance and current service state are not established here.
3. **Impact.** [Observed] Independent Python/blob and `git grep` sweeps agree at the ledger's stated baseline `8340fa22`: 2,858 tracked blobs, 2,854 UTF-8 decoded, four undecodable; 40 value files, 73 value-or-key files, 18 prose files and seven prose-only files. At this reviewed commit the corresponding counts are 2,869, 2,865, four, 50, 85, 25 and seven. `independent-probes.json` retains the exact path sets and skipped paths. The additional live-value sites and parity/evaluation identity effects are covered; Finding 3 adds unaffected consumers.
4. **Asks.** [Inferred] The split and combined-recording rule are safe within their stated bounds. No implementation or adoption is performed by this draft or this review.
5. **Versions.** [Inferred] Keeping `1.2.0-candidate.1` is defensible as an explicitly disclosed owner choice, not a claimed adherence to the prior convention. I checked the `.18` version bump and its convention text. The exact digest distinguishes the bytes, and the cost of losing version-string discrimination is stated. A different owner choice requires redraft and fresh review as the packet says.
6. **Builder.** [Observed] `--check` reports `unapplied, verifies`; `--selftest` reports 22 of 22 predicates held. I read the mutations and their matched refusal messages. Independently constructed unapplied and prescribed applied fixtures verify; an out-of-hunk sibling edit fails through the manifest predicate. The specific Round-1 failure and bypass examples are repaired. Finding 2 bounds the remaining scanner guarantees.

[Observed] The canonical block was extracted from this commit's `PROJECT-STATUS.md` and run in this clone: 106 commands (105 checks plus the doctrine-tag listing), no nonzero command. A separate parse of the retained log agrees with the command-result JSON. `check_governance.py` reports 32 OK, 21 WARN, 0 FAIL over 53 checks; its selftest reports 406 fixtures, none failing. These are the observed checker outcomes, not a claim that warnings disappear or every fixture suite ran: the already-applied spec-policy builder explicitly reports that its unapplied fixtures did not run.

[Observed — review execution disclosure] I installed the clone's dependencies with `npm ci` and started `npx vitest run packages/three-surface-poc-core apps/three-surface-poc` to corroborate the impact dry run. That command started fixture HTTP servers and browser cases; I stopped its owned process subtree because the brief permits builder checks and read-only sweeps and says not to start a daemon. I launched no private POC daemon against Butlers. The live Butlers test entries present in the partial log were skipped. I do not claim a completed Vitest suite, the ledger's 2,017-tests/124-files non-browser denominator, or a new runtime size measurement. The printed command also selects browser cases at this reviewed commit, so future reproduction should explicitly declare exclusions. The partial output is retained and excluded from completed verification.

[Observed] Retained outside the disposable clone under `/home/tze/.cache/syzygy-p114-review-2026-10-20/`: `builder-check.log`, `builder-selftest.log`, `builder-digests.log`, `builder-manifest-digest.log`, `independent_probes.py`, `independent-probes.json`, `independent-probes.log`, `run_battery.py`, `canonical-battery-baseline.log`, `canonical-battery-baseline.json`, `battery-progress.log`, `npm-ci.log`, `vitest-baseline.log` and `reviewed-artifact-digests.json`. No governed artifact, tracker state, act record or tag was changed by this review. The scratch clone is removed after the raw and verification artifacts are retained.
