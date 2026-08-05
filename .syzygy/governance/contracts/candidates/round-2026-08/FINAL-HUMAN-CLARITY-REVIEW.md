# Final human-clarity review — 2026-08-05

Assesses the round against its own governing standard. Written by the round
lead, who held the authoring context — which is exactly why this file is not
evidence. **The evidence is the eight raw reviews in `reviews/`**, each
written by a fresh context with no access to the authoring conversation.
Where this file and a raw report disagree, the raw report wins.

## The standard

> A technically capable person unfamiliar with Syzygy can understand its
> purpose, current state, governing rules, and next step without
> reconstructing the project from hidden history — and an LLM can receive
> exactly the context needed for one task without ingesting the entire
> Project Genome.

Two halves. The human half is met. The machine half is met for the one task
that was actually run, with a named structural gap for the general case.

## 1. The human half

**Met.** `[Observed]` A fresh reviewer answered all four Test A questions in
30 seconds from the README alone, and all six Test B questions in its own
words from the documents alone. Both from clone-equivalent material with no
`_bootstrap/` access.

What changed to make that true:

- **A front door existed at all.** The README was one line before this round.
  A reader's first question — *what is this?* — had no answer in the
  repository.
- **Status left the artifacts.** Four documents carried hand-maintained
  status paragraphs that froze a claim at authoring time; the overview's froze
  it *inside a digest*. Status now lives in one place, `PROJECT-STATUS.md`,
  which routes every row to the record that owns it and hardcodes no digest.
- **Authority became typed and visible.** Doctrine, contracts, policies,
  topology and projections each say what they are in their own banner, and
  `check_governance.py` CG-4/CG-5/CG-9 fail the build when a banner lies or
  two homes claim the same authority. Before this round, nine canonical craft
  files described themselves as "the bootstrap-phase record" — an inverted
  authority relation, stated in the first line of each file.
- **Progressive disclosure replaced density.** The overview now has four
  layers: a 30-second thesis, a five-minute argument, a technical model, and
  an exact-authority drill-down. A reader chooses depth instead of paying for
  the deepest.

**Residual human load**, all recorded rather than smoothed:

- Adopted doctrine cites a README glossary ambiguously (P-20). **Correction 2026-08-05b:** the glossary **exists**, at `.syzygy/governance/doctrine/README.md:15` (`## Glossary (read first)`). The real defect is narrower: adopted doctrine says "README glossary" without saying *which* README, and the root `README.md` — the one a reader is holding — has none. See P-20 as amended.
- The craft cluster's engineering bar is adopted by reference to a
  machine-local skill tree a clone cannot read (P-20) — a gate-approved
  authority that is, from a clone, unreadable.
- Eight of the thirty foundational public terms have no adopted definition
  anywhere; several are already used on the public surface (P-17). Act 1 and
  act 5 close this. Until then it is a knowing deferral, and the surface says
  so rather than implying the terms are settled.

## 2. The machine half

**Met for the demonstrated task; incomplete for the general case.**
`[Observed]` The Test C packet answered all six required dimensions plus
security from 11.0% of the corpus, under the token trigger, with no waiver.

`[Observed]` But the same review showed that a compiler following the routing
indexes *as written* would produce a packet both larger (23,950 tokens, over
the trigger) and less complete (unable to state the accessibility or security
obligation) than the hand-scoped one. The indexes route contracts well and
route doctrine and craft barely at all: of eight reader-map rows, two name a
doctrine or craft source. The fix is small and known — a doctrine/craft
column on eight rows — and it is not done.

This is the round's most useful negative result, and it was produced by
*running* the acceptance test rather than reading about it.

## 3. What the round got wrong, and how it found out

The round's own headline defect is worth stating plainly, because it is the
same failure mode the whole apparatus exists to prevent.

`[Observed]` **Every one of the four digest-bound act arguments was stale.**
The round's corrections churned three of the four digest sets. Each
regeneration was recorded — in the manifests, in the semantic-delta register,
in the round inventory. The one document that *offers the acts* was never
repointed. For a period, the repository's central artifact offered four
ceremonies that would have accepted packages that no longer existed, while a
status page one directory up said "Known blocking defects: none."

Six of eight independent reviewers found it. No amount of authoring care
found it, because the author had written every one of the records that made
it discoverable.

Three responses, in ascending order of value:

1. The four arguments were re-quoted, and §1a of the acceptance record states
   what changed and why.
2. `check_governance.py` gained **CG-7c** — acts 2, 3 and 4 had *no* machine
   check at all. The tool had been truthfully reporting "1 argument examined"
   over a population of four.
3. It gained **CG-7d**, which checks every act digest quoted *anywhere* in
   the repository, with a per-line exemption for values explicitly marked
   retired. That check immediately found a fifth stale copy, in the craft
   install record, that no reviewer had reported.

`[Inferred]` The generalizable lesson, recorded in `PROCESS-LESSONS.md`: a
derived value quoted for convenience is a promise, and a promise no tool
checks will go stale silently. Either check every copy or keep one.

## 4. Where this round stopped short

- **No review has bound the current bytes.** The battery predates the fix
  batch its own findings required, and the planned ninth review over the
  exact final manifest was never run — three reviewer sessions hit the
  account's session limit. Disclosed as the principal residual.
- **Twelve classes of finding were carried, not fixed** (`ROUND-DISPOSITIONS.md`
  §4, items A–L; item L alone enumerates 32 individual accounting residuals
  across six reviews). Each has a raw-report citation. The reason is uniform:
  fixing them meant editing digest-bound material after its review on a
  lead's judgment, which is the failure this record spent §3 describing.
- **The corpus is still roughly twice its target band** (99,094 words against
  35–50k). Compaction bought selection, not smallness. Whether selection is
  enough is a question the specification phase answers, not this report.

## 5. Verdict

`[Inferred]` The repository now tells the truth about itself to a stranger,
in about ten minutes, without hidden history — and it can be *checked* on
that claim mechanically, which is a stronger property than the claim itself.

It is not finished. It is legible, and its unfinished parts are enumerated
where a reader will find them rather than where an author would prefer them.
That was the round's actual goal, and on the evidence of eight independent
reviews it was met — with the four owner acts, and one more review, still
outstanding.
