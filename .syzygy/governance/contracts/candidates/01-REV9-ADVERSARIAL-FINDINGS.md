# Rev9 adversarial findings

Findings against the rev9 package as it stands at the open gate. F1 was
identified by the owner (directive §2) and verified against the artifact text;
the rest are the lead's adversarial pass informed by the directive. Each names
its evidence. These drive the rev10 rework; none is fixed by editing the
frozen rev9 corpus.

## F1 — Acceptance-semantic contradiction (blocking; directive §2, verified)

[Observed] `FOUNDATIONAL-RFC-ACCEPTANCE-RECORD.md` §2 states: "That committed
act record *is* the effective status." But the RFCs it would accept say:

- RFC3-16: effective status is established by "an independently verifiable
  **owner-act record**" (RFC-0003:408–413);
- RFC3-16(a): the A1 mechanism class is ceremony correlated to "an
  independently kept audit trail … which must live **outside `.syzygy/**`**
  and outside the untrusted actor class's write reach, or the correlation
  proves nothing" (RFC-0003:510–515);
- RFC3-16(b) bootstrap correlation: chat-phrase ceremonies plus git
  commits/tags are historical bootstrap acts requiring "a **one-time recorded
  correlation act**" once the mechanism exists; "until then those artifacts
  render with their gap stated honestly (the A9 posture), **not as
  verified**" (RFC-0003:563–571).

`.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md` is a same-tree
committed file inside the untrusted actor class's write reach. It is durable
historical evidence of a bootstrap act — it is **not** the independent audit
mechanism RFC3-16 requires, and the record's sentence claims for it exactly
the status RFC3-16(b) says a pre-mechanism act cannot have. The transaction's
five steps are executable and stay; the *status claim* overclaims.

**Repair direction (owner, directive §2):** distinguish
`owner-adopted bootstrap act` (human/social governance fact — phrase + digest
+ commit/tag; the human may govern development by it) from
`Syzygy-verified effective act` (the bootstrap act after one-time correlation
through the independent A1 mechanism). Until correlation: Syzygy must not
claim independent verification; provenance renders the gap honestly; git
commits/tags alone remain never sufficient. Update RFC 0003 and the
acceptance transaction consistently, weakening nothing.

## F2 — Context bloat is an architecture defect, not a style issue

[Observed] Active normative reading path ≈ 121,000 words (90,410 RFC;
see preflight). No mechanism selects task-relevant context; every governed
task implicitly requires whole-corpus loading. [Inferred] This is a material
correctness risk, not just cost: an agent that cannot load everything will
silently drop constraints, and no record shows what it actually saw.
Rev9 has no context-packet identity, no clause-level metadata, no
applicability rules. (Directive §1.3/§1.4 make this owner direction.)

## F3 — The RFC 0009 split assessment optimized the wrong variable

[Observed] `RFC-0009-SPLIT-ASSESSMENT.md` recommended no split, weighing
~208 external RFC9-n citations' stability over maintainability of a
19,269-word file. [Observed] The owner reverses this (directive §4): nothing
is accepted, nothing implements it, no OpenSpec requirement depends on its
file shape — this is the cheapest moment to restructure. Clause identities
are preserved via a package index, so the assessment's actual concern
survives the reversal.

## F4 — Validation claims are not reproducible off this machine

[Observed] `scripts/verify_rfcs.py` and `verify_rev7.sh` carry `/home/tze/…`
path assumptions and live under git-excluded `_bootstrap/`; the rev9 packet's
mechanical-verification story depends on them. The rev8 confirming reviewer
flagged machine-local script paths as an owner-attention observation; the
directive (§11) elevates it: a fresh reviewer on another machine cannot re-run
the checks from the delivered packet.

## F5 — Machine-client authentication is now foundational, still open

[Observed] RFC 0005 leaves the machine-client authentication mechanism an
open §8 question, acceptable while all clients were hypothetical. [Inferred]
Owner direction §1.1 makes an official CLI, scripts, and an MCP adapter
first-class clients of the one canonical service — so the
browser-vs-machine-client contract and the authentication *requirement*
(not the credential technology) must close before Mission Control can be
specified truthfully. Leaving it open would let RFC 0010/0011 cite an
authentication model that does not exist.

## F6 — No mission or autonomy contract exists

[Observed] Doctrine's human-triggered propagation posture and RFC 0008's work
model are one-work-item-grained; no contract lets a human approve one bounded
Mission under an envelope agents cannot widen. [Observed] The workspace
manifest is presentation-only (RFC 0003); no platform-level governance store
exists for budgets, portfolio priority, or cross-project execution authority —
so Mission Control direction (§1.1/§1.2) has no lawful home in rev9.

## F7 — No governed memory or context provenance

[Inferred] Rev9 execution records capture evidence of what ran, but nothing
records *what context an agent was given* — no packet digest in execution
records, no omitted-context accounting, no rule that chat history is not
canonical memory. Directive §1.4 makes this a first-class gap (RFC 0011).

## F8 — Open-question triage claims need re-proof after compaction

[Observed] Rev9 carries 21 open §8 questions with per-question "does not
block" rationales written against the rev9 corpus and the four-act gate.
[Inferred] Compaction, the §2 repair, and RFCs 0010/0011 change what several
questions block (notably RFC 0005 machine-client auth — F5; the workspace
manifest classification vs the new governance store). Every rationale must be
re-derived, not carried forward (directive §9).

---

Disposition of all findings: F1 → RFC 0003 rework + new acceptance record;
F2 → §3/§5/§7 compaction, metadata, context compiler; F3 → §4 split;
F4 → §11 portable scripts; F5 → RFC 0005 closure/scoping + RFC 0010/0011;
F6 → RFC 0010; F7 → RFC 0011; F8 → `08-OPEN-QUESTION-TRIAGE.md`.
