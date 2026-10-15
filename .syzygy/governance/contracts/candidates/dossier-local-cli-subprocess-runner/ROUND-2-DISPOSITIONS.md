> **Candidate — binds nothing.** Classification of review round 2. A
> disposition performs no act, and this one repairs nothing.

# Round 2 dispositions — DOSSIER-CLI-RUNNER-1

Raw: `docs/reviews/R-DOSSIER-CLI-SUBPROCESS-2-RAW.md`, verdict `REVISE`
(line 4), over commit `b386b433eceaf0cffdbbb8c125c93328083e0f74`. Round-1
closure: 10 of 11 closed, finding 1 not closed in part (raw line 41). New
findings: one revise and five notes (raw line 110).

The lead decided, under the owner's autonomy direction, to run one confirming
round: a notes-only round clears the bytes, and a `REVISE` is classified,
with nothing repaired, after which the drafting lane stops. This round is
`REVISE`, so `SEMANTIC-DELTA.md` is **not edited**, it is **not cleared**,
and it is **not offered for sign-off**. Register row P-111 says so.

| # | Class | Needs an owner choice? | Classification |
|---|---|---|---|
| 1 | revise | No (drafter repair) | Administrator-managed settings stay in effect and are only disclosed, so they could redirect the provider while the run reads as covered. This is the remainder of round-1 finding 1. The raw offers two repairs: read the managed layer's provider-selecting and `env` keys and refuse on a mismatch, or weaken the effective-provider guarantee and disclose it as unconfirmed. The drafter recommends the first arm, because it keeps the guarantee and stays fail-closed. |
| 2 | note | No | The allow-list wording would admit the declared provider's own credential variables. Tighten it to admit no credential variable. |
| 3 | note | No | The Falsifier drops the scenario's credential-file exception. Align the two. |
| 4 | note | No | The excluded sources leave out skills, custom agents, commands and output styles, in the operator's home and in the clone. Add them to the list and the Cases. |
| 5 | note | No | The prototype's `SYZYGY_POLARIS_AGENT` stand-in override is a substitution route the requirement forbids. Name it in Downstream impact as test-only or removed. |
| 6 | note | Yes, already asked | The content-class arm is the owner's choice, already P-111 Q2. Nothing to repair. |

Next step, if the owner or the lead directs it: one repair of items 1–5
and a round 3. Until then the round-1 repair stays unconfirmed.
