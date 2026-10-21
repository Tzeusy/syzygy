// Surface-route capture over fixtures. Usage:
//   node route-capture.mjs <tree> <out.json>
// For one built tree, serve the app's route set (pocRoutes, materializeRoutes,
// reobserveRoutes: the three groups apps/three-surface-poc/src/main.ts
// registers) on a private daemon (--port 0, scratch state dir) over several
// fixture models, request every registered route in its direct and tailnet
// forms (Host: the tailnet host), and record status, content type, length and
// sha256 of the body. Credentialed routes are requested with the machine
// bearer token and, separately, without it. Only scratch paths are masked.
// No target repository is read: every model comes from the app's own
// fixtures (test-model-fixture, test-project-shape-fixture).
import * as http from 'node:http';
import { createHash } from 'node:crypto';
import { mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import * as path from 'node:path';
import { pathToFileURL } from 'node:url';

const tree = path.resolve(process.argv[2]);
const outFile = path.resolve(process.argv[3]);
// A fixed fixture repository path: the evaluation inputs digest includes the
// repository root, so two captures are comparable only over the same path.
const fixedRepo = path.resolve(process.argv[4]);
const imp = (rel) => import(pathToFileURL(path.join(tree, rel)).href);

const { createDaemon } = await imp('packages/cap1-daemon/dist/index.js');
const { pocRoutes } = await imp('apps/three-surface-poc/dist/routes.js');
const { materializeRoutes } = await imp('apps/three-surface-poc/dist/materialize-action.js');
const { reobserveRoutes } = await imp('apps/three-surface-poc/dist/reobserve-action.js');
const { buildFixtureModel } = await imp('apps/three-surface-poc/dist/test-model-fixture.js');
const shapeFixture = await imp('apps/three-surface-poc/dist/test-project-shape-fixture.js');
const { TAILNET_HOST } = await imp('apps/three-surface-poc/dist/browser-origin.js');

import { cpSync, existsSync } from 'node:fs';
const { fixtureRepoWithGit } = await imp('apps/three-surface-poc/dist/test-model-fixture.js');
let fixtureRepo;
if (existsSync(fixedRepo)) {
  fixtureRepo = JSON.parse(readFileSync(fixedRepo + '.json', 'utf8'));
} else {
  const made = fixtureRepoWithGit([]);
  cpSync(made.repoRoot, fixedRepo, { recursive: true });
  fixtureRepo = { repoRoot: fixedRepo, revision: made.revision };
  writeFileSync(fixedRepo + '.json', JSON.stringify(fixtureRepo));
}
const scratch = mkdtempSync(path.join(tmpdir(), 'zz-route-capture-'));
const cleanups = [];

const VARIANTS = {
  'shape-not-evaluated': () => buildFixtureModel(cleanups, { fixtureRepo }),
  'shape-admitted': () => buildFixtureModel(cleanups, { fixtureRepo, projectShape: { authority: shapeFixture.ADMITTING_AUTHORITY, runGit: shapeFixture.projectShapeFixtureGit() } }),
  'shape-rejected': () => buildFixtureModel(cleanups, { fixtureRepo, projectShape: { authority: shapeFixture.REJECTING_AUTHORITY, runGit: shapeFixture.projectShapeFixtureGit() } }),
  'shape-with-secret': () => buildFixtureModel(cleanups, { fixtureRepo, projectShape: { authority: shapeFixture.ADMITTING_AUTHORITY, runGit: shapeFixture.projectShapeFixtureGit(shapeFixture.PROJECT_SHAPE_FIXTURE_TEXTS_WITH_SECRET) } }),
  'shape-with-baseline-spec': () => buildFixtureModel(cleanups, { fixtureRepo, projectShape: { authority: shapeFixture.ADMITTING_AUTHORITY, runGit: shapeFixture.projectShapeFixtureGit(shapeFixture.PROJECT_SHAPE_FIXTURE_TEXTS_WITH_BASELINE_SPEC) } }),
};

function request(port, method, urlPath, host, token) {
  return new Promise((resolve, reject) => {
    const headers = { Host: host };
    if (token !== undefined) headers.Authorization = `Bearer ${token}`;
    const req = http.request({ hostname: '127.0.0.1', port, path: urlPath, method, headers }, (res) => {
      const chunks = [];
      res.on('data', (chunk) => chunks.push(chunk));
      res.on('end', () => resolve({ status: res.statusCode ?? 0, contentType: res.headers['content-type'] ?? null, body: Buffer.concat(chunks) }));
    });
    req.on('error', reject);
    req.end();
  });
}

function mask(text) {
  return text
    .replaceAll(scratch, '<SCRATCH>')
    .replaceAll(fixedRepo, '<FIXTURE-REPO>')
    .replace(/127\.0\.0\.1:\d+/g, '127.0.0.1:<PORT>');
}

const result = {};
let responses = 0;
for (const [variant, build] of Object.entries(VARIANTS)) {
  const model = build();
  const stateDir = path.join(scratch, variant, 'state');
  mkdirSync(stateDir, { recursive: true });
  const routes = [
    ...pocRoutes(() => model),
    ...materializeRoutes({ getModel: () => model, targetRepoRoot: path.join(scratch, variant, 'target'), stateDir: () => stateDir, onMaterialized: () => undefined }),
    ...reobserveRoutes({ reobserve: async () => ({ kind: 'failed', reason: 'zz-capture-no-reobserve' }) }),
  ];
  const start = await createDaemon({ stateDir, port: 0, routes });
  if (!start.started) throw new Error(`daemon did not start for ${variant}: ${JSON.stringify(start.failure)}`);
  const daemon = start.daemon;
  const token = readFileSync(daemon.credentialPath, 'utf8').trim();
  const record = { routeCount: routes.length, routes: {} };
  for (const route of routes) {
    for (const form of ['direct', 'tailnet']) {
      const host = form === 'tailnet' ? TAILNET_HOST : `127.0.0.1:${daemon.port}`;
      const modes = route.credentialClass === 'machine-credentialed' ? ['bearer', 'anonymous'] : ['anonymous'];
      for (const mode of modes) {
        // Only side-effect-free requests are made with a credential: a
        // credentialed POST would write state (materialize) or re-observe.
        if (route.method !== 'GET' && route.method !== 'HEAD' && mode === 'bearer') continue;
        const response = await request(daemon.port, route.method, route.path, host, mode === 'bearer' ? token : undefined);
        const body = Buffer.from(mask(response.body.toString('utf8')), 'utf8');
        record.routes[`${form} ${mode} ${route.method} ${route.path}`] = {
          status: response.status,
          contentType: response.contentType,
          bodyLength: body.length,
          bodySha256: createHash('sha256').update(body).digest('hex'),
        };
        responses += 1;
      }
    }
  }
  await daemon.close();
  result[variant] = record;
}

for (const dir of cleanups) rmSync(dir, { recursive: true, force: true });
rmSync(scratch, { recursive: true, force: true });
writeFileSync(outFile, JSON.stringify(result, null, 1) + '\n', 'utf8');
console.log(`variants=${Object.keys(result).length} routesPerVariant=${Object.values(result).map((r) => r.routeCount).join(',')} responses=${responses} out=${outFile}`);
