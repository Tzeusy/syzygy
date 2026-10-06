# Redis local-agent sitting brief — round-3 review notes

> **Candidate — binds nothing.** This is the sibling record for the notes of
> the sitting brief's third fresh-context review,
> `docs/reviews/R-REDIS-LOCAL-AGENT-SITTING-BRIEF-3-RAW.md` (verdict
> `CONFIRM WITH EXCEPTIONS` over commit `6568ed95`, no revise-level finding,
> three notes). Under the owner's notes-only rule
> (`../../decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md` §1), that
> round clears the exact bytes it read, and its notes go here, never into
> the reviewed bytes. So `REDIS-LOCAL-AGENT-SITTING-BRIEF.md` is not edited
> for them; any edit to it would retire the review (rule 10). This record
> adopts, signs and performs nothing (VIS-4). The brief binds no act
> digest, so nothing here is registered in `check_governance.py`.

Read these three corrections beside the brief when the sitting is put.

## Note 1 — what refuses the run, and how far

The brief's paragraph "What declining does to the sitting" cites the
installer's `REQUIRED` tuple for every refusal it lists. The clauses are
three, all in `validate_answers` of
`scripts/install_redis_local_agent_sitting.py`:

- `REQUIRED` holds A, B, E, H and I;
- `DRAWER_OR_PROVIDER` and the check after it require one of F's options;
- "screening-v2 needs rfc5" refuses D without C.

Each is one more reason in the same list, so **signing D while declining C
refuses the whole run, exactly as declining A does**; it does not fail D
alone.

[Inferred] Steps 3 to 9 of "After the sitting" show each recorder's own
command. They are there to name what step 10 runs, not as a route around
it: run by hand, they would leave out step 10's registrations and battery
lines, and the rehearsal (`docs/evidence/redis-local-agent-sitting-rehearsal-2026-10-07.json`)
covered only the installer path. If any required answer is held, the
sitting records nothing; the acts wait for a later sitting or a changed
installer.

## Note 2 — E is a quote, not an option

Under E, "let the option you select name your reading" should read **"let
your quoted selection name your reading"**. E has no label field: the
installer passes it as one quoted line and the recorder writes it verbatim
after "Owner selection:". The act is unaffected.

## Note 3 — a dependency sentence under E is spent and was false

Under E, "If PR #367 has not merged by the sitting, this row waits; nothing
else in this brief depends on its timing except step 7 below." Its
condition is spent, since PR #367 has merged. It was also false under the
installer as merged: the installer requires an E answer, so **every act at
the sitting waited on PR #367**, not only step 7. *(Marked here 2026-10-07,
since the brief's bytes are cleared and not edited.)*
