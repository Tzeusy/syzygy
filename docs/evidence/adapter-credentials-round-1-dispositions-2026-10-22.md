# Adapter-credential declarations: round-1 review dispositions

[Observed] This record dispositions the notes of
`docs/reviews/R-GP-IMPL-ADAPTER-CREDENTIALS-1-RAW.md`, the round-1 CC-REV-1
review of `syzygy-bpyt.8.9` (pull request #499).

- Verdict: `CONFIRM WITH EXCEPTIONS` (line 2 of the raw).
- Reviewed commit: `4cd9a511` (line 3).
- Subject: `r1-review.diff` sha256
  `a63d5501d0c518a6e67baf1ba3537b3a357bf427902d4320e44fe6e96d6ce88d` (line 4),
  equal to `git diff 32c16625 4cd9a5119ca18e0f852cda24d8be5a466ad04269`.

The raw says "No blocking finding." (section 4) and counts the changed
outcomes as "More lenient: 0 of 154." (section 5). Under the owner's notes-only
stopping rule
(`.syzygy/governance/decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md`
section 1), the round clears the exact bytes it read, and those bytes are not
edited. This record sits beside them and holds every correction the notes ask
for. It is an implementation record and binds nothing.

Revise-severity findings: 0

## N1: a declaration refusal skips the step's credential reads

[Observed by the reviewer] The declaration refusal returns before the list is
read and before any credential is opened. In 27 of the 45 reason-changed
differential rows, an observation the base made is no longer made.
REQ-polaris-generation-033's falsifier names "a credential read is skipped at
a check … after a permitting brief". This is unreachable at the reviewed
commit, because the permitting arm is off and no adapter declares a
credential. The base already skips the reads in the same way when the list
source fails.

**Disposition:** filed as `syzygy-bpyt.8.15` (P2, owner-gated). It must close
before the arm flips, and it is linked from `syzygy-bpyt.1.6` (the CC-SEC-3
packet). The fix changes a pre-existing refusal string, so the packet lists
it for the owner, or puts to the owner the reading that a fail-closed refusal
without reads satisfies REQ-033.

## N2: a non-read refusal renders as an Observed readability claim

[Observed by the reviewer] `render.ts:605` renders every failed probe,
labelled Observed, as a credential that "was readable", and every failure
carries the kind `adapter-credential-readable`. A declaration refusal would
therefore render as an Observed claim about a read that was never made. The
pull request's residual 4 already disclosed this for list-source refusals.

**Disposition:** carried in `syzygy-bpyt.8.15` with N1. A configuration refusal
gets its own finding kind and render text, not labelled Observed. That changes
rendered bytes and a wire value, so it waits for the owner's listing.

## N3: the Claude Code login copies need an owner ruling

[Observed by the reviewer] `polaris.ts:338-345` copies the operator's Claude
Code login into each launched session's home under the state root, and no
tracked source removes the copies. [Inferred by the reviewer] The lane's
classification, the session's own login and not a typed-adapter credential, is
defensible for the attended session but contestable for copies that Syzygy
writes and keeps. Settling it is a security-posture decision.

**Disposition:**
- The owner question, with both arms and what follows from each, is recorded
  on `syzygy-bpyt.1.6` for the CC-SEC-3 packet. SEC-3's credential clause binds
  only at that sign-off, so the sign-off is where the owner decides.
- The unlabelled comment at `credential-probe.ts:123-124` is qualified in
  `syzygy-bpyt.8.16`.

## N4: exact membership is pinned only against `path.normalize`

[Observed by the reviewer] The case-folding mutant R2 and the trimming mutant
R3 survive.

**Disposition:** filed as `syzygy-bpyt.8.16` (P3). It adds three spelling
variants to the membership test and records R2 and R3 killed.

## N5: the declaration list is a second hand-kept constant

**Disposition:** recorded on `syzygy-bpyt.1.6`, which states the residual in
plain words. When the first credential-holding adapter lands,
`CONFIGURED_ADAPTER_DECLARATIONS` is derived from the adapter modules or a
registry field, with a test that every source opening a credential path is
represented.

## N6: the rendered disabled reason disagrees with the comment above it

`execution-rule.ts:18` still names `syzygy-qkea.5`, which closed in pull
request #380. Rewording it changes every brief's bytes, which GP-Q0 does not
list, so the pull request correctly left it.

**Disposition:** recorded on `syzygy-bpyt.1.6`. It is reworded in the bead that
flips the arm, inside the same owner-visible change.

## N7: the authority citation and the owner notice

**Correction.** The pull request body cites "GP-Q0 part 3" as the authority for
the new refusal. The listing that authorizes it is GP-Q7,
`.syzygy/governance/decisions/OWNER-DIRECTION-GREENFIELD-PARITY-ANSWERS-2026-10-21.md`
lines 132-134: "Separate beads cover: … a credential list that fails closed
when a configured adapter declares a credential the list lacks."

**Disposition:** the class-4 owner notice is posted on `syzygy-bpyt.10` when the
pull request merges.
