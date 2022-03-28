const { readFileSync, writeSync } = require("fs");
const res = readFileSync(0)
  .toString()
  .trim()
  .replace(/(.*) \#(\d+)$/, "$2 $1")
  .replace(/[^a-zA-Z0-9]+/g, "-")
  .toLowerCase();
writeSync(1, res);
