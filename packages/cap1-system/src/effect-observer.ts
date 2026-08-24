import { spawn, type ChildProcess } from 'node:child_process';
import {
  accessSync,
  constants,
  mkdtempSync,
  readFileSync,
  rmSync,
} from 'node:fs';
import { tmpdir } from 'node:os';
import { delimiter, isAbsolute, join } from 'node:path';

export type EffectObserverFailureKind =
  | 'strace-unavailable'
  | 'observer-spawn-failed'
  | 'observer-timeout'
  | 'trace-unreadable'
  | 'trace-parse-failed'
  | 'trace-cleanup-failed';

export class EffectObserverError extends Error {
  readonly kind: EffectObserverFailureKind;

  constructor(kind: EffectObserverFailureKind, detail: string) {
    super(`[${kind}] ${detail}`);
    this.name = 'EffectObserverError';
    this.kind = kind;
  }
}

export interface EffectObservation<T> {
  readonly code: number | null;
  readonly signal: NodeJS.Signals | null;
  readonly stdout: string;
  readonly stderr: string;
  readonly trace: T;
}

export interface EffectObserverOptions<T> {
  readonly targetExecutable: string;
  readonly targetArgs: readonly string[];
  readonly parseTrace: (trace: string) => T;
  readonly straceExecutable?: string | undefined;
  readonly timeoutMs?: number | undefined;
}

export interface EffectObserverDependencies {
  readonly resolveExecutable: (executable: string) => string | undefined;
  readonly makeTraceDir: () => string;
  readonly readTrace: (tracePath: string) => string;
  readonly removeTraceDir: (traceDir: string) => void;
  readonly spawnObserver: typeof spawn;
}

function executableOnPath(executable: string): string | undefined {
  const candidates = isAbsolute(executable)
    ? [executable]
    : (process.env['PATH'] ?? '')
        .split(delimiter)
        .filter((entry) => entry !== '')
        .map((entry) => join(entry, executable));
  for (const candidate of candidates) {
    try {
      accessSync(candidate, constants.X_OK);
      return candidate;
    } catch {
      // Continue through the declared PATH population.
    }
  }
  return undefined;
}

const DEFAULT_DEPENDENCIES: EffectObserverDependencies = {
  resolveExecutable: executableOnPath,
  makeTraceDir: () => mkdtempSync(join(tmpdir(), 'syz-effect-trace-')),
  readTrace: (tracePath) => readFileSync(tracePath, 'utf8'),
  removeTraceDir: (traceDir) => rmSync(traceDir, { recursive: true, force: true }),
  spawnObserver: spawn,
};

function errorDetail(cause: unknown): string {
  if (cause instanceof Error) {
    return cause.message;
  }
  return String(cause);
}

function isMissingExecutable(cause: unknown): boolean {
  return (cause as NodeJS.ErrnoException).code === 'ENOENT';
}

/**
 * Run one process under the required Linux strace effect observer.
 *
 * The observer fails closed when strace is unavailable. Every event path uses
 * one settlement gate, and that gate removes the trace directory before the
 * returned promise resolves or rejects. Dependency overrides exist only so
 * system tests can inject child-process and filesystem boundary failures.
 */
export function observeProcessEffects<T>(
  options: EffectObserverOptions<T>,
  overrides: Partial<EffectObserverDependencies> = {},
): Promise<EffectObservation<T>> {
  const dependencies = { ...DEFAULT_DEPENDENCIES, ...overrides };
  const requestedStrace = options.straceExecutable ?? 'strace';
  const resolvedStrace = dependencies.resolveExecutable(requestedStrace);
  if (resolvedStrace === undefined) {
    return Promise.reject(
      new EffectObserverError(
        'strace-unavailable',
        `required system-test effect observer \`${requestedStrace}\` is not executable on PATH`,
      ),
    );
  }

  return new Promise((resolve, reject) => {
    const traceDir = dependencies.makeTraceDir();
    const tracePath = join(traceDir, 'effects.strace');
    let child: ChildProcess | undefined;
    let stdout = '';
    let stderr = '';
    let settled = false;
    let deadline: NodeJS.Timeout | undefined;

    const settle = (
      outcome:
        | { readonly ok: true; readonly observation: EffectObservation<T> }
        | { readonly ok: false; readonly error: EffectObserverError },
    ): void => {
      if (settled) {
        return;
      }
      settled = true;
      if (deadline !== undefined) {
        clearTimeout(deadline);
      }

      try {
        dependencies.removeTraceDir(traceDir);
      } catch (cause) {
        reject(
          new EffectObserverError(
            'trace-cleanup-failed',
            `could not remove observer trace directory ${traceDir}: ${errorDetail(cause)}`,
          ),
        );
        return;
      }

      if (outcome.ok) {
        resolve(outcome.observation);
      } else {
        reject(outcome.error);
      }
    };

    const finishFromTrace = (code: number | null, signal: NodeJS.Signals | null): void => {
      if (settled) {
        return;
      }
      let rawTrace: string;
      try {
        rawTrace = dependencies.readTrace(tracePath);
      } catch (cause) {
        settle({
          ok: false,
          error: new EffectObserverError(
            'trace-unreadable',
            `observer trace could not be read: ${errorDetail(cause)}`,
          ),
        });
        return;
      }

      let parsedTrace: T;
      try {
        parsedTrace = options.parseTrace(rawTrace);
      } catch (cause) {
        settle({
          ok: false,
          error: new EffectObserverError(
            'trace-parse-failed',
            `observer trace could not be parsed: ${errorDetail(cause)}`,
          ),
        });
        return;
      }
      settle({
        ok: true,
        observation: { code, signal, stdout, stderr, trace: parsedTrace },
      });
    };

    try {
      child = dependencies.spawnObserver(
        resolvedStrace,
        [
          '-f',
          '-qq',
          '-e',
          'trace=%file,%network,%process',
          '-o',
          tracePath,
          options.targetExecutable,
          ...options.targetArgs,
        ],
        { stdio: ['ignore', 'pipe', 'pipe'] },
      );
    } catch (cause) {
      settle({
        ok: false,
        error: new EffectObserverError(
          isMissingExecutable(cause) ? 'strace-unavailable' : 'observer-spawn-failed',
          `effect observer could not start: ${errorDetail(cause)}`,
        ),
      });
      return;
    }

    child.stdout?.setEncoding('utf8');
    child.stderr?.setEncoding('utf8');
    child.stdout?.on('data', (chunk: string) => {
      stdout += chunk;
    });
    child.stderr?.on('data', (chunk: string) => {
      stderr += chunk;
    });
    child.once('error', (cause) => {
      settle({
        ok: false,
        error: new EffectObserverError(
          isMissingExecutable(cause) ? 'strace-unavailable' : 'observer-spawn-failed',
          `effect observer could not start: ${errorDetail(cause)}`,
        ),
      });
    });
    child.once('exit', finishFromTrace);
    child.once('close', finishFromTrace);

    deadline = setTimeout(() => {
      child?.kill('SIGKILL');
      settle({
        ok: false,
        error: new EffectObserverError(
          'observer-timeout',
          `effect observer did not settle within ${String(options.timeoutMs ?? 30_000)}ms`,
        ),
      });
    }, options.timeoutMs ?? 30_000);
  });
}
