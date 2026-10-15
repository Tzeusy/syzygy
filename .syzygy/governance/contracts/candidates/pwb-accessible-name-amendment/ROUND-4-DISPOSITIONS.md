> # Record beside the package — not authority, binds nothing
>
> Dispositions of the fourth fresh-context review of the PWB accessible-name
> amendment package (PWB-REQ-016, P-99, slice C), the
> regeneration-confirmation round over the P-86 sign-off. This record is
> not a package artifact: the manifest does not hash it and no builder
> reads it. It is the sibling record the owner's 2026-09-26 ruling provides
> for a notes-only round
> (`../../../decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md` §1),
> named by the shared brief
> (`../pwb-opening-index-amendment/REVIEW-BRIEF.md` §"Round 4"). It offers
> nothing and performs no act (VIS-4).

# Round 4 dispositions — PWB accessible-name amendment

Reviewed record: docs/reviews/R-PWB-ACCESSIBLE-NAME-AMENDMENT-4-RAW.md

Manifest SHA-256: f794d73536f55b916fa09bff8504cecf7b9b67d225c0cc0916211184cbb95490

Revise-severity findings: 0

- **Reviewed commit (raw line 2):**
  `83b29c96775d9c2215292fa41e1599080f0b802c`.
- **Verdict (raw line 4):** `CONFIRM WITH EXCEPTIONS`. Three findings,
  every one a note; no revise and no blocking finding (raw line 116:
  "Every finding below is a note."). The raw has no closing count; the
  three were counted by script from its `**Finding N — …** (note)`
  headings. Finding 3 applies to this package and to the opening-index
  package (P-98), whose own round 4 is judged in its own raw.
- **Why the round ran.** The owner's cycle-3 directions, recorded in
  `../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-3-2026-10-14.md`:
  for P-99, "Carry if review clears" — its v1.0 sign-off carries to the
  version regenerated over P-86 if this confirmation review is notes-only
  and `proposed/spec.md.patch` is byte-identical to the version round 3
  read.
- **What clears.** Under the 2026-09-26 ruling, a round with no
  revise-severity finding clears the exact bytes it read: the manifest
  whose file digest stands above, at the reviewed commit, the proposed
  bytes it hashes, and the package prose beside it. [Observed 2026-10-15
  on `governance/cycle-3-records` over `origin/main` `60995b23`] the
  manifest file hashes to that digest; `git diff --stat 83b29c96` over
  this directory, its builder, the shared engine and the PWB change
  directory is empty; `proposed/spec.md.patch` has the same git blob at
  `d6b3784f` (round 3's reviewed commit) and here, sha256
  `6ba8075c8a76c25c5108944e6d814903553299bb8b2d504e8859304d4bf600cc`.
- **Nothing in the package is edited.** Every note below is dispositioned
  here, not in the reviewed bytes. Each is **open**, with the repair the
  raw suggests.
- **What the clearance is not.** It is not a sign-off by itself. The
  owner's carry-over answer, applied in the same change as this record,
  is what signs v1.0 (`../../../decisions/PWB-ACCESSIBLE-NAME-AMENDMENT-SIGNOFF-v1.0.md`).

## Corrections carried here instead of in the package

These sentences in the cleared bytes are no longer true as of 2026-10-15.
This record, not an edit, carries the correction:

- `ROUND-3-DISPOSITIONS.md` §"Regenerated over the P-86 sign-off", "They
  await one regeneration-confirmation round, briefed in … §"Round 4" and
  not yet run", and "Whether the owner's Q1 answer, "Sign v1.0", carries
  to the regenerated version or is asked again is the owner's to say".
  Round 4 has run and returned notes only, and the owner answered "Carry
  if review clears".
- The "P-86 pending" sentences finding 1 names: `SEMANTIC-DELTA.md`
  lines 205 and 218, `IMPACT-LEDGER.md` lines 21, 69 and 85, and
  `OWNER-DECISION-PACKET.md` line 132. P-86 was signed v1.0 on 2026-10-14
  (`../../../decisions/PWB-CLASS-GRANULAR-EXTRACTION-AMENDMENT-SIGNOFF-v1.0.md`);
  the pending siblings at the reviewed commit were this package, P-98 and
  P-85.
- `ROUND-3-DISPOSITIONS.md` §"Composition at the integration branch", "all
  four pending PWB builders' `--check` pass … class-granular". True at
  `8acb0795`; at the reviewed commit class-granular is performed and its
  builder fails by design (finding 3).

The shared brief is not edited. Register row P-99 and `docs/README.md`'s
opening-index and accessible-name row sit outside the package and are
updated directly.

## Dispositions

### 1 — The P-86 sign-off made the package's "P-86 pending" sentences false, and the dispositions do not carry that correction (note)

**Dispositioned here.** Raw line 120. The correction is carried in the
section above; the package prose is not edited.

### 2 — The byte-identical spec patch now applies by offset (note)

**Open, checked.** Raw line 144. The hunk headers are the round-3 base's;
`git apply` places both hunks by context. [Observed 2026-10-15] The
recorder applies through the builder (`engine.apply`), whose `--check`
passed on this branch before the sign-off, so the offset patch applied.
A later regeneration may refresh the headers.

### 3 — Composition and sibling state at this commit (applies to both packages) (note)

**Open.** Raw line 162. Once this package is signed, P-98 and P-85 are
regenerated over its applied bytes and reviewed again before they are
offered; their builders' `--check` is expected to fail until then.
