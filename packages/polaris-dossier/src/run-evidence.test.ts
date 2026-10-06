import { execFileSync, spawnSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import * as fs from 'node:fs';
import { tmpdir } from 'node:os';
import * as path from 'node:path';
import { pathToFileURL } from 'node:url';
import { afterEach, beforeAll, describe, expect, it } from 'vitest';
import { FIXTURE_URL, PLANTED_SECRET, REAL_ROOT, fullFixtureRun, makeClone } from './full-run.testkit.js';
import type { DossierRenderer } from './render.js';

/** scripts/dossier_run_evidence.mjs, the S12 evidence-record builder (syzygy-qkea.13): every file is named by path, size and a
 * digest computed here, no body is copied, a link is listed and never followed, and the subject is named (rules 3 and 11). */

const SCRIPT = path.join(REAL_ROOT, 'scripts', 'dossier_run_evidence.mjs');

let renderer: DossierRenderer;
beforeAll(async () => {
  const module = pathToFileURL(path.join(REAL_ROOT, 'apps/three-surface-poc/src/polaris-generation/dossier-render.ts')).href;
  renderer = ((await import(module)) as { renderDossier: DossierRenderer }).renderDossier;
});

const cleanups: (() => void)[] = [];
afterEach(() => { for (const cleanup of cleanups.splice(0).reverse()) cleanup(); });
const tempDir = (prefix: string): string => {
  const dir = fs.realpathSync(fs.mkdtempSync(path.join(tmpdir(), prefix)));
  cleanups.push(() => fs.rmSync(dir, { recursive: true, force: true }));
  return dir;
};
type Doc = Record<string, any>; // eslint-disable-line @typescript-eslint/no-explicit-any
const sha256 = (file: string): string => createHash('sha256').update(fs.readFileSync(file)).digest('hex');

/** Every regular file under `root`, relative and sorted, by a walk independent of the script's. */
function regularFiles(root: string): string[] {
  return (fs.readdirSync(root, { recursive: true }) as string[])
    .filter((entry) => fs.lstatSync(path.join(root, entry)).isFile())
    .sort((a, b) => (a < b ? -1 : a > b ? 1 : 0));
}

function evidence(...args: string[]): { status: number | null; stdout: string; stderr: string } {
  const result = spawnSync(process.execPath, [SCRIPT, ...args], { encoding: 'utf8' });
  return { status: result.status, stdout: result.stdout, stderr: result.stderr };
}

async function closedRun(): Promise<{ run: string; commit: string; dir: string }> {
  const dir = tempDir('dossier-evidence-');
  const { clone, commit } = makeClone(path.join(dir, 'repo'));
  const { run } = await fullFixtureRun({ clone, commit, stateRoot: path.join(dir, 'state'), renderer, plantSecret: true, closeArgs: ['--usage-turns', '12'] });
  return { run, commit, dir };
}

describe('dossier run evidence record (S12)', () => {
  it('names the subject, the Syzygy commit and the digest of every file the run and its sessions left', async () => {
    const { run, commit } = await closedRun();
    const result = evidence(run);
    expect(result.status).toBe(0);
    const record = JSON.parse(result.stdout) as Doc;
    expect(record.format).toBe('polaris-dossier-run-evidence/1');
    expect(record.measuredOn.syzygyCommit).toBe(execFileSync('git', ['-C', REAL_ROOT, 'rev-parse', 'HEAD'], { encoding: 'utf8' }).trim());
    expect(record.subject.runId).toBe(path.basename(run));
    expect(record.subject.repository.url).toBe(FIXTURE_URL);
    expect(record.subject.pinnedRevision.commit).toBe(commit);
    expect(record.subject.label).toBe('Inferred');
    expect(record.declared.values.agentTool).toBe('claude-code');
    expect(record.executionRule.arm).toBe('sec-3');

    expect(record.outcome.closed).toBe(true);
    expect(record.outcome.executionRecordSha256).toBe(sha256(path.join(run, 'record.json')));
    expect(record.outcome.agentUsage.turns).toBe(12);
    const sites = fs.readdirSync(path.join(run, 'site')).map(Number).sort((a, b) => a - b);
    expect(record.outcome.sites).toEqual(sites);
    expect(record.outcome.latestSiteMachineSha256).toBe(sha256(path.join(run, 'site', String(sites[sites.length - 1]), 'machine.json')));

    for (const [key, root] of [['runDirectory', run], ['sessionsDirectory', `${run}.sessions`]] as const) {
      const files = record[key].files as { path: string; bytes: number; sha256: string }[];
      expect(files.map((file) => file.path)).toEqual(regularFiles(root));
      expect(files.length).toBeGreaterThan(0);
      for (const file of files) {
        expect(file.sha256).toBe(sha256(path.join(root, file.path)));
        expect(file.bytes).toBe(fs.statSync(path.join(root, file.path)).size);
      }
    }
    expect(Object.values(record.operatorDeclared).filter((value) => value !== null && typeof value !== 'string')).toEqual([]);
    expect(record.operatorDeclared.label).toBe('Inferred');
  });

  it('copies no file body: a credential-shaped token the draft carries never reaches the record', async () => {
    const { run } = await closedRun();
    expect(fs.readFileSync(path.join(run, 'drafts', 'next.json'), 'utf8')).toContain(PLANTED_SECRET);
    const result = evidence(run);
    expect(result.status).toBe(0);
    expect(result.stdout).not.toContain(PLANTED_SECRET);
    expect(result.stdout).not.toContain(fs.readFileSync(path.join(run, 'brief.md'), 'utf8').slice(0, 200));
  });

  it('lists a symbolic link without following it', async () => {
    const { run, dir } = await closedRun();
    const outside = path.join(dir, 'outside.txt');
    fs.writeFileSync(outside, 'outside the run directory\n');
    fs.symlinkSync(outside, path.join(run, 'drafts', 'link.json'));
    const record = JSON.parse(evidence(run).stdout) as Doc;
    expect(record.runDirectory.others).toEqual([{ path: path.join('drafts', 'link.json'), kind: 'symbolic link, not followed' }]);
    expect(record.runDirectory.files.map((file: Doc) => file.sha256)).not.toContain(sha256(outside));
  });

  it('reports an open run as not closed, and refuses anything but one run directory', async () => {
    const { run, dir } = await closedRun();
    expect(evidence().status).toBe(2);
    const twice = evidence(run, run);
    expect(twice.status).toBe(2);
    expect(twice.stderr).toContain('usage:');
    expect(evidence(path.join(dir, 'absent')).status).toBe(2);
    const noRecord = evidence(dir);
    expect(noRecord.status).toBe(2);
    expect(noRecord.stderr).toContain('holds no readable run.json');

    fs.rmSync(path.join(run, 'record.json'));
    const open = JSON.parse(evidence(run).stdout) as Doc;
    expect(open.outcome.closed).toBe(false);
    expect(open.outcome.executionRecordSha256).toBeNull();
  });
});
