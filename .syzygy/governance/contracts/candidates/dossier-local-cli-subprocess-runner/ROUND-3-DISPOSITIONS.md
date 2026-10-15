> **Candidate — binds nothing.** Classification of review round 3. A
> disposition performs no act, and this one repairs nothing.

# Round 3 dispositions — DOSSIER-CLI-RUNNER-1

Raw: `docs/reviews/R-DOSSIER-CLI-SUBPROCESS-3-RAW.md`, verdict `REVISE`
(line 4), over commit `d0f776d8e584fa188674fa7f47053253027c776b`. Round-2
closure: 5 closed and 1 carried to the owner (finding 6), with none left
open (raw line 91). New findings: one revise and three notes (raw line 91).

The lead set the cycle-3 rule: a `REVISE` is classified, nothing is
repaired, and the drafting lane stops. So `SEMANTIC-DELTA.md` stays as
reviewed. It is **not cleared** and **not offered for sign-off**, and
register row P-111 says so.

| # | Class | Needs an owner choice? | Classification |
|---|---|---|---|
| 1 | revise | No (drafter repair) | This comes from the round-2 note-2 repair. The declared-credential-variable exception takes whatever name the operator gives, and nothing checks that the variable only authenticates. A base-URL or provider-switch variable declared as "the credential variable" would therefore reach the tool, while the page reads as covered. The raw's repair is to admit the declared name only from a closed list, kept per tool and provider and recorded as Observed for the version, and to refuse the run otherwise, with a Case to test it. The simpler alternative is the disposition's original round-2 wording: admit no credential variable at all, leaving only the tool's own login. The drafter recommends that alternative, because it removes the input rather than adding a list to maintain. |
| 2 | note | No | The managed-settings read is a third credential-adjacent use, but the oracle and the Falsifier except only two. Name it as a third exception, by key name only. |
| 3 | note | No | The Falsifier and the Case lack the third managed-settings refusal arm, which covers keys not known for the version. Add it to both. The raw's Unknown about managed settings stored somewhere other than a file can be covered by the same arm. |
| 4 | note | Yes, already asked | The content-class arm is P-111 Q2. Nothing to repair. |

Next step, only if the owner or the lead directs it: one repair of items 1–3,
followed by a round 4. Until then the round-2 repair stays unconfirmed.
