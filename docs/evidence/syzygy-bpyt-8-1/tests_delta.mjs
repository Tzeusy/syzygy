// syzygy-bpyt.8.1: the PR's `Tests: +a ~b -c`, read off the syntax of every test file the change touches. A test is an `it`/`test`
// call (`.each`, `.skip`, `.only`, `.skipIf(...)` included) keyed by its describe chain and title as written; it is modified when its
// call's text changed. Usage: node tests_delta.mjs <tree> <old commit> <new commit>   (prints JSON)
import { execFileSync } from 'node:child_process';
import * as path from 'node:path';
import { createRequire } from 'node:module';

const [TREE, OLD, NEW] = [path.resolve(process.argv[2]), process.argv[3], process.argv[4]];
const ts = createRequire(path.join(TREE, 'package.json'))('typescript');
const git = (...args) => execFileSync('git', ['-C', TREE, ...args], { encoding: 'utf8', maxBuffer: 1 << 28 });
const show = (commit, file) => { try { return execFileSync('git', ['-C', TREE, 'show', `${commit}:${file}`], { encoding: 'utf8', maxBuffer: 1 << 28, stdio: ['ignore', 'pipe', 'ignore'] }); } catch { return null; } };
const changed = git('diff', '--name-only', OLD, NEW).split('\n').filter((f) => /\.test\.ts$/u.test(f));

const head = (expr) => {
  while (ts.isCallExpression(expr) || ts.isPropertyAccessExpression(expr)) expr = ts.isCallExpression(expr) ? expr.expression : expr.expression;
  return ts.isIdentifier(expr) ? expr.text : null;
};
function tests(text) {
  if (text === null) return new Map();
  const file = ts.createSourceFile('t.ts', text, ts.ScriptTarget.Latest, true);
  const found = new Map();
  const visit = (node, chain) => {
    if (ts.isCallExpression(node) && ['describe', 'it', 'test'].includes(head(node.expression) ?? '') && node.arguments.length > 0) {
      const title = node.arguments[0].getText(file);
      if (head(node.expression) === 'describe') { node.arguments.slice(1).forEach((arg) => visit(arg, [...chain, title])); return; }
      found.set([...chain, title].join(' > '), node.getText(file));
      return;
    }
    ts.forEachChild(node, (child) => visit(child, chain));
  };
  visit(file, []);
  return found;
}
const rows = changed.map((file) => {
  const before = tests(show(OLD, file)), after = tests(show(NEW, file));
  return { file, added: [...after.keys()].filter((k) => !before.has(k)), removed: [...before.keys()].filter((k) => !after.has(k)),
    modified: [...after.keys()].filter((k) => before.has(k) && before.get(k) !== after.get(k)) };
});
const total = (key) => rows.reduce((n, row) => n + row[key].length, 0);
console.log(JSON.stringify({ old: git('rev-parse', OLD).trim(), new: git('rev-parse', NEW).trim(), changedTestFiles: changed.length,
  summary: `Tests: +${total('added')} ~${total('modified')} -${total('removed')}`, rows }, null, 2));
