> **Candidate — binds nothing.** Classification of review round 4. A
> disposition performs no act, and this one repairs nothing.

# Round 4 dispositions — DOSSIER-CLI-RUNNER-1

Raw: `docs/reviews/R-DOSSIER-CLI-SUBPROCESS-4-RAW.md`, verdict `REVISE`
(line 4), over commit `7a6ef22cf9e619f6330d01c78dc5716a3030683b`. Round-3
closure: 2 closed, 1 not closed (partly repaired) and 1 carried to the owner
(raw line 104). New findings: one revise and four notes (raw line 104).

The lead set the final-cycle rule: a `REVISE` in round 4 is classified,
nothing is repaired, and it goes to the owner with no round 5. So
`SEMANTIC-DELTA.md` stays as reviewed. It is **not cleared** and **not
offered for sign-off**, and register row P-111 says so.

The reviewer's own judgement (raw lines 97–102) is that the removed
credential-variable machinery leaves no residue. Apart from finding 1, every
transmission stays inside an act in force, and the requirement fails closed
on every arm it states. Finding 1 is a defect of form: the intent is
unambiguous, but no route is reopened.

| # | Class | Needs an owner choice? | Classification |
|---|---|---|---|
| 1 | revise | No (one-word drafter repair) | The round-3 repair removed the clause that carried "SHALL" for the bar on provider-selecting options. Paragraph 1 now says "Every provider-selecting option ... either absent or set by Syzygy to the declared provider" with no verb. Repair: insert "SHALL be". |
| 2 | note | No | Paragraph 1's credential exception does not yet name the managed-settings inspection that the oracle and the Falsifier allow. Repair: add the read-only inspection to that exception, or match authenticating keys by name and presence only. |
| 3 | note | No | Managed settings carrying an authenticating key for the *declared* provider are not refused, so "authenticates only through its own credential file" overstates. Repair: treat any managed authenticating key as a mismatch. The drafter recommends this, because it matches paragraph 1's rule that only the credential file may authenticate. |
| 4 | note | No | The authentication refusal says nothing about when it runs and has no test. Repair: add "before any session starts", a Case with a missing credential file, and the Falsifier clause. |
| 5 | note | Yes, already asked | The content-class arm is P-111 Q2. Nothing to repair. |

Items 1–4 need no choice from the owner. The owner can direct one more
repair of items 1–4 (finding 1 is one word), sign as is, or decline.
