/** Test support. Owner-act text rendered by the real recorders (scripts/record_public_repo_admission_acts.py and
 * scripts/record_public_egress_v2_act.py), so a reader's expected forms are tested against what the writer writes. */
import { spawnSync } from 'node:child_process';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

export type RecorderActKey = 'requests-observation' | 'redis-observation' | 'egress-anthropic' | 'egress-anthropic-v2';
const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../..');
const cache = new Map<string, string>();

/** The act record the recorder renders for `key`, with the given argument digest, date and `Recorded at (UTC)` instant. */
export function renderRecorderAct(key: RecorderActKey, argument: string, date: string, instant: string): string {
  const id = [key, argument, date, instant].join('|');
  const hit = cache.get(id);
  if (hit !== undefined) return hit;
  const module = key === 'egress-anthropic-v2' ? 'record_public_egress_v2_act' : 'record_public_repo_admission_acts';
  const py = `import sys; sys.path.insert(0, 'scripts'); import ${module} as m
sys.stdout.write(m.render_act(m.ACT_BY_KEY['${key}'], '${argument}', '${date}', 'b'*64, 'c'*40, 'CONFIRM', m.Selection('opening', 'label', 'description'), 'f'*64, '${instant}'))`;
  const run = spawnSync('python3', ['-c', py], { cwd: ROOT, encoding: 'utf8' });
  if (run.status !== 0) throw new Error(`recorder render failed: ${run.stderr}`);
  cache.set(id, run.stdout);
  return run.stdout;
}

/** The public-source screening-scope policy act as scripts/record_public_source_screening_scope_act.py renders it. */
export function renderPolicyAct(argument: string, date: string, instant: string): string {
  const id = ['policy', argument, date, instant].join('|');
  const hit = cache.get(id);
  if (hit !== undefined) return hit;
  const py = `import sys; sys.path.insert(0, 'scripts'); import record_public_source_screening_scope_act as m
sys.stdout.write(m.render_act(m.ACT, '${argument}', '${date}', 'b'*64, 'c'*40, 'CONFIRM', m.Selection('opening', 'label', 'description'), 'f'*64, '${instant}', '1'*64, '1.2.0-public-source-candidate.1'))`;
  const run = spawnSync('python3', ['-c', py], { cwd: ROOT, encoding: 'utf8' });
  if (run.status !== 0) throw new Error(`recorder render failed: ${run.stderr}`);
  cache.set(id, run.stdout);
  return run.stdout;
}
