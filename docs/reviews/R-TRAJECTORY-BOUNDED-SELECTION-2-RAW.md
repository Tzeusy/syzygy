# Independent re-review: bounded Trajectory selection
Reviewed commit: c336bc262fad278b742f6ebf64f9d76368b1457e
Subject manifest SHA-256: f330fa69a55ff411b7fac7a960a98d370e60f657ce4207c004833fa6bb89036a
Verdict: CONFIRM

[Inferred] **CONFIRM applies to the repaired bounded-selection source and its scoped regressions.** Final repaired-head mutation, measurement and full-gate receipts remain a separate completion gate, explicitly pending in this subject. This verdict does not certify a later moving head or those unfinished receipts.

[Observed] Reviewed the repaired source against the original acceptance criteria and the first raw's P2/P3 findings. The first raw remains unchanged, SHA-256 `6bea0d844b7d4419858b4c6f787fa5026aa70b31d8e8bf2da934d57a511f1ad3`. The cumulative six-file change is against base `3d03f693a52328cf03804f4f5ecb15236617ce15`. Source bytes were read with `git show` at this subject and exercised in a detached disposable clone after its own `npm ci`. No author worktree or Beads state was modified.

## Findings and disposition

- **Blocking findings:** [Inferred] None identified within the reviewed selection implementation, documentation and scoped behavior. The prior P2 finding is resolved on the exercised counterexamples and additional cases below.
- **Prior P2 — resolved.** [Observed] `packages/three-surface-poc-core/src/trajectory-projection.ts:55-80` now rejects unsupported timestamp syntax before parsing, requires an explicit timezone, validates Gregorian dates including century leap rules, bounds clock/offset fields, and preserves up to nine fractional digits in the ordering key. Both population sorts use that helper. Timezone-less and impossible dates no longer outrank valid recorded instants; equivalent offset-adjusted instants fall through to the explicit ascending-ID tie rule. The implementation does not substitute creation, update or closure fields for one another.
- **Prior P3 — resolved.** [Observed] `packages/three-surface-poc-core/src/trajectory-projection.test.ts:31-46` now passes a frozen observation with reversed ID order, frozen item records and frozen provenance. A scratch-only mutation from `const sorted = [...workItems.items].sort(byId);` to `const sorted = workItems.items.sort(byId);` makes exactly that selected regression fail with a read-only-array error. The source was restored byte-for-byte. `immutability-mutant-2.json` retains the subject, subject digest, exact old/new fragments, command and result; `immutability-mutant-2.log` contains the complete failure.
- **Unfinished evidence, not a new source defect.** [Observed] The evidence JSON's status explicitly says repaired-head source mutation, after-size, independent review and clean-clone gates are pending. It retains earlier-head receipts with their earlier subject identity; these do not establish repaired-head verification. Final completion requires inspection of the finished receipts at the exact final head. No final performance claim is confirmed by this source review.

## Independent behavior verification

[Observed] Retained full logs and probe sources beside this raw:

| Check | Result | Retained output |
|---|---|---|
| Checked-in projection and app tests | 28 passed / 28, two files | `targeted-tests-2.log` |
| Original independent repros, unchanged fixture source | 5 passed / 5 | `independent-probes-2.log` |
| Additional independent edge cases | 14 passed / 14 | `independent-edges-2.log` |
| In-place-sort mutation against the strengthened checked-in test | 1 failed, 13 skipped / 14 collected; expected failure | `immutability-mutant-2.log` |

[Observed] The original probes now select the explicitly zoned item under UTC, Asia/Singapore and America/New_York. The impossible February date ranks after the valid March instant in both the non-closed and closed populations. The retained probe title names its original subject because its bytes were reused unchanged; the actual rerun used this raw's detached subject commit. Its other passing checks retain 64 deterministic permutations of a deeply frozen ten-item observation across seven declared statuses, literal selected memberships, full reconciliation, and distinct observed-empty versus Unknown results.

[Observed] The additional fourteen cases are seven literal cases exercised separately for open and closed items, each under UTC, Asia/Singapore, America/New_York and Pacific/Honolulu. They cover nanosecond ordering, equivalent instants with different explicit offsets and ID ties, fractional instants before the Unix epoch, valid year-2000 versus invalid year-1900/year-2100 leap days, unsupported formats and invalid-value ID ties, invalid numeric offset fields, and prevention of field substitution. They also check the full denominator and literal Backlog/Done placement. Expected memberships are constants; no production parser or sorting helper computes the expected values. Their source is `trajectory-review-edges.test.ts`.

[Observed] The checked-in app test still exercises `buildPocModel` and the actual `/api/poc` route: 252 full machine work items, 250 selected human cards, 2 exclusions and 50 Done cards. Demonstrated open and closed items outside their population limits retain the explicit outside-selection callout. The updated core tests cover both invalid update and invalid closure times, offset ordering and timestamp/ID ties. Production model limits remain 200 non-closed plus 50 closed, and card ordering remains ascending ID within the unchanged status columns. No extra demonstrated-item card bypasses the limits.

## Scope, doctrine and documentation

[Observed] The implementation documentation now states the supported timestamp grammar, timezone-less handling, both population limits, ID tie/card ordering rules, rendered/excluded/full count disclosure, complete machine population, and the limitation that fixed counts bound card growth rather than arbitrary selected text. The visible selection rule matches the new missing/invalid/timezone-less behavior. The evidence record's truth-floor statement correctly identifies the affected floor; the reviewed diff leaves the other CC-BAR-5 floors unchanged.

[Observed] Enumerated the cumulative changed paths with both `git diff --name-only` and `git diff --raw`; the six path sets match. No adopted specification, source-read/egress implementation, response ceiling, registry or P-100 governing-intent implementation is part of that diff. P-100's deliberate base revert is preserved and outside this review.

[Observed] The six governing files listed in `subject-digests-2.json` remain byte-identical to the first reviewed commit: the adopted POC specification (POC-REQ-040/041/042 and adjacent 043), both mode/improvement-cycle directions, doctrine `vision.md` (VIS-1/VIS-2 and Performance), the engineering-bar policy and the performance policy. The first review's governing reading therefore applies unchanged. The relevant obligations are declared status placement, ordering from recorded instants, explicit scope/count reconciliation, deterministic truthful observations, declared narrowing under CC-PERF-1, and retained before/after evidence under CC-PERF-3. Skills used: engineering-bar, heart-and-soul and test-rigor.

[Unknown] The implementation owner is finishing the repaired-head full gates and measurement/mutation receipts. This re-review deliberately did not duplicate the full suite, run live observation, read Butlers repository bodies or read live response bodies. The source confirmation is independently supported by the scoped checks above, not by the author's reported results.

## Exact source subjects

The manifest digest in the header is SHA-256 of `source-subjects-2.sha256`: each row is its file SHA-256, two spaces, the path and one terminating newline, in the displayed order. Each digest was generated from frozen `git show` bytes and checked against the exercised clone after scratch mutation restoration.

| Path | SHA-256 |
|---|---|
| `apps/three-surface-poc/src/trajectory.test.ts` | `d57c80c650eca043b9f7e4f2cda0533ec2c52197bbc25a341ec4942fb8deb27b` |
| `docs/THREE-SURFACE-POC.md` | `b7a1d158ef726ed797ebcfa33d8fcb4c56eb2adf4e3031bea082aec272745aa2` |
| `docs/evidence/syzygy-blbu-trajectory-selection-2026-10-20.json` | `bfe79bb1aa7bae87e2de8f183cd5a4200585278544654a54b09baa12c32bce1e` |
| `packages/three-surface-poc-core/src/model.ts` | `c31c6937ec4592fca828fe511ac87e896ca2bd047a3d9b08ccbc185340eb0460` |
| `packages/three-surface-poc-core/src/trajectory-projection.test.ts` | `015a1d4c8bc37b6e7b9381e03987737282fb0e640c65d828a7a9a72e9d560607` |
| `packages/three-surface-poc-core/src/trajectory-projection.ts` | `f0d2a5b90e8b76e8a7fad815b96c66bbe7cc53b3f671c982ab088c1bcfd91647` |

[Inferred] Final disposition for this repaired source: **CONFIRM**. Obtain separate confirmation of the exact final receipt/docs delta before treating the task as complete.
