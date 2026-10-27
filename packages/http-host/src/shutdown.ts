import type { RunningDaemon } from './server.js';

// The signal handling both entries repeated (apps/syzygy and the
// Three-Surface POC, syzygy-bpyt.7.3): the first SIGINT or SIGTERM
// closes the daemon once, and every later signal does nothing.

export type ShutdownSignal = 'SIGINT' | 'SIGTERM';

export interface ShutdownIo {
  readonly onSignal: (signal: ShutdownSignal, listener: () => void) => void;
  /** Told the first signal, before the daemon closes. */
  readonly announce: (signal: ShutdownSignal) => void;
  /** Told why a close failed. Absent, a failed close ends as quietly as a clean one. */
  readonly closeFailed?: (cause: unknown) => void;
}

/** Resolves once the first SIGINT or SIGTERM has closed `daemon`, whether the close succeeded or failed. */
export function closeOnSignal(daemon: Pick<RunningDaemon, 'close'>, io: ShutdownIo): Promise<void> {
  return new Promise<void>((resolve) => {
    let closing = false;
    const shutdown = (signal: ShutdownSignal): void => {
      if (closing) return;
      closing = true;
      io.announce(signal);
      void daemon.close().then(resolve, (cause: unknown) => {
        io.closeFailed?.(cause);
        resolve();
      });
    };
    io.onSignal('SIGINT', () => shutdown('SIGINT'));
    io.onSignal('SIGTERM', () => shutdown('SIGTERM'));
  });
}
