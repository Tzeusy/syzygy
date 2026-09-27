# Owner decision packet — each project's profile declares its container shapes

> **Inert draft.** This packet performs nothing. It records no act,
> authorizes no implementation and changes no signed byte. A commit, review,
> merged pull request, passing check, silence or general approval performs no
> act. The phrase below is kept only so governance checks can see it go
> stale; it is not offered until the exact bytes pass a fresh independent
> review.

Date: 2026-09-27. Gate bead: `syzygy-u05.8` (N8).

Warrant: your 2026-09-26 answer "Draft it now (Recommended)" to "Draft the
spec change that lets each project declare its own formats?", recorded in
§6 of `.syzygy/governance/decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md`.
That answer is direction to draft, not an act.

Manifest: `PWB-CONTAINER-SHAPE-PROFILE-MANIFEST.txt`, eleven rows over the
subject's manifest population (the subject tracks 15 files; the manifest
leaves out the three contract-coverage parts and `tasks.md`, as every
sibling PWB manifest does). Three rows hash proposed bytes and eight hash
current bytes.

Manifest SHA-256:
`c8e2cfef5a7e62bf8fd396b7d238b7b73fc91b5e90007ca70d1921edf2020ab0`

The builder writes the manifest; this digest was computed from it by script.
Any change to a patch, the manifest or the subject retires it.

## What this package is, in one paragraph

Today the PWB specification says exactly how Butlers' files are read: which
file, which heading, and how the items sit under it — a numbered list, a
table's rows, a folder in the tree, one TOML field. That last part is the
**container shape**. Because it is written into the specification for
Butlers, a second project that keeps the same kind of item in a different
shape cannot be read at all. This draft names the nine shapes Butlers
already uses as a fixed list, and the eight ways Butlers names an item (the
**key forms**) as a second fixed list. A project's **profile** then lists
**grammar rows**: each row says which kind of item, which file, which
heading, one shape and one key form. A kind of item may need several rows —
Butlers' project account needs six, from three files. Butlers' rows give
today's rules, word for word. Until Butlers' profile is loaded, today's
written rules stay in use; once a profile is loaded, a kind of item it
leaves out or gets wrong is shown as Unknown — never guessed with a
built-in rule.

## What you would be deciding

Whether to amend `PWB-REQ-002` and its reader definitions this way. The
full text, with each clause it rests on, is in `SEMANTIC-DELTA.md`; `--diff`
prints the exact change.

Under the drafted text:

- the nine shapes and eight key forms are fixed in the specification; a
  profile cannot add one. Each shape's sentence says what it reads and every
  way it fails. The sentences are the `syzygy-dov.24` registry draft's (PR
  #123), word for word; the builder checks that once both are in the tree;
- a profile declares one or more grammar rows for each kind of item, each
  with its file, heading or headings, the settings its shape or key form
  needs (a table column, a TOML table and field, a key prefix), one shape
  and one key form;
- the profile is carried in the observer's owner-adopted registry entry;
- until Butlers' profile is loaded, the observer reads Butlers by the rules
  written in the specification, as a built-in default. No other project has
  one;
- once a profile is loaded, a kind of item with no row, or a row naming a
  shape or key form not on the lists, is Unknown, and so is the category it
  belongs to. Every file stays counted;
- the rules that make reading exact — heading text, NFC, no partial item
  sets — now cover every project, not only Butlers;
- Butlers read through its profile must give exactly today's items and
  counts.

## Already ruled, and what it settles here

P-74 Q2 (`POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`, line 64)
reads: "one registry-entry amendment act before slice 5's fifth limb only,
the first four limbs thread a profile parameter with current constants as
default". So:

- the profile's home is a registry-entry amendment, and there is one such
  act. `syzygy-dov.24` drafts it;
- until that act and limb 5, the code runs on today's constants. The
  drafted text writes that in as Butlers' built-in default, so the code
  conforms by the text, not by chance.

## Open questions for you

1. **What does "declare its own formats" cover?** The draft lets the profile
   declare the whole rule — file, heading, shape and key form — not only
   the shape. Your §6 reading speaks of "container shapes". Is the whole rule
   what you meant, or only the shape, with files and headings staying in the
   specification?
2. **Where do the lists of shapes and key forms live?** The draft puts both
   in the specification, so adding a tenth shape needs a specification
   amendment. An earlier pursuit move (L1-M1) put the list in the registry
   entry, so adding one needs only a registry act. Which should it be?
3. **Should the key forms also be a fixed list?** The draft fixes them at
   the eight Butlers uses. A second project may name its items another way
   (for example, by heading text alone). Keep them fixed, or leave them open?
4. **What happens when a loaded profile is incomplete?** The draft marks the
   affected kind of item, and its category, Unknown. The `syzygy-dov.24`
   draft and the L1-M1 move instead refuse to load the whole profile. The
   drafted text allows a whole-load refusal only if every file is still
   counted with an Unknown item count. Which do you want?
5. **Keep Butlers' rules written in the specification?** The draft keeps
   them, so the oracle has a written reference and the interim default has
   words to point at. The cost: any change to how Butlers is read needs both
   a registry act and a specification amendment. Counter-view: move them
   out, and let the registry entry alone say it.
6. **When should this be signed?** No code reads a profile yet: limb 5
   (`syzygy-dov.8.3` and after) is not started. Because the interim default
   is written in, signing now leaves today's code conforming. *Recommended:
   sign this before the `syzygy-dov.24` registry act, so the registry and
   the specification agree the first time; `syzygy-dov.24`'s own question 1
   recommends the same* [Inferred].
7. **The one registry act P-74 Q2 ruled: is it `syzygy-dov.24`'s, and does
   it come after this sign-off?** P-74 Q2 settles that there is one act. What
   it does not settle is whether `syzygy-dov.24`'s drafted act is that act
   for this profile too, and its order relative to this sign-off. No
   secret-policy act looks needed: the policy lists no per-class files, only
   a seed rule [Inferred, read from the policy]. *Recommended: yes, and
   after.*
8. **This package and M15 both amend `PWB-REQ-002`. Keep them separate?**
   P-82 ruled "One CC-REV-2 semantic delta to PWB-REQ-002", sequenced behind
   lane B, adding a partially-extracted state, an unenumerated-heading
   reason and root-independence flags (`syzygy-dov.15.1`, not drafted). The
   two deltas are kept apart in meaning: this one says only which rules read
   a kind of item, and on failure defers to the exactness sentence ("fails
   as a source in which a class fails") without saying how much of the file
   fails. M15 would decide that. But this package moves that exactness
   sentence into its own bullet, word for word, and M15 is likely to edit
   the same sentence. So whichever lands second is regenerated and
   re-reviewed. The 2026-09-22 pursuit suggested L1-M1 ride M15's delta
   instead of opening a second one. *Recommended: keep them separate; they
   answer different questions and the second is a mechanical regenerate*
   [Inferred]. If you would rather merge, this package waits for M15.
9. **Should the Butlers-only wording elsewhere be widened now?** The source
   population and declared-item bullets still name Butlers. The draft leaves
   them alone, to stay inside §6. Widen them here, or in a later change?
10. **Is "profile" the right word?** RFC 0005 already uses "a per-project
    profile" for a SEC-3 execution profile, and RFC 0007 speaks of a
    "governed-project profile" for presentation. Both are unrelated. Keep
    "project profile", or rename (for example, "reading profile")?
11. **Where in the landing order?** What you ruled covers four packages
    only: `.21` → `.30` → `.22` → lane B (the 2026-09-23 owner-values
    record, §6; the 2026-09-26 sitting says N8 does not change it). Where
    this package falls is not ruled. The drafter proposes it land after
    lane B; `syzygy-dov.29` (PR #121) also proposes last, and M15 (question
    8) is behind lane B too. Each earlier specification act means this
    manifest is regenerated with `--write` and re-reviewed.

## What this would still leave unread

Syzygy's own craft policies are written as numbered paragraphs of prose.
None of the nine shapes reads that, so they would stay Unknown [Inferred,
from the pursuit's slice 1/2 matrix]. Syzygy's principles and success
criteria look readable with the existing shapes [Inferred]. No shape is
added for that here; §6 asks for Butlers' shapes as they are.

## Not yet offered: the sign-off phrase

The act phrase for this manifest would be:

`SIGN OFF PWB CONTAINER-SHAPE PROFILE AMENDMENT: c8e2cfef5a7e62bf8fd396b7d238b7b73fc91b5e90007ca70d1921edf2020ab0`

It is registered so governance checks see it go stale, but it is **not
offered**: no independent review has run. If you reply with this phrase now,
nothing is performed. A future recorder must reject a digest that differs
from the manifest then present and must prove every manifest row against the
tree after the patches are applied.

## What this act would not do

- It would not change any doctrine, contract, policy, consent record,
  registry entry or retention direction.
- It would not add a shape, a kind of item, a file or a heading.
- It would not admit any project other than Butlers, or read any new source.
- It would not change any implementation file or authorize M8 slice 5.
- It would not decide the order of the other PWB successors.

## Owner-visible consequences

1. The registry entry and the secret policy both pin today's `spec.md`
   digest. An adopted successor stales both pins; this package does not
   repair them.
2. Every sibling's generated dependencies patch collides with this one, as
   they already collide with each other.
3. Coverage row 4 is reworded; the counts stay 31 of 31. Contract coverage
   is unchanged.

## Required sequence if you choose to proceed

1. Answer the open questions; revise the bytes if any answer changes them.
2. Independent fresh-context review of the exact package head, raw output
   kept, every finding dispositioned.
3. After each earlier specification act lands, regenerate with `--write` and
   re-review.
4. A dedicated recorder validates the exact phrase, applies the three patches
   in one change, writes the act record and appends one aggregate section.
5. Add this link to `PWB_SUCCESSOR_CHAIN` in the performed order.
6. The registry act for the profile (question 7) and any continuation
   direction for limb 5, each as its own decision.
7. Run the canonical governance battery in a clone and keep the transcript.

If unanswered, the signed text stays in force and only Butlers' written
rules apply.

## Review record

Round 1: `docs/reviews/R-N8-CONTAINER-SHAPE-PROFILE-RAW.md`, a
fresh-context review of commit `a7eda10`. Verdict: REVISE. Every finding
and what was done:

| Finding | Severity | Disposition |
|---|---|---|
| R1 — one source and one shape per class cannot express Butlers' own grammar | revise | Fixed. The profile is a list of grammar rows; a class has one or more, each with its source, heading or headings, the parameters its shape or key form reads, one shape and one key form. This matches `syzygy-dov.24`'s rows. |
| R2 — no built-in rule conflicts with P-74 Q2's "current constants as default"; question 7 already ruled | revise | Fixed. Butlers' written grammar is its built-in default until its profile is loaded; the no-built-in rule applies only once a profile is loaded. P-74 Q2 is quoted above, "by coincidence" is gone, and question 7 asks only what is left. |
| R3 — landing order credited the owner with `.20` and `.18` | revise | Fixed. Only `.21` → `.30` → `.22` → lane B is attributed to you (question 11); the ledger's list is corrected the same way. |
| R4 — a missing rule names no source, so nothing turned Unknown | revise | Fixed. A class with no row, or with an invalid row, makes the class and its category Unknown; separate scenarios for the missing row and the invalid row. |
| R5 — shape sentences looser than the code; exactness paragraph left Butlers-only | revise | Fixed. The nine shape sentences and seven key-form sentences are `syzygy-dov.24`'s, word for word, each naming every failure; the builder compares them once `syzygy-dov.24`'s builder is in the tree. The exactness paragraph is its own bullet covering every grammar. |
| N1 — the written-grammar oracle compared identities only | note | Fixed. It now compares identities and D. |
| N2 — the builder guards phrases, not unchanged text | note | Partly. The exactness paragraph and the nine Butlers class bullets are now compared with today's bytes. Other untouched regions are not hash-pinned; the diff is the check there. |
| N3 — the bare digest at packet line 22 is unguarded | note | Not changed. It is checker-wide and older than this package. |
| N4 — the ledger missed run and range citers of `PWB-REQ-002` | note | Fixed. The ledger publishes the regex and lists the 13 files, and Table 2 adds the code citer. |
| N5 — M15 (P-82) not listed as a sibling | note | Fixed. Listed in the ledger, and put to you as question 8. |
| N6 — warrant paraphrased VIS-2 and VIS-7 | note | Fixed. Both are quoted at source. |
| N7 — key-form list wording | note | Fixed by R5: each key form carries its full sentence. |
| N8 — "whole subject" | note | Fixed, here and in the delta. |
| N9 — where the raw was recorded | note | The raw is retained under `docs/reviews/` with its campaign row. |

## Verification before any answer

```sh
python3 scripts/build_pwb_container_shape_profile_amendment.py --check
python3 scripts/build_pwb_container_shape_profile_amendment.py --selftest
python3 scripts/build_pwb_container_shape_profile_amendment.py --diff
python3 scripts/check_governance.py
python3 scripts/check_governance.py --selftest
```

This branch leaves CG-26's coupled battery lists untouched; the builder joins
them at the integration commit.
