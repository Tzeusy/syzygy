// Pins the export-entry reader's segment rules (workspace-reach.testkit.ts, syzygy-bpyt.70) against the Node that runs it.
//
//   node docs/evidence/syzygy-bpyt-70/tools/node_segments.mjs [--write]
//
// 1. The two regexes the reader copies must equal, source and flags, the ones in Node's own
//    lib/internal/modules/esm/resolve.js, read from the running binary.
// 2. For each target in the test's case rows, a scratch package exports it under `import`, and a child `node` imports the
//    package. Node's outcome (ERR_INVALID_PACKAGE_TARGET: refuses; DEP0166 on stderr: warns; else loads) must equal the
//    reader's and the test's. The file the target names is created first, so a target Node accepts loads.
// Exit 1 on any mismatch. With --write, the result goes to node-segments.json beside this directory.
import { spawnSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import { mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const root = join(here, '../../../..');
const kit = await import(join(root, 'packages/polaris-generation-core/src/workspace-reach.testkit.ts'));

// The case rows of workspace-reach.test.ts, read from its source so that each recorded expectation is the test's own.
const testFile = 'packages/polaris-generation-core/src/workspace-reach.test.ts';
const testSource = readFileSync(join(root, testFile), 'utf8');
const block = testSource.slice(testSource.indexOf('const CASES'), testSource.indexOf('];', testSource.indexOf('const CASES')));
const CASES = [...block.matchAll(/\['((?:[^'\\]|\\.)*)', '(loads|refuses|warns)'\]/g)].map((match) => [match[1].replace(/\\(.)/g, '$1'), match[2]]);
if (CASES.length !== (block.match(/\['/g) ?? []).length || CASES.length === 0) throw new Error(`${testFile}: unreadable CASES`);

const nodeSource = process.binding('natives')['internal/modules/esm/resolve'];
const literal = (name) => {
  const line = nodeSource.split('\n').find((text) => text.startsWith(`const ${name} = `));
  return line === undefined ? null : line.slice(`const ${name} = `.length).replace(/;$/, '');
};
const regexes = [['invalidSegmentRegEx', kit.INVALID_SEGMENT], ['deprecatedInvalidSegmentRegEx', kit.REFUSED_SEGMENT]].map(([name, copy]) => {
  const node = literal(name);
  return { node: name, nodeLiteral: node, copy: String(copy), equal: node === String(copy) };
});

const readerOutcome = (target) => {
  const fault = kit.segmentFaultOf({ import: target }, false);
  if (fault === undefined) return 'loads';
  if (fault.endsWith('which Node refuses (ERR_INVALID_PACKAGE_TARGET)')) return 'refuses';
  if (fault.endsWith('which Node loads with a deprecation warning (DEP0166)')) return 'warns';
  return fault;
};

const scratch = mkdtempSync(join(tmpdir(), 'node-segments-'));
const cases = [];
try {
  CASES.forEach(([target, expected], index) => {
    const dir = join(scratch, String(index));
    const pkg = join(dir, 'node_modules', 'pkg');
    mkdirSync(pkg, { recursive: true });
    writeFileSync(join(pkg, 'package.json'), JSON.stringify({ name: 'pkg', type: 'module', exports: { '.': { import: target } } }));
    // The file a loading target names, as Node joins it (empty segments collapse; `.hidden`, `..x` stay).
    const file = join(pkg, target.replace(/\/+/g, '/'));
    mkdirSync(dirname(file), { recursive: true });
    writeFileSync(file, 'export default "loaded";\n');
    writeFileSync(join(dir, 'probe.mjs'), "const m = await import('pkg');\nprocess.stdout.write(String(m.default));\n");
    const run = spawnSync(process.execPath, ['probe.mjs'], { cwd: dir, encoding: 'utf8' });
    const stderr = run.stderr.split('\n').filter((line) => line.trim() !== '');
    const node = run.status === 0 && run.stdout === 'loaded'
      ? (stderr.some((line) => line.includes('DEP0166')) ? 'warns' : stderr.length === 0 ? 'loads' : 'other')
      : stderr.some((line) => line.includes('ERR_INVALID_PACKAGE_TARGET')) ? 'refuses' : 'other';
    const reader = readerOutcome(target);
    cases.push({ target, node, reader, test: expected, equal: node === reader && node === expected, status: run.status, stderr: stderr.slice(0, 2).map((line) => line.slice(0, 200)) });
  });
} finally {
  rmSync(scratch, { recursive: true, force: true });
}

const record = {
  subject: 'packages/polaris-generation-core/src/workspace-reach.testkit.ts',
  subjectSha256: createHash('sha256').update(readFileSync(join(root, 'packages/polaris-generation-core/src/workspace-reach.testkit.ts'))).digest('hex'),
  casesFrom: testFile,
  casesFromSha256: createHash('sha256').update(testSource).digest('hex'),
  node: process.version,
  nodeFile: 'lib/internal/modules/esm/resolve.js',
  regexes,
  cases,
  mismatches: regexes.filter((row) => !row.equal).length + cases.filter((row) => !row.equal).length,
};
if (process.argv.includes('--write')) writeFileSync(join(here, '..', 'node-segments.json'), `${JSON.stringify(record, null, 1)}\n`);
process.stdout.write(`${record.node} regexes ${regexes.map((row) => row.equal).join(' ')} cases ${cases.filter((row) => row.equal).length}/${cases.length} mismatches ${record.mismatches}\n`);
process.exit(record.mismatches === 0 ? 0 : 1);
