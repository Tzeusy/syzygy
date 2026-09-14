# R-POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL — review 6 (raw, retained verbatim)

Independent fresh-context review. Read-only: no file in any repo or worktree
was edited, no state-changing git command was run, no `bd` write, no daemon,
no network, no Butlers checkout read. This file is the only file written.

## Subject and digests

Worktree `…/scratchpad/m2wt`, branch `agent/syzygy-dov.2`, commit
`da1497b92a8d4cb7da83ce426404f137c2667189` ("docs: M2 funnel review 5
retained and K1–K9 repaired [syzygy-dov.2]"); the worktree is clean
(`git status --porcelain` empty) and `main` is still
`a9f671e9d69e1a20c89c7f6ed0c6d9e58a644c1d` [Observed]. Sizes from `wc -c`,
digests from `sha256sum`, computed this session, never transcribed.

| File | Bytes | sha256 |
|---|---|---|
| `docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md` | 90210 | `d1a597c5f010afe5fe3143e0729824ab361f1c7997ff29f0f7d00f53d2ca262d` |
| `docs/evidence/polaris-m2-evidence-currency-funnel-2026-09-14.json` | 11067 | `ad53b1ff1bdb064807767d1e6cce714c4f3cd2a4ddd7be5fac4eafb0341658f5` |
| `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` | 30011 | `63d54c6e10d753a0b0c07c79b1c7a406f4221d304c29b4177d59681f1320d145` |

Inputs re-derived from, also computed this session:

| File | Bytes | sha256 |
|---|---|---|
| `docs/reviews/R-POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL-5-RAW.md` | 27581 | `205bd6634870a215c83c8bdf11f75b5a037445cec9a2b979aafafa0b8963cc9a` |
| `…/scratchpad/m1/measure/after/polaris-tailnet.html` (retained lane A capture) | 1484487 | `e8a04b4631dedbda159dd162d25f4e8a7ed4f9f4059a37ca1bca87b717790111` |
| `…/scratchpad/m1/measure/after/api-poc.json` | 5520314 | `a89b0e059b5fdadc5f359c2bee58115cd50747399cfb00444703e0fafdfb466e` |

The packet's review-5 header (27581 bytes, sha256 `205bd66…`) matches the
retained raw exactly; the capture's bytes and digest match the packet's and
the evidence record's claims exactly [Observed].

By verification rule 10 this review binds these bytes and no later ones.

## Checks run this session

All figures below were re-derived, not read off the packet.

- `python3 scripts/check_governance.py`, run from the worktree root →
  `32 OK, 20 WARN, 0 FAIL (52 checks)` [Observed].
- Claim tuples on the capture: 713 `<span class="claim-tuple">` opening tags;
  713 carry `data-epistemic-freshness`; all 713 are `fresh`. Full tuple
  shapes: `Observed/report-fact/fresh/unchallenged` × 702 and
  `Unknown/unstated/fresh/unchallenged` × 11 (challenge read from
  `data-challenge-state`). One distinct `data-evaluation-id`,
  `evaluation:pwb-body-read:2026-09-13T13:33:24.295Z`, 713 occurrences
  [Observed; predicate: the literal tag regex plus per-attribute extraction;
  denominator 713 = every such tag in the 1,481,819-character capture].
  Matches the Measurements table and the evidence record exactly.
- ISO instants: 719 in the bytes, 713 inside `data-evaluation-id`. With every
  tag blanked in place so offsets are preserved, 6 remain in text, at
  859145, 859189, 860858, 1477549, 1477638 and 1481753 — 57.98 % ("58.0 %"),
  58.09 %, 99.71 %, 99.72 %, 100.0 %. The two earlier `YYYY-MM-DD` strings
  are at 840110 (56.69 %) and 841381 (56.78 %), both inside a cited source
  filename [Observed]. Every figure agrees with the packet.
- `data-polaris-item="` → 409; bare `data-polaris-item` → 417; of which
  `data-polaris-items` → 8 [Observed]. Matches.
- Machine capture: `projectShape.items` 415, `sources` 278, `facts` 439,
  `projectAccount` 6 [Observed]. 13 fact keys contain `project-account`:
  six `item:project-account-section:<key>`, six `project-account:<key>`,
  one `count:project-account-section` — so the packet's "twelve keys among
  439" is the 6 + 6 pair forms and is correct [Observed; denominator 439].
- 22 of the 439 machine fact keys do not occur as literal strings in the
  served bytes: 6 `item:project-account-section:<key>`, 9 `count:<class>`,
  7 `catalog-count:<key>` [Observed; predicate: literal substring test of
  each key; denominator 439]. This is K9's figure exactly.
- `data-polaris-section="claim:project-account:` occurs 6 times;
  `claim:item:project-account-section` occurs 0 times [Observed].
- `grep -c 'return full'` over `apps/three-surface-poc/src/polaris-reading.ts`
  → **13**, at lines 44, 48, 49, 50, 51, 53, 61, 64, 72, 79, 88, 99, 103;
  confirmed by an independent Python `re` line sweep. One at 44, **twelve**
  structural [Observed; denominator: every `return full` in the file].
- Page-size arithmetic: 1,484,487 − 1,400,000 = 84,487; 1,478,637 −
  1,400,000 = 78,637; 2,097,152 − 1,484,487 = 612,665; 2,097,152 −
  1,478,637 = 618,515 [Observed]. The 1,478,637 direct figure and
  `q3Target.bytes` = 1,400,000 are both in
  `docs/evidence/pwb-m1-polaris-lane-a-measurement-2026-09-13.json`
  [Observed]. The "625 KB of narrative JSON" is that record's 639,806 bytes
  on the binary convention [Observed].
- Clause quotations checked against the defined locations and read in full:
  PWB-REQ-020 at spec lines 902–933 (SHALL sentence, Case, Observable,
  Oracle, Oracle independence, Mutation proof, Falsifier, Scenario);
  PWB-REQ-007 at 439–485 (SHALL 443–446, Falsifier 466–468, currency
  scenario 470–474, `warrants` at 480 listing `RFC2-9, RFC2-10`);
  PWB-REQ-004 at 491–498; PWB-REQ-014 at 763–765; CAP1-REQ-062 heading at
  line 1837 of the Capability 1 spec with the quoted sentence at 1841–1846;
  RFC2-9 at line 187 and RFC2-10 at line 209 of
  `.syzygy/governance/contracts/rfcs/RFC-0002/snapshot-and-evaluation-core.md`;
  VIS-2 at `vision.md`:96, VIS-7 at 183; `architecture.md`:221–236;
  `trust-and-evidence.md`:97–104. Every quoted string is verbatim at the
  cited location [Observed].
- Code citations re-read: `staleness.ts` `assessCurrency` opens at 87 and
  closes at 155, the `no-bound-declared` return object is 98–103 with its
  guard brace at 104, and the three `stale` returns carry
  `freshness: 'stale'` at 117, 132 and 142 — the packet's own correction of
  review 5's 121/133/143 is right [Observed]. `project-shape-model.ts`
  comment 162–166, `FRESH` at 167, assignments at 185 and 193, the
  `@syzygy/cap1-core` import at 19–27. `polaris.ts`:357 renders the four
  freshness sentences; 506–510 shows neither the selected-passages label nor
  the full-account disclosure when `condensed` is false and `chapters` is
  undefined; 1220 renders `classBlock(shape, 'project-account-section',
  false)`. `polaris-copy.ts`:45–49 (label plus four sentences).
  `walkthrough-preflight.ts`:212–220 collects terms from presented claims
  and tests `"<term> —"`. `git-observation.ts`:61 is `rev-parse HEAD`;
  `main.ts` 80–81, 113, 134, 187, 201 as cited. `model.ts` 100–110 defines
  the evaluation as `snapshot`, `snapshotLabel`, `inputsDigest`, `asOf`.
  `polaris-parity-sweep.test.ts` 202–209 carries the quoted comment
  (202–206) and the omission set (209) [Observed].
- `assessCurrency` appears in exactly three source files —
  `packages/cap1-core/src/staleness.ts` and two conformance tests — and 0
  times under `packages/three-surface-poc-core` or `apps/three-surface-poc`;
  no `dist/` tree in this worktree [Observed; two methods: `grep -rlF` and a
  file-list sweep].
- P-68 absence: `git show a9f671e:…/PENDING-OWNER-DECISIONS.md | grep -c
  P-68` → 0; `git ls-tree -r a9f671e` over the lane B directory → 0 paths;
  `find` over the worktree → 0 paths [Observed].
- CG-1b surface: no Butlers path appears in a backtick code span anywhere in
  the packet [Observed; predicate: `grep -nE` for a backticked span
  containing `about/`, `openspec/specs/`, `roster/`, `butler.toml`, `/v1.md`
  or `docs/superpowers/` → 0 rows].
- Code-span path resolution: 62 path-shaped code spans in the packet; 38
  resolve verbatim from the worktree root. The remaining 24 are the accepted
  classes — bare basenames used after a full path in the same sentence
  (`polaris.ts`, `main.ts`, `architecture.md`, `project-shape-model.ts`, …),
  the `decisions/…` shorthand (all three named act files verified present
  under `.syzygy/governance/decisions/`), glob forms (`packages/*/src`),
  routes (`/api/poc`), a package name, a branch name, a command, `dist/`,
  `-RAW.md`, and the lane B directory the packet explicitly says is absent
  from this branch [Observed]. No unresolvable path.
- Dossier identifiers: `S5-F1`, `L4-F1…F6` and `L4-M5` all resolve.
  `L4-F5` and `L4-F6` are in `docs/pursuits/2026-09-13-vision-pursuit-data.json`,
  not the summary markdown; a sweep of the markdown alone would report a
  false absence [Observed; the literal `L4-F` occurs 6 times in the summary,
  all F1–F4, and no continuation form appears].
- Not re-derivable under this review's constraints, and disclosed as such:
  the L4-F1 re-measurement (15 of 278 sources, 9 of 415 machine items, 9 of
  409 rendered rows) needs Butlers tree reads, which this review is
  forbidden [Unknown to this review; the evidence record names its methods
  and its 0-mismatch self-check].

## Findings

### L1 — non-blocking — `docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md`:461 and :534

**Defect.** Twice, unlabeled, the packet reads PWB-REQ-020's word
*disclosure* as a free-standing category the currency probe's facts fall
into: "it enters PWB-REQ-020's parity population as a 'disclosure Polaris
presents', so parity applies to it like any other" (461) and "Every horizon
*fact* the page renders (the probe claim, its instant, its counts) is a
disclosure Polaris presents and therefore enters that population in both
channels" (534). I read the clause. The enumeration is headed **"Every
project-shape identity, statement, source anchor, coverage state,
denominator, contradiction, body-read authority state and walkthrough-judgment
state or disclosure Polaris presents"** — the last item reads naturally as
"walkthrough-judgment state **or disclosure**", and both supporting bullets
confirm that pairing: the Case says "including every PWB-REQ-005 authority
state and **PWB-REQ-022 judgment state and disclosure**", and the Falsifier
says "one fact, authority state, **judgment state or disclosure**". PWB-REQ-022
is *Absent or unlawful owner judgment never becomes success* — the
walkthrough-judgment requirement. So the contrary reading, that *disclosure*
is scoped to PWB-REQ-022 and the enumeration's head is `project-shape`, is at
least as available as the packet's.

The tension is sharper because the packet relies on the opposite
characterisation forty lines earlier for a different purpose: line 470 says
the probe "is **not a project-shape claim**, so PWB-REQ-007's complete-tuple
requirement does not reach it". A claim that is not project-shape enough for
PWB-REQ-007 is being placed inside an enumeration whose head is
"Every project-shape …" without a word about the step.

Neither sentence carries `[Observed]` or `[Inferred]`, which AGENTS.md
§Epistemic discipline and verification rule 8 both require of a substantive
claim about a digest-bound clause. This is the sixth pass over PWB-REQ-020's
scope in this packet (F2, G5, H1, J6, K1 were the first five) and the first
one that reads the clause *against* the packet's own interest, which is why
it is non-blocking rather than blocking: if the narrower reading is right,
the probe simply sits outside the parity population, slice 3's
equal-multiset argument gets easier, and no recommended answer moves. But
an owner reading line 461 is told a contestable clause scope as settled fact.

**Repair.** Label both sentences `[Inferred]` and add the alternative in one
clause: PWB-REQ-020's Case attaches *disclosure* to the PWB-REQ-022 judgment
state, so the probe's facts may fall outside the enumerated population
entirely; slice 2 renders them in both channels either way, and slice 3's
argument holds under both readings. The verbatim enumeration already quoted
at 530–532 is the right anchor; it just needs the reading marked as one.

### L2 — non-blocking — `…FUNNEL.md`:1059

**Defect.** The J6 disposition row still reads "Accepted and repaired:
statements and anchor sets shared, six claim identities machine-only, the
twelve keys named, **PWB-REQ-020's direction** and the sweep's omission
stated". That "direction" clause is exactly what review 5's blocking K1 found
false and what the K1 row 25 lines below records as "the clause deleted". The
sibling J5 row at 1058 *was* annotated in place when K3 corrected it — "(the
row first said 'eleven', copied from J5 — review 5 finding K3)" — so the
packet's own convention is to mark the superseded sentence where it stands,
which is also the AGENTS.md docs lesson ("Mark staleness at the stale
sentence"). Row 1059 was left unmarked, so a reader working down the J-table
is told the direction reading was stated as a repair and is not told it was
withdrawn until the K-table.

**Repair.** One parenthetical, in the J5 row's shape: "(the direction clause
was withdrawn after review 5 finding K1)".

### L3 — editorial — `…FUNNEL.md`:534–535

**Defect.** "…and therefore enters that population in both channels **with
the same claim id and the same evaluation**." The intended referent is
"the same in both channels", which is right and is what PWB-REQ-020's
Falsifier ("associated with a different evaluation in either channel")
requires. But the probe's whole design is that it is a *second identified
evaluation*, distinct from the pinned one (slice 2, 443–446; Q3), and a
reader meeting "the same evaluation" in a paragraph about the pinned
evaluation's parity population can take it the other way — the precise
confusion Q3 exists to prevent.

**Repair.** "…with the same claim id and the same evaluation identity in
both channels".

### L4 — editorial — `…FUNNEL.md`:594, 606–613

**Defect.** Slice 6 opens "The dossier's L4-M5", but L4-M5's stated move is
to "render a named reduced-fidelity notice carrying **the plan id, the
expected and actual digests** and the route" (`docs/pursuits/2026-09-13-vision-pursuit-data.json`,
the L4-M5 record) [Observed]. The slice carries the route and a reason value
and drops the plan id and both digests, without saying so. That may well be
the right call — the reason vocabulary generalises to the twelve structural
guards, which digests do not — but a slice that names itself a dossier move
and then narrows it should say which part it kept.

**Repair.** One clause after "The dossier's L4-M5": "narrowed to a reason
value and a route; the plan id and the expected/actual digests L4-M5 named
are not carried, because the two non-digest reasons have no digests to show."

## K1–K9 verification

| # | Severity in review 5 | Verdict | Evidence |
|---|---|---|---|
| K1 | blocking | **REPAIRED** | The "one-directional human-to-machine invariant permits" clause is gone from slice 3; the string `one-directional` now occurs once in the packet, in the K1 disposition row itself, and nowhere in the evidence record or the register [Observed]. Lines 567–571 now read "Whether PWB-REQ-020's equal-multiset Observable permits a machine-only claim identity at all is the *same* open reading this slice already discloses above, and it is not settled here **[Inferred]**; if it does not, the six are a finding against the current implementation, never a precedent M2 may rely on." The sweep's omission is stated separately as `[Observed]` with the test lines (564–566). I read PWB-REQ-020 in full: the SHALL sentence is human→machine, and the Observable ("both populations contain equivalent multisets"), the Scenario ("the complete human fact multiset equals the machine fact multiset") and the Falsifier ("…in either channel") are the bidirectional limbs — the packet's verbatim quotation at 523–528 is exact and the open reading is now labeled, not settled. The labels are right: Observed for the sweep fact, Inferred for the clause reading, and the enumerated-population reading at 539–543 is still Inferred with its contingency. Gate 5's slice-3 sentence (726–728) carries the matching `[Inferred, see slice 3 …]`. No recommended answer moved. Residual: L1, which is a different sentence and a different limb |
| K2 | non-blocking | **REPAIRED** | Line 534 reads "is a disclosure Polaris presents"; the string "project-shape statement" survives only in the K2 disposition row [Observed] |
| K3 | non-blocking | **REPAIRED** | "twelve structural guards" at 599 and 608, twelve line numbers listed (48, 49, 50, 51, 53, 61, 64, 72, 79, 88, 99, 103), "thirteen guard returns" at 597, and the J5 disposition row at 1058 annotated. I counted independently: **13** `return full`, one at 44 and twelve structural, two methods agreeing [Observed]. "eleven" survives only in the two disposition rows that describe the miscount |
| K4 | non-blocking | **REPAIRED** | S3 (768–773) now reads "AND the probe's own claim carries no `data-epistemic-freshness` attribute, AND no `data-epistemic-freshness` value anywhere on the page is derived from it" — presence and derivation as two conjuncts. Line 474 reads "S3 requires both that …"; "already" is gone [Observed] |
| K5 | non-blocking | **REPAIRED** | Gate 6 item 4 (918–919) adds "the probe's no-freshness invariant (set `data-epistemic-freshness` on the probe's bracket and confirm S3's no-attribute conjunct fails)", which names the conjunct K4 created, so the mutant has something to fail against [Observed] |
| K6 | non-blocking | **REPAIRED** | Slice 6's Test (618–630) now names three cases, one per reason, and I checked each against the current function: `digest-mismatch` via a wrong `statementSha256` (line 44, first disjunct); `no-passages` via a matching digest and an empty list (line 44, second disjunct); `plan-malformed` via a passage whose `end` precedes its `start`, which is line 48's `end <= start` — the first structural guard in the loop, reached because line 44 passes and `previousEnd` starts at 0 [Observed, `polaris-reading.ts`:42–51]. Three rule-6 mutants are named ("drop the reason from each of the three returns in turn"), matching Gate 6 item 4's "one mutant per reason value", and the line-44 split is stated for the implementer at 627–630 |
| K7 | non-blocking | **REPAIRED** | The P-69 row's Q7 clause now reads "…recommended **`stale` with reason `no-currency-bound-declared` kept distinct** [Inferred], **against which stands RFC2-10's 'never dressed as a freshness state' — the packet weighs it and still prefers `stale` because PWB-REQ-007 requires the field on every project-shape tuple**; the alternative is a Capability 1 amendment so the engine carries the value, and slice 5 renders no undeclared class until Q7 is ruled" [Observed, register:200]. The counter-argument, the reason it does not win, the alternative and the hold are all there, matching the packet's Q7 |
| K8 | editorial | **REPAIRED** | Line 675 reads "**CAP1-REQ-062 assigning neither** a freshness value" — the agent is named, and the sentence no longer reads against the three `stale` returns at `staleness.ts`:117, 132, 142 [Observed] |
| K9 | editorial | **REPAIRED** | Line 559 reads "what the **machine's item population** carries and the **page's item rows** do not is six *claim identities*". I re-derived both populations: 409 distinct `claim:item:*` ids on the page against 415 machine items, difference six, each a `project-account-section` key; and separately 22 of 439 machine fact keys absent as literal strings (6 + 9 `count:` + 7 `catalog-count:`), the figure whose invisibility K9 named [Observed] |

## Q1–Q7

| # | Scope truthful? | Genuine gate? | Recommendation follows? | Register matches packet? |
|---|---|---|---|---|
| Q1 | Yes. The comment is at `project-shape-model.ts`:162–166 with `FRESH` at 167; RFC2-9's "Every claim class must declare a currency bound … before any of its claims can leave Unknown" is verbatim at RFC-0002:187; PWB-REQ-007's `warrants` block at spec:480 lists `RFC2-9, RFC2-10` [Observed] | Yes — a conformance ruling only the owner may make (VIS-4), and the packet says so | Yes. Rule 8 does not admit an implementation's reading of a clause as the clause; the current rendering is named a *disclosed* non-conformance, not declared unlawful | Yes |
| Q2 | Yes. The registry entry and both named act files exist at the cited paths [Observed] | Yes — an act-shape ruling | Yes. Arm (a) reuses an existing phrase, recorder and `--check`; arm (b)'s cost is concrete | Yes, including both act shapes by name |
| Q3 | Yes | Yes — and the packet says one arm is unlawful on its own reasoning and discloses it for confirmation rather than offering a free choice | Yes, on RFC2-10's evaluation scoping (verbatim at RFC-0002:209), with render-time drift explicitly kept as a non-ground | Yes, including "VIS-7's identity test is not the ground" |
| Q4 | Yes. `git-observation.ts`:61 is `rev-parse HEAD`; `main.ts`:80–81 calls it twice [Observed] | Yes | Yes. The absence claim is stated as "no act found", not "no act exists" — the right form under rule 9; the withdrawn unattended-coordination warrant stays withdrawn | Yes |
| Q5 | Yes. `polaris-copy.ts`:46–49 holds the four sentences, each rendered exactly once on the capture; `walkthrough-preflight.ts`:212–220 collects terms from *presented* claims and tests `"<term> —"`, so extra entries are permitted and a marker after the em-dash sentence cannot break it [Observed] | Yes — a copy ruling between two lawful arms | Yes, and both arms are stated lawful | Yes, including "both arms lawful" |
| Q6 | Yes. P-68 is absent from main's register at `a9f671e` and the lane B directory is absent from this branch, both disclosed and both re-checked [Observed: 0 and 0] | Yes — a sequencing ruling | Yes. Slices 1–4 and 6 touch no governed artifact; slice 5 touches the registry, not the spec | Yes — the row names slices 1–4 and 6, enumerates the five workstreams, and carries the lane-B-estimate conditionality the packet states in the collision section |
| Q7 | Yes. The `no-bound-declared` arm returns `state`, `label`, `reason`, `claimClass` and no `freshness` [Observed: `staleness.ts`:98–103]; PWB-REQ-007 requires freshness on every project-entity and project-fact claim (spec:443–446) and its Falsifier names "a tuple field is absent/out of vocabulary" (466–467); RFC2-10 closes the vocabulary (RFC-0002:209–223) | Yes — RFC2-10 says in terms that no implementation may make this choice | Yes, with the counter-argument quoted against it in both Q7 and slice 5, the reason it still loses, and the alternative with its CC-REV-2 route | Yes — K7 repaired |

Every clause of Q1–Q7 that carries a recommendation, a ground, an
alternative or a hold appears in both the packet and the P-69 row. The row
additionally carries the "Default if unanswered" sentence (a register field,
not a packet claim) and omits Q6's "honest target" sentence and Q1's
warrants-line citation; neither omission changes what the owner is asked.

## Regression spot-check (F1–F20, G1–G14, H1–H10, J1–J8)

Re-derived, not re-litigated. F1: all four arithmetic differences recomputed
above [Observed]. F8: `project-shape-model.ts`:19–27 already imports
`FRESHNESS_STATES` and `FreshnessState` from `@syzygy/cap1-core`, so slice 5
adds no boundary [Observed]. F14/G4: the six instants and the two earlier
filename dates re-derived at the offsets above [Observed]. F15/J7:
`assessCurrency` opens at 87 and closes at 155; "87–155" is right in Gate 1,
Gate 3 and slice 5 [Observed]. F17: three source files name
`assessCurrency`, 0 references in either POC tree, no `dist/` [Observed].
F18/H2: the `data-polaris-item="` predicate and the 417/8 disclosure
re-derived [Observed]. G8: the `stale` marker's reason is the
constant-assignment reason with slice 5 as its route, so it stops being true
exactly when slice 5 lands [Observed, 405–410]. G9/H4: Q5 is outside the
one-lawful-arm sentence and both arms are stated lawful in packet and row
[Observed]. H5: success criterion 5 reads "renders the condensed form and no
withdrawal sentence" [Observed]. H7: slice 6 is "medium" in the size
paragraph (15), the slice heading (592) and the summary block (1100)
[Observed]. H10: the evidence record's key is
`before_first_evaluation_instant` [Observed]. J1: PWB-REQ-004 is quoted
verbatim at lines 491–498 in slice 2, the slice-2 act row and Gate 5, with
the contingency in all three [Observed]. J4: criterion 2 (121–126) and S1
(755–761) both read "and, where one exists, the route" and both say the
oracle enforces the marker, not the route [Observed]. J8: the register's
review-2 clause matches G1/G2/G3 [Observed].

**No regression found.** The K1 repair is confined to the packet, and the
evidence record's `project_account_section_items` block never carried the
withdrawn characterisation.

## Other things a fresh reader would want said (no finding)

- The packet cites `architecture.md`:227 at line 509 for a sentence that
  begins on line 226 ("it may only degrade a claim (toward stale or /
  Unknown), never establish or improve one"). The citation lands inside the
  clause and Gate 2 quotes the full 221–229 window, so this is a wrap, not a
  miscitation.
- The packet's slice-3 citation of the parity sweep moved from 202–207
  (review 5's span) to 202–209. That is an improvement, not a drift: 202–206
  is the quoted comment and 209 is the `omitted` set that implements it
  [Observed].
- Line 21's baseline parenthetical ("the only working-tree change is a
  co-lead's in-flight `AGENTS.md`") describes the primary checkout at
  authoring time; this worktree is clean and `main` is still `a9f671e`, so
  the measurement baseline the sentence exists to fix is intact.
- The evidence record's `review5.re_derived_before_applying` block stores
  both the packet's `staleness.ts` stale-return lines (117, 132, 142) and
  the ones review 5 cited (121, 133, 143). Recording a review's wrong figure
  beside the right one, rather than quietly correcting it, is the right
  shape for a rule-10 record.
- The packet's `docs/reviews/` count is now five retained raws; this file
  will be the sixth and, per the packet's own rule, must be a new
  `-RAW.md`, never an overwrite of a digest-cited earlier one.

## Counts

Blocking 0. Non-blocking 2 (L1, L2). Editorial 2 (L3, L4). Total 4.

Verdict: CONFIRM WITH EXCEPTIONS
