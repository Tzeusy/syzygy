> # Record beside the package — not authority, binds nothing
>
> Dispositions the findings of the first fresh-context review of the
> regenerated item-depth package. It is not a package artifact: the manifest
> does not hash it and no builder reads it. It offers nothing and performs no
> act (VIS-4).

# Round 1 dispositions — item-depth package

- **Reviewed commit:** `c1612d31a85a22ef0c65a430df74cef210a6d37e`.
- **Verdict (raw line 4):** `REVISE`; eight findings: one blocking (1), four
  revise (2-5) and three notes (6-8), counted from the raw's finding headings.
- **Effect:** the package bytes the review read are retired by the repair
  below (rule 10). A fresh review of the repaired bytes is required before any
  sign-off is offered.

Reviewed record: docs/reviews/R-PWB-ITEM-DEPTH-AMENDMENT-REVIEW-4-RAW.md

## Dispositions

### 1 — a sixth subject, `CONTRACT-COVERAGE.md`, is missing (blocking)

Repaired. The repair-delta patch uses the generator's comma-only list for the
three rows citing PWB-REQ-013 and PWB-REQ-015. A sixth patch carries
`CONTRACT-COVERAGE.md`, produced by the repository's own generator over the
proposed repair rows, and the manifest, ledger, delta, packet and brief count
six moving subjects and five unchanged rows. The builder's `--check` now runs
the generator's `--check` over the proposed bytes in a scratch tree, and its
selftest holds mutation-checked predicates for a stale summary, a semicolon
separator, a row citing a missing requirement, the generated-equals-proposed
comparison and a landing without the sixth subject.

### 2 — the relation claim has no admitted source (revise)

Repaired by stating the absence. PWB-REQ-002's classes and PWB-REQ-004's
closed population admit no governing-relation declaration, so the amended text
mints none and defines a captured relation as an admitted-extractor
declaration; until a separate owner-scoped change admits a source, every
relation claim is the absent arm. The text names the claim's class
(`governing-intent-relation`) and leaves its currency treatment to
PWB-REQ-007. PWB-REQ-002, PWB-REQ-003 and PWB-REQ-004 are listed as reached
and unchanged. Widening PWB-REQ-002 and PWB-REQ-004 inside this delta is the
other lawful arm and is an owner choice (open point 1).

### 3 — the plural-relation arm is not total (revise)

Repaired. Exclusion is defined by an admitted declaration that names two
relations mutually exclusive for the same item; class, label, basename,
similarity, generated prose and a PWB-REQ-004 precedence outcome never create
or resolve one. Each population has exactly one result: none is
`missing-declaration`; one or more with no exclusion is one Observed set; any
exclusion makes the whole population `contradicted-pending-adjudication`,
however many compatible relations it holds. The sweep, oracle, mutation proof
and falsifier carry the mixed and precedence cases, and the builder selftest
mutates each rule. The Observed-set versus all-contradiction choice remains
open point 2.

### 4 — capability-to-item matching is undefined (revise)

Repaired. A capability matches an item only by exact equality of their
declared keys. A match of exactly one item makes that item's detail the deep
dive; no match or several gives no detail, no proposal rendering and an
Unknown disclosure (`missing-declaration`, `contradicted-pending-adjudication`).
The matching declaration and the loss of a deep dive for an unmatched
capability are open point 3, including the unestablished assumption that the
capability artifact declares a comparable key.

### 5 — "renders verbatim" against "verbatim-reachable", and the gate point (revise)

Repaired. Reachability through PWB-REQ-011's exact-source route is the only
obligation: that route is the only place the text is encoded and the band
embeds no body. An excluded, missing, unreadable or gate-failed related source
leaves only that text Unknown with its own reason and route and never changes
the relation claim. The former gate-failure open point is replaced by open
point 4, which names every non-served outcome and the other arm.

### 6 — PWB-REQ-010 and PWB-REQ-011 speak only of capability depth (note)

Repaired as a disclosure. The delta's "does NOT change" list says both
requirements still name capability detail, that item detail is read as one of
their available depths, and that a later wording amendment may align them.

### 7 — the ledger's overlap sentence is false for one applied sibling (note)

Repaired. Re-derived over the 23 `.patch` files of the six applied packages,
counting changed non-header lines containing `PWB-REQ-015`: 0 in a
`spec.md.patch`, 2 in the dismissal-expiry package's generated dependency
patch. The ledger states that population and those figures.

### 8 — comprehension restated, no defect (note)

No change. The reader-restatement stands; its two gaps (findings 2 and 3) are
repaired above and the brief now asks the reviewer to judge each.
