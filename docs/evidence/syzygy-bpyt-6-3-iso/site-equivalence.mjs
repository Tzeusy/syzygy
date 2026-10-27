// Is each changed source file the old file with exactly the declared edit and nothing else? For syzygy-bpyt.6.3 stack 4.
// Usage: node site-equivalence.mjs <git repo> <base commit> <head commit> <out.json>
//        node site-equivalence.mjs --selftest
// Run from a checkout that has `typescript` installed (npm ci).
//
// An independent check of apply-is-record.mjs and apply-iso-of.mjs: it never looks at the syntax tree or at the applier's rules.
// For every .ts file under packages/*/src and apps/*/src that differs between the commits it transpiles both versions (comments
// and types removed: this compares what runs) and requires
//     normalize(emit(base)) === normalize(emit(head))
// where normalize drops, from the base side only, the emitted text of the censused local definitions (isObj, isObject, isRecord,
// isoOf) and renames every remaining isObj / isObject identifier to isRecord, and from both sides the `isRecord` and `isoOf` import
// bindings. A definition or an old name still in the head is therefore a difference. Types are not compared here (tsc owns them).
// Test files are listed, not compared: they are the change's own pins. A file that differs by anything else, or that the change adds or
// removes, is listed and fails. Exit status 1 when any file fails.
import { execFileSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import { writeFileSync } from 'node:fs';
import { createRequire } from 'node:module';
import { pathToFileURL } from 'node:url';

const ts = createRequire(import.meta.url)('typescript');
const sha = (v) => createHash('sha256').update(v).digest('hex');
const emit = (source, path) => ts.transpileModule(source, { fileName: path, compilerOptions: { target: ts.ScriptTarget.ES2022, module: ts.ModuleKind.ESNext, removeComments: true } }).outputText;

// The emitted text of every censused local definition, from the definitions themselves.
const DEFINITIONS = [
  "const isObj = (value: unknown): value is Readonly<Record<string, unknown>> => value !== null && typeof value === 'object' && !Array.isArray(value);",
  "const isObject = (value: unknown): value is Readonly<Record<string, unknown>> => value !== null && typeof value === 'object' && !Array.isArray(value);",
  "const isObject = (value: unknown): value is Record<string, unknown> => value !== null && typeof value === 'object' && !Array.isArray(value);",
  "const isRecord = (value: unknown): value is Record<string, unknown> => value !== null && typeof value === 'object' && !Array.isArray(value);",
  "type Fields = Readonly<Record<string, unknown>>;\nconst isObject = (value: unknown): value is Fields => value !== null && typeof value === 'object' && !Array.isArray(value);",
  "function isRecord(value: unknown): value is Record<string, unknown> {\n  return typeof value === 'object' && value !== null && !Array.isArray(value);\n}",
  'const isoOf = (instant: number): string => new Date(instant).toISOString();',
].map((d) => emit(d, 'definition.ts').trim());

const IMPORT_SUPPORT = /^import \{ ([^}]*) \} from '@syzygy\/support';$/m;

export function normalize(js, side) {
  let out = js;
  // only the base side loses its definitions and its old names: a definition or an old name left in the head is a difference
  if (side === 'base') {
    for (const d of DEFINITIONS) out = out.split(d).join('');
    out = out.replace(/\bisObj(?:ect)?\b/g, 'isRecord');
  }
  // the new bindings: `isRecord` in the support import, and the isoOf import line
  out = out.replace(/^import \{ isoOf \} from '\.\/iso-of\.js';\n/m, '');
  out = out.replace(IMPORT_SUPPORT, (_, names) => {
    const kept = names.split(',').map((n) => n.trim()).filter((n) => n !== 'isRecord');
    return kept.length === 0 ? '' : `import { ${kept.join(', ')} } from '@syzygy/support';`;
  });
  out = out.replace(/^import \{ isRecord \} from '@syzygy\/support';\n/m, '');
  return out.split('\n').filter((line) => line.trim() !== '').join('\n');
}

export function compareFiles(baseText, headText, path) {
  const a = normalize(emit(baseText, path), 'base');
  const b = normalize(emit(headText, path), 'head');
  return { equal: a === b, baseSha256: sha(a), headSha256: sha(b) };
}

function selftest() {
  const base = "import { sha256 } from '@syzygy/support';\nconst isObj = (value: unknown): value is Readonly<Record<string, unknown>> => value !== null && typeof value === 'object' && !Array.isArray(value);\nexport const f = (x: unknown) => (isObj(x) ? sha256(String(x['a'])) : '');\n";
  const head = "import { isRecord, sha256 } from '@syzygy/support';\nexport const f = (x: unknown) => (isRecord(x) ? sha256(String(x['a'])) : '');\n";
  const ok = (h, expected, why) => { if (compareFiles(base, h, 'x.ts').equal !== expected) throw new Error(`selftest: ${why}`); };
  ok(head, true, 'the declared edit is equal');
  ok(head.replace("String(x['a'])", "String(x['b'])"), false, 'a changed key is not equal');
  ok(head.replace('isRecord(x) ?', '!isRecord(x) ?'), false, 'a negated test is not equal');
  // (transpileModule drops an import nothing uses, so an unused extra binding is invisible to an emit comparison; tsc owns that)
  ok(head.replace("import { isRecord, sha256 } from '@syzygy/support';\n", "import { isRecord } from '@syzygy/support';\nimport { sha256 } from './elsewhere.js';\n"), false, 'a different import source is not equal');
  ok(`${head}export const g = 1;\n`, false, 'an added statement is not equal');
  // a definition the applier forgot to delete, and an old name it forgot to rename, are differences
  ok(base.replace('isObj(x)', 'isRecord(x)').replace('import { sha256 }', 'import { isRecord, sha256 }'), false, 'a leftover definition is not equal');
  ok(head.replace('isRecord(x)', 'isObj(x)'), false, 'a leftover old name is not equal');
  console.log('site-equivalence selftest ok');
}

if (import.meta.url === pathToFileURL(process.argv[1] ?? '').href) {
  if (process.argv[2] === '--selftest') {
    selftest();
  } else {
    const [repo, base, head, out] = process.argv.slice(2);
    if (out === undefined) throw new Error('usage: site-equivalence.mjs <git repo> <base> <head> <out.json>');
    const git = (...args) => execFileSync('git', ['-C', repo, ...args], { maxBuffer: 1 << 28 });
    const changed = git('diff', '--name-status', '-z', base, head).toString('utf8').split('\0').filter(Boolean);
    const entries = [];
    for (let i = 0; i < changed.length; i += 2) entries.push({ status: changed[i], path: changed[i + 1] });
    const all = entries.filter((e) => /^(packages|apps)\/[^/]+\/src\/.*\.ts$/.test(e.path));
    const sources = all.filter((e) => !e.path.endsWith('.test.ts'));
    const testFiles = all.filter((e) => e.path.endsWith('.test.ts')).map((e) => `${e.status} ${e.path}`);
    const rows = sources.map(({ status, path }) => {
      if (status !== 'M') return { path, status, equal: false, note: 'added or removed by the change: outside this check' };
      const result = compareFiles(git('show', `${base}:${path}`).toString('utf8'), git('show', `${head}:${path}`).toString('utf8'), path);
      return { path, status, ...result };
    });
    const modified = rows.filter((r) => r.status === 'M');
    const result = {
      base: git('rev-parse', base).toString().trim(), head: git('rev-parse', head).toString().trim(),
      changedSourceFiles: sources.length, testFilesNotCompared: testFiles, modified: modified.length, equal: modified.filter((r) => r.equal).length,
      notEqual: rows.filter((r) => !r.equal).map((r) => r.path), rows,
    };
    writeFileSync(out, `${JSON.stringify(result, null, 1)}\n`);
    console.log(JSON.stringify({ ...result, rows: undefined }, null, 1));
    process.exitCode = result.notEqual.length === 0 ? 0 : 1;
  }
}
