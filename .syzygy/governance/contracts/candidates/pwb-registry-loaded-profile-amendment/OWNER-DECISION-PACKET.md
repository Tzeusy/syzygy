# Owner decision packet — write the Butlers source grammar into the registry entry

> **Candidate — binds nothing.** Drafted by agents under P-74 question 2
> of `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`
> (2026-09-21), which the drafters read as authorizing drafting only
> [Inferred]. This file offers no act, quotes no act argument and labels
> nothing accepted. Only the owner performs an act (`VIS-4`). **Reviewed
> three times, verdict REVISE each time;** every finding of all three
> rounds was repaired in this revision, which has not yet been reviewed.
> The review record is at the end of this file.

## What this package is, in one paragraph

Today the observer's rules for reading Butlers — where the root index is,
which file feeds which kind of item, which headings to look under, what
shape the items take — live only in TypeScript constants. M8 slice 5 wants
the observer to load those rules from the registry entry instead, so that a
governance act, not a code change, decides how a project is read. Your
P-74 Q2 answer was "one registry-entry amendment act before slice 5's fifth
limb only".
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
Nothing else in the entry changes, byte for byte: outside the two version
lines and the one inserted block, the file is `.18`'s bytes exactly. The
builder checks both the parsed values and the bytes. (Before round 3 it
checked values only, and the proposed file had re-written one array onto
three lines and two em dashes as escapes; see the round-3 record.)

**How we know it restates today's reading, and how far that goes.** The
builder's `--check` tests the fields three ways [Observed, `--check`]:

1. every heading text is present in the specification's reader
   definitions;
2. the root path, depth, pillar keys and labels, file bindings and tree
   patterns match the TypeScript constants;
3. the observer's own code is run under Node over files the builder writes
   from the fields alone. It must derive the source list the fields
   predict and read the items they predict — class, key, text and, where
   the code sets one, context. Then 123 probes each feed it one varied file
   and check that the code does what one clause of one sentence says, and
   that the sentence says it. The probes run for every row, so a row given
   the wrong shape or key sentence is caught even when another row uses
   that shape correctly. A row carrying a field its shape does not read is
   refused.

`--selftest` then breaks the fields and the checks deliberately in 268
ways, including the 17 wrong versions the first reviewer used, the 8
the second reviewer found surviving and the third reviewer's survivors
that change what the code reads; every one is caught [Observed,
`--selftest`].

What this does **not** prove: the sentences are prose, and a clause no
probe exercises is checked only by its exact wording being pinned in the
builder. The pin is the builder's own copy of each sentence, so a
sentence rewritten the same way in both the builder and the entry passes
every check; only a review of the builder's diff catches that. Nor can a
check show that the code has no rule these fields leave out.

Order carries no meaning in four places, and no check pins it: the list of
file bindings, the reading rules after the project-account ones (which
must follow `fixedProjectAccountKeys`), the tree populations, and the keys
of the shape list. The observer reads none of them in order [Inferred from
the code; the third reviewer's order-only mutants all passed the behaviour
check]. The rules every project shares are now listed in one sentence and left
to code, which is what the first review asked for.

Today's source manifest and observation digests are **not** evidence for
most of these fields. Neither the observation code nor the manifest code
uses the extraction code [Observed, their imports], so those two digests
depend only on `rootIndex`, `pillars` and `sourcePopulation` [Inferred]; a
wrong heading, shape or key in `classGrammar`, `containerShapes` or
`sourceGrammarSemantics` would leave them unchanged. The entry's scope
sentence therefore also requires a loader to reproduce, for every source,
the items the extraction reads from it. For those three fields the only
evidence today is the builder's behaviour check above. Whether slice 5's
first step will compare extracted items as well as the two digests is
[Unknown]: that step is not built.

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

**What you ruled.** Asked "Landing order for lane B and the three
spec-touching packages?", you answered "Readiness order, lane B last
(Recommended)" (the 2026-09-23 owner-values record, §6). As presented,
that option read `.21` → `.30` → `.22` → lane B; that is the order it
selected, and it covers those four packages only.

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
   profile reproduces today's digests **and** the items extraction reads
   from every source, and the names match.* Today's two digests alone
   would not show `classGrammar`, `containerShapes` or
   `sourceGrammarSemantics` right, because they do not depend on the
   extraction (see "How we know it restates today's reading"); whether
   limb 1 will compare extracted items is [Unknown]. Counter-view: acting
   now fixes the names and lets limb 1 build against them.
3. **Does a sentence in the ruling record's "What it means" column stop
   this package?** Row P-74's "What it means" column says "The consent
   record, the registry entry and PWB-REQ-005 are edited on no arm." That
   column is the recorder's gloss, not your answer; your answer (the
   "Ruled" column) is "Q2 one registry-entry amendment act before slice
   5's fifth limb only, the first four limbs thread a profile parameter
   with current constants as default". Read literally, the gloss forbids this
   package's subject, which your Q2 answer puts under an act. Two readings
   reconcile them:
   - *Reading A:* the gloss covers the other slices' arms, and Q2's act is
     the one exception.
   - *Reading B:* "edited" means changed in place outside an act. A new
     superseding act is not an edit — the act in force draws the same
     line ("changes travel as a new act") — so the gloss and Q2 never
     conflict. The same stock sentence appears in other rows' "What it
     means" column (P-78: "The registry entry is edited on no arm.").

   Both let this package proceed; they differ on whether any *other* arm
   may change the entry by act. Where the gloss and your answer differ,
   the draft follows your answer. *No recommendation between the readings*
   [Inferred]. Does either reading misstate what your Q2 answer meant?
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
   the funnel's Q2 counter-argument named, and your P-74 Q2 answer chose
   the registry act anyway* [Inferred].
7. **Does limb 5 need a plain continuation direction on top of this act?**
   `.18` needs one (`syzygy-dov.19`) because a registry amendment crosses
   an escalation trigger. *Recommended: yes, the same kind of short
   direction, given with or after this act.*
8. **Should the `.18` and this amendment be merged into one act?** They
   touch the same entry and would land close together. Your P-72 Q2 answer
   was "Q2 mint `maxBriefingResponseBytes` under a superseding registry
   act, the fold-in ruled now" (row P-72, "Ruled" column). That the
   briefing ceiling and P-69 Q2(a) then travel together as `.18` is the
   recorder's reading of that answer, not your words; nothing you ruled
   joins this package to `.18`.
   *Recommended: keep them
   separate — `.18` is ready for its review round and this one waits on
   limbs 1–4* [Inferred]. Merging would retire `.18`'s reviews.
9. **Should this entry say anything about root independence before M15's
   delta does?** Your P-82 answer was "Q1 arm (b), draft the delta only"
   and "Q4 design the root-independence flags in the same delta". That
   delta's place, PWB-REQ-002, comes from the row's "What it means"
   column, and `.15.1`, after `.17`, from its "Applied by" column; both
   are the recorder's words, not your answer. M15's
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
| R1 — the restatement check was much weaker than claimed: it found literals, not which row they belong to; 16 of the reviewer's 18 wrong versions survived | revise | Fixed. A third check runs the observer's own code over files built from the fields and compares sources and items; each row's heading, level, source and key are now bound behaviourally or structurally. All 17 wrong versions still applicable are in `--selftest` and caught. Both overclaiming paragraphs are rewritten to say what is and is not proved. **Corrected 2026-09-27:** "each row's heading, level, source and key are now bound" was false. The shape and key-form probes ran once per shape and once per form, and extra fields were accepted, so round 2 found 8 wrong versions that passed (its D1). See round 2 below. |
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

2026-09-27, after round 1 (no review round): an attribution sweep compared
every sentence this package presents as your ruling with the answer cell
("Ruled" column) of the ruling record. Three had quoted other text as your
words: the "edited on no arm" sentence and "Slice 5's fifth limb waits for
the registry act" (both from P-74's "What it means" column), and "one
registry act, not two" (the record's cross-cutting heading; your P-72 Q2
answer is quoted instead). Question 3, question 8, question 9, the delta's
warrant, the brief's criterion 7 and the ledger's M15 row now name which
column each quotation comes from. These edits retire any review of the
previous bytes.

Round 2: `docs/reviews/R-DOV24-LOADED-PROFILE-AMENDMENT-2-RAW.md`, a
fresh-context confirmation review of commit `1395d44`. Verdict: REVISE.
Every finding and what was done (2026-09-27):

| Finding | Severity | Disposition |
|---|---|---|
| D1 — each row's container shape and key form were not bound; 8 wrong versions survived (N2, N3, N17, N22, X3, X4–X6) | revise | Fixed. The shape and key-form probes now run for every row, not once per shape or form. The witness predicts each row's key from its own key sentence for every shape, including the tree and TOML rows, and each row's context where the code sets one. A row may carry only the fields its shape and key form read, and needs every one of them; a field no shape reads is refused. All 8 survivors, and further structural and sentence-swap wrong versions, are in `--selftest` and caught (223 predicates). The round-1 R1 disposition above carries a dated correction. |
| D2 — the manifest and observation digests cannot show `classGrammar`, `containerShapes` or `sourceGrammarSemantics` right | revise | Fixed. Neither the observation code nor the manifest code uses the extraction code, so the packet, the delta and question 2 no longer call those digests the proof for the three fields. The entry's scope sentence now also requires every source's extracted items to be reproduced. The present evidence is named — the builder's behaviour check — and whether slice 5's first step will compare extracted items is marked [Unknown]. |
| D3 — question 3 and the delta's warrant treated the recorder's "What it means" column as the owner's words | revise | Already fixed before this review landed, in the attribution sweep recorded above, in a later commit than the one reviewed. Question 3 names the sentence as the recorder's reading and asks whether either reading misstates your answer; the warrant quotes only the "Ruled" cell as your words. Checked again for this round; no further change. |
| D4 — the landing order and question 8 quoted option text and a recorder heading as your answer | note | Fixed. The landing order quotes your verbatim answer, "Readiness order, lane B last (Recommended)", with the arrows cited as the option it selected and the record's own question ("lane B and the three spec-touching packages"). Question 8 cites P-72's "Ruled" cell and names the joining of the two amendments as the recorder's reading. The delta and brief are aligned. |
| D5 — four behaviours of the code were not stated | note | Fixed. Headings are ATX headings at column 0, so an indented line is not a heading; the design key is trimmed and NFC-normalized and the cell must be one whole link; the TOML value is trimmed and NFC-normalized, a backslash escape is not decoded, and the value is the item's context; catalog items' context is the heading they were read under, and topology items' context is the ordinal. Each is checked by a probe or by the witness's predicted context. The same sentences, word for word, are in N8's specification amendment, and the key-form names now match N8's. |

These edits retire any review of the previous bytes.

Round 3: `docs/reviews/R-DOV24-LOADED-PROFILE-AMENDMENT-3-RAW.md`, a
fresh-context confirmation review of commit `929100f`. Verdict: REVISE
(line 2 of the raw). It found every round-2 finding resolved (D1 with one
residual gap, its F2). Every new finding and what was done (2026-09-27):

| Finding | Severity | Disposition |
|---|---|---|
| F1 — "Nothing else in the entry changes" was false at byte level: the patch re-wrote the `questions` array onto three lines and two em dashes in the precedence rows as `\u2014` escapes; the builder compared parsed values only | revise | Fixed. The patch is regenerated so only the two version lines and the one inserted block differ from `.18`'s bytes; the two precedence strings and the array are `.18`'s bytes again. A new byte check allows exactly those three differences and nothing else, and `--selftest` breaks it five ways (a re-serialized file, one escaped dash, one reflowed array, an unbumped version line, a second inserted block), each caught. The statement above and the delta's two "byte-for-byte" sentences now hold, and the brief's criterion 4 stays in bytes. The manifest row changed; the new row is in `PWB-LOADED-PROFILE-AMENDMENT-MANIFEST.txt`. |
| F2 — the second heading of the two-heading `v1-scope` row was not probed, so deleting its level passed | revise | Fixed. The heading probes now run for every heading a row declares, not only the first, and the reviewer's mutant (the second heading's level deleted) is in `--selftest` and caught. |
| N1 — extra keys passed in the pillar-root table, the file bindings and the source population | note | Fixed. Each of the three now has a fixed key set; the reviewer's four mutants are in `--selftest` and caught. |
| N2 — a redundant `pillar`, a padded TOML name, and order-only changes passed | note | Fixed for the first two: a row carries `pillar` exactly when two bindings share its source name, and a TOML table or field name must be a bare key (letters, digits, `_`, `-`), so `"name "` is refused; both are in `--selftest`, with a missing-pillar and a padded-table mutant. Order is stated free above, in the builder's comments and in the delta, because the observer reads none of those lists in order. |
| N3 — three sentence clauses looser or stricter than the code, and the consistent-rewrite gap | note | Fixed. (a) The link title is now "a title in double quotes", with a probe that a single-quoted title fails and a double-quoted one reads. (b) The TOML sentence now says an array-of-tables header such as `[[other]]` neither opens a table nor ends the declared one, with a probe. (c) The pillar-link sentence now reads "after the table is read, every link in the root index, wherever it stands in the file", with a probe that a link placed before the table counts. (d) The consistent-rewrite gap is stated above. |
| N4 — P-82 recorder columns read as the ruling | note | Fixed. Question 9, the delta's M15 bullet and the ledger's M15 row now quote only the "Ruled" cell as your answer and name the "What it means" and "Applied by" columns as the recorder's. The delta's and this packet's "authorizes drafting only" are labelled as the drafters' reading [Inferred]. |
| N5 — the delta's review section still said the revision was unreviewed after round 2 | note | Fixed, with the stale sentence kept quoted and dated beside the correction. |

These edits retire any review of the previous bytes.
