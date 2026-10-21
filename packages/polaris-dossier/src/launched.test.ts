import { execFileSync } from 'node:child_process';
import * as fs from 'node:fs';
import * as os from 'node:os';
import * as path from 'node:path';
import { afterEach, describe, expect, it } from 'vitest';
import { expectedLaunch, launchFormRefusal, launchedMarkerState, writeLaunchedMarker } from './launched.js';

// syzygy-bpyt.8.8: the launched marker is read fail-closed. Only a missing file means a run the operator started; anything present that is
// not the marker Syzygy writes is `unreadable`, and no caller treats that more leniently than a launched run. Expected values are literals.

const cleanups: string[] = [];
afterEach(() => { for (const dir of cleanups.splice(0)) fs.rmSync(dir, { recursive: true, force: true }); });
const runDir = (): string => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'polaris-marker-'));
  cleanups.push(dir);
  return dir;
};
const marker = (dir: string): string => path.join(dir, 'launched.json');

const PRESENT_BUT_NOT_THE_MARKER: readonly [string, (dir: string) => void][] = [
  ['an empty file', (dir) => fs.writeFileSync(marker(dir), '')],
  ['invalid JSON', (dir) => fs.writeFileSync(marker(dir), '{"format": "polaris-dossier-launched/1"')],
  ['JSON null', (dir) => fs.writeFileSync(marker(dir), 'null')],
  ['a JSON array', (dir) => fs.writeFileSync(marker(dir), '[]')],
  ['a JSON string', (dir) => fs.writeFileSync(marker(dir), '"polaris-dossier-launched/1"')],
  ['another format', (dir) => fs.writeFileSync(marker(dir), '{"format": "polaris-dossier-launched/2"}')],
  ['no format', (dir) => fs.writeFileSync(marker(dir), '{"runId": "run-x"}')],
  ['a format that is not a string', (dir) => fs.writeFileSync(marker(dir), '{"format": 1}')],
  ['a byte-order mark before the marker', (dir) => fs.writeFileSync(marker(dir), '\uFEFF{"format": "polaris-dossier-launched/1"}')],
  ['a directory', (dir) => fs.mkdirSync(marker(dir))],
  ['a dangling symbolic link', (dir) => fs.symlinkSync(path.join(dir, 'nowhere.json'), marker(dir))],
  ['a symbolic link to the marker Syzygy writes', (dir) => { fs.mkdirSync(path.join(dir, 'elsewhere')); writeLaunchedMarker(path.join(dir, 'elsewhere'), 'run-x', Date.UTC(2026, 9, 21)); fs.symlinkSync(path.join(dir, 'elsewhere', 'launched.json'), marker(dir)); }],
  ['a symbolic link to a character device', (dir) => fs.symlinkSync('/dev/zero', marker(dir))],
  ['a FIFO', (dir) => execFileSync('mkfifo', [marker(dir)])],
  ['a marker padded past 4096 bytes', (dir) => fs.writeFileSync(marker(dir), `{"format": "polaris-dossier-launched/1", "pad": "${'x'.repeat(4096)}"}`)],
  ['a file its reader may not read', (dir) => { fs.writeFileSync(marker(dir), '{"format": "polaris-dossier-launched/1"}'); fs.chmodSync(marker(dir), 0o000); }],
];

describe('launchedMarkerState', () => {
  it('is absent when no file of that name exists, and when the run directory itself is missing', () => {
    const dir = runDir();
    expect(launchedMarkerState(dir)).toBe('absent');
    expect(launchedMarkerState(path.join(dir, 'missing-run'))).toBe('absent');
  });

  it('is launched for the marker Syzygy writes', () => {
    const dir = runDir();
    writeLaunchedMarker(dir, 'run-x', Date.UTC(2026, 9, 21));
    expect(launchedMarkerState(dir)).toBe('launched');
  });

  it('is launched for the marker\'s bytes typed by hand, so the reader and the writer cannot drift together', () => {
    const dir = runDir();
    fs.writeFileSync(marker(dir), '{\n  "format": "polaris-dossier-launched/1",\n  "runId": "run-x",\n  "startedAt": "2026-10-21T00:00:00.000Z",\n  "command": "syzygy polaris",\n  "executionPermitted": false,\n  "direction": "POLARIS-DOSSIER-ONE-COMMAND-RUN-2026-10-14"\n}\n');
    expect(launchedMarkerState(dir)).toBe('launched');
  });

  it.each(PRESENT_BUT_NOT_THE_MARKER)('is unreadable for %s', (_name, plant) => {
    const dir = runDir();
    plant(dir);
    expect(launchedMarkerState(dir)).toBe('unreadable');
  });

  it('is unreadable when the run directory is a file', () => {
    const dir = runDir();
    fs.writeFileSync(path.join(dir, 'not-a-run'), '');
    expect(launchedMarkerState(path.join(dir, 'not-a-run'))).toBe('unreadable');
  });
});

describe('launch forms in a run whose marker is unreadable', () => {
  it.each(PRESENT_BUT_NOT_THE_MARKER)('count neither a declared form nor a syzygy-launched one: %s', (_name, plant) => {
    const dir = runDir();
    plant(dir);
    const refusal = 'the run\'s launched marker is present but cannot be read as the one Syzygy writes, so no launch form counts, declared or syzygy-launched';
    expect(launchFormRefusal(dir, { value: 'terminal', declaredBy: 'operator', label: 'Inferred' })).toBe(refusal);
    expect(launchFormRefusal(dir, { value: 'bang', declaredBy: 'operator', label: 'Inferred' })).toBe(refusal);
    expect(launchFormRefusal(dir, { value: 'syzygy-launched', declaredBy: 'syzygy', label: 'Observed' })).toBe(refusal);
  });

  it('name what a counted record must carry, by marker state', () => {
    expect(expectedLaunch('launched')).toBe('a syzygy-launched launch');
    expect(expectedLaunch('absent')).toBe('a terminal or bang launch');
    expect(expectedLaunch('unreadable')).toBe('a countable launch (the run\'s launched marker is present but unreadable, so none counts)');
  });
});
