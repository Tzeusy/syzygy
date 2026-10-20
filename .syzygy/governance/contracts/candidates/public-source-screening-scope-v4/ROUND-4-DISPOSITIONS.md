# Round 4 dispositions — public-source screening scope, version 4

> **Candidate — binds nothing.** A sibling record for
> `docs/reviews/R-OLMR-SCREENING-SCOPE-V4-4-RAW.md` (verdict line 5:
> `Verdict: CONFIRM WITH EXCEPTIONS`; reviewed commit and manifest digest on
> its lines 3 and 4). Written 2026-10-15. Under the owner's notes-only rule
> (`decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md` §1), a round with
> no revise-severity finding clears the exact bytes it read, and its notes go
> in a record beside the package, never into the reviewed bytes. No package
> file, builder line or proposed byte was edited after the review.

Revise-severity findings: 0 (five findings, all `note`; raw lines 28, 62, 88,
99 and 119; "No blocking or revise finding." follows Finding 5).

| Finding | Severity | Disposition |
|---|---|---|
| 1 — the delta's "Not caught" list for key headers is narrower than what the bytes miss (URL-encoded, JSON-escaped, concatenated, en-dash, three-dash and lower-case headers) | note | Accepted as stated. None of these forms is a detector match, so each falls under the general cost already disclosed in the delta and packet ("a secret no detector matches reaches the fidelity packet"); the packet's key-block sentence lists only what the bytes catch. Carried to install: the delta's sentence should read "Not caught, among others: …; any encoded, escaped or split header" in any successor or readability pass. Not edited here |
| 2 — common unmatched shapes (provider API keys `sk_live_`, `AIza`, `github_pat_`; `Authorization: Bearer`; `curl -u`; Azure `AccountKey=`; passphrases with spaces; YAML block scalars) are not named individually | note | Accepted. Covered by the general cost sentence; the packet's named shapes are examples, not a closed list. The owner is told in the P-110 offer (register row) that provider keys and `Authorization` headers in a README quick-start reach the packet when another line in the file matches a detector |
| 3 — the packet omits the delta's `https` password containing `/` | note | Accepted. Within the general cost sentence; the delta carries the case. Named in the P-110 offer |
| 4 — editorial residue in delta lines 199–205 (trailing round-2 citation, "a docs settings .txt file"); `.md`/`.rst` under `docs/` are documentation by path too | note | Accepted as editorial. The substance is right by the reviewer's probe G; the class is decided by path, as the delta states. For any successor or readability pass. Not edited here |
| 5 — the impact ledger does not name `wholeArtifactLinePattern` (per-line in JavaScript: apply per line or with the `m` flag) or the anywhere-in-body `wholeArtifactFragments` comparison as install items | note | Accepted. The ledger's requirement to run the builder's body fixtures through the TypeScript screens carries both checks (six fixtures exercise them, three mid-line). The install bead must name both checks and the `m`-flag point explicitly |

Result: the bytes the raw names are cleared. P-110 is ready to offer to the
owner: "Sign screening scope version 4, variant span-guides" (recommended),
variant `span`, or decline.

## Recorder form (added 2026-10-20, at the version-4 act)

Reviewed record: docs/reviews/R-OLMR-SCREENING-SCOPE-V4-4-RAW.md

*(Added 2026-10-20 when the owner's version-4 act was recorded: the line
above and the numbered headings below are the form
`scripts/record_public_source_screening_scope_v4_act.py` reads, through
`record_versioned_signoff.validate_disposition`. No disposition changed; each
heading restates the table row above by its number, and the table stays the
disposition of record. The install items are carried in bead
`syzygy-olmr.1`.)*

### 1 — key-header "Not caught" list narrower than the bytes miss

Note; accepted as stated in the table above. Carried to install and to any
successor or readability pass.

### 2 — common unmatched credential shapes not named individually

Note; accepted. Covered by the general cost sentence, and named to the owner
in the P-110 offer and the 2026-10-20 question.

### 3 — the packet omits the delta's `https` password containing `/`

Note; accepted. Within the general cost sentence.

### 4 — editorial residue in delta lines 199–205

Note; accepted as editorial, for any successor or readability pass.

### 5 — the ledger does not name `wholeArtifactLinePattern` (per-line, `m` flag) or the anywhere-in-body `wholeArtifactFragments` check

Note; accepted. The install bead names both checks and the `m`-flag point
explicitly.
