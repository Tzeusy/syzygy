# Three-Surface POC

This is a local, non-release product experiment against one explicit Butlers
checkout. It does not adopt intent, write implementation code, execute Butlers
code, deploy anything, or claim conformance.

## Start from a fresh Syzygy checkout

Run this one command from the Syzygy repository root:

```sh
npm ci && npm run poc -- --repo /home/tze/GitHub/butlers
```

The command builds the bounded POC, binds only to `127.0.0.1`, and prints the
human URL, authenticated machine endpoint, observed Butlers revision, and the
machine credential file's location. It never prints the credential value.

Use `--port 0` for an ephemeral port or `--state-dir <path>` for an explicit
local credential directory.

## First-slice walkthrough

1. Open the printed human URL. Polaris shows the purpose and governing intent
   for WhatsApp transport identity normalization.
2. Confirm the live-runtime relationship is visibly Unknown. Repository state
   is not deployment evidence.
3. In Trajectory, confirm work materialization and captured test evidence are
   Unknown. A test definition is not a test run.
4. In Orrery, follow the selected capability to its intent, manually mapped
   code region, and test definition. The rest of Butlers code remains visible
   as an Unknown region.
5. Query authenticated `GET /api/poc` using the credential at the printed path.
   The JSON entity and relationship facts are the same objects rendered by the
   human page.

## Deliberately absent in this slice

- No Beads item is materialized yet.
- No worker is dispatched and no implementation code is changed.
- No test-run artifact is captured or ingested.
- No deployment or live-runtime observation is supplied.
- No broad code inventory or generalized spatial layout is computed.

Those absences are product facts, not setup failures. They remain Unknown until
the later bounded POC items produce the corresponding authoritative records.
