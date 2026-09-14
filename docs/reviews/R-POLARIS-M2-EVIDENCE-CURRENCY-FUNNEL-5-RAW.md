# R-POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL — review 5 (raw, retained verbatim)

Independent fresh-context review. Read-only: no file in any repo or worktree
was edited, no state-changing git command was run, no `bd` write, no daemon,
no network, no Butlers checkout read. This file is the only file written.

## Subject and digests

Worktree `…/scratchpad/m2wt`, branch `agent/syzygy-dov.2`, commit
`1befd6f` ("docs: Polaris M2 funnel packet — review 4 retained and J1–J8
repaired [syzygy-dov.2]"). Sizes from `wc -c`, digests from `sha256sum`,
computed this session, never transcribed.

| File | Bytes | sha256 |
|---|---|---|
| `docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md` | 85236 | `6be6ccb0c6a55947e39468749492c63aa9ba0d4942dbf0853c4e0eaa35493798` |
| `docs/evidence/polaris-m2-evidence-currency-funnel-2026-09-14.json` | 9870 | `f50dbd787814caa2c845b236188cfc180287e905fd0c73af6a9822c9e2da8fb2` |
| `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` | 29513 | `653e2a933b25a3999d32d3497e585b2da7702d5b65a74b04fe9aa82bdaa298af` |

Inputs re-derived from, also computed this session:

| File | Bytes | sha256 |
|---|---|---|
| `…/scratchpad/m1/measure/after/polaris-tailnet.html` (retained lane A capture) | 1484487 | `e8a04b4631dedbda159dd162d25f4e8a7ed4f9f4059a37ca1bca87b717790111` |
| `…/scratchpad/m1/measure/after/api-poc.json` | 5520314 | `a89b0e059b5fdadc5f359c2bee58115cd50747399cfb00444703e0fafdfb466e` |
| `packages/cap1-core/src/staleness.ts` | — | `520305502eed72a3ac0c0bf3c2e05ca4ae81a031ac41b60e8f02739e7ad2b31d` |
| `apps/three-surface-poc/src/polaris-reading.ts` | — | `bea0e59d36ac1f4c9d671eda88f4ba7ab39ac7f5c198461d977e09321ededdc3` |

The capture's byte size and digest match the packet's and the evidence
record's claims exactly [Observed].

By verification rule 10 this review binds these bytes and no later ones.

## Checks run this session

- `python3 scripts/check_governance.py` → `32 OK, 20 WARN, 0 FAIL (52 checks)`
  [Observed].
- Every `data-epistemic-freshness`-bearing `<span class="claim-tuple">` tag on
  the capture parsed: 713 tags, 713 `fresh`; tuple shapes
  `Observed/report-fact/fresh/unchallenged` × 702 and
  `Unknown/unstated/fresh/unchallenged` × 11; one distinct
  `data-evaluation-id`. Matches the packet's Measurements table and the
  evidence record exactly [Observed; predicate: the literal tag regex
  `<span class="claim-tuple"[^>]*>` plus per-attribute extraction; denominator
  713 = every such tag in the 1,481,819-character capture].
- Four freshness glossary sentences, each occurring exactly once [Observed;
  predicate: literal substring count of each sentence].
- Human-visible ISO instants: 6, at character offsets 859145, 859189, 860858,
  1477549, 1477638, 1481753; first at 57.98 % ("58.0 %" as the packet rounds
  it). Two earlier `YYYY-MM-DD` strings at 840110 (56.69 %) and 841381
  (56.78 %), both inside the cited filename
  `…/specs/2026-08-24-whatsapp-identity-r…`. Denominator 719 ISO instants in
  the bytes [Observed; predicate: tags blanked in place so offsets are
  preserved, then `\d{4}-\d{2}-\d{2}T\d{2}:\d{2}` over the residue]. Every
  figure agrees with the packet and the evidence record.
- `data-polaris-item="` → 409; bare `data-polaris-item` → 417; of which
  `data-polaris-items` → 8 [Observed]. Matches.
- Machine capture: `projectShape.items` 415, `sources` 278, `facts` 439,
  `projectAccount` 6 [Observed].
- Page claim-id families: 713 `data-claim-id` occurrences over 703 distinct
  ids — `claim:item:*` 419 occurrences / 409 distinct, `claim:source:*` 278,
  `claim:class:*` 9, `claim:project-account:*` 6, `claim:project-shape:*` 1
  [Observed].
- `check_governance` CG-1b surface: no Butlers path appears in a backtick code
  span anywhere in the packet [Observed; predicate: `grep -nE` for backtick +
  `about/`, `openspec/specs/`, `roster/`, `butler.toml`, `v1.md` → 0 rows].
  The Butlers paths in the evidence record are JSON string values, not code
  spans.
- Code-span path resolution: 47 path-shaped code spans in the packet; 31
  resolve verbatim from the worktree root; the remaining 16 are bare
  basenames used after a full path in the same sentence (`polaris.ts`,
  `main.ts`, `architecture.md`, …), the `decisions/…` shorthand this
  repository's AGENTS.md uses (all three act files verified present under
  `.syzygy/governance/decisions/`), `dist/` and `-RAW.md` as category names,
  and the lane B directory the packet explicitly says is not on this branch
  [Observed]. No unresolvable path.
- Clause quotations checked against the defined locations: PWB-REQ-004 at
  spec lines 491–498, PWB-REQ-007 at 439–468 with its currency scenario at
  470–474, PWB-REQ-014 at 759–773, PWB-REQ-020 at 902–926; RFC2-9 and RFC2-10
  in `RFC-0002/snapshot-and-evaluation-core.md`; VIS-2 and VIS-7 in
  `vision.md`. Every quoted string is verbatim at the cited clause
  [Observed].
- Not re-derivable under this review's constraints, and disclosed as such:
  the L4-F1 re-measurement (15 of 278 sources changed, 9 of 415 machine items,
  9 of 409 rendered rows) needs Butlers tree reads, which this review is
  forbidden [Unknown to this review; the evidence record names its two
  methods and its self-check].

## Findings

### K1 — blocking — `docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md`:563

**Defect.** The J6 repair introduced, inside slice 3, the clause "which
PWB-REQ-020's **one-directional human-to-machine invariant** permits and the
parity sweep omits by name". Forty lines above, at 523–530, the same slice
states the opposite in the packet's own words and with the clause quoted
verbatim: "PWB-REQ-020 does not permit the machine channel to carry more
*facts* than the page: its Observable reads 'both populations contain
equivalent multisets', its Scenario 'the complete human fact multiset equals
the machine fact multiset', and its Falsifier ends 'or associated with a
different evaluation in either channel'". I read the clause: the SHALL
sentence is indeed human→machine, but the Observable, the Scenario and the
Falsifier ("in either channel") are the bidirectional limbs, and those are
the limbs the packet itself quoted to reject this very reading.

This is review 1's blocking F2 — "PWB-REQ-020 paraphrased into its opposite"
— regressed at a new site, and it is unlabeled: a substantive claim about a
digest-bound clause carrying neither `[Observed]` nor `[Inferred]`, contrary
to AGENTS.md §Epistemic discipline and verification rule 8.

It is not merely stylistic. If the equal-multiset limbs govern, the six
machine-only `item:project-account-section:<key>` identities are a candidate
**non-conformance of the existing implementation** — which is exactly how
review 2's G5 repair and review 3's H1 repair left them, "disclosed as a
possible finding against the existing implementation", with slice 3 resting
on the enumerated-population reading alone and labeled Inferred. Line 563
converts that open, disclosed question into settled permission, and then
leans on it as precedent for adding fields to the machine channel. That is an
owner question smoothed into consensus.

**Repair.** Delete "which PWB-REQ-020's one-directional human-to-machine
invariant permits and". Say instead what is observable and what is open: the
parity sweep omits the six by its stated reason
(`polaris-parity-sweep.test.ts`:202–207) [Observed]; whether PWB-REQ-020's
equal-multiset Observable permits a machine-only claim identity at all is the
*same* open reading slice 3 already discloses [Inferred], and if it does not,
the six are a finding against the current implementation rather than a
precedent M2 may rely on. Keep the contingency sentence that already follows
the slice-3 reading.

### K2 — non-blocking — `…FUNNEL.md`:533

**Defect.** "Every horizon *fact* the page renders (the probe claim, its
instant, its counts) **is a project-shape statement** and disclosure and
therefore enters that population in both channels." Slice 2 (lines 449–465)
now argues at length that the probe's count is *not* a project fact — that is
the J1 repair — and that it "enters PWB-REQ-020's parity population as a
'disclosure Polaris presents'". Calling the same claim a "project-shape
statement" is the pre-J1 framing surviving in the next slice, and it is the
over-claim J1 was raised to remove: PWB-REQ-020's enumeration opens "Every
project-shape identity, statement, source anchor…", so "project-shape
statement" names a member of the project-shape family that PWB-REQ-004 closes.

**Repair.** "is a disclosure Polaris presents and therefore enters that
population in both channels" — the ground slice 2 already states, and
sufficient for the argument.

### K3 — non-blocking — `…FUNNEL.md`:590, 599 (and disposition row 1039)

**Defect.** "thirteen guard returns — the pinned-digest mismatch and the
empty-passage list at line 44, and **eleven** structural guards on passages,
figures and chapters at lines 48, 49, 50, 51, 53, 61, 64, 72, 79, 88, 99 and
103". The sentence lists **twelve** line numbers and 1 + 11 ≠ 13. I counted
independently: `grep -c 'return full'` over
`apps/three-surface-poc/src/polaris-reading.ts` returns **13**, at lines 44,
48, 49, 50, 51, 53, 61, 64, 72, 79, 88, 99, 103 — one at line 44 and **twelve**
structural [Observed; denominator: every `return full` in the file]. The
total "thirteen" is right; "eleven" is wrong, twice (line 590 and line 599,
where it defines what `plan-malformed` must cover).

Review 4's own J5 text carried the same miscount (`…-4-RAW.md`:313, 329) and
the packet inherited it — a review can be wrong, and this one was. The
consequence is not cosmetic: an implementer building `plan-malformed` to
cover "the eleven structural guards" leaves one full-declaration return
silent, which is the exact defect slice 6 exists to close.

**Repair.** "twelve structural guards" in both places, and in the J5
disposition row.

### K4 — non-blocking — `…FUNNEL.md`:474 against 752–755

**Defect.** Slice 2's new "probe's own freshness" paragraph asserts that
"`data-epistemic-freshness` is never set on it (S3 already requires that no
freshness value on the page derive from it)". S3, at 752–755, reads "AND no
`data-epistemic-freshness` value anywhere on the page **is derived from it**".
Derivation and presence are different predicates: a probe bracket that
carried `data-epistemic-freshness="fresh"` — a constant, derived from nothing
— would satisfy S3 as written and would be precisely the J2 defect. S3 does
not already require what line 474 says it requires, so the J2 invariant has
no scenario behind it.

**Repair.** Add a conjunct to S3: "AND the probe's own claim carries no
`data-epistemic-freshness` attribute", and drop "already" at 474.

### K5 — non-blocking — `…FUNNEL.md`:896–901 (Gate 6 item 4)

**Defect.** Gate 6 item 4 requires rule-6 mutation evidence "for every new
guard branch" and enumerates four mutant families: `assessCurrency`'s five
arms, the copy oracle's two directions, "the probe's evaluation-identity
separation (make the probe write the pinned evaluation's id and confirm S3
fails)", and the reading-plan announcement. The J2 invariant — the probe
carries no freshness value and its bracket has no freshness slot — is a new,
load-bearing guard with **no mutant named**. The listed probe mutant proves
only the identity half of S3.

**Repair.** Add: set `data-epistemic-freshness` on the probe's bracket and
confirm the S3 conjunct fails. (This mutant needs K4's repair to have
something to fail against.)

### K6 — non-blocking — `…FUNNEL.md`:609–615 against 766–773

**Defect.** S9 names three reasons (`digest-mismatch`, `no-passages`,
`plan-malformed`) and slice 6 adds `plan-malformed` specifically "so that no
full-declaration return stays silent". Slice 6's **Test** paragraph exercises
one: a wrong `statementSha256`, then a corrected one. Neither `no-passages`
nor `plan-malformed` is exercised, and `plan-malformed` is the new value
covering twelve guards (K3). Gate 6 item 4's "every new guard branch" is not
met by the test the slice states.

A second, smaller point for the implementer: `polaris-reading.ts`:44 is a
single `return full` covering *both* the digest mismatch and the empty
passage list, so emitting `digest-mismatch` and `no-passages` as distinct
reasons requires splitting that return. The packet names both conditions at
line 44 but does not say the return must split.

**Repair.** Name a `no-passages` case and at least one `plan-malformed` case
in the test paragraph, and note the line-44 split.

### K7 — non-blocking — `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`:200 (P-69, Q7 clause)

**Defect.** The packet's Q7 now carries, per review 4's J3, the strongest
counter-argument to its own recommendation — RFC2-10's "A condition genuinely
outside the four is disclosed as a fact of the render, never dressed as a
freshness state" — stated against the recommendation in both Q7 and slice 5.
The P-69 row's Q7 clause carries the recommendation, the `[Inferred]` label
and the alternative, but **not the counter-argument**. The register row is the
owner's route into the decision; a recommendation reaching the owner without
the sentence that cuts against it is the same defect class review 3 graded
non-blocking at H3 (the Q3 clause citing the wrong ground) and H4 (the Q5
clause silent on the two lawful arms), both of which were repaired in the row
rather than only in the packet.

**Repair.** One clause: "against which stands RFC2-10's 'never dressed as a
freshness state' — the packet weighs it and still prefers `stale` because
PWB-REQ-007 requires the field on every project-shape tuple".

Every other clause of Q1–Q7 matches between the packet and the row; see the
Q-table below.

### K8 — editorial — `…FUNNEL.md`:657–660

**Defect.** Slice 5: "CAP1-REQ-062 puts an unbounded class under the same
invariant as out-of-bound evidence …, both rendering Unknown with distinct
reasons **and neither assigned a freshness value**". The passive has no agent.
Read as "CAP1-REQ-062 assigns neither", it is true. Read as "neither is
assigned a freshness value", it is false and is contradicted four paragraphs
above in the same slice, which maps "the three `stale` returns → Unknown with
`stale-beyond-currency-bound` **and freshness `stale`**" — verified in the
engine at `packages/cap1-core/src/staleness.ts` lines 121, 133 and 143, each
returning `freshness: 'stale'` [Observed]. Q7's row avoids the ambiguity by
naming CAP1-REQ-062 as the subject of "assigns"; slice 5 does not.

**Repair.** "and CAP1-REQ-062 assigns neither a freshness value".

### K9 — editorial — `…FUNNEL.md`:558–560

**Defect.** "what the machine carries and the page does not is six *claim
identities*" states a gap without naming the population it is over. It is
true of the item family and only of it: 409 distinct `claim:item:*` ids on the
page against 415 machine items, difference six, each of the six a
`project-account-section` key [Observed, re-derived below]. A reader who runs
the obvious sweep gets a different number: of the 439
`projectShape.facts[].fact.fact` keys, **22** do not occur as literal strings
in the served bytes — nine `count:<class>`, seven `catalog-count:<key>` and
the six `item:project-account-section:<key>` [Observed; predicate: literal
substring test of each key against the 1,484,487-byte capture; denominator
439]. The first sixteen are not missing facts: the page carries those under
`claim:class:<class>` and catalog identities rather than under the machine
key string. The sentence is correct but its scope is invisible.

**Repair.** "what the machine's item population carries and the page's item
rows do not is six claim identities".

## J1–J8 verification

| # | Severity in review 4 | Verdict | Evidence |
|---|---|---|---|
| J1 | blocking | **REPAIRED** | The count is restated as an "epistemically labeled claim" (PWB-REQ-014) and "a disclosed fact of the render" (RFC2-10), never a project fact, at 449–465. PWB-REQ-004 is quoted at lines 491–498 of the digest-bound spec in three places (slice 2 at 456–462, the slice-2 act row at 387, Gate 5 at 700–708) and I read those spec lines: the quote is verbatim and 491–498 is the exact span [Observed]. The reasoning holds against the clause — the closed population is four forms (`item:<class>:<declared-key>`, `count:<class>`, `catalog-count:<catalog-key>`, `project-account:<key>`), the probe's count is in none, and the SHALL is about what an extractor admits, which the probe is not. PWB-REQ-014's three roles are verbatim at spec lines 764–765, inside the 760–768 window. The contingency is stated in all three places ("if that reading is rejected the row flips to yes and slice 2 joins Q6"; "Were the owner to read the count as a project fact…"). Gate 0's specification row names PWB-REQ-004 with its role. PWB-REQ-007's SHALL is scoped to "Every project entity and project-fact claim" (spec:443–444), so the packet's parallel claim that PWB-REQ-007 does not reach the probe is sound at the clause. Residual: K2 (slice 3 still calls the same claim a "project-shape statement") |
| J2 | non-blocking | **PARTIAL** | The no-freshness property is stated in slice 2 (467–479), in the rendered bracket sample (486–488, no freshness token), in slice 3's `evidence` block field list (511–513, no freshness field), in slice 5's `currencyBounds` sketch (619–621, "none for slice 2's currency probe, which carries no freshness value") and in success criterion 4 ("not as a freshness value") — consistent everywhere it is asserted. But S3, the scenario the packet points at, forbids only *derivation*, not presence (K4), and Gate 6's mutant list has no mutant for the new invariant (K5). The claim "S3 already requires" it is false as S3 is written |
| J3 | non-blocking | **REPAIRED** (packet) / **PARTIAL** (register) | RFC2-10's "never dressed as a freshness state" is quoted against the recommendation in Q7 and again in slice 5 (663–672), with both reasons the packet still prefers `stale` (PWB-REQ-007's Falsifier "a tuple field is absent/out of vocabulary" — verbatim at spec:466 — and the engine-amendment alternative not escaping the same sentence) and with the alternative and its CC-REV-2 route named. The counter-argument is stated fairly, in the clause's own words, and the recommendation survives it: PWB-REQ-007's SHALL does require freshness on every project-fact claim, so the disclosure route cannot discharge the slot there, which is a real asymmetry against the probe. The owner is given both. The P-69 row omits the counter-argument entirely (K7) |
| J4 | non-blocking | **REPAIRED** | Success criterion 2 (lines 121–126) and S1 (739–745) both read "and, where one exists, the route", both say the oracle enforces the marker and not the route, and criterion 2 names `superseded` as the marker with a reason and no route. Slice 1's three marker texts match: `stale` has a route (slice 5), `broken` and `superseded` do not [Observed] |
| J5 | non-blocking | **PARTIAL** | "thirteen guard returns" is correct — I counted 13 `return full` in `polaris-reading.ts`, at lines 44, 48, 49, 50, 51, 53, 61, 64, 72, 79, 88, 99, 103 [Observed]. `plan-malformed` is added and S9 restated to three reasons, consistent with slice 6's design paragraph. Two defects remain: the structural count is twelve, not eleven (K3), and slice 6's test paragraph exercises only `digest-mismatch` while S9 and Gate 6 item 4 require all three (K6). The renderer citation is right: `polaris.ts`:506–510 shows neither the "selected passages" label nor the "full account" disclosure when `condensed` is false and `chapters` is undefined [Observed] |
| J6 | non-blocking | **PARTIAL** | Re-derived from the retained `api-poc.json`: 439 facts; 13 `projectShape.facts[].fact.fact` keys contain `project-account` — six `item:project-account-section:<key>`, six `project-account:<key>` and one `count:project-account-section` [Observed; denominator 439]. The packet's "twelve keys among 439" is exactly the 6 + 6 pair forms and is correct as written; the thirteenth is disclosed in the evidence record, not in the packet. The page renders six `data-polaris-section="claim:project-account:<key>"`, one per key, and zero `claim:item:project-account-section:<key>` [Observed]; 409 distinct `claim:item:*` ids on the page against 415 machine items, difference six [Observed]. The sweep's quoted comment is verbatim at `polaris-parity-sweep.test.ts`:202–207. What is *not* repaired is the conclusion drawn from it: K1 (the "one-directional … permits" clause, blocking) and K9 (the unstated population) |
| J7 | non-blocking | **REPAIRED** | `export function assessCurrency(` is line 87 and its closing brace is line 155 of `packages/cap1-core/src/staleness.ts`; line 156 is blank and 157 opens the next comment [Observed]. "87–155" is correct in both places (Gate 1 and slice 5), and the review-3 disposition row now records H9 as not a defect. The `no-bound-declared` citation "lines 98–104" covers the return object (98–103) and the closing brace of its guard (104) |
| J8 | editorial | **REPAIRED** | The P-69 row's review-2 clause reads "REVISE — three blocking findings — two register/packet mismatches and a scenario with no slice", which matches G1 (register row kept the withdrawn Q4 warrant), G2 (register row misnamed the no-act slices) and G3 (S9 had no slice) [Observed] |

## Q1–Q7

| # | Scope truthful? | Genuine gate? | Recommendation follows? | Register matches packet? |
|---|---|---|---|---|
| Q1 | Yes. The constant is at `project-shape-model.ts`:162–167 and the comment says "the evaluation itself is the currency: `fresh`" [Observed]. RFC2-9's "Every claim class must declare a currency bound … before any of its claims can leave Unknown" is verbatim at RFC-0002:187, and PWB-REQ-007's `warrants` block lists `RFC2-9, RFC2-10` at spec:480 [Observed] | Yes — a conformance ruling only the owner may make (VIS-4), and the packet says so | Yes. Verification rule 8 does not admit an implementation's reading of a clause as the clause; the recommendation names the current rendering a *disclosed* non-conformance rather than declaring the page unlawful | Yes |
| Q2 | Yes. The registry entry and both named acts exist at the cited paths [Observed] | Yes — an act-shape ruling | Yes. Arm (a) reuses an existing phrase, recorder and `--check`; the cost argument for arm (b) is concrete | Yes |
| Q3 | Yes | Yes — and the packet correctly says one arm is unlawful on its own reasoning and discloses it for confirmation rather than presenting a free choice | Yes, on RFC2-10's evaluation scoping (verbatim at RFC-0002:209), with the render-time-drift argument explicitly kept as a non-ground | Yes, including "VIS-7's identity test is not the ground" (H3's repair) |
| Q4 | Yes. `git-observation.ts`:61 is `rev-parse HEAD` and `main.ts`:80–81 calls it twice [Observed] | Yes | Yes. The absence claim is stated as "no act found", not "no act exists" — the right form under rule 9. The withdrawn unattended-coordination warrant stays withdrawn | Yes (G1's repair holds) |
| Q5 | Yes. `polaris-copy.ts`:46–49 holds the four sentences and the capture renders each exactly once [Observed]. `walkthrough-preflight.ts`:212–219 collects terms from *presented* claims only and tests `"<term> —"`, so extra entries are permitted and a marker appended after the em-dash sentence cannot break it [Observed] | Yes — a copy ruling between two lawful arms | Yes, and both arms are stated lawful (G9's repair holds) | Yes, including "both arms lawful" (H4's repair) |
| Q6 | Yes. P-68 is absent from main's register at `a9f671e` and the lane B directory is absent from this branch, both disclosed and both re-checked [Observed: 0 paths] | Yes — a sequencing ruling | Yes. Slices 1–4 and 6 touch no governed artifact; slice 5 touches the registry, not the spec | Yes — the row names slices 1–4 and 6 and enumerates five workstreams (G2's repair holds) |
| Q7 | Yes. The engine's `no-bound-declared` arm returns `state`, `label`, `reason`, `claimClass` and no `freshness` [Observed: `staleness.ts`:98–103]; PWB-REQ-007 requires freshness; RFC2-10 closes the vocabulary | Yes — RFC2-10 says in terms that no implementation may make this choice, so it is the owner's | Yes, with the counter-argument now weighed (J3) and the alternative named | **Partial — K7.** The row omits the counter-argument the packet was repaired to carry |

## Regression spot-check (F1–F20, G1–G14, H1–H10)

Re-derived, not re-litigated. F1: 1,484,487 − 1,400,000 = 84,487 and
1,478,637 − 1,400,000 = 78,637 over the target; 2,097,152 − 1,484,487 =
612,665 and 2,097,152 − 1,478,637 = 618,515 under the ceiling — all four
arithmetic [Observed]. F8: `project-shape-model.ts`:19–27 already imports
`FRESHNESS_STATES` and `FreshnessState` from `@syzygy/cap1-core`, so slice 5
adds no boundary [Observed]. F14/G4: the six instants and the two earlier
filename dates re-derived at the offsets above [Observed]. F15/J7: five return
paths over three states, confirmed by reading the function [Observed]. F17:
three source files name `assessCurrency`, no `dist/` in this worktree
[Observed]. F18/H2: the `data-polaris-item="` predicate and the 417/8
substring disclosure re-derived [Observed]. H5: success criterion 5 reads
"renders the condensed form and no withdrawal sentence" [Observed]. H7: slice
6 is "medium" in the size paragraph, the topology row and the slice heading
[Observed]. H10: the evidence record's key is
`before_first_evaluation_instant` [Observed]. G8: the `stale` marker's reason
is the constant-assignment reason with slice 5 as its route, so it stops
being true exactly when slice 5 lands [Observed].

**One regression found:** F2 — see K1. The evidence record's own
`project_account_section_items` block does not repeat the "one-directional"
characterization, so the regression is confined to the packet.

Nothing else previously confirmed has moved.

## Other things a fresh reader would want said (no finding)

- The evidence record files
  `apps/three-surface-poc/src/fresh-checkout-demo-main.ts:286` under
  `freshness_value_producers_non_test_poc_sources`. That line reads
  `freshness: shape.claim.epistemic.freshness ?? null` — a pass-through, not a
  value producer [Observed]. The packet's prose ("the only freshness value any
  non-test source … *assigns* is `FRESH`, at lines 185 and 193") is accurate;
  the JSON key is looser than its contents. Not worth an edit.
- `apps/three-surface-poc/src/polaris.ts`:1220 renders
  `classBlock(shape, 'project-account-section', false)`, so the class itself is
  on the page even though its six item rows are not. Consistent with the
  packet's account; noted because it is the fact that makes the six "rendered
  once, as the account's own section" true rather than a story.
- Nine of the 439 machine fact keys are `count:<class>` and seven are
  `catalog-count:<key>`, none of which appear as literal key strings in the
  served bytes (see K9). If a future pass wants a *complete* parity statement
  for slice 3, it needs the machine→page identity map, not a key-substring
  sweep; the existing parity sweep already has that map.

## Counts

Blocking 1 (K1). Non-blocking 6 (K2, K3, K4, K5, K6, K7). Editorial 2 (K8,
K9). Total 9.

Verdict: REVISE
