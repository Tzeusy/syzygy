/** Test support. Owner-act text rendered by the real recorders (scripts/record_public_repo_admission_acts.py, the registry-entry recorder and
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

/** The public-source screening-scope policy act as scripts/record_public_source_screening_scope_act.py (version 1) or
 * scripts/record_public_source_screening_scope_v2_act.py (version 2) renders it. */
export function renderPolicyAct(argument: string, date: string, instant: string, version: 1 | 2 = 1, supersededArgument = '1'.repeat(64)): string {
  const id = ['policy', version, argument, date, instant, supersededArgument].join('|');
  const hit = cache.get(id);
  if (hit !== undefined) return hit;
  const py = version === 1
    ? `import sys; sys.path.insert(0, 'scripts'); import record_public_source_screening_scope_act as m
sys.stdout.write(m.render_act(m.ACT, '${argument}', '${date}', 'b'*64, 'c'*40, 'CONFIRM', m.Selection('opening', 'label', 'description'), 'f'*64, '${instant}', '1'*64, '1.2.0-public-source-candidate.1'))`
    : `import sys; sys.path.insert(0, 'scripts'); import record_public_source_screening_scope_v2_act as m
sys.stdout.write(m.render_act(m.ACT, '${argument}', 'none', '${date}', 'b'*64, 'c'*40, 'CONFIRM', m.Selection('opening', 'label', 'description'), 'f'*64, '${instant}', '${supersededArgument}', '2026-10-03', '1.2.0-public-source-candidate.2'))`;
  const run = spawnSync('python3', ['-c', py], { cwd: ROOT, encoding: 'utf8' });
  if (run.status !== 0) throw new Error(`recorder render failed: ${run.stderr}`);
  cache.set(id, run.stdout);
  return run.stdout;
}

/** The RFC5-14 project-documentation class amendment act as scripts/record_rfc5_project_documentation_act.py renders it. */
export function renderClassAct(argument: string, date: string, instant: string): string {
  const id = ['class', argument, date, instant].join('|');
  const hit = cache.get(id);
  if (hit !== undefined) return hit;
  const py = `import sys; sys.path.insert(0, 'scripts'); import record_rfc5_project_documentation_act as m
sys.stdout.write(m.render_act('${argument}', '${date}', 'b'*64, 'c'*40, 'CONFIRM', m.Selection('opening', 'label', 'description'), 'f'*64, '${instant}'))`;
  const run = spawnSync('python3', ['-c', py], { cwd: ROOT, encoding: 'utf8' });
  if (run.status !== 0) throw new Error(`recorder render failed: ${run.stderr}`);
  cache.set(id, run.stdout);
  return run.stdout;
}

/** The public Git-hosting source-acquisition registry entry act as scripts/record_public_admission_registry_entries_acts.py renders it
 * (key `git-source-acquisition`). */
export function renderRegistryAct(argument: string, date: string, instant: string): string {
  const id = ['registry', argument, date, instant].join('|');
  const hit = cache.get(id);
  if (hit !== undefined) return hit;
  const py = `import sys; sys.path.insert(0, 'scripts'); import record_public_admission_registry_entries_acts as m
sys.stdout.write(m.render_act(m.ACT_BY_KEY['git-source-acquisition'], '${argument}', '${date}', 'b'*64, 'c'*40, 'CONFIRM', m.Selection('opening', 'label', 'description'), 'f'*64, '${instant}'))`;
  const run = spawnSync('python3', ['-c', py], { cwd: ROOT, encoding: 'utf8' });
  if (run.status !== 0) throw new Error(`recorder render failed: ${run.stderr}`);
  cache.set(id, run.stdout);
  return run.stdout;
}
