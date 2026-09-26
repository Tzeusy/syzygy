# Owner decision packet — dismissal with a live expiry

> **Inert draft.** This packet performs nothing. It records no act,
> authorizes no implementation and changes no signed byte. A commit, review,
> merged pull request, passing check, silence or general approval performs no
> act. The phrase below is kept only so governance checks can see it go
> stale; it is not offered until the exact bytes pass a fresh independent
> review.

Date: 2026-09-26. Gate bead: `syzygy-dov.29` (P-79 question 5, M12 slice 4).

Warrant: your 2026-09-21 answer to P-79 question 5 — a dismissal is an
amendment, needing a CC-REV-2 delta and a new act "before any dismissal
touches a tuple". That answer is direction to draft, not an act.

Manifest: `PWB-DISMISSAL-EXPIRY-MANIFEST.txt`, eleven rows over the signed
PWB behavior subject. Six rows hash proposed bytes and five hash current
bytes.

Manifest SHA-256:
`460cb535e43e0921f470298dcf5546a1aa53ae92d01332c74c8d3b2b7da85d46`

The builder writes the manifest; this digest was computed from it by script.
Any change to a patch, the manifest or the subject retires it.

## What you would be deciding

Whether PWB-REQ-007 should admit one thing it is silent on today: a recorded,
reasoned, expiring human dismissal of an Unknown claim.

Under the drafted text:

- only a dismissal record committed to the governed plane can dismiss a claim
  — never a view setting, browser or daemon state, a note, or a model;
- only Unknown claims can be dismissed, and never a contradiction waiting for
  your adjudication;
- each evaluation decides whether a dismissal is in effect at its own as-of
  instant, so a dismissal ends only when a new evaluation runs — a page never
  flips on its own when the clock passes the expiry;
- the claim still shows everything it showed before (its Unknown label,
  reason, route, freshness and identities), with the dismissal's reason,
  expiry and author beside it, the same in the human and machine views;
- no tuple value changes, and no count ever treats a dismissed claim as
  resolved or good.

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
   an inference. Is it right, and should Inferred claims also be dismissable?
5. **Expiry bounds.** The draft requires an explicit expiry instant and sets
   no maximum and no minimum. Do you want a longest allowed dismissal, or a
   rule against an expiry already in the past when the record is written?
6. **When is a reason still current?** The draft says a dismissal's reason
   stays current only while the claim's primary Unknown reason is the one the
   record named. So if the claim becomes Unknown for a different reason, the
   dismissal stops applying at the next evaluation. Is that the rule you
   want, or should reasons be judged some other way?
7. **Does a dismissal change a tuple, or only what is shown?** The draft says
   only what is shown: "SHALL not change any tuple value". If you choose the
   challenge-state arm instead, a dismissal changes a tuple value, and the
   2026-09-23 retention direction (which retains the tuple and challenge
   state) would then carry dismissals. Would that be a retention change
   needing its own direction?
8. **What does a dismissal render as?** The draft shows the words *dismissed
   by decision* in place of the claim's status, with all the facts, the
   reason, the expiry instant, the author and the record identity beside it,
   and a separate count in aggregates. Is anything missing, such as the
   decision date?
9. **Is PWB-REQ-001 affected?** The draft makes dismissal records inputs of
   evaluation, and PWB-REQ-001 governs evaluation inputs. The draft leaves
   PWB-REQ-001 unchanged and marks "decisions affecting precedence" as honestly
   uncovered (RFC2-1.r2). Should PWB-REQ-001 be amended too?
10. **Other sibling states.** The draft marks `challenge-pending`,
    `unadopted-draft` and `editorial-draft` travelling beside the tuple as
    believed not applicable (RFC6-14.r5), as the base row did. Another row
    (RFC6-17.r2) says `unadopted-draft` is used. Keep this disposition?
11. **Landing order.** You fixed `.21 → .30 → .22 → lane B`, then `.20` and
    `.18`. This package proposes to land **last, after all of them**. Its
    manifest must be regenerated with `--write` and re-reviewed after each
    earlier act that touches the same files lands (lane B, `.20` and every
    sibling's generated dependencies file collide with it). Is last the
    position you want?
12. **Implementation authority.** Signing this amends the specification only.
    Would building slice 4 need a fresh implementation authorization or a
    continuation direction, given the continuation act's trigger "a further
    amendment to the signed PWB specification beyond the 2026-09-05 package"?

## Not yet offered: the sign-off phrase

The act phrase for this manifest would be:

`SIGN OFF PWB DISMISSAL-EXPIRY AMENDMENT: 460cb535e43e0921f470298dcf5546a1aa53ae92d01332c74c8d3b2b7da85d46`

It is registered so governance checks see it go stale, but it is **not
offered**: no independent review has run. If you reply with this phrase now,
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

- **Retention direction (2026-09-23).** The specification bytes do not depend
  on it. The drafted arm was chosen partly *because* of it: dismissals stay
  out of the three retained fields, so no retention question arises.
  [Inferred]
- **M12 slice 1** (retained records) and slice 2. The specification does not
  need them, but slice 4's implementation follows them in the M12 plan, and
  the "lapses between two evaluations" scenario is easiest to show with two
  retained evaluations side by side. [Observed plan order; Inferred
  dependency]

## Owner-visible consequences

1. Six contract consequences move to covered and one new row stays honestly
   `unknown-uncovered` (decisions affecting precedence). Contract coverage
   becomes 625 rows: 143 covered, 236 Unknown, 246 believed not applicable.
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
