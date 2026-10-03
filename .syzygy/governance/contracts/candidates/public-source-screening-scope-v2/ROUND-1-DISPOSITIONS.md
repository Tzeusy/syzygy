# Round 1 dispositions — public-source screening scope, version 2

> **Candidate — binds nothing.** Record for
> `reviews/R-PUBLIC-SOURCE-SCREENING-SCOPE-V2-1-RAW.md` (verdict REVISE;
> findings 1 to 4 blocking, 5 to 8 notes), written 2026-10-04. The raw is
> retained verbatim. Every repair below changes bound bytes (the patch and the
> manifest), so the round-1 review is retired and a round-2 review is needed.
> No digest is copied here.

## Machine-readable binding

Reviewed record: .syzygy/governance/contracts/candidates/public-source-screening-scope-v2/reviews/R-PUBLIC-SOURCE-SCREENING-SCOPE-V2-1-RAW.md
Revise-severity findings: 4

## Dispositions

### 1 — The policy bytes contradicted themselves and the packet's withheld list was false (blocking)

Repaired. The root names security, design, governance and code of conduct are
removed from the rule; `notMapped` and `indeterminate` now say what the rule
does. The packet's sendable and withheld lists are generated from the rule's
constants into a marked block, and `--check` fails when they differ (selftest:
a hand edit and a missing block are both caught). Each example in the packet is
a fixture the reference reader checks.

### 2 — Governance text mapped by name and directory (blocking)

Repaired by the lead's decisions. Default rule: DESIGN, GOVERNANCE, SECURITY and
CODE_OF_CONDUCT (both spellings) are withheld; ARCHITECTURE and MANIFESTO are two
owner opt-ins, off by default (packet Q2 and Q3, with the cost of declining
stated). The docs tree excludes any path with a directory segment adr, adrs,
decisions, rfc, rfcs, spec, specs, specification, design or governance, and
`.txt` files named cmakelists.txt or robots.txt or starting requirements. The
reviewer's list also named policy and security directories; policy, policies and
security are added to the excluded segments for consistency with dropping the
root SECURITY name (a deviation from the lead's list, reported to the lead). Q3
is split into Q2 to Q4 with a default each.

### 3 — The prefix admitted non-ASCII digits (blocking)

Repaired. `rootStemNumericPrefix` is data: exactly two characters from the ASCII
digits 0-9 and a hyphen, optional; the reference reader compares code points
against that set and uses no Unicode-aware class. Fixtures with Arabic-Indic
digits are False. A mutant that uses `str.isdigit` is caught. The delta carries
a note for a TypeScript consumer.

### 4 — `--ready` read a path that does not exist (blocking)

Repaired: it reads the installed RFC-0005 module under the governance contracts
directory. The selftest has `readiness()` met, class missing, act missing and
file absent, and asserts the real path exists. The candidates mirror is not
consulted: a prerequisite is the in-force text.

### 5 — The Unicode fixtures were inert (note)

Repaired. The old fixtures are replaced by long s in a root name (caught by
casefold), long s in a docs directory name (caught by casefold the other way),
the Kelvin sign inside a denylisted file name (caught by `str.lower` and
casefold), and the Arabic-Indic digits. Each swap mutant is run. The brief no
longer claims the dotted-capital-I and Kelvin names.

### 6 — The design attribution was not anchored to the clause (note)

Repaired: the delta and packet now say withholding design is this policy's
choice, and that the amendment names doctrine, spec, decision and policy text.

### 7 — Supersession and the post-act state were unspecified (note)

Repaired in the delta (supersession section) and covered in the builder: after
the act the disk hash equals this manifest's row, reversing the patch gives the
version-1 row, and `--check` stays current (selftest, with a refusal when the
disk is neither row). The recorder, its phrase and record name are still
written after the review.

### 8 — Q2 was not a decision; a selftest label mismatched (note)

Repaired: the order is stated as fact in the packet, and the label now reads "a
second licences tree root".
