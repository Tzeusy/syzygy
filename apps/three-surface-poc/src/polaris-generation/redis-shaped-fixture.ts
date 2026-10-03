import { execFileSync } from 'node:child_process';
import { mkdirSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';

/**
 * A SYNTHETIC repository shaped like a large C key-value server, built only
 * from public, general knowledge of how such a project is laid out: an
 * `src/` of C files and headers, vendored `deps/`, Tcl `tests/`, `modules/`,
 * `utils/`, a sample config, a README, a licence and release notes, and a few
 * files over 100,000 characters. No file here was read from, copied from or
 * derived from any real repository's contents; every body is generated filler
 * naming its own path. It exists to measure discovery on a tree of that shape
 * without reading a real one.
 */

/** Core-mechanism file stems, by role; the fixture's `src/` holds a `.c` and a `.h` for most. */
export const CORE_FILES = {
  eventLoop: ['src/ae.c', 'src/ae_epoll.c', 'src/ae_kqueue.c', 'src/networking.c', 'src/server.c'],
  persistence: ['src/aof.c', 'src/rdb.c', 'src/rio.c'],
  replication: ['src/replication.c', 'src/cluster.c', 'src/cluster_legacy.c', 'src/sentinel.c'],
  dataTypes: ['src/t_string.c', 'src/t_list.c', 'src/t_hash.c', 'src/t_set.c', 'src/t_zset.c', 'src/t_stream.c'],
} as const;

const SRC_STEMS = ['server', 'networking', 'ae', 'ae_epoll', 'ae_kqueue', 'ae_select', 'ae_evport', 'aof', 'rdb', 'rio', 'replication', 'cluster', 'cluster_legacy', 'sentinel',
  'module', 'db', 'object', 'dict', 'sds', 'adlist', 'intset', 'listpack', 'quicklist', 'ziplist', 'rax', 'config', 'eval', 'script_lua', 'multi', 'pubsub', 'expire', 'evict',
  'lazyfree', 'bio', 'latency', 'slowlog', 'acl', 'tls', 'geo', 'geohash', 'hyperloglog', 'bitops', 'sort', 'debug', 'util', 'zmalloc', 'crc16', 'crc64', 'lzf_c', 'lzf_d',
  'redis-cli', 'redis-benchmark', 'redis-check-aof', 'redis-check-rdb', 'sha1', 'sha256', 'endianconv', 'syncio', 'release', 'setproctitle', 'blocked', 'call_reply', 'childinfo',
  'defrag', 'functions', 'function_lua', 'kvstore', 'lolwut', 'lolwut5', 'lolwut6', 'monotonic', 'notify', 'resp_parser', 'rand', 'siphash', 'slowlog', 'socket', 'timeout',
  'tracking', 'unix', 'localtime', 'mt19937', 'memtest', 'redisassert', 'threads_mngr', 'ebuckets', 'estore', 'fmtargs', 'fwtree', 'hotkeys', 'iothread', 'lrulfu', 'mstr',
  'commands', 'connection', 'debugmacro', 'pqsort', 'stream_commands', 'valgrind', 'zipmap', 'cli_common', 'cli_commands', 'asciilogo'];

/** t_* data-type files and the filler that brings the C count to about 150. */
const SRC_C = [...SRC_STEMS, 't_string', 't_list', 't_hash', 't_set', 't_zset', 't_stream', 't_vset'];
const SRC_FILLER = Array.from({ length: Math.max(0, 150 - new Set(SRC_C).size) }, (_, i) => `aux_${String(i).padStart(3, '0')}`);

const JEMALLOC = ['jemalloc', 'arena', 'background_thread', 'base', 'bin', 'bitmap', 'buf_writer', 'cache_bin', 'ckh', 'counter', 'ctl', 'decay', 'div', 'ecache', 'edata',
  'edata_cache', 'ehooks', 'emap', 'eset', 'exp_grow', 'extent', 'extent_dss', 'extent_mmap', 'fxp', 'hook', 'hpa', 'hpa_hooks', 'hpdata', 'inspect', 'large', 'log', 'malloc_io',
  'mutex', 'nstime', 'pa', 'pac', 'pages', 'peak_event', 'prof', 'prof_data', 'prof_log', 'prof_recent', 'prof_sys', 'psset', 'rtree', 'safety_check', 'san', 'san_bump', 'sc',
  'sec', 'stats', 'sz', 'tcache', 'test_hooks', 'thread_event', 'ticker', 'tsd', 'witness'];
const LUA = ['lapi', 'lauxlib', 'lbaselib', 'lcode', 'ldblib', 'ldebug', 'ldo', 'ldump', 'lfunc', 'lgc', 'linit', 'liolib', 'llex', 'lmathlib', 'lmem', 'loadlib', 'lobject',
  'lopcodes', 'loslib', 'lparser', 'lstate', 'lstring', 'lstrlib', 'ltable', 'ltablib', 'ltm', 'lundump', 'lvm', 'lzio', 'lua_cjson', 'lua_cmsgpack', 'lua_struct', 'lua_bit',
  'strbuf', 'fpconv'];
const HIREDIS = ['alloc', 'async', 'dict', 'hiredis', 'net', 'read', 'sds', 'sockcompat', 'ssl'];

const tclTests = (dir: string, names: readonly string[]): [string, string][] => names.map(name => [`tests/${dir}/${name}.tcl`, `# synthetic Tcl test ${dir}/${name}\n`]);

/**
 * A permissive-licence header of the usual shape (a copyright line and the standard three-clause
 * wording, written from general knowledge of how such headers read), about 1,600 characters, so
 * the old 1,500-character excerpt of a C file is nothing but this block. The holder is a placeholder.
 */
function licenceHeader(path: string): string {
  return `/*
 * Copyright (c) 2009-2024, Example Author <author at example.invalid>
 * All rights reserved.
 *
 * SYNTHETIC FIXTURE FILE ${path}: generated filler, not the contents of any real repository.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 *   * Redistributions of source code must retain the above copyright notice,
 *     this list of conditions and the following disclaimer.
 *   * Redistributions in binary form must reproduce the above copyright
 *     notice, this list of conditions and the following disclaimer in the
 *     documentation and/or other materials provided with the distribution.
 *   * Neither the name of the copyright holder nor the names of its
 *     contributors may be used to endorse or promote products derived from
 *     this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE.
 */
`;
}

/** C-family filler with the layout such files have: licence block, an overview comment, includes, defines, a struct, then functions (prototypes in a header). */
function cBody(path: string, chars: number): string {
  const ident = path.replace(/[^A-Za-z0-9]/gu, '_');
  const header = path.endsWith('.h');
  const lines: string[] = [licenceHeader(path),
    `/* ${path}: synthetic overview. This unit owns the ${ident} state machine: it accepts work from the event loop, applies it to the keyspace and reports the outcome to the caller. */\n`,
    '#include "server.h"\n', `#define ${ident.toUpperCase()}_MAX 1024\n`, `#define ${ident.toUpperCase()}_FLAG(x) ((x) & 0x1)\n`,
    `struct ${ident}_state {\n    int phase;\n    long pending;\n};\n`, `typedef struct ${ident}_item {\n    int id;\n} ${ident}_item;\n`];
  let size = lines.reduce((total, line) => total + line.length, 0);
  for (let i = 0; size < chars; i++) {
    const line = header
      ? `int ${ident}_op_${i}(struct ${ident}_state *s, int arg);\n`
      : `int ${ident}_op_${i}(struct ${ident}_state *s, int arg) {\n    s->pending += arg + ${i};\n    return (int)s->pending; /* ${path} stub ${i} */\n}\n\n`;
    lines.push(line);
    size += line.length;
  }
  return lines.join('');
}

/** About `chars` characters of generated, path-naming filler: a header comment and numbered stubs. */
function body(path: string, chars: number): string {
  if (/\.[ch]$/u.test(path)) return cBody(path, chars);
  const ident = path.replace(/[^A-Za-z0-9]/gu, '_');
  const head = `/* SYNTHETIC FIXTURE FILE ${path}: generated filler, not the contents of any real repository. */\n`;
  const lines: string[] = [head];
  let size = head.length;
  for (let i = 0; size < chars; i++) {
    const line = `static int ${ident}_step_${i}(int arg) { return arg + ${i}; } /* ${path} stub ${i} */\n`;
    lines.push(line);
    size += line.length;
  }
  return lines.join('');
}

export interface RedisShapedFixture {
  /** Every file written, relative path to character count. */
  readonly files: ReadonlyMap<string, number>;
  readonly commit: string;
  /** Paths whose body exceeds 100,000 characters. */
  readonly oversize: readonly string[];
}

export function redisShapedFiles(): Map<string, string> {
  const files = new Map<string, string>();
  const put = (path: string, chars: number): void => { files.set(path, body(path, chars)); };
  files.set('README.md', '# Synthetic key-value server fixture\n\nThis repository is SYNTHETIC. It was generated by the Syzygy test suite from public, general knowledge of how a large C key-value server is laid out, to measure source discovery on a tree of that shape without reading any real repository. No file contains the contents of any real project.\n');
  files.set('LICENSE.txt', 'SYNTHETIC LICENCE PLACEHOLDER. This fixture carries no real licence text.\n'.repeat(8));
  put('00-RELEASENOTES', 110_000);
  put('redis.conf', 60_000);
  put('Makefile', 3_000);
  put('src/Makefile', 6_000);
  const bigSrc = new Set(['src/server.c', 'src/redis-cli.c', 'src/cluster_legacy.c']);
  for (const stem of new Set([...SRC_C, ...SRC_FILLER])) {
    const path = `src/${stem}.c`;
    put(path, bigSrc.has(path) ? 130_000 : stem.startsWith('aux_') ? 2_500 : 8_000 + (stem.length * 397) % 14_000);
  }
  for (const stem of [...new Set([...SRC_C, ...SRC_FILLER])].slice(0, 70)) put(`src/${stem}.h`, 1_500 + (stem.length * 211) % 5_000);
  for (const stem of JEMALLOC) { put(`deps/jemalloc/src/${stem}.c`, stem === 'jemalloc' ? 160_000 : 4_000 + (stem.length * 331) % 12_000); }
  for (const stem of JEMALLOC.slice(0, 40)) put(`deps/jemalloc/include/jemalloc/internal/${stem}.h`, 1_500);
  for (const stem of LUA) { put(`deps/lua/src/${stem}.c`, 5_000 + (stem.length * 457) % 20_000); put(`deps/lua/src/${stem}.h`, 1_200); }
  for (const stem of HIREDIS) { put(`deps/hiredis/${stem}.c`, 6_000); put(`deps/hiredis/${stem}.h`, 2_000); }
  put('deps/linenoise/linenoise.c', 40_000); put('deps/linenoise/linenoise.h', 2_000);
  for (const stem of ['hdr_histogram', 'hdr_atomic', 'hdr_alloc', 'hdr_endian', 'hdr_tests']) { put(`deps/hdr_histogram/${stem}.c`, 8_000); put(`deps/hdr_histogram/${stem}.h`, 2_000); }
  put('deps/README.md', 2_500);
  for (const [path] of tclTests('unit', Array.from({ length: 40 }, (_, i) => ['expire', 'dump', 'scan', 'type_list', 'type_hash', 'type_set', 'type_zset', 'type_stream', 'latency', 'acl'][i % 10]! + (i >= 10 ? `_${Math.floor(i / 10)}` : '')))) put(path, 9_000);
  for (const [path] of tclTests('integration', Array.from({ length: 30 }, (_, i) => ['replication', 'aof', 'rdb', 'psync2', 'block_cmds', 'convert', 'logging'][i % 7]! + (i >= 7 ? `_${Math.floor(i / 7)}` : '')))) put(path, 9_000);
  put('tests/test_helper.tcl', 14_000);
  put('tests/helpers/bg_complex_data.tcl', 2_000);
  put('tests/support/util.tcl', 20_000);
  for (const stem of ['hello', 'helloworld', 'hellotype', 'hellocluster']) put(`modules/${stem}.c`, 5_000);
  put('modules/Makefile', 1_000);
  for (const stem of ['redis-copy', 'speed-regression', 'gen-test-certs', 'lru-test', 'systemd-redis_server.service', 'install_server']) put(`utils/${stem}.sh`, 2_000);
  put('utils/hashtable/rehashing.c', 3_000);
  return files;
}

/** Writes the fixture as one commit in `dir` (created) and returns what it holds. */
export function buildRedisShapedFixture(dir: string): RedisShapedFixture {
  const git = (...args: string[]): string => execFileSync('git', ['-C', dir, ...args], { encoding: 'utf8' }).trim();
  mkdirSync(dir, { recursive: true });
  git('init', '-q'); git('config', 'user.email', 'f@example.invalid'); git('config', 'user.name', 'F');
  const files = redisShapedFiles();
  for (const [path, text] of files) { mkdirSync(dirname(join(dir, path)), { recursive: true }); writeFileSync(join(dir, path), text); }
  git('add', '-A'); git('commit', '-qm', 'synthetic fixture');
  return { files: new Map([...files].map(([path, text]) => [path, text.length])), commit: git('rev-parse', 'HEAD'), oversize: [...files].filter(([, text]) => text.length > 100_000).map(([path]) => path).sort() };
}
