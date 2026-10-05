# Round 2 dispositions — D9 doctrine amendment packet

> **Candidate — binds nothing.** This record lists each finding of round 2
> and its one repair. The raw review is
> docs/reviews/R-DOCTRINE-AMENDMENT-D9-2-RAW.md, which the lead retains. It
> reviewed commit `63e4196885544d4b78e1995eb43c9f31359653c3` (package digest
> `c9b9d750eb7b959dac7cd005cce0cd95ee0654394970c95c1535cea20bc804c7`) and
> returned the verdict `REVISE`, with 2 revise-level findings and 9 notes.
> Under the stopping rule the package then went to the owner. On 2026-10-06
> the owner answered two questions, recorded in
> POLARIS-DOSSIER-LOCAL-AGENT-D9-ROUND-2-DIRECTION.md: "Any feature, per-run
> choice (Recommended)" and "Close the gap, one more round (Recommended)".
> The lead's dispositions of the same day directed each repair below. None of
> them is confirmed until round 3, the last confirming round. A third
> `REVISE` returns to the owner.

## Revise-level findings

| # | Finding (short) | Repair |
|---|---|---|
| F1 | Arm A permits any Syzygy instruction in any feature once a choice is recorded, at no stated granularity, while the packet said it permits "what you ruled and nothing more" and the delta headed it "matches the ruling" | **The owner chose the width:** any feature, on a choice recorded per run. Arm A's permitted case now requires that "the owner has recorded a choice for that one run, naming what the instruction covers. A standing or per-project record does not qualify." Condition 1 and the new violation sentence say "for that run", and the violation list adds "or on a standing record". The delta's arm A heading and packet Q1 say that arm A covers any feature, give a dispatched work item as the example, say it is wider than the dossier ruling by the owner's 2026-10-06 choice, and say a future feature needs no new doctrine act. Q1 records the scope as the owner's answer and leaves adoption open. "Nothing more" and "matches the ruling" are gone (0 occurrences in the package). Arm W's condition 1 and violation sentence take the same per-run wording, so the two arms differ only in reach |
| F2 | Condition 4 reached only "the session", so observed code the session leaves running could read an adapter credential, and RFC5-24's "never" could fail; "readable" could be read as an agent tool-permission rule | Condition 4 now reads: "Syzygy keeps every credential it holds for its typed adapters where neither the session nor any process it starts, directly or not, can read it at the operating-system level, for as long as any of them runs." "Directly or not" covers grandchildren of the session. The delta says the reading is OS-level (file permissions, a separate OS user or a protected store), and that tool-permission rules do not satisfy it because child processes ignore them. Q3's cost no longer says "during attended runs"; it says the credential must be unreadable by the owner's user while any process the session started still runs. Ledger RFC5-24 row updated |

## Notes

| # | Note (short) | Repair |
|---|---|---|
| N1 | Q1 and Q2 are one choice; Q2's "No" makes the lead's reading doctrine | Merged. Q1 now asks "Which text, and so whom does SEC-3's execution rule bind?": A is the "No" answer written as doctrine, and W is "Yes" without a list of lawful outside executions. Q2's row is kept as "folded into Q1" so Q3–Q5 keep their numbers. Packet §3 and the delta's "What arm A means" say that arm A makes "SEC-3 only binds Syzygy's own execution", which the review-1 rulings direction called "the lead's reading, not the doctrine's text", the doctrine's text for execution, and that this restores the premise of the owner's first answer |
| N2 | Under arm A, the case's limits bind only what Syzygy may instruct; the packet read them as limits on the session | **Decided: they bind Syzygy's instruction, not the session.** The text's bullet is renamed "Whom the case binds: Syzygy" and ends "Once the instruction is given, SEC-3 governs what Syzygy does about the session, not what the session does." Packet §2 says so at the bullet, including that SEC-3 does not forbid the owner walking away or the session leaving a server running, and that condition 4 remains Syzygy's duty while any such process runs. The bullet refers to no condition by name, so deleting the credential lines leaves it whole |
| N3 | "Instruction Syzygy's software issues" was defined only in the delta; static skills and prompt kits, and a typed CI adapter, were unclassified | The definition is now in arm A's text: "every instruction a Syzygy feature gives an agent (a brief, prompt, skill or work item)". A shipped skill or prompt kit is covered whether or not it is emitted at run time. Ledger §3.6 classifies `AGENTS.md` (not a feature's instruction), shipped skills and prompt kits (governed), and a Syzygy-triggered CI run through a typed adapter (forbidden outside a profile under arm A; not the permitted case; reading CI artifacts stays observation under RFC5-19). §5 item 1 routes the CI question with dispatch |
| N4 | "The owner's recorded choice" has no stated provenance | Granularity is now fixed: per run, naming scope. Provenance is left to the specification and said so: packet §3 ("Who records your choice is left to the specification"), the delta's terms and "What arm A means", and ledger §5 item 6, which names PR #353's agent-written, agent-editable record |
| N5 | The ledger's claim that neither sweep finds `capture-test-artifact-main.ts` is false | Corrected in ledger §1, with the false sentence named. The code-lane term hits were read at `5863d470`: 17 files, each classified in §1; only the two capture-tool files execute observed code. §1 now says which lanes the round-1 read covered |
| N6 | "Verification then shows `Verified`" is unconditional | Packet §3 and ledger §3.6 now say "can show" / "can render", with the three conditions from `docs/THREE-SURFACE-POC.md` |
| N7 | The credential-line deletion is not digest-checkable | The delta gives both no-credential digests and line counts, computed by script from the fenced blocks: arm A 47 lines, arm W 44 lines. The reviewer's figures (41 and 42 lines) describe the round-1 repair's bytes, which this repair replaces. Migration step 2 and packet §7 say to check the result against the digest. SEC-4 lands at 109 without the lines and 112 with them under arm A; the second is [Observed] in the probe |
| N8 | "Attends" is defined only by exclusion | Arm A's text now defines it positively: the owner "attends it, being present to see and stop what it does". Packet Q5 and the delta say that a session in an auto-approve or permission-bypass mode with the owner away is not attended, and ledger §5 item 7 notes that Syzygy cannot observe attendance |
| N9 | Ledger dates `eb7be564` as 2026-10-06 | Corrected to its commit date, 2026-10-05 23:57 +0800 |

## Other changes made in this repair

- The branch was rebased onto `origin/main` `5126610b`, which carries the
  owner's round-2 direction and the round-2 raw. The doctrine,
  accepted-contract and craft-and-care trees and `PROJECT-STATUS.md` are
  identical to `eb7be564` [Observed: `git diff --quiet`]. The probe and the
  sweep re-measurement ran at `5863d470`, its parent, which differs only in
  those four non-doctrine files.
- The application probe was re-run at `5863d470` with the repaired arm A
  applied: 78 commands; unapplied 0 nonzero; applied 4 nonzero, the same four
  regenerations. On regeneration the directive register moves SEC-4 to 112
  and SEC-5 to 125 (ledger §4).
- The identifier sweep was re-measured at `5863d470`: 244 files, a superset
  of the 241 at `eb7be564` by three files, all named in ledger §1.
- The arm A text's "What this binds" and "Whom the case binds" bullets were
  reworded to carry F1, N2 and N3. The cost bullet keeps its words and is
  only rewrapped; the violation bullet adds "for that run" twice and "or on a
  standing record". The kept bytes (title,
  "untrusted whoever owns the project", the profile bullets and the original
  violation sentence) are unchanged.
- Register row P-103 is updated, with a dated round-2 note.
