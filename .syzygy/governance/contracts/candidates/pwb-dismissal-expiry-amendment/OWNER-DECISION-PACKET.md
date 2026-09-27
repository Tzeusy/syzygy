# Owner decision packet — dismissal with a live expiry

> **Inert draft.** This packet performs nothing. It records no act,
> authorizes no implementation and changes no signed byte. A commit, review,
> merged pull request, passing check, silence or general approval performs no
> act. The phrase below is kept only so governance checks can see it go
> stale; it is not offered until the exact bytes pass a fresh independent
> review.

Date: 2026-09-26; repaired 2026-09-27 after review rounds 1, 2 and 3 (all
REVISE; see the review record at the end). Gate bead: `syzygy-dov.29`
(P-79 question 5, M12 slice 4).

Warrant: your 2026-09-21 answer to P-79 question 5, which reads "dismissal
is an amendment — CC-REV-2 delta plus a new act before any dismissal touches
a tuple". Reading that answer as a direction to draft this delta is the
drafter's reading [Inferred]; the answer itself requires a delta and an act,
and is not an act.

Manifest: `PWB-DISMISSAL-EXPIRY-MANIFEST.txt`, eleven rows over the signed
PWB behavior subject. Six rows hash proposed bytes and five hash current
bytes.

Manifest SHA-256:
`9f4063d303e75b893bc7348df0aef9e5e84c381df6ae98b3d15b4b7c22af9838`

The builder writes the manifest; this digest was computed from it by script.
Any change to a patch, the manifest or the subject retires it.

## What you would be deciding

Whether PWB-REQ-007 should admit one thing it is silent on today: a recorded,
reasoned, expiring human dismissal of an Unknown claim.

Under the drafted text:

- only a dismissal record committed to the governed plane can dismiss a claim
  — never a view setting, browser or daemon state, a note, or a model;
- every such record present when an evaluation takes its snapshot is an
  input of that evaluation, so an evaluation cannot skip one;
- only Unknown claims can be dismissed, and never a contradiction waiting for
  your adjudication or a claim held by an open challenge;
- each evaluation decides whether a dismissal is in effect at its own as-of
  instant: in effect only while that instant is before the expiry, so a
  dismissal ends only when a new evaluation runs — a page never flips on its
  own when the clock passes the expiry;
- the claim still shows everything it showed before (its Unknown label,
  reason, route, freshness and identities), with the dismissal's reason,
  expiry and author beside it, on the same page and without an extra click,
  the same in the human and machine views;
- no tuple value changes; a dismissed claim stays in every label, tier,
  freshness and reason count (so in every Unknown count) and is also counted
  separately as dismissed, and no count treats it as resolved or good;
- a record that dismisses nothing is shown as exactly one of three things,
  checked in this order and shown as the first that fits: **refused**
  (incomplete, or itself tries to dismiss a reason that may not be
  dismissed — never because of what has happened to the claim), then
  **bound to a retired identity** (the evaluation records that the claim it
  named was split or merged away; a new record is needed for the
  successor), then **lapsed** (its expiry has passed, the evaluation no
  longer shows the claim it names — for example because the declaration
  behind it was deleted — or the claim's reason is not the one it named,
  even when that reason may not be dismissed). A lapsed record says which
  of these tests failed; it does not say whether it ever took effect, so a
  record that never matched its claim is shown the same way as one whose
  claim changed;
- if the dismissal records cannot be read, or no home for them has been
  chosen (question 2), nothing is dismissed and the dismissed count is shown
  as Unknown, never as zero;
- if two records are in effect for the same claim, both are shown beside it
  and the claim is counted once as dismissed.

The full reasoning, with every contract clause quoted, is in
`SEMANTIC-DELTA.md`.

## Open questions for you

1. **Which arm?** The draft keeps the tuple unchanged and shows the dismissal
   as the `dismissed-by-decision` sibling state beside it. Your P-79 words
   say "before any dismissal touches a tuple"; this arm never touches one.
   The M12 funnel's Q5 row names three arms: (1) an amendment that widens
   the challenge-state vocabulary so a dismissal lives inside the tuple;
   (2) a dismissal beside the tuple, leaving every tuple byte unchanged;
   (3) do not build slice 4. The draft is closest to arm 2, but written as
   an amendment, as your P-79 answer requires. The funnel says arm 2 is
   "exactly the 'view filter over a rendered list' shape L2-M8 argues would
   violate VIS-6(a)". The draft answers that objection by letting only a
   governed-plane record dismiss; it survives only if no governed-plane home
   for records is chosen (question 2), and then nothing can dismiss at all.
   [Inferred; the full argument is in `SEMANTIC-DELTA.md`.] Does the drafted
   arm answer what you asked?
2. **Where do dismissal records live, and who writes them?** The draft says
   only "committed to the governed plane", and does not say whose. Two
   readings are possible [Inferred]: Syzygy's own governed files, which
   Syzygy could one day write to; or the observed project's governed plane,
   which is how the M12 funnel reads VIS-6(a) promotion, and which Syzygy may
   not write to. Your question-4 answer reads "write act deferred", and this
   package gives Syzygy no way to write a record. Which path should the records use,
   and do you author them by hand until a write act exists?
3. **Who may dismiss?** The draft requires an attributed human author. With
   multi-user support forbidden, the only author today is you. Should the
   text say "the owner" rather than "a human"? RFC1-12 says "re-dismissal is
   an owner act", so the coverage row for that part (RFC1-12.r3) stays
   `unknown-uncovered` until you answer.
4. **Which claims may be dismissed?** The draft says Unknown claims only,
   excluding contradictions. The contracts speak of dismissing a *gap*; the
   draft reads an Unknown PWB claim as the gap it discloses. That reading is
   an inference: the contracts give claims and gaps separate identities. Until
   you answer, three coverage rows that would credit the gap clauses
   (RFC1-20.r1, RFC1-25.r1, RFC2-15.r1) stay honestly Unknown. Is the reading
   right, and should Inferred claims also be dismissable?
5. **Expiry bounds.** The draft requires an explicit expiry instant and sets
   no maximum and no minimum. Do you want a longest allowed dismissal, or a
   rule against an expiry already in the past when the record is written?
6. **When is a reason still current?** The draft says a dismissal's reason
   stays current only while the claim's primary Unknown reason is the one the
   record named. So if the claim becomes Unknown for a different reason, the
   dismissal stops applying at the next evaluation. Is that the rule you
   want, or should reasons be judged some other way?
7. **Retention.** Your 2026-09-23 retention direction keeps, per claim, only
   the claim identity, the tuple and the challenge state, and commits no
   record to a governed plane. The draft's first scenario says a retained
   evaluation, re-read after the expiry, still shows the claim dismissed. A
   dismissal is in none of the three kept fields, so that works only if the
   dismissal record's bytes stay reachable from the retained evaluation for
   as long as it is kept, or if a fourth field is kept. Is either of those a
   retention change needing its own direction? (Under the challenge-state
   arm the dismissal would sit inside a kept field, which is plainly a
   change to what is retained.)
8. **What does a dismissal render as?** The draft shows the words *dismissed
   by decision* in place of the claim's status, with all the facts, the
   reason, the expiry instant, the author and the record identity beside it,
   and a separate count in aggregates. Is anything missing, such as the
   decision date?
9. **Is PWB-REQ-001 affected?** The draft makes dismissal records inputs of
   evaluation, and PWB-REQ-001 governs evaluation inputs. The draft leaves
   PWB-REQ-001 unchanged and marks "decisions affecting precedence" as honestly
   uncovered (RFC2-1.r2). Should PWB-REQ-001 be amended too?
10. **Landing order.** You fixed `.21 → .30 → .22 → lane B`. This package
    proposes `.20` then `.18` after that, and itself **last** [Inferred];
    the builder shows the spec patch composes when applied in the order
    `.21`, `.30`, `.22`, `.20`, then this one. Whichever of this package and
    lane B lands second must first be regenerated with `--write` and
    re-reviewed, and the same holds after `.20` and every sibling whose
    generated dependencies file collides with this one. Is last the position
    you want?
11. **Implementation authority.** Signing this amends the specification only.
    Would building slice 4 need a fresh implementation authorization or a
    continuation direction, given the continuation act's trigger "a further
    amendment to the signed PWB specification beyond the 2026-09-05 package"?
12. **Claims held by an open challenge.** The draft refuses a dismissal of a
    claim whose reason is `challenge-suspended`: such a claim leaves that
    state only when its challenge is resolved, and a dismissal on top would
    blur which of the two restored it. No claim can carry that reason today.
    Keep the exclusion, or allow it?

## Not yet offered: the sign-off phrase

The act phrase for this manifest would be:

`SIGN OFF PWB DISMISSAL-EXPIRY AMENDMENT: 9f4063d303e75b893bc7348df0aef9e5e84c381df6ae98b3d15b4b7c22af9838`

It is registered so governance checks see it go stale, but it is **not
offered**: rounds 1, 2 and 3 returned REVISE and no review has confirmed these
bytes. If you reply with this phrase now, nothing is performed. A future
recorder must reject a digest that differs from the manifest then present and
must prove every manifest row against the tree after the patches are
applied.

## What this act would not do

- It would not amend any doctrine, contract, policy, topology, consent,
  registry value or retention direction.
- It would not widen `CHALLENGE_STATES` or change any implementation file.
- It would not create a write path for dismissal records, or promote notes
  into governance. Your question-4 answer ruled "no promotion" and deferred
  only the write act.
- It would not authorize M12 slice 4, or any slice.
- It would not decide the performance order of the other PWB successors.

## How this presupposes other decisions

- **Retention direction (2026-09-23).** The drafted arm keeps dismissals out
  of the three retained fields, but that does not settle retention: the
  first scenario needs a retained evaluation to keep showing its dismissal,
  which needs the record's bytes kept reachable or a fourth field. Question 7
  routes this to you as a possible retention change, which would need its
  own direction. [Inferred]
- **M12 slice 1** (retained records) and slice 2. The specification does not
  need them, but slice 4's implementation follows them in the M12 plan, and
  the "lapses between two evaluations" scenario is easiest to show with two
  retained evaluations side by side. [Observed plan order; Inferred
  dependency]

## Owner-visible consequences

1. Four contract consequences move to covered (RFC1-12.r1, RFC2-1.r3,
   RFC6-14.r4, RFC6-17.r7). RFC1-12.r1 covers only the no-transfer rule; the
   retired class it covers is reachable only once PWB records a split or
   merge, which it does not specify today [Observed: no such line in the
   current `spec.md`], so the credit is conditional. Re-dismissal by the
   owner (RFC1-12.r3) is held `unknown-uncovered` until you answer question
   3. Three rows that would credit the gap clauses are held
   `unknown-uncovered` until you answer question 4, and new rows for
   decisions affecting precedence and for `unadopted-draft`,
   `challenge-pending` and `editorial-draft` travel stay honestly
   `unknown-uncovered`. Contract coverage becomes 628 rows: 141 covered, 242
   Unknown, 245 believed not applicable (today 622: 137, 237, 248).
2. The observer-registry and secret-policy candidates both pin today's
   `spec.md` digest. An adopted successor stales both pins; this package does
   not repair them.
3. Every sibling's generated dependencies patch collides with this one, as
   they already collide with each other.

## Required sequence if you choose to proceed

1. Answer the open questions; revise the bytes if any answer changes them.
2. Independent fresh-context review of the exact package head, raw output kept,
   every finding dispositioned.
3. After each earlier act lands, regenerate with `--write` and re-review.
4. A dedicated recorder validates the exact phrase, applies the six patches in
   one change, regenerates both derived files, writes the act record and
   appends one aggregate section.
5. Add this link to `PWB_SUCCESSOR_CHAIN` in the performed order.
6. Run the canonical governance battery in a clone and keep the transcript.

If unanswered, current signed behavior stays in force and slice 4 does not
ship.

## Verification before any answer

```sh
python3 scripts/build_pwb_dismissal_expiry_amendment.py --check
python3 scripts/build_pwb_dismissal_expiry_amendment.py --selftest
python3 scripts/build_pwb_dismissal_expiry_amendment.py --diff
python3 scripts/check_governance.py
python3 scripts/check_governance.py --selftest
```

This branch leaves CG-26's coupled battery lists untouched; the builder joins
them at the integration commit.

## Review record

Round 1: a fresh-context review over commit `9b18409` returned **REVISE**
with eleven revise findings and seven notes. The raw is kept verbatim at
`docs/reviews/R-DOV29-DISMISSAL-EXPIRY-DELTA-RAW.md` (verdict line 271).
`9b18409` was the pre-rebase head. The repair was reviewed in round 2 as
commit `82cc6c4`, whose parent is `8cf689d` (the draft rebased onto
`66114ac`); an earlier note here named `f5f97b8`, which is on no branch
(round-2 note N10). Before the round-2 repair the branch was rebased again,
onto `08d4d02`, where the draft was `6e6d60c` and the round-1 repair
`28b88a3`. *Correction 2026-09-27 (round-3 note N-A3): `6e6d60c` and
`28b88a3` are on no remote branch and are not ancestors of the branch
head; `82cc6c4` and `8cf689d` survive only on `origin/review-pr-121`. The
branch was then rebased once more, onto `96ee305` (PR #130), and that
rebase was not recorded. The reachable chain on `96ee305` is `7d0049c`
(draft), `def4d6a` (round-1 repair), `21df27a` (round-2 repair) and
`8307180` (partition recount), which round 3 reviewed.* Package and builder
bytes are unchanged by every rebase. Every
repair retires the round before it (rule 10); a confirmation round must bind
the manifest digest above. The builder's self-test went from 67 to 102
mutants killed in round 1.

| # | Kind | Finding (short) | Disposition |
|---|---|---|---|
| 1 | REVISE | The paragraph binds a claim; `dismisses` targets a gap | Repaired in part, rest routed to you. RFC1-18 and RFC1-5's Gap row quoted and the reading labelled [Inferred] in `SEMANTIC-DELTA.md` and `IMPACT-LEDGER.md`. RFC1-20.r1, RFC1-25.r1 and RFC2-15.r1 held `unknown-uncovered` (RFC1-20.r1 too, since the same inference carries it). Question 4 asks you. |
| 2 | REVISE | RFC1-12 omitted | Repaired. Third class "bound to a retired identity", never transferred; Scenario 3; RFC1-12 warrant; rows RFC1-12.r1 (covered) and r2 (believed not applicable). |
| 3 | REVISE | Refused and lapsed conflated | Repaired. Lapsed is its own disclosed class; refused is only for incomplete or ineligible records; Scenario 3 says neither is shown as refused. |
| 4 | REVISE | Scenario 1 "same tuple values" false | Repaired. Each evaluation carries the values its own snapshot and as-of instant give, none changed by the dismissal. |
| 5 | REVISE | "on the primary surface" not carried | Repaired. "on the same surface as the claim and without further disclosure". |
| 6 | REVISE | Aggregate sentence could drop Unknown counts | Repaired. Dismissed members stay in every label, tier and reason count and are also counted as a sibling state; a Falsifier line and a forbidden-wording rule check it. *Round-2 correction (N4): no forbidden-wording rule checked it; the reviewer's mutant P3 survived. Removal and exclusion wordings are now forbidden, and freshness counts are named (N3).* |
| 7 | REVISE | "No retention question arises" unsupported | Withdrawn. Routed to you as question 7, a possible retention change. |
| 8 | REVISE | Arm framing misstates the funnel | Repaired. The funnel's three arms quoted verbatim; the drafted arm placed against arm 2; L2-M8's objection answered, and the case where it survives stated. [Inferred] |
| 9 | REVISE | RFC6-14.r5 versus RFC6-17.r2 | Repaired. `unadopted-draft` travel split out as RFC6-14.r6, `unknown-uncovered`; r5 narrowed; old question 10 dropped. |
| 10 | REVISE | PWB-REQ-007 count does not reproduce | Repaired. Re-derived by two methods at `3ee61c7`: 113 files, 540 occurrences (515 is the line count); method published in `IMPACT-LEDGER.md`. |
| 11 | REVISE | Question 11 put a package proposal in your mouth | Repaired. Now question 10: you fixed `.21 → .30 → .22 → lane B`; `.20`, `.18` and this package after it are the package's proposal [Inferred]. |
| 12 | NOTE | Builder rules presence-only | Repaired. Scenario body rules, forbidden wordings (clock, hide, collapse, expire-on-read) and their mutants; the reviewer's two surviving mutants are now caught. *Round-2 correction (N4): four new mutants (P3, P5, P9, S1) still survived; see the round-2 table.* |
| 13 | NOTE | Expiry boundary unspecified | Repaired. In effect only while the as-of instant is earlier than the expiry; equal means lapsed; Scenario 1 tests equality. |
| 14 | NOTE | `challenge-suspended` dismissable without argument | Repaired by exclusion, argued in `SEMANTIC-DELTA.md`; question 12 asks whether to allow it. |
| 15 | NOTE | Input binding scoped to records "read" | Repaired. Every record present at the snapshot is an identified input. |
| 16 | NOTE | Retention quote elided record-level fields | Repaired. The elision is marked in `SEMANTIC-DELTA.md`. |
| 17 | NOTE | Sweep omitted range forms | Repaired. Range-form sweep with its regex published in `IMPACT-LEDGER.md`: 13 lines in 9 files carry a range, 7 lines in 6 files span 007. |
| 18 | NOTE | Composition checked pairwise only | Repaired. The builder now applies every composing sibling in order, then this package, and re-checks the text; question 10 names the order. |

Round 2: a fresh-context confirmation review over commit `82cc6c4` returned
**REVISE** with two revise findings and nine notes, and resolved 13 of the 18
round-1 findings in full. The raw is kept verbatim at
`docs/reviews/R-DOV29-DISMISSAL-EXPIRY-DELTA-2-RAW.md` (verdict line 2; the
closing verdict section repeats it). The builder's self-test went from 102
to 121 mutants killed.

| # | Kind | Finding (short) | Disposition |
|---|---|---|---|
| N1 | REVISE | Scenario 2 refused a record by the claim's current reason, against the paragraph and Scenario 3 | Repaired. Scenario 2 now refuses a record "whose own dismissed primary reason is" one that may not be dismissed; the paragraph says the same ("itself names, as the reason it dismisses"); a record whose claim has since moved to such a reason is lapsed, stated in the paragraph and in Scenario 3. The builder requires both sentences and forbids the old wording. |
| N2 | REVISE | "Exactly one of three classes" over overlapping tests | Repaired. The classes are tested in order, refused, then bound to a retired identity, then lapsed, and a record is shown in the first whose test it meets. The Falsifier now fails any record shown in a later class. |
| N3 | NOTE | Freshness counts not named | Repaired. The paragraph, Scenario 2 and the Falsifier name per-label, tier, freshness and reason counts; the full list of kept facts is a required rule (kills P10). |
| N4 | NOTE | Mutants P3, P5, P9, S1 survived; dispositions 6 and 12 overstated the guard | Repaired. New forbidden wordings (removal, exclusion, a second refusal route, a permissive dismissal source, the old Scenario 2 refusal) and a once-only rule for Scenario 1's rendering phrases; each has its own self-test mutant. Dispositions 6 and 12 above carry a dated correction. |
| N5 | NOTE | Question 2 glossed "governed plane" one way | Repaired. Question 2 gives both readings, labelled [Inferred]. |
| N6 | NOTE | Question 1 did not map the drafted arm to the funnel | Repaired. Question 1 lists the funnel's three arms, places the draft nearest arm 2 and quotes L2-M8's objection. |
| N7 | NOTE | RFC6-14.r5 believed not applicable while RFC6-17.r5 and r8 are Unknown | Repaired. RFC6-14.r5 is now `unknown-uncovered`; totals 627 / 141 / 241 / 245. *Round-3 update: 628 / 141 / 242 / 245 after the RFC1-12.r3 split (N-C1).* |
| N8 | NOTE | Continuation predicate published in words | Repaired. `IMPACT-LEDGER.md` publishes the regex and the hyphen form. |
| N9 | NOTE | "Deferred" misstated the question-4 answer | Repaired. The answer ruled "no promotion" and deferred only the write act. |
| N10 | NOTE | Review record named a commit on no branch | Repaired. The round-1 paragraph names `8cf689d` and the later rebase. |
| N11 | NOTE | A bare packet digest copy is unguarded (systemic) | Not repaired here. Filed separately and owned by another bead; it affects the missing-currency packet the same way. |

Round 3: a fresh-context confirmation review over commit `8307180` returned
**REVISE** with one revise finding and seven notes, and resolved N1–N9 and
N11 of round 2 (N10 recurred as N-A3). The raw is kept verbatim at
`docs/reviews/R-DOV29-DISMISSAL-EXPIRY-DELTA-3-RAW.md` (verdict line 2; the
closing verdict section repeats it). The builder's self-test went from 121
to 136 mutants killed, and the total is now a fixed number the self-test
asserts.

| # | Kind | Finding (short) | Disposition |
|---|---|---|---|
| R1 | REVISE | A record for a claim that simply vanished was refused; the refused and retired tests read the world and the evaluation differently | Repaired. Refusal now depends only on the record itself, and "a record is never refused because of the state of the claim it names". Retirement is "when the evaluation records the claim identity it names as retired by a split or merge", in the paragraph and in Scenario 3's WHEN. A record whose claim identity the evaluation does not carry is lapsed with that condition; Scenario 3 adds that third record. The plain-language list above says the same. |
| N-A1 | NOTE | A record that never matched was shown with a "no longer" condition | Repaired. The lapse tests say "is not", and the condition "names the test that failed and never states whether the record once took effect", so a never-matched record is lapsed under the same condition as a changed one. |
| N-A2 | NOTE | "deferred any write act"; "direction to draft" unlabelled | Repaired. Question 2 quotes "write act deferred". The warrant line here and the delta's banner quote the answer and label "direction to draft" as the drafter's reading [Inferred]. The delta names the "What it means" column as the recorder's words. |
| N-A3 | NOTE | Review record named off-branch commits; the `96ee305` rebase was unrecorded | Repaired. A dated correction in the round-1 paragraph names the reachable chain on `96ee305` and says which commits are unreachable; the impact ledger records both later bases. |
| N-B1 | NOTE | "and"→"or" (M2), the refused guard (M7) and "as lapsed and as refused" (M14) survived; `SCENARIO_ONCE` tested itself | Repaired. The three in-effect tests are one rule, so the connectives are pinned (M2 killed). Retirement is pinned to the evaluation's record, and refusal by an uncarried claim is forbidden wording (M7 and its reversal killed). A record put in two classes is forbidden wording (M14 killed). The self-test asserts the `SCENARIO_ONCE` population and its own total as literals: dropping a phrase from `SCENARIO_ONCE` now fails with "once-only scenario phrase population changed". The additive mutants M1 and M9 are also killed now: "not counted" is forbidden, and a permissive source now includes "SHALL dismiss". |
| N-C1 | NOTE | RFC1-12.r1 credited `covered` while "re-dismissal is an owner act" rests on question 3 | Repaired. RFC1-12.r1 now covers the no-transfer rule only, and says the retired class is unreachable until PWB records a retirement. New row RFC1-12.r3, "re-dismissal of a successor is an owner act", is `unknown-uncovered` until you answer question 3. Totals 628 / 141 / 242 / 245. The delta's "a valid owner act is never shown as refused" now reads "a complete record". |
| N-C2 | NOTE | VIS-2: an unreadable or homeless record set could yield a dismissed count of 0 | Repaired. When the record set cannot be read, or no home is designated, the evaluation "dismisses no claim and SHALL disclose its dismissed count and the count of each record class below as Unknown, never as zero". The Case and Falsifier lines cover it. |
| N-C3 | NOTE | Two records in effect for one claim were in no class | Repaired by disclosure: "When more than one record is in effect for the same claim, each is disclosed that way beside the claim and the claim is counted once as dismissed." |
