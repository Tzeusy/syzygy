> # Record beside the package — not authority, binds nothing
>
> Dispositions the notes of the round-2 fresh confirmation review of the
> second Anthropic egress version. It is not a package artifact: the manifest
> does not hash it and no builder reads it. Nothing here offers a phrase or
> performs an act (VIS-4).

# Round 2 dispositions — public egress version 2

- **Reviewed commit:** `d2f9ab90b530c00e4c96d5f1a4e6ccff4c78f5b5`.
- **Raw:** `reviews/R-EGRESS-V2-2-RAW.md`, retained verbatim (CC-REV-6).
- **Verdict (raw line 4):** `CONFIRM WITH EXCEPTIONS`; six notes (N-1 to N-6),
  no revise or blocking finding.
- **Effect:** a notes-only round clears the bytes it read (owner ruling of
  2026-09-26). The lead nevertheless ordered one narrow repair for N-1, which
  misstated what the owner consents to; every byte it changes retires this
  review (rule 10), so a delta review (round 3) follows, and it is the last.

## Machine-readable binding

Reviewed record: .syzygy/governance/contracts/candidates/public-egress-v2/reviews/R-EGRESS-V2-2-RAW.md
Revise-severity findings: 0

## Dispositions

### N-1 — the packet presented code defaults as limits that signing carries

Repaired. The packet no longer states the caps as terms. It says the record
caps no volume, names the defaults as defaults of the discovery code (1,500
characters, 40 files per map call, 40 map calls, and up to 400 claims of up to
400 characters in the second call), says a larger discovery budget stays inside
the consent, and says the run budget the trigger supplies bounds volume, which
the owner sets and this act does not.

### N-2 — the dispatch brief's expected manifest digest was the record digest

Accepted; the labels were swapped in the dispatch, not in the scripts. The
manifest file's digest is what `--manifest-digest` prints and what the head
carries; `--digests` prints the record's digest, the act argument. The brief
now says so and says a dispatch names each by the command that prints it.

### N-3 — the template pin was count-only

Repaired. `v2.json` pins the SHA-256 of the template's unified diff against the
first version's, as well as the counts, and `--check` fails when either moves.
The selftest has the reviewer's mutant: a sentence changed in place with the
line counts unchanged.

### N-4 — the first version's recorder selftest covered the predicate, not the call site

Repaired. The selftest now calls `do_record` for the first version's egress act
with the second version's act record present and requires the refusal, with its
reason, and no file written; disabling the refusal at the call site fails the
selftest (tried, 35 of 36 held). The lost docstring of `selftest()` is
restored. The coupling between the two recorders' file name is asserted when the
second version's recorder lands, in its own selftest.

### N-5 — the Agent SDK summary omitted `cache_control` on the fixed system prefix

Repaired. The template says `cache_control` sits on the fixed system prefix and
on the generator's system prompt and input.

### N-6 — delegation reaches any successor entry in the same role

Recorded as a known limitation, in plain words, in the packet: a later
owner-approved successor entry flows into this consent without a new egress
version, bounded by the absolute ban and the refusal of fields outside the
table, and that entry needs its own owner act.
