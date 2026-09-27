# Owner decision packet — dismissal with a live expiry

> **Inert draft.** This packet performs nothing. It records no act,
> authorizes no implementation and changes no signed byte. A commit, review,
> merged pull request, passing check, silence or general approval performs no
> act. The phrase below is kept only so governance checks can see it go
> stale; it is not offered until the exact bytes pass a fresh independent
> review.

Date: 2026-09-26; repaired 2026-09-27 after review round 1 (REVISE; see
the review record at the end). Gate bead: `syzygy-dov.29` (P-79 question 5, M12 slice 4).

Warrant: your 2026-09-21 answer to P-79 question 5 — a dismissal is an
amendment, needing a CC-REV-2 delta and a new act "before any dismissal
touches a tuple". That answer is direction to draft, not an act.

Manifest: `PWB-DISMISSAL-EXPIRY-MANIFEST.txt`, eleven rows over the signed
PWB behavior subject. Six rows hash proposed bytes and five hash current
bytes.

Manifest SHA-256:
`dec888c6399cad83d35da6b7a24a63ed458ae5ab2db272dda6d16ab6c670c91d`

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
- no tuple value changes; a dismissed claim stays in every Unknown count and
  is also counted separately as dismissed, and no count treats it as resolved
  or good;
- a record that dismisses nothing is shown as one of three things, never
  confused: **refused** (incomplete, or names something it may not),
  **lapsed** (its expiry has passed, or the claim's reason has changed since),
  or **bound to a retired identity** (the claim it named was split or merged
  away; a new record is needed for the successor).

The full reasoning, with every contract clause quoted, is in
`SEMANTIC-DELTA.md`.

## Open questions for you

1. **Which arm?** The draft keeps the tuple unchanged and shows the dismissal
   as the `dismissed-by-decision` sibling state beside it. Your P-79 words
   say "before any dismissal touches a tuple"; this arm never touches one.
   The other arms are: widen the challenge-state vocabulary so a dismissal
   lives inside the tuple (the M12 funnel's framing), or do not build slice 4.
   Does the drafted arm answer what you asked?
2. **Where do dismissal records live, and who writes them?** The draft says
   only "committed to the governed plane" — that is, in Syzygy's own
   governed files, never in the observed repository, which Syzygy may not
   write to. Your question-4 answer deferred any write act, so this package
   gives Syzygy no way to write a record. Which path should the records use,
   and do you author them by hand until a write act exists?
3. **Who may dismiss?** The draft requires an attributed human author. With
   multi-user support forbidden, the only author today is you. Should the
   text say "the owner" rather than "a human"?
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

`SIGN OFF PWB DISMISSAL-EXPIRY AMENDMENT: dec888c6399cad83d35da6b7a24a63ed458ae5ab2db272dda6d16ab6c670c91d`

It is registered so governance checks see it go stale, but it is **not
offered**: round 1 returned REVISE and no review has confirmed these bytes. If you reply with this phrase now,
nothing is performed. A future recorder must reject a digest that differs
from the manifest then present and must prove every manifest row against the
tree after the patches are applied.

## What this act would not do

- It would not amend any doctrine, contract, policy, topology, consent,
  registry value or retention direction.
- It would not widen `CHALLENGE_STATES` or change any implementation file.
- It would not create a write path for dismissal records, or promote notes
  into governance (your question-4 answer deferred that).
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
   RFC6-14.r4, RFC6-17.r7). Three rows that would credit the gap clauses are
   held `unknown-uncovered` until you answer question 4, and new rows for
   decisions affecting precedence and `unadopted-draft` travel stay honestly
   `unknown-uncovered`. Contract coverage becomes 627 rows: 141 covered, 240
   Unknown, 246 believed not applicable (today 622: 137, 237, 248).
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
`9b18409` was the pre-rebase head; the branch was rebased to `f5f97b8`
before the repair, and the repair was made on `f5f97b8`. Every repair
retires round 1 (rule 10); a confirmation round must bind the manifest digest
above. The builder's self-test went from 67 to 102 mutants killed.

| # | Kind | Finding (short) | Disposition |
|---|---|---|---|
| 1 | REVISE | The paragraph binds a claim; `dismisses` targets a gap | Repaired in part, rest routed to you. RFC1-18 and RFC1-5's Gap row quoted and the reading labelled [Inferred] in `SEMANTIC-DELTA.md` and `IMPACT-LEDGER.md`. RFC1-20.r1, RFC1-25.r1 and RFC2-15.r1 held `unknown-uncovered` (RFC1-20.r1 too, since the same inference carries it). Question 4 asks you. |
| 2 | REVISE | RFC1-12 omitted | Repaired. Third class "bound to a retired identity", never transferred; Scenario 3; RFC1-12 warrant; rows RFC1-12.r1 (covered) and r2 (believed not applicable). |
| 3 | REVISE | Refused and lapsed conflated | Repaired. Lapsed is its own disclosed class; refused is only for incomplete or ineligible records; Scenario 3 says neither is shown as refused. |
| 4 | REVISE | Scenario 1 "same tuple values" false | Repaired. Each evaluation carries the values its own snapshot and as-of instant give, none changed by the dismissal. |
| 5 | REVISE | "on the primary surface" not carried | Repaired. "on the same surface as the claim and without further disclosure". |
| 6 | REVISE | Aggregate sentence could drop Unknown counts | Repaired. Dismissed members stay in every label, tier and reason count and are also counted as a sibling state; a Falsifier line and a forbidden-wording rule check it. |
| 7 | REVISE | "No retention question arises" unsupported | Withdrawn. Routed to you as question 7, a possible retention change. |
| 8 | REVISE | Arm framing misstates the funnel | Repaired. The funnel's three arms quoted verbatim; the drafted arm placed against arm 2; L2-M8's objection answered, and the case where it survives stated. [Inferred] |
| 9 | REVISE | RFC6-14.r5 versus RFC6-17.r2 | Repaired. `unadopted-draft` travel split out as RFC6-14.r6, `unknown-uncovered`; r5 narrowed; old question 10 dropped. |
| 10 | REVISE | PWB-REQ-007 count does not reproduce | Repaired. Re-derived by two methods at `3ee61c7`: 113 files, 540 occurrences (515 is the line count); method published in `IMPACT-LEDGER.md`. |
| 11 | REVISE | Question 11 put a package proposal in your mouth | Repaired. Now question 10: you fixed `.21 → .30 → .22 → lane B`; `.20`, `.18` and this package after it are the package's proposal [Inferred]. |
| 12 | NOTE | Builder rules presence-only | Repaired. Scenario body rules, forbidden wordings (clock, hide, collapse, expire-on-read) and their mutants; the reviewer's two surviving mutants are now caught. |
| 13 | NOTE | Expiry boundary unspecified | Repaired. In effect only while the as-of instant is earlier than the expiry; equal means lapsed; Scenario 1 tests equality. |
| 14 | NOTE | `challenge-suspended` dismissable without argument | Repaired by exclusion, argued in `SEMANTIC-DELTA.md`; question 12 asks whether to allow it. |
| 15 | NOTE | Input binding scoped to records "read" | Repaired. Every record present at the snapshot is an identified input. |
| 16 | NOTE | Retention quote elided record-level fields | Repaired. The elision is marked in `SEMANTIC-DELTA.md`. |
| 17 | NOTE | Sweep omitted range forms | Repaired. Range-form sweep with its regex published in `IMPACT-LEDGER.md`: 13 lines in 9 files carry a range, 7 lines in 6 files span 007. |
| 18 | NOTE | Composition checked pairwise only | Repaired. The builder now applies every composing sibling in order, then this package, and re-checks the text; question 10 names the order. |
