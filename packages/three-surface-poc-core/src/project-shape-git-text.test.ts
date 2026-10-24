import { describe, expect, it } from 'vitest';

import { classifyPhaseASeed, compileDetectors, PWB_SECRET_POLICY } from './content-classification.js';
import { observeProjectShapeSources, type GitRunner } from './project-shape-observation.js';

// The three git commands whose output the observer decodes as text (syzygy-bpyt.6.3): the exact commit, the committer
// instant and the tree listing. Bytes that are not well-formed UTF-8 stop the observation as a capture failure that
// names the command; they are never decoded with replacement characters. Expected details are typed here.
const enc = new TextEncoder();
const detectors = compileDetectors(PWB_SECRET_POLICY);
const classifyPhaseA = (text: string) => classifyPhaseASeed(detectors, text);
const COMMIT = '3'.repeat(40);
const BAD = Uint8Array.from([0x61, 0xff, 0x0a]);

function observe(answers: Readonly<Record<string, Uint8Array | 'throw'>>) {
  const calls: string[] = [];
  const runGit: GitRunner = (args) => {
    const command = args[0] ?? '';
    calls.push(command);
    const answer = answers[command];
    if (answer === undefined || answer === 'throw') throw new Error(`stop at ${command}`);
    return answer;
  };
  const result = observeProjectShapeSources({ repositoryId: 'repository:probe', revision: 'main', capturedAt: '2026-10-25T00:00:00.000Z', runGit, classifyPhaseA });
  return { result, calls };
}

describe('observeProjectShapeSources decoding of git output', () => {
  const good = { 'rev-parse': enc.encode(`${COMMIT}\n`), show: enc.encode('2026-08-15T10:00:00+00:00\n') };

  it('stops at the first command whose output is not UTF-8 and names it', () => {
    const stages: ReadonlyArray<readonly [string, Record<string, Uint8Array | 'throw'>, string[]]> = [
      ['rev-parse', { 'rev-parse': BAD }, ['rev-parse']],
      ['show', { ...good, show: BAD }, ['rev-parse', 'show']],
      ['ls-tree', { ...good, 'ls-tree': BAD }, ['rev-parse', 'show', 'ls-tree']],
    ];
    for (const [command, answers, calls] of stages) {
      const observed = observe(answers);
      expect(observed.result, command).toMatchObject({ kind: 'unknown', failureState: 'gitCaptureFailed', detail: `git ${command} produced non-UTF-8 output` });
      expect(observed.calls, command).toEqual(calls);
    }
  });

  it('tells a command that failed from one whose output is not UTF-8', () => {
    expect(observe({ ...good, 'ls-tree': 'throw' }).result).toMatchObject({ failureState: 'gitCaptureFailed', detail: 'git ls-tree failed: stop at ls-tree' });
  });

  it('goes on past a rev-parse answer that is well-formed, with or without a byte-order mark', () => {
    for (const answer of [good['rev-parse'], Uint8Array.from([0xef, 0xbb, 0xbf, ...good['rev-parse']])]) {
      const observed = observe({ 'rev-parse': answer });
      expect(observed.calls).toEqual(['rev-parse', 'show']);
      expect(observed.result).toMatchObject({ detail: 'git show failed: stop at show' });
    }
  });
});
