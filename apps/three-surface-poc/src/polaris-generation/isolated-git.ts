import { execFileSync } from 'node:child_process';

/** Every git call that touches an unfamiliar repository runs with no system or
 * global config, no prompts, no replace refs, and the repo-local settings that
 * execute programs (fsmonitor, hooks) overridden. `-c` outranks the
 * repository's own config. */
export const ISOLATED_GIT_FLAGS: readonly string[] = ['-c', 'core.fsmonitor=false', '-c', 'core.hooksPath=/dev/null', '-c', 'protocol.file.allow=never', '--no-optional-locks', '--no-replace-objects'];

/** The environment is built from an allowlist, never copied from the caller:
 * an ambient `GIT_DIR`, `GIT_EXEC_PATH`, `GIT_OBJECT_DIRECTORY`, `GIT_ALTERNATE_OBJECT_DIRECTORIES`,
 * `GIT_CONFIG_*`, askpass or proxy variable cannot steer the call. */
export const ISOLATED_GIT_ENV_KEYS: readonly string[] = ['PATH', 'LANG', 'GIT_CONFIG_NOSYSTEM', 'GIT_CONFIG_GLOBAL', 'GIT_TERMINAL_PROMPT', 'GIT_NO_REPLACE_OBJECTS'];
export const isolatedGitEnv = (): NodeJS.ProcessEnv => ({
  PATH: process.env.PATH ?? '/usr/bin:/bin', LANG: process.env.LANG ?? 'C',
  GIT_CONFIG_NOSYSTEM: '1', GIT_CONFIG_GLOBAL: '/dev/null', GIT_TERMINAL_PROMPT: '0', GIT_NO_REPLACE_OBJECTS: '1',
});

export function isolatedGit(repoRoot: string, args: readonly string[], input?: string): Buffer {
  return execFileSync('git', [...ISOLATED_GIT_FLAGS, '-C', repoRoot, ...args], { maxBuffer: 512_000_000, env: isolatedGitEnv(),
    ...(input === undefined ? {} : { input }), stdio: ['pipe', 'pipe', 'ignore'] });
}

/** For git calls that reach a remote or create a repository: the isolated allowlist plus a
 * scratch `HOME` (never the caller's) and the protocols the call may use. This drops the
 * caller's proxy and CA settings (`https_proxy`, `GIT_SSL_CAINFO`, ...): a fetch that needs
 * them fails closed rather than inheriting ambient network configuration. */
export const NETWORK_GIT_ENV_KEYS: readonly string[] = [...ISOLATED_GIT_ENV_KEYS, 'HOME', 'GIT_ALLOW_PROTOCOL'];
export const minimalGitEnv = (home: string, allowProtocol: string): NodeJS.ProcessEnv => ({ ...isolatedGitEnv(), HOME: home, GIT_ALLOW_PROTOCOL: allowProtocol });
