# Owner decision packet — write the Butlers source grammar into the registry entry

> **Candidate — binds nothing.** Drafted by agents under P-74 question 2
> of `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`
> (2026-09-21), which authorizes drafting only. This file offers no act,
> quotes no act argument and labels nothing accepted. Only the owner
> performs an act (`VIS-4`). **Reviewed once, verdict REVISE;** every
> finding was repaired in this revision, which has not yet been reviewed.
> The review record is at the end of this file.

## What this package is, in one paragraph

Today the observer's rules for reading Butlers — where the root index is,
which file feeds which kind of item, which headings to look under, what
shape the items take — live only in TypeScript constants. M8 slice 5 wants
the observer to load those rules from the registry entry instead, so that a
governance act, not a code change, decides how a project is read. You ruled
that its fifth step waits for one registry-entry amendment act (P-74 Q2).
This package drafts that amendment: six new fields that write down exactly
what the code does today, nothing more, plus a version bump. It is drafted
on top of the `.18` currency-and-briefing amendment to the same entry, so
its builder needs `.18` applied first; you have not ruled on that order
(see "Landing order").

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
| `rootIndex` | Where the project's main index is and how it names each pillar's folder: its Pillar/Directory table, and then its links. | The index file under the about folder, its Pillar/Directory table. |
| `pillars` | The five pillar keys and their display names. | heart-and-soul → "Heart and Soul". |
| `sourcePopulation` | How far the index chain goes, and which file feeds which kinds of item. | vision.md feeds project-account sections, principles and success criteria. |
| `containerShapes` | A fixed list of nine shapes an item can take in a file, each with a sentence saying what is read and what fails. | "each top-level numbered list item in the section". |
| `classGrammar` | For each of the fifteen reading rules: the file, the heading, the shape, and what becomes the item's name. | Principles are the numbered list under "Non-Negotiable Rules". |
| `sourceGrammarSemantics` | Six sentences on how to apply the above. One lists the reading rules every project shares, which stay in code; the last says a loader refuses a missing field rather than guessing. | — |

`registryVersion` and `observerVersion` move to `1.3.0-candidate.1`.
Nothing else in the entry changes; the builder checks that.

**How we know it restates today's reading, and how far that goes.** The
builder's `--check` tests the fields three ways [Observed, `--check`]:

1. every heading text is present in the specification's reader
   definitions;
2. the root path, depth, pillar keys and labels, file bindings and tree
   patterns match the TypeScript constants;
3. the observer's own code is run under Node over files the builder writes
   from the fields alone. It must derive the source list the fields
   predict and read the items they predict — class, key and text. Then 79
   probes each feed it one varied file and check that the code does what
   one clause of one sentence says, and that the sentence says it.

`--selftest` then breaks the fields and the checks deliberately in 190
ways, including the 17 wrong versions the first reviewer used; every one
is caught [Observed, `--selftest`].

What this does **not** prove: the sentences are prose, and a clause no
probe exercises is checked only by its exact wording being pinned in the
builder. Nor can a check show that the code has no rule these fields leave
out. The rules every project shares are now listed in one sentence and left
to code, which is what the first review asked for. Slice 5's first step,
which rebuilds today's digests from the profile, remains the full proof
[Inferred].

## The act, if you choose to perform it

A superseding `adopt-registry-entry` act over
`.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`,
in the shape of
`.syzygy/governance/decisions/PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md`.
The builder's `--apply --at-adoption` refuses unless `.18`'s bytes are
already in place. That is how the builder is written, not an order you
ruled.

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

**What you ruled.** For the four specification-touching packages only:
`.21` → `.30` → `.22` → lane B (the 2026-09-23 owner-values record, §6).

**What you have not ruled.** Where `.20`, `.18` and this package fall. This
package's builder needs `.18` applied first, because both edit the same
entry and this diff is drafted on `.18`'s bytes. That is a drafting
constraint; it would change if you chose a different order, at the cost of
a redraft.

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
- **The root-independence flags M15 will design** — question 9.

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
   and PWB-REQ-005 are edited on no arm" be read?** Read literally it
   forbids this package's subject, yet Q2 in the same row rules an act
   over it. Two readings fit both:
   - *Reading A:* the sentence covers the other slices' arms, and Q2's
     act is the one exception.
   - *Reading B:* "edited" means changed in place outside an act. A new
     superseding act is not an edit — the act in force draws the same
     line ("changes travel as a new act") — so the sentence and Q2 never
     conflict. The same stock sentence appears in other rows (P-78: "The
     registry entry is edited on no arm.").

   Both let this package proceed; they differ on whether any *other* arm
   may change the entry by act. *No recommendation* [Inferred]. Please
   say which you meant.
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
9. **Should this entry say anything about root independence before M15's
   delta does?** You ruled (P-82 Q4) that M15's one delta to PWB-REQ-002
   designs "the root-independence flags" (`.15.1`, after `.17`). M15's
   design calls the flag `rootIndexRequired`, set per tree population with
   the rule it came from. The first draft of this package added its own
   flag, `rootIndependent`, for the same idea; this revision removes it.
   One clause remains: the list of shared reading rules ends "the tree
   populations are enumerated from the Git tree whether or not the root
   index or any pillar index reads". That is what the code does today and
   what M15's default arm keeps [Observed for the code]. If you adopt
   M15's recommended arm, that clause becomes false and a later registry
   act replaces it with the per-population flag.
   - *Keep the clause* (recommended): the entry then states today's
     behaviour completely, and M15's later act changes one clause.
   - *Drop the clause*: the entry is silent on root independence and
     leaves it wholly to M15, but its opening sentence no longer holds —
     a loader could not reproduce today's reading from the fields plus
     the listed shared rules alone.

## How to verify this package before acting

```
python3 scripts/build_pwb_registry_loaded_profile_amendment.py --check
python3 scripts/build_pwb_registry_loaded_profile_amendment.py --selftest
python3 scripts/build_pwb_registry_loaded_profile_amendment.py --diff
python3 scripts/check_governance.py
```

`--check` and `--selftest` need Node 22.18 or later on the path; the
behaviour check runs the observer's TypeScript directly. Both work
whether `.18` is pending or applied, and after this package is applied.

## Review record

Round 1: `docs/reviews/R-DOV24-LOADED-PROFILE-AMENDMENT-RAW.md`, a
fresh-context review of commit `31305bc`. Verdict: REVISE. Every finding
and what was done:

| Finding | Severity | Disposition |
|---|---|---|
| R1 — the restatement check was much weaker than claimed: it found literals, not which row they belong to; 16 of the reviewer's 18 wrong versions survived | revise | Fixed. A third check runs the observer's own code over files built from the fields and compares sources and items; each row's heading, level, source and key are now bound behaviourally or structurally. All 17 wrong versions still applicable are in `--selftest` and caught. Both overclaiming paragraphs are rewritten to say what is and is not proved. |
| R2 — container-shape sentences looser than the code | revise | Fixed. Every shape sentence names each failure the code raises and what it ignores; the two-heading reading and the ordinal test are stated as the code does them. Each clause the code exercises has a probe. |
| R3 — rules in the code that no field stated | revise | Fixed. Per-project rules the fields missed are added: duplicate keys, leading-label failures and key normalisation. Rules every project shares are listed in a new `sharedReadingRules` sentence, and the opening sentence now says those stay in code. |
| R4 — the delta misdescribed the pillar-link rule | revise | Fixed. Links are read always, after the table; two different roots for one pillar make it Unknown. Stated in the entry and the delta, and probed. |
| R5 — the landing order credited the owner with `.20` and `.18` | revise | Fixed. Only `.21` → `.30` → `.22` → lane B is attributed to you; the rest is marked unruled, and ".18 first" is called a builder constraint. |
| R6 — overlap with M15's root-independence flag not disclosed | revise | Fixed. `rootIndependent` is removed; the overlap and the one remaining clause are question 9. |
| R7 — `--selftest` crashed once `.18` was applied | revise | Fixed. The builder recognises three states — `.18` pending, `.18` applied, this package applied — and `--check` and `--selftest` pass in each. |
| N1 — the ledger swept half the new names; one already in use | note | Fixed. The ledger sweeps every new name, whole-word, at a new baseline, and reports the three already in use in code. |
| N2 — "exact constant source lines" overstated | note | Fixed with R1; the wording is gone. |
| N3 — question 3 gave one reading | note | Fixed. Both readings are put to you, with no recommendation. |
| N4 — the other open questions are genuine | note | No change needed. |
| N5 — two ways of writing a heading level | note | Fixed. Every row writes its heading as a `heading` object, with `level` wherever the code fixes one; the catalog row names where its texts come from with `textsFrom`, and the level is range-checked in every row. |
