import { escapeHtml, type Route } from '@syzygy/cap1-daemon';
import {
  ARTIFACT_PATHS,
  buildMaterializationPacket,
  clearMaterializationRecordFile,
  materializeWorkItem,
  readMaterializationRecordFile,
  writeMaterializationRecordFile,
  type MaterializationPacket,
  type MaterializeResult,
  type PocModel,
} from '@syzygy/three-surface-poc-core';

import { browserRequestAllowed } from './browser-origin.js';
import { mountPrefixForRequest, TAILNET_MOUNT_PREFIX, withMountPrefix } from './tailnet.js';

export const MATERIALIZE_HUMAN_PATH = '/trajectory/materialize' as const;
export const MATERIALIZE_TAILNET_PATH = `${TAILNET_MOUNT_PREFIX}/trajectory/materialize` as const;

// Kept as a local literal, not imported from `trajectory.ts`, to avoid a
// cycle (`trajectory.ts` imports `renderMaterializePanel` from this file).
const TRAJECTORY_BACK_PATH = '/trajectory' as const;

// Identifies the mechanism in Butlers' own audit trail (`bd`'s
// `--actor`), distinct from the machine's real account (which `bd`
// still records separately as `owner`). Fixed, never user-supplied —
// this action is human-triggered but not human-identified.
export const MATERIALIZE_ATTRIBUTION =
  'syzygy-three-surface-poc:human-triggered-materialize-action' as const;

export function buildTrajectoryMaterializationPacket(model: PocModel): MaterializationPacket {
  return buildMaterializationPacket({
    targetRepoRoot: model.project.root,
    proposalPath: ARTIFACT_PATHS.proposal,
    designPath: ARTIFACT_PATHS.design,
  });
}

export function currentMaterializedBeadId(model: PocModel): string | null {
  return model.materializedBeadId;
}

export const MATERIALIZE_PANEL_STYLE = `
  .materialize-panel { background: linear-gradient(145deg, #102126, var(--panel)); border: 1px solid var(--line); padding: 1.2rem 1.4rem; margin: 0 0 2rem; display: grid; gap: .8rem; }
  .materialize-panel h2 { font-size: 1.1rem; margin: 0; }
  .materialize-panel dl { display: grid; grid-template-columns: max-content 1fr; gap: .2rem 1rem; margin: 0; font-size: .82rem; }
  .materialize-panel dt { color: var(--muted); }
  .materialize-panel dd { margin: 0; overflow-wrap: anywhere; }
  .materialize-status { font-size: .85rem; }
  .materialize-panel button { font: inherit; background: var(--cyan); color: #06171a; border: none; padding: .55rem 1rem; cursor: pointer; }
  .materialize-panel button:hover, .materialize-panel button:focus-visible { filter: brightness(1.1); }
`;

/** Preview panel — read-only, embedded on the Trajectory page (AC1). */
export function renderMaterializePanel(model: PocModel, mountPrefix = ''): string {
  const packet = buildTrajectoryMaterializationPacket(model);
  const beadId = currentMaterializedBeadId(model);

  const status =
    beadId === null
      ? `<p class="materialize-status" data-parity-field="materialize-status">Not yet materialized.</p>`
      : `<p class="materialize-status" data-parity-field="materialize-status">Already materialized as <code>${escapeHtml(beadId)}</code>. Triggering again is idempotent — it will reuse this same Bead.</p>`;

  return `
    <section class="materialize-panel" aria-label="Materialize planned work" data-materialize-panel>
      <h2>Materialize this work item</h2>
      <p class="notice">Preview of the exact Bead this human-triggered action would create. Nothing is written until the button below is explicitly clicked; Syzygy never triggers this on its own.</p>
      <dl>
        <dt>Target repository</dt><dd data-parity-field="materialize-target-repo">${escapeHtml(packet.targetRepoRoot)}</dd>
        <dt>Governing intent</dt><dd data-parity-field="materialize-governing-intent">${escapeHtml(packet.governingIntent.requirementId)} (${escapeHtml(packet.governingIntent.proposalPath)})</dd>
        <dt>Title</dt><dd data-parity-field="materialize-title">${escapeHtml(packet.title)}</dd>
        <dt>Description</dt><dd data-parity-field="materialize-description">${escapeHtml(packet.description)}</dd>
        <dt>Labels</dt><dd data-parity-field="materialize-labels">${escapeHtml(packet.labels.join(', '))}</dd>
        <dt>Type / priority</dt><dd data-parity-field="materialize-type-priority">${escapeHtml(packet.issueType)} / P${escapeHtml(String(packet.priority))}</dd>
        <dt>External reference</dt><dd data-parity-field="materialize-external-ref"><code>${escapeHtml(packet.externalRef)}</code></dd>
      </dl>
      ${status}
      <form method="POST" action="${escapeHtml(withMountPrefix(mountPrefix, MATERIALIZE_HUMAN_PATH))}">
        <button type="submit" data-parity-field="materialize-trigger">${beadId === null ? 'Materialize this work item' : 'Re-run materialize (idempotent)'}</button>
      </form>
    </section>`;
}

function resultPage(input: { readonly heading: string; readonly body: string; readonly mountPrefix: string }): string {
  const backHref = withMountPrefix(input.mountPrefix, TRAJECTORY_BACK_PATH);
  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Materialize · Syzygy three-surface POC</title>
  <style>${MATERIALIZE_PANEL_STYLE}</style>
</head>
<body style="font-family: system-ui, sans-serif; background: #06171a; color: #e7f3f2; padding: 2rem; max-width: 60ch; margin: 0 auto;">
  <h1>${escapeHtml(input.heading)}</h1>
  ${input.body}
  <p><a href="${escapeHtml(backHref)}" data-parity-field="materialize-back-link">Back to Trajectory</a></p>
</body>
</html>`;
}

export interface MaterializeRoutesOptions {
  readonly getModel: () => PocModel;
  readonly targetRepoRoot: string;
  readonly stateDir: () => string;
  readonly onMaterialized: () => void;
  /** Test-only seams; production always uses `materializeWorkItem`'s real
   * `bd` runners. */
  readonly runQuery?: (repoRoot: string, sql: string) => string;
  readonly runCreate?: (
    repoRoot: string,
    packet: MaterializationPacket,
    attribution: string,
  ) => string;
}

function runMaterialize(options: MaterializeRoutesOptions): MaterializeResult {
  const packet = buildTrajectoryMaterializationPacket(options.getModel());
  const dir = options.stateDir();
  return materializeWorkItem({
    targetRepoRoot: options.targetRepoRoot,
    packet,
    attribution: MATERIALIZE_ATTRIBUTION,
    now: () => new Date().toISOString(),
    readRecord: () => readMaterializationRecordFile(dir),
    writeRecord: (record) => writeMaterializationRecordFile(dir, record),
    ...(options.runQuery === undefined ? {} : { runQuery: options.runQuery }),
    ...(options.runCreate === undefined ? {} : { runCreate: options.runCreate }),
  });
}

/** The one narrow human-triggered action: POST-only, human-open, and
 * guarded by the same same-origin check every human route uses. */
export function materializeRoutes(options: MaterializeRoutesOptions): readonly Route[] {
  const handle: Route['handle'] = async ({ request }) => {
    if (!browserRequestAllowed(request.headers)) {
      return {
        status: 403,
        contentType: 'application/json',
        body: JSON.stringify({ served: 'nothing', reason: 'browser-origin-refused' }),
      };
    }

    const mountPrefix = mountPrefixForRequest(request.headers);
    const result = runMaterialize(options);
    if (result.kind === 'unknown') {
      const suffix =
        result.beadId === undefined
          ? 'No Bead was left in a partially-created state; the local record was not written.'
          : `Bead <code>${escapeHtml(result.beadId)}</code> exists in the configured Butlers repository, but the local record of it could not be written; a retry will reconcile via that existing Bead rather than creating a duplicate.`;
      return {
        status: 502,
        contentType: 'text/html; charset=utf-8',
        body: resultPage({
          heading: 'Materialization did not complete',
          body: `<p>Unknown — ${escapeHtml(result.reason)}. ${suffix}</p>`,
          mountPrefix,
        }),
      };
    }

    options.onMaterialized();
    const verb = result.kind === 'created' ? 'Created' : 'Reused';
    return {
      status: 200,
      contentType: 'text/html; charset=utf-8',
      body: resultPage({
        heading: `${verb} Beads item ${result.beadId}`,
        body: `<p data-parity-field="materialize-result-bead-id">${verb} <code>${escapeHtml(result.beadId)}</code> in the configured Butlers repository. Trajectory now shows it as planned.</p>`,
        mountPrefix,
      }),
    };
  };

  return [
    { method: 'POST', path: MATERIALIZE_HUMAN_PATH, credentialClass: 'human-open', handle },
    { method: 'POST', path: MATERIALIZE_TAILNET_PATH, credentialClass: 'human-open', handle },
  ];
}
