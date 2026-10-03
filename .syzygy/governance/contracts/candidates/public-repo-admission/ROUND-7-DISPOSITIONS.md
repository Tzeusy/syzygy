> # Record beside the package — not authority, binds nothing
>
> Dispositions the notes of the round-7 fresh confirmation review of the
> public-repository admission package. It is not a package artifact: the
> admission manifest does not hash it and no builder reads it. Nothing here
> offers a phrase or performs an act (VIS-4).

# Round 7 dispositions — public-repository admission package

- **Reviewed commit:** `7704b4a575acf29de93e3872ff549a856e6395ec`.
- **Raw:** `reviews/R-PUBLIC-ADMISSION-7-RAW.md`, retained verbatim (CC-REV-6).
- **Verdict (raw line 4):** `CONFIRM WITH EXCEPTIONS`; five notes, no revise or
  blocking finding.
- **Effect:** under the owner ruling of 2026-09-26 a notes-only round clears the
  bytes it read. No package byte is edited by this record; the stopping rule
  for the carried-content item ends here.

## Machine-readable binding

Reviewed record: .syzygy/governance/contracts/candidates/public-repo-admission/reviews/R-PUBLIC-ADMISSION-7-RAW.md
Revise-severity findings: 0

Arguments the reviewed manifest carries, copied by script (`--digests`); each
goes stale the moment its record moves, which is rule 10 made visible:

CONSENT TO PUBLIC OBSERVATION OF PSF-REQUESTS: d154165cc4c4e0d995644f1d764bfacddf070a9aa301ee2c9fc62dff4ba06d41
CONSENT TO PUBLIC OBSERVATION OF REDIS-REDIS: a733220dcbc4276d396e32f51c39dcc4665e07579ecca3f0074e7e6e5a1916a4
CONSENT TO PUBLIC TARGET EGRESS TO ANTHROPIC: cbae0a845b1086e1371906536f8b96d742317ad87fb3967362687b083adaf073

## Dispositions

### 1 — the "no class fails the derivation" sentence is broader than the call-site parse

Left in the confirmed bytes; carried forward outside them. The omission fails
closed (the egress check refuses a field outside the table). The derivation
script is not a manifest row, so it is hardened without touching any signed
byte: a stage the parse does not match, or a stage called through a variable or
a differently quoted name, fails the derivation instead of dropping out, with a
mutant for each. The sentence's "each field" is read as "each sent field": the
`input`, `permit` and `signal` port rows are not sent classes.

### 2 — classes are field-name labels, not provenance

Left. The table is a field-level gate; the class of content is decided at the
egress check from its origin under the screening scope (RFC5-14, RFC5-15).
Carried to the public-source screening scope package, whose rule text now says
the classification is by origin at the runtime check and never by the field name.

### 3 — the run-profile rule names a file and a validation the generator lacks

Left; the packet already presents it as an open owner ruling and no signed byte
assumes the answer. Carried to the screening scope package, whose run-profile
rule names the validation that is to land in code with the typed reader
questions (lane-e, PR #259) and says the generator does not validate
`readerQuestions` today.

### 4 — excluded-source metadata: paths are not sent, reasons are not closed in code, the alternative costs a code change

Left in the signed bytes. The record already encodes the recommended answer and
the packet says so. Carried to the owner sitting packet (PR #260): paths of
excluded sources are not sent today; `reason` must come from a closed list the
screening scope imposes; sending admitted sources' metadata only needs a change
to the pipeline's source-population construction and a regenerated record.

### 5 — the admitted-pairs list renders as a peer of the population bullets

Left. Cosmetic, in signed bytes; an indent at the next version.
