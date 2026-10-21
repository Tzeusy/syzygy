rev-pr489-q8m3vt

Review of draft PR #489 at head `9e63b8569d94710f054ff0f2594c18de7e0043b6`. I made no edits and no git, gh or bd writes. I ran `check_governance.py` on the PR worktree and on main at `29e036f4`, and wrote the two outputs to my scratchpad. Line numbers refer to `.syzygy/governance/decisions/OWNER-DIRECTION-IMPLEMENTATION-SIGNED-AMENDMENTS-2026-10-20.md` (called "record" below) unless another path is given.

**What checks out**

- **Quotation (item 1).** [Observed] The questionnaire does not hold the question text: its log row (`.syzygy/local/owner-questionnaire-2026-10-20.md:367`) gives only a summary. So I compared the record against the lead session transcript instead (`~/.claude/projects/-home-tze-GitHub-syzygy/49123ca9-….jsonl`, AskUserQuestion call at 14:03:17Z, answer at 14:05:05Z).
  - A script matched both question stems, all six options and both answers, byte-exact and NFC, against record:40–66.
  - The quote of `syzygy-dov.19`'s design (record:191–192) matches the bead.
  - The quote of the missing-currency packet's gates (record:186–188) matches `pwb-missing-currency-disclosure-scenario/OWNER-DECISION-PACKET.md:105-115`.
- **Items not authorized (item 1).** [Observed] Exact-source render-mode is not authorized (record:199–200), and the PROJECT-STATUS row for it is unchanged. Missing-currency is held back correctly:
  - the packet names two gates still open (`.19` and a fresh authorization that resolves the five gaps);
  - `.19` requires an exact phrase;
  - `syzygy-dov.2.2`'s only open dependency is `.19`.
- **Tags and citations (item 2).** [Observed] All seven tags exist. Their commit order is opening-band, render-mode, machine-view, missing-currency, dismissal, container-shape, item-depth. That matches the chain rationale at record:167–169. The cited act lines (machine-view :86, opening-band :87–89) are correct.
- **Bounds (item 3).** [Observed] Every bound in the 2026-10-15 record is present, and the new ones only narrow: ceilings before members, and no write or retention change for dismissal. Nothing is widened. The chain order is lawful and marked [Inferred], and the owner may reorder it.
- **Act-bound bytes (item 4).** [Observed]
  - Neither edited file's digest, before or after the change, appears in any manifest or act record.
  - `PROJECT-STATUS.md`'s path does appear in two manifests, neither of them performed:
    - `polaris-edit-repair-deletion-scenario/…-MANIFEST.txt:14` lists it as a PATCHED row of a candidate that binds nothing until its act;
    - the act-4 row in `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` mentions it only in prose.
  - `check_governance` gives 0 FAIL on both trees. The only extra WARN lines on the PR side are CG-1f frozen-lane paths from raw review files this PR does not touch, which I read as worktree-environment effects. CG-27 output is identical.
- **Sentence marks (item 4).** [Observed] The marks at PROJECT-STATUS rows 241, 244, 246 and 248 sit at the stale sentence, are dated and keep the old text, as the CG-27 lesson asks.

**Findings**

1. **Important. [Observed / Inferred] The confirmation mechanism cannot be carried out as written.** Record:20–24 says the owner confirms the recorder's mapping "by approving the pull request". The PR's author is `Tzeusy`, which is the owner's account. [Inferred] GitHub does not let an author approve their own PR, so the only action left is a merge, and lead sessions merge routinely. A merge by an agent would then put the recorder's reading in force without the owner confirming it (a VIS-4 risk). No other decision record uses this mechanism; a grep of `decisions/` finds only this file. Name a confirmation the owner can actually perform and that is recorded, for example an owner-only merge or an in-file confirmation line.

2. **Important. [Observed] Item depth's signed text depends on the missing-currency behaviour that this record withholds.**
   - `spec.md:1993-1999` (PWB-REQ-015) requires every relation claim to be Unknown with reason `no-currency-bound-declared`, "its exact resolution route and the outside-slot disclosure PWB-REQ-007 requires". That is the missing-currency scenario (`spec.md:1037-1062`), and item depth was signed after it.
   - Record:216 lists "the missing-currency scenario" as not authorized, yet record:115 authorizes item depth as "exactly the signed text". The record never resolves the overlap.
   - [Inferred] The opening band (record:113) is an aggregate over Unknown claims, so the missing-currency aggregate-count rule (`spec.md:1056-1062`) probably reaches it too.
   - The per-claim disclosure is partly built already (`apps/three-surface-poc/src/polaris.ts:349`).
   - Fix: state what an authorized row may build of PWB-REQ-007's currency disclosure (separate from M2 slice 5's declared bound), or route the overlap to escalation explicitly.

3. **Important. [Observed / Inferred] Dismissal questions 2 and 7 are left unanswered but only partly fenced.** Packet questions 2 and 7 (`pwb-dismissal-expiry-amendment/OWNER-DECISION-PACKET.md:95-102, 130-139`) are correctly left open and marked [Unknown] at record:221–229. The fences are incomplete:
   - **Question 2:** record:226–229 forbid a write path and Butlers reads, which covers the "who writes" half. Nothing stops a lane from settling where the records live by picking a governed-plane path in code. [Inferred]
   - **Question 7:** the fence forbids changing what the retention direction keeps. A lane could still decide that keeping dismissal bytes reachable from a retained evaluation is not a retention change, which is exactly what question 7 asks the owner.
   - The escalation trigger covers only "write path, Butlers read, retention change". Add the record home and the retained re-read scenario to the stop list.
   - [Observed] The same packet's question 11 (fresh authorization or continuation?) is answered by the owner's own selection, so it is not answered silently. I found no other open question that the record answers.

4. **Note. [Inferred] The machine-view "not shared-model" call is defensible but is a reinterpretation.** The 2026-10-15 rule includes rows "computed against its machine answer". The signed text requires every derived-view value to be "independently verified as derivable from the machine answer's own bytes" (`spec.md:2312-2314`), and record:129 concedes that "its oracle checks against that answer". The P-77 precedent and the P68-P83 decision ("Nothing else touches `PocModel`", line 81) support the record's reading. Even so, record:118–120 says the rule is "applied without change" when it is really narrowing "computed against" to "contributes to the answer". Say so, so the owner confirms that reading rather than a restatement.

5. **Note. [Observed] Two machine-view beads go beyond the signed text without saying so.**
   - `syzygy-dov.11.2` is a status machine route. It is in neither signed category, and `spec.md:2333-2334` says "A route in neither category is neither admitted nor forbidden". Its authority is P-78 plus the continuation act, not the machine-view text.
   - `syzygy-dov.7.2` serves `/polaris/draft/<runId>`. The machine-view act (`PWB-MACHINE-VIEW-AMENDMENT-ACT.md:90-92`) leaves that category's "record-level fields and its relation to the exact-source anchors … to the later route amendment". The record does not fence that line.

6. **Note. [Observed] One unmarked sentence is now stale.** `PROJECT-STATUS.md:250` (tree framing, marked 2026-10-15) says "last in the shared-model WIP-one chain". After this PR it no longer is.

7. **Note. [Observed] Minor wording issues in the summary rows.**
   - `PROJECT-STATUS.md:247` (container shape) adds an undated new sentence rather than a dated mark, unlike its sibling rows. No stale sentence existed in that row, so this is cosmetic.
   - The README row ("Same bounds", `decisions/README.md:85`) and the gate row ("with the 2026-10-15 bounds", `PROJECT-STATUS.md:304`) don't mention the added carve-outs: ceilings before members, and no write or retention change for dismissal.

8. **Note. [Observed] One sentence reads as inconsistent with the quote beside it.** Record:192–193 says `syzygy-dov.2.2` "is blocked only on `syzygy-dov.19`". That is true of the bead graph, but it sits next to the packet's statement that a third gate (resolving the five gaps) is also open and has no bead. Reword to say which graph "only" refers to.

9. **Note. [Observed] An evidence record no longer matches PROJECT-STATUS.** `docs/evidence/p114-machine-ceiling-battery-counts-2026-10-21.json:8` holds the pre-PR digest of `PROJECT-STATUS.md`, and `PROJECT-STATUS.md:483-485` calls that comparison "for this revision". The PR leaves the battery lines and counts alone, so the record goes stale only by digest. It is not act-bound.

10. **Note. [Observed] A dismissal dependency is outside the chain.** `syzygy-dov.12.1` (the dependency of dismissal bead `syzygy-dov.12.3`) is marked "Shared-model: WIP-one" in its own notes. It appears in neither chain, so when it resumes it competes for the slot without a stated position.

Verdict: REVISE