import { readFileSync } from 'node:fs';
import { PassThrough } from 'node:stream';

import { describe, expect, it } from 'vitest';

import { describeReevaluation } from '@syzygy/three-surface-poc-core';

import type { ReobserveResult } from './reobserve-action.js';
import { attachWatchMode } from './watch-mode.js';

// syzygy-u05.2: --watch re-observes on the owner's Enter and at no other time.

const PROMPT = 'Press Enter to re-observe. Nothing re-observes on its own; close input (Ctrl-D) to leave watch mode.';

function collect(stream: PassThrough): () => string {
  let text = '';
  stream.on('data', (chunk: Buffer) => { text += chunk.toString('utf8'); });
  return () => text;
}

async function settle(): Promise<void> {
  for (let i = 0; i < 5; i += 1) await Promise.resolve();
}

describe('--watch console', () => {
  it('re-observes once per Enter, never without one, and prints the named result', async () => {
    const input = new PassThrough();
    const output = new PassThrough();
    const written = collect(output);
    let calls = 0;
    const results: ReobserveResult[] = [
      { kind: 'reobserved', reevaluation: describeReevaluation({
        prior: { evaluation: 'evaluation:first', clocks: { butlersHead: 'head-a', workingTreeDigest: 'tree-a', doltRevision: 'dolt-a' } },
        next: { evaluation: 'evaluation:second', clocks: { butlersHead: 'head-a', workingTreeDigest: 'tree-b', doltRevision: 'dolt-a' } },
        projectChange: { changedSources: 0, addedSources: 0 },
        observatory: { buildRevision: 'syzygy-build', currentRevision: 'syzygy-build', commitsSinceBuild: 0 },
      }) },
      { kind: 'failed', reason: 'POC runtime inputs are dirty; re-observation was refused' },
    ];
    const done = attachWatchMode({ input, output, reobserve: async () => results[calls++] as ReobserveResult });
    await settle();
    expect(calls).toBe(0);
    expect(written()).toBe(`${PROMPT}\n`);

    const printed = new Promise<void>((resolve) => {
      output.on('data', () => { if (written().includes('Observatory limb')) resolve(); });
    });
    input.write('\n');
    await printed;
    expect(calls).toBe(1);
    expect(written()).toContain([
      'Re-observing…',
      'Evaluation: evaluation:second',
      'Supersedes: evaluation:first',
      'Butlers HEAD: head-a (unchanged)',
      'Working-tree digest: tree-b (moved)',
      'Dolt revision: dolt-a (unchanged)',
      'Observed-project limb: 0 changed, 0 added since the superseded evaluation',
      'Observatory limb: 0 Syzygy commits since build syzygy-build',
      PROMPT,
    ].join('\n'));

    input.write('not a command, still one Enter\n');
    input.end();
    await done;
    expect(calls).toBe(2);
    expect(written()).toContain('Re-observation unavailable: Unknown — POC runtime inputs are dirty; re-observation was refused. The prior complete evaluation remains served.');
  });

  it('closing input without an Enter re-observes nothing', async () => {
    const input = new PassThrough();
    const output = new PassThrough();
    let calls = 0;
    const done = attachWatchMode({ input, output, reobserve: async () => { calls += 1; return { kind: 'failed', reason: 'unused' }; } });
    input.end();
    await done;
    expect(calls).toBe(0);
  });
});

// P-69: the re-observation path schedules nothing. Every production file the
// re-observation slice touches is scanned for a timer, a poller or a file
// watcher; the list is literal so a new file must be added on purpose.
const REOBSERVATION_SOURCES = [
  'apps/three-surface-poc/src/cli.ts',
  'apps/three-surface-poc/src/git-observation.ts',
  'apps/three-surface-poc/src/main.ts',
  'apps/three-surface-poc/src/page-shell.ts',
  'apps/three-surface-poc/src/reevaluation-copy.ts',
  'apps/three-surface-poc/src/reobserve-action.ts',
  'apps/three-surface-poc/src/reobserve-state.ts',
  'apps/three-surface-poc/src/routes.ts',
  'apps/three-surface-poc/src/watch-mode.ts',
  'packages/three-surface-poc-core/src/reevaluation.ts',
] as const;
const UNATTENDED = [/\bsetInterval\b/, /\bsetTimeout\b/, /\bsetImmediate\b/, /\bwatchFile\b/, /\bwatch\s*\(/, /\bfs\.watch/, /\bchokidar\b/, /\bfs\/promises['"][^;]*\bwatch\b/, /\{[^}]*\bwatch\b[^}]*\}\s*from\s*['"](?:node:)?fs/];

describe('no unattended re-observation (P-69)', () => {
  it.each(REOBSERVATION_SOURCES)('%s carries no timer, poller or file watcher', (path) => {
    const text = readFileSync(new URL(`../../../${path}`, import.meta.url), 'utf8');
    expect(text.length).toBeGreaterThan(0);
    expect(UNATTENDED.filter((pattern) => pattern.test(text)).map(String)).toEqual([]);
  });

  it('the scan detects each forbidden form (fixture self-check)', () => {
    for (const sample of ['setInterval(f, 1)', 'setTimeout(f)', 'setImmediate(f)', 'fs.watchFile(p)', 'watch(p, f)', 'fs.watch(p)', "import chokidar from 'chokidar'", "import { watch } from 'node:fs'"]) {
      expect(UNATTENDED.some((pattern) => pattern.test(sample)), sample).toBe(true);
    }
    expect(UNATTENDED.some((pattern) => pattern.test("attachWatchMode({ input }); '--watch'"))).toBe(false);
  });
});
