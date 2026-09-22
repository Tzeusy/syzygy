# Confirmation review — PWB opening-band aggregate scenario (PWB-REQ-010)
Reviewed commit: dfb605cacfb95bac77501076ee5232ba41e733ac
Manifest SHA-256: 7f80cb05f644dd1e4f49e7b212d6972ee4754e40682450e59a6c3245546d5c46
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer: fresh-context session. No authoring context — this session did not
draft or repair the reviewed bytes, and no other agent working the parallel
2026-09-21/23 sitting was consulted, per CC-REV-1's independence
requirement. Read-only throughout; the one rule-6 mutation below ran on the
tracked worktree file and was reverted with `git checkout --` before any
other step, confirmed clean by `git status --porcelain`. Class: fresh-reader
confirmation review (rule 10) over the bytes at the commit above, against
`REVIEW-BRIEF.md`'s twelve criteria, the first review's three dispositions,
and the owner's 2026-09-23 rulings on OQ-1–OQ-5.

**Commission.** `REVIEW-BRIEF.md` states one review has already run
(`docs/reviews/R-PWB-OPENING-BAND-SCENARIO-DELTA-RAW.md`, commit `59733d3`,
CONFIRM WITH EXCEPTIONS, three notes) and that the brief "stays live" for
"any further review, including one over the repaired bytes." This review is
that further review, commissioned by the caller to confirm the repaired
bytes at `origin/main`, and independently to check the package against the
owner's 2026-09-23 answers to OQ-1 through OQ-5.

---

## What I ran

1. `git rev-parse HEAD` → `dfb605cacfb95bac77501076ee5232ba41e733ac`;
   `git rev-parse origin/main` → identical; `git status --porcelain` →
   empty at the start of the session.
2. `sha256sum PWB-OPENING-BAND-SCENARIO-MANIFEST.txt` →
   `7f80cb05f644dd1e4f49e7b212d6972ee4754e40682450e59a6c3245546d5c46`
   (scripted, never transcribed — rule 3). Equal to the digest quoted in
   `OWNER-DECISION-PACKET.md` and to the digest the first raw review names.
3. `python3 scripts/build_pwb_opening_band_scenario.py --check` → exit 0:
   "PWB opening-band scenario manifest matches 11 proposed behavior subjects
   (2 patched, 9 unchanged); the proposed declaration equals its
   regeneration and the spec patch composes with the lane B spec patch in
   both orders."
4. `--selftest` → exit 0: "closed population, byte drift, path order,
   subject drift, patch corruption, lane B composition (both orders and a
   corrupted case), generated-declaration tampering and the
   declaration-patch collision all fail closed" — matches criterion 10's
   named predicate list exactly.
5. **Rule 6, my own mutation, independent of the selftest's self-report.**
   In the tracked worktree (not a copy — see reviewer note above), flipped
   the first byte of the manifest's `spec.md` row digest (`9a44bdb6` →
   `0a44bdb6`) with `sed`. Re-ran `--check`: it failed — "PWB opening-band
   scenario manifest does not verify: manifest differs from exact
   regeneration over the proposed bytes", exit 1. Reverted with
   `git checkout --`, confirmed `git status --porcelain` empty, re-ran
   `sha256sum` (identical to step 2) and `--check` (passed, identical
   output to step 3). The checker fails closed on a tampered digest,
   confirmed by an externally authored mutation, not by the selftest's own
   fixture.
6. `git diff 59733d3 HEAD -- .syzygy/governance/contracts/candidates/pwb-opening-band-scenario/`
   and `--stat`: four files changed — `IMPACT-LEDGER.md`,
   `OWNER-DECISION-PACKET.md`, `REVIEW-BRIEF.md`, `SEMANTIC-DELTA.md` — 133
   insertions, 24 deletions, all prose. **No byte of `proposed/spec.md.patch`,
   `proposed/GOVERNING-DEPENDENCIES.md.patch` or
   `PWB-OPENING-BAND-SCENARIO-MANIFEST.txt` moved between the reviewed
   commit and this one**, confirmed by the diffstat naming only the four
   prose files and by the manifest digest in step 2 being unchanged. This
   means criteria 2, 3, 4, 5, 8, 10 and 12 — which the first review found
   clean by direct inspection of the patches, the manifest and the
   scenario's own bytes — are unaffected by the repair and still hold at
   this commit without re-derivation; my own work below focuses on the
   edited prose (criteria 1, 9, 11) and on the three dispositions.
7. Read all three edited prose files in full at this commit
   (`SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`, `OWNER-DECISION-PACKET.md`,
   `REVIEW-BRIEF.md`) and the diff against `59733d3` line by line.
8. **Finding 1's repair, independently re-derived.** Wrote a Python script
   reading `git ls-files -z` (captured to a plain file first; git output was
   not piped through a subprocess call, to respect this session's
   worktree-isolation constraints) over the current 1,384-file population,
   opened every path, and counted UTF-8 decode failures and literal
   NUL-byte occurrences separately. Result: **4** decode failures (all four
   PNGs `IMPACT-LEDGER.md` now names) and **6** NUL-byte files (the same
   four PNGs plus `packages/three-surface-poc-core/src/owner-act-record.ts`
   and `packages/three-surface-poc-core/src/project-shape-coverage.test.ts`)
   — the same paths and the same 4/6 split `IMPACT-LEDGER.md` reports,
   reproduced at a later, larger population than the ledger's own 1,343
   (the ledger's own denominator is a stated, different snapshot; both are
   internally consistent).
9. **Finding 3's repair, checked against the ruling record's actual bytes.**
   Read `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`
   rows P-74 and P-78 in full. P-74's "What it means" cell ends "The consent
   record, the registry entry and PWB-REQ-005 are edited on no arm." — one
   sentence closing the whole cell, which answers Q1–Q7, not scoped to Q4.
   P-78's "What it means" cell ends "The registry entry is edited on no
   arm." — same shape, closing a cell that answers Q1–Q5. Confirms the
   repair's substance: the sentence is a whole-row summary in both rows, not
   a Q4-scoped ruling, so withdrawing the "Q4" tag while keeping the
   substance is the correct repair. See finding A below for a residual
   quotation-fidelity nit this reveals.
10. **RFC2-26's defined clause, re-checked at this commit.** Read
    `.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md`
    lines 190–221 (via `DIRECTIVE-REGISTER.md`:260). The quoted sentences
    ("Before implementation, every observable consequence either maps to an
    approved OpenSpec requirement and scenario…" and "Rows are per
    observable consequence, not per clause.") are byte-exact against
    `SEMANTIC-DELTA.md` and `OWNER-DECISION-PACKET.md`'s quotations —
    unchanged by the repair and unaffected by it, since neither touched
    file quotes RFC2-26.
11. **Owner's 2026-09-23 answers to OQ-1–OQ-5, read in full.**
    `.syzygy/governance/decisions/POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md`
    §3 (OQ-1: "Fold into dov.26 package"; OQ-2: "(A) Under PWB-REQ-010") and
    `.syzygy/governance/decisions/POLARIS-GATE-PACKAGE-OPEN-QUESTIONS-2026-09-23-DECISION.md`
    §1 (OQ-3: "Keep clause; code adds secondary"; OQ-4: "Clarify inside
    .26"; OQ-5: "Account first, then band"). Checked each against the
    package's drafted text — see the dedicated section below. Both records
    state plainly that they perform no act, bind no digest and amend no
    specification byte, consistent with `AGENTS.md`'s prohibition on an
    agent adopting intent or a directive record binding by itself.
12. Hygiene sweep (criterion 11) on the four edited files: no occurrence of
    the current performed `spec.md` digest (`42d073c…`) outside
    `proposed/GOVERNING-DEPENDENCIES.md.patch` (a diff artifact, unedited by
    the repair); no `accepted`/`adopted`/`signed off` language describing
    the package itself (the only hits are "Accepted and repaired" /
    "Accepted; wording promoted" / "Accepted and withdrawn", which are the
    semantic-delta template's disposition verbs for a *review finding*, not
    a claim that the package is accepted); every file head still carries its
    candidate/inert banner.

---

## Prior findings — resolution

**Finding 1 (note) — the ledger's "none did" was false.** **Resolved.**
`IMPACT-LEDGER.md`'s Population section (lines 24–50) no longer asserts
"none did"; it now enumerates the four skipped paths, states the population
they were re-derived over (1,343), and adds the six-file NUL-byte remainder
with the predicate distinction ("binary" vs. "undecodable") that rule 2
demands of a second method returning a different set. Independently
re-derived at item 8 above: the same four paths decode-fail and the same
six carry a NUL byte. Quote, current bytes: "**Four** paths fail UTF-8
decode and are skipped, all binary images under `docs/evidence/`... A
NUL-byte scan over the same 1,343 files returns **six** files... which
carry a literal NUL byte yet decode as UTF-8 and were therefore swept, not
skipped."

**Finding 2 (note) — OQ-2 should not be rounded off.** **Resolved as a
wording promotion; correctly not resolved as a decision.** Both
`SEMANTIC-DELTA.md` (lines 401–410) and `OWNER-DECISION-PACKET.md` (lines
137–144) now carry the paragraph "OQ-2 is a precondition, not a placement
preference" / "Read this as a precondition, not a rounding error," stating
plainly that until OQ-2 is answered it is not settled that the scenario
clears RFC2-26 limb 1 even for slice 3. This is exactly what the
disposition promised — wording only, no decision taken inside the delta,
consistent with rule 6. The owner's 2026-09-23 answer to OQ-2 ("(A) Under
PWB-REQ-010") is on record in a *separate* file
(`POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md`), not inside
this package, which is the correct shape: the delta itself still does not
settle its own open question.

**Finding 3 (note) — the "Q4" attribution was tighter than the source.**
**Resolved.** All three prose files (`SEMANTIC-DELTA.md` line 514–518,
`IMPACT-LEDGER.md` lines 138–144, `OWNER-DECISION-PACKET.md` lines 198–202)
now say the sentence closes each row's whole "What it means" cell, name the
withdrawal of the earlier "Q4" tag explicitly, and cite `§Review finding 3`.
Verified against the ruling record's actual bytes at item 9 above: correct
— the sentence is a whole-cell summary in both P-74 and P-78, not scoped to
a numbered sub-question. See finding A below for a fidelity nit this
particular repair surfaces without introducing.

**What no disposition changed, verified.** `git diff --stat` (item 6) shows
only the four prose files; the manifest digest, the two `proposed/*.patch`
files, the scenario text, and all five open questions are byte-identical to
the reviewed commit. `SEMANTIC-DELTA.md`'s own closing line, "No patch
byte, no manifest row, no requirement, no scenario text, and none of the
five open questions [moved]," is true of these bytes.

---

## Consistency with the owner's 2026-09-23 answers to OQ-1–OQ-5

The task commissioning this review asked specifically whether the package
stays consistent with the owner's answers, which the owner's own records say
"required no byte change." Checked each:

- **OQ-1** ("Fold into dov.26 package"): matches the package's own route
  (a) — SEMANTIC-DELTA.md's OQ-1 names exactly this as one of the routes
  the owner might take ("a further OpenSpec amendment for slices 4–5,
  possibly inside the P-75 Q1 three-surface package at gate bead
  `syzygy-dov.26`"). No scenario text depends on slices 4–5; nothing to
  change.
- **OQ-2** ("(A) Under PWB-REQ-010"): the drafted placement, unchanged. The
  owner-values record itself states "OQ-2 keeps the drafted placement, so
  no patch byte moves and the reviewed manifest is unchanged" — confirmed
  true by the unchanged manifest digest.
- **OQ-3** ("Keep clause; code adds secondary"): the scenario's third bullet
  already reads "as PWB-REQ-007 requires of an aggregate" without softening
  the clause — the reading the owner selected is the one already drafted;
  no PWB-REQ-007 amendment is sought by this package either way.
- **OQ-4** ("Clarify inside .26"): the package already defers this question
  to a different signed specification's amendment ("not this package's to
  decide... the same package that OQ-1 already routes slices 4 and 5 to");
  the owner's answer routes it to the same place the package already named.
- **OQ-5** ("Account first, then band," with the currency probe before the
  Unknown aggregate inside the band): this is stated by the owner's own
  record to be "a design value for slices 2 and 3, not a specification
  sentence," compatible with and not requiring any change to the scenario's
  fourth bullet ("displaces and defers no project-level category of this
  requirement"), which constrains ordering relative to PWB-REQ-010's
  project-level categories only, not the internal order of the band.

All five check out: none of the owner's 2026-09-23 answers requires or
implies a byte this package has not already got right. No contradiction
found between the package's drafted text and any of the five answers.

---

## New findings

**Finding A — non-blocking.** The repair to finding 3 quotes the fragment
"is edited on no arm" (singular verb) as common ground between "the P-74
and P-78 rows" in three places (`SEMANTIC-DELTA.md`:514–518,
`IMPACT-LEDGER.md`:138–140, `OWNER-DECISION-PACKET.md`:198–200). P-78's
sentence is byte-exact: "The registry entry is edited on no arm." P-74's
sentence, however, reads "The consent record, the registry entry and
PWB-REQ-005 **are** edited on no arm" — a compound subject taking the
plural, not "is." Presenting "is edited on no arm" in quotation marks as
shared wording between both rows is a paraphrase of P-74 dressed as a
quotation of it (criterion 1, rule 8: nearby prose is not the clause — here
a grammatically adjacent conjugation is not the same sentence). The
substance is unaffected: P-74 does say the registry entry is one of three
items edited on no arm, and the repair's real content (withdrawing the
"Q4" tag) is correct regardless. This nit predates the repair — the same
quoted fragment, with the same imprecision against P-74, was already present
in the bytes the first review confirmed (`59733d3`) and was not flagged
there either, so it is not introduced by this repair. Non-blocking:
substance correct, form loosely quoted. **Suggested repair, not required
for this verdict:** attribute the quoted fragment to P-78 alone, or drop the
quotation marks and paraphrase both rows in the delta's own words.

**Finding B — editorial.** `REVIEW-BRIEF.md`'s repaired banner paragraph
(lines 10–18) is now, itself, singular in most of the corpus: it is one of
very few package files that name the *disposition* location correctly
(`SEMANTIC-DELTA.md` §Review) while also stating "This brief stays live... 
including one over the repaired bytes" — which is exactly the commission
this review discharges. No defect; noted only because a reader landing on
`REVIEW-BRIEF.md` first, without the two owner-ruling records this review
also had, would correctly conclude a fresh review over the repaired bytes
was still owed. That gap is now closed by this file. Editorial, informational
only.

No finding rises to blocking. Criteria 2, 3, 4, 5, 8, 10 and 12 are
unaffected by the repair (item 6) and remain clean on the record of the
first review, reconfirmed here by an independent `--check`/`--selftest`
run and an independent rule-6 mutation (items 3–5). Criteria 1, 6, 9 and 11
were re-checked directly against the edited bytes and hold, net of finding
A's non-blocking nit. Criterion 7 (RFC2-26) is unaffected: the repair
promotes wording, taking no new position on OQ-2, so the "clears slice 3
only, with OQ-2 open" claim (the first review's finding 2, restated rather
than resolved by design) stands exactly as the first review left it.

---

## Verdict rationale

CONFIRM WITH EXCEPTIONS. All three findings from the first review
(`docs/reviews/R-PWB-OPENING-BAND-SCENARIO-DELTA-RAW.md`, commit `59733d3`)
are resolved at this commit: finding 1 by enumeration (independently
re-derived here, same four-and-six split), finding 2 by wording promotion
with no decision taken (consistent with rule 6, and with the owner's actual
OQ-2 answer landing in a separate, non-binding record), and finding 3 by
withdrawing an over-scoped attribution while keeping the correct substance
(verified against the ruling record's own bytes). No patch byte, no
manifest row and no open question moved, confirmed by diff and by an
unchanged, independently-recomputed manifest digest, so the criteria the
first review verified against the package's machine-checkable bytes
(builder `--check`/`--selftest`, both re-run and re-mutated here; the
scenario's form; composability; the impact ledger's five swept figures,
which are unchanged since no swept byte moved) still hold without needing
re-derivation. The package also stays consistent with all five of the
owner's 2026-09-23 answers to OQ-1–OQ-5, none of which required or implies
an unmade byte change, matching what both owner-ruling records themselves
say. One new, non-blocking finding (A) is a quotation-fidelity nit
predating this repair, in a fragment substantively correct but loosely
quoted against P-74; one editorial note (B) is informational only. Neither
warrants REVISE. The package still performs no act, still leaves OQ-1,
OQ-3, OQ-4 and OQ-5 to the owner inside its own bytes (the 2026-09-23
answers to those live in separate direction records, correctly not folded
into the package), and a conforming implementation may still render no
opening aggregate at all.
