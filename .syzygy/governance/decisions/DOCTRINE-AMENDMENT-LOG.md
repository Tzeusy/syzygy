# Doctrine amendment log

Every amendment to adopted doctrine (`../doctrine/`), one row each. Doctrine
itself carries only current text; this log carries its history. Identifiers
are never reused.

| Id | Date | What changed | Authority |
|---|---|---|---|
| D1 | 2026-08-01 | `architecture.md`, two sites (layout comment; `map/` definition bullet): the map's scope now reads "observed, intended, proposed, and historical system state" — historical rendering added unconditionally. | Owner decision D1, ratifying the packet at `../decisions/DOCTRINE-AMENDMENT-D1-MAP-HISTORICAL.md` (extracted under FD-037; original authored in the bootstrap record); scope made unconditional by rev7 rework directive item A2 (not owner decision A2). *FD-n identifiers and the rev7 directive live in the founder-local bootstrap log, which is not in the clone — a known reachability gap, queued as P-15; the ruling itself is fully stated here* |
| D5 | *on adoption* | All six doctrine files rewritten for readability: rules, definitions, and scope restated in plainer structure (lists, a success-test table) with every identifier, rule title, VIS-1 rank, VIS-6 exception letter, trust-floor bullet order, and cited section title kept. Folds in P-25(a) (glossary citations name their file) and P-25(c) (glossary defines *actuator*). The amendment log moved here from the doctrine README | Owner adoption of [`DOCTRINE-AMENDMENT-D5-READABILITY.md`](DOCTRINE-AMENDMENT-D5-READABILITY.md) |
