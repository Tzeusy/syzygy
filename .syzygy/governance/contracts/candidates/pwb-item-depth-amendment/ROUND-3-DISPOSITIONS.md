> # Record beside the package — not authority, binds nothing
>
> Dispositions the findings of the third fresh-context review of the
> repaired item-depth package. It is not a package artifact: the manifest
> does not hash it and no builder reads it. It offers nothing and performs no
> act (VIS-4).

# Round 3 dispositions — item-depth package

- **Reviewed commit:** `13778bd8d2cbb1841a6db66fd3ca16fe692b0702`.
- **Verdict (raw line 4):** `CONFIRM WITH EXCEPTIONS`; four findings, all
  notes, none revise or blocking, counted from the raw's finding headings.
- **Effect:** a notes-only round clears the bytes it read. The package is not
  edited by this record; editing a reviewed byte would retire the clearance.
  The package bytes at the reviewed commit equal the bytes at the commit this
  record lands on (`git diff 13778bd` over the package directory is empty
  before this file is added).

Reviewed record: docs/reviews/R-PWB-ITEM-DEPTH-AMENDMENT-REVIEW-6-RAW.md

## Dispositions

### 1 — PWB-REQ-013's scenario also reads false for an unmatched capability

Accepted and disclosed. The behavior is already stated in the package (an
unmatched capability gets no detail and renders no proposal); the omission is
one named consequence. Reader note for the sign-off: the PWB-REQ-013 scenario
"Proposal is shown only in affected capability detail" reads false for a
capability that matches no item or several, exactly as the PWB-REQ-011
scenario does in open point 3. Not edited into SEMANTIC-DELTA.md.

### 2 — the Unknown disclosure for an unmatched capability has no stated claim subject

Left and routed. The amended text forbids minting an identity from this
requirement; the disclosure attaches to the capability's existing identity
under PWB-REQ-007. The implementation-authorization stage names that subject
before any code lands; this amendment authorizes no implementation.

### 3 — a contradicted population is not surfaced before a currency bound exists

Accepted and disclosed. One primary reason (`no-currency-bound-declared`)
follows PWB-REQ-007; whether a contradiction may appear as a closed secondary
reason is an owner ruling for when a relation source is admitted. Until then
the exclusive-pair arm is unreachable (open point 1).

### 4 — the Observed and contradicted arms are untestable against production

Accepted and disclosed. Conformance evidence for those arms is fixture-only
(the oracle populations the Case specifies) until a source is admitted, as
open point 1 states.
