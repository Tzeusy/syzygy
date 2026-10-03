import { createInterface } from 'node:readline';
import type { Readable, Writable } from 'node:stream';

import type { ReobserveResult } from './reobserve-action.js';
import { reevaluationLines } from './reevaluation-copy.js';

// `--watch` (syzygy-u05.2; P-69: re-observation is human-triggered only).
// The console re-observes once per line the owner enters and at no other
// time: it schedules nothing, polls nothing and watches no file. Each
// result names the evaluation it supersedes and the three clock readings.

export const WATCH_PROMPT = 'Press Enter to re-observe. Nothing re-observes on its own; close input (Ctrl-D) to leave watch mode.';

export interface WatchModeOptions {
  readonly input: Readable;
  readonly output: Writable;
  readonly reobserve: () => Promise<ReobserveResult>;
}

/** Attach the Enter-driven console; resolves when the input closes. */
export function attachWatchMode(options: WatchModeOptions): Promise<void> {
  const { output } = options;
  const lines = createInterface({ input: options.input, terminal: false });
  let pending: Promise<void> = Promise.resolve();
  output.write(`${WATCH_PROMPT}\n`);
  lines.on('line', () => {
    pending = pending.then(async () => {
      output.write('Re-observing…\n');
      const result = await options.reobserve();
      if (result.kind === 'failed') {
        output.write(`Re-observation unavailable: Unknown — ${result.reason}. The prior complete evaluation remains served.\n`);
      } else {
        output.write(`${reevaluationLines(result.reevaluation).join('\n')}\n`);
      }
      output.write(`${WATCH_PROMPT}\n`);
    });
  });
  return new Promise((resolve) => {
    lines.on('close', () => { void pending.then(resolve, resolve); });
  });
}
