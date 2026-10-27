// Independent check of syzygy-bpyt.8.22's premise, over the compiled reader's own helper definitions (extracted, not retyped).
import * as fs from 'node:fs';
const js = fs.readFileSync(process.argv[2], 'utf8').split('\n');
const grab = (start) => { const i = js.findIndex(l => l.startsWith(start)); if (i < 0) throw new Error(start); let j = i; while (!/;\s*$/.test(js[j]) || (start.startsWith('const stemFolds') && !/^};/.test(js[j]))) j++; return js.slice(i, j + 1).join('\n').replace(/^export /, ''); };
const code = ['export const INSTANCES_DIR', 'export const EGRESS_V2_INSTANCE', 'const fold = ', 'const stemFolds = ', 'const carries = ', 'const ADMISSION_STEMS', 'const ADMISSION_PATHS'].map(grab).join('\n');
const env = new Function(`${code}\nreturn { fold, stemFolds, carries, ADMISSION_STEMS, ADMISSION_PATHS };`)();
const { stemFolds, carries, ADMISSION_STEMS: S, ADMISSION_PATHS: P } = env;
console.log('extracted:\n' + code + '\n');
let ok = true;
for (const p of P) {
  const np = stemFolds(p)[0], np1 = stemFolds(p)[1];
  const inside = S.filter(s => np.includes(stemFolds(s)[0]));
  console.log(JSON.stringify({ path: p, needleFold: np, sameAsLowercase: np === p.toLowerCase(), bothFormsEqual: np === np1, stemsContained: inside }));
  if (inside.length === 0) ok = false;
}
// Fuzz: random texts that carry a path in some spelling; whenever carries(text, path) holds, some stem must be carried too.
const spell = [p => p, p => p.toUpperCase(), p => p.toUpperCase().replace(/-/g, '_'), p => p.replace(/-/g, '­-'), p => p.replace(/-/g, '​'),
  p => p.replace(/-/g, '–'), p => p.replace(/-/g, ' \n\t '), p => p.replace(/[!-~]/g, c => String.fromCharCode(c.charCodeAt(0) + 0xfee0)), p => p.replace(/-/g, '--'), p => p.replace(/-/g, '_­_')];
const junk = ['', 'x', ' ', '­', '-', 'café ', '`', '​', 'ﬁ', 'ﷺ'];
let rnd = 7; const r = n => { rnd = (rnd * 1103515245 + 12345) % 2147483648; return rnd % n; };
let trials = 0, pathHits = 0, violations = 0;
for (let k = 0; k < 20000; k++) {
  const p = P[r(P.length)], s = spell[r(spell.length)](p);
  const cut = r(s.length + 1), keep = r(3) === 0 ? s.slice(0, cut) + junk[r(junk.length)] + s.slice(cut) : s;
  const text = junk[r(junk.length)] + 'See ' + keep + junk[r(junk.length)];
  trials++;
  if (P.some(q => carries(text, q))) { pathHits++; if (!S.some(st => carries(text, st))) { violations++; console.log('VIOLATION', JSON.stringify(text)); } }
}
console.log(JSON.stringify({ containmentHoldsForEveryPath: ok, fuzzTrials: trials, textsCarryingAPath: pathHits, textsCarryingAPathButNoStem: violations }));
