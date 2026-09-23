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

## Restart one local POC listener

For a POC started from this checkout with an explicit, nonzero `--port` and
`--state-dir`, run from the same Syzygy checkout:

```sh
npm run poc:restart -- --port <that-poc-port>
```

The command finds exactly one listener on `127.0.0.1` at that port, verifies
that its process is this checkout's built POC with the original repository,
state directory, port and arguments, and checks the same process generation
again before signaling. It sends one SIGTERM, waits for the socket to close,
then starts one successor with the identical arguments and state directory.
This local operator command requires Linux `ss` and `/proc` process metadata.
It verifies the successor and unchanged credential bytes. It does not use
SIGKILL, a pidfile, an automatic retry, or a Butlers write. Use
`--timeout-ms <100..30000>` for a bounded wait other than the 10-second default.

An absent, multiple, changed or unidentifiable listener, a timeout, a failed
successor, or a simultaneous restart attempt is a refusal. The state directory
is preserved; inspect the named failure before a further attempt. A stale
restart lock in the OS temporary directory is intentionally fail-closed and
requires operator inspection before removal. The system tests exercise only
private fixture listeners and disposable state directories.
An unreadable identity before SIGTERM is refused. After SIGTERM, a brief loss
of process identity while the old socket closes is treated as unknown ownership:
the command waits for verified socket absence or the bounded timeout, never
starts the successor merely because the identity could not be read.

Each non-2xx daemon response writes one structured JSONL diagnostic to local
stderr. The line contains only its status, registered route or unmatched path
length, closed reason and safe response-limit fields; it never includes a
credential, request content or handler exception text. Human pages expose a
compact evaluation and breach line below the header. It is an execution
disclosure, not a health verdict or a new machine status route.

## Evidence and re-observation

Each evaluation carries an additive evidence block on the authenticated
machine responses: the pinned revision and committer instant, the observation
instant, and a currency probe comparing the pinned revision with the current
Git head. Currency bounds remain empty until their separately gated owner act.
The Polaris opening band presents the same probe identity and changed/added
counts; the probe is a disclosure, not a project claim or freshness value.

The daemon does not poll or advance its observation from the wall clock. To
capture a new identified evaluation, POST to `/polaris/reobserve` from the
same-origin human surface (or its tailnet-mounted path). Concurrent requests
single-flight; a failed re-observation leaves the prior complete model served.

## First-slice walkthrough

The three surface headers identify distinct planes: Polaris presents desired
state, Trajectory execution state, and Orrery observed state. The home panels
and each page's separate surface-state legend derive those names from the
shared model. They are not Observed/Unknown evidence labels or a claim that
work completion verifies intent.

Cross-surface links connect the two Polaris region counts, its nine
reality-band entities, Trajectory's governing-intent preview, and Orrery's
mapped capability to their existing human targets. The Orrery spatial block
keeps its exact-table link as well. Links use native anchors and the current
direct or tailnet mount; if the same evaluation lacks a target, the renderer
shows an unavailable disclosure without an href. The served-page test checks
the complete 13-link fixture population and fetches every target in both
forms, including the Orrery link created after its local script runs.

1. Open the printed human URL. Polaris shows the purpose and governing intent
   for WhatsApp transport identity normalization.
2. Confirm the live-runtime relationship is visibly Unknown. Repository state
   is not deployment evidence.
3. In Trajectory, review the materialize panel's preview of the exact Bead a
   human-triggered action would create, then optionally click "Materialize
   this work item" (or, if already materialized, "Re-run materialize
   (idempotent)") to actually create — or, on a repeat run, reuse — that Bead
   in the configured Butlers repository. This is the one state-changing,
   human-only action in the POC; Syzygy never triggers it on its own.
4. After materializing, Trajectory's board shows the worker-change observer's
   state for that item ("External worker: Planned / Active / Changed /
   merged", tracking real git activity against it) alongside its independent
   Bead status — these are two separately honest fields, not one. A
   captured, verified test-run artifact (see below) additionally renders a
   "Verification: Verified — …" badge once a real, matching JUnit artifact
   has been ingested for the governing seam; absent that, it stays
   "Verification: Not verified".
5. Test-run evidence is not captured automatically. Run
   `npm run poc:capture-test-artifact -- --repo <butlers> --scope <path>
   --state-dir <dir>` separately (see "Capturing test-run evidence" below) to
   ingest a real JUnit artifact; Trajectory and the machine endpoint then
   reflect it.
6. In Orrery, follow the selected capability to its intent, manually mapped
   code region, and test definition. The rest of Butlers code remains visible
   as an Unknown region. Orrery's spatial city view is the one surface with
   real client-side rendering (an inline, self-served script, no build step
   or CDN); without JavaScript it falls back to the same facts in exact
   tables.
7. Query authenticated `GET /api/poc` using the credential at the printed path.
   The JSON entity and relationship facts are the same objects rendered by the
   human page.

## Capturing test-run evidence

Test-run capture is a separate, manually invoked step — the running daemon
never shells the observed test suite itself:

```sh
npm run poc:capture-test-artifact -- \
  --repo /home/tze/GitHub/butlers \
  --scope <path-under-test> \
  --state-dir <dir> [--python <bin>]
```

This runs the real focused pytest suite against the configured Butlers
checkout, ingests the resulting JUnit artifact (command, exit status, capture
time, commit, scope, digest, and a safe summary only — never raw test output),
and verification renders `Verified` only when the captured commit exactly
matches the git-observed worker-change commit for the same seam, the exit
code is 0, and the capture time is neither future-dated nor earlier than the
commit itself. This evidence is scoped to the worker-change seam
(`whatsapp_user_client.py`) — a different code path than the identity
normalization capability Polaris and Orrery describe.

## Deliberately absent in this slice

- No worker is dispatched and no implementation code is changed by Syzygy.
- No deployment or live-runtime observation is supplied.
- No broad code inventory or generalized spatial layout is computed — Orrery's
  city view is deterministic over observed structure and declared mappings
  only, and unmapped code stays visibly Unknown.
- Test-run capture is a separate, manually invoked step, never automatic.

Those absences are product facts, not setup failures. They remain Unknown until
a later bounded POC item produces the corresponding authoritative record.
