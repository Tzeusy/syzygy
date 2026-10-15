# Impact ledger — PWB release-label amendment

> **Candidate — binds nothing.** A census of what the amendment touches and
> what cites the requirement it amends. It decides nothing.

## Predicate and population

[Observed, re-measured 2026-10-14 at `8f1fbec7` for the round-2 repair]

- **Population:** every tracked file at that commit, 2,658 paths
  (`git ls-tree -r -z --name-only 8f1fbec7`).
- **Predicate:** Python `re`, run form included:
  `PWB-REQ-(\d{3})((?:[ \t]*(?:/|,|–|\.\.|…|and)[ \t]*\d{3}\b)*)`. A file
  counts when any match's first number or any continuation number is `001`.
- **Result:** 95 files cite PWB-REQ-001. The same script at `0a10977b` gives
  1,947 paths and 74 files, the figures this ledger first published on
  2026-10-03.
- **Second method, implementation files only:** `git grep -l PWB-REQ-001`
  over `apps` and `packages` gives 8 files at `8f1fbec7` and 7 at
  `0a10977b`, equal to the script's rows below.
- **Re-measured 2026-10-14 at `814fbcc1` for the cycle-2 repair.** The
  same script gives 2,683 paths and 96 files. The one added file is under
  `docs/reviews/` (22 there now): this package's round-3 raw. Every other
  area count below is unchanged, and the second method still gives 8
  implementation files. The rows below keep their `8f1fbec7` figures.
- **Re-measured 2026-10-14 at `7460aec8` for the cycle-3 repair.** The
  same script gives 2,704 paths and 99 files. Against `814fbcc1`, three
  files are added: one under `docs/reviews/` (23 there now), this package's
  round-4 raw; and two under `contracts/candidates/` (31 there now), this
  package's `ROUND-3-DISPOSITIONS.md` and the accessible-name package's
  `ROUND-3-DISPOSITIONS.md`. The class-granular package's two files now
  belong to a performed package (P-86, signed v1.0 at `235b71eb`), so two
  pending packages remain among the citers, accessible-name and
  opening-index. Every other area count is unchanged, and the second method
  still gives 8 implementation files.

| Area | Files | Effect of this amendment |
|---|---:|---|
| `docs/reviews/` | 21 | None. Raw output is never edited (CC-REV-6). Two of them are this package's round-1 and round-2 raws. |
| Other `docs/` (plans, designs, evidence, pursuits) | 17 | None. Evidence records name the bytes they measured. |
| `.syzygy/governance/contracts/candidates/` | 29 | Nine are this package's own files. Four are files of three pending PWB packages: the accessible-name, class-granular (two files) and opening-index amendments, which name this package as a pending sibling; each of their builders' `--check`, which composes every pending spec patch in every order, passes over the repaired spec patch. One is the SEC-3 doctrine amendment's ledger, which cites PWB-REQ-001 and does not patch the PWB spec. The other fifteen belong to performed packages and repins: none. *(Marked 2026-10-15, cycle 4, for round-5 Note 4: "three pending PWB packages" and "each of their builders' `--check` … passes" are no longer true. All three are performed: class-granular (P-86) at `235b71eb`, accessible-name (P-99) and opening-index (P-98) on 2026-10-15. Their builders' `--check` is history for a performed package, and no pending sibling remains.)* |
| `openspec/changes/polaris-project-wide-butlers-model/` | 11 | Five patched (spec, capability coverage, design, proposal, contract-coverage repair delta) and two regenerated (`GOVERNING-DEPENDENCIES.md`, `CONTRACT-COVERAGE.md`). The three matrix files, the three parts files and `tasks.md` are unchanged. |
| `scripts/` | 7 | At sign-off, `check_spec_reconciliation.py` changes twice: its literal census (17 requirements, 55 scenarios, PWB-REQ-001 at 5) and the PWB child's successor chain. This package's builder is the guard itself. The others are unchanged: the coverage and dependency builders regenerate, and the three sibling builders are history. *(Marked 2026-10-15, cycle 4, for round-5 Note 4: "17 requirements, 55 scenarios, PWB-REQ-001 at 5" is no longer the census this sign-off would write. [Observed 2026-10-15] This package's builder `--check` over the cycle-4 bytes, on `main` after the P-98 sign-off, reports 17 requirements and 68 scenarios, and PWB-REQ-001 now carries six scenarios.)* |
| `packages/three-surface-poc-core/src/` | 5 | Implementation consumers. Sign-off authorizes no change to them. |
| `apps/three-surface-poc/src/` | 3 | The mutation sweep (two files) cites PWB-REQ-001's oracle, and `polaris-reconciliation.test.ts` cites the requirement. Sign-off authorizes no change. |
| `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` | 1 | Register row P-85 itself. |
| `AGENTS.md` | 1 | None. |

## Files a later implementation would touch

[Inferred — named for planning, not authorized]

- **Observer.** `apps/three-surface-poc/src/git-observation.ts` captures only
  `rev-parse HEAD` today (lines 62 and 106). It needs the tag set and commit
  ancestry, but only after the registry entry admits them.
- **Model.** `packages/three-surface-poc-core/src/project-shape-observation.ts`
  and `project-shape-model.ts` need the label value.
- **Polaris rendering.** It needs the label with the full object id beneath.
- **Not covered by this package.** `apps/three-surface-poc/src/page-shell.ts`
  line 41 renders the project revision in the footer shared by all surfaces,
  and `apps/three-surface-poc/src/orrery.ts` line 187 renders it in Orrery's
  eyebrow. Both are POC-governed on Trajectory and Orrery.
  *(Marked 2026-10-14: those lines and "footer" were measured at
  `0a10977b`, and the bullet missed that the shared component reaches
  Polaris. Re-measured at `814fbcc1`: `page-shell.ts` `humanStatusLine`
  (line 47) shows the project revision's twelve-digit prefix in the
  operability status line every surface renders, Polaris included, through
  `pageShell({ …, status })` (`polaris.ts` lines 1870–1882). Orrery shows it
  at `orrery.ts` lines 197 and 212. This version excepts that status line by
  name from PWB-REQ-001's visible-id prohibition and changes nothing in
  `page-shell.ts`; whether it should carry the label on Polaris is
  `OWNER-DECISION-PACKET.md` Question 5, which interacts with Question 3.)*
- **Polaris visible ids an implementation would mark.** [Observed at
  `814fbcc1`; Inferred as to what each needs] Polaris shows revision
  prefixes as per-claim provenance stamps (`polaris.ts` lines 241, 299,
  1200 and 1244, each a `data-parity-field="provenance-revision"` code
  element), in the shape fact line (line 1209), in prose sentences (lines
  298 and 1190) and in refusal sentences (`verbatim-route.ts` line 82;
  `capability-detail.ts` lines 231 and 238). Under this version each stamp
  is marked as a provenance stamp and carries no label; each prose or
  refusal occurrence either wraps its id in a marked stamp or becomes a
  label unit. Sign-off authorizes none of these changes.
  *(Marked 2026-10-14, cycle 3: "wraps its id in a marked stamp" is
  withdrawn. It is the route round 4 found let a page mark every naming as
  a stamp (raw Finding 1), and under this version a stamp is only the
  revision element of a citation, so a prose or refusal occurrence can no
  longer be one. The inventory also missed occurrences. Re-measured at
  `7460aec8`, with the treatment this version intends for each [Inferred as
  to what each needs]:*
  - *Citation stamps: `polaris.ts` lines 241, 299 and 1200. Each is a
    `provenance-revision` code element after a cite whose attributes come
    from `anchorAttrs`, which writes a `data-anchor-id` (line 216); at 299
    and 1200 the pair sits in a `citation` span. They stay stamps once the
    element around each pair holds nothing else, the cite names its record
    and the stamp's text is that record's revision. Line 1244's cite
    carries a `data-proposal-artifact` digest, not a record identity; it
    needs one to stay a stamp.*
  - *Running text, which becomes a label unit or drops the id: the shape
    statement (line 1190), the shape identity line "Revision …" (line 1209),
    the code-structure sentence (line 298), the currency-probe band
    "Evaluated at revision …", which shows the full observed revision
    (line 466; its `pinnedRevision` is the observed revision,
    `main.ts` lines 107 and 144), and the refusal sentences
    (`verbatim-route.ts` line 82; `capability-detail.ts` lines 231 and
    238).*
  - *Identities shown whole, excepted: the footer's evaluation identity on
    `/polaris` (`polaris.ts` line 1881) and on the exact-source route
    (`polaris-source.ts` line 140), whose text begins with the full revision
    (`production-reobserve.ts` lines 85–89), and the exact-source route's
    source identity line (`polaris-source.ts` line 117), whose identity
    holds it too (round-4 Note 2).*
  - *A naming before any label unit: the exact-source route's eyebrow,
    "Polaris · Butlers" followed by the twelve-digit prefix
    (`polaris-source.ts` line 135). Under the lead rule it becomes the
    page's label unit or drops the id.*
  - *Not a Polaris page under this version: the re-observation result
    (`reobserve-action.ts` line 25).*
  - *The Dolt revision in the work-items sentence and citation (`polaris.ts`
    lines 319–320) is not the observed Butlers revision, so the sweep does
    not count it.*

## Registry entry

[Observed]
`.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`
admits no tag ref and no commit-ancestry input. This package does not edit it.
See `SEMANTIC-DELTA.md` §"The read the owner's direction did not see".
