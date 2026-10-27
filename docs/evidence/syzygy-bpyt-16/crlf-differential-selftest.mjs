// Rule 6 for crlf-differential.mjs: mutate the HEAD build and confirm each predicate fails on its own.
// Usage: node crlf-differential-selftest.mjs <base dist> <head dist> <node_modules dir> <scratch dir> <out.json>
// The scratch dir is created fresh (it must not exist); the head dist is copied into it with node_modules linked beside it, one
// mutation is applied to the copy, and the differential runs against it. A mutation is killed when the differential exits 1 and
// its failures include the predicate the mutation targets; `exact` records whether no other check failed with it (a changed line
// split moves every later check too, so only S1 and S4 isolate their predicate).
import { execFileSync } from 'node:child_process';
import { cpSync, existsSync, mkdirSync, readFileSync, rmSync, symlinkSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const [baseDist, headDist, nodeModules, scratch, out] = process.argv.slice(2);
if (out === undefined) throw new Error('usage: crlf-differential-selftest.mjs <base dist> <head dist> <node_modules> <scratch> <out.json>');
if (existsSync(scratch)) throw new Error(`${scratch} exists`);

// [id, predicate, file, old, new, expected checks]
const MUTANTS = [
  ['S1', 'C1 LF unchanged', 'markdown-code-context.js', 'return run[0] === char && run.length >= length;', 'return run[0] === char && run.length > length;', ['C1']],
  ['S2', 'C2 rendering equals LF', 'markdown-code-context.js', 'const LINE_END = /\\r\\n|\\r|\\n/g;', 'const LINE_END = /\\n/g;', ['C2']],
  ['S3', 'C3 mask invariants', 'markdown-code-context.js', "line + (terminators[index] ?? '')", "line + (terminators[index] === '\\r\\n' ? '\\r ' : (terminators[index] ?? ''))", ['C3']],
  ['S4', 'C4 CRLF positions', 'git-object-reader.js', 'if (text.charCodeAt(i) === 10) {', 'if (text.charCodeAt(i) === 10 || text.charCodeAt(i) === 13) {', ['C4']],
];

const results = [];
rmSync(scratch, { recursive: true, force: true });
for (const [id, predicate, file, oldText, newText, expected] of MUTANTS) {
  const root = join(scratch, id);
  const dist = join(root, 'packages', 'three-surface-poc-core', 'dist');
  mkdirSync(dirname(dist), { recursive: true });
  cpSync(headDist, dist, { recursive: true });
  symlinkSync(nodeModules, join(root, 'node_modules'));
  const path = join(dist, file);
  const source = readFileSync(path, 'utf8');
  if (source.split(oldText).length !== 2) throw new Error(`${id}: the old fragment is not in ${file} exactly once`);
  writeFileSync(path, source.replace(oldText, () => newText));
  const outJson = join(root, 'out.json');
  let exit = 0;
  try {
    execFileSync('node', [join(here, 'crlf-differential.mjs'), baseDist, dist, outJson], { stdio: ['ignore', 'ignore', 'ignore'], maxBuffer: 1 << 28 });
  } catch (error) {
    exit = error.status ?? -1;
  }
  const checks = existsSync(outJson) ? [...new Set(JSON.parse(readFileSync(outJson, 'utf8')).failingChecks)].sort() : [];
  const killed = exit === 1 && expected.every((check) => checks.includes(check));
  const exact = JSON.stringify(checks) === JSON.stringify(expected);
  results.push({ id, predicate, file, old: oldText, new: newText, exit, failingChecks: checks, targetChecks: expected, killed, exact });
}
rmSync(scratch, { recursive: true, force: true });
writeFileSync(out, `${JSON.stringify({ mutants: results, killed: results.filter((r) => r.killed).length, total: results.length }, null, 1)}\n`);
console.log(JSON.stringify(results.map(({ id, predicate, exit, failingChecks, killed, exact }) => ({ id, predicate, exit, failingChecks, killed, exact })), null, 1));
if (results.some((r) => !r.killed)) process.exit(1);
