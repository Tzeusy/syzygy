# Owner decision packet — Three-Surface POC block-provenance amendment (N9, POC half)

> **Candidate — binds nothing.** Nothing here is signed, adopted or labelled
> accepted. This packet puts three questions to the owner; only the owner's
> answer binds anything (VIS-4). Register row: P-97.

**Status:** drafted 2026-10-03 under bead `syzygy-u05.9`. One fresh-context
review round covers this package and its PWB sibling; its verdict and
dispositions are recorded in the PWB half's `ROUND-1-DISPOSITIONS.md`, in
`../pwb-anchor-resolution-amendment/`, once the round has run.

## What you would be signing

One amendment to POC-REQ-001 (code structure) and POC-REQ-010 (work items) in
the signed Three-Surface POC specification. Read `SEMANTIC-DELTA.md` for the
full account. In short:

- **One provenance shape.** Each of the two observations states where it came
  from once, as one record in the same shape the machine answer's entities and
  relationships already use. Today they use three different shapes.
- **No row repeats it.** No work item and no file entry may carry the
  observation's revision or capture instant in a field of its own. Each still
  carries the revision as provenance, by belonging to the observation.

[Observed] At Butlers `32f38feb`, every one of 7,952 work items and 6,950 file
entries repeats its block's revision. That is 772,900 bytes, 13.44% of the
`/api/poc` body. No surface reads the per-row copy.

**What signing does not do.** It starts no implementation; removing the
fields needs a fresh implementation authorization after sign-off. It changes
no served fact and no human surface.

## Question 1 — sign this version?

| Option | Meaning |
|---|---|
| **Sign v1.0** (recommended once the review clears) | The sign-off change applies the patches and carries the reconciliation updates in `IMPACT-LEDGER.md`. |
| Decline | The two requirements stay as signed, and every row keeps its revision. |
| Revise | Name what to change; a new version gets a new review round. |

## Question 2 — by which route?

The same question P-84 already asks for the POC identity amendment. The
2026-10-02 Scope A direction names "the PWB specification deltas, the
observer registry entry and the contract successors queued behind them"; a
POC specification amendment is not in that list.

| Option | Meaning |
|---|---|
| **Follow your P-84 answer** (recommended) | Whatever route you choose there applies here too, so the two POC amendments are signed the same way. |
| Extend Scope A to this package alone | Signed by version tag; the sign-off change registers it with `scripts/record_versioned_signoff.py`. |
| Phrase and digest | A dedicated recorder is written, and you type a phrase naming the manifest digest. |

## Question 3 — the narrower rule

The bead asked for "the rule that a row may not repeat a value its block
declares". This package forbids exactly two values per row: the observation's
revision and its capture instant.

- **Why narrower.** [Observed] The only other repeats of this kind in the body
  are inside PWB-owned project-shape declarations, where a per-declaration
  value is evidence: in one of 416, the fact is Unknown and states no value
  while its declaration still carries the value it declared. A general rule
  would reach those fields, and this package may not amend the PWB
  specification.
- **What it costs.** A future block could add a new header field and repeat
  it per row without breaking this rule.

| Option | Meaning |
|---|---|
| **The two identity values** (recommended) | As drafted. |
| Every header value | A wider rule, with a list per block of what it declares; it needs a PWB carve-out or a matching PWB delta. |

## Order against the POC identity amendment (P-84)

That package touches the reader notes, POC-REQ-054, 055 and 060, not 001 or
010. The spec patches compose in either order. Both rewrite the dependency
declaration's one digest line, so whichever you sign later is regenerated
over the earlier one first. That is mechanical and needs no answer from you.
