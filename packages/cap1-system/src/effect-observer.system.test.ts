import { type ChildProcess, spawn } from 'node:child_process';
import { EventEmitter } from 'node:events';
import { PassThrough } from 'node:stream';
import { describe, expect, it, vi } from 'vitest';

import {
  observeProcessEffects,
  type EffectObserverDependencies,
} from './effect-observer.js';

class FakeChild extends EventEmitter {
  readonly stdout = new PassThrough();
  readonly stderr = new PassThrough();
  readonly kill = vi.fn(() => true);
}

interface ObserverRig {
  readonly child: FakeChild;
  readonly dependencies: Partial<EffectObserverDependencies>;
  readonly makeTraceDir: ReturnType<typeof vi.fn>;
  readonly readTrace: ReturnType<typeof vi.fn>;
  readonly removeTraceDir: ReturnType<typeof vi.fn>;
}

function observerRig(emitEvents: (child: FakeChild) => void): ObserverRig {
  const child = new FakeChild();
  const makeTraceDir = vi.fn(() => '/observer/trace-1');
  const readTrace = vi.fn(() => 'trace-record');
  const removeTraceDir = vi.fn();
  const spawnObserver = (() => {
    queueMicrotask(() => emitEvents(child));
    return child as unknown as ChildProcess;
  }) as unknown as typeof spawn;
  return {
    child,
    makeTraceDir,
    readTrace,
    removeTraceDir,
    dependencies: {
      resolveExecutable: () => '/usr/bin/strace',
      makeTraceDir,
      readTrace,
      removeTraceDir,
      spawnObserver,
    },
  };
}

function observe(
  rig: ObserverRig,
  parseTrace: (trace: string) => string = (trace) => trace,
) {
  return observeProcessEffects(
    {
      targetExecutable: '/usr/bin/node',
      targetArgs: ['daemon.js'],
      parseTrace,
      timeoutMs: 1_000,
    },
    rig.dependencies,
  );
}

describe('system effect-observer lifecycle', () => {
  it('fails closed with one named diagnostic before allocating when strace is unavailable', async () => {
    const makeTraceDir = vi.fn(() => '/observer/should-not-exist');

    await expect(
      observeProcessEffects(
        {
          targetExecutable: '/usr/bin/node',
          targetArgs: ['daemon.js'],
          parseTrace: (trace) => trace,
        },
        { resolveExecutable: () => undefined, makeTraceDir },
      ),
    ).rejects.toMatchObject({
      kind: 'strace-unavailable',
      message:
        '[strace-unavailable] required system-test effect observer `strace` is not executable on PATH',
    });
    expect(makeTraceDir).not.toHaveBeenCalled();
  });

  it('settles once and cleans once when spawn emits ENOENT followed by exit and close', async () => {
    const rig = observerRig((child) => {
      const unavailable = Object.assign(new Error('spawn strace ENOENT'), { code: 'ENOENT' });
      child.emit('error', unavailable);
      child.emit('exit', 127, null);
      child.emit('close', 127, null);
    });

    await expect(observe(rig)).rejects.toMatchObject({
      kind: 'strace-unavailable',
    });
    expect(rig.removeTraceDir).toHaveBeenCalledOnce();
    expect(rig.readTrace).not.toHaveBeenCalled();
  });

  it('cleans after a synchronous observer spawn failure', async () => {
    const rig = observerRig(() => undefined);
    const spawnObserver = (() => {
      throw Object.assign(new Error('spawn blocked'), { code: 'EACCES' });
    }) as unknown as typeof spawn;

    await expect(
      observeProcessEffects(
        {
          targetExecutable: '/usr/bin/node',
          targetArgs: ['daemon.js'],
          parseTrace: (trace) => trace,
        },
        { ...rig.dependencies, spawnObserver },
      ),
    ).rejects.toMatchObject({ kind: 'observer-spawn-failed' });
    expect(rig.removeTraceDir).toHaveBeenCalledOnce();
    expect(rig.readTrace).not.toHaveBeenCalled();
  });

  it('waits for close to include data emitted after nonzero exit and settles duplicate events once', async () => {
    const rig = observerRig((child) => {
      child.emit('exit', 1, null);
      child.stdout.write('late-stdout');
      child.stderr.write('late-stderr');
      child.emit('close', 1, null);
      child.emit('error', new Error('late duplicate event'));
    });

    const observation = await observe(rig);
    expect(observation).toMatchObject({
      code: 1,
      signal: null,
      stdout: 'late-stdout',
      stderr: 'late-stderr',
      trace: 'trace-record',
    });
    expect(rig.readTrace).toHaveBeenCalledOnce();
    expect(rig.removeTraceDir).toHaveBeenCalledOnce();
  });

  it('cleans before rejecting an unreadable trace', async () => {
    const rig = observerRig((child) => child.emit('close', 0, null));
    rig.readTrace.mockImplementation(() => {
      throw Object.assign(new Error('missing trace'), { code: 'ENOENT' });
    });

    await expect(observe(rig)).rejects.toMatchObject({
      kind: 'trace-unreadable',
    });
    expect(rig.removeTraceDir).toHaveBeenCalledOnce();
  });

  it('cleans before rejecting a trace parser failure', async () => {
    const rig = observerRig((child) => {
      child.emit('exit', 0, null);
      child.emit('close', 0, null);
    });

    await expect(
      observe(rig, () => {
        throw new Error('malformed trace fixture');
      }),
    ).rejects.toMatchObject({ kind: 'trace-parse-failed' });
    expect(rig.removeTraceDir).toHaveBeenCalledOnce();
  });

  it('kills a non-settling observer and cleans its trace directory on timeout', async () => {
    const rig = observerRig(() => undefined);

    await expect(
      observeProcessEffects(
        {
          targetExecutable: '/usr/bin/node',
          targetArgs: ['daemon.js'],
          parseTrace: (trace) => trace,
          timeoutMs: 5,
        },
        rig.dependencies,
      ),
    ).rejects.toMatchObject({ kind: 'observer-timeout' });
    expect(rig.child.kill).toHaveBeenCalledWith('SIGKILL');
    expect(rig.removeTraceDir).toHaveBeenCalledOnce();
  });

  it('removes the trace directory before exposing a successful result to caller assertions', async () => {
    const rig = observerRig((child) => child.emit('close', 0, null));

    const observation = await observe(rig);
    expect(rig.removeTraceDir).toHaveBeenCalledOnce();
    expect(() => expect(observation.trace).toBe('deliberately-wrong')).toThrow();
    expect(rig.removeTraceDir).toHaveBeenCalledOnce();
  });
});
