// Usage: node yaml-byte-equality.mjs <repo-root> <yaml-cases.json>
// For each recorded case (the old inline declaration literal, with template
// interpolations replaced by <<PLACEHOLDER>> text, and the fields the
// builder is now called with), the builder output must equal the old literal
// byte for byte. Reads the built builder from the repository's dist.
import { readFileSync } from 'node:fs';
import * as path from 'node:path';
import { pathToFileURL } from 'node:url';

const root = path.resolve(process.argv[2]);
const cases = JSON.parse(readFileSync(path.resolve(process.argv[3]), 'utf8'));
const { projectYaml } = await import(
  pathToFileURL(path.join(root, 'packages/cap1-conformance/dist/fixtures/index.js')).href
);

let equal = 0;
const unequal = [];
for (const entry of cases) {
  const built = projectYaml(entry.fields);
  if (built === entry.old) equal += 1;
  else unequal.push(`${entry.file}:${entry.line}`);
}
console.log(`cases=${cases.length} byte-equal=${equal} unequal=${unequal.length}`);
if (unequal.length > 0) {
  console.log(unequal.join('\n'));
  process.exit(1);
}
