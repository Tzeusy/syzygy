# R-DOV29-3 — confirmation review of PR #121
Verdict: REVISE
Reviewed commit: 830718077d8235a7b55399d73058594c06574139
Manifest sha256: 2f60fd6352f472aec500e2efea7d9c85cf9f272ccd8bc98ccf2148388c628f73

Reviewer: fresh-context confirmation reviewer, read-only. Detached worktree
at the reviewed commit (branch `origin/agent/tier4-dov29`), parent chain
`21df27a` → `def4d6a` → `7d0049c` → `96ee305` (= `origin/main`, the PR #130
tip; `git merge-base HEAD origin/main` = `96ee305`). Nothing committed,
pushed or left edited; every mutation below was reverted and `git status`
was clean after each.

Head-line note: `REVIEW-BRIEF.md` sets no form for the manifest line (it
asks only for a leading verdict word, `REVIEW-BRIEF.md:99-100`). The act
argument is the digest of the manifest *file*: the phrase at
`OWNER-DECISION-PACKET.md:145` is `SIGN OFF PWB DISMISSAL-EXPIRY
AMENDMENT: <digest of PWB-DISMISSAL-EXPIRY-MANIFEST.txt>`, and the builder's
manifest header says the rows bind "by the owner act that names this file's
digest". The package has eleven row digests, none of which is the argument.
Line 4 therefore carries the manifest file's SHA-256, the same form as the
round-2 raw's line 4. The eleven row digests were re-derived separately
(command 5).

## Commands run and outputs read

All [Observed] at the reviewed commit unless labelled.

1. `python3 scripts/check_governance.py`: "32 OK, 20 WARN, 0 FAIL (52
   checks)", exit 0. CG-1b OK (6950 refs), CG-7d WARN 62 quotations 0
   findings, CG-7e OK (40 files, 0 findings), CG-15 OK, CG-22 OK, CG-26 OK
   (36 published, 36 hosted, 36 shared). `--selftest`: "285 fixtures, 0
   failing", exit 0.
2. Builder `--check`: "manifest matches 11 proposed subjects (6 patched, 5
   unchanged); ... 15 declared sibling-composition outcomes and the
   sequential sibling order verify", exit 0. `--selftest`: "121 mutants
   killed", exit 0. `--diff`: exit 0, prints the six patches.
3. `python3 scripts/check_docs_review_campaign_partition.py`: total=250
   assigned=250 raw=225 other=25 unmatched=0 overlaps=0; `docs/README.md:99`
   states "56 rows ... 250 files, 250 assigned". Consistent at this commit.
   The new campaign row's verdict cites (`R-DOV29-DISMISSAL-EXPIRY-DELTA-RAW.md:271`
   "Verdict: REVISE"; `-2-RAW.md:2` "Verdict: REVISE") match the raws.
   The retained round-2 raw is byte-identical to the scratchpad copy (`cmp`).
4. Manifest file digest, two methods: `sha256sum` and Python `hashlib` both
   give `2f60fd6352f472aec500e2efea7d9c85cf9f272ccd8bc98ccf2148388c628f73`,
   equal to the packet copies at `OWNER-DECISION-PACKET.md:22` and `:145`.
   The drafter-reported `2f60fd63…` is confirmed.
5. Manifest rows re-derived independently: `git archive` of the subject
   directory into a scratch tree, `git apply` of all six `proposed/*.patch`
   (all applied), Python `hashlib` over each of the 11 files, and `diff`
   against the manifest rows: identical (11/11). The five unchanged rows also
   equal `sha256sum` of the committed tree files.
6. Coverage totals, independent parse of the post-apply scratch tree: base
   matrix rows matching `^RFC\d+-\S+\.c\d+[a-z]?$` = 613; repair rows
   `^RFC\d+-\S+\.r\d+[a-z]?$` = 91; superseded base IDs = 77, 0 absent from
   base; effective 613 − 77 + 91 = **627**: covered 141, unknown-uncovered
   241, believed-not-applicable 245. Equal to the generated
   `CONTRACT-COVERAGE.md:11` line and to the packet's figures. The twelve
   dispositions named in `REPAIR_DISPOSITIONS` were read from the parsed rows
   and match (RFC1-20.r1, RFC1-25.r1, RFC2-15.r1, RFC6-14.r5, RFC6-14.r6,
   RFC2-1.r2 unknown-uncovered; RFC1-12.r2, RFC1-25.r2 believed-not-applicable;
   RFC1-12.r1, RFC2-1.r3, RFC6-14.r4, RFC6-17.r7 covered).
7. Impact sweep at `3ee61c7`, Python over `git ls-tree -r -z` + `git show`:
   1,537 files, 1,533 decoded; `PWB-REQ-007` 113 files / 540 occurrences.
   Published continuation regex (`IMPACT-LEDGER.md:47-49`) → 7 lines / 6
   files. Published range regex (`:58-59`) → 13 lines / 9 files carrying a
   range, 7 lines / 6 files spanning 007. A broader range regex (also `-`
   and `to` separators, `\s*`) adds no line spanning 007. All equal the
   ledger. Spec-digest pins (12-char prefix of the current `spec.md`
   digest): 19 files at `3ee61c7`; 20 at HEAD, the one addition being this
   package's own `proposed/GOVERNING-DEPENDENCIES.md.patch`.
8. Quotation fidelity (rule 8): each of the 19 blockquotes in
   `SEMANTIC-DELTA.md` after the banner was whitespace- and emphasis-folded
   and located at its definition site: P-79 Ruled cell and What-it-means
   cell; the spec's PWB-REQ-007 sentence; RFC2-15 (both, `reconciliation-chain.md`);
   RFC1-20, RFC1-25 `dismisses` row, RFC1-18, RFC1-5 rows, RFC1-12
   (RFC-0001); RFC2-24 row 9 and RFC2-25 (`rendering-vocabularies.md`);
   RFC2-13 (`challenge-lifecycle.md`); RFC2-1 item 9
   (`snapshot-and-evaluation-core.md`); RFC6-14; VIS-6(a) and its violation
   line (`vision.md`); the M12 funnel's three arms (each checked
   separately) and slice-4 lines. 19/19 found; the retention quote's
   elision is marked.
9. CG-7e after #130 (N11): changing one hex character of the bare digest at
   `OWNER-DECISION-PACKET.md:22` (`2f60fd63` → `2f60fd64`) makes
   `check_governance.py` report "FAIL CG-7e ... 1 finding". Restored; clean.
10. VIS-4 sweep: `adopted|accepted|approved|signed off|in force|binds` over
    the package's `*.md` and `proposed/*.patch`, excluding "binds nothing"
    and "signed PWB/spec/behav…": 17 hits, all contract or clause context
    ("accepted contracts", "binds a record to a claim", `unadopted-draft`),
    none claiming this package binds or is adopted. The phrase is marked not
    offered (`OWNER-DECISION-PACKET.md:141-152`).
11. Registration diff in `scripts/check_governance.py`: label, dir, subject,
    act path, `_act_subjects()` entry, `ACT_DIGEST_COPY_FILES` packet row,
    existence-gated activation and selftest rows; no `PWB_SUCCESSOR_CHAIN`
    link; CG-26 lists untouched.

### Rule-6 mutations by this reviewer

Harness A (in-process): take the builder's own proposed bytes, mutate
`spec.md`, regenerate `GOVERNING-DEPENDENCIES.md` with the dependency
generator (what a drafter's `--write` path needs), then run the builder's
`requirement_findings` and `dependency_findings`. Harness B (end-to-end, in
the worktree): `--apply --at-adoption`, mutate `spec.md`, regenerate
dependencies, `git diff -U1` both files into `proposed/`, restore the tree,
`--write`, `--check`, rewrite every registered copy of the old manifest
digest to the new one, then `check_governance.py`. Denominators given per
group.

Round-2 survivors, re-run (Harness A), 5/5 killed:
- P3 add "A dismissed Unknown claim is removed from the aggregate's Unknown
  total." — KILLED (forbidden removal wording).
- P5 "Otherwise it is a lapsed record" → "Otherwise it is a refused record
  also" — KILLED (lapse conditions; second refusal route).
- P9 add "Yet a model assertion MAY dismiss a claim." — KILLED (permissive
  dismissal source).
- P10 drop "freshness," from the fact list — KILLED (every fact named).
- S1 add a Scenario-1 AND line "once the expiry passes, the first evaluation
  renders the claim without the sibling state" — KILLED (once-only phrase).

New spec-text mutants, 15 attempted, 13 hit; 2 KILLED, 11 SURVIVED
(Harness A; the five marked † also run through Harness B, where `--write`
0, `--check` 0 and `check_governance.py` "32 OK, 20 WARN, 0 FAIL"):
- KILLED: M3 "Unknown" → "Unknown or Inferred" in the scope sentence;
  M10 drop "expiry instant," from the refused test.
- SURVIVED: M1† add "A dismissed claim is not counted in the aggregate's
  Unknown headline."; M2† in-effect conjunction "…expiry instant **and** the
  claim's primary reason…" → "**or**" (substitution: a dismissal stays in
  effect after expiry while the reason matches); M4 add "A lapsed record is
  disclosed as a refused record."; M5 Scenario 1 "renders the same claim
  state" → "…until the page is refreshed, when the claim shows plain
  Unknown"; M6 Scenario 2 add "though the headline shows it as resolved";
  M7† refused guard "neither carries nor records as retired" → "does not
  carry" (substitution: retired records become refused, reversing the class
  precedence); M8 Scenario 3 add "the second record then applies to the
  successor"; M9† add "A model assertion SHALL dismiss a claim when the
  owner is absent."; M11 Scenario 1 add "(the first evaluation is re-derived
  at read time)"; M12 add "(it renders green)"; M13 add "except that the
  machine view MAY omit the tuple"; M14† Scenario 3 "as lapsed" → "as
  lapsed and as refused" (contradicts the same scenario's last line).

Builder-source mutants, 6; 5 KILLED by `--selftest` or `--check`, 1 SURVIVED:
- KILLED: delete FORBIDDEN "claim-reason refusal"; break the "removal"
  regex; RFC6-14.r5 disposition → believed-not-applicable; lane-B spec
  outcome collide → compose; drop the disposition comparison in
  `companion_findings`.
- SURVIVED: drop `"without the sibling state"` from `SCENARIO_ONCE`
  (`scripts/build_pwb_dismissal_expiry_amendment.py:230-232`) — `--check`
  0, `--selftest` exit 0 reporting "120 mutants killed". The selftest
  derives its mutants from the same table (`:806`), so a removed rule
  removes its own test.

## Resolution of round-2 findings N1–N11

| # | Round 2 | Status | Evidence |
|---|---|---|---|
| N1 | revise | Resolved | Scenario 2 now refuses "a record whose own dismissed primary reason is `contradicted-pending-adjudication` or `challenge-suspended`" (`proposed/spec.md.patch:102-105`); the paragraph's refused test is "itself names, as the reason it dismisses" (:40-41); the lapsed test covers a claim that moved to an undismissable reason (:46-48); Scenario 3 says so (:113-114). FORBIDDEN "claim-reason refusal" guards the old wording (killed when deleted). |
| N2 | revise | Resolved as stated, with R1 below | Order refused → retired → lapsed, first match wins (:35-37), each later test opened by "Otherwise"; Falsifier line (:76-77). The two cases N2 named now decide: (a) incomplete + retired → refused; (b) complete + retired + expired → retired. See R1 for a reachable state the order classifies against criterion 8. |
| N3 | note | Resolved | "per-label, tier, freshness and reason count" in paragraph (:31), Scenario 2 (:100) and Falsifier (:74-75); the full kept-fact list is a builder rule (P10 killed). |
| N4 | note | Resolved for the named mutants | P3, P5, P9, P10, S1 all killed (above); the packet's dated corrections to dispositions 6 and 12 are present (`OWNER-DECISION-PACKET.md:244`, `:250`). Guards remain presence-and-wordlist only; see N-B1. |
| N5 | note | Resolved | Q2 gives both readings labelled [Inferred] (`OWNER-DECISION-PACKET.md:78-85`). |
| N6 | note | Resolved | Q1 lists the three funnel arms, places the draft nearest arm 2 and quotes L2-M8's objection (:64-77). |
| N7 | note | Resolved | RFC6-14.r5 `unknown-uncovered` (`proposed/CONTRACT-COVERAGE-REPAIR-DELTA.md.patch:38`); totals 627/141/241/245 reproduced (command 6). |
| N8 | note | Resolved | Regex published with separators and case (`IMPACT-LEDGER.md:47-49`); hyphen form disclosed (:51-56); reproduced 7/6 (command 7). |
| N9 | note | Resolved at the site named | `OWNER-DECISION-PACKET.md:160-161` now says "ruled 'no promotion' and deferred only the write act". See N-A2 for a sibling sentence. |
| N10 | note | Partially resolved; recurs | The packet now names `8cf689d`, but then names `6e6d60c` and `28b88a3` on `08d4d02` (`OWNER-DECISION-PACKET.md:230-232`); neither is on any remote branch nor an ancestor of the reviewed commit, and the rebase onto `96ee305` (#130) that produced `7d0049c`/`def4d6a`/`21df27a` is not recorded. See N-A3. |
| N11 | note | Resolved (by PR #130) | A one-hex change to the bare copy at `OWNER-DECISION-PACKET.md:22` now fails CG-7e (command 9). |

## New findings

### R1 — revise — a record for a claim that has simply vanished is disclosed as refused (criteria 8, 16)

[Observed] The refused test includes a record that "names a claim identity
the evaluation neither carries nor records as retired"
(`proposed/spec.md.patch:39-40`), and refused is tested first (:35-37). The
retired class covers only an identity "a split or merge has retired"
(:41-42). [Inferred] A claim identity can leave an evaluation without any
split or merge: the observed project deletes or renames the declaration a
claim is derived from, and the next evaluation no longer carries it. PWB
specifies no retirement recording at all (a grep of the current `spec.md`
for `split|merge|retired` returns no line). A complete, once-in-effect
record for such a claim meets the refused test and is disclosed as refused,
i.e. as a record that tried to dismiss without authority. Criterion 8 asks
that "a valid record that no longer applies is shown as lapsed or bound to a
retired identity, never refused"; Scenario 3's own title says the same
("A record that no longer applies is lapsed or retired, never refused",
:107). The same predicate split also bites the retired case: Scenario 3's
WHEN is world-side ("a claim identity that a split or merge has retired",
:111), while the refused guard is evaluation-side ("records as retired"),
so a split the evaluation does not record is refused by the paragraph and
never refused by Scenario 3. The owner packet describes the refused case
as "names a claim that does not exist" (`OWNER-DECISION-PACKET.md:53`),
which a non-specialist reads as "never existed", not "no longer carried".

Repair options (drafter's choice, or route to the owner): classify "names a
claim identity the evaluation does not carry and does not record as
retired" as lapsed with its condition stated (the evaluation cannot tell a
mistyped identity from a vanished one), or add it as its own disclosed
condition; and make Scenario 3's WHEN and the retired test use the same
evaluation-side predicate ("an identity the evaluation records as retired
by a split or merge"). Fix the packet's plain-language gloss to match.

### N-A1 — note — a record that never applied is disclosed as "lapsed"

[Observed] The lapse condition is "the claim's primary reason is no longer
the one it dismissed, including because the claim is no longer Unknown"
(`proposed/spec.md.patch:45-47`). [Inferred] A complete record that named
a dismissable reason the claim never carried, or a claim that was never
Unknown, meets no refused test and falls to lapsed, and is disclosed with a
condition phrased "no longer", implying it once took effect. Consider "is
not" in the condition, or a condition value that distinguishes
"never matched".

### N-A2 — note — owner-attribution wording, two places

[Observed] (a) `OWNER-DECISION-PACKET.md:83-84` says "Your question-4
answer deferred any write act". The Ruled cell says "write act deferred"
(`POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md:67`); "any" widens it.
The packet's own `:160-161` gets this right ("deferred only the write act").
The broader bar exists, but in the retention direction's item 7, not in the
Q4 answer. (b) `OWNER-DECISION-PACKET.md:13-15` and `SEMANTIC-DELTA.md:3-6`
call the P-79 Q5 answer "direction to draft". The Ruled cell says only that
a dismissal "is an amendment — CC-REV-2 delta plus a new act before any
dismissal touches a tuple". [Inferred] "to draft" is the drafter's reading.
Label it, or say "the answer requires a delta and an act". `SEMANTIC-DELTA.md:44-46`
quotes "slice 4 waits for the dismissal delta, its sign-off and act" as
something the row "records". That text is in the "What it means" column, the
recorder's words. The attribution is to the row, not to the owner, so it is
acceptable, but naming the column would be exact. No other owner-attributed
text was found. P-79 Q4/Q5 match the Ruled cell. The retention quotes match
the direction's issued text. The landing order ".21 → .30 → .22 → lane B" is
the text of the option the owner selected verbatim ("Readiness order, lane B
last (Recommended)", `POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md:114-118`).

### N-A3 — note — review record still names off-branch commits (N10 recurs)

[Observed] `OWNER-DECISION-PACKET.md:230-232` says the branch was rebased
"onto `08d4d02`, where the draft is `6e6d60c` and the round-1 repair
`28b88a3`". Both commits exist locally but are contained in no remote
branch and are not ancestors of the reviewed commit. The reviewed chain is
`7d0049c` (draft) → `def4d6a` (round-1 repair) → `21df27a` (round-2 repair)
→ `8307180`, on `96ee305`. The #130 rebase is unrecorded. The manifest
binding is unaffected.

### N-B1 — note — builder guards stay presence-plus-wordlist; two substitutions survive

[Observed] 11 of 13 new spec-text mutants survive every check (listed above).
Nine are additive contradictions, which a presence checker cannot be
expected to catch. Two are one-token substitutions inside required
semantics that the rules do not pin:
- M2: "and" → "or" between the expiry test and the reason-currency test.
  The rules "expiry boundary" and "reason currency" are separate substrings
  (`scripts/build_pwb_dismissal_expiry_amendment.py:112-118`), so the
  connective is free. The mutant makes a dismissal outlive its expiry.
- M7: the refused guard's "nor records as retired". It is not inside any
  rule, so dropping it silently reverses refused-versus-retired precedence.

Separately, `SCENARIO_ONCE` is self-testing: removing a phrase removes its
mutant, and `--selftest` still exits 0 (count 121 → 120). [Inferred] Joining
the two in-effect rules into one rule string, extending the refused rule
through "records as retired", and asserting the selftest's mutant count, or
a fixed `SCENARIO_ONCE` population, would kill all three. The manifest
digest remains the real guard on these bytes. The packet claims no more
than that (`OWNER-DECISION-PACKET.md:270`).

### N-C1 — note — RFC1-12.r1 credited `covered` though "re-dismissal is an owner act" rests on open Q3

[Observed] RFC1-12 ends "re-dismissal is an owner act". RFC1-12.r1's
effective consequence reads "re-dismissal needs a new record"
(`proposed/CONTRACT-COVERAGE-REPAIR-DELTA.md.patch:29`), and the paragraph
admits any "attributed human decision" (`proposed/spec.md.patch:8`). Packet
Q3 asks whether that should be "the owner" (`OWNER-DECISION-PACKET.md:86-88`).
[Inferred] The package holds rows that depend on open Q4 at
`unknown-uncovered`. It credits RFC1-12.r1 `covered` while its owner-act
component depends on open Q3. The retired class is also unreachable under
today's PWB, which specifies no split, merge or retirement record; the
IMPACT-LEDGER labels that conditional at `:95`. Consider holding the row
Unknown until Q3 is answered, or saying in the row why an attributed human
record meets "owner act". `SEMANTIC-DELTA.md:327-328` calls a lapsed
record "a valid owner act", which the paragraph does not require.

### N-C2 — note — VIS-2: the dismissed count when the record set cannot be read

[Observed] The paragraph makes "every dismissal record present in the
governed plane at an evaluation's snapshot" an input (:11-12) and requires
dismissed members to be "additionally ... counted" (:32). It does not say
what an evaluation renders when that record set cannot be read, or when no
home exists (Q2 is open, so no home exists today). [Inferred] Claims stay
Unknown in that case, which is the safe polarity, so no claim goes green.
But a dismissed count of 0, and an empty refused or lapsed disclosure,
would be a zero produced by missing evidence. Consider one sentence: an
unreadable or undesignated record set is disclosed as Unknown, never as
zero dismissed.

### N-C3 — note — two records in effect for one claim

[Inferred] Nothing in the paragraph prevents two complete, unexpired
records for the same claim and reason. The in-effect rendering names one
reason, expiry, author and record identity
(`proposed/spec.md.patch:26-27`). Which record renders, or whether both
render, is unstated. Human/machine parity is required, so an implementation
must choose, and the text does not fix the choice. A reachable state, not in
any class.

## Confirmed without finding

[Observed] No wall clock: the in-effect test is at the evaluation's own
as-of instant (:18-22). Scenario 1 re-reads the first evaluation after the
expiry and requires the same state (:88-89). Equality means lapsed:
"earlier than" (:19) and "not earlier than" (:45) are exact complements, and
Scenario 1 tests equality (:84-85). No tuple value changes (:29). The
challenge vocabulary and `CHALLENGE_STATES` are untouched. RFC2-13's
`resolved-dismissed` is kept distinct (`SEMANTIC-DELTA.md:243-251`).
VIS-2 per claim: only Unknown claims may be dismissed, the label stays
visible, dismissed members stay in every label, tier, freshness and reason
count, and nothing renders them as positive, resolved, aligned or current.
Proposal, capability row 32 and totals 26/6/32 are consistent. The six
patched and five unchanged subjects match (command 5). No adoption is
claimed (VIS-4). No Butlers path appears in this raw.

## Verdict

REVISE. R1 alone blocks: a reachable record state, a valid record whose
claim no longer exists for a reason other than split or merge, is
classified refused, against criterion 8 and Scenario 3's title. The notes
N-A1 through N-C3 do not block on their own. Owner-only questions still
open are the packet's Q1 to Q12. R1 can be repaired in the bytes or routed
as a thirteenth question.
