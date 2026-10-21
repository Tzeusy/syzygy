# GP-Q0 confirmation (round 4, narrow)

**Result:** All four parts of the round-3 fix and all three round-3 notes are in the current bytes, and the edit added no material defect. GP-Q0 now passes. Four non-material notes remain; the first is a leftover of the round-3 defect in the summary table.

**Subject:** `/home/tze/GitHub/syzygy/.syzygy/local/questionnaires/2026-10-21-greenfield-parity.md`, 296 lines, sha256 `7a089a75b132a74cac7f50bde3af0e3fedc3a360f8e14742c72cb7b226fd73c8`. I read GP-Q0, lines 29–120, plus the summary row and shared background that belong to it.

**Scope verdict: Pass.** The three-part question is unchanged and still right. The background now quotes CC-REV-1 exactly ("Changes touching any of seven classes require review by an independent, fresh-context reviewer, and the agent performing the change never finally decides which classes it touches"), and the output-changing list is complete.

**Recommendation verdict: Pass.** Option A now applies CC-REV-1 to every class, and the extra bar is scoped as prescribed. The round-3 defect is fixed in the option text the owner chooses.

**Material corrections:** None.

**The four parts of the fix** [Observed]:
1. **Review for every class-touching PR.** Line 62 reads: "any PR whose classes are not 'none' gets the CC-REV-1 independent default-model review".
2. **Extra bar where prescribed.** Line 62: "Class 1/3/4 PRs, and class-6 PRs that remove an endpoint, additionally get" the differential, a rule-6 mutant per predicate, and the owner notice.
3. **The three beads are listed.** `5.4` (class 6) and `6.1` (class 3) are on the known list (line 47). `5.4` and `2.2` are on the output list (lines 54–55).
4. **Class names use the clause's wording.** Classes 1, 3 and 4 match CC-REV-1, `review-and-documentation.md:16-41`. Class 6 is shortened; see note 3.

**The three round-3 notes** [Observed]:
- **bd ready count.** Line 10 says "Fifteen" and names `2.1`, `4.1`, `4.2`, `4.5`, `4.6`, `5.4`, `5.5`, `6.1`, `6.2`, `7.2`, `8.1`, `8.3`, `8.4`, `9.1` and `9.4`. Re-running `bd ready` now gives the same 15, plus `1.1`.
- **Rationale.** Line 69 names `9.4`, `5.4` and `2.2`.
- **Option C count.** It reads "about twelve or thirteen" (line 64).

**Notes (not material):**
1. **The summary table still says the old thing.** Line 25 reads "class-1/3/4 refactors are reviewed under CC-REV-1, with a differential corpus and an owner notice". That restates the narrowing round 3 fixed. It is not material because the owner chooses option A, whose text is now correct. Fix it before presenting: every class-touching PR gets the CC-REV-1 review, and class 1/3/4 and endpoint-removing class-6 PRs also get the differential and the notice.
2. **The review record doesn't match the raw.**
   - Line 32 says "Passed". The raw's verdict words are "Scope verdict: Pass" and "Recommendation verdict: Revise" (`…-review-3-RAW.md:21,30`). Copy them exactly.
   - "Applied verbatim" overstates it: the fix was applied in substance and adds "default-model".
   - "Not re-reviewed" (lines 32, 85, 100) is no longer true. Under the stopping rule on line 6, a material defect doesn't make an item Review-ready on its own. The Review-ready state (lines 25, 31) should cite this confirmation.
   - Line 4 lists only the round-1 and round-2 raws. `…-review-3-RAW.md` exists (11,509 B); add it, and this confirmation once it is retained.
3. **Class 6 is cut short.** Line 47 drops "anything an external consumer can depend on" (clause lines 40–41), which is class 6's broadest part. The list says "include", so the cut is allowed, but add the phrase.
4. **5.4 is described too narrowly.** Line 54 says 5.4 removes "machine and presentation routes". `routes.ts:286-319` and the bead show eight path-prefixed registrations, which also cover the human Polaris, Trajectory and Orrery routes, the source route and the mount root. Two fixes:
   - Describe it as removing all eight path-prefixed routes.
   - Keep the bead's own premise-check stop visible, so the approval cannot be read as overriding it. The bead stops if the machine `links` array or a signed spec names the prefixed paths, and it requires remaining routes to stay byte-identical.

**Evidence freshness:** HEAD `eba011dfbe254c09a88ccc374b3efe5ff5df1762`; the tracked tree is unmodified. I read CC-REV-1 at `review-and-documentation.md:16-41`, `apps/three-surface-poc/src/routes.ts:286-319`, and the round-3 raw's verdict lines, and re-ran `bd ready` against the local Dolt database on 2026-10-21. Not inspected: bd remote, GitHub PR and CI state, other sessions' worktrees, live CLI or daemon runs. Everything was read-only.