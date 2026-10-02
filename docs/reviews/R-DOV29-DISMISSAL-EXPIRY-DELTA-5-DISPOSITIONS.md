# R-DOV29-5 dispositions — dismissal-expiry amendment, confirmation round 5

> **Candidate record — binds nothing.** This page dispositions the notes of
> one review. It performs no act, issues no direction and edits no reviewed
> byte.

**Review:** `R-DOV29-DISMISSAL-EXPIRY-DELTA-5-RAW.md`, retained verbatim
beside this page. Its verdict line (line 2) reads `Verdict: CONFIRM WITH
EXCEPTIONS`. It has no revise-severity finding and four notes, N-C4, N-A7,
N-A8 and N-B3 (raw lines 55, 70, 77 and 87; severity at line 138).

**Subject:** the candidate package
`.syzygy/governance/contracts/candidates/pwb-dismissal-expiry-amendment/`
and `scripts/build_pwb_dismissal_expiry_amendment.py`, as reviewed at commit
`b8ca841`. The review binds the package by the manifest file digest in the
raw's head (line 4), the act argument the package's REVIEW-BRIEF predicate
names.

**Why nothing here edits the package or the builder.** Under the 2026-09-26
sitting rule (`POLARIS-GATE-SITTING-2026-09-26-DECISION.md` §1), a notes-only
CONFIRM WITH EXCEPTIONS clears the exact bytes the review read. Any edit to
them retires that review (rule 10). This commit adds only this page, the raw
and the `docs/README.md` row and count; the package and builder have no diff
against `b8ca841` [Observed: `git diff --stat b8ca841 HEAD`].

| Note | Summary | Disposition |
|---|---|---|
| N-C4 | The packet's Q3 VIS-4 quote (`OWNER-DECISION-PACKET.md:105-108`) omits VIS-4's scope (shape-defining deltas) and reads the feature-level P-79 answer as applying per record. `SEMANTIC-DELTA.md:355-364` is accurate, and the rule stands on RFC2-15 alone. | **Routed to `syzygy-dov.34`.** The rule itself is unaffected; the note is about the packet's rationale. The owner should read Q3 with this note in hand. |
| N-A7 | An agent-committed record that states a human author would be in effect, because the author's kind is taken from the record alone; the packet does not disclose this. | **Routed to `syzygy-dov.34`**, to be named in Q2 or Q3. Surfaced to the owner with this clearing. |
| N-A8 | The Falsifier (`spec.md.patch:89-97`) does not name the inverse case (a refused, retired or lapsed record shown as in effect); the Case line (`:73-80`) omits the closed-list reason refusal. | **Routed to `syzygy-dov.34`.** |
| N-B3 | Builder mutants B12–B17 and B21–B23 survive both `--check` and `--selftest`; `selftest()` never calls `check()`. No docstring claim is false. | **Routed to `syzygy-dov.34`.** |

`syzygy-dov.29` stays open: the owner has not performed or declined the
dismissal-expiry amendment act.
