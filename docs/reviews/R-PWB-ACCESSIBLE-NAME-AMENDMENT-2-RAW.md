# R-PWB-ACCESSIBLE-NAME-AMENDMENT-2 — fresh-context review, PWB accessible-name amendment (PWB-REQ-016), round 2
Reviewed commit: ae8c074066d8e6c511d8064b505e3f89e3f2b43d
Manifest SHA-256: 0509c31999aa65cee90bc2814120693f907fd530329837c0d6d8638641788d51
Verdict: REVISE

Package: `.syzygy/governance/contracts/candidates/pwb-accessible-name-amendment/`
(manifest `PWB-ACCESSIBLE-NAME-AMENDMENT-MANIFEST.txt`). The head digest
above is the sha256 of that file's bytes at the reviewed commit, computed
with `git show ae8c0740…:<path> | sha256sum` and matched by a second Python
hash over the clone's working file. Brief:
`pwb-opening-index-amendment/REVIEW-BRIEF.md`. This round covers both
packages, as round 1 did. This raw judges package C only. Round 1:
`docs/reviews/R-PWB-ACCESSIBLE-NAME-AMENDMENT-1-RAW.md` (`REVISE`, at
`0241fb83`). Repairs: `ROUND-1-DISPOSITIONS.md`.

## Mechanics run (fresh clone at the reviewed commit)

[Observed] Run from the root of a `git clone` checked out detached at
`ae8c0740`. I read the output and the exit code of each:

- `build_pwb_accessible_name_amendment.py --check`: exit 0. "11 proposed
  subjects (2 patched); 17 requirements, 53 scenarios; … pending-sibling
  composition (pairwise, and one result in every order) verify".
- `build_pwb_accessible_name_amendment.py --selftest`: exit 0. "20 structure
  mutants …". That is 5 shared engine mutants plus 15 declared in the
  builder, each matched against its own expected prefix.
- `build_pwb_opening_index_amendment.py --check` and `--selftest`: exit 0.
- `build_pwb_class_granular_extraction_amendment.py --check` and
  `build_pwb_release_label_amendment.py --check`: exit 0.
- `check_governance.py`: "32 OK, 21 WARN, 0 FAIL (53 checks)".
  `check_spec_reconciliation.py --check`: "7 of 7 predicates without FAIL;
  PASS". The R6 WARN was there before this package.
- Independent byte check, my own script. I applied both patches to a copy.
  All 11 manifest rows hash to the proposed bytes. Only `spec.md` and
  `GOVERNING-DEPENDENCIES.md` differ, and the only changed requirement block
  is PWB-REQ-016. A line diff shows exactly 3 signed lines changed. They are
  the builder's 3 `replaced` lines, and each survives as the prefix of its
  extended line. The warrants are unchanged. The Three-Surface POC
  specification is untouched (`git diff c371339d ae8c0740` over it is
  empty).
- Composition: all 120 orders of the five pending spec patches on main
  apply, and all give 1 result (my own `git apply` script).
- Census: re-derived with the ledger's own regex over the 2,006 paths at
  `c371339d`. 92 files cite PWB-REQ-016, and every area count reproduces
  (27/22/28/5/1/2/7).
- Today's checker: `polaris-accessibility.ts` is unchanged since
  `c371339d`. Lines 523-540 check non-empty names on the roles in
  `NAMED_ROLES` (line 356: link, heading, region, navigation) and compare
  link counts. A fixed-string search for `level` finds 0 lines. The delta's
  claims hold.
- Citations: RFC-0007 lines 241 and 249-251 say what the delta quotes, and
  `CAPABILITY-COVERAGE.md` row 19 is as cited. No capture figure is quoted.
- Rule-6 probes over the proposed bytes through `spec_findings`:
  - Truncating the replaced Falsifier line raises "replaced line lost its
    signed text". Round 1's engine gap is closed.
  - Two edits return **no finding**: rewriting "the words added to it name
    the item or source by the identity PWB-REQ-014 renders for it" as
    "are free text", and inverting the heading exclusions to "including
    those hidden".

Round-1 repairs, checked one by one:

- **1 (page population).** Repaired in the text. The scope is "every
  Polaris page served at one whole-project evaluation". A page count is
  reported, and the Oracle and Falsifier carry it. Note 2 remains.
- **2 (targets).** Repaired for buttons and form controls, and for the
  heading population. The interactive population is still open: note 3.
- **3 (label-in-name).** Addressed by a new sentence, but that sentence is
  finding 1.
- **4 (register rows).** P-98 and P-99 exist.
- **5 (pair-checking).** Repaired. The 120-order claim reproduces.
- **6 (engine).** Repaired, and the check fires.
- **7 (collision with A).** Addressed in A.

Criterion 2 (scope) holds. Slice D is put to the owner with the
one-category reasoning (packet question 4).

## Findings

**Finding 1 — The label-in-name and identity rule added in repair is a new obligation with no oracle limb, no falsifier limb and no scenario that carries it** (revise)

Anchor: `proposed/spec.md.patch:13-16`: "The accessible name SHALL begin
with the visible label, and the words added to it name the item or source
by the identity PWB-REQ-014 renders for it." This was added for round-1
note 3. Criterion 3 says "Each new obligation has an oracle limb, a
falsifier limb and a scenario." The gaps:

- The Oracle (`:55-59`) groups elements by computed name and compares
  targets. It never compares a name with its visible label, or the added
  words with a PWB-REQ-014 identity.
- The Falsifier (`:64-68`) names only shared names across different
  targets.
- The scenario "Repeated source links are told apart by name" (`:77-81`)
  asks only that each name "names the source it routes to" and that names
  are distinct.

An implementation whose names are distinct but do not begin with the
visible label meets every verification limb and still breaks the SHALL.
Speech-input users, the delta's own reason (`SEMANTIC-DELTA.md:118-119`),
are then unprotected. [Observed] The identity half is also unpinned: my
probe rewrote it as "are free text" and the builder raised no finding.

The scope of "The accessible name" is also unclear. The sentence sits under
the repeated-label bullet, but it does not say whether it covers every
interactive element or only repeated labels. This matters where it meets
package A's rows, which A says have names that "name [their] question".

Repair: add oracle, falsifier and scenario limbs for the label prefix and
the identity source, scope the sentence explicitly, and pin it.

**Finding 2 — "Every Polaris page served" has no stated enumeration, so the page denominator is only as independent as whoever lists the pages** (note)

Anchor: `:28-33` and the Oracle (`:57-58`), "each check's page count must
equal the pages Polaris serves at that evaluation". "Including the entry
page and each exact-source route response" is an open list. Nothing says
how the pages Polaris serves are enumerated, or from what. Possible sources
are the route table, the model's admitted source identities times the
PWB-REQ-011 render modes, or a crawl from the entry page. Without that, an
oracle that takes its page list from the renderer shares the
implementation's view (CC-SPEC-4's independence limb). Packet question 6
calls the population "the entry page and each exact-source page". That is a
closed reading, and the text does not close it. Naming the enumeration
source, outside the renderer, would close the round-1 finding fully.

**Finding 3 — The interactive population is not defined the way the heading population now is** (note)

Anchor: `:6-9`, `:31-32` ("the complete interactive and heading
population") and the Oracle's "the population the browser enumerates". The
repair defines the heading population: after load, including headings
inside a closed `details`, excluding hidden ones. It defines no interactive
population. A DOM enumeration includes links inside a closed `details` and
under `hidden`. The accessibility tree omits both, and that is the tree
today's checker reads (`polaris-accessibility.ts:525-526`, `page.axTree()`
filtered to non-ignored nodes). So two good-faith checkers would report
different denominators and different shared-name groups. One sentence
mirroring the heading rule would settle it.

**Finding 4 — The verbatim-heading exemption covers no heading today, and its stated reason does not match how Polaris renders Butlers headings** (note)

Anchor: `:25-27`: "Headings inside a verbatim Butlers body rendered under
PWB-REQ-011 are counted and reported but are outside the level-1 and order
rules: Polaris renders them as written". Also `SEMANTIC-DELTA.md:114-117`.
What the code does [Observed at `ae8c0740`]:

- The PWB-REQ-011 exact-source route renders each verbatim body as escaped
  text in a `<pre>` (`apps/three-surface-poc/src/polaris-source.ts:121-124`).
  That puts no heading element on the page, so the exemption is empty
  there.
- Butlers-declared Markdown on the entry page is rendered by
  `polaris-markdown.ts`, called from `polaris.ts:625-647`, with real heading
  elements. Their levels are re-based to an anchor level
  (`polaris-markdown.ts:177-180`): `anchorHeadingLevel + 1 + depth −
  shallowest`, capped at 6. So Polaris already chooses those levels and does
  not render them "as written".

Those are the headings that can skip, and they are not "rendered under
PWB-REQ-011". [Inferred] So they fall under the heading rule. That is
workable, because the re-basing can close gaps without touching text. But
the package does not say so, and the delta's reason for the exemption
("cannot be repaired by Polaris without breaking verbatim rendering") does
not hold for them.

The exemption also leaves open:

- how a checker recognizes "a verbatim body";
- whether an exempt heading still counts as "the heading before" the next
  Polaris heading.

The new scenario's AND (`:89-90`, "a skipped heading level, a second
level-1 heading … fails the check") carries no verbatim exception, unlike
the Falsifier (`:66`).

**Finding 5 — Several sentences went stale in the repair** (note)

- `IMPACT-LEDGER.md:41-42` plans a fixture that runs "over a page rendered
  from a whole-project evaluation". The repaired scope is every page.
- The builder docstring (`scripts/build_pwb_accessible_name_amendment.py:6-8`)
  says the same: "the complete population of a page rendered from a
  whole-project evaluation".
- Register row P-99 (`PENDING-OWNER-DECISIONS.md:1157`) says "both checks
  run over a whole-project page".
- `SEMANTIC-DELTA.md:176-179`, `OWNER-DECISION-PACKET.md:9-14` and P-99 say
  "no round 2 was dispatched". This raw makes that false. The next edit
  should mark it, dated, at the sentence.

**Finding 6 — Pinning: the heading-population exclusions and the added-word identity are unpinned; the engine's prefix check accepts any line** (note, applies to both packages)

[Observed] The required phrase for the heading population ends at
"including those inside a closed `details`". Inverting the exclusions that
follow ("excluding those hidden by …" became "including those hidden by …")
raised no finding. Neither did the identity edit in finding 1. In the
shared engine, the replaced-line check accepts the signed stem as the start
of any line in the block, not only the one in the replaced line's position.
All three of this package's replaced lines pass on their own lines, so the
current bytes hold. A later `--write` would not be protected.

**Finding 7 — Sibling order was checked against main only; the repaired P-85 and P-86 remain for sign-off time** (note, applies to both packages)

As the dispatcher directed, I did not fetch the branches that hold the
repaired release-label (P-85) and class-granular (P-86) packages. On main:

- both of those builders' `--check` pass;
- their `PENDING_SIBLINGS` lists include this package;
- all 120 orders of the five spec patches give one result.

What remains is to compose the repaired P-85 and P-86 patches with this
one. This builder's `--check` does that live when they land, and the
packet's "whichever is signed second is regenerated … and reviewed again"
covers the manifest.
