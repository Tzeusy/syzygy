# Review - D7 doctrine amendment packet (held derived computation, P-101), round 3
Reviewed commit: 7071a7440fbf85e8d12f13e804dbd57af400a453
Package digest: cc9709730aeab80f51256b57f1ac5d27515d9be229f3e957df6c66524af1490f
Verdict: REVISE

Reviewer: one fresh-context agent. I had no access to the drafting, round-1,
round-2 or cycle-2 repair sessions. Brief:
`.syzygy/governance/contracts/candidates/doctrine-amendment-held-derived-computation-d7/REVIEW-BRIEF.md`,
§"Round 3" (head contract, stopping rule, subject, references). That section
lists both earlier raws as governing references, so I read them and checked
each round-2 finding against the current bytes.

Method: a git worktree detached at the reviewed commit (`git rev-parse HEAD`
equal to it, `git status --porcelain` empty). Package digest: I ran the
brief's command in two forms, because the sandbox would not accept the
`$(git ls-files …)` form as one command. (a) `git ls-files` over the package
gave six paths, already in C order. `sha256sum` over those six paths, piped
into `sha256sum`, gave `cc970973…`. (b) A Python `hashlib` script rebuilt
the same `sha256sum` output from `git ls-files` (paths sorted by byte value)
and hashed it, with the same result. Every digest below was scripted. I did
not read any Butlers repository.

## What was confirmed

- [Observed] Section 1's proposed doctrine bytes are unchanged since round
  2. `git diff 8f1fbec7..7071a744` on the packet has no hunk inside either
  `markdown` block of §1.1 or §1.2. The only §1.2 hunk is the sentence that
  describes the block. The delta's two blocks are not touched either.
- [Observed] The anchor sha256 values hold at the reviewed commit:
  `vision.md` 93cc5fbb…0506d, `architecture.md` d1987f7f…cb565,
  `RFC-0002/reconciliation-chain.md` 7d7f876b…38bb5,
  `RFC-0005/admission-and-boundary.md` a742a77f…3e0, the P68–P83 decision
  a59294d4…71079, and `RFC-0002/snapshot-and-evaluation-core.md`
  7f573ba1…b3526 (the new §4.1 value). I compared full values by
  `sha256sum`. The anchor text is exact at `vision.md` 105–107 and
  `architecture.md` 329–334. The section intro is at `vision.md` 86–87.
- [Observed] The §4.1 clause citations are right. RFC2-17's reservation is
  at 122–124, RFC2-18's scope sentence at 141–142, "**merged** is execution
  state" at 153, the reconciliation-pending bullet at 155–157 and RFC2-19 at
  245–247. RFC2-1 item 1 is at `snapshot-and-evaluation-core.md` 78–79.
  `grep -F "merge fact"` over the RFC-0002 directory returns 8 hits: lines
  61, 146, 156, 158, 225, 274 and 334 of the chain module, and line 101 of
  the core module. None is a definition. This matches §4.1 and disposition
  repair 1.
- [Observed] Round-2 finding 2 is repaired. I re-ran the ledger §4 reader
  sweep at `66d42d090e7966812f397bb38760b70bc9e63ac6`: Python `re` over `git
  ls-tree -r -z` and `git show`, then `git grep -l -E` over the same
  pathspecs. Both give 417 files and 11 hits, and the hit sets are
  identical. The 11 are exactly the ledger's enumeration, and 1 + 2 + 1 + 4
  + 1 + 2 = 11. `build_contract_index.py` line 46 at `66d42d09` reads
  `GOV_SOURCES = [("../../doctrine", "doctrine", "doctrine"),`, as the
  ledger says.
- [Observed] Round-2 finding 4 is repaired. The resulting paragraph has ten
  lines, and packet §1.2 and the delta now both say so correctly.
  `ROUND-1-DISPOSITIONS.md` row 15 is marked at the sentence.
- [Observed] Round-2 finding 5 is repaired. Line 320 is blank. The RFC5-11
  paragraph spans 321–323: its bold lead is on 321, and the quoted words
  "Recording a revocation …" begin on 322. Citing 321–323 is correct for
  the clause.
- [Observed] Round-2 finding 6 is repaired. Arm B's defect is now "records a
  Normative change as if it were Clarifying", and the bullet's bar is
  correctly limited to autonomy beyond VIS-4's bounds.
- [Observed] Round-2 finding 7 is repaired. Packet §7 and the ledger's
  `vision.md` row both state the extra weight.
- [Observed] Round-2 finding 8 is repaired. Each sentence the raw named is
  marked at the sentence, dated, with the old text kept: packet lines 17–31,
  delta lines 8–12 and 249–256, `ROUND-1-DISPOSITIONS.md` lines 6–8 and
  22–24 and rows 4, 12 and 15, `ROUND-2-DISPOSITIONS.md` lines 6–9, 30–33
  and 47–53, and `REVIEW-BRIEF.md` lines 13–18. The round-1 and round-2 raws
  are not in the diff. I found no stale "no round 2" or "not repaired"
  sentence left unmarked inside the package. One sentence outside it is
  stale; see note 6.
- [Observed] Round-2 finding 3 is repaired in substance. Section 1's text is
  untouched. §2 names the page-open residual. Nothing claims that a test
  exists ("the daemon as it stands has no such test [Inferred]"; "this
  packet drafts none"). The Trigger row qualifies "a commit". Note 3 covers
  a residual wording issue.
- [Observed] Round-2 finding 1, the structure of the repair: §0, §2's
  "unprompted" paragraph, §4's two RFC2 rows, §4.1, §6 items 1 and 2, the
  ledger header, its two RFC2 rows and closing paragraph, and the delta's
  RFC2 bullet and downstream summary all now name both readings. All of
  them label the narrow reading as the one relied on. On what arm A permits
  under each reading, they agree with §4.1's table. Both readings are stated
  fairly from the clause text. The narrow reading is labelled and argued
  from RFC2-18's scope sentence, the definite article, and RFC2-17 and
  RFC2-19's "reconciliation" wording. The wide reading is argued from line
  146 and RFC2-1 item 1. Whether the POC's repository carries materialized
  merged work is labelled [Unknown]. Finding 1 below concerns Q5's
  consequences only.
- [Observed] Every package file is NFC.
- [Observed] `python3 scripts/check_governance.py` at the reviewed commit
  gives 53 checks: 32 OK, 21 WARN, 0 FAIL. I counted the `^(OK|WARN|FAIL) `
  lines (53) and the `^WARN ` lines (21), and `^FAIL ` matched nothing. No
  output line names `held-derived-computation-d7`.

## Findings

1. **[Observed] revise-level: Q5 states the consequences of its arms
   inconsistently. Its recommended arm says "No further step", when the
   same Unknown it attaches to the other arm applies to it too.**
   Q5 asks the owner which reading of accepted RFC2-18/RFC2-19 text
   "should bind" (packet §8, lines 546–568). Its arms say:
   - Arm W (lines 556–562): "Choosing W is the owner ruling on the meaning
     of accepted RFC2-18/RFC2-19 text; whether a plain owner ruling
     suffices for that, or a contract act is needed, is **[Unknown]**".
   - Arm N (lines 551–555, recommended): "Consequence: arm A makes
     unprompted re-observation … lawful at the doctrine level;
     implementation authority stays separate. No further step."

   Choosing N is just as much an owner ruling on the meaning of the same
   accepted text. The packet itself says "the contract supports two
   readings" (§0, line 75) and labels its own reading [Inferred] (§4 RFC2
   row). If a plain ruling may not suffice to fix the reading of an accepted
   contract, that holds for N as well as for W. If it does suffice, W's
   Unknown is unwarranted.

   The packet also contradicts itself on this point elsewhere:
   - §4's merge-chain row (line 293): what stays unlawful can be made
     lawful by "an RFC2 amendment (a contract act) or an explicit owner
     ruling on these two clauses".
   - §6 item 1 (lines 390–391): "an RFC2 amendment or an owner ruling on
     those clauses".

   Both treat an owner ruling on these clauses as sufficient, with no
   Unknown. The ledger's merge-chain row (line 117) says the wide reading
   leaves the headline example "unlawful until RFC2 is amended" and drops
   the owner-ruling alternative entirely.

   The brief asks whether Q5 is "a well-formed owner question with honest
   consequences". The recommended arm's consequence omits a possible
   contract-act step that the packet flags for the other arm, and the
   owner is told three different things about whether a ruling on RFC2's
   meaning suffices. This is the same class as round-2 finding 1: the
   consequence of adoption is misstated.

   Repair: state one position on whether an owner ruling can settle the
   reading of accepted RFC2 text, labelled [Unknown] if it is unknown. Apply
   it symmetrically to N and W, and make §4's row, §6 item 1 and ledger row
   117 say the same. Alternatively, argue why choosing the reading the
   clause states (N) is not an interpretation of accepted text while
   choosing W is.

2. **[Inferred] note: §4.1 does not weigh RFC4's own reading of RFC2-19.**
   `contracts/rfcs/RFC-0004/named-adapters.md` cites RFC2-19 twice as
   governing "ordinary human-triggered observation passes":
   - line 420: "Capture runs inside ordinary human-triggered observation
     passes (RFC2-19)";
   - line 492: "ordinary human-triggered observation passes (RFC2-19)".

   RFC2-19's own wording ("run inside a deliberately triggered
   propagate/sync or observation pass") presupposes that observation passes
   are deliberately triggered. An accepted contract therefore reads RFC2-19
   as describing every observation pass, not only reconciliation
   evaluations. That is evidence on the reading question that §4.1 leaves
   out. The ledger's RFC4 row (line 118) disposes of these lines as
   "consistent: no clock trigger", which answers only the clock question.

   I do not find a sentence made false: a page open is human-triggered, and
   RFC4 says "human-triggered", not "deliberately". But a reader could build
   a third, broader reading from these lines: any held re-observation is an
   observation pass, and RFC2-19 places observation passes inside deliberate
   triggering. Q5's owner should see it. Repair: name these two lines in
   §4.1, and give the ledger row a disposition on the reading question.

3. **[Inferred] note: the page-open residual states a legal effect that
   section 1 does not carry.**
   - §2 (lines 254–256) says the packet "leaves held computation on a page
     open unlawful until an implementation authority supplies" a test.
   - §6 item 7 says the same for a page open "not shown to be human".

   Section 1 makes held computation lawful "when the trigger is a human
   act". It has no showing requirement, and §2's own table lists "a human
   opening a page" as lawful. Whether a trigger was human is a question of
   fact and evidence. "Unlawful until shown" is this packet's reading and
   would not travel with the doctrine bytes if arm A were adopted.

   Q3's strict arm also says "on this arm an implementation must show a
   trigger was human, for a hook and for a page open alike" (lines
   532–534). That ties the page-open burden to Q3's hook arm, although the
   page-open requirement comes from section 1's "human act" whichever way
   Q3 is answered.

   Section 1's text is not changed and nothing claims a test exists, so
   the brief's two direct checks pass. Repair: label the "unlawful until
   shown" sentence as the packet's reading or an implementation obligation,
   and make Q3 say that the page-open burden does not depend on its arm.

4. **[Observed] note: two cross-references in the ledger are stale, and one
   line range is off by one.**
   - Ledger §5 item 1 (line 215) says "By packet §6.1 the hook is not
     lawful", but the hook is now packet §6 item 2.
   - Ledger row 126 says "(packet §6.2)" for the regeneration rehearsal,
     which is now item 3.

   Both references were right at `fc46ec4`, where §6 item 1 was the hook
   (packet line 222) and item 2 the rehearsal (line 242). They went stale
   when the round-1 repair inserted the new item 1, and round 2 did not
   catch them.

   Packet §4.1 cites "the merge facts carried by RFC2-1 items 1 and 3" at
   line 146. The quoted "the" is at the end of line 145, so the range is
   145–146.

   All three are trivial fixes.

5. **[Observed] note: the cycle-2 repair left two lines unwrapped.**
   - Packet line 515 is 128 columns ("…drafter's, and the owner has taken
     the interpretation route before; this packet recommends against it.
     Cheaper and reversible;").
   - Ledger line 153 is 123 columns ("…capture the merge of a materialized
     work item (packet §4.1). A sentence elsewhere that confines
     computation to a deliberate").

   Both came from the cycle-2 edits (see the diff from `8f1fbec7`). Every
   other prose line in these two files is at most 93 columns. Nothing
   wrongly applies, and neither line is inside a code span, so no citation
   is split.

6. **[Observed] note: the warrant for round 3 is not recorded, and the
   recorded direction still says the opposite.** At the reviewed commit,
   `decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2026-10-14.md` lines 82–84
   still read "The other eight are `REVISE` and go to the owner with their
   findings open. Under the stopping rule none is repaired again and no
   further round is dispatched". The package cites the further direction
   only as "[Observed: as relayed; not yet recorded under `decisions/`]"
   (brief line 106, packet lines 26–27, `ROUND-2-DISPOSITIONS.md` lines
   50–51).

   The label is honest. But the stopping rule this round runs under rests
   on a direction that no file under `decisions/` records. The package
   discloses this and leaves it to the lead session
   (`ROUND-2-DISPOSITIONS.md` lines 91–94). It is recorded here so that the
   owner sees it before relying on any outcome of this round.

## Answers to the brief's Round 3 questions

- Each of the eight round-2 findings is repaired as `ROUND-2-DISPOSITIONS.md`
  §"Repairs" says. Findings 2, 4, 5, 6, 7 and 8 are fully repaired. Finding
  3 is repaired, with a residual wording issue (note 3). Finding 1 is
  repaired in structure and in what the sections say arm A permits, but the
  new Q5 brings a new inconsistency about what the owner must do (finding
  1). The repairs also brought two unwrapped lines (note 5). Stale
  cross-references from round 1 survive (note 4).
- Finding 1: both readings are stated fairly. The relied-on reading is
  labelled and argued. §0, §2, §4, §6, the ledger and the delta agree on
  what arm A permits on each reading. Q5 is not yet well-formed on the
  consequences of its arms (finding 1). §4.1 leaves out RFC4's reading of
  RFC2-19 (note 2).
- Finding 2: I re-ran the sweep at `66d42d09`: 417 files and 11 readers by
  two methods, with the enumeration summing to 11.
- Finding 3: the residual is named without changing section 1, and nothing
  claims a test exists (note 3).
- Dated status marks: they sit at the stale sentences, with the old text
  kept. None is left unmarked inside the package. Outside it, see note 6.
- Section 1's bytes are unchanged from those round 2 read, and the anchors'
  sha256 values hold.

Under the brief's stopping rule this `REVISE` goes to the owner with its
findings open. There is no further repair and no round 4 without a new owner
direction.

Revise-level findings: 1 (1). Notes: 5 (2–6).
