> # Record beside the package — not authority, binds nothing
>
> Dispositions the notes of the fourth fresh-context review of the
> missing-currency package. It is not a package artifact: the manifest does
> not hash it and no builder reads it. It offers nothing and performs no act
> (VIS-4).

# Round 4 dispositions — missing-currency package

- **Reviewed commit:** `12abd623a63c5f6722f3519b11cf8af8e2a4bac2`.
- **Verdict (raw line 4):** `CONFIRM WITH EXCEPTIONS`; six notes, none
  revise or blocking.
- **Effect:** a notes-only round clears the bytes it read. The package is not
  edited by this record; editing a reviewed byte would retire the clearance.

Reviewed record: docs/reviews/R-PWB-MISSING-CURRENCY-DISCLOSURE-SCENARIO-DELTA-CONFIRMATION-4-RAW.md

## Dispositions

### 1 — the ledger says there is no chain link, but one is registered

Accepted as a stale sentence. The link in the governance check is
existence-gated: it binds nothing until a sign-off record exists, and the
version-tagged recorder performs the sign-off. The ledger sentence describes
the earlier plan and is left unedited to keep the reviewed bytes.

### 2 — the delta's quoted scenario omits two AND bullets

Left. The patch under `proposed/` is the inserted text and the manifest
hashes it; the delta discloses both omitted bullets in its "does not change"
items 6 and 7. The quote is illustrative, not the insertion.

### 3 — machine-answer parity rests on an `[Inferred]` sentence

Left and routed. The implementation bead must test that the machine answer
carries the disclosure under the PWB-REQ-020 parity obligation; this
amendment authorizes no implementation, and the Inferred label stays.

### 4 — builder predicates are token-presence checks

Accepted. The builder is a mechanical guard on the patch text, not a
semantic oracle. Semantic correctness is carried by fresh review, which
read these bytes. Strengthening the predicates is optional hardening.

### 5 — stale phrase wording in the packet and brief

Left. The wording is inert and the sign-off is version-tagged; the sign-off
record, not the packet, states how the owner gave it.

### 6 — the primary reason is fixed without a stated precedence

Left, and surfaced to the owner with the sign-off question. RFC2-24 defines
no precedence among Unknown reasons, and RFC2-9 already names this reason
for the class, so the scenario is consistent with the contract; the choice
to harden a precedence is the owner's to confirm.
