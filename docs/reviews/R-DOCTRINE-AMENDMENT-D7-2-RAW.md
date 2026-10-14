# Review - D7 doctrine amendment packet (held derived computation, P-101) — round 2
Reviewed commit: 8f1fbec7723a4e60b8c00f03f260a1979e3d7738
Package digest: 63f16c10a03f34a91eac5499261dd42c0a7b8c834d954ca386d1fd8eb79f377d
Verdict: REVISE

Reviewer: one fresh-context agent with no access to the drafting or
round-1 sessions. Brief:
`.syzygy/governance/contracts/candidates/doctrine-amendment-held-derived-computation-d7/REVIEW-BRIEF.md`
(unchanged since round 1; it still titles itself round 1 and sets a
one-round stopping rule — see note 8). Also read: the round-1 raw
`docs/reviews/R-DOCTRINE-AMENDMENT-D7-1-RAW.md` and the package's
`ROUND-1-DISPOSITIONS.md`. Method: a clean worktree with
`git rev-parse HEAD` equal to the reviewed commit and an empty
`git status --porcelain`. The package digest was computed by the brief's
command in that worktree (five tracked files, now including
`ROUND-1-DISPOSITIONS.md`). Every digest below was scripted (Python
`hashlib`), every quote was checked by script against its source (exact,
or exact after whitespace normalization for wrapped quotes), and every
ledger sweep was re-run at `66d42d09` with Python `re` over
`git ls-tree -r -z` / `git show`. No Butlers repository was read.

## What was confirmed

- [Observed] Anchor digests at the reviewed commit match the packet and
  delta: `vision.md` 93cc5fbb…, `architecture.md` d1987f7f…, the P68–P83
  decision a59294d4…, RFC-0005 `admission-and-boundary.md` a742a77f…,
  RFC-0002 `reconciliation-chain.md` 7d7f876b… (full values compared by
  script). No doctrine byte is edited (acceptance criterion 5).
- [Observed] Anchors are exact: `vision.md` 105–107 and `architecture.md`
  329–334. The resulting `architecture.md` paragraph in §1.2: its first
  five lines equal the anchor's lines 329–333 byte for byte, its sixth line
  begins with the anchor's line 334. The two `markdown` blocks in
  `SEMANTIC-DELTA.md` are byte-identical to the packet's, both NFC, no line
  over 78 columns.
- [Observed] Quotes checked against source and found exact: the D4 ruling's
  designation sentence (lines 17–18, wrapped), D3 line 38 "delegation of the
  always-human decision", N14's "one amendment to VIS-4 and the 'Not
  autonomous' clause" (pursuit line 301), the bounded-mission act sentence,
  P-69 (line 56), P-71 Q3 arm (b) and P-71-Q5 (58–59), P-79 Q4 and Q6 (67),
  the M4 funnel's arm (b) (115), the M2 funnel's Q4 arms and ground (48),
  the trusted-bootstrap direction (34, 41), the PWB continuation act
  (134–135), VIS-4's adjudication-RFC definition (177–179) and "the owner's
  explicit doctrine amendment" (180), VIS-6's projection rule (232), the
  mandate sentences (302, 306), `v1.md` 89 and 103, RFC2-19 (245–247), RFC2
  155–157, RFC4-16 (432–435). The pursuit data file carries every cited
  finding and move id (L11-F1, L11-F8, L10-F3, L4-F2, L11-M5, L10-M6,
  L4-M4).
- [Observed] Ledger sweeps re-run at `66d42d09`
  (`66d42d090e7966812f397bb38760b70bc9e63ac6`), package excluded: §1 1,536
  files, 95 hit files, 346 occurrences, every lane figure reproduced
  exactly; §1a wrap-tolerant 95 files, 348 occurrences, the two extra hits
  being `doctrine/vision.md` and
  `round-2026-08b/reviews/RC-2-vision-polaris-RAW.md`, as stated; §1b 212
  files, 10 hits, the same ten files listed; §2 229 files, 1 hit
  (`decisions/PROCESS-LESSONS.md`); §4 417 files, 11 readers (but see
  note 2 for the breakdown).
- [Observed] `python3 scripts/check_governance.py` at the reviewed commit:
  32 OK, 21 WARN, 0 FAIL (53 checks); no finding names the package path
  (0 matches for `held-derived-computation-d7` in the output).

## Round-1 findings, checked against the repaired bytes

- R1-1 (class contradiction) — **repaired.** §7 now states Normative;
  arm B says choosing it is the owner ruling the change Clarifying,
  contrary to the packet; the delta's class paragraph agrees. Residual
  overstatement in note 6.
- R1-2 ("beyond" consequence) — **repaired.** §7 and Q1 say arm B is
  unavailable on "beyond", arm A needs an accepted adjudication RFC and a
  redraft, and whether VIS-4's spec-gate RFC can serve a trigger question
  is [Unknown]. Matches VIS-4 lines 174–180.
- R1-3 (text pre-answers the bounds question) — **repaired.** The heading
  is reason-stating; the bounds question is Q1, ruled first; §1's "Order of
  rulings" makes the text lawful only after "inside". This is the D4
  pattern (ruling first, reason-stating text designated by it).
- R1-4 (RFC2 binds more than the hook) — **repaired in structure, but the
  repair over-reads the clause** (finding 1 below).
- R1-5 (watcher and effect gaps) — **repaired.** "clock or watcher", "file
  or event watcher", "dispatches or reprioritizes", "sets its own next
  trigger" are in the text; the table's extra "approve, sign or label
  accepted" is covered by the first sub-bullet's "nothing more" and by
  VIS-4.
- R1-6 (model output via the evaluation disjunct) — **repaired.** "a new
  identified evaluation of observed state … and never model output".
- R1-7 through R1-17 (notes) — each repaired as the dispositions say,
  checked at the cited lines; exceptions are notes 2 and 4 below
  (R1-12 and R1-15 repairs carry small new inaccuracies).

## Findings

1. **[Inferred] revise-level — the repair of R1-4 reads RFC2's "merge
   fact" as any merge in a repository's history, which overstates what
   arm A leaves unlawful and misstates the consequence of adoption.**
   Packet §0 (lines 54–60): "RFC2 requires every evaluation that captures a
   merge fact to run inside a deliberately triggered pass … an unprompted
   re-observation of a repository whose history carries a merge — which is
   most of them — stays unlawful even after D7." §2 (lines 199–201) and §6
   item 1 (276–279) repeat the scope. But the clause the repair cites sits
   under RFC2-18, whose scope is stated: "**RFC2-18 — The chain.** Every
   materialized work item that reaches merge enters a first-class chain on
   its durable identity" (`reconciliation-chain.md` line 141–142), and
   "**merged** is execution state: the change reached the integration
   branch" (153). RFC2-17 reserves "reconciliation" for "the post-merge
   evaluation of whether a merged change satisfies the intent revision that
   warranted it" (122–124), and RFC2-19 binds "reconciliation evaluations"
   (245–246). On that reading the confinement reaches an evaluation that
   captures the merge of a *materialized work item*, not any repository
   whose git history contains a merge commit. For a repository with no
   materialized work in the chain — plausibly the one Butlers repository
   the POC observes, where dispatch is not authorized — arm A plus
   "relaxes no contract" would make unprompted re-observation lawful at the
   doctrine level (implementation authority still separate), which is the
   opposite of what §0 and §6 item 1 tell the owner. The wider reading is
   not impossible (RFC2-1 item 1 snapshots every repository, and "merge
   fact" is not separately defined), but the packet adopts it silently and
   adds "which is most of them", which round 1 did not say. The brief asks
   whether the text "could be read to license an effect the packet says it
   [does not]"; here it can. Repair: state both readings of "merge fact"
   with RFC2-18's scope sentence, label which the packet relies on, and
   restate §0, §2's "unprompted" paragraph, §4's two RFC2 rows, §6 item 1
   and the ledger's two RFC2 rows (110–111) so the owner sees what arm A
   permits for a repository with no materialized merged work.

2. **[Observed] note — the ledger §4 reader breakdown does not sum to its
   own figure.** The sweep returns 11 readers, reproduced. The prose
   accounts for them as "the two generators and the two scripts in the
   table; `scripts/check_governance.py`; five tests and one script …; and
   the self-corpus row". Only one generator,
   `scripts/build_directive_register.py`, is a predicate hit;
   `build_contract_index.py` is not among the 11. "Five tests" names four
   (`git-blob-batch.test.ts`, `req-023`, `req-061`, `req-integration`);
   the fifth test hit is `self-corpus.test.ts`, which the table puts in the
   self-corpus row. Enumerated: directive-register builder 1, table scripts
   2, check_governance 1, fixture tests 4, `polaris_generator_approval.py`
   1, self-corpus pair 2 = 11. Say that the contract-index generator was
   found by another route (or is not a reader), and correct "five".

3. **[Inferred] note — the page-open trigger has the same human-versus-agent
   problem Q3 addresses for hooks, and no test.** The text requires "the
   trigger is a human act". A page open by an agent (this repository's own
   CDP sweeps hit `/polaris`) or by a scheduled `curl` someone else owns is
   not a human act, so the text forbids held computation on it — but the
   daemon cannot tell the two apart, and an external loop hitting the page
   is a poller by proxy that P-69 and the "clock or watcher" sub-bullet aim
   at. Q3 makes hooks fire "only on a human act"; nothing in §2, §6 or the
   entry criteria says how a page-open trigger shows it was human. Relatedly,
   §2's Trigger row lists "a commit" as a human act without qualification;
   an agent commit is not one, and Syzygy can only learn of a commit
   unprompted through a hook (Q3) or a watcher (forbidden). Name the
   residual, or qualify the examples.

4. **[Observed] note — §1.2's description of its own bytes is incomplete.**
   "the first five lines are unchanged and the sixth line is extended"
   (packet lines 134–135, repeated in disposition 15): the resulting
   paragraph is ten lines; the sixth is extended and lines 7–10 are added.
   The exact bytes are given, so nothing applies wrongly; the sentence
   should say so.

5. **[Observed] note — RFC5-11 cited at lines 320–323** (packet §3);
   line 320 is blank; the quoted words sit on 321–323. Carried unchanged from
   round 1; trivial.

6. **[Inferred] note — arm B's defect is slightly overstated.** Q2 arm B:
   "B records as existing meaning something the text does not contain —
   the 'reinterpretation' the bullet forbids." The bullet forbids
   reinterpretation only as a licence for "autonomy beyond VIS-4's stated
   bounds"; B is available only after a Q1 "inside" ruling, where that
   prohibition does not reach. B's real defect, if the packet's class is
   right, is a misrecording of existing meaning (it treats a Normative
   change as Clarifying), which the same paragraph already states. Drop or
   qualify the "the bullet forbids" clause.

7. **[Inferred] note — the "Not autonomous" section intro (vision.md
   86–87) stays true only on the packet's own classification.** The ledger
   row (line 107) says so; good. Recorded here only because, under finding
   1's narrower reading, D7 licenses more unprompted computation than the
   packet describes, and "not autonomous" then carries more weight than
   the row's argument assumes.

8. **[Observed] note — this round departs from the recorded stopping rule,
   and several sentences go false with it.** `REVIEW-BRIEF.md` lines 9–12
   ("One round … no round 2 is dispatched"), packet lines 14–16 ("no round
   2 was dispatched: these repaired bytes are unconfirmed"), delta lines
   8–9 and 234–236, and dispositions lines 16–18 say no second round
   exists. This raw is one. Whoever dispatched it should record the
   departure and its warrant beside the dispositions, and the next repair
   should mark those sentences at the sentence (not with a page banner);
   the brief and the round-1 raw are not edited.

## Answers to the brief's questions

- Change class Normative: agreed; §3 and §7 are now honest that D7 adds
  the trigger (R1-1 repaired; residual note 6).
- Quotes, anchors, line numbers, sha256: all checked and correct except
  the small line-range slip in note 5 and the self-description in note 4.
- Text versus §2's table: now aligned row by row; the "nothing more"
  closure covers the table's extra adoption words. The open question is
  what the "relaxes no contract" clause leaves lawful (finding 1) and how
  "human act" is shown for page opens (note 3).
- VIS-4 bounds and the "beyond" arm: argued, ordered first, and the
  consequence is now stated correctly for A, B and C.
- RFC2-19: the repair binds every trigger, as round 1 asked, but reads the
  merge-fact scope wider than RFC2-18 states (finding 1). Ledger sweeps
  re-run and reproduced; no other in-force sentence found made false.
- Composition with D3: holds; §1.3 now describes the designated wording
  and quotes the D4 ruling correctly.
- Entry criteria: E1, E2, E4–E6 testable and off doctrine; E3's
  withdrawal is argued.

Revise-level findings: 1 (1). Notes: 7 (2–8).
