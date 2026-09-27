# Owner decision packet — write the Butlers source grammar into the registry entry

> **Candidate — binds nothing.** Drafted by agents under P-74 question 2
> of `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`
> (2026-09-21), which authorizes drafting only. This file offers no act,
> quotes no act argument and labels nothing accepted. Only the owner
> performs an act (`VIS-4`). **Not reviewed:** no independent review has
> been run; `REVIEW-BRIEF.md` says what one needs.

## What this package is, in one paragraph

Today the observer's rules for reading Butlers — where the root index is,
which file feeds which kind of item, which headings to look under, what
shape the items take — live only in TypeScript constants. M8 slice 5 wants
the observer to load those rules from the registry entry instead, so that a
governance act, not a code change, decides how a project is read. You ruled
that its fifth step waits for one registry-entry amendment act (P-74 Q2).
This package drafts that amendment: six new fields that write down exactly
what the code does today, nothing more, plus a version bump. It is drafted
on top of the `.18` currency-and-briefing amendment to the same entry,
which lands first.

## What you would be deciding

Whether to perform one superseding `adopt-registry-entry` act over the
entry with these fields added. The act uses the existing phrase `ADOPT
POLARIS BUTLERS PROJECT-SHAPE OBSERVER REGISTRY ENTRY` followed by the
digest of the proposed bytes. **It is not offered here**; see "Not yet
offered" below and the open questions first — at least two of them are
reasons to wait.

## The six fields, in plain words

| Field | In plain words | Example from today's Butlers |
|---|---|---|
| `rootIndex` | Where the project's main index is and how it names each pillar's folder. | The index file under the about folder, its Pillar/Directory table. |
| `pillars` | The five pillar keys and their display names. | heart-and-soul → "Heart and Soul". |
| `sourcePopulation` | How far the index chain goes, and which file feeds which kinds of item. | vision.md feeds project-account sections, principles and success criteria. |
| `containerShapes` | A fixed list of nine shapes an item can take in a file, each with a sentence saying what is read and what fails. | "each top-level numbered list item in the section". |
| `classGrammar` | For each of the fifteen reading rules: the file, the heading, the shape, and what becomes the item's name. | Principles are the numbered list under "Non-Negotiable Rules". |
| `sourceGrammarSemantics` | Five sentences on how to apply the above; the key one says a loader refuses a missing field rather than guessing. | — |

`registryVersion` and `observerVersion` move to `1.3.0-candidate.1`.
Nothing else in the entry changes; the builder checks that.

**How we know it restates today's reading and adds nothing.** The builder
checks every heading text against the specification's reader definitions,
and checks the root path, depth, pillars, file bindings, tree patterns and
heading texts against the exact lines of the TypeScript constants. Both
checks were mutation-tested: 68 deliberately wrong versions, every one
caught [Observed, `--selftest`]. What the check cannot prove is that the
code has no rule these rows leave out; slice 5's first step, which rebuilds
today's digests from the profile, is that proof [Inferred].

## The act, if you choose to perform it

A superseding `adopt-registry-entry` act over
`.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`,
in the shape of
`.syzygy/governance/decisions/PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md`.
It must come **after** the `.18` act; the builder's `--apply --at-adoption`
refuses otherwise.

### Not yet offered: the argument

The argument is the SHA-256 of the proposed registry bytes. Those bytes
exist only as the result of applying the two patches, so the digest appears
in no Markdown file here. It lives in the one row of
`PWB-LOADED-PROFILE-AMENDMENT-MANIFEST.txt`, written and re-checked by
`scripts/build_pwb_registry_loaded_profile_amendment.py`. Run `--check`,
then read the row. It changes whenever `.18`'s patch or this one changes.

### Why nothing is registered in `check_governance.py` now

The same four reasons the `.18` packet gives, unchanged:

1. The phrase is already registered for this subject (`PWB_EFFECT_ACTS`
   and `PWB_EFFECT_AMENDMENT_ACTS`); a superseding act of the same type
   reuses it.
2. The new amendment row needs the act record and the act-time digest,
   which do not exist until you perform the act.
3. Registering the manifest in `ACT_DIGEST_COPY_FILES` would compare the
   proposed digest against the current hash, which must differ while this
   is a candidate — a permanent false failure.
4. No file here quotes the argument.

## Landing order

The Polaris gate packages land in this order: `.21` → `.30` → `.22` → lane
B, then `.20` and `.18`. This package lands **after `.18`**.

- If `.18`'s patch changes before its act, rerun this builder's `--write`;
  the manifest row moves.
- Once `.18` is applied, the builder applies this patch alone and the row
  is unchanged (the bytes are the same either way).
- The specification acts (`.21`, `.30`, `.22`, lane B) do not change this
  manifest. They could change its specification check if they moved a
  heading text out of the reader definitions; rerun `--check` after each.
- `.25`'s second registry entry (PR #120) is regenerated after this act if
  you choose to copy these fields into it.
- N8's specification amendment would point at `containerShapes`; see
  question 1.

## What is still gated, and is not in this package

- **Slice 5 limbs 1–4** (`syzygy-dov.8.3`). They write the profile type
  and its schema and prove today's digests are reproduced. Not started.
- **Whether limb 5 needs its own continuation direction** — question 7.
- **N8** — question 1.

## Open questions this package did not resolve

Each has a recommendation; none is decided here.

1. **Does N8's registry need ride this act, or a later one?** The sitting
   (§6) asks for a specification amendment letting a project's profile
   declare its own container shapes, with Butlers declaring today's. This
   package already writes Butlers' shapes into `containerShapes`. If N8 is
   signed off first, one act here covers both. If N8's vocabulary changes
   in review, this package is redrafted. *Recommended: one act, performed
   after N8's sign-off, so the registry and the specification agree on
   the first try.*
2. **Wait for limbs 1–4 and the profile schema before acting?** The field
   names here are a guess at what limb 1's schema will call things. If the
   schema chooses different names, a second registry act follows.
   *Recommended: wait; perform this act only once limb 1 has proven the
   profile reproduces today's digests and the names match.* Counter-view:
   acting now fixes the names and lets limb 1 build against them.
3. **How should P-74's sentence "The consent record, the registry entry
   and PWB-REQ-005 are edited on no arm" be read?** Literally it forbids
   this package's subject. Q2 in the same row rules an act over it.
   *Recommended reading: the sentence covers the other slices' arms and
   not Q2's act* [Inferred]. Please confirm or correct.
4. **Should `discoveryVersion` move?** It is left alone because discovery
   does not change. Counter-view: once limb 5 lands, discovery reads from
   the entry, and a new version marks that. *Recommended: leave it; bump
   it in limb 5's change if its behaviour moves.*
5. **Are the version numbers right?** `1.3.0-candidate.1` for both,
   following `.18`'s `1.2.0-candidate.1`.
6. **Should the heading texts stay in the entry at all?** M8's Q1 records
   that portability is named by no requirement. The heading texts are
   Butlers' own words; writing them into a governance artifact is the
   point of the profile, but it also means every future Butlers heading
   edit needs an owner act. *Recommended: keep them; that cost is the one
   the funnel's Q2 counter-argument named and you ruled past it.*
7. **Does limb 5 need a plain continuation direction on top of this act?**
   `.18` needs one (`syzygy-dov.19`) because a registry amendment crosses
   an escalation trigger. *Recommended: yes, the same kind of short
   direction, given with or after this act.*
8. **Should the `.18` and this amendment be merged into one act?** They
   touch the same entry and would land close together. You ruled "one
   registry act, not two" for `.18`'s two parts. *Recommended: keep them
   separate — `.18` is ready for its review round and this one waits on
   limbs 1–4* [Inferred]. Merging would retire `.18`'s reviews.

## How to verify this package before acting

```
python3 scripts/build_pwb_registry_loaded_profile_amendment.py --check
python3 scripts/build_pwb_registry_loaded_profile_amendment.py --selftest
python3 scripts/build_pwb_registry_loaded_profile_amendment.py --diff
python3 scripts/check_governance.py
```
