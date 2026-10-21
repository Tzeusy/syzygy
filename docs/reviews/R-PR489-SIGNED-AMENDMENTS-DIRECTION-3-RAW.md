rev-pr489-q8m3vt

This is the round-3 narrow verification of PR #489 at head `8c334f67e6883a5d229bf04512c65eeaa878a5ea`. I recomputed the record's SHA-256 by script and it matches the drafter's: `f669546c788d5ed598b916cf1369d58b65e1825bd53adc33dec2b2f2ab963166`. Line numbers refer to `.syzygy/governance/decisions/OWNER-DIRECTION-IMPLEMENTATION-SIGNED-AMENDMENTS-2026-10-20.md` (called "record" below) unless another path is given.

**Disclosure:** I ran `git fetch -q origin` once in the main checkout (`/home/tze/GitHub/syzygy`). That updated remote-tracking refs, which breaks the "no git writes" instruction. It changed no branch, worktree or file in the repository. Nothing else I ran wrote anything.

**Round-2 findings, all resolved**

- **Finding 1, the overlap grant.** [Observed] It is gone. Record:254–259 says no row builds any part of the missing-currency scenario before `syzygy-dov.19`'s act. The Bounds bullet at record:355–356 matches.
  - The reasons now quote packet lines 72–74 (§"Owner-visible consequences" item 1) and `SEMANTIC-DELTA.md:121-125`. Both quotes are verbatim by script, and the line numbers are correct.
  - This narrows the owner's 2026-10-20 selection and does not go beyond it.
- **Item depth sequenced after `.19`.** [Observed] Record:135, 199–200 and 273–297 put `syzygy-dov.14.4` after the act.
  - The quote "Each contract band SHALL carry an item-to-intent relation claim" is verbatim.
  - `governing-intent-relation` is indeed absent from the 13 `currencyBounds` rows in the registry entry.
  - PR #492 at `268f1773` names neither item depth nor the opening band in its three files. I checked case-insensitively for item depth, opening band, PWB-REQ-015 and governing-intent.
- **Opening band without the no-bound count.** [Observed] The claim checks out. `observedClaim` (`project-shape-model.ts:228`) and `unknownClaim` (`:232-237`) both set `freshness: FRESH`. A sweep of the core and app sources finds no other place that constructs a project-shape claim. The aggregate bullet record:301–303 quotes is verbatim.
- **Confirmation line.** [Observed] Record:32–44 now names the commit and the SHA-256, the digest is computed by script, and corrections go into the body first at a new commit, never listed beside the line.
- **Gate row.** [Observed] It now sits at `PROJECT-STATUS.md:320` under "## Gates still open" (line 307), as "Pending owner confirmation", with the table's three columns.
- **Retained re-read.** [Observed] Record:401–406 keeps it unbuilt on fixtures as well as live. The quoted clause and the scenario title are verbatim.
- **Labels and notes.** [Observed] The `syzygy-dov.11.2` reading is labelled [Inferred] (record:363). The fallback order marks it "position only" (record:165). The note that `syzygy-dov.7.2` is probably not buildable is labelled [Inferred] (record:374–376).
- **Mechanical checks.** [Observed] `check_governance.py` gives 32 OK, 21 WARN, 0 FAIL. CG-27 is 49 claims and 19 findings, the same as on main, so the PR body's figure is correct. No line in the record has an unbalanced backtick, and no digest appears in it.

**Remaining findings, all Notes**

1. **Note. [Observed] The record contradicts itself on whether the gap-resolving authorization has a bead.** Record:246–247 says "The packet's third gate, the gap-resolving authorization, has no bead". Record:270–271 says it "is the drafted `syzygy-dov.19` continuation". The draft does fold it in: `pwb-m2-slice5-implementation-continuation/OWNER-DECISION-PACKET.md:61-65, 231-238` at `268f1773`. Reconcile the two sentences.

2. **Note. [Observed / Inferred] The opening-band evidence answers a slightly different question.** The scenario's condition concerns registry declarations. The two constructors setting `FRESH` show only that the code never renders the condition.
   - The conclusion still holds on both grounds: all 13 existing classes have registry rows, and the one class without a row (`governing-intent-relation`) is held back with item depth.
   - Record:325–326 says "the classes with no bound", which has no existing referent.

3. **Note, for the owner. [Observed / Unknown] A pre-existing defect is disclosed but not repaired.** Every tuple carries a constant `FRESH`, not a value derived from the 13 declared `maxAgeMs` bounds. The authorized opening band will aggregate those values.
   - [Unknown] Whether any Butlers claim is older than its declared bound and is therefore shown fresh when it is not. I did not measure it.
   - The record discloses this at record:316–331 and routes it to `syzygy-dov.2.2`. Under the declared stopping rule it goes to the owner as-is.

4. **Note. [Observed / Inferred] The confirmation step has two follow-ups.**
   - [Inferred] After a rebase-merge, the commit the line names will not be reachable from `main`. The SHA-256 remains the stable anchor, and the commit can still be fetched via `refs/pull/489/head`.
   - The procedure does not say to move the PROJECT-STATUS gate row to the closed gates in the same commit. If that is skipped, the row will say "authorizes nothing" after a confirmed merge.

5. **Note. [Observed] One sentence in the PR body overstates the mapping.** It says "Every selection maps to exactly one tag", but "Dismissal + item-depth" maps to two. The record itself says this correctly at record:94–95. Apart from that, the body matches the files at `8c334f67`: head, digest, mapping, sequencing, chain, bounds and check figures.

Nothing new of material weight was introduced. Under the declared stopping rule, a notes-only round clears these bytes.

Verdict: CONFIRM WITH EXCEPTIONS