# R-PWB-OPENING-INDEX-AMENDMENT-5 — regeneration confirmation of P-98 over the P-99 sign-off
Reviewed commit: eda0e345b032ef279d0db231a983f1d963fe9c8f
Manifest SHA-256: 1afaa59d9e127c575c00770f8c6b2dffcaf099300dac23ec4c5e202b893178de
Verdict: CONFIRM WITH EXCEPTIONS

## Method and provenance

- Reviewer: fresh-context agent, round 5, briefed by `REVIEW-BRIEF.md`
  §"Round 5" of `.syzygy/governance/contracts/candidates/pwb-opening-index-amendment/`.
- Clone: `git clone git@github.com:Tzeusy/syzygy.git` into
  `/home/tze/.cache/claude-tmp-a3f4/r5-clone`, detached at
  `eda0e345b032ef279d0db231a983f1d963fe9c8f`. Round-4 reviewed commit
  compared against: `83b29c96775d9c2215292fa41e1599080f0b802c`.
- Head line 3 computed by `git -C <clone> show eda0e345…:<package>/PWB-OPENING-INDEX-AMENDMENT-MANIFEST.txt | sha256sum`.
  The same command at `83b29c96` gives `fe0791ef…441867`, the digest round 4
  bound, so the two differ as the regeneration says they must.
- No Butlers or other target-repository content was read; no daemon or
  observer was run. Nothing was edited, committed or pushed.
- Independent verifier: `/home/tze/.cache/claude-tmp-a3f4/r5tools/verify.py`
  (written for this round; imports neither the builder nor the engine). It
  reads bytes with `git show`, applies each `proposed/*.patch` with
  `git apply` in a scratch directory outside any repository, and hashes with
  `hashlib.sha256`. It checks every manifest row, the byte identity of the
  spec patch, the two-order composition over `spec.md` at `83b29c96`, the
  signed `spec.md` at `eda0e345` against `83b29c96` + the P-99 patch, and
  prints the signed-to-proposed `GOVERNING-DEPENDENCIES.md` diff.
- Rule 6 mutation of the verifier: run with the manifest read from
  `83b29c96` instead (argv hook) over the same `eda0e345` tree, it reports
  `rows matching: 9/11` (the two moved rows BAD), `composition equals
  manifest spec row: False` and `OVERALL FAIL`. Unmutated: `11/11`, `PASS`.
- Mechanics, each run with `env TMPDIR=/home/tze/.cache/claude-tmp-a3f4`
  from the clone, output read:
  - `build_pwb_opening_index_amendment.py --check`: exit 0, "opening-index
    candidate matches 11 proposed subjects (2 patched); 17 requirements, 63
    scenarios; structure, regeneration, contract coverage, sibling
    classification and pending-sibling composition (pairwise, and one result
    in every order) verify".
  - `--selftest`: exit 0, "position selftest: 4 fixtures fail closed with
    named findings" and "selftest: 50 structure mutants, … all fail closed on
    their own predicates".
  - `build_pwb_release_label_amendment.py --check`: exit 1, the single
    finding "GOVERNING-DEPENDENCIES.md.patch does not apply: error: patch
    failed: …/GOVERNING-DEPENDENCIES.md:9". Cause [Observed]: P-85's patch
    removes the `Source:` line carrying `107125b2…dfe7f1` (the pre-P-99
    `spec.md` digest, its line 6), while the signed `GOVERNING-DEPENDENCIES.md`
    at `eda0e345` now carries `c3ea81d9…2690a`, the post-P-99 digest. This
    is the expected failure: P-85 has not been regenerated over P-99.
  - `check_governance.py`: exit 0, "32 OK, 21 WARN, 0 FAIL (53 checks)";
    a sweep of the output finds 53 status lines and 0 starting `FAIL`. The
    WARN lines are report-only or by-design buckets (CG-8 18 and CG-27 18
    findings, CG-21 1, CG-24 1; the rest 0 findings).
  - `check_spec_reconciliation.py --check`: "7 of 7 predicates without
    FAIL; PASS". R2 "56 examined, 0 findings". R6 WARN, 2 findings: the
    adapter-registry and secret-classification pins name
    `0d50f8f4…`, current PWB `spec.md` is `c3ea81d9…` (Unknown until
    `syzygy-2g0d`); report-only and not introduced by this package.

## Criteria

1. **Spec patch byte-identical.** [Observed] `git rev-parse` gives blob
   `9e9d9efbc831c739d559962f85c7c2ed3995dba9` at both commits; the verifier
   compares the bytes directly (equal; sha256 `b0fc434d…380c` both). Pass.
2. **Regeneration only.** [Observed] `git diff 83b29c96 eda0e345` over the
   manifest changes exactly two rows (`GOVERNING-DEPENDENCIES.md`
   `0f56b63d…` → `69915806…`; `spec.md` `eb13c1e0…` → `44f4ad77…`); header
   comments and the other nine rows are unchanged. Over
   `proposed/GOVERNING-DEPENDENCIES.md.patch` it changes exactly the two
   `Source:` digest lines (old side `107125b2…` → `c3ea81d9…`, new side
   `eb13c1e0…` → `44f4ad77…`); hunk header, counts and context unchanged.
   Pass.
3. **Rows hash the produced bytes.** [Observed] Verifier: 11/11 rows match;
   the 2 patched rows equal sha256 of signed bytes at `eda0e345` with each
   patch applied, the 9 unpatched rows equal sha256 of the signed bytes.
   The proposed `GOVERNING-DEPENDENCIES.md` differs from the signed one only
   on line 11, whose new digest `44f4ad77…` equals the proposed `spec.md`
   row. Both patch targets are manifest rows. Pass.
4. **Composition.** [Observed] Over `spec.md` at `83b29c96` (sha256
   `107125b2…`), P-99's then P-98's spec patch and P-98's then P-99's both
   give `44f4ad77e62525595be5839883ac491d26bdd6859f353f91edc1d48903011ed2`,
   equal to the manifest's `spec.md` row. The signed `spec.md` at
   `eda0e345` (`c3ea81d9…`) equals `83b29c96` + P-99's patch, and P-99's
   spec patch is byte-identical at both commits. Pass.
5. **Nothing else changed.** [Observed] `git diff --stat 83b29c96 eda0e345`
   over the package directory, the builder and the engine lists five files:
   the manifest and GD patch (criterion 2); `REVIEW-BRIEF.md` (+103 lines,
   one hunk appended after line 385, the §"Round 5" section only);
   `ROUND-4-DISPOSITIONS.md` (see finding 1); and the engine (+3/−1: the
   `pwb-accessible-name-amendment` entry and its comment added to
   `PERFORMED_SIBLINGS`, removed from `PENDING_SIBLINGS`). The builder,
   `proposed/spec.md.patch`, `OWNER-DECISION-PACKET.md`, `SEMANTIC-DELTA.md`,
   `IMPACT-LEDGER.md` and `ROUND-1/2/3-DISPOSITIONS.md` are unchanged. Pass.
6. **PWB-REQ-016 (signed) against proposed PWB-REQ-010.** [Inferred] No
   contradiction found. Read clause by clause:
   - Distinct accessible names: the nine index rows are links whose targets
     differ, so the signed rule requires distinct names; REQ-010 makes each
     row's visible text begin with a different declared row name, so a
     conforming row already satisfies it and, where another link shares a
     row's visible label, the signed "begin with that visible label" rule is
     one a row's text already meets. A row whose target is not rendered
     "route[s] nowhere", so it is not a link with an `href` and falls outside
     the interactive population. The `exact-requirement` row routes to an
     element on the page (the first link to an exact requirement), not to an
     exact-source route response, so the signed path rule does not reach it.
   - Heading order: REQ-010 requires no heading of its own, and the stopping
     line's visible text is only numbers and a unit, so neither adds a level
     or a second `h1`. The signed rule constrains only successive headings
     and the `h1` count, neither of which the index fixes.
   - Populations: REQ-016 counts interactive elements and headings inside a
     closed `details`; REQ-010 excludes closed-`details` text from its word
     count. They measure different things and their hidden-element
     exclusions (`hidden`, `aria-hidden="true"`, `display: none`) agree.
   Pass.
7. **Mechanics.** As above: opening-index `--check` and `--selftest` pass;
   `check_governance.py` 0 FAIL of 53; `check_spec_reconciliation.py --check`
   PASS; release-label `--check` fails for the stated, expected reason. Pass.

## Findings

Every finding below is a note.

**Finding 1 — `ROUND-4-DISPOSITIONS.md` is wholly new since round 4, not only its dated section** (note)

[Observed] The file does not exist at `83b29c96`. It was created in
`e5cf8124` (113 lines, the round-4 sibling record under the 2026-09-26
ruling), and `eda0e345` adds 34 lines: the §"Regenerated over the P-99
sign-off, 2026-10-15" section. Criterion 5 names only "the dated section".
The rest is the notes-only round's own disposition record, which the
manifest does not hash and no builder reads, so it is no package change; a
future brief can name both commits.

**Finding 2 — Package prose still calls P-99 pending** (note)

[Observed] Stale since the P-99 sign-off, not made false by the
regeneration itself: `IMPACT-LEDGER.md` lines 86 and 92 ("the three still
pending: P-99, P-86 and P-85"; "the two still pending, P-99 and P-85");
`SEMANTIC-DELTA.md` line 311 and `OWNER-DECISION-PACKET.md` line 282
("three spec patches remain pending: this one, P-99 and P-85"); each also
says the package "was regenerated … in the cycle-3 repair", which is no
longer its latest regeneration. `SEMANTIC-DELTA.md` line 255 and the packet
row at line 203 condition on P-99 being signed, which it now is. The new
section of `ROUND-4-DISPOSITIONS.md` records the regeneration but its
§"Corrections carried here instead of in the package" does not list these
sentences. The round-5 sibling record can carry them.

**Finding 3 — "Its distinct-name rule covers them" is true of accessible names, not of visible text** (note)

[Inferred] The packet line 203 says that, with P-99 signed, "its
distinct-name rule covers" the rows, against the alternative that "nothing
stops another link on the page sharing a row's words". The signed
PWB-REQ-016 makes differently targeted links' *accessible names* differ and
start with their shared visible label; it does not forbid another link from
showing a row's visible words. So that sentence is right for the accessible
tree only; a sighted reader may still see two links with a row's words.
Round 4 cleared this prose and it is no contradiction between the two
requirements (criterion 6); it is worth one clause when the packet is next
revised.

**Finding 4 — P-85 and the P-95 pins remain stale over the signed tree** (note)

[Observed] Outside this package but in the battery: release-label
`--check` fails on its `GOVERNING-DEPENDENCIES.md.patch` (cause above), and
`check_spec_reconciliation.py` R6 reports two behaviour-contract pins
Unknown against the current `spec.md`. The P-99 sign-off record says both
follow from that sign-off. Signing P-98 moves `spec.md` again, so P-85 must
then be regenerated over P-98 as well, and the P-95 re-pin re-staled, as
`OWNER-DECISION-PACKET.md` §"Interaction with the P-95 re-pin" already says.

Count: 4 findings — 0 blocking, 0 revise, 4 note.
