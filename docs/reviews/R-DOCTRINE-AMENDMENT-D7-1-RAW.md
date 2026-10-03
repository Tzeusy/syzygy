# Review - D7 doctrine amendment packet (held derived computation, P-101)
Reviewed commit: fc46ec4169a19109631832f5f1783210955fea25
Package digest: de326819b0a76c3fc3b5996dde2ee3d4d2c3e86e3dc5a2235e733d4dbb7f42ea
Verdict: REVISE

Reviewer: one fresh-context agent, no access to the drafting session. Brief:
`.syzygy/governance/contracts/candidates/doctrine-amendment-held-derived-computation-d7/REVIEW-BRIEF.md`.
Method: a clean clone checked out at the reviewed commit; package digest
computed by the brief's method in that clone; every digest below scripted
(`sha256sum`), every sweep re-run with Python `re` and confirmed with
`git grep`. Nothing outside the clone was read except the worktree path
this file is written to; no Butlers repository was read.

## What was confirmed

- [Observed] Anchor digests at `66d42d09` and at the reviewed commit are
  identical and match the packet: `vision.md` 93cc5fbb…, `architecture.md`
  d1987f7f…, P68-P83 decision a59294d4…, RFC-0005 admission-and-boundary
  a742a77f…, RFC-0002 reconciliation-chain 7d7f876b… (full values compared
  by script, not transcribed). The commit adds only the four package files.
- [Observed] The quoted anchors are exact: `vision.md` 105–107, and
  `architecture.md` 329–334. Quotes of RFC2-19 (245–247), RFC4-16
  (433–435), RFC5-11 (320–323), P-69, P-71 Q3, P-71-Q5, P-79 Q4 and Q6,
  the M2 funnel Q4 ground, the M4 funnel Q3 arm (b), the bounded-mission
  interpretation act and the trusted-bootstrap observation direction match
  their sources. `v1.md` line 89 ("Human-triggered propagation…") and line
  103 (deferral row) are as cited.
- [Observed] Ledger §1 re-run: population 1,536 files; 95 hit files, 346
  occurrences; `git grep -l -i -E` returns 95. Lane split reproduces exactly
  (doctrine 3/5, accepted 4/12, decision 5/7, spec 5/5, candidate 13/51,
  other 10/30, evidence 15/141, raw 27/61, historical 13/34).
- [Observed] Ledger §2 re-run: 229 files, 1 hit
  (`decisions/PROCESS-LESSONS.md`). A wider sweep (`alert`, `notify`,
  `push notification`, `email`, `webhook`) over doctrine, accepted RFCs,
  decisions and `openspec/` at the reviewed commit also returns 0.
- [Observed] "held derived computation" occurs in 0 tracked files at
  `66d42d09`; the two doctrine digests are cited only by the three files of
  `docs/evidence/polaris-understanding-reconciliation-2026-09-28/`; the
  2026-10-03 roadmap has 0 case-insensitive `fleet` matches; the amendment
  log holds D1, D5, D6. All relative links in the package resolve.
- [Observed] `python3 scripts/check_governance.py` in the clone: 31 OK,
  21 WARN, 0 FAIL (52 checks).

## Findings

1. **[Observed] revise-level — the packet classifies D7 two incompatible
   ways, and arm B rests on the classification the delta rejects.**
   `SEMANTIC-DELTA.md` lines 22–30: "It is not Clarifying: the current text
   does not *already* admit the class … D7 adds a trigger, not that it
   reveals one." Packet §7 (lines 269–271): "D7 clarifies what
   'human-triggered' admits for a closed set of non-deciding effects".
   Packet Q1 arm B (lines 286–288): an interpretation act "recording that
   existing doctrine admits the section 2 class". If the Normative claim is
   right, arm B asks the owner to record as existing meaning something the
   packet says existing meaning does not contain — which is the
   "reinterpretation" the anchor bullet itself names as the forbidden route.
   The bounded-mission interpretation act is not a parallel: D3's own
   packet called its change a clarification of trigger grain. Repair: either
   state that choosing B is the owner ruling the change Clarifying (and say
   what that does to the delta's class), or drop "clarifies" from §7 and
   explain why B is still lawful for a Normative change.

2. **[Inferred] revise-level — the "beyond" arm's consequence is misstated
   for arm B.** Q2 (lines 300–302): "'Beyond' makes an adjudication RFC a
   precondition of arms A and B." Under "beyond", the anchor text says such
   autonomy "is licensed only through the mechanism VIS-4 names, never by
   reinterpretation", and VIS-4's mechanism includes "the owner's explicit
   doctrine amendment". Arm B is by definition no doctrine amendment and is
   an interpretation, so under "beyond" B is unavailable outright, not
   available with an RFC added. D3 §6 states the analogous consequence
   correctly ("no `vision.md` insertion is lawful without an accepted
   adjudication RFC"). The packet also does not say that the adjudication
   RFC VIS-4 describes is defined for the spec-adoption gate (adversarial
   independence, ambiguity determination, revertability), so whether any
   such RFC could serve a trigger question is itself open.

3. **[Inferred] revise-level — the proposed text pre-answers Q2, the exact
   defect RC-7 F10 judged blocking for D3.** The first inserted sub-bullet
   is headed "**Held derived computation is not autonomy.**" — a
   classification stipulated in doctrine text, inside the one bullet whose
   second half forbids settling that question by reinterpretation. D3 §6
   records RC-7 F10's disposition, "closes by an owner ruling, not only by
   text", and the D4 ruling designated the reason-stating wording for that
   reason. Here Q2 is asked after Q1, nothing says Q2 must be ruled first,
   and nothing says what arm A's text becomes if Q2 is answered "beyond"
   (the heading would then be false doctrine). The text also states no
   reason in the D4-designated style (e.g. "…delegates no decision and is
   for that reason inside VIS-4's stated bounds"). Repair: order Q2 before
   Q1, and either make the heading reason-stating or state that arm A's text
   is lawful only on a Q2 "inside" ruling.

4. **[Inferred] revise-level — RFC2 binds the core page-open trigger, not
   only the hook, and the ledger misses one of the clauses.** RFC2-19:
   "reconciliation evaluations run inside a deliberately triggered
   propagate/sync or observation pass". RFC2 reconciliation-chain line
   155–157 (not in the ledger; the predicate does not reach it):
   reconciliation-pending "attaches automatically and deterministically at
   the first evaluation that captures the merge fact (inside RFC2-19's
   deliberately triggered passes — never on a live merge event)". D7's
   result is "a new identified evaluation", and packet §2 defines the
   unprompted case as one where the human act "was not a request for that
   computation" — so a page-open re-observation is, by the packet's own
   definition, not a deliberately triggered pass. Either D7 evaluations may
   never capture a merge fact or carry a reconciliation evaluation (stated
   nowhere), or arm A leaves an accepted contract forbidding D7's own
   headline example. The architecture insertion's "is not a pass of this
   loop" does not resolve it: RFC2 binds evaluations, and observation is a
   named stage of the loop. Packet §4 and ledger §3 present RFC2-19 as
   binding "the hook option" only; the ledger's "No authority-lane sentence
   is made false by arm A" is untested against line 157. Repair: extend §4's
   RFC2-19 row (and §6) to the page-open trigger, or narrow the D7 class so
   it excludes merge-fact capture and reconciliation evaluation.

5. **[Observed] revise-level — the proposed text is narrower in its
   prohibitions than §2's table, so it can be read to license what the
   table forbids.** The table's Unlawful trigger column includes "a timer,
   schedule, poller **or file watcher** inside Syzygy"; the text's clock
   sentence is "**A clock Syzygy owns is never a trigger:** no timer,
   schedule, poller, or wake Syzygy sets for itself." A file watcher is not
   a clock, and when it fires on a human editing a file the text's
   permission ("when the trigger is a human act") is literally met — and it
   is not "a hook a human installed by hand". The M2 funnel Q4 named "a
   timer, poll or file watcher inside the daemon" as one unauthorized arm,
   so the omission is load-bearing. Lesser gaps of the same kind: the table
   forbids "reprioritize work" and "set its own next trigger", and defines
   notify to include an interrupting badge; the text says only "dispatches
   work", "wakes itself" and "notifies". Repair: name any watcher or
   listener Syzygy sets, and bring the effect list into the text.

6. **[Inferred] revise-level — the "new identified evaluation" disjunct lets
   non-rebuildable content be held, contrary to §6.2.** The text: "It is a
   new identified evaluation or data rebuildable from its inputs (VIS-6)".
   §6.2 says a held generated draft (model output) "may not be held as
   Syzygy-only state" because it is not rebuildable — but that argument
   addresses only the second disjunct. Nothing in the text restricts what a
   "new identified evaluation" may contain, and VIS-6(b) exempts
   evaluation-identified observation records from rebuildability, so model
   output recorded under an evaluation identity satisfies the text
   literally. Repair: bound the first disjunct (e.g. an evaluation of
   observed state under RFC2's evaluation rules) or state the exclusion in
   the text.

7. **[Inferred] note — the text bounds writes, egress and execution but not
   reads.** "Syzygy may observe …" with "opens no write, egress, or
   execution path that is not separately authorized" leaves read authority
   (per-repository consent, content class, the PWB-REQ-005 body-read gate)
   unmentioned; §2's "Paths it opens" row likewise omits reads. Acts in force
   still gate reads, so nothing is made lawful today, but a reader of the
   doctrine alone sees an unqualified doctrinal licence to observe. Adding
   "read" to the list closes it.

8. **[Inferred] note — the "stage a draft" row overstates the precedent's
   width.** P-71 Q3 arm (b) is "a pure drafter that writes no file" which
   "emits packet *data* on request … an operator command renders it". D7
   stages and *holds* the draft until a human next looks, which implies
   persistence in Syzygy's state. "Keeps arm (b)'s width" is true of governed
   trees but not of "writes no file at all".

9. **[Inferred] note — the "hold" row's precedent is nominal.** The row maps
   hold to VIS-6(a) and P-79 Q4 (the owner's own unpromoted note), then
   says D7 "does **not** stretch VIS-6(a)". The actual footing is VIS-6's
   general projection rule; VIS-6(a)/P-79 Q4 do not license holding a
   computed result. Say so instead of citing them as the licence.

10. **[Observed] note — §1.3 describes D3's `vision.md` edit by its rev1
    §1.2 text, not the designated one.** D4-RULING-DECISION.md designates
    "the reviewer's reason-stating §1.2 wording" (D3 §6) as the text act 5
    would carry; that wording replaces the semicolon form with separate
    sentences, so "a parenthetical after 'human-triggered', before the
    semicolon" is stale. The composition conclusion (different bytes, append
    after the bullet's last line, re-anchor by fresh review) still holds.

11. **[Observed] note — §7's attribution.** "in the D4 ruling's reading,
    delegation of an always-human decision class" — the D4 ruling file
    contains no such reading; the phrase is D3's packet position (D3 lines
    37–39), on which D4 ruled for bounded missions only. Cite D3 for the
    reading and D4 for the mission ruling.

12. **[Observed] note — two sweep-coverage gaps in the ledger.** (a) The
    trigger predicate misses the wrapped "and not\nautonomous." at
    `vision.md` 86–87, the section intro directly above D7's anchor; a
    whitespace-tolerant re-run over the same 1,536 files finds this as the
    only authority-lane wrap miss. (b) The predicate has no bare
    `autonomous behavior` form, which is the exclusion wording of many acts
    in force (e.g. `POLARIS-PROJECT-WIDE-SPEC-SIGNOFF-ACT.md` line 58,
    `PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md` lines 134–135, the POC
    and PWB proposals' out-of-scope lists). D7 does not falsify them, but by
    declaring a class "not autonomy" it narrows what those exclusions catch;
    the delta's "any new daemon behaviour still needs its own authority" is
    the mitigation and should be tied to that population. (c) §4's
    derived-artifact sweep covers `scripts/` and YAML only; a wider sweep
    finds `apps/three-surface-poc/src/polaris-generation/self-corpus.ts`
    reading the doctrine root, at a pinned revision, so unaffected — no
    consequence found, but the stated population is narrower than the claim.

13. **[Observed] note — the delta says "VIS-4, VIS-5 and VIS-6 are cited by
    the new text"** (SEMANTIC-DELTA line 19–20); the inserted text cites
    VIS-5, VIS-6, SEC-2 and SEC-3, and not VIS-4.

14. **[Observed] note — undisclosed departure from N14's scope.** The
    pursuit's N14 "What" asks for "one amendment to VIS-4 and the 'Not
    autonomous' clause"; the packet amends the bullet and the loop
    paragraph and leaves VIS-4 untouched. That is probably the better shape,
    but the packet should say it departed and why.

15. **[Observed] note — the `architecture.md` insertion is "verbatim" and
    "rewrapped … on application"**, so the post-application bytes are not
    fixed by the reviewed text, and §9 step 1 says "apply … verbatim". Give
    the rewrapped resulting paragraph so the applied bytes are what a review
    saw (rule 10).

16. **[Observed] note — packet lines 13–14** say D3 is "in this directory";
    it is in the parent, `contracts/candidates/`.

17. **[Inferred] note — entry criteria.** E1, E2, E4, E5, E6 each carry a
    concrete test and stay off doctrine as claimed (Q4's v1.md alternative
    is not drafted). E3 ("the trigger boundary is on record") is a
    governance-record gate rather than a capability prerequisite for
    watching fleets live, and its rationale ("live watching is a trigger
    question") is asserted, not argued: live observability is watching
    agent work, which needs no unprompted Syzygy computation if a human
    opens the view. The owner may reasonably drop it.

## Answers to the brief's questions

- Change class Normative: agreed; the non-expansion section is honest that
  D7 adds the trigger, but §7 and arm B contradict it (findings 1, 2).
- Quoted text, anchors, line numbers, sha256: all checked and correct
  except the D3 description (10) and the D4 attribution (11).
- Text versus §2's table: the text is narrower in prohibitions and wider in
  the evaluation disjunct (5, 6, 7).
- VIS-4 bounds: argued, but the text stipulates the answer and the "beyond"
  consequence is wrong for B (2, 3).
- RFC2-19: binds more than the hook (4); no other in-force sentence found
  made false, subject to 12.
- Composition with D3: holds mechanically (10).
- Entry criteria: testable, off doctrine; E3 questionable (17).

Revise-level findings: 6 (1–6). Notes: 11 (7–17).
