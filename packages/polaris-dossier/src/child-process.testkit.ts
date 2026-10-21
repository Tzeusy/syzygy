/** Test support: run a command without blocking the vitest worker. A worker answers its parent over an RPC with a fixed 60 s timeout,
 * so a synchronous child that outlasts it fails the run with every test passed (syzygy-w90k; the suite guard in
 * apps/three-surface-poc/src/sync-child-process-guard.test.ts). */
import { execFile, type ExecFileOptions } from 'node:child_process';

export interface Exited { readonly status: number | null; readonly stdout: string; readonly stderr: string }

/** What spawnSync would report: the exit code, or null when the command could not start or a signal (or the timeout) ended it. */
export function exited(file: string, args: readonly string[], options: ExecFileOptions = {}): Promise<Exited> {
  return new Promise((resolve) => {
    execFile(file, args, { ...options, encoding: 'utf8' }, (error, stdout, stderr) => {
      resolve({ status: error === null ? 0 : typeof error.code === 'number' ? error.code : null, stdout, stderr });
    });
  });
}
