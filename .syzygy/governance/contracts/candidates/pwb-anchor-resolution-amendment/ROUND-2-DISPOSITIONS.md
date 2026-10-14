> # Record beside the packages — not authority, binds nothing
>
> Dispositions of the second fresh-context review of the two N9
> machine-channel amendment packages: this directory's PWB anchor-resolution
> amendment (P-96) and `../three-surface-poc-block-provenance-amendment/`
> (P-97). This record is not a package artifact: neither manifest hashes it
> and no builder reads it. It is the sibling record the owner's 2026-09-26
> ruling provides for a notes-only round
> (`../../../decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md` §1). It
> offers nothing and performs no act (VIS-4).

# Round 2 dispositions — N9 machine-channel amendments (PWB and POC halves)

Reviewed record: docs/reviews/R-N9-MACHINE-CHANNEL-AMENDMENTS-2-RAW.md

PWB manifest SHA-256: e7f304c79959341a9735516e87ccb991c012e695c2a16a90ee18ad2f1928c8f9

POC manifest SHA-256: c16bbb9bebdf82df37a40cbf070910a254ec47b0ca459e538bfe872993b28a50

Revise-severity findings: 0

- **Reviewed commit (raw line 2):**
  `ae8c074066d8e6c511d8064b505e3f89e3f2b43d`.
- **Verdicts (raw lines 5 and 6):** PWB `CONFIRM WITH EXCEPTIONS`; POC
  `CONFIRM WITH EXCEPTIONS`. Fourteen findings, every one a note; no revise
  and no blocking finding (raw lines 390–391). Findings 12, 13 and 14 apply
  to both packages.
- **Why the round ran.** The brief's stopping rule said one round only. The
  owner's direction of 2026-10-14
  (`../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2026-10-14.md`)
  ordered one fresh confirmation round per packet before the owner is asked
  the content questions. This raw is that round. The reviewer recorded
  "[Unknown] Whether the owner ordered it" (raw line 17–18); the direction
  record answers that.
- **What clears.** Under the 2026-09-26 ruling, a round with no
  revise-severity finding clears the exact bytes it read. These are the two
  manifests whose file digests stand above, at the reviewed commit, and the
  package prose beside them. [Observed 2026-10-14] Both manifest files hash
  to those digests on the integration branch, and `git diff ae8c0740` over
  both package directories was empty before this record was added. Both
  builders' `--check` pass there with the repaired P-84, P-85 and P-86
  patches landed, so the sign-off-time composition step the raw names
  (raw lines 97–104) holds at that commit; a later change to a sibling
  patch needs the check again.
- **Nothing in either package is edited.** Every note below is
  dispositioned here, not in the reviewed bytes; repairing any of them in
  the package would retire the clearance (rule 10). Each is **open** for
  the owner, with the repair the raw suggests.
- **What the clearance is not.** It is not a sign-off. P-96 and P-97 still
  ask their own questions, and only the owner's answer binds.

## Correction carried here instead of in the package (finding 14)

These sentences in the cleared bytes say no round 2 was dispatched or that
the repaired bytes are unreviewed. They are no longer true as of
2026-10-14, and this record, not an edit, carries the correction:

- both `SEMANTIC-DELTA.md` Review sections;
- both `OWNER-DECISION-PACKET.md` Status lines;
- this directory's `ROUND-1-DISPOSITIONS.md` ("no second round is
  dispatched"; "neither package's repaired bytes have been reviewed").

Register rows P-96 and P-97 sit outside the packages and are updated
directly.

## A residual for the sign-off recorder

[Observed 2026-10-14] `scripts/record_versioned_signoff.py`'s `parse_head`
requires exactly one `Manifest SHA-256:` line and one `Verdict:` line in a
raw's first four non-blank lines. This raw's head carries
`PWB manifest SHA-256:` and `POC manifest SHA-256:` lines, and its verdict
lines are its fifth and sixth. Run against it, `parse_head` refuses: "review
head does not carry exactly one `Manifest SHA-256:` line". Its findings
section parses (14 findings, all notes). Neither package is registered in
that recorder yet. Recording a sign-off of either half on this raw needs
recorder support for a two-package head; the raw is not edited.

## Dispositions

### 1 — the impact ledger still describes the resolver round 1 found unrunnable (note, PWB)

**Open.** Raw line 171. `IMPACT-LEDGER.md` says the resolver "reads only the
machine answer's bytes"; the amended oracle reads "the machine narrative's
anchors and the machine answer's bytes". The normative text is right; the
implementation guidance is stale. Suggested repair: copy the oracle's
wording into the ledger bullet.

### 2 — the pair's PWB-REQ-020 derivability is asserted, not argued (note, PWB)

**Open.** Raw line 181. The argument that holds is transitive (each anchor
is itself a served value PWB-REQ-020 already requires to be derivable), and
no PWB-REQ-020 derivability checker exists for the narrative today.
Suggested repair: one sentence in the delta stating both.

### 3 — "an `identity` field of its own" still leaves a semantic call (note, PWB)

**Open.** Raw line 198. Selecting by key and then excluding references
needs judgment for a future `identity`-keyed reference. Suggested repair:
state the rule structurally ("a field named `identity` is a record's own
identity; no other key is").

### 4 — the withholding limb does not say whether the narrative is re-rendered (note, PWB)

**Open.** Raw line 210. Re-running only the resolver tests the resolver, not
the served pair. Suggested repair: "serve the narrative again from a machine
answer with that identity withheld".

### 5 — "does not resolve" collides with POC-REQ-031's "resolves" (note, PWB)

**Open.** Raw line 221. A reader may take the 19 non-resolving anchors for
the dangling citations signed POC-REQ-031 says there are none of. Suggested
repair: one sentence saying a non-resolving anchor is not a dangling
citation.

### 6 — the PWB package names two pending siblings; its builder declares four (note, PWB)

**Open.** Raw line 238. The delta, ledger and packet name class-granular and
release-label only; the builder also declares accessible-name and
opening-index, and `scripts/pwb_requirement_amendment.py` lists this
package as pending. Suggested repair: name all four, and add the engine to
the ledger's "At adoption" item 5.

### 7 — the POC package omits its second pending sibling and the exclusive pair (note, POC)

**Open.** Raw line 260. The POC half names only the identity amendment
(P-84), not the governing-intent amendment (P-100) or the declared
mutually exclusive pair. Suggested repair: name P-100 and the pair.

### 8 — the POC-REQ-010 time exemption is open in the obligation and closed in the oracle (note, POC)

**Open.** Raw line 276. Suggested repair: make the obligation, oracle and
falsifier say the same thing, either the three named times everywhere or
the open class in the oracle.

### 9 — the POC falsifiers do not mirror the capture-instant limb of the oracle (note, POC)

**Open.** Raw line 291. The oracle catches it; the falsifier does not list
it. Suggested repair: add "or an observation whose own fields hold the
capture instant other than once".

### 10 — one [Observed] sentence goes beyond the evidence record (note, POC)

**Open.** Raw line 304. The 416th declaration is outside `headerRepeats`'
population. Suggested repair: relabel it [Inferred], or add the case to the
script and the record.

### 11 — the POC ledger's list of header readers predates two new readers (note, POC)

**Open.** Raw line 319. `reevaluation.ts` and `reevaluation-copy.ts` read
the header at the reviewed commit and are not in the ledger's list. The
spec is unaffected. Suggested repair: re-derive the list at the sign-off
commit.

### 12 — the token guard misses lowercase permissive sentences (note, both)

**Open.** Raw line 335. Three inserted lowercase-`may` sentences and one
widened scenario count pass the structure gate. The reviewed bytes contain
no such sentence; the review stays the gate. Suggested repair: count
`\bmay\b` case-insensitively, count `authority` and `snapshot input` per
block, and pin the scenario's THEN line whole.

### 13 — the evidence record does not name the script revision that produced it (note, both)

**Open.** Raw line 355. `measuredOn.syzygyCommit` names a commit at which
the measurement script does not exist. Suggested repair: record the
script's commit or sha256 in the record.

### 14 — the status prose will be stale once this round is retained (note, both)

**Dispositioned by this record.** Raw line 365. The stale sentences are
listed under "Correction carried here" above and are not edited, as the
raw advises; the direction record names who ordered the round. Register
rows P-96 and P-97 are updated outside the packages.
