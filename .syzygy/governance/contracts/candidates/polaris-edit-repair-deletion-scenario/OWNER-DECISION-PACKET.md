# Owner decision packet — Polaris edit/repair deletion-account scenario

> **Candidate — binds nothing until you sign it off.** This is the one
> package standing between bead `syzygy-dov.6.3` (M6 slice 4) and the
> implementation work you already ruled on in P-73.

## Why this is here

On 2026-09-21 you ruled P-73 option A, which included: implement M6 slices
1, 2, 3 and 5 now, but hold slice 4 (the generator's "edit" and "repair"
steps accounting for what they changed) until it has a proper written
scenario, reviewed and signed off. You said drafting that scenario could
start right away and wouldn't bind anything by itself. This package is that
draft.

## The problem in plain terms

Polaris generates a manifesto draft in stages: it writes a first version,
then an "edit" stage can revise it, and if a review finds problems a
"repair" stage can fix them. Right now, nothing in the specification (or
the code) requires the edit or repair stage to say what it changed. It
could quietly delete an entire section and nothing would flag it as wrong —
the system has no place to record "I removed this part, and here's why."

That's a real gap: it means a "repair" run could look successful while
silently throwing content away, and there'd be no way to tell that apart
from a repair that simply decided nothing needed fixing.

## What the package changes

Two files, as proposed patches only (nothing is touched yet):

1. **The specification** (`openspec/changes/polaris-manifesto-understanding-amendment/specs/polaris-generation/spec.md`,
   the requirement titled "Independent review and repair"): adds one rule —
   *the edit and repair stages must account for every block of content they
   touch. If they remove one, they have to say so and give a reason. If a
   repair leaves everything as-is because nothing was fixable, that has to
   be recorded too, and it has to look different in the record from an
   actual repair.* One new worked example ("scenario") is added showing
   exactly what an invalid silent deletion looks like versus a valid
   "nothing was fixable" outcome.
2. **`PROJECT-STATUS.md`**: a housekeeping digit. It currently says the
   specification has "177 scenarios"; adding the one new example above
   makes that "178." This keeps a page you read for orientation from
   quietly going wrong the day this lands.

The separately authorized P-76 sentence about the current no-model-called
operator path is already in that status paragraph. It is current status, not
part of this package's proposed patch. The patch still changes only `177` to
`178`; open question 2 below remains yours to decide.

Nothing else in the specification changes. No other requirement is touched.

## What the package does not change

- No code. The generator's actual behavior isn't touched — this is only
  the written rule the code will eventually have to satisfy. Building that
  (giving the edit/repair steps somewhere to record what they changed) is
  the separate implementation work for slice 4, still gated behind your
  sign-off here.
- No provider calls, no new data reads.
- Nothing about slices 1, 2, 3 or 5 — those already have your go-ahead and
  this package doesn't touch them.

## What it buys and what it costs

**Buys**: closes a real honesty gap — right now a silent deletion in
edit/repair is indistinguishable from a correct pass, and there's no
written rule saying that's not allowed. Signing this off is what unblocks
slice 4's actual implementation per your own P-73 ruling.

**Costs**: one sentence added to an existing requirement's paragraph, one
new worked example under it, and one digit changed on the status page.
Small, mechanical, reviewed the same way the two sibling packages (the
"opening band" and "exact-source render mode" scenarios) were.

## Options

- **(a) Sign off as drafted.** The scenario and paragraph addition go in
  as written; slice 4's implementation is unblocked per your P-73 ruling
  (subject to open question 1 below about whether a separate act is still
  needed for the implementation itself).
- **(b) Sign off with changes.** Name what should read differently; the
  package is revised and re-verified before landing.
- **(c) Hold.** Slice 4 stays blocked; nothing changes.

## Open questions this package cannot answer for you

1. Does signing off this scenario also count as clearing slice 4 for
   implementation under the existing `POLARIS-GENERATOR-IMPLEMENTATION-AUTHORIZATION-ACT.md`,
   or does implementation still need its own new act? (The earlier planning
   document that this scenario's wording is drawn from flagged this exact
   ambiguity and did not resolve it.)
2. Is bundling the `PROJECT-STATUS.md` digit fix into this same package the
   right call, or should that be handled separately as ordinary upkeep?
3. This package checks that the scenario count moves by exactly one, using
   two independent counting methods — it does not re-derive the full
   177/178 total from scratch. If you want that full recomputation done as
   part of sign-off, say so.

## Not yet offered: the sign-off phrase

The act phrase for this package's manifest would be:

```
SIGN OFF POLARIS EDIT/REPAIR DELETION-ACCOUNT SCENARIO: 3055106206db93b3fb89787fe4d1b77d778b9961eec368298e9068db5b0579b9
```

It is written here, following the sibling packages' convention, only so the
governance checks (`check_governance.py`'s CG-7d/CG-7e) can see this exact
digest go stale the moment the manifest changes. It is **not offered**:
independent review has confirmed the candidate manifest and proposed patches,
but owner question 2 above remains unanswered. The selected arm must receive
its own review, and a dedicated recorder must exist, before this phrase can
be offered. Replying with it now performs nothing; no sign-off or patch
application occurs here.

## What happens after a "yes"

The performing act runs the package's builder script with
`--apply --at-adoption`, which writes the two patches to the real files,
re-verifies `--check` against the resulting tree, and records the
manifest's digests in the act. `PENDING-OWNER-DECISIONS.md` and bead
`syzygy-dov.6.3` are updated to reflect the unblock (or, if question 1
above needs a separate ruling, to reflect exactly what remains blocked).
