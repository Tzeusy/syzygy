# Review brief — public-repository admission, round 6

> **Candidate — binds nothing.** This brief says what an independent
> reviewer is given and what they decide. It is not a review and carries no
> verdict. Rounds 1-5 returned REVISE (`reviews/R-PUBLIC-ADMISSION-1-RAW.md`
> to `-5-RAW.md`); round 6 is over the round-5 repair, which changed the
> egress record's model of what a request carries.

## What the reviewer is given, and nothing else

CC-REV-1 calls for a fresh context holding only the artifact, its governing
references and the acceptance criteria. Read the prior raws for their
findings only; do not read the drafter's dispositions as evidence.

**The artifact under review.** Every file of
`.syzygy/governance/contracts/candidates/public-repo-admission/` except
`reviews/`: `OWNER-DECISION-PACKET.md`, this brief,
`PUBLIC-REPO-ADMISSION-MANIFEST.txt`, `templates/` (3 files) and
`instances/` (`requests/`, `redis/`, `egress-anthropic/`: a `params.json` and
one record each), plus `scripts/build_public_repo_admission.py` and
`.syzygy/governance/decisions/PUBLIC-REPO-ADMISSION-OWNER-ANSWERS-2026-10-03.md`.

**Governing references.**

- Doctrine: SEC-2 and SEC-3 in `.syzygy/governance/doctrine/security.md`;
  VIS-4.
- RFC3-16(a), RFC3-30; RFC4-1; RFC5-12 to RFC5-16, each read at its
  defining clause (`DIRECTIVE-REGISTER.md` locates them; quote the clause).
- `openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md`:
  REQ-polaris-generation-001, 017 and 025.
- The Q5 precedent: `decisions/PWB-SECRET-CLASSIFICATION-POLICY-BEHAVIOR-CONTRACT-REPIN-ACT.md`
  (its Ceremony section) and
  `decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`.
- `docs/polaris-generation/TARGETS.md`, for the pinned revisions.
- `AGENTS.md`, "Hard prohibitions" and "Verification rules".

## Acceptance criteria

Each is a yes/no question with the evidence that settles it.

1. **Are the round-4 findings repaired in the bytes?** For each of R4
   findings 1 to 5, quote the clause of the egress record or packet that
   repairs it, and say whether it does. Do the same for any R1-R3 blocking
   finding the later moves could have regressed (the egress record moved
   from `instances/requests/` to `instances/egress-anthropic/`).
2. **Do the records follow the owner's answers?** Q1 to Q7, as recorded in
   the answers direction, against the three records: provider and route,
   classes (all but `work-history`), run-directory retention, observing
   project, local-only editorial draft, and Q7's class not yet present.
3. **Does the egress record's scope equal the admitted observations?** It
   must list exactly the `(project:syzygy, repository)` pairs the two
   observation records name, no more. Is the scope sentence consistent with
   REQ-polaris-generation-025 (consents separately revocable, neither
   implying the other)?
4. **Are the Redis revisions right and the grant consistent?** The four
   commit object ids in `instances/redis/` must equal the pins in
   `TARGETS.md` (compare the text; do not contact any hosting service and do
   not read any repository body). Does the "fetch each admitted commit alone"
   scope still hold for four revisions?
5. **Is the Q7 position coherent?** The egress record lists the five classes
   in force and omits `project-documentation`. Confirm no record or packet
   sentence promises README or LICENSE egress before the RFC5-14 amendment,
   and that the packet says what the omission costs.
6. **Does the manifest mean what it says?** Run
   `python3 scripts/build_public_repo_admission.py --check`, `--selftest` and
   `--digests`; confirm each manifest row equals `sha256sum` of its record
   and that the row population equals the instance records. Name any
   builder or manifest claim that no selftest mutant covers.
7. **Is the signing-path reasoning sound?** Is the packet right that
   Scope A does not cover these consents, and that option selection at
   manifest rows is the precedent's form for them? Is that labelled
   Inferred where it is an inference?
8. **Does the package claim any authority it lacks?** No file may label
   anything accepted, adopted, approved or signed off; every banner must say
   it binds nothing; none may say a Redis (or requests) body was read. No
   Markdown file of the package may carry a 64-hex digest.
9. **Is the packet accurate about itself?** Its file locations, round
   counts, dispositions and the statement of what is unreviewed.
10. **Is the sent-content model closed and consistent?** Run
    `npx tsc -b packages/polaris-generation-core` then
    `node scripts/derive_generator_sent_text.mjs`. Do the envelope fields,
    per-stage `inputs` fields and the two instruction-text symbols in the
    egress record's "What a request carries" section equal the script's
    output? Is every byte a request can carry either a target span under
    an observation consent, a composite computed from one, an instruction-text
    symbol the screening scope's rule names, or a runtime-fixed byte the route
    entry will list? Under RFC5-15 part 2 and RFC5-14 ("never an attribute the
    composing step asserts about its own output"), is the instruction-text
    class determined by a policy rule rather than by the consent? Name any byte
    not covered.
11. **Do the R5 dispositions hold?** For each of R5 findings 1 to 6, quote
    the bytes that repair it and say whether they do.

## Out of scope

- Whether to perform any act; that is the owner's alone.
- The recorder and the `check_governance.py` registration. They are prepared
  after this review, against the confirmed commit, and get their own check.
- The public-source screening scope and registry entries (drafted separately).

## Recording

Store the raw output verbatim under the package's `reviews/` as
`R-PUBLIC-ADMISSION-6-RAW.md` (a re-issue is a second `-RAW.md`, never an
overwrite). **The raw's head is a predicate the recorder enforces.** The first
four non-blank lines must be the title and exactly:

```text
Reviewed commit: <the 40-hex commit the reviewer read>
Manifest SHA-256: <SHA-256 of the FILE PUBLIC-REPO-ADMISSION-MANIFEST.txt>
Verdict: CONFIRM | CONFIRM WITH EXCEPTIONS | REVISE
```

`Manifest SHA-256` is the digest of the manifest **file** at the reviewed
commit, which carries all three act arguments as rows; it is not any one row.
Print it with
`python3 scripts/build_public_repo_admission.py --manifest-digest`, or with
`sha256sum`. Keep the verdict within the first four non-blank lines, with no
blank-line padding. Number findings continuously as
`**Finding N — title** (blocking|revise|note)` under a `## Findings`
heading. A CONFIRM WITH EXCEPTIONS clears the bytes only when every finding is
a `note`; those notes go in a sibling `ROUND-<n>-DISPOSITIONS.md` naming the
raw on a `Reviewed record:` line, never by editing the reviewed files. Any
later edit to the package retires the review (rule 10).
