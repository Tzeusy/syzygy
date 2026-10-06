import { readdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { describe, expect, it } from 'vitest';

// syzygy-4mbu round 1, finding 1: an operator-reported run resolves to the
// `reported` kind, capped at report-fact (RFC5-19). Every consumer of the
// verification kind must treat it as not verified. This sweep fixes the
// consumer population, so a new reader of the kind fails here until it is
// added below with the reason it is safe; the behaviour of each listed
// consumer is asserted in its own test file (named beside it).

const ROOT = fileURLToPath(new URL('../../../', import.meta.url));
const TREES = ['apps', 'packages'];
const DEFINITION = 'packages/three-surface-poc-core/src/test-artifact-verification.ts';

/** Every non-test TypeScript source under the two implementation trees. */
function sources(): Map<string, string> {
  const found = new Map<string, string>();
  for (const tree of TREES) {
    for (const entry of readdirSync(join(ROOT, tree), { recursive: true, encoding: 'utf8' })) {
      const path = `${tree}/${entry}`;
      if (!path.endsWith('.ts') || path.endsWith('.test.ts') || path.endsWith('.d.ts')) continue;
      if (path.includes('/node_modules/') || path.includes('/dist/')) continue;
      found.set(path, readFileSync(join(ROOT, path), 'utf8'));
    }
  }
  return found;
}

const CONSUMER = /\.testArtifactVerification\b|\bTestArtifactVerificationResult\b/;
const VERIFIED_COMPARISON = /\bkind\s*[!=]==?\s*['"]verified['"]/g;
const VERIFIED_ARM = /\bcase\s+['"]verified['"]\s*:/g;

/** The consumers of the kind, each with why `reported` cannot read as
 * verified there and the test that holds it. */
const EXPECTED_CONSUMERS: Readonly<Record<string, string>> = {
  'apps/three-surface-poc/src/trajectory.ts':
    'renders `reported` in the Unknown encoding with its disclosure, never "Verified" (trajectory.test.ts)',
  'packages/three-surface-poc-core/src/model.ts':
    'adds `reported` to the Unknown subjects with its disclosure (trajectory.test.ts reads it back)',
  'apps/three-surface-poc/src/fresh-checkout-demo-main.ts':
    'copies the kind string into its evidence record; it gates nothing on it',
};

/** Every `kind === 'verified'` comparison and `case 'verified':` arm. */
const EXPECTED_VERIFIED_SITES: Readonly<Record<string, number>> = {
  'apps/three-surface-poc/src/trajectory.ts': 2,
  [DEFINITION]: 0,
};

describe('every consumer of the test-artifact verification kind treats `reported` as not verified', () => {
  it('finds exactly the listed consumers', () => {
    const all = sources();
    expect(all.size).toBeGreaterThan(100);
    const consumers = [...all].filter(([path, text]) => path !== DEFINITION && CONSUMER.test(text)).map(([path]) => path);
    expect(consumers.sort()).toEqual(Object.keys(EXPECTED_CONSUMERS).sort());
  });

  it('finds exactly the listed `verified` comparisons and switch arms, and none of them admits `reported`', () => {
    const sites = new Map<string, number>();
    for (const [path, text] of sources()) {
      const count = [...text.matchAll(VERIFIED_COMPARISON)].length + [...text.matchAll(VERIFIED_ARM)].length;
      if (count > 0) sites.set(path, count);
    }
    const expected = Object.entries(EXPECTED_VERIFIED_SITES).filter(([, count]) => count > 0);
    expect([...sites].sort()).toEqual(expected.sort());
    // The two Trajectory comparisons: the Observed badge requires `verified`
    // exactly, and the no-intent branch names `reported` beside it.
    const trajectory = sources().get('apps/three-surface-poc/src/trajectory.ts') ?? '';
    expect(trajectory).toContain("if (verification.kind === 'verified' && governingIntentId !== null) {");
    expect(trajectory).toContain("if (verification.kind === 'verified' || verification.kind === 'reported') {");
    const observedBadge = trajectory.split('\n').filter((line) => line.includes('epistemic-observed') && line.includes('worker-change-verification'));
    expect(observedBadge).toHaveLength(1);
  });

  it('keeps `reported` out of the Observed record type', () => {
    const definition = sources().get(DEFINITION) ?? '';
    expect(definition).toContain("| { readonly kind: 'verified'; readonly record: ObservedRunTestArtifactRecord }");
  });
});
