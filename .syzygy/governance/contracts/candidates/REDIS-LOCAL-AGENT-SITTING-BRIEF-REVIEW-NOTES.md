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

## Lead's notes, added 2026-10-07 after the bytes cleared

These two are not from the review. The lead added them as dispositions
within the notes-only rule. They correct facts and change no
recommendation.

### Note 4 — G and H wait on PR #377

[Observed] On main, `packages/polaris-dossier/src/gate-sources.ts` has
`D9_ACT_FORM` and `RFC7_20_RULING_ACT_FORM` set to null. G and H take
effect at the gate only after #377 (`syzygy-qkea.21`) merges, and the
sitting is not put until then.

### Note 5 — the P-95 re-derivation bead is `syzygy-fxro`

Under B, the brief's "Tracking" line names `syzygy-qggu`. That bead was
closed as a duplicate of `syzygy-fxro` (P1, open). Its scope was widened
to cover the tree-framing package as one unit, both acts' review binding,
and direction C's policy-role wording. Read `syzygy-fxro` wherever the
brief says `syzygy-qggu`.

### Note 6 — no decisions file may name a recorded act it is not the record of

*(Added 2026-10-07, `syzygy-s6xo`.)* [Observed] Every gate reader refuses
an act that a file under `decisions/` names without being its record. It
reads such a file as a withdrawal, or as a form it does not define. Its
needles are the act and identity stems, the statement record IDs and
subject tuples, the sitting records' paths, and the entry sign-off's stems,
tag and installed path. Each matches case-, underscore- and space-folded.
`ACCEPTANCE-ACT-RECORD.md` is exempt except on its identity, record and
subject field lines. So a sitting log, or a P-104 row edit, that names one
of these refuses the act it describes, and the next run reads it as
withdrawn. The P-104 row must also keep its `| P-104 |` prefix.

Citing a record by its path does not avoid this. Each dedicated record's
filename carries its act stem (`DOSSIER-LOCAL-AGENT-<stem>-ACT.md`), and the
sitting records' paths are needles themselves. A sitting log should name
the acts by this brief's item letters (A to I) and point to
`ACCEPTANCE-ACT-RECORD.md` for the rest. Step 10's installer now runs the gate
package's real-tree tests after installing, and its `--check` runs them
again (`GATE_TESTS`). Re-run `--check` after writing any sitting log and
before committing. The step adds no step order to the brief.

The sitting resolves P-104 [Observed: its rows 1 to 5 are this brief's
acts A, E, F, G and H], so its row is resolved in place, in the form P-53
took (`| P-104 | [Observed] **Resolved <date>:** …`), naming the acts by
item letter. It is never moved to `DECISION-HISTORY.md`, where the registry
gate refuses it. The installer writes that row from the answers, and refuses
to overwrite a row in any other form. Before installing and in `--check`, it
refuses unless the register carries exactly one P-104 row and the history
none. Its gate sweep proves the new row names no swept stem. It never
re-pins the gate's P-104 exemption, which then matches no line; removing it
is `syzygy-kgv5`.
