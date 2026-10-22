// Test support: exports with no non-test importer are consumed by tests only, by design.

import { lstatSync, readdirSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

/** The fixture helper's temp-directory names carry the pid of the process that made
 * them, `p<pid>-` straight after the prefix (or after `template-`), so a later run can
 * tell a killed run's leftovers from a live run's directories (syzygy-bpyt.4.10). */
export const FIXTURE_PREFIX = 'syzygy-poc-surface-fixture-';
export const ownedCopyPrefix = (): string => `${FIXTURE_PREFIX}p${process.pid}-`;
export const ownedTemplatePrefix = (): string => `${FIXTURE_PREFIX}template-p${process.pid}-`;

/** A name made before pids were added has the random suffix where the pid segment now
 * sits and no hyphen after it, so it never matches. */
const FIXTURE_NAME_WITH_OWNER = /^syzygy-poc-surface-fixture-(?:template-)?p(\d+)-/;

/**
 * A run killed before its teardown hooks run (SIGKILL, a CI timeout, a closed terminal)
 * leaves its fixture directories behind. Called once per run, from the app project's
 * global setup, this removes the ones whose owner process is gone. It lists `directory`
 * (the temp directory) and nothing else; an entry is removed only if its name carries a
 * pid that answers ESRCH to signal 0 and `lstat` says it is a directory, so a symlink or a
 * file with such a name is never followed and never removed. A pid that answers, or fails
 * with anything but ESRCH (EPERM, a pid out of range), may be alive and is kept, as is
 * every name without a pid segment. A directory that cannot be removed is left: a sweep
 * must not fail the run that starts it.
 */
export function removeFixturesOfDeadProcesses(directory: string = tmpdir()): void {
  for (const name of readdirSync(directory)) {
    const pid = FIXTURE_NAME_WITH_OWNER.exec(name)?.[1];
    if (pid === undefined || ownerMayBeAlive(Number(pid))) continue;
    const entry = join(directory, name);
    try {
      if (lstatSync(entry).isDirectory()) rmSync(entry, { recursive: true, force: true });
    } catch {
      // Left for the next run.
    }
  }
}

function ownerMayBeAlive(pid: number): boolean {
  try {
    process.kill(pid, 0);
    return true;
  } catch (error) {
    return (error as NodeJS.ErrnoException).code !== 'ESRCH';
  }
}
