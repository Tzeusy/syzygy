# Launch-gate trend log

One appended line per administration (instrument §6); this is F1's
evidence. **Administration 1 was run 2026-08-18** (out-of-family, v2.4,
commit `71e5986`): `NOT READY`. The record is
`ADMINISTRATION-2026-08-18-CAPABILITY-1.json` (this directory); the
Markdown beside it is generated, never parsed back.

**Why the 2026-08-09 pilot does not open this log** (project-specific
record, moved here from instrument §6 at v1.6 so §6 stays
project-invariant). The pilot administration (v1.3, commit `067d8a0`) is
steering evidence, not the formal trend baseline: its findings stand and
its record is immutable, but it does not open the formal trend because
(1) the instrument was not committed at the administered commit; (2) no
instrument digest was recorded; (3) no parameter-block digest was
recorded; (4) the reviewer was from the same model family that authored
the corpus. The formal trend begins with the first administration meeting
the instrument's §2 integrity requirements ("Administration 1").

| Date | Commit | Not-met | Scoped | Unknown | Deferred | Reopened | New findings vs prior | Gate verdict |
|------|--------|---------|--------|---------|----------|----------|----------------------|--------------|
| 2026-08-18 | 71e5986 | 10 | 2 | 5 | 0 | 0 | n/a (no prior record) | NOT READY |
