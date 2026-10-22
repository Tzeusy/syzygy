// Prints the brief's dossier guidance exactly as brief.ts derives it at base, plus its version and sha256. Usage: node guidance.mjs <core dist/index.js>
import { createHash } from 'node:crypto';
const { promptForStage, ILLUSTRATION_HEADING } = await import(process.argv[2]);
const p = promptForStage('author', 'dossier');
const open = 'This run produces a dossier:', close = `\n\n${ILLUSTRATION_HEADING}`;
if (p.system.split(open).length !== 2 || p.system.split(close).length !== 2) throw new Error('shape');
const g = p.system.slice(p.system.indexOf(open), p.system.indexOf(close));
const out = { version: p.version, sha256: createHash('sha256').update(g, 'utf8').digest('hex'), bytes: Buffer.byteLength(g), lines: g.split('\n').length,
  backticks: (g.match(/`/g) ?? []).length, dollarBrace: g.includes('${'), backslashes: (g.match(/\\/g) ?? []).length, nonAscii: [...new Set([...g].filter(c => c.charCodeAt(0) > 126))].join('') };
console.log(JSON.stringify(out));
if (process.argv[3]) (await import('node:fs')).writeFileSync(process.argv[3], g);
