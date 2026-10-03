import { execFileSync } from 'node:child_process';

/** Every git call that touches an unfamiliar repository runs with no system or
 * global config, no prompts, and the repo-local settings that execute programs
 * (fsmonitor, hooks) overridden. `-c` outranks the repository's own config. */
export const ISOLATED_GIT_FLAGS: readonly string[] = ['-c', 'core.fsmonitor=false', '-c', 'core.hooksPath=/dev/null', '-c', 'protocol.file.allow=never', '--no-optional-locks'];
export const isolatedGitEnv = (): NodeJS.ProcessEnv => ({ ...process.env, GIT_CONFIG_NOSYSTEM: '1', GIT_CONFIG_GLOBAL: '/dev/null', GIT_TERMINAL_PROMPT: '0' });

export function isolatedGit(repoRoot: string, args: readonly string[], input?: string): Buffer {
  return execFileSync('git', [...ISOLATED_GIT_FLAGS, '-C', repoRoot, ...args], { maxBuffer: 512_000_000, env: isolatedGitEnv(),
    ...(input === undefined ? {} : { input }), stdio: ['pipe', 'pipe', 'ignore'] });
}
