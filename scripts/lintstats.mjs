#!/usr/bin/env node
// @ts-check
// WIP
import * as readline from "node:readline";

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});

let warnings = 0;
let errors = 0;

rl.on("line", (line) => {
  if (line.includes("  Error:")) errors++;
  if (line.includes("  Warning:")) warnings++;
});

rl.on("close", () => {
  console.log(`Errors: ${errors}\nWarnings: ${warnings}`);
});
