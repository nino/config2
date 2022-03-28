"use strict";

const fs = require("fs");
const { promisify } = require("util");
const appendFile = promisify(fs.appendFile);

module.exports = msg =>
  appendFile("/Users/nino/log.log", `${new Date().toString()}: ${msg}\n`);
