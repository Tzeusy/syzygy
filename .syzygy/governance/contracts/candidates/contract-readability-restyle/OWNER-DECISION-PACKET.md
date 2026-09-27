# Contract readability restyle — owner decision packet

> **Status:** Proposal. It binds nothing until the owner performs the act
> below (VIS-4). Until then the accepted RFC bytes stay exactly as the
> general trusted-bootstrap transaction bound them.

The package restyles 29 of the 30 accepted modules of RFC 0001–0009 for
readability, to CC-REV-8. No clause changes meaning. The owner adopts it by
saying so, which the recorder captures as:

```text
ADOPT CONTRACT READABILITY RESTYLE: 6e83675fd61bf72a1912152dbc3c6dda64303e892eeadcf1273ce6aebe6ab134
```

The argument is the sha256 of
[`CONTRACT-AMENDMENT-MANIFEST.txt`](CONTRACT-AMENDMENT-MANIFEST.txt).

## What the package holds

- **29 patches** under `proposed/`, one per module, and the manifest of the
  bytes they produce.
- **The excluded module:** `rfcs/RFC-0007/rendering-and-surface.md` stays
  byte-identical, because the pending scoped-attributes package patches its
  exact bytes.
- **Nothing is applied yet.** CG-7h keeps both mirrors on the bootstrap bytes
  until the act is recorded; the recorder then writes the act records, and
  `build_contract_readability_restyle.py --apply --at-adoption` installs the
  bytes in the same change.

```mermaid
flowchart LR
  P["Package: 29 patches + manifest"] -->|"owner says the phrase"| R["Recorder: dedicated record + aggregate section"]
  R -->|"record first, then"| A["Builder --apply --at-adoption: both mirrors"]
  A --> C["CG-7h folds the restyle link into the expected bytes"]
```

## What changes, and what cannot

- **Changes:**
  - each module's §0 reader map and each package README open with their
    answer, and give the map as a tree;
  - long clause paragraphs become a lead sentence plus bullets reusing the
    clause's own words; inline enumerations become lists;
  - diagrams where a clause describes a flow, lifecycle, boundary or
    placement, each captioned "non-normative; the clauses govern".
- **Frozen, checked by script and by the builder:** YAML front matter; the
  Status, Package and Serves paragraphs; every clause lead; every heading;
  every item number and letter in order; every History/Amended
  parenthetical; every link and code span; every epistemic label's span.
- **Three code spans change whitespace only.** Each was broken across a
  line in the original and is now joined on one line, rendering identically:
  RFC2-18's chain span, RFC7-11(a)'s drift marker, and a span in RFC 0003's
  "The predicate". Adoption accepts these three byte changes.

## Review

Every review is a fresh-reader review, stored raw under `docs/reviews/`
as `R-TREE-STYLE-CONTRACT-*-RAW.md`.

- **Round 1, five groups, all `REVISE`.** The recurring defect: splitting a
  paragraph into a list narrowed the text a trailing `[Inferred]` or
  `[Observed]` label covered. Other findings: diagrams that made a necessary
  condition look sufficient, and a few new words inside normative clauses.
  Every paragraph whose label narrowed was restored to its original bytes.
- **Round 2, five groups, all `CONFIRM WITH EXCEPTIONS`,** notes only. Under
  the owner's notes-only stopping rule this clears the bytes.
- **Binding review:** confirms the patches reproduce exactly the bytes round
  2 reviewed, and carries this manifest digest in its head; the recorder is
  pinned to it.

## Found while restyling, not changed

These would change meaning or citations, so they are left for the owner.

- **Wrong or loose citations:**
  - RFC2-5 cites "RFC2-17…20" for the reconciliation chain; the chain clause
    is RFC2-18.
  - RFC4-11 cites RFC4-28 for the closed cause list; it is RFC4-24.
  - RFC8-8's "§8 q4" means module 3's §8, not module 1's.
  - RFC 0009 §7 case 3 cites RFC9-11/16; the prohibition is in RFC9-17.
- **Counts and ranges:**
  - RFC 0001 §1 gives "RFC1-1 … RFC1-32", but §3.11 holds RFC1-33.
  - RFC 0004 README §5 says RFC3-16(a) gates six clauses; RFC4-30 makes it
    arguably seven.
  - RFC 0009 §8 says every clause is evaluable with RFC 0001–0006 bound;
    RFC9-8(a) says "RFC 0001–RFC 0009".
  - RFC9-45 says "that vocabulary is closed at twelve".
- **Integration lists:** RFC 0005 module 3 §5 names only RFC 0010 for the
  execution gate, where the README names RFC 0010 and RFC 0011; module 2 §5
  names only the egress choke point as checking RFC3-16(a).
- **Worth an owner read:** RFC4-23 items 2–3 may never let `active` render,
  since "between signals, worker liveness renders Unknown".
- **Minor:** RFC5-12 "(Project, provider)" against "(project, provider)";
  RFC4-19's "Execution record" against "Execution Record"; RFC 0007's front
  matter names RFC7-2(a)–(c) and RFC7-9(a)–(c), which the body marks only
  as "(a)"; RFC9-45 and RFC9-47(a) carry amendment narration in past tense.
