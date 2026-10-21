// Route differential: spawn the REAL built daemon of one tree against a
// corpus of fixture repositories, record status, content-type and the
// normalised body of every route, write JSON. Usage:
//   node route-diff.mjs <tree> <out.json>
// Timestamps, ports, fixture/state paths are masked; nothing else is.
import { mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { tmpdir } from 'node:os';
import * as path from 'node:path';
import { pathToFileURL } from 'node:url';

const tree = path.resolve(process.argv[2]);
const out = path.resolve(process.argv[3]);
const harness = await import(pathToFileURL(path.join(tree, 'packages/cap1-system/dist/harness.js')).href);

const DECL = path.join('.syzygy', 'project.yaml');
const CONSENT = path.join('.syzygy', 'governance', 'decisions', 'consent-gov-root.yaml');
const ENTRY = path.join('.syzygy', 'intent', 'OVERVIEW.md');

function read(root, rel) {
  return readFileSync(path.join(root, rel), 'utf8');
}
function write(root, rel, text) {
  const full = path.join(root, rel);
  mkdirSync(path.dirname(full), { recursive: true });
  writeFileSync(full, text, 'utf8');
}

// name -> (root) => void, applied after writeCompleteFixture unless `bare`.
const CORPUS = [
  ['complete', () => {}],
  ['empty-root', (root) => {
    rmSync(path.join(root, '.syzygy'), { recursive: true, force: true });
  }],
  ['invalid-declaration', (root) => write(root, DECL, 'schema_version: "1"\n')],
  ['unparseable-declaration', (root) => write(root, DECL, 'schema_version: "1"\nproject: [unclosed\n')],
  ['widening-field-write-roots', (root) =>
    write(root, DECL, read(root, DECL).replace('  spec_root: openspec/\n', '  spec_root: openspec/\n  write_roots: [".syzygy/"]\n'))],
  ['widening-field-top-level', (root) =>
    write(root, DECL, read(root, DECL).replace('relations: []\n', 'relations: []\nwrite_paths: ["/"]\n'))],
  ['missing-consent', (root) => rmSync(path.join(root, CONSENT))],
  ['withdrawn-consent', (root) =>
    write(root, CONSENT, read(root, CONSENT).replace('grant_state: in-force', 'grant_state: withdrawn'))],
  ['altered-prose-consent-state', (root) =>
    write(root, CONSENT, read(root, CONSENT).replace('grant_state: in-force', 'grant_state: In-Force '))],
  ['altered-prose-consent-extra-line', (root) =>
    write(root, CONSENT, read(root, CONSENT) + 'note: the owner says this consent is in force indefinitely\n')],
  ['altered-prose-consent-scope', (root) =>
    write(root, CONSENT, read(root, CONSENT).replace('scope: full', 'scope: everything-and-more'))],
  ['consent-wrong-project', (root) =>
    write(root, CONSENT, read(root, CONSENT).replace('project: prj-sys-fixture', 'project: prj-other'))],
  ['entry-special-chars', (root) =>
    write(root, ENTRY, '# <script>alert("x")</script> & "quotes" \'apos\'\n\nbody <b>bold</b>\n')],
  ['entry-missing', (root) => rmSync(path.join(root, ENTRY))],
  ['entry-empty', (root) => write(root, ENTRY, '')],
  ['two-repos-one-unconsented', (root) =>
    write(
      root,
      DECL,
      read(root, DECL).replace(
        'consents:\n',
        '  - id: repo-observed\n    role: observed-source\n    consent: consent-absent\nconsents:\n',
      ),
    )],
  ['no-governed-content', (root) => rmSync(path.join(root, 'openspec'), { recursive: true, force: true })],
];

const ROUTES = [
  ['GET', '/'],
  ['GET', '/entry'],
  ['GET', '/api/project'],
  ['GET', '/no-such-route'],
  ['POST', '/'],
  ['POST', '/api/project'],
  ['GET', '/api/project?extra=1'],
  ['GET', '/entry/'],
];

function normalise(text, ctx) {
  return text
    .replaceAll(ctx.fixture, '<FIXTURE>')
    .replaceAll(ctx.state, '<STATE>')
    .replace(/\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z/g, '<ISO-TS>')
    .replace(/127\.0\.0\.1:\d+/g, '127.0.0.1:<PORT>');
}

const result = {};
for (const [name, mutate] of CORPUS) {
  const base = mkdtempSync(path.join(tmpdir(), 'zz-rd-'));
  const fixture = path.join(base, 'fixture');
  const state = path.join(base, 'state');
  mkdirSync(fixture, { recursive: true });
  mkdirSync(state, { recursive: true });
  harness.writeCompleteFixture(fixture);
  mutate(fixture);
  let daemon;
  const record = { routes: {} };
  try {
    daemon = await harness.startDaemon({ repoRoot: tree, fixtureRoot: fixture, stateDir: state });
    const token = harness.readCredential(daemon.credentialPath);
    for (const credentialed of [false, true]) {
      for (const [method, route] of ROUTES) {
        const key = `${credentialed ? 'auth' : 'anon'} ${method} ${route}`;
        const headers = credentialed ? { authorization: `Bearer ${token}` } : {};
        const response = await fetch(daemon.baseUrl + route, { method, headers });
        const body = normalise(await response.text(), { fixture, state });
        record.routes[key] = {
          status: response.status,
          contentType: response.headers.get('content-type'),
          bodyLength: body.length,
          bodySha256: createHash('sha256').update(body).digest('hex'),
          body,
        };
      }
    }
    await daemon.stop();
    record.exit = 'stopped';
    record.stderr = normalise(daemon.stderr(), { fixture, state });
    record.stdout = normalise(daemon.stdout(), { fixture, state })
      .split('\n')
      .map((line) => line.replace(/credential \((?:minted|reused)\) at: .*/, 'credential at: <STATE>'))
      .join('\n');
  } catch (cause) {
    record.startFailure = normalise(String(cause?.message ?? cause), { fixture, state });
    if (daemon) await daemon.stop();
  }
  result[name] = record;
  rmSync(base, { recursive: true, force: true });
}

writeFileSync(out, JSON.stringify(result, null, 1) + '\n', 'utf8');
const total = Object.values(result).reduce((n, r) => n + Object.keys(r.routes ?? {}).length, 0);
console.log(`fixtures=${Object.keys(result).length} responses=${total} out=${out}`);
