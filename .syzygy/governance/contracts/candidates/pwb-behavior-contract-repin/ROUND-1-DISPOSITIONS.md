> # Record beside the package — not authority, binds nothing
>
> Dispositions the findings of the first fresh-context review of the PWB
> behaviour-contract re-pin package. It is not a package artifact: the
> manifest does not hash it and no builder reads it. It offers nothing and
> performs no act (VIS-4).

# Round 1 dispositions — PWB behaviour-contract re-pin

- **Reviewed commit:** `140874b7364266475dd8980be480e2783e0d8e72`.
- **Verdict (raw line 5, the fourth non-blank line):** `CONFIRM WITH
  EXCEPTIONS`; two findings, both notes, counted from the raw's finding
  headings.
- **Effect:** a notes-only round clears the bytes it read. The package and
  its builder are unchanged since the reviewed commit.

Reviewed record: docs/reviews/R-PWB-BEHAVIOR-CONTRACT-REPIN-RAW.md

## Dispositions

### 1 — the "exactly two lines change" predicate has no mutant that kills it alone

Accepted as a note. The reviewer confirmed the claim directly
(`git apply --numstat` reports `2 2` per patch, and the applied bytes hash
to the manifest rows). A whitespace-only mutant would make the selftest
prove it; it is left for the act-recording change, which edits the builder's
neighbours anyway.

### 2 — the registry digest-path argument is sound; one supporting sentence is uncited

Accepted as a note. The Scope A direction's "What this does not do" says the
existing phrase-and-digest acts "remain the only way to perform the queued
packages" until the contract change lands; that sentence independently
supports the digest path the packet drafts. Read the packet's "Signing path"
together with it.
