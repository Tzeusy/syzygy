// THROWAWAY (untracked): the root config plus the call recorders.
import { mergeConfig } from 'vitest/config';
import base from './vitest.config.ts';

const setup = ['./zz-diff.setup-core.ts'];
if (process.env['DIFF_TESTING'] === '1') setup.push('./zz-diff.setup-testing.ts');

export default mergeConfig(base, { test: { setupFiles: setup } });
