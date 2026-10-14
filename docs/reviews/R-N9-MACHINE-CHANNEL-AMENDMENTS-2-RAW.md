# R-N9 machine-channel amendments, round 2 (PWB and POC halves)
Reviewed commit: ae8c074066d8e6c511d8064b505e3f89e3f2b43d
PWB manifest SHA-256: e7f304c79959341a9735516e87ccb991c012e695c2a16a90ee18ad2f1928c8f9
POC manifest SHA-256: c16bbb9bebdf82df37a40cbf070910a254ec47b0ca459e538bfe872993b28a50
PWB verdict: CONFIRM WITH EXCEPTIONS
POC verdict: CONFIRM WITH EXCEPTIONS

Reviewer: fresh-context subagent. I did not draft either package or the
round-1 repairs. I read a fresh local clone checked out detached at the
reviewed commit (`git rev-parse HEAD` printed the commit above). I computed
both manifest digests with `git show <commit>:<path> | sha256sum`. I wrote
nothing to the tree. My mutation and apply scripts lived only in the
session scratchpad.

**Round context.** The brief's stopping rule says "One round only … no
second round is dispatched". The dispatcher sent this round anyway, as the
confirmation round both packets recommend under their Q1. [Unknown] Whether
the owner ordered it. Finding 14 covers the prose that this round makes
stale.

## Checks run (clone, reviewed commit)

[Observed] All nine commands in the brief exit 0. Their output:

- `build_pwb_anchor_resolution_amendment.py --check`: "11 proposed subjects (2 patched); 17 requirements, 52 scenarios; structure, regeneration, siblings, composition in every order and the manifest verify".
- `build_pwb_anchor_resolution_amendment.py --selftest`: "25 structure mutants, patch drift, an unclassified sibling, a vanished pending sibling, each declared pending sibling removed (4), a clashing sibling, divergent and failing application orders, and an undeclared or malformed exclusive pair all fail closed on their own predicates".
- `build_three_surface_poc_block_provenance_amendment.py --check`: it prints one `WARN` (identity and governing-intent amendments declared mutually exclusive), then "6 proposed subjects (2 patched); 24 requirements, 24 scenarios; … verify".
- `build_three_surface_poc_block_provenance_amendment.py --selftest`: "19 structure mutants, … each declared pending sibling removed (2), … all fail closed on their own predicates".
- `build_pwb_class_granular_extraction_amendment.py --check`: "11 proposed subjects (5 patched); 17 requirements, 54 scenarios; … verify".
- `build_pwb_release_label_amendment.py --check`: "11 proposed subjects (7 patched); 17 requirements, 55 scenarios; … verify".
- `build_three_surface_poc_identity_amendment.py --check`: "6 proposed subjects (4 patched, 2 unchanged); 26 requirements … verify".
- `check_governance.py`: "32 OK, 21 WARN, 0 FAIL (53 checks)".
- `check_spec_reconciliation.py --check`: "7 of 7 predicates without FAIL; PASS". R6 WARN: the same two stale behaviour-contract pins as round 1 (`syzygy-2g0d`).

Independent checks:

- [Observed] **Patches applied with plain `git apply`.** I applied each
  package's two patches to a scratch copy of its change directory. All 11 PWB
  manifest rows and all 6 POC rows match the resulting bytes, with 0
  mismatches. Only `spec.md` and `GOVERNING-DEPENDENCIES.md` change in each
  package. The text before the first requirement is unchanged, and so are
  the requirement ids and their order (17 PWB, 24 POC).
- [Observed] **Changed blocks.** Only PWB-REQ-014 changes in the PWB spec,
  and only POC-REQ-001 and POC-REQ-010 in the POC spec.
- [Observed] **Lost signed lines.** I found 6 in PWB-REQ-014, 13 in
  POC-REQ-001 and 11 in POC-REQ-010. Each set equals the builder's
  `replaced` tuple, and the counts match the deltas' "six" and "13 … 11"
  (criterion 6 holds).
- [Observed] **Mutants of my own.** I ran them through the engine's
  `structure_findings`, scratch only:
  - Each of these fails on its own pinned phrase:
    - narrowing the Unknown limb ("Unknown or zero");
    - dropping "is rounded up" from the falsifier;
    - widening the POC-REQ-010 exemption ("and any other field");
    - dropping "with it in another shape" from POC-REQ-001.
  - Three pass the structure gate. Finding 12 covers them:
    - a lowercase-`may` authority sentence;
    - a lowercase-`may` snapshot-input sentence in PWB-REQ-014;
    - a lowercase-`may` restatement sentence in POC-REQ-001.
- [Observed] **Evidence-record arithmetic.**
  - 7,952 × 50 + 6,950 × 54 = 772,900, and 772,900 / 5,751,883 = 0.13437
    (13.44%).
  - The 19 unresolved anchors split 11 + 5 + 1 + 1 + 1 by class and scheme,
    and 883 + 19 = 902.
  - `servedIdentities` equals `servedIdentitiesInProjectShapeSources` (285).
  - `secondMethod` is 0 of 19, and `deepDiveLeaves` is 1 of 1.
  - The script at the reviewed commit computes every key the record carries,
    under the predicate strings the record quotes.
  - I could not re-run the measurement, because the captures are not
    retained (`capturesRetained: false`).
- [Observed] **Line citations at `71b4f525`.** `polaris.ts` lines 283 and
  304 hold `git-tree:${cs.revision}` and `beads-dolt:${wi.doltRevision}`, as
  the PWB delta cites. At the reviewed commit those lines are 293 and 314.
  The delta dates its citations to `71b4f525`, so they are correct as cited.
- [Observed] **`doltRevision` file count.** `git grep -l -F doltRevision --
  apps packages` gives 17 files at `71b4f525`, as the POC impact ledger says,
  and 26 at the reviewed commit (finding 11).
- [Observed] **Pending-sibling lists.** Both
  `build_pwb_class_granular_extraction_amendment.py` and
  `build_pwb_release_label_amendment.py` list
  `pwb-anchor-resolution-amendment` as a pending sibling. So does
  `scripts/pwb_requirement_amendment.py`, the engine that drives the
  opening-index and accessible-name packages.
- [Observed] **Sibling patches.** Neither the accessible-name patch nor the
  opening-index patch edits a PWB-REQ-014 line. Each mentions PWB-REQ-014
  once, in an added line inside its own requirement.

**Sibling ordering (dispatcher's note).** I reviewed against `main` as
checked out and did not fetch the repaired P-84, P-85 or P-86 branches. At
this commit, all-orders composition passes for every pending sibling on
`main`:

- PWB: class-granular, release-label, opening-index and accessible-name;
- POC: identity and governing-intent, with the declared exclusive pair
  warned.

What remains for sign-off time:

- re-run both builders' `--check` once the repaired P-85 (release-label) and
  P-86 (class-granular) patches land, because a repaired patch can move lines
  this composition was proved against;
- the same for the repaired P-84 (POC identity) patch against the POC half;
- regenerate with `--write` whichever package is signed later (all of them
  rewrite the one `Source:` line).

## Round-1 findings: repair check

| R1 | Class | Repaired? | Evidence at this commit |
|---|---|---|---|
| 1 | revise | Yes | The text names the field (`identity`) and the whole-value comparison, and excludes references and composed identities. The script's population matches it. The residual is finding 3. |
| 2 | revise | Yes in the spec; one stale copy | The oracle reads "only the machine narrative's anchors and the machine answer's bytes". The impact ledger still describes the old resolver (finding 1). |
| 3 | note | Yes | "The pair is itself presentation: no evidence, snapshot input or status claim SHALL take it as input." The RFC7-3 disambiguation bullet is present. |
| 4 | note | Yes | The Unknown arm is in the obligation, the case, the oracle and the falsifier. |
| 5 | note | Yes | "begins with the identity of the one block it belongs to followed by `#`". |
| 6 | note | Mostly | All six round-1 mutants are now selftest mutants and fail on their own phrases, and `token_counts` was added. The guard is narrower than the disposition says (finding 12). |
| 7 | revise | Yes | "The capture instant stays on the observation beside that record … not a second statement of provenance". "One record in the shape each element of … provenance lists takes". |
| 8 | revise | Yes | "No other field of the observation, its own or an entry's, SHALL hold the revision as its whole value". The oracle sweeps every field and wants exactly one holder of each value, and the falsifier carries "any other field holding the revision". |
| 9 | revise | Yes for the figures; one label slip | `headerRepeats`, `secondMethod` and `deepDiveLeaves` are computed by the script and recorded. One [Observed] sentence goes beyond the record (finding 10). |
| 10 | note | Yes | Database times are excluded from the capture-instant arm. Its residual is finding 8. |
| 11 | note | Yes | "The observation so produced / so served SHALL …". |
| 12 | note | Yes | Both deltas place S6-M3 in a test-only bead. |

## Criteria

1. **The rulings are carried.** Yes for both packages.
   - Every unit stays non-citable, and the pair is offered instead.
   - RFC7-3 is put to the owner as question 2 and left undrafted.
   - The block-to-anchor link is stated as already met (902 of 902).
   - The per-row rule is drafted against POC-REQ-010. POC-REQ-001 belongs
     there: S6-F2 names `codeStructure` as one of the three shapes, and the
     772,900-byte figure counts its rows.
   - The dov.10.1 ordering is named as stale.
2. **One category per change.** Yes. Each package patches one specification
   (I applied the patches independently).
3. **RFC7-3 and RFC7-4 are not crossed.** [Inferred] I found no reading
   under which a unit or the pair becomes authority. Every limb is
   unconditional: a fully resolved block stays non-citable, nothing derived
   from the pair may make a unit citable or stand as a label, and the pair
   may not feed evidence, snapshot input or a status claim. The signed
   "SHALL cite Polaris" bullet is pinned. The one gap is that the structure
   gate cannot see a lowercase-`may` insertion (finding 12). That is a
   tooling residual; the bytes reviewed contain no such sentence.
4. **The predicates are checkable.** Yes, with notes 2, 3, 4 and 8.
   - "Resolves", the pair, the `#` relation and the POC whole-value sweep
     each have an oracle, a denominator and a falsifier limb.
   - The derivability argument for the pair is stated only in part
     (finding 2).
5. **The specification bar.** Each amended requirement keeps one form. The
   new bullets are tied to their requirement's own trigger, so POC-REQ-001
   and POC-REQ-010 stay `event-response`. Scenarios carry the text. The
   remaining oracle and falsifier asymmetries are notes 8 and 9.
6. **Signed bytes.** Verified independently (see Checks).
7. **Honest claims.**
   - The headline figures reproduce from the record.
   - [Unknown] is used where nothing was measured: the predicate behind the
     pursuit's 934, and the pair's carrier object.
   - No adoption is claimed and no build is authorized.
   - The packages' sibling and adoption lists predate siblings that landed
     later (findings 6, 7 and 11).
8. **Mechanics.**
   - Every `--check` and `--selftest` passes.
   - I sampled the selftest mutants, and the selftest asserts that each one
     fails on its own named phrase. I did not re-run each built-in mutant
     separately.
   - The sibling builders' `--check` passes.
9. **Plain language.** Both packages restate cleanly. Finding 5 is the one
   reader-facing ambiguity.

## Findings

**Finding 1 — the impact ledger still describes the resolver round 1 found unrunnable** (note) [PWB]

`IMPACT-LEDGER.md`, "Files a later implementation would touch", says: "an
independent resolver that imports no rendering code, reads only the machine
answer's bytes and reproduces every pair". That is the round-1 finding 2
defect, which the repaired oracle no longer has. The amended oracle reads
"the machine narrative's anchors and the machine answer's bytes". The
normative text is right, but the implementation guidance contradicts it.
Fix: copy the oracle's wording into the ledger bullet.

**Finding 2 — the pair's PWB-REQ-020 derivability is asserted, not argued** (note) [PWB]

PWB-REQ-020 says: "Every value such a view serves SHALL be independently
verified as derivable from the machine answer's own bytes at that
evaluation". The delta's argument is: "The resolver reads the narrative's
anchors and the machine answer … That keeps the pair inside PWB-REQ-020's
rule". But that resolver's input is the view plus the answer, not the
answer alone.

[Inferred] The argument that holds is transitive. Each anchor is itself a
served view value that PWB-REQ-020 already requires to be derivable, so a
count over derivable anchors and the answer is derivable. The delta should
say so in one sentence. It should also say that no PWB-REQ-020 derivability
checker exists for the narrative today: a search for `derivab` under `apps/`
and `packages/` finds only `test-artifact-verification.ts` and the Polaris
generation source. The chain rests on that unbuilt check.

**Finding 3 — "an `identity` field of its own" still leaves a semantic call** (note) [PWB]

The text selects a field by its key (`identity`), then excludes "a field that
refers to another record's identity". A future object whose key is
`identity` but whose value is a reference would need a judgment call, which
CC-SPEC-4 asks oracles to avoid. Today the call never arises: 285 of 285
`identity` keys are `projectShape.sources[]`. The script, by contrast,
counts every string `identity` key. Fix: state the rule structurally, for
example "a field named `identity` is a record's own identity; no other key
is". Then the reference exclusion becomes an example rather than a second
test.

**Finding 4 — the withholding limb does not say whether the narrative is re-rendered** (note) [PWB]

The case says "withhold one resolved target's identity from the machine
answer and resolve again". The oracle adds that the affected blocks' counts
fall "and every such block stays non-citable". If only the independent
resolver re-runs over mutated bytes, the served blocks never change, and the
limb tests the resolver rather than the builder. If the builder re-renders
from the mutated model, the limb tests the served pair, which is the point.
Either can be implemented, and they test different things. Fix: say "serve
the narrative again from a machine answer with that identity withheld".

**Finding 5 — "does not resolve" collides with POC-REQ-031's "resolves"** (note) [PWB]

Signed POC-REQ-031 requires every positive Polaris claim to "cite provenance
that resolves to an identified observation or governed artifact", with
"zero dangling citations". Its test counts `region:work-items` and
`region:code-structure` as resolved (`polaris.test.ts`, lines 40–54).

Under the PWB amendment, the work-items and code-structure region anchors,
and the 17 provenance-record anchors, "do not resolve". Their targets are
served, but not as a record with its own `identity`. A reader who sees
"883 of 902" can take the 19 for dangling citations, which the signed POC
specification says there are none of. Neither package mentions POC-REQ-031.

Fix: add one sentence, in the delta or the scenario, saying that a
non-resolving anchor is not a dangling citation. It points at something the
answer serves that has no identity of its own.

**Finding 6 — the PWB package names two pending siblings; its builder declares four** (note) [PWB]

`build_pwb_anchor_resolution_amendment.py` declares four pending siblings:
`pwb-accessible-name-amendment`, `pwb-class-granular-extraction-amendment`,
`pwb-opening-index-amendment` and `pwb-release-label-amendment`. The first
and third were added by `df3f996b`, after round 1. The package text has not
caught up:

- `SEMANTIC-DELTA.md` ("All three spec patches compose in either order"),
  `IMPACT-LEDGER.md` ("Packages and fields this collides with") and the
  owner packet ("Order against the pending PWB packages") name only
  class-granular and release-label;
- the builder's own comment ("Neither touches PWB-REQ-014") counts two;
- `IMPACT-LEDGER.md`, "At adoption", item 5 names only the class-granular
  and release-label builders' sibling lists. `scripts/pwb_requirement_amendment.py`,
  the engine for the opening-index and accessible-name packages, also lists
  this package as pending. The sign-off change must move it there too, or
  those builders will try to apply an already-applied patch.

The mechanical claim holds: the composition check passes in every order
over all four. Fix: name all four, and add the engine to item 5.

**Finding 7 — the POC package omits its second pending sibling and the exclusive pair** (note) [POC]

The POC builder declares two pending siblings:
`three-surface-poc-identity-amendment` and
`three-surface-poc-governing-intent-amendment` (P-100). It also declares the
two mutually exclusive with each other (`81dd2e87`, `19241aac`), and
`--check` prints that WARN on every run.

`SEMANTIC-DELTA.md` ("Order against the identity amendment"),
`IMPACT-LEDGER.md` ("Packages and fields this collides with") and the owner
packet ("Order against the POC identity amendment (P-84)") name only the
identity amendment. Composition with each passes, so nothing is broken.
But the owner is not told that a third POC package rewrites the same
`Source:` line, or that the two siblings exclude each other. Fix: name
P-100 and the declared pair.

**Finding 8 — the POC-REQ-010 time exemption is open in the obligation and closed in the oracle** (note) [POC]

- The obligation exempts "a time the database itself records for that item",
  an open class.
- The falsifier exempts "a time the database records for that item", also
  open.
- The oracle exempts only "each item's created, updated and closed times",
  a closed list of three.

Suppose a later item field carries another database time (a due or defer
time) that equals the capture instant. The obligation allows it and the
oracle fails it. [Inferred] That is unlikely today: `WorkItemFact` has only
the three. Fix: make all three limbs say the same thing, either by naming
the three fields everywhere or by stating the open class in the oracle.

**Finding 9 — the POC falsifiers do not mirror the capture-instant limb of the oracle** (note) [POC]

Both oracles require that "exactly one holds the capture instant, the
observation's own". Neither falsifier lists either of these:

- an observation with no capture instant;
- an observation whose own fields hold the capture instant twice, say a
  second header timestamp.

Each falsifier lists only an entry or item carrying it. The oracle catches
both cases, so this is a CC-SPEC symmetry gap, not a hole. Fix: add "or an
observation whose own fields hold the capture instant other than once".

**Finding 10 — one [Observed] sentence goes beyond the evidence record** (note) [POC]

The delta says: "The 416th declaration shows why a declaration carries its
own value: its fact is Unknown and states none, while the declaration still
records what it declared". The owner packet's Q3 labels the same claim
"[Observed, the evidence record's `headerRepeats`]".

`headerRepeats` counts a `value` row only where the holding fact has a
scalar `value`, so the 416th declaration is outside its population. The
record shows 415 of 415. It does not show that the 416th declaration carries
a value. [Inferred] The `Declaration` type and the coverage code
(`project-shape-coverage.ts` line 426: `value: d.value`) make the claim
likely. Relabel it [Inferred], or add the case to the script and the record
(round-1 finding 9's rule).

**Finding 11 — the POC ledger's list of header readers predates two new readers** (note) [POC]

The ledger's 17 files at `71b4f525` is exact. At the reviewed commit,
`doltRevision` appears in 26 files under `apps/` and `packages/`. Two of the
new files are non-test readers of the header:

- `packages/three-surface-poc-core/src/reevaluation.ts` line 35 reads
  `model.workItems.doltRevision`;
- `apps/three-surface-poc/src/reevaluation-copy.ts` renders the result.

Neither is in "Header readers, which move to the record". This does not
affect the spec: the reevaluation clocks sit outside the observation, so the
sweep does not reach them. But an implementation slice built from the
ledger would miss these two readers. Fix: re-derive the list at the
sign-off commit.

**Finding 12 — the token guard misses lowercase permissive sentences** (note) [both]

The round-1 disposition says `token_counts` means "an inserted permissive
sentence fails even when every required phrase survives". [Observed] That
holds only when the sentence contains `citable` or uppercase `MAY`. These
inserted lines pass the structure gate with 0 spec findings:

- "A block at its full count may stand as the authority for its claims." (PWB-REQ-014)
- "A status claim may take the narrative's pair as a snapshot input." (PWB-REQ-014)
- "An entry may also restate the revision under another key." (POC-REQ-001)

Changing the scenario's "2 of 3" to "2 of 3 or 3 of 3" also passes, because
the pinned phrase is a substring. The disposition does disclose the general
residual ("a weakening that adds no counted token … still passes"), and the
review stays the gate. Suggested fixes:

- count `\bmay\b` case-insensitively;
- count `authority` and `snapshot input` per block;
- pin the scenario's THEN line whole.

**Finding 13 — the evidence record does not name the script revision that produced it** (note) [both]

`measuredOn.syzygyCommit` is `71b4f525`. At that commit the measurement
script does not exist: its only commit is `eb688df1`, after the round-1
extension. The `scriptCommitNote` says the script "was extended after review
round 1" but names no commit or digest. Today the script is unchanged since
`eb688df1`, so a reader can find it. A later edit would leave the record
naming no runnable revision (rule 11; the AGENTS.md rule-6 evidence lesson).
Fix: record the script's commit or sha256 in the record.

**Finding 14 — the status prose will be stale once this round is retained** (note) [both]

The following say "no round 2 was dispatched" and "the repaired bytes are
unreviewed":

- both `SEMANTIC-DELTA.md` Review sections;
- both owner packets' Status lines;
- `ROUND-1-DISPOSITIONS.md`;
- register rows P-96 and P-97.

This raw is that round 2. It also contradicts the brief's own stopping rule
("One round only … no second round is dispatched"). Whoever retains this raw
should:

- mark those sentences dated, where they stand (the CG-27 lesson);
- record who ordered the round;
- not rewrite the round-1 text.

Under the brief's head contract, a notes-only verdict clears the bytes it
read: the two manifests above, at the reviewed commit. Any repair of
findings 1–13 retires that clearance (rule 10), unless the repair goes in a
sibling record, as the owner's 2026-09-26 stopping-rule ruling provides.

## Counts

- PWB: 0 blocking, 0 revise. Notes: 1, 2, 3, 4, 5, 6, 12, 13 and 14 (9 notes).
- POC: 0 blocking, 0 revise. Notes: 7, 8, 9, 10, 11, 12, 13 and 14 (8 notes).
- Findings 12, 13 and 14 apply to both packages, so they are counted under
  each.
