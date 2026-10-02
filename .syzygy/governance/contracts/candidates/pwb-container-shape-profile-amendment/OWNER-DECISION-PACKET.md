# Owner decision packet — each project's profile declares its container shapes

> **Inert draft.** This packet performs nothing. It records no act,
> authorizes no implementation and changes no signed byte. A commit, review,
> merged pull request, passing check, silence or general approval performs no
> act. The phrase and digest below are retained only so governance checks can
> detect drift; they are not offered. Sign-off is by version once a fresh
> review has confirmed the exact bytes (see "How it is signed"). Four review
> rounds have run and all said REVISE; this head repairs the fourth and was
> regenerated over the current base on 2026-10-02 (review record below).

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
`afe181c82ed78bf1eeb5ac559f612ad21647b2e526a160092b0112786c512aae`

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
today's rules, word for word. Until a profile is declared for Butlers,
today's written rules stay in use; once a profile is loaded, a kind of item
it leaves out or gets wrong is shown as Unknown — never guessed with a
built-in rule. If Butlers' profile is refused, or is declared but never
read, Butlers is shown as Unknown too; it does not go back to the written
rules. Any other project with no profile has Unknown counts, never zero.

## What you would be deciding

Whether to amend `PWB-REQ-002` and its reader definitions this way. The
full text, with each clause it rests on, is in `SEMANTIC-DELTA.md`; `--diff`
prints the exact change.

Under the drafted text:

- the nine shapes and eight key forms are fixed in the specification; a
  profile cannot add one. Each shape's sentence says what it reads and how
  that reading fails; the rules every shape shares (how a heading is found,
  a missing or repeated heading, a row with several headings) are stated
  once. A `heading-section` row may name at most two headings. The
  sentences and names are the `syzygy-dov.24` registry draft's (PR #123) as
  they stand at its commit `1d5966c`, word for word; the builder proves it
  with a digest of that draft's two tables;
- a grammar row states its key form by carrying that form's sentence, as
  `syzygy-dov.24`'s rows do; the names are labels for the sentences. A
  numbered key over several headings keeps counting across them rather than
  starting again at each;
- a profile declares one or more grammar rows for each kind of item, each
  with its file, heading or headings, the settings its shape or key form
  needs (a table column, a TOML table and field, a key prefix), one shape
  and one key form;
- the profile is carried in the observer's owner-adopted registry entry;
- until a profile is declared for Butlers, the observer reads Butlers by the
  rules written in the specification, as a built-in default. A Butlers
  profile the observer refuses, or one that is declared but that the
  observer does not read for any reason, does not bring those rules back. No
  other project has a default: with no profile, its counts are Unknown;
- once a profile is loaded, a kind of item with no row, or a row naming a
  shape or key form not on the lists, is Unknown, and so is the category it
  belongs to. Every file stays counted;
- nothing else in the specification changes: the builder holds every other
  byte of it to today's;
- the rules that make reading exact — heading text, NFC, no partial item
  sets — now cover every project, not only Butlers;
- Butlers read through its profile must give exactly today's items and
  counts;
- each kind of item is written down as belonging to one category (Heart and
  Soul, Legends and Lore, Spec and Spine, Lay and Land, Craft and Care or
  roster identity), as the code already groups them.

## Already ruled, and what it settles here

P-74 Q2 (`POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`, line 64)
reads: "one registry-entry amendment act before slice 5's fifth limb only,
the first four limbs thread a profile parameter with current constants as
default". So:

- the profile's home is a registry-entry amendment, and there is one such
  act. `syzygy-dov.24` drafts it;
- until limb 5, the code runs on today's constants. The drafted text makes
  Butlers' written rules its built-in default only **until a profile is
  declared for Butlers**, not until limb 5. So today's code conforms by the
  text only while no Butlers profile is declared. Once one is declared and
  before limb 5 reads it, the code does not conform (the window below).

### The window between a declared profile and limb 5

P-74 Q2 puts the registry act before limb 5. Suppose that act puts Butlers'
grammar rows into the registry entry, as `syzygy-dov.24` drafts. Then from
the day it lands until limb 5 lands, Butlers has a declared profile that no
code reads. The drafted text treats such a profile as refused, so every
Butlers kind of item, and every category, must show Unknown. Today's code
would still show known counts from its constants. For that whole window the
code would not conform to the text, and the falsifier "a refused Butlers
profile returns Butlers to the built-in grammar" would fire on it [Inferred,
from the drafted text and today's code].

The draft keeps "declared" on purpose. It is the fail-closed choice: a
profile that has been declared but is not being read never falls back to
the written rules (review round 3, N-a). The reviewer's other repair, to
keep the default "until limb 5's loader reads a profile", would reopen that
gap, so it is not taken here. How to handle the window is the second part of
question 7.

## Open questions for you

1. **What does "declare its own formats" cover?** The draft lets the profile
   declare the whole rule — file, heading, shape and key form — not only
   the shape. The question you answered says "formats"; the record's §6
   reading, which is the recorder's and not your words, says "container
   shapes". Is the whole rule what you meant, or only the shape, with files
   and headings staying in the specification?
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
   is written in, signing now leaves today's code conforming, but only while
   no Butlers profile is declared; question 7 covers what happens once one
   is. *Recommended:
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

   **Second part: must that registry act land together with limb 5, or may
   it land first?** P-74 Q2 orders the act before limb 5; it does not say
   how long the gap may be. If the act declares Butlers' profile and lands
   first, Butlers must show Unknown until limb 5 lands, and today's code,
   which shows known counts, does not conform during that time (the window
   above). The options, none decided here:

   - (a) Land the registry act and limb 5 together, so no declared Butlers
     profile ever goes unread.
   - (b) Let the registry act land first, with the window disclosed: until
     limb 5 lands, the text says Butlers is Unknown while the code shows
     known counts, and the "refused Butlers profile" falsifier fires.

   The recommendation above ("yes, and after") is about this sign-off; it
   does not choose between (a) and (b).
8. **This package and M15 both amend `PWB-REQ-002`. Keep them separate?**
   Your P-82 answer was "Q1 arm (b), draft the delta only; Q2 design
   `partially-extracted` inside it, build only after sign-off and a fresh
   authorization; Q3 design the `unenumerated-heading` reason as
   surface-flag (a counted, routed Unknown); Q4 design the root-independence
   flags in the same delta" (decision record, line 70, Ruled column). The
   record's "What it means" column, the recorder's gloss and not your words,
   reads that as "One CC-REV-2 semantic delta to PWB-REQ-002", sequenced
   behind lane B's open manifest (`syzygy-dov.15.1`, not drafted;
   **superseded 2026-10-02:** lane B was declined and closed). The two
   are not fully apart in meaning, and an earlier draft of this question said
   they were. This package decides which rules read a kind of item. It also
   makes the exactness sentence ("it never produces a partial item set")
   bind every project's rules, not only Butlers', and it adds that when a
   kind of item is Unknown, its whole category is Unknown too. Both touch
   what M15 is to design (`partially-extracted`, and the root-independence
   flags). M15 is also likely to edit the exactness sentence this package
   moves. So whichever lands second is regenerated and re-reviewed, and may
   reopen what the first decided. The 2026-09-22 pursuit suggested L1-M1 ride M15's delta
   instead of opening a second one. *Recommended: keep them separate; they
   answer different questions. The second is not only a mechanical
   regenerate: its review must check the category rule and how far the
   exactness sentence reaches* [Inferred]. If you would rather merge, this package waits for M15.
9. **Should the Butlers-only wording elsewhere be widened now?** The
   declared-item bullet said each kind of item had "one extraction rule",
   which clashed with a kind of item having several rows, so the draft now
   changes it to "read by that class's extraction rule (for a loaded
   profile, the class's grammar rows)" and adds which category each kind
   counts toward. Its list of kinds, and the source population bullet, still
   name Butlers' files and headings; the draft leaves those alone, to stay
   inside §6. Widen them here, or in a later change?
10. **Is "profile" the right word?** RFC 0005 already uses "a per-project
    profile" for a SEC-3 execution profile, and RFC 0007 speaks of a
    "governed-project profile" for presentation. Both are unrelated. Keep
    "project profile", or rename (for example, "reading profile")?
11. **Where in the landing order?** Your answer on 2026-09-23 was
    "Readiness order, lane B last (Recommended)", an option presented as
    `.21` → `.30` → `.22` → lane B (the owner-values record, §6). It covers
    those four packages only. The 2026-09-26 sitting record states that it
    does not change that order; that sentence is the recorder's, under
    "What this does not do". Where this package falls is not ruled. The
    drafter proposes it land after lane B (**superseded 2026-10-02:** lane B
    was declined and closed, and the opening-band, render-mode, machine-view,
    missing-currency and dismissal-expiry amendments are signed, so this
    package is next in your order); `syzygy-dov.29` (PR #121) also
    proposes last, and the record's reading (not your answer) puts M15
    (question 8) behind lane B too. Each earlier
    specification act means this manifest is regenerated with `--write` and
    re-reviewed.

## What this would still leave unread

Syzygy's own craft policies are written as numbered paragraphs of prose.
None of the nine shapes reads that, so they would stay Unknown [Inferred,
from the pursuit's slice 1/2 matrix]. Syzygy's principles and success
criteria look readable with the existing shapes [Inferred]. No shape is
added for that here; §6 asks for Butlers' shapes as they are.

## How it is signed

Sign-off is by version, under
`.syzygy/governance/decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`:
once a fresh independent review of these exact bytes returns CONFIRM, or
CONFIRM WITH EXCEPTIONS with every finding a note, you are asked once whether
to sign off version 1.0. Nothing is performed until you say so, and replying
before then performs nothing. The recorder
`scripts/record_versioned_signoff.py` then proves every manifest row against
the tree after the patches are applied, applies the three patches in one
change, writes the record and tags the merged commit. The retained
phrase, for governance checks only:

`SIGN OFF PWB CONTAINER-SHAPE PROFILE AMENDMENT: afe181c82ed78bf1eeb5ac559f612ad21647b2e526a160092b0112786c512aae`

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
2. This package's generated dependencies patch is rebased on the current
   base (the signed missing-currency amendment and the earlier acts). A
   later amendment to the same files is regenerated the same way.
3. Coverage row 4 is reworded; the counts stay 32 of 32. Contract coverage
   is unchanged.

## Required sequence if you choose to proceed

1. Answer the open questions; revise the bytes if any answer changes them.
2. Independent fresh-context review of the exact package head, raw output
   kept, every finding dispositioned.
3. After each earlier specification amendment lands, regenerate with
   `--write` and re-review.
4. The versioned recorder applies the three patches in one change, writes the
   sign-off record and appends one aggregate section.
5. The chain link comes from the versioned-package table, with the sign-off.
6. The registry act for the profile (question 7) and any continuation
   direction for limb 5, each as its own decision; whether they must land
   together is question 7's second part.
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
| R2 — no built-in rule conflicts with P-74 Q2's "current constants as default"; question 7 already ruled | revise | Fixed. Butlers' written grammar is its built-in default until its profile is loaded (**superseded 2026-09-27, rounds 3 and 4:** until a profile is declared for Butlers; round 4, R-D, found that this does not keep today's code conforming once a profile is declared and before limb 5, and the window is now disclosed); the no-built-in rule applies only once a profile is loaded. P-74 Q2 is quoted above, "by coincidence" is gone, and question 7 asks only what is left. |
| R3 — landing order credited the owner with `.20` and `.18` | revise | Fixed. Only `.21` → `.30` → `.22` → lane B is attributed to you (question 11); the ledger's list is corrected the same way. |
| R4 — a missing rule names no source, so nothing turned Unknown | revise | Fixed. A class with no row, or with an invalid row, makes the class and its category Unknown; separate scenarios for the missing row and the invalid row. |
| R5 — shape sentences looser than the code; exactness paragraph left Butlers-only | revise | Fixed. The nine shape sentences and seven key-form sentences are `syzygy-dov.24`'s, word for word, each naming every failure; the builder compares them once `syzygy-dov.24`'s builder is in the tree. The exactness paragraph is its own bullet covering every grammar. |
| N1 — the written-grammar oracle compared identities only | note | Fixed. It now compares identities and D. |
| N2 — the builder guards phrases, not unchanged text | note | Partly. The exactness paragraph and the nine Butlers class bullets are now compared with today's bytes. Other untouched regions are not hash-pinned; the diff is the check there. **Superseded 2026-09-27, round 3 (N-f):** the whole spec is now pinned. |
| N3 — the bare digest at packet line 22 is unguarded | note | Not changed. It is checker-wide and older than this package. |
| N4 — the ledger missed run and range citers of `PWB-REQ-002` | note | Fixed. The ledger publishes the regex and lists the 13 files, and Table 2 adds the code citer. **Corrected 2026-09-27:** the count is 14 (63 in all); round 2, N-5. |
| N5 — M15 (P-82) not listed as a sibling | note | Fixed. Listed in the ledger, and put to you as question 8. |
| N6 — warrant paraphrased VIS-2 and VIS-7 | note | Fixed. Both are quoted at source. |
| N7 — key-form list wording | note | Fixed by R5: each key form carries its full sentence. |
| N8 — "whole subject" | note | Fixed, here and in the delta. |
| N9 — where the raw was recorded | note | The raw is retained under `docs/reviews/` with its campaign row. |

Round 2: `docs/reviews/R-N8-CONTAINER-SHAPE-PROFILE-2-RAW.md`, a
fresh-context review of commit `c103523`. Verdict: REVISE. Every finding and
what was done:

| Finding | Severity | Disposition |
|---|---|---|
| R-A — a refused Butlers profile is "not loaded", so it fell back to the written rules; a project with no profile had no rule | revise | Fixed. The bullet now opens "Until the observer reads a profile for Butlers" (**superseded 2026-09-27, round 3 (N-a):** it now opens "Until a profile is declared for Butlers") and says "A Butlers profile the loader refuses never returns Butlers to the built-in default"; a project other than Butlers with no loaded profile has Unknown class and category denominators, never zero. The body, case and falsifier of `PWB-REQ-002` say the same, and a fourth scenario, "Refused Butlers profile does not fall back", is added. |
| R-B — recorder readings given as the owner's rulings (P-82 at three sites, §6 at question 1) | revise | Fixed at `bfdcf71`, before this round's repairs: the three P-82 sites quote the Ruled cell and name "What it means" as the record's gloss, and question 1 calls the §6 reading the recorder's. One more site was found and fixed: question 11 said M15 "is behind lane B"; it now says that is the record's reading. |
| N-1 — six key-form names differed from `syzygy-dov.24`'s | note | Fixed jointly with PR #123: both now use the same eight names. The key-form bullet adds that a row states its form by carrying the form's sentence (or `<prefix>:<one-based ordinal>`), which is how `syzygy-dov.24`'s rows do it. |
| N-2 — several headings defined only for `heading-section` | note | Fixed. The vocabulary bullet says a list or table row with more than one heading reads the section under each, in the order declared, and its items are all of theirs; so `syzygy-dov.24`'s one catalog row with nine headings has a meaning here. |
| N-3 — "every way it fails" overstated | note | Fixed. The claim is now "what the shape reads and how that reading fails", and the rules every shape shares are stated once: ATX headings at column 0 outside fenced code, the declared level (any level when none is declared), exact text, missing-heading and duplicate-key for a repeated heading. How list markers, table rows, fenced code and TOML lines are recognized is said to be left to the observer. The shared sentences carry `syzygy-dov.24`'s round-2 text word for word. |
| N-4 — the M15 disclosure said this package decides nothing about failure size | note | Fixed. Question 8, the semantic delta and the ledger now say that the package makes the exactness sentence bind every grammar and adds the category rule, both in M15's path. |
| N-5 — citer count 63, not 62; U+2026 missing; a code citer missing | note | Fixed. Both sweeps re-run with `…` added: 14 files beyond the literal 49, 63 in all, at the baseline and at `96ee305`. `project-shape-model.ts` is in the list and in Table 2. |
| N-6 — "no independent review has run" | note | Fixed. The sign-off section now says both rounds said REVISE and these bytes are unreviewed. |
| N-7 — seven spec mutants survived | note | Fixed. The four added scenarios are compared word for word and the first scenario byte for byte with today's; the requirement body's two SHALL sentences and the five clause labels are rules; the source-path bullet is compared byte for byte with today's; the declared-item bullet is checked rule by rule. The seven survivors are now selftest mutants and fail closed; the selftest kills 146 (was 106). |
| N-8 — "one extraction rule" and no class-to-category mapping | note | Fixed; question 9 is rewritten to match. The declared-item bullet reads "read by that class's extraction rule (for a loaded profile, the class's grammar rows)" and maps each class to its category, as `classesForPillar` in `project-shape-model.ts` already does, with roster identity its own category. **Corrected 2026-09-27, round 3 (N-d):** the code that shows this mapping is `CLASS_ROWS` in `project-shape-coverage.ts`; `classesForPillar` gives Spec and Spine no class and has no roster entry. |

Round 3: `docs/reviews/R-N8-CONTAINER-SHAPE-PROFILE-3-RAW.md`, a
fresh-context review of commit `81315da`. Verdict: REVISE. Every finding and
what was done:

| Finding | Severity | Disposition |
|---|---|---|
| R-C — the falsifier "a project with no profile reports a known item denominator" fired on Butlers today, which has no profile and lawfully reports known counts | revise | Fixed at all four sites: the patch, the builder's rule, the semantic delta (item 7) and the review brief (criterion 5). The clause is now "a project other than Butlers with no loaded profile reports a known item denominator". The reviewer's repair-form wording was killed by the old builder; the old unscoped wording is now a selftest mutant and fails closed. |
| N-a — "until the observer reads a profile" left a declared but unread profile falling back | note | Fixed. The bullet opens "Until a profile is declared for Butlers" and adds that a declared profile the observer does not read, for any reason, is treated as refused, and so is one the observer cannot tell is declared or not. (Round 7 replaced that last clause: only the loader determines whether a profile is declared, and before a loader exists the built-in default applies.) Scenario 4 is now "Refused or unread Butlers profile does not fall back". The ledger's "until a profile is loaded" now says the same. |
| N-b — no case or scenario for a project other than Butlers with no profile | note | Fixed. The case list adds it, and a fifth scenario, "Project with no profile has Unknown item denominators", shows each class's and category's item denominator Unknown, never zero. A whole-profile refusal now also makes every class and category Unknown. |
| N-c — two shared sentences did not match the code (a link title in single quotes; an `[[other]]` header) | note | Fixed by carrying `syzygy-dov.24`'s round-3 text, which repaired both. Identity is proved by digest: the SHA-256 of that builder's `SHAPES` and `ITEM_KEY_SENTENCES` at `1d5966c` is pinned in this builder and checked on every `--check`; a sentence drifted on both sides at once is a selftest mutant. The same digest holds at `0d1ccc5`, where that branch is frozen. |
| N-d — class-to-category mapping cited to `classesForPillar` | note | Fixed at the three sites: the semantic delta (item 8), the ledger (Table 2) and the round-2 row above now cite `CLASS_ROWS`, `packages/three-surface-poc-core/src/project-shape-coverage.ts` lines 85-95. The review brief cites it too. |
| N-e — mutants B6 (the exact manifest comparison) and B7 (the undeclared-subject check) survived the selftest | note | Fixed. The selftest adds a manifest with one row digest corrupted and the path order kept, and an extra patch that changes `design.md`; both fail closed, and a builder with either check removed fails the selftest. |
| N-f — "no other requirement changes" and "source population unchanged" were held only by the digest and review | note | Fixed by enforcing them. The builder now pins the whole proposed `spec.md`: it must equal today's with this package's eight edits applied, byte for byte. The reviewer's twelve surviving `PWB-REQ-002` clause mutants, the scenario swap, `PWB-REQ-003`'s SHALL NOT made MAY and the source population's "do not recurse" removed are selftest mutants and fail closed, with one more on `PWB-REQ-001`'s title. The rule tables are digest-pinned so a weakened rule fails the selftest. |
| N-g — label trimming, which failure wins, three or more headings, and whether a numbered key restarts | note | Two fixed in this package's own text: a `heading-section` row declares at most two headings, and a declared third makes the row unreadable; a `prefixed-ordinal` key counts across a row's headings and does not restart. Two are disclosed, not fixed: the `ordinal-and-label` key trims the label (`nfc(label.trim())` in `project-shape-extraction.ts`, line 519), and when a source breaks several rules the code reports the first it meets. Both belong to the shared sentences, which must stay identical to `syzygy-dov.24`'s, so they go to `syzygy-dov.32` with that package's shared notes. |

After round 3 the selftest killed 185 mutants (was 146).

Round 4: `docs/reviews/R-N8-CONTAINER-SHAPE-PROFILE-4-RAW.md`, a
fresh-context review of commit `e381e4e`. Verdict: REVISE. It found round 3's
R-C and N-a–N-g resolved. Every new finding and what was done:

| Finding | Severity | Disposition |
|---|---|---|
| R-D — the default lasts "until a profile is declared for Butlers", but P-74 Q2 puts the registry act before limb 5; if that act declares Butlers' profile, today's code does not conform until limb 5, and the package said it did | revise | Fixed by the reviewer's option (a); round 3's "declared" is kept. The window and what it means are now stated in this packet (under "Already ruled") and in the semantic delta. The three sites that said the opposite are corrected: the "Already ruled" bullet above, the semantic delta's warrant and its downstream item 1, and the ledger's extraction-code row. The review brief's criterion 5 said the same and is corrected too. Question 7 gains a second part: must the registry act land together with limb 5, or may it land first with the window disclosed. It is put to you, not decided. |
| N-h — no falsifier names a known count for a class a loaded profile leaves unreadable, or for a refused or unread Butlers profile | note | Fixed. The falsifier adds "a class a loaded profile leaves unreadable, or any class of a Butlers profile that is refused or declared but unread, reports a known item denominator". The builder checks it as a rule. |
| N-i — the selftest did not show that `--check` actually calls the manifest comparison and the shared-text digest | note | Fixed. The selftest runs the full check with a corrupted manifest, and again with a wrong shared-text digest; each must fail. A builder with either call removed now fails the selftest. |
| N-j — "each anchor occurs exactly once" was tested only for absence | note | Fixed. The selftest adds each of the eight anchors a second time; each must fail. A builder that checks only "at least once" now fails the selftest. |
| N-k — the three matrix parts were said to "regenerate" | note | Fixed in the semantic delta and the ledger. They are files the contract-coverage generator reads, not files it writes. They are unchanged, and the builder checks that: each has a manifest row, and it refuses a change to any file no patch is declared to change. |
| N-l — the semantic delta called `syzygy-dov.24`'s fields the one registry act P-74 Q2 ruled | note | Fixed. It now says those fields are the drafted home, and that whether `syzygy-dov.24`'s act is the one P-74 Q2 ruled is open (question 7). |

The selftest then killed 196 mutants (was 185), against a total fixed in the
builder. That figure was not the builder's: round 6 re-ran the selftest and
counted 181. The present figure is 182, printed by `--selftest`.

Round 5: `docs/reviews/R-N8-CONTAINER-SHAPE-PROFILE-5-RAW.md`, a
fresh-context review of commit `51b82b6`. Verdict: CONFIRM WITH EXCEPTIONS,
five notes (N-m to N-q), dispositioned in
`docs/reviews/R-N8-CONTAINER-SHAPE-PROFILE-5-DISPOSITIONS.md` and routed to
`syzygy-u05.18`. That review read the pre-regeneration bytes. The 2026-10-02
regeneration (rebased dependencies patch, coverage totals 32, the retired
sibling-composition table, this section's sign-off wording) changed them, so
by rule 10 it confirms history and nothing about these bytes; a fresh review
is required before any sign-off question.

Round 6: `docs/reviews/R-N8-CONTAINER-SHAPE-PROFILE-6-RAW.md`, a fresh-context
review of the regenerated bytes at `2b7f084`. Verdict: REVISE, one revise
finding and three notes. Repaired in the next revision:

| Finding | Class | Disposition |
|---|---|---|
| 1 — the oracle required equality with the written grammar for a Butlers profile the same text requires to be Unknown | revise | Fixed. The oracle applies the written grammar only to a loaded profile that reproduces it; for a class a loaded profile leaves unreadable the expected D is Unknown and the written grammar is not applied. The builder splits the clause into two predicates, so each fails its own mutant. |
| 2 — mutant counts in the prose were stale | note | Fixed. The packet and brief state what `--selftest` prints (182). |
| 3 — "cannot tell is or is not declared" pulled against the claim that today's code conforms | note | Fixed. Only the loader determines whether a profile is declared; before a loader exists the built-in default applies. |
| 4 — the brief's raw-head predicate was not the one the versioned recorder parses | note | Fixed. The brief states the recorder's four-line head and finding format. |

Those bytes changed, so by rule 10 round 6 confirms history; a fresh review
of this revision is required before any sign-off question.

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

**Attribution sweep, 2026-09-27.** Every sentence here, in the ledger and in
the semantic delta that says the owner ruled, chose or answered something was
checked against the owner's verbatim answer: the Ruled column of the
P-68–P-83 decision record, and the "Owner's answer (verbatim)" column of the
2026-09-23 and 2026-09-26 records. Pattern (Python `re`, case-sensitive):
`\b(ruled?|rules|chose|chosen|decided|answer(ed)?)\b`, then `\b[Rr]eading\b`.
Six sites were repaired: question 1 had called the record's §6 reading
yours; question 8, ledger row M15 and semantic-delta item 5 had quoted
P-82's "What it means" gloss as the ruling, and question 11 and ledger row
`.21`–lane B had given the presented option's order as the owner's words.
The P-74 Q2 quotations already matched the Ruled cell and are unchanged.
