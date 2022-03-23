local fs = require('diagnosticls-configs.fs')

return {
  sourceName = 'rustfmt',
  command = fs.executable('rustfmt'),
  args = { '%file' },
  isStdout = false,
  doesWriteToFile = true,
}
