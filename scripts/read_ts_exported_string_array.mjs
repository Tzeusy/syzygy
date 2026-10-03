#!/usr/bin/env node
// Read one exported string-array constant from a TypeScript file through the
// compiler API. Usage: read_ts_exported_string_array.mjs <file> <symbol>
// Prints the members as a JSON array, or exits 1 with a reason on stderr.
// Fail closed: the file must parse without syntax errors, the symbol must be
// bound by exactly one top-level statement, that statement must be
// `export const SYMBOL = [ 'a', 'b' ] as const;` (string literals only), and
// no other export may mention the symbol. Nothing is executed.
import { readFileSync } from 'node:fs';
import ts from 'typescript';

const [file, symbol] = process.argv.slice(2);
const refuse = (why) => { process.stderr.write(`${why}\n`); process.exit(1); };
if (!file || !symbol) refuse('usage: <file> <symbol>');

const sf = ts.createSourceFile(file, readFileSync(file, 'utf8'), ts.ScriptTarget.Latest, true, ts.ScriptKind.TS);
if (sf.parseDiagnostics.length > 0) refuse(`${file} has syntax errors`);

const exported = (node) => (ts.getModifiers(node) ?? []).some(m => m.kind === ts.SyntaxKind.ExportKeyword);
const bindings = [];   // every top-level statement that binds or exports the symbol
for (const st of sf.statements) {
  if (ts.isVariableStatement(st)) {
    for (const d of st.declarationList.declarations) {
      if (ts.isIdentifier(d.name) && d.name.text === symbol) bindings.push({ st, d });
      else if (!ts.isIdentifier(d.name) && d.name.getText(sf).includes(symbol)) bindings.push({ st, d: null });
    }
  } else if (ts.isFunctionDeclaration(st) || ts.isClassDeclaration(st) || ts.isEnumDeclaration(st)
             || ts.isTypeAliasDeclaration(st) || ts.isInterfaceDeclaration(st) || ts.isModuleDeclaration(st)) {
    if (st.name && st.name.text === symbol) bindings.push({ st, d: null });
  } else if (ts.isExportDeclaration(st) || ts.isImportDeclaration(st) || ts.isImportEqualsDeclaration(st)) {
    if (st.getText(sf).includes(symbol)) bindings.push({ st, d: null });
  } else if (ts.isExportAssignment(st) && st.getText(sf).includes(symbol)) {
    bindings.push({ st, d: null });
  }
}
if (bindings.length === 0) refuse(`${symbol} is not declared at the top level of ${file}`);
if (bindings.length > 1) refuse(`${symbol} is bound or exported by more than one top-level statement in ${file}`);
const { st, d } = bindings[0];
if (!d || !ts.isVariableStatement(st)) refuse(`${symbol} is not bound by a variable statement`);
if (!exported(st)) refuse(`${symbol} is not exported from ${file}`);
if (!(st.declarationList.flags & ts.NodeFlags.Const)) refuse(`${symbol} is not declared with const`);
if (st.declarationList.declarations.length !== 1) refuse(`${symbol} shares its statement with another declaration`);
if (d.type) refuse(`${symbol} carries a type annotation; the literal must stand alone`);
const init = d.initializer;
if (!init || !ts.isAsExpression(init) || !ts.isTypeReferenceNode(init.type)
    || init.type.typeName.getText(sf) !== 'const') refuse(`${symbol} is not initialised by a literal array \`as const\``);
if (!ts.isArrayLiteralExpression(init.expression)) refuse(`${symbol} is not initialised by an array literal`);
const members = [];
for (const el of init.expression.elements) {
  if (!ts.isStringLiteral(el)) refuse(`${symbol} holds a member that is not a string literal`);
  members.push(el.text);
}
process.stdout.write(`${JSON.stringify(members)}\n`);
