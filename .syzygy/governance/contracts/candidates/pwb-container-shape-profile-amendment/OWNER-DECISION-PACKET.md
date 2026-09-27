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
signed PWB behavior subject. Three rows hash proposed bytes and eight hash
current bytes.

Manifest SHA-256:
`3eb181c44ca29d57f31f2804caaebcc8b3deb9f81d79391395a04e4bc299fca6`

The builder writes the manifest; this digest was computed from it by script.
Any change to a patch, the manifest or the subject retires it.

## What this package is, in one paragraph

Today the PWB specification says exactly how Butlers' files are read: which
file, which heading, and how the items sit under it — a numbered list, a
table's rows, a folder in the tree, one TOML field. That last part is the
**container shape**. Because it is written into the specification for
Butlers, a second project that keeps the same kind of item in a different
shape cannot be read at all. This draft names the nine shapes Butlers
already uses as a fixed list, and says each project's **profile** picks, per
kind of item, which file, heading, shape and naming rule applies. Butlers'
profile is today's rules, word for word. If a profile leaves a rule out or
names a shape not on the list, that kind of item is shown as Unknown —
never guessed with a built-in rule.

## What you would be deciding

Whether to amend `PWB-REQ-002` and its reader definitions this way. The
full text, with each clause it rests on, is in `SEMANTIC-DELTA.md`; `--diff`
prints the exact change.

Under the drafted text:

- the nine shapes are fixed in the specification; a profile cannot add one;
- a profile declares, for each kind of item, the file, the heading, one
  shape and one of eight fixed naming rules ("key forms");
- the profile is carried in the observer's owner-adopted registry entry;
- a missing or unknown rule makes that kind of item's count Unknown, and the
  file itself stays counted;
- Butlers' rules stay written in the specification, and Butlers read through
  its profile must give exactly today's items and counts.

## Open questions for you

1. **What does "declare its own formats" cover?** The draft lets the profile
   declare the whole rule — file, heading, shape and naming rule — not only
   the shape. Your §6 reading speaks of "container shapes". Is the whole rule
   what you meant, or only the shape, with files and headings staying in the
   specification?
2. **Where does the list of shapes live?** The draft puts the nine shapes in
   the specification, so adding a tenth needs a specification amendment. An
   earlier pursuit move (L1-M1) put the list in the registry entry, so adding
   one needs only a registry act. Which should it be?
3. **Should the naming rules also be a fixed list?** The draft fixes them at
   the eight Butlers uses. A second project may name its items another way
   (for example, by heading text alone). Keep them fixed, or leave them open?
4. **What happens when a profile is incomplete?** The draft marks only the
   affected kind of item Unknown. The `syzygy-dov.24` registry draft (PR #123)
   and the L1-M1 move instead refuse to load the whole profile. A whole-load
   refusal satisfies this text only if every source path is still counted.
   Which do you want?
5. **Keep Butlers' rules written in the specification?** The draft keeps
   them, so the oracle has a written reference. The cost: any change to how
   Butlers is read needs both a registry act and a specification amendment.
   Counter-view: move them out, and let the registry entry alone say it.
6. **When should this be signed, given that no code reads a profile yet?**
   The observer reads built-in constants. Profile loading is M8 slice 5's
   fifth limb (`syzygy-dov.8.3`), not started. Signing now leaves the code
   conforming for Butlers only by coincidence of its constants, a gap that
   would be disclosed. *Recommended: sign this together with, or just before,
   the `syzygy-dov.24` registry act, then give a continuation direction for
   limb 5* [Inferred].
7. **Does the registry need ride `syzygy-dov.24`'s act?** The profile needs
   a home in the registry entry. `syzygy-dov.24` (PR #123) drafts one, and its
   own first question asks the same. No secret-policy act looks needed: the
   policy lists no per-class files, only a seed rule [Inferred, read from the
   policy]. *Recommended: yes, one registry act after this sign-off.*
8. **Should the Butlers-only wording elsewhere be widened now?** The source
   population and declared-item bullets still name Butlers. The draft leaves
   them alone, to stay inside §6. Widen them here, or in a later change?
9. **Is "profile" the right word?** RFC 0005 already uses "a per-project
   profile" for a SEC-3 execution profile, and RFC 0007 speaks of a
   "governed-project profile" for presentation. Both are unrelated. Keep
   "project profile", or rename (for example, "reading profile")?
10. **Where in the landing order?** Your order is `.21` → `.30` → `.22` →
    lane B, then `.20` and `.18`. This package proposes to land **after all of
    those**; `syzygy-dov.29` (PR #121) also proposes last. Which of the two
    goes first? Each earlier specification act means this manifest is
    regenerated with `--write` and re-reviewed.
11. **Should the shape sentences match the registry draft word for word?**
    They paraphrase `syzygy-dov.24`'s. If they must match, one of the two is
    redrafted.

## What this would still leave unread

Syzygy's own craft policies are written as numbered paragraphs of prose.
None of the nine shapes reads that, so they would stay Unknown [Inferred,
from the pursuit's slice 1/2 matrix]. Syzygy's principles and success
criteria look readable with the existing shapes [Inferred]. No shape is
added for that here; §6 asks for Butlers' shapes as they are.

## Not yet offered: the sign-off phrase

The act phrase for this manifest would be:

`SIGN OFF PWB CONTAINER-SHAPE PROFILE AMENDMENT: 3eb181c44ca29d57f31f2804caaebcc8b3deb9f81d79391395a04e4bc299fca6`

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
6. The registry act for the profile (question 7) and a continuation
   direction for limb 5 (question 6), each as its own decision.
7. Run the canonical governance battery in a clone and keep the transcript.

If unanswered, the signed text stays in force and only Butlers' written
rules apply.

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
